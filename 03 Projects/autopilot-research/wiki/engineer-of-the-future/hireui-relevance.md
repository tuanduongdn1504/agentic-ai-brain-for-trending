# hireui Relevance — Answerability IS the Candidate-LLM ADR

> How this bundle translates to **hireui** (the operator's recruitment SaaS; Goal #2 build target). See the RATIFIED **candidate-LLM legibility ADR**: *any hireui LLM path touching a candidate MUST be fixed + legible + audited + human-in-the-loop + eval/bias-gated.*

## The headline: Osmani's thesis is a first-principles derivation of hireui's own ADR

The candidate-LLM legibility ADR was justified by the **EU AI Act Annex III** (recruitment = high-risk). Osmani arrives at the *same* requirements from engineering first principles — which makes his keynote the **conceptual backbone** for the ADR:

| Osmani concept | hireui ADR clause |
|---|---|
| **"Explain it or don't ship it"** | *legible + audited* — every candidate-facing decision must be explainable |
| **Own the verdict** (ship/block/redirect/accept-risk) | *human-in-the-loop* — the recruiter owns the hiring decision, not the model |
| **Inner loop = capability, outer loop = agency** | LLM drafts/scores (inner loop, behind Mosh A2); recruiter decides + owns (outer loop) |
| **Verification is the bottleneck; make it cheap/clear/hard-to-skip** | *eval/bias-gated* — the evals harness is the verification system |
| **CODEOWNERS / who owns the blast radius** | a named human accountable for each candidate-facing surface |

**Takeaway:** cite this topic (not just the EU AI Act) when defending the ADR — it reframes legibility from "compliance cost" to "the definition of engineering in the agent era."

## Direct, adopt-now translations

1. **"Answerability record" on any Match-Explain output.** For every candidate score/summary the LLM produces, persist the **evidence** (which inputs, which prompt/version), the **understanding** (a short human-readable "why"), and require a recruiter **verdict** (accept / override / reject) before it affects a candidate. This is Osmani's evidence/understanding/verdict triad implemented literally — and it's exactly what an Annex-III audit trail needs.
2. **Keep the recruiter on the outer loop.** The LLM may investigate/summarize/rank (inner loop); the recruiter decides, and the UI must make that decision *cheap to verify* — Karpathy's "GUI speeds verification": show a legible diff/evidence panel, not opaque scores (cf. the PokéSynergy "short reason you can act on" pattern already in the corpus).
3. **Evals-as-forcing-function (LangChain) = the bias/eval gate.** hireui's `evals/` harness + the A1 anchor-validation gate already shipped in `bin/autopilot-drain.py` — treat recruiter-labeled evals as the "training gradient" for any prompt/harness change. Don't ship a prompt change without the eval delta.
4. **Guard the three failure modes on the team.** *Cognitive debt* — keep the matching logic explainable, not a black box even the team can't defend. *Cognitive surrender* — never auto-accept an LLM candidate verdict (the Wharton 73% is a legal/bias liability in recruitment). *Orchestration tax* — don't fan out candidate-facing agents faster than a human can own the results.

## What NOT to take from this bundle

- **Ng's "~100% AI code" and Cursor's "~30% fully-autonomous PRs"** are about *internal engineering*, not *candidate-facing product behavior*. hireui can run agents hard on its own codebase; it must **not** let candidate-facing decisions run without a human verdict. Keep the two loops separate.
- **"Move fast / small generalist teams"** (Ng) is fine for building hireui; it does **not** relax the candidate-facing ADR.

## Pilot framing

- **No new pilot required** — this is a **thesis that strengthens existing ADRs + pilots**, not a tool. Its value: a citable, first-principles argument for why the Match-Explain feature must be built legible-and-audited from day one (Osmani), and a concrete "answerability record" data shape to bake into the Match-Explain spec.
- Sequence it *before* any candidate-facing LLM ships: the "answerability record" is a design constraint, not a retrofit.

## Key Takeaways

- **Osmani's answerability thesis independently derives hireui's candidate-LLM legibility ADR** — cite it as the engineering-first-principles backbone.
- Adopt-now: an **"answerability record"** (evidence + understanding + recruiter verdict) on every candidate-facing LLM output; recruiter stays on the **outer loop**; **evals gate** every prompt/harness change.
- Keep **internal-engineering autonomy** (fast, ~100% AI) strictly separate from **candidate-facing decisions** (human verdict required).
- Guard cognitive debt / surrender / orchestration tax as *governance* controls, not just personal habits.

## See also

- [[engineer-of-the-future/osmani-answerability-thesis]] · [[engineer-of-the-future/inner-loop-outer-loop]] · [[engineer-of-the-future/three-failure-modes]]
- [[miai-cv-matching-agent/_index]] — the recruitment-domain feature this governs
- [[prompt-evaluation/_index]] — the eval gate · [[api-security-7-techniques/_index]] — candidate-data authz
- [[pokesynergy-niche-business-tool/_index]] — "explainable constraint-solver" UX pattern for Match-Explain
