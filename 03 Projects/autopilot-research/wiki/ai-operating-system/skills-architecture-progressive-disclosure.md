# Skills architecture — progressive disclosure + build-via-failure + chaining

The highest-leverage token-cost optimization in the corpus, plus the corpus's most-cited skill-authoring tactic.

## Source

- Raw: [`raw/2026-05-29-ai-operating-system-5-skills-framework.md`](../../raw/2026-05-29-ai-operating-system-5-skills-framework.md), §Trends-2

## Skills = SOPs for AI (Remy Gaskell)

Remy Gaskell's framing: skills are **"SOPs for AI"** — Standard Operating Procedures that let you explain a process **once and never again**. This is the corpus's load-bearing definition: a skill captures a worked process so it can be replayed.

This is the same workflow as [[../claude-cowork/skills-to-plugins-pipeline]] but pitched at the *system-design* level rather than the *operator* level.

## Progressive disclosure (Simon Scrapes + Ross Mike)

The single highest-leverage cost optimization in the corpus:

- The agent's primary context only sees the skill's **name and description**
- The **full instruction set** is only loaded if the agent determines the skill is necessary
- Drastically reduces token usage on every turn

Mechanically: instead of pre-loading every SOP into context, the agent sees an *index* of skills and pulls the full text just-in-time. Same idea as **lazy evaluation** in programming languages, applied to agent context.

This composes naturally with **vault Skills standard** ([[external|Storm Bear: agent-skills-standard (v76)]]) — the skill registry format the vault adopts is structurally aligned with progressive disclosure.

## Build-via-failure (Ross Mike's "recursive skill building")

Ross Mike advocates for **never hand-writing skills from scratch**. The recipe:

1. Walk the agent through a workflow **manually**
2. Let it **fail**
3. **Correct** it
4. Once a successful run completes, ask the agent: **"review what you just did and create a skill for it"**

Result: skills that capture **actual successful runs** in the operator's unique workflow context, not abstract best-practices.

This is the same pattern as Bart Slodyczka's codify-after-success in [[../claude-cowork/skills-to-plugins-pipeline]], but Ross Mike adds:
- **Anti-distribution stance** — argues pre-made skills lack the operator's unique context (see [[off-the-shelf-vs-handbuilt-skills]])
- **Failure-as-data** — letting the agent fail is part of the process; corrections become skill IP

## Skill chaining (Simon Scrapes)

For multi-step pipelines:

- Build **modular components** (e.g., a transcription skill, a copywriting skill)
- **Chain them together** to form a full content pipeline
- Each skill is independently testable; the chain is the integration

This is the **Unix philosophy applied to AI skills** — small, sharp tools composing into larger workflows. Maps to vault's `bin/autopilot-drain.py` pattern of chaining yt-search + selection + NotebookLM-bundle + analysis steps.

## "Skillception" — the corpus's strongest pun

The general phenomenon of **skills calling skills** — a skill can invoke other skills it depends on, with each level managed via progressive disclosure. The agent navigates a tree of available capabilities, expanding nodes only when needed.

Worth noting: skillception requires careful **dependency graph** thinking. Cyclic dependencies between skills can produce subtle infinite loops; the corpus does not discuss this risk explicitly.

## Composition stack

```
                 [progressive disclosure]
                          │
                          ▼
┌──────────────────────────────────────────┐
│   Skill registry (name + description)    │  ← always loaded
└──────────────────┬───────────────────────┘
                   │ agent selects on-demand
                   ▼
┌──────────────────────────────────────────┐
│   Full SKILL.md content                  │  ← loaded just-in-time
│   - step-by-step process                 │
│   - tool / MCP / connector usage         │
│   - calls to other skills (skillception) │
└──────────────────┬───────────────────────┘
                   │
                   ▼
              [execution]
```

## When to author a new skill — Jack Roberts's handover test (from sister topic)

From [[../claude-cowork/skills-to-plugins-pipeline]]: codify a workflow into a reusable skill only if it passes the **handover test** — *could a stranger run this process from the file alone, without asking questions?* If yes → ready for skill. If no → keep ad hoc.

This criterion isn't in the AIOS corpus explicitly but composes cleanly with Ross Mike's "build-via-successful-run" — first prove the run, then test handover-readiness, then codify.

## Anti-pattern: pre-built skill marketplace dependence

Ross Mike explicitly warns against this:

> "I don't install skills... I don't download skills"

He even admits to **posting his own skill on GitHub just to get "stars"** while telling his audience: **"Do not download it... do not use it."**

The reasoning: pre-made skills lack the **specific context of a successful run** in your unique workflow. They're optimized for distribution, not for your operations.

See [[off-the-shelf-vs-handbuilt-skills]] for the full debate.

## Key Takeaways

- **Progressive disclosure** is the most-leverage token optimization in the corpus — every skill registry should use it
- **Build-via-failure** (Ross Mike) produces skills with real operational context — superior to abstract-best-practice skills
- **Skill chaining** (Simon Scrapes) applies Unix-philosophy modularity to agent capabilities
- **Skillception** is a real pattern but requires dependency-graph thinking (cyclic-dependency risk unspoken in corpus)
- **The handover test** (from Cowork sibling) composes cleanly with build-via-failure as a codification criterion
- **Pre-built skill marketplaces are contentious** — see [[off-the-shelf-vs-handbuilt-skills]] for the strongest disagreement axis in the corpus

## Related

- [[overview]] — AIOS framing
- [[instruction-layer-markdown-files]] — token-pressure concerns motivate both
- [[off-the-shelf-vs-handbuilt-skills]] — the sharpest disagreement axis
- [[memory-and-context-rot]] — progressive disclosure is also a context-rot mitigation
- [[../claude-cowork/skills-to-plugins-pipeline]] — sister topic; same pattern at the product layer
- [[external|Storm Bear: agent-skills-standard (v76)]] — the vault's curated skill-format standard
