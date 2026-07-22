# gRPC, RPC, and tRPC

**Source:** 2026-07-21 NotebookLM digest (Codist, LetDiv, Ulbi TV, ByteByteGo) · `raw/2026-07-21-api-types-explained-rest-soap-graphql-grpc-websock.md`

## The RPC spine: call a remote function as if it were local

RPC stands for **Remote Procedure Call**. The one framing: instead of asking a server "please fetch data" via HTTP GET/POST, you call a function that lives on the other side of the network — `getUser(123)` — and the RPC framework hides the fact that it's remote.

Why this matters: in your code, remote calls **look identical** to local calls. No `fetch()`, no JSON parsing, no serialization ceremony. Write `result = add(2, 3)` and the RPC layer handles HTTP, encoding, deserialization.

This simplicity carries a cost: RPC is **tightly coupled** (client + server share a function contract) and **not web-native** (browsers speak HTTP; RPC is an abstraction layer on top). But for internal microservices, the coupling is a feature, not a bug.

## gRPC: Google's binary RPC (the "Formula 1" of internal APIs)

**What it is:**
- Google's production RPC framework, open-source since 2015.
- **Protocol Buffers (Protobuf)** serialize data into binary format (not JSON, not XML).
- Runs over **HTTP/2**, which enables [[websocket-and-realtime#http2-multiplexing|multiplexing]] (multiple concurrent requests on one TCP connection) and **bidirectional streaming** (client and server both send data simultaneously).

**Speed claim (with nuance per C1):**
- **Source claim:** gRPC is "7–10× faster than REST with JSON" (Codist, LetDiv, Ulbi TV).
- **Accurate scoping:** 7–10× speedup is **true specifically for large payloads and high-throughput scenarios** (100+ requests/second).
  - **REST is faster for small payloads** (single small GET returns faster than gRPC overhead).
  - **HTTP/2 with binary REST narrows gRPC's advantage to 10–25%**, not 7–10×. The gap closes when REST also uses binary encoding.
  - Comparison assumes HTTP/1.1 + JSON on the REST side; most comparisons don't control for this variable.

**Why Protobuf is smaller/faster:**
- Binary format ≈ 2–3× smaller than JSON for the same data.
- Serialization/deserialization faster (binary parser vs JSON parser).
- No whitespace, no quotes, no repeated field names.

**Trade-offs:**
- **Not browser-friendly.** Binary protocol, no human-readable requests. Unsuitable for web clients (use [[rest-and-web-api]] or [[graphql]] instead).
- **Not human-readable.** Can't curl a gRPC endpoint or inspect raw traffic easily. Need gRPC-specific tools (grpcurl).
- **Schema-first design.** Must define `.proto` files upfront; Protobuf compiler generates code. Contrast: [[#trpc-end-to-end-type-safe-typescript-rpc|tRPC]] skips this step.
- **Best for microservices.** Internal service-to-service communication where the coupling is intentional.

**Real-world use:**
- Google Cloud, Netflix, Uber, Stripe (internal APIs) — wherever low latency + high throughput is critical.

## tRPC: end-to-end type-safe TypeScript RPC

**What it is:**
- Modern RPC framework optimized for **TypeScript** (both client and server).
- No schema definitions (no `.proto`, no code generation, no IDL).
- **Type safety comes "for free"** — share type definitions via import, not code generation.

**Why it differs from gRPC:**
| Aspect | gRPC | tRPC |
|---|---|---|
| **Language scope** | Language-agnostic wire protocol (Java client ↔ Go server) | TypeScript-only on both sides (requires monorepo or module import) |
| **Schema** | `.proto` files compiled to code | TypeScript types (no compilation step) |
| **Serialization** | Binary (Protobuf) | JSON (over HTTP) |
| **Transport** | HTTP/2 (multiplexing + streaming) | HTTP/1.1 or HTTP/2 (standard REST-like calls, but typed) |
| **Use case** | Microservices, high-throughput internal APIs | Full-stack TypeScript apps (Node + React frontend) |

**Key constraint (per C8):**
- **tRPC is TypeScript-only**, not language-agnostic like gRPC.
- While tRPC's underlying HTTP/JSON protocol *could* theoretically be called from other languages, doing so **defeats tRPC's value** (end-to-end type safety only works when both sides are TypeScript).
- Non-TypeScript clients must revert to [[rest-and-web-api|REST]] or use separate schema definition (defeating the "no code generation" selling point).

**Simplicity benefit:**
- No `.proto` compiler, no build step, no versioning ceremony.
- Change a function signature in the server, type error in the client immediately.
- Suitable for full-stack monorepos (Next.js + tRPC backend is a common pattern).

## Selection: gRPC vs tRPC

| Scenario | Pick gRPC | Pick tRPC |
|---|---|---|
| Polyglot microservices (Java, Go, Python mix) | ✅ Language-agnostic | ❌ Breaks type safety |
| Full-stack TypeScript (Next.js + Node backend) | ❌ Overkill | ✅ Perfect fit |
| High-throughput internal APIs (100k+ RPS) | ✅ Binary + multiplexing | ❌ JSON serialization slower |
| Sub-millisecond latency requirement | ✅ Designed for it | ❌ No special optimizations |
| Need browser clients | ❌ Not web-native | ~ Maybe via REST wrapper |
| Simple, fast iteration | ❌ Schema-first | ✅ Type-first |

See [[selection-framework]] for task → API type lookup.

## Cross-cutting concerns

Both gRPC and tRPC are RPC frameworks and thus subject to the same operational concerns as [[rest-and-web-api]]:
- **Authentication** (e.g., JWT tokens in metadata headers for gRPC, cookies/headers for tRPC).
- **Rate limiting** (prevent one client from overwhelming the service).
- **Error handling** (gRPC has standard status codes; tRPC uses HTTP status + structured errors).

See [[api-security-7-techniques/_index]] for authorization + injection defense patterns.

## Key Takeaways

- **RPC = call a remote function as if it were local.** Hides HTTP/serialization details; trades HTTP flexibility for procedural simplicity.
- **gRPC = binary RPC over HTTP/2 (Protobuf + multiplexing + bidirectional streaming).** 7–10× faster than REST+JSON *specifically for large payloads at high throughput*; slower for small payloads.
- **tRPC = TypeScript-only RPC (no `.proto`, no code generation).** Type safety via shared TS types; ideal for full-stack TS monorepos.
- **gRPC's speed claim is benchmark-specific:** assumes HTTP/1.1 + JSON on REST side; HTTP/2 + binary REST closes the gap to 10–25%.
- **Not all RPC is created equal:** gRPC is language-agnostic (good for polyglot teams), tRPC is TS-only (good for homogeneous TS stacks).
- **Neither is browser-native:** gRPC is completely opaque to browsers; tRPC needs a wrapper for web clients. Use [[rest-and-web-api]] or [[graphql]] for browser-facing APIs.
- **Choose by coupling tolerance:** RPC assumes tight coupling (shared interface contract) — acceptable for internal microservices, not for public/third-party APIs.

