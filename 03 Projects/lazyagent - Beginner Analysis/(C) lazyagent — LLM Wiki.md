# (C) lazyagent — LLM Wiki (v165)

> **Subject:** [`illegalstudio/lazyagent`](https://github.com/illegalstudio/lazyagent) — *"Monitor all your coding agents from one terminal — Claude Code, Cursor, OpenCode, pi and more."*
> **Built:** 2026-06-15 · wiki **v165** · routine **v2.6** · branch `wiki/v165-lazyagent` off `main`.
> **Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.
> ⚠️ **Standing-lever flag (read first):** this is the **13th consecutive "tool for operating/monitoring AI coding agents" ship (v153→v165), ZERO piloted** — and the **observability sub-archetype now reaches N=11.** The v162/v163/v164 audits all said the same thing in plain words: *pilot one or vary the domain, not another in this space.* See **§9** below.

---

## 1. What it is

A **multi-interface monitoring tool** for AI coding agents. Its whole thesis is *observe, don't replace*: **"Unlike other tools, lazyagent doesn't replace your workflow — it watches it. Launch agents wherever you want (terminal, IDE, desktop app), lazyagent just observes."** No server, no account, no lock-in — purely local + observational.

It surfaces every coding agent you have running from **one place**, via **four delivery surfaces**:

1. **Terminal UI** — interactive, lazygit-style; inspect **projects, sessions, agents, subagents, tools, prompts and outputs** in one view; built for day-to-day observability.
2. **macOS menu-bar app** (tray) — a Wails-based GUI.
3. **HTTP API** — Bearer-token-protected; open, so you can build your own clients on top.
4. **iOS app** — on the App Store (paid, funds development); pairs with the HTTP API for phone/iPad monitoring.

It tracks, in **real time**: agent activity, **token usage breakdowns per session** (model tokens / tokens saved by cache reuse / cache-creation tokens), and **cost**.

## 2. Supported agents

**9 agents:** Claude Code · Cursor · Codex · Grok CLI · Kilo · Kimi Code CLI · Amp · pi · OpenCode. Detection is observational — lazyagent reads each agent's local session data; it does not require reconfiguring or wrapping the agents (you launch them wherever you like and it watches).

## 3. The distinctive part — maintenance / housekeeping commands

This is the one thing lazyagent does that **no prior corpus subject does**. Beyond display, it actively **manages the stored session/transcript files**:

- **`lazyagent prune`** — delete chat files older than *N* days (dry-run preview + automatic backup).
- **`lazyagent compact`** — shrink session files by truncating bulk payloads (reduces disk + rate-limit/billing impact; README cites typical ~80+ MiB/year reclaimed).
- **`lazyagent search`** — full-text search across transcripts with highlighted snippets.
- **`lazyagent limits`** — rate-limit / billing summaries.

`prune`/`compact`/`search` are **post-hoc file-level housekeeping of already-stored transcripts** — distinct from runtime context-compression (see the v144 headroom distinction in **§7**).

## 4. Install & run

- **Homebrew:** `brew install illegalstudio/tap/lazyagent`
- **Go:** `go install github.com/illegalstudio/lazyagent@latest`
- **Source:** Make targets (Node.js required for the Wails GUI build).
- Launch: Terminal-UI modes · API server · GUI · combined · maintenance subcommands (filterable by agent type, e.g. `claude`, `grok`, `kimi`).

## 5. §37 provenance (volatile facts — recency + source + confidence)

| Fact | Value | Provenance |
|---|---|---|
| Stars | ≈**165★** | as of 2026-06, github.com/illegalstudio/lazyagent repo page — **stated, NOT API-verified §37.4** (env mocks the GitHub API) |
| Forks / watchers / open issues | 12 / 0 / 0 | same — stated, NOT API-verified |
| Commits | **373** | same |
| Latest release | **v0.12.5** (Jun 14 2026) | same |
| Creation date | not shown | → **velocity unestablished → NOT a Pattern #52 claim** (165★ small anyway; a Show HN exists [HN 47349851] but I do **not** derive velocity from an unverified birth date) |
| License | **MIT** | repo badges + footer — stated |
| Languages | Go 91.3% · TypeScript 4.5% · Svelte 3.8% · CSS/Make/Shell | repo page — stated |
| Stack | Go core + **Wails** (menu-bar/GUI) + HTTP API + iOS companion | README |
| Owner | org `illegalstudio`, handle `nahime0` (X: @nahime0) | repo page — **no disclosed real name / affiliation / location** |
| Docs | lazyagent.dev | (fetch returned HTTP 403 / bot-block; structure: getting-started / concepts / interfaces / maintenance / reference) |

## 6. Phase 0.9 verdict — GOAL-ALIGNED INCLUDE 3/4

- **(a) FAIL** — `nahime0` / `illegalstudio` is a bare handle + an org name; no disclosed real name, affiliation, or location → **no cultural-peer inferred from the handle** (the v139 / v159-steipete / v160-ping-island / v164-rainnoon discipline; the v151-audit rec (ii) "require a *solid* (a) signal, not a name/heritage inference"). The "illegalstudio" org name and the X handle carry no geographic/cultural signal. **No axis minted.**
- **(b) STRONG (not STRONGEST)** — monitoring Claude Code + 8 peer agents (activity / tokens / cost / sessions) from one place = dead-center goal #1 *and* a real heavy-Claude-Code vault workflow. **STRONG-not-STRONGEST** = an **observability surface *around* the agents**, not the agent substrate (Claude/Anthropic) or a methodology — the v154/v157/v158/v159/v160/v164 calibration. → **GOAL-ALIGNED INCLUDE.**
- **(c) STRONG** — Go core (91.3%) + Wails menu-bar GUI + Bearer-token HTTP API + iOS companion + four delivery surfaces + maintenance commands (with dry-run + auto-backup safety); **mature for its star count** (373 commits / v0.12.5).
- **(d) STRONG** — the **v158-CONFIRMED "AI-Agent Observability / Status-Surface Tool" sub-archetype** (sub-flavor (a) metering/usage-logs); Pattern #84 cross-tool (9 agents); the **lazy*-TUI lineage** (self-credited: lazygit / lazyworktree / pixel-agents); HTTP-API-for-clients + iOS remote-monitoring delivery axis.

## 7. Pattern Library implications

### §35 — STAYS CLEAR
Window {v163 GA, v164 GA, **v165 GA**} = 0 OG → **clear**. **13 consecutive goal-aligned ships v153→v165.** NOT an override → override-frequency UNCHANGED (lifetime 10).

### PHASE 4b PRIMARY (Library-vocab §C) — 1 NEW standalone, CORPUS-FIRST
**"Agent Session-Transcript Maintenance / Housekeeping (prune / compact / full-text-search stored agent session files to reclaim disk + rate-limit budget)" — N=1, CORPUS-FIRST.** No prior corpus subject does **file-level maintenance of stored agent session data** (delete-old / shrink / search). This is the *capability* mint (the subject overall is a clean observability instance — see SECONDARY), exactly the **v158 ai-token-monitor shape** (a clean observability instance that *also* minted one corpus-first capability standalone — accepted by the v158 audit as "the legitimate payoff"). It passes the **v160 functional-novelty test** (a genuinely new *function* — write/manage stored data — not new stack/scale). **§28: 1 new standalone ≤ 2.** Filed to registry `06` §C + §F. **Promotion-eligible at N=2.**

**Distinct from v144 headroom** ("Agent Context-Compression Layer"): headroom is a multi-surface, **reversible, pre-LLM** interceptor that compresses what the agent *reads* (tool-outputs/logs/RAG/files/history) at runtime to save the **context window**. lazyagent operates **post-hoc on already-stored transcript files on disk** to reclaim **disk + rate-limit/billing** budget (prune is destructive-with-backup; compact truncates bulk payloads; search indexes). Different layer (stored files vs runtime read-path), different purpose (disk/rate-limit hygiene + searchability vs context-window economy).

### PHASE 4b SECONDARY (tier sub-archetype) — clean instance-strengthening
**Observability sub-archetype → N=10 → N=11**, sub-flavor **(a) metering / quota / usage-logs → N=5 → N=6** (v89 + v109 + v157 + v158 + v159 + **v165 lazyagent**). lazyagent tracks real-time tokens/cost (model / cache-reuse / cache-creation) + `limits` rate/billing + a logs/sessions dashboard = a clean **(a)** instance. **0 mints at the sub-archetype layer** — it is the **broadest multi-interface instance** (TUI + menu-bar + HTTP-API + iOS) and the **deepest-inspection instance** (projects/sessions/agents/subagents/tools/prompts/outputs), but *multi-interface delivery and inspection-depth are scale/delivery, not new structure* (the v164 "stack ≠ structure" / v159 "broadest-coverage = a count, not a mint" discipline). Recorded in `02b` + `06` §F (rule-5 "filing is an act").

### Observations (NOT minted)
- **Multi-interface delivery** (TUI + macOS menu-bar/Wails + Bearer-token HTTP-API + paid iOS App Store companion) — a distinctive *delivery* axis (remote/mobile monitoring via an open API), but **delivery ≠ structure** (the v164/v120 line) → observation. The iOS-app-funds-OSS is a mild monetization/funnel note.
- **lazy*-TUI lineage** — self-credits lazygit / lazyworktree / pixel-agents (the "lazy-" terminal-tool genre) → genre note, not a cited-to-subject elevation.
- **Pattern #84 84c** cross-tool (9 agents, agent-agnostic, reads each agent's local session data).
- **Real-time token/cost with cache-reuse + cache-creation breakdown** = the metering sub-flavor (a) fit.

### Boundary lines (anti-conflation)
- **NOT LV-C7 #22** ("Tauri-Desktop Management-GUI for a Coding Agent") — lazyagent **OBSERVES** (reads/surfaces state, even prune/compact act on *transcript files*, not on the agent's provider/account/config); it does not control the agent's operation. The observe-vs-control line (v154/v158/v164). *(Also: lazyagent's GUI is Wails/Go, not Tauri — but the load-bearing reason is observe-not-control, not the stack.)*
- **NOT #18 #8** (Multi-Source LLM Aggregator) — it routes/aggregates no providers; it reads state.
- **NOT a new sub-flavor** of the observability sub-archetype — it is neither an ambient pet (b) nor an attention/approval-interrupt router (c); it's a plain multi-interface status/metering monitor = sub-flavor (a). Minting a 4th "dashboard/mission-control" sub-flavor would be inflation (v159/v164 discipline).

### Counts after this ship
**46 patterns / 10 CONFIRMED Library-vocab — UNCHANGED.** Tracked PROVISIONAL Library-vocab surface ≈25 → **≈26** (+1 §C standalone). Observability sub-archetype N=11; metering sub-flavor (a) N=6.

## 8. ⚠️ Name collision (cataloguing-hazard note, the v148 goose lesson)

There is a **different, similarly-named project**: [`chojs23/lazyagent`](https://github.com/chojs23/lazyagent) — *"Watch what your AI coding agents (claude, codex and opencode) are doing on your terminal and browser"* (v0.3.1). It is a **separate repo by a different author**, similar concept, similar name. **The canonical subject of this wiki is `illegalstudio/lazyagent` (v0.12.5)** — the URL the operator provided. Flagged so a future reader (or audit) does not conflate the two. (A 3rd unrelated `runpod/lazy-agent` "LazyVim-for-AI-agents" also exists — not the subject.)

## 9. ⚠️ Standing lever — the blunt part

This is the **13th consecutive "tool for operating/monitoring AI coding agents" ship (v153→v165), and ZERO of them have been piloted.** It is another **AI-agent observability monitor** (sub-archetype now **N=11**), in the most catalogue-saturated corner of the corpus. The genuine mint here (transcript-maintenance) is real and additive — but a mint is not a pilot, and the v162 + v163 + v164 audits all said the same thing in plain words: **pilot one or vary the domain, not another in this space.** The corpus also owes an **overdue audit** (two N=2 orchestration buckets from v162/v163, the observability sub-archetype now at N=11, the standing override-review, and a shim reconcile).

**The two genuinely high-value next moves (not a v166 in this niche):**
1. **Pilot one** — lazyagent itself is a fair pilot (MIT + mature + reads existing session data + Homebrew/Go install, reversible). Or agentpet (v154), ping-island (v160), CodexBar (v159), oc-claw (v164). ⚠️ Pilot fence: `prune` **deletes** chat files (dry-run + backup first), `compact` **truncates** session files (irreversible truncation of bulk payloads), and the HTTP API + iOS pairing exposes session data over the network (Bearer-token) — `install-snapshot` first, trial on a scratch project, and test `prune`/`compact` in dry-run before pointing them at real transcripts.
2. **Run the overdue audit** — it has been ripe for several ships.

## 10. Pilot assessment

**Fair pilot candidate.** Pros: MIT, mature (373c / v0.12.5), reads existing agent session data (no agent reconfiguration), reversible install (`brew`/`go install`), genuinely useful (one-pane view of all your agents + token/cost). Cons / fence: `prune` deletes + `compact` truncates stored transcripts (data-loss surface — dry-run/backup first); HTTP API + iOS expose session data over the network. **If you pilot exactly one of the v153→v165 run, this or agentpet (v154) are the most directly vault-useful.**

## 11. Cross-references

- **v158-CONFIRMED observability sub-archetype** + sub-flavors (a)/(b)/(c) → `_patterns/02b-confirmed-patterns-v42-plus.md`.
- **Metering sub-flavor (a) siblings:** v89 VibeCodingTracker · v109 cclog-cli · v157 ClaudeBar · v158 ai-token-monitor · v159 CodexBar.
- **v144 headroom** — the nearest neighbor to the transcript-maintenance mint (distinguished in §7).
- **Registry:** `_patterns/06-library-vocab-registry.md` §C (new standalone) + §F (running log).
- **Verdict + PRIMARY docs:** `01 Analysis/`.
