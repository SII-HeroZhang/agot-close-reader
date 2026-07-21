#!/usr/bin/env python3
"""Fail the build when content, anchors, or GitHub Pages links drift."""
from __future__ import annotations

import json
import os
import struct
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup


SITE = Path(__file__).resolve().parent
DIST = SITE / "dist"
BASE = os.environ.get("BASE_PATH", "/agot-close-reader").rstrip("/")
EXPECTED_SECTIONS = 73
EXPECTED_PARAGRAPHS = 6763


def fail(message: str) -> None:
    raise AssertionError(message)


def output_for_url(path: str) -> Path:
    if BASE and not (path == BASE or path.startswith(f"{BASE}/")):
        fail(f"Internal URL escaped base path: {path}")
    relative = path[len(BASE):].lstrip("/") if BASE else path.lstrip("/")
    target = DIST / unquote(relative)
    return target / "index.html" if not relative or path.endswith("/") else target


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        fail(f"Invalid PNG: {path}")
    return struct.unpack(">II", data[16:24])


def main() -> None:
    manifest = json.loads((DIST / "data/manifest.json").read_text(encoding="utf-8"))
    search = json.loads((DIST / "data/search-index.json").read_text(encoding="utf-8"))
    page_map = json.loads((DIST / "data/page-map.json").read_text(encoding="utf-8"))
    if len(manifest) != EXPECTED_SECTIONS:
        fail(f"Expected {EXPECTED_SECTIONS} sections, found {len(manifest)}")
    if len(search) != EXPECTED_PARAGRAPHS:
        fail(f"Expected {EXPECTED_PARAGRAPHS} search rows, found {len(search)}")
    if sum(int(chapter["count"]) for chapter in manifest) != EXPECTED_PARAGRAPHS:
        fail("Manifest paragraph total does not equal 6,763")

    expected_routes = [DIST / "index.html", DIST / "library/index.html", DIST / "pdf/index.html"]
    expected_routes += [DIST / f"chapters/{chapter['id']}/index.html" for chapter in manifest]
    missing = [str(path) for path in expected_routes if not path.is_file()]
    if missing:
        fail(f"Missing routes: {missing[:5]}")
    if len(list(DIST.rglob("index.html"))) != EXPECTED_SECTIONS + 3:
        fail("Unexpected number of generated HTML routes")

    all_anchors: list[str] = []
    ids_by_file: dict[Path, set[str]] = {}
    for chapter in manifest:
        page = DIST / f"chapters/{chapter['id']}/index.html"
        soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
        cards = soup.select("article.reader-content > section.paragraph-card[data-anchor]")
        if len(cards) != chapter["count"]:
            fail(f"{chapter['label']}: expected {chapter['count']} cards, found {len(cards)}")
        local_anchors = [card["data-anchor"] for card in cards]
        if len(local_anchors) != len(set(local_anchors)):
            fail(f"{chapter['label']}: duplicate paragraph anchor")
        for card, anchor in zip(cards, local_anchors):
            if not card.find(id=anchor):
                fail(f"{chapter['label']}: card lacks its target id {anchor}")
            if not card.find("h3") or not card.select_one(".paragraph-tools"):
                fail(f"{chapter['label']}: incomplete paragraph UI at {anchor}")
            if card.parent and card.parent.name == "p":
                fail(f"{chapter['label']}: invalid section nested inside paragraph at {anchor}")
            pdf_button = card.select_one(".js-open-pdf[data-pdf-page]")
            if not pdf_button or pdf_button.get("data-anchor") != anchor:
                fail(f"{chapter['label']}: missing PDF companion control at {anchor}")
        toc_targets = [link.get("href", "").removeprefix("#") for link in soup.select(".local-toc a[href^='#']")]
        if toc_targets != local_anchors:
            fail(f"{chapter['label']}: paragraph TOC order does not match source")
        all_anchors.extend(local_anchors)

    if len(all_anchors) != EXPECTED_PARAGRAPHS or len(set(all_anchors)) != EXPECTED_PARAGRAPHS:
        fail("Paragraph anchors are not globally unique")
    search_anchors = [row["anchorId"] for row in search]
    if search_anchors != all_anchors:
        fail("Search index order/anchors do not match rendered chapters")
    mapped_anchors = {row["anchorId"] for rows in page_map.values() for row in rows}
    if mapped_anchors != set(all_anchors):
        fail("PDF page map does not cover every paragraph anchor")
    if any(not (1 <= int(page) <= 755) for page in page_map):
        fail("PDF page map contains an invalid page number")

    html_files = list(DIST.rglob("*.html"))
    for page in html_files:
        soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
        ids_by_file[page] = {tag["id"] for tag in soup.select("[id]")}
    checked_links = 0
    for page in html_files:
        soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
        for tag in soup.select("[href]"):
            href = tag.get("href", "")
            if not href or href.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            parts = urlsplit(href)
            target = page if not parts.path else output_for_url(parts.path)
            if not target.exists():
                fail(f"Broken link in {page.relative_to(DIST)}: {href}")
            if parts.fragment and target.suffix == ".html":
                if parts.fragment not in ids_by_file.get(target, set()):
                    fail(f"Missing fragment in {page.relative_to(DIST)}: {href}")
            checked_links += 1

    indexed_text = " ".join(
        f"{row['original']} {row['summary']} {row['note']} {row['background']} {row['vocab']}" for row in search
    ).casefold()
    for probe in ("direwolf", "守夜人", "riverrun"):
        if probe.casefold() not in indexed_text:
            fail(f"Search coverage probe missing: {probe}")

    for required in ("assets/site.css", "assets/site.js", "assets/pdf-reader.js", "assets/search-worker.js", "assets/og.png", "assets/agot-original.pdf", "data/page-map.json", "robots.txt", "sitemap.xml", ".nojekyll"):
        if not (DIST / required).exists():
            fail(f"Missing required artifact: {required}")
    pdf_path = DIST / "assets/agot-original.pdf"
    if pdf_path.stat().st_size != 4_921_287 or pdf_path.read_bytes()[:5] != b"%PDF-":
        fail("Hosted PDF is missing, damaged, or not the expected 755-page source file")
    width, height = png_size(DIST / "assets/og.png")
    if width < 1200 or height < 630:
        fail(f"OG image is too small: {width}x{height}")

    print(json.dumps({
        "status": "PASS",
        "routes": len(expected_routes),
        "sections": len(manifest),
        "paragraphs": len(all_anchors),
        "uniqueAnchors": len(set(all_anchors)),
        "checkedLinks": checked_links,
        "searchRows": len(search),
        "pdfMappedPages": len(page_map),
        "pdfMappedAnchors": len(mapped_anchors),
        "hostedPdfBytes": pdf_path.stat().st_size,
        "ogImage": f"{width}x{height}",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
