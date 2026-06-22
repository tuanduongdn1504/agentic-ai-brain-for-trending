# (C) cortex-hub — LLM Wiki

> **Subject:** `lktiep/cortex-hub` — Self-hosted AI Agent Memory + Code Intelligence Platform · v0.7.0 · MIT · author **Jack Le** (`lktiep`, jackle.dev)
> **Ship:** v181 (2026-06-22) · **Tier:** T2 Service · **Verdict:** GOAL-ALIGNED INCLUDE 3/4 [(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG] · **NO MINT** (counts 46/10 unchanged)
> **Source of truth:** cloned + source-verified at commit `27d5d23` (default branch `master`, 2026-06-15). Facts below are checked against code, not README-parroted. Verdict + collision record → `01 Analysis/`.
> **Browsable HTML companion:** https://claude.ai/code/artifact/a355ae01-b7df-44ef-8745-92fa3c646d50

---

## 1. What it is (one paragraph)

cortex-hub is a **self-hosted backend that gives every AI coding agent on your team a shared brain** — persistent memory, AST-aware code search, a temporal knowledge base, recipe-learning, an LLM gateway, and quality gates — exposed through **a single MCP endpoint** that Claude Code / Cursor / Antigravity / Codex / Gemini / Windsurf all connect to. README tagline (verbatim): *"Self-hosted AI Agent Memory + Code Intelligence Platform — one MCP endpoint for persistent memory, AST-aware code search, shared knowledge, and quality enforcement across all your AI coding agents."* It is a **TypeScript monorepo** (an MCP server + a Next.js dashboard + a custom memory engine + a VS Code extension) that, at its core, **orchestrates a handful of services behind one endpoint** — two of the headline ones being third-party engines it wires up, not code it wrote.

**Mental model:** *agentmemory v66's "memory MCP" + codegraph v70 / codebase-memory-mcp v172's "code knowledge-graph MCP" + cc-switch v73's "provider gateway," bundled into one self-hosted hub with a dashboard and an experimental cross-IDE task-delegation layer on top — so the capabilities that the corpus has only ever seen as separate point-solutions arrive integrated.*

---

## 2. Why it exists (the problem it solves)

README problem statement (verbatim): *"Every AI coding agent works in **isolation**. Switch IDE, switch machine, switch project — the agent starts from zero."*

The thesis is **anti-isolation**: an agent's memory, the team's accumulated knowledge, and a project's code structure should live in **one shared, persistent, self-hosted place** that any agent on any machine can query — rather than being re-derived per session, per tool, per developer. cortex-hub is the backend that holds that shared state and serves it over MCP.

This is **uncannily close to the operator's own setup**: hireui's CONSTITUTION is "GitNexus-first," and cortex-hub's code-intelligence layer *is* GitNexus (see §4.2). cortex-hub is, in effect, a productized version of "wrap GitNexus + a memory store + a gateway behind one MCP endpoint for Claude Code."

---

## 3. Repository shape (source-verified at `27d5d23`)

```
cortex-hub/
├── apps/
│   ├── hub-mcp/          ← the MCP server (the 18 cortex_* tools)
│   ├── dashboard-api/    ← REST API + SQLite (cortex.db) + Conductor backend
│   ├── dashboard-web/    ← Next.js 15 / React 19 dashboard (static export; 13 pages)
│   └── cortex-extension/ ← VS Code extension (Conductor WebSocket UI panel)
├── packages/
│   ├── shared-types/     ← shared TS types
│   ├── shared-utils/     ← shared utilities
│   └── shared-mem9/      ← "mem9" — cortex-hub's OWN embedding + memory engine
├── benchmarks/           ← the MemPalace comparison
├── infra/                ← docker-compose.yml + Dockerfile.gitnexus (+ patches)
├── scripts/              ← install.sh, run-agent.sh
├── docs/                 ← conductor.md (marks orchestration EXPERIMENTAL) etc.
├── templates/skills/install/SKILL.md  ← the /install skill
├── AGENTS.md  ·  CLAUDE.md  ·  .cursorrules   ← agent-instruction artifacts
└── LICENSE (MIT) · package.json · turbo.json · pnpm-workspace.yaml
```

**Languages (page-stated):** TypeScript 65.6% · CSS 15.4% · Shell 12.1% · PowerShell 5.9% · JS 1.0%.
**Engagement (page-stated, §37.4 NOT API-verified):** 57★ / 17 forks / 2 releases / latest **v0.7.0 (2026-04-11)**.

---

## 4. The capabilities — and what's real vs. vendored

### 4.1 Memory — `mem9` (cortex-hub's OWN code) ✅
- `packages/shared-mem9` is purpose-built (not a wrapper around mem0 / agentmemory / supermemory / Letta — **none of those are dependencies**, verified).
- **Embeddings:** `Xenova/all-MiniLM-L6-v2` (local, in-process, free, via `@huggingface/transformers`) by default; `gemini-embedding-001` (paid) as a fallback.
- **Vector store:** **Qdrant** (`qdrant/qdrant:v1.13.6`, a separate Docker container on `:6333`) — not embedded.
- **Hierarchical recall:** branch-scoped → project-scoped → agent-scoped namespacing via `userId`.
- MCP tools: `cortex_memory_store` · `cortex_memory_search` · `cortex_memory_delete`.

### 4.2 Code intelligence — "GitNexus" (THIRD-PARTY, and it's a corpus subject) ⚠️
**This is the headline corpus finding.** cortex-hub's "GitNexus (AST graph, multi-repo search, symbol context, impact analysis)" is **not cortex-hub's code**. It is the external npm package **`gitnexus`** — which is **`abhigyanpatwari/GitNexus`, the corpus's own v33 subject** (Abhigyan Patwari, India; an AST→knowledge-graph code-intelligence tool; **PolyForm Noncommercial 1.0.0**; ~36.8k weekly npm downloads).

Evidence (`infra/Dockerfile.gitnexus`):
```dockerfile
RUN npm install -g gitnexus@latest --timeout=600000
# then PATCHES the installed package in place:
RUN sed -i "s/server\.listen(port, '127\.0\.0\.1'/server.listen(port, '0.0.0.0'/g" \
      /usr/lib/node_modules/gitnexus/dist/cli/eval-server.js
RUN sed -i 's/const HEAP_MB = 8192/const HEAP_MB = 3072/g' \
      /usr/lib/node_modules/gitnexus/dist/cli/analyze.js
```
It runs as a container on `:4848`; cortex-hub proxies to it (`cortex_code_search`, `cortex_code_impact`, `cortex_code_context`, `cortex_code_reindex`, `cortex_list_repos`, `cortex_cypher`, `cortex_detect_changes`). The code-graph engine is GitNexus's (the `cortex_cypher` handler even works around "Kuzu doesn't support multi-label WHERE").

**There is NO credit/attribution to abhigyanpatwari/GitNexus anywhere in the repo, and no NOTICE file.** That is a real concern: **GitNexus is PolyForm-Noncommercial** (free for personal/non-commercial use only; commercial use requires a license from the author), while **cortex-hub is MIT** and invites use "across all your AI coding agents" — i.e. plausibly by commercial teams. A commercial team self-hosting cortex-hub would be using GitNexus commercially, uncredited and (per PolyForm) unlicensed. **Flagged honestly; the operator (commercial Scrum-coaching / SaaS) must resolve the GitNexus license before any commercial use.** (See `01 Analysis` for the full corpus-recursive-dependency reasoning.)

### 4.3 Knowledge base — temporal, "MemPalace-inspired" ✅
- SQLite (`cortex.db`) + Qdrant for semantic search.
- **6 hall types** (`knowledge.ts`): `fact` · `event` · `discovery` · `preference` · `advice` · `general`.
- **Temporal validity:** `validFrom` (ISO date) on store; `asOf` filter on search ("query only facts valid at this point in time"); an `invalidate` endpoint.
- MCP tools: `cortex_knowledge_store` · `cortex_knowledge_search`.
- README credits **MemPalace** (`milla-jovovich/mempalace`) as the competing system it benchmarks against (a NON-corpus project).

### 4.4 Recipe system — auto-learning from execution ✅ (described; thin in code)
- Auto-captures on `task.complete` / `session_end`; an LLM extracts reusable "recipes" from execution logs.
- Hybrid ranking: `vector_similarity*0.6 + effective_rate*0.3 + recency*0.1`; deprecates a recipe when `fallback_rate > 0.4`.
- README credits **HKUDS/OpenSpace** as inspiration for this system (a NON-corpus project).

### 4.5 LLM gateway — "CLIProxy" (THIRD-PARTY) ⚠️
- The "multi-provider LLM gateway with fallback chains" is the external service **`eceasy/cli-proxy-api:latest`** (Docker, `:8317`, OpenAI-compatible), not cortex-hub's code.
- Routes OpenAI / Anthropic / Gemini / any OpenAI-compatible API; uncredited in the README.

### 4.6 Quality gates — 4-dimension scoring ✅
- 4 dimensions × 25 weight each: **Build** (compiles) · **Regression** (no broken tests) · **Standards** (conventions) · **Traceability** (changes linked to requirements).
- MCP tool: `cortex_quality_report` (gate_name / passed / score / details) + `cortex_plan_quality`.

### 4.7 Conductor — multi-agent orchestration (EXPERIMENTAL) ⚠️
`docs/conductor.md` marks this **explicitly experimental**. State:
- ✅ Shipped: agent identity · agent registry + WebSocket · task creation/assignment · task pickup · task lifecycle (accept→in_progress→completed) · strategy review · `/conductor` dashboard page.
- 🔄 Partial: auto-reassignment on failure · strategy auto-approval · cross-IDE push notifications.
- 📋 Planned: smart agent matching · task dependency auto-resolution · multi-step plan execution · conductor cost analysis.
- README (verbatim): *"It is not feature-complete — agents can already create/pickup tasks, but autonomous strategy execution and smart agent matching are still WIP."*
- Task tools (`tasks.ts`, **not** in the root MCP endpoint list): `cortex_task_create` · `cortex_task_pickup` · `cortex_task_accept` (+ update/status).

---

## 5. MCP tool surface — ⚠️ README says 24, code registers 18

`apps/hub-mcp/src/index.ts` (lines ~126–145) registers **18 tools** on the endpoint:

```
cortex_health · cortex_memory_store · cortex_memory_search · cortex_memory_delete ·
cortex_knowledge_store · cortex_knowledge_search · cortex_code_search · cortex_code_impact ·
cortex_code_context · cortex_code_reindex · cortex_list_repos · cortex_cypher ·
cortex_detect_changes · cortex_quality_report · cortex_session_start · cortex_session_end ·
cortex_changes · cortex_plan_quality
```

The README's **"24 tools"** is not borne out by the endpoint registration (18). The gap is roughly the Conductor `cortex_task_*` family + `cortex_tool_stats`, which exist in source but are **not** in the root endpoint list. **Documents the code-verified count (18); the "24" is a doc-vs-code inflation, flagged.** (Same class of honest flag as camofox v179's 30-min-vs-10-min session timeout.)

