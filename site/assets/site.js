(() => {
  "use strict";

  const config = window.AGOT_CONFIG || { basePath: "", chapters: [] };
  const DATA_KEY = "agot-reader:v1";
  const PREFS_KEY = "agot-reader:prefs:v1";
  const now = () => new Date().toISOString();
  const chapterById = new Map(config.chapters.map((chapter) => [String(chapter.id), chapter]));

  const emptyData = () => ({
    version: 1,
    progress: { last: null, chapters: {} },
    completed: [],
    bookmarks: [],
    vocabulary: [],
  });

  function validData(value) {
    return Boolean(
      value && value.version === 1 && value.progress && typeof value.progress === "object" &&
      value.progress.chapters && typeof value.progress.chapters === "object" &&
      !Array.isArray(value.progress.chapters) &&
      Array.isArray(value.completed) && value.completed.every((id) => typeof id === "string" || typeof id === "number") &&
      Array.isArray(value.bookmarks) && value.bookmarks.every((item) => item && typeof item === "object" &&
        (typeof item.chapterId === "string" || typeof item.chapterId === "number") && typeof item.anchorId === "string") &&
      Array.isArray(value.vocabulary) && value.vocabulary.every((item) => item && typeof item === "object" &&
        typeof item.term === "string" && typeof item.meaning === "string")
    );
  }

  function normalizeData(value) {
    if (!validData(value)) return null;
    const normalized = emptyData();
    normalized.progress = value.progress;
    normalized.completed = [...new Set(value.completed.map(String))];
    const bookmarks = new Set();
    normalized.bookmarks = value.bookmarks.filter((item) => {
      item.chapterId = String(item.chapterId);
      const key = `${item.chapterId}|${item.anchorId}`;
      if (bookmarks.has(key)) return false;
      bookmarks.add(key); return true;
    });
    const vocabulary = new Set();
    normalized.vocabulary = value.vocabulary.filter((item) => {
      item.chapterId = String(item.chapterId || "");
      const key = `${item.term.toLocaleLowerCase()}|${item.meaning}`;
      if (vocabulary.has(key)) return false;
      vocabulary.add(key); return true;
    });
    return normalized;
  }

  function loadData() {
    try {
      const parsed = JSON.parse(localStorage.getItem(DATA_KEY) || "null");
      return normalizeData(parsed) || emptyData();
    } catch {
      return emptyData();
    }
  }

  let study = loadData();
  function saveData() {
    localStorage.setItem(DATA_KEY, JSON.stringify(study));
    window.dispatchEvent(new CustomEvent("agot:data-change", { detail: study }));
  }

  function loadPrefs() {
    try {
      const value = JSON.parse(localStorage.getItem(PREFS_KEY) || "{}");
      return {
        theme: ["auto", "light", "dark"].includes(value.theme) ? value.theme : "auto",
        fontSize: Math.min(24, Math.max(16, Number(value.fontSize) || 18)),
        lineWidth: Math.min(920, Math.max(620, Number(value.lineWidth) || 760)),
      };
    } catch {
      return { theme: "auto", fontSize: 18, lineWidth: 760 };
    }
  }

  let prefs = loadPrefs();
  function applyPrefs() {
    const root = document.documentElement;
    if (prefs.theme === "auto") root.removeAttribute("data-theme");
    else root.dataset.theme = prefs.theme;
    root.style.setProperty("--font-size", `${prefs.fontSize}px`);
    root.style.setProperty("--reader-width", `${prefs.lineWidth}px`);
    document.querySelectorAll("[data-theme-choice]").forEach((button) => {
      button.classList.toggle("is-active", button.dataset.themeChoice === prefs.theme);
    });
    const font = document.getElementById("font-size-control");
    const width = document.getElementById("line-width-control");
    if (font) font.value = String(prefs.fontSize);
    if (width) width.value = String(prefs.lineWidth);
    const fontOutput = document.getElementById("font-size-output");
    const widthOutput = document.getElementById("line-width-output");
    if (fontOutput) fontOutput.textContent = `${prefs.fontSize}px`;
    if (widthOutput) widthOutput.textContent = `${prefs.lineWidth}px`;
  }
  function savePrefs() {
    localStorage.setItem(PREFS_KEY, JSON.stringify(prefs));
    applyPrefs();
  }
  applyPrefs();

  const sidebarOpeners = document.querySelectorAll("[data-open-sidebar]");
  const sidebarClosers = document.querySelectorAll("[data-close-sidebar]");
  sidebarOpeners.forEach((button) => button.addEventListener("click", () => document.body.classList.add("sidebar-open")));
  sidebarClosers.forEach((button) => button.addEventListener("click", () => document.body.classList.remove("sidebar-open")));
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") document.body.classList.remove("sidebar-open");
  });

  const settingsDialog = document.getElementById("settings-dialog");
  document.querySelectorAll(".js-open-settings").forEach((button) => button.addEventListener("click", () => settingsDialog?.showModal()));
  document.querySelectorAll(".js-theme-toggle").forEach((button) => button.addEventListener("click", () => {
    const resolvedDark = document.documentElement.dataset.theme === "dark" ||
      (!document.documentElement.dataset.theme && matchMedia("(prefers-color-scheme: dark)").matches);
    prefs.theme = resolvedDark ? "light" : "dark";
    savePrefs();
  }));
  document.querySelectorAll("[data-theme-choice]").forEach((button) => button.addEventListener("click", () => {
    prefs.theme = button.dataset.themeChoice;
    savePrefs();
  }));
  document.getElementById("font-size-control")?.addEventListener("input", (event) => {
    prefs.fontSize = Number(event.target.value);
    savePrefs();
  });
  document.getElementById("line-width-control")?.addEventListener("input", (event) => {
    prefs.lineWidth = Number(event.target.value);
    savePrefs();
  });

  const backToTop = document.querySelector(".back-to-top");
  addEventListener("scroll", () => backToTop?.classList.toggle("is-visible", scrollY > 700), { passive: true });
  backToTop?.addEventListener("click", () => scrollTo({ top: 0, behavior: "smooth" }));

  // Search: the large bilingual index is loaded only after the first query.
  const searchDialog = document.getElementById("search-dialog");
  const searchInput = document.getElementById("search-input");
  const searchStatus = document.getElementById("search-status");
  const searchResults = document.getElementById("search-results");
  let searchWorker = null;
  let searchTimer = null;
  function openSearch() {
    if (!searchDialog) return;
    searchDialog.showModal();
    setTimeout(() => searchInput?.focus(), 20);
  }
  document.querySelectorAll(".js-open-search").forEach((button) => button.addEventListener("click", openSearch));
  document.addEventListener("keydown", (event) => {
    const target = event.target;
    const editing = target instanceof HTMLInputElement || target instanceof HTMLTextAreaElement || target?.isContentEditable;
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
      event.preventDefault(); openSearch();
    } else if (!editing && event.key === "/") {
      event.preventDefault(); openSearch();
    }
  });

  function ensureSearchWorker() {
    if (searchWorker) return searchWorker;
    searchWorker = new Worker(`${config.basePath}/assets/search-worker.js`);
    searchWorker.addEventListener("message", ({ data }) => {
      if (data.type === "ready") {
        if (searchStatus) searchStatus.textContent = `索引已载入 · ${data.count.toLocaleString()} 个段落`;
      }
      if (data.type === "results") renderSearchResults(data);
      if (data.type === "error" && searchStatus) searchStatus.textContent = `搜索索引加载失败：${data.message}`;
    });
    return searchWorker;
  }

  function textWithMark(text, query) {
    const fragment = document.createDocumentFragment();
    const normalized = text.toLocaleLowerCase();
    const needle = query.toLocaleLowerCase();
    const index = normalized.indexOf(needle);
    if (index < 0 || !needle) { fragment.append(document.createTextNode(text)); return fragment; }
    fragment.append(document.createTextNode(text.slice(0, index)));
    const mark = document.createElement("mark"); mark.textContent = text.slice(index, index + query.length); fragment.append(mark);
    fragment.append(document.createTextNode(text.slice(index + query.length)));
    return fragment;
  }

  function renderSearchResults(data) {
    if (!searchResults || !searchStatus) return;
    searchResults.replaceChildren();
    searchStatus.textContent = data.total ? `找到 ${data.total.toLocaleString()} 个结果，显示前 ${data.results.length} 个` : "没有找到匹配段落";
    for (const result of data.results) {
      const link = document.createElement("a"); link.className = "search-result"; link.href = result.url;
      const meta = document.createElement("div"); meta.className = "search-result-meta";
      const left = document.createElement("span"); left.textContent = `${result.chapterLabel} · ${result.pov}`;
      const right = document.createElement("span"); right.textContent = `${result.displayId} · p.${result.pdfPage}`;
      meta.append(left, right);
      const title = document.createElement("strong"); title.append(textWithMark(result.title, data.query));
      const snippet = document.createElement("p"); snippet.append(textWithMark(result.snippet, data.query));
      link.append(meta, title, snippet); searchResults.append(link);
    }
  }

  searchInput?.addEventListener("input", () => {
    clearTimeout(searchTimer);
    const query = searchInput.value.trim().slice(0, 120);
    if (query.length < 2) {
      if (searchStatus) searchStatus.textContent = "输入至少 2 个字符开始搜索";
      searchResults?.replaceChildren(); return;
    }
    if (searchStatus) searchStatus.textContent = "正在搜索…";
    searchTimer = setTimeout(() => ensureSearchWorker().postMessage({ type: "search", query }), 140);
  });

  function displayChapter(id) {
    return chapterById.get(String(id)) || { label: `Chapter ${id}`, pov: "", url: `${config.basePath}/` };
  }

  // Home catalog and continuation.
  document.querySelectorAll("[data-pov-filter]").forEach((button) => button.addEventListener("click", () => {
    document.querySelectorAll("[data-pov-filter]").forEach((item) => item.classList.toggle("is-active", item === button));
    const filter = button.dataset.povFilter;
    document.querySelectorAll("[data-pov]").forEach((card) => { card.hidden = filter !== "all" && card.dataset.pov !== filter; });
  }));

  function updateHome() {
    for (const card of document.querySelectorAll("[data-chapter-card]")) {
      const id = card.dataset.chapterCard;
      const progress = study.progress.chapters[id];
      const complete = study.completed.includes(id);
      const percent = complete ? 100 : Math.round(progress?.percent || 0);
      const bar = card.querySelector(".card-progress span");
      const status = card.querySelector(".card-status");
      if (bar) bar.style.width = `${percent}%`;
      if (status) status.textContent = complete ? "已读完" : percent ? `已读 ${percent}%` : "尚未开始";
    }
    const box = document.getElementById("continue-card");
    const last = study.progress.last;
    if (!box || !last) return;
    const chapter = displayChapter(last.chapterId);
    box.querySelector(".continue-label").textContent = `上次读到 · ${last.displayId || last.anchorId}`;
    box.querySelector("h3").textContent = `${chapter.label} — ${chapter.pov}`;
    box.querySelector("p").textContent = `阅读进度 ${Math.round(last.percent || 0)}% · 继续回到上次段落`;
    const link = box.querySelector("a"); link.href = `${chapter.url}#${last.anchorId}`; link.textContent = "继续阅读";
  }
  updateHome();
  addEventListener("agot:data-change", updateHome);

  // Chapter interactions.
  if (config.pageKind === "chapter" && config.currentChapter) {
    const chapterId = String(config.currentChapter);
    const chapter = displayChapter(chapterId);
    let activeAnchor = location.hash.slice(1) || document.querySelector(".paragraph-card")?.dataset.anchor || "";
    let progressTimer = null;

    function writeProgress() {
      const doc = document.documentElement;
      const max = Math.max(1, doc.scrollHeight - innerHeight);
      const percent = Math.max(0, Math.min(100, (scrollY / max) * 100));
      study.progress.chapters[chapterId] = { anchorId: activeAnchor, percent, updatedAt: now() };
      study.progress.last = { chapterId, anchorId: activeAnchor, displayId: activeAnchor.toUpperCase(), percent, updatedAt: now() };
      if (percent > 97 && !study.completed.includes(chapterId)) study.completed.push(chapterId);
      saveData(); updateChapterControls();
    }

    function updateChapterControls() {
      const progress = study.progress.chapters[chapterId]?.percent || 0;
      const bar = document.getElementById("reading-progress-bar");
      if (bar) bar.style.width = `${Math.round(progress)}%`;
      const complete = study.completed.includes(chapterId);
      const completeButton = document.getElementById("mark-complete");
      if (completeButton) completeButton.textContent = complete ? "✓ 已读完（点击撤销）" : "标记本章已读";
      const bookmarkSet = new Set(study.bookmarks.map((item) => `${item.chapterId}|${item.anchorId}`));
      document.querySelectorAll(".js-bookmark").forEach((button) => {
        const saved = bookmarkSet.has(`${chapterId}|${button.dataset.anchor}`);
        button.setAttribute("aria-pressed", String(saved)); button.firstChild.textContent = saved ? "★ " : "☆ ";
      });
      const vocabSet = new Set(study.vocabulary.map((item) => `${item.term.toLocaleLowerCase()}|${item.meaning}`));
      document.querySelectorAll(".js-vocab-save").forEach((button) => {
        const saved = vocabSet.has(`${button.dataset.term.toLocaleLowerCase()}|${button.dataset.meaning}`);
        button.classList.toggle("is-saved", saved); button.textContent = saved ? "✓ 已收藏" : "+ 收藏";
      });
    }

    addEventListener("scroll", () => {
      const doc = document.documentElement;
      const percent = Math.max(0, Math.min(100, scrollY / Math.max(1, doc.scrollHeight - innerHeight) * 100));
      const bar = document.getElementById("reading-progress-bar"); if (bar) bar.style.width = `${percent}%`;
      clearTimeout(progressTimer); progressTimer = setTimeout(writeProgress, 550);
    }, { passive: true });

    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
      if (!visible.length) return;
      activeAnchor = visible[0].target.dataset.anchor;
      document.querySelectorAll("[data-toc-anchor]").forEach((link) => link.classList.toggle("is-active", link.dataset.tocAnchor === activeAnchor));
    }, { rootMargin: "-15% 0px -72% 0px" });
    document.querySelectorAll(".paragraph-card").forEach((section) => observer.observe(section));

    document.querySelectorAll(".js-bookmark").forEach((button) => button.addEventListener("click", () => {
      const anchorId = button.dataset.anchor;
      const key = `${chapterId}|${anchorId}`;
      const index = study.bookmarks.findIndex((item) => `${item.chapterId}|${item.anchorId}` === key);
      if (index >= 0) study.bookmarks.splice(index, 1);
      else study.bookmarks.unshift({ chapterId, anchorId, displayId: anchorId.toUpperCase(), page: button.closest(".paragraph-card")?.querySelector(".page-pill")?.textContent || "", url: `${chapter.url}#${anchorId}`, createdAt: now() });
      saveData(); updateChapterControls();
    }));

    document.querySelectorAll(".js-copy-link").forEach((button) => button.addEventListener("click", async () => {
      const url = `${location.origin}${location.pathname}#${button.dataset.anchor}`;
      try { await navigator.clipboard.writeText(url); button.querySelector("span").textContent = "已复制"; }
      catch { prompt("复制这个段落链接：", url); }
    }));

    document.querySelectorAll(".js-vocab-save").forEach((button) => button.addEventListener("click", () => {
      const item = {
        term: button.dataset.term, pronunciation: button.dataset.pronunciation || "", pos: button.dataset.pos || "",
        meaning: button.dataset.meaning || "", chapterId, anchorId: button.dataset.anchor,
        url: `${chapter.url}#${button.dataset.anchor}`, createdAt: now(),
      };
      const key = `${item.term.toLocaleLowerCase()}|${item.meaning}`;
      const index = study.vocabulary.findIndex((value) => `${value.term.toLocaleLowerCase()}|${value.meaning}` === key);
      if (index >= 0) study.vocabulary.splice(index, 1); else study.vocabulary.unshift(item);
      saveData(); updateChapterControls();
    }));

    document.getElementById("mark-complete")?.addEventListener("click", () => {
      const index = study.completed.indexOf(chapterId);
      if (index >= 0) study.completed.splice(index, 1); else study.completed.push(chapterId);
      saveData(); updateChapterControls();
    });
    updateChapterControls();
    setTimeout(writeProgress, 800);
  }

  // Library rendering and versioned import/export.
  function renderLibrary() {
    if (config.pageKind !== "library") return;
    const progressList = document.getElementById("progress-list");
    const bookmarkList = document.getElementById("bookmark-list");
    const vocabularyList = document.getElementById("vocabulary-list");
    if (!progressList || !bookmarkList || !vocabularyList) return;
    progressList.replaceChildren(); bookmarkList.replaceChildren(); vocabularyList.replaceChildren();

    const progressItems = Object.entries(study.progress.chapters).sort((a, b) => String(b[1].updatedAt).localeCompare(String(a[1].updatedAt)));
    if (!progressItems.length) progressList.innerHTML = '<p class="empty-state">尚无阅读记录。</p>';
    for (const [id, progress] of progressItems) {
      const chapter = displayChapter(id); const item = document.createElement("article"); item.className = "study-item";
      const link = document.createElement("a"); link.href = `${chapter.url}#${progress.anchorId || ""}`;
      const strong = document.createElement("strong"); strong.textContent = `${chapter.label} — ${chapter.pov}`;
      const p = document.createElement("p"); p.textContent = `${Math.round(progress.percent || 0)}% · ${progress.anchorId?.toUpperCase() || "章节开头"}`;
      link.append(strong, p); const status = document.createElement("span"); status.textContent = study.completed.includes(id) ? "✓ 已读完" : "继续 →";
      item.append(link, status); progressList.append(item);
    }

    if (!study.bookmarks.length) bookmarkList.innerHTML = '<p class="empty-state">尚未收藏段落。</p>';
    for (const bookmark of study.bookmarks) {
      const chapter = displayChapter(bookmark.chapterId); const item = document.createElement("article"); item.className = "study-item";
      const link = document.createElement("a"); link.href = bookmark.url;
      const strong = document.createElement("strong"); strong.textContent = bookmark.displayId;
      const p = document.createElement("p"); p.textContent = `${chapter.label} — ${chapter.pov} · ${bookmark.page}`;
      link.append(strong, p); const remove = document.createElement("button"); remove.type = "button"; remove.textContent = "删除";
      remove.addEventListener("click", () => { study.bookmarks = study.bookmarks.filter((value) => !(value.chapterId === bookmark.chapterId && value.anchorId === bookmark.anchorId)); saveData(); });
      item.append(link, remove); bookmarkList.append(item);
    }

    if (!study.vocabulary.length) vocabularyList.innerHTML = '<p class="empty-state">尚未收藏词汇。</p>';
    for (const word of study.vocabulary) {
      const chapter = displayChapter(word.chapterId); const item = document.createElement("article"); item.className = "vocab-item";
      const link = document.createElement("a"); link.href = word.url;
      const strong = document.createElement("strong"); strong.textContent = `${word.term} ${word.pronunciation || ""}`.trim();
      const p = document.createElement("p"); p.textContent = `${word.pos ? word.pos + " · " : ""}${word.meaning} · ${chapter.label}`;
      link.append(strong, p); const remove = document.createElement("button"); remove.type = "button"; remove.textContent = "删除";
      remove.addEventListener("click", () => { const key = `${word.term.toLocaleLowerCase()}|${word.meaning}`; study.vocabulary = study.vocabulary.filter((value) => `${value.term.toLocaleLowerCase()}|${value.meaning}` !== key); saveData(); });
      item.append(link, remove); vocabularyList.append(item);
    }
  }
  renderLibrary();
  addEventListener("agot:data-change", renderLibrary);

  document.getElementById("export-data")?.addEventListener("click", () => {
    const payload = { version: 1, exportedAt: now(), progress: study.progress, completed: study.completed, bookmarks: study.bookmarks, vocabulary: study.vocabulary };
    const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
    const link = document.createElement("a"); link.href = URL.createObjectURL(blob); link.download = `agot-study-${new Date().toISOString().slice(0, 10)}.json`; link.click();
    setTimeout(() => URL.revokeObjectURL(link.href), 1000);
  });

  document.getElementById("import-data")?.addEventListener("change", async (event) => {
    const status = document.getElementById("import-status"); const file = event.target.files?.[0]; if (!file) return;
    try {
      const value = JSON.parse(await file.text());
      const imported = normalizeData(value);
      if (!imported) throw new Error("文件不是有效的 version 1 学习数据，或字段类型不正确");
      if (!confirm("导入会替换当前浏览器中的学习记录。继续吗？")) return;
      study = imported; saveData(); if (status) status.textContent = `已导入并去重：${imported.bookmarks.length} 个书签、${imported.vocabulary.length} 个词汇。`;
    } catch (error) { if (status) status.textContent = `导入失败：${error.message}`; }
    event.target.value = "";
  });

  document.getElementById("reset-data")?.addEventListener("click", () => {
    if (!confirm("确定清空当前浏览器中的全部阅读记录、书签和词汇吗？")) return;
    study = emptyData(); saveData(); const status = document.getElementById("import-status"); if (status) status.textContent = "本机学习数据已清空。";
  });
})();
