# (C) PROPOSED ADR — Candidate-Facing LLM Paths Stay Fixed, Legible, and Audited

> **✅ RATIFIED by the operator on 2026-07-15 as a standing, forward-looking policy.**
> This is the operator's adopted decision governing **all FUTURE candidate-impacting LLM work in hireui**. Because hireui has **no LLM code yet**, there is nothing to attach it to today — it binds the work *when it begins*. **Mirror it into hireui's own ADR log** — per hireui's constitution (**I-2 `agent-*` branch, GitNexus-first, hireui's ADR path/format**) — **when the first candidate-impacting LLM feature starts** (expected: Match-Explain). Until then, this vault copy is the ratified policy of record. See "How to land this" at the bottom.

---

- **ADR:** hireui-adr-NNNN (assign next number in hireui's ADR sequence)
- **Title:** Candidate-facing LLM paths stay fixed, legible, and audited
- **Status:** **Accepted** — ratified by the operator 2026-07-15 (standing forward-looking policy; hireui-ADR-log mirror pending the first candidate-impacting LLM feature)
- **Date:** 2026-07-15 (ratified same day)
- **Deciders:** Storm Bear (operator)
- **Trigger:** [[../wiki/adaptive-engineering-beyond-harness/failure-modes]] — the strongest objection to "adaptive engineering" (emergent, self-organizing multi-agent harnesses) is that **legibility collapse is unacceptable in regulated domains — recruiting, finance, medicine.** hireui *is* a recruiting product. This ADR turns that objection into a standing design rule **before** the first LLM feature ships.

## Context

- **hireui has no LLM integration in product code yet** (verified 2026-06-15). So this is a **build-it-right, preventive** decision, not a retrofit — the cheapest possible time to set the rule.
- The **first planned LLM feature is Match-Explain** (CV↔job matching + explanation: Haiku structured outputs, no-vector-DB v1, behind the Mosh A2 vendor seam, gated by recruiter-labeled evals).
- hireui's domain — **automated evaluation/ranking/filtering of job candidates** — is a **high-risk AI use case under the EU AI Act (Annex III, employment/worker-management)**, which carries obligations around **transparency, human oversight, logging/traceability, accuracy, and record-keeping**. *(High-risk obligations are phasing in ~2026–2027; confirm the current effective dates before relying on specifics. Similar transparency/anti-discrimination expectations exist under GDPR Art. 22 automated-decision rules and various local hiring laws, e.g. NYC LL144.)*
- The industry frontier (per the "Beyond the Harness" talk) is drifting toward **emergent, adaptive, self-organizing multi-agent orchestration** where the "harness" is not specified in advance. That is **explicitly out of scope** for anything that affects a candidate's outcome here.
- The talk's own author is a physician — the domain least tolerant of "the agents self-organized." Recruiting sits in the same bucket.

## Decision

**Any LLM-driven path that influences a candidate's outcome — Match-Explain, ranking/scoring, shortlisting, screening, auto-rejection, or ordering candidates for a recruiter — MUST be built as a *fixed, legible, audited* harness. Emergent / adaptive / self-organizing multi-agent orchestration is prohibited on candidate-impacting paths.**

Concretely, a candidate-impacting LLM path must satisfy all of:

1. **Fixed harness** — the prompt, model, tools, and control flow are specified before runtime and version-controlled. No runtime self-reorganization; no "let the harness emerge." (A single model call with structured output is the *preferred* shape; a deterministic, spec-driven multi-step pipeline is allowed. A self-directed agent swarm is not.)
2. **Legible output** — every candidate-affecting result is **traceable to its inputs**: which fields/evidence drove the score, the rubric applied, the model + prompt version. Scores/rankings are **explainable to the recruiter and, on request, to the candidate.** No unexplained black-box ordering.
3. **Human in the loop** — the LLM **advises**; a human recruiter makes or can override the decision. No fully-automated rejection/shortlisting without a human checkpoint.
4. **Audited** — each candidate-impacting inference **logs a durable record** (input hash, model+prompt version, rubric version, output, timestamp, and the reviewing user) sufficient to reconstruct and defend the decision. Logs are retained per policy.
5. **Evaluated** — the path is gated by **recruiter-labeled evals** (accuracy + adverse-impact/bias checks) before rollout and re-run on prompt/model changes.
6. **Isolated behind the vendor seam** — candidate-impacting LLM calls go through the **Mosh A2 vendor seam**, so the model is swappable and the boundary is the natural place to attach logging + eval hooks.

## Scope

- **In scope (rule applies):** Match-Explain, candidate scoring/ranking/matching, shortlisting, screening, auto-communications that gate progression.
- **Out of scope (rule does not restrict):** internal developer tooling (Claude Code, cc-sdd, the autopilot vault), non-candidate content generation (e.g. job-description drafting a recruiter edits), and other non-candidate-impacting internal features — though legibility/logging remain good practice there too.

## Consequences

**Positive**
- Regulatory posture aligned with EU AI Act high-risk expectations **from day one** (transparency, human oversight, logging) — far cheaper than retrofitting after launch.
- Composes with existing threads: the **api-security BOLA/authorization** work (a candidate must only ever see decisions about themselves), the **residency** posture (candidate PII), and the **recruiter-labeled evals** plan.
- Makes Match-Explain's design decision trivial: it's a **single structured-output call with an explanation field + a logged rubric**, not an agentic system. Removes a whole class of over-engineering.

**Negative / costs**
- Rules out (for candidate paths) the "let agents self-organize" approaches that may become fashionable; accepts being deliberately behind that frontier here. *(This is the intended trade — see [[../wiki/adaptive-engineering-beyond-harness/vs-harness-engineering-corpus]]: the corpus evidence favors deliberate harnesses anyway.)*
- Adds logging + human-checkpoint + eval overhead to every candidate-impacting feature. Accepted as the cost of operating in a regulated domain.

**Neutral**
- Does not prescribe the model or exact rubric — only the *shape* (fixed/legible/audited) of the harness.

## Alternatives considered

1. **No policy (decide per-feature).** Rejected — the cheapest time to set this is *before* the first LLM feature; ad-hoc decisions risk an opaque scorer shipping and becoming load-bearing.
2. **Adaptive/emergent multi-agent orchestration for matching.** Rejected for candidate paths — legibility collapse + no working implementation + regulatory exposure ([[../wiki/adaptive-engineering-beyond-harness/failure-modes]]).
3. **Black-box embedding-similarity ranking with no explanation.** Rejected — fails legibility/human-oversight; hard to defend under high-risk AI obligations and bias scrutiny.

## Implementation notes (non-binding)

- Attach a `decision_log` write at the vendor seam (input hash + model/prompt/rubric versions + output + reviewer + ts).
- Match-Explain v1: one Haiku structured-output call returning `{score, per_criterion_evidence[], rationale, rubric_version}`; recruiter UI shows the rationale; recruiter confirms/overrides.
- Wire the recruiter-labeled eval set as a pre-merge gate on the seam (composes with the prompt-evaluation thread's harness).

## How to land this in hireui (per hireui's constitution)

1. Branch: `agent-adr-candidate-llm-legibility` (I-2 `agent-*` naming).
2. GitNexus-first: locate hireui's existing ADR directory + numbering + template; renumber this to fit.
3. Reformat to hireui's ADR template if it differs from this MADR-ish layout.
4. Open a PR to **mirror this already-ratified decision** into hireui's ADR log (the operator ratified it 2026-07-15; the PR records it in-repo, it is not re-litigated).
5. Cross-reference the api-security posture doc + the Match-Explain / Mosh-seam / evals specs.

## Open questions

- Exact EU AI Act high-risk effective dates + whether hireui's EU footprint triggers them now vs. later — **confirm before relying** on the regulatory framing.
- Retention period + access controls for the decision log (ties to the residency ADR).
- Whether candidate-facing *explanations* are shown proactively or on-request (product decision).

## Key takeaway

This ADR is the "Beyond the Harness" talk's own best objection, inverted into a hireui guard-rail: **on any path that affects a candidate, stay fixed, legible, and audited — decide it now, before the first LLM feature ships.**
