# Beyond the video — production concerns

The six API explainer videos ([LetDiv](source-provenance.md), [Codist](source-provenance.md), [ByteByteGo](source-provenance.md), [Ulbi TV](source-provenance.md), [Be A Better Dev](source-provenance.md), [Learn with Whiteboard](source-provenance.md)) build solid conceptual foundations. They cover **architecture, protocol, trade-offs**. They omit almost everything that makes an API **actually survive in production**. This article catalogs those gaps — not alternative opinions, but operational blindspots.

---

## The six categories of omission

### 1. Authentication & Authorization (AuthN/AuthZ)

**Beginner claim:** "Send a token in the authorization header." (Ulbi TV, ByteByteGo)

**Reality for production:**
- Token lifecycle is harder than transmitting it. You need:
  - **OAuth2** or **OpenID Connect** for issuing tokens (not just validation)
  - **JWT signing** — keys exist, rotate, expire. Key rotation without service restart is non-trivial.
  - **Revocation** — blacklist/blocklist when a token must die early (logout, password reset, permission change)
  - **Rate limiting per principal** — not just per IP, but per authenticated user/API key
- Example challenge from [[api-security-7-techniques/_index]]: **BOLA (Broken Object-Level Authorization)** — the API respects your token but lets you read resources you shouldn't. The videos don't mention this vulnerability class at all.
- **Patterns:** mTLS (mutual TLS) for service-to-service; OAuth2 + PKCE for mobile/SPA clients; API keys + secrets for programmatic access with separate revocation per key.

See [[critical-appraisal]] for how existing comparisons rank on security completeness.

### 2. API Gateways & Request Routing

**Beginner assumption:** "One server, one API." (implicit in all 6 sources)

**Reality for production:**
- A single API endpoint is a fallacy. You typically have:
  - Multiple backend services (microservices)
  - Multiple versions of the same service (v1 and v2 running in parallel)
  - Different protocols (gRPC internally, REST externally)
  - Rate-limiting, protocol translation, authentication — applied to **all** requests, not per-service
- **Tools:** Kong, NGINX, AWS API Gateway, Envoy, Traefik
- **Responsibilities gateways own:**
  - Request routing (by version, by tenant, by geographic region)
  - Protocol translation (REST ↔ gRPC ↔ WebSocket)
  - Authentication enforcement (OAuth2 token validation, mTLS)
  - Rate limiting and quota management
  - Request/response transformation (add headers, extract fields, reshape JSON)
  - TLS termination
- **Why it matters:** Without a gateway, you implement these features **per service**, duplicating code and creating inconsistent security posture.

### 3. Service Meshes & Internal Communication

**Beginner assumption:** "Services talk directly to each other via HTTP calls."

**Reality for production:**
- Direct calls fail silently, cascade failures, lose observability. A **service mesh** (Istio, Linkerd, Consul) intercepts all inter-service communication:
  - **Automatic retries** with exponential backoff
  - **Circuit breaking** — stop calling a broken service, return early
  - **Distributed tracing** — every request gets a trace ID; you see the call chain across 10+ services
  - **mTLS by default** — service-to-service encryption without explicit certificate management
  - **Load balancing** — smart distribution across instances (not just round-robin)
- **Trade-off:** meshes add latency (~1-5ms per hop) and operational complexity (sidecar injection, configuration). For small systems (<5 microservices), meshes are overkill.

### 4. Observability (The Three Pillars)

**Beginner claim:** "Test the API in the Playground." (LetDiv, Codist, Ulbi TV)

**Reality for production:**
- Playgrounds don't exist at 3am when the service is on fire. You need:
  - **Metrics** — request count, latency (p50/p95/p99), error rate, per endpoint. Export to Prometheus/Grafana.
  - **Structured logging** — JSON logs with request ID, user ID, service name, latency. Searchable in Datadog/Splunk/ELK.
  - **Distributed tracing** — trace a single request through 5+ microservices, see where it gets stuck. Tools: Jaeger, Zipkin, Datadog.
  - **Health checks** — `/health` endpoints that return 200 when ready, 503 when degraded. Kubernetes / load balancers use these to route around broken instances.
- **Why it matters:** Without these, you're blind. A customer says "the API is slow" — slow for whom? Slow on which endpoint? At what time? You have no data.

### 5. Resilience Patterns (Handling Failure)

**Beginner assumption:** "If a request fails, retry it." (implicit)

**Reality for production:**
- Naive retries break systems. You need:
  - **Rate limiting** — reject requests if you're at capacity, rather than queue them and hope. Strategies: token bucket, sliding window, leaky bucket.
  - **Throttling** — deliberately slow down a client that's misbehaving (either human or bot) using 429 Too Many Requests.
  - **Circuit breakers** — if a downstream service fails 5× in a row, stop calling it for 30s and return a cached response or error. Prevents cascading failures.
  - **Exponential backoff** — retry with 100ms, 200ms, 400ms, 800ms delays (not instant hammering).
  - **Timeouts** — every call must have a deadline. If a service takes >5s, kill the request and move on.
- **Why it matters:** A single misbehaving client can DOS your entire system if you don't rate-limit. A cascading failure in one service can bring down ten others if you don't have circuit breakers. See [[aws-email-at-scale-sqs-lambda-ses/_index]] for how SQS + Lambda leverage these patterns.

