# NCC Mock Interview — Completed (autopilot answer key)

> You answered **Q1 & Q2 live (both Strong)**, then went to sleep. I finished the mock on autopilot. **Q3–Q18 + behavioral below are the model "answer key"** — what a *Strong* answer contains, the trap to avoid, and an anchor to your real work. Study/rehearse against these tomorrow (say each out loud in ~60s, ending with *"I used this on [project]"*).
>
> **Honest note:** I can only *grade* Q1–Q2 (your real answers). Q3–Q18 are reference answers, not a score of your performance.

---

## Live results (your real answers)

- **Q1 — Map vs Object · STRONG.** Nailed the object-key-coercion bite + SameValueZero. Fix carried: *JS Map IS insertion-ordered; objects order integer-like keys numerically first.*
- **Q2 — Arrow vs normal `this` · STRONG.** Full call-site rules + lexical `this` + `.map()`/React examples. Completion carried: *arrows also have no `arguments` and no `prototype`.*

You're strong on JS fundamentals. The rest is the reference key.

---

## Area 2 — Async & the event loop

**Q3 — Predict the output + `process.nextTick`.**
```js
console.log(1);
setTimeout(() => console.log(2), 0);
Promise.resolve().then(() => console.log(3));
console.log(4);
```
- **Answer: `1, 4, 3, 2`.** Sync first (`1`, `4`) → call stack empties → **all microtasks drain** (Promise `.then` → `3`) → **then one macrotask** (`setTimeout` → `2`).
- **Node `process.nextTick(() => console.log(5))`:** the **nextTick queue runs before the Promise microtask queue** → order becomes **`1, 4, 5, 3, 2`**. (nextTick is the highest-priority queue in Node.)
- **Trap:** thinking `setTimeout(…,0)` runs before the Promise. It never does — microtasks beat macrotasks.

**Q4 — What do Promises solve?**
- Strong answer names: **callback hell** (nesting), **inversion-of-control trust** (a callback called too early / too late / twice), **unified error handling** (`.catch`), and **composition** (`Promise.all` / `race` / `allSettled`). Foundation for async/await.
- **Trap:** "Promises are faster than callbacks." They're not — they're about *control & readability*.

**Q5 — async/await; parallelize.**
- `async` fn **always returns a Promise** (return→resolved, throw→rejected). `await` suspends the fn until the Promise settles, yielding to the loop. **Sugar over `.then()`.** `try/catch` for errors.
- **Two independent awaits run in parallel with `Promise.all([a(), b()])`** — sequential `await a(); await b();` serializes them.
- **Dart:** `Future<T>` = one async value; `Stream<T>` = many over time; `FutureBuilder` renders loading/error/data.

---

## Area 3 — Node/JS runtime internals

**Q6 — Single-threaded, yet non-blocking I/O — how?** *(the "should know this" question)*
- JS runs on **one thread**; **I/O is delegated to libuv**. Filesystem / DNS / crypto use a **thread pool (default 4, `UV_THREADPOOL_SIZE`)**; network uses the OS event mechanism (**epoll/kqueue**). `fs.readFile` offloads and **returns immediately** → the next sync line runs first → the callback is queued (poll phase) and runs when the stack is empty. Reactor pattern.
- **CPU-bound work still blocks** the one thread → offload to **`worker_threads`**.
- **Trap:** "Node is multi-threaded." No — *your JS* is single-threaded; libuv does I/O off-thread.

**Q7 — What is a garbage collector?**
- Frees **unreachable** objects — reachability from roots (**not** reference counting). **V8 is generational:** Scavenge for the young generation, Mark-Sweep-Compact for the old. High allocation churn → more GC pauses (CPU cost).
- **Trap:** "GC uses reference counting" / "variables live in the heap." (Locals live on the **stack**; the heap holds objects.)

---

## Area 4 — React Native / React

**Q8 — Virtual DOM / reconciliation.**
- An in-memory JS tree; on change React **diffs new vs previous** and **patches only the changed nodes**. **Keys** let it match list items across renders (index-as-key breaks on reorder/insert/delete).

**Q9 — Hooks + `useEffect(fn, deps)`.**
- Hooks (React 16.8+; before = class components): `useState`, `useEffect`, `useMemo` (memoize a **value**), `useCallback` (memoize a **function**), `useRef`, `useReducer`, `useContext`.
- **`useEffect` three cases:** no array → every render; `[]` → once on mount (cleanup on unmount); `[a,b]` → mount + when a/b change. **Return = cleanup.**
- **Trap:** missing deps → **stale closures**; unstable object/array dep → infinite loop.

