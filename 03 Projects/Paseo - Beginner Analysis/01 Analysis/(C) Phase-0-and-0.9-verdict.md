# (C) getpaseo/paseo — Phase 0 + Phase 0.9 STRICT verdict (v150)

**Subject:** `getpaseo/paseo` — https://github.com/getpaseo/paseo
**Date:** 2026-06-03 · **Routine:** v2.6 (§31 + §35 + §37)
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG

---

## Phase 0 — scope gate
**Squarely in scope — one of the most goal-#1-central subjects in the recent corpus.** Paseo is a **control plane for coding agents**: *"One interface for Claude Code, Codex, Copilot, OpenCode, and Pi agents… coding agents from your phone, desktop and CLI."* It runs heterogeneous third-party coding agents as the orchestration units (self-hosted, full dev-env access), cross-device (iOS/Android/desktop/web/CLI), voice-controllable, privacy-first — and ships a `/paseo-*` **skill suite that teaches an agent to orchestrate other agents**. Goal #1 is "master Claude and autonomous agents for software development"; an orchestration layer over Claude Code + peers is dead-center.

## Phase 0.9 STRICT — four axes

### (a) Cultural-peer / geographic — **FAIL**
- Owner = org `getpaseo`; the badge shows **@moboudra** (the founder; **name/location not stated on the repo page**). Inferred MENA/Arabic-speaking from the handle ("Boudra" is a Maghrebi surname) — **inference only, undeclared**.
- MENA/Arabic-speaking is **not a registered cultural-peer (a) axis** and this is **not (a)-7**. Per the v139 / v149 discipline, **(a) FAILs and NO axis is minted** for an inferred-only single subject. No rescue.
- **Observation (NOT minted):** v149 Scrapling (Karim Shoair) + v150 Paseo (@moboudra) are back-to-back inferred-MENA/Arabic-speaking authors. Noted for the audit; **no axis minted** (inferred-only; the exact (a)-8 over-minting trap retired at v115).
- (a) FAIL is immaterial — this is a GOAL-ALIGNED-on-(b) INCLUDE (cf. v140/v143/v144/v149: a FAIL + b STRONG).

### (b) Goal-relevance — **STRONG** (load-bearing; near-STRONGEST)
- A **multi-vendor coding-agent orchestration platform** — it orchestrates **Claude Code + Codex + Copilot + OpenCode + Pi** as units, self-hosted, cross-device, with a skill suite (`/paseo-handoff` / `/paseo-loop` / `/paseo-advisor` / `/paseo-committee`) that lets one agent orchestrate others ("agent-of-agents"). This is core goal-#1 infrastructure for autonomous coding agents — broader than v99 cmux (which got (b) STRONG as a single-device session multiplexer).
- **STRONG, not STRONGEST:** held at STRONG because Paseo is a third-party orchestration **product/control-plane** (with a hosted desktop/mobile app + privacy-first marketing), not the agent *substrate* (Claude itself) or a *methodology* (the v126/v131 STRONGEST bar). It is, however, at the strong end — one of the most goal-central subjects in the recent corpus. No §35 pressure to inflate (the ceiling is already clear post-v149).

### (c) Instructive engineering — **STRONG**
Self-hosted agent execution with full dev-env access; a multi-vendor provider abstraction (`--provider claude/opus-4.6`); cross-device clients (Swift iOS + Kotlin Android + TS web/desktop/CLI); a skills system; Nix; privacy-first architecture (no telemetry/forced login). Actively shipped — TypeScript 98.7%, 110 releases, v0.1.89, 3,695 commits. (395 open issues = active-but-rough; doesn't materially dent (c).) STRONG.

### (d) Corpus connectivity — **STRONG**
- **Multi-agent-orchestration cluster** — v99 cmux (ADJACENT: single-device session multiplexer vs Paseo's cross-device multi-vendor orchestration) + v131 harness (generates a team's architecture) + v126 compound-engineering + v94/v118.
- **Pattern #84 multi-harness / cross-vendor ecosystem-tolerance** — N+1 (5 vendor agents; `.claude/skills` + `.agents/skills` + AGENTS.md).
- **Library-vocab #12 routing-artifacts** — N+1 (AGENTS.md + `.claude/skills` + `.agents/skills`).
- **Pattern #18 #8 Multi-Source aggregator — ADJACENT, NOT counted** (Paseo aggregates *agents*, a layer above the LLM-*provider* aggregation of cc-switch/freellmapi/CodexPlusPlus). Observation only (anti-dilution).

---

## §35 — Soft Off-Goal-Rate Ceiling — **STAYS CLEAR**
- v149 cleared the v146/v148 double-`[ceiling-override]` breach. After a GOAL-ALIGNED v150: rolling-3-ship window {v148 OG, v149 GA, v150 GA} = **1 OG ≤ 1 → CLEAR.**
- v150 is a clean goal-aligned ship — **NOT a ceiling-override.** Override-frequency triggers UNCHANGED (lifetime overrides still 9; the 6-in-20 trip stands → next audit RE-MANDATED, but v150 adds nothing to it).

## §37 — Fact-provenance
≈**7.4k★** / 707 forks / 23 watchers / 395 open issues / v0.1.89 (Jun 2 2026) / 110 releases / 3,695 commits / AGPL-3.0 / TypeScript 98.7% (+ Swift/Kotlin/Nix/Shell) (page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified §37.4**; this env mocks the GitHub API). Young (v0.1.x), creation date not stated on the page → velocity/age unestablished → **NOT a Pattern #52 claim.** Owner org `getpaseo`; @moboudra founder, name/location undeclared → (a) FAIL, no axis minted.

## Streak (v2.6 §32)
GA:14 · OG:9 [6 ov] → **GA:15 · OG:9 [6 ov]** (v150 = 15th goal-aligned PASS; §35 STAYS CLEAR; "49+3\*" frozen @v125; lifetime overrides 9 UNCHANGED — v150 is not an override).

## PILOT — Tier-1, genuinely
Directly goal-#1 and genuinely usable for a software-dev + Scrum coach: orchestrate **Claude Code itself** (+ Codex/Copilot/OpenCode/Pi) from phone/desktop/CLI, with a `/paseo-committee`-style agent-of-agents workflow. `npm install -g @getpaseo/cli` → `paseo run --provider claude/... "task"`; reversible. **`install-snapshot` recommended** (global npm install + desktop app). Joins v144 headroom + v149 Scrapling as the directly-vault-applicable goal-aligned pilots.

## Honest non-claims
- (a) genuinely FAILS (org/founder, inferred-MENA-only, undeclared; no axis minted; the back-to-back-MENA-inferred note is an observation, not a mint).
- (b) STRONG-not-STRONGEST (third-party orchestration product/control-plane, not the agent substrate or a methodology) — though near-STRONGEST.
- Metrics page-stated, NOT API-verified; NOT a #52 claim.
- Phase 4b: **1** new standalone (orchestration-platform shape; cmux ADJACENT, not the same) + observations; NO new top-level Pattern, NO tier sub-archetype promotion, NO confirmed-count change.