---

## 6. How agents connect

`scripts/install.sh` (a real POSIX shell script — **not** a binary downloader) auto-detects installed agents and **writes their MCP config** to point at the hub (`http://localhost:8318/mcp`), then installs git hooks (via `lefthook`) and a global `/install` skill (`~/.claude/skills/install/SKILL.md`). Supported: **Claude Code · Gemini CLI / Antigravity · Cursor · Windsurf · VS Code · Codex**. The `apps/cortex-extension` VS Code extension is a **separate Conductor WebSocket UI panel** (not an MCP provider).

This is a clean **Pattern #18 sub-archetype B / B1-MCP** instance — *one MCP endpoint, many agent clients auto-configured* (the agentmemory v66 / codegraph v70 / devspace v171 / codebase-memory-mcp v172 lineage).

---

## 7. Benchmarks (vendor-stated, vs. MemPalace — NOT independently reproduced)

README (page-stated): R@5 **96.0%** (vs MemPalace 96.6%) · R@10 **97.8%** · NDCG@10 **1.44** · embedding **~10 ms/text** (vs ~600 ms) · 500-query search **52.6 s** (vs ~5 min) · cost **$0/run** (vs ~$2–5). These are the author's own unreplicated numbers (a `benchmarks/` dir exists). → Library-vocab **#20 Token-Economy-Quantification QUALIFIED-ADJACENT** (cost/perf quantification, page-stated → N stays 4); **NOT a #52 claim**.

