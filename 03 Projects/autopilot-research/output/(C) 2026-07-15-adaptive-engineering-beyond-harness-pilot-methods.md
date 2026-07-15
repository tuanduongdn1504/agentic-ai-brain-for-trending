# Pilot Methods — adaptive-engineering-beyond-harness

> Source topic: [[../wiki/adaptive-engineering-beyond-harness/_index]] · Talk: Rajiv Chandegra, *"Beyond the Harness"* (AI Engineer Europe 2026)
> Generated: 2026-07-15 · Companion to the in-wiki [[../wiki/adaptive-engineering-beyond-harness/hireui-and-vault-pilot]]

## ⚠️ Unusual posture: this is a "watch, don't build" topic

This talk is a design **philosophy** with **no method, tool, benchmark, or working implementation**. There is nothing to install or clone. Every prescriptive claim ("let the harness emerge") is a *direction*, not a *procedure*, and the vault's own 62-wiki evidence currently points the **opposite** way (deliberate harness engineering keeps winning — see [[../wiki/adaptive-engineering-beyond-harness/vs-harness-engineering-corpus]]). So the "pilots" below are **lenses and guard-rails**, plus an explicit do-not-build list.

---

## Tier A — Adopt now (zero-cost lenses)

| # | Method | What / Why | Effort | Deliverable |
|---|---|---|---|---|
| **A1** | **Cynefin "complicated vs complex" pre-flight** | Before designing any harness, classify the task. Complicated (knowable/plannable) → keep the fixed harness. Complex (self-organizing/non-decomposable) → probe-sense-respond. Almost all hireui + vault work is **complicated** → the talk *validates* the current approach. | ~15 min | One line in the harness-design checklist. |
| **A2** | **Three-dials review lens** | Describe existing vault workflows on *enable↔govern*, *reward↔cost*, *coupling-rate*. Spot steps that are over-locked-down for exploratory work. | ~1 h | Annotate the wiki-ship / autopilot loop with dial positions. |
| **A3** | **Design-time vs runtime adaptivity vocabulary** | Stop calling configurable-up-front harnesses (Pi, custom CLAUDE.md, skills) "adaptive." Reserve "adaptive" for runtime self-reorganization (unbuilt). | ~0 | Terminology note in harness-engineering thread. |

## Tier B — hireui guard-rails (the anti-adoption value)

| # | Method | What / Why | Effort | Deliverable |
|---|---|---|---|---|
| **B1** | **Legibility-required ADR for candidate-facing LLM paths** | The critic's sharpest point: emergent/opaque agents are unacceptable in **recruiting** (hireui's domain). Turn it into a rule: Match-Explain / ranking / screening must be **fixed, legible, audited** — no emergent orchestration. | ~30 min | ADR: *"candidate-impacting LLM decisions → fixed legible harness only."* Composes with api-security BOLA work + miai recruiter-labeled evals. |
| **B2** | **Reinforce "harness > model" cost posture** | Agrees with Pocock/Tejas Kumar: leverage is in the harness. Keep hireui's first LLM feature model-agnostic behind the Mosh A2 vendor seam, cheap model + good harness. | (already planned) | No new work — cross-reference. |

## Tier C — Vault / knowledge-work

| # | Method | What / Why | Effort | Deliverable |
|---|---|---|---|---|
| **C1** | **Wire this in as harness-engineering's named counter-thesis** | When the harness-engineering thread approaches Storm Bear promotion (v66+ candidate), cite this as the strongest "fixed harnesses may not be the end state" articulation. Prevents "more structure = always good." | ~20 min | Cross-link added (done this ship). |
| **C2** | **Watch the horizontal-intelligence bet** | The talk's one falsifiable claim: group-coordination > individual-smartness. If a future ingest shows emergent orchestration beating coordinator-directed on a real task, that's the trigger to re-evaluate. | ongoing | Flag in multi-agent-orchestration research-roadmap. |

## Tier D — Explicit skip / do-not-build

- **D1 · Do NOT build an emergent multi-agent orchestrator** for hireui or the vault. No implementation to copy; failure modes (drift, monoculture, legibility collapse) bite hardest in the operator's regulated domain.
- **D2 · Do NOT relax the autopilot routine's constitutional constraints** in the name of "emergence." It's a fixed harness on purpose, for a complicated problem — exactly where the talk agrees the factory model is right.

## The verdict

> **Adopt the question (A1: complicated vs complex?), adopt the guard-rail (B1: keep candidate paths legible), watch the bet (C2: horizontal intelligence). Build nothing (D1/D2).**

The most valuable thing this talk gives the operator is *the clearest articulation of the risk that justifies staying with deliberate, legible harness engineering* — i.e. its own best objection.
