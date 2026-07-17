# ⭐ hireui Translation — the borrowable pattern

*The point of ingesting this. PokéSynergy's core UX = an **interactive constraint-solver with live, explainable tradeoff feedback** + **expert defaults**. This is a near-perfect fit for hireui **because** it is deterministic and legible — which satisfies the operator's [[external|RATIFIED candidate-LLM legibility ADR]] (any LLM path affecting a candidate outcome must be fixed, legible, audited, human-in-loop, eval+bias-gated; emergent orchestration prohibited on candidate-decision paths).*

## The pattern mapping

| PokéSynergy | hireui |
|---|---|
| Click a threat ("survive Wave Crash") | Adjust a requirement/weight ("require 5+ yrs backend") |
| Points auto-shift **deterministically** (math) | Shortlist re-ranks **deterministically** (weighted score) |
| Live feedback: speed drops, defense up, cost shown | Live feedback: pool size, salary median, evidence per candidate |
| **Explainable reason** for each label | **Explainable evidence trail** for each pass/fail |
| "Auto-build" from top meta spreads | Presets from **your own successful-hire history** |

The critical property: **PokéSynergy's value comes from deterministic, transparent math with human-readable reasons — no black box.** That is exactly what the legibility ADR demands. The borrow is *natively ADR-compliant*.

---

## Feature 1 — Requirement Constraint Solver (deterministic; ADR-safe; ship now)

Recruiter sets a weighted must-have / nice-to-have checklist. As they adjust, the shortlist re-ranks **live**:

- **Per-candidate scorecard** — which must-haves met, which nice-to-haves missing, each with a **deterministic evidence trail** (CV section, linked GitHub, date math — *not* NLP).
- **Pool-level impact** — "47 / 240 pass at these weights"; drop a weight → pool expands live, new entrants highlighted.
- **Cost signal** — median salary expectation of the passing set vs role budget.

**Deterministic/LLM boundary:** score = `Σ(wᵢ × hasSkillᵢ)`; skill presence = keyword/tag/linked-profile/historical-hire match; sort deterministic, ties by recency. **No LLM anywhere in the ranking path.** Every weight change logged with operator ID + timestamp. **Status: ADR-safe, ship-now.**

> ⚠️ Adverse-impact monitoring (e.g. distribution of the passing set across protected attributes) is worth building — but **displaying/collecting protected-attribute data is itself EU-AI-Act-sensitive** and must go through its own legal/ADR review. Treat as aggregate, opt-in, audited — not a casual "diversity counter."

## Feature 2 — "Does this candidate survive the screen?" (hybrid; gated LLM; behind Mosh A2)

Select a candidate → see:

1. **Structured signals (deterministic):** years relevant experience, skill-match count, cohort stats from your own prior hires.
2. **Draft explanation (LLM, advisory, NON-binding):** e.g. "Strong backend + TypeScript; distributed-systems evidence is thin (1 project) — suggest probing in interview."
3. **Operator gate:** recruiter must **approve / edit / reject** before it's saved; the artifact is **read-only, human-context only**.

**Hard ADR guarantees:** the LLM text **never affects ranking or any cutoff**; the **candidate never sees it**; full audit trail (prompt, model, output, operator action). Rejecting the draft changes nothing about the candidate's standing. Ranking stays 100% deterministic (Feature 1). **Status: ADR-safe *only* with the operator gate + Mosh A2 lock + eval/bias monitoring.**

## Feature 3 — Quick-Hire Profile Builder (deterministic; ADR-safe)

PokéSynergy's "auto-build" → **preset requirement profiles derived from your own hire history** ("Junior Backend": from N past successful hires — median exp, top languages, salary band). Recruiter applies + customizes.

**Boundary:** pure SQL aggregation over hire history; **zero LLM**. Transparent sourcing ("N past hires matched this profile"). This is where your **proprietary defaults corpus** becomes the moat PokéSynergy lacks. **Status: ADR-safe, ship-now.**

---

## Sequencing (respecting the ADR + the 8-pilots/0-deployed bottleneck)

1. **Now:** Feature 1 as a Candidate-Detail tab, 3 must-haves, deterministic weights. Measure: does it speed up shortlisting? (A/B vs control.)
2. **Next:** Feature 3 presets from hire history (also deterministic).
3. **Later, gated:** Feature 2's advisory LLM explanation behind Mosh A2 — *only after* deterministic evals + bias monitoring are in place ([[prompt-evaluation/_index]]), and only as read-only operator context.

## Guardrails to carry from the rest of the corpus

- **Legibility ADR** (above) is the governing constraint — deterministic-first, LLM strictly gated & non-binding on candidate outcomes.
- **Authorization / data exposure:** any candidate-data view must respect BOLA/authz discipline — see [[api-security-7-techniques/_index]].
- **First-LLM-feature vendor seam & eval-first:** [[mosh-ai-powered-apps/_index]] + [[prompt-evaluation/_index]].
- **Recruitment-domain sibling** (Match-Explain): [[miai-cv-matching-agent/_index]]; candidate-side inverse: [[external|Storm Bear: career-ops]].

## Key Takeaways

- The borrow = **interactive constraint-solver + live explainable tradeoffs + expert defaults**, and it's **natively ADR-compliant** because it's deterministic and legible.
- **Two ship-now deterministic features** (Constraint Solver, Profile Builder) + **one gated advisory LLM feature** (Survive-the-Screen) with a hard "never affects the candidate outcome" boundary.
- The **explainability-first** ethos ("a short reason you can act on, not opaque scores") is the single best idea to steal wholesale.
