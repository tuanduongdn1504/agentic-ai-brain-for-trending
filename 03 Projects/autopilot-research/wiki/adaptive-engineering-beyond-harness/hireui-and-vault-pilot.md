# Pilot Posture — hireui & the Vault

**Honest framing first:** this is the rare corpus topic where the correct pilot posture is mostly **"do NOT deploy this yet."** The talk is a design *philosophy* with no method, no tool, no benchmark, and no working implementation ([[failure-modes]]). There is nothing to `npx`, clone, or install. So this file is a *lens*, not a menu of harnesses — what to **think differently** about, what to **watch**, and the one small thing that's actually usable today.

Ranked by usefulness, most-actionable first.

## Tier A — Usable today (a lens, not a build)

- **A1 · Run the Cynefin "complicated vs complex" pre-flight before designing any harness.** The single most portable, zero-cost idea in the talk. Before you spec a fixed harness for a task, ask: *is this **complicated** (knowable, decomposable, plannable) or **complex** (self-organizing, non-decomposable, needs probe-sense-respond)?*
  - **hireui:** Candidate-Detail refactor, CV-parsing, Match-Explain, API-security hardening, Docker/CI-CD — **all complicated.** → keep using the deliberate fixed harness (cc-sdd / spec-first / verify-loop). The talk *validates* the operator's current approach for these.
  - **Genuinely complex** cases in the operator's world: multi-team Scrum org dynamics, a live hiring market's behavior — *these* are where probe-sense-respond beats a plan. Different tool for a different problem.
  - **Deliverable:** one line in the hireui/vault harness-design checklist: *"Complicated → plan & fix the harness. Complex → constrain & sense-respond. Don't treat complex as complicated."*

- **A2 · Apply the three constraint-dials as a review lens on the vault's own multi-agent work.** The talk's one concrete mechanic = **enable↔govern**, **reward-cohesion↔cost-deviation**, **rate-of-coupling** ([[adaptive-engineering-mechanics]]). Use them to *describe* (not redesign) the vault's existing orchestration:
  - The [[autopilot-research-routine]] loop and the verification workflows in this very ingest are **hard-governed, deviation-costed, low-coupling** harnesses — deliberately. Naming where they sit on the three dials is a cheap way to reason about whether a given workflow is *too* locked-down for an exploratory task.
  - **Deliverable:** annotate one workflow (e.g. the wiki-ship pipeline) with its position on the three dials; note whether any *exploratory* step (e.g. "find candidate topics") would benefit from *more enable / higher coupling*.

- **A3 · Import the design-time-vs-runtime adaptivity distinction.** [[adaptive-engineering-mechanics]] sharpens a fuzzy corpus term: most "adaptive/extensible" harnesses (Pi, custom CLAUDE.md, skills) are **design-time** adaptive; runtime self-reorganization is unbuilt. Use this to avoid over-claiming "adaptive" for anything that's just *configurable up front*.

## Tier B — hireui relevance (indirect, via the legibility objection)

- **B1 · Legibility is a *requirement*, not a nice-to-have — and this talk is the argument for why.** The critic's sharpest objection ([[failure-modes]] L2-#3) is that emergent/opaque agent behavior is unacceptable in **recruiting** (hireui's exact domain), medicine, and finance. Flip it into a hireui design rule: **any LLM feature that affects a candidate's outcome (Match-Explain, ranking, screening) must be legible and auditable** — decisions traceable to inputs, no "the agents self-organized." This composes with the [[external|api-security-7-techniques/_index]] BOLA/authorization work and the [[external|miai-cv-matching-agent/_index]] recruiter-labeled-evals posture.
  - **Deliverable:** an ADR line — *"hireui candidate-facing LLM decisions: fixed, legible, audited harness only. Adaptive/emergent orchestration is out of scope for candidate-impacting paths."* (This is the *anti*-adaptive-engineering decision, and the talk is the best articulation of the risk it guards against.)

- **B2 · "Harness > model" reinforces the existing cost posture.** Chandegra's premise agrees with [[external|pocock-agentic-workflow/_index]] and [[external|harness-engineering/tejas-kumar-anchor]]: leverage is in the harness, not the model. → keep hireui's first LLM feature model-agnostic behind a vendor seam (the [[external|mosh-ai-powered-apps/_index]] A2 seam), cheap model + good harness.

## Tier C — Vault / knowledge-work

- **C1 · Add "adaptive engineering" as the named counter-thesis in the harness-engineering thread.** This topic exists so the [[external|harness-engineering/_index]] flagship has a *loyal opposition*. When that thread approaches Storm Bear promotion (it's a candidate at v66+), it should cite this talk as the strongest articulation of "why fixed harnesses might not be the end state." Prevents the corpus from treating "more structure" as unconditionally good.
- **C2 · Watch the horizontal-intelligence bet.** The talk's one falsifiable strategic claim (horizontal group-coordination > vertical individual-smartness) maps onto [[external|multi-agent-orchestration/_index]]. If a future ingest shows decentralized/emergent orchestration beating a coordinator-directed one on a real task, *that's* the evidence that would move this from frontier-watch to adopt.

## Tier D — Explicit skip / do-not-do

- **D1 · Do NOT build an emergent multi-agent orchestrator for hireui or the vault.** No implementation exists to copy; the failure modes (drift, monoculture, legibility collapse) bite hardest in the operator's regulated domain; and every *shipped* corpus win is a *more* deliberate harness. This is a research direction, not a 2026 build ([[vs-harness-engineering-corpus]]).
- **D2 · Do NOT relax the autopilot routine's constitutional constraints** ("NEVER recurse," scope clamp, metric-bounded) in the name of "letting the harness emerge." The routine is a fixed harness *on purpose*, for a *complicated* problem (knowledge compilation) — exactly the case the talk itself says the factory model is right for.

## The one-line pilot verdict

> **Adopt the *question* (complicated vs complex?), not the *answer* (let it emerge). Use the talk as the reason hireui's candidate-facing LLM paths must stay legible. Watch the horizontal-intelligence bet; build nothing.**

## Key takeaways

- Highest-value, zero-cost action: **A1** — the Cynefin pre-flight, which *validates* the operator's current fixed-harness approach for hireui's (complicated) work.
- The talk's best hireui contribution is a **guard-rail** (B1: keep candidate-impacting decisions legible), i.e. the argument *against* adopting the talk's own prescription for that domain.
- Everything buildable here is **watch, not build** (D1/D2) — and that's the honest, evidence-based call as of mid-2026.
