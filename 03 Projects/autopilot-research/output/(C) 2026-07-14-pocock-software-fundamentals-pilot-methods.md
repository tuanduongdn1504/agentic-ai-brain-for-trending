# (C) Pilot methods — pocock-software-fundamentals (2026-07-14)

> Source topic: `wiki/pocock-software-fundamentals/` · Scorecard 13/2 speaker (0 false/fabricated) — safe to build on.
> **Framing note:** this is a *theory* talk; most of its operational content is already piloted or ranked via the sibling Pocock topics. The genuinely NEW pilotable material is **deep modules / improve-codebase-architecture**, **TDD-as-pacing**, and the **grilling fact/decision split**. Methods below avoid duplicating the 23-method pocock-agentic-workflow and 26-method pocock-real-feature-build menus — composability is flagged instead.

## A — hireui Goal #2 (real-software evidence)

- **A1 ⭐ HEADLINE — Deep-module interface-first spec for Match-Explain.** Before implementing hireui's first LLM feature (Match-Explain, per the miai-cv-matching thread), write the module interface FIRST (deep module: one simple interface, LLM plumbing hidden), review only the interface + tests, delegate the implementation to the agent. This *is* the talk's "design the interface, delegate the implementation" — and it is the Mosh A2 vendor-seam pilot's theory, so it upgrades an in-flight pilot rather than adding a new one. Measure: interface churn vs implementation churn; % of implementation you actually had to read. (~0 setup; discipline change only.)
- **A2 — improve-codebase-architecture skill on the Candidate-Detail area.** Copy the MIT SKILL.md into the hireui harness (respect CONSTITUTION I-8 operator-only skills; run it operator-invoked). It scans git-history hot spots, applies the deletion test, and emits an HTML report of deepening candidates — run it on the drifted CandidateDetailScreen area and see if its candidates match the known refactor plan (a cheap validity test of the skill AND a second opinion on the refactor). (~30 min.)
- **A3 — TDD-as-pacing on one agent-built slice.** For one Match-Explain sub-task, force red-green-refactor per step (the `tdd` skill or a constraint line). Measure step size + rework vs the default. Composes with the hireui verify loop; tests-per-commit evidence cf. pocock-real-feature-build.

## B — Vault / pipeline self-improvement

- **B1 ⭐ — The fact/decision split into the routine's operator prompts.** Add the grilling skill's line — *facts from the environment, decisions from the human* — to the autopilot routine's clarification behavior: agents look up what's checkable (gh api, WebFetch) and only surface genuine decisions. This is already implicit practice; codify it as a prompt line in the routine skill at the next routine v2 edit. (5 min, riding an existing edit.)
- **B2 — "Rate of feedback is your speed limit" as a workflow design rule.** When authoring verification workflows, prefer pipeline (verify-as-you-go) over big-bang barriers — this ship's workflow already does it; write the line into the routine's workflow-authoring guidance so it survives.

## C — Personal Claude Code harness

- **C1 — Adopt grilling's matured mechanics** (one-question-at-a-time + act-only-after-confirmation) in your own planning skill, replacing any older grill-me copy. The stage version is outdated; pull from `skills/productivity/grilling/`.

## D — Scrum coaching / teaching

- **D1 — The talk as a 20-minute team explainer.** It's the best short "why fundamentals survive AI" artifact in the corpus (967K views, zero false claims, five real books) — usable as-is for a team viewing + retro. Pair with the [[../wiki/system-thinking-ai-coding/_index]] 3-golden-questions gate for the practice half.
- **D2 — Beck's full quote as the refactoring-budget argument.** "We invest in the design every day, but we have the additional constraint that we need to keep our APIs stable" — the *full* version (with the constraint) is a better coaching line than the talk's trim: daily design investment WITH interface stability = how you sell refactoring to product owners.

## Skip list

- **Don't adopt the anti-specs-to-code position wholesale** — the vault's #1 ranked pilot is cc-sdd (SDD). The synthesis: run the planned cc-sdd pilot AND apply A1's interface-first rule inside it; the two are compatible in practice even though the rhetoric conflicts (both front-load design; they disagree on code-as-artifact).
- **Don't install the full mattpocock/skills pack** — blank-slate discipline (his own June advice) says pull individual procedures (grilling, improve-codebase-architecture) only.
- **Don't cite "vertical slices" from this talk** — description copy only; the talk never covers it.

## Critic reframe

The durable contribution is one sentence: **module boundaries are now agent infrastructure** — interfaces are where humans concentrate design, review, testing, and trust budgets; implementations are where agents work. A1 is that sentence as a pilot, attached to the feature hireui already plans to build — so this topic's pilot cost is ~zero marginal and its evidence lands on the existing Goal-#2 bottleneck (8 ranked pilots / 0 deployed → make A1 part of the first actual deployment, not a 9th ranked item).
