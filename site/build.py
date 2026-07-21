#!/usr/bin/env python3
"""Build the dependency-light static study reader from outputs/*.md."""
from __future__ import annotations

import html
import json
import os
import re
import shutil
from collections import Counter
from pathlib import Path

import markdown
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SITE = Path(__file__).resolve().parent
OUTPUTS = ROOT / "outputs"
READERS = OUTPUTS / "AGOT_逐章精读"
DIST = SITE / "dist"
BASE = os.environ.get("BASE_PATH", "/agot-close-reader").rstrip("/")
SITE_ORIGIN = os.environ.get("SITE_ORIGIN", "https://example.github.io").rstrip("/")
REPOSITORY_URL = os.environ.get("REPOSITORY_URL", "https://github.com/OWNER/agot-close-reader").rstrip("/")
SITE_URL = f"{SITE_ORIGIN}{BASE}"
SITE_TITLE = "冰与火之歌"


def route(path: str = "") -> str:
    suffix = "/" + path.lstrip("/") if path else "/"
    return f"{BASE}{suffix}" if BASE else suffix


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def field(block: dict, *names: str) -> str:
    for name in names:
        value = block.get(name)
        if isinstance(value, str):
            return value
    return ""


def strip_markdown(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"[`*_>#|\[\]()]", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def vocab_for_block(markdown_text: str, block_id: str) -> str:
    marker = f"### {block_id}"
    start = markdown_text.find(marker)
    if start < 0:
        return ""
    tail = markdown_text[start + len(marker):]
    next_match = re.search(r"\n<a id=|\n### (?:CH|PRO)-", tail)
    chunk = tail[: next_match.start()] if next_match else tail
    match = re.search(r"\*\*难词与短语\*\*(.*?)(?:\*\*这一段说了什么\*\*)", chunk, re.S)
    return strip_markdown(match.group(1)) if match else ""


def load_chapters() -> list[dict]:
    sources: list[tuple[int, str, Path, Path, str]] = [
        (0, "prologue", OUTPUTS / "AGOT_Prologue_精读.md", OUTPUTS / "source_map.json", "WILL")
    ]
    for md_path in sorted(READERS.glob("Chapter_*_精读.md")):
        match = re.match(r"Chapter_(\d+)_([A-Z]+)_精读\.md", md_path.name)
        if not match:
            continue
        number = int(match.group(1))
        sources.append((number, str(number), md_path, READERS / "source_maps" / f"Chapter_{number:02d}_source_map.json", match.group(2)))

    chapters: list[dict] = []
    for number, slug, md_path, map_path, pov in sources:
        source = read_json(map_path)
        blocks = source["blocks"]
        page_range = source.get("page_range") or source.get("paper", {}).get("pdf_page_range")
        markdown_text = md_path.read_text(encoding="utf-8")
        label = "Prologue" if number == 0 else f"Chapter {number}"
        normalized_blocks = []
        for block in blocks:
            normalized_blocks.append({
                "id": block["id"],
                "page": block["page"],
                "endPage": block.get("end_page", block["page"]),
                "original": field(block, "original_text"),
                "summary": field(block, "explanation_zh", "paragraph_explanation_zh"),
                "note": field(block, "literary_note_zh", "reading_note_zh"),
                "background": field(block, "background_zh", "background_note_zh"),
                "vocab": vocab_for_block(markdown_text, block["id"]),
            })
        chapters.append({
            "number": number,
            "id": slug,
            "label": label,
            "pov": pov,
            "pages": page_range,
            "count": len(blocks),
            "markdown": markdown_text,
            "blocks": normalized_blocks,
            "url": route(f"chapters/{slug}/"),
        })
    if len(chapters) != 73:
        raise RuntimeError(f"Expected 73 sections, found {len(chapters)}")
    return chapters


def render_markdown(chapter: dict) -> str:
    rendered = markdown.markdown(
        chapter["markdown"],
        extensions=["extra", "tables", "fenced_code", "sane_lists"],
        output_format="html5",
    )
    soup = BeautifulSoup(rendered, "html.parser")
    # The source notes contain hand-written Chinese fragment links such as
    # #段落目录.  Add matching ids without running Markdown's global TOC
    # extension, which would both transliterate those headings and duplicate
    # the explicit stable paragraph ids.
    fragment_targets = {
        link["href"][1:]
        for link in soup.select('a[href^="#"]')
        if len(link.get("href", "")) > 1
    }
    for source_heading in soup.find_all(re.compile(r"^h[1-6]$")):
        heading_text = source_heading.get_text(" ", strip=True)
        if heading_text in fragment_targets and soup.find(id=heading_text) is None:
            source_heading["id"] = heading_text
    first_h1 = soup.find("h1")
    if first_h1:
        first_h1.decompose()
    by_id = {block["id"]: block for block in chapter["blocks"]}

    for block_id, block in by_id.items():
        heading = soup.find("h3", string=lambda value: isinstance(value, str) and value.strip() == block_id)
        if heading is None:
            raise RuntimeError(f"Missing heading {block_id}")
        anchor = soup.find(id=block_id.lower())
        # Markdown wraps a standalone HTML anchor in a paragraph.  Move that
        # complete paragraph into the card; inserting a <section> inside the
        # generated <p> would create invalid HTML and cause browsers to close
        # the card before the paragraph content.
        start = anchor.parent if anchor and anchor.parent.name == "p" else (anchor or heading)
        wrapper = soup.new_tag("section")
        wrapper["class"] = "paragraph-card"
        wrapper["data-anchor"] = block_id.lower()
        wrapper["data-chapter"] = chapter["id"]
        start.insert_before(wrapper)
        node = start
        while node is not None:
            next_node = node.next_sibling
            is_end = getattr(node, "name", None) == "hr"
            wrapper.append(node.extract())
            if is_end:
                break
            node = next_node

        toolbar = soup.new_tag("div")
        toolbar["class"] = "paragraph-tools"
        toolbar.append(BeautifulSoup(
            f'<button type="button" class="page-pill pdf-page-button js-open-pdf" '
            f'data-pdf-page="{block["page"]}" data-anchor="{block_id.lower()}" '
            f'aria-label="在 PDF 中查看第 {block["page"]} 页">▣ PDF p.{block["page"]}</button>'
            f'<button type="button" class="icon-button js-bookmark" data-anchor="{block_id.lower()}" '
            f'aria-pressed="false" aria-label="收藏段落 {block_id}">☆ <span>书签</span></button>'
            f'<button type="button" class="icon-button js-copy-link" data-anchor="{block_id.lower()}" '
            f'aria-label="复制段落链接 {block_id}">↗ <span>复制链接</span></button>',
            "html.parser",
        ))
        heading.insert_after(toolbar)

        vocab_label = next((p for p in wrapper.find_all("p") if p.get_text(" ", strip=True) == "难词与短语"), None)
        table = vocab_label.find_next_sibling("table") if vocab_label else None
        if table:
            header_row = table.find("tr")
            if header_row:
                th = soup.new_tag("th")
                th.string = "收藏"
                header_row.append(th)
            for row in table.find_all("tr")[1:]:
                cells = row.find_all(["td", "th"], recursive=False)
                if not cells:
                    continue
                values = [cell.get_text(" ", strip=True) for cell in cells]
                term = values[0]
                if not term:
                    continue
                td = soup.new_tag("td")
                button = soup.new_tag("button")
                button["type"] = "button"
                button["class"] = "vocab-save js-vocab-save"
                button["data-term"] = term
                button["data-pronunciation"] = values[1] if len(values) > 1 else ""
                button["data-pos"] = values[2] if len(values) > 2 else ""
                button["data-meaning"] = values[3] if len(values) > 3 else ""
                button["data-anchor"] = block_id.lower()
                button["aria-label"] = f"收藏单词 {term}"
                button.string = "+ 收藏"
                td.append(button)
                row.append(td)

    return str(soup)


def chapter_nav(chapters: list[dict], current: str | None = None) -> str:
    links = []
    for chapter in chapters:
        active = ' aria-current="page" class="is-current"' if chapter["id"] == current else ""
        links.append(
            f'<a href="{chapter["url"]}" data-chapter-link="{chapter["id"]}"{active}>'
            f'<span>{chapter["label"]}</span><small>{chapter["pov"]}</small></a>'
        )
    return (
        '<aside class="chapter-sidebar" id="chapter-sidebar" aria-label="章节导航">'
        '<div class="sidebar-heading"><span>全书目录</span><button class="sidebar-close" type="button" '
        'data-close-sidebar aria-label="关闭章节目录">×</button></div>'
        f'<nav class="sidebar-utility"><a href="{route("pdf/")}"><strong>▣ 阅读完整 PDF</strong><small>原文与解读对照</small></a>'
        f'<a href="{route("library/")}"><strong>我的书房</strong><small>进度、书签与词汇</small></a></nav>'
        '<nav class="chapter-link-list">' + "".join(links) + '</nav></aside>'
    )


def global_header() -> str:
    return f'''<header class="site-header">
      <button type="button" class="header-icon mobile-only" data-open-sidebar aria-label="打开章节目录">☰</button>
      <a class="brand" href="{route()}"><span class="brand-mark">冰</span><span>{SITE_TITLE}</span></a>
      <nav class="top-nav" aria-label="主导航">
        <a href="{route()}">首页</a><a href="{route('pdf/')}">PDF 阅读器</a><a href="{route('library/')}">我的书房</a>
      </nav>
      <div class="header-actions">
        <button type="button" class="header-button js-open-search" aria-label="打开全文搜索">⌕ <span>搜索</span><kbd>⌘K</kbd></button>
        <button type="button" class="header-icon js-theme-toggle" aria-label="切换深浅色">◐</button>
        <button type="button" class="header-icon js-open-settings" aria-label="阅读设置">Aa</button>
      </div>
    </header>'''


def dialogs() -> str:
    return '''<dialog class="search-dialog" id="search-dialog" aria-labelledby="search-title">
      <form method="dialog" class="dialog-head"><div><p class="eyebrow">全文检索</p><h2 id="search-title">搜索 6,763 个段落</h2></div><button aria-label="关闭搜索">×</button></form>
      <label class="search-field"><span class="sr-only">搜索中英文内容</span><input id="search-input" type="search" maxlength="120" autocomplete="off" placeholder="输入英文原句、单词或中文概念…"></label>
      <p class="search-status" id="search-status" aria-live="polite">输入至少 2 个字符开始搜索</p>
      <div class="search-results" id="search-results"></div>
    </dialog>
    <dialog class="settings-dialog" id="settings-dialog" aria-labelledby="settings-title">
      <form method="dialog" class="dialog-head"><div><p class="eyebrow">阅读偏好</p><h2 id="settings-title">阅读设置</h2></div><button aria-label="关闭设置">×</button></form>
      <label>正文字号 <output id="font-size-output">18px</output><input id="font-size-control" type="range" min="16" max="24" step="1" value="18"></label>
      <label>正文宽度 <output id="line-width-output">760px</output><input id="line-width-control" type="range" min="620" max="920" step="20" value="760"></label>
      <fieldset><legend>主题</legend><div class="segmented"><button type="button" data-theme-choice="auto">跟随系统</button><button type="button" data-theme-choice="light">浅色</button><button type="button" data-theme-choice="dark">深色</button></div></fieldset>
    </dialog>
    <dialog class="pdf-dialog" id="pdf-dialog" aria-labelledby="pdf-dialog-title">
      <div class="dialog-head pdf-dialog-head"><div><p class="eyebrow">PDF Companion</p><h2 id="pdf-dialog-title">原文与解读对照</h2></div>
        <div class="pdf-head-actions"><button type="button" class="text-button js-select-pdf">更换 PDF</button><button type="button" class="dialog-close js-close-pdf" aria-label="关闭 PDF 对照阅读">×</button></div></div>
      <div class="pdf-split"><section class="pdf-viewer-shell" data-pdf-viewer>
        <div class="pdf-empty-state"><strong>正在载入原始 PDF</strong><p>如果内嵌阅读器无法显示，可以使用下方按钮在新标签页打开当前页。</p></div>
        <iframe class="pdf-frame js-pdf-frame" title="A Game of Thrones 原始 PDF"></iframe>
        <a class="pdf-open-tab js-pdf-open-tab" target="_blank" rel="noopener">在新标签页打开当前页 ↗</a>
      </section><aside class="pdf-companion"><div class="pdf-companion-heading"><div><p class="eyebrow">Close reading</p><h2>对应解读</h2></div><span class="js-pdf-page-label">PDF p.—</span></div>
        <div id="pdf-companion-content"><p class="empty-state">从章节中的段落点击“PDF p.X”，即可在这里查看对应解读。</p></div></aside></div>
    </dialog>
    <input class="sr-only" id="pdf-file-input" type="file" accept="application/pdf,.pdf" aria-label="选择另一份本地 PDF 文件">'''


def footer() -> str:
    return f'''<footer class="site-footer"><p><strong>非商业学习笔记。</strong> 原著文字版权归 George R. R. Martin 及相关权利人所有。</p>
    <p>本站用于个人语言学习与文本分析；如有权利问题，请通过<a href="{html.escape(REPOSITORY_URL)}/issues/new">仓库 Issues 联系或申请下架</a>。</p></footer>'''


def html_page(*, title: str, description: str, body: str, chapters: list[dict], current: str | None = None, page_kind: str = "page") -> str:
    manifest = [{k: c[k] for k in ("id", "number", "label", "pov", "pages", "count", "url")} for c in chapters]
    config = json.dumps({"basePath": BASE, "currentChapter": current, "pageKind": page_kind, "chapters": manifest}, ensure_ascii=False).replace("</", "<\\/")
    if page_kind == "home":
        canonical_path = ""
    elif page_kind in {"library", "pdf"}:
        canonical_path = f"{page_kind}/"
    else:
        canonical_path = f"chapters/{current}/"
    canonical = f"{SITE_URL}/{canonical_path}"
    return f'''<!doctype html><html lang="zh-CN"><head>
    <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
    <title>{html.escape(title)}</title><meta name="description" content="{html.escape(description)}">
    <meta name="robots" content="index,follow"><link rel="canonical" href="{canonical}">
    <meta name="theme-color" content="#0d1722"><meta property="og:type" content="website">
    <meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(description)}">
    <meta property="og:url" content="{canonical}"><meta property="og:image" content="{SITE_URL}/assets/og.png">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="stylesheet" href="{route('assets/site.css')}"><script>window.AGOT_CONFIG={config};</script>
    <script src="{route('assets/site.js')}" defer></script><script src="{route('assets/pdf-reader.js')}" defer></script></head>
    <body data-page="{page_kind}">{global_header()}<div class="sidebar-scrim" data-close-sidebar></div>
    {chapter_nav(chapters, current)}{body}{dialogs()}{footer()}<button type="button" class="back-to-top" aria-label="返回顶部">↑</button></body></html>'''


def build_home(chapters: list[dict]) -> str:
    total = sum(c["count"] for c in chapters)
    first_page = min(c["pages"][0] for c in chapters)
    last_page = max(c["pages"][1] for c in chapters)
    povs = Counter(c["pov"].title() for c in chapters)
    filter_buttons = ['<button type="button" class="is-active" data-pov-filter="all">全部</button>'] + [
        f'<button type="button" data-pov-filter="{html.escape(pov)}">{html.escape(pov)} <span>{count}</span></button>'
        for pov, count in sorted(povs.items())
    ]
    cards = []
    for chapter in chapters:
        cards.append(f'''<a class="chapter-card" href="{chapter['url']}" data-pov="{chapter['pov'].title()}" data-chapter-card="{chapter['id']}">
          <div><span class="chapter-number">{chapter['label']}</span><span class="chapter-pov">{chapter['pov']}</span></div>
          <p>PDF pp.{chapter['pages'][0]}–{chapter['pages'][1]} · {chapter['count']} 段</p>
          <div class="card-progress"><span></span></div><small class="card-status">尚未开始</small>
        </a>''')
    body = f'''<main class="home-main">
      <section class="hero"><div class="hero-copy"><p class="eyebrow">A Game of Thrones · 逐章精读</p><h1>{SITE_TITLE}</h1>
      <p class="hero-lead">从 Prologue 到 Chapter 72，保留英文原段，逐段拆解词汇、叙事、人物动机与无剧透背景。</p>
      <div class="hero-actions"><a class="primary-button" href="{route('pdf/')}">阅读完整 PDF</a><a class="secondary-button" href="{route('chapters/prologue/')}">从序章开始</a><button type="button" class="secondary-button js-open-search">搜索全书</button></div></div>
      <div class="hero-stats"><div><strong>73</strong><span>篇章</span></div><div><strong>{total:,}</strong><span>精读段落</span></div><div><strong>{first_page}–{last_page}</strong><span>PDF 正文页</span></div></div></section>
      <section class="pdf-home-callout"><div><p class="eyebrow">Read the original</p><h2>直接阅读完整原文 PDF</h2><p>755 页原书已内置。左侧读原文，右侧按页查看对应解读；也可以从任意精读段落一键返回原页。</p></div>
      <div><a class="primary-button" href="{route('pdf/')}">进入 PDF 对照阅读器</a><a class="secondary-button" href="{route('assets/agot-original.pdf')}" target="_blank" rel="noopener">单独打开 PDF ↗</a></div></section>
      <section class="continue-section"><div class="section-heading"><div><p class="eyebrow">Continue reading</p><h2>继续阅读</h2></div><a href="{route('library/')}">打开我的书房 →</a></div>
      <article class="continue-card" id="continue-card"><div><span class="continue-label">还没有阅读记录</span><h3>从 Prologue 开始这次守望</h3><p>阅读进度只保存在当前浏览器，可随时导出备份。</p></div><a href="{route('chapters/prologue/')}">开始阅读</a></article></section>
      <section class="catalog"><div class="section-heading"><div><p class="eyebrow">73 sections</p><h2>章节目录</h2></div></div>
      <div class="pov-filters" aria-label="按视角筛选">{''.join(filter_buttons)}</div><div class="chapter-grid">{''.join(cards)}</div></section>
    </main>'''
    return html_page(title=f"{SITE_TITLE} · A Game of Thrones 逐章精读", description="A Game of Thrones 中英逐段精读：词汇、段意、写法、人物动机与无剧透背景。", body=body, chapters=chapters, page_kind="home")


def build_chapter(chapter: dict, chapters: list[dict]) -> str:
    index = chapters.index(chapter)
    prev_chapter = chapters[index - 1] if index else None
    next_chapter = chapters[index + 1] if index + 1 < len(chapters) else None
    toc = "".join(
        f'<a href="#{block["id"].lower()}" data-toc-anchor="{block["id"].lower()}"><span>{block["id"]}</span><small>p.{block["page"]}</small></a>'
        for block in chapter["blocks"]
    )
    prev_link = f'<a href="{prev_chapter["url"]}">← {prev_chapter["label"]}</a>' if prev_chapter else '<span></span>'
    next_link = f'<a href="{next_chapter["url"]}">{next_chapter["label"]} →</a>' if next_chapter else '<a href="' + route('library/') + '">前往我的书房 →</a>'
    article = render_markdown(chapter)
    body = f'''<div class="reader-shell"><main class="reader-main">
      <header class="chapter-hero"><p class="eyebrow">{chapter['label']} · PDF pp.{chapter['pages'][0]}–{chapter['pages'][1]}</p>
      <h1>{chapter['pov']}</h1><p>{chapter['count']} 个原文段落 · 英文姓名 · 无剧透精读</p>
      <div class="chapter-actions"><button type="button" class="secondary-button" id="mark-complete">标记本章已读</button><button type="button" class="secondary-button js-open-search">在全书中搜索</button><button type="button" class="secondary-button js-open-pdf" data-pdf-page="{chapter['pages'][0]}">PDF 对照阅读</button></div>
      <div class="reading-progress-track" aria-hidden="true"><span id="reading-progress-bar"></span></div></header>
      <article class="reader-content">{article}</article>
      <nav class="chapter-pagination" aria-label="章节翻页">{prev_link}{next_link}</nav></main>
      <aside class="local-toc"><div><p class="eyebrow">On this chapter</p><h2>段落目录</h2><span>{chapter['count']} 段</span></div><nav>{toc}</nav></aside></div>'''
    return html_page(title=f"{chapter['label']} — {chapter['pov']} · {SITE_TITLE}", description=f"{chapter['label']} {chapter['pov']} 逐段精读，PDF pp.{chapter['pages'][0]}–{chapter['pages'][1]}。", body=body, chapters=chapters, current=chapter["id"], page_kind="chapter")


def build_library(chapters: list[dict]) -> str:
    body = f'''<main class="library-main"><header class="library-hero"><p class="eyebrow">Your local study room</p><h1>我的书房</h1>
      <p>书签、词汇与阅读记录只保存在这个浏览器。导出 JSON，即可在另一台设备继续。</p>
      <div class="library-actions"><button type="button" class="primary-button" id="export-data">导出学习数据</button><label class="secondary-button file-button">导入 JSON<input id="import-data" type="file" accept="application/json"></label><button type="button" class="danger-button" id="reset-data">清空本机数据</button></div>
      <p class="import-status" id="import-status" aria-live="polite"></p></header>
      <section class="library-grid"><article class="library-panel"><div class="section-heading"><div><p class="eyebrow">Progress</p><h2>阅读进度</h2></div></div><div id="progress-list" class="study-list"><p class="empty-state">尚无阅读记录。</p></div></article>
      <article class="library-panel"><div class="section-heading"><div><p class="eyebrow">Bookmarks</p><h2>段落书签</h2></div></div><div id="bookmark-list" class="study-list"><p class="empty-state">尚未收藏段落。</p></div></article>
      <article class="library-panel wide"><div class="section-heading"><div><p class="eyebrow">Vocabulary</p><h2>词汇收藏</h2></div></div><div id="vocabulary-list" class="vocabulary-library"><p class="empty-state">尚未收藏词汇。</p></div></article></section>
      <aside class="privacy-note"><strong>隐私说明</strong><p>本站没有账号、服务器数据库或分析追踪。清除浏览器站点数据会删除记录，请定期导出备份。</p></aside></main>'''
    return html_page(title=f"我的书房 · {SITE_TITLE}", description="本机保存的阅读进度、段落书签与词汇收藏。", body=body, chapters=chapters, page_kind="library")


def build_pdf_reader(chapters: list[dict]) -> str:
    body = f'''<main class="pdf-reader-main"><header class="pdf-reader-hero"><p class="eyebrow">Read · Compare instantly</p><h1>PDF 对照阅读器</h1>
      <p>在左侧直接阅读原始 PDF，右侧按当前页查看精读段落。章节页中的每个“PDF p.X”按钮也能立即打开原页与对应解读。</p>
      <div class="pdf-reader-actions"><a class="primary-button" href="{route('assets/agot-original.pdf')}" target="_blank" rel="noopener">在新标签页打开完整 PDF</a><button type="button" class="secondary-button js-select-pdf">改用本地 PDF</button><button type="button" class="secondary-button js-remove-pdf" hidden>恢复站内 PDF</button><span class="pdf-file-status js-pdf-file-status">正在载入站内 PDF…</span></div></header>
      <section class="pdf-reader-toolbar" aria-label="PDF 页码控制"><button type="button" data-pdf-step="-1" aria-label="上一页">←</button>
        <form id="pdf-page-form"><label for="pdf-page-input">PDF 页码</label><input id="pdf-page-input" type="number" min="1" max="755" value="6" inputmode="numeric"><span>/ 755</span><button type="submit">前往</button></form>
        <button type="button" data-pdf-step="1" aria-label="下一页">→</button></section>
      <div class="pdf-reader-layout"><section class="pdf-viewer-shell pdf-reader-viewer" data-pdf-viewer>
        <div class="pdf-empty-state"><strong>正在载入《A Game of Thrones》PDF</strong><p>如果浏览器不支持内嵌 PDF，可以在新标签页中打开当前页。</p></div>
        <iframe class="pdf-frame js-pdf-frame" data-pdf-page="6" title="A Game of Thrones 原始 PDF"></iframe>
        <a class="pdf-open-tab js-pdf-open-tab" target="_blank" rel="noopener">在新标签页打开当前页 ↗</a>
      </section><aside class="pdf-page-notes"><div class="pdf-companion-heading"><div><p class="eyebrow">Page companion</p><h2>本页解读</h2></div><span id="pdf-reader-page-label">PDF p.6</span></div>
        <p class="pdf-page-hint">点击条目进入完整精读。跨页段落也会显示，并标记为“承接上页”。</p><div id="pdf-page-results" aria-live="polite"><p class="empty-state">正在载入页码索引…</p></div></aside></div>
      <aside class="privacy-note"><strong>版权提示</strong><p>PDF 与英文原文版权归 George R. R. Martin 及相关权利人所有，本站仅用于非商业语言学习与文本分析。权利人可通过仓库 Issues 联系处理或申请下架。</p></aside></main>'''
    return html_page(title=f"PDF 对照阅读器 · {SITE_TITLE}", description="在浏览器本地阅读 A Game of Thrones PDF，并按页查看对应中文精读。", body=body, chapters=chapters, page_kind="pdf")


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def main() -> None:
    chapters = load_chapters()
    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "assets").mkdir(parents=True)
    (DIST / "data").mkdir(parents=True)
    for asset in (SITE / "assets").iterdir():
        if asset.is_file():
            shutil.copy2(asset, DIST / "assets" / asset.name)
    public_dir = SITE / "public"
    if public_dir.exists():
        for public_file in public_dir.iterdir():
            if public_file.is_file():
                shutil.copy2(public_file, DIST / "assets" / public_file.name)

    write_text(DIST / "index.html", build_home(chapters))
    write_text(DIST / "library" / "index.html", build_library(chapters))
    write_text(DIST / "pdf" / "index.html", build_pdf_reader(chapters))
    for chapter in chapters:
        write_text(DIST / "chapters" / chapter["id"] / "index.html", build_chapter(chapter, chapters))

    manifest = [{k: c[k] for k in ("id", "number", "label", "pov", "pages", "count", "url")} for c in chapters]
    search_rows = []
    for chapter in chapters:
        for block in chapter["blocks"]:
            search_rows.append({
                "chapterId": chapter["id"], "chapterLabel": chapter["label"], "pov": chapter["pov"],
                "anchorId": block["id"].lower(), "displayId": block["id"], "pdfPage": block["page"],
                "url": f'{chapter["url"]}#{block["id"].lower()}', "original": block["original"],
                "summary": block["summary"], "note": block["note"], "background": block["background"], "vocab": block["vocab"],
            })
    if len(search_rows) != 6763:
        raise RuntimeError(f"Expected 6763 search records, found {len(search_rows)}")
    write_text(DIST / "data" / "manifest.json", json.dumps(manifest, ensure_ascii=False, separators=(",", ":")))
    write_text(DIST / "data" / "search-index.json", json.dumps(search_rows, ensure_ascii=False, separators=(",", ":")))

    page_map: dict[str, list[dict]] = {}
    for chapter in chapters:
        for block in chapter["blocks"]:
            for page in range(block["page"], block["endPage"] + 1):
                page_map.setdefault(str(page), []).append({
                    "chapterId": chapter["id"], "chapterLabel": chapter["label"], "pov": chapter["pov"],
                    "anchorId": block["id"].lower(), "displayId": block["id"], "pdfPage": page,
                    "startPage": block["page"], "continued": page > block["page"],
                    "url": f'{chapter["url"]}#{block["id"].lower()}', "original": block["original"],
                    "summary": block["summary"],
                })
    write_text(DIST / "data" / "page-map.json", json.dumps(page_map, ensure_ascii=False, separators=(",", ":")))

    urls = [f"{SITE_URL}/", f"{SITE_URL}/library/", f"{SITE_URL}/pdf/"] + [f"{SITE_ORIGIN}{c['url']}" for c in chapters]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{html.escape(url)}</loc></url>\n" for url in urls) + "</urlset>\n"
    write_text(DIST / "sitemap.xml", sitemap)
    write_text(DIST / "robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    write_text(DIST / ".nojekyll", "")
    print(json.dumps({"status": "built", "sections": len(chapters), "paragraphs": len(search_rows), "dist": str(DIST)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
