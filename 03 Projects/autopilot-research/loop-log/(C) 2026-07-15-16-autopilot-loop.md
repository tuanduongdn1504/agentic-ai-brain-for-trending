# (C) Autopilot Loop — 2026-07-15-16

> **Trigger:** /loop (interactive, operator-submitted single video)
> **Topic:** okf-open-knowledge-format
> **Started:** 2026-07-15 ~16:05 +07
> **Ended:** 2026-07-15 ~16:35 +07
> **Duration:** ~30m (main-loop direct-write; 1 background verification workflow ~3m)

## Trigger detail

Operator asked to "start build knowledge from other video" and submitted `https://www.youtube.com/watch?v=T33iI6izAKw` — Cole Medin, *"Finally, an Open Standard for the Karpathy LLM Wiki is HERE"* (19:37, 2026-07-02, ~59K views). Queue had 0 pending topics; this is a path-5 single-video ingest.

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 (cold-start, NEW topic) | 1 (yt-dlp captions) | 1 | 0 | 1.0 |

New topic `okf-open-knowledge-format` did not exist at start (gaps_at_start = 1). Compiled to 10 articles, no stubs, no `(TODO)`/`(gap)` markers → gaps_at_end = 0. **gaps_closed_ratio = 1.0.**

## Sources ingested

- `raw/2026-07-15-okf-open-knowledge-format.md` — YAML header + full description + deduped 43-paragraph transcript (yt-dlp EN auto-subs → `bin/vtt-to-md.py`). Read in full in main loop.

## Verification

- Workflow `wf_a8b95e41-6b3` — 8 agents (4 fact-check clusters + corpus-xref + thesis-critique + pilot-design + completeness-critic); ~392K tokens, 56 tool calls, 0 errors, 0 empty; all Haiku 4.5 (per-agent sonnet/opus overrides silently ignored by the runtime — flagged in source-provenance).
- Main-loop Opus ground-checks (before compile): `gh api` on both repos; WebFetch on OKF SPEC.md + launch blog + Karpathy gist; WebSearch for gist star count + GPT-5.5/Opus-4.8 reality. Caught the 40K→5K star error pre-compile.
- **Scorecard: 11 CONFIRMED / 5 MISLEADING / 2 FALSE / 0 FABRICATED / 2 OPINION** (20 checkable claims).

## Wiki articles created/updated

- `wiki/okf-open-knowledge-format/_index.md` (NEW)
- `wiki/okf-open-knowledge-format/overview.md` (NEW)
- `wiki/okf-open-knowledge-format/what-okf-standardizes.md` (NEW)
- `wiki/okf-open-knowledge-format/personal-vs-enterprise-framing.md` (NEW)
- `wiki/okf-open-knowledge-format/claims-scorecard.md` (NEW)
- `wiki/okf-open-knowledge-format/caveats-and-corrections.md` (NEW)
- `wiki/okf-open-knowledge-format/thesis-critique.md` (NEW)
- `wiki/okf-open-knowledge-format/vault-adoption-pilot.md` (NEW)
- `wiki/okf-open-knowledge-format/vs-karpathy-and-corpus.md` (NEW)
- `wiki/okf-open-knowledge-format/source-provenance.md` (NEW)
- `wiki/_master-index.md` (UPDATED — new top entry)
- `raw/_inventory.md` (UPDATED — new top table row)
- Operator memory: `project_okf_open_knowledge_format_pilot_thread.md` (NEW) + `MEMORY.md` index (UPDATED)

## Final metric

- `gaps_closed_ratio` = 1.0
- Stop reason: single-video ingest fully compiled; no unprocessed sources remain.

## Top-3 open items (not gaps — follow-ups)

1. The bundle-consumption "prompt" Cole references [12:04] wasn't shown in the video or located in the bundle README — flagged in caveats.
2. OKF real-world adoption footprint (public bundles, native consumers) not measured — the "WATCH" pilot verdict rests partly on it being early.
3. `samples/` dir in the OKF repo not reviewed — would test cross-domain adoption ease.

## Suggested next action

Run the **40-minute OKF experiment** from `vault-adoption-pilot.md` (OKF-ify one topic → query with a fresh agent → gate on friction) — **after** cc-sdd pilots. Separately: the operator's `MEMORY.md` index is ~20KB (nearing the 24.4KB read limit) — consider `/consolidate-memory`.
