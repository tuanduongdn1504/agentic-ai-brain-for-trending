# (C) Pilot methods — quanit-becoming-ai-engineer-2026

> **Source:** Quân IT, "Becoming An AI engineer in 2026" ([`RcF6ofU2nLs`](https://www.youtube.com/watch?v=RcF6ofU2nLs)). Wiki: `wiki/quanit-becoming-ai-engineer-2026/`.
> **Headline:** this talk is less a *new* technique and more a **deploy-now spur** — its Pillar 4 ("build the hard real thing; tutorials won't make you good") is a direct argument against the operator's current 8-pilots/0-deployed holding pattern. The single best action is to **start the hireui Match-Explain build**, sequenced by Quân's Pillars 3→4, inside the RATIFIED candidate-LLM legibility ADR.

## The one-move recommendation

**Ship Match-Explain Tier A this week (zero code).** Interview 3–5 recruiters + analyze ~30 recently-rejected matches → write 5 concrete failure modes + a "what "correct match" means" definition. This is Quân's "ask what's a headache" (Pillar 4) *and* the legibility ADR's "eval-gated" precondition (you can't gate on evals you haven't defined). It unblocks everything downstream and costs ~a day.

## A–D pilot menu (detail)

### Tier A — Know the problem (≈5–8 h, 1 wk) · Pillar 4
- Interview 3–5 internal recruiters: *"When does a match feel wrong? What did you reject last week and why?"*
- Pull ~30 rejected matches from the last 30 days; tag each with a failure category.
- **Deliverable:** `failure-modes.md` — 5 concrete modes (e.g. title-synonym miss, location radius wrong, skill present in CV but not parsed, seniority mismatch, domain-jargon miss) + a one-paragraph "definition of a correct match."
- **Gate:** this file *is* the eval spec Tier C scores against.

### Tier B — Deterministic foundation + guardrails (≈30–35 h, 2–3 wk) · Pillar 3
- **Ingestion:** normalize job titles, dedupe fields, and **mark PII zones** (name/email/phone/address) in a schema.
- **Baseline matcher:** keyword/skill-overlap scoring, **no LLM** — the floor to measure the AI against.
- **Guardrails ADR** (mirror into hireui's ADR log): the LLM sees cleaned skills/years/title **only**; never candidate PII. Every call audit-logged (input, output, recruiter feedback). Behind **I-8** recruiter-only permissions. Wire through the **Mosh A2 vendor seam**.
- **Also close the api-security gap:** add the **BOLA/authorization** check flagged as hireui's #1 risk (see `wiki/api-security-7-techniques`).

### Tier C — RAG + human-in-loop eval (≈35–40 h, 2–3 wk) · Pillars 2+3
- Index job postings + the company hiring policy as retrieval context (start simple — no vector DB needed at v1; long-context or keyword retrieval first, per the "stack is dated" caveat).
- Call **Haiku 4.5** on ~20–30 **sanitized** matches (PII stripped by Tier B).
- Recruiters label each output: *correct / good-reasoning-wrong-outcome / hallucinated-detail / missed-constraint.*
- **Metrics:** accuracy %, cost/match, p50/p95 latency. **War-story checkpoint:** which Tier-A assumption broke first?

### Tier D — Ship, measure, iterate (≈15–20 h, 1–2 wk) · Pillar 4
- Feature-flag Match-Explain (behind I-8), beta to 2–3 recruiters for a week.
- Measure adoption, monthly cost, recurring error patterns; write the war-story doc (what surprised you / what failed / what you'd change).

## What to take, what to skip (from the critical appraisal)

- **Take:** "domain knowledge + security + fundamentals > model sophistication"; deterministic-baseline-first; recruiters-as-verifiers; build-don't-research.
- **Skip / update:** don't treat Pillar 2's RAG/vector-DB stack as mandatory (long-context + caching may be enough at v1); don't adopt "you don't need internals" literally (keep failure-mode literacy — hallucination, token limits, drift).
- **Add (missing from the talk):** guardrails + observability + evals as first-class, because a hallucinating matcher affects a *cohort* of candidates, not one user — and this path is bias/fairness-sensitive.

## Non-hireui applications

- **Personal/skills:** run the "pick a project beyond your ability" heuristic on the operator's own harness work; the struggle-doc becomes portfolio/war-story material.
- **Scrum-coaching:** Quân's "ask what's a headache, don't pitch a solution" is a clean facilitation move for requirement discovery / retro framing.

## Rank

**HIGH — deploy spur, not a new tool.** Doesn't add a technique; it removes the excuse. Best paired with the already-ranked Mosh A2 seam + prompt-evaluation harness as the concrete first LLM feature. Recommended next action: **Tier A this week.**
