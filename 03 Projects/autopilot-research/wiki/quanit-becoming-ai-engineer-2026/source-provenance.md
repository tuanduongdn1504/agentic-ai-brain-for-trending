# Source provenance

## Video

| Field | Value |
|-------|-------|
| Title | "Becoming An AI engineer in 2026" |
| Video ID | [`RcF6ofU2nLs`](https://www.youtube.com/watch?v=RcF6ofU2nLs) |
| Creator | Quân IT (Vietnamese practitioner-YouTuber; AI-skeptic/anti-hype commentary; hotel/restaurant-IT background) |
| Uploaded | 2026-07-15 |
| Duration | 19:23 |
| Views at ingest | ~2,167 |
| Language | Vietnamese |

## Ingest pipeline (path 1 — /loop, operator-submitted single video)

1. `yt-dlp --write-auto-subs --sub-langs vi-orig` → `cap.vi-orig.vtt` (202 KB). *(The `en` auto-translate track did not serve on this run; not needed — VN original read directly, no MT layer.)*
2. `bin/vtt-to-md.py` → deduped, word-timing-tags stripped → **483 cue lines / 41 timestamped paragraphs.**
3. Raw file: `raw/2026-07-16-quanit-becoming-ai-engineer-2026.md` (front-matter + full VN transcript). Read **in full** in the main loop.
4. **No NotebookLM** (`notebook_id: none`) — the modern caption pipeline, per the July-2026 corpus norm.

## Verification

- **Workflow `wf_0f3ff851-bd2`** — 10 agents (Haiku 4.5), 0 errors, 0 empty, ~396K tokens, 86 tool calls, ~4.9 min:
  - 3 refute-first fact-check clusters (models-companies / tech-protocols / products-incidents) → each independently re-checked by a second refute pass (maker/checker).
  - `corpus-xref` (general-purpose agent) — grep/ls-verified which candidate cross-links actually exist.
  - `thesis-critique` + `pilot-design` + `completeness-critic`.
- **Main-loop cross-checks:** independent `ls` of all 17 candidate cross-link targets (16 exist, `career-ops` absent — confirmed the xref agent); stripped agent-introduced errors (fabricated `vNNN` version numbers; unverified "Ryan Lopopolo" authorship) per the wiki-verify discipline.
- **Scorecard:** 8 CONFIRMED / 1 MISLEADING / 0 FALSE / 0 FABRICATED / 1 UNVERIFIABLE (10 claims). Details: [[quanit-becoming-ai-engineer-2026/claims-scorecard|claims-scorecard]].

## Deliverables

- Wiki: `wiki/quanit-becoming-ai-engineer-2026/` — 12 files (this + 11).
- Pilot methods: `output/(C) 2026-07-16-quanit-becoming-ai-engineer-2026-pilot-methods.md`.
- Loop log: `loop-log/(C) 2026-07-16-00-autopilot-quanit-ai-engineer.md`.
- Inventory row: `raw/_inventory.md` (Status → compiled at ship).

## Cross-links (all verified to exist as local `wiki/<slug>/_index.md`)

[[ai-engineering/_index]] · [[pocock-software-fundamentals/_index]] · [[adaptive-engineering-beyond-harness/_index]] · [[harness-engineering/_index]] · [[system-thinking-ai-coding/_index]] · [[hoidanit-fullstack-vibe-coding/_index]] · [[agent-memory-architecture/_index]] · [[claude-code-memory-systems/_index]] · [[multi-agent-orchestration/_index]] · [[prompt-evaluation/_index]] · [[api-security-7-techniques/_index]] · [[miai-cv-matching-agent/_index]] · [[mosh-ai-powered-apps/_index]] · [[codesistency-mobile-app-course/_index]] · [[jsm-practical-vibe-coding/_index]] · [[pocock-agentic-workflow/_index]]

External (Storm Bear curated vault, not a local topic): [[external|Storm Bear: career-ops]].

## Key Takeaways

- **Clean provenance:** VN-original captions read directly, no NotebookLM, full transcript in-loop, adversarially verified, cross-links ground-truthed.
- **Notable:** 2nd VN-practitioner career piece (with [[hoidanit-fullstack-vibe-coding/_index]]); no corpus collision — a genuinely new topic with a large, verified integration surface.
