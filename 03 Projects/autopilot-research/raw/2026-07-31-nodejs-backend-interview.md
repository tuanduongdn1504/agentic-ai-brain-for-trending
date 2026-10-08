---
source: yt-dlp (single operator-submitted video; NO NotebookLM, NO yt-search)
topic: nodejs-backend-interview
video_id: 6OYzD13GtKs
video_title: "BE Interview Nguyễn Chánh Đạt"
channel: Tuấn Dương (2 subs, 3 views — tiny personal/training channel)
upload_date: 2026-06-17
duration: 3792s (~63 min)
language: vi (Vietnamese) — auto-captions only (no manual subs); heavy ASR garble
generated: 2026-07-31
path: 5 yt-dlp-only (--write-auto-subs --sub-langs vi → grep/sed/awk dedup → transcript_clean.txt 1224 lines / 52KB → read in full in main loop → this faithful structured extraction)
---
<!-- compiled: 2026-07-31 → wiki/nodejs-backend-interview/ (12 files); Workflow wf_a6a465f8-155; 82C/3CBI/1MIS/0F/0FAB -->

# BE Interview Nguyễn Chánh Đạt — faithful structured extraction

> **What this is:** a real Node.js/backend **internship screening interview**, in Vietnamese, ~63 min. A senior engineer ("anh Hoàng Phạm") technically screens a 4th-year software-engineering student from a Polytechnic university (Đại học Bách Khoa), **Nguyễn Chánh Đạt**, applying for a **Node.js intern** role. A second person (channel owner "anh Tuấn" / Tuấn Dương) observes + handles the HR close. Posted to a 2-subscriber channel, almost certainly as an internal training/review recording.
>
> **Why it's valuable (operator goal = interview prep):** it is a dense, escalating **backend/Node.js question bank** delivered Socratically. The candidate's answers are frequently incomplete or inverted, and the interviewer supplies corrections + real-world framing — so the study payload is the **canonical answers + the interviewer's teaching points**, NOT the candidate's raw answers.
>
> **Reading convention below:**
> - **Q** = question the interviewer actually asked (paraphrased from garbled ASR).
> - **[candidate]** = what the candidate actually answered (faithful summary — may be wrong).
> - **[interviewer]** = the interviewer's actual correction/teaching from the video.
> - **[CANONICAL]** = the correct textbook answer, added by the librarian for study. NOT claimed to be spoken in the video unless it overlaps [interviewer].
> - **⚠️VERIFY** = a claim (usually the interviewer's) that must be refute-first fact-checked before shipping as truth.
>
> **⚠️ ASR garble warning:** the auto-captions mangle nearly every technical term (async→"Singway/Singabaya", GraphQL→"grap q/Graql/RQL", dependency injection→"defensy injection", callback→"comback", call stack→"cost", ESM→"is modal", garbage collector→"máy dòng rác"). Full garble→term map is in the caveats section of the compiled wiki. Interpretations below are the librarian's best faithful reading of intent.

---

## Participants & context

- **Candidate:** Nguyễn Chánh Đạt — 4th-year Software Engineering student, Đại học Bách Khoa (Polytechnic). Found the internship via the company website. Prior work: a **cinema-booking system** (team project, SCRUM) and a **personal to-do-list app**.
- **Interviewer (technical):** "anh Hoàng Phạm" — senior/lead engineer; Socratic style; repeatedly contrasts "textbook / what juniors say" vs "what actually happens in 3–4 years of real work."
- **Observer / HR close:** "anh Tuấn" (Tuấn Dương, channel owner).
- **Role:** Node.js intern (backend). Company takes ~4 interns; trains them toward full-time conversion (not a train-then-leave program); conversion is mutual (company evaluates + candidate chooses), no obligation.
- **Interview philosophy stated up front:** "Answer what you understand. If you don't understand a question, ask me to rephrase. If you know the concept but can't map my wording to it, say so and I'll explain, then you explain your understanding." (A healthy signal to model in a coach.)

---

## The question bank (chronological)

### Q1 — What is the `Map` data structure in JavaScript? How does it differ from `Object`?
- **[candidate]** Map is like an array of objects, each with a key and value; you set/get a value by its key. When pressed on Map-vs-Object: "in JS both are just key→value; Map has convenient methods (set/get)."
- **[interviewer]** Pushed: with a Map you can index straight by the key to get the value; hinted that Object effectively forces string keys ("most of the time you must use a string to define the value") — so Map ≠ Object in a specific way.
- **[CANONICAL]** `Map` = keyed collection where **keys can be ANY type** (objects, functions, NaN), **preserves insertion order**, has `.size`, is **directly iterable** (`for..of`, `.entries()`), and is optimized for frequent add/remove. `Object` keys are only **strings/Symbols**, carries a **prototype** (collision/injection risk), not directly iterable, best as a static record/struct. Methods: `set/get/has/delete/clear`. Rule of thumb: unknown/dynamic or non-string keys → Map; fixed known shape → Object.

### Q2 — What is the `Set` data structure? When do you use it?
- **[candidate]** A collection of distinct elements. Use case: given an array with duplicates, get a unique array. (Correct.)
- **[CANONICAL]** `Set` = collection of **unique values** (any type), insertion-ordered, iterable, ~O(1) `add/has/delete`. Canonical uses: **dedup** `[...new Set(arr)]`, fast membership testing, set algebra. `WeakSet` for GC-friendly object membership.

### Q3 — Difference between arrow functions and normal functions?
- **[candidate]** Explained `this` binding but **INVERTED it**: claimed arrow-function `this` points to the object created from the class, and a normal function's `this` "belongs to the class." (Wrong.)
- **[interviewer]** "That's a bit backwards, but okay." (Accepted without fully re-teaching — a gap the study guide must close.)
- **[CANONICAL — corrects the candidate]** Arrow functions **do NOT have their own `this`**; they capture `this` **lexically** from the enclosing scope at definition time. Normal functions get `this` from the **call-site** (method call → the object; plain call → undefined/global in strict/sloppy; `new` → the new instance; `call/apply/bind` → explicit). Arrow functions also have **no `arguments`**, **no `prototype`**, and **cannot be used with `new`** (not constructors). The candidate's mapping was exactly reversed.

### Q4 — Why do people use arrow functions (not normal functions) as the callback to `.map()`?
- **[candidate]** Could not answer. Interviewer: "don't overthink; I'll come back to it." (Never fully resolved on camera.)
- **[CANONICAL — the intended answer]** (1) **Lexical `this`** — the callback keeps the surrounding `this`, avoiding the classic "lost `this`" bug inside class methods; (2) **conciseness** for short one-liners; (3) **implicit return** (`arr.map(x => x*2)`). Not about performance.

### Q5 — What problems does the Promise mechanism solve?
- **[candidate]** Handles async ordering: e.g. a data-fetch function — the code after it waits until it finishes; covers the case where data isn't ready yet.
- **[interviewer]** "Could you do it with callbacks?" **[candidate]** using too many callbacks makes the code messy ("rất là số" ≈ "very [nested/messy]" — callback hell).
- **[CANONICAL]** Promises solve **callback hell** (deep nesting / pyramid of doom) and the **inversion-of-control** trust problems of raw callbacks (called too early/late/never/multiple times). They give a **first-class object for a future value** (`.then/.catch/.finally`), **composition** (`Promise.all/allSettled/race/any`), **unified error propagation**, and are the foundation `async/await` is built on.

### Q6 — How is a Promise handled in the event loop? *(interviewer: "this one's a bit hard")*
- **[candidate]** Struggled; improvised a muddled example (a function taking `y`, recursion, `.then()`, a `for` loop creating promises, resolving `y+1`, summing a series). Admitted he'd "read about" the event loop but couldn't explain it.
- **[interviewer]** Kept redirecting to "the JavaScript **event loop** specifically." Left it as a go-home-and-study item.
- **[CANONICAL]** Promise reactions (`.then/.catch/.finally` callbacks, and the continuation after `await`) are queued on the **microtask queue**. After the current **synchronous call stack empties**, the event loop **drains ALL microtasks** before taking the next **macrotask** (timers/`setTimeout`, I/O callbacks) and before rendering. So microtasks (Promises, `queueMicrotask`) out-prioritize macrotasks. In Node, `process.nextTick` runs before other microtasks; libuv phases = timers → pending → poll → check(`setImmediate`) → close, with the microtask queue drained between phases.

### Q7 — What is `async`/`await` fundamentally? Convert an `async/await` function to `.then()` form.
- **[candidate]** "async is a Promise." **[interviewer]** "Correct." Candidate then converted a sample `async function getData(): Promise<void>` (with `const data = await fetch(...)`) into `promiseFn().then(data => …)` form — roughly right.
- **[CANONICAL]** `async` makes a function **always return a Promise** (return value is wrapped; a `throw` becomes a rejected Promise). `await` **suspends** the async function until the awaited Promise settles, yielding control back to the event loop, then resumes with the resolved value (or throws on reject). It's **syntactic sugar over `.then()` chains** (generator + Promise machinery underneath). Sequential `await`s serialize; use `Promise.all` to parallelize independent awaits.

### Q8 — If a function is NOT promise-based (callback-style), how do you make it promise-based? (promisify)
- **[candidate]** First didn't understand the question. After the interviewer rephrased, agreed you must **wrap** the callback function inside your own Promise.
- **[interviewer]** Rich teaching: early Node APIs were **callback-based, not promise-based** (e.g., reading a file took a callback). To modernize you **wrap the callback fn in a Promise** ("promisify"). The **`fs` module HAS a promise API** (`import * as fs from 'fs/promises'` — returns promises) but the **`net`/networking module does NOT** — network programmers must promisify a lot; there's a design reason it's callback-based. When you **refactor an old callback codebase**, converting callbacks → promises for readability is "a technique you must have." Fully explaining it "involves a lot": **call stack** ("cost"), **stack overflow** from too much recursion ("đệ quy"), and *when/whether callbacks get pushed onto the call stack alongside the calling function's context* — "a bit magical," and uncomfortable for someone coming from C/C++/Python/Java.
- **[CANONICAL]** Promisify wraps an error-first callback fn:
  ```js
  const readFileP = (path) => new Promise((resolve, reject) =>
    fs.readFile(path, (err, data) => err ? reject(err) : resolve(data)));
  ```
  Node ships **`util.promisify`** for exactly this. Convention: **error-first callbacks** `(err, result)`. `fs/promises` and `timers/promises` are the promise-native cores; many older/event-emitter APIs (`net`, streams) stay callback/event-based.
- **⚠️VERIFY** "`fs` has a promise-based API but `net` does not." (Expect: TRUE — `fs/promises` exists; `net` is EventEmitter/callback-based with no promise API.)

### Q9 — CommonJS vs ES Modules.
- **[candidate]** Syntax differs: CommonJS `require`, ESM `import/export`. ESM "more convenient"; something about being better with singletons/tree-shaking (garbled). Concluded: mainly a syntax difference; performance ~ the same.
- **[interviewer]** Agreed performance is basically identical; some pedants benchmark `require` as marginally faster but it's negligible — "not worth living-and-dying to research."
- **[CANONICAL]** **CommonJS**: `require`/`module.exports`, **synchronous**, **dynamic** runtime resolution, `__dirname`/`__filename` available, the historical Node default. **ESM**: `import`/`export`, **static** structure (enables **tree-shaking** + better static analysis), **asynchronous** loading, **top-level await**, browser-standard; use `import.meta.url` instead of `__dirname`. Interop caveats (ESM can import CJS; CJS can't `require` ESM synchronously). Perf difference negligible for app code; the real ESM win is static analyzability/tree-shaking.
- **⚠️VERIFY** "require slightly faster than import, negligible." (Expect: CORRECT-BUT-INCOMPLETE — startup/resolution nuances exist; negligible in practice.)

### Q10 — What is a garbage collector? *(asked here; answered fully later, tied to DI container)*
- **[candidate]** Recognized the term from a 4-year course but couldn't define it; got confused when the interviewer offered "máy dọn rác" (garbage cleaner) and asked if it related to language processing / compilers.
- **[interviewer — later, lines ~1144-1165]** Tied GC to the DI-container discussion: an object's **lifecycle** — you create it, use it, and once **nothing references it**, the GC is **triggered** and cleans it. If objects are **continuously created and destroyed**, GC runs and **burns CPU cycles → hurts performance**. **Service objects whose state doesn't change** you **register in a DI container**; they stay **always-referenced** (held by the container), so **GC never churns them**.
- **[CANONICAL]** GC = automatic reclamation of **unreachable** objects (reachability from GC roots, **not** literal reference counting). V8 uses a **generational** collector: **Scavenge** (fast, copying) for the young generation, **Mark-Sweep-Compact** for the old generation, run **incrementally/concurrently** to shrink pauses. High allocation churn → more GC pauses → CPU cost; reusing long-lived singletons (e.g., via a container) reduces GC pressure. The interviewer's reachability + churn-cost framing is correct.

### Q11 — Is Node single- or multi-threaded? With ONE thread, how is file I/O non-blocking?
- **[candidate]** "Single thread." Then **could not explain** why the main thread doesn't block on `fs.readFile`, nor why a `console.log` written *after* it prints *before* the file callback.
- **[interviewer]** Set it up precisely: one Node process, one main thread; in C/Java, reading a file **blocks** until done; Node is single-threaded, yet the code below `fs.readFile(...)` keeps running and the callback's data prints **after**. "**Why?**" Said: "This is hard, but I **expect a fresh grad to answer it** — people who've worked years and forgotten the theory get a pass, but you should remember." Left it as homework. (His own phrasing here was also ASR-garbled — "một tay trading" ≈ single-threaded.)
- **[CANONICAL — the intended answer]** Node's **JavaScript runs on one main thread**, but I/O is delegated to **libuv**, which uses the OS's async I/O plus a **thread pool** (default **4 threads**, `UV_THREADPOOL_SIZE`) for filesystem/DNS/crypto/zlib. `fs.readFile` **hands the work to libuv and returns immediately** (non-blocking) → the main thread runs the synchronous code below (so `console.log` prints first). When the read completes, libuv **queues the callback** in the event-loop **poll phase**; the main thread runs it once the **call stack is empty** (so the callback's output prints after). This is the **reactor pattern**: single-threaded event loop + offloaded I/O + callback queue. (CPU-bound work still blocks the one thread → use `worker_threads`.)
- **⚠️VERIFY** libuv default thread-pool size = 4; fs uses the thread pool while network I/O uses OS epoll/kqueue directly.

### Q12 — Describe the git flow you used on the team project.
- **[candidate]** Team used **SCRUM**: split each sprint into tasks/subtasks; **one branch per subtask**; open a **pull request** to review + merge. When pressed "push to WHICH branch / do you separate environments (prod/staging)?" → **only ONE branch; code straight to production.**
- **[interviewer]** Flagged it plainly: "code done → straight to production… ok." (A maturity red flag surfaced, not lectured.)
- **[CANONICAL]** Mature flow: short-lived **feature branches** off `main`/`develop` → **PR + code review + CI** → merge into a **protected main**; **environment separation** dev/staging/prod with promotion; GitHub-Flow or trunk-based for CD, Git-Flow for release trains. **No direct-to-prod.** The single-branch-to-prod pattern is the concrete gap to name in a coach.

### Q13 — Do you know unit testing?
- **[candidate]** Heard of it; **never written one.**
- **[interviewer]** Empathetic but firm: students "just get it done for grades" and ignore tests; many juniors test only via **Postman / manual clicking after deploy** — "that is NOT how you build software properly." Proper software = **everything is testable** (even the compose file). Learn the basics.
- **[CANONICAL]** Unit test = a **small unit in isolation**, **fast**, **deterministic**, **no external dependencies** (DB/network/filesystem) — replace them with **fakes/mocks/stubs**. Test **pyramid**: many unit > fewer integration > few e2e. Tooling: Jest/Vitest/Mocha+Sinon. Manual Postman ≠ automated regression safety.

### Q14 — What is Docker for? Why write a Dockerfile if images already exist? What was in your docker-compose?
- **[candidate]** Build an **image** from your code (Dockerfile) → a **container** so it runs on any machine. Why a Dockerfile: each project has different libraries/deps, so you customize. Wrote a **docker-compose** for a personal to-do app (web UI, list, add/pick-date, delete). When pressed on which **services** were in the compose (DB? web server returning HTML?) → answer was thin.
- **[interviewer]** Accepted it as "experience-level" exposure; probed for services + a DB tier but didn't get a solid answer.
- **[CANONICAL]** **Image** = immutable snapshot (app + deps + runtime) built from a **Dockerfile**; **container** = a running instance of an image. You write a Dockerfile because base images (`node`, `postgres`) are **generic** — you layer **your** code, dependencies, env, and exposed ports on top (reproducible builds). **docker-compose** declares a **multi-container** app (e.g., `app` + `db` + `redis`) with a shared network + volumes. A real to-do app compose has **at least** an app service **and a database service** — the missing-DB-service is the tell.

### Q15 — REST API design rules; REST vs GraphQL. *(long, multi-part)*
- **Q15a — REST vs GraphQL basics.** **[candidate]** REST hits **different endpoints per request**; GraphQL uses **one endpoint** and the **frontend decides the shape/schema** it wants; the backend just maps fields. (Directionally right.)
- **Q15b — REST design rules you follow?** **[candidate]** FE and BE must **agree on the DTO**; the response must have **no extra and no missing** info.
- **Q15c — Do you use all HTTP verbs or POST everything?** **[candidate]** Uses GET/POST/PUT/DELETE (not all-POST). (Correct.)
- **Q15d — GraphQL scenario (over/under-fetching).** Interviewer: `getTodo` returns `{id, title, description, status, tasks}`. Case 1: FE wants only `id`. Case 2: FE wants `id + title + description`. How does BE support the FE choosing fields? **[candidate]** BE builds a schema, maps fields, a resolver returns requested fields; from the DB, **fetch all columns then map** to the requested shape.
- **Q15e — Pros/cons of "fetch-all-then-map" vs "query only requested fields"?** **[candidate]** Fetch-all wastes **network bandwidth** (returns unneeded data). Query-only = FE flexibility, **but** BE must handle many permutations; **ORM-generated queries get hard to control** when you push too much branching logic to cover every request shape.
- **[interviewer] — GraphQL history + the security thesis (the load-bearing teaching):**
  - Claims GraphQL was **created by Facebook**, and its **original intention was NOT the frontend**. He frames it as an **abstraction layer between the web API and backend microservices/services** (web API → Todo Service, etc.), i.e. sitting between **web-API and services**, not between **web-API and frontend**; only **later** did people push it to the frontend to give clients query control.
  - **Security thesis:** letting the **frontend drive the query** is a **security risk** — a **hacked/compromised frontend** could query `password` or anything it wants. So in practice you **don't** give the client free query power: the client passes the **minimum** data, and you return the **minimum necessary** (no more, no less). Big companies are **still experimenting** with GraphQL; it's **not a settled "done-right" thing**.
  - **REST is simpler** because the **contract is server-controlled** — you don't have to involve the frontend; a public API just needs **documentation**. GraphQL, because you cede drive to the client, forces you to **design for whatever the client may ask.**
- **[CANONICAL]** **REST**: resource-oriented, multiple endpoints, **server-defined** responses, HTTP verbs + status codes, HTTP caching; suffers **over/under-fetching**. **GraphQL**: single endpoint, **client-specified** queries over a **typed schema**; fixes over/under-fetching **but** adds **caching complexity**, the **N+1 problem** (needs DataLoader/batching), and **query-depth/complexity DoS** + security (needs **persisted/allow-listed queries**, depth/cost limits, **field-level authorization**). The interviewer's security point is **valid and important** (client-driven queries need strict authz), and his "don't hand raw query power to an untrusted client" advice is sound.
- **⚠️VERIFY (important, likely a correction)** The interviewer's **GraphQL-origin claim** — "built as an abstraction layer between web-API and microservices, **not** for the frontend." Historically **debatable/misleading**: GraphQL was created at **Facebook in 2012** (public 2015) by **Lee Byron, Nick Schrock, Dan Schafer** specifically to power **Facebook's native mobile clients' News Feed** — i.e., **for the client/frontend**, to cut round-trips and over-fetching. So "not for the frontend" is the **opposite** of the usual history. Flag this as the interviewer's personal reframing, not accepted fact.

### Q16 — Design patterns → Dependency Injection (the deep dive, ~20 min). *(the centerpiece)*
- **Warm-up.** **[candidate]** Knows some patterns; gestured at a class extending an interface and overriding methods (garbled — possibly Strategy). Interviewer redirected to **Dependency Injection**.
- **[candidate]'s initial DI model:** class A calls `class1` (which implements an interface) to do a service; to swap `class1 → class2` (both implement the interface) you use an intermediate **config/container** to pick one, initialized via the **constructor**. Asked "what's the application / why do DI?" → "saves time when changing a class/property."
- **[interviewer]'s worked example:** `UserService.createUser` needs the DB → use the **repository pattern** to abstract DB access → `UserService` has a `private readonly userRepository`, initialized in the **constructor**, and `createUser` calls `await userRepository.create(data)`. "Have I done dependency injection? What's missing?"
- **[candidate]** "To be DI you'd have a `UserRepository` class and return `userRepositoryA` or `userRepositoryB`."
- **[interviewer]'s KEY corrections (the gold):**
  1. **The "swap implementation A→B" justification is TRUE but RARE.** In 3–4 years you almost never swap a repository implementation. When you hand juniors DI, their first question is *"why are we doing this?"*, and "you can swap A for B" doesn't convince because it rarely happens.
  2. **The REAL everyday value of DI = faking for unit tests.** Because you inject (ideally through an interface), you can supply a **FakeUserRepository** whose methods are stubbed, guaranteeing your code **never hits the DB/network** — it **runs entirely in RAM**. A unit test **must run very fast and entirely in memory**, calling **nothing external**. So DI's first practical application is **enabling fakes/mocks in unit tests.**
  3. **Terminology untangled (the crux — he says people always conflate these three because they travel together):**
     - **Dependency Injection** = simply **injecting a behavior into something**. Even **without an interface** — just passing a concrete instance via the constructor — you have **ALREADY done DI**.
     - **Functional-programming illustration:** no class/object, just a function. `updateRandom()` calls `random()+5` — hard to test because `random()` is nondeterministic (you could assert a range). Better example: a function that does `new Date()` +1 week — a unit test is **nondeterministic** (different result each day). Fix: **inject the behavior** — make date-creation a **parameter** defaulting to `new Date()`; in the test, inject a **fake date** you control. **FP injects via parameter; OOP injects via constructor.** *That* is dependency injection.
     - **The interface part** (what the candidate described) is **Dependency Inversion** ("đảo chiều phụ thuộc" — inverting the dependency direction), **NOT** dependency injection. DI stops at "inject a behavior into something."
     - **The container** (the "choose A or B" thing) is the **DI Container**: on app startup it **initializes all defined objects into a "box"; when you need one, it pulls it out** — avoiding manual wiring (and, tying to Q10, those held objects stay referenced so **GC won't churn them**).
  4. Loose coupling ("**loosely coupling**") between two components **through the interface/abstraction** = the benefit of Dependency **Inversion**; it lets you swap the later implementation — real, but secondary to the testing payoff.
- **[interviewer] closing:** "Explaining DI well is good — **many people can't.**"
- **[CANONICAL]** The interviewer's tripartite distinction is **correct and unusually well-articulated**:
  - **Dependency Injection (DI):** a component **receives** its dependencies from outside (constructor / setter / parameter / method) instead of `new`-ing them itself. About **how a component gets its collaborators.**
  - **Dependency Inversion Principle (DIP):** the **"D" in SOLID** — high- and low-level modules both depend on **abstractions (interfaces)**, not concretions; abstractions don't depend on details. About the **direction of coupling.**
  - **DI / IoC Container:** framework machinery that **constructs and wires the object graph**, resolving dependencies (NestJS DI, Spring, tsyringe, Awilix).
  - **Everyday payoff = testability** (inject fakes/stubs for fast in-memory unit tests), exactly as he said; implementation-swapping is the textbook-but-rare reason. Injecting the **clock/`Date`** and **`random`** to make tests deterministic is a canonical technique (a.k.a. "humble object" / "inject the clock").
- **⚠️VERIFY** the DI vs DIP vs DI-Container distinction as stated (expect: CONFIRMED — it's textbook-correct and a genuinely strong explanation).

### Close — candidate's questions + logistics
- Candidate asked how many interns the company takes → **~4**. Program **trains toward full-time conversion**; staying is mutual (company evaluation + candidate's choice), no obligation either direction.
- Candidate is **part-time** available (still studying; ~one class day/week); next term = business internship + a project/thesis internship. Interviewer notes he's **"dân Bách Khoa"** (Polytechnic student).

---

## Claims to verify (refute-first targets for the workflow)

1. **GraphQL origin** — interviewer: "made by Facebook as an abstraction layer between web-API and microservices, NOT for the frontend." → check against real history (Facebook 2012, Byron/Schrock/Schafer, built for **mobile clients**). **Likely MISLEADING.**
2. **`fs` has a promise API; `net` does not.** → check (`fs/promises` yes; `net` EventEmitter/callback). **Likely TRUE.**
3. **`require` slightly faster than `import`, negligible.** → check. **Likely CORRECT-BUT-INCOMPLETE.**
4. **Arrow vs normal `this`** — candidate inverted it; confirm the canonical (arrow = lexical `this`, no own `this`).
5. **DI vs Dependency Inversion vs DI Container** distinction as stated. → check. **Likely CONFIRMED.**
6. **Unit tests must run fast + entirely in RAM + no external calls.** → check. **Likely CONFIRMED (canonical unit-test definition).**
7. **libuv thread pool default = 4; fs uses the pool, network uses OS epoll/kqueue.** → check. **Likely CONFIRMED.**
8. **Microtask (Promise) vs macrotask (setTimeout) scheduling; `process.nextTick` highest.** → check. **Likely CONFIRMED.**
9. **V8 GC is generational mark-sweep/scavenge, reachability-based (not refcount).** → check. **Likely CONFIRMED.**
10. **Map keys any type / Object keys strings+symbols; Set uniqueness.** → check. **Likely CONFIRMED.**

---

## Coverage map (topic → article)

- Q1–Q4 → `01-javascript-core.md`
- Q5–Q8 → `02-async-promises-event-loop.md`
- Q9, Q10, Q11 → `03-nodejs-runtime-internals.md`
- Q15 → `04-rest-graphql-api-design.md`
- Q16 → `05-dependency-injection.md`
- Q12, Q13, Q14 → `06-testing-git-docker.md`
- unanswered/struggled (Q4, Q6, Q10, Q11) → `study-guide-and-gaps.md`
