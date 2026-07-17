# Autopilot loop — 2026-07-17 (interactive)

- **Trigger:** operator-submitted anchor URL (interactive `/loop`-style burst; not the nightly queue — queue was empty at 00:12 today).
- **Topic:** NEW — `data-structures-16-in-32-min`
- **Source:** https://www.youtube.com/watch?v=uHpzKcm8qh0 — Học Giải Thuật Cùng HPN, "Tất Tần Tật Về Cấu Trúc Dữ Liệu Trong 32 Phút" (2026-07-12, 32:22, ~15K views, VN)
- **Ingest path:** 5 (yt-dlp `vi-orig` auto-subs → deduped ~27KB clean transcript → read in full in main loop; `notebook_id: none`)

## What ran

1. `yt-dlp` metadata + `vi-orig`/`vi` VTT subtitle pull → dedup clean (venv python; broken `python3` shim routed to `.venv/bin/python`).
2. Full VN transcript read in main loop → 16-structure content understood.
3. Collision check (grep + ls): **no pre-existing data-structures/algorithms topic** — genuinely new (prior "skip-list"/"bloom-filter" hits = incidental metaphors in unrelated pilot docs).
4. Adversarial verification Workflow `wf_83c9b13a-5b9` — **10 agents** (6 refute-first WebSearch fact-check clusters + corpus-xref librarian + CS-history nuance-hunter + educational appraisal + completeness critic); ~377.6K tokens, 88 tool calls, **0 errors / 0 empty / 0 skipped**; all Haiku 4.5.
5. Main-loop synthesis of 20 wiki files; ASR-garble correction; honest re-grading of corpus-xref cross-link verdicts (thematic vs. content).

## Verification result

- **Scorecard (24 checkable claims): 22 CONFIRMED · 1 ANECDOTAL · 1 CORRECT-BUT-INCOMPLETE · 0 MISLEADING · 0 FALSE · 0 FABRICATED.**
- One of the highest-integrity sources in the corpus — a well-researched CS-history explainer.
- ANECDOTAL: red-black "laser printer" (Sedgewick's account) vs. Guibas's "the pens we had" — contested.
- CORRECT-BUT-INCOMPLETE: DFS "Lucas 1883" ~1yr off (Récréations Mathématiques vol.1 = 1882); Tarry 1895 exact (captions garble "Tarry"→"Cherry").
- ~20 ASR proper-name garbles corrected (Bman→Bachmann, Chargen→Tarjan, Crossco→Kruskal, etc.).

## Metric Δ

- **Topics:** 61 → **62** (+1 NEW).
- **Scope this cycle:** 1/1 sources compiled = **100%**.
- **Files added:** 20 wiki files (`wiki/data-structures-16-in-32-min/`) + 1 raw (`raw/2026-07-17-data-structures-16-in-32-min.md`).
- **Corpus firsts:** first pure CS-fundamentals topic; 2nd non-Claude/non-agent topic (after `self-hosted-devops-oss`).

## Librarian bookkeeping

- ✅ `wiki/_master-index.md` — new entry added (newest-first, above quanit).
- ✅ topic `_index.md` — created (20-file listing + honest cross-link grading).
- ✅ `raw/_inventory.md` — row appended (Status: compiled).
- ✅ `[[wiki links]]` — cross-links throughout; content link = graphify-codebase-graph; thematic = Pocock/Quân-IT/system-thinking.

## Flags (fail-loud)

- ⚠️ **Coverage gap (pre-existing, NOT fixed):** this worktree's `raw/_inventory.md` lags its `wiki/_master-index.md` by ~10 topics (okf / adaptive-engineering / pocock-writing-great-skills / miai-iphone-ocr-server / codesistency / scroll-world / etc. are in the master-index but were never appended to the inventory). Out of scope for this ship — flagged for an inventory-reconciliation pass.
- **No git commit made** — work staged in the working tree on branch `autopilot-research`, left for operator review/commit per harness policy.

## Next action

- Operator: review the 20 files (start at `wiki/data-structures-16-in-32-min/_index.md`), then commit (suggested message: `autopilot-research: NEW topic data-structures-16-in-32-min`). Optionally run an inventory-reconciliation pass to close the coverage gap above.
