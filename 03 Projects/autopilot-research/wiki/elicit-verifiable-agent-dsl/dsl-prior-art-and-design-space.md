# DSL prior art + the design space

## Source

- Prior-art characterizations fetched against primary docs (priorart-accuracy verdict = PARTIAL: most CONFIRMED, a few of my draft claims corrected — captured below) — [[source-provenance]].

ÆPL is novel in *application* (an LLM-written planning DSL for research agents) but every design ingredient has strong prior art. Verified characterizations, so this wiki doesn't overclaim:

## Turing-incomplete / terminating languages

| Language | Verified characterization | Correction vs. my first draft |
|---|---|---|
| **Starlark** (Bazel) | Syntax "inspired by Python 3"; `for`/loops **not allowed at top-level**; **recursion not allowed** | Termination is *inferred from constraints*, not an explicit doc guarantee; it's Python-3-inspired (not "Python 2 and 3") |
| **Dhall** | "**Dhall is not Turing-complete**"; "**evaluation always terminates, no exceptions**" | Docs say non-Turing-complete + always-terminates; the word "total" is my gloss, not their term |
| **CEL** (Google Common Expression Language) | "**not Turing-complete**", "does not allow mutations", "evaluates in **linear time**"; built for safe embedded evaluation | CONFIRMED, stronger than claimed |
| **RestrictedPython** | Python subset for sandboxed execution (not independently re-fetched this pass — cite cautiously) | — |

ÆPL's "no loops / no recursion / no mutation / terminating" places it squarely in this family — but with **LLM-authored** programs and **domain research primitives**, which none of the above target.

## Content-addressed stores (the memoization backbone)

| System | Verified characterization |
|---|---|
| **Unison** | "references code by hash instead of by name"; "dependencies are deployed on the fly" |
| **Nix** | Store paths from cryptographic hashes of *all inputs*; distinct variants get distinct paths |
| **git** | Literally a "content-addressable filesystem"; SHA-1-addressed blobs/trees/commits |

ÆPL's content-addressed store (hash an expression → cached value) is the same idea applied at **expression granularity** inside an interpreter — enabling whole-program reinterpretation to stay cheap ([[whole-program-reinterpretation]]).

## Event sourcing (the state backbone)

- **Martin Fowler**: "capturing all changes to application state as a sequence of events"; the event log is "a purely additive structure." Elicit's append-only event log + Python-service-as-message-broker is a textbook instance ([[architecture-curator-interpreter]]).

## The "base your DSL on a training-data-rich language" thesis

Brady's agent-ergonomics point has independent 2026 articulations (fetched):

- **Microsoft All-Things-Azure devblog** — "AI Coding Agents and Domain-Specific Languages: Challenges and Practical Mitigation Strategies."
- **firetiger.com** — "What are domain-specific languages (DSLs) for AI agents?"
- **Takafumi Endo (Medium)** — "Domain-Specific Languages: The Deterministic Backbone of AI Agents."
- Academic: AutoDSL (arXiv:2406.12324), VeriSafe Agent (logic-based action verification, arXiv:2503.18492), AgentSLA (arXiv:2511.02885).

Consensus of that literature: DSLs give agents **determinism, verifiability, and a bounded action space** — but a *bespoke-syntax* DSL fights the model's training prior. Brady's mitigation (an opinionated **subset of Python**) is the field's recommended answer: keep the host grammar the model already knows, constrain semantics.

## Where ÆPL is genuinely distinctive

1. The DSL is **written by the model** (curator), not by humans — so agent-ergonomics is a first-order design axis.
2. **Domain primitives are research actions** (paper retrieval, clinical-trial lookup, screening) as language built-ins.
3. **Whole-program reinterpretation + expression-hash memoization** as the correctness/perf strategy — the specific combination is the novel engineering.
4. Two **legibility surfaces** derived from the same artifact (executable code + graph) for dual human/agent audiences.

## Key Takeaways

- ÆPL = (terminating-DSL family) × (content-addressed memoization) × (event sourcing) × (LLM-authored + research primitives). The parts are proven; the *product synthesis* is the contribution.
- "Subset of a popular language" beats "new syntax" for agent-authored DSLs — vendor and academic sources agree.
- Verified prior-art wording matters: don't say "guarantees termination" for Starlark (inferred) or "total" for Dhall (their word is "non-Turing-complete") — precision per Rule 12.
- If you want ÆPL-like guarantees cheaply, you can often compose existing pieces (CEL/Starlark for the plan language, git/Nix-style hashing for cache, an event log for state) rather than build from scratch.
