# The 8-item build checklist (if the desiderata point you at a DSL)

## Source

- EN transcript lines 741–824; every item + priority statement verbatim-verified ([[source-provenance]]).

Brady's caveat first: "It's not the easiest thing to build... reach for it if the desiderata for your product and your organization point you in that direction."

## The checklist, with his own priority grading

| # | Item | What it is | Brady's grading |
|---|---|---|---|
| 1 | **The DSL itself** | Agent-ergonomic: base it on a training-data-rich existing language; "a surprisingly small amount of work went into the DSL compared to everything else" | "You have to do one. That's obvious." |
| 2 | **Wrapper** | Harness/model abstraction in front of the curator — swap harnesses and models freely ([[pi-harness-and-curator-models]]) | "Would recommend number two." |
| 3 | **Interrupt handling** | Mid-run user input "gracefully flows back into the curator so it can redraft its plan **without stopping the world**. That isn't something that any harness handles natively, so that's something we had to build." | "Most people would probably need to do three, four, five, and six." |
| 4 | **Session rehydration** | "Come back to sessions in the future and rehydrate them... we had to build a whole thing for that. Not really a native feature." | (same — needed) |
| 5 | **Credential isolation** | The gateway: all LLM traffic through one API-key-holding choke point; anti-exfiltration ([[architecture-curator-interpreter]]) | (same — needed) |
| 6 | **Model-message handling** | "A weirdly annoying amount of stuff to handle messages coming out of the models and make sure they're not just lost to standard out" | (same — needed) |
| 7 | **Event sourcing** | Append-only event log as the state backbone — "We're really happy with that pattern. That's not a small lift." | "Number seven, you have to do something there" (some state story is mandatory; event sourcing is their choice) |
| 8 | **A dedicated eval team** | "It's **so hard to do eval when the system is writing programs and executing them on the fly**... we've invested a lot of time there, and I'd really strongly recommend that you do the same." | Strongly recommended |

## Readings

- **The language is ~10% of the project.** Items 2–8 are "conventional software engineering" — the checklist is really a warning label: a DSL is a *system* commitment, not a parser weekend.
- Items 3, 4, 6 are **harness gaps**: things "no harness handles natively" in 2026 — a concrete build-vs-buy map for anyone embedding a harness ([[../harness-engineering/_index]]; the corpus's harness-primitive lists get three confirmed missing primitives here).
- Item 8 connects to Elicit's real eval practice — 17-PhD Reports eval, systematic-review screening recall 93.6% etc. ([[ought-process-supervision-lineage]]) — the eval team predates and outlives any one architecture.
- Eval difficulty claim is specific: evaling a system that *generates and executes programs on the fly* is a moving-target problem — the same reason this vault's [[../prompt-evaluation/_index]] harness evals *anchors/gates* rather than full outputs.

## Key Takeaways

- Budget by the checklist: 1 language + 6 systems items + 1 org item (evals).
- The universally-needed core per Brady = interrupts, rehydration, credential isolation, message plumbing (3–6).
- Event sourcing is *a* answer to item 7, not *the* answer — but "you have to do something there."
- If you can't fund a dedicated eval effort, the DSL's trust story is incomplete — verifiability of plans ≠ quality of outcomes.
- Use the checklist as a due-diligence lens on any "we built an agent DSL" claim.
