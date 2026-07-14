# Crosswalk — where this talk sits among the three Pocock topics (and beyond)

## Source

- Comparison of `raw/2026-07-14-pocock-software-fundamentals.md` against [[../pocock-agentic-workflow/_index]], [[../pocock-real-feature-build/_index]], [[../system-thinking-ai-coding/_index]].

## The three Pocock topics, by date and register

| | This talk | [[../pocock-real-feature-build/_index|real-feature-build]] | [[../pocock-agentic-workflow/_index|agentic-workflow]] |
|---|---|---|---|
| Date | 2026-04-08/10 (AIE Europe, London) | 2026-03-18 | 2026-06-18 |
| Register | 18-min conference argument | 44-min first-party worked example | 62-min third-party podcast |
| Contributes | the **why** (failure modes → fundamentals) | the **how** (every step on a real repo) | the **worldview** (harness>model, AFK queues) |

- Chronology of the *ideas*: the worked example (March) already **uses** grill-me + glossary + PRD-with-modules; this talk (April) is the earliest recorded **argument for why** they work; the podcast (June) generalizes to harness-over-model. Nothing in this talk contradicts the other two — it's the missing middle layer.
- ⚠️ Not to be confused with the **~96-min AI-Engineer-2026 workshop** that [[../pocock-agentic-workflow/_index]] deliberately excluded (Smart-Zone/Brooks/tracer-bullets/4-role content). This 18-min talk independently confirms **Brooks was part of Matt's 2026 conference material** — the design-concept/design-tree thread the exclusion note hinted at.

## Overlaps with named sources (cite the deep version)

- **Ousterhout strategic/tactical + sergeant-general** → deep version: [[../pocock-agentic-workflow/strategic-vs-tactical]] (incl. the attribution caveat: the AI extension is Matt's, not Ousterhout's).
- **Ubiquitous language / glossary** → deep version: [[../pocock-real-feature-build/ubiquitous-language-for-llms]]; this talk adds the verbosity/thinking-trace framing ([[shared-language-with-ai]]).
- **Grill-me → PRD → issues → AFK agent** → deep version: [[../pocock-real-feature-build/grill-me-in-practice]] + [[../pocock-real-feature-build/prd-and-issues-pipeline]]; this talk adds the Brooks design-concept theory ([[design-concept-and-grill-me]]).
- **Deep modules + improve-codebase-architecture skill** → **NEW here** — no prior corpus article covers deep modules as a first-class topic ([[deep-modules-and-tdd]]).
- **TDD-as-agent-pacing** → **NEW here** as an explicit argument.

## The Brooks ↔ Naur bridge (strongest cross-corpus link)

- Matt's Brooks rendering — the design concept is "**not an asset**… the **invisible theory** of what you're building" — is functionally identical to **Naur's 'theory'** in [[../system-thinking-ai-coding/naur-programming-as-theory-building]]: the knowledge that lives in the builders and **cannot be fully written down**.
- Both talks draw the same practical conclusion from it: artifacts (specs, plans) cannot substitute for shared understanding; processes that rebuild the theory in the human (grilling / design-before-prompt / reverse review) can.
- Two first-party educators (UK, VN), two months apart, two different 20th-century sources — same conclusion. This is independent convergence, not lineage: worth a Storm Bear observation-track note at the next audit.

## The SDD counter-thread

- This talk is the corpus' fullest **anti-specs-to-code** argument ([[anti-specs-to-code-thesis]]) — the named opposing pole to [[../jsm-six-file-context/_index]] (spec-driven, mass-market) and the cc-sdd/OpenSpec/spec-kit line (Storm Bear Pattern #21).
- The synthesis both poles agree on: **front-load design, keep humans on interfaces/boundaries** — they disagree on whether code is a designed artifact or build output.

## Key Takeaways

- Read the three Pocock topics as **why / how / worldview**; this one is the why.
- The genuinely new corpus content here: **deep modules for AI-navigability**, **TDD as pacing**, and the **Brooks design-concept theory** under grill-me.
- Brooks↔Naur is the headline synthesis link: two independent 2026 talks grounding AI-era practice in "theory lives in people, not artifacts."
- When citing Pocock in the SDD debate, cite this talk for the argument and [[../pocock-real-feature-build/_index]] for the evidence his own workflow still writes PRDs.
