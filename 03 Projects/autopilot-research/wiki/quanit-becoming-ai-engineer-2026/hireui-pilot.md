# hireui pilot — Quân's 4 pillars → the Match-Explain build

> Turns the talk's advice into a concrete A–D path for hireui (TalentAxis recruitment SaaS, the operator's Goal-#2 target). hireui has **no LLM integration yet**; the planned first feature is **Match-Explain** (explain *why* a candidate matches a job). Full operator-facing methods: `output/(C) 2026-07-16-quanit-becoming-ai-engineer-2026-pilot-methods.md`.

## Why this talk is the right pilot spur

Quân's Pillar 4 is, in effect, an argument *against the operator's current holding pattern* (many pilots researched, zero deployed): **tutorials/research won't make you good — build the real thing.** His Pillars 2–3 (RAG over the company's messy data, domain knowledge as the verifier, guardrails/permissions) map almost 1:1 onto a legible Match-Explain feature. And crucially, this composes with the **RATIFIED hireui candidate-LLM legibility ADR**: any candidate-affecting LLM path must be fixed + legible + audited + human-in-loop + eval/bias-gated, behind the Mosh A2 seam. Quân's "domain knowledge verifies nondeterministic output" is exactly the mechanism that ADR needs — the recruiters are the domain experts who label correctness.

## The menu (A = lowest friction)

| Tier | Title | hireui action | Effort · pillar |
|------|-------|---------------|-----------------|
| **A** | Know the problem deeply | Interview 3–5 recruiters ("when do matches feel wrong? what got rejected last week?"); analyze ~30 recent rejected matches; write **5 concrete failure modes** (title mismatch, location, skill missing from CV parse…). **No code.** Defines what "correct match" means. | ~5–8 h / 1 wk · **P4** (recruiters = the "friend with a headache") |
| **B** | Deterministic foundation + guardrails | Build: (1) CV/job ingestion pipeline (normalize titles, dedupe fields, **mark PII zones**); (2) **deterministic baseline matcher** (keyword/skill overlap, *no LLM*); (3) a **guardrails ADR** — the LLM sees cleaned skills/years/title, **never name/phone/email**; add audit-log middleware (input, output, feedback logged). Behind **I-8** recruiter permissions. | ~30–35 h / 2–3 wk · **P3** (the 70% — system design, schema, security, permissions) |
| **C** | RAG + human-in-loop eval | Layer RAG (index job postings + company hiring policy as context). Run **Haiku 4.5** on ~20–30 **sanitized** matches. Recruiters label each: *correct / good-reasoning-wrong-outcome / hallucinated-detail / missed-constraint.* Measure accuracy %, cost/match, latency. War-story checkpoint: which assumptions broke? | ~35–40 h / 2–3 wk · **P2+P3** (RAG supplies domain data; domain knowledge verifies output) |
| **D** | Ship, measure, iterate | Feature-flag Match-Explain in the UI (behind I-8), beta to 2–3 recruiters for a week. Measure adoption, cost/month, error patterns. Document what surprised you / what failed. Iterate. | ~15–20 h / 1–2 wk · **P4** (ship real code, collect war-stories, no vaporware) |

## How this differs from prior pilot menus

- It is **build-sequenced, not idea-sequenced** — A establishes ground truth (labeled failure modes) *before* any model call, which is both Quân's "know the problem" and the legibility ADR's "eval-gated."
- Tier B's **deterministic baseline before the LLM** is the disciplined move Quân's Pillar 3 implies and the ADR requires: you need a non-AI floor to measure the AI against.
- It deliberately reuses, not replaces, prior threads: the **Mosh A2 vendor-seam** ([[mosh-ai-powered-apps/_index]]) is the boundary the LLM lives behind; **prompt-evaluation** ([[prompt-evaluation/_index]]) supplies the eval harness; **api-security-7-techniques** ([[api-security-7-techniques/_index]]) supplies the guardrail checklist (esp. the BOLA/authorization gap that is hireui's #1 risk).

## Cross-domain note

hireui is the **employer/recruiter side**; the candidate-side inverse is covered by [[external|Storm Bear: career-ops]]. The Match-Explain scoring rubric and the candidate-side rubric should stay mirror-images so explanations are consistent from both sides.

## Key Takeaways

- **The pilot's spine is Quân's Pillars 3→4:** do the 70% engineering (ingestion, deterministic baseline, permissions, audit log) *first*, then add the AI thinly and measure it against a labeled ground truth.
- **Guardrails are Tier B, not an afterthought** — PII never reaches the model; every call is audited; behind I-8. This satisfies the candidate-LLM legibility ADR by construction.
- **This is a deploy-now argument, not another research thread** — the talk's whole point is that shipping the hard, real thing is the education.
