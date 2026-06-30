# Overview — Matt Pocock's Agentic Engineering Workflow (the podcast)

## Source

- **Video:** ["Matt Pocock's Agentic Engineering Workflow (just copy him)"](https://www.youtube.com/watch?v=nQwJVHCtDDY) — `nQwJVHCtDDY`
- **Channel:** **David Ondrej** (@DavidOndrej) — the *interviewer*, not Matt Pocock. (David also runs the AI channel + companies **Scale Software** / **Vectal.ai**.)
- **Guest:** **Matt Pocock** (@mattpocockuk, [aihero.dev](https://www.aihero.dev/))
- **Format / length:** conversational podcast, **1:02:24** · **Uploaded** 2026-06-18 · **245,765 views** · **Sponsor:** SerpApi
- **Raw transcript:** `raw/2026-06-30-pocock-agentic-workflow.md` (deduped, 12,548 words, read in full)

## Who is Matt Pocock

A well-known **TypeScript educator** (Total TypeScript course + book), formerly a **voice/singing coach** with an MA in Voice (~6 years), then a software developer (~5 years), an **XState** core-team member and a **Vercel** developer advocate. Now an independent **AI-engineering** educator at **aihero.dev** (free guides + a 70,000-developer "Skills" newsletter + paid workshops). Author of the **[mattpocock/skills](https://github.com/mattpocock/skills)** repo (150.8K★) and the **[mattpocock/sandcastle](https://github.com/mattpocock/sandcastle)** AFK orchestrator. He runs **Claude Code with Opus 4.8 at medium effort** and explicitly **did not** rush onto Fable when it launched "yesterday."

## The thesis chain (one screen)

1. **Harness > model.** Everyone obsesses over the model — the F1 *engine* — when the engine is only part of the car. You have **far more control over the harness** (prompts, skills, codebase, workflow, environment) than over the model. Treat it as **50/50**, not 90/10. → [[pocock-agentic-workflow/harness-over-model]]
2. **AI ate tactical programming; be strategic.** Borrowing **John Ousterhout's** tactical-vs-strategic distinction: AI now does the day-to-day code-writing (tactical) better and cheaper than you. Your edge is **strategic programming** — designing the system, scoping the work, defining interfaces and tests. You're the *general* directing an "infinite fleet of tactical programmers." → [[pocock-agentic-workflow/strategic-vs-tactical]]
3. **Your skills are the ceiling on what AI can do.** AI makes a *senior* ~10× because it has richer context to work with; a junior gets a small boost. The multiplier is *your* judgment. So **upskill the human**, don't delegate the thinking. → [[pocock-agentic-workflow/strategic-vs-tactical]]
4. **Skills = procedures (you invoke) vs abilities (the model invokes).** Matt prefers **procedures** — he keeps the steering wheel. Every model-invoked skill **leaks a description into the context window**, so he disables model-invocation on the ones he wants to drive himself. → [[pocock-agentic-workflow/skills-procedures-vs-abilities]]
5. **Work AFK through a queue, not a loop.** The real unlock isn't an infinite "Ralph" loop — it's **away-from-keyboard** agents picking scoped tasks off a **queue** (triage → explore → implement → review → merge), parallelized via **Sand Castle**. Push the human checkpoints **as far right as safe**, and build **self-improving** loops (e.g., a nightly security review) instead of expecting a fancier model to cover the gaps. → [[pocock-agentic-workflow/afk-queues-not-loops]]

## The closing prescription (the most actionable line in the video)

> *"First thing I would do: **delete every single skill, every plugin, every MCP server. Delete your `claude.md`, delete your `agents.md`** — go back to absolutely nothing, and observe the agent. See what it does. Everyone bloats their context window. Then layer things back on top — and make sure they're **procedures, not abilities** — that **you** decide. My skills repo is a great place to start. And try as much as you can to delegate the implementation to an **AFK agent**."*

This is the whole philosophy compressed: **strip the harness to bare metal, observe, then re-add only what you deliberately choose** — keeping the human in control of the context and the strategy.

## A few smaller, concrete habits he mentions

- **Dictation is "overpowered."** Matt dictates with **Wispr Flow** (the podcast says "Whisper Flow"; the product is *Wispr Flow*). "Output tokens from your brain and back into your brain" faster.
- **Don't chase new models.** He waited ~a month on Opus 4.5 and is doing the same with Fable; the cost/latency/availability usually isn't worth the launch-week hype.
- **Build a business the old way.** AI doesn't give you original ideas — *talk to customers*, build prototypes, and **ask AI what to remove**, not what to add. Product fundamentals are unchanged.
- **Enthusiasm beats experience.** A great junior who's an AI true-believer + a little software fundamentals can out-produce a reluctant senior — but the *senior who embraces it* gets the biggest multiplier.

## Key Takeaways

- The video is a **conversation**, not a structured talk — the value is the *mental model*, not a step-by-step. (For the structured version with Smart Zone / tracer-bullets / the 4-role architecture, that's Matt's **separate AI-Engineer-2026 workshop** — see [[pocock-agentic-workflow/source-provenance]].)
- Every claim here is **Matt's operating philosophy**, much of it opinion he flags himself ("I'm not a pundit"). The deep-dives separate **what's a verifiable fact about the tools** from **what's Matt's stance** — see [[pocock-agentic-workflow/caveats-and-disagreements]].
- The single most portable idea: **you control the harness; spend your effort there.**
