# (C) Kimi K3 — decision & pilot methods

> Deliverable for topic [[../wiki/kimi-k3-worlds-most-powerful-ai/_index]], compiled 2026-07-17.
> **Posture: WATCH / don't-adopt** (like [[../wiki/adaptive-engineering-beyond-harness/_index]] and [[../wiki/okf-open-knowledge-format/_index]]) — this is a knowledge/landscape topic, not a buildable pattern. The "pilot" here is a *decision gate*, not a build.

## Headline

**Do not put Kimi K3 on any hireui candidate-facing path. Full stop.** Three independent hard stops (residency, 51% hallucination, closed/unauditable) against the RATIFIED candidate-LLM legibility ADR — before price is even considered. Claude (Haiku 4.5 for Match-Explain; Sonnet 5 if more headroom is needed, same price tier) remains the answer. The only legitimate K3 use is **throwaway, non-candidate UI prototyping**, and even that is optional.

## Decision tiers

### Tier A — decide & document (this week, ~20 min, zero code)
- **A1. Record the AVOID.** Add a one-line ADR note to the hireui LLM decision log: *"Kimi K3 evaluated 2026-07-17 → AVOID for candidate paths (Chinese-hosted / EU AI Act Annex III; 51% hallucination; closed-source-unauditable at launch). Re-evaluate only if EU on-prem self-host becomes practical AND an eval/bias harness exists."* Closes the "is the cheap Chinese model an option?" question with a cited rationale so it doesn't get re-litigated.
- **A2. Correct the framing if it comes up.** If anyone cites this video as "we should switch to the cheaper, more powerful open model," the three facts to counter with: weights weren't even downloadable (hosted-only), it's a 5× price *increase* over K2.6 (same tier as Sonnet 5), and it's #3–4 overall / #9 on text — not "most powerful."

### Tier B — optional non-candidate spike (only if there's appetite; ~half a day)
- **B1. Frontend-prototyping spike.** K3's one real, verified strength is frontend/visual coding (#1 Frontend Arena). A **throwaway** Figma→React spike on the CandidateDetail refactor (noted 2026-06-20), or design variations for an internal admin UI — **no candidate data, nothing deployed**. Measure: does its output beat the current Claude workflow enough to justify a second vendor's API + ToS surface? Likely "no," but it's the only place K3's strength applies.
- **Guard:** keep it in a sandbox; never wire a Chinese-hosted API into a path that sees candidate PII, even in dev.

### Tier C — WATCH triggers (revisit only when ALL true)
- Full K3 (2.8T) weights actually shipped **and** quantized variants + `llama.cpp`/Ollama support mature enough for a realistic EU on-prem cluster;
- a recruitment-specific **eval/bias harness** exists to gate it;
- **and** a measured reason Claude can't do the job. Until then: no action. Natural revisit at a future landscape audit.

### Tier D — do NOT
- **D1.** Do not route candidate data through K3 (hosted or via OpenRouter resale — the "unofficial API key" ToS trap the corpus already learned).
- **D2.** Do not treat the July-27 open-weights promise as a residency fix — the hardware wall makes on-prem infeasible for months.
- **D3.** Do not repeat the video's numbers ("2,840 Elo writing," "beats Fable 5," "US restricted it") — several are false/unverifiable.

## The transferable lesson (worth more than the model)

This topic's real payload is a **reading protocol for benchmark-hype launch videos**, reusable on the next one:
1. **Specs are usually right; framing usually isn't.** Verify availability, competitive *ranking* (not cherry-picked boards), pricing *context* (vs its own predecessor, not just vs the most expensive rival), and any geopolitics — that's where these videos break.
2. **Search before believing *and* before dismissing** (discard-as-garble guard, both directions): the model was real (don't dismiss), but "open source now" was false (don't believe).
3. **First-party demos = capability ceiling, not reliability floor.** The number that predicts real use (hallucination 51%, agentic tool-calling) is the one the video omits.

## Cross-refs
[[../wiki/kimi-k3-worlds-most-powerful-ai/hireui-translation]] · [[../wiki/kimi-k3-worlds-most-powerful-ai/claims-scorecard]] · [[../wiki/adaptive-engineering-beyond-harness/_index]] (legibility-in-regulated-domains) · [[../wiki/mosh-ai-powered-apps/_index]] (the Claude vendor seam this would replace) · [[../wiki/miai-cv-matching-agent/_index]] (Match-Explain / Haiku 4.5)
