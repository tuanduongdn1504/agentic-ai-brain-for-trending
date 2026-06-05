# (C) tddworks/ClaudeBar (v157 wiki)

> **Status: GOAL-ALIGNED INCLUDE 3/4** ((a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG). A native-macOS menu-bar quota monitor for 10 AI coding tools — goal-aligned, genuinely vault-useful, and the ship that gives the AI-agent-observability sub-archetype a clean **metering sub-flavor N=3**. Strong pilot candidate. See `01 Analysis/`.

**Repo:** https://github.com/tddworks/ClaudeBar · **Owner:** `tddworks` (GitHub org) · **License:** MIT
**Tagline:** *"A macOS menu-bar application monitoring AI coding assistant usage quotas across multiple providers."*

## What it is
A **quota dashboard for your AI coding tools, living in the macOS menu bar.** It shows — at a glance, with color-coded gauges — how much of your session / weekly / per-model budget you've used across every provider you've enabled, and notifies you when a quota status changes (so you don't discover you're rate-limited mid-task). For a heavy Claude Code user juggling several providers, it's an ambient "how much gas is left in each tank" readout.

## Providers it monitors (10)
**Claude** · **Codex** · **Gemini** · **GitHub Copilot** · **Antigravity** · **Z.ai** · **Kimi** · **Kiro** · **Amp** · **OpenCode Go** — each individually toggleable. Reads quota via each provider's CLI (`claude`, `codex`, `kimi`, …) or direct API auth.

## Core features (from the README)
- **Multi-Provider Support** — tracks multiple AI coding assistants simultaneously.
- **Real-Time Quota Tracking** — usage percentages across sessions and models.
- **Visual Status Indicators** — color-coded progress bars (green/yellow/red).
- **System Notifications** — on quota-status changes.
- **Multiple Themes** — including imported terminal themes (`.itermcolors`); automatic light/dark adaptation.

## Architecture (the instructive part)
- Native **Swift 97.2% + SwiftUI**, generated with **Tuist**; macOS 15+ / Swift 6.2+. MIT.
- Per-provider quota **adapters** over each provider's CLI or API — and a `.claude/skills/add-provider/` **TDD-based skill** that documents how to add a new provider (fitting the `tddworks` test-driven ethos). That extension model is the part worth studying: a clean adapter pattern + a documented, test-first path to broaden coverage.
- Very mature: **784+ commits / 106 releases / v0.4.65** (high release cadence).

## Where it sits in the corpus
- It's the **metering flavor** of the corpus's **"AI-agent observability" sub-archetype** — alongside **v89 VibeCodingTracker** (usage+cost) and **v109 cclog-cli** (logs/metrics). With ClaudeBar that **metering sub-flavor reaches N=3**, pairing with the **ambient-pet sub-flavor N=3** (v154 agentpet, v155 openpets, v156 clawd-on-desk). So the sub-archetype is now N=4 with a clean two-sub-flavor split — ripe for the audit to confirm.
- It's **native Swift** (Swift-native-macOS cluster with v99 cmux, v100 Easydict, v154 agentpet).
- Distinct from **v153 ai-switcher**: ClaudeBar *observes/displays* quota; ai-switcher *manages and auto-switches* accounts on quota exhaustion — observability vs management.

## Provenance (§37)
≈**1.2k★** / 100 forks / **784+ commits** / **106 releases** (latest v0.4.65, Jun 2 2026) / 48 open issues / MIT / Swift 97.2% / native macOS menu-bar (SwiftUI + Tuist).
*Page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified (§37.4)**; this environment mocks the GitHub API.* Creation date unstated → velocity unestablished → **NOT a Pattern #52 claim.** Owner `tddworks` (GitHub org).

## Why it's goal-aligned (and a strong pilot)
- **On goal #1:** it observes the coding agents themselves (their quota state), not an app that merely calls an LLM.
- **Directly vault-applicable:** you run Claude Code heavily; ambient multi-provider quota awareness + "you're about to hit your limit" notifications is a concrete, low-friction workflow aid.
- **Strong pilot candidate:** MIT, very mature, native; `install-snapshot` first (or build via Tuist); reversible. ⚠️ **But this is the 5th "manage/monitor AI coding tools" ship in a row (v153–v157), with ZERO piloted.** The catalogue is well past ripe — the highest-value next move is the **overdue audit** (four ripe N=3 promotions) or actually **piloting** one of these five (ClaudeBar is arguably the most directly useful; clawd-on-desk the most mature pet; openpets the cleanest MCP integration).

## §35 note
A goal-aligned v157 keeps the ceiling clear: window {v155 GA, v156 GA, v157 GA} = 0 OG (five consecutive goal-aligned ships). Streak GA:19·OG:11 → **GA:20·OG:11 [7 ov]** (20th goal-aligned PASS).
