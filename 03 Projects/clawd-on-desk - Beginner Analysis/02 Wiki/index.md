# (C) rullerzhou-afk/clawd-on-desk — "Clawd on Desk" (v156 wiki)

> **Status: GOAL-ALIGNED INCLUDE 4/4** ((a) PASS-MODERATE inferred-China-Mainland · (b) STRONG · (c) STRONG · (d) STRONG). A pixel desktop pet that watches Claude Code + 11 agents via hooks — goal-aligned, and the **3rd independent instance** that brings the reactive-desktop-pet-status-surface standalone to **N=3 (promotion-eligible)**. Pilot candidate. See `01 Analysis/`.

**Repo:** https://github.com/rullerzhou-afk/clawd-on-desk · **Creators:** @rullerzhou-afk (鹿鹿) + @YOIMIYA66 · **License:** AGPL-3.0 (code; artwork rights reserved)
**Tagline:** *"A pixel desktop pet that watches Claude Code, Codex, Cursor & other AI coding agents — so you don't have to."*

## What it is
A **desktop pet that watches your AI coding agents.** A pixel-art character lives on your desktop and animates to reflect what your agent is doing — thinking, typing, building, juggling multiple subagents, erroring, celebrating. When an agent needs a tool permission, the pet pops a **permission bubble** you can approve or deny in place. It tracks **multiple agents at once** (multi-agent coexistence). The most mature and popular of the corpus's three desktop-pet-for-agents projects.

## Agents it watches (11+)
**Claude Code** (full integration via hooks + an HTTP permission system) · **Codex CLI** (official hooks + JSONL fallback) · **Copilot CLI** · **Gemini CLI** · **Antigravity CLI** · **Cursor Agent** · **CodeBuddy** · **Kiro CLI** · **Kimi Code CLI** · **Qwen Code** · **opencode** · **Pi** · **OpenClaw** · **Hermes Agent** — the **broadest cross-tool surface in the corpus.**

## Core features (from the README)
- "Real-time state awareness — agent hooks and log polling drive Clawd's animations automatically."
- "12 animated states — idle, thinking, typing, building, subagent groove, multi-subagent juggling, error, happy, notification, sweeping, carrying, sleeping."
- "Permission bubble … when Claude Code, Codex CLI, CodeBuddy … request supported tool permissions."

## Architecture (the instructive part)
- **Electron**, cross-platform (Windows 11 / macOS / Ubuntu-Linux), JavaScript 92.4% (+ HTML/CSS/Python/Shell).
- Integration via **agent hooks + HTTP permission system** (Claude Code) with **JSONL/log-polling fallback** for agents lacking hooks — a *different* mechanism from its siblings (v155 openpets uses MCP; v154 agentpet uses a Unix-socket daemon + CLI wrapper).
- The notable step beyond its siblings: a **permission-approve/deny bubble** — the pet doesn't only *watch*, it lets you *act* on the agent's tool requests.

## Where it sits in the corpus
- It's the **3rd independent "reactive desktop-pet status surface for AI coding agents"** — v154 agentpet + v155 openpets + v156 clawd-on-desk — bringing that corpus-first standalone to **N=3, promotion-eligible** (the audit should now confirm it). The three span **three integration mechanisms**: socket/wrapper · MCP · hooks/log-polling — settling the "is the pet-surface one class?" question toward **yes, one class with multiple mechanisms.**
- **Pattern #84 cross-tool** at its widest (11+ agents). References **Hermes / Antigravity / OpenClaw** (corpus-recursive neighbors) and acknowledges visual lineage from `clawd-tank`.
- **AGPL-3.0 code + artwork rights reserved** = a code-vs-asset license split (a Pattern #45 note).

## Provenance (§37)
≈**3.7k★** / 367 forks / **1,123 commits** / **25 releases** (latest v0.8.1, May 27 2026) / AGPL-3.0 (code; artwork reserved) / JavaScript 92.4% / Electron.
*Page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified (§37.4)**; this environment mocks the GitHub API.* Creation date unstated → velocity unestablished → **NOT a Pattern #52 claim** (most-starred of the pet trio: 3.7k vs openpets 968 vs agentpet 40). Creators @rullerzhou-afk (鹿鹿) + @YOIMIYA66.

## Why it's goal-aligned (and a real pilot)
- **On goal #1:** it watches Claude Code (+ 10 peers) via hooks and lets you handle tool permissions in place — agent infrastructure, not an app that merely calls an LLM.
- **Directly vault-applicable:** ambient awareness + in-place permission handling across parallel Claude Code sessions is a concrete workflow aid.
- **Pilot candidate** (most mature/popular pet; hooks + HTTP-permission plug into Claude Code). ⚠️ **But this is the 4th "manage/monitor AI coding tools" ship in a row (v153/v154/v155/v156), 3 of them desktop-pets, with ZERO piloted.** The catalogue is now *ripe* — the highest-value next move is the **overdue audit** (to bank the N=3 promotions) or actually **piloting one of these four**, not a 5th entry.

## §35 note
A goal-aligned v156 keeps the ceiling clear: window {v154 GA, v155 GA, v156 GA} = 0 OG (four consecutive goal-aligned ships). Streak GA:18·OG:11 → **GA:19·OG:11 [7 ov]** (19th goal-aligned PASS).
