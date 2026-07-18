# herdr — agent multiplexer that lives in your terminal

> **Topic created:** 2026-07-18 (autopilot `/loop`, operator anchor `neK8ydl0Vlk` Chase AI + 6-video bundle)
> **Subject:** [github.com/ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) — a Rust terminal multiplexer purpose-built for running multiple AI coding agents in one place, with zero-config agent-state awareness. Solo author **Oğulcan Çelik**.
> **Verification:** refute-first multi-agent workflow `wf_65ed9753-32f` (28 agents; 6 digests → 19 load-bearing claims → refute-first verify → synthesize → completeness critic). Grounded on the GitHub API + repo README + herdr.dev docs, with plugin/issue specifics independently re-checked by the main loop.

## One-line

**Herdr is "tmux for AI agents"**: a single Rust binary that runs 21 coding agents (Claude Code, Codex, Grok, Devin, OpenCode, …) across panes/tabs/workspaces, shows each agent's **idle / working / blocked** state in a sidebar via zero-config detection, keeps sessions alive after you detach (survives restarts, works over SSH), and exposes a **socket API** so agents can spawn panes and coordinate with each other.

## Claims scorecard (19 load-bearing claims)

**9 CONFIRMED · 7 CORRECT-BUT-INCOMPLETE · 3 MISLEADING · 0 FALSE · 0 UNVERIFIABLE**

The videos were **directionally accurate** — no outright falsehoods — but several claims need caveats (license, state-model, tmux comparisons, workspace hierarchy). See [[claims-scorecard]] and [[caveats-and-corrections]].

## Articles

| Article | What's in it |
|---|---|
| [[what-herdr-is]] | Definition + the multi-agent chaos it solves |
| [[architecture-and-detection]] | PTY multiplexer, zero-config state detection, socket API, persistence, SSH remote |
| [[supported-agents-and-install]] | The 21 detected agents + install methods |
| [[competitive-landscape]] | vs tmux, cmux, and other agent multiplexers |
| [[license-and-adoption-caveats]] | **AGPL-3.0 + commercial dual license**, solo-maintainer/beta risk, open bugs |
| [[claims-scorecard]] | All 19 claims with verdicts |
| [[caveats-and-corrections]] | The MISLEADING/INCOMPLETE items + corrected forms + the fetch-block incident |
| [[sources-and-stances]] | The 6 video sources, their stances, and bias notes |
| [[hireui-translation]] | Herdr as a **local operator dev-tool** — borrow/pilot/avoid (NOT candidate-facing) |

## Key facts (primary-source verified 2026-07-18)

- **17,839★ / 1,133 forks / 76 open issues**; created 2026-03-27 (~3.7 months old); latest **v0.7.4** (2026-07-15); active (pushed 2026-07-18).
- **Rust** single binary, no Electron. Runs in your existing terminal.
- **License: dual — GNU AGPL-3.0-or-later + commercial.** (GitHub's detector shows "NOASSERTION" because dual-licensing confuses it.)
- **21 agents** detected zero-config (Gemini CLI + Cline "less thoroughly tested").
- Author **Oğulcan Çelik** (`ogulcancelik`), solo, full-time "in the open"; gold sponsor Terminal Trove. Stated ambition: "the path to a real agent runtime."

## Bottom line

A genuinely differentiated, fast-moving tool in the crowded agent-multiplexer space (cmux, Conductor, Paneflow, Orca…). Its real edges: **zero-config agent-state detection across 21 agents** and a **socket API for agent-to-agent orchestration** — neither of which tmux does. Caveats that matter for adoption: **AGPL copyleft** (or pay for commercial), **solo maintainer**, **Windows beta**, and documented **status-detection bugs**. For the operator: a strong candidate as a **local dev-orchestration layer** for the multi-agent hireui workflow — see [[hireui-translation]].
