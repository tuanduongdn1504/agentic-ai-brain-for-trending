# The payload: audit your own skills

This topic is different from most corpus sources. It isn't a product to evaluate or a claim to fact-check — it's a **rubric + a tool for the operator's own harness**. The operator runs two skill layers this checklist applies to *directly*:

- **This vault's skills** — `05 Skills/` (9 skills) + project-local `autopilot-research/skills/` (`yt-pipeline`, `yt-search`, `notebooklm`, `autopilot-research-routine`, `bypass-403-escalation`).
- **hireui's skills** — the operator-only (I-8) skills in the hireui repo (see [[external|memory: hireui pilot target]]).

Full method menu (A–D tiers): `output/(C) 2026-07-15-pocock-writing-great-skills-pilot-methods.md`. Headlines below.

## Headline pilots

- **A1 — Run `writing-great-skills` over the autopilot-research routine (⭐, ~zero cost).** Install the skill (`npx`/clone from `mattpocock/skills`), invoke it over `(C) autopilot-research-routine.md`. It's a **~1,200-line orchestration skill** — the exact "massive skill" the Pruning axis targets. Look for: **no-ops** (instructions Claude already obeys), **sediment** (rules accreted across sessions/versions), **duplication** (constitutional invariants restated in multiple places), and **branch-only reference** (the 8-phase detail) that could move behind context pointers into `references/`. Success = a smaller, more auditable routine with the same behaviour (deletion-test each cut).
- **A2 — Apply the Trigger axis to `05 Skills/`.** For each of the 9 skills, classify user-invoked vs model-invoked and check it's the *right* choice. Skills with side effects or timing you control (anything that writes/ships) should be **`disable-model-invocation: true`** (Matt's rule: "you don't want Claude deciding to deploy"). This directly encodes hireui's **I-8 operator-only** constraint into the frontmatter mechanism.
- **A3 — Adopt "leading words" in the routine's agent prompts.** The autopilot workflow prompts already lean on dense terms ("refute-first," "docs-lag," "Rule-12 override"). Formalize them as **leading words** and watch the workflow agents echo them in their reasoning — a cheap steering win with a built-in verification signal (the trace).
- **B1 — Split for legwork: `grill-with-docs` → `to-spec` for hireui specs.** hireui's Goal-#2 work (Match-Explain, Candidate-Detail) suffers the exact plan-mode rush Matt describes. Pilot the **two-skill split**: a user-invoked interview skill that *only* interviews (no plan), then a separate spec skill that *only synthesizes* — forcing full clarifying-question legwork. Compare against the current single plan-mode pass. Pairs with [[pocock-real-feature-build/_index]]'s pipeline and [[how-we-claude-code/_index]]'s interview-first phase.
- **B2 — Add a "router skill" to `05 Skills/`.** The talk's unsolved cognitive-load problem (too many user-invoked skills to remember) has a documented cure in the published GLOSSARY: **one user-invoked router skill** that names the others and when to reach for each. This is a direct fix for the vault's growing skill count.
- **C1 — `writing-great-skills` as a pre-merge gate for new skills.** Any new vault skill must pass the checklist (single source of truth, no no-ops, right invocation mode) before it's committed — the skill-authoring analogue of [[prompt-evaluation/_index]]'s eval gate. Ties to Matt's point that **model-invoked skills force you to eval triggering**: prefer user-invoked for the vault's operator-run skills to *avoid* needing triggering-evals.

## The meta-observation for the vault

- **This vault IS a `mattpocock/skills`-style setup**: a `.claude`-directory-of-skills operating system, mostly **user-invoked orchestration** (`/loop autopilot research`) commanding **model-invoked reusable patterns** (the workflow dive/verify agents). The two-layer design in [[pocock-writing-great-skills/trigger-invocation-and-superpowers]] is *already* the vault's implicit architecture — this talk makes it explicit and gives it vocabulary.
- **Deploy-shape note:** unlike most corpus pilots this needs no new infra, no vendor, no cost — it's `npx cc-skills`/clone + invoke over files the operator already owns. It's the **lowest-friction pilot in the corpus** and a candidate to run *this week* alongside the standing cc-sdd / free-claude-code pilot backlog.

## Cross-links

- [[pocock-software-fundamentals/_index]] — the WHY (deep modules, design-the-interface); this is the HOW for the skills that carry it
- [[claude-code-skills-stack/_index]] + [[claude-skills/_index]] — skill composition + grill-me lineage
- [[prompt-evaluation/_index]] — the eval-gate analogue
- [[external|memory: hireui pilot target]] — the I-8 operator-only skill layer this audits
