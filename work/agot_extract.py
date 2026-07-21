#!/usr/bin/env python3
"""Shared selectable-text extraction for chapter-sized AGOT PDF ranges."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


PDF = Path("/Users/herozhang/Downloads/A Game Of Thrones.pdf")


def extract_range(start_page: int, end_page: int, heading: str, prefix: str) -> list[dict[str, object]]:
    proc = subprocess.run(
        ["pdftotext", "-f", str(start_page), "-l", str(end_page), "-layout", str(PDF), "-"],
        check=True, capture_output=True, text=True,
    )
    provisional: list[dict[str, object]] = []
    page_count = end_page - start_page + 1
    for page, raw in enumerate(proc.stdout.split("\f")[:page_count], start=start_page):
        lines = []
        for line in raw.replace("\r", "").splitlines():
            stripped = line.strip()
            if stripped == "previous | Table of Contents | next":
                continue
            if page == start_page and stripped == heading:
                continue
            lines.append(stripped)
        for block in re.split(r"\n\s*\n+", "\n".join(lines).strip()):
            text = re.sub(r"(?<=\w)-\n(?=\w)", "-", block)
            text = re.sub(r"\s*\n\s*", " ", text)
            text = re.sub(r"\s+", " ", text).strip()
            if text:
                provisional.append({"page": page, "text": text})

    merged: list[dict[str, object]] = []
    for block in provisional:
        if merged and int(block["page"]) != int(merged[-1]["end_page"]):
            previous, current = str(merged[-1]["text"]), str(block["text"])
            if previous[-1] not in '.!?\"”' and current[:1].islower():
                merged[-1]["text"] = previous + " " + current
                merged[-1]["end_page"] = block["page"]
                continue
        merged.append({"page": block["page"], "end_page": block["page"], "text": block["text"]})

    for order, block in enumerate(merged, start=1):
        block["id"] = f"{prefix}-P{int(block['page']):03d}-{order:03d}"
        block["order"] = order
    return merged
