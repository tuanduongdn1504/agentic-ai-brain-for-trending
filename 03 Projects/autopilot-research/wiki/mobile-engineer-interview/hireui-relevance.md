# hireui relevance & operator use

Three uses: **(1)** interview prep for the operator (interviewee), **(2)** a ready-made **mobile/front-end screening rubric** for a recruiter, and **(3)** an ADR-safe product tie-in for hireui (the recruitment SaaS, Goal #2).

## 1. Interviewee prep

This corpus *is* a study deck for a React Native / React / Flutter role. Fastest path: [[study-guide-and-gaps]] (Tier-1 drills) → your stack's article → [[08-behavioral-and-interview-craft]]. The portable cheatsheet (`output/(C) 2026-08-06-mobile-engineer-cheatsheet-handoff.md`) lets another agent run mock rounds and probe "why".

## 2. Screening rubric (recruiter side)

A concrete, reusable rubric distilled from Tuấn's method — a **fixed** instrument, not emergent LLM scoring:

**JavaScript/Dart core (weight 25%)** — data types & primitives vs modifiers; `null`/`undefined`; `==`/`===`; higher-order fns; array transforms + **live dedupe with `Set`/spread**. Pass = writes a dedupe/sort from a blank editor.

**Async (20%)** — Promise/Future states; async-await as sugar over Promises; event loop micro/macrotask. Pass = explains non-blocking + predicts a `setTimeout`-vs-Promise log order.

**Framework depth (25%, stack-specific)** — React: Virtual DOM, hooks, **useEffect deps**, CSR/SSR. Flutter: Stateless/Stateful + **lifecycle**, **ListView-in-Column**, state mgmt. RN: **Play Store pipeline**, Axios/fetch, REST vs GraphQL. Pass = explains the "why", not just names.

**Engineering hygiene (15%)** — Git (conflicts done right, rebase vs merge, `.gitignore`); a unit test in isolation; SOLID/DRY. **Red flag = "rename the file to avoid a conflict".**

**Behavioral/judgment (15%)** — specialise-then-broaden; scenario answers lead with **communicate/negotiate/escalate**, not "all-nighter"; honest about gaps + a learning plan.

**Scoring bands:** did-not-know / partial / correct per item (mirrors the candidate_verdict scale in [[claims-scorecard]]). A junior/intern hire is bought on **growth trajectory + coachability**, so weight *how they reason and self-correct* alongside raw correctness.

## 3. hireui product tie-in — ADR-safe only

hireui has **no LLM integration yet** ([[external|Storm Bear: hireui-no-llm-yet]]); this is a *build-it-right* opportunity, not a retrofit. Any hireui feature that scores/ranks a candidate for a mobile/front-end role using this rubric **must obey the RATIFIED candidate-LLM legibility ADR** ([[external|Storm Bear: hireui candidate-LLM legibility ADR]]):

- **Fixed + legible:** the rubric above is a **static, human-authored instrument** an LLM grades *against* — never an emergent LLM opinion of "is this a good engineer".
- **Audited + human-in-the-loop:** the LLM proposes per-item verdicts (did-not-know/partial/correct) **with the transcript span cited**; a human recruiter owns the decision.
- **Eval/bias-gated:** behind a vendor seam (Mosh A2), with an eval set + bias checks before it touches a real candidate. This corpus is **Vietnamese-language** — any transcription/scoring path inherits ASR-garble + language-bias risk (see [[caveats-and-corrections]]); that risk is exactly why scoring must be legible + human-owned, per EU AI Act Annex III (hiring = high-risk).

**Adopt-now:** ship the rubric as a **structured interview-scorecard template** (fixed items, manual verdicts, evidence field) inside hireui — the same shape as [[nodejs-backend-interview/hireui-relevance]]'s backend rubric, extended to the mobile/front-end stack. **Out of scope:** any unaudited LLM generation of a candidate verdict.

## Cross-links

- [[nodejs-backend-interview/hireui-relevance]] — the sibling backend rubric (same interviewer, same ADR posture).
- [[miai-cv-matching-agent/_index]] — the CV↔job-matching feature this rubric would feed.
- [[api-types/_index]] · [[api-security-7-techniques/_index]] — the API/authz layer behind the RN backend questions.

## Key Takeaways

- This corpus = a study deck **and** a reusable, fixed screening rubric across JS/Dart core, async, framework depth, hygiene, judgment.
- In hireui, the rubric is **ADR-safe only as a fixed instrument an LLM grades against with cited evidence + human ownership** — never emergent candidate scoring.
- Vietnamese-language + ASR-garble risk is precisely why any scoring path must be legible, audited, and human-in-the-loop.

**Back to** [[_index]].