---

## 8. Deploy, ops & security surface

- **Install:** `curl -fsSL ".../scripts/install.sh" | bash` (a `curl|bash`; the script writes configs/hooks/skill — review it first; `install-snapshot` before running).
- **Run:** `infra/docker-compose.yml` brings up **5 services** — Qdrant (`:6333`) · gitnexus (`:4848`) · llm-proxy/CLIProxy (`:8317`) · dashboard-api (`:4000`) · hub-mcp (`:8318`).
- **Network:** Bearer-token auth gates `/mcp`; optional **Cloudflare Tunnel** ("zero open ports on host").
- **Secrets:** API keys in `.env` / Docker env (none committed).
- **No `postinstall` scripts; no detected RCE vectors** in the MCP server (auth-gated). Standard self-hosted-agent-platform risk profile, **plus** the GitNexus PolyForm license wrinkle (§4.2).

---

## 9. Maturity / honesty signals

- **v0.7.0**, "Phase 6 (Polish, docs, testing, GA)" per AGENTS.md → **pre-GA**.
- **Honesty HIGH** where it counts: Conductor is explicitly flagged experimental with a candid capability table; the MemPalace benchmark even reports MemPalace winning R@5.
- **Testing MINIMAL:** ~2 test files (`conductor*.test.ts`) over ~78 `.ts` files (<5%).
- **Zero `TODO`/`FIXME` markers** in source — unusually clean (either finished or sanitized).
- **README count inflation** ("24 tools" vs 18) + **uncredited third-party engines** (GitNexus, CLIProxy, Qdrant, Xenova) are the deflating signals.

