# Caveats and corrections — don't re-fabricate

## Source

- Adversarial-verify pass of Workflow `wf_8897fa8d-c95` + operator `gh api` ground-checks (2026-07-03). Ledger: [[source-provenance]].

## The don't-re-fabricate list

| # | Wrong claim (source of error) | Correct fact |
|---|---|---|
| 1 | settings.local.json has "170+" allow entries (deep-dive overstatement) | **89 entries** (counted via API) |
| 2 | Ralph loop "max 100 iterations" (video's spoken claim) | Current `.sandcastle/main.ts`: **`MAX_ITERATIONS = 10`**. Code wins over video; the March harness may have differed, but never cite 100 as current. |
| 3 | "/ubiquitous-language skill doesn't exist" (a VERIFIER's misfire) | It **exists, deprecated**: `skills/deprecated/ubiquitous-language/SKILL.md`; superseded by `skills/engineering/domain-modeling/` |
| 4 | mattpocock/skills ≈ 53K★ (deep-dive undercount) / "repo couldn't exist before June 2026" (verifier confusing a release tag with repo creation) | **154,511★** (2026-07-03); repo **created 2026-02-03**; v1.0.0 release tag 2026-06-17 is a *tag*, not creation |
| 5 | Cohort ends April 13 | **March 30 → April 8, 2026**, $795 |
| 6 | `/btw` shipped in v2.1.187 | Shipped **by v2.1.79 or earlier**; v2.1.187 only improved it |
| 7 | "Ralph" is a tool Matt built | **Ralph = technique** (Huntley lineage); the tool is **Sandcastle** (`@ai-hero/sandcastle`) |
| 8 | Repo has ~637 closed issues | That was March point-in-time; **1,109+** by 2026-07 |
| 9 | arXiv:2410.01985 shows "lost-in-the-middle" | It's **Lost-in-Distance** (relative separation between facts) — related but distinct; don't cite it for middle-position claims |
| 10 | aihero.dev shortlinks in the description work | **Both 404 now** (`/s/FpvIa6`, `/s/BQGSo5`) |

## Video-vs-current-repo drift (neither is "wrong" — check dates)

- `pnpm ralph` (video) → **`pnpm sandcastle`** invoking `.sandcastle/main.ts` (now).
- Monolithic loop prompt (video) → **4-phase Plan→Implement→Review→Merge** with per-phase prompts (now).
- One-issue-at-a-time (video) → **4 issues in parallel** (now).
- Label-based human-in-the-loop skipping (video claim) → **dependency-based selection** + implement-label gating in current source; the video's label-skip line was not found in today's code.
- Issue closed on commit (video narration) → **two-phase closure at merge** (now).

## Claims that are positions, not facts

- **"Specs-to-code is just never going to work."** Matt's stance, argued from one QA-discovered edge case. This vault's SDD thread (cc-sdd #1 pilot, OpenSpec, spec-kit; Storm Bear Pattern #21) is the counter-position; note Matt himself front-loads ~22 min of requirement grilling + a PRD — the disagreement is about *degree and rigidity* of upfront spec, not its existence. Zen van Riel's anti-SDD stance ([[../harness-engineering/personal-repo-zen-mixed-effort-parallel]]) is the corpus's other datapoint on this axis.
- **"Not calling a tool is always more token-efficient"** (his AskUserQuestion rationale) — directionally true but weakened by Claude 4.x token-efficient tool use; his UI/flow preference is the durable half of the argument.
- **Q&A-co-location = attention hotspot** — plausible, supported only indirectly (Lost-in-Distance research); no controlled study.

## Unverified / reported-only

- **Jaman** (day-shift/night-shift attribution) — not located; keep as "attributed by Matt."
- Exact per-run stats beyond what's on screen (5 iterations / 6 commits run 1; 14 commits total; 6 issues in 8 min QA) — on-screen observations, not repo-derivable.
- The video's ~1,200-commit count — plausible, unpaginated, unverified exactly.

## Key Takeaways

- The two headline numbers people will misquote: **89** allow-list entries and **10** max iterations.
- The recurring corpus lesson repeats: **verifiers that can't find something declare it fabricated** — this run's ddd-verifier refuted a real-but-deprecated skill and invented an impossible-timeline argument from a release tag. Ground-check before accepting refutations of *existence* claims.
- Distinguish three claim classes when citing this topic: **video-time facts** (may have drifted), **current-source facts** (dated 2026-07-03), and **Matt's positions** (argue, don't cite as fact).
