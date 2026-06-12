# (C) CodePilot — Phase 0 scope gate + Phase 0.9 four-axis verdict

**Subject:** `op7418/CodePilot` (v161 wiki ship, 2026-06-05). **Routine:** v2.6 (§31 / §35 / §37).
**Requested:** "build LLM wiki for op7418/CodePilot ... macOS app to manage multiple AI coding tools."

## Phase 0 — scope gate
**In scope, and a domain-shift from the v153–v160 monitor niche.** The request framed it as another "manage multiple AI coding tools" subject, but CodePilot is functionally a different archetype: it is the **client/operating surface itself** — a native desktop GUI for Claude Code that you chat/code/run-sessions in — not a menu-bar/notch tool that watches or switches your agents from the outside. It is squarely goal #1 (operating Claude Code + multiple AI coding tools) and a real heavy-Claude-Code vault workflow. Nearest neighbors: v150 Paseo (orchestration platform), v118 OpenHuman (agentic desktop assistant), the #18 #8 aggregator cluster — NOT the v153–v160 observability/management-utility niche.

## Phase 0.9 — STRICT four-axis verdict: **GOAL-ALIGNED INCLUDE 4/4**

**(a) Cultural-peer / vendor-direct — PASS.**
`op7418` = **歸藏 / Guizang** (guizang.ai, @op7418 on X) — a known Chinese AI KOL and a **recurring corpus cultural-peer**: v105 guizang-social-card-skill is his, and v83 open-design bundles his `skills/guizang-ppt/`. This is a **declared, identity-confirmed** cultural-peer (China-Mainland cluster N+1), not a handle-inference — the first genuine (a) PASS since the v153–v160 run of FAILs/handle-inferences. Held **PASS (solid), not STRONGEST**: Guizang is primarily a designer/KOL rather than a pure software-development peer, but he ships real agent dev tooling (prompts repo, Claude-to-IM skills, now a full Electron Claude Code client), so a clear PASS.

**(b) Goal-relevance — STRONG (not STRONGEST).**
A visual desktop GUI client/front-end for Claude Code + 17-provider aggregation + MCP/skills + remote control is dead-center goal #1 (master Claude + multiple AI coding tools) AND a genuine vault workflow — and it is the *operating surface*, arguably more central than the monitors that merely watch it. **STRONG-not-STRONGEST** = it is still a third-party GUI wrapper *around* the Claude substrate, not the substrate (Claude itself) or a methodology (the established v150 Paseo / cluster calibration). Near-STRONGEST given breadth.

**(c) Engineering quality — STRONG.**
Next.js 16 + Electron 40 + Claude Agent SDK + Vercel AI SDK + Radix/shadcn + Tailwind 4 + Motion; 17+ provider adapters; MCP stdio/sse/http with runtime monitoring; session pause/resume/rewind-to-checkpoint; split-screen dual sessions; skills system + skills.sh marketplace; remote bridge across 5 messaging platforms; task scheduler; media studio; local SQLite (WAL). **1,160 commits / v0.55.1** = mature, broad, sophisticated multi-integration app. (The "built in a day, AI-assisted" origin is a marketing claim about *velocity*, not a quality deduction — the artifact is substantial.)

**(d) Corpus connectivity — STRONG.**
High connectivity: Pattern #18 #8 Multi-Source LLM Aggregator (CONFIRMED N=3) N+1; T4c Operator-Notification/Control-Bridge via Messaging Platform (v88 teleport) N+1; agentskills.io / skills.sh (57k-adjacent); agent-memory persona files (v66/v132); observability token/cost analytics; **op7418/Guizang corpus-recursive** (v105 + v83 → 3rd appearance); Pattern #19 Chinese-AI-KOL N+1; Electron (contrast the Swift-native cluster); LV-C3 self-referential AI-built (SOFT).

## §35 — STAYS CLEAR
Window {v159 GA, v160 GA, **v161 GA**} = 0 OG (nine consecutive goal-aligned ships v153→v161). NOT an override → override-frequency UNCHANGED (lifetime 10). Streak GA:23·OG:11 [7 ov] → **GA:24·OG:11 [7 ov]** (24th GOAL-ALIGNED PASS).

## §37 — provenance (NOT API-verified)
≈**5.9k★** / 641 forks / 369 open issues / 74 PRs / **1,160 commits** / v0.55.1 (Jun 4 2026) / **BSL-1.1** (free for personal/academic/non-profit; commercial requires a separate license; change-date 2029-03-16 → Apache 2.0) / TypeScript 97.5% / Electron 40 + Next.js 16 / cross-platform. Created ~Feb 11 2026 (blog.bonza.cn + Guizang's X launch thread). Page-stated via WebFetch + WebSearch, **NOT independently API-verified (§37.4)** — env mocks the GitHub API. ~115 days × ~51★/d ≈ SUSTAINED-MODERATE-HIGH band IF accurate → **velocity NOT API-verified → NOT a #52 claim.** Owner op7418 = 歸藏/Guizang.

## Honest non-claims
- **(a) genuinely PASSes** — Guizang is a declared, recurring corpus cultural-peer (NOT a handle-inference; the v139/v151 discipline is satisfied because the identity is established, not guessed). Held PASS (solid), not STRONGEST.
- **(b) held STRONG, not STRONGEST** — a third-party GUI wrapper around Claude, not the substrate/methodology.
- **NOT a clean LV-C7 #22 instance** — #22 = a management-GUI that *switches config/accounts* (cc-switch/CodexPlusPlus/ai-switcher, Tauri); CodePilot's identity is a *full client/front-end* you operate Claude Code in, not a config-switcher (it has a control dimension but that is one feature of a broad client). Filing it as a 4th #22 would repeat the v118-OpenHuman-vs-LV-C7 honest-downgrade error ("uses a desktop GUI" ≠ "is a management-GUI"). It mints its own §C standalone instead.
- **NOT a new top-level Pattern** — the new shape is a §C standalone (N=1), not a top-level pattern.
- **Pattern #18 #8 = instance-strengthening, not a new sub-variant** — 17-provider aggregation in a GUI client is a clean N+1 of the CONFIRMED sub-archetype; a "GUI-client aggregator" sub-variant is flagged for the audit, NOT minted now (anti-inflation).
- **Persona-memory files (`claude.md`/`memory.md`) are NOT a Karpathy-LLM-wiki** — agent-memory adjacency (v66/v132), declined as a v94/v118/v134 corpus-recursive instance (it is per-assistant memory, not a self-maintaining knowledge wiki).
- **LV-C3 self-referential build is SOFT** — "built in a day entirely by AI (Opus 4.6 + Agent Teams + Claude Code)" is Guizang's launch claim, not an in-repo generator stamp; recorded as a soft observation, not counted.
- **NOT a #52 claim** (creation date + stars page-stated; API mocked §37.4).
- **BSL-1.1** is a notable license shape (source-available, commercial-gated, time-delayed to Apache) — recorded as a Pattern #45 sub-variant observation, not minted.
