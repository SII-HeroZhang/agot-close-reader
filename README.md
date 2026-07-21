# 冰与火之歌 · A Game of Thrones 逐章精读

一个面向个人英语学习的静态阅读网站。内容覆盖 **Prologue + Chapter 1–72**，共 **73 篇、6,763 个精读段落**；每段包含英文原文、难词与短语、段意、写法分析以及无剧透背景，人名统一保留英文。

## 在线网站

### [立即开始阅读 →](https://sii-herozhang.github.io/agot-close-reader/)

[![站点预览](site/public/og.png)](https://sii-herozhang.github.io/agot-close-reader/)

[![Deploy static reader to GitHub Pages](https://github.com/SII-HeroZhang/agot-close-reader/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/SII-HeroZhang/agot-close-reader/actions/workflows/deploy-pages.yml)

> 阅读进度、书签和词汇收藏只保存在当前浏览器，不需要注册账号，也不会上传到服务器。换浏览器或设备前，请先在“我的书房”中导出学习数据。

## 网站功能

- **逐段精读**：保留英文原段，讲解词汇、段意、叙事手法、人物动机和当前可知背景。
- **中英全文搜索**：可以搜索英文原句、单词、人物、中文概念与背景说明。
- **段落书签**：收藏任意段落，之后从“我的书房”直接返回原位置。
- **词汇收藏**：在词汇表中单独收藏单词、音标、词性和语境释义。
- **阅读进度**：自动记录最近阅读段落、章节进度和已完成章节。
- **阅读设置**：支持系统主题、手动深浅色、正文字号和阅读行宽调节。
- **本地数据备份**：学习记录可导出为 version 1 JSON，并支持导入、校验和去重。
- **响应式布局**：桌面端提供章节侧栏和段落目录，移动端使用抽屉导航。

## 使用指南

### 1. 选择章节

进入[网站首页](https://sii-herozhang.github.io/agot-close-reader/)后，可以：

- 从 **Prologue** 开始顺序阅读；
- 在章节目录中直接打开 Chapter 1–72；
- 使用 POV 按钮筛选 Bran、Catelyn、Daenerys、Eddard、Jon、Sansa、Tyrion、Arya 等视角章节；
- 点击“继续阅读”回到上次读到的段落。

### 2. 阅读一个精读段落

每个段落均有稳定编号，例如 `PRO-P006-001` 或 `CH01-P016-001`，并依次提供：

1. 英文原文；
2. 难词与短语，包括音标、词性、语境释义和原文搭配；
3. “这一段说了什么”；
4. 值得注意的叙事、语气、人物心理或文学表达；
5. 当前阅读进度允许范围内的背景与伏笔。

段落右上方可以添加书签或复制该段的永久链接。桌面端右侧目录可以快速跳转到本章任意段落。

### 3. 全文搜索

点击页面顶部的“搜索”，或使用快捷键：

- macOS：`⌘ K`
- Windows / Linux：`Ctrl K`
- 非输入状态下也可以按 `/`

搜索覆盖英文原文、难词、中文段意、写法分析和背景说明。结果会显示章节、POV、PDF 页码和段落编号，点击后可直接跳到对应段落。

### 4. 收藏词汇和段落

- 点击段落工具栏中的 **☆ 书签** 收藏整段；
- 点击词汇表中的 **+ 收藏** 保存单词；
- 再次点击可以取消收藏；
- 所有收藏内容可在顶部导航的 **我的书房** 中集中查看和删除。

### 5. 阅读进度与已读章节

网站会自动记录当前章节、最近可见段落和阅读百分比。接近章节末尾时会自动标记完成，也可以使用章节顶部的“标记本章已读”手动切换状态。

这些记录通过 `localStorage` 保存在当前浏览器。无账号、无云同步，也不包含分析追踪。

### 6. 导出与导入学习数据

打开 **我的书房**：

1. 点击“导出学习数据”，下载 JSON 备份；
2. 在另一台设备打开同一网站；
3. 点击“导入 JSON”并选择备份文件；
4. 网站会验证数据版本和字段类型，并自动去除重复书签与词汇。

导入会替换当前浏览器中的学习记录。清除浏览器站点数据前，建议先导出备份。

### 7. 调整阅读体验

页面右上角提供：

- `◐`：快速切换深色或浅色主题；
- `Aa`：设置跟随系统、正文字号和正文行宽；
- `↑`：长页面中快速返回顶部。

## 本地构建

要求 Python 3.10+。

```bash
git clone https://github.com/SII-HeroZhang/agot-close-reader.git
cd agot-close-reader
python -m pip install -r site/requirements.txt
BASE_PATH= SITE_ORIGIN=http://localhost:8000 python site/build.py
BASE_PATH= python site/audit_site.py
python -m http.server 8000 --directory site/dist
```

打开 `http://localhost:8000/` 即可预览。GitHub Actions 会使用生产环境的 `/agot-close-reader/` base path 重新构建并再次审计。

## 项目结构

```text
.
├── outputs/                       # Markdown 精读与 source map，网站唯一内容源
├── site/
│   ├── assets/                    # 样式、交互脚本和搜索 Web Worker
│   ├── public/og.png              # 社交分享卡片
│   ├── build.py                   # 静态网站生成器
│   ├── audit_site.py              # 页面、锚点、索引和链接审计
│   └── dist/                      # 构建产物，不进入版本控制
├── work/                          # 内容提取、生成与审计脚本
└── .github/workflows/             # GitHub Pages 自动部署
```

`site/build.py` 兼容 Prologue、Chapter 1–7 的旧版 source-map 字段和 Chapter 8–72 的新版字段。每次构建必须通过以下门禁：

- 73 个阅读页面；
- 6,763 个唯一段落锚点；
- 6,763 条搜索记录；
- 章节导航、段落目录和 GitHub Pages base path 链接检查。

## 更新内容与发布

修改 `outputs/` 中的精读 Markdown 或 source map 后，先在本地重新构建和审计：

```bash
BASE_PATH=/agot-close-reader \
SITE_ORIGIN=https://sii-herozhang.github.io \
REPOSITORY_URL=https://github.com/SII-HeroZhang/agot-close-reader \
python site/build.py

BASE_PATH=/agot-close-reader python site/audit_site.py
python work/audit_agot_readers.py
```

推送到 `main` 后，[GitHub Actions](https://github.com/SII-HeroZhang/agot-close-reader/actions/workflows/deploy-pages.yml) 会自动构建、审计并发布到 GitHub Pages。

## 版权说明

本站为非商业语言学习与文本分析项目。原著文字版权归 George R. R. Martin 及相关权利人所有。公开发布完整原文存在版权风险；免责声明不构成授权，也不能消除该风险。如有权利问题，请通过 [GitHub Issues](https://github.com/SII-HeroZhang/agot-close-reader/issues/new) 联系处理或请求下架。
