# (C) ai-agent-session-center — LLM Wiki (v166)

> **Ship:** v166 · 2026-06-15 · branch `wiki/v166-ai-agent-session-center` off `main` (at `fdf2041` = v165)
> **Verdict:** GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG
> **Pattern outcome:** 0 mints. Clean instance-strengthening of the v158-CONFIRMED "AI-Agent Observability / Status-Surface Tool" sub-archetype → **N=11 → N=12**.
> **Tier:** T2 Service (web-based multi-session AI-coding-agent observability dashboard + 3D-robot status viz + light prompt-queue/approval layer).
> ⚠️ **14th consecutive "tool for operating/monitoring AI coding agents" ship (v153→v166), ZERO piloted.** Built at explicit operator election after being flagged (AskUserQuestion → "Build the v166 wiki anyway"). The audits at v162/v163/v164 + the ships at v164/v165 all said the same: pilot one or run the overdue audit, not another in this niche.

---

## 1. What it is

`coding-by-feng/ai-agent-session-center` — verbatim tagline:

> *"Real-time dashboard that turns AI coding agent sessions (Claude Code, Gemini CLI, Codex) into animated 3D robots — with live terminals, prompt history, tool logs, and queuing. Runs on any device."*

A self-hosted **web dashboard** (`npx ai-agent-session-center` → `localhost:3333`) that **observes** multiple AI-coding-agent sessions and renders each as an animated 3D robot in an interactive "cyberdrome," alongside live terminal views, prompt history, and tool logs. You launch Claude Code / Gemini CLI / Codex yourself in your own terminals; the dashboard discovers and visualizes them. Runs on any device on the network (the "any device" claim = the web UI is reachable from a phone/tablet/other machine).

**The load-bearing architectural fact (verified this ship):** it **OBSERVES, it does not host.** Per the README:

> *"No modifications to any CLI are needed. The hooks are purely observational."*

