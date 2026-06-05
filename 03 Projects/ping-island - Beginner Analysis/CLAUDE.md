# ping-island — Beginner Analysis (project CLAUDE.md)

**Subject:** `erha19/ping-island` (v160 wiki ship, 2026-06-05).
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.
**Routine:** v2.6 (§31/§35/§37). **Ships into the v158-audit-CONFIRMED Pattern Library.**

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis verdict + §35 + §37 + honest non-claims.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY NEW sub-flavor (c) attention/approval-interrupt-routing (N=1, CORPUS-FIRST); sub-archetype N=8→N=9; observations.
- `02 Wiki/index.md` — the knowledge page.

## One-paragraph summary
**"A Dynamic Island-style command center for managing all your AI coding agents on macOS."** A native-macOS **Swift 6.1** (98.5%) **notch / Dynamic-Island** surface (Apache 2.0; macOS 14+) by `erha19` (no disclosed identity) that stays compact until a coding agent **needs action** — tool-call approval, input/follow-up, review, intervention — then surfaces it in the notch with one-click **approve / deny / answer** and **routes focus back** to the originating terminal/IDE. Works with **13 agents** (Claude Code, Codex, Gemini CLI, Hermes, Qwen, Kimi, OpenClaw, OpenCode, Cursor, Qoder, CodeBuddy, WorkBuddy, Copilot) via **managed hook files** (`~/.claude/settings.json` etc.) + live `codex app-server` WebSocket + **SSH bridge forwarding** of remote sessions + IDE extensions. Explicitly **"actionable focus interrupts ... rather than read-only dashboards."** v0.21.1; 832★; 433 commits.

## Verdict rationale
- **(b) STRONG** = an attention/approval router for Claude Code + 12 agents = goal #1 + arguably the most *operationally useful* shape in the niche (the actionable layer, not a dashboard). **STRONG-not-STRONGEST** = a surface *around* the agents.
- **(a) FAIL** = `erha19` discloses no name/affiliation/location; **no cultural-peer inferred from the handle** (v139 / v151-(a)-rescue discipline); no axis minted. (b) carries.
- (c) STRONG (Swift 6.1 native + notch UI + 13-client managed-hook integration + codex app-server WS + SSH bridge + IDE extensions; 433c/v0.21.1). (d) STRONG (observability sub-archetype new sub-flavor (c) → N=9 + Swift-native-macOS cluster + #84 cross-tool 13 + hooks/permission mechanism shared with v156).

## §35 / streak
**§35 STAYS CLEAR** — window {v158 GA, v159 GA, v160 GA} = 0 OG (8 consecutive goal-aligned ships v153→v160). NOT an override → override-frequency UNCHANGED (lifetime 10). Streak GA:22·OG:11 [7 ov] → **GA:23·OG:11 [7 ov]** (23rd GOAL-ALIGNED PASS).

## Pattern Library
**PRIMARY: NEW 3rd sub-flavor (c) "Attention / Approval-Interrupt-Routing Surface (notch/Dynamic-Island-first, focus-return + SSH-forwarding)" of the v158-audit-CONFIRMED "AI-Agent Observability / Status-Surface Tool" sub-archetype — PROVISIONAL N=1, CORPUS-FIRST.** Distinct from (a) metering (v89/v109/v157/v158/v159 — read-only numbers) and (b) ambient-pet (v154/v155/v156 — affective character). **A genuine mint, NOT manufactured** (unlike v159 CodexBar's 0-mint clean metering instance): ping-island is functionally neither metering nor a pet; external corroboration (NOT counted) = the forming "Dynamic Island for agents" genre (CodeIsland/xisland/Vibe Island). Minimal-inflation home = a 3rd sub-flavor inside the existing sub-archetype (the (a)/(b)-inside / 8a/8b precedent). **Sub-archetype N=8 → N=9; 0 new §C standalones; CONFIRMED Library-vocab UNCHANGED at 10; top-level pattern count UNCHANGED at 46.** Promotion-eligible at a genuine in-corpus N=2. Observations (NOT minted): light-control affordance (approve/deny agent's own prompts = pass-through, v156's affordance) ≠ LV-C7 #22 (observe+route ≠ control config/accounts); hooks-integration mechanism shared w/ v156; SSH-forwarding corpus-first capability within (c); Swift-native-macOS cluster N+1; #84 cross-tool (13); NOT #18 #8; NOT a #52 claim (832★, age unverified §37.4); (a) FAILS (no identity, no handle-inference).

## Provenance (§37)
≈**832★** / 89 forks / 1 watcher / 3 issues / **433 commits** / v0.21.1 (Jun 5 2026) / Apache 2.0 / Swift 6.1 (98.5%) + Shell / macOS 14+ — page-stated via WebFetch + erha19.github.io/ping-island, **NOT independently API-verified §37.4** (env mocks the GitHub API). Created date NOT shown → velocity unestablished → **NOT a #52 claim.** Owner `erha19` (no disclosed identity).

## Pilot
**Strong pilot candidate — the most operationally useful of the niche** (it targets the real flow-break: an agent blocked on your approval/input you didn't notice). Apache-2.0 + mature (433c/v0.21.1) + `brew install --cask ping-island`; reversible; ⚠️ it installs **managed hooks into your agents' config files** (`~/.claude/settings.json` etc.) — `install-snapshot` first AND snapshot those config files; review what it writes. ⚠️ **8th consecutive "monitor/manage AI coding tools" subject (v153–v160), ZERO piloted** — this one mints a real sub-flavor (more additive than v159), but a mint is still not a pilot; pilot one or vary the domain.

Shipped on branch `wiki/v160-ping-island` stacked on `wiki/v159-codexbar` (which is stacked on `wiki/audit-v158`, off main at c3ca247=v158). Not auto-merged — operator merges the stack in order: audit → v159 → v160.
