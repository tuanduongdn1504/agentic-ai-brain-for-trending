# REST and the 'Web API' Umbrella

**Source:** [2026-07-21-api-types-explained-rest-soap-graphql-grpc-websock.md](../../raw/2026-07-21-api-types-explained-rest-soap-graphql-grpc-websock.md) · NotebookLM digest of 6 videos · `raw/`

---

## The core thesis: REST is not a protocol, it's a philosophy

REST (**REpresentational State Transfer**) is an **architectural style**, not a protocol. It's a set of principles for how to structure interactions between a client and a server:

- **Resources** — every piece of data gets a URL. A user is `/users/123`, not `/getUser?id=123`.
- **HTTP methods** — use GET, POST, PUT, DELETE to mean *retrieve, create, update, delete*. Not POST for everything.
- **Statelessness** — each request contains all the information the server needs. The server does not store context about the client between calls. This makes the system horizontally scalable (LetDiv, Codist, Learn with Whiteboard).
- **JSON (usually)** — most modern REST APIs use JSON for the request/response body instead of XML.

REST's **flexibility** is why it dominates. It sits on top of HTTP, which every device, browser, and firewall understands. A smartphone, a CLI tool, a JavaScript frontend, and a server-to-server integration can all call the same REST endpoint.

---

## The real weakness: over/underfetching

The biggest legitimate complaint against REST is the **overfetching and underfetching** problem (ByteByteGo, Codist, LetDiv):

- **Overfetching**: the server sends back MORE data than the client needs. Example: you ask for a user's name and email, but the endpoint returns the entire user object (address, phone, subscription history, preferences, etc.). Wastes bandwidth.
- **Underfetching**: the client gets LESS data than it needs in one call, forcing multiple round-trips. Example: fetch a blog post → now you need the author details → now you need the author's profile photo. Three API calls where one would be ideal.

GraphQL was designed to fix this exact problem (see [[graphql]]). REST cannot, because the server decides what fields to return, not the client.

This is a **real architectural constraint** of REST, not an overclaim. (Verdict: CONFIRMED.)

---

## The terminology disagreement: "Web API" as umbrella?

**This is a real contradiction in the sources, not a settled fact.**

**Learn with Whiteboard's framing:**
- Treats "Web API" as a **broad umbrella** that encompasses REST, SOAP, and XML-RPC.
- A Web API is any API that uses standard web protocols like TCP/IP or HTTP.
- REST is *one kind* of Web API.

**Ulbi TV's (and most other sources') framing:**
- REST, SOAP, and gRPC are **parallel types**, not categories within a hierarchy.
- They're fundamentally different kinds of things:
  - **REST** = architectural style (how you think about resources)
  - **SOAP** = protocol (a rigid, XML-based communication spec)
  - **gRPC** = RPC + HTTP/2 + binary serialization
- Grouping them under "Web API" obscures these distinctions.

**The resolution:** Ulbi TV is correct that the categories are different. REST is a design *philosophy*, SOAP is a *protocol*, and gRPC is a *framework*. Calling all of them "Web APIs" is like calling apples, oranges, and hammers "tools"—technically true but loses all precision. However, Learn with Whiteboard's framing isn't *wrong*, just coarser. In contexts where you don't care about the distinction (e.g., "we need *some* API"), the umbrella term works. In production architecture, the distinctions matter.

**For this wiki:** REST and SOAP are separate [[soap|sibling articles]], not a parent-child relationship.

---

## REST's statelessness principle

Every request must carry all the information the server needs to process it. The server does **not** keep session state between calls. Why?

- **Scalability** — if the server doesn't store context, you can handle the next request on a different server in a load-balanced cluster. No sticky sessions. No shared state to synchronize.
- **Simplicity** — the client can retry a request without worrying about partial state on the server.
- **Cacheability** — stateless requests are cacheable (see [[http-semantics-and-rest-conventions]] for GET vs POST).

(Sourced from LetDiv, Learn with Whiteboard, Codist.)

