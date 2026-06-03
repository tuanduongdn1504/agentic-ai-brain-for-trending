# Paseo — Wiki (v150)

> **One line:** **"One interface for Claude Code, Codex, Copilot, OpenCode, and Pi agents"** — *"Coding agents from your phone, desktop and CLI."* A cross-device, multi-vendor **coding-agent orchestration platform** that ships a `/paseo-*` skill suite teaching an agent to orchestrate *other* agents.
> **Tier:** T2 Service (cross-device multi-vendor coding-agent orchestration platform) + bundled T1 skill suite. **Verdict:** GOAL-ALIGNED INCLUDE 3/4 (a FAIL · b/c/d STRONG).
> **Repo:** `getpaseo/paseo` · AGPL-3.0 · TypeScript 98.7% (+ Swift / Kotlin / Nix / Shell) · org `getpaseo` (@moboudra).
> **§37 provenance:** ≈7.4k★ / 707 forks / 23 watchers / 395 open issues / v0.1.89 (Jun 2 2026) / 110 releases / 3,695 commits (page-stated as of 2026-06, repo page — *NOT independently API-verified; this env mocks the GitHub API §37.4*). Young (v0.1.x), creation date not stated → velocity/age unestablished → **NOT a Pattern #52 claim.**

## Why it's in the corpus (and why it's a strong goal-#1 subject)
This is about as dead-center on goal #1 ("master Claude and autonomous agents for software development") as a subject gets: Paseo is a **control plane for coding agents**. It runs heterogeneous third-party agents — **Claude Code, Codex, GitHub Copilot, OpenCode, Pi** — as the orchestration units, self-hosted on your machine with full dev-environment access, drivable from **iOS / Android / desktop / web / CLI**, with voice control and a privacy-first ("no telemetry / no forced login") posture.

The genuinely novel part: it ships a **skill suite that teaches an agent to orchestrate *other* agents** —
> "Skills teach your agent to use Paseo to orchestrate other agents."

`/paseo-handoff` · `/paseo-loop` · `/paseo-advisor` · `/paseo-committee` (across `.claude/skills` + `.agents/skills` + `AGENTS.md`). That's an **agent-of-agents** recursion: one agent uses Paseo skills to spawn/route/hand-off to a *committee* of other vendor agents.

## How it's used
```
npm install -g @getpaseo/cli
paseo run --provider claude/opus-4.6 "implement user authentication"
paseo ls
paseo attach [id]
paseo send [id] "follow-up task"
```
Desktop/mobile apps at `paseo.sh/download` or GitHub releases. TypeScript 98.7% core; Swift (iOS) + Kotlin (Android) clients; Nix; AGPL-3.0.

## Corpus connectivity
- **Multi-agent-orchestration cluster** — nearest neighbor is **v99 cmux** (native-desktop terminal multiplexer hosting multiple coding agents). Paseo is **ADJACENT, not the same**: cmux is single-device session-hosting a human drives; Paseo is *cross-device, multi-vendor orchestration* where a `/paseo-*` skill lets one agent orchestrate others. Also relates to v131 harness (generates a multi-agent *team's architecture*; Paseo *runs* heterogeneous vendor agents) + v126 compound-engineering + v94/v118.
- **Pattern #84 multi-harness / cross-vendor ecosystem-tolerance** — N+1 (orchestrates 5 vendor agents; `.claude/skills` + `.agents/skills` + AGENTS.md).
- **Library-vocab #12 routing-artifacts** — N+1 (AGENTS.md + `.claude/skills` + `.agents/skills`).
- **Multi-Source aggregator (Pattern #18 #8) — ADJACENT, NOT counted** — #8 aggregates LLM *providers* (cc-switch/freellmapi/CodexPlusPlus, a lower layer); Paseo aggregates *agents* (a layer up). Observation only, not a #8 instance (the v123 anti-dilution discipline).
- **`/paseo-*` skills = Paseo-native, npm-distributed (`@getpaseo/cli`)** — NOT asserted as a 57k `npx skills add` agentskills.io implementer (the v143/v149 discipline); flagged as a candidate for chain reconciliation, not claimed.
- See `01 Analysis/` for the full verdict + Phase 4b (PRIMARY = NEW Library-vocab standalone "Cross-Device Multi-Vendor Coding-Agent Orchestration Platform" N=1 CORPUS-FIRST).

## §35 — Soft Off-Goal-Rate Ceiling
**STAYS CLEAR.** v149 already cleared the v146/v148 breach; a GOAL-ALIGNED v150 keeps it clear — rolling-3-ship window {v148 OG, v149 GA, v150 GA} = **1 OG ≤ 1 → CLEAR.** v150 is NOT an override; override-frequency triggers UNCHANGED (lifetime 9; still 6-in-20 → next audit RE-MANDATED, but v150 adds nothing to it).

## Pilot note — Tier-1, genuinely
Directly goal-#1 and genuinely usable: Paseo orchestrates **Claude Code itself** (plus Codex/Copilot/OpenCode/Pi) from phone/desktop/CLI. For a software dev + Scrum coach, "drive Claude Code from anywhere + orchestrate a committee of agents" is a real workflow. Lowest-friction, reversible: `npm install -g @getpaseo/cli` → `paseo run --provider claude/... "task"`. **`install-snapshot` recommended** (global npm install + a desktop app). Joins v144 headroom + v149 Scrapling as the directly-vault-applicable goal-aligned pilots.

## Honest non-claims
- (a) genuinely FAILS — org `getpaseo`, @moboudra (founder; name/location not stated on the page); inferred MENA/Arabic-speaking from the handle, undeclared — **not** a registered cultural-peer axis, **not** (a)-7; **no axis minted** (the v139/v149 discipline). The v149 Scrapling + v150 Paseo back-to-back inferred-MENA authors is an *observation only*, not a minted axis.
- (b) STRONG, near-STRONGEST — held at STRONG (not STRONGEST) because it's a third-party orchestration **product/control-plane**, not the agent substrate (Claude itself) or a methodology; but it is one of the most goal-central subjects in the recent corpus.
- Metrics page-stated, NOT API-verified; **NOT a #52 claim** (young, creation date unestablished here).
- Phase 4b: **1** new standalone (the orchestration-platform shape) + observations; NO new top-level Pattern, NO tier sub-archetype promotion, NO confirmed-count change (46/8).
