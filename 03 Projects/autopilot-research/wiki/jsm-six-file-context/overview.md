# Overview — "How Senior Engineers Actually Build With AI in 2026"

> **Source:** [14RP8liACqo](https://www.youtube.com/watch?v=14RP8liACqo) — JavaScript Mastery (Adrian Hajdin), uploaded 2026-05-01, 3:58:17, ~680K views, 1.25M subs. Raw transcript: `raw/2026-07-03-jsm-six-file-context.md` (~40.3K words, read in full).
> **Companion repo:** [adrianhajdin/ghost-ai](https://github.com/adrianhajdin/ghost-ai) — created 2026-04-27 (4 days before the video), 240★/93 forks, 33 commits, 8 PRs, **no license**.

## The thesis

- Opening claim: *"It's 2026 and most of the senior engineers I know aren't really writing code anymore. They design the systems and let AI handle the implementation."* Contrasted with "vibe coding" (describe outcome → let agent run → react), which Adrian argues collapses on non-trivial projects "by week three."
- Grounding analogy: at Google/Amazon/Netflix, serious projects start with weeks of design docs / RFCs / one-pagers; senior engineers "sometimes go months without writing production code" (transcript ~150–169). *"Software engineering has never really been about typing the most lines per day."* — AI "didn't invent that discipline. It just made it the most important skill in the room."
- Headline claim about the build: *"I didn't write a single line of it. An agent built the whole thing."* — rhetorically true for implementation code; the human wrote/curated the six context files + 29 feature specs + all prompts (see [[caveats-and-corrections]]).

## What actually gets built

**Ghost AI** (README calls it "Ghost Arc") — a real-time collaborative systems-architecture canvas SaaS:
user submits a plain-English prompt → a Gemini-powered **design agent** draws nodes/edges live onto a shared React Flow + Liveblocks canvas → team refines collaboratively → a second AI task converts the graph + chat history into a downloadable Markdown **technical spec**.

Stack: Next.js 16.2.4 / React 19 / TypeScript / Tailwind v4 / shadcn/ui / Prisma 7.8 + Postgres / Clerk auth / Liveblocks / Trigger.dev / Vercel Blob / CodeRabbit review. Details in [[ghost-ai-product]].

## The meta-loop (explicit, verified)

> *"I built this app using the exact methodology the app itself is designed to teach. Specs first, architecture defined, every feature planned before we start building."*

The product **automates the methodology**: the six-file system + feature specs are the manual discipline; Ghost AI's design-agent + generate-spec tasks are the same discipline productized (prompt → architecture diagram → spec document). The output spec is pitched as input for "a thinking or planning AI agent... the strongest possible starting point" for building an app — the loop closes on itself.

## The methodology in one screen

1. **Architecture first** — design the system (with a planning AI as sparring partner) before any code.
2. **Six-file context system** in `context/` — [[six-file-context-system]]: project-overview, architecture-context, ui-context, code-standards, ai-workflow-rules, progress-tracker. `AGENTS.md` tells every agent to read them in order.
3. **One numbered feature spec per unit of work** (29 in the repo) with a "Check When Done" gate — [[feature-spec-workflow]].
4. **One new chat per spec** — canonical meta-prompt: *"Read this file. Update the progress tracker. Implement exactly as specified."*
5. **Vendor agent skills** installed per stack tool via `npx skills add` — [[skills-supply-chain]].
6. **Review** via CodeRabbit (PR bot and/or VS Code extension) + manual browser testing — [[verification-and-review]]; NOTE: **no test suite exists** (verified).
7. **Progress tracker** updated per feature = persistent memory across sessions.

## Economics and model choice

- Adrian runs **Sonnet 4.6** ("fast... inexpensive... it sometimes gets lost **unless you have the context files**") over the default Opus 4.7 (1M context, "you're going to hit the limits very soon") — an explicit harness-compensates-for-smaller-model position; the individual-scale version of the [[../harness-engineering/_index|harness-over-model]] thesis.
- New-chat-per-spec is framed as token-budget discipline: it "lowers the overall context window and the amount of tokens that we're spending for each transaction, and it also makes the agent that much more focused."
- Empirical moment against batching: 7 fixes in one chat → 1 silently missed; *"as soon as you go deeper into the conversation, the agent can easily get lost."*
- 28 features completed in the documented arc; full auth feature landed in ~2 minutes of agent execution; ~1 major on-camera failure (canvas drag-and-drop) rescued by a vendor skill.

## Role definition

> *"You are the architect and agent is just a coder."*

The human's leverage: writing/refining specs, choosing split boundaries, reviewing diffs and CodeRabbit findings, manual QA. The agent's job: execute a bounded spec against pinned context.

## Key Takeaways

- The six-file system is a **portable context architecture** — the files travel with the repo, so any agent (Claude Code, Codex — both demoed) resumes with one prompt.
- **Scoping discipline is the core mechanism**: "work on one feature unit or subsystem at a time... prevents most failures that agents cause" (transcript + `ai-workflow-rules.md`, verified verbatim).
- Spec quality is presented as **capital allocation**: effort spent up front buys predictable execution and fewer corrections downstream.
- The strongest verified finding for our corpus is not the six files but the **skills supply chain** around them — vendor-published skills + lockfile + symlinked `.agents/skills/` ([[skills-supply-chain]]).
- Treat the "senior engineers don't write code anymore" framing as **marketing-sharpened**, not established consensus — see [[originality-and-reception]] for the counter-evidence.
