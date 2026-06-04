# (C) ntd4996/agentpet — "AgentPet" (v154 wiki)

> **Status: GOAL-ALIGNED INCLUDE 4/4** ((a) PASS-MODERATE declared-VN · (b) STRONG · (c) STRONG · (d) STRONG). A native-macOS live monitor for multiple AI coding agents — squarely goal #1 and directly vault-applicable. **The ship that fully clears the §35 breach.** Pilot candidate (firmer than v153). See `01 Analysis/` for the verdict + Pattern-Library Phase 4b.

**Repo:** https://github.com/ntd4996/agentpet · **Owner:** Nguyễn Thành Đạt (`ntd4996`, Vietnamese) · **License:** MIT
**Tagline:** *"A native macOS menu-bar application that monitors multiple AI coding agents simultaneously using a desktop-pet character that responds to agent activity states."*

## What it is
An **ambient cockpit for your parallel AI coding sessions.** When you have several agents running (a Claude Code refactor here, a Codex task there, a Gemini CLI job in a third repo), AgentPet sits in the macOS menu bar and shows you — at a glance — what each one is doing, and pings you the moment one finishes or needs your input. The signature touch: a **desktop-pet character** whose mood tracks the *aggregate* state of all your agents (working / waiting / done / celebrate).

## Agents it monitors
- **Claude Code** · **Codex** · **Gemini CLI** · **Cursor** · **Windsurf** · **opencode** · **GLM (Z.AI)**
- **Universal wrapper** — instrument *any* CLI agent via `agentpet run -- <command>`.

## Core features (from the README)
- **Live agent list** — "every agent with a colored status dot, the project, what it's doing, and a per-state timer."
- **Reactive desktop pet** — "reacts to the aggregate state (working / waiting / done / celebrate)."
- **Native notifications** — "when an agent finishes or needs input."
- **Online pet library** — "browse … and download with one click."

## Architecture (the instructive part)
- **Native macOS, Swift 95.9% + SwiftUI**, single SwiftPM package, macOS 13 Ventura+ (Xcode 16 / Swift 6 to build).
- A **Unix-socket daemon** ingests agent events; a **CLI helper** + the **universal `agentpet run --` wrapper** instrument agents that don't emit events natively.
- The clean idea worth borrowing: **decouple event ingestion (socket daemon) from presentation (menu-bar + pet)**, so any agent that can be wrapped becomes observable without bespoke integration.

## Where it sits in the corpus
- It's the **3rd "AI-agent observability" tool** (after **v89 VibeCodingTracker** — usage/cost metering; **v109 cclog-cli** — log/metrics CLI) → that sub-archetype reaches **N=3, promotion-eligible**. AgentPet is the first of the three to do **live, real-time, multi-agent run-state monitoring + ambient notification** rather than after-the-fact metering — a distinct sub-flavor flagged for the next audit.
- Its **reactive desktop-pet UI** is a **corpus-first** UX device for agent observability (affective/ambient signal, not a dashboard) → filed as a new standalone.
- It's **native Swift**, joining the Swift-primary macOS cluster (v99 cmux, v100 Easydict). Note it's **not** Tauri, so it is *not* an LV-C7 management-GUI (v73/v117/v153) — a different layer: those *control* agents, this *observes* them.
- It does **not** aggregate LLM providers, so it's **not** a Pattern #18 #8 instance. It rounds out the multi-{provider / agent-orchestration / account / observability} taxonomy: PROVIDER=#8 · AGENT-orchestration=v150 Paseo · ACCOUNT-mgmt=v153 ai-switcher · **AGENT-observability=v89/v109/v154**.

## Provenance (§37)
≈**40★** / 10 forks / **114 commits** / latest **v1.1.6** (Jun 4 2026) / MIT / Swift 95.9% / native macOS menu-bar.
*Page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified (§37.4)**; this environment mocks the GitHub API.* Micro-scale → **NOT a Pattern #52 claim.** Owner Nguyễn Thành Đạt (`ntd4996`, Vietnamese declared, location undeclared).

## Why it's goal-aligned (and a real pilot)
- **On goal #1:** the subject *operates/observes* multiple coding agents — agent infrastructure, not an app that merely calls an LLM.
- **Directly vault-applicable:** Storm Bear runs Claude Code heavily; live status + "needs input" notifications across parallel sessions is a concrete workflow win.
- **Firmer pilot than v153:** MIT-licensed, mature (114 commits / v1.1.6). Native macOS — build with Xcode 16/Swift 6 or grab a release; `install-snapshot` first; reversible. Joins the un-piloted goal-aligned backlog (v153 ai-switcher, v150 Paseo, v149 Scrapling, v144 headroom).

## §35 note
A goal-aligned v154 **fully clears** the §35 breach that v151/v152 opened: window {v152 OG, v153 GA, v154 GA} = 1 OG ≤ 1 → CLEAR. Streak GA:16·OG:11 → **GA:17·OG:11 [7 ov]** (17th goal-aligned PASS). The corpus is back on its core — two consecutive goal-aligned agent-tooling ships (v153 + v154).
