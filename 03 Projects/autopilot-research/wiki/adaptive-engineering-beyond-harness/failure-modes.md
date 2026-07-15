# Failure Modes & Objections

Two layers here: (1) the failure modes **the speaker names himself** — a point in his favor; and (2) the **harder objections** from the independent thesis-critique agent (`thesis-critique`, [[source-provenance]]). Keep both when citing this topic.

## Layer 1 — The speaker's own failure modes ([32:59–34:56])

Chandegra is explicit that adaptive engineering "has a huge number of failure modes," and lists four:

1. **Premature attractors without selection pressure → drift.** Emergence "leans toward stability" (an attractor) — but a structure that *feels* stable and optimal isn't necessarily the best. Without a **genuine selection pressure** (the environmental pressure that "is evolution"), the system just **drifts**. *"We as a community need to find that in adaptive engineering, otherwise you just get drift."*
2. **Monoculture.** "You don't get genuine diversity among agents because they're all trained on the same data." Since **diversity is the fuel** of a complex system ([[complexity-science-foundations#5]]), shared training data collapses the very mechanism the paradigm depends on. *(This is a strong, self-aware objection — the boids analogy assumes heterogeneous agents, but LLM agents are near-clones.)*
3. **Legibility collapse.** "As adaptability increases, you can't really pin down or explain things… and that's a feature of complex systems." You lose the auditability that the fixed harness bought you.
4. **No pre-runtime predictability.** "Things are constantly moving." You cannot know ahead of time what the system will do.

His framing: *"These are the real failure modes we must apprehend, because adaptive engineering is something we're going to be more inclined toward — it's going to race forward in the future."*

## Layer 2 — The critic's harder objections

The independent critique agent steelmanned the thesis first (see [[caveats-and-corrections#thesis-critique]]), then raised four objections the talk does **not** answer:

1. **Falsifiability & actionability gap.** The thesis is a high-altitude *direction*, not engineering guidance. What are the primitives? How do you implement "rules of play" for a real system on Monday? Boid analogies are clean because simulations have deterministic physics — **LLM orchestration does not.** It reads as a research direction, not a shippable practice.
2. **Rebrand of known literature without attribution.** Multi-agent systems, swarm intelligence, decentralized/polycentric governance (Ostrom), constraint-based design — these are 20–40 years deep. The talk neither cites this prior art nor explains why the application to LLM coordination is *mechanically* different. Valuable repositioning, but **not novel**. (Compounds the [[complexity-science-foundations|Cynefin/boids attribution gaps]].)
3. **Legibility collapse is operationally reckless in real domains.** In compliance, **medical, recruiting, finance**, unpredictable agent behavior is not acceptable. "The agents self-organized" is not a legal defense for a harmful outcome. The thesis assumes operators accept opacity; regulated systems do not. **(Sharp irony: the speaker is himself a physician — the domain where legibility collapse is least tolerable.)**
4. **No working-implementation proof.** It contrasts documented, working *fixed* harnesses (cc-sdd, the vault's Loop Routine v2.1, adversarial-review architectures) against *emergent* orchestration whose only existence-proof is a boid simulation. "Let the harness emerge" is, absent evidence, **indistinguishable from "let it fail until it works."** Where is the demonstration that emergent LLM orchestration beats a fixed harness on a **non-toy production problem**?

## Where the two layers meet

The speaker's **monoculture** worry and the critic's **no-implementation** objection are the same crack seen from two sides: the boids model needs *diverse* agents reacting to *deterministic* local physics; LLM agents are *near-identical* and their "local physics" (what another agent's output makes a third agent do) is *stochastic and unbounded*. Until someone shows emergence surviving those two facts on a real problem, adaptive engineering is a **hypothesis about a mechanism**, not a mechanism.

## The honest scorecard on the argument

- **Descriptively strong:** over-specification really is brittle; local adaptation really does have value; the complicated/complex mis-categorization really is a common and expensive mistake.
- **Prescriptively unproven:** there is no bridge from *"complex systems have this property"* to *"here's how to engineer it into an AI system, and here's proof it wins."*
- **Verdict (critic):** *a direction to watch, not a practice to adopt* — see [[vs-harness-engineering-corpus]] for how this lands against the vault's evidence.

## Key takeaways

- Give the speaker credit: he names **drift, monoculture, legibility collapse, and unpredictability** himself.
- The **monoculture** objection is the most technically damaging and is the speaker's own — LLM agents are not diverse the way birds are.
- The **legibility** objection bites hardest in exactly the operator's domains (recruiting/hireui, and the speaker's own medicine).
- The missing piece is a **working implementation on a real problem**; without it the thesis stays a research question.
