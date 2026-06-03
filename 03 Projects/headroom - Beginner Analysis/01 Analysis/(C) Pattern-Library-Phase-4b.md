# (C) headroom — Pattern Library Phase 4b (v144)

**Routine v2.6 · §28 (single registry / ≤2-new-standalones / clustering-first / filing-is-an-act).**

## PRIMARY — 1 NEW Library-vocab standalone (FILED to registry 06 §C)

### "Agent Context-Compression Layer (multi-surface, content-aware, reversible pre-LLM context interceptor)" — N=1 CORPUS-FIRST
- **What:** a dedicated layer that intercepts **everything an AI agent reads** (tool outputs, logs, RAG chunks, files, conversation history) and compresses it **before it reaches the LLM**, deployable as a **library / HTTP proxy / MCP server / CLI wrapper** (5 surfaces), using **content-aware compressors** (SmartCrusher JSON, CodeCompressor AST-aware, Kompress-base own-model for prose, CacheAligner KV-prefix) rather than LLM-summarization, with **reversible retrieval** (CCR: originals kept locally, fetched via `headroom_retrieve`) and accuracy-preserving benchmarks.
- **Why it's its own mechanism:** the corpus has a token-compression *CLI* (v97 distill — compresses CLI-pipe/session text + a bundled own-model) and Library-vocab #20 Token-Economy-Quantification (*measuring* token cost). headroom is the first **agent-context layer**: it sits between the agent and the LLM, transparently across multiple deployment surfaces, intercepting the agent's *entire read-context* with reversible (not lossy-only) compression + cross-agent shared memory + MCP exposure. The novel axis = "transparent, reversible, multi-surface context interception for agents," distinct from a CLI compressor and from token-accounting.
- **Distinct from:** v97 distill (a CLI-pipe session-text compressor — ADJACENT, see the cluster note + the own-model re-registration); Library-vocab #20 (measures tokens, doesn't compress context); v140 tool-tiers (gates which tools register, not context compression).
- **Promotion-eligibility:** N=2 if a 2nd transparent multi-surface agent-context-compression layer appears. **Stale-watch ~v159.**
- **§28 new-standalone count this ship = 1 (≤ 2).** Registry 06 §C edited (rule-5).

## SECONDARY — re-registration + observations (§28-disciplined)

- **RE-REGISTER "Own-Trained Bundled Expert (small) Model for a narrow task" → N=2** (v97 distill `distill-1.7B-MLX` for compression + v144 headroom **Kompress-base** "our HuggingFace model trained on agentic traces" for prose compression). First minted at v97 (PROVISIONAL N=1, "Own-Trained Bundled Expert Language Model at Solo-Founder Scale"); auto-retired ~v112 (15-wiki rule) with no 2nd instance; §28/§2 permit re-registration on a genuine 2nd, which v144 is. A **strengthening, NOT a new standalone → does NOT consume the §28 cap.** Both are own-trained small models bundled for a narrow purpose (compression); promotion-eligible at a genuine N=3.
- **Pattern #18 sub-mechanism B1 "MCP" — N+1.** `headroom mcp install` exposes `headroom_compress` / `headroom_retrieve` / `headroom_stats` to any MCP client. Strengthens the (now dense) MCP B1 line; top-level count UNCHANGED.
- **Library-vocab #20 Token-Economy-Quantification — N+1.** Accuracy-vs-compression benchmarks (GSM8K 0.870→0.870; 73–92% token reduction; SQuAD-v2 97% @ 19%).
- **Context-management / context-rot corpus-recursive — OBSERVATION.** headroom productizes the vault's own discipline (the `_state/` CLAUDE.md refactor for context-thrashing; v94; v137 RLM Step 2.6; hello-agents Ch 9). The pilot story, not a mint.
- **`headroom learn` failure-mined auto-authoring of routing artifacts — OBSERVATION.** Mines failed agent sessions → auto-writes corrections to `CLAUDE.md`/`AGENTS.md`/`GEMINI.md` (Library-vocab #12 routing-artifacts + the v134 auto-author thread). Recorded, not minted.
- **Multi-deployment-surface thread — OBSERVATION.** 5 surfaces (library/proxy/MCP/CLI/Docker) for one capability — connects to v141 dual-deployment + v143 agent-native CLI ("same capability, N delivery surfaces"). Folded into the PRIMARY's "multi-surface" axis; not separately minted.

## Pattern Library state change: NONE
46 confirmed / ~25 active / 8 Library-vocab CONFIRMED → UNCHANGED. PROVISIONAL standalone surface +1 (Agent Context-Compression Layer); + 1 re-registration (own-trained-model N=2, within an existing slot). NO top-level Pattern, NO tier sub-archetype, NO confirmed-count movement.

## Audit hand-off note
v144 hands the overdue ~v139–v140 audit: (1) the **own-trained-bundled-model** re-registration (v97+v144) now at N=2 — watch for a clean N=3; (2) the MCP B1 line is *very* dense now (v66/v70/v119/v132/v134/v140 servers + v141 11-connectors + v143-adjacent + v144) — an "MCP-server/MCP-exposure" tier sub-archetype review is overdue, NOT minted here; (3) a **token-compression / context-management cluster** forming (v97 distill + v144 headroom; + Library-vocab #20) — candidate class if a 3rd appears. NOTHING for the override-frequency thread (v144 is a clean goal-aligned ship).
