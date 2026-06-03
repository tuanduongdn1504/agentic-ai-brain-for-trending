# (C) chopratejas/headroom — Phase 0 + Phase 0.9 STRICT verdict (v144)

**Subject:** `chopratejas/headroom` — https://github.com/chopratejas/headroom
**Date:** 2026-06-03 · **Routine:** v2.6 (§31 + §35 + §37)
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG

---

## Phase 0 — scope gate
In scope, and unusually vault-relevant. **"The context compression layer for AI agents"** — it compresses everything an agent reads (tool outputs, logs, RAG chunks, files, conversation history) **before it reaches the LLM**, "same answers, fraction of the tokens." Dead-center goal #1 (infrastructure for autonomous coding agents) AND it directly targets **this vault's most-documented operational pain — context-rot / token budget** (the vault refactored `CLAUDE.md` into `_state/` chapters precisely because of context-thrashing; headroom is the productized fix).

## Phase 0.9 STRICT — four axes

### (a) Cultural-peer / geographic — **FAIL**
- Owner `chopratejas` (likely Tejas Chopra; Indian-heritage name) — **no name/role/location disclosed in-repo** (confidence: speculation). Per the v98 (mukul975) / v112 / v113 (rohitg00) precedent, an Indian-heritage individual without an Asian-cluster registration is **(a) FAIL** — no new (a) sub-axis minted (the v97→v115 anti-pattern). No rescue.

### (b) Goal-relevance — **STRONG** (load-bearing)
- Infrastructure for AI coding agents (Claude Code / Cursor / Codex / Aider / multi-agent), shipped as a Python/TS **library**, an **HTTP proxy** (zero code change), an **MCP server**, and a **CLI wrapper** (`headroom wrap claude`). Content-aware compression (not LLM-summarization) with **reversible retrieval** (CCR — originals kept, fetched on demand) and accuracy-preserving benchmarks (GSM8K 0.870→0.870; 73–92% token reduction on real workloads).
- **STRONG, and the single most directly-vault-applicable subject in a long run:** it's an operational tool the vault could actually use against its own context-rot problem (the v94/v97 "DIRECT vault-utility" tier). Held at **STRONG not STRONGEST** only because it's a third-party context tool, not the agent substrate/methodology itself — but flagged as a genuine **Tier-1 pilot** (see PILOT).

### (c) Instructive engineering — **STRONG**
A well-built multi-mechanism system: **SmartCrusher** (universal JSON), **CodeCompressor** (AST-aware: Python/JS/Go/Rust/Java/C++), **Kompress-base** (own HuggingFace model trained on agentic traces, for prose), **CacheAligner** (stabilizes prefixes for provider KV-cache hits), **CCR** (reversible — local original store + `headroom_retrieve`). Python 76.8% + Rust 18.4% (engine) + TS. 5 deployment surfaces; Docker `ghcr.io/chopratejas/headroom`. Apache-2.0.

### (d) Corpus connectivity — **STRONG**
- **v97 distill sibling / token-compression cluster** — and a strong one: headroom's **Kompress-base own-trained model** echoes distill's own-trained `distill-1.7B` (see Phase 4b — re-registers the "Own-Trained Bundled Expert Model" Library-vocab at N=2).
- **Pattern #18 B1 MCP** — ships an MCP server (`headroom_compress` / `headroom_retrieve` / `headroom_stats`). N+1.
- **Library-vocab #20 Token-Economy-Quantification** — quantified accuracy-vs-compression benchmarks. N+1.
- **Context-management / context-rot corpus-recursive** — the vault's own discipline (the `_state/` refactor; v94; v137 RLM Step 2.6; the hello-agents Ch 9 lesson). headroom = the productized version.
- `headroom learn` failure-mining → auto-writes `CLAUDE.md`/`AGENTS.md`/`GEMINI.md` (Library-vocab #12 routing-artifacts + auto-author threads, cf. v134).

---

## §35 — Soft Off-Goal-Rate Ceiling
**STAYS CLEAR.** Rolling-3-ship window after v144 = **{v142 OG, v143 GA, v144 GA} = 1 OG ≤ 1 → CLEAR.** v144 is GOAL-ALIGNED; NOT a ceiling-override. Override-frequency triggers UNCHANGED (lifetime 6).

## §37 — Fact-provenance
≈**7.0k★** / 479 forks / Apache-2.0 / Python 76.8% + Rust 18.4% + TS / Python 3.10+ (as of 2026-06, repo page — **stated, NOT API-verified §37.4**; env mocks the GitHub API). Benchmark figures (73–92% reduction, GSM8K 0.870) are **repo-stated, not independently verified**. Velocity/age not established → **NOT a Pattern #52 claim**. Author identity undisclosed.

## Streak (v2.6 §32)
GA:11 · OG:6 [3 ov] → **GA:12 · OG:6 [3 ov]** (v144 = 12th goal-aligned PASS; "49+3\*" frozen @v125).

## PILOT — Tier-1, genuinely (the answer to the standing "ships goal-aligned, pilots none" critique)
The **highest-real-applicability pilot in a long stretch** for THIS vault: it productizes the fix for the vault's own context-rot problem. Lowest-friction path — `pip install "headroom-ai[all]"` then `headroom mcp install` (MCP) or `headroom wrap claude` (CLI wrapper), reversible, BYO. `install-snapshot` recommended. Even a READ of its compressor design (AST-aware CodeCompressor, CacheAligner KV-prefix stabilization, CCR reversible store) is worth borrowing as ideas for the vault's surgical-extract discipline.

## Honest non-claims
- (a) genuinely FAILS (undisclosed individual, Indian-heritage-name inferred only, not a cultural-peer, not (a)-7).
- (b) STRONG-not-STRONGEST (third-party context tool, not the agent substrate) — but the most vault-applicable in a while.
- Benchmarks are repo-stated, not independently verified; NOT a #52 claim.
- Phase 4b: **1** new standalone + **1** re-registration (own-trained-model N=2 — a strengthening, does NOT consume the §28 cap); NO new top-level Pattern, NO tier sub-archetype, NO confirmed-count change.
