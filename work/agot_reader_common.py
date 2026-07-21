#!/usr/bin/env python3
"""Shared renderer for paragraph-by-paragraph AGOT chapter readers."""

from __future__ import annotations

import json
from pathlib import Path

from agot_extract import PDF
from build_agot_prologue_reader import english_names, term_present


def vocab_for(text, vocab):
    seen, found = set(), []
    for item in vocab:
        term = item[0]
        if term not in seen and term_present(term, text):
            found.append(item)
            seen.add(term)
    return found


def source_label(block):
    if block["page"] == block["end_page"]:
        return f"PDF p.{block['page']}"
    return f"PDF pp.{block['page']}–{block['end_page']}"


def staged_note(order, key_notes, stages):
    if order in key_notes:
        return key_notes[order]
    return next(text for start, end, text in stages if start <= order <= end)


def render_markdown(*, chapter, pov, page_start, page_end, blocks, summaries,
                    key_notes, stages, backgrounds, default_background, vocab,
                    guide, people, terms, synthesis, contrasts, questions):
    pages = {}
    for block in blocks:
        pages.setdefault(block["page"], []).append(block["id"])

    lines = [
        f"# *A Game of Thrones* Chapter {chapter} — {pov} 逐段精读", "",
        "> **阅读模式：** 无剧透｜人物姓名保留英文｜英文原段 + 难词 + 段意 + 写法 + 当前可知背景  ",
        f"> **文本范围：** 原 PDF 第 {page_start}–{page_end} 页，共 {len(blocks)} 个正文段落", "",
        "## 本章导读", "", guide, "",
        "## 人物表", "", "| 人物 | 当前身份与作用 |", "|---|---|",
    ]
    lines.extend(f"| {name} | {description} |" for name, description in people)
    lines += ["", "## 地名与专名", "", "| 英文 | 中文解释 |", "|---|---|"]
    lines.extend(f"| {term} | {description} |" for term, description in terms)
    lines += ["", "## 段落目录", ""]
    for page, ids in pages.items():
        lines.append(f"- [PDF 第 {page} 页：{ids[0]}–{ids[-1]}](#{ids[0].lower()})")
    lines += ["", "---", "", "## 逐段精读", ""]

    for block, summary in zip(blocks, summaries, strict=True):
        order, bid, original = block["order"], block["id"], block["text"]
        note = staged_note(order, key_notes, stages)
        background = backgrounds.get(order, default_background)
        lines += [
            f'<a id="{bid.lower()}"></a>', f"### {bid}", "",
            f"**来源：** {source_label(block)}", "", "**英文原段**", "", f"> {original}", "",
            "**难词与短语**", "",
        ]
        found = vocab_for(original, vocab)
        if found:
            lines += ["| 词语 | 音标 | 词性 | 此处含义 | 用法提示 |", "|---|---|---|---|---|"]
            for term, ipa, pos, meaning, usage in found:
                lines.append(f"| `{term}` | {ipa} | {pos} | {meaning} | {english_names(usage)} |")
        else:
            lines.append("本段没有新增的四级以上重点词；重点留意语气和上下文。")
        lines += [
            "", "**这一段说了什么**", "", summary,
            "", "**值得注意的地方**", "", note,
            "", "**背景与伏笔（无剧透）**", "", background,
            "", "[回到段落目录](#段落目录)", "", "---", "",
        ]

    lines += ["## 本章整体梳理", "", synthesis, "", "### 关键对照与意象", ""]
    lines.extend(f"- {item}" for item in contrasts)
    lines += ["", "### 当前仍未解答的问题", ""]
    lines.extend(f"{i}. {question}" for i, question in enumerate(questions, 1))
    lines += ["", "以上问题不使用后文章节答案。", "", "## 词汇总表", "", "| 词语 | 音标 | 词性 | 核心释义 |", "|---|---|---|---|"]
    all_text = " ".join(block["text"] for block in blocks)
    seen = set()
    for term, ipa, pos, meaning, _ in vocab:
        if term not in seen and term_present(term, all_text):
            lines.append(f"| `{term}` | {ipa} | {pos} | {meaning} |")
            seen.add(term)
    return "\n".join(lines) + "\n"


def render_source_map(*, chapter, pov, page_start, page_end, blocks, summaries,
                      key_notes, stages, backgrounds, default_background):
    return {
        "work": "A Game of Thrones",
        "section": f"Chapter {chapter} — {pov}",
        "source_file": str(PDF),
        "source_format": "pdf-text",
        "page_range": [page_start, page_end],
        "block_count": len(blocks),
        "name_policy": "Personal names remain in original English.",
        "spoiler_policy": "Only information available through each current paragraph is used.",
        "pages": [
            {
                "page": page,
                "first_id": next(b["id"] for b in blocks if b["page"] == page),
                "last_id": [b["id"] for b in blocks if b["page"] == page][-1],
            }
            for page in sorted({b["page"] for b in blocks})
        ],
        "blocks": [
            {
                "id": b["id"], "page": b["page"], "end_page": b["end_page"],
                "type": "paragraph", "order": b["order"], "original_text": b["text"],
                "translation": "", "explanation_zh": summaries[b["order"] - 1],
                "literary_note_zh": staged_note(b["order"], key_notes, stages),
                "background_zh": backgrounds.get(b["order"], default_background),
                "bbox": [0, 0, 0, 0], "confidence": "high", "refs": [], "insert_after": None,
            }
            for b in blocks
        ],
    }


def write_chapter(*, out: Path, chapter, pov, page_start, page_end, blocks, summaries,
                  key_notes, stages, backgrounds, default_background, vocab, guide,
                  people, terms, synthesis, contrasts, questions, extraction_notes="无额外跨页修复"):
    assert len(blocks) == len(summaries)
    out.mkdir(parents=True, exist_ok=True)
    (out / "source_maps").mkdir(exist_ok=True)
    (out / "notes").mkdir(exist_ok=True)
    stem = f"Chapter_{chapter:02d}_{pov}"
    markdown = render_markdown(
        chapter=chapter, pov=pov, page_start=page_start, page_end=page_end,
        blocks=blocks, summaries=summaries, key_notes=key_notes, stages=stages,
        backgrounds=backgrounds, default_background=default_background, vocab=vocab,
        guide=guide, people=people, terms=terms, synthesis=synthesis,
        contrasts=contrasts, questions=questions,
    )
    source_map = render_source_map(
        chapter=chapter, pov=pov, page_start=page_start, page_end=page_end,
        blocks=blocks, summaries=summaries, key_notes=key_notes, stages=stages,
        backgrounds=backgrounds, default_background=default_background,
    )
    (out / f"{stem}_精读.md").write_text(markdown, encoding="utf-8")
    (out / "source_maps" / f"Chapter_{chapter:02d}_source_map.json").write_text(
        json.dumps(source_map, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    notes = f"""# Chapter {chapter} 生成说明

- 范围：PDF pp.{page_start}–{page_end}
- 视角：{pov.title()}
- 段落数：{len(blocks)}
- 人名策略：保留原始英文
- 剧透策略：严格限于当前段落已知信息
- 翻译策略：不提供逐段完整中译，仅提供中文段意和精读
- 提取修复：{extraction_notes}
"""
    (out / "notes" / f"Chapter_{chapter:02d}_notes.md").write_text(notes, encoding="utf-8")

