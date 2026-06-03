# headroom — Beginner Analysis (project CLAUDE.md)

**Subject:** `chopratejas/headroom` (v144 wiki ship, 2026-06-03).
**Verdict:** GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.
**Tier:** T2 Service (agent context-compression layer). **Routine:** v2.6 (§31/§35/§37).

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis verdict + §35 + §37 + PILOT + honest non-claims.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY (1 new standalone) + 1 re-registration (own-trained-model N=2) + observations; NO state change.
- `02 Wiki/index.md` — the knowledge page.

## One-paragraph summary
**"The context compression layer for AI agents"** — compresses everything an agent reads (tool outputs/logs/RAG/files/history) before it hits the LLM, content-aware (SmartCrusher JSON / CodeCompressor AST / Kompress-base own-model / CacheAligner KV-prefix) + reversible (CCR), across 5 surfaces (Python/TS lib, HTTP proxy, MCP server, CLI wrapper, Docker). Plus `headroom learn` (failure-mining → auto-writes CLAUDE.md/AGENTS.md/GEMINI.md) and SharedContext (cross-agent memory). Apache-2.0; Python+Rust. Repo-stated 73–92% token reduction with preserved accuracy. Directly targets the vault's own context-rot problem.

## Phase 4b headline
PRIMARY = NEW Library-vocab standalone **"Agent Context-Compression Layer"** N=1 CORPUS-FIRST (registry 06 §C). SECONDARY: **RE-REGISTER "Own-Trained Bundled Expert Model" → N=2** (v97 distill + v144 Kompress-base; strengthening, not a new standalone) + Pattern #18 B1 MCP N+1 + Library-vocab #20 Token-Economy N+1 + observations (context-rot corpus-recursive; `headroom learn` auto-authoring; multi-surface). NO Pattern Library state change (46/8).

## §35 / streak
§35 STAYS CLEAR (window {v142 OG, v143 GA, v144 GA} = 1 OG ≤ 1). Streak GA:11·OG:6 [3 ov] → **GA:12·OG:6 [3 ov]**.

## Provenance (§37)
≈7.0k★/479 forks + the 73–92% benchmarks are **repo-stated, NOT API-verified/independently-verified** (env mocks GitHub API). Author identity undisclosed (chopratejas; Indian-heritage-name inferred → (a) FAIL, no axis minted). NOT a #52 claim.

## PILOT — Tier-1, genuinely
The most directly-vault-applicable subject in a long run (productizes the fix for the vault's context-rot). `pip install "headroom-ai[all]"` → `headroom mcp install` or `headroom wrap claude`, reversible, BYO, `install-snapshot` recommended. Worth piloting, not just cataloguing.

Shipped on branch `wiki/v144-headroom` off main per the 2026-06-02 convention. Not auto-merged.
