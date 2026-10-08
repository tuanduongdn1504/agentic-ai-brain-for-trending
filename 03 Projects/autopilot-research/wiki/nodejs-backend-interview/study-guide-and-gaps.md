# Study Guide & Gaps — the questions that broke the candidate

**Ranked hardest-first (per the workflow's completeness critic). These are the exact questions a real Node.js intern candidate could not answer or got inverted. If you can nail these five cold, you clear the technical bar this interview set. Each has a 30-second model answer + a self-drill prompt.**

For the full treatment of each topic, follow the article links.

---

## Gap 1 (hardest) — Single thread, yet non-blocking I/O

> **Candidate:** completely blank. **Interviewer:** *"I expect a fresh grad to answer this."* → [[03-nodejs-runtime-internals]] Q11

**The question:** Node is single-threaded. So why doesn't `fs.readFile` block? And why does a `console.log` written *after* it print *before* the file callback?

**30-second answer:** Node's **JavaScript** runs on one thread, but I/O is handed to **libuv**. `fs.readFile` offloads the read to libuv's **thread pool** (default 4 threads) and **returns immediately** — so the main thread runs the next line (`console.log`) right away. When the read finishes, libuv queues the callback in the event loop's **poll phase**; it runs only once the call stack is empty. That's why the sync `console.log` prints first and the callback prints second. It's the **reactor pattern**: one JS thread + offloaded I/O + a callback queue. (Network I/O uses the OS's epoll/kqueue directly, not the pool; CPU-bound work still blocks — use `worker_threads`.)

**Drill:** Predict the output of `console.log('a'); fs.readFile('x',()=>console.log('b')); console.log('c');` and explain *each* line's ordering. (Answer: `a`, `c`, `b`.)

---

## Gap 2 — Promises in the event loop (microtask vs macrotask)

> **Candidate:** muddled improvisation, then admitted he couldn't explain it. **Interviewer:** *"this one's a bit hard."* → [[02-async-promises-event-loop]] Q6

**The question:** How is a Promise handled in the event loop?

**30-second answer:** Promise reactions (`.then/.catch/.finally`, and code after `await`) go on the **microtask queue**. After the synchronous call stack empties, the event loop **drains ALL microtasks** before it takes the **next macrotask** (`setTimeout`, I/O callbacks). So a Promise callback always runs **before** a `setTimeout(…, 0)` registered alongside it. In Node, `process.nextTick()` runs before even other microtasks.

**Drill:** What does this print?
```js
console.log(1);
setTimeout(() => console.log(2), 0);
Promise.resolve().then(() => console.log(3));
console.log(4);
```
(Answer: `1, 4, 3, 2` — sync first, then the microtask, then the timer.)

---

## Gap 3 — Why arrow functions in `.map()`

> **Candidate:** complete blank. **Interviewer:** *"don't overthink; I'll come back to it."* → [[01-javascript-core]] Q4

**The question:** Why do people use arrow functions (not `function`) as `.map()` callbacks?

**30-second answer:** The real reason is **lexical `this`** — an arrow callback keeps the surrounding `this`, so inside a class method `arr.map(x => x * this.multiplier)` still sees the instance. A normal-function callback would reset `this` to `undefined` (strict) and break. Secondary reasons: **concise syntax** and **implicit return**. It is *not* about performance.

**Drill:** Rewrite `arr.map(function(x){ return x * this.factor; })` inside a class method so it works, and say *why* the original fails.

---

## Gap 4 — What is a garbage collector

> **Candidate:** recognized the term, couldn't define it. → [[03-nodejs-runtime-internals]] Q10

**30-second answer:** The GC automatically frees memory for objects that are **no longer reachable** from any root (call stack, globals, closures) — reachability, **not** reference counting. V8 is **generational**: fast **Scavenge** for short-lived young objects, **Mark-Sweep-Compact** for the old generation. High allocation churn → frequent GC pauses → CPU cost. That's why you hold long-lived **service objects in a DI container** (always referenced → never churned). *(This is the exact bridge the interviewer drew between Q10 and the DI deep dive.)*

**Drill:** Explain why creating a fresh logger object on every HTTP request is worse for GC than holding one logger in a container.

---

## Gap 5 — Unit testing

> **Candidate:** never written one. **Interviewer:** *"that is NOT how you build software properly."* → [[06-testing-git-docker]] Q13 + [[05-dependency-injection]]

**30-second answer:** A unit test exercises **one unit in isolation**, and must be **fast, deterministic, and entirely in-memory** — **no** database, network, filesystem, or real clock. You replace those with **fakes/mocks/stubs**, which is exactly **why dependency injection exists** (inject a `FakeUserRepository`, inject the clock). Testing by Postman or clicking the UI is manual verification, not regression safety.

**Drill:** Given `UserService.createUser()` that calls a `UserRepository`, describe how you'd unit-test it without touching a database.

---

## The meta-lesson (what the interviewer actually rewards)

The candidate's *knowledge* gaps mattered less than two habits the interviewer prized:

1. **Reason out loud when unsure.** He explicitly gave credit for *"I'm not certain, but here's how I'd think about it."* A blank silence scores worse than a structured guess.
2. **Distinguish textbook-reason from working-reason.** On DI he rejected the memorized answer ("swap A for B") and rewarded the practitioner's answer (testability). On Map/ESM he *deflated* over-researched trivia. Know *why* a thing is used day-to-day, not just its definition.

## The one thing to un-learn from this interview

The interviewer's **GraphQL origin story is wrong** (he said it wasn't built for the frontend; it was — Facebook, 2012, for mobile clients). If you're studying from the raw interview, don't absorb that claim. See [[04-rest-graphql-api-design]] Q15f and [[claims-scorecard]].

---

## Cross-links

- [[overview]] · [[claims-scorecard]] · [[caveats-and-corrections]] · all six topic articles.
- [[data-structures-16-in-32-min/_index]] — the CS-fundamentals companion (arrays/hash/trees) behind these questions.
- [[api-types/_index]] — deeper REST/GraphQL/gRPC taxonomy for Q15.
