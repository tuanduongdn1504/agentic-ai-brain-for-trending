# openpets — Beginner Analysis (project CLAUDE.md)

**Subject:** `alvinunreal/openpets` ("OpenPets") (v155 wiki ship, 2026-06-04).
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.
**Routine:** v2.6 (§31/§35/§37).
**Requested:** "build LLM wiki ... macOS app to manage multiple AI coding tools."

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis verdict + §35 + §37 + honest non-claims.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY: v154 standalone → N=2 (NO new standalone); registry 06 edited.
- `02 Wiki/index.md` — the knowledge page.

## One-paragraph summary
**"Desktop pets for AI coding agents. Install pets, connect Claude Code via MCP, and see live coding status on your desktop."** An **Electron** (TypeScript 84.9%) cross-platform (macOS/Win/Linux) **tray-first desktop companion**: an animated pixel-art pet that idles + **reacts to agent activity via MCP** (thinking / editing / testing / permission requests / success / error), supporting **Claude Code, OpenCode, Cursor, Pi + any MCP-capable agent**; ships Claude memory instructions + hooks + OpenCode plugins; bundled abilities (ambient check-ins, break nudges, focus timers); pet-pack management; privacy-conscious local IPC (static, local hook speech). Goal-aligned (operating + observing coding agents). Owner `alvinunreal` (Boring Dystopia Development); MIT; v2.5.0; 968★.

## Verdict rationale
- **(b) STRONG** = a desktop surface that shows **live Claude Code status via MCP** + reacts to agent activity = goal #1 (operating/observing coding agents) + vault-applicable. **STRONG-not-STRONGEST** = an ambient companion surface *around* the agents, not the substrate (the v154 calibration).
- **(a) FAIL** = `alvinunreal` / "Boring Dystopia Development" — no cultural-peer signal, not (a)-7. No (a)-rescue needed (b carries the goal-aligned include).
- (c) STRONG (Electron + MCP integration + hooks + OpenCode plugins + pet-packs; **968★ / 132 commits / 14 releases / v2.5.0** = more mature + popular than v154 agentpet [40★] and v153). (d) STRONG (strengthens the v154 desktop-pet-status-surface standalone to N=2 + Pattern #18 B1 MCP + #84 cross-tool + T2 observability adjacency).

## §35 / streak
**§35 STAYS CLEAR** — window {v153 GA, v154 GA, v155 GA} = 0 OG (3 consecutive goal-aligned ships). NOT an override → override-frequency UNCHANGED (7-in-20 trailing; lifetime 10). Streak GA:17·OG:11 [7 ov] → **GA:18·OG:11 [7 ov]** (18th GOAL-ALIGNED PASS).

## Pattern Library
**PRIMARY: "Ambient/Affective Multi-Agent Status Surface (reactive desktop-pet UI)" → N=2** (v154 agentpet native-Swift+socket/wrapper + v155 openpets Electron+MCP) — a genuine, fast, **independent** 2nd instance of the standalone minted one ship ago → **PROMOTION-ELIGIBLE at N=3.** Two integration sub-flavors recorded: socket-daemon/CLI-wrapper (v154) vs **MCP** (v155). **§28: 0 new standalones** (a strengthening, not a mint); registry 06 ACTUALLY edited (rule-5, the v154 row → N=2). NO confirmed-count change (46 patterns / 9 Library-vocab CONFIRMED). Observations (NOT minted): Pattern #18 B1 MCP N+1 (the integration mechanism); **T2 observability sub-archetype ADJACENT** (openpets shows live status but is companion/affective-centered with focus-timer/break abilities → NOT hard-counted as observability N=4; the affective-pet-surface standalone is its cleaner home — anti-inflation); Electron-desktop (cross-platform) vs v154 native-Swift contrast; Pattern #84 cross-tool (Claude Code/OpenCode/Cursor/Pi + generic MCP); #66 privacy-conscious local-IPC (static/local hook speech); Claude-memory-instructions + hooks + OpenCode-plugins integration surface; productivity-companion facet (focus timers / break nudges).

## Provenance (§37)
≈**968★** / 35 forks / **132 commits** / **14 releases** (latest v2.5.0, May 27 2026) / MIT / TypeScript 84.9% (+ JS 12.8%) / Electron (macOS/Win/Linux) — page-stated as of 2026-06 via WebFetch, **NOT independently API-verified §37.4** (env mocks the GitHub API). Creation date unstated → velocity unestablished → **NOT a #52 claim** (even at 968★). More popular than v154 agentpet (40★). Owner `alvinunreal` (Boring Dystopia Development).

## Pilot
**Pilot candidate** — MIT, mature (v2.5.0 / 132 commits / 968★), MCP-based so it plugs into Claude Code cleanly; cross-platform Electron. Genuinely vault-useful (live Claude Code status + ambient presence). `install-snapshot` first; reversible. ⚠️ But this is now the **3rd "manage/monitor AI coding tools" ship in a row (v153/v154/v155) with ZERO piloted** — the standing recommendation (pilot, don't just catalogue) is louder than the build.

Shipped on branch `wiki/v155-openpets` (stacked on the unmerged v154 branch). Not auto-merged — operator merges.