**Q10 — RN architecture: the Bridge vs the New Architecture.** ⭐ *(the #1 senior RN question)*
- Old **Bridge**: async, **JSON-serialized** messages between JS and native → the bottleneck.
- **New Architecture (default, 2026):** **JSI** (C++ layer, JS calls native **directly & synchronously**, no JSON) · **Fabric** (new renderer) · **TurboModules** (lazy-loaded, typed) · **Codegen** (type-safe glue) · **Hermes** (default engine). *"Expo handles the New Architecture for me."*

**Q11 — RN performance.**
- Watch **re-renders** (`React.memo`, `useMemo`, `useCallback`, no inline objects/arrows as props). **Lists → FlatList/FlashList** (`keyExtractor`, `getItemLayout`, `windowSize`), not `.map` in a ScrollView. **Animations → Reanimated** (runs on the **UI thread** via worklets). Hermes for startup. **Measure before optimizing** (React DevTools Profiler, Flipper).
- **Anchor:** your crash-reduction story = reproduce → stack trace → root cause → fix → test.

**Q12 — Ship an app to the stores.** *(your real strength — anchor hard)*
- **Android:** keystore (signing key, **SHA-1/256 fingerprint**) → build a signed **`.aab`** → Play Console testing track (Internal→Closed→Open, note the **20-testers-for-14-days** rule for new accounts) → review → Production. **Back up the keystore.**
- **iOS:** App Store Connect → `.ipa` via `eas build` → Transporter/`eas submit` → TestFlight → review.
- **Anchors:** the **D-U-N-S company-account setup**, the **Space360 Apple rejection → account-deletion fix → TalentAxis first-pass**, OTA via Stallion, **Fastlane** for automation. This is a top-tier "end-to-end ownership" story — lead with it.

---

## Area 5 — Flutter *(your 2nd stack — play the dual-stack card)*

**Q13 — Widget, lifecycle, the ListView-in-Column trap.**
- **Widget** = immutable description of UI; everything is a widget; `build()` returns widgets.
- **Stateless** (immutable, `build()` only) vs **Stateful** (mutable, `setState()` → rebuild).
- **✅ Lifecycle methods live on the `State` class** (`initState → didChangeDependencies → build → didUpdateWidget → dispose`); only `createState()` is on the widget.
- **⚠️ `ListView` inside a `Column`** → both want unbounded height → overflow. Fix: `Expanded(child: ListView)` / `shrinkWrap: true` / `SingleChildScrollView`.
- **State mgmt ladder:** `setState` (local) → **Provider** → **GetX** (you've used it) → **BLoC** (streams, testable, scales). Know *why* you'd pass `setState`: share state across screens.
- **✅ `const` (compile-time) vs `final` (runtime), both immutable** — don't invert it.

---

## Area 6 — API design (full-stack probe)

**Q14 — REST design rules.**
- Agree the **DTO/contract** (no over/under-fetch), correct HTTP **verbs** (not all-POST), proper **status codes**, **statelessness**, **pagination/filtering/sorting** (cursor > offset for large lists), **versioning** (`/v1`), HTTPS + JWT/OAuth. HATEOAS exists (Richardson Level 3) but most APIs are Level 2.

**Q15 — REST vs GraphQL + the N+1 problem.**
- REST = multiple endpoints, server-defined shape, HTTP-cacheable, over/under-fetch. GraphQL = single endpoint, **client-chosen fields** over a typed schema; fixes over/under-fetch **but** adds caching complexity, the **N+1 problem** (→ **DataLoader** batches), query-depth/cost **DoS** (→ persisted/allow-listed queries + field-level authz).
- **Security:** never give an untrusted client raw query power (a hacked frontend could ask for `password`).
- **✅ Origin fact:** GraphQL was built at **Facebook in 2012 for native mobile** (kill over-fetching), *not* "for microservices" — don't repeat that myth.
- **Honest framing:** "REST + SQL is standard and sufficient for most RN apps; I've used GraphQL on Flutter."

---

## Area 7 — Dependency injection (backend-probe centerpiece)

**Q16 — What is DI, and DI vs Dependency Inversion vs DI Container.**
- **DI** = a component **receives** its dependencies from outside (constructor/parameter) instead of `new`-ing them. Repository pattern: `UserService` gets `userRepository` via its constructor.
- **⭐ The *working* reason = testability:** inject a **`FakeUserRepository`** so unit tests run **entirely in RAM** — fast, deterministic, no DB/network. Also inject the **clock** and **randomness** to make time/random testable. *(Lead with this, not "swap A for B" — that's rare.)*
- **Dependency Inversion (SOLID "D")** = high- and low-level modules both depend on **abstractions (interfaces)**, not concretions — the *interface* part.
- **DI Container (IoC)** = framework machinery (NestJS/Spring/tsyringe) that builds + wires the object graph at startup.
- **Signal:** being able to separate these three = strong; conflating them = common miss.

---

## Area 8 — Databases (full-stack probe)

**Q17 — ACID + isolation levels; SQL vs NoSQL.**
- **ACID:** Atomicity (all-or-nothing), Consistency (valid state→valid state), Isolation (concurrent txns don't interfere), Durability (committed = permanent).
- **Isolation levels ↑ / anomalies ↓:** Read Uncommitted (dirty read) → Read Committed (Postgres default) → Repeatable Read → Serializable. Postgres uses **MVCC** (readers don't block writers).
- **SQL** (Postgres/MySQL — relational, ACID, joins) vs **NoSQL** (document/key-value — flexible, horizontal scale). **Redis** = in-memory cache/sessions.
- **Indexing:** mostly **B-tree** (O(log n)); composite indexes follow **left-most-prefix**; indexes speed reads but **slow writes**.
- **Anchors:** Space360 = **Supabase (Postgres)**; TalentAxis = **microservices**; you built a **FastAPI + SQLite** backend (claude-agentic-os).

---

## Area 9 — Engineering practice

**Q18 — Unit testing + Git flow + the merge-conflict red flag.**
- **Unit test** = one unit **in isolation**, fast + deterministic + **in-memory**, no DB/network/real-clock (use **mocks/stubs/fakes** — this is *why* DI exists). **Test pyramid:** many unit > integration > few e2e. Jest/RN Testing Library; flutter_test. *(Postman/clicking ≠ testing.)*
- **Git flow:** feature branch → PR + review + CI → **protected main**; separate **dev/staging/prod**; no direct-to-prod.
- **⚠️ Merge conflicts:** edit to the correct result, **delete the `<<<< ==== >>>>` markers**, `add` + `commit`. **NEVER "rename the file to avoid it"** — instant red flag.
- **SOLID** (explain **S**ingle-responsibility well) · **DRY** (one source of truth). You've used **SonarQube** gates — cite it.

---

## Behavioral (they weight coachability + judgment)

- **Self-intro (~60–90s):** timeline → stack (RN + Flutter) → shipped App Store apps → PSM II → AI-first. Lead with the most relevant.
- **Conflict / slacking teammate:** assume good intent → **1:1 to understand the blocker** → set expectation → document → escalate only if needed. *(Not "I'll work harder / all-nighter.")*
- **Deadline clash:** **flag to stakeholders early + negotiate scope**, then manage time. Ownership ≠ silent sacrifice.
- **Career (1–2yr / 5yr):** **specialize then broaden** — deepen React Native, then add native Kotlin/Swift. Depth before breadth.
- **English:** honest calibration ("reading/writing strong from daily technical docs; speaking improving — here's my plan"). Don't inflate.
- **Questions to ask them:** which stack per project (RN/Flutter/native)? team size you'd help lead? client-communication language? CI/CD & release pipeline? how juniors level up? *(Never "no questions.")*

---

## Scorecard

```
NCC Mock — Results
- JavaScript core .......... STRONG (Q1, Q2 — your real answers)
- Async & event loop ....... [answer key provided — rehearse Q3–Q5]
- Runtime internals ........ [answer key — Q6, Q7]
- React Native / React ..... [answer key — Q8–Q12]  ← your core, anchor hard
- Flutter .................. [answer key — Q13]      ← dual-stack differentiator
- API / DB / DI (backend) .. [answer key — Q14–Q17]  ← "growing full-stack", honest
- Engineering + behavioral . [answer key — Q18 + scenarios]
Soft signal (Q1–Q2): reasoned aloud, precise, self-corrected — excellent.
```

## Tomorrow — the 5 highest-ROI drills *(rehearse out loud, 60s each)*

1. **Q3 event loop** — predict `1,4,3,2` + where `process.nextTick` lands (`1,4,5,3,2`).
2. **Q10 RN New Architecture** — JSI / Fabric / TurboModules / Hermes (your #1 senior RN filter).
3. **Q6 single-thread + non-blocking I/O** — libuv, thread pool of 4.
4. **Q16 DI** — lead with *testability* (inject a fake repo), then DI vs DIP vs container.
5. **Q15 GraphQL N+1** — name the problem + DataLoader; don't repeat the origin myth.

**The one habit that wins the round:** answer the concept in one line, then *"I used this on TalentAxis / Space360 / claude-agentic-os / NodeMedia."* Definition + real anchor = senior.

---

*Autopilot-completed while you slept. Q1–Q2 were your real answers (both Strong); Q3–Q18 are the reference key. Rehearse the 5 drills out loud tomorrow, anchor every answer to a real project, and keep the honest "mobile-core, growing full-stack" framing.*
