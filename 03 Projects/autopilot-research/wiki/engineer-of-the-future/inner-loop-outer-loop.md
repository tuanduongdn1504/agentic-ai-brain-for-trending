# Inner Loop = Capability, Outer Loop = Agency

> **Source:** Addy Osmani keynote [`n97BCfyFIvw`](https://www.youtube.com/watch?v=n97BCfyFIvw), AI Engineer World's Fair 2026 ("Don't build agents you can't answer for" / [Own the Outer Loop](https://addyo.substack.com/p/own-the-outer-loop)).

## The boundary that organizes everything

Osmani's central architectural distinction:

| | **Inner loop = capability** | **Outer loop = agency** |
|---|---|---|
| Who | Agents | Humans |
| What | investigate · implement · test · report | decide · verify · approve · own |
| Nature | execution | responsibility |

> "The boundary is **not** *human looks at AI output*. The boundary is **evidence and responsibility**."

This holds whether you run a handful of agents or thousands. The agent returns evidence (diffs, tests, logs, rationale, traces, screenshots — whatever the work requires); **then the engineering begins**: decide whether the work was worth doing, verify the evidence is enough, and approve / redirect / own what reaches production.

## How we got here: harness → loop → factory

Osmani frames three escalating layers (all dominant themes at AIEWF 2026):

1. **Harness engineering** — the coding agent is *model + harness* (context, tools, filesystem, git). The harness is what turns raw intelligence into something you can *delegate to*. (See [[harness-engineering/_index]].)
2. **Loop engineering** — you stop prompting one run. You design systems that **keep prompting, checking, remembering, and deciding what happens next.** This is when agents "start to feel like infrastructure." (See [[autonomous-loops-human-in-the-loop/_index]].)
3. **Software factory** — put it together and agents run the **inner loop** while **evidence comes out**. Humans still make the production decisions. *(Osmani credits "Dex's talk" — Dex Horthy of HumanLayer, whose AIEWF talk was "Harness Engineering is not Enough: Why Software Factories Fail"; Osmani's parallel essay is "Software Factories, Light and Dark." The two present complementary views: Osmani — humans own the outer loop; Horthy — hype outpaces discipline.)*

The through-line: the wind isn't moving humans *out* of the loop; it's moving **human judgment to the highest-leverage checkpoint.**

## Execution ≠ responsibility

> "Agents can choose, route, merge, escalate, and operate inside policy. In many systems they can and should. But **execution and responsibility are very different things. The agent can follow your runbook, but it can't inherit the consequences.**"

When something fails, the questions are human: *Who understood the policy? Who accepted the risk? Who owns the blast radius?*

## The agency ladder

Osmani's ladder of increasing ownership:

**flag → execute → diagnose → propose → recommend → resolve → discernment**

- Bottom: someone who *flags* a problem and leaves it for the system.
- Top (rare): **discernment** — finding a problem and deciding *whether it's even worth investing in* (maybe it isn't; maybe you move on).
- Point: when agents make more paths possible, agency is **not chasing every path** — it's **deciding which paths deserve your ownership and attention.**

**High agency** = "ownership with judgment attached." *Not* "I personally do everything" (doesn't scale), *not* "hustle theater."

## Key Takeaways

- **Inner loop = capability (agents); outer loop = agency (humans).** The boundary is evidence + responsibility, not "human eyeballs on output."
- The stack that produced this: **harness engineering → loop engineering → software factory.**
- **Execution ≠ responsibility** — an agent follows the runbook but can't inherit the consequences / blast radius.
- The **agency ladder** tops out at *discernment*: deciding which problems are worth owning at all.
- High agency = ownership with judgment attached, at any agent count.

## See also

- [[engineer-of-the-future/osmani-answerability-thesis]] — "own the verdict" / "explain it or don't ship it"
- [[engineer-of-the-future/three-failure-modes]] — orchestration tax is what breaks the outer loop at scale
- [[engineer-of-the-future/cursor-tab-agent-teams]] — the same shift as an industry trajectory ("agent managers")
- [[engineer-of-the-future/langchain-agent-futures]] — the systems view (continual learning across model/harness/context)
- [[harness-engineering/_index]] · [[autonomous-loops-human-in-the-loop/_index]] · [[multi-agent-orchestration/_index]]
