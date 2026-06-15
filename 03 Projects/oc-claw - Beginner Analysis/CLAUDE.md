# oc-claw — Beginner Analysis (project CLAUDE.md)

**Subject:** `rainnoon/oc-claw` (v164 wiki ship, 2026-06-15).
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.
**Routine:** v2.6 (§31/§35/§37). **Ships into the v158-audit-CONFIRMED Pattern Library.**

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis verdict + §35 + §37 + honest non-claims.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY clean strengthening (sub-flavor (b) ambient-pet → N=4, sub-archetype → N=10, 0 mints); observations; the standing lever.
- `02 Wiki/index.md` — the knowledge page.

## One-paragraph summary
**"A desktop pet that monitors your AI coding agents in real time. Supports macOS and Windows."** A cross-platform **Tauri v2** (Rust 48.9% + TypeScript 44.0% + Astro 5.6%; MIT) desktop-pet by `rainnoon` (no disclosed identity; built at the KAON Hackathon) that puts an **animated character on the macOS notch / Windows taskbar** and **animates by aggregate agent run-state** — working / idle / waiting — across **7 agents** (OpenClaw + Claude Code + Cursor + Codex + Gemini CLI + OpenCode + Hermes Agent). OpenClaw is first-class (JSONL session auto-discovery + chat history + token/call metrics in a notch hover-panel); the others via installed hooks/plugins; + remote SSH connectivity + custom animations + sound effects. Design-inspired by Notchi + Vibe Island. v1.8.6; 288★; 525 commits.

## Verdict rationale
- **(b) STRONG** = real-time monitoring of Claude Code + 6 peers = goal #1 + a real vault workflow. **STRONG-not-STRONGEST** = an observability surface *around* the agents (the v154/v155/v156/v159/v160 calibration).
- **(a) FAIL** = `rainnoon` discloses no name/affiliation/location; no cultural-peer inferred from the handle (v139 / v160-ping-island discipline); KAON Hackathon-origin is a (d)/origin note, not an (a) signal. (b) carries.
- (c) STRONG (Tauri v2 + Rust SSH/system + React/TS; JSONL polling + hooks/plugins for 7 agents + notch UI + animations + SFX; 525c/v1.8.6; macOS + Windows). (d) STRONG (observability sub-flavor (b) ambient-pet + notch+SSH shared w/ v160 + Tauri stack + #84 cross-tool 7 + OpenClaw/Hermes corpus-recursive).

## §35 / streak
**§35 STAYS CLEAR** — window {v162 GA, v163 GA, v164 GA} = 0 OG (**12 consecutive goal-aligned ships v153→v164**). NOT an override → override-frequency UNCHANGED (lifetime 10). Streak GA:26·OG:11 [7 ov] → **GA:27·OG:11 [7 ov]** (27th GOAL-ALIGNED PASS).

## Pattern Library
**PRIMARY: clean instance-strengthening — observability sub-flavor (b) ambient-pet → N=4** (v154 agentpet + v155 openpets + v156 clawd-on-desk + v164 oc-claw; 4 mechanisms: socket/wrapper / MCP / hooks+log-polling / Tauri+JSONL+hooks); **sub-archetype overall → N=10** (a:5 / b:4 / c:1). **The v159 CodexBar shape — mints NOTHING new** (a notch-placed Tauri pet with token-metrics is sub-flavor (b) + a touch of (a); the "firsts" are stack/UI/blend, not structure — the v158/v159 anti-inflation discipline). **0 new §C standalones; CONFIRMED Library-vocab UNCHANGED at 10; top-level pattern count UNCHANGED at 46.** Observations (NOT minted): first Tauri-stack pet · pet+metering blend · SSH-forwarding within the cluster → N=2 (v160+v164) · OpenClaw-first + OpenClaw/Hermes corpus-recursive · #84 cross-tool (7) · independent of v156 clawd-on-desk (not a fork) · KAON-Hackathon origin + Notchi/Vibe-Island genre-corroboration (NOT counted). NOT (c) (no approval-routing/act-in-place) · NOT LV-C7 #22 (observes, doesn't control — "Tauri-but-NOT-LV-C7") · NOT #18 #8 · (a) FAILS (no identity) · NOT a #52 claim (288★, age unverified §37.4).

## Provenance (§37)
≈**288★** / 18 forks / 0 watchers / 9 issues / **525 commits** / v1.8.6 (Jun 8 2026) / MIT / Rust 48.9% + TS 44.0% + Astro 5.6% / macOS + Windows (Tauri v2) — page-stated via WebFetch of the rendered repo, **NOT independently API-verified §37.4** (env mocks the GitHub API). Creation date NOT shown → velocity unestablished → **NOT a #52 claim.** Owner `rainnoon` (no disclosed identity).

## Pilot
**Fair pilot candidate** (MIT + mature 525c/v1.8.6 + cross-platform incl. Windows + reversible) — ⚠️ installs **hooks/plugins into your agents' config files** + `curl|bash`-style `install.sh`/`install.ps1`: `install-snapshot` first, snapshot `~/.claude/settings.json` (etc.), review what it writes. ⚠️ **12th consecutive monitor/manage-AI-coding-tools subject (v153→v164), ZERO piloted; 4th desktop-pet; mints nothing** — pilot one (oc-claw / agentpet / ping-island) or run the overdue audit, not a v165 in this niche.

Shipped on branch `wiki/v164-oc-claw` off main (at 8a054e0 = v163). Not auto-merged — operator reviews + merges.
