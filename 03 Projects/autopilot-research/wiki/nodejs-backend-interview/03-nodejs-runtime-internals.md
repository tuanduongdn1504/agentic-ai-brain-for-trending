# Node.js Runtime Internals

This article covers the three pillars of Node.js architecture: how modules are loaded and executed, how the garbage collector reclaims memory under load, and the magic that makes a single-threaded JavaScript runtime handle non-blocking I/O. These are the concepts that separate understanding Node from just using it.

## Source

**Interview:** BE Interview Nguyễn Chánh Đạt, YouTube 6OYzD13GtKs, 2026-06-17 (Tuấn Dương channel).

**Raw extraction:** `raw/2026-07-31-nodejs-backend-interview.md`

**Questions covered:** Q9 (CommonJS vs ES Modules), Q10 (garbage collection), Q11 (single-threaded yet non-blocking I/O).

---

## Q9 — CommonJS vs ES Modules

**Asked:** What is the difference between CommonJS (`require`/`module.exports`) and ES Modules (`import`/`export`)? Does one perform better than the other?

**Candidate answered:** Syntax differs: CommonJS uses `require`, ESM uses `import`/`export`. ESM is more convenient. Something about tree-shaking and singletons (garbled). They're mainly a syntax difference; performance is roughly the same.

**Interviewer taught:** Agreed. Performance difference is negligible — some pedants benchmark `require` as marginally faster, but it's not worth "living and dying to research." Not a meaningful concern in practice.

**Canonical answer:**

- **CommonJS** (`require`/`module.exports`): **synchronous**, **dynamic** runtime resolution, exports the full namespace at once. Built into Node early. Has `__dirname` and `__filename` available; every module has its own scope; `module.exports` is the single export point.
  
- **ES Modules** (`import`/`export`): **static** structure (the import graph is known **at parse time**, not runtime), **asynchronous** loading, **top-level await** support, browser-standard. Enables **tree-shaking** (static analyzers remove unused `export`s at build time). Modern standard (official `*.mjs` or `"type": "module"` in `package.json`).

- **Interop caveats:** ESM can `import` CommonJS (treated as a single default export); CommonJS can `require` a *synchronous* ES module (one without top-level `await`) on modern Node, but for an ESM with **top-level `await`** it **cannot** `require` it — you must use dynamic `import()` (returns a Promise).

- **Performance reality:** negligible difference in practice. The gain from tree-shaking is at **build time** (bundler removes code before running), not runtime. Both execute fast once loaded.

> ⚠️ **Gotcha:** The candidate conflated tree-shaking (static analysis benefit) with runtime performance. Tree-shaking happens at build time in your bundler; it doesn't make the running code faster, only smaller.

---

## Q10 — Garbage Collection

**Asked:** What is a garbage collector? (The candidate struggled with the basic definition; the interviewer later tied it to a DI-container discussion.)

**Candidate answered:** Recognized the term from coursework but couldn't define it. Got confused when the interviewer offered the Vietnamese phrase "máy dòn rác" (garbage cleaner) and asked if it related to language processing or compilers.

**Interviewer taught:** An object's **lifecycle** — you create it, use it, and once **nothing references it anymore**, the garbage collector is **triggered** and cleans it up. If objects are **continuously created and destroyed**, the GC runs frequently and **burns CPU cycles**, hurting performance. **Service objects** whose state doesn't change should be **registered in a DI container**, where they stay **always referenced** (held by the container) — this way the **GC never churns them**, avoiding the CPU cost.

**Canonical answer:**

- **GC = automatic reclamation of memory** from **unreachable objects** (objects with no live reference path from GC roots: the call stack, global object, closures). **NOT** reference counting — an object with 100 references but zero reachability is still garbage.

