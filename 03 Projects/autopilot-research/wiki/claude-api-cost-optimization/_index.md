# claude-api-cost-optimization

> **Topic:** How to cut Claude **API** cost (up to ~90%) without losing model intelligence, per an Anthropic Platform-team talk.
> **Compiled:** 2026-06-15 from a single YouTube transcript (path 5 yt-dlp-only) + first-party Anthropic doc verification.
> **Source video:** [y6hvZGpwf7E](https://www.youtube.com/watch?v=y6hvZGpwf7E) — BizMate AI Official re-upload (Vietnamese subs) of **Punit/Puneet Shah** (PM, Platform team, Anthropic) at **"Code with Claude" London** (closing session).
> **⚠️ Provenance caveat:** the *original English video* could not be located on Anthropic's official channel via automated search; speaker spelling and exact session listing are unconfirmed. **Every technique below was independently verified against first-party Anthropic docs and is real.** See [[source-provenance]] for the full verification record.

---

## What this is

A single 26-minute talk that walks one demo app (HeroCorp, a fictional "superhero outsourcing" company) from **~£31 per dashboard load down to a fraction of that**, by stacking four cost levers in order. The thesis: *"If you remember one thing, remember prompt caching."* Then context engineering, then model-tiering via the Advisor tool.

The talk's repeated meta-advice: **always read the agent transcript** to see what the model actually sees — most cost waste is junk context you didn't realize you were sending.

## The four levers (in the order the talk applies them)

| # | Lever | What it does | First-party feature | Article |
|---|---|---|---|---|
| 1 | **Prompt caching** | Stop re-billing unchanged input tokens (~90% off cached reads) | GA — `cache_control` | [[prompt-caching]] |
| 2a | **Tool Search** | Don't load every tool schema into context; load on demand | GA — `tool_search_tool_*` | [[context-engineering]] |
| 2b | **Programmatic Tool Calling** | Claude writes code to call tools + filter results before they hit context | GA — `code_execution_20260120` + `allowed_callers` | [[context-engineering]] |
| 2c | **Compaction** | Summarize old turns near the context limit → near-infinite effective context | Beta — `compact-2026-01-12` | [[context-engineering]] |
| 3 | **Advisor strategy** | Cheap executor (Sonnet/Haiku) + expensive advisor (Opus) called only when stuck | Beta tool — `advisor_20260301` | [[advisor-strategy]] |

Live demo cost arc + the "read the transcript" discipline: [[demo-cost-progression]].

## Key Takeaways

- **Caching is the highest-leverage, lowest-effort win.** Cached input tokens bill at ~0.1× (90% off) AND don't count against rate limits (an 80% hit rate ≈ 5× effective rate limit) AND lower time-to-first-token. Start here. Target >80% hit rate (top customers hit 90%+).
- **The #1 silent cache killer is a timestamp in the system prompt.** Any byte change in the prefix invalidates everything after it. Keep the prefix frozen; put volatile content last.
- **Context engineering is "intelligence-positive."** Removing junk context doesn't just cut tokens — it improves model performance because the model sees only relevant information.
- **The Advisor strategy is a real, first-party tool**, not just a pattern: set your loop on Sonnet/Haiku and give it an `advisor_20260301` tool backed by Opus. Pareto-optimal — no extra cost on easy tasks, Opus-grade catch on hard ones.
- **"Don't build for the demo, build for production."** The talk's framing: the win is matching context to need so the *product* succeeds, not a flashy demo.

## Original / authoritative sources (for the knowledge)

The canonical "original resources" for everything here are Anthropic's first-party docs — see [[source-provenance]] for the full list and verification verdicts. Primary anchors:
- Prompt caching — `https://platform.claude.com/docs/en/build-with-claude/prompt-caching`
- Tool search — `https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool`
- Programmatic tool calling — `https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling`
- Compaction — `https://platform.claude.com/docs/en/build-with-claude/compaction`
- Context editing — `https://platform.claude.com/docs/en/build-with-claude/context-editing`
- Advisor tool — Claude API skill `shared/tool-use-concepts.md` §Advisor (`advisor_20260301`, beta `advisor-tool-2026-03-01`)
- Event — `https://claude.com/code-with-claude/london` (Code with Claude London, May 19–20 2026)

## Cross-links

- [[external|Storm Bear: Cost-Discipline Enforcement Primitive observation-track]] (`_patterns/03-active-candidates.md`) — this topic is direct first-party evidence for that wiki←product thread.
- Pilot application methods for Storm Bear's own stack: see `output/(C) 2026-06-15-claude-api-cost-pilot-methods.md`.
