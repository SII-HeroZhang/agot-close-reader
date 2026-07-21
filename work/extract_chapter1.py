#!/usr/bin/env python3
"""Extract stable paragraph blocks for Chapter 1 (BRAN), PDF pages 16–23."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path


PDF = Path("/Users/herozhang/Downloads/A Game Of Thrones.pdf")


def extract() -> list[dict[str, object]]:
    proc = subprocess.run(
        ["pdftotext", "-f", "16", "-l", "23", "-layout", str(PDF), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    provisional: list[dict[str, object]] = []
    for page, raw in enumerate(proc.stdout.split("\f")[:8], start=16):
        lines: list[str] = []
        for line in raw.replace("\r", "").splitlines():
            stripped = line.strip()
            if stripped == "previous | Table of Contents | next":
                continue
            if page == 16 and stripped == "BRAN":
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
            previous = str(merged[-1]["text"])
            current = str(block["text"])
            if previous[-1] not in '.!?\"”' and current[:1].islower():
                merged[-1]["text"] = previous + " " + current
                merged[-1]["end_page"] = block["page"]
                continue
        merged.append({"page": block["page"], "end_page": block["page"], "text": block["text"]})

    for order, block in enumerate(merged, start=1):
        block["id"] = f"CH01-P{int(block['page']):03d}-{order:03d}"
        block["order"] = order
    return merged


if __name__ == "__main__":
    print(json.dumps(extract(), ensure_ascii=False, indent=2))