Integration is via lightweight bash **hooks** (`npm run install-hooks` writes them into the CLIs' config) that append JSON events to a queue file (`/tmp/claude-session-center/queue.jsonl`); the Node server watches that file and broadcasts updates over WebSocket. It does **not** spawn or own the agent processes (contrast v99 cmux / v162 agent-of-empires, which host the sessions in PTYs/tmux they own). The `node-pty`/`xterm.js` "live terminals" attach/display; they are not the mechanism by which the agents are launched.

## 2. Capabilities (from README + docs)

- **3D-robot status viz** — every session spawns a procedural robot (6 models: robot / mech / drone / spider / orb / tank, auto-assigned neon colors) with **8 animation states** (idle, walk, run, wait, dance, wave, offline) driven by **real-time session run-state** (Idle / Prompting / Working / Waiting / Approval / Input / Ended).
- **Live terminals** — xterm.js views of the agent sessions.
- **Prompt history + tool logs** — per-session transcript/event surface.
- **Prompt queue** — *"Global queue view — see all pending prompts across every session in one place"* + *"Auto-send mode — queued prompts auto-dispatch when the target session becomes idle."* Compose / reorder / send prompts to agents through the dashboard. (= a **light orchestration/control** layer on top of observe — the one feature that goes beyond pure observation.)
- **Session actions** — Resume, Kill, Archive, Delete, Summarize, Alert; **approve / deny tool requests** (the approval-interrupt affordance).
- **Setup wizard** — 5-step onboarding (Welcome → DepsCheck → Configure → Install → Done): resolve port, pick which CLIs to monitor, hook density, debug, history retention, then install hooks.

## 3. Architecture / stack

- **Backend:** Node.js 18+ (ESM), Express 5, WebSocket (`ws`), `node-pty`.
- **Frontend:** React 19, TypeScript, Vite; **Three.js / React Three Fiber** for the 3D scene; `xterm.js` for terminals.
- **Storage:** SQLite (server, WAL mode) + IndexedDB (browser).
- **Tests:** Vitest (400+ tests), Playwright (E2E) — genuinely well-tested for its size.
- **Languages:** TypeScript 81.4% / CSS 12.8% / JavaScript 4.7%.

## 4. Phase 0.9 verdict — GOAL-ALIGNED INCLUDE 3/4

- **(a) FAIL.** `coding-by-feng` is a bare handle. "feng" is plausibly a Chinese surname element, but that is a *heritage hint*, not a disclosed identity — no name, affiliation, or location is given. Per the v139 / v160-ping-island / v164-rainnoon / v165-lazyagent discipline + the v151-audit rec (ii) ("require a *solid* (a) signal, not a name/heritage inference"), **no cultural-peer is inferred from the handle; no axis minted.**
- **(b) STRONG (not STRONGEST).** Monitoring Claude Code + Gemini + Codex from one place = goal #1 and a real heavy-Claude-Code vault workflow. STRONG-not-STRONGEST because it is an observability surface *around* the agents, not the agent substrate or a methodology (the v154/v158/v164/v165 calibration).
- **(c) STRONG.** Coherent modern stack (Node/Express + React 19/Three.js + xterm/node-pty + SQLite-WAL), 400+ Vitest tests + Playwright E2E, 200 commits, versioned releases — mature for a 72★ project.
- **(d) STRONG.** Observability sub-archetype + #84 cross-tool (Claude/Gemini/Codex, + OpenCode/Cursor/Windsurf compatibility notes) + hooks-integration mechanism shared with v156 clawd-on-desk / v160 ping-island / v164 oc-claw + Three.js/web-dashboard form.

## 5. Pattern Library outcome — 0 mints (clean strengthening)

**PRIMARY: a clean instance-strengthening of the v158-CONFIRMED "AI-Agent Observability / Status-Surface Tool" sub-archetype → N=11 → N=12.** Same outcome shape as v164 oc-claw and v165 lazyagent: a real, well-built instance that introduces **no new structure.**

Why no mint (the v159/v164/v165 anti-inflation discipline):
- Its distinctive features are **blend + delivery, not structure.** It blends sub-flavor **(b) ambient/affective** (the 3D robots react to run-state — the web-dashboard cousin of the v154/v155/v156/v164 desktop-pets) with sub-flavor **(c) attention/approval-routing** (approve/deny tool requests, Approval/Input states, Alert — the v160 ping-island idea, here a minor feature) plus a **light prompt-queue orchestration** layer, all delivered as a **web 3D dashboard.** Multi-sub-flavor blend + a novel UI form factor = scale/delivery, exactly the kind of thing v164 (pet + metering blend) and v159 (broadest coverage) declined to mint.
- A 4th "dashboard/mission-control" sub-flavor would **inflate** — the v160 discipline (declined the dashboard-as-sub-flavor mint for lazyagent's reasoning too).

**Boundary lines (NOT):**
- **NOT a session-hosting multiplexer** (the cmux v99 / AoE v162 species). This was the wrinkle flagged at intake; verification settled it — hooks are *"purely observational,"* the agents are launched independently, the dashboard discovers them. The `node-pty` terminals attach/display; they don't spawn the agents. → the species stays N=2 (cmux + AoE).
- **NOT LV-C7 #22** (Tauri/management-GUI control-plane). It observes + offers a light prompt-queue + approve/deny *pass-through of the agents' own prompts* (the v156/v160 affordance) + kill/archive/delete *sessions*. It does **not** control provider/account/config. (The prompt-queue auto-send is the closest thing to control and is recorded as an **orchestration-lite observation**, not a mint — a sub-feature of an observability dashboard, the v156 permission-bubble precedent.)
- **NOT #18 / #8** — no provider aggregation or routing.
- **NOT a new sub-flavor** — it's a web-dashboard blend of existing (b) + (c) + observe.

**Observations (NOT minted):** hooks-integration mechanism shared with v156/v160/v164 (#84 84c adjacent) · 3D-robot/Three.js ambient viz = a novel *delivery* of the ambient/affective idea (web vs desktop-pet) · prompt-queue auto-send = orchestration-lite sub-feature (watch: a 2nd "observe + queue/dispatch prompts" subject could form a sub-flavor) · #84 cross-tool (3 agents + compat notes) · `/tmp/...queue.jsonl` hook-event-file mechanism (cousin of the JSONL-parsing observability instances v89/v158, but event-emitting hooks rather than reading the agents' own session JSONL).

## 6. §37 provenance

≈**72★** / 9 forks / **200 commits** / latest release **v2.10.30 (Jun 7 2026)** / **MIT** / TypeScript 81.4% (page-stated via WebFetch of the rendered repo + WebSearch corroboration — the repo, a `docs/feature/frontend/setup-wizard.md` doc page, and a DEV.to "command center for AI coding agents" writeup). **NOT independently API-verified §37.4** (this environment mocks the GitHub API). **Creation date NOT shown** → velocity unestablished → **NOT a #52 claim** (72★ is small regardless). ⚠️ The README's `v2.10.30` semver "appears to be a test/CI-style date" per the fetch — version recorded, not relied on.

⚠️ **Cataloguing-hazard note (the v148 lesson):** the canonical subject is `coding-by-feng/ai-agent-session-center` per the operator URL. A search-adjacent project, `asheshgoplani/agent-deck` ("Terminal session manager for AI coding agents"), is a **different** project (a TUI session manager) — not conflated. A DEV.to "Command Center for AI Coding Agents (Claude Code + Codex)" post (by `deivid11`) surfaced adjacent in search; treated as genre-corroboration only, **not** assumed to be about this repo.

## 7. Streak / state

- **Streak:** `GA:28 · OG:11 [7 ov]` → **`GA:29 · OG:11 [7 ov]`** (29th GOAL-ALIGNED PASS; NOT an override).
- **§35:** window {v164 GA, v165 GA, **v166 GA**} = 0 OG → **STAYS CLEAR** (14 consecutive goal-aligned ships v153→v166).
- **Counts:** 46 confirmed patterns / 10 CONFIRMED Library-vocab **UNCHANGED**. Observability sub-archetype N=11 → **N=12** (tier-sub-archetype layer). 0 new §C standalones. Tracked PROVISIONAL surface ≈26 UNCHANGED.

## 8. Pilot note

**Fair pilot candidate** — MIT + `npx ai-agent-session-center` (zero-build) + observational hooks (it does not change how your CLIs behave). ⚠️ **Pilot fence:** the setup wizard **writes hook files into your CLI configs** (`~/.claude/...` etc.) → `install-snapshot` first + snapshot those configs; the dashboard can **Kill / Archive / Delete** sessions and **approve/deny tool requests** and **auto-send queued prompts** — a real control surface, not pure read-only — so trial on a scratch session before pointing it at real work; it binds a web server on `:3333` reachable on your network (the "any device" feature) → mind exposure.

⚠️ **But a pilot of *this* is the 14th-in-niche temptation, not the lever.** The genuinely high-value moves remain: **pilot one of the existing 13** (agent-of-empires v162 is closest to Storm Bear's own workflow; ai-token-monitor v158 / CodexBar v159 are the most directly useful monitors; agentpet v154 / ping-island v160) **or run the badly-overdue ~v167 audit** (it owes: the session-multiplexer species N=2 confirm/rename, the orchestration-platform N=2, the observability sub-archetype now at N=12, the 7-in-20 override-review, and a full shim reconcile). A v167 in this niche is the lowest-value move on the board.

## Suggested next action

Commit the v166 ship on `wiki/v166-ai-agent-session-center` (don't merge — operator reviews + merges). Then **pilot one** (existing 13, not a 15th) **or run the overdue audit** — not a v167 monitor.
