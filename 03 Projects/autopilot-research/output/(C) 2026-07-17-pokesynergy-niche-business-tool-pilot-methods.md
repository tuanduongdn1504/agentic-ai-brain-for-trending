# (C) Pilot Methods — PokéSynergy → "build a business tool like this"

> **Source topic:** [[../wiki/pokesynergy-niche-business-tool/_index]]
> **Operator payload:** *"inspire from it and make business tools like this."*
> **Frame:** PokéSynergy's borrowable core = an **interactive constraint-solver with live, explainable tradeoff feedback + expert defaults**. The recruitment analogue is a **Candidate Constraint Solver** for hireui. Everything below is sequenced against the RATIFIED **candidate-LLM legibility ADR** (deterministic-first; LLM strictly gated + non-binding on candidate outcomes).
> **Ranking note:** this is a *pattern/inspiration* pilot, not a tool to deploy. It competes for attention with the existing 8-pilots/0-deployed backlog — its value is that Tier A is **zero-new-infra** and reuses the Match-Explain work already spec'd in [[../wiki/miai-cv-matching-agent/_index]].

Tiers: **A** = zero/low-code, this week · **B** = deterministic build · **C** = gated-LLM build · **D** = decisions/principles (no build).

---

## Tier A — this week, near-zero code

- **A1 — Paper-prototype the Constraint Solver.** On one real open req, mock the UX: must-have/nice-to-have weights → live shortlist re-rank → per-candidate pass/fail with a **deterministic evidence trail** (CV field / linked profile / date math). Figma or even a spreadsheet. Goal: does "click-to-tune + see who passes + why" actually speed a recruiter up? Measure vs current flow.
- **A2 — Write the explainability spec.** Steal PokéSynergy's ethos verbatim: *every score/label has "a short reason you can act on."* Turn it into hireui's Match-Explain output contract (each match/reject shows the deterministic reasons). This is the eval target for any later LLM work.
- **A3 — Local-first / no-login funnel decision.** Decide whether a recruiter can *try* the solver on sample data with no account (PokéSynergy's trust move). Cheap onboarding-friction win; note PII implications (sample/synthetic data only until auth).

## Tier B — deterministic build (ADR-safe, ship-now)

- **B1 — Candidate Constraint Solver (Feature 1).** Weighted requirements → deterministic live re-rank → evidence trail. `score = Σ(wᵢ × hasSkillᵢ)`; skill presence = keyword/tag/linked-profile/hire-history match; **no LLM in the ranking path**. Log every weight change (operator + timestamp). A/B vs a control group.
- **B2 — Quick-Hire Profile Builder (Feature 3).** Presets from *your own* successful-hire history (SQL aggregation, zero LLM). This is the **proprietary-defaults moat** PokéSynergy lacks — lean into it.
- **B3 — Adverse-impact monitor (guarded).** Aggregate-only distribution checks on the passing set. ⚠️ Collecting/showing protected attributes is itself EU-AI-Act-sensitive → its own legal/ADR review before build; opt-in, aggregate, audited.

## Tier C — gated-LLM build (only after B + evals)

- **C1 — "Does this candidate survive the screen?" (Feature 2).** Deterministic structured signals + an **advisory, non-binding** LLM draft explanation behind **Mosh A2**. Hard guarantees: never affects ranking/cutoff; candidate never sees it; operator must approve/edit/reject; full audit trail (prompt/model/output/action). Gate on deterministic evals + bias monitoring being live first ([[../wiki/prompt-evaluation/_index]]).
- **C2 — Vendor seam.** Route the LLM call through the abstraction from [[../wiki/mosh-ai-powered-apps/_index]] so the model is swappable and metered.

## Tier D — decisions / principles (no build)

- **D1 — Don't copy the business model, copy the patterns.** ADR entry: hireui borrows PokéSynergy's *UX + explainability + distribution*, not its *free-forever/deferred-monetization* model (which only works because YouTube subsidizes Scoriox). hireui must have monetization defined pre-launch.
- **D2 — Own-your-data / own-your-platform is the moat.** Principle: PokéSynergy's existential weaknesses (Nintendo IP landlord, ~3–4yr platform cycle, ~10–15K TAM, subsidized founder) are all things hireui *doesn't* have. Protect that advantage; don't build hireui features that make it dependent on a third party's data/platform in the same way.
- **D3 — Compete on workflow + explainability, not commodity calc.** The EV-optimization "moat" was commodity (many tools do it). For hireui, generic match-scoring is commodity too; the durable edge is explainable "why" + your hire corpus + recruiter-workflow fit.
- **D4 — Beware demo hype.** PokéSynergy's YouTube pitch oversold an "auto-optimizer" the live product doesn't claim. Ship claims defensible on the live product.

---

## The one thing to actually do

**B1 (Candidate Constraint Solver) is the deploy-worthy borrow** — it's deterministic, natively ADR-compliant, reuses the Match-Explain spec, and directly attacks the "0 deployed" bottleneck. Prototype it in A1 this week; if recruiters are faster, build B1. Everything else is supporting cast.
