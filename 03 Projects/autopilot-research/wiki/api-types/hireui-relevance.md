# Hireui Relevance

**Source:** [[overview]] + [[rest-and-web-api]] + [[graphql]] + [[grpc-and-rpc]] + [[websocket-and-realtime]] + [[webhook]] + [[selection-framework]]

hireui is a recruitment SaaS product with a regulated compliance surface (EU AI Act Annex III). API type choices directly affect:

1. **Candidate data legibility** — the product's capacity to audit and verify what data flows where
2. **Integration surface** — how the platform talks to ATS systems, job boards, and email infrastructure
3. **Real-time requirements** — whether recruiter notifications / live job matching demand persistent connections
4. **Cost + caching discipline** — GraphQL's cache-evading POST requests vs REST's cacheable GET (especially relevant for price-per-API-call vendor seams)

## The one framing

**"What API surface lets us build a regulated, auditable product?"**

The answer is: **strict REST boundaries with typed contract (OpenAPI), not flexible GraphQL**. Not because GraphQL is wrong, but because the regulatory requirement (candidate-LLM legibility ADR) demands legible, fixed API contracts.

## hireui's API surface (external)

### REST + OpenAPI — the core choice

- **Candidate-facing** (search, filtering): REST GET endpoints with **typed query parameters** documented in OpenAPI schema
  - Fixed contract ≠ client-defined query complexity
  - Caching is predictable (all GET, all cacheable)
  - Regulatory audit trail: every field returned is in the schema, human-readable
  
