# Design concept + grill-me — fixing "the AI didn't build what I wanted"

## Source

- Transcript `raw/2026-07-14-pocock-software-fundamentals.md` (failure mode #1 of [v4F1gFy-hqg](https://www.youtube.com/watch?v=v4F1gFy-hqg)) · skill text ground-checked via `gh api` 2026-07-14.

## The failure mode

- You had an idea; the AI built something else. PragProg's diagnosis: **"no one knows exactly what they want"** — prompting *is* requirements gathering, and the requirements live in your head, unextracted.

## Brooks' design concept

- From Frederick P. Brooks, ***The Design of Design*** (2010): when multiple designers work together, the thing being designed exists as a shared, **ephemeral idea floating between them** — the **design concept**.
- Matt's rendering: "It's **not an asset**, it's not something you can put in a markdown file, it is the **invisible sort of theory** of what you're building."
- His diagnosis of the failure mode: **"Me and the AI don't share a design concept."** The fix is not a better artifact — it's a process that *builds the shared theory*.
- ⚠️ This is a near-restatement of **Naur's "Programming as Theory Building"** (1985) — see [[video-to-corpus-crosswalk]] for the Brooks↔Naur mapping against [[../system-thinking-ai-coding/naur-programming-as-theory-building]].

## The grill-me skill

- On-stage text: *"Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree — which is another thing from Frederick P. Brooks — resolving dependencies between decisions one by one."*
- **Ground-checked 2026-07-14:** the live skill is now split — [`skills/productivity/grill-me/SKILL.md`](https://github.com/mattpocock/skills) is a stub (`disable-model-invocation: true`) that runs a `/grilling` session, and [`skills/productivity/grilling/SKILL.md`] carries the text: *"Interview me relentlessly about every aspect of **this** until we reach a shared understanding. Walk down each branch of the **decision tree**, resolving dependencies between decisions one-by-one."*
  - Two evolutions since the stage version: "this plan" → "this" (broader trigger surface) and **"design tree" → "decision tree"** (the Brooks term genericized).
  - ⚠️ Brooks nuance ([[the-originals]]): the design tree appears in Brooks Ch. 2 as the **"Rational Model" he critiques as unrealistic** — grill-me repurposes it as a deliberate interview procedure, which is defensible, but don't cite Brooks as endorsing tree-walking design.
  - The matured skill adds: one question at a time ("asking multiple questions at once is bewildering"), recommended answer per question, **facts looked up from the environment vs decisions put to the human**, and a hard gate: "Do not act on it until I confirm we have reached a shared understanding."
- Effect he reports: 40–100 questions before the model is satisfied; the AI becomes "a kind of adversary." The grilled conversation then becomes a PRD, or (small changes) goes **straight to issues** for the AFK agent — the exact pipeline demonstrated in [[../pocock-real-feature-build/grill-me-in-practice]].

## The plan-mode critique

- "Don't at me on this": grill-me is **better than default plan mode** in Claude Code, because plan mode is "extremely eager to create an asset" — it wants a plan file and to start working — whereas the point is to **reach a shared design concept first**, then let artifacts fall out.
- This is the theory behind the "grill-me-as-plan-mode" pilot already ranked in [[../pocock-agentic-workflow/_index]]'s methods file: the artifact-first vs theory-first distinction is Brooks' distinction, operationalized.

## Key Takeaways

- The root cause of "built the wrong thing" is a missing **shared theory**, not a missing document — so the fix is interrogation (grill-me), not more spec prose.
- The skill's stage text survives near-verbatim in production (`grilling`), with "design tree"→"decision tree" the only conceptual drift — the Brooks lineage is real but now unlabeled in the repo.
- Grill-me deliberately inverts plan mode's artifact eagerness; artifacts (PRD/issues) are *outputs* of shared understanding, never substitutes for it.
- Facts-from-environment vs decisions-from-human is the matured skill's sharpest line — it splits the interview into what the agent should look up and what only you can answer.
- Cross-links: [[../pocock-real-feature-build/grill-me-in-practice]] (22 minutes of this skill in real use) · [[../how-we-claude-code/_index]] (Anthropic's interview-first pillar — independent convergence) · [[../workflow-ai-coding/_index]] (grill-me's first corpus appearance).
