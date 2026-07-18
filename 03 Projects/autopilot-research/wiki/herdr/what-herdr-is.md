# What Herdr is

## Source
- Bundle: `raw/2026-07-18-herdr/` (6 transcripts; t1 Chase AI anchor + t2-t6). See [[sources-and-stances]].
- Ground truth: [github.com/ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) README + [herdr.dev/docs](https://herdr.dev/docs/).

## Definition

- Herdr is a **terminal multiplexer** — like tmux, it lets you drive many terminal programs from one screen (panes, tabs, splits). Its tagline: *"agent multiplexer that lives in your terminal."*
- What makes it an **agent** multiplexer (not just a terminal one): it **detects the AI coding agent** running in each pane and shows its live state (**idle / working / blocked**) in a sidebar — zero configuration. [CONFIRMED — C01, C09]
- One **Rust** binary, no Electron; runs inside whatever terminal you already use.

## The problem it solves

The videos are consistent on the pain point (the Chase AI anchor states it cleanly):

- Running Claude Code + Codex + OpenCode (etc.) at once means **6-8 terminal windows**, no way to see at a glance **which agent needs you** vs which is still working, and the ever-present risk of **accidentally killing a window mid-task**.
- `agent view` inside Claude Code helps — but **only for Claude Code**. Developers increasingly mix harnesses (Codex, Grok, Devin, OpenCode), and want one cross-harness view. [CONFIRMED — C34]

Herdr answers that with **three core benefits** (the anchor's framing, all verified):

1. **Organization** — workspaces → tabs + panes group agents by project/subtask. [CONFIRMED — C34]
2. **Monitoring** — the agent sidebar shows idle/working/blocked across every agent, even ones not currently visible. [CONFIRMED — C09, C34]
3. **Persistence** — Herdr runs as a background server; close the window (or your laptop) and agents **keep running**; reattach later, even over SSH. [CONFIRMED — C15, C16, C34]

## What it is *not*

- Not a wrapper/interpreter around agents — the README stresses *"real terminal views, not a wrapped interpretation."* Each pane is a true PTY shell.
- Not a rendering surface — like tmux, it has **no built-in browser** for viewing rendered web output. (A video framed this as "unlike tmux" — that's backwards; both lack it. See [[caveats-and-corrections]], C25.)
- Not (yet) a fully cross-platform production tool — **Windows is beta**. [C13]

## Related

- [[architecture-and-detection]] — how the multiplexer + state detection + socket API work
- [[competitive-landscape]] — why it's positioned as "tmux for AI agents"
- [[external|Storm Bear: multi-agent-orchestration]] — the operator's related pilot thread