- **Recruiter-facing** (create job, match candidates): REST POST/PUT with strict request/response bodies
  - No risk of nested GraphQL queries triggering database table scans (verdict C3: GraphQL's "unexpected table scan" risk is real and documented)
  - Payload size is bounded and predictable

### NOT GraphQL for the public API

Tempting for the candidate/job **graph** (candidate skills → job requirements ↔ candidate history ↔ job salary range), but:

1. **Caching complexity** (verdict C2, corrected): GraphQL uses POST by default, which HTTP/CDN caches do not handle. Persisted queries + APQ solve this, but add operational burden. For a small SaaS, the ROI is negative.
2. **Database security risk** (verdict C3): A candidate submitting a deeply nested query (`candidate.jobs[].matches[].company.history[].team.members`) could trigger a full-table scan. Rate limiting + query depth limits are essential mitigations, but are *additional friction* on an already-complex schema.
3. **Regulatory visibility**: A GraphQL introspection query reveals the entire schema. For a product handling PII (resumes, hiring decisions), exposing that schema to the internet is a security smell.

**Decision: offer a public REST API, internal GraphQL optional later (if we scale to 50+ microservices).**

## Webhook integrations (primary)

hireui talks to external systems via **webhooks** (reverse APIs), not by polling.

### Job board integrations (e.g., LinkedIn, Upwork, Indeed)

- **Inbound**: Job board POST→hireui when a candidate applies or a job status changes
  - Webhook receiver @ `POST /webhooks/job-board/<job_board_id>`
  - Signed with HMAC (vendor standard; e.g., Stripe-style `X-Signature` header)
  - Endpoint returns 2XX immediately, enqueues processing asynchronously (don't block the job board's retry logic)

### ATS integrations (e.g., Workable, Greenhouse, Lever)

- **Bidirectional**: hireui syncs candidates / hiring stage / offers to the ATS
  - Inbound: ATS webhook → hireui when a stage changes
  - Outbound: hireui calls ATS REST API to POST new candidate / update status (this is traditional REST, not a webhook)

### Email infrastructure (aws-email-at-scale)

- **SNS bounce/complaint events** (link: [[aws-email-at-scale-sqs-lambda-ses/_index]])
  - Email delivery failures (bounces, complaints, unsubscribes) trigger SNS messages
  - hireui webhook receiver ingests them asynchronously via SQS→Lambda→hireui
  - Critical for candidate inbox deliverability (do not ignore bounce events or SES will suspend your account)

**Webhook discipline:**

- Every webhook signature must be verified (HMAC-SHA256 standard)
- Every webhook receiver must be idempotent (vendor may retry; use a request ID deduplication key)
- Exponential backoff on failures (vendor expects the endpoint to be flaky)

## Real-time requirements (WebSocket vs polling)

### Recruiter notifications (job match, new application, offer acceptance)

**Current hireui use case:** recruiter refreshes the job list manually every N seconds.

**Future evolution:** real-time notification when a new matching candidate appears.

- **WebSocket is correct** (verdict C5, corrected): polling is inefficient; WebSockets eliminate ~80% of overhead vs polling (per RFC 6455 design motivation) and deliver sub-second latency. **However**, polling remains viable if acceptable latency is > 5 seconds and implementation simplicity matters more than efficiency.
- **Decision**: Start with polling (simpler), escalate to WebSocket when recruiter pain (candidates lost to delay) exceeds engineering cost.

### Candidate real-time search results

**Non-requirement for v1.** If hireui's candidate index is large (100K+), real-time search result streaming MAY become desirable. Remains REST + pagination for now.

## Internal microservices (gRPC only if you scale)

hireui is **monolithic** initially (single web server + database). **Do not adopt gRPC yet.**

- **Trigger**: when internal service A calls service B >100 times/second OR payload sizes >10 MB
- gRPC + Protocol Buffers are 7-10× faster than REST + JSON for large payloads (verdict C1, corrected: advantage is payload-dependent; gRPC wins at >10 MB, REST wins at <1 KB)
- Cost: significant operational complexity (service discovery, load balancing, gRPC gateways for browser clients)
- **Verdict**: Monolith → monolith + 1-2 services (e.g., embeddings sidecar) → gRPC when service mesh becomes necessary

## API contracts + regulatory legibility

The [[external|Storm Bear: hireui candidate-LLM legibility ADR]] (ratified) mandates:

> Any hireui LLM path touching a candidate MUST be fixed + legible + audited + human-in-loop + eval/bias-gated.

This translates directly to API contracts:

- **OpenAPI schemas** must document every field, its type, and constraints (e.g., `candidate.resume` is read-only, `job.salary_min` is audited)
- **API versioning** (e.g., `/v1`, `/v2`) makes breaking changes explicit and auditable
- **Request/response logging** (link: [[mosh-ai-powered-apps/_index]] for the vendor-seam pattern) must capture every API call, not just "LLM calls"
- **Rate limiting** (per user, per endpoint) prevents data-exfiltration attacks (credentials scraping via exhaustive API queries)

## Cross-links

- [[webhook]] — deep dive into webhook mechanics + patterns
- [[rest-and-web-api]] — REST semantics (GET = safe, PUT/DELETE = idempotent)
- [[graphql]] — the temptation + trade-offs
- [[grpc-and-rpc]] — when to escalate from REST
- [[selection-framework]] — decision tree for choosing an API type
- [[api-security-7-techniques/_index]] — securing these APIs (rate limiting, BOLA, CSP)
- [[miai-cv-matching-agent/_index]] — recruiting domain example: calling job-board APIs
- [[mosh-ai-powered-apps/_index]] — vendor-seam pattern: hireui's Claude API integration
- [[aws-email-at-scale-sqs-lambda-ses/_index]] — webhook receiver for email bounce events

## Key Takeaways

- **API types are architectural decisions, not implementation details** — they directly affect auditability, compliance, and cost.
- **hireui chooses REST + OpenAPI for external APIs** — strict contracts support the candidate-LLM legibility ADR better than GraphQL's flexibility.
- **Webhooks are the integration pattern** — inbound from job boards/ATS/email infrastructure; no polling.
- **WebSocket real-time is future-optional** — polling is acceptable until recruiter latency pain exceeds engineering cost.
- **gRPC is a scaling decision, not an initial choice** — monolith first, microservices when internal call volume justifies it.
- **Regulatory compliance rides on API contract legibility** — OpenAPI schemas + versioning + request logging are compliance infrastructure, not nice-to-haves.
- **This is foundational architecture, not novel** — no pilot required. Use this to ratify hireui's public-API surface decision before implementation.
