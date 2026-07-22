# API Types — REST, SOAP, GraphQL, gRPC, WebSocket, Webhook

**A beginner-to-intermediate map of the main API architecture styles / communication patterns — each with its mechanism, trade-offs, and the "which one when" decision — compiled from a 6-video bundle and verified claim-by-claim against authoritative docs (RFCs, official gRPC/GraphQL/W3C specs, MDN).**

- **Source:** 6-video bundle, anchored on [7 Loại API Bạn Phải Biết](https://www.youtube.com/watch?v=RsgyCswZBGA) · LetDiv (VN) · 2026-07-17 · 12:38 — + Codist, ByteByteGo, Ulbi TV, Be A Better Dev, Learn with Whiteboard. Full list in [[source-provenance]].
- **Ingested:** 2026-07-21 (Path 1 `/loop`; drain → NotebookLM `ed17cc3d…`) · raw: `raw/2026-07-21-api-types-explained-rest-soap-graphql-grpc-websock.md`
- **Verification:** Workflow `wf_640f115f-0a8` (25 agents, 0 errors) → **5 CONFIRMED / 7 CORRECT-BUT-INCOMPLETE / 0 MISLEADING / 0 FALSE** — technically honest sources; every correction is a beginner over-generalization refined. See [[claims-scorecard]].
- **Corpus first:** the wiki's **first API-architecture-styles / API-types-taxonomy topic** (distinct from [[api-security-7-techniques/_index]] = OWASP security, and [[claude-api-cost-optimization/_index]] = Claude API pricing; collision-checked CONFIRMED).

## The one framing

**An "API type" is a contract (what data, how shaped) + a transport/interaction pattern (how it moves).** No type wins absolutely — you choose by workload: security, speed, real-time latency, client flexibility, bandwidth, infrastructure. REST is the flexible default; binary protocols (gRPC) trade legibility for speed; GraphQL moves data-shaping to the client (with real caching/DoS costs); real-time needs persistent or event-driven connections (WebSocket/Webhook/WebRTC), not polling.

## Articles

### Concepts
- [[overview]] — the one framing, the 8-type taxonomy table, and the recurring cross-source theses.
- [[selection-framework]] — the payoff: a workload → API-type decision guide ("no type wins absolutely").
- [[http-semantics-and-rest-conventions]] — HTTP methods/CRUD, PUT vs PATCH, idempotency (nuanced), statelessness, versioning, OpenAPI/Swagger.

### The types
- [[rest-and-web-api]] — REST as the flexible default (stateless, resources, JSON/HTTP) + the "Web API" umbrella-term disagreement.
- [[soap]] — formal XML/WSDL/WS-Security protocol; a **legacy operational incumbent** in banking, not the modern choice.
- [[graphql]] — client-defined queries solve over/underfetching, but bring caching complexity + query-DoS risk (the ByteByteGo cautions).
- [[grpc-and-rpc]] — the RPC family: gRPC (binary Protobuf + HTTP/2) with the honest "7–10× faster" scoping, plus tRPC (TypeScript-only).
- [[websocket-and-realtime]] — WebSockets (persistent full-duplex), WebRTC (P2P + signaling/TURN reality), and the polling-vs-push debate resolved by scope.
- [[webhook]] — the "reverse API": server POSTs to your callback URL on an event; the inverse of polling.

### Appraisal
- [[beyond-the-video]] — the production layer the beginner videos skip: OAuth2/JWT, API gateways, observability, resilience, contract testing.
- [[critical-appraisal]] — how much to trust this source set (a solid on-ramp, not an implementation guide).
- [[claims-scorecard]] — the 12-verdict refute-first table.
- [[caveats-and-corrections]] — every correction applied at compile (magnitudes, framing, source disagreements).
- [[hireui-relevance]] — API-type choices for hireui (REST+OpenAPI over GraphQL; webhooks for integrations; the legible-contract angle for the candidate-LLM ADR).
- [[source-provenance]] — the 6 sources, ingestion, and verification trail.

## Cross-links (corpus)

- [[api-security-7-techniques/_index]] — securing any of these APIs (OWASP/BOLA, the auth layer [[beyond-the-video]] points to)
- [[aws-email-at-scale-sqs-lambda-ses/_index]] — webhooks + SNS event delivery + queues in a real pipeline
- [[claude-api-cost-optimization/_index]] — a concrete REST/LLM API surface
- [[data-structures-16-in-32-min/_index]] — sibling CS-fundamentals "N types, choose by workload" survey
- [[miai-cv-matching-agent/_index]] — recruitment domain; calling job-board APIs
- [[mosh-ai-powered-apps/_index]] — hireui's LLM vendor seam
