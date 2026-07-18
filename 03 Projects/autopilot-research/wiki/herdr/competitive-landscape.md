# Competitive landscape

## Source
- Video comparisons (t1 Chase AI, t2 DevOps Toolbox, t4 Hal Shin) + primary docs. The dropped t8 (Fru Dev "Tmux vs Cmux vs Herdr vs Paneflow") would have added a head-to-head — see [[sources-and-stances]] for why it wasn't fetched.

## vs tmux

Herdr is explicitly positioned as **"the tmux for AI agents"** (Hal Shin). Genuine differences:

| Dimension | tmux | Herdr |
|---|---|---|
| Mouse | supported but **manual config** | **first-class, zero-config** |
| Agent-state awareness | none | **zero-config detection across 21 agents** (idle/working/blocked) |
| Session persistence | lost if the server process dies (unless persisted externally) | **persistent storage survives server restart** |
| Agent API | text-based `send-keys` | **pure socket API** (agents spawn panes, read output, wait on each other) |
| Keyboard / maturity | mature, huge ecosystem | tmux-style prefix, but far younger ecosystem |

- ⚠️ One video framed tmux comparisons too strongly: mouse & persistence aren't things tmux *lacks* — they're things Herdr does **zero-config vs manual**. And "unlike tmux, Herdr has no built-in browser" is backwards — **neither** has one. [CORRECT-BUT-INCOMPLETE C24 · MISLEADING C25; see [[caveats-and-corrections]]]

## vs cmux and the agent-multiplexer field

- The anchor's cmux comparison: Herdr's edges over cmux are **persistence** and **easy Windows** use (though Windows is beta). [context — not independently verified against cmux; treat as the video's claim]
- The category is **crowded and moving fast** — the source search surfaced Herdr alongside **cmux, Conductor, Superset, Paneflow, Orca, AionUi, Omnigent**, plus Herdr+Hermes for phone orchestration. Herdr is currently the attention leader (17.8K★, HN front page per secondary sources).

## Deepen (t7 Better Stack + t8 Fru Dev comparison) — verified additions

**The structural axis that matters: CLI vs native desktop-app.** t8 surveys the field; the cleanest real distinction is form factor:
- **CLI / terminal-native:** Herdr (Rust), tmux — run inside your existing terminal.
- **Native desktop apps:** **cmux** (`manaflow-ai/cmux`, **Swift, Ghostty-based macOS app, 24,724★**, created 2026-01-28 — independently verified), Paneflow (brew-installed macOS app). These add a GUI (vertical tabs; cmux has a built-in browser) but are **macOS-bound** and outside the terminal.
- Herdr's pitch on this axis: the desktop-app conveniences (agent tabs, state sidebar, notifications) **without leaving the terminal** and **without macOS lock-in**.

**cmux is the nearest rival** — `manaflow-ai/cmux`, **24,724★**, Swift/macOS, and **older than Herdr** (Jan 2026 vs Mar 2026). Native app with a built-in browser + notifications; Herdr trades the GUI for terminal-nativity, cross-platform reach, and the socket API. t8's practitioner rates them closely — personally leans cmux as daily driver, calls Herdr "very promising."

**Why one practitioner switched to Herdr (t8):** tmux was "buggy" — long-running jobs froze — which pushed him to Herdr. A genuine reliability motivation, though anecdotal (no repro captured).

⚠️ **Do not trust t8's other competitor names/numbers.** Its auto-captions badly garble tool names ("Emacs/SiMax", "armox", "Ron Pane", "CC Max") and even swap tmux↔cmux (the caption reads "tmux has a built-in browser" — false; the creator was describing *cmux*). Only the independently-verified cmux facts above + the CLI-vs-desktop axis are asserted; every other competitor name/star-count from t8 is treated as **unverified**. See [[caveats-and-corrections]].

## What's genuinely differentiated

Stripping the hype, Herdr's defensible advantages are two:

1. **Zero-config agent-state detection across 21 harnesses** — the sidebar telling you which of N agents is blocked/working/idle, without wiring anything up, and with remote-updated manifests. No general multiplexer does this.
2. **Socket API as an agent-orchestration primitive** — agents spawning panes and waiting on each other turns the multiplexer into a substrate for multi-agent workflows, not just a human viewer. This is the "path to a real agent runtime" ambition.

Everything else (panes/tabs/persistence/mouse/SSH) is table-stakes multiplexer functionality done cleanly, not a moat. tmux still wins on maturity and ecosystem breadth.

## Related
- [[what-herdr-is]] · [[architecture-and-detection]] · [[hireui-translation]]
