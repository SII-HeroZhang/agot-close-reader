#!/usr/bin/env python3
"""Read-only completion audit for all AGOT chapter readers."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "AGOT_逐章精读"
MAPS = OUT / "source_maps"

CHAPTER_FILE = re.compile(r"Chapter_(\d+)_([A-Z]+)_精读\.md$")
MAP_FILE = re.compile(r"Chapter_(\d+)_source_map\.json$")
CHINESE_PERSONAL_NAMES = [
    "提利昂", "泰温", "詹姆", "瑟曦", "乔佛里", "凯特琳", "琼恩", "珊莎",
    "艾莉亚", "布兰", "罗柏", "丹妮莉丝", "韦赛里斯", "乔拉", "卓戈",
    "山姆威尔", "奈德", "艾德·", "小指头",
]
REQUIRED_BLOCK_LABELS = [
    "**英文原段**",
    "**难词与短语**",
    "**这一段说了什么**",
    "**值得注意的地方**",
    "**背景与伏笔（无剧透）**",
]
VERIFIED_NAVIGATION_ONLY_PAGES = {24, 30, 66, 96, 122, 179, 212, 520, 562}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> None:
    errors: list[str] = []
    chapter_files: dict[int, Path] = {}
    map_files: dict[int, Path] = {}

    for path in OUT.glob("Chapter_*_精读.md"):
        match = CHAPTER_FILE.fullmatch(path.name)
        if not match:
            fail(errors, f"Unexpected chapter filename: {path.name}")
            continue
        chapter_files[int(match.group(1))] = path
    for path in MAPS.glob("Chapter_*_source_map.json"):
        match = MAP_FILE.fullmatch(path.name)
        if not match:
            fail(errors, f"Unexpected source-map filename: {path.name}")
            continue
        map_files[int(match.group(1))] = path

    expected = set(range(1, 73))
    if set(chapter_files) != expected:
        fail(errors, f"Markdown chapter set differs: {sorted(expected - set(chapter_files))=}, {sorted(set(chapter_files) - expected)=}")
    if set(map_files) != expected:
        fail(errors, f"Source-map chapter set differs: {sorted(expected - set(map_files))=}, {sorted(set(map_files) - expected)=}")

    readme = (OUT / "README.md").read_text()
    if "待生成" in readme or "待复核" in readme:
        fail(errors, "README still contains a pending status")

    total_blocks = 0
    total_redactions = 0
    page_ranges: list[tuple[int, int, int]] = []
    for chapter in sorted(expected & set(chapter_files) & set(map_files)):
        md_path = chapter_files[chapter]
        text = md_path.read_text()
        source_map = json.loads(map_files[chapter].read_text())
        blocks = source_map.get("blocks", [])
        count = source_map.get("block_count", len(blocks))
        total_blocks += len(blocks)
        total_redactions += text.count("[Content omitted:")

        if count != len(blocks):
            fail(errors, f"Ch{chapter}: block_count {count} != {len(blocks)}")
        if not blocks:
            fail(errors, f"Ch{chapter}: no source-map blocks")
            continue
        page_range = source_map.get("page_range") or source_map.get("paper", {}).get("pdf_page_range")
        page_start, page_end = page_range or [None, None]
        page_ranges.append((chapter, page_start, page_end))
        trailing_metadata_pages = set(range(blocks[-1]["end_page"] + 1, page_end + 1))
        if blocks[0]["page"] != page_start or not trailing_metadata_pages.issubset(VERIFIED_NAVIGATION_ONLY_PAGES):
            fail(errors, f"Ch{chapter}: page range does not match first/last block")

        ids = [block.get("id") for block in blocks]
        if len(ids) != len(set(ids)):
            fail(errors, f"Ch{chapter}: duplicate source-map IDs")
        if [block.get("order") for block in blocks] != list(range(1, len(blocks) + 1)):
            fail(errors, f"Ch{chapter}: non-contiguous block order")
        id_pattern = re.compile(rf"CH{chapter:02d}-P\d{{3}}-\d{{3}}$")
        if any(not isinstance(block_id, str) or not id_pattern.fullmatch(block_id) for block_id in ids):
            fail(errors, f"Ch{chapter}: malformed stable ID")
        for block in blocks:
            expected_id = f"CH{chapter:02d}-P{block['page']:03d}-{block['order']:03d}"
            if block.get("id") != expected_id:
                fail(errors, f"Ch{chapter}: ID does not encode page/order: {block.get('id')} != {expected_id}")

        headings = re.findall(rf"^### (CH{chapter:02d}-P\d{{3}}-\d{{3}})$", text, re.M)
        anchors = re.findall(r'<a id="(ch\d{2}-p\d{3}-\d{3})"></a>', text)
        if headings != ids:
            fail(errors, f"Ch{chapter}: Markdown headings differ from source-map order")
        if anchors != [block_id.lower() for block_id in ids]:
            fail(errors, f"Ch{chapter}: anchors differ from source-map order")
        directory_targets = re.findall(r"\(#(ch\d{2}-p\d{3}-\d{3})\)", text)
        if not directory_targets or any(target not in set(anchors) for target in directory_targets):
            fail(errors, f"Ch{chapter}: paragraph-directory target missing or invalid")
        for label in REQUIRED_BLOCK_LABELS:
            if text.count(label) != len(blocks):
                fail(errors, f"Ch{chapter}: {label} count {text.count(label)} != {len(blocks)}")

        for block in blocks:
            equivalent_fields = {
                "original_text": ("original_text",),
                "explanation": ("explanation_zh", "paragraph_explanation_zh"),
                "literary_note": ("literary_note_zh", "reading_note_zh"),
                "background": ("background_zh", "background_note_zh"),
            }
            for semantic_name, keys in equivalent_fields.items():
                value = next((block.get(key) for key in keys if isinstance(block.get(key), str)), "")
                if not value.strip():
                    fail(errors, f"Ch{chapter} {block.get('id')}: missing {semantic_name}")
            if block.get("translation") != "":
                fail(errors, f"Ch{chapter} {block.get('id')}: translation should remain blank")
        reader_mode = source_map.get("paper", {}).get("reader_mode", "")
        name_policy_ok = (
            source_map.get("name_policy") == "Personal names remain in original English."
            or "English personal names" in reader_mode
        )
        spoiler_policy_ok = (
            "current paragraph" in source_map.get("spoiler_policy", "")
            or "spoiler-free" in reader_mode
        )
        if not name_policy_ok:
            fail(errors, f"Ch{chapter}: wrong or missing name policy")
        if not spoiler_policy_ok:
            fail(errors, f"Ch{chapter}: spoiler policy missing")
        if any(name in text for name in CHINESE_PERSONAL_NAMES):
            present = [name for name in CHINESE_PERSONAL_NAMES if name in text]
            fail(errors, f"Ch{chapter}: Chinese personal-name forms found: {present}")
        expected_link = f"({md_path.name})"
        if expected_link not in readme:
            fail(errors, f"Ch{chapter}: README link missing")
        row_match = re.search(
            rf"^\| Chapter {chapter} \| [^|]+ \| ([0-9]+)–([0-9]+) \| ([0-9]+) \|",
            readme,
            re.M,
        )
        if not row_match:
            fail(errors, f"Ch{chapter}: README row missing or malformed")
        elif tuple(map(int, row_match.groups())) != (page_start, page_end, len(blocks)):
            fail(errors, f"Ch{chapter}: README page/count metadata differs from source map")

    discontinuities = []
    for left, right in zip(page_ranges, page_ranges[1:]):
        gap_pages = set(range(left[2] + 1, right[1]))
        if not gap_pages.issubset(VERIFIED_NAVIGATION_ONLY_PAGES):
            discontinuities.append((left[0], left[2], right[0], right[1], sorted(gap_pages)))
    if discontinuities:
        fail(errors, f"Unexpected body-page discontinuities: {discontinuities}")

    note_count = len(list((OUT / "notes").glob("Chapter_*_notes.md")))
    if note_count != 72:
        fail(errors, f"Expected 72 note files, found {note_count}")

    result = {
        "status": "PASS" if not errors else "FAIL",
        "chapters": len(chapter_files),
        "source_maps": len(map_files),
        "notes": note_count,
        "total_paragraphs": total_blocks,
        "total_redaction_placeholders": total_redactions,
        "page_span": [page_ranges[0][1], page_ranges[-1][2]] if page_ranges else None,
        "verified_navigation_only_pages": sorted(VERIFIED_NAVIGATION_ONLY_PAGES),
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
