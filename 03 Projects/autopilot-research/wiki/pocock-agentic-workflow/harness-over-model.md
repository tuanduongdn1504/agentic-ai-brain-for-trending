# Harness over model — the central argument

## Source

The spine of the [nQwJVHCtDDY](https://www.youtube.com/watch?v=nQwJVHCtDDY) conversation. Matt Pocock's "hot take," stated and re-stated across the hour. This is the **individual-scale** articulation of the same thesis [[../harness-engineering/_index]] documents at org scale (Lopopolo: "humans steer, agents execute").

## The argument

- **"Everyone's obsessed with the model — the engine of the Formula 1 car."** But the engine is only part of the system: there's the chassis, the aerodynamics, how it moves through the air. The **harness** is everything around the model that you can actually control: *the prompts, the skills, the codebase, the workflow, the environment the model runs in.*
- **You have far more control over the harness than over the model.** You can't change how Opus 4.8 thinks; you *can* change the spec it reads, the skills it pulls, and the codebase it edits.
- **Treat it as 50/50, not 90/10.** Matt's complaint isn't that the model doesn't matter — it's the *allocation of attention*. People put ~90% of their energy on model choice and ~10% on the harness; he thinks the split should be roughly even.

## "Optimize token spend" = improve the codebase

The most concrete, repeatable version of the thesis, in Matt's own framing:

> *"People ask me all the time, how do you optimize for token spend? **Have a codebase that's easier to make changes in.**"*

- A cleaner architecture with better guardrails means the agent **explores less, bangs its head against fewer walls, and spends fewer tokens.**
- Crucially: **a better harness lets a *cheaper/stupider* model succeed.** If you hamstring the model with a muddy codebase from day one, you'll *need* a top-tier model to claw value out of it.
- This is a direct bridge to [[../claude-api-cost-optimization/_index]]: the cheapest cost-optimization is often *architectural*, not a caching trick.

## DX vs AX (Developer Experience vs Agent Experience)

- **AX = the experience the *agent* has working in your codebase.** Anything that improves it — better skills, a clearer codebase, a more powerful model — raises output.
- **DX and AX overlap heavily.** A senior who knows how to build a codebase that's pleasant for *humans* is, mostly, building one that's legible to *agents* too. (See the mirror argument in the pilot menu: if a human can't follow your spec, the agent fails silently on it.)
- People remember to improve skills and chase models, Matt says, but **forget to improve the codebase itself** for AX — the biggest lever they actually own.

## Keep the harness model-agnostic

- **"I try to keep my workspace and my harness agent-agnostic as much as possible."** Apply good software fundamentals that have worked for 30–40 years and they'll likely keep working with the next model.
- **Don't over-optimize around one model.** If you tune everything to a specific model's quirks (this one likes short prompts; that one's bad at X), you lose focus on the fundamentals — and your setup rots when the model changes.
- **Corollary — don't chase new models.** Matt runs **Opus 4.8 at medium effort**, waited ~a month before trusting Opus 4.5, and is deliberately *not* rushing onto Fable. The launch-week "I one-shotted X" noise rarely survives the cost/latency/availability trade-off.

## The Bitter Lesson tension (and why it's miscalibrated)

David raises **Richard Sutton's *The Bitter Lesson*** (2019): in ML, general methods that ride increasing **compute** beat hand-crafted, human-knowledge-engineered approaches every time. The needle: *isn't Matt "falling into the Bitter Lesson" by optimizing his harness instead of just waiting for the model to get better?*

Matt's answer — and the deep-dive's sharper version of it:

- **The Bitter Lesson is about *algorithmic means* on problems with fixed ground truth** (chess, Go, vision, speech). It says: don't hand-engineer task-specific domain knowledge; let general learning + search win.
- **Harness engineering is *not* hand-engineered domain knowledge.** It's execution discipline — spec clarity, verification, a legible codebase. Sutton's lesson doesn't say "never invest in tooling or best practices."
- So Matt's conclusion — **optimize the harness AND expect the models to improve** — is *not actually in tension* with Sutton. The two operate on different layers. (The same essay shows up in [[../how-we-claude-code/_index]], where a speaker uses it as a looser *analogy* — "trust the model to extract requirements" — which over-reaches in the opposite direction.)
- Matt's own framing of the practical takeaway: **don't *wait* for AGI** ("that's a very stupid idea"); actively improve everything you control *and* use a good model. The disagreement with David is only about the *ratio*.

## David's counter (held for the critic article)

David pushes back: *"if you swap in a better engine, all of that [harness work] is instantly better"* and *"better models find deeper bugs you didn't even know to look for."* Matt's reply: you could surface those same bugs with a cheaper model **and the right harness** (e.g., a daily cron security review) — "we're lagging behind in our practices and expecting the model to pick up the slack." Full exchange in [[pocock-agentic-workflow/caveats-and-disagreements]].

## Key Takeaways

- **Spend your effort where you have control.** The harness — prompts, skills, codebase, workflow — is the lever; the model is the part you mostly can't change.
- **Cheapest token optimization = a codebase that's easy to change.** Better architecture → a cheaper model succeeds.
- **Improve AX, not just the model or the skills.** The codebase itself is the most-forgotten lever.
- **Stay model-agnostic and don't chase launches.** Fundamentals that worked for decades port across models; week-one hype usually doesn't survive cost/latency.
- **The Bitter Lesson doesn't condemn harness work** — it condemns hand-engineering *domain knowledge*. Optimizing execution discipline is orthogonal and compatible.