### 6. Contract Testing & CI/CD Pipelines

**Beginner claim:** "Use Swagger to document the API." (Ulbi TV)

**Reality for production:**
- Swagger is **read-only documentation**. Production needs **executable contracts**:
  - **Pact** — a client and server agree on request/response shapes; the test suite verifies both sides honor the contract. Catches breaking changes before deployment.
  - **Postman collections** — API requests in a format that CI/CD can run automatically (not just humans clicking in the Playground).
  - **Schema validation** — at request entry, validate the JSON against a schema (OpenAPI, JSON Schema). Rejects malformed requests early.
- **Deployment strategies:**
  - **Blue-green** — two identical environments (blue and green). Send traffic to blue, deploy to green, then switch. Instant rollback if something breaks.
  - **Canary** — deploy to 5% of traffic, monitor for errors, gradually increase to 100% if stable.
  - **Feature flags** — code deployed but toggled off. Disable a broken feature without redeploying.
- **Why it matters:** Without contract tests, you deploy a breaking change to production and discover it when customers start hitting 400 errors. With them, you catch it in CI.

### 7. Database Performance Tuning (especially for GraphQL)

**Beginner claim (ByteByteGo):** "GraphQL can bring down your database with unexpected table scans."

**Reality for production:**
- The claim is correct but vague. Specific mitigations:
  - **Query cost analysis** — assign a cost to each field in the GraphQL schema (scalar = 1, list = 5, nested object = 10). Reject queries that exceed a cost budget. Blocks pathological queries before they hit the DB.
  - **Depth limiting** — reject queries with more than N levels of nesting (e.g., max depth 5). Prevents quadratic query blowup.
  - **Field-level authorization** — a user can query `user.name` but not `user.salary`. This also reduces query scope.
  - **Database indexing** — add indexes on frequently-filtered fields (GraphQL often filters by ID, created_at, status). Use EXPLAIN ANALYZE to find missing indexes.
  - **Query execution plans** — understand which queries are slow. PostgreSQL's EXPLAIN tells you; MySQL's EXPLAIN FORMAT=JSON shows table scans.
- **Why it matters:** Without these, a single malicious GraphQL query can lock your database for 10 seconds, timing out all other requests. With them, pathological queries are rejected (or throttled) at the edge, never reaching the DB.

---

## Implementation roadmap (roughly in order of urgency)

1. **Start with a gateway** (Kong / NGINX / AWS API Gateway) — centralizes auth, rate-limiting, versioning.
2. **Add structured logging** — JSON logs with request ID, latency, user ID. Search is free if you add it now; retrofitting is painful.
3. **Add metrics** (Prometheus + Grafana, or Datadog). Even basic metrics (request count, p99 latency) prevent blindness.
4. **Add distributed tracing** (Jaeger or Datadog). Wires up automatically if you use a library like OpenTelemetry.
5. **Implement circuit breakers** (Hystrix, Polly, or built into your framework). Prevents one broken service from cascading.
6. **Add contract tests** (Pact). Integrate into CI/CD so breaking changes are caught before production.
7. **Implement query cost analysis** (if using GraphQL). A small DSL that assigns costs to fields.
8. **Adopt canary deployments** (blue-green is a fallback if you don't have canary tools). Catches bugs in 5% of traffic before 100%.

---

## Cross-link to security specifics

[[api-security-7-techniques/_index]] dives deeper into OWASP API threats (injection, CORS misconfig, rate-limit bypass, BOLA). The threats listed there are **not prevented by protocol choice** — REST, GraphQL, and gRPC are all equally vulnerable if you don't implement the defenses. The seven techniques apply uniformly.

---

## Scope boundary: what videos COULD have covered but chose not to

The six sources are **architecture explainers for beginners**, not operations courses. The omissions are intentional scoping, not errors:

- Observability (metrics / logging / tracing) — requires running code, not just understanding HTTP
- Circuit breakers — operational pattern, not architectural
- Database tuning — orthogonal to API choice
- Deployment strategies — infrastructure, not API design

A beginner who learns gRPC from the videos has learned gRPC. A production team deploying gRPC has much more work ahead.

---

## Key Takeaways

- **AuthN/AuthZ is not "send a token"** — it includes key rotation, JWT signing, revocation, and per-user rate limiting. See [[api-security-7-techniques/_index]] for BOLA and other authorization flaws.
- **API gateways are not optional** — they centralize auth, rate-limiting, protocol translation, and request routing across multiple backends and versions.
- **Service meshes prevent cascading failures** — at the cost of ~1-5ms latency per hop. Use for >5 microservices.
- **You are blind without observability** — metrics, structured logs, and distributed tracing are as important as the protocol. Add them early.
- **Resilience patterns are crucial** — rate limiting, circuit breakers, timeouts, and exponential backoff prevent one broken client or service from cascading to the whole system.
- **Contract testing catches breaking changes in CI** — Pact and Postman collections are executable contracts, not just documentation.
- **GraphQL + databases require explicit defenses** — query cost analysis and depth limiting prevent pathological queries from locking your database.
