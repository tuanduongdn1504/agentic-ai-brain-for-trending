# (C) supermemory — Phase 0 + Phase 0.9 verdict (v132)

**Subject:** `supermemoryai/supermemory` — "State-of-the-art memory and context engine for AI."
**Date:** 2026-06-01. **Routine:** v2.6. **Verdict:** **GOAL-ALIGNED INCLUDE 3/4.**
**Numbering:** requested as "v133" → **corrected to v132** (git-authoritative: v131 harness is the latest ship, v130 the audit, no v132 exists; "v133" would create a phantom gap and mis-key the §35 window).

---

## Phase 0 — scope / decision gate

In-scope on first read: an **AI agent-memory / context engine** with a dev SDK + **MCP server** + **Claude Code plugin** + agentskills.io skill. Corpus's core domain (agent infrastructure; direct precedent v66 agentmemory). No decision-gate concerns. Proceed to Phase 0.9.

**Metadata (verified, gh API + raw README + recursive tree 2026-06-01):** 23,726★ / 2,130 forks (fork_ratio 0.090) / created 2024-02-27 / pushed 2026-06-01 (**~825 days**) / ~28.8★/day lifetime. MIT. TypeScript 63% + MDX 30% + Python 6%. Bun+Turbo monorepo (Cloudflare Workers/Pages/KV, Drizzle, Postgres, Remix, Tailwind, Vite). `latestRelease: null`; default branch `main`; homepage supermemory.ai/docs. Topics: agent-memory, ai-memory, memory, cloudflare-workers, drizzle-orm, postgres, remix, typescript. Org **supermemoryai** (`owner.type: Organization`, US-based, self-described "research lab", bio "Give infinite context to your LLMs", @supermemoryai, 1,582 followers, 27 repos).

---

## Phase 0.9 — STRICT INCLUDE/SKIP (4 criteria)

### (a) cultural-peer / (a)-7 foundational-vendor — **FAIL**

supermemoryai is a **US-based AI-startup / "research lab" org.** Not a VN/Asian cultural-peer (none of (a)-1…(a)-6 apply); not (a)-7 (it is not a vault-substrate foundational vendor — the vault depends on Anthropic/Claude, not on supermemory). Clean FAIL, consistent with v126 Every / v124 K-Dense (US commercial orgs).

### (b) goal-relevance — **STRONG** (verdict-carrier; NOT STRONGEST)

Goal #1 = "Master Claude and autonomous agents for software development." supermemory is **agent-memory infrastructure**: it ships a **Claude Code plugin** (`supermemoryai/claude-supermemory`) + an **MCP server** (Claude Desktop/Cursor/Windsurf/VS Code/Claude Code) + a **Claude Memory Tool** integration + a dev SDK (npm `supermemory` + pip `supermemory`) + drop-in wrappers for **LangGraph / OpenAI Agents SDK / Mastra / Vercel AI SDK**. Memory is a *core component* of autonomous agents — an agent without persistent memory is the problem supermemory exists to fix.

