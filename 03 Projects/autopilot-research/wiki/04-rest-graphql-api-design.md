# API Design — REST conventions, REST vs GraphQL, over/under-fetching, ORM trade-offs

REST and GraphQL are two fundamentally different philosophies for API design. REST is simple, server-controlled, and HTTP-semantic; GraphQL is client-driven, flexible, and eliminates over/under-fetching—but at the cost of complexity and security concerns. This article teaches the tradeoffs and the real-world implementation gotchas that interviews probe.

## Source

- **Interview:** BE Interview Nguyễn Chánh Đạt (YouTube 6OYzD13GtKs, 2026-06-17)
- **Raw extraction:** `raw/2026-07-31-nodejs-backend-interview.md`, lines 118–129
- **Questions covered:** Q15 in full — REST vs GraphQL basics (Q15a), REST design rules (Q15b), HTTP verbs (Q15c), over/under-fetching scenario (Q15d), fetch-all-then-map vs query-only tradeoff (Q15e), GraphQL history + security thesis (interviewer teaching).

---

### Q15a — REST vs GraphQL basics

**Asked:** How do REST and GraphQL differ fundamentally?

**Candidate answered:** REST hits different endpoints per request. GraphQL uses a single endpoint and the frontend decides the shape/schema it wants; the backend maps fields.

**Canonical answer:**
- **REST**: **resource-oriented** (each endpoint is a resource), **multiple endpoints** (`/todos`, `/todos/:id`, `/users/:id/todos`), **server-defined response shape** (the endpoint decides what fields to return), HTTP verbs (GET/POST/PUT/DELETE) + status codes, **HTTP caching** via ETag/Last-Modified/Cache-Control.
- **GraphQL**: **single endpoint** (usually `/graphql`), **client-specified query** over a **typed schema**, client says what fields it wants (`query { todo(id: 1) { id title } }`), returns **exactly those fields**, no HTTP verb distinction (typically POST), **custom caching** (query-based, harder for HTTP proxies).

---

### Q15b — REST design rules

**Asked:** What rules do you follow when designing REST APIs?

**Candidate answered:** FE and BE must agree on the DTO; the response must have no extra and no missing info.

**Canonical answer:**
- **API contract = fixed shape**: both sides agree upfront on the response structure (e.g., `{ id: number, title: string, description: string }` — **nothing more, nothing less**).
- **Server-side enforcement**: the endpoint always returns this shape (or a small set of variants controlled by query params, e.g., `?fields=id,title`).
- **HTTP semantics matter**: GET = safe/idempotent/cacheable, POST = create (non-idempotent), PUT = replace (idempotent), DELETE = remove (idempotent), PATCH = partial update. Use the right verb for the right action.
- **No silent over/under-fetching**: the endpoint is **designed for the client's actual needs**—not a generic "fetch everything and the client picks" (that's lazy and sends extra data over the wire).

> ⚠️ **Red flag**: "let's just return all fields and the client picks which to use" — that's not REST design discipline, that's a bulk-return anti-pattern.

---

### Q15c — HTTP verbs

**Asked:** Do you use all HTTP verbs (GET/POST/PUT/DELETE) or just POST for everything?

**Candidate answered:** Uses GET/POST/PUT/DELETE (not all-POST).

**Canonical answer:**
- **GET** = retrieve a resource, idempotent (safe to repeat), cacheable, **no body**.
- **POST** = create a new resource, non-idempotent (each POST may create a new entity), body contains the data.
- **PUT** = replace a resource (idempotent — the same PUT twice produces the same result), body is the full replacement.
- **PATCH** = partial update (idempotent in many cases, but semantically differs from PUT).
- **DELETE** = remove a resource (idempotent).
- Using all verbs correctly is **REST discipline**. All-POST is **lazy**: you lose HTTP semantics, browsers can't cache safely, HTTP proxies can't optimize, and the API is harder to reason about.

---

### Q15d — GraphQL scenario: over/under-fetching

**Asked:** Suppose a `getTodo` resolver can return `{ id, title, description, status, tasks }`. Frontend case 1 wants only `id`. Case 2 wants `id + title + description`. How do you support the frontend choosing fields? What's the tradeoff?

**Candidate answered:** Backend builds a GraphQL schema, maps fields, a resolver returns only the requested fields. **From the DB, fetch all columns then map** to the requested shape.

