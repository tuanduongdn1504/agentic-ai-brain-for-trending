# GraphQL

A query language + schema that lets the **client** request exactly the fields it needs — directly solving REST's [[overview|over- and underfetching]] (LetDiv, ByteByteGo). The hype: "perfect data every time." The caution: caching gets harder, queries can crash your database, and the upfront tooling investment may not be worth it for simple CRUD.

## The core mechanism

- **Schema** — server defines all available types, fields, and relationships (like a contract)
- **Query language** — client writes a query naming exactly the fields it wants (not server-predefined endpoints)
- **Single endpoint** — all queries POST to one URL (e.g., `/graphql`), not multiple REST routes
- **Response shape matches request** — if you ask for `user { name email }`, you get exactly that, nothing extra (no overfetching)
- **GraphQL Playground** — interactive web IDE where developers test queries + explore the schema (self-documenting, beloved by LetDiv and Codist)

## The appeal: solving REST inefficiency

| Problem | REST | GraphQL |
|---|---|---|
| **Overfetching** | Server returns `/users/123` with 20 fields; client needs 3 | Client requests exactly 3 fields; response is tiny |
| **Underfetching** | Client needs user + their posts + post comments; requires 3 separate calls | One query fetches all three in a single round-trip |
| **Flexibility** | Adding a new field to the response requires server change | Client can ask for the field if schema includes it; zero server changes needed |

This is genuinely powerful for **mobile clients** and **frontend-driven development** — the frontend engineer can iterate on data needs without coordinating with the backend (Codist, LetDiv).

## The ByteByteGo cautions: real costs (C2, C3)

### 1. Caching is different, not just "harder"

- **The problem:** GraphQL uses POST by default, which doesn't leverage browser/CDN GET-based caching ✓ (ByteByteGo, confirmed)
- **The nuance:** REST with GET also sends no request body; GraphQL POSTs queries as the body, so standard HTTP caching sees every query as a "different request"
- **The solution exists:** Industry-standard **persisted queries** (Apollo, Hasura) + **Automatic Persisted Queries (APQ)** replace query bodies with hashes, enabling GET-equivalent caching via URL parameters. Caching is different, not inherently harder, but requires deliberate setup (ByteByteGo does NOT mention these — gap in the source) (C2)
- **Practical implication:** You WILL need client-side caching + a caching layer (Redis, CDN proxy) to match REST's cache hit rates

### 2. Query DoS / "unexpected table scans"

- **The risk:** A client sends a deeply nested query (e.g., 10 levels of nested user → friends → posts → comments → likes) that triggers a database table scan, consuming all server resources
- **Real impact:** 80% of GraphQL APIs are vulnerable to this (Markaicode 2025, verified in C3); tested payloads show 10-level nesting causing 442ms+ delays or timeouts
- **Mitigation:** 
  - **Depth limiting** — reject queries deeper than N levels (e.g., N=3)
  - **Query cost analysis** — assign "cost units" to each field; reject queries above cost budget (e.g., cost("user.posts") = 10, cost("post.comments") = 5; max query cost = 100)
  - Rate limiting + field-level authorization as complementary layers, not replacements
- **Note:** Schema design matters — circular relationships (user → friends → user...) make you more vulnerable; flat schemas reduce attack surface (C3)

### 3. Upfront tooling is non-trivial

- Simple CRUD endpoints? REST wins. GraphQL setup includes schema validation, cost analysis, depth guards, caching layer — overhead not justified for CRUD
- Complex, interconnected data? GraphQL wins. The flexibility pays for itself
- **Honest middle:** If your API is mostly simple reads with occasional complex queries, a hybrid (REST for CRUD + GraphQL for analytics/deeply-related-data) may be best (ByteByteGo hints at this; not stated explicitly)

## The "perfect data" trap

LetDiv and Codist emphasize the elegance of requesting exactly what you need. True. ByteByteGo emphasizes that you MUST budget for the complexity: query cost limits, depth guards, separate caching strategy, monitoring query patterns to catch slow queries. The first perspective is what sells; the second is what ships.

## Key Takeaways

- GraphQL solves REST's over/underfetching by letting clients request exactly the fields they need in a single query
- Caching is different from REST (POST by default), but persisted queries + APQ enable HTTP-layer caching; client-side caching is still critical
- Deeply nested queries can cause database table scans; mitigate with depth limits + query cost analysis (mandatory for production)
- GraphQL Playground provides excellent developer experience and schema introspection
- Upfront investment (cost analysis, guards, caching layer) is only justified for complex, interconnected data; simple CRUD applications rarely justify the cost
- Verdict: powerful for frontend-driven iteration + mobile-optimized APIs; use caution on database-heavy workloads without proper safeguards

## Cross-references

- **Sibling articles:** [[overview|API Architecture Overview]], [[rest-and-web-api]], [[grpc-and-rpc]], [[http-semantics-and-rest-conventions]], [[selection-framework]]
- **API security implications:** [[api-security-7-techniques/_index]] covers authentication, authorization, and rate limiting — all necessary when protecting a GraphQL endpoint from the DoS vectors described above
- **Corpus:** hireui product code does not yet use GraphQL — when a recruitment SaaS begins exposing candidate data to frontends, GraphQL's client-flexibility may become valuable; REST's simplicity is still the default
- **Real-world implementation:** [[mosh-ai-powered-apps/_index]] uses REST for Claude API calls; a production recruitment SaaS might use GraphQL for complex candidate-job-match queries

## Sources

- **(LetDiv)** Học Lập Trình Đảm Bảo, "7 Loại API Bạn Phải Biết: Giải Thích Đơn Giản 9 Phút!" (2026-07-17)
- **(ByteByteGo)** "What Is GraphQL? REST vs. GraphQL" (2022-11-10)
- **(Codist)** "Every Type of API Simply Explained in 9 Minutes!" (2025-09-27)
- **C2 verdict:** Apollo GraphQL persisted queries, Hasura caching guide, Stellate APQ implementation
- **C3 verdict:** Imperva GraphQL DoS, Escape.tech security checklist, Markaicode 2025 vulnerability report
