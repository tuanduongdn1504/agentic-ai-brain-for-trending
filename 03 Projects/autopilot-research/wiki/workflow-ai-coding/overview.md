# Overview — Workflow for AI Coding

## The Ralph Wiggum loop

The dominant pattern across these 6 talks is what Greg Isenberg labels the **Ralph Wiggum loop** — a workflow that lets autonomous agents implement complex software while preserving code quality. The shape:

1. **"Grilling" / interview phase** — AI relentlessly interviews the developer until both reach a shared understanding of project goals.
2. **PRD generation** — that shared understanding crystallizes into a Product Requirements Document.
3. **Atomic decomposition** — the PRD is broken into small, verifiable user stories or kanban-board tickets.
4. **Autonomous implementation** — an agent picks tickets, writes code + tests, commits, logs progress, moves to the next.
5. **AFK execution** — the developer can be away from keyboard while the loop runs.

Test-driven development and acceptance criteria are the glue that keeps the agent honest. See [[core-patterns]] for the 5 trend clusters that show up across speakers.

## The contrarian frame: code as a premium asset

Underneath the loop sits a philosophical choice: how cheap is code? Two camps:

- **Ryan Lopopolo (OpenAI):** "code is free" — it's a disposable build artifact, like a compiler's machine code output. Implementation is no longer scarce.
- **Matt Pocock:** "code is not cheap" — bad code is more expensive than ever because it lowers the ceiling of what an agent can accomplish in that codebase.

Both speakers run AFK loops. They disagree on what's allowed to rot. See [[expert-disagreements]].

## Software fundamentals matter more, not less

Matt Pocock's central thesis (echoed in his "Software Fundamentals Matter More Than Ever" talk and the AI Engineer keynote) is that **bad codebases make bad agents**. Concretely:

- "Deep modules" (complex logic behind simple interfaces) are easier for AI to navigate than "shallow modules" (many tiny interconnected files).
- Test-driven development is the primary feedback loop — failing-test-first prevents the agent "outrunning its headlights".
- Reviewer-agent personas (security, reliability) in CI/CD catch slop before merge.

The role of the human shifts from *writing code* to *designing the harness* — prompts, guardrails, tests — that lets autonomous agents execute the full job while the human steers strategy. Ryan Lopopolo calls this **harness engineering**.

## What this means for an individual operator

Three operational shifts:

1. **You manage a token budget, not human-hours** — decide how many parallel agents to fire at a problem (Lopopolo).
2. **You orchestrate skills, not specialized agents** — Anthropic's Barry Zhang & Mahesh Murag argue against per-domain agents in favor of one general-purpose agent that pulls in skill folders at runtime.
3. **You think like a staff engineer managing a massive team** — code is free, agents are infinitely patient, your job is direction-setting and review.

See [[practical-takeaways]] for the 10 adoptable rules. See [[gaps-and-followups]] for what these talks don't cover.
