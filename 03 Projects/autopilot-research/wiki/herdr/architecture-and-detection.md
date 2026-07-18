# Architecture & detection

## Source
- [herdr.dev/docs](https://herdr.dev/docs/) (concepts, agents, session-state, persistence-remote, socket-api) + repo README. Raw: `raw/2026-07-18-herdr/`.

## Structure: workspace → tabs + panes

- **Workspace** = top-level container (the anchor calls them "spaces"; think projects/folders). A workspace **owns tabs AND panes**.
- **Tab** = a layout inside a workspace. **Pane** = a real terminal (a true PTY shell).
- ⚠️ **Correction:** tabs and panes are **peer-level children of the workspace**, not "panes nested inside tabs." Several videos (incl. the anchor) described a strict spaces → tabs → panes nesting; the docs say *"a workspace owns tabs and panes."* [MISLEADING — C06; see [[caveats-and-corrections]]]

## Zero-config agent-state detection (the differentiator)

Detection requires **no per-agent setup**. Two-step mechanism (per herdr.dev/docs/agents):

1. **Foreground-process identification** — Herdr identifies the foreground process in each pane.
2. **Screen-manifest evaluation** — for agents without complete lifecycle hooks, it reads the live **bottom-buffer screen snapshot** and evaluates **TOML manifests** against it to classify state.

- **States:** docs classify **idle / working / blocked**; the README's marketing also uses "done". Treat the authoritative set as **idle (default) / working / blocked (needs input)**. [CORRECT-BUT-INCOMPLETE — C10: state names vary by source; audio/visual notifications not confirmed in primary docs.]
- Herdr also fetches **remote manifest updates from herdr.dev** and applies valid per-agent rule updates **automatically, without a restart** — so detection for new/changed agents improves without upgrading the binary.

## Socket API (agents drive Herdr)

- A **pure socket API** lets agents themselves **spawn panes, read output, and wait on each other** — i.e. an agent can orchestrate a multi-pane session programmatically (see the [agent skill](https://herdr.dev/docs/agent-skill/)). [CONFIRMED that agents spawn panes + read output + sync — C11]
- Nuance: agents **spawning panes** is documented; whether agents can independently **create whole workspaces** is not stated in primary docs. [CORRECT-BUT-INCOMPLETE — C11]
- The **response serialization format** (JSON vs other) is **not specified** in the primary README/docs summaries — refer to the agent-skill / socket-api docs for specifics. Do not assume JSON. [CORRECT-BUT-INCOMPLETE — C21]

This socket API is the concrete thing that makes Herdr an *agent runtime* rather than only a human-facing multiplexer — it's the most borrow-worthy idea for the operator ([[hireui-translation]]).

## Persistence & remote

- **Client-server:** a persistent server holds session state; the client can detach and the server + agents keep running. [CONFIRMED — C04]
- **Session state survives restart** — layout/tabs/panes resume automatically on reconnect; sessions persist across terminal closure, app restart, and (as long as the machine stays on) laptop-lid-close. Vanilla tmux loses sessions if its server dies; Herdr's persistent storage is a genuine architectural difference. [CONFIRMED — C05, C15]
- **Detach/reattach:** `ctrl+b q` detaches; running `herdr` reattaches. [CONFIRMED — C16]
- **SSH remote:** `herdr --remote <hostname>` or `herdr --remote ssh://you@server:2222`. Herdr becomes a thin local client, manages an SSH config with keepalive + a per-attach control socket, and attaches to the remote Herdr server. [CONFIRMED — C17]

## Input

- **Keyboard and mouse both first-class.** Keyboard uses a **tmux-style prefix** (default `ctrl+b`, then a key — e.g. prefix→v to split). Mouse supports click, drag-to-resize, split. [CORRECT-BUT-INCOMPLETE — C07: "mouse-first" overstates it (both are first-class); right-click is shown in a video but not documented in primary sources.]

## Related
- [[what-herdr-is]] · [[supported-agents-and-install]] · [[competitive-landscape]] · [[license-and-adoption-caveats]]
