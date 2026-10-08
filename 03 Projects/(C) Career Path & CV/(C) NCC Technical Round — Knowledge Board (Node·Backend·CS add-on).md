# NCC Technical Round — Knowledge Board (Node · Backend · CS add-on)

> Companion to the **RN Prep Pack**. Your 55 Q&A are strong but ~90% **backend/Node/CS** — so NCC is clearly probing **full-stack**. This board (1) organizes them, (2) **corrects the errors in your AI-generated notes** (studying wrong facts loses points), (3) fills the **high-probability gaps** they don't cover, and (4) anchors everything to your real work.

> **Honest full-stack framing — say this, don't oversell:** *"My core is mobile / React Native. But I have solid JavaScript/TypeScript fundamentals, I've integrated against microservices and SQL/Supabase in production, I run Docker + Jenkins + SonarQube, and I've actually built a small backend myself — a FastAPI + SQLite service (claude-agentic-os). So I'm genuinely growing full-stack. Deep backend infra like Kubernetes and Kafka I know at concept level."* — This is true and defensible. Do **not** claim deep Node/backend production depth you don't have.

---

## 1. Your study board — the 55 clustered by theme + priority

Rate each: can you **explain it in 60 seconds out loud**? (⭐ = must-nail for a full-stack round)

| # | Cluster | Your Q# | Priority |
|---|---|---|---|
| C1 | **API design** — REST vs GraphQL, REST rules, GraphQL resolvers, over/under-fetching, projection/pagination/field-security | 4–9 | ⭐⭐⭐ |
| C2 | **OOP · SOLID · Design Patterns · DI** — patterns, DI deep-dive, DIP vs DI vs DI-container, clean code | 10–19, 25 | ⭐⭐⭐ |
| C3 | **JS/TS internals** — instance/prototype/inheritance, Set/Map, TS transpile/type-checker/recursive types, arrow vs normal fn, CommonJS vs ESM | 15, 22, 24, 26–29, 38 | ⭐⭐⭐ |
| C4 | **Async & the runtime** — Promise, event loop, call stack, async/await↔Promise, callback→Promise, single vs multi-thread | 30–37, 43 | ⭐⭐⭐ (the #1 JS interview area) |
| C5 | **Memory & GC** — GC mark-sweep/generational, DI↔GC | 20, 21, 39, 40 | ⭐⭐ |
| C6 | **Clean code & testing** — clean-code rules, unit test, mock/stub via DI | 17, 18, 25, 45 | ⭐⭐⭐ |
| C7 | **Data structures & complexity** — Set/Map, DS Big-O, DB execution-plan complexity | 22, 26, 27, 47–49 | ⭐⭐⭐ |
| C8 | **Databases** — MySQL vs Postgres, ACID, indexing, mobile DB | 48–54 | ⭐⭐⭐ |
| C9 | **DevOps & workflow** — Git flow, Docker, Jenkins/SonarQube | 44, 46, 55 | ⭐⭐ |
| C10 | **Paradigms** — FP vs OOP vs Imperative/Declarative | 23, 41, 42 | ⭐ |

**Study order:** C4 → C3 → C1 → C2 → C8 → C7 → C6 → then C5/C9/C10. C4 + C3 are where JS engineers get separated from JS users.

---

## 2. ⚠️ Corrections & sharpenings *(fix these before you repeat them)*

Your notes are mostly good, but these will cost you with a sharp interviewer:

1. **GraphQL's killer weakness has a NAME: the N+1 query problem.** (Your Q6 mentions DataLoader but never names the problem.) One query for a list of users + one query *per user* for their posts = N+1 DB hits. **Fix = DataLoader (batches + caches per request)** or eager-loading/joins. *This is the single most-asked GraphQL interview question — name it.*
2. **MySQL does NOT use "WAL" — that's PostgreSQL's term.** (Your Q40/Q52/Q53 say MySQL uses WAL.) MySQL/InnoDB uses the **redo log** (a write-ahead mechanism) + doublewrite buffer. PostgreSQL uses **WAL**. Say the right term per DB.
3. **The Node.js event loop has PHASES — your Q31/Q32 only describe the browser model.** Senior Node answer: 6 phases — **timers → pending callbacks → poll → check (`setImmediate`) → close** — and **between every phase** the microtask queue drains, with **`process.nextTick` running before Promise microtasks**. Know: `setTimeout(0)` vs `setImmediate` (check phase) vs `process.nextTick` (highest priority). *This distinction is a classic senior filter.*
4. **libuv's thread pool default size = 4** (`UV_THREADPOOL_SIZE`, max 1024). (Your Q43 says "thread pool" but not the number.) That's the concrete detail that shows you actually know it — CPU-bound crypto/fs/dns run there.
5. **Strategy Pattern ≠ Dependency Injection.** (Your Q10 note "Strategy = interface + constructor + setter injection" conflates them.) Strategy = a *behavioral pattern* (swap interchangeable algorithms at runtime). DI = a *technique* to supply dependencies from outside. They **compose** (you often inject a strategy), but they're different concepts. The "3 types of DI" (constructor / setter / interface) is correct — just don't equate it with Strategy.
6. **DI container and Garbage Collector are largely orthogonal** (your Q20 overstates the link). DI **lifetime scopes** (singleton / transient / scoped) control *how long a reference is held*; GC frees an object only when *nothing* references it. A leaked singleton keeps its graph alive → GC can't collect it. So: DI affects *when references drop*, GC does the actual freeing. Don't say "DI helps the GC."
7. **HATEOAS is rarely implemented in practice** (your Q5 lists it as a rule). It's **Richardson Maturity Model Level 3**; most "RESTful" APIs stop at **Level 2** (proper verbs + status codes). Know the term, but say "most real APIs are Level 2."
8. **`arguments` is array-like, not an array** (your Q28 example has a typo `{'0':1,'0':2}` → should be `{'0':1,'1':2}`). It has `length` and indices but **no `.map`/`.filter`** — convert with `Array.from(arguments)` or use rest `...args`.
9. **Complex TS types slow the COMPILER/IDE, not runtime** (sharpen your Q24). Types are fully erased at compile time → zero runtime cost. But deep recursive/conditional types can make `tsc` and your editor slow. Good nuance to mention.

---

## 3. Gap-fill — high-probability topics your 55 don't cover

A full-stack/Node round almost certainly asks some of these. Concise answers:

**Auth (authN) vs Authorization (authZ)** — authN = *who you are* (login); authZ = *what you can do* (permissions/roles). **JWT** = 3 base64 parts `header.payload.signature`; stateless; signature verifies integrity (don't put secrets in the payload — it's readable). **Refresh-token rotation:** short-lived access token + long-lived refresh token; rotate refresh on use. **Token storage:** httpOnly cookie (safe from XSS, needs CSRF protection) vs localStorage (easy but XSS-exposed). *(You used JWT + REST at TalentAxis — anchor here.)*

**API security (name several):** **CORS** (browser cross-origin policy), **CSRF** (forged requests — mitigate with tokens/SameSite cookies), **XSS** (injected scripts — escape output, CSP), **SQL injection** (→ **parameterized queries / prepared statements**, never string-concat SQL), **rate limiting**, input validation, `helmet` for headers, HTTPS.

**Express middleware pattern** — functions `(req, res, next)` chained; call `next()` to pass control. **Error-handling middleware has 4 args** `(err, req, res, next)` and must be registered last. Auth, logging, validation, parsing are all middleware.

**Database indexing (mechanism):** most indexes are **B-tree** → O(log n) lookup. **Composite index** follows the **left-most-prefix rule** (index on `(a,b)` helps `WHERE a` and `WHERE a AND b`, not `WHERE b` alone). **Covering index** = query answered from the index alone (no table lookup). **Trade-off:** indexes speed reads but **slow writes** and cost storage — don't over-index.

**Transaction isolation levels** (know the anomaly table):

| Level | Dirty read | Non-repeatable read | Phantom read |
|---|---|---|---|
| Read Uncommitted | ✅ possible | ✅ | ✅ |
| Read Committed | ❌ | ✅ | ✅ |
| Repeatable Read | ❌ | ❌ | ✅ (Postgres MVCC prevents it too) |
| Serializable | ❌ | ❌ | ❌ |

Postgres default = Read Committed; uses **MVCC** (readers don't block writers). *(Your Q52 touches MVCC — this table is the crisp version.)*

**Caching strategies:** **cache-aside** (app reads cache, on miss loads DB + populates — most common, Redis), **write-through** (write cache+DB together), **write-behind**. Always set a **TTL**. "There are only two hard things: cache invalidation and naming." *(You mention Redis — this is the "how.")*

**Idempotency** — same request repeated = same result, no extra side-effect. **GET/PUT/DELETE are idempotent; POST is not.** For payments/retries, use an **idempotency key** so a retried request doesn't double-charge. *(Ties to your Space360 payment-adjacent work.)*

**Scaling Node** — Node is single-threaded per process. **`cluster`** = fork N processes (one per CPU core) behind a load balancer (PM2 does this). **`worker_threads`** = real threads for CPU-bound work sharing memory. **`child_process`** = spawn separate processes. Use cluster for throughput, worker_threads for heavy computation.

**Streams & backpressure (Node)** — process data in chunks instead of loading it all in memory (files, HTTP). **Backpressure** = when the consumer is slower than the producer; `.pipe()` handles it automatically. Great for large files/video. *(Ties to your NodeMedia streaming.)*

**Message queues (why):** decouple producer/consumer, absorb spikes, retry on failure, async processing. **Kafka** = distributed **log/event-stream**, very high throughput, replayable (analytics/event-sourcing). **RabbitMQ** = traditional **broker** with flexible routing (task queues). *(JD lists Kafka — concept-level is fine.)*

**Pagination — offset vs cursor:** `LIMIT/OFFSET` is simple but slow at large offsets and **unstable** when rows are inserted (items shift). **Cursor/keyset** (`WHERE id > last_id`) is stable and fast for large/real-time lists. *(Your Q9 has OFFSET — cursor is the senior upgrade.)*

**Realtime: WebSockets vs SSE vs polling** — polling = repeated requests (simple, wasteful); **SSE** = server→client one-way stream; **WebSocket** = full-duplex persistent connection (chat, live). *(Ties to your NodeMedia livestream.)*

**Testing pyramid + test doubles:** many **unit** tests (fast, isolated) → fewer **integration** → few **e2e** (slow). **Doubles:** *mock* (verify interactions), *stub* (canned returns), *spy* (record calls), *fake* (working lightweight impl). Structure tests **AAA** (Arrange-Act-Assert). *(Your Q45 + DI-for-testing Q17/Q18 — this is the frame.)*

---

## 4. Map the topics to YOUR real work *(anchor every answer)*

| Topic | Your real anchor |
|---|---|
| REST, JWT, microservices, auth | **TalentAxis** — RN client against **Django/FastAPI microservices**, JWT |
| SQL / Postgres / full-stack / React web | **Space360** — **Supabase (Postgres)**, Turbo monorepo, React web |
| **You built a real backend** | **claude-agentic-os** — **FastAPI + SQLite + React** (your proof of full-stack, not just talk) |
| GraphQL | **Enouvo (Flutter)** — GraphQL in production |
| Docker, CI, quality gates | **Docker + Jenkins + SonarQube** across projects |
| Streams / WebSockets / realtime | **NodeMedia** livestream integration |
| Clean code, mentoring, reviews | **SonarQube gates + mentoring juniors** (SOLID/DRY in review) |

**The move:** when asked a concept, answer the definition in one line, then say *"I used this on…"* — that's what separates mid/senior from junior.

---

## 5. The 15 most-likely questions to drill *(cross-section of your 55 + the gaps)*

1. Explain the **event loop** — and the difference between `setTimeout(0)`, `setImmediate`, and `process.nextTick`. *(§2.3)*
2. **REST vs GraphQL** — and what's the **N+1 problem**? *(C1 + §2.1)*
3. **`async/await` vs Promises** — and how are Promises scheduled (microtask queue)? *(C4)*
4. **Explain Dependency Injection** — and why it makes testing easier. *(C2)*
5. **SOLID** — give one real example of the **D** (Dependency Inversion) or **S** (Single Responsibility). *(C2)*
6. **How do you secure a REST API?** (auth, SQLi, CORS/CSRF/XSS, rate limit) *(§3)*
7. **ACID** — and what are the **isolation levels / read anomalies**? *(C8 + §3)*
8. **How does a database index work**, and when does it hurt? *(§3)*
9. **MySQL vs PostgreSQL** — when each? *(C8)*
10. **Is Node single- or multi-threaded?** How does non-blocking I/O work (libuv, thread pool)? *(C4 + §2.4)*
11. **Design a RESTful API for `users`** — verbs, status codes, pagination, versioning. *(C1)*
12. **`Map` vs `Object`, `Set` — when do you use them?** *(C3/C7)*
13. **Big-O of common data structures** — array vs hash map vs BST. *(C7)*
14. **Arrow vs normal function** — `this`, `arguments`, hoisting, constructor. *(C3)*
15. **How do you write a good unit test?** (AAA, mock/stub, DI, coverage) *(C6)*

**Drill method:** answer each **out loud in 60s**, then add *"I used this on [your project]."* If you can do all 15 that way, you're ready.

---

*Bottom line: your notes are a solid base — I fixed 9 things that were subtly wrong (N+1, MySQL-WAL, event-loop phases, Strategy≠DI, HATEOAS, DI↔GC, etc.) and added the ~14 topics a full-stack round expects but your set skips (auth, API security, indexing, isolation levels, caching, idempotency, Node scaling, streams, queues, cursor pagination, realtime, testing pyramid). Study C4+C3 hardest, anchor every answer to a real project — especially claude-agentic-os as your real full-stack proof — and keep the honest "mobile-core, growing full-stack" framing so you're never caught overclaiming.*
