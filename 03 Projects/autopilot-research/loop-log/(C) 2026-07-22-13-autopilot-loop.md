# (C) Autopilot Loop — 2026-07-22-13

> **Trigger:** `/loop` (interactive) — operator: "Can I start build knowledge from this video [n97BCfyFIvw] with loop or anything in queue now?"
> **Topic:** engineer-of-the-future (Addy Osmani AIEWF-2026 keynote + 5-video role-under-AI-agents bundle)
> **Started:** 2026-07-22
> **Mode:** anchor + bundle (operator-elected via AskUserQuestion)

## Pre-flight

- **Queue state at start:** `topics-queue.md` had **0 pending topics** (only Completed section + hoidanit watch-note) — nothing to drain. Confirmed to operator; this run is a fresh Path-1 ingest, not a queue drain.
- **Collision check:** no existing coverage of Osmani / `n97BCfyFIvw` in `raw/` or `wiki/` → genuinely new topic.
- **Goal alignment:** dead-center on the corpus spine (harness/loop engineering, engineering role under agents) + Goal #2 (hireui governance).

## Source bundle (Path 1 `/loop` yt-dlp)

| # | ID | Speaker / Channel | Date | Len |
|---|---|---|---|---|
| ⭐ | `n97BCfyFIvw` | Addy Osmani / AI Engineer (AIEWF 2026) | 2026-07-14 | 18:26 |
| 2 | `LCEmiRjPEtQ` | Andrej Karpathy / Y Combinator | 2025-06-19 | 39:31 |
| 3 | `g8um2AEf5ZA` | Andrew Ng / DeepLearningAI (AI Dev 26) | 2026-05-20 | 19:21 |
| 4 | `8h9j2rskP14` | Michael Truell / Cursor | 2026-05-12 | 9:38 |
| 5 | `ubrfeaLEVVA` | Gergely Orosz / Sonar Summit 2026 | 2026-03-04 | 36:51 |
| 6 | `R9K2574YEAg` | Harrison Chase / LangChain (Interrupt 26) | 2026-05-21 | 22:10 |

- Fetch: `yt-dlp --write-auto-subs --write-subs --sub-langs "en.*" --cookies-from-browser chrome` — **all 6 clean, no 429/bot-gate** → `bin/vtt-to-md.py` → **~27.4K words, all read in full in the main loop.** NO NotebookLM.
- Raw capture: `raw/2026-07-22-engineer-of-the-future-osmani-aie-keynote-bundle.md`.

## Verification (maker/checker split)

- **Workflow `wf_dabc1f67-f9f`** — 15 refute-first claim-cluster verifiers (WebSearch/WebFetch, "default UNVERIFIABLE if thin") + 1 corpus-collision agent. **16 agents; 0 errors / 0 empty / 0 skipped; ~711K tokens; 253 tool calls; ~4.9 min; all Haiku 4.5.**
- Main-loop (Opus) authored all 15 articles from full transcript context, folding in verdicts.

## Wiki articles created (15 files, all NEW)

- `wiki/engineer-of-the-future/_index.md`
- `osmani-answerability-thesis` · `inner-loop-outer-loop` · `alpha-decay-and-taste` · `three-failure-modes`
- `karpathy-software-is-changing` · `andrew-ng-future-of-swe` · `cursor-tab-agent-teams` · `pragmatic-engineer-field-report` · `langchain-agent-futures`
- `convergent-thesis` · `hireui-relevance` · `claims-scorecard` · `caveats-and-corrections` · `source-provenance`
- Updated: `wiki/_master-index.md` (+1 topic, top) · `raw/_inventory.md` (+1 row +1 footer bullet) · `raw/topics-queue.md` (+1 Completed entry)

## Metric

- `gaps_at_start` = 1 (cold-start new topic) → `gaps_at_end` = 0 (index + all articles + cross-links complete; 14 cross-link targets verified present on disk, 0 dead links).
- **`gaps_closed_ratio` = 1.0** — target (0.5) reached.

## Scorecard

- **53 checkable claims: 29 CONFIRMED / 21 CORRECT-BUT-IMPRECISE / 1 MISLEADING / 2 UNVERIFIABLE / 0 FALSE / 0 FABRICATED.**
- 1 MISLEADING: "Cherny stopped opening IDE / Opus 4.5 wrote all his PRs" = actually Hamel Husain's quote (misattributed in Gergely's talk).
- 2 UNVERIFIABLE: Ng's "Fed Bank of Philadelphia study"; "Star Wars premiered at Cursor's office."
- Discard-as-garble guard honored: date-sensitive claims (Opus 4.5 / GPT-5.2 dates, Steinberger→OpenAI, GPT-Realtime-2) search-confirmed TRUE, not dismissed.

## Stop reason

- `gaps_closed_ratio` (1.0) ≥ target (0.5); single-topic interactive burst complete.

## Suggested next action

- **Commit on `autopilot-research` branch (done in this run); operator merges to main when ready** (per standing rule — branch wikis, don't auto-merge).
- **hireui follow-through:** fold the **"answerability record"** shape (evidence + understanding + recruiter verdict) into the Match-Explain spec, and cite `engineer-of-the-future/hireui-relevance` alongside the EU AI Act when defending the candidate-LLM legibility ADR. This is the strongest first-principles backing the ADR has received.
- Optional DEEPEN later: Dex Horthy's "Why Software Factories Fail" talk (the counter-view Osmani references) would sharpen the autonomy-optimism-vs-caution tension in `convergent-thesis`.
