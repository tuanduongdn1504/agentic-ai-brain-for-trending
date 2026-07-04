# Harness economics + the subscription/ToS timeline (April–July 2026)

> Companion to [[archon-harness-builder-anchor]]. The video's most consequential *practical* claims are economic (per-node model routing, subscription-vs-API) and legal (can a harness run on your Claude subscription?). Both moved AFTER the video — this article pins the timeline as of 2026-07-04.

## Source

Video srx9iwnjK2M Q&A segments + refute-first verifiers (`wf_8a0f2da5-1d0`: subscription-tos, rate-limits, advisor-postvideo) + main-loop fetch of support.claude.com article #15036540 (2026-07-04).

## The ToS timeline (Rule-7 conflict surfaced, not averaged)

| Date | Event |
|---|---|
| ≤2026-03 | De-facto: Agent SDK apps on subscription auth work; Rasmus on stream: "used it every day since November, no bans" |
| 2026-04-03 | **Boris Cherny X post announces the RESTRICTION**: "Starting tomorrow at 12pm PT, Claude subscriptions will no longer cover usage on third-party tools like OpenClaw…" |
| 2026-04-04 | Restriction live; OpenClaw/OpenCode subscription use cut off |
| 2026-04-05 | OpenClaw creator Peter Steinberger's account suspended ("suspicious activity") — reversed within hours after outcry |
| ~2026-04 | Anthropic **reinstates** third-party agent usage "with a catch" (VentureBeat) |
| 2026-04-11 | **The video.** Cole: "Boris made it super clear — you can use your subscription for personal use with the Agent SDK." |
| ~2026-05/06 | Planned formalization: per-plan **Agent SDK monthly credits** (Pro $20 / Max-5x $100 / Max-20x $200), slated 2026-06-15 |
| 2026-07-04 (fetch) | **Credits plan PAUSED.** Support article #15036540: *"We're pausing the changes… For now, nothing has changed: Claude Agent SDK, `claude -p`, and third-party app usage still draw from your subscription's usage limits."* |

**Assessment of the video's claim:** PARTIAL. Direction right for the *current* state (Agent SDK usage draws from subscription limits = permitted), but "Boris made it very clear" mis-cites the author of the restriction as the author of the blessing, and the legal-and-compliance page has (at times) flatly said OAuth-token reuse in the Agent SDK "is not permitted" — the docs conflicted with each other during this window. **Serving OTHER users through your subscription remains clearly prohibited** (per-user credits, "do not ship multi-user apps on plan auth") — which is exactly the line Cole drew on stream (self-hosted personal Archon OK, deployed multi-user not). **Pilot rule: re-check #15036540 the week of any Archon deployment; policy has flipped 3× in 3 months.** Archon v0.5.0's per-user credential vault + PKCE flows is the project tracking this same instability.

## Rate limits (context for the harness-economics pitch)

- **CONFIRMED:** 2026-03-26 Anthropic added peak-hour throttling (5-hour budget drains faster weekdays 5–11am PT) — the "worse rate limits" backdrop of the stream.
- **CORRECTED framing:** the "off-peak special" was the **"Claude 2x" promotion 2026-03-13→27** (2× usage limits off-peak, bonus exempt from weekly caps), which had just ended — it granted 2× capacity, not "2× lower consumption."
- **CONFIRMED:** dual-layer limits (5-hour window + weekly cap) — the video's live readings (37% of 5h during 4 parallel workflows + PRD + GSD build; 32% weekly the day after reset) are a useful real-world datapoint: **a comprehensive multi-node harness run ≈ single-digit % of a Max 5-hour budget.**
- **CORRECTED:** "$200 = 4× the $100 plan, 20× the $20 plan" — right multipliers, subtly wrong basis: Max-20x = 20× *Pro*; Max-5x = 5× *Pro*; so 20x = 4× the 5x plan's multiplier.
- Post-video easing (NOT in the video): 2026-05-06 doubled 5-hour limits + removed peak-hour throttling; 2026-05-13 weekly limits +50% through 07-13. The agent-memory-architecture pin ("50% off-peak discount," workshop-spoken) did **not** match any written mechanism here — likely conflation with the May-13 weekly +50%; that pin stays workshop-spoken-only.

## The economics thesis (what survives verification)

- **Per-node model routing is the harness-native cost lever:** shipped defaults use haiku-class for classification, mid-tier for planning/review, top-tier only for implementation. Cole's stronger claim — "Archon+Sonnet beats Opus-alone Claude Code" — is self-reported, uncorroborated; treat like Lopopolo claim #4.
- **Anthropic now ships the same idea as a product feature:** the **advisor tool** (CONFIRMED — Claude Code v2.1.98+, beta API 2026-04-09; blog "The Advisor Strategy"): executor Sonnet/Haiku consults Opus on demand. Vendor evals: Sonnet+Opus-advisor +2.7pts SWE-bench-Multilingual at −11.9% cost; **Haiku 4.5 + Opus 4.6 advisor: 19.7%→41.2% at 85% less cost than Sonnet** (vendor-reported). The video mentioned advisor mode as something to build INTO Archon — it's real and orthogonal: per-node routing (harness layer) + advisor (model layer) compose.
- **Vendor-swap for routine loads:** Archon's own maintainer `-minimax` variants (MiniMax M2.7, real, 2026-05-26, Anthropic-compatible endpoint) = downgrade the *vendor*, not just the tier, for repetitive aggregation. Third rung of the cost ladder.
- Cross-check with [[external|claude-api-cost-optimization/_index]]: cache-read ≈0.1×, batch 50% — a harness that re-enters fresh contexts per node forfeits cache warmth; Archon's `persist_session` (v0.5.0) is the knob that trades bias-avoidance against cache economics. Nobody in this corpus has measured that trade yet → added to [[research-roadmap]].

## Key Takeaways

- Treat harness legality as **configuration, not doctrine**: 3 policy flips in 3 months; single-user self-hosted Agent-SDK use currently draws from subscription limits and is sanctioned; multi-user on plan auth is not.
- The cost ladder a harness gives you, in order of leverage: **deterministic nodes (0 tokens) → per-node tier routing → advisor pairing → vendor swap for routine loads → session persistence vs fresh-context (unmeasured trade)**.
- The video's live rate-limit readings are the best public datapoint yet that comprehensive harness runs are cheaper than they look — but they're one operator, one week, pre-May-easing.

## Cross-links

[[archon-harness-builder-anchor]] · [[archon-default-workflows-and-dogfood]] · [[external|claude-api-cost-optimization/_index]] · [[external|claude-code-observability/_index]] (measure before believing Sonnet+harness ≥ Opus) · [[external|agent-memory-architecture/_index]] (off-peak pin resolution)
