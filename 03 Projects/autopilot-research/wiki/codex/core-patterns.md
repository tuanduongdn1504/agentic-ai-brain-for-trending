# Codex — Core Patterns

> **Topic:** [[_index|codex]]
> **Source:** `../../raw/2026-05-13-codex-long-running-agentic-harness-alternative-to.md` § Trends

The 6 sources cluster around five recurring techniques that work the same way regardless of whether the harness is Codex or Claude Code. These are the operational primitives a Codex user is expected to know.

---

## Pattern 1: Project memory files (`agents.md` / `claude.md`)

The **single most-cited setup step** in the bundle [Source 4, Source 5]. Both Codex and Claude Code read a designated markdown file at the project root on every startup and use it as an **onboarding document**: project context, architecture, conventions, "rules the agent must not violate" [Source 4, Source 5].

- Codex convention: **`agents.md`** [Source 1]
- Claude Code convention: **`claude.md`** [Source 4, Source 5]
- Same role, different filename

Teacher's Tech calls this the **"single most important thing"** to set up before any other work [Source 4]. Mosh agrees and treats `claude.md` as foundational [Source 5].

Keith AI takes it further with an **automated update loop**: a cron-triggered skill analyzes recent agent interactions, detects misunderstandings, and **automatically updates `agents.md`** to encode the resolution [Source 1]. The memory file evolves over time, with the agent itself doing the maintenance.

> See `[[../claude-md-12-rules/_index]]` for the Mnilax/Karpathy individual-scale behavioral contract that fits inside this file.

---

## Pattern 2: Planning Mode (plan first, build second)

Multiple speakers — Mosh, Teacher's Tech, Riley Brown — advocate for **toggling into Planning Mode** before any multi-step task [Source 3, Source 4, Source 5].

- Triggered with **Shift+Tab** in Claude Code [Source 4, Source 5]; Codex has an equivalent mode demonstrated by Riley Brown and Keith AI [Source 1, Source 3]
- Agent drafts a **multi-step to-do list / implementation plan** for human approval [Source 4, Source 5]
- Human reviews the plan, edits if needed, approves
- Only then does the agent touch code

Why it matters: prevents the agent from "going down the wrong path" before any code is changed [Source 4]. Cheap to redirect a plan; expensive to undo half-finished code edits across many files.

The pattern composes with adversarial evaluation (Pattern 4) — Codex can be used to **review the plan** before Claude executes it [Source 6].

---

## Pattern 3: Git worktrees for parallel agent threads

The technical primitive that makes long-running parallel agents safe [Source 1, Source 3].

- Each parallel agent gets its **own git worktree** (separate folder, separate branch)
- Agents work in isolation — no risk of two threads editing the same file simultaneously
- Human reviews each worktree's diff, merges the good results, discards the bad

Keith AI and Riley Brown both demo running **10+ tasks in parallel** using this pattern [Source 1, Source 3]. Without git worktrees, parallelism is unsafe — agents will clobber each other's edits.

This is the operational backbone of "vibe coding multitasker" mode (see [[expert-disagreements]]).

> See `[[../autonomous-loops-human-in-the-loop/_index]]` for the human-oversight side of long-running parallel runs.

---

## Pattern 4: Adversarial evaluation (generator + evaluator)

The bundle's response to a hard problem: **agents are poor self-evaluators** [Source 2].

- The AI Automators describe a **"generator-evaluator" pattern** inspired by GAN networks [Source 2]
- The **generator** writes code (typically Claude Code)
- A separate **evaluator** is prompted to be **skeptical** of the generator's output — flag bugs, refuse mediocre work
- The evaluator does NOT share the generator's context, so it doesn't share the generator's blind spots

The key failure mode this pattern fixes: Claude often **identifies legitimate bugs but then "talks itself into deciding they weren't a big deal"** and approves the work anyway [Source 2]. A separate evaluator agent with adversarial system prompts breaks that self-rationalization loop.

