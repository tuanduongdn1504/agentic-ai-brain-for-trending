# (C) Paseo — Pattern Library Phase 4b (v150)

**Routine v2.6 · §28 (single registry / ≤2-new-standalones / clustering-first / filing-is-an-act).**

## PRIMARY — 1 NEW Library-vocab standalone (FILED to registry 06 §C)

### "Cross-Device Multi-Vendor Coding-Agent Orchestration Platform (agent-of-agents via a skill suite)" — N=1 CORPUS-FIRST
- **What:** a platform that orchestrates **heterogeneous third-party coding agents** (Claude Code / Codex / Copilot / OpenCode / Pi) as the orchestration *units*, self-hosted with full dev-env access, drivable across **iOS / Android / desktop / web / CLI**, and shipping a `/paseo-*` **skill suite** (`/paseo-handoff` / `/paseo-loop` / `/paseo-advisor` / `/paseo-committee`) that teaches one agent to orchestrate the others — an **agent-of-agents** control plane.
- **Why it's its own mechanism (the distinct combination):** the corpus has multi-agent subjects, but each differs on a load-bearing axis:
  - **v99 cmux** = a native-**desktop** terminal multiplexer that *hosts* multiple coding-agent sessions a **human** drives — single-device, session-hosting. Paseo is **cross-device** and the *agent itself* orchestrates other agents via skills. **Nearest neighbor → ADJACENT, not the same.**
  - **v131 harness** = *generates* a bespoke multi-agent **team's architecture** (Pipeline/Supervisor/…); it doesn't *run* heterogeneous third-party vendor agents.
  - **v126 compound-engineering** = a methodology plugin (agents within one harness).
  - **Pattern #18 #8 Multi-Source LLM Aggregator** (cc-switch/freellmapi/CodexPlusPlus) = routes LLM **providers** — a **lower layer** than orchestrating *agents*.
  - The corpus-first combination = *heterogeneous-vendor coding-agent orchestration, as a cross-device product, with a skill suite that makes one agent the orchestrator of others.*
- **Promotion-eligibility:** N=2 if a 2nd cross-device multi-vendor agent-orchestration platform (agent-of-agents) appears. **Stale-watch ~v165.**
- **§28 new-standalone count this ship = 1 (≤ 2).** Registry 06 §C + §F edited (rule-5).

## SECONDARY — observations + instance notes (§28-disciplined, NOT minted)

- **Pattern #84 multi-harness / cross-vendor ecosystem-tolerance — N+1.** Orchestrates 5 vendor agents; ships `.claude/skills` + `.agents/skills` + `AGENTS.md`. Instance note; top-level count UNCHANGED.
- **Library-vocab #12 LLM-routing artifacts — N+1.** `AGENTS.md` + `.claude/skills` + `.agents/skills`.
- **Pattern #18 #8 Multi-Source aggregator — ADJACENT, NOT counted.** Paseo aggregates *agents* (a layer up), not LLM *providers* — counting it as a #8 instance would dilute #8 (the v123 anti-dilution discipline). Observation only; recorded for the audit's "multi-AGENT vs multi-PROVIDER aggregation layer" distinction.
- **`/paseo-*` skill suite = Paseo-native, npm-distributed (`@getpaseo/cli`) — OBSERVATION.** NOT asserted as a Pattern #57 57k `npx skills add` agentskills.io implementer (the v143/v149 discipline); the skills are vendor-native, distributed via the Paseo CLI. Flagged as a candidate for the chain reconciliation, not claimed.
- **Back-to-back inferred-MENA/Arabic-speaking authors (v149 Karim Shoair + v150 @moboudra) — OBSERVATION, NOT minted.** Inferred-only; minting a MENA (a)-axis from two inferred handles is the exact (a)-8 over-minting trap retired at v115. Noted for the audit; no axis.
- **AGPL-3.0 — instance note** (copyleft; cf. v142/v145 AGPL). Not minted.
- **Cross-device client breadth (Swift iOS + Kotlin Android + TS web/desktop/CLI) — OBSERVATION.** Multi-platform-client; folded into the PRIMARY's "cross-device" axis, not separately minted.

## Pattern Library state change: NONE
46 confirmed / ~25 active / 8 Library-vocab CONFIRMED → **UNCHANGED.** PROVISIONAL standalone surface +1 (Cross-Device Multi-Vendor Coding-Agent Orchestration Platform). NO top-level Pattern, NO tier sub-archetype, NO confirmed-count movement.

## Audit hand-off note
v150 hands the **overdue ~v139–v140 audit** (now further overdue): (1) the still-open **LV-C1 N=3** promote/split call (v149 Scrapling); (2) the **dense MCP-server B1 line** sub-archetype review (now v66/v70/v119/v132/v134/v140/v141/v144/v149); (3) a NEW **"multi-AGENT orchestration vs multi-PROVIDER aggregation"** layer distinction (Paseo agent-orchestration vs Pattern #18 #8 provider-routing — worth a clean taxonomy line); (4) whether the new "Cross-Device Multi-Vendor Coding-Agent Orchestration Platform" standalone and v99 cmux's "session multiplexer" sub-archetype should be reconciled into one orchestration-tier taxonomy; (5) the standing **6-in-20 override-frequency** review. NOTHING for the override thread from v150 itself (clean goal-aligned ship). The back-to-back inferred-MENA author observation is noted, not actionable (no axis).
