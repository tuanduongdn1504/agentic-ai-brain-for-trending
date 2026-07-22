# Overview — An API type is a Contract + Transport Pattern

**Source:** NotebookLM digest of 6 videos (LetDiv, Codist, ByteByteGo, Ulbi TV, Be A Better Dev, Learn with Whiteboard) · 2026-07-21 · `raw/2026-07-21-api-types-explained-rest-soap-graphql-grpc-websock.md`

## The one framing

An **API type** is a **contract** (what data you exchange, how it's shaped) **plus a transport/interaction pattern** (how programs send that data back and forth). REST says "stateless HTTP, standard verbs, JSON"; GraphQL says "typed schema, client-defined queries, POST"; WebSocket says "persistent bidirectional connection"; gRPC says "binary serialization, HTTP/2 streams, call-reply."

**No type wins absolutely.** Each trades off:
- REST ↔ flexibility & human-readability vs. data precision & caching
- GraphQL ↔ client power & bandwidth vs. query complexity & DoS surface
- gRPC ↔ speed & throughput vs. human legibility & ecosystem maturity
- WebSocket ↔ real-time latency vs. server resource cost
- SOAP ↔ formality & enterprise trust vs. heavyweight XML

Picking well means matching the trade-off to your workload (security, speed, real-time, client flexibility, bandwidth, infrastructure).

## The taxonomy (8 core types + broader categories)

| Type | Protocol | Core Pattern | Best For |
|---|---|---|---|
| **REST** | HTTP (GET/POST/PUT/DELETE) | Stateless request-response + standard semantics | Default choice; web APIs; CRUD; caching |
| **SOAP** | HTTP/HTTPS + XML | Formal contracts (WSDL); digital signatures; WS-Security | Legacy banking/fintech; enterprise compliance |
| **GraphQL** | HTTP (usually POST) | Client-defined queries against typed schema | Mobile-bandwidth-constrained; complex data graphs |
| **gRPC** | HTTP/2 + Protocol Buffers | Bidirectional streaming; binary; typed schema | Microservices; high-throughput; latency-sensitive |
| **tRPC** | HTTP/JSON | TypeScript end-to-end type safety; no code-gen | TypeScript monorepos only (not language-agnostic) |
| **WebSocket** | TCP upgrade via HTTP | Persistent bidirectional connection; push-on-change | Chat; live notifications; real-time bidirectional sync |
| **Webhook** | HTTP POST (server → client) | Event-driven; "reverse API"; callback URL | Payment processors; CI/CD; event propagation |
| **WebRTC** | UDP (via STUN/TURN signaling) | Peer-to-peer real-time audio/video/data | Browser-to-browser calls; requires signaling server + NAT relay |

### "Web API" as umbrella term (disagreement flagged)

Some sources treat "Web API" as a broader category encompassing REST, SOAP, and XML-RPC. Others treat REST, SOAP, and GraphQL as parallel "types," not sub-categories. See [[rest-and-web-api]] for the categorization nuance — this inconsistency is real in the corpus.

## Recurring theses across sources

1. **REST is the flexible default** (LetDiv, Codist, Learn with Whiteboard, Ulbi TV)
   - Standard HTTP semantics (GET retrieves, POST creates, PUT replaces entirely, PATCH updates fields, DELETE removes)
   - Stateless per-request design enables horizontal scaling
   - Caches transparently via standard HTTP GET
   - But overfetches and underfetches data — clients get more than needed or must make multiple round-trips

2. **Binary protocols trade human-readability for speed** (ByteByteGo, Ulbi TV)
   - gRPC + Protocol Buffers achieves 7–10× speedup over REST+JSON *specifically for large payloads and high-throughput scenarios* (100+ RPS)
   - Against HTTP/2 with binary REST alternatives, advantage shrinks to 10–25%
   - REST faster on small payloads; gRPC dominates at scale
   - Binary buys concurrency via HTTP/2 multiplexing (many concurrent streams on one TCP connection)

3. **GraphQL moves data-shaping to the client — with real costs** (ByteByteGo, LetDiv, Codist)
   - Client writes a query: `{ user { name email posts { title } } }` — only those fields returned
   - Solves overfetch/underfetch by letting the client ask for exactly what it needs
   - BUT: POST-only pattern doesn't leverage HTTP GET caching; requires **persisted queries** or **automatic persisted queries (APQ)** for CDN caching — different approach, not harder, but deliberate tooling needed
   - Bigger risk: deeply nested queries can trigger database table scans and DoS. Need **query depth limiting + cost analysis** (both standard Apollo recommendations)

4. **Real-time needs persistent or event-driven connections, not polling** (Be A Better Dev, Ulbi TV, LetDiv)
   - Short polling = client repeatedly asks "any updates?" — wastes bandwidth, causes latency, stresses server/database
   - WebSocket = persistent full-duplex connection; server pushes the moment data changes — ~80% less overhead
   - BUT: polling remains appropriate for low-frequency asynchronous updates (status checks, non-urgent notifications) where seconds of delay are acceptable — context-dependent, not universally anti-pattern
   - Webhooks = "reverse API"; server calls your callback URL on event — simpler than you polling, trades your infrastructure costs for provider's push costs

## LetDiv's "7 types" framing (VN anchor)

LetDiv structures the lesson as 7 types: REST, SOAP, GraphQL, gRPC, WebSocket, Webhook, WebRTC. This wiki expands slightly (adds tRPC as distinct from generic RPC), bringing the practical count to 8. The sources show agreement on definitions but real disagreement on categorization and best-practice boundaries (see [[critical-appraisal]]).

## Key operational nuances

**Idempotency (REST semantics):** GET, PUT, DELETE are idempotent (same server state on repetition), but response status codes *may differ* — DELETE returns 204, then 404 on already-deleted resources. Idempotent ≠ "same response"; only server state is guaranteed.

**WebRTC realities:** Marketed as "peer-to-peer," but requires a **signaling server** for initial coordination AND typically relies on **STUN/TURN servers** for NAT traversal. Direct peer connections only possible on compatible networks; production deployments usually relay traffic through TURN intermediaries.

**SOAP in banking:** SOAP persists as an operational legacy incumbent in banking due to sunk costs and WS-Security heritage, not active preference in 2026. Modern banking standards (FAPI 2.0, ISO 20022, REST APIs) dominate greenfield development. SOAP remains "still operational" but is no longer the preferred architectural choice for new systems.

**tRPC limitation:** Delivers TypeScript end-to-end type safety without code generation, but is **TypeScript-only on both client and server**. Calls from non-TypeScript clients defeat its core value proposition (type safety). Not language-agnostic like gRPC.

## Key Takeaways

- An API type = contract + transport pattern. No type wins universally; choose by workload (security, latency, throughput, client flexibility, caching needs).
- **REST** is the flexible default: standard HTTP semantics, transparent caching, but overfetches/underfetches.
- **gRPC** (binary + HTTP/2) achieves 7–10× speedup over REST for large-payload, high-throughput scenarios; REST faster for small payloads.
- **GraphQL** shifts data-shaping to the client (solving overfetch) but requires deliberate caching tooling (persisted queries/APQ) and depth-limiting to prevent DoS.
- **Real-time** systems need persistent connections (WebSocket, Webhook, WebRTC), not polling — but polling remains appropriate for low-frequency asynchronous updates.
- **SOAP** is legacy-operational in banking, not preferred for new systems; **tRPC** is TypeScript-only, not language-agnostic.
- Request/response properties are nuanced: idempotent methods don't guarantee identical responses; WebRTC requires signaling + TURN relays in practice.
- Cross-link to [[selection-framework]] for task→type matching, [[rest-and-web-api]] for categorization nuance, [[critical-appraisal]] for source disagreements.
