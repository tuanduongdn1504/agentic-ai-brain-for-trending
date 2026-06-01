# (C) supermemory — Pattern Library Phase 4b (v132)

**Subject:** `supermemoryai/supermemory`. **Date:** 2026-06-01. **Routine v2.6.**
**Net Pattern Library state change at ship: NONE** (46 confirmed / ~25 active / 8 Library-vocab CONFIRMED unchanged). 1 Pattern-layer strengthening (Pattern #85 → N=2); 1 NEW Library-vocab standalone filed (MemoryBench); the rest are observations. §28 honored (1 new standalone ≤ 2 cap; filed, not just claimed).

---

## PRIMARY — Pattern #85 "Platform-Primitive Foundation" / Agent-Memory-System sub-archetype → N=2

**Claim.** supermemory is the corpus's **2nd dedicated agent-memory-system / memory-as-a-platform-primitive**, after **v66 agentmemory** (which anchored Pattern #85 "Platform-Primitive Foundation" at N=1). Both are foundational *memory* primitives that other agents/apps build on top of (a platform layer, not an end-application).

**Cross-instance spread (why N=2 is meaningful, not a near-duplicate):**
| Axis | v66 agentmemory | v132 supermemory |
|---|---|---|
| Scale | small OSS project | 23,726★, large monorepo, benchmark-leading |
| Backing | self-hosted OSS | hosted SaaS + OSS engine/plugins/SDKs |
| Surface | memory backend | SDK + MCP + Claude Code plugin + connectors + consumer app |
| Author | individual (rohitg00) | US org / "research lab" |
| Evidence | — | #1 on LongMemEval/LoCoMo/ConvoMem |

→ Genuine cross-author + cross-scale spread. **N=2 → promotion-eligible at N=3.**

**⚠️ Honest caveat (load-bearing):** I'm asserting the *agent-memory-system* reading of Pattern #85 from the v66 shim record ("NEW Pattern #85 Platform-Primitive Foundation"), **not** a verified line-by-line match against Pattern #85's full definition (I did not re-read the pattern's confirmed-entry this session). The next audit should confirm supermemory satisfies Pattern #85's exact criteria before treating the N=2 as firm — if Pattern #85 is narrower than "agent-memory platform-primitive," reclassify this as a standalone "Agent-Memory-System / Memory-as-a-Platform sub-archetype N=2 (v66+v132)" instead. Either way the substantive claim — *2nd dedicated agent-memory platform in corpus* — holds.

---

## SECONDARY — 1 NEW Library-vocab standalone (FILED) + observations

### FILED to registry `06` section C: "Open Comparative Benchmark Framework for Own Category" — N=1, CORPUS-FIRST
supermemory ships **MemoryBench** — an *open-source* framework that benchmarks memory providers **head-to-head, including named competitors (Mem0, Zep)** — and supermemory is itself **#1** on the three external benchmarks it points to (LongMemEval/LoCoMo/ConvoMem). The structural move: **a vendor provides the open measuring-stick for its own category and tops it.** Distinct from Pattern #82 (quantitative-marketing = *claiming* numbers) — here the subject *ships the reproducible comparative harness*. CORPUS-FIRST; promotion-eligible at N=2 (a 2nd vendor shipping an open comparative benchmark for its own category). *(1 new standalone — within the §28 ≤2 cap; clustering checked, no existing cluster fits.)*

### Observations (recorded, NOT minted)
- **agentskills.io 57k chain — another implementer:** in-repo `skills/supermemory/SKILL.md` (+ references/{api-reference, architecture, quickstart, sdk-guide, use-cases}) + the `supermemoryai/memorybench` skill via `npx skills add`. Administrative; CONFIRMED N=3 unchanged. ⚠️ exact implementer-count flagged for audit reconciliation (v115 caution — the running count label has been error-prone).
- **Pattern #18 sub-mechanism B1 (MCP, one-server-many-clients) N+1:** an OAuth MCP server (`mcp.supermemory.ai/mcp`) with tools `memory`/`recall`/`context`, 8 listed clients (Claude Desktop/Code, Cursor, Windsurf, VS Code, OpenCode, OpenClaw, Hermes).
- **Pattern #82 quantitative-marketing (substantiated):** "#1 on LongMemEval/LoCoMo/ConvoMem", "81.6%", "~50ms" — but paired with *verifiable external benchmark links*, so it's substantiated, not puffery (contrast the un-replicated v131 "+60%" claim).
- **Internal Claude-Code-in-CI:** `.github/workflows/{claude.yml, claude-code-review.yml, claude-auto-fix-ci.yml}` + root `CLAUDE.md` = the v122/v128 "engineering-exhaust" thread, here in a *stronger* full-CI-automation form. **NOT conflated with the v122/v128 framing** (which was specifically "off-goal subject whose *only* corpus thread is internal Claude") — supermemory is goal-aligned with abundant direct corpus surface, so its internal Claude usage is a different role. Noted, not counted toward that N-tally.
- **Connectivity threads:** Hermes (NousResearch/hermes-agent, v78/v112), n8n (v53), Claude Memory Tool (Anthropic foundational-vendor adjacency), Mem0/Zep competitor-mapping.

---

## §28 compliance + honest non-claims

- **1 NEW Library-vocab standalone** (MemoryBench "Open Comparative Benchmark Framework for Own Category"), **actually written** into `_patterns/06-library-vocab-registry.md` section C this session (v120 rule-5: "filing is an act"). Within the §28 ≤2-new-standalones cap.
- **Pattern #85 → N=2 is a strengthening, not a mint** (Pattern-layer; recorded in wiki + shim, not the Library-vocab registry).
- **(b) STRONG, not STRONGEST** — consumer-product duality + hosted-SaaS core + general-not-dev-specific; not inflated (STRONG already cleared the §35 ceiling).
- **NOT a 3rd instance of the v94/v118 corpus-recursive-at-methodology-influence pattern.** supermemory is a memory *engine/database* (fact-extraction + RAG + user profiles), **not** a Karpathy-LLM-wiki / Obsidian-markdown-vault structure like v118 OpenHuman. It's conceptually a "brain" (adjacent), but architecturally different — explicitly **not counted** (the v126 audit's no-manufactured-corpus-recursive discipline). This is the one tempting over-claim, and I'm declining it.
- **NO new top-level Pattern; NO Pattern Library state change at ship** (46 confirmed / 8 Library-vocab CONFIRMED unchanged).

## Next-audit queue items from v132
1. **Pattern #85 N=2** — verify against Pattern #85's exact definition; if it doesn't match, reclassify as an "Agent-Memory-System / Memory-as-a-Platform sub-archetype N=2." Promotion-eligible at N=3.
2. **MemoryBench "Open Comparative Benchmark Framework for Own Category"** — N=1 standalone; promotion-eligible at N=2.
3. **agentskills.io implementer-count reconciliation** (carried from v115) — still owed.
4. **§35 ceiling CLEARED at v132** — confirm the rolling-window accounting ({v129 OG, v131 GA, v132 GA} = 1 OG).