**Canonical answer:**
- **Over-fetching** = a REST endpoint returns fields you don't need (e.g., `GET /todos/1` returns the full todo with 10 fields, but the client only needs `id`). Wastes bandwidth.
- **Under-fetching** = the endpoint doesn't return enough; the client must make a second call (e.g., `GET /todos/1` returns the todo, but the client then needs `GET /todos/1/tasks` for the tasks). Extra round-trips.
- **GraphQL fixes both**: the client specifies exactly what it wants:
  ```graphql
  query {
    todo(id: 1) {
      id
    }
  }
  # vs
  query {
    todo(id: 1) {
      id
      title
      description
    }
  }
  ```
  The resolver returns **only those fields** — no over-fetching.
- **Implementation tradeoff**: the candidate's approach (fetch all columns from the DB, then map in code) is **simple but wasteful**:
  ```js
  const resolver = (parent, args, context) => {
    const todo = db.query('SELECT * FROM todos WHERE id = ?', args.id); // all columns
    return { id: todo.id, title: todo.title }; // return only what was asked
  };
  ```
  This works when the table is narrow (5–10 columns), but if you're fetching 50 columns just to return 2, that's wasteful at scale.

---

### Q15e — Fetch-all-then-map vs query-only-requested

**Asked:** Compare the tradeoffs: fetching all columns from the DB and mapping in code vs building a query to fetch only requested fields.

**Candidate answered:** Fetch-all wastes **network bandwidth** (returns unneeded data). Query-only = FE flexibility, **but** BE must handle many permutations; **ORM-generated queries get hard to control** when you push too much branching logic.

**Interviewer taught:**
- Fetch-all-then-map is **simple to code** (no branching, one query shape, predictable).
- Query-only-requested is **bandwidth-efficient** (no waste from the DB layer).
- **Real tradeoff**: as you add more field-selection logic, **complexity explodes** (handling every permutation, ORM query control becomes fragile). Big companies **still experiment** with GraphQL; it's **not a solved/settled thing**.

**Canonical answer:**
- **Fetch-all** (simpler, but potentially wasteful):
  ```js
  const todo = await db.todo.findUnique({ where: { id: args.id } }); // Prisma SELECT *
  return todo; // return all fields; resolver picks what client asked for
  ```
  Pros: simple code. Cons: DB returns all columns; bandwidth waste at scale.

- **Query-only** (selective, more complex):
  ```js
  const todo = await db.todo.findUnique({
    where: { id: args.id },
    select: { id: true, title: true } // Prisma: SELECT id, title only
  });
  return todo;
  ```
  Pros: only fetch what you need. Cons: **requires field-aware query building** (Prisma has `select`, raw SQL is error-prone + injection risk).

- **N+1 problem** in GraphQL (not mentioned in the interview, but crucial): if each field is a separate DB query (e.g., a `todo.tasks` field that queries the DB for each todo), a query fetching 100 todos + their tasks becomes 101 queries (the initial todos query + 100 task queries). Solution: **DataLoader / batching** — a separate library that collects N requests and batches them into one.

> ⚠️ **Red flag**: "we'll just fetch everything and map as needed" works for small datasets, but doesn't scale. "We'll dynamically build SQL per query" is a security/maintenance nightmare. Real GraphQL uses field projection + DataLoader + persisted queries.

---

### Q15f — GraphQL history and security thesis (⚠️VERIFY)

**Asked:** [Implied] Where does GraphQL come from? Why is it good / problematic?

**Interviewer taught:**
- GraphQL was **created by Facebook**.
- **Original intention was NOT the frontend**. Instead, it was designed as an **abstraction layer between the web API and backend microservices/services** — i.e., sitting between **web API → Todo Service / User Service** (the services layer), **not** between **web API → frontend**.
- Only **later** did people push it to the frontend to give clients query control.
- **Security thesis (the key correctness point):** letting the **frontend drive the query is a security risk**. A hacked or compromised frontend could query sensitive fields (e.g., `password`). So in practice you **don't** give free query power: the client passes **minimum** data, and you return the **minimum necessary** (no more, no less).
- Big companies are **still experimenting** with GraphQL; it's **not a settled "done-right" thing**.
- **REST is simpler** because the **contract is server-controlled** — the frontend doesn't drive the shape; you just document the API and the frontend calls it. GraphQL cedes query power to the client, so you must **design for whatever the client may ask** (harder to reason about).

