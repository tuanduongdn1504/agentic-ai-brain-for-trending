# elicit-verifiable-agent-dsl — topic index

> **What:** How **Elicit** (the AI research assistant, Ought spinout) makes agentic workflows **trustworthy and verifiable** with **ÆPL ("Ash PL")** — a custom Turing-incomplete, purely functional, typed subset of Python that a Claude-powered "curator" *writes* and a plain-Python service *interprets*. Told by **James Brady, Head of Engineering**, at **Code with Claude: Extended London (2026-05-20)**. The plan is not a description of the work — **the plan IS the executable**.
> **Created:** 2026-07-04 (operator-submitted BizMate VN dub → Claude-channel EN original; double deep-dive into Elicit/Ought originals; 30-agent dive+refute-first verify workflow `wf_7c12cab8-7c9`).
> **Why it matters here:** this is the strongest first-party counter-position to freeform agent loops in the corpus — verifiable-plan-as-code, process-over-outcome supervision productized — and it lands directly on this vault's loop/verify discipline and hireui's Goal-#2 first LLM feature.

## Articles

- [[overview]] — the talk, the "mechanism matters" thesis, 3 desiderata, headline findings
- [[aepl-language-design]] — ÆPL properties (Turing-incomplete / pure / typed / reactive / opinionated Python subset) + agent-ergonomics rationale
- [[architecture-curator-interpreter]] — curator / wrapper / gateway / Python service / sandbox / append-only event log / content-addressed store
- [[whole-program-reinterpretation]] — the signature mechanism: rewrite + reinterpret everything, memoize by hash; why snippets = drift
- [[pi-harness-and-curator-models]] — "Pi with the Anthropic models": Pi = Earendil/Mario Zechner's pi harness (ground-truthed); the Codex aside
- [[eight-item-build-checklist]] — Brady's 8-item "if you build a DSL-based system" checklist with his own priority ordering
- [[demo-research-landscape]] — the biology-foundation-models demo, ground-truthed against the real world (AlphaFold 3, ESM3, EvoDiff, AI@HHMI, AISI MOUs)
- [[ought-process-supervision-lineage]] — 2017 Ought → factored cognition → "Supervise Process, not Outcomes" (2022) → ICE → Factored Verification → Elicit spinout (2023-09-25) → this talk
- [[dsl-prior-art-and-design-space]] — Starlark / Dhall / CEL / Unison / Nix / git / event sourcing, verified characterizations + the "train-data-rich base language" thesis
- [[source-provenance]] — pipeline, source tiers, 19 verdicts, misfire log
- [[caveats-and-corrections]] — caption garbles, VN-dub artifacts, verifier misfires (incl. a stale-cutoff Codex misread), qualified claims

## Key takeaways (topic level)

1. **Mechanism matters** — two systems with identical output do not deserve equal trust; trust rides on the *process* that produced the output. This is Ought's 2022 "Supervise Process, not Outcomes" thesis productized ([[ought-process-supervision-lineage]]).
2. **Three desiderata drove the DSL**: process legible (to users AND other agents), iteration retains fidelity (no drift), process followed faithfully (the plan executes as checked).
3. **ÆPL is deliberately weak**: no loops, no recursion, no mutation, purely functional, typed — weakness IS the feature (checkability, memoization, termination).
4. **Whole-program reinterpretation** every iteration + content-addressed memoization = consistency without re-paying compute ([[whole-program-reinterpretation]]).
5. **The DSL was the small part** — "a surprisingly small amount of work went into the DSL compared to everything else"; the system around it (wrapper, interrupts, rehydration, credential isolation, event sourcing, evals) is where the engineering went ([[eight-item-build-checklist]]).
6. **Curator = Claude via the pi harness** (Earendil Inc. / Mario Zechner) after trying an agent-SDK implementation and "Pi with Codex" ([[pi-harness-and-curator-models]]).
7. **This talk is the only public source naming ÆPL** — zero written footprint found on any sampled Elicit surface (homepage, blog, docs, GitHub) or anywhere else ([[caveats-and-corrections]] for the qualifier).

## Cross-links

- Same event (CWC Extended London 2026-05-20): [[../agentic-analytics-harness/_index]] (Chris Merrick, Omni), the Kevin Chen "Agents that remember" workshop ([[../agent-memory-architecture/anthropic-memory-stores-and-dreaming]] — venue hedge resolved by this pass), a London "How we Claude Code" workshop (Arnaud Doko) distinct from [[../how-we-claude-code/_index]].
- Harness choice: pi — the vault holds a Storm Bear curated wiki on pi-mono: [[external|Storm Bear: pi-mono]] (`_state/04-projects-v30-v39.md`).
- Verifiable-plan-vs-freeform-loop tension: [[../pocock-agentic-workflow/_index]] (queues-not-loops), [[../harness-engineering/_index]] (humans steer, agents execute), [[../multi-agent-orchestration/_index]].
- Eval culture: [[../prompt-evaluation/_index]] (this vault's `evals/` harness), Elicit's eval posts in [[ought-process-supervision-lineage]].
- VN dub chain: third BizMate/licensed-dub provenance chain after [[../google-zero-open-web/_index]] + [[../agent-memory-architecture/_index]].
