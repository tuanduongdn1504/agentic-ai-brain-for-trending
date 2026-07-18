# (C) Autopilot Loop — 2026-07-18-09

> **Trigger:** /loop (manual, operator-submitted URL)
> **Topic:** copywriting-11h-course
> **Source:** https://www.youtube.com/watch?v=zuIudgESKDk — Trương Phương, "Khoá Học Copywriting 11 Tiếng Cho Người Mới | Từ 0 Đến $1.000/Tháng Thực Chiến (MIỄN PHÍ)" (11:20:22, Vietnamese, uploaded 2026-07-07, ~32.6K views)
> **Started:** 2026-07-18 ~09:19 ICT
> **Ended:** 2026-07-18 ~10:2x ICT
> **Duration:** ~65 min main-loop (incl. one 17-min background verification workflow)

## Pre-flight notes

- **Off-corpus-theme flag raised before ingesting.** All 65 prior topics are AI/agent/dev-tooling; this is a copywriting/marketing-skills course. Flagged the fit + the 11h/148K-word scale to the operator; operator chose **"full multi-article vertical."** No silent assumption.
- **Scale-driven deviation from the standard pipeline:** at 147,904 words the transcript was **too large for a NotebookLM bundle** (`notebook_id: none`). Pulled `vi` captions via yt-dlp, cleaned (dedupe rolling captions) to 16,864 lines, split into 12 chunks, and analysed directly via a Workflow.

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 (11h video → 148K-word transcript) | 1 (topic is a gap) | 0 (17-file topic created) | ~1.0 |

## Sources ingested

- `raw/2026-07-18-copywriting-11h-course.md` (path 1 /loop yt-dlp; full transcript in scratchpad; `notebook_id: none`)

## Analysis workflow

- **`wf_1fc6cda8-8bf`** — 50 agents (12 digest → 1 synthesise → 24 refute-first verify → 13 draft); 0 errors / 0 empty / 0 skipped; ~2.84M tokens; 362 tool calls; ~17 min.
- **Main-loop follow-up:** 3 draft agents came back as under-developed stubs with mangled slugs → re-drafted to depth; 6 invalid `[[wikilinks]]` fixed; corpus-first verified by grep; the 60,000× line corrected; 3 meta-articles (scorecard/caveats/provenance) + `_index` built in the main loop from the structured verification/garble data.

## Wiki articles created (17, NEW topic)

`wiki/copywriting-11h-course/`: `_index` + overview + what-is-copywriting-core-definition + psychology-persuasion-five-stages + hooks-curiosity-loops-five-formulas + storytelling-golden-structure-6-point + core-email-templates-pas-bab-educational + writing-process-research-draft-80-percent-edit + email-marketing-owned-asset-vs-ads + customer-acquisition-niche-selection-lead-magnets-outreach + monetization-roadmap-0-to-1000-per-month + deliberate-practice-common-mistakes-mental-resilience + critical-appraisal + hireui-relevance + claims-scorecard + caveats-and-corrections + source-provenance.

`wiki/_master-index.md` UPDATED (new topic prepended; 65→66). `raw/_inventory.md` UPDATED (row + change-log bullet).

## Verification result

- **24 claims: 3 CONFIRMED · 7 CORRECT-BUT-INCOMPLETE · 4 MISLEADING · 1 FALSE · 9 UNVERIFIABLE · 0 FABRICATED; 19/24 (79%) marketing hype.**
- Profile: **a sound skills course wrapped in an income-promise sales pitch.** The craft (frameworks, process, psychology, templates) is legitimate; the evidence used to sell the outcome (income testimonials, inflated benchmarks, one debunked stat) is not.
- 1 FALSE (60,000× image myth); 2 extraction distortions caught + corrected (the "Zara" story = instructor's own; Dan Henry over-reach).

## Final metric

- `gaps_closed_ratio` = **~1.0** (cold-start topic fully created).
- **Stop reason:** single-source topic complete (Phase 6 condition 5 — no more unprocessed sources; target ratio met).

## Suggested next action

- **Operator merges `autopilot-research` → `main`** when ready (not auto-merged, per standing rule).
- Optional: if this is the start of a real copywriting/marketing vertical, queue a second source (e.g. an English copywriting reference) so the topic isn't single-source; otherwise leave as a standalone.
- hireui: the concrete borrow is a **human-authored, audited job-ad + outreach template library** with copywriting structure (PAS/BAB/hooks) — deterministic, ADR-safe, no LLM in the candidate-facing path. See `wiki/copywriting-11h-course/hireui-relevance.md`.
