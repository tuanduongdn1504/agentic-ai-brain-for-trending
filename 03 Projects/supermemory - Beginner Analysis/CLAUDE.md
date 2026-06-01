# supermemory — Project Context

**Subject:** [`supermemoryai/supermemory`](https://github.com/supermemoryai/supermemory) — "State-of-the-art memory and context engine for AI. And yes — you can use it as a company/personal brain."
**Wiki version:** v132 (Routine **v2.6**). ⚠️ Requested as "v133" — corrected to **v132** (next sequential; v131 harness was the last ship, v130 the audit, no v132 existed).
**Status:** SHIPPED 2026-06-01. **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL US-org + (b) STRONG + (c)(d) STRONG. **As a goal-aligned v132, this ship CLEARS the breached §35 ceiling** (window → {v129 OG, v131 GA, v132 GA} = 1 OG ≤ 1).

## One-line

AI memory + context engine / "Memory API for the AI era": auto-extracts facts, builds static+dynamic user profiles, hybrid RAG+memory search, auto-forgets, multi-modal ingest. **#1 on LongMemEval (81.6%)/LoCoMo/ConvoMem.** Dev SDK (npm+pip TS/Python) + **MCP server** (Claude Desktop/Cursor/Windsurf/VS Code/Claude Code) + **Claude Code plugin** (separate repo) + in-repo agentskills.io `skills/supermemory/SKILL.md` + MemoryBench + connectors (Drive/Gmail/Notion/GitHub) + a consumer app/browser-extension. Bun+Turbo monorepo, Cloudflare/Drizzle/Postgres/Remix. MIT, TypeScript. By **supermemoryai** (US-based "research lab" org). **23,726★ / ~825d / ~29★/d lifetime, lower-edge SUSTAINED-MODERATE-HIGH** (long-lived steady accruer, recent ramp higher). Uses Claude Code in its own CI (claude.yml + claude-code-review + claude-auto-fix-ci + CLAUDE.md).

## Pattern Library impact

**PRIMARY: Pattern #85 "Platform-Primitive Foundation" / Agent-Memory-System sub-archetype → N=2** (v66 agentmemory + v132 supermemory; 2nd dedicated agent-memory platform-primitive, strong cross-scale spread — v66 small OSS vs supermemory large benchmark-leading hosted-SaaS; promotion-eligible at N=3; ⚠️ confirm against Pattern #85's exact criteria at audit).

**SECONDARY (observations; 1 standalone filed — §28):** **NEW Library-vocab standalone (N=1, FILED to registry 06 section C):** "Open Comparative Benchmark Framework for Own Category" (MemoryBench benchmarks self + named competitors Mem0/Zep; supermemory is #1 on the external benchmarks; CORPUS-FIRST; promotion-eligible at N=2). + agentskills.io 57k chain another-implementer (in-repo SKILL.md + memorybench skill; administrative, CONFIRMED N=3 unchanged); Pattern #18 B1 MCP N+1 (8 clients); Pattern #82 quantitative-marketing (substantiated — #1/81.6%, external benchmark links); internal-Claude-Code-in-CI (v122/v128 engineering-exhaust thread, stronger CI-automation form, NOT the only corpus thread so a different role — noted not conflated).

**§28 filing — DONE not claimed:** the MemoryBench standalone written into `_patterns/06-library-vocab-registry.md` section C this session (1 new standalone ≤ 2 cap). **NO Pattern Library state change** (46 confirmed / 8 Library-vocab CONFIRMED unchanged). **Honest non-claims:** (b) STRONG not STRONGEST (consumer-duality + hosted-SaaS + general-not-dev-specific); **NOT a 3rd instance of the v94/v118 corpus-recursive-at-methodology-influence pattern** (supermemory is a memory engine/DB, not a Karpathy-LLM-wiki/markdown-vault — adjacent, explicitly not counted per v126 discipline); Pattern #85 N=2 is a strengthening not a mint.

## §35 ceiling status (v2.6)

**Ceiling was BREACHED** entering this ship (window {v128 OG, v129 OG, v131 GA} = 2 OG). **v132 = GOAL-ALIGNED INCLUDE → CLEARS the ceiling**: new rolling-3-window = {v129 OG, v131 GA, v132 GA} = **1 OG ≤ 1 → CLEAR** (§35.3). v131 satisfied the §35.2 mandate; v132 is the goal-aligned ship that scrolls v128 out and fully clears. No override; v132 is not an override (override-frequency triggers unchanged).

## Streak (v2.5 §32 forward / v2.6)

Historical **"49+3\*" frozen @v125**. Forward: **`GA:2 · OG:3 [1 ov]` → `GA:3 · OG:3 [1 ov]`** (v132 = 3rd goal-aligned PASS under v2.5/v2.6; consecutive GA stream v131→v132 = 2). Override subset `[1 ov]` UNCHANGED.

## Numbering note

⚠️ Requested as "v133"; built as **v132** (git-authoritative: v131 harness latest ship, v130 audit, no v132). Trivially renamable if a skip was intended.

## Files

- `02 Wiki/index.md` — wiki page.
- `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` — GOAL-ALIGNED INCLUDE gate + §35 ceiling-CLEAR analysis.
- `01 Analysis/(C) Pattern-Library-Phase-4b-Pattern-85-Agent-Memory-Platform-N2.md` — Pattern #85 N=2 + MemoryBench standalone + secondaries.

## Pilot note

**Goal-aligned, genuinely pilot-worthy, low-friction for this operator** (it's the productized version of what the vault does by hand). Fenced trial: `npx -y install-mcp@latest https://mcp.supermemory.ai/mcp --client claude --oauth=yes`, use `/context` + let `memory`/`recall` accrue over a few Claude Code sessions on a SCRATCH/non-sensitive project. **Caveat:** core engine is a **hosted SaaS** (memories on their servers unless self-hosted) → fenced, non-sensitive first; and it's a different model from the vault's hand-curated markdown wiki (fact-extraction DB, not a Karpathy-LLM-wiki). Read `concepts/memory-vs-rag` + `skills/supermemory/references/architecture.md` regardless. Complements v126 compound-engineering + v131 harness (all three still un-piloted).
