# WebSockets, WebRTC and Real-Time

**Source:** [2026-07-21-api-types-explained-rest-soap-graphql-grpc-websock.md](../../raw/2026-07-21-api-types-explained-rest-soap-graphql-grpc-websock.md) · NotebookLM digest of 6 videos

---

## The one framing

Real-time APIs solve a single problem: **how do you push data from server to client the moment it changes, instead of having the client repeatedly ask?**

The answer is: upgrade from HTTP's request-response chain to a persistent, bidirectional channel. Three patterns:
1. **WebSockets** — persistent TCP upgraded from HTTP; server can push anytime.
2. **WebRTC** — peer-to-peer browser-to-browser audio/video/data (with server help for signaling).
3. **Short polling** — client asks repeatedly; inefficient but sometimes unavoidable.

---

## WebSockets: persistent full-duplex

- **Mechanism:** HTTP upgrade handshake (`Connection: Upgrade`, `Upgrade: websocket`) establishes a single persistent TCP connection that stays open for the session.
- **Bidirectionality** (full-duplex): server *and* client can send messages anytime, independently — the moment an event happens, server pushes to client instead of waiting for the next poll.
- **Overhead advantage:** ~80% less overhead than polling; instant latency vs. polling's delay equal to the poll interval.
- **Use case:** real-time chat, live dashboards, collaborative editing, multiplayer games — anything where seconds of delay is unacceptable.
- **Note:** WebSockets are NOT suitable for request-response queries (no inherent request-ID correlation); treat each message as an event.

### Polling (the anti-pattern in high-frequency scenarios)

- **Short polling:** client sends "any updates?" repeatedly (e.g., every 2 seconds).
- **Why it's inefficient:** creates many redundant HTTP requests + network overhead; latency = poll interval (not instant).
- **Server/database stress:** per (Be A Better Dev), polling puts "stress on your server and database" because every request (even when empty) costs resources.
- **CORRECTED verdict (C5):** Polling is NOT universally an anti-pattern. It's appropriate for low-frequency updates where 5–30 second latency is acceptable (e.g., Gmail's historical long-polling for new messages, status checks, or fallback when WebSockets unavailable). The choice is **context-dependent**: latency requirements, update frequency, infrastructure constraints, and complexity tolerance determine which is correct — not a universal right/wrong.
- **Best practice:** Use WebSockets as the default for new real-time chat projects. Retain polling as a fallback mechanism or for asynchronous status checks.

---

## WebRTC: peer-to-peer real-time media

- **Mechanism:** W3C standard for browser-to-browser real-time communication (audio, video, arbitrary data channels).
- **Intended topology:** peer-to-peer — endpoint-to-endpoint, no intermediary server carrying the media.
- **Reality (C10):** WebRTC requires three types of server involvement:
  - **Signaling servers** to exchange session description protocol (SDP) and ICE candidates so peers can find each other.
  - **STUN servers** (Session Traversal Utilities for NAT) to detect your public IP + port when behind a firewall.
  - **TURN servers** (Traversal Using Relays around NAT) to relay media when direct connection is impossible (NAT incompatibility, restrictive firewalls).
- **Direct connection likelihood:** only when network topology permits. In practice, TURN relay is the normal case in production deployments.
- **Complexity:** higher than WebSockets; requires coordination of multiple media streams + ICE candidate negotiation + browser codec/bitrate negotiation.
- **Use case:** video conferencing, screen sharing, peer-to-peer file transfer, real-time games with high-frequency state updates.

---

## REST polling vs. WebSockets: the disagreement resolved

**Learn with Whiteboard** claimed REST is "suitable for real-time chat."  
**Be A Better Dev** called REST polling "primitive and outdated" for chat.

**Which is correct?** Both, depending on scope.

- **WebSockets should be the default** for new real-time chat projects (sub-second latency, efficient, industry-standard).
- **REST polling remains viable** for low-frequency asynchronous updates, reliable fallback when WebSockets unavailable, or simpler implementation when latency tolerance exists.
- **The contradiction resolves by workload:** WebSockets are categorically better for synchronous bidirectional communication. Polling trades efficiency for simplicity and reliability (standard HTTP, fewer proxy issues). Modern systems use WebSockets for chat but retain polling strategies for notifications and status checks.

The claim "primitive/outdated" is too absolute; it's context-dependent, not universally wrong.

---

## HTTP/2 and multiplexing

Per (LetDiv, Codist, Ulbi TV), gRPC leverages **HTTP/2** to support "multiple simultaneous requests over a single connection."

**Correct but incomplete (C7):** HTTP/2 supports multiple concurrent streams on one TCP connection, enabling bidirectional communication patterns. However:
- Per-connection concurrency is subject to limits (RFC 7540 Section 5.1.2: `SETTINGS_MAX_CONCURRENT_STREAMS`, typically 100–∞ depending on implementation).
- Practical concurrency is also constrained by flow control and bandwidth.
- HTTP/2 multiplexing is architectural—not the same as WebSocket's full-duplex push (WebSocket is event-driven; HTTP/2 streams are still request-response).

---

## When NOT to use WebSockets

- **Stateless APIs** — REST is better for independent, stateless operations (CRUD, queries).
- **Browser caching** — HTTP GET is cacheable; WebSocket connections are not.
- **Simple status checks** — polling is simpler to implement and is fine when latency tolerance is high.
- **Fallback requirements** — if you need to support very old browsers or restrictive network environments (some corporate proxies block WebSockets), polling + HTTP is safer.

---

## Cross-references

- [[overview]] — API types comparison.
- [[rest-and-web-api]] — REST's request-response model (the thing WebSockets improve on).
- [[webhook]] — the other push pattern (server-to-server, not server-to-client).
- [[grpc-and-rpc]] — HTTP/2 multiplexing in more detail.
- [[selection-framework]] — when to use each API type.

---

## Key Takeaways

- **WebSockets upgrade HTTP to persistent, bidirectional TCP** — server can push data instantly instead of waiting for the client's next request.
- **Polling (repeated HTTP requests) is inefficient for high-frequency real-time chat** but remains appropriate for low-frequency updates and reliable fallback.
- **WebRTC enables peer-to-peer audio/video/data** but requires signaling + STUN/TURN servers; direct peer connections are network-topology-dependent, not guaranteed.
- **REST polling vs. WebSockets is context-dependent, not universally right/wrong** — choose by latency requirements, update frequency, and complexity tolerance.
- **HTTP/2 multiplexing** (used by gRPC) allows multiple concurrent streams on one connection, but is still request-response, not event-driven push like WebSockets.
- **Industry standard:** use WebSockets as the default for new real-time projects; retain polling as fallback when WebSockets unavailable.
- **This is corpus-first coverage** of real-time interaction patterns — see [[critical-appraisal]] for known gaps (signaling server implementation, TURN server selection, congestion control in WebRTC).
