# (C) Autopilot Loop — 2026-07-13-19

> **Trigger:** interactive `/loop` request (operator: "start build knowledge from other video with loop" → single-URL follow-up `GrNbuWWJYiI`)
> **Topic:** agent-memory-architecture (deepening pass 3 — NOT a new topic)
> **Started:** 2026-07-13T19:05:00+07:00
> **Ended:** 2026-07-13T19:45:00+07:00
> **Duration:** ~40m

## Pre-flight: duplicate + scope check

- User's first URL (`Zof2Oaj14rk`) was already in-corpus verbatim (`local-ai-coding-agents`, shipped 2026-07-11) — flagged before any work, user chose to substitute a different video.
- Second URL (`GrNbuWWJYiI`) — NOT a duplicate video ID, but scouting revealed it's a **direct sequel** by a creator already in-corpus (Sean Chen / ShenSeanChen, whose prior video `mY3bR9qjZr4` is the existing `agent-memory-architecture` topic, compiled 2026-07-03, deepened 2026-07-04). Reading all 14 existing articles + 4 adjacent topics (`agent-development-lifecycle/langchain-interrupt-26-anchor`, `claude-code-hooks/`, `prompt-evaluation/`, `harness-engineering/terminology`) showed **~90% of this new video's content was already verified in-corpus**. Decision: treat as **deepening pass 3**, not a new topic — matches the file's own established 2026-07-04 precedent, avoids wasteful duplicate re-verification.

## Source

- Video `GrNbuWWJYiI` — Sean's AI Stories, *"You Can Learn AI Agent Harness & Loop Engineering In 19 Min | LLM Ops, Eval, Tracing, RAG"* (2026-06-26, 20:00, ~92K views) — one week after the topic's primary source.
- Path 5 (yt-dlp-only). EN auto-captions only (no manual track) → dedupe → ~7K-word transcript, read in full in the main loop. No NotebookLM.

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 (video); narrow new-ground dive (Langfuse + harness-tool status) | ~2 (Langfuse under-covered; sequel content uncross-linked) | 0 | 1.0 |

`gaps_closed_ratio` = **1.0** — the only two real gaps (Langfuse depth; sequel cross-links) were fully closed; everything else was already covered and just needed citing, not re-deriving.

## Verification workflow

- 5-agent workflow (2 dives + 2 refute-first verifiers + 1 completeness critic) — **~195K tokens, 72 tool calls, ~75 min wall-clock**. Right-sized deliberately: a full mega-workflow (like the original 28-agent pass) would have re-verified ground already settled.
- 0 agent deaths, 0 empty results.
- **Misfires caught (Rule 12 — verify layer working as designed):** the Langfuse dive drafted a wrong investor name ("General Catalyst" — not on Langfuse's own investor list) and implied a dataset-versioning eval feature is live when Langfuse's docs say it's "coming soon"; the harness-tools dive drafted a fabricated "LangGraph GA October 2025" date with zero supporting evidence. All three caught by the refute-first verify stage before reaching the wiki — these were errors in this pass's own research, not claims made by the video.
- **Genuinely new fact surfaced:** Langfuse was acquired by ClickHouse on 2026-01-16 and "stays open source" per their own blog — not previously in this corpus.

## Scorecard (sequel video claims)

8 claims graded, all ✅ CONFIRMED or ⚠️ VARIANT-DEFINITION/REPEAT — **0 FALSE, 0 FABRICATED** (consistent with the presenter's track record: the original memory-system video also had only one substantive error, the vector-store-universality claim). Full table: [wiki/agent-memory-architecture/caveats-and-corrections.md](../wiki/agent-memory-architecture/caveats-and-corrections.md) (2026-07-13 section).

## Sources ingested

- raw/2026-07-13-sean-agent-harness-loop-llmops.md (transcript)

## Wiki articles created/updated

- wiki/agent-memory-architecture/harness-loop-llmops-sequel.md (NEW)
- wiki/agent-memory-architecture/langfuse-and-harness-tools.md (NEW)
- wiki/agent-memory-architecture/_index.md (UPDATED — +2 articles, now 16)
- wiki/agent-memory-architecture/source-provenance.md (UPDATED — deepening pass 3 section + misfire log)
- wiki/agent-memory-architecture/caveats-and-corrections.md (UPDATED — 8-claim sequel scorecard)
- wiki/harness-engineering/terminology.md (UPDATED — "Variant definitions" note under Harness engineering, cross-linking Sean Chen's horse-metaphor sense)
- wiki/_master-index.md (UPDATED — agent-memory-architecture entry extended)
- raw/_inventory.md (UPDATED — new row, Status: compiled)

## Pilot angle (folded into loop-log — content too narrow for a standalone pilot-menu revision)

Langfuse is genuinely relevant to hireui's Goal #2 (no LLM integration exists yet — see memory pin `project_hireui_no_llm_yet`): it's MIT-licensed, self-hostable for free, and traces+evals agent runs — a lighter-weight, cheaper alternative to standing up the full LangSmith/SmithDB stack already documented for hireui's first LLM feature (Match-Explain, per the Mosh vendor-seam plan). Worth a one-line addition to the existing pilot-methods doc at the next pilot-ranking refresh, not urgent enough to justify a new deliverable today.

## Top unclosed gap (follow-up)

- Langfuse's exhaustive eval-template list and exact integration count remain unverifiable from official docs (flagged, not blocking) — re-check if/when Langfuse is actually adopted for a hireui pilot.

## Suggested next action

No further action required on this video — it's fully absorbed into `agent-memory-architecture`. Per the vault's own pilot-deployment backlog (8 ranked pilots accumulated / 0 deployed, per root CLAUDE.md), the next highest-leverage move remains **deploying one of the already-ranked pilots** (cc-sdd #1 or codex-plugin-cc #1.5) rather than accumulating further research passes — this session added corpus depth, not deployment progress.
