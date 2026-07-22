# Claims Scorecard — api-types

**How to read this:** every load-bearing / checkable claim extracted from the 6-video bundle was handed to an independent, refute-first fact-checker (WebSearch-grounded, told to try to *disprove* it). Verdicts drive the corrections in [[caveats-and-corrections]] and the nuances baked into each article.

- **Verification run:** Workflow `wf_640f115f-0a8` — 25 agents (11 claim verifiers + 1 corpus-collision check + 12 article drafters + 1 completeness critic), **0 errors / 0 empty / 0 skipped**, ~1.28M tokens, 158 tool calls, ~5.2 min. All agents ran Haiku 4.5 (disclosed).
- **Tally (12 verdicts):** **5 CONFIRMED · 7 CORRECT-BUT-INCOMPLETE · 0 MISLEADING · 0 FALSE · 0 UNVERIFIABLE.**
- **Profile:** technically honest source set. Nothing is fabricated or false; the failure mode is **beginner oversimplification** — blanket magnitudes ("7–10× faster") and dated framing ("SOAP for banks") that a refute-first check turns into "correct, with important context."

## Scorecard

| # | Claim (short) | Verdict | Confidence | Correction / nuance |
|---|---|---|---|---|
| C1 | gRPC+Protobuf is 7–10× faster than REST+JSON | **CORRECT-BUT-INCOMPLETE** | high | True *for large payloads + high throughput (100+ RPS)*. REST is faster for small payloads; vs HTTP/2 + binary REST the gap shrinks to **10–25%**. Assumes HTTP/1.1+JSON on the REST side. See [[grpc-and-rpc]]. |
| C2 | GraphQL is harder to cache (POST bypasses GET/CDN caching) | **CORRECT-BUT-INCOMPLETE** | high | Core fact right (POST isn't URL-cacheable), but "harder" misleads: queries *can* use GET, and **persisted queries / APQ** enable full CDN caching. It's **different, not harder**. See [[graphql]]. |
| C3 | GraphQL client-defined queries risk DB DoS (table scans) | **CONFIRMED** | high | Real, documented (Apollo/Imperva/Escape). Mitigate with **depth limiting + query-cost analysis** (composable, both needed). See [[graphql]]. |
| C4 | SOAP is still the preferred/standard choice for banking & fintech | **CORRECT-BUT-INCOMPLETE** | high | SOAP is a **legacy operational incumbent**, not preferred for *new* systems in 2026. Greenfield banking/fintech = REST, FAPI 2.0, ISO 20022. Persists via sunk cost, not active preference. See [[soap]]. |
| C5 | REST+polling for real-time is an anti-pattern; use WebSockets | **CORRECT-BUT-INCOMPLETE** | high | WebSockets are the default for **synchronous** real-time (chat); polling is *not* universally an anti-pattern — fine for **low-frequency async** updates / as a fallback. Resolves the source disagreement by scope. See [[websocket-and-realtime]]. |
| C6 | A webhook is a "reverse API" (server POSTs to a callback URL on event) | **CONFIRMED** | high | Standard industry definition (Red Hat/Twilio/Stytch). POST is near-universal; add HMAC signature verification + retries in production. See [[webhook]]. |
| C7 | gRPC runs over HTTP/2 → multiplexing + bidirectional streaming | **CONFIRMED** | high | Correct (gRPC PROTOCOL-HTTP2.md, RFC 7540). Concurrency bounded by `SETTINGS_MAX_CONCURRENT_STREAMS` + flow control. See [[grpc-and-rpc]]. |
| C8 | tRPC = type-safe RPC for TS without schema/codegen | **CORRECT-BUT-INCOMPLETE** | high | Accurate, but **TypeScript-only on both ends** — not a language-agnostic wire protocol like gRPC. Non-TS clients defeat its value. See [[grpc-and-rpc]]. |
| C9 | GET/PUT/DELETE idempotent, POST not; PUT replaces, PATCH partial | **CORRECT-BUT-INCOMPLETE** | high | Spec-correct (RFC 7231/5789), but idempotent ≠ identical response (DELETE → 204 then 404). Guarantees **server state**, not status code. See [[http-semantics-and-rest-conventions]]. |
| C10 | WebRTC enables peer-to-peer browser audio/video/data | **CORRECT-BUT-INCOMPLETE** | high | "P2P" is the design intent; in practice needs a **signaling server** + usually **STUN/TURN** for NAT traversal, often relaying. See [[websocket-and-realtime]]. |
| C11 | Over/underfetching are recognized REST weaknesses GraphQL addresses | **CONFIRMED** | high | Correct (AWS AppSync / howtographql / O'Reilly). Design-intent claim solid; full resolution may need Relay/patterns. See [[graphql]], [[rest-and-web-api]]. |
| — | **Corpus:** api-types is a corpus-first API-architecture-styles topic; no collision | **CONFIRMED** | high | Grep over 70 topics: only 3 incidental REST/GraphQL mentions; `api-security-7-techniques` (OWASP) and `claude-api-cost-optimization` (pricing) are different subjects. Genuinely new. |

## Bottom line

The bundle is a **trustworthy conceptual on-ramp** — every definition checks out. But it hand-waves magnitudes and currency, and two sources openly contradict each other on REST-for-realtime. Read [[caveats-and-corrections]] before quoting any number, and [[critical-appraisal]] for the source-quality read.

## Key Takeaways

- 12 verdicts: **5 CONFIRMED / 7 CORRECT-BUT-INCOMPLETE / 0 MISLEADING / 0 FALSE** — no fabrication, no outright errors.
- Every CBI is an *over-generalization*, not a mistake: right claim, missing the "it depends" (payload size, caching strategy, sync vs async, TS-only, greenfield vs legacy).
- The single most-corrected claim is the gRPC "7–10× faster" magnitude (C1) — the topic's headline caveat.
- Corpus-collision check CONFIRMED: this is genuinely new knowledge, not overlapping `api-security-7-techniques` or `claude-api-cost-optimization`.