---

## REST for real-time? The disagreement resolved

**Learn with Whiteboard claims:** REST is suitable for real-time chat and streaming.

**Be A Better Dev claims:** REST polling is a primitive and outdated approach for real-time, stressing servers and databases.

**Resolution (Verdict C5: CORRECT-BUT-INCOMPLETE):**

- **For new chat/real-time projects**, WebSockets are categorically better. They eliminate polling overhead (~80% savings), enable instant bidirectional push, and are the modern standard (see [[websocket-and-realtime]]).
- **However**, polling is NOT universally an anti-pattern. It remains appropriate for:
  - Low-frequency updates where seconds of delay are acceptable (e.g., status checks every 30s).
  - Simple implementations where WebSocket infrastructure isn't available.
  - Reliable fallback when WebSockets fail (some proxies block them).

The clash resolves by scope: **default to WebSockets for new synchronous real-time applications; polling is a valid choice for asynchronous, low-frequency, or compatibility scenarios.**

---

## Semantic HTTP: the method you use matters

REST's power comes from using HTTP methods correctly:

| Method | Semantics | Idempotent? | Example |
|--------|-----------|-------------|---------|
| GET | Retrieve data; does NOT modify state | Yes | `GET /users/123` |
| POST | Create a new resource | No | `POST /users` with body `{name, email}` |
| PUT | Replace a resource entirely | Yes | `PUT /users/123` with full new body |
| DELETE | Remove a resource | Yes | `DELETE /users/123` |

(See [[http-semantics-and-rest-conventions]] for deeper semantics: PATCH vs PUT, response codes, idempotency details.)

Using POST for everything is technically possible but defeats REST's benefit: you lose the semantic clarity that tools (proxies, caches, HTTP libraries) can use to handle requests correctly.

---

## Why REST dominates

1. **Uses HTTP, which is universal** — every device, network, and firewall speaks it.
2. **Human-readable** — JSON is easier to debug than binary protocols.
3. **Flexible** — no heavy frameworks or schemas required to get started.
4. **Stateless** — horizontally scalable.
5. **Caching-friendly** — GET requests can be cached by browsers and CDNs.

The trade-off: overfetching/underfetching, no built-in schema enforcement, no query language. Solutions exist (GraphQL, JSON:API) but add complexity.

---

## Quick comparison with other types

| Type | Protocol? | Use Case | Main Weakness |
|------|-----------|----------|---------------|
| REST | HTTP (architectural style) | General APIs, web services | Over/underfetching |
| [[graphql|GraphQL]] | HTTP (query language) | Flexible data fetching | Complexity, caching, DoS risk |
| [[grpc-and-rpc|gRPC]] | HTTP/2 + Protobuf | Microservices, high throughput | Binary, not human-readable |
| [[soap|SOAP]] | HTTP/HTTPS (rigid protocol) | Legacy banking, enterprise | Verbose, heavyweight |
| [[websocket-and-realtime|WebSocket]] | TCP upgrade | Real-time bidirectional | More complex than HTTP |

---

## Key Takeaways

- **REST is an architectural style**, not a protocol — it's about structuring resources (URLs) + using HTTP methods semantically + statelessness.
- **Overfetching and underfetching** are genuine REST weaknesses; GraphQL and JSON:API solve them.
- **"Web API" as an umbrella term** is a real terminology disagreement: Learn with Whiteboard uses it broadly; most other sources treat REST/SOAP/gRPC as parallel types. Both framings are internally consistent; pick the one that matches your abstraction level.
- **Polling vs. WebSockets**: WebSockets are superior for real-time; polling remains valid for low-frequency asynchronous updates.
- **REST dominates** because it's simple, scalable, universal, and requires no heavy infrastructure.
- **Statelessness** enables horizontal scaling — the foundation of REST's operational advantage.
- Detailed HTTP semantics (idempotency, response codes, caching rules, versioning) live in [[http-semantics-and-rest-conventions]].
