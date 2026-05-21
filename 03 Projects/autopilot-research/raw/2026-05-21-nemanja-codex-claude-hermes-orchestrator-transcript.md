---
source: yt-dlp-only
path: 5-yt-dlp
url: https://www.youtube.com/watch?v=O-PEeD7fymo
video_id: O-PEeD7fymo
title: "Codex Builds. Claude Reviews. Hermes Agent Runs It."
channel: Nemanja Mirkovic
channel_id: "@nemanja-mirkovic"
duration: 13:48
uploaded: 2026-05-20
views: 2175
fetched: 2026-05-21
language: en
notes: |
  Single-video ingest via yt-dlp auto-subtitles (no NotebookLM bundle).
  Operator-named anchor from Telegram message — user-elected single-video
  knowledge build, not topic burst.

  Pattern claim: Hermes Agent as orchestrator that delegates BUILD to Codex
  CLI and REVIEW to Claude Code CLI, with subscription-arbitrage motivation
  (running Codex+Claude through their native CLIs uses the user's existing
  subs; routing Claude through Hermes Profiles would burn extra balance).

  Architectural distinction from prior personal-repo sources: this is
  orchestrator-mediated cross-vendor cooperation (Hermes as 3rd-party
  conductor), distinct from router-mediated cross-vendor (howznguyen via
  9Router) and distinct from plugin-bridge cross-vendor (codex-plugin-cc
  publishes a plugin INSIDE Claude Code).
---

# Codex Builds. Claude Reviews. Hermes Agent Runs It. — transcript

