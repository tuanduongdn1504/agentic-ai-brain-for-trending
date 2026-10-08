# Relevance — interview prep + a ready-made screening rubric

The operator submitted this to **prepare knowledge for interviews**. It pays off two ways, plus a product tie-in for TalentAxis/hireui.

## 1. As the interviewee (the stated goal)

Use [[study-guide-and-gaps]] as a **spaced-repetition deck**: five questions that broke a real candidate, each with a 30-second model answer and a drill. Then the six topic articles for depth. The meta-lesson matters as much as the facts:

- **Reason out loud when unsure** — the interviewer explicitly credited *"I'm not sure, but here's how I'd think about it"* over silence.
- **Know the working reason, not just the definition** — he *rejected* the memorized DI answer ("swap A for B") and rewarded the practitioner's answer (testability), and *deflated* over-researched trivia (CommonJS-vs-ESM perf). Depth is "why is this used day-to-day," not recall.

## 2. As the interviewer (a screening rubric)

TalentAxis is a recruitment company; this transcript is effectively a **calibrated backend/Node.js intern-to-junior screening script** by a working senior engineer. It gives you:

- A **difficulty-ramped question bank** (fundamentals → internals → a design/reasoning centerpiece) — see the escalation arc in [[overview]].
- **Model answers + the common wrong/inverted answers** to grade against — every article ends with an "Interviewer red flags (what to avoid saying)" section.
- **Signal-rich questions** that separate levels: DI (can they articulate DI vs Dependency Inversion vs Container?), single-thread non-blocking I/O (do they have the libuv mental model?), and unit testing (have they actually done it, or just Postman?).
- A **soft-skill rubric**: does the candidate reason under uncertainty and ask clarifying questions?

## 3. The portable handoff (for another agent)

A self-contained **interview-coach brief** for another agent lives at `output/(C) 2026-07-31-nodejs-interview-coach-handoff.md`. Drop it into any agent's context (or adapt it into a `SKILL.md` / `AGENTS.md`) and it will run a **mock backend/Node interview**: ask escalating questions, grade against the model answers, probe Socratically like this interviewer, and drill the five known gap areas. It carries its own provenance + the one correction (GraphQL history) so a downstream agent doesn't re-teach the interviewer's mistake.

## 4. hireui product tie-in (the honest, narrow version)

If hireui ever offers **candidate-facing technical screening**, this topic is a concrete example of what a *good* screen looks like — and a reminder of the guardrails. Per the operator's **RATIFIED candidate-LLM legibility ADR** ([[external|Storm Bear: hireui candidate-LLM legibility ADR]]):

- A question bank + model-answer rubric like this is **deterministic, legible, and auditable** — the ADR-safe way to assist screening. Ship it as a **fixed rubric an LLM grades against with a visible reason**, human-in-the-loop, never as emergent LLM judgment of a candidate.
- The interviewer's own instinct is the ADR in miniature: he **explains every correction** and never scores on an opaque gut-feel — "explain it or don't ship it."
- ⚠️ **Do not** let an LLM free-form "interview" or score real candidates unaudited (EU AI Act Annex III: recruitment = high-risk). The coach handoff is for **the operator's own practice / for interviewing prep**, not for scoring live candidates.

## Cross-links

- [[miai-cv-matching-agent/_index]] — the recruitment-domain sibling (candidate↔job matching; the Match-Explain rubric shares the "legible reason" discipline).
- [[api-types/_index]] · [[data-structures-16-in-32-min/_index]] — the CS/API-fundamentals this interview probes.
- [[pocock-software-fundamentals/_index]] · [[quanit-becoming-ai-engineer-2026/_index]] — "fundamentals matter more than ever," the thread this interview lives on.
- [[hoidanit-fullstack-vibe-coding/_index]] · [[aws-email-at-scale-sqs-lambda-ses/_index]] — VN-language backend-engineering siblings.
