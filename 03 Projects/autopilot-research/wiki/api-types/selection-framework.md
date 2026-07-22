# Selection framework — which API type when

**Source:** [[overview]], [[rest-and-web-api]], [[soap]], [[graphql]], [[grpc-and-rpc]], [[websocket-and-realtime]], [[webhook]]

## The one question

Each of the 7 core API types answers a single recurring question: **"given my workload and constraints, which trade-off is worth making?"** — just like [[data-structures-16-in-32-min/_index]] does for data structures.

No type wins absolutely. Each is a mould (khuôn) that fits different data and different jobs:

- **REST** is human-readable, cacheable, stateless, but requires multiple round-trips for nested data
- **GraphQL** lets clients fetch exactly what they need, but invites DoS via malicious queries + requires per-request cost analysis
- **gRPC** is blazingly fast with Protocol Buffers (7–10× vs REST *for large payloads on high-throughput paths*; REST wins on small payloads; HTTP/2 + binary REST narrows the gap to 10–25%) (ByteByteGo), but requires polyglot tooling (code generation)
- **SOAP** enforces strict contracts via WSDL + WS-Security, but XML verbosity makes it slow and legacy-heavy (fintech *still* runs SOAP for sunk-cost and regulatory continuity, not new preference) (Ulbi TV)
- **WebSocket** enables real-time bidirectional chat + dashboards, but requires persistent connections (infrastructure + memory cost)
- **Webhook** pushes events asynchronously to client-supplied URLs, eliminating polling, but requires reliable retry logic + callback URL management
- **WebRTC** enables peer-to-peer audio/video/data, but *requires signaling servers + STUN/TURN for NAT traversal*—traffic often relays through intermediaries instead of direct peer paths (MDN)
- **tRPC** is a TypeScript-only RPC framework—provides end-to-end type safety without code generation, but *cannot interoperate with non-TypeScript clients without losing the type-safety guarantee* (LogRocket, Nordic APIs)

## Decision table: workload → API type

| Workload | API type | Why | See |
|---|---|---|---|
| Public web API (CRUD + pagination) | **REST** | Cacheable, human-readable, stateless, standard tooling | [[rest-and-web-api]] |
| Mobile app with bandwidth constraints / flexible client data-shaping / many nested resources | **GraphQL** | Client queries only needed fields, reduce overfetch. *Guard with depth limits + cost analysis against table-scan DoS* (C3) | [[graphql]] |
| Internal high-throughput microservices (>100 RPS, large payloads) | **gRPC + Protobuf** | Binary + HTTP/2 multiplexing. *Gap vs HTTP/2 + binary REST is 10–25%, not universal 7–10×* (C1) | [[grpc-and-rpc]] |
| Real-time bidirectional (chat, live dashboards, notifications) | **WebSocket** | Full-duplex, low latency, instant push. *Avoid REST polling for sub-second sync* (C5) | [[websocket-and-realtime]] |
| Event notifications between systems (payment processed, code pushed, job queued) | **Webhook** | Server initiates POST to callback URL on event. Async, push-based. *Requires HMAC auth + exponential backoff retries* (C6) | [[webhook]] |
| Peer-to-peer real-time media (audio, video, data channels) | **WebRTC** | Browser-to-browser connectivity. *Assumes signaling servers + STUN/TURN relays; direct P2P only on compatible networks* (C10) | [[websocket-and-realtime]] |
| Enterprise finance / legacy banking (strict contracts, regulatory continuity) | **SOAP + WSDL** | Enforced schema + WS-Security. *Incumbent in legacy systems, not preferred choice for new development* (C4) | [[soap]] |
| TypeScript monorepo (client + server co-located) | **tRPC** | Type-safe RPC without code generation. *TypeScript-only on both sides; interop breaks type safety* (C8) | [[grpc-and-rpc]] |

## The tradeoffs

### Human-readable vs. binary (speed cost)
- **REST + JSON**: human-readable, debuggable, but slower to parse and larger on the wire
- **gRPC + Protobuf**: compact binary format, 3–10× smaller, but requires schema + code generation

### Cacheable vs. post-only
- **REST (GET)**: browser/CDN cache hits, conditional requests, 304 Not Modified
- **GraphQL (POST)**: default POST blocks CDN caching, but *persisted query + APQ techniques enable full HTTP caching with minimal overhead* (Hasura, Apollo) — caching is different, not inherently harder (C2)

### Request-response vs. streaming
- **REST, SOAP, HTTP RPC**: single request → single response, simple timeouts, natural request/response matching
- **gRPC, WebSocket**: bidirectional streams, partial responses, requires backpressure handling

### Idempotency guarantees
- **GET, PUT, DELETE**: *server state identical on repeat, but response status codes may differ* (DELETE returns 204 then 404 on already-deleted) (C9); safe for retry logic
- **POST, PATCH**: not idempotent; multiple identical requests can create duplicates

### Security model
- **REST**: OAuth2, bearer tokens in Authorization header, standard CORS, rate limiting via HTTP headers
- **gRPC**: mTLS (mutual TLS), bearer tokens in metadata, channel-level security
- **SOAP**: WS-Security, digital signatures, encryption at message level (overkill for new systems)
- **Webhook**: HMAC signature in header, IP whitelist, exponential backoff

See [[api-security-7-techniques/_index]] for OWASP API security (rate limiting, CORS, injection, XSS, CSRF, VPN, firewall).

## Common pairings (real systems use multiple types)

- **Public REST API** + **internal gRPC microservices** — best of both worlds (client-friendly + fast internals)
- **REST CRUD API** + **WebSocket for notifications** — stateful reads via HTTP, real-time updates via WS
- **GraphQL** + **Webhook ingress** — flexible queries for clients, event-driven sync from upstream systems
- **REST** + **Webhook** — hireui job-board polling → internal event notifications (see [[mosh-ai-powered-apps/_index]])

## Key Takeaways

- **No API type wins absolutely.** Each is a trade-off; match the type to your workload (payloads, throughput, latency, update frequency, client sophistication).
- **REST remains the safe default** for public APIs: human-readable, cacheable, stateless, standard tooling. Deviate only if a workload forces it.
- **gRPC for internal microservices** where speed matters (but measure: large payloads + high throughput unlock the 7–10× claim; small payloads favor REST).
- **GraphQL for complex client needs**, but *mandatory controls: depth limits + cost analysis + rate limiting*. Not a free lunch.
- **WebSocket for real-time sync**, not inefficient polling (but polling remains valid for low-frequency, tolerance-for-latency scenarios).
- **Webhook for event notifications**—push, not pull. Standard HMAC + retry discipline required.
- **WebRTC for peer media**, but *expect signaling servers + TURN relays in practice*.
- **tRPC for TS monorepos**—type safety without code gen, but *TS-only on both sides*.
- **SOAP is legacy**—still operational in banking for sunk-cost + regulatory reasons, not new preference.
- **The selection framework is decision-tree-like, not prescriptive.** Read the workload row, check the constraints column, pick the type. Then [[critical-appraisal]] for context-specific gotchas.
