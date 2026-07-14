# The anti-specs-to-code thesis — "code is not cheap"

## Source

- Transcript `raw/2026-07-14-pocock-software-fundamentals.md` (opening ~4 minutes of [v4F1gFy-hqg](https://www.youtube.com/watch?v=v4F1gFy-hqg)).

## The argument, step by step

1. **The specs-to-code promise** (as Matt renders it): write a spec → AI turns it into code → on problems, edit the *spec* and "run the compiler again" — never look at the code.
2. **His empirical report:** he tried it; each re-run produced **worse** code than the last, converging on "garbage." (First-person testimony, audience hands went up on the same experience.)
3. **Diagnosis via old books:**
   - **Ousterhout:** bad code = *complex* code = "anything related to the structure of a software system that makes it hard to understand and modify." A codebase you can't change without bugs is a bad codebase.
   - **The Pragmatic Programmer:** **software entropy** — every change made without regard for whole-system design degrades the system. Specs-to-code re-runs are exactly such changes, at machine speed.
4. **The economic inversion:** specs-to-code assumes *code is cheap*. Matt: **bad code is the most expensive it's ever been**, because AI performs brilliantly in good codebases and drowns in bad ones — so the quality of your code now *multiplies or caps* your AI leverage.
5. **The kicker:** "The idea that we can just ignore the code and have the code manage itself is just sort of **vibe coding by another name**."
6. **Kent Beck close:** specs-to-code **divests** from system design; the alternative is to "**invest in the design of the system every day**" (see [[the-originals]] for attribution verification).

## Position in the corpus' SDD debate

- This is the **most complete first-person argument** for the anti-spec pole the corpus has: [[../pocock-real-feature-build/_index]] recorded the one-line stance ("specs-to-code is never going to work"); this talk supplies the *mechanism* (entropy + compounding complexity across regenerations).
- The opposing thread is well-represented: [[../jsm-six-file-context/_index]] (spec-driven at mass-market scale), cc-sdd / OpenSpec / spec-kit (Storm Bear Pattern #21 SDD Methodology Emergence).
- **Precision matters when citing him:** Matt's target is the *regenerate-from-spec-and-don't-read-the-code* loop. His own workflow still produces PRDs and issues from grilled conversations ([[../pocock-real-feature-build/prd-and-issues-pipeline]]) — he is anti-**code-as-disposable-artifact**, not anti-written-plans. Conflating the two misquotes him.
- Note the near-agreement hidden under the disagreement: SDD frameworks like cc-sdd also front-load design; the fight is over **whether the code remains a first-class designed artifact** (Pocock: yes, invest daily) or becomes build output (specs-to-code: no).

## Key Takeaways

- The thesis is an *economic* claim, not nostalgia: code quality is now the multiplier on AI leverage, so fundamentals appreciated in value.
- The failure mechanism he reports (monotonic degradation across spec→code regenerations) is software entropy operating at generation speed.
- Quote him precisely: anti "never look at the code," not anti planning/PRDs.
- The corpus now holds both poles with named mechanisms — cite this article and [[../jsm-six-file-context/_index]] together when the SDD debate comes up.
- Cross-links: [[the-originals]] (book verification) · [[../pocock-agentic-workflow/harness-over-model]] (the June articulation) · [[../system-thinking-ai-coding/code-vs-architecture-and-tech-debt]] ("easy, not cheap" — the VN talk's sibling framing).