Jack Roberts operationalizes this as the **"Three Brain Auto-Router"** [Source 6]:
- Claude → builder / generator
- Codex / GPT-5.5 → adversarial reviewer / evaluator
- Gemini → long-context analysis specialist

The router is itself a skill that decides which model to tag in based on the job [Source 6].

This is **the** core composition-pattern argument for keeping Codex installed even if Claude Code is your default builder.

---

## Pattern 5: Sandbox / permission model

The bundle treats sandboxing as **binary** [Source 3]:

- **Sandbox mode** — agent is restricted, must ask for permission to do dangerous things
- **Full access mode** — agent runs without permission prompts; user moves on to other tasks while the agent "cooks"

Riley Brown uses **full access** frequently to enable his multitasker workflow [Source 3]. Mosh and Teacher's Tech are more conservative — review every change [Source 4, Source 5].

The bundle's gap (see [[gaps-and-followups]]): **no granular IAM**. Production environments need fine-grained permission boundaries, not binary all-or-nothing. This is one of the largest unaddressed areas in the 6-source bundle.

Keith AI raises a related warning: **using Claude Code inside third-party wrappers (e.g. Open Code) carries "risk of being banned" by Anthropic** [Source 1]. The tool-choice question is not just technical — vendor policy matters.

---

## Pattern 6: Context management (compaction and resets)

A recurring operational technique to handle long-running sessions [Source 5].

- **`/compact`** — summarize the conversation history, free context window space [Source 5]
- **`/clear`** — start fresh, optionally with a summary file as the new context anchor [Source 5]
- Goal: avoid **"context anxiety"** — the failure mode where the model rushes to finish as the window fills up [Source 2]

Mosh notes that a full context window leads to **lower-quality responses AND higher token costs per request** [Source 5]. Both pressures push toward proactive context management.

The AI Automators offer a cynical take: even with Anthropic's claimed 1M-token Opus 4.6 window, context anxiety isn't fully solved — and Anthropic is incentivized to encourage long contexts because more tokens means more revenue [Source 2]. See [[expert-disagreements]].

---

## Pattern 7: Voice input (Whisper Flow / dictation)

A speed primitive cited by **three** speakers (Riley Brown, Keith AI, Mosh) [Source 1, Source 3, Source 5].

- Voice input via Whisper Flow or built-in OS dictation
- Speaking is **2-3× faster than typing** [Source 3]
- Essential for managing multiple parallel agent threads — typing becomes the bottleneck once you're orchestrating more than 2-3 worktrees [Source 1, Source 3]

This is the operational glue that makes the "10+ parallel tasks" workflow viable.

---

## Pattern 8: Skills and automations (cron-scheduled agents)

Riley Brown and Keith AI both center workflows around two layered concepts [Source 1, Source 3]:

- **Skills** — reusable workflow packages, like macros for agent behavior
- **Automations** — cron jobs that run skills on a schedule (e.g. weekly SEO report, nightly `agents.md` maintenance) [Source 1]

Plain-English **workflow files** describe repeatable processes step-by-step. Teacher's Tech argues these recipes outperform one-off prompts because they provide the agent with a clear reason-and-adapt framework [Source 4].

This pattern is identical to the autopilot-research `/loop` and `/schedule` invocations described in `../../CLAUDE.md`.

---

## Key Takeaways

- **Memory file at root** (`agents.md` / `claude.md`) is the "single most important" setup step [Source 4]
- **Planning Mode before coding** — every multi-step task gets a plan first [Source 4, Source 5]
- **Git worktrees** are the technical primitive that makes parallel long-running agents safe [Source 1, Source 3]
- **Adversarial evaluator** (separate agent / separate model) fixes Claude's "talks itself into approving" failure mode [Source 2, Source 6]
- **Three-brain routing** (Claude builds, Codex reviews, Gemini long-context) is the dominant multi-model composition [Source 6]
- **Voice input** is operationally necessary once you're running more than 2-3 parallel agents [Source 1, Source 3, Source 5]
- **Sandbox vs full-access is binary** in this bundle — granular IAM is a gap (see [[gaps-and-followups]])