- **V8 (Node's JavaScript engine) uses a generational collector:**
  - **Scavenge** (young generation): fast, copying-based, frequently run. New objects live here.
  - **Mark-Sweep-Compact** (old generation): slower, full-heap. Moves surviving objects here.
  - Generational assumption: **young objects die quickly**; old objects live forever. Most GC work is in the young gen (cheaper).

- **The churn cost:** Every GC pause stops the world (even incremental/concurrent modes). High allocation rate → frequent GC pauses → measurable CPU cost. A request handler that creates 1 MB of temporary objects on every call will trigger GC frequently; if those objects were reused (or avoided), GC pauses shrink.

- **The DI container insight (real everyday win):** Service objects (database connections, loggers, config) are created once and reused for the app's lifetime. If the container **holds a strong reference**, they stay in the **old generation** and GC never touches them. If each request created a new logger, GC would reclaim it after the request — wasted CPU. The interviewer's framing is correct: **holding long-lived objects in a container avoids GC churn**, not because of any GC magic, but because the objects are **never deallocated** (no reclamation = no pause).

> ⚠️ **Gotcha:** Many juniors think GC is a performance tax you must pay. It is — but GC pauses are driven by **allocation rate**, not total memory. A 100 MB app with 1 KB/sec allocation churn pauses far less than a 10 MB app with 10 MB/sec allocation.

---

## Q11 — Single-Threaded Yet Non-Blocking I/O

**Asked:** Node.js is single-threaded, right? If so, how is file I/O non-blocking? Why does `console.log` written *after* `fs.readFile(...)` print *before* the file callback?

**Candidate answered:** "Single thread." Then **could not explain** why `fs.readFile` doesn't block the main thread or why the `console.log` executes before the callback. Admitted it was unclear.

**Interviewer taught:** One Node process, one JavaScript main thread. In C or Java, reading a file **blocks** until done. Node is single-threaded, yet the code below `fs.readFile(...)` keeps running, and the callback's output prints **after**. Asked "Why?" — the candidate had no answer. Interviewer flagged it as something a fresh grad should be able to answer (people with years of experience who forgot the theory get a pass). Left it as homework.

**Canonical answer:**

- **Node's JavaScript executes on one main thread**, but **I/O is not done by that thread** — it's delegated to **libuv**, a C library.

- **libuv's architecture (the reactor pattern):**
  - For **filesystem I/O** (and DNS, crypto, zlib): libuv uses an **OS-independent thread pool** (default **4 threads**, configurable via `UV_THREADPOOL_SIZE` environment variable).
  - For **network I/O** (TCP/UDP sockets): libuv uses the OS's native async mechanisms (`epoll` on Linux, `kqueue` on macOS, `IOCP` on Windows) — **no thread pool**.

- **Why `console.log` prints first:**
  1. `fs.readFile(path, callback)` is called on the main thread.
  2. libuv **receives the work** and **offloads it to a thread pool thread** (or queues it).
  3. `fs.readFile` **returns immediately** — the main thread is **not blocked**.
  4. The next synchronous line (`console.log(...)`) runs right away and **prints** (output to stdout is fast/buffered).
  5. Meanwhile, the file-read thread finishes, and libuv **queues the callback** in the event loop's **poll phase**.
  6. The event loop **drains the call stack** (the `console.log` returns), then **checks the poll queue**.
  7. The **callback is called**, reading the file content and printing it — **after** the `console.log`.

- **Code example:**
  ```js
  const fs = require('fs');
  
  console.log('1. Before readFile');
  fs.readFile('file.txt', (err, data) => {
    console.log('3. Inside callback, file:', data.toString());
  });
  console.log('2. After readFile (before callback)');
  
  // Output:
  // 1. Before readFile
  // 2. After readFile (before callback)
  // 3. Inside callback, file: <contents>
  ```

- **This is the reactor pattern:** one main thread event loop + offloaded work (I/O, CPU tasks) + callback queue. It avoids the need for multithreading at the application level. (If you do CPU-bound work on the main thread, you still block — use `worker_threads` for that.)

- **Thread pool size matters:** The default 4 threads is often enough for moderate I/O concurrency. If 100 file-read requests arrive simultaneously, 4 of them run; 96 queue. When one thread finishes, it picks up the next queued request. On a high-concurrency server, you may tune `UV_THREADPOOL_SIZE=128` or higher (OS limits apply; see `ulimit -n` for file descriptor limits).

> ⚠️ **Gotcha (the candidate's exact gap):** Juniors often think "single-threaded" means "everything blocks." It doesn't. Single-threaded refers to **your JavaScript code**. I/O and async operations are handled by libuv **outside** the main thread, which is the entire point.

---

## Key takeaways

- **CommonJS** is synchronous and dynamic; **ESM** is static and asynchronous. Tree-shaking (ESM's famous win) happens at build time, not runtime. Performance difference is negligible.

- **Garbage collection** reclaims unreachable objects; high allocation churn → frequent GC pauses → CPU cost. Holding long-lived objects in a DI container avoids churn because they're never deallocated.

- **Node is single-threaded at the JavaScript level**, but libuv's thread pool handles filesystem I/O asynchronously. File operations hand work off to a thread pool and return immediately, allowing the main thread to continue running. Callbacks are queued and executed once the call stack empties.

- **The reactor pattern** — event loop + offloaded I/O + callback queue — is the core of Node's non-blocking design. CPU-bound work still blocks; use `worker_threads` for that.

- **`console.log` after `fs.readFile` prints first** because `fs.readFile` is non-blocking: it queues the work and returns, allowing the next line to run. The callback prints only after the main thread's call stack is empty.

---

## Interviewer red flags (what to avoid saying)

- "CommonJS and ES Modules have different performance characteristics" — negligible; this is not a reason to choose one.

- "Single-threaded means everything is slow" or "Node can't do concurrent I/O" — wrong. Concurrency comes from libuv's thread pool, not your code's threads.

- "Garbage collection is magical; I don't need to think about allocation" — false. High churn is a real performance tax. Reuse objects and avoid unnecessary allocations.

- "The callback runs when the file operation finishes" (without explaining why that's **after** the `console.log`) — incomplete. The callback is queued, not run immediately; the event loop drains the call stack first.

---

## Related articles

- [[02-async-promises-event-loop]] — deep dive on microtasks, macrotasks, and the event loop phases that make the callback scheduling work.
- [[01-javascript-core]] — arrow functions and `this` binding, which affect callback behavior.
- [[05-dependency-injection]] — the DI container pattern that was woven through the Q10 GC discussion.
