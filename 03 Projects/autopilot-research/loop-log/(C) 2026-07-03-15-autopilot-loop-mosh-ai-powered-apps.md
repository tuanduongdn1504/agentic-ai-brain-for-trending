# (C) Autopilot Loop — 2026-07-03-15 — mosh-ai-powered-apps

> **Trigger:** operator-submitted URL (path 5) — "build knowledge from this video + double deep dive into the original resource + pilot methods"
> **Topic:** mosh-ai-powered-apps (NEW)
> **Started:** 2026-07-03T15:30+07:00
> **Ended:** 2026-07-03T16:05+07:00 (approx)
> **Duration:** ~35m main-loop + ~6.5m background workflow

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 video + 2 originals (course page + repo) + 4 doc ground-checks | 1 (cold-start topic) | 0 | 1.0 |

## Sources ingested

- yt-dlp: PtETUYa3i2Q metadata + EN auto-captions → ~22.9K-word transcript (scratchpad; read in main loop + 4 workflow chunk-readers)
- WebFetch/gh (via workflow `wf_05723834-938`, 28 agents, ~1.15M tokens, 438 tool calls): codewithmosh.com course + pricing pages, mosh-hamedani/ai-powered-apps-course (file-level), OpenAI docs (models/conversation-state/token-counting), tiktoken repos, author verification
- Main-loop ground-checks: OpenAI conversation-state guide, Amazon AI-review-highlights announcement, claude-api skill reference

## Wiki articles created/updated

- wiki/mosh-ai-powered-apps/ — 12 NEW: _index, overview, ai-engineering-foundations, tokens-and-cost, choosing-models-and-settings, calling-models-responses-api, fullstack-scaffold-bun-monorepo, chatbot-validation-and-errors, layered-architecture-refactor, the-originals, openai-to-claude-mapping, caveats-and-corrections, source-provenance
- wiki/_master-index.md — UPDATED (new topic section)
- raw/_inventory.md — UPDATED (+1 row)
- output/(C) 2026-07-03-mosh-ai-powered-apps-pilot-methods.md — NEW (pilot menu)

## Final metric

- `gaps_closed_ratio` = 1.0 (cold-start topic fully compiled)
- Stop reason: single-topic operator request complete

## Verification headline

28-agent adversarial workflow + 5 main-loop overrides of verifier misfires (incl. a NEW misfire class: refuting **retired-but-real** items from current docs — inverse of the usual post-cutoff misfire). 2 verifier deaths ("Prompt is too long") closed by operator knowledge. Full log: wiki/mosh-ai-powered-apps/source-provenance.md

## Top-3 unclosed gaps

1. Paid-course sections (prompt engineering / review summarizer / Ollama) known only via section titles + repo code — a repo-code deep-read of the review summarizer would fully close it
2. "Claude Code for Professional Developers (9h)" catalog claim — single-fetch, unverified
3. Frontend half of the chatbot (not in the free video) — repo client code exists if ever needed

## Suggested next action

Pick a pilot from `output/(C) 2026-07-03-mosh-ai-powered-apps-pilot-methods.md` — headline: build hireui's first LLM feature (candidate-feedback summarizer) Claude-native on the course's layered seam.
