# Overview — "Making agentic workflows trustworthy and verifiable with a custom DSL"

## Source

- **EN original:** https://www.youtube.com/watch?v=qOjleN2-50c — official **Claude** channel, uploaded 2026-05-22, 29:39. Session: **Code with Claude: Extended London**, 2026-05-20, Builder stage, **14:05–14:35 BST** (official event page; a search snippet's "14:50–15:20" was REFUTED against it).
- **Speaker:** James Brady, **Head of Engineering, Elicit** (GitHub `goodgravy`, X `@james_elicit`; joined Ought as Head of Engineering January 2022, pre-spinout).
- **VN dub (operator-submitted):** https://www.youtube.com/watch?v=UjskE6hGx6c — BizMate AI Official, 2026-06-23, 470 views / 10 likes at fetch (2026-07-04).
- Raw transcripts: `raw/2026-07-04-elicit-verifiable-agent-dsl.md` (both read in full in the main loop).
- Official video description (yt-dlp ground truth): *"System design of agentic research assistant built unconventionally: one component outputs plan in custom Turing-incomplete programming language, another interprets it, quiver of models executes concrete tasks. Architectural choices as concrete instantiations of company values."*

## The thesis: mechanism matters

Opening question: **two systems produce identical output — do you trust them equally?** No: trust depends on *what went on inside*. His example: a static-analysis tool says "no security vulnerabilities, safe to ship." If that verdict came from an older model (3.5 Sonnet) vs. a state-of-the-art model that did tool use, critique, and redrafting — "the message might be literally identical, but you would react very differently."

- There is **no single correct mechanism** — it's a design choice conditioned on domain, user, task.
- There is a real **speed-vs-rigor trade-off**; Elicit deliberately sits at the rigor end ("that's not really where we differentiate ourselves" on speed).
- **Provider brand and taste matter**: Elicit's brand = "super high reliability, really high quality, data provenance."
- Closing symmetry: it's "not crazy to imagine Opus coming up with one of those tables" — the *table* isn't the moat; the **painstaking, exposed, verifiable process** is. "My pitch is not that you should go and use a DSL. My pitch is that you should care a lot about the mechanism."

## The three desiderata (what led to a DSL)

1. **The process must be legible** — to the user *and to other agents* ("spot-checkable by the human, spot-checkable by other agents... we can run critique agents over it").
2. **Iteration on the process retains fidelity** — adding layers/directions must not drift from what the user originally wanted (drift "definitely harms trust").
3. **The process is followed faithfully** — a checked plan must be what actually executes: "otherwise, what are we doing here?"

He is explicit this is *not* a universal prescription: "I'm not saying that everyone should be using a DSL, you shouldn't" — the desiderata pointed *Elicit* there.

## The answer: ÆPL, a plan you can execute

- The DSL is **ÆPL** ("Ash PL" — the Æ ligature, "an old English diphthong"). Full language treatment: [[aepl-language-design]].
- Signature line of the talk: *"the ÆPL is not just a representation of a plan. It is **literally the plan which is executable** — that's what lets us really be sure that we're following through on the plan as stated."*
- The system loop: a **curator** (Claude via the pi harness — [[pi-harness-and-curator-models]]) writes ÆPL → a plain-Python service parses/type-checks/interprets it → results flow back → curator **redrafts the whole program** → reinterpret. Architecture: [[architecture-curator-interpreter]]; the whole-program discipline: [[whole-program-reinterpretation]].

## Headline findings from the verification pass

- Every load-bearing on-camera claim **CONFIRMED** (19 verdicts: 17 CONFIRMED, 2 PARTIAL on meta-items) — see [[source-provenance]].
- **This talk is the only public source for ÆPL** — no Elicit blog/docs/GitHub mention (qualified in [[caveats-and-corrections]]).
- The Ought lineage is real and documented a decade deep: [[ought-process-supervision-lineage]].
- The demo's outputs are real-world-grounded (AlphaFold 3, AI@HHMI $500M, Anthropic×AISI MOUs): [[demo-research-landscape]].

## Key Takeaways

- Trust is a property of **process + exposure of process**, not of output quality alone.
- Make the plan executable, and "did the agent follow the plan?" stops being a monitoring problem and becomes a **language-runtime guarantee**.
- Legibility is dual-audience: humans spot-check; **critique agents** read the same plan.
- Elicit chose the rigor end of the speed/rigor spectrum *as brand strategy*, and built the architecture to match — "architectural choices as concrete instantiations of company values" (official description).
- The prescription is transferable even without a DSL: care about the mechanism; expose it.
