# Hermes Agent — Memory System

## Source
`raw/2026-07-18-hermes-agent/` (esp. t5 Tonbi masterclass, t7 Plastic Labs/Honcho, t8 AI LABS) + official docs. Verified via `wf_06a79485-687` (C8 = CONFIRMED).

## Three layers (all primary-confirmed)
1. **FTS5 cross-session recall** — SQLite full-text search over what the agent has learned; it keeps and searches memory across every session (this is "the single biggest difference from a standard chatbot," per the marketing).
2. **LLM summarization + file-based memory** — concretely (t8): memory lives in **`user.md` + `memory.md`** files with a **hard token limit**. The agent updates them after each run; when a file hits its limit, the model prunes non-useful entries and keeps the newest. The token cap is deliberate — it prevents context-window bloat from degrading the model's attention on the actual task.
3. **Honcho dialectic user modeling** — an evolving profile of *how you work*, layered on top of the built-in memory.

## Honcho (the third-party piece — treat as a dependency)
- **Honcho is made by Plastic Labs, not Nous Research** (t5 + t7 are explicit about this). It is an external "user-modeling / peer-modeling" layer that "uses a custom model to reason about context."
- Plastic Labs' pitch (t7, first-party-adjacent, **promotional**): it will *"get to know you better than any other memory framework that exists"* — this superlative is **unsupported** (no comparative evidence); do not assert it.
- **Open gaps** (flagged by critics): whether Honcho is *required* or *optional*, how it differs from the built-in FTS5+summarization, its latency impact, and any **vendor lock-in / data-residency** implications of routing user-model data to a third-party layer. Not documented in what was reviewed.
- Tonbi's masterclass also surveyed **alternative memory providers** Hermes can use — Memo (server-side LLM extraction), Hindsight (knowledge-graph), Supermemory (multi-container partitioning) — indicating the memory layer is **pluggable**.

## Version-dependent detail — do not over-pin
- A "Gemini Flash summarization layer" (t5) is **not in official docs** — possibly outdated/undocumented; do not assert.
- Tonbi references "version 7" and "Honcho 0.11.0" — version schemes differ from the confirmed Hermes CalVer (`v2026.7.7.2` = v0.18.2); treat specific sub-version claims as unverified.

## Key Takeaways
- Memory is Hermes' most concrete strength: **file-based (`user.md`/`memory.md`) + FTS5 search + LLM-summarized pruning under a token cap** — a legibly-engineered answer to context-rot, not a black box.
- **Honcho is a separate Plastic Labs product** — a real capability but also a third-party dependency with undocumented residency/lock-in implications. For any privacy-sensitive deployment this is the piece to scrutinize.
- The memory layer appears **pluggable** (Honcho / Memo / Hindsight / Supermemory), which is good for the operator's data-residency concerns — you can pick where user-model data lives.
- Maps onto the corpus's [[agent-memory-architecture|agent-memory-architecture]] taxonomy (semantic/episodic memory + procedural skills) and [[claude-code-memory-systems|claude-code-memory-systems]] (file-first, no-vector-DB memory — same design lineage as Anthropic's memory tool).
