# Whole-program reinterpretation + content-addressed memoization

## Source

- EN transcript lines 384–415 and 656–712 (`raw/2026-07-04-elicit-verifiable-agent-dsl.md`); 8 sub-claims verified ([[source-provenance]]).

## The mechanism

- Every iteration, the curator **rewrites the whole ÆPL program** and the interpreter **reinterprets the whole thing from scratch**: "We don't just interpret the actual code that's been re-written. We re-draft the program and then reinterpret the whole kitten caboodle from top to bottom."
- That would be ruinously slow — except ÆPL is **pure**, so every expression can be **hashed**: "we can hash an expression and say, if this has been evaluated before, we just store that away in a map... 'oh yeah, this boiled down to 42' — we can just use that straight away from the hash."
- The cache is the **content-addressed store** — "this is super duper crucial. Nothing would work here if we weren't really careful about this."

## Why whole-program (the anti-drift argument)

> "It's easy to be confident about and make statistical guarantees of cohesion and correctness when you're literally interpreting the whole program every single time. If you're just interpreting little snippets, **that's where the drift can come in**."

- This is desideratum 2 (iteration retains fidelity) implemented as a runtime property rather than a prompt-engineering hope. The user's original intent stays literally present at the top of the program, executed (from cache) on every iteration.
- Demo evidence: the first artifact's program was ~100–150 lines; by the end of the session (open/closed-source comparison + GTM layer + oversight-bodies layer + a natural-language "join") it was **~1,000+ lines** — and "the top of the program is identical to what we had before... the vast majority of it is just memoized and you get it back straight away."

## Design reading

- **Correctness strategy**: recompute everything, logically. **Performance strategy**: pay only for what changed, physically. Purity + hashing dissolves the usual trade-off — the same trick as Nix/git/Unison content-addressing and build-system incrementalism ([[dsl-prior-art-and-design-space]]).
- Contrast with the corpus's freeform-loop patterns ([[../pocock-agentic-workflow/_index]] queues, Ralph loops in [[../harness-engineering/_index]]): those iterate by *appending conversation*, which is precisely "interpreting little snippets" — context drift is the known failure mode this design deletes.
- The vault analogy: this wiki's own routine re-reads `_master-index.md` + full topic indexes each cycle rather than diffing — same instinct, no memoization layer. (Pilot angle B in the methods file.)

## Key Takeaways

- Rewrite-everything + reinterpret-everything is the **strong version of "keep the plan in context"** — the plan isn't in context, it *is* the execution.
- Purity is the enabling constraint: memoization by expression hash only works when evaluation has no side effects.
- Drift is framed as an *interpreter-granularity* problem, not a model problem — a structural fix, not a prompting fix.
- Growth pattern to expect: programs accrete layers monotonically; old layers become free (cached) history.
- Transferable without a DSL: keep a canonical, complete, re-executed artifact of intent; never iterate on fragments.
