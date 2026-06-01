# supermemory — Wiki (v132)

> `supermemoryai/supermemory` · **"State-of-the-art memory and context engine for AI. And yes — you can use it as a company/personal brain."** · The memory + context layer for AI: auto-extracts facts from conversations, builds user profiles, resolves contradictions, auto-forgets expired info, and serves RAG + memory in one query. **#1 on LongMemEval (81.6%), LoCoMo, and ConvoMem.** Dev SDK (npm+pip) + MCP server + Claude Code plugin + connectors.

**(C) Claude-generated wiki page.** Fetched 2026-06-01 (GitHub API + README + recursive tree + monorepo map). Routine **v2.6, wiki #132** (⚠️ requested as "v133" — corrected to v132, the next sequential number; v131 harness was the last ship, v130 the audit, no v132 existed). Phase 0.9: **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL, (b) **STRONG**, (c) STRONG, (d) STRONG. **As a goal-aligned v132 this ship CLEARS the breached §35 ceiling** (window → {v129 OG, v131 GA, v132 GA} = 1 OG ≤ 1).

---

## Identity

| Field | Value |
|---|---|
| Repo | [`supermemoryai/supermemory`](https://github.com/supermemoryai/supermemory) |
| What | **AI memory + context engine / "Memory API for the AI era"** — dev SDK + MCP server + Claude Code plugin + consumer app, in one Bun/Turbo monorepo |
| Tier / archetype | **T2 Service** (memory-as-a-platform) — **2nd dedicated agent-memory-system in corpus** (after v66 agentmemory) + agentskills.io SKILL.md implementer + MCP server |
| Stars / forks | **23,726★ / 2,130 forks** (fork_ratio **0.090**) |
| Created / pushed | 2024-02-27 / 2026-06-01 (**~825 days**, pushed today — very active) |
| Velocity | **~29 stars/day lifetime → lower-edge Pattern #52 SUSTAINED-MODERATE-HIGH** (25–150/d band, sustained 825d; a long-lived steady accruer — lifetime avg understates the recent ramp) |
| License | **MIT** (LICENSE + GitHub API agree) |
| Language | **TypeScript** (63%) + **MDX** (30%, the large `apps/docs/`) + **Python** (6%) |
| Stack | Bun + Turbo monorepo; Cloudflare Workers/Pages/KV, Drizzle ORM, Postgres, Remix, TailwindCSS, Vite |
| Distribution | npm `supermemory` + pip `supermemory`; MCP `https://mcp.supermemory.ai/mcp` (OAuth); plugins via separate repos; `npx skills add supermemoryai/memorybench` |
| Default branch / homepage | `main` / [supermemory.ai/docs](https://supermemory.ai/docs) |
| Topics | agent-memory, ai-memory, memory, cloudflare-workers, drizzle-orm, postgres, remix, typescript |
| Author | **supermemoryai** (`owner.type: Organization`, US-based; self-described **"research lab building the engine, plugins and tools"**; bio "Give infinite context to your LLMs"; @supermemoryai; 1,582 followers, 27 repos) |
| Benchmarks | **#1 on LongMemEval (81.6%), LoCoMo, ConvoMem** (the 3 major AI-memory benchmarks); ships **MemoryBench**, an open framework to benchmark memory providers head-to-head (Supermemory vs Mem0 vs Zep…) |

## What it is

A memory + context layer that fixes "your AI forgets everything between conversations." It **extracts facts** from conversations, **maintains a per-user profile** (`profile.static` long-term facts + `profile.dynamic` recent context, ~50ms one-call), runs **hybrid search** (RAG + memory in a single query), **auto-forgets** expired/contradicted info, and ingests multi-modal sources (PDF/image-OCR/video-transcription/AST-aware code chunking). Its thesis: **"Memory is not RAG"** — RAG retrieves stateless document chunks; memory tracks *facts about users over time* (it knows "I moved to SF" supersedes "I live in NYC").

**Two audiences, one engine:**
- **Developers building AI products** — a single API/SDK (TS `npm i supermemory` + Python `pip install supermemory`): `client.add()`, `client.profile()`, `client.search.memories()`, `client.documents.uploadFile()`. "No vector DB config. No embedding pipelines. No chunking strategies." Drop-in framework wrappers: **Vercel AI SDK, LangChain, LangGraph, OpenAI Agents SDK, Mastra, Agno, Claude Memory Tool, n8n.**
- **AI-tool users** — a free consumer **app** (app.supermemory.ai, with an embedded agent "Nova"), a **browser extension**, a **Raycast extension**, **MCP server**, and **plugins**.

**Direct goal-#1 / Claude surface (why it's on-corpus):**
- **MCP server** (`mcp.supermemory.ai/mcp`, OAuth) exposing 3 tools — `memory` (save/forget), `recall` (search), `context` (inject profile; `/context` in Cursor & Claude Code). Clients: **Claude Desktop · Cursor · Windsurf · VS Code · Claude Code · OpenCode · OpenClaw · Hermes.**
- **Open-source plugins** in separate repos: **Claude Code** (`supermemoryai/claude-supermemory`), OpenCode, OpenClaw, and the **Hermes** agent (NousResearch/hermes-agent) as a memory provider.
- **In-repo agentskills.io skill** `skills/supermemory/SKILL.md` (+ references/{api-reference, architecture, quickstart, sdk-guide, use-cases}) and a **MemoryBench skill** (`npx skills add supermemoryai/memorybench` → `/benchmark-context`).
- **Connectors:** Google Drive · Gmail · Notion · OneDrive · GitHub · Web Crawler (real-time webhooks).

**Monorepo (Bun + Turbo):** `apps/{web, mcp, browser-extension, raycast-extension, docs, memory-graph-playground}` + `packages/{ai-sdk, openai-sdk-python, pipecat-sdk-python, cartesia-sdk-python, agent-framework-python, memory-graph, tools, ui, lib, hooks, validation}` + `skills/supermemory/`. The org also **uses Claude Code in its own CI** — `.github/workflows/{claude.yml, claude-code-review.yml, claude-auto-fix-ci.yml}` + a root `CLAUDE.md`.

## Why it's in the corpus

**GOAL-ALIGNED INCLUDE** (v2.5 §31 tier — (b) passes, so this is the corpus's core, not an off-goal capture):

- **(a) FAIL** — supermemoryai is a **US-based AI-startup / "research lab" org**. Not a VN/Asian cultural-peer; not (a)-7 (not a vault-substrate foundational vendor). Clean FAIL — like v126 Every, v124 K-Dense.
- **(b) STRONG** — **agent-memory infrastructure**, squarely goal #1 ("autonomous agents for software development"): it ships a **Claude Code plugin + MCP server + Claude Memory Tool integration + a dev SDK** and drop-in wrappers for LangGraph / OpenAI Agents SDK / Mastra. Direct corpus precedent: **v66 agentmemory** (in-scope, Pattern #85) and v112 freellmapi (infra → STRONG INCLUDE). It's also **specifically resonant for Storm Bear** — the vault *is* a hand-built memory/knowledge system (Karpathy LLM-wiki); supermemory is the productized memory layer. **Not STRONGEST** because (i) half of it is a **consumer "personal brain" product** (app + browser extension), (ii) the core engine is a **hosted SaaS** (the OSS repo is the engine + plugins + SDKs, but the service is hosted), and (iii) it's general-AI-memory, not dev-process-specific. Held at STRONG, honestly — and STRONG already clears the §35 ceiling, so there's no incentive to inflate.
- **(c) STRONG** — a mature, **benchmark-leading** (#1 on the 3 major memory benchmarks), well-architected engine with extensive docs, an open MCP server, multi-language SDKs, a memory-graph, and **MemoryBench** (an open comparative benchmark framework). Instructive on memory-vs-RAG, static+dynamic user profiles, auto-forgetting/contradiction-resolution, AST-aware code chunking.
- **(d) STRONG** — very high connectivity: MCP server (Pattern #18 B1) + agentskills.io 57k chain (in-repo `skills/supermemory/SKILL.md` + the `memorybench` skill via `npx skills add`) + **agent-memory sibling v66 agentmemory / Pattern #85** + **Hermes** (v78/v112 thread) + **n8n** (corpus subject) + **Claude Memory Tool** (Anthropic foundational-vendor adjacency) + internal Claude-Code CI (the v122/v128 "engineering-exhaust" thread, here in a stronger CI-automation form). Competitor-mapping vs Mem0/Zep via MemoryBench.

## Pattern Library contribution (summary)

- **PRIMARY — Pattern #85 "Platform-Primitive Foundation" / Agent-Memory-System sub-archetype → N=2** (v66 agentmemory + **v132 supermemory**): the corpus's 2nd dedicated agent-memory platform-primitive — and a strong cross-instance spread (v66 was small-scale OSS; supermemory is large-scale, benchmark-leading, multi-SDK, hosted-SaaS-backed). **N=2 → promotion-eligible at N=3.** *(Honest caveat: confirm against Pattern #85's exact criteria at the next audit — I'm asserting the agent-memory-system reading, not a verified pattern-definition match.)*
- **SECONDARY (observations / 1 standalone filed — §28 disciplined):**
  - **NEW Library-vocab standalone (N=1, filed to registry):** **"Open Comparative Benchmark Framework for Own Category"** — supermemory ships **MemoryBench**, an open framework that benchmarks memory providers *including named competitors (Mem0, Zep)* head-to-head, and is itself #1 on the external benchmarks. A category-defining "we provide the measuring stick (and we top it)" move. CORPUS-FIRST; promotion-eligible at N=2.
  - **agentskills.io 57k chain — another implementer** (in-repo `skills/supermemory/SKILL.md` + `supermemoryai/memorybench` via `npx skills add`). Administrative; CONFIRMED N=3 unchanged; exact implementer-count flagged for audit (v115 caution).
  - **Pattern #18 sub-mechanism B1 (MCP, one-server-many-clients)** N+1 — 8 listed MCP clients incl. Claude Code/Desktop/Cursor/Windsurf/VS Code.
  - **Pattern #82 quantitative-marketing** — "#1 on LongMemEval/LoCoMo/ConvoMem", "81.6%", "~50ms" (paired with verifiable external-benchmark links, so it's *substantiated* marketing).
  - **Internal Claude-Code-in-CI** (`claude.yml` + `claude-code-review.yml` + `claude-auto-fix-ci.yml` + root CLAUDE.md) — the v122/v128 "engineering-exhaust" thread, here as full CI automation (NOT supermemory's only corpus thread, so a different role than v122/v128 — noted, not conflated).
- **Honest non-claims:** **(b) STRONG, not STRONGEST** (consumer-product duality + hosted-SaaS + general-not-dev-specific) — not inflated, and STRONG already cleared the ceiling; **NOT a 3rd instance of the v94/v118 corpus-recursive-at-methodology-influence pattern** — supermemory is a memory *engine/database* (fact-extraction + RAG + profiles), NOT a Karpathy-LLM-wiki / markdown-vault structure like v118 OpenHuman; conceptually adjacent (it's a "brain"), explicitly *not* counted (the v126 audit's no-manufactured-corpus-recursive discipline); **Pattern #85 N=2 is a strengthening, not a mint**; **only 1 new Library-vocab standalone** (MemoryBench), within the §28 ≤2 cap; **NO Pattern Library state change at ship** (46 confirmed / 8 Library-vocab CONFIRMED unchanged).

## Pilot

**Goal-aligned and genuinely pilot-worthy — and unusually low-friction for *this* operator.** supermemory's MCP server + Claude Code plugin give your Claude/agent workflows persistent cross-session memory, and it's directly adjacent to what the vault does by hand. Recommended trial: `npx -y install-mcp@latest https://mcp.supermemory.ai/mcp --client claude --oauth=yes` (or the manual `mcpServers` config), then use `/context` and let `memory`/`recall` accrue across a few Claude Code sessions on a scratch project. **Caveats to weigh first:** the core engine is a **hosted SaaS** (your memories live on supermemory's servers unless you self-host the OSS engine) — so treat it as a **fenced pilot** (scratch/non-sensitive context first), and note it's a *different* memory model from the vault's hand-curated markdown wiki (a fact-extraction DB, not a Karpathy-LLM-wiki). **Also worth reading regardless:** the `concepts/memory-vs-rag` docs + the `skills/supermemory/references/architecture.md`. Complements (doesn't replace) the still-un-piloted **v126 compound-engineering** (dev process) and **v131 harness** (team generator).

---

*See `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` and `01 Analysis/(C) Pattern-Library-Phase-4b-Pattern-85-Agent-Memory-Platform-N2.md`.*
