# Claims scorecard — 18 claims verified

## Source

- Workflow `wf_75a9c75d-7e4` (32 agents: 6 dives + 25 refute-first verifiers + critic; ~1.56M tokens, 412 tool calls, 0 errors) + main-loop `gh api`/WebFetch ground-checks. Method + misfire log: [[source-provenance]].

## Tally

**Speaker claims (15): 13 CONFIRMED · 2 CORRECT-BUT-INCOMPLETE · 0 MISLEADING · 0 FALSE · 0 FABRICATED.**
**Channel-description claims (3): 1 CORRECT-BUT-INCOMPLETE · 2 MISLEADING.**

A **high-integrity talk** — every book quote, skill, and number the speaker put on stage checks out; the only misleading items are the **AI Engineer channel's description copy**, not Matt's words. Joins [[../github-copilot-cli-agents/_index]] (same channel!), [[../local-ai-coding-agents/_index]], [[../miai-iphone-ocr-server/_index]] at the honest end of the corpus spectrum.

## Speaker claims

| # | Claim | Verdict | Ground truth |
|---|---|---|---|
| 1 | Teaches "Claude Code for Real Engineers" (caption garbles it "Clojure Code") | **CONFIRMED** | [aihero.dev cohort page](https://www.aihero.dev/cohorts/claude-code-for-real-engineers-2026-04); cohort ran 2026-03-30 → 04-08 (ended days before this talk was given); prior version 2,500+ students |
| 2 | Ousterhout's complexity definition | **CONFIRMED** | Verbatim, Ch. 2 ([[the-originals]]) |
| 3 | Deep vs shallow modules rendering | **CONFIRMED** | Faithful paraphrase, Ch. 4 |
| 4 | PragProg "software entropy" chapter | **CONFIRMED** | Topic 3, Ch. 1 (broken windows) |
| 5 | PragProg "no one knows exactly what they want" | **CONFIRMED** | Tip 75, Ch. 8 "Before the Project" |
| 6 | PragProg "outrunning your headlights" / "rate of feedback is your speed limit" | **CONFIRMED** | Topic 27, Ch. 4 — tagline is the book's own |
| 7 | Brooks "design concept" (shared invisible idea) | **CONFIRMED** | *The Design of Design*; "shared invisible entity," conceptual integrity |
| 8 | Brooks "design tree" (walk branches, dependent decisions) | **CORRECT-BUT-INCOMPLETE** | The tree IS in Brooks Ch. 2 — as the "Rational Model" **he critiques as unrealistic**; talk presents it unqualified |
| 9 | Kent Beck: "Invest in the design of the system every day" | **CORRECT-BUT-INCOMPLETE** | XP Explained 2nd ed., Incremental Design — real, but original adds "…keep our APIs stable" |
| 10 | Grill-me repo "has like 13,000 stars or something" | **CONFIRMED** | Approximately right at the time (repo created 2026-02-03; ~13K around the talk; garble-of-130K **mathematically refuted** — 130K then would mean growth *deceleration*, contradicting the verified 150.8K→169.6K trajectory). Same-day third-party recap ([tldrecap.tech](https://tldrecap.tech/posts/2026/aie-europe/software-fundamentals-ai/)) independently heard "over 13,000 stars" |
| 11 | "It just went nuts, went viral" | **CONFIRMED** | 13K → **169,558★** (gh api 2026-07-14) in ~12 weeks; Storm Bear Pattern #52 extreme-viral-velocity subject |
| 12 | Grill-me skill text as shown on slide | **CONFIRMED** (evolved) | Near-verbatim in `skills/productivity/grilling/SKILL.md`; grill-me is now a stub invoking it; drift: "this plan"→"this", "design tree"→"decision tree" ([[design-concept-and-grill-me]]) |
| 13 | Ubiquitous-language skill (scans codebase → term tables) | **CONFIRMED** (lifecycle) | Now `skills/deprecated/ubiquitous-language/`, superseded by `skills/engineering/domain-modeling/` |
| 14 | TDD skill exists | **CONFIRMED** | `skills/engineering/tdd/` ("red-green-refactor") |
| 15 | "Improve codebase architecture" skill exists | **CONFIRMED** | `skills/engineering/improve-codebase-architecture/` — "turn shallow modules into deep ones… testability and AI-navigability" |

## Channel-description claims (not the speaker's words)

| # | Claim | Verdict | Ground truth |
|---|---|---|---|
| 16 | Principles covered include "**vertical slices**" | **MISLEADING** | Zero mentions in the talk (grep-verified) — description promises a fourth principle the talk never delivers |
| 17 | "ship high-quality applications with **AI agent swarms**" | **MISLEADING** | The talk is a **single AFK agent + human strategist** model; no swarm/orchestration content at all |
| 18 | "After **18 months** of teaching developers to build with AI agents" | **CORRECT-BUT-INCOMPLETE** | AI Hero's first public cohort launched 2025-07-14 (~9 months before upload); 18 months only works counting content development from ~Oct 2024 |

## Context claims (established during verification, not from the video)

- Event: **AI Engineer Europe 2026** (London, Queen Elizabeth II Centre, April 8–10) — NOT the World's Fair the description promos ([[caveats-and-corrections]] for the verifier-misfire story).
- **967K views ≈ 15–290× the channel's typical conference talk** (8 sampled comparisons: 3.3K–63.5K views) — this is the AI Engineer channel's breakout video, and a Pocock-reach datum consistent with his 296K-sub channel + 287.4K X followers (both verified).
- mattpocock/skills now **39 skills / 6 categories** (grew from 37 on 2026-07-03).

## Key Takeaways

- Zero false or fabricated claims from the speaker — the corpus' third consecutive high-integrity source from the AI Engineer channel orbit.
- The two precision notes worth repeating when citing the talk: Beck's quote is simplified; Brooks' design tree is the model Brooks critiqued.
- The two misleads are description copy — a recurring pattern (cf. [[../miai-iphone-ocr-server/_index]]'s intro framing): **verify the packaging separately from the content**.
- Cross-links: [[the-originals]] · [[caveats-and-corrections]] · [[source-provenance]].
