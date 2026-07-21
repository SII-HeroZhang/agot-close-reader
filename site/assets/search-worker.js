let recordsPromise;

function normalize(value) {
  return String(value || "").normalize("NFKC").toLocaleLowerCase().replace(/\s+/g, " ").trim();
}

function loadRecords() {
  if (!recordsPromise) {
    recordsPromise = fetch(new URL("../data/search-index.json", self.location.href))
      .then((response) => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
      })
      .then((records) => {
        for (const row of records) {
          row._fields = [row.original, row.summary, row.vocab, row.note, row.background].map(normalize);
        }
        postMessage({ type: "ready", count: records.length });
        return records;
      });
  }
  return recordsPromise;
}

function scoreRecord(row, query, tokens) {
  const weights = [60, 48, 44, 30, 24];
  let score = 0;
  let matched = 0;
  row._fields.forEach((field, index) => {
    if (!field) return;
    const exact = field.indexOf(query);
    if (exact >= 0) score += weights[index] + Math.max(0, 16 - exact / 100);
    let fieldMatched = 0;
    for (const token of tokens) {
      if (field.includes(token)) fieldMatched += 1;
    }
    if (fieldMatched === tokens.length) matched = Math.max(matched, fieldMatched);
    score += fieldMatched * (weights[index] / 8);
  });
  return matched === tokens.length ? score : 0;
}

function makeSnippet(row, query) {
  const choices = [row.summary, row.original, row.vocab, row.note, row.background].filter(Boolean);
  let text = choices.find((value) => normalize(value).includes(query)) || choices[0] || "";
  text = text.replace(/\s+/g, " ").trim();
  const index = normalize(text).indexOf(query);
  const start = Math.max(0, index > 80 ? index - 70 : 0);
  const slice = text.slice(start, start + 220);
  return `${start ? "…" : ""}${slice}${start + 220 < text.length ? "…" : ""}`;
}

self.addEventListener("message", async ({ data }) => {
  if (data?.type !== "search") return;
  const rawQuery = String(data.query || "").trim().slice(0, 120);
  const query = normalize(rawQuery);
  if (query.length < 2) return postMessage({ type: "results", query: rawQuery, total: 0, results: [] });
  try {
    const records = await loadRecords();
    const tokens = query.split(" ").filter(Boolean);
    const scored = [];
    for (const row of records) {
      const score = scoreRecord(row, query, tokens);
      if (score > 0) scored.push({ row, score });
    }
    scored.sort((a, b) => b.score - a.score || a.row.pdfPage - b.row.pdfPage);
    const results = scored.slice(0, 50).map(({ row }) => ({
      chapterLabel: row.chapterLabel, pov: row.pov, displayId: row.displayId, pdfPage: row.pdfPage,
      url: row.url, title: row.summary || row.original.slice(0, 100), snippet: makeSnippet(row, query),
    }));
    postMessage({ type: "results", query: rawQuery, total: scored.length, results });
  } catch (error) {
    postMessage({ type: "error", message: error instanceof Error ? error.message : String(error) });
  }
});