**Canonical answer (with VERIFICATION):**

⚠️ **CRITICAL FACT-CHECK:** The interviewer's **GraphQL-origin claim is MISLEADING/INVERTED**.

**Interviewer's claim:**
> GraphQL was built as an abstraction layer between web-API and microservices, **NOT for the frontend**.

**Actual history:**
- GraphQL was created at **Facebook in 2012** (first public release 2015).
- **Creators:** Lee Byron, Nick Schrock, Dan Schafer.
- **Original purpose:** specifically to power **Facebook's native mobile clients' News Feed** — i.e., **for the client/frontend**.
- **Why:** mobile clients needed to be bandwidth-efficient and eliminate over-fetching (because of cellular data costs). REST APIs were returning too much data per request.
- **Conclusion:** GraphQL's origin is **exactly the opposite** of what the interviewer claimed. It was **made for the frontend**, not for microservices abstraction.

**What he may have confused:**
- Some companies (Google, Twitter, Shopify) use GraphQL as an **internal API gateway** — sitting between frontend and internal microservices. But that's a **deployment pattern**, not GraphQL's reason for existing.
- GraphQL the technology is **agnostic** to where it sits (it can front a monolith, microservices, or a mix). The interviewer may conflate **"GraphQL sitting in a microservices architecture"** with **"GraphQL was designed for microservices."**

**The security thesis is VALID and IMPORTANT:**
- If you expose GraphQL directly to an untrusted client (a web browser), that client can attempt to query any field the schema allows.
- **Mitigations** (real companies use these):
  - **Persisted/allow-listed queries** — the client can only send pre-approved query strings, not arbitrary queries.
  - **Field-level authorization** — each field checks if the user is allowed to resolve it.
  - **Query-depth limits** — prevent deeply nested queries that could N+1-bomb the DB.
  - **Query-cost analysis** — assign a "cost" to each field; reject queries that exceed a budget.
- **Conclusion:** the interviewer's rule is **correct**: don't hand raw query power to untrusted clients. You must gate it.

---

## Key takeaways

- **REST** = server-defined contracts, multiple endpoints, HTTP semantics, simple to reason about. Clients may over/under-fetch, but you control the shape.
- **GraphQL** = client-specified queries, single endpoint, fixes over/under-fetching, but adds query complexity, caching challenges, N+1 risk, and **requires strict security gating** (persisted queries, field-level auth, depth/cost limits).
- **REST discipline:** agree on DTOs, use HTTP verbs correctly (GET/POST/PUT/DELETE, not all-POST), return exactly the fields the client needs (no extra).
- **GraphQL implementation:** don't just fetch all columns and map; use field projection (Prisma `select`) + DataLoader for batching + persisted queries for security.
- **Security rule:** never give an untrusted client (web frontend) free GraphQL query power. Use allow-listed queries, field-level authorization, depth limits.
- **GraphQL origin (fact-check):** built by Facebook for mobile clients to solve over/under-fetching (NOT as a microservices abstraction layer, despite some narratives claiming otherwise).
- **GraphQL maturity:** big companies still experiment with how to do it right; it's not a universally "settled" thing—trade-offs are real.

---

## Interviewer red flags (what to avoid saying)

- ❌ "GraphQL was built as a microservices abstraction layer, not for clients." (Opposite of history; confuses a deployment pattern with GraphQL's origin.)
- ❌ "We just fetch all columns and map in the resolver, so the client can request any fields." (Doesn't scale to many columns; wastes DB bandwidth; N+1 risk if nested fields are resolved per-item.)
- ❌ "GraphQL is a strict improvement over REST; I'd use it everywhere." (Overstating; GraphQL has real trade-offs: caching complexity, query-complexity DoS, N+1 risk, security gating burden.)
- ❌ "We let the frontend query any fields it wants in GraphQL without restriction." (Security hole; a hacked frontend could query `password`, `ssn`, or other sensitive data. Must use persisted/allow-listed queries + field-level authorization.)

---

## See also

- [[02-async-promises-event-loop]] — async/await for async API handlers
- [[03-nodejs-runtime-internals]] — event loop and non-blocking I/O in Node
- [[05-dependency-injection]] — injecting repositories and services for testable API layers
- [[06-testing-git-docker]] — testing API endpoints and mocking external dependencies
