# Caveats & Corrections — api-types

Corrections applied during compile so the wiki states the **verified** version, not the video's original framing. Sourced from the refute-first verification run (`wf_640f115f-0a8`); see [[claims-scorecard]] for the full verdict table.

> **No claim was OVERTURNED and none was FALSE.** These are refinements to *beginner-explainer over-generalizations* — the sources are technically honest.

## Magnitude corrections (don't quote the round number without context)

- **gRPC "7–10× faster than REST" (C1)** — payload- and benchmark-specific. True for **large payloads + high throughput (100+ RPS)**. For **small payloads REST is faster**; against **HTTP/2 + binary-encoded REST** the advantage collapses to **~10–25%**. The 7–10× figure silently assumes HTTP/1.1 + JSON on the REST side. Quote it only with the scope attached.
- **WebSocket "~80% less overhead than polling" (C5)** — directionally right for high-frequency real-time, but it's a rule-of-thumb, not a universal constant; the win depends on update frequency.

## Framing corrections

- **"SOAP is preferred for banking/fintech" (C4)** → SOAP is a **legacy operational incumbent**, *not* the preferred choice for new systems in 2026. Kong's 2026 banking-API landscape omits SOAP entirely; REST dominates (~83% adoption); SWIFT's Nov-2026 migration targets **ISO 20022**; modern rails (Plaid, Stripe, Modern Treasury) are REST. SOAP persists through sunk cost + regulatory continuity, not active preference. WS-Security's role is now filled by OAuth 2.0 / FAPI 2.0 / mTLS.
- **"GraphQL is harder to cache" (C2)** → **different, not harder.** POST isn't URL-cacheable, but queries *can* use GET, and **persisted queries / automatic persisted queries (APQ)** give full HTTP/CDN caching. Client-side caching (Apollo/Relay normalized cache) is arguably *better* than REST. The difficulty only appears when caching isn't deliberately designed — true of REST too.
- **tRPC "type-safe RPC without codegen" (C8)** → accurate but **TypeScript-only on both client and server**. It is *not* a language-agnostic wire protocol like gRPC; a non-TypeScript client defeats its entire value proposition. Don't file it as a gRPC peer for polyglot systems.
- **WebRTC "peer-to-peer" (C10)** → the P2P is the *design intent*, not the guaranteed data path. WebRTC needs a **signaling server** to set up the connection and, in most production networks, **STUN/TURN** servers for NAT traversal — traffic frequently **relays through TURN**, not truly direct.
- **HTTP idempotency (C9)** → idempotent (GET/PUT/DELETE) guarantees the same **server state** on repetition, *not* an identical HTTP response. A repeated DELETE legitimately returns `204` then `404`. Different PUT bodies legitimately produce different states.

## Source-vs-source disagreements (surfaced, not averaged)

- **REST for real-time (C5):** *Learn with Whiteboard* calls REST "suitable for real-time chat/streaming"; *Be A Better Dev* calls REST-for-chat "primitive/outdated." **Resolution by scope:** for synchronous, sub-second bidirectional chat, Be A Better Dev is right — WebSockets are the correct default. But "anti-pattern in all contexts" is too absolute: **polling remains valid** for low-frequency async updates, status checks, and as a WebSocket fallback. See [[websocket-and-realtime]].
- **"Web API" taxonomy:** *Learn with Whiteboard* treats "Web API" as a **broad umbrella** over REST/SOAP/XML-RPC; most other sources (and Ulbi TV's own caveat) treat REST/SOAP/gRPC as **parallel types** — because they're different *kinds* of thing (protocol vs architectural style vs query language). Recorded as a real terminology disagreement in [[rest-and-web-api]], not resolved to one "right" hierarchy.

## Scope caveats (what the sources are NOT)

- These are **beginner conceptual explainers**, not implementation guides. Zero production depth on auth (OAuth2/JWT), gateways, observability, resilience, or contract testing — see [[beyond-the-video]].
- The bundle mixes languages (VN anchor + EN + one RU source, Ulbi TV) and eras (2021–2026); NotebookLM synthesized across them, so specific phrasings are its paraphrase, not verbatim quotes.

## Method notes (Rule 12 — fail loud)

- The gRPC↔WebSocket multiplexing cross-link (`[[websocket-and-realtime#http2-multiplexing]]`) points at the shared HTTP/2 discussion; multiplexing is properly a gRPC/HTTP-2 property, noted here to avoid implying it's WebSocket-specific.
- Link hygiene: 4 articles had drafter-introduced link defects (a `moshi-` typo, several `external|` markers on topics that are actually **local**, escaped `\|` pipes) — all corrected deterministically at compile; every wiki-link was filesystem-validated (157 checked). No fabricated cross-links survived.

## Key Takeaways

- Nothing false or fabricated — every correction is a *"true, but here's the context"* refinement of a beginner over-generalization.
- The one number to never quote bare: gRPC **"7–10× faster"** (C1) — scope it to large payloads / high throughput / HTTP-1.1-JSON baseline.
- The one dated framing to fix on sight: **SOAP "for banks"** (C4) — legacy incumbent, not the modern choice.
- Two sources genuinely disagree on REST-for-realtime; the wiki keeps both and resolves by scope rather than averaging.
