# (C) Autopilot Loop — 2026-07-06-12

> **Trigger:** manual operator session ("build knowledge from this video + double deep dive + pilot methods")
> **Topic:** claude-tag-multiplayer-agent (NEW)
> **Started:** 2026-07-06T11:40+07:00
> **Ended:** 2026-07-06T~13:10+07:00
> **Duration:** ~90m (incl. ~10m session-limit outage wait)

## Source chain

- Operator-submitted: `6kU_TpceoJ4` BizMate AI Official VN dub "(New Update) Anthropic ra mắt Claude Tag" (2026-07-05, 11:26, ~292 views; full dub, no divergence from original)
- Resolved original: `MhfnicQVkgY` official Claude channel "The future of work with @Claude" (2026-07-02, 11:26, ~87K views) — Boris Cherny + Cat Wu, both transcripts read in full in main loop
- First-party double-dive: claude.com/tag + 7 docs pages + announcement + 3 support articles + Slack Marketplace + agent-identity blog + METR primary sources + press sweep

## What happened

1. Ingest + original-resource resolution in main loop (yt-dlp captions ×2; "Claude Tag is a dub artifact" hypothesis REFUTED — it's the real product name).
2. Workflow `wf_36db963e-d86` launched: 11 dives + corpus-positioning + 18 refute-first verifiers + critic.
3. **Session-limit outage** (resets 12:10 +07) killed docs dive, corpus dive, all 18 verifiers, critic mid-run. 9 dives survived (~484K tokens / 239 calls).
4. **Recovery: Workflow resume** (`resumeFromRunId`) after reset — cached dives reused, failures re-ran (~1.33M tokens / 440 calls cumulative). First resume-recovery in this project; markedly cheaper than the historical main-loop-takeover-everything pattern.
5. 11 machine verdicts (5 CONFIRMED / 6 PARTIAL / 0 REFUTED); 7 verifiers died on StructuredOutput → closed by main-loop takeover from already-fetched primary sources.
6. Compile: 15 wiki files (NEW topic), master index entry, inventory row raw→compiled, this log.
7. Pilot deliverable: `output/(C) 2026-07-06-claude-tag-pilot-methods.md` (A/B/C/D/E tracks, 16 methods).

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 2 videos + ~20 first-party/press pages | 1 (new topic) | 0 topic-level (watch-list items logged in caveats) | 1.0 |

- `gaps_closed_ratio` = **1.0** (cold-start topic fully compiled; residual unknowns are watch-list items, not stubs: GA pricing post-09-01, Teams timing, region availability, ambient-injection docs, reaction re-drain ~2026-08)
- Stop reason: single-topic manual session complete

## Incidents & misfires (prime-directive ledger)

- **Session-limit outage mid-workflow** → recovered via workflow resume with cached dives. Lesson recorded: for long workflows near limit-reset boundaries, resume-from-journal beats relaunch AND beats main-loop takeover; keep the script file path + runId from the launch result.
- **7 verifier deaths on StructuredOutput schema-compliance** (haiku-tier verify agents) → main-loop takeover closures, documented per claim in caveats. Recurring pattern (cf. miai 1 death, jsm 13 deaths): consider `effort` bump or explicit schema-example in verify prompts next ship.
- **Verifier misfire:** METR verifier declared the 16h quote "not in the launch video" (couldn't fetch video; mistook fetch-failure for absence) → overridden by main-loop captions. Same class as prior video-fetch misfires; captions-in-main-loop-first discipline validated again.
- **Corpus-agent overreaches quarantined:** "Anthropic violates own ToS" (wrong — org billing ≠ plan-auth), "78% of IT leaders" (no source, likely confabulated), "2-year-old Telegram stack" (2 months). All caught pre-publication; do-not-quote list in caveats + corpus-positioning.

## Wiki articles created

- wiki/claude-tag-multiplayer-agent/ — _index + 14 articles (see inventory row)
- wiki/_master-index.md — NEW topic entry prepended
- raw/2026-07-06-claude-tag-future-of-work.md — full EN transcript + VN dub notes
- raw/_inventory.md — row raw→compiled

## Suggested next action

Pick a pilot from `output/(C) 2026-07-06-claude-tag-pilot-methods.md` — recommended: **B1 ambient-lite proactive rules on the existing Telegram channel** (zero new infrastructure, directly tests the one pattern the operator's stack lacks) and **C3 hireui agent-PR-share instrumentation** (one `git log` script; produces the operator's own auditable 65%-analog). Re-drain community reaction ~2026-08 after the forced migration + credit expiry produce real-world data.
