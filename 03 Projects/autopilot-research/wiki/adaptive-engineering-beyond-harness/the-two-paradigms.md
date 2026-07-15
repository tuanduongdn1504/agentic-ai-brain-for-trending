# The Two Paradigms — Fixed/Factory Harness vs Adaptive Engineering

The spine of the talk is a single dichotomy, explicitly framed as a **continuum** rather than a binary. See [[overview]] for the arc and [[complexity-science-foundations]] for the philosophy underneath.

## Shared definition (both paradigms agree on this)

> *"The model is the engine, and the harness is everything built around it to make that engine useful."* — [05:21]

Chandegra's harness anatomy (all pre-runtime in the current paradigm):

- **Vendor system prompt** — set by the harness vendor; users can't modify it; defines what the harness can/can't do.
- **`AGENTS.md` / `CLAUDE.md`** — "loaded into every context window at the start of a session." *(See [[claims-scorecard]] CL-B: true for CLAUDE.md in Claude Code; the AGENTS.md-native-read nuance is a known corpus caveat.)*
- **Tool calling.**
- **Agents** — specialized entities "harnessed" with unique capabilities, manifest as **skills**, role typology, and rules → targeted outputs (code, docs, issues, handoffs).
- **Loops** — "loop engineering has become a thing" → an eventual outcome (feature / problem solved) reviewed by a human.

This definition is **the same one the corpus uses** for [[external|harness-engineering/terminology]] (Lopopolo) and [[external|harness-engineering/tejas-kumar-anchor]] (the model/tools/context/guardrails/loop/verify decomposition). The disagreement is not *what a harness is* — it's *when and by whom it is decided*.

## Paradigm A — Fixed / Factory harness ("harness engineering")

| Property | Description (from the talk) |
|---|---|
| **When decided** | Entirely **before** runtime; "pre-engineered." Customization happens "ahead of the engineering runtime, not mid-engineering," and is human-directed. |
| **Metaphor** | Factory assembly line; **"Taylorism for AI"** — each station engineered in advance, each agent one job, a sequence, defined handoffs. |
| **Payoffs** | **Reliable** (same input → similar outputs), **auditable** (inspect what changed and when), **linear causality** (trace a break to its source). |
| **Metaphysics** | Reductionist — the world is stable parts wired together; relationships are secondary (see [[complexity-science-foundations]]). |
| **Best for** | **Complicated** problems: well-defined product/problem, known features, closed deterministic systems. "For most engineering problems, this is the perfect method." |
| **The catch** | Reliability is bought by **suppressing the variance that novelty requires**. Determinism and emergence pull in opposite directions. Every unanticipated situation needs a **human to patch the harness**; the more real-world it gets, the more rules you bolt on, until "the harness becomes more complicated than the problem." |

Examples the talk names as fixed harnesses: **Claude Code, Codex, Cursor, Pi, LangChain, Hermes, Cline, Goose** (all verified real — [[claims-scorecard]] CL5).

## Paradigm B — Adaptive engineering

> *"The discipline of designing constraints to the extent that the harness emerges on its own, stabilizes, and adapts as needed in response to the changing environment in ways that you could not specify in advance. **The harness becomes the ongoing output rather than the input.**"* — [21:36]

| Property | Description (from the talk) |
|---|---|
| **When decided** | The harness **emerges, stabilizes, changes, and dissolves at runtime** ("mid-engineering"). |
| **Metaphor** | A **flock of birds** (boids) — agents follow local rules; the harness = the flock. "The agents create the harness the same way the birds relate so the flock can emerge." |
| **Engineer's role** | **Not abolished — relocated.** You design the **constraints** ("rules of play"), not what should happen; then you **sense and respond** to the emergent structure rather than stopping and restarting. |
| **Metaphysics** | Relational/systems — the world is processes and relationships; a "stable thing" is a slow pattern in a flow (see [[complexity-science-foundations]]). |
| **Best for** | **Complex** problems: multi-agent, multi-human, multi-institutional, physical; messy and constantly changing. |
| **The risks** | Drift (attractors without selection pressure), monoculture, legibility collapse, no pre-runtime predictability (see [[failure-modes]]). |

## The continuum (explicit)

Chandegra is careful: *"This is not binary… it's very much a continuum. There's no purely fixed harness and no purely completely adaptive autonomous way… and one is not better than the other. They just have two different use cases."* [27:22]

- **Fixed pole:** prescribe the structure; agents run it; you rarely change it mid-run.
- **Adaptive pole:** agents freely interact and *create* the structure that guides them, changing it mid-run.
- It is **not** "a swarm of agents loose with no roles and intelligence magically appears."

**Two axes hide inside the continuum** (the talk introduces them separately — see [[adaptive-engineering-mechanics]]):
1. **Fixed ↔ adaptive** (when the structure is set).
2. **Vertical ↔ horizontal** intelligence (smarter individuals vs better group coordination). Hermes is adaptive-but-vertical; the talk's bet is on **horizontal**.
3. And a **design-time vs runtime** distinction: Pi is "adaptive at the design stage" (customizable up front) but not "adaptive at runtime."

## Key takeaways

- The two paradigms share a definition of "harness" and differ only on **when the structure is decided and who/what decides it.**
- Fixed harness = reliable *because* it suppresses variance; that same suppression caps novelty. This trade-off is the whole argument.
- "Right answer to a fixed problem, wrong answer to a moving problem" is the compressed thesis.
- The continuum framing is genuine — the talk repeatedly refuses to say adaptive is "better," only "different use case." That honesty is worth preserving when this topic is cited against [[vs-harness-engineering-corpus]].
