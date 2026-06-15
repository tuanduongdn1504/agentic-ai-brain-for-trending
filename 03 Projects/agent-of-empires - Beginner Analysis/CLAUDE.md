# agent-of-empires — Beginner Analysis (project CLAUDE.md)

**Subject:** `agent-of-empires/agent-of-empires` (AoE), canonical fork `njbrake/agent-of-empires` (**v162** wiki ship, 2026-06-15).
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.
**Routine:** v2.6 (§31/§35/§37). **Ships into the v158-audit-CONFIRMED Pattern Library.**

> **⚠️ Version catch:** v161 was already taken by **CodePilot** (commit `6c40e6a`; the root shim was stale at v160 and never recorded it). agent-of-empires = **v162**; streak GA:24 → **GA:25**. The shim is brought current + the drift flagged in this ship.

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis verdict + §35 + §37 + honest non-claims + the v161/v162 numbering catch.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY (session-multiplexer species N=2, decompose-the-held-theme, defer confirm/rename to audit) + observations.
- `02 Wiki/index.md` — the knowledge page.

## One-paragraph summary
**"A session manager for AI coding agents on Linux and macOS. Use it from the terminal (TUI) or from any browser (web dashboard)."** A **human-driven multiplexer** by **Nate Brake** (Mozilla.ai) that runs multiple AI coding agents (Claude Code + 12 others) **in parallel** — each in its own persistent **tmux** session on an auto-created **git worktree**, optionally inside a **Docker/Podman/Apple-Container sandbox** — with a ratatui **TUI** and a React **web dashboard / PWA** for live status, diffs, file-editing, and approvals; an **ACP structured view** (plan panels / tool-call cards / swipe-to-approve, with raw-tmux fallback); **`R`-to-expose-over-HTTPS** for phone access (Tailscale/Cloudflare Tunnel + QR/passphrase); and a **CLI + HTTP API** to drive sessions from external orchestrators ("integrates with OpenClaw"). Rust 68.7% + TS 29.7%; MIT; ≈2.6k★ / 1,370 commits / v1.11.0.

## Verdict rationale
- **(b) STRONG** = runs multiple coding agents in parallel = dead-center goal #1, and **literally this vault's own workflow**; **STRONG-not-STRONGEST** = a third-party harness *around* the agents (STRONGEST is reserved for the substrate / a methodology — the cmux/Paseo/v153 calibration).
- **(a) FAIL** = Nate Brake (US individual) + Mozilla.ai-backed community OSS; not a cultural-peer, not (a)-7 (Mozilla.ai **raised-and-rejected**: ships agent OSS but isn't a vault-substrate dependency); notable ≠ PASS (v139); no axis minted.
- (c) STRONG (mature Rust+TS, 1,370c/103 releases/v1.11.0; tmux+worktrees+sandbox+ACP+HTTP-API+PWA+Nix; the `#[setting(...)]` single-source-of-truth config macro + server-projected theming + 75%-Codecov-gate/dual-Playwright CI). (d) STRONG (session-multiplexer species N=2 with cmux; Paseo/cmux/harness theme decomposition; #84 13-agent cross-tool; OpenClaw/Hermes corpus-recursive; ACP-as-#18-B-candidate; #66 supply-chain; v122 dev-exhaust thread N=5).

## §35 / streak
**§35 STAYS CLEAR** — window {v160 GA, v161 GA, v162 GA} = 0 OG (**10 consecutive goal-aligned ships v153→v162**). NOT an override → override-frequency UNCHANGED (lifetime 10). Streak GA:24·OG:11 [7 ov] → **GA:25·OG:11 [7 ov]** (25th GOAL-ALIGNED PASS).

## Pattern Library
**PRIMARY (tier layer, 02b): the genuine 2nd "session-hosting multiplexer for AI coding agents (human-driven)" instance → species N=2** (v99 cmux native-desktop + v162 AoE cross-platform-TUI+web). **Decomposes** the v151/v158 "AI-agent orchestration theme HELD heterogeneous" finding (session-multiplexer species N=2 / Paseo agent-of-agents platform N=1 / harness team-generator adjacent); **DEFER confirm-or-split + rename to the overdue audit** (the v158 "don't generalize-to-fit" discipline). **0 new §C standalones.** Paseo stays N=1 (AoE is its *inverse* — orchestrate-ABLE via HTTP API, not an orchestrator). AoE ≠ v161 CodePilot's GUI-client standalone (multiplexer vs single-agent visual front-end). **NO confirmed-count change: 46 patterns / 10 Library-vocab CONFIRMED.** Observations (NOT minted): ACP architecturally-first-class but NOT corpus-first (v60/goclaw/get-shit-done prior) → future home Pattern #18 sub-mechanism B protocol-variant candidate, NOT a §C standalone; #66 supply-chain (curl|bash + tunnel exposure); #84 cross-tool (13 agents); OpenClaw/Hermes corpus-recursive; v122 internal-dev-exhaust thread N=5 (first goal-aligned member); single-source-of-truth `#[setting(...)]` config + server-projected theming; Nix flake (v68/v118/v150); agent-deck inspiration (cited-to-subject-elevation watch); NOT #18 #8 / NOT observability sub-archetype / NOT LV-C7 #22.

## Provenance (§37)
≈**2.6k★** / 226 forks / 14 watchers / **105 open issues** / **1,370 commits** / **v1.11.0** (Jun 10 2026) / **103 releases** / MIT / Rust 68.7% + TS 29.7% / Linux+macOS — page-stated via WebFetch (repo + agent-of-empires.com + Better Stack), **NOT API-verified §37.4** (env mocks the GitHub API). Age/velocity **inferred** (Show HN 2026-01-12 + v0.0.4 "Jan 9" → ~5 months → ≈~17★/day) → **NOT a #52 claim.** Owner Nate Brake (`njbrake`/@natebrake), Mozilla.ai.

## Pilot
**Strong pilot candidate — the single most pilotable subject of the entire v153→v162 run for THIS vault** (it's literally Storm Bear's workflow: run parallel Claude Code agents across branches, drive from the phone). `brew install aoe` / `nix run …` / cargo; MIT + cross-platform + reversible. ⚠️ **Pilot fence:** `curl|bash` install + the `R` remote-exposure tunnel (Tailscale/Cloudflare) puts your dev dashboard on the public internet → `install-snapshot` first + do NOT enable remote exposure on a real repo without understanding the tunnel. ⚠️ **10th consecutive "tool for operating AI coding agents" subject (v153→v162), ZERO piloted** — v161 CodePilot already broke out of the monitor sub-niche, so AoE is a follow-on, not the escape; the lever is unchanged and louder: **pilot one (AoE is the best candidate) or vary the domain.**

Shipped on branch `wiki/v162-agent-of-empires` off main (at b4b2caa, post-v161-CodePilot). Not auto-merged — operator reviews + merges.