---

## 10. Corpus placement (for the wiki maintainer)

- **Closest cousins / family:** the **augment-backend** MCP servers — agentmemory v66 / supermemory v132 (memory), **codegraph v70 / codebase-memory-mcp v172 §C#32** (code knowledge-graph), cc-switch v73 (provider gateway). cortex-hub **bundles** their capability classes behind one endpoint.
- **DISTINCT from** the self-contained agent **runtimes** PilotDeck v175 §C#35 / OpenHuman v118 (cortex-hub is *not* its own agent — it augments existing third-party agents) and from devspace v171 §C#31 (which *manufactures* a local agent from a hosted host — opposite direction).
- **Conductor** is an *adjacency* to the orchestration platforms Paseo v150 / ai-maestro v163 §C#23 — but it is **experimental/WIP**, not a clean orchestration-platform instance.
- **Code-intel = GitNexus v33** re-used via dependency → cortex-hub does **not** add a clean new instance to §C#32; it surfaces an audit note (GitNexus v33 + graphify v16 actually predate codegraph v70 in that family) + a corpus-recursive-dependency data-point + the PolyForm/MIT license flag.
- **Pattern outcome: NO MINT.** A "unified multi-capability shared agent-infra hub" *would* be corpus-first as a class, but cortex-hub is a **thin orchestration layer wrapping third-party engines** (two of three headline capabilities vendored, one a corpus subject), with README-inflated counts and an experimental orchestration layer → the v179/v180 "packaging-not-capability + weak/early-instance + family-overlap" decline. The unified-hub facet is **recorded as a DEFERRED watch axis**, to be minted on a cleaner/heavier exemplar later (then cortex-hub is a credited prior data-point). Counts UNCHANGED **46/10**. Full reasoning → `01 Analysis/(C) v181 cortex-hub — Verdict & Collision-Check Record.md`.

---
*Built inline (no multi-agent workflow — see vault memory `feedback_wiki_verify_independently_check_collisions`). Facts source-verified from the clone at `27d5d23` + an exhaustive code read; the GitNexus = abhigyanpatwari/GitNexus = corpus v33 identity verified by hand (npm `gitnexus` owner + PolyForm license confirmed via WebSearch) — not assumed from the shared component name.*
