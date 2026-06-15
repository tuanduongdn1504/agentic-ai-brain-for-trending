# (C) rainnoon/oc-claw (v164 wiki)

> **Status: GOAL-ALIGNED INCLUDE 3/4** ((a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG). A cross-platform **desktop pet** (macOS notch / Windows taskbar) that **monitors AI coding agents in real time** — an animated character that reacts to whether your agents are working, idle, or waiting, across 7 tools. **This is a clean 4th desktop-pet** (the v158-CONFIRMED observability sub-archetype, sub-flavor (b) ambient-pet → N=4) — the v159 CodexBar shape: a clean instance-strengthening that **mints nothing new.** See `01 Analysis/`.

**Repo:** https://github.com/rainnoon/oc-claw · **Owner:** `rainnoon` (no name / affiliation / location disclosed) · **License:** MIT
**Tagline:** *"A desktop pet that monitors your AI coding agents in real time. Supports macOS and Windows."*
**Origin:** built at the **KAON Hackathon** · design inspiration credited to **Notchi** and **Vibe Island**.

## What it is
An **ambient/affective status surface** for multi-agent coding. It puts an animated character on the **macOS notch** (or **Windows taskbar**) that **animates by aggregate agent run-state** — working / idle / waiting — so the pet *is* the at-a-glance status display. Hovering the macOS notch reveals **session-detail panels**. It is a watch-and-react companion, not a controller: it surfaces what the agents are doing; it does not manage their config/accounts and (unlike v160 ping-island) it does not route approval-interrupts or act in place.

The name reads as **"OpenClaw" + claw** — OpenClaw is its first-class integration (auto-discovery of local OpenClaw sessions), and the rest of the agents hang off the same status surface. It is **independent** of v156 `clawd-on-desk` (different author, different stack; "claw" there = a "Clawd" Claude-pet pun, here = OpenClaw) — a parallel instance, not a fork (the v154→v155 independence shape).

## Agents it works with (7)
OpenClaw · Claude Code · Cursor · Codex · Gemini CLI · OpenCode · Hermes Agent.

## How it integrates
- **OpenClaw (first-class):** auto-discovers local OpenClaw sessions by **polling JSONL session files**, and surfaces **chat history + token/call metrics** in the notch detail panel (a light *metering* element layered onto the pet).
- **Claude Code / Codex / Cursor / Gemini CLI:** installed **hooks / plugins** in each client's config (the v156 clawd-on-desk / v160 ping-island hooks-integration mechanism).
- **Hermes Agent:** via its **plugin system**.
- **Remote SSH connectivity** to server-hosted agents (the same remote-forwarding capability v160 ping-island made a core workflow — N=2 within the observability cluster).
- Cosmetic layer: custom character animations + island-background customization + completion / waiting **sound effects**.

## Where it sits in the corpus
- It is a clean member of the **CONFIRMED (v158 audit) "AI-Agent Observability / Status-Surface Tool" sub-archetype**, specifically **sub-flavor (b) — "Ambient / affective status-surface (reactive desktop-pet/avatar whose state tracks aggregate agent run-state as the *primary* display)."**
  - **Sub-flavor (b) → N=4** (v154 agentpet native-Swift + v155 openpets Electron+MCP + v156 clawd-on-desk Electron+hooks + **v164 oc-claw Tauri+JSONL/hooks**). **Sub-archetype overall → N=10.**
  - **It mints NOTHING new** — the honest v159-CodexBar outcome. A notch-placed pet with token/call metrics is sub-flavor (b) ambient-pet + a touch of sub-flavor (a) metering, both already-confirmed sub-flavors. The only "firsts" are stack/UI/blend details, **not** structural mints (see below).
- **Distinct from sub-flavor (c) (v160 ping-island attention/approval-interrupt-routing):** both live on the notch, but oc-claw **animates by status and hover-reveals detail** — it does NOT surface actionable interrupts or handle approve/deny/answer in place. So it is (b), not (c). The notch is a shared UI-location, not a sub-flavor marker.
- **OBSERVES, does NOT control → NOT Library-vocab #22 LV-C7** (the Tauri management-GUIs v73/v117/v153 control provider/account/config; oc-claw is *built on Tauri* but only reads/surfaces state — the v158 "Tauri-but-NOT-LV-C7" line, drawn for v158 ai-token-monitor).
- **NOT Pattern #18 #8** (routes/aggregates no LLM providers — it reads agent state).

## Observations (NOT minted — the v158/v159 anti-inflation discipline)
- **First Tauri-stack desktop-pet** (v154 native-Swift, v155/v156 Electron) — a stack note, not a structure mint (the v120 "archetype ≠ stack-popularity" line).
- **Pet + metering blend:** the OpenClaw detail panel carries token/call metrics — a mild cross-sub-flavor (b)+(a) blend. Observation.
- **SSH-forwarding within the observability cluster → N=2** (v160 ping-island + v164). Observation.
- **OpenClaw-first integration** (oc = OpenClaw) + Hermes/OpenClaw/OpenCode corpus-recursive refs (v149/v156/v160 OpenClaw; v78/v112/v160 Hermes). #84 cross-tool (7 agents).
- **KAON Hackathon origin** + **Notchi / Vibe Island** design-inspiration credit — Vibe Island was named at v160 as part of the forming external "Dynamic Island for AI coding agents" micro-genre (NOT in corpus, NOT counted). Genre-corroboration, not a cited-to-subject elevation.

## Provenance (§37)
≈**288★** / 18 forks / 0 watchers / 9 open issues / **525 commits** / latest **v1.8.6** (Jun 8 2026) / MIT / **Rust 48.9% + TypeScript 44.0% + Astro 5.6%** / macOS + Windows (Tauri v2).
*Page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified (§37.4)**; env mocks the GitHub API.* Creation date NOT shown → velocity unestablished → **NOT a Pattern #52 claim** (and 288★ is small). Owner `rainnoon` — the repo discloses no real name, affiliation, or location, so **no cultural-peer inferred from the handle** (the v139 / v160-ping-island discipline); **KAON Hackathon-origin is a (d)/origin note, not an (a) signal.**

## Why it's goal-aligned (and a fair pilot)
- **On goal #1:** it monitors Claude Code + 6 peers in real time = operating/monitoring AI coding agents, a real heavy-Claude-Code workflow. **(b) STRONG-not-STRONGEST** = an observability surface *around* the agents, not the substrate.
- **Fair pilot candidate** (MIT + mature 525c/v1.8.6 + cross-platform incl. Windows + reversible) — ⚠️ but it installs **hooks/plugins into your agents' config files**, so `install-snapshot` first + snapshot those configs and review what it writes; the `install.sh`/`install.ps1` are `curl|bash`-style scripts (pilot fence).
- ⚠️ **12th consecutive "tool for operating/monitoring AI coding agents" subject (v153→v164), ZERO piloted — and the 4th desktop-pet.** It mints nothing (a clean N=4, the v159 shape). The high-value move is to **pilot one** (oc-claw / agentpet / ping-island) or **run the overdue audit**, not to catalogue a v165 in this niche.

## §35 note
A goal-aligned v164 keeps the ceiling clear: window {v162 GA, v163 GA, v164 GA} = 0 OG (**12 consecutive goal-aligned ships v153→v164**). Streak GA:26·OG:11 → **GA:27·OG:11 [7 ov]** (27th goal-aligned PASS; not an override).
