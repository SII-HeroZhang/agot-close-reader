# *A Game of Thrones* 逐章精读总审计

审计日期：2026-07-21  
审计范围：Prologue 与 Chapter 1–72

## 结论

**PASS — 全部章节已生成并通过结构与来源映射审计。**

| 项目 | 结果 |
|---|---:|
| 独立章节 Markdown | 72 / 72 |
| 章节 source map | 72 / 72 |
| 章节校勘 notes | 72 / 72 |
| Chapter 1–72 正文段落 | 6,654 |
| Prologue 正文段落 | 109 |
| 全书精读段落合计 | 6,763 |
| Chapter 1–72 安全占位符 | 33 |
| 章节 PDF 正文范围 | pp.16–731 |
| 中文音译人物姓名命中 | 0 |
| 待生成 / 待复核目录项 | 0 |

## 已验证项目

- Chapter 1–72 文件与章节编号连续、无缺章或重复章。
- 每章均有独立 Markdown、source map 和校勘 notes。
- 每个正文段落均有：英文原段、难词与短语、中文段意、写法讲解、无剧透背景。
- 每个段落 ID 唯一，并准确编码章节号、起始 PDF 页码和段落顺序。
- Markdown 标题、HTML 锚点与 source map ID 按顺序逐一相等。
- README 中每章页码、段落数和文件链接与 source map 一致。
- source map 中原文、段意、文学讲解和背景字段均非空；不附逐段完整翻译。
- 全部人物姓名保持英文形式；常见中文音译形式全目录扫描无命中。
- 33 个敏感段落均使用稳定英文占位符，段落编号与剧情后果仍保留。
- Prologue 的 109 个段落、109 个标题、109 个锚点和五项精读栏目另行核对一致。

## PDF 非正文页面

以下页面只含 `previous | Table of Contents | next` 导航文字，不属于小说正文：

`24, 30, 66, 96, 122, 179, 212, 520, 562`

这些页面解释了部分相邻章节正文页码之间的一页间隔。Chapter 56 元数据范围止于 p.562，但最后一个正文段落位于 p.561；p.562 已确认只是导航页。

## Source map 兼容性

Chapter 1–7 使用早期等价字段名：

- `paragraph_explanation_zh`
- `reading_note_zh`
- `background_note_zh`

Chapter 8–72 使用新版字段名：

- `explanation_zh`
- `literary_note_zh`
- `background_zh`

审计器按语义等价字段验证；两种 schema 都包含稳定 ID、PDF 页码、原文和三类中文讲解。

## 复现审计

在项目根目录运行：

```bash
python work/audit_agot_readers.py
```

预期结果为 `"status": "PASS"` 且 `"errors": []`。
