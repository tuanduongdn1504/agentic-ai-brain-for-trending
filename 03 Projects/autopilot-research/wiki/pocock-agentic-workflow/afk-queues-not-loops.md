# AFK, "queues not loops," and self-improving systems

## Source

The back half of [nQwJVHCtDDY](https://www.youtube.com/watch?v=nQwJVHCtDDY), where David asks about the "agentic loops" hype. Originals deep-dived: **Geoffrey Huntley's Ralph** (ghuntley.com/ralph) and **Peter Steinberger**. Sibling topic: [[../autonomous-loops-human-in-the-loop/_index]].

## AFK vs human-in-the-loop

- **Human-in-the-loop (HITL):** you're at the keyboard with the agent — best for **planning, complex implementations, and unscoped work** you need to figure out together.
- **AFK (away-from-keyboard):** you fire off an agent on a **scoped** task and it goes and does it. **"The moment I discovered AFK was the moment I really got into AI coding"** — because instead of babysitting permission prompts, "suddenly there are two of me, three, four, five" producing code you then review.
- AFK is the real multiplier; it just takes a little setup (the sandbox + workflow), then "it goes crazy."

## "Queues, not loops" — the reframe

David frames the hype: "agentic loops" went viral (he attributes the spark to **Peter Steinberger**, ~a week before); half of it is "research labs selling more tokens," half might be useful. Matt's reframe:

- **The Ralph loop** (Geoffrey Huntley): a literal `while` loop that pipes the same prompt to a coding agent again and again — `while :; do cat PROMPT.md | claude-code ; done`. Matt was talking about Ralph back in January.
- **But you don't need an infinite loop.** What you actually need is an **AFK agent that takes a specific scoped task and does it.** "The only thing I need out of this is the AFK agent."
- **So think in *queues*, not loops.** A queue is just a **backlog of tasks** (bug reports, feature requests). Multiple nodes/agents pick items off it; items get **triaged → explored → labeled → implemented → reviewed → merged**, and an item **comes off the queue when its PR merges.** *"That's all development is, really."*
- A single magic loop "that just goes and completes all the tasks" doesn't match how dev teams actually work — anyone can add a task or a label and kick off work. The loop idea is "useful but not the whole picture"; the queue is the better mental model.

Matt's live example: his **Sand Castle** repo's GitHub issues *are* the queue. He triages an issue **AFK** (explore → "is this trivial? possible?"), puts it back on the queue, then adds an **`agent-implement` label** to fire the implementation in his GitHub-Actions Sand Castle setup → PR → merge → off the queue. (See [[pocock-agentic-workflow/sandcastle-deep-dive]].)

David's analogy that Matt endorses: a **medieval king** with ministers. A minister you deploy and never hear from is "running on a loop" (could go right or wrong). What you actually want is the **queue**: people bring you problems ("famine here, invasion coming"), you **prioritize** ("50 bug reports, 3 are critical — fix those first"), and you stay in charge.

## Push human checkpoints "as far right as you can"

- **The goal is to remove HITL checkpoints where possible** — auto-merge the genuinely trivial (a misaligned UI element, an internal refactor that changes no behavior).
- **But "who reviews the AI that decides a PR is safe to skip?"** You still **spot-check** some of the PRs the agent marked auto-mergeable, to check the *reviewer* is calibrated — and you improve that over time.
- **What you gain from review is two things:** (1) **gating dangerous changes** (security, leaks) out of production, and (2) **insight into your own system** — watching the agent work tells you whether your *harness* is good. **You're reviewing the system that produces the code, not just the code.** That's [[../claude-code-observability/_index]] applied to your agents.
- Make review *seamless* to keep humans willing to do it: Matt cites people who have the **agent record a video walkthrough of a front-end change** and overlay text-to-speech narration, so the PR ships with a narrated demo — "one button-click away instead of a whole debugging session away."

## Self-improving systems — "if someone keeps stealing your bike, buy a lock"

When David marvels that a new model (Fable) found a deep security bug other models missed, Matt's response is the philosophy in miniature:

- The lesson isn't only "Fable is good" — it's **"there are security issues in your code, and you should have something that *checks* for them."**
- **You could run a daily cron job that does a security review** — a different part of the repo each day — with a **relatively cheap model**, and surface most of those bugs without the fancy model. *"We're lagging behind in our practices and expecting the model to pick up the slack."*
- This is what engineers have always done — **test suites, human reviews, refactoring** — to make code testable, correct, and changeable. A model uncovering a gap just means *do more of that*. **Design systems that improve over time**, rather than reaching for a fancier model each time.
- David's matching line: figure out **why it happened** — "if someone keeps stealing your bike, maybe buy a lock." Patch the *underlying* issue (a new skill, a staging process, a check), not just the symptom. That's a habit Matt puts "on the list" of what separates 10× AI builders.

## On the originals (corrections live in [[pocock-agentic-workflow/the-originals]])

- **Ralph is real and correctly attributed to Geoffrey Huntley** (article ["Ralph Wiggum as a software engineer," ghuntley.com/ralph](https://ghuntley.com/ralph/), **14 July 2025**; companion repo [ghuntley/how-to-ralph-wiggum](https://github.com/ghuntley/how-to-ralph-wiggum), 1.7K★). It's a single-agent, **file-system-as-state**, **greenfield-only** technique. (The deep-read's "$10.42/hr", "worked with Yegge at Sourcegraph," and "named because it made him want to vomit" details were **fabricated and excluded**.)
- **Steinberger** (Peter Steinberger, *steipete*, founder of PSPDFKit, creator of **OpenClaw**, now at OpenAI) was the **viral popularizer** of "design loops that prompt your agents" (~June 2026) — **not the originator** (Ralph predates him by ~a year). David hedged ("if I'm not mistaken") appropriately.

## Key Takeaways

- **AFK > babysitting.** Fire scoped tasks at agents and review the output; that's the real output multiplier.
- **Queues, not loops.** Development is a backlog worked by parallel agents (triage → explore → implement → review → merge), not one infinite loop. Labels/issues *are* the queue.
- **Push HITL checkpoints right, but spot-check the reviewer-AI.** Auto-merge the trivial; keep gating the dangerous; never stop sampling.
- **Review is observability into your harness** — you review the *system* that makes the code, not just the code.
- **Build self-improving loops** (e.g., a cheap nightly security-review cron) instead of expecting a fancier model to cover gaps. "Buy a lock."