**Corpus precedent for INCLUDE-ing agent infrastructure:** v66 agentmemory ("first dedicated agent-memory-system", Pattern #85) was in-scope; v112 freellmapi (provider-aggregation infra) was a STRONG INCLUDE on "LOW-cost × real dev-utility." supermemory is the same class, larger and benchmark-leading.

**Operator-specific resonance:** the vault *is* a hand-built memory/knowledge system (Karpathy LLM-wiki). supermemory is the productized memory layer — directly studyable and pluggable for Storm Bear specifically.

**Why STRONG and not STRONGEST (honest brakes):**
1. **Consumer-product duality** — roughly half the product is a consumer "company/personal brain" app + browser extension + Raycast extension (off-goal for a dev mastering agents).
2. **Hosted SaaS** — the core engine runs on supermemory's servers (the OSS repo is the engine + plugins + SDKs; the live memory service is hosted), so the highest-value path is a *managed dependency*, not a local tool.
3. **General-AI-memory, not dev-process-specific** — it's memory for any AI use, not a software-development workflow like v126 compound-engineering (STRONGEST).

Held at STRONG, honestly. **Note:** STRONG already passes (b) MODERATE+ and clears the §35 ceiling, so there is no incentive to inflate — and I am not. (b) would be GOAL-ALIGNED even at MODERATE.

### (c) instructive-exemplar — **STRONG**

A mature, **benchmark-leading** engine (#1 on LongMemEval 81.6%, LoCoMo, ConvoMem — the 3 major AI-memory benchmarks, with verifiable external links) and an excellent reference for memory/context-layer architecture: **memory-vs-RAG** distinction, **static + dynamic user profiles** (one ~50ms call), **auto-forgetting + contradiction resolution + temporal supersession**, **AST-aware code chunking**, hybrid RAG+memory in a single query. Extensive `apps/docs/` (MDX) + an open MCP server + multi-language SDKs + a memory-graph + **MemoryBench** (an open comparative benchmark framework).

### (d) corpus-connectivity — **STRONG**

- **MCP server** → Pattern #18 sub-mechanism B1 (one-server-many-clients); 8 listed clients incl. Claude Code/Desktop/Cursor/Windsurf/VS Code.
- **agentskills.io 57k chain** — in-repo `skills/supermemory/SKILL.md` (+ references/) + `supermemoryai/memorybench` via `npx skills add` (vercel-labs/skills mechanism; v114/v121/v126 lineage).
- **Agent-memory sibling v66 agentmemory + Pattern #85** — supermemory is the 2nd dedicated agent-memory platform-primitive (larger scale).
- **Hermes** (NousResearch/hermes-agent as a supermemory memory provider) → v78 ECC / v112 thread.
- **n8n** integration → corpus subject (v53).
- **Claude Memory Tool** integration → Anthropic foundational-vendor adjacency.
- **Internal Claude-Code-in-CI** — `.github/workflows/{claude.yml, claude-code-review.yml, claude-auto-fix-ci.yml}` + root `CLAUDE.md` (the v122/v128 "engineering-exhaust" thread, here as full CI automation).
- Competitor-mapping vs **Mem0 / Zep** (MemoryBench).

---

## Verdict

| Criterion | Call | Note |
|---|---|---|
| (a) cultural-peer / (a)-7 | **FAIL** | US AI-startup org; not a peer, not (a)-7 |
| (b) goal-relevance | **STRONG** | agent-memory infra (Claude Code plugin + MCP + Claude Memory Tool + SDK); NOT STRONGEST (consumer duality + hosted SaaS + general-not-dev-specific) |
| (c) instructive | **STRONG** | benchmark-leading, well-documented memory engine; memory-vs-RAG, profiles, auto-forgetting |
| (d) connectivity | **STRONG** | MCP + agentskills.io chain + v66 agentmemory sibling + Hermes/n8n/Claude-Memory-Tool + internal Claude CI |

**→ GOAL-ALIGNED INCLUDE 3/4** (v2.5 §31 tier: (b) PASSes MODERATE+, so this is the corpus's core, not an off-goal capture). The INCLUDE rests on (b)(c)(d); (a) FAILs cleanly.

---

## §35 soft off-goal-rate ceiling — analysis (THIS SHIP CLEARS IT)

- **Entering this ship the ceiling was BREACHED:** rolling-3-window = {v128 OG, v129 OG, v131 GA} = 2 OG (v131 satisfied the §35.2 "next ship goal-aligned" mandate but did not fully clear).
- **v132 supermemory is GOAL-ALIGNED** → the new rolling-3-window = {v129 OG, **v131 GA, v132 GA**} = **1 OG ≤ 1 → CEILING CLEARS (§35.3).** v132 is the goal-aligned ship that scrolls v128 out of the window. No `[ceiling-override]` used or needed.
- **Override-frequency triggers (2-in-20 / 3-in-30):** UNCHANGED — v132 is not an override (`[1 ov]` holds, nothing trips).

## Streak (v2.5 §32 forward / carried under v2.6)

Historical **"49+3\*" FROZEN @v125** (not recomputed). Forward: **`GA:2 · OG:3 [1 ov]` → `GA:3 · OG:3 [1 ov]`** — v132 = the **3rd GOAL-ALIGNED PASS** under v2.5/v2.6; consecutive-GA stream v131→v132 = 2 in a row. Override subset `[1 ov]` UNCHANGED.

## Honest summary

A clean, on-corpus GOAL-ALIGNED INCLUDE that — as v132 — fully clears the breached §35 ceiling. I held **(b) at STRONG, not STRONGEST**, with concrete brakes (consumer-product duality, hosted-SaaS core, general-not-dev-specific), and noted that STRONG already cleared the ceiling so there was no inflation incentive. (a) FAILs honestly (US AI-startup org). The build flags the requested-"v133" → **v132** numbering correction prominently rather than silently accepting an off-by-one.
