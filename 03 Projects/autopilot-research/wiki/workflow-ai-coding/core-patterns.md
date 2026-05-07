# Core Patterns — 5 trend clusters

Five clusters of recurring practice surface across the 6 speakers. Each cluster has multiple advocates — these are the patterns where consensus exists.

## 1. Planning-first workflow

**Alignment before execution** is treated as the most critical stage.

- **"Grill Me" technique (Pocock):** force the AI to interview you until you reach a shared design concept. Inverts the usual flow — the AI is the adversary, the developer is the source of truth.
- **PRD as destination (Pocock, Carson):** start with a Product Requirements Document. Concrete end-state beats vague intent.
- **Plan Mode (Boris / Claude Code):** Anthropic's default — back-and-forth alignment chat before any file edits.
- **Vertical slices / tracer bullets (multiple speakers):** instead of "all DB then all UI", write thin chunks of functionality that span the whole stack. Integrated feedback from minute one.

> Pocock and Boris disagree on Plan Mode vs Grill Me — see [[expert-disagreements]].

## 2. The autonomous "Ralph" loop

The shared pattern for AFK (away-from-keyboard) development.

- **Atomic task decomposition** — features split into small user stories with clear acceptance criteria.
- **Iterative cycle** — agent picks story from backlog (often JSON or markdown file), implements, runs tests, commits, logs progress, moves on.
- **Context management** — speakers warn against the "dumb zone" of large context windows. Recommend short sessions, "compacting" information, or fresh loops to keep AI sharp. (Note: Pocock and Lopopolo disagree on compact vs clear — see [[expert-disagreements]].)

This is a closed loop. The developer can be asleep; the agent keeps shipping.

## 3. Tooling and persistent memory

The trend is moving away from custom per-domain agents toward **standardized skills + repository-level instructions**.

- **Skills over agents (Zhang & Murag, Anthropic):** build a library of skills — folders of markdown instructions and scripts — that any general-purpose agent can pull in at runtime. Don't build a "Tax Agent"; build a "Tax Skill" that Claude Code loads when needed.
- **Markdown-based memory:**
  - `claude.md` / `agents.md` = project's long-term memory (tech stack, coding conventions, dos and don'ts).
  - `progress.txt` = short-term memory for a specific multi-step iteration.
- **Model Context Protocol (MCP):** the emerging standard for connecting agents to external tools (Slack, browsers, databases). Mentioned by Boris and others as the integration layer.

The composition: one general agent + many skills + persistent project memory + MCP-connected tools.

## 4. Verification and software fundamentals

There's strong consensus that **software fundamentals matter MORE because bad codebases make bad agents**.

- **Test-driven development (TDD)** — write failing test first. Forces small, verifiable steps. Universal advocacy.
- **Deep modules (Pocock)** — complex logic hidden behind simple interfaces. Easier for agents to test and navigate than shallow, tightly-coupled module trees.
- **Reviewer-agent personas (Lopopolo, OpenAI)** — agents that act as security engineer, reliability expert, etc. in CI/CD. They catch slop before merge. Replaces some traditional human code review.

This is the layer that distinguishes "AI-augmented engineering" from "vibe coding".

## 5. Infinite parallelization

Once you accept that code is cheap and agents are patient, you scale by **count of parallel agents**, not by individual productivity.

- **Parallel execution (Boris, Pocock):** multiple Claude Code sessions or sandboxes in parallel, each on a different branch or independent kanban issue.
- **Token budgeting (Lopopolo):** the unit of cost is no longer engineer-hours, it's tokens. Decide how many parallel agents to fire at a problem.
- **Staff-engineer mindset:** treat yourself as managing a massive team, not as an IC.

This pattern is what makes the [[practical-takeaways|10 takeaways]] worth adopting — without parallelization, the loop is just "AI typing for me", which doesn't justify the operational overhead.

## How the patterns compose

A typical day for someone running these:

1. Morning: grill phase + PRD + atomic-story decomposition for next feature (~30 min).
2. Kick off 2-4 parallel Ralph loops on independent stories.
3. Reviewer agents run in CI/CD as agents commit.
4. Human spot-checks merged code, updates `claude.md` with new lessons.
5. Repeat.

See [[overview]] for the philosophical frame, [[expert-disagreements]] for where speakers diverge, [[practical-takeaways]] for the rules.
