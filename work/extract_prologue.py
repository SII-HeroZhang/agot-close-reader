#!/usr/bin/env python3
"""Inspect and extract paragraph blocks from the AGOT prologue PDF pages."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path


PDF = Path("/Users/herozhang/Downloads/A Game Of Thrones.pdf")


def clean_page(raw: str, page: int) -> str:
    lines = raw.replace("\r", "").splitlines()
    kept: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            kept.append("")
            continue
        if stripped == "previous | Table of Contents | next":
            continue
        if page == 6 and stripped == "PROLOGUE":
            continue
        kept.append(stripped)
    return "\n".join(kept).strip()


def extract() -> list[dict[str, object]]:
    proc = subprocess.run(
        ["pdftotext", "-f", "6", "-l", "15", "-layout", str(PDF), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    pages = proc.stdout.split("\f")[:10]
    provisional: list[dict[str, object]] = []
    for page, raw in enumerate(pages, start=6):
        text = clean_page(raw, page)
        for idx, block in enumerate(re.split(r"\n\s*\n+", text)):
            # In this chapter, the only explicit end-of-line hyphen is the
            # semantic compound "half-bored", so preserve it.
            joined = re.sub(r"(?<=\w)-\n(?=\w)", "-", block)
            joined = re.sub(r"\s*\n\s*", " ", joined)
            joined = re.sub(r"\s+", " ", joined).strip()
            if joined:
                provisional.append({"page": page, "page_block": idx + 1, "text": joined})

    # A paragraph that reaches a page edge is split by the PDF page boundary.
    merged: list[dict[str, object]] = []
    for block in provisional:
        if merged and block["page"] != merged[-1]["end_page"]:
            previous_text = str(merged[-1]["text"])
            current_text = str(block["text"])
            if previous_text and previous_text[-1] not in '.!?\"”' and current_text[:1].islower():
                merged[-1]["text"] = previous_text + " " + current_text
                merged[-1]["end_page"] = block["page"]
                continue
        merged.append(
            {
                "page": block["page"],
                "end_page": block["page"],
                "text": block["text"],
            }
        )

    # Page 8 opens in the middle of the Will/poaching paragraph even though
    # the previous page happens to end at a sentence boundary.
    for idx, block in enumerate(merged):
        if block["page"] == 8 and str(block["text"]).startswith("Mallister freeriders"):
            merged[idx - 1]["text"] = str(merged[idx - 1]["text"]) + " " + str(block["text"])
            merged[idx - 1]["end_page"] = 8
            del merged[idx]
            break

    for order, block in enumerate(merged, start=1):
        block["id"] = f"PRO-P{int(block['page']):03d}-{order:03d}"
        block["order"] = order
    return merged


if __name__ == "__main__":
    print(json.dumps(extract(), ensure_ascii=False, indent=2))
