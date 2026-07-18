# Claims scorecard

> 19 load-bearing claims consolidated from 6 videos (201 raw claims), refute-first verified against primary ground truth. Workflow `wf_65ed9753-32f`. Verified 2026-07-18.

## Tally

| Verdict | Count |
|---|---|
| ✅ CONFIRMED | **9** |
| 🟡 CORRECT-BUT-INCOMPLETE | **7** |
| 🟠 MISLEADING | **3** |
| ❌ FALSE | **0** |
| ❔ UNVERIFIABLE | **0** |
| **Total** | **19** |

**Read:** the bundle was directionally honest — **no false claims** — but promotional/tutorial framing left ~half the claims needing a caveat. The heaviest corrections are license, workspace hierarchy, and over-strong tmux comparisons.

## CONFIRMED (9)

| ID | Claim | Anchor of proof |
|---|---|---|
| C01 | Herdr is a terminal/agent multiplexer managing many agents+terminals from one interface | README tagline + docs |
| C04 | Client-server: persistent server keeps running after the client detaches | docs (persistent sessions, socket API) |
| C05 | Separates session (layout) from process state; layout survives server restart, unlike tmux | docs (survives restarts) |
| C09 | Auto-detects & displays agent state (Claude Code, Codex, Grok, Pi, OpenCode) in a sidebar | docs/agents (zero-config, 21 agents) |
| C15 | Sessions persist across shutdown/closure/restart; layout resumes on reconnect | docs (persistence) |
| C16 | Detach/reattach (prefix-q) exits client while server+agents keep running | docs (`ctrl+b q` / `herdr`) |
| C17 | SSH remote attach via `--remote <host>`; reads SSH config, connects to remote server | docs/persistence-remote |
| C29 | Software can be buggy; status-tracking mismatches observed | GH issues #198, #1514, #1441, #1243; 76 open |
| C34 | Three core benefits: organization, multi-agent monitoring, persistence | docs + tagline |

## CORRECT-BUT-INCOMPLETE (7)

| ID | Claim (as stated) | Missing caveat |
|---|---|---|
| C02 | "Rust, open-source under *unspecified* license, free to use" | License IS specified — **AGPL-3.0-or-later + commercial**; "free" omits copyleft. |
| C07 | "mouse-**first** (click, right-click, drag-resize)" | Keyboard & mouse are **both first-class**; right-click not in primary docs. |
| C10 | "states: idle/working/blocked/**done** + audio-visual notifications" | Docs say idle/working/blocked; "done" is marketing; notifications unconfirmed. |
| C11 | "skill lets agents spawn panes, **create workspaces**, orchestrate" | Spawning panes confirmed; **agent workspace-creation** not documented. |
| C13 | "works on Mac, Windows, and Linux" | **Windows is beta** (open Windows detection bug #1514). |
| C21 | "CLI/socket API; **all operations return JSON**" | Socket API confirmed; **response format not documented** — don't assume JSON. |
| C24 | "Unlike tmux: mouse, agent state, beautiful defaults, session/process separation" | tmux *has* mouse+persistence (manual); Herdr's edge is **zero-config**; "beautiful defaults" subjective. |

## MISLEADING (3)

| ID | Claim | Correction |
|---|---|---|
| C06 | "workspaces → tabs → **panes inside tabs**" (strict nesting) | A **workspace owns tabs AND panes as peers**; panes aren't nested in tabs. (docs/concepts) |
| C22 | Plugins include "file viewer, **Herder reviewer**, mirror" | file-viewer ✓ (156★) and mirror ✓ (35★) are real; **no "reviewer" plugin** could be located. |
| C25 | "Unlike tmux, Herdr has no built-in browser; agents **must** use Playwright/Chrome DevTools MCP" | **Neither** tmux nor Herdr has a browser (alike, not unlike); the "must use X" is unsupported by docs. |

## Notes
- Full reasoning + corrected forms per claim: see the verify-phase output referenced in the [[_index]] and the corrections article [[caveats-and-corrections]].
- Independent re-checks by the main loop (not just the workflow): the two plugin repos and issue #198/#1514 were confirmed directly via the GitHub API.
