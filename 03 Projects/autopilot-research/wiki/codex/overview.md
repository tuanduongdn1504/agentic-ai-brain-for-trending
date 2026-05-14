# Codex — Overview

> **Topic:** [[_index|codex]]
> **Source:** `../../raw/2026-05-13-codex-long-running-agentic-harness-alternative-to.md`

---

## What Codex is in May 2026

By May 2026, **OpenAI Codex** has matured from "the model that powered the original GitHub Copilot" into a **long-running agentic harness** that lives in the terminal and runs end-to-end engineering tasks autonomously [Source 1, Source 3]. Keith AI and Riley Brown both frame it explicitly as **"the best AI coding tool"** or **"the best long-running agentic harness"**, positioning it head-to-head with Claude Code rather than as a chat-style assistant [Source 1, Source 3].

In this framing, Codex is not a model — it is a **harness** that wraps a model (GPT-5.5-class) with:

- Terminal-resident CLI
- File-system access
- Shell-command execution
- Git workflow integration
- Persistent project memory (`agents.md`)
- Planning mode
- Parallel-thread orchestration via git worktrees

This is the same architectural shape as Claude Code [Source 4, Source 5]. The bundle treats both tools as members of the **same category** ("agentic harness") that happen to come from different vendors [Source 1, Source 3, Source 6].

---

## The long-running-agent framing

A defining shift discussed across the bundle: the move **away from chat-style interaction** and toward agents that run for **minutes-to-hours** without needing per-step approval [Source 2, Source 3].

- The AI Automators source explicitly calls this Anthropic's "new blueprint for long-running AI agents" [Source 2]
- Riley Brown and Keith AI demonstrate Codex running parallel threads across multiple git worktrees, with the human acting more as orchestrator than line-by-line reviewer [Source 1, Source 3]
- The trade-off: long runs amplify both the upside (work completed while you sleep / multitask) and the downside ("context anxiety", quality regression in long sessions) [Source 2, Source 5]

The bundle's overall thesis: **agentic harnesses are the new primary surface for AI-assisted coding**, replacing copy-paste-from-chat. Codex and Claude Code are the two reference implementations of this category [Source 1, Source 3, Source 5].

---

## How Codex compares to Claude Code

The 6 sources draw the comparison from multiple angles. The recurring picture:

| Dimension | Codex | Claude Code | Notes |
|---|---|---|---|
| **Surface** | Terminal-resident CLI | Terminal-resident CLI, editor-agnostic [Source 5] | Same shape |
| **Memory file** | `agents.md` [Source 1] | `claude.md` [Source 4, Source 5] | Same role — "onboarding document" the agent reads at every startup [Source 4] |
| **Planning** | Planning mode (multi-step todo before code edits) [Source 1, Source 3] | Planning mode (Shift+Tab toggle) [Source 4, Source 5] | Same pattern |
| **Parallelism** | Git worktrees, multitasking across threads [Source 1, Source 3] | Git worktrees, parallel threads | Same pattern; Riley Brown and Keith AI both demo it heavily on Codex side |
| **Adversarial role** | Often used as the **judge** for Claude's output [Source 6] | Often used as the **builder**; "poor QA agent" by default [Source 2, Source 6] | Asymmetric — see [[expert-disagreements]] |
| **Context window** | Not directly characterized in this bundle | Anthropic claims 1M-token window with Opus 4.6 [Source 2] | The AI Automators are skeptical of this claim [Source 2] |
| **Stability claim** | "The NEW Best AI Coding Tool" [Source 3] | Mixed — "10x faster" [Source 5] vs "Forest Gump turned up" [Source 6] | See [[expert-disagreements]] |

The bundle does not give a head-to-head benchmark. The comparison is qualitative and based on speakers' lived experience over weeks/months of use [Source 1, Source 3, Source 5, Source 6].

---

## Where Codex fits in a multi-tool stack

The most explicit composition pattern in the bundle is **Jack Roberts' "Three Brain Auto-Router"** [Source 6]:

- **Claude** → primary builder (best at multi-file code generation and refactor)
- **Gemini** → long-context analysis (PDFs, videos, very large source trees)
- **Codex / GPT-5.5** → **adversarial review** of Claude's output

The router is a skill that automatically tags in the right model for the job, so the human doesn't manage three CLIs by hand [Source 6]. This is the most-detailed multi-model composition in the bundle and the single most-cited reason to keep Codex installed even if Claude Code is your default builder.

Counter-position from The AI Automators: with Opus 4.6's 1M-token window, you can "simplify the architecture" and remove planner/evaluator splits — effectively one-shot entire apps on Claude alone [Source 2]. See [[expert-disagreements]].

---

## Vibe coding vs real engineering — the philosophical layer

The bundle splits on what Codex (and Claude Code) are *for*:

- **Riley Brown and Keith AI** lean into "vibe coding" — fast multitasking, "full access" permissions, "let the agent cook" while moving on to other tasks [Source 1, Source 3]
- **Mosh and Teacher's Tech** insist on the **carpenter mindset** — AI is a power saw, not a replacement; the developer reviews every line of code and applies real engineering practices [Source 4, Source 5]

Codex is technically capable of both modes. Which mode you pick is a personal/team policy choice, not a Codex configuration choice. See [[expert-disagreements]] for the full split.

---

## Key Takeaways

- **Codex in May 2026 is a terminal-resident long-running agentic harness** — same category as Claude Code, not a chat assistant [Source 1, Source 3]
- The bundle treats Codex and Claude Code as **architecturally equivalent**: terminal CLI + memory file + planning mode + git worktree parallelism [Source 1, Source 3, Source 4, Source 5]
- The dominant composition pattern is **multi-brain routing** — Claude builds, Codex reviews, Gemini handles long-context [Source 6]
- The "long-running agent" framing matters: success measured in minutes-to-hours of autonomous work, not turn-by-turn chat [Source 2, Source 3]
- The bundle's value claims for Codex are **strong but unbenchmarked** — "NEW Best" [Source 3] sits alongside contrarian Claude regression takes [Source 6] with no head-to-head data
- Memory file naming convention: **`agents.md` for Codex, `claude.md` for Claude Code** — same role, different filename [Source 1, Source 4, Source 5]
- See [[practical-takeaways]] for the 10 actionable rules; [[core-patterns]] for the techniques; [[expert-disagreements]] for the unresolved fights
