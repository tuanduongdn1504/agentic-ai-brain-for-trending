# Rate Limiting — scopes, the missing bucket, and "≠ DDoS defense"

## Source

Video technique #1. Verified against OWASP API4:2023 (Unrestricted Resource Consumption), OWASP Denial-of-Service / Bot-Management / Credential-Stuffing cheat sheets, and RFC 6585 (HTTP 429).

## What the video says (accurate parts)

- Rate limiting caps how many requests a client can make per time window (e.g. 100 req / 15 min).
- Apply it at multiple **scopes**: per-endpoint (an expensive `/upload-video` gets a tight limit), per-user/per-IP, and an **overall/global** limit.
- Per-IP alone is defeatable: an attacker spins up many bots, each with its own IP, each under the per-IP cap — so you also need a global limit. *(The video correctly names this DDoS-by-botnet.)*
- Motivations named: brute-force / credential-stuffing on `/login`, and system overload.

## Canonical corrections

1. **Rate limiting is NOT DDoS defense (MISLEADING as framed).** It stops *application-layer* abuse at the "requests per minute" scale — brute-force, credential stuffing, scraping, logic-flaw abuse. It does **not** stop *volumetric* DDoS (Gbps-scale). OWASP's DoS cheat sheet is explicit: anti-DoS "cannot be one-step solutions" — volumetric attacks require **upstream CDN / carrier filtering** (Cloudflare, AWS Shield). Rate limiting is one layer, not the answer.

2. **The missing bucket: per-username (moderate omission).** For credential stuffing, the primary bucket is **per-username/account** (independent of source IP) — because a distributed attacker spreads low-volume requests across many IPs while targeting *one* account, sliding under any per-IP cap. OWASP Bot Management mandates **both** per-username **and** per-IP/per-ASN buckets simultaneously. The video's "per-IP + global" is incomplete; a global limit doesn't protect a single targeted account.

3. **The missing architecture: a shared store (major omission).** Multi-instance/load-balanced APIs need rate-limit state in a **shared persistent cache (Redis / Memcached)**. A counter on instance A is useless if instance B handles the next request. This is not optional in production — it's the single most common way naive rate limiting silently fails.

4. **RFC 6585 details (minor).** The correct status is **HTTP 429 Too Many Requests**; `Retry-After` is *SHOULD* (recommended) not *MUST*; 429 responses **must not** be cached by intermediaries.

## Correct model

Rate limiting = one control within **OWASP API4 Unrestricted Resource Consumption**, which *also* includes execution timeouts, memory/payload caps, pagination limits, file-size caps, and third-party spend caps. Request-count limiting alone doesn't satisfy API4.

## hireui relevance

- **Recon finding:** rate limiting is **ABSENT** in the hireui frontend repo; login/signup live on the separate backend. This is a real gap on the auth endpoints.
- Design: `POST /auth/login` (per-username **and** per-IP, ~5/15min), expensive/bulk endpoints (per-user quota), a global fallback, **all backed by Redis** — plus a WAF/edge layer for volumetric DDoS (which rate limiting won't cover).

## Key Takeaways

- **Right idea, wrong ceiling:** rate limiting stops app-layer abuse, not volumetric DDoS.
- **Two buckets, not one:** per-username *and* per-IP for credential stuffing; global for scraping.
- **Shared store or it's theatre** in any multi-instance deployment.
- It's one slice of [[what-the-videos-miss-owasp-api-top-10]] API4 — pair it with timeouts, payload caps, and pagination.
