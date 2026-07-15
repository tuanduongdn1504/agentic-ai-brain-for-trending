# Talk vs the published skill — how `writing-great-skills` evolved past the talk

The only non-CONFIRMED scorecard item (CL5) and several verifier objections all trace to one thing: **the published [`writing-great-skills`](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md) skill has grown richer than the 20-minute talk.** The talk is a faithful, simpler snapshot; the repo is the living, refined version. None of this is a talk *error* — it's the gap between a June recording and a July repo.

## The published skill maps 1:1 to the talk's 4 sections

The `GLOSSARY.md` is organized by four **axes** — exactly the talk's four checklist parts:

| Talk section | Published axis |
|---|---|
| Trigger | **Invocation** |
| Structure | **Information Hierarchy** |
| Steering | **Steering** |
| Pruning | **Pruning** |

…with a **root virtue the talk only implies**: *"A skill exists to wrangle determinism out of a stochastic system; the root virtue is **Predictability** — the agent taking the same **process** every run, not producing the same output."*

## Vocabulary in the repo that the talk doesn't name

The talk gives you 4 axes + ~7 named concepts. The published GLOSSARY adds a fuller domain model (all confirmed present):

- **Router skill** — one user-invoked skill that names the others and when to reach for each; the documented cure for "too many user-invoked skills to remember" (the cognitive-load problem the talk raises but doesn't solve).
- **Information hierarchy** — a **3-tier ladder**: (1) in-skill step, (2) in-skill reference, (3) external reference (behind a context pointer). The talk's "steps + reference + external reference" is this ladder, un-named.
- **Completion criterion** — the checkable, ideally *exhaustive* condition that ends a step ("every modified model accounted for", not "produce a change list"); a vague one invites **premature completion**.
- **Premature completion**, **negation**, **sprawl**, **co-location**, **granularity**, **relevance**, **disclosed reference**, **progressive disclosure** — additional levers/failure modes.

Practical read: **the talk is the tutorial; the GLOSSARY is the reference.** For real skill-authoring work, use the repo.

## The `2PRD` → `to-spec` evolution (scorecard CL5)

- The talk's worked example is a skill called **`2PRD`** ("creates a PRD… three steps… two references"). **There is no `2prd`/`2-prd`/`to-prd` skill in the repo today** (0 code-search hits, no such path).
- The current **`to-spec`** skill is its clear counterpart: its own description says it *"produces a spec (**you may know this document as a PRD**)"*, and its process is the same shape — explore repo → sketch + **check test seams with the user** (the talk's human-in-the-loop checkpoint) → write the spec from an inline template.
- **What evolved:** `to-spec` now also **publishes the spec to the project issue tracker** with a `ready-for-agent` label — a step the talk doesn't mention. The test-seam material is handled inline in step 2 rather than as a separately-labelled reference block.
- **Honest limit:** whether `2PRD` was a *literal earlier name* (renamed) or the presenter's spoken shorthand for a skill always named differently is **unconfirmed** — no `2PRD` trace survives in the repo to prove a rename event. The wiki asserts *correspondence*, not a rename.
- Precedent: the same talk-vs-repo drift shows up in the sibling topic — [[pocock-software-fundamentals/_index]] noted `ubiquitous-language` → `domain-modeling` and `grill-me` (stub) → `/grilling`.

## The sediment-vs-sprawl refinement (scorecard CL10)

- The talk treats a bloated skill's cure loosely: for "a skill with a lot of sediments, look at structure… move to the right branch, or kill it."
- The **published skill separates two failure modes** the talk blends:
  - **Sediment** (stale/irrelevant accreted lines) → cured by **pruning discipline** (delete).
  - **Sprawl** (a skill too long *even when every line is live*) → cured by **structure** (branching, external references).
- So the talk's "fix sediment via structure" is the earlier, coarser framing; the repo's taxonomy is finer. The talk's advice is still basically sound (real-world sediment often *is* misplaced-branch material + stale crud).

## "Deletion test" is talk terminology (scorecard CL11)

- The **no-op concept** is formally in the GLOSSARY ("a line the model already obeys by default"). The **"deletion test"** *label* is **talk-only** — the repo encodes the concept, not that name.
- The talk frames the deletion test as *the* way "I get my skills so small"; the published methodology frames **information hierarchy + progressive disclosure** as the *primary* minimalism lever, with the deletion test as one tool among several. A matter of emphasis, not contradiction.

## Bottom line

Everything the talk teaches is present and correct in the repo. The differences are **additive** (richer vocabulary), **evolutionary** (`2PRD`→`to-spec` gained a publish step), or **emphasis** (info-hierarchy as primary minimalism lever). This is exactly why the scorecard is 13 CONFIRMED / 1 CORRECT-BUT-INCOMPLETE with zero misleads: a domain authority accurately describing his own system, caught only by the clock.
