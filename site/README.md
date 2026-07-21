# Static site generator

`build.py` 将 `../outputs/` 中的 73 篇精读内容统一为静态页面、搜索索引与章节清单。它只依赖 Markdown 和 Beautiful Soup，不需要 Node.js 或服务端运行时。

- `assets/site.js`：搜索、书签、词汇收藏、阅读进度、导入导出和阅读偏好。
- `assets/search-worker.js`：按需加载的中英全文检索。
- `assets/site.css`：现代典籍主题与响应式布局。
- `audit_site.py`：页面、段落、锚点、链接、索引和 OG 图片门禁。

