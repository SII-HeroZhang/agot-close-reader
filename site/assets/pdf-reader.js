(() => {
  "use strict";

  const config = window.AGOT_CONFIG || { basePath: "", pageKind: "" };
  const DB_NAME = "agot-local-pdf";
  const STORE_NAME = "files";
  const PDF_KEY = "primary";
  const MAX_PAGE = 755;
  const HOSTED_PDF_URL = `${config.basePath}/assets/agot-original.pdf`;
  const HOSTED_PDF = { name: "A Game of Thrones · 站内 PDF", size: 4921287, hosted: true };
  const input = document.getElementById("pdf-file-input");
  const dialog = document.getElementById("pdf-dialog");
  const companion = document.getElementById("pdf-companion-content");
  let pdfRecord = HOSTED_PDF;
  let pdfUrl = HOSTED_PDF_URL;
  let pageMapPromise = null;

  function clampPage(value) {
    return Math.max(1, Math.min(MAX_PAGE, Number.parseInt(value, 10) || 1));
  }

  function openDatabase() {
    return new Promise((resolve, reject) => {
      if (!("indexedDB" in window)) { reject(new Error("当前浏览器不支持 IndexedDB")); return; }
      const request = indexedDB.open(DB_NAME, 1);
      request.onupgradeneeded = () => {
        const db = request.result;
        if (!db.objectStoreNames.contains(STORE_NAME)) db.createObjectStore(STORE_NAME);
      };
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error || new Error("无法打开本地 PDF 存储"));
    });
  }

  async function readStoredPdf() {
    const db = await openDatabase();
    return new Promise((resolve, reject) => {
      const request = db.transaction(STORE_NAME, "readonly").objectStore(STORE_NAME).get(PDF_KEY);
      request.onsuccess = () => { db.close(); resolve(request.result || null); };
      request.onerror = () => { db.close(); reject(request.error); };
    });
  }

  async function storePdf(record) {
    const db = await openDatabase();
    return new Promise((resolve, reject) => {
      const transaction = db.transaction(STORE_NAME, "readwrite");
      transaction.objectStore(STORE_NAME).put(record, PDF_KEY);
      transaction.oncomplete = () => { db.close(); resolve(); };
      transaction.onerror = () => { db.close(); reject(transaction.error); };
    });
  }

  async function removeStoredPdf() {
    const db = await openDatabase();
    return new Promise((resolve, reject) => {
      const transaction = db.transaction(STORE_NAME, "readwrite");
      transaction.objectStore(STORE_NAME).delete(PDF_KEY);
      transaction.oncomplete = () => { db.close(); resolve(); };
      transaction.onerror = () => { db.close(); reject(transaction.error); };
    });
  }

  function formatSize(bytes) {
    return `${(bytes / 1024 / 1024).toFixed(1)} MB`;
  }

  function pageUrl(page) {
    return pdfUrl ? `${pdfUrl}#page=${clampPage(page)}&view=FitH` : "";
  }

  function updateViewer(viewer, page) {
    const frame = viewer.querySelector(".js-pdf-frame");
    const openTab = viewer.querySelector(".js-pdf-open-tab");
    const targetPage = clampPage(page || frame?.dataset.pdfPage || 1);
    if (frame) frame.dataset.pdfPage = String(targetPage);
    viewer.classList.toggle("has-pdf", Boolean(pdfUrl));
    if (!pdfUrl) {
      if (frame) frame.removeAttribute("src");
      if (openTab) openTab.removeAttribute("href");
      return;
    }
    const url = pageUrl(targetPage);
    if (frame && frame.src !== url) frame.src = url;
    if (openTab) openTab.href = url;
  }

  function refreshViewers() {
    document.querySelectorAll("[data-pdf-viewer]").forEach((viewer) => {
      if (viewer.closest("#pdf-dialog") && !dialog?.open) return;
      updateViewer(viewer, viewer.querySelector(".js-pdf-frame")?.dataset.pdfPage);
    });
  }

  function updateFileUi(message = "") {
    const label = pdfRecord ? `${pdfRecord.name} · ${formatSize(pdfRecord.size)}` : "尚未选择 PDF";
    document.querySelectorAll(".js-pdf-file-status").forEach((node) => { node.textContent = message || label; });
    document.querySelectorAll(".js-remove-pdf").forEach((button) => { button.hidden = !pdfRecord?.blob; });
    refreshViewers();
  }

  function activatePdf(record, message = "") {
    if (pdfUrl.startsWith("blob:")) URL.revokeObjectURL(pdfUrl);
    pdfRecord = record?.blob ? record : HOSTED_PDF;
    pdfUrl = record?.blob ? URL.createObjectURL(record.blob) : HOSTED_PDF_URL;
    updateFileUi(message);
  }

  async function selectPdf(file) {
    if (!file || !(/\.pdf$/i.test(file.name) || file.type === "application/pdf")) {
      updateFileUi("请选择有效的 PDF 文件"); return;
    }
    const record = { name: file.name, size: file.size, type: file.type || "application/pdf", lastModified: file.lastModified, blob: file };
    activatePdf(record, `${file.name} · 正在保存到当前浏览器…`);
    try {
      await storePdf(record);
      updateFileUi(`${file.name} · ${formatSize(file.size)} · 已保存在当前浏览器`);
      navigator.storage?.persist?.().catch(() => {});
    } catch {
      updateFileUi(`${file.name} · 仅在本次页面会话中可用`);
    }
  }

  function cardForButton(button) {
    const direct = button.closest(".paragraph-card");
    if (direct) return direct;
    const hashAnchor = location.hash.slice(1);
    if (hashAnchor) {
      const match = [...document.querySelectorAll(".paragraph-card")].find((card) => card.dataset.anchor === hashAnchor);
      if (match) return match;
    }
    return document.querySelector(".paragraph-card");
  }

  function cloneCompanion(card) {
    if (!companion) return;
    companion.replaceChildren();
    if (!card) {
      const note = document.createElement("p"); note.className = "empty-state";
      note.textContent = "当前页没有选中的精读段落。可以在右侧章节内容中点击具体的 PDF 页码。";
      companion.append(note); return;
    }
    const clone = card.cloneNode(true);
    clone.classList.add("pdf-cloned-card");
    clone.removeAttribute("data-anchor"); clone.removeAttribute("data-chapter");
    clone.querySelectorAll("[id]").forEach((node) => node.removeAttribute("id"));
    clone.querySelectorAll(".paragraph-tools, hr").forEach((node) => node.remove());
    clone.querySelectorAll(".js-vocab-save").forEach((button) => button.closest("td")?.remove());
    clone.querySelectorAll("th").forEach((cell) => { if (cell.textContent.trim() === "收藏") cell.remove(); });
    clone.querySelectorAll("p").forEach((paragraph) => {
      const text = paragraph.textContent.replace(/\s+/g, " ").trim();
      if (!text || text.startsWith("来源：")) paragraph.remove();
    });
    const vocabLabel = [...clone.querySelectorAll("p")].find((paragraph) => paragraph.textContent.trim() === "难词与短语");
    const vocabTable = vocabLabel?.nextElementSibling?.tagName === "TABLE" ? vocabLabel.nextElementSibling : null;
    if (vocabLabel && vocabTable) {
      const details = document.createElement("details"); details.className = "pdf-vocab-details";
      const summary = document.createElement("summary"); summary.textContent = "难词与短语";
      vocabLabel.replaceWith(details); details.append(summary, vocabTable);
    }
    companion.append(clone);
    companion.parentElement?.scrollTo({ top: 0, behavior: "auto" });
  }

  function openPdfDialog(button) {
    if (!dialog) return;
    const page = clampPage(button.dataset.pdfPage || 1);
    const frame = dialog.querySelector(".js-pdf-frame");
    if (frame) frame.dataset.pdfPage = String(page);
    dialog.querySelectorAll(".js-pdf-page-label").forEach((node) => { node.textContent = `PDF p.${page}`; });
    cloneCompanion(cardForButton(button));
    updateViewer(dialog.querySelector("[data-pdf-viewer]"), page);
    if (!dialog.open) dialog.showModal();
  }

  document.querySelectorAll(".js-select-pdf").forEach((button) => button.addEventListener("click", () => input?.click()));
  input?.addEventListener("change", async () => {
    const file = input.files?.[0]; input.value = "";
    if (file) await selectPdf(file);
  });
  document.querySelectorAll(".js-remove-pdf").forEach((button) => button.addEventListener("click", async () => {
    if (!confirm("从当前浏览器移除已保存的 PDF？精读笔记和学习进度不会受影响。")) return;
    activatePdf(null, "已恢复使用站内 PDF");
    try { await removeStoredPdf(); } catch { /* Nothing else to remove. */ }
  }));
  document.querySelectorAll(".js-open-pdf").forEach((button) => button.addEventListener("click", () => openPdfDialog(button)));
  dialog?.querySelector(".js-close-pdf")?.addEventListener("click", () => dialog.close());

  async function loadPageMap() {
    if (!pageMapPromise) {
      pageMapPromise = fetch(`${config.basePath}/data/page-map.json`).then((response) => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
      });
    }
    return pageMapPromise;
  }

  function excerpt(value, length) {
    const clean = String(value || "").replace(/\s+/g, " ").trim();
    return clean.length > length ? `${clean.slice(0, length).trim()}…` : clean;
  }

  async function renderPageNotes(page) {
    const box = document.getElementById("pdf-page-results");
    if (!box) return;
    box.innerHTML = '<p class="empty-state">正在载入本页解读…</p>';
    try {
      const pageMap = await loadPageMap();
      const rows = pageMap[String(page)] || [];
      box.replaceChildren();
      if (!rows.length) {
        const empty = document.createElement("p"); empty.className = "empty-state";
        empty.textContent = page < 6 || page > 731 ? "这一页不在 Prologue–Chapter 72 的精读范围内。" : "这一页没有正文段落，可能是章节导航页或留白页。";
        box.append(empty); return;
      }
      for (const row of rows) {
        const link = document.createElement("a"); link.className = "pdf-note-card"; link.href = row.url;
        const meta = document.createElement("div"); meta.className = "pdf-note-meta";
        const location = document.createElement("span"); location.textContent = `${row.chapterLabel} · ${row.pov}`;
        const id = document.createElement("span"); id.textContent = row.continued ? `${row.displayId} · 承接 p.${row.startPage}` : row.displayId;
        meta.append(location, id);
        const original = document.createElement("strong"); original.textContent = excerpt(row.original, 180);
        const summary = document.createElement("p"); summary.textContent = excerpt(row.summary, 240);
        link.append(meta, original, summary); box.append(link);
      }
    } catch (error) {
      box.replaceChildren();
      const failure = document.createElement("p"); failure.className = "empty-state";
      failure.textContent = `页码索引载入失败：${error.message}`;
      box.append(failure);
    }
  }

  function setReaderPage(value, updateUrl = true) {
    const page = clampPage(value);
    const pageInput = document.getElementById("pdf-page-input");
    if (pageInput) pageInput.value = String(page);
    const label = document.getElementById("pdf-reader-page-label");
    if (label) label.textContent = `PDF p.${page}`;
    const viewer = document.querySelector(".pdf-reader-viewer[data-pdf-viewer]");
    const frame = viewer?.querySelector(".js-pdf-frame");
    if (frame) frame.dataset.pdfPage = String(page);
    if (viewer) updateViewer(viewer, page);
    renderPageNotes(page);
    if (updateUrl) {
      const url = new URL(location.href); url.searchParams.set("page", String(page));
      history.replaceState(null, "", url);
    }
  }

  if (config.pageKind === "pdf") {
    const initialPage = clampPage(new URL(location.href).searchParams.get("page") || 6);
    setReaderPage(initialPage, false);
    document.getElementById("pdf-page-form")?.addEventListener("submit", (event) => {
      event.preventDefault(); setReaderPage(document.getElementById("pdf-page-input")?.value || 1);
    });
    document.querySelectorAll("[data-pdf-step]").forEach((button) => button.addEventListener("click", () => {
      const current = Number(document.getElementById("pdf-page-input")?.value || 1);
      setReaderPage(current + Number(button.dataset.pdfStep));
    }));
    document.addEventListener("keydown", (event) => {
      if (!event.altKey || !["ArrowLeft", "ArrowRight"].includes(event.key)) return;
      event.preventDefault();
      const current = Number(document.getElementById("pdf-page-input")?.value || 1);
      setReaderPage(current + (event.key === "ArrowRight" ? 1 : -1));
    });
  }

  readStoredPdf().then((record) => { if (record?.blob) activatePdf(record); else activatePdf(null); }).catch(() => activatePdf(null));
  addEventListener("beforeunload", () => { if (pdfUrl.startsWith("blob:")) URL.revokeObjectURL(pdfUrl); });
})();
