# ÆPL — language design

## Source

- EN transcript lines 159–254 (`raw/2026-07-04-elicit-verifiable-agent-dsl.md`); all properties verbatim-verified against both EN and VN transcripts ([[source-provenance]]).

## Name

- **ÆPL**, pronounced "Ash PL": *"The kind of weird smushed together AE thing is apparently called Ash. It's like an old English diphthong or something."* (Æ/æ is indeed the Old English "ash" letter — linguistically accurate.)
- Spelling caveat: the name is **spoken-only**; no written first-party rendering exists anywhere we could find. "AshPL" (VN dub description) and "ÆPL" are both reconstructions — see [[caveats-and-corrections]].

## Properties (all on-camera, all verified)

| Property | Quote/basis |
|---|---|
| **Turing-incomplete** | "firstly it is Turing incomplete. It's relatively simple" |
| **No loops** | "There's no loops" |
| **No recursion** | "there's no recursion" |
| **No mutation** | "There's no mutation" |
| **Purely functional** | "It's purely functional" |
| **Reactive** | "It's a reactive language" |
| **Typed** | "we're keen on types. It's typed. That lets us do fast redrafts if you've got a type error" |
| **Opinionated subset of Python** | "not just a generic simplification of Python... Not like Python with a couple of bits taken off at random" |
| **Domain primitives added** | "we add some extra primitives in which are specific to our domain... retrieving academic research papers or clinical trials... built into the language" |

- Domain = "scientific research and empirical decision-making, high-stakes decision-making."
- ÆPL code "looks a lot like Python because it is a subset of Python" — the example shown on stage was Elicit doing **a competitive analysis of Elicit itself** (searches for academic search engines / AI assistants / systematic-review tools → join → enrich).

## Why weak-by-design works for agents

1. **Checkability**: no loops/recursion/mutation ⇒ the interpreter can type-check and statically validate a plan cheaply; a type error is kicked back to the curator as a *cheap, fast* redraft signal ("Hey, you've got a typo. Have a look at line 52 and redraft it").
2. **Memoization**: purity ⇒ any expression can be **hashed** and its value cached in a content-addressed store — the enabling trick for [[whole-program-reinterpretation]].
3. **Termination**: no unbounded constructs ⇒ plans can't run away (same family of guarantees Starlark/Dhall/CEL sell — [[dsl-prior-art-and-design-space]]).
4. **Agent ergonomics** — the key transferable insight: *"you'll have a better time if you base your DSL on an existing language that has a lot of examples in the training data... the model doesn't need to learn the syntax. It just needs to know there's a subset that it can go for."*
5. **Effort asymmetry**: *"a surprisingly small amount of work went into the DSL compared to everything else. Everything else is kind of like conventional software engineering."* The language is the cheap part; the system is the expensive part ([[eight-item-build-checklist]]).

## What ÆPL is NOT

- Not a general-purpose language, not open-source (no repo, no docs, no license found — sampled surfaces, 2026-07-04).
- Not a prompt format: it is parsed, type-checked, AST-walked, and executed by plain Python ([[architecture-curator-interpreter]]).
- Not primarily for human reading: "looking at the ÆPL is not particularly fun... most people don't do this" — its *existence* as an executable contract is the point; humans get a derived graphical view instead ([[demo-research-landscape]]).

## Key Takeaways

- Subtraction is the design move: remove loops/recursion/mutation, add domain primitives — an **opinionated** subset, not a truncated one.
- Base the DSL on a training-data-rich host language so frontier models already "speak" it — syntax familiarity is free capability.
- Types are there for the *agent's* redraft loop at least as much as for correctness.
- Purity is load-bearing: it's what makes whole-program reinterpretation affordable.
- Budget expectation: DSL ≪ system. If you can't afford the system checklist, don't start the language.
