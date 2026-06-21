# (C) Phase-0.9 Verdict — v175 PilotDeck — GOAL-ALIGNED INCLUDE 3/4

**Subject:** `OpenBMB/PilotDeck` · **Date:** 2026-06-20 · **Routine:** LLM Wiki Routine v2.6
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — `(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG`
**§31 tier-key:** (b) MODERATE+ → **GOAL-ALIGNED** (not OFF-GOAL). (a) does NOT key the tier.

---

## Criterion (a) — Storm Bear cultural-peer / identity axis → **FAIL (clean, no axis)**

- **Author = OpenBMB**, an institutional umbrella: *"Open Lab for Big Model Base … towards AGI,"* jointly developed here by **Tsinghua University THUNLP + ModelBest + OpenBMB + AI9Stars**.
- **Not Anthropic** → fails (a)-7 (Anthropic-only).
- A **major institutional AI lab** is not the *individual cultural-peer* axis. The cultural-peer axis is for an individual peer building in public (a solo VN/Asia dev), not a mega-org / academic lab. This is the **declared-non-Anthropic-institution** situation: matches **ByteDance v143** (declared Chinese corporation, FAIL), **NVIDIA v169** (corporate-not-Anthropic, FAIL), **Google v140**.
- A "Chinese-origin / academic-lab heritage" inference is **NOT an (a)-rescue** — the v159→v174 discipline + standing recommendation (ii) (require a *solid* declared/located individual signal or registered (a)-7; not a heritage inference). OpenBMB's identity is *declared* (so not even an inference question) — it's simply an institution, not a peer.
- **Note (not a rescue):** this is the **first OpenBMB / THUNLP / Tsinghua-lineage subject** in the corpus, and the first *academic-lab* author (vs the prior commercial-vendor FAILs ByteDance/NVIDIA/Google). That distinction is logged as a **(d)/identity data-point** (Pattern #19 19a institutional-portfolio), NOT a new (a) axis.

**Result: (a) FAILS, no axis minted.** This does not lower the tier — §31 keys on (b).

---

## Criterion (b) — goal-relevance → **STRONG** (the tier-keying criterion)

Goal #1 = *"Master Claude and autonomous agents for software development."* PilotDeck is **dead-center**:

1. It is a **full autonomous-agent operating system** — long-lived agents, always-on background execution, task discovery, WorkSpace isolation. This *is* the autonomous-agent substrate the goal is about.
2. **Native Anthropic/Claude support** (one of OpenAI / Anthropic / DeepSeek / Qwen / Kimi / MiniMax / OpenAI-compatible).
3. **White-box editable/rollback memory** lands directly on the operator's **CC-memory-systems** pilot thread *and* on the vault's own pain point — the **584 KB CLAUDE.md context-pollution** refactor is exactly the failure mode "WorkSpace-Level Isolation … avoiding global context pollution" is designed to prevent. This is a study-relevant *memory-architecture reference*.
4. **Smart routing** lands on the **claude-api-cost-optimization** thread (task-difficulty → flagship vs light model).
5. **MCP native.**

**STRONG, not STRONGEST:** it is a *third-party* agent runtime that *uses* Claude as one provider among several — a complementary/alternative platform, not the Anthropic substrate itself. STRONGEST is reserved for the substrate (Claude/Anthropic) or a methodology directly embodying the vault's own pattern. This is the same STRONG-not-STRONGEST calibration as OpenHuman v118, devspace v171, Agent-Reach v174.

→ **(b) STRONG ⇒ GOAL-ALIGNED INCLUDE.**

*(Operator-reviewable alternative: one could argue (b) is the single strongest in the recent run, since PilotDeck bundles agent-runtime + memory + routing + MCP all on-goal. Either way the tier is GOAL-ALIGNED; recorded, not minted.)*

---

## Criterion (c) — engineering substance → **STRONG**

- TS-heavy full platform (TS 70.8% / JS 22.1% / Python 3.8%): WorkSpace-isolation engine, white-box memory store with rollback, **Dream Mode** idle consolidation, **ClawXRouter** smart routing, **ClawXMemory** memory system, **MCP host**, multi-frontend (Web/CLI/IM), lifecycle hooks (`PreToolUse`/`UserPromptSubmit`), pluggable memory-store providers.
- Built on OpenBMB's own component stack (ClawXRouter / ClawXMemory / **UltraRAG**) + UI (Vite/React/Tailwind/shadcn).
- Three install paths (one-line / source / Docker-compose). Institutional engineering weight (Tsinghua THUNLP / ModelBest).
- **Caveat (honest):** young — v0.1.0, **1 release**, open-sourced ~3 weeks ago (2026-05-28). The surface is substantial but the maturity is early.

---

## Criterion (d) — connectivity → **STRONG**

- **Family sibling:** OpenHuman v118 (self-contained agentic platform) — but distinct organizing primitive (see PRIMARY doc).
- **Memory-engine contrast:** agentmemory v66 (4-tier auto-consolidation) / supermemory v132 (MemoryBench) / codebase-memory-mcp v172 (code graph) — PilotDeck's white-box editable/rollback memory is a contrasting *design*.
- **Distinct from** orchestration platforms (Paseo v150 / ai-maestro v163 §C #23), multiplexers (cmux v99 / AoE v162), GUI client (CodePilot v161 §C #27).
- **Pattern #57 corpus-recursive cross-reference (genuine):** README thanks *"Agent OS pioneers such as OpenClaw, Claude Code, Codex, Cursor, and Hermes for their explorations"* — an explicit influence-acknowledgment of corpus subjects (stronger than the recent "mentions ≠ recursion" cases, where subjects were only named as *clients*). NOT a #57 promotion; a real data-point.
- Threads: CC-memory-systems, claude-api-cost-optimization, MCP (#18 consumer side), Dream-Mode memory-consolidation echo.

---

## Streak / ceiling / counts

- **Streak (v2.5 §32 forward-only):** GA:36 → **GA:37 · OG:11 [7 ov]**. (37th goal-aligned PASS; NOT an override; historical "49+3*" frozen @v125.)
- **§35 soft off-goal ceiling: CLEAR.** Rolling-3-ship window {v173 GA, v174 GA, **v175 GA**} = **0 OFF-GOAL** (≤1 holds).
- **22 consecutive goal-aligned ships v153→v175.** Stays on the **goal-#1 substrate core** (5th consecutive core-substrate ship after v171/v172/v173/v174).
- **Override-frequency triggers (2-in-20 / 3-in-30):** UNCHANGED (this is not an override; lifetime overrides = 10).
- **Counts UNCHANGED: 46 confirmed patterns / 10 CONFIRMED Library-vocab.** §C live-standalone surface ≈32 → **≈33** (+1 N=1).

---

## Build method & verification (honest disclosure)

- **Verdict produced inline** (NOT the multi-agent build workflow). Rationale: (1) Ultracode was off for this session; (2) the v171 ship established that an inline §31 read is at least as reliable for a (b)-keys-the-tier verdict; (3) the `feedback_wiki_verify_independently_check_collisions` memory documents that the 3-lens+critic workflow has *confabulated* corpus facts (v174: a lens invented a "v142 claude-web-research" collision) — so independent verification is the load-bearing safeguard, and it was done by hand here.
- **Independent verification performed:** grep over `_state/*.md` + `_patterns/*.md` for OpenBMB/ChatDev/UltraRAG/MiniCPM/agent-OS/white-box-memory/smart-routing collisions; 2× WebFetch (repo page + raw README) + 1× WebFetch (OpenBMB org page). Confirmed: (i) **first OpenBMB subject** (only "MiniCPM" model-name prior); (ii) OpenHuman v118 anchors **no** §C standalone (no priority to erase); (iii) **no existing agent-OS / WorkSpace-isolation / white-box-memory standalone** in §C; (iv) PilotDeck ≠ the orchestration-platform / multiplexer / GUI-client / pluggable-memory-engine classes.
- **inflation_check:** 1 mint (≤2 cap honored), N=1 correct (corpus-first), max top-level pattern stays #85, counts 46/10 unchanged, no improper N-bumps, no double-count.

---

## Honest non-claims

- (a) genuinely **FAILS** (institutional non-Anthropic lab; not a cultural peer; no axis).
- (b) **STRONG not STRONGEST** (third-party runtime using Claude as one provider).
- **GOAL-ALIGNED, not OFF-GOAL** (§35 clear; not an override).
- The mint is **1 capability standalone at N=1 (CORPUS-FIRST)**, **NOT** a new top-level pattern (no #86).
- **NOT #52** (metrics page-stated, NOT API-verified; velocity unestablishable).
- **NOT #18 B1-MCP** (MCP host/consumer, not a one-server-many-clients server).
- **NOT** an orchestration platform (#23), multiplexer (cmux/AoE), GUI client (CodePilot v161 §C #27), or pluggable memory engine (agentmemory/supermemory).
- Cost/benchmark figures are the **project's own unreplicated single-scenario** claims.
- **NO confirmed-count change (46/10).**
