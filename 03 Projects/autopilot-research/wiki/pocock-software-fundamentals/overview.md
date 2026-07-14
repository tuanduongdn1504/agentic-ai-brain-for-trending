# Overview — "Software Fundamentals Matter More Than Ever"

## Source

- Video: [v4F1gFy-hqg](https://www.youtube.com/watch?v=v4F1gFy-hqg) — **AI Engineer conference channel**, uploaded 2026-04-23, 18:26, ~967K views / 33.1K likes (fetched 2026-07-14; **15–290× the channel's typical talk** — its breakout video).
- Event (verified): **AI Engineer Europe 2026** — London, Queen Elizabeth II Centre, April 8–10 — NOT the World's Fair the description promos (see [[caveats-and-corrections]]). Same-day recap: [tldrecap.tech](https://tldrecap.tech/posts/2026/aie-europe/software-fundamentals-ai/).
- Raw transcript: `raw/2026-07-14-pocock-software-fundamentals.md` (3,340 words, auto-subs deduped, read in full).
- Speaker: **Matt Pocock** (aihero.dev; ex-Total TypeScript) — **third Pocock topic in this wiki**, after [[../pocock-agentic-workflow/_index|pocock-agentic-workflow]] (podcast theory, June) and [[../pocock-real-feature-build/_index|pocock-real-feature-build]] (first-party worked example, March).

## What this talk is

- An 18-minute **conference keynote-style argument**: the compact, public, stage version of the philosophy the other two Pocock topics document at podcast length and worked-example depth.
- **Thesis:** "Code is cheap" is wrong — **bad code is the most expensive it's ever been**, because a hard-to-change codebase can't absorb AI's bounty. Good codebases amplify AI; therefore *software fundamentals matter more than ever*.
- **Anti-thesis target:** the **specs-to-code movement** ("change the spec, re-run the 'compiler', never look at the code") — which Matt reports trying and abandoning after successive runs produced *monotonically worse* code. He calls specs-to-code "vibe coding by another name."
- **Structure:** a sequence of AI **failure modes**, each fixed by a decades-old book + a skill he wrote:
  1. *AI didn't build what I wanted* → Brooks' **design concept** → **grill-me** skill ([[design-concept-and-grill-me]])
  2. *AI is too verbose / cross-purposes* → DDD **ubiquitous language** → ubiquitous-language skill ([[shared-language-with-ai]])
  3. *Right thing, doesn't work* → PragProg **"outrunning your headlights"** → **TDD** skill ([[deep-modules-and-tdd]])
  4. *(testability)* → Ousterhout **deep modules** → **improve-codebase-architecture** skill
  5. *Shipping faster than your brain* → **"design the interface, delegate the implementation"** (gray-box modules)
- Closing frame: AI = **tactical** "sergeant on the ground"; you = **strategic** layer above — the same Ousterhout-derived framing documented in [[../pocock-agentic-workflow/strategic-vs-tactical]], here in its earlier, compressed stage form.
- All skills live in **[mattpocock/skills](https://github.com/mattpocock/skills)** (MIT; 169,558★ on 2026-07-14; ground-checked — see [[claims-scorecard]]).

## Why it matters to this corpus

- It is the **earliest-dated** (2026-04-23 upload) full statement of the Pocock position the corpus already holds from June/March sources — useful for lineage: *deep modules* and *design concept* were on stage **before** the June podcast's "harness > model" articulation.
- It is the corpus' sharpest **first-person anti-specs-to-code testimony** — direct counter-thread to the SDD line ([[../jsm-six-file-context/_index]], cc-sdd, Storm Bear Pattern #21) and companion evidence to his documented "specs-to-code is never going to work" stance in [[../pocock-real-feature-build/caveats-and-corrections]].
- Brooks' "design concept" ("not an asset… the invisible theory of what you're building") is a near-exact restatement of **Naur's theory-building** — see [[video-to-corpus-crosswalk]] and [[../system-thinking-ai-coding/naur-programming-as-theory-building]].

## Key Takeaways

- Bad code now has a *higher* price tag than pre-AI, because it caps what agents can do for you — the inverse of "code is cheap."
- Every AI failure mode in the talk is fixed by a pre-AI idea: Brooks (1975/2010), Evans (2003), Hunt/Thomas (1999), Ousterhout (2018), Beck (1999/2004).
- The practical unit of adoption is a **skill per fundamental** — all four demoed skills verified present in mattpocock/skills ([[claims-scorecard]]).
- Deep modules are framed as **AI-navigability** infrastructure, not just human ergonomics — shallow-module sprawl is "really hard for the AI to explore."
- The talk's stage numbering is loose (jumps to "failure mode six" / "tip five") — see [[caveats-and-corrections]] before quoting its structure.
