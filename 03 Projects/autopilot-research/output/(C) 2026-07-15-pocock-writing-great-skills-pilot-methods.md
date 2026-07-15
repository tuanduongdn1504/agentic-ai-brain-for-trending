# (C) Pilot methods — pocock-writing-great-skills (2026-07-15)

> Source: [[pocock-writing-great-skills/_index]] — Matt Pocock, *"Building Great Agent Skills: The Missing Manual"* (AI Engineer World's Fair 2026, `UNzCG3lw6O0`).
> **Unique framing:** this source is a **rubric + tool for the operator's own harness**, not an external product. The deliverable is *auditing and rewriting the skills the operator already runs* — the lowest-friction pilot in the corpus (no vendor, no infra, no cost).
> Targets: (1) this vault's skills — `05 Skills/` + `autopilot-research/skills/`; (2) hireui's I-8 operator-only skills.
> The tool: [`writing-great-skills`](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md) from `mattpocock/skills` (MIT).

Tags: 🧰 skill-authoring · 🔒 I-8/side-effects · 🧪 gate · 🏗️ vault-infra

---

## A — This week, ~zero cost (vault-local)

- **A1 ⭐ — Prune the autopilot-research routine with `writing-great-skills`.**
  - Install: `npx cc-skills add mattpocock/skills` (or clone the repo and copy `skills/productivity/writing-great-skills/`).
  - Invoke it over `03 Projects/autopilot-research/skills/(C) autopilot-research-routine.md` (~1,200 lines = the "massive skill" the Pruning axis is built for).
  - Hunt the four failure modes: **no-ops** (deletion-test each instruction Claude already obeys), **sediment** (rules accreted across v1/v2.1/session-66 amendments), **duplication** (constitutional invariants restated in CLAUDE.md *and* the routine), **branch-only reference** (the 8-phase detail + loop-log template → move behind context pointers into a `references/` file).
  - Success criterion (goal-driven, per Rule 4): a smaller routine that produces an **identical loop-log + wiki** on a re-run of a known topic. Deletion-test every cut against that.
- **A2 — Trigger-axis audit of `05 Skills/` (9 skills).** Classify each user-invoked vs model-invoked; verify the choice. Anything with **side effects or operator-controlled timing** → `disable-model-invocation: true`. This encodes hireui's **I-8 operator-only** rule into the actual frontmatter mechanism, and matches Matt's "you don't want Claude deciding to deploy."
- **A3 — Formalize leading words in the workflow prompts.** The dive/verify/critic prompts already use dense terms ("refute-first," "docs-lag," "Rule-12 override," "discard-as-garble"). Promote them to explicit **leading words** in the routine's prompt templates; watch the workflow agents echo them in reasoning traces (built-in verification signal). Cheap steering win.

## B — Next, structural (vault + hireui)

- **B1 ⭐ — Legwork split for hireui specs: `grill-with-docs` → `to-spec`.** hireui's Goal-#2 features (Match-Explain, Candidate-Detail) hit the exact plan-mode rush Matt names. Pilot two skills: an interview-only skill (no plan) then a synthesize-only spec skill (no interview) — forcing full clarifying-question legwork. Bake-off against the current single plan-mode pass; measure question depth + rework. Pairs with [[pocock-real-feature-build/_index]] + [[how-we-claude-code/_index]].
- **B2 — Add a router skill to `05 Skills/`.** Cure the growing cognitive-load of many user-invoked skills with one user-invoked **router** that names the others + when to reach for each (documented in the published GLOSSARY; the talk raises the problem but doesn't solve it).
- **B3 — Two-layer refactor of the autopilot skills.** Make the split explicit: `autopilot-research-routine` + `/loop` entry = **user-invoked orchestration**; push shared sub-procedures (`yt-search`, `notebooklm`) toward **model-invoked reusable patterns** the routine reaches — the `mattpocock/skills` two-layer design ([[pocock-writing-great-skills/trigger-invocation-and-superpowers]]).

## C — Gate / discipline

- **C1 — `writing-great-skills` as a pre-commit gate for new vault skills.** No new skill ships until it passes the checklist (single source of truth · no no-ops · right invocation mode · branch-only material externalized). The skill-authoring analogue of [[prompt-evaluation/_index]]'s eval gate.
- **C2 — Prefer user-invoked to avoid triggering-evals.** Matt's insight: model-invoked skills force you to *eval that they fire correctly*. For operator-run vault skills, default to **user-invoked** — it removes that eval burden entirely (and matches how the operator already works: `/loop`, `/schedule`, `compile`).

## D — Decide / ADR

- **D1 — Portability ADR: Claude-Code extension vs agentskills.io core.** `disable-model-invocation` is a **Claude Code extension**, not in the portable [agentskills.io](https://agentskills.io) 6-field standard ([[pocock-writing-great-skills/disable-model-invocation-mechanism]]). Decide whether the vault's skills target *portable* (core 6 fields, works on Copilot CLI/Codex CLI too) or *Claude-Code-optimized* (use extensions freely). Ties to the corpus agentskills.io thread ([[github-copilot-cli-agents/agent-skills-shared-standard]]).
- **D2 — "Skill hell" audit of the operator's installed skill sets.** The operator tracks many external skill sets (cc-sdd, superpowers, Eric-Tech 8, G-Stack, Taste Skill…). Run `writing-great-skills` over the *community* skills before adopting them — Matt's explicit recommended use ("check the skills you're pulling in are any good"). Feeds the standing pilot backlog.

---

## Skip / don't

- Don't rewrite all 9 `05 Skills/` at once — A1 on the one routine first, measure, then generalize (Rule 2 simplicity + Rule 3 surgical).
- Don't treat the checklist as gospel over the vault's own librarian rules — where they conflict (e.g. "ask before editing existing notes" vs an aggressive prune), **strictest wins** per the 12-Rule CLAUDE.md.
- Don't assume the published skill == the talk — use the live GLOSSARY (richer): [[pocock-writing-great-skills/talk-vs-published-skill]].

## Why this ranks high

- **Lowest-friction pilot in the corpus:** no vendor, no infra, no spend — `npx`/clone + invoke over files the operator owns.
- **Compounding:** every vault skill it improves makes every future `/loop` cheaper + more auditable (Pattern: the vault's own Rule 6 token-budget discipline made mechanical).
- Deploy-shape: run **A1 this week** alongside the standing cc-sdd / free-claude-code pilot backlog; it's orthogonal (skill-quality layer) and needs ~1 hour.
