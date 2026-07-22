# Cursor — Tab → Agent → Teams, and the Rise of the "Agent Manager"

> **Source:** Cursor, "The next era of AI coding" (`8h9j2rskP14`, May 2026). Speaker: **Michael Truell** (Cursor co-founder/CEO — verified; also delivered as the Compile 26 opening keynote).

## Framing: technology redefines categories

Truell opens on **Star Wars (1977)** and the **Dykstraflex** computer-controlled camera — a "before/after" moment for a whole industry — arguing software engineering is at the same inflection. *(The claim that the venue is now Cursor's office is **unverifiable**; the Star Wars premiere + Dykstraflex are real — see caveats.)* He also notes software's complexity is **hidden** (unlike a Gothic cathedral), which is why stakeholders underestimate the cost of change.

## The three eras

1. **Tab** — autocomplete; you drive, char by char.
2. **Agent** — you delegate a body of work; babysit 1–3 local agents editing the same codebase.
3. **Teams** — dozens of cloud agents, each on **its own computer**, running for hours/days autonomously.

**The measured shift (over 2025):**
- **Agent requests up ~15× YoY**; the ratio of agent-vs-tab usage inverted (from ~2.5:1 favoring tab a year earlier to ~2:1 favoring agents).
- Internally, **~30% of Cursor's own PRs are developed end-to-end by an agent with no human writing a line** (some sources report 35%) — the agent runs on its own cloud computer, works hours/days, opens the PR itself.
- In Cursor's **enterprise** segment, AI-generated code rose from **~15% a year ago to ~75%** — humans delegate rather than touch syntax.

## The role shift: engineers become "agent managers"

- Mental model: you no longer have "a couple thousand engineers" — you have "**tens of thousands of ghost colleagues**" working alongside the humans.
- Engineers increasingly **delegate and manage** parallel agents; they spend **much more time on review** (reading syntax, build versions, testing) and on **multitasking / parallelism / context-switching.**
- There's a **bad path**: you *can* generate unsustainable code, bad architecture, bugs — which is exactly why review time goes up. (This is the industry-trajectory version of Osmani's [[engineer-of-the-future/inner-loop-outer-loop]] — humans move to the outer loop.)

## The far-future experiment: an agent-built browser

- Cursor ran a project (**"FastRender"**): **hundreds of GPT-5.2 agents, ~1 week, ~3 million lines of code**, many PRs — building a prototype web browser.
- "No humans in the loop" is imprecise: it used an **agent hierarchy** — Planners, Workers, Judges (AI oversight tiers). Day 1 it couldn't render apple.com; by the end it *mostly* rendered simple sites. **Maintainability score ~1.3/5.** Explicitly nascent, not production-ready — a probe to inform the teams-era product.

## Key Takeaways

- **Three eras — tab → agent → teams.** Over 2025 agent requests rose **~15×**; internal end-to-end-agent PRs hit **~30%**; enterprise AI-generated code went **~15% → ~75%.**
- Engineers become **"agent managers,"** shifting time to **review + parallel orchestration** ("tens of thousands of ghost colleagues").
- There's a real **bad path** (unsustainable code) — hence more review, not less.
- The **FastRender** experiment (hundreds of agents, 1 week, 3M LOC) shows the ceiling *and* the fragility (maintainability 1.3/5) of full autonomy today.

## See also

- [[engineer-of-the-future/inner-loop-outer-loop]] — "agent manager" = owning the outer loop
- [[engineer-of-the-future/three-failure-modes]] — orchestration tax is the risk of this trajectory
- [[engineer-of-the-future/pragmatic-engineer-field-report]] — independent corroboration (Cursor internal stats)
- [[engineer-of-the-future/caveats-and-corrections]] — FastRender detail, Star-Wars-venue unverifiable
- [[herdr/_index]] · [[multi-agent-orchestration/_index]] — managing many parallel agents in practice
