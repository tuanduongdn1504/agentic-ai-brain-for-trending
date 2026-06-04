# (C) alvinunreal/openpets — "OpenPets" (v155 wiki)

> **Status: GOAL-ALIGNED INCLUDE 3/4** ((a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG). A desktop pet that shows live Claude Code status via MCP — goal-aligned, and the **independent 2nd instance** of the reactive-desktop-pet-status-surface standalone minted at v154 (agentpet). Pilot candidate. See `01 Analysis/`.

**Repo:** https://github.com/alvinunreal/openpets · **Owner:** `alvinunreal` (Boring Dystopia Development) · **License:** MIT
**Tagline:** *"Desktop pets for AI coding agents. Install pets, connect Claude Code via MCP, and see live coding status on your desktop."*

## What it is
A **tray-first Electron desktop companion**: an animated pixel-art pet that lives on your desktop and **reacts to what your AI coding agent is doing**. Connect Claude Code (and peers) over **MCP**, and the pet reflects agent activity — thinking, editing, testing, asking permission, success, error — as ambient, glanceable status. It also stands alone as a focus/break companion (focus timers, break nudges, ambient check-ins).

## Agents it connects to
- **Claude Code** · **OpenCode** · **Cursor** · **Pi** · **any MCP-capable agent**
- Ships **Claude memory instructions + hooks + OpenCode plugins** as the integration layer.

## Core features (from the README)
- "A small pet that idles, reacts, and gives OpenPets a friendly presence."
- "Bundled abilities for ambient presence, breaks, playful actions, and focus sessions."
- "Any MCP-capable agent can send short safe speech bubbles and reactions."
- "Privacy-conscious by design — automatic hook speech is static and local."

## Architecture (the instructive part)
- **Electron**, cross-platform (macOS / Windows / Linux), TypeScript 84.9% (+ JS 12.8%).
- **MCP integration layer** — agents push reactions/status to the pet via the Model Context Protocol (vs v154 agentpet's Unix-socket daemon + CLI wrapper). Local IPC; privacy-conscious (static, local hook speech).
- Pet-pack management (browse + select animated pets) + bundled abilities.

## Where it sits in the corpus
- It's the **2nd "reactive desktop-pet status surface for AI coding agents"** — and an **independent** one (different author + stack, not a fork) — alongside **v154 agentpet**. That standalone, minted one ship earlier, is now **N=2, promotion-eligible**. The two show the *same* corpus-first idea via two integration mechanisms: **MCP** (openpets) vs **socket-daemon/CLI-wrapper** (agentpet).
- **Pattern #18 B1 MCP** is the integration mechanism. It's **adjacent** to the T2 "AI-agent observability" sub-archetype (v89/v109/v154) — it shows live status — but its center is a **companion/affective** surface with productivity abilities, so it's not hard-counted as a 4th observability tool.
- It's **Electron**, contrasting v154 agentpet's native-Swift — the pet-surface idea now spans both stacks.

## Provenance (§37)
≈**968★** / 35 forks / **132 commits** / **14 releases** (latest v2.5.0, May 27 2026) / MIT / TypeScript 84.9% / Electron (macOS/Win/Linux).
*Page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified (§37.4)**; this environment mocks the GitHub API.* Creation date unstated → velocity unestablished → **NOT a Pattern #52 claim** (even at 968★, the most popular of the v153/v154/v155 trio). Owner `alvinunreal` (Boring Dystopia Development).

## Why it's goal-aligned (and a real pilot)
- **On goal #1:** it connects to Claude Code via MCP and surfaces live agent status — agent infrastructure, not an app that merely calls an LLM.
- **Directly vault-applicable:** ambient awareness of Claude Code's state (thinking / needs-permission / done) is a concrete workflow aid.
- **Pilot candidate:** MIT, mature (v2.5.0 / 132 commits / 968★), MCP plugs into Claude Code cleanly; `install-snapshot` first; reversible. ⚠️ **But this is the 3rd "manage/monitor AI coding tools" ship in a row (v153 ai-switcher, v154 agentpet, v155 openpets) with ZERO piloted** — the genuinely useful next move is to *pilot one of the three*, not catalogue a fourth.

## §35 note
A goal-aligned v155 keeps the ceiling clear: window {v153 GA, v154 GA, v155 GA} = 0 OG (three consecutive goal-aligned ships). Streak GA:17·OG:11 → **GA:18·OG:11 [7 ov]** (18th goal-aligned PASS).