> **Source:** [YouTube](https://www.youtube.com/watch?v=O-PEeD7fymo) — Nemanja Mirkovic, 13:48, uploaded 2026-05-20, 2175 views at fetch
> **Fetched:** 2026-05-21 via `yt-dlp --write-auto-subs`
> **Compile target:** `wiki/harness-engineering/personal-repo-hermes-orchestrator.md` (6th individual-scale sibling article)

---

## Topline thesis (from intro 00:00–00:30)

> "Everyone is trying to pick the best AI coding agent. Is it Claude Code? Is it Codex? Or is it Hermes agent? But I think that is the wrong question. What if we could use all three and use them for what they are actually good at? Codex builds, Claude reviews, Hermes agent orchestrates the whole thing and runs the loop."

The video sets up Hermes Agent as the **single touchpoint** for the operator. Hermes commands both Codex CLI and Claude Code CLI — the operator does not talk to Codex or Claude directly during the loop.

Credit: idea originated from a Shubham post on X about "Hermes + `/goal`".

---

## Architectural diagram (narrated)

```
operator
   │
   │ /goal "Build a demo Next.js app with SQLite..."
   ▼
┌──────────────────────────────────────────────────┐
│  Hermes Agent (orchestrator)                     │
│  - receives goal                                 │
│  - assigns worker                                │
│  - retains context layer + memory + logic        │
│  - final verification vs original spec criteria  │
│  - built-in Kanban task tracking                 │
│  - visual checks via vision (browser screenshot) │
└──────────────────────────────────────────────────┘
        │                            ▲
        │ subagent profile           │ subagent profile
        │ "coder"                    │ "reviewer"
        ▼                            │
   ┌─────────────┐              ┌─────────────┐
   │  Codex CLI  │  ──code──▶   │ Claude Code │
   │  (GPT-5.5)  │              │  CLI (Sonnet)│
   │  builds     │  ◀─errors─   │  reviews     │
   └─────────────┘   to fix     └─────────────┘
        │                            │
        └────── loops until ─────────┘
            ready for handoff
                    │
                    ▼
            Hermes final verify
                    │
              done / not done
```

---

## Why this composition (4 stated reasons)

1. **Subscription arbitrage.** Codex works fine with Hermes Profiles, but Claude doesn't — connecting Claude through a Hermes Profile pulls **extra balance** instead of using the user's actual Claude subscription limits and credits. Solution: invoke Codex CLI and Claude Code CLI as separate processes (each with native auth), not as Hermes-internal model providers.
2. **Clear separation of concerns.** Codex builds, Claude reviews. Roles are explicit.
3. **Native ecosystem retention.** Both CLIs keep their MCPs, plugins, skills, and tools intact. Hermes does NOT replace the harness — it conducts the harnesses.
4. **Hermes retains its strengths.** Hermes is good at context layer + memory + logic + the loop itself, so use it for that.

> "Hermes actually ships with two skills, one for Codex and one for Claude. So, it knows exactly how to use these two CLIs."

---

## Setup steps (narrated)

1. Verify `codex` and `claude` CLIs installed and authenticated.
   - If missing, ask Hermes itself: *"Hey, I need you to install Cloud Code CLI and Codex CLI so that I can log in with my subscription credentials."* Hermes installs both.
2. In VS Code with Hermes running, invoke `/goal <prompt>` where prompt explicitly assigns Hermes as orchestrator and instructs it to use the `coder` and `reviewer` profiles.
3. The example prompt: *"Build a demo Next.js app with SQLite. You're the orchestrator. Do not use coder reviewer..."* (Note: transcript is slightly garbled here; the prompt explicitly delegates to two specialized Hermes profiles configured to use the CLI subprocess rather than Hermes' native tools/models — the profiles act as triggers for the CLIs.)
4. Hermes creates a spec file (PRD-like) from the prompt.
5. Hermes opens its built-in Kanban app and starts driving tasks/subtasks.
6. Loop runs autonomously — operator can step away for 1-2 hours.

---

## /goal = Ralph loop internally

The host's previous video covered `/goal`, which is **"essentially Ralph loop, which runs internally in Hermes agent."** This composition (Hermes + Codex + Claude) is positioned as an upgrade to plain Ralph loop with only Codex.

---

## Observed run characteristics (Kanban Next.js + SQLite demo)

| Observation | Detail |
|---|---|
| Build model | Codex CLI, **GPT-5.5 fallback** (not the host's preferred default — flagged as anomaly) |
| Review model | Claude Code CLI, **Sonnet** (host explicitly says *"That's what I want to use. I don't use Opus cell."*) |
| Kanban behavior | First task appeared **unassigned** (flagged as weird) — Hermes did the work from terminal anyway, Kanban cards lagged |
| Build artifact visibility | Files appeared in repo (page, layout, API, lib — next.js scaffold) without showing in Kanban initially |
| Review pass | Claude review returned `pass` after Codex fixed dev-server error |
| Visual check | Hermes used vision to analyze the rendered page mid-loop — flagged as new/interesting capability |
| Functional verification | Drag-and-drop on Kanban worked first try ("very difficult for agents to figure out, you need a couple iterations, but this one got it right") |
| End state | Goal achieved, final report generated, app running |
| Comparison vs Ralph loop | "much better than the Ralph loop one. I'm quite surprised." Plain Ralph used only Codex 5.5; trio produced better output |

> Anomaly noted at end: *"The Codex `/go` wasn't available. Why is that? That's weird. I'll have to check into that."* — unresolved.

> Aesthetic caveat: *"It doesn't look the greatest, like it's not the best design"* — host suggests pre-feeding a design (e.g., from Claude Design) along with the prompt to fix.

---

## Generalization claim (closing, 12:30–13:30)

> "The conclusion here is it's not just about coding and reviews and all that. You can actually have your main instance of Cloud code or Codex with all the plugins, with all the scripts that you like, with all the automation that you already have, and have Hermes initiate those and run those. And that is the beauty of this. It doesn't have to be code. It can be any workflow that you use with Cloud or Codex, and Hermes can operate them, and that is what Hermes excels at."

Plus the subscription point reiterated: *"you can use Hermes with Cloud subscription, which doesn't cost you arm and a leg in the long run."*

---

## What's NOT in the video (gap list)

- **No Hermes installation/setup instructions** — host refers to previous videos.
- **No `agents.md` / coder.md / reviewer.md profile contents shown** — host offers to attach in comments if requested.
- **No discussion of failure modes** — what if Codex+Claude disagree forever? What's the loop terminator besides spec-match?
- **No cost comparison** — claim is "no additional API costs" because subs are leveraged, but actual token consumption per task vs single-Codex-loop not measured.
- **No comparison to router-mediated cross-vendor** — Hermes is a parallel mechanism to howznguyen's 9Router, but host doesn't acknowledge the alternative.
- **No discussion of vendor-platform risk** — Hermes is a 3rd-party orchestrator wrapping two competitor CLIs; what happens when Anthropic or OpenAI change their CLI APIs?
- **Codex `/go` missing anomaly** — flagged but not investigated.
- **Hermes Profiles vs CLI-subprocess delta** — host says Claude through Profile burns extra balance; doesn't explain WHY (presumably profile uses API-key billing, CLI uses subscription auth) — operator may want to verify.

---

## Quick takeaways

1. **Subscription-aware orchestration is the load-bearing innovation here**, not the role split. The role split (build/review) is already well-established (Pattern #76 in Storm Bear corpus). The novel piece is preserving native CLI auth for cost reasons.
2. **Hermes ships with skills for both rival CLIs** — concrete evidence of a 3rd-party agent platform investing in cross-vendor support.
3. **Single-touchpoint UX claim**: operator only talks to Hermes; both Codex and Claude are workers, not interfaces.
4. **`/goal` as Ralph-loop primitive**: this is the second source in the corpus claiming a slash command implements Ralph-loop as a first-class feature (vs hand-rolled scripting).
5. **Visual check via vision mid-loop** is a primitive not surfaced in the prior 5 personal-repo sources or the harness-engineering anchor.
6. **N=1 source** — claims require corroboration before promotion. Specifically: subscription-billing claim, the "much better than plain Ralph" comparison, and the generalization to non-code workflows.
