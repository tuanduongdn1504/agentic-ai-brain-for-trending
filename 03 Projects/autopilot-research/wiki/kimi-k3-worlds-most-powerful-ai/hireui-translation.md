# hireui translation

**Question:** should the operator adopt Kimi K3 as a cheaper-Claude alternative for hireui (TalentAxis recruitment SaaS)?

**Recommendation: AVOID for any candidate-facing path. WATCH (deferred) for a possible non-candidate niche.**

This is a rare clear-cut verdict — K3 hits **three independent hard stops** against the RATIFIED hireui candidate-LLM legibility ADR, before cost even enters the conversation.

## Why AVOID (candidate-facing)

1. **Data residency (hard stop).** K3 is a **Chinese-hosted API** (Moonshot/Beijing). hireui recruitment paths are **EU AI Act Annex III high-risk**; candidate PII flowing through a non-EU/non-US controller is exactly what the residency posture (and the prior "official API keys" + Memory-Stores residency ADRs) rules out. Self-hosting in the EU is the only fix — and it's **blocked for months** by the 2.8T hardware wall ([[open-weights-reality]]).
2. **Anti-fabrication (hard stop).** K3's **hallucination rate is 51%** (up from 39%). In recruitment, a fabricated qualification, requirement, or reason on a candidate-facing Match-Explain is **legal liability + bias risk**. The corpus already chose **Claude Haiku 4.5** for Match-Explain precisely for legibility and control; K3 moves the wrong way.
3. **Legibility / auditability (hard stop).** The ADR requires **fixed + legible + audited + human-in-loop + eval/bias-gated**. K3 at launch is **closed** (weights not out) with an **undisclosed system prompt and safety classifiers** — you can't audit what you can't inspect, can't verify bias behavior, can't guarantee candidate-safety instructions hold.

Supporting: **agentic tool-calling is unproven** (Match-Explain reads a CV, calls the Candidate API, correlates against a job — the exact tool-use the Frontend-Arena #1 does *not* measure, per Willison); and the **distillation cloud** over K3's provenance ([[reception-and-skeptics]]) sits badly with a "no silent assumptions" ADR.

## Where it *could* legitimately fit (non-candidate only)

- **Throwaway UI prototyping.** K3's real strength (frontend/visual coding #1) maps to **non-deployed, no-candidate-data** work — e.g. a Figma→React spike on the CandidateDetail refactor, design variations, mock component trees. Low-risk if nothing candidate-facing ships from it.
- **Internal / admin-only tooling.** Recruiter-workflow mockups, internal dashboards, admin reporting UIs — plays to the strength, touches no candidate path.
- **A distant WATCH (defer):** *if* the July-27 weights enable practical EU on-prem deployment once quantized variants + tooling mature (months out) **and** a strong eval/bias harness is built, revisit. Not now.

## The honest bottom line

For hireui's actual need — a **legible, auditable, low-hallucination, residency-safe** model on candidate paths — **Claude (Haiku 4.5 for Match-Explain, Sonnet 5 if more capability is needed) beats K3 on every axis that matters**, and Sonnet 5 sits in the **same price tier** ([[pricing-and-the-end-of-cheap-chinese-ai]]). K3's cheapness-vs-Opus is real but irrelevant when the blocking constraints are residency, fabrication, and legibility — not price. This mirrors [[../adaptive-engineering-beyond-harness/_index]]'s sharpest objection: *legibility collapse is reckless in regulated domains* — recruitment is one.

## N=3 update (Theo t3.gg pass) — the AVOID *strengthens*

The independent hands-on source sharpened three of the hard stops:

- **Fabrication (stop #2) is now more precisely bad for candidate use.** Theo praises K3's honesty via the composite AA-Omniscience *Index* (+18) — but that index rewards *refusing* ("I don't know"). The metric that governs a candidate-facing Match-Explain is the **raw fabrication rate, which rose to 51%**: a model that honestly refuses is useless for the task, and when it *does* answer it now invents *more* often. The favorable index does **not** rescue the use case. [[theo-benchmarks-and-the-hallucination-reconciliation]]
- **Residency (stop #1) — corrected in K3's favor on server location, worsened on data-use.** The international API is **MOONSHOT AI PTE. LTD. (Singapore)**, not literally Chinese servers — but the [privacy policy](https://platform.kimi.ai/docs/agreement/userprivacy) says **inputs *and* outputs may be used to train the models by default** (opt-out = negotiate an enterprise arrangement), with a Beijing parent. Candidate PII entering a training corpus is a *harder* stop than server geography. [[theo-cost-speed-and-how-to-use]]
- **A new (fourth) governance stop:** **no system/safety card at launch** + visibly relaxed offensive-use refusals = exactly the unauditable, un-governed vendor profile the ADR rules out. [[theo-security-safety-and-open-weight-risk]]

Net: a skeptical practitioner who *likes* the model still lands the recommendation exactly where the corpus did — **AVOID candidate-facing.**

## Corpus note (excluded confabulation)

The synthesis draft asserted "K3 covers 13 languages" — that is the **cc-sdd platform figure bleeding in from vault context**, not a verified K3 fact. **Excluded** per wiki-verify discipline; K3's language coverage was not independently confirmed here and no bilingual (VN/EN) hallucination data is public — itself a reason to distrust it for a VN-first product.

## Key Takeaways

- **AVOID candidate-facing** — 3 hard ADR stops (residency, fabrication, legibility) before cost matters.
- **Narrow legitimate use:** throwaway, non-candidate UI prototyping where its frontend strength lives.
- **Claude stays the answer** for hireui's regulated paths; Sonnet 5 is the honest same-tier price comparison, not Opus.
