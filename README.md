# 冰与火之歌 · A Game of Thrones 逐章精读

一个面向个人英语学习的静态阅读网站。内容覆盖 Prologue 与 Chapter 1–72，共 73 篇、6,763 个带稳定锚点的精读段落；人名统一保留英文。

## 功能

- 中英全文检索：英文原文、词汇、段意、写法与背景，首次搜索时才加载索引，并由 Web Worker 检索。
- 本地学习数据：段落书签、词汇收藏、阅读进度、完成章节、版本化 JSON 导入与导出。
- 长文阅读体验：章节侧栏、段落目录、深浅主题、字号和行宽设置、移动端抽屉导航。
- GitHub Pages 项目站点：所有链接和资源兼容 `/agot-close-reader/` base path。

## 本地构建

要求 Python 3.10+。

```bash
python -m pip install -r site/requirements.txt
BASE_PATH= SITE_ORIGIN=http://localhost:8000 python site/build.py
BASE_PATH= python site/audit_site.py
```

预览构建结果：

```bash
python -m http.server 8000 --directory site/dist
```

然后打开 `http://localhost:8000/`。GitHub Actions 会自动使用生产环境的 `/agot-close-reader/` base path 重新构建并再次审计。

## 内容源与生成结果

- `outputs/` 是网站唯一内容源，包含 Markdown 精读与 source map。
- `site/build.py` 兼容 Prologue、Chapter 1–7 的旧字段和 Chapter 8–72 的新字段。
- `site/dist/` 是可重新生成的构建产物，不进入版本控制。
- 每次构建必须通过 73 个阅读页面、6,763 个唯一段落锚点、搜索索引和内部链接审计。

## 发布

推送 `main` 后，`.github/workflows/deploy-pages.yml` 会构建、审计并发布 GitHub Pages。仓库的 Pages Source 需设置为 **GitHub Actions**。

目标地址：`https://<username>.github.io/agot-close-reader/`

## 版权说明

本站为非商业语言学习与文本分析项目。原著文字版权归 George R. R. Martin 及相关权利人所有。公开发布完整原文存在版权风险；免责声明不构成授权，也不能消除该风险。如有权利问题，请通过仓库 Issues 联系处理或请求下架。
