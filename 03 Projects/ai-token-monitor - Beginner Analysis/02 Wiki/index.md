# (C) soulduse/ai-token-monitor (v158 wiki)

> **Status: GOAL-ALIGNED INCLUDE 3/4** ((a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG). A cross-platform system-tray token/cost monitor for Claude Code + Codex + OpenCode — goal-aligned, vault-useful, and corpus-first for one thing: a **social/competitive leaderboard** layer over AI-coding usage. Pilot candidate (with a privacy caveat). See `01 Analysis/`.

**Repo:** https://github.com/soulduse/ai-token-monitor · **Owner:** `soulduse` · **License:** MIT
**Tagline:** *"A system tray application for macOS and Windows that monitors token usage, costs, and activity across multiple AI coding tools in real-time."*

## What it is
A **token + cost dashboard for your AI coding tools, in the system tray.** It watches the session files your tools already write — Claude Code's `~/.claude/projects/`, Codex's `~/.codex/sessions/`, OpenCode's `~/.local/share/opencode/` — and turns them into real-time usage and cost stats with per-provider cost models. Then it adds a layer no prior corpus tool has: a **social/competitive** one — compare your usage against other developers on a leaderboard, chat with them, and get monthly/yearly recap cards.

## Providers it monitors (3)
**Claude Code** (primary) · **Codex** (OpenAI) · **OpenCode** — switchable, each with its own cost model.

## Core features (from the README)
- **Real-time token tracking** — parses session JSONL from Claude Code, Codex, OpenCode for accurate usage stats.
- **Multi-provider support** — switch sources, per-provider cost models.
- **Activity graph** — GitHub-style contribution heatmap with 2D/3D toggle.
- **Leaderboard** — compare daily/weekly/monthly usage with other developers.
- **Chat** — for leaderboard members.
- **Webhook alerts** — Discord, Slack, Telegram.
- **Recap card** — monthly/yearly, with top model, busiest day, and streaks.

## Architecture (the instructive part)
- **Tauri v2** (Rust backend + React 19 frontend), system-tray, macOS + Windows. MIT.
- **File watchers** over each tool's session JSONL (the same log-parsing observability mechanism as v89 VibeCodingTracker — no agent reconfiguration needed; it reads what your tools already write).
- A **Postgres (PLpgSQL) shared backend** powers the social features — which is the architectural tell that the leaderboard/chat are real, and that **your usage data leaves the machine** for them (a privacy trade-off; local tracking works without opting in).

## Where it sits in the corpus
- It's the **metering flavor** of the corpus's **"AI-agent observability" sub-archetype**, bringing that sub-flavor to **N=4** (v89 VibeCodingTracker + v109 cclog-cli + v157 ClaudeBar + v158) and the sub-archetype overall to **N=5** — robustly ripe for the audit to confirm.
- **Corpus-first:** the **social/competitive shared-backend layer** (leaderboard + chat + recap cards) inverts the local-private default of every prior monitor — filed as a new standalone.
- It's **Tauri**, but it **observes** rather than **controls** — so it is *not* an LV-C7 management-GUI (v73/v117/v153, which manage an agent's config/accounts). Different layer.

## Provenance (§37)
≈**227★** / 44 forks / **339 commits** / **73 releases** (latest v0.19.12) / MIT / TypeScript 62.2% + Rust 29.9% + PLpgSQL 7.1% / Tauri v2 system-tray.
*Page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified (§37.4)**; this environment mocks the GitHub API.* Creation date unstated → velocity unestablished → **NOT a Pattern #52 claim.** Owner `soulduse` (no visible location/bio).

## Why it's goal-aligned (and a pilot, with a caveat)
- **On goal #1:** it observes the coding agents (their token/cost/activity), not an app that merely calls an LLM.
- **Directly vault-applicable:** for heavy Claude Code use, real-time token/cost awareness across providers is a concrete workflow aid — and it reads your existing JSONL with no agent reconfiguration.
- **Pilot candidate, with a privacy caveat:** the local token-tracking is reversible and low-friction (`install-snapshot` first); but the leaderboard/chat features upload usage to a shared backend — opt into those deliberately. ⚠️ **This is the 6th "manage/monitor AI coding tools" ship in a row (v153–v158), with ZERO piloted.** The audit is critically overdue (five ripe promotion calls); the highest-value move is the audit or actually piloting one of these six — not a v159.

## §35 note
A goal-aligned v158 keeps the ceiling clear: window {v156 GA, v157 GA, v158 GA} = 0 OG (six consecutive goal-aligned ships). Streak GA:20·OG:11 → **GA:21·OG:11 [7 ov]** (21st goal-aligned PASS).
