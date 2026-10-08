# 02 — Async & the event loop

Asked in some form in **all five** interviews (JS `Promise`/async-await, Dart `Future`/async-await, and the event-loop internals). This is the single highest-yield conceptual area.

## Why async at all

- JavaScript (and Dart on its main isolate) is **single-threaded**. Async lets slow work — network, file I/O, timers — run **without blocking** the one thread, keeping the UI responsive.
- ⚠️ The very-junior candidate (video 3) answered that "asynchronous" means *data types not being consistent* — **wrong**. Async is about **not blocking the thread while waiting**, nothing to do with types. This is the misconception to avoid.

## Promise

- An object representing a future value, with **3 states: pending → fulfilled | rejected**.
- Constructed with `(resolve, reject)`; consume with `.then(value => …)` and `.catch(err => …)`, `.finally(…)`.
- Solves **callback hell** (deeply nested callbacks) by making async composable and giving one error channel.
- The strong candidate (video 5) described resolve/reject + `.then`/`.catch` accurately — a model answer.

## async / await

- `async` marks a function that **always returns a Promise**. `await` **pauses that function** until the awaited Promise settles, then yields its value — while the event loop runs other code in the meantime (non-blocking).
- It is **syntactic sugar over Promises** — same mechanism, more readable (reads like synchronous code; error handling via `try/catch` instead of `.catch`). ⚠️ It is *not* a replacement for Promises and (in modern engines) *not* implemented "via generators" you need to reason about — treat it as sugar on Promises.
- Dart is identical in shape: mark the function `async`, `await` a `Future<T>`, the function returns a `Future`. `Future<T>` = Dart's Promise; a `Stream` = a sequence of async values over time.

## The event loop (the "how")

The mechanism that lets single-threaded JS be non-blocking:

1. **Call stack** — LIFO; holds the currently-executing function calls **and their local variables**. ⚠️ Correction: local variables live on the **stack**, *objects* live on the **heap** (one candidate said variables live in the heap — wrong).
2. **Web APIs** (browser) / platform APIs — `setTimeout`, `fetch`, DOM events, timers. These run **outside** the JS engine; when done they hand a callback to a queue.
3. **Task queues** — the **macrotask** queue (`setTimeout`, I/O, UI events) and the **microtask** queue (resolved Promise callbacks, `queueMicrotask`).
4. **Event loop** — when the call stack is empty, it drains **all microtasks first**, then takes **one macrotask**, then repeats. This microtask-priority is why a resolved-Promise `.then` runs before a `setTimeout(…, 0)`.

The candidate (video 5) got the stack-empty → dequeue → execute loop but **missed the micro/macrotask split** — knowing that split is what separates a solid answer from a great one.

## Dart `Future` specifics

- `Future<T>` = a value available now/later/never. Created by async work (network, `Future.delayed`, file I/O). Consume with `await` (inside `async`) or `.then()`/`.catchError()`.
- In Flutter, `FutureBuilder` renders loading/error/data states off a `Future` without manual `setState`.

## Model answer template (for "explain async/await")

> "The runtime is single-threaded, so blocking on I/O would freeze the UI. A `Promise` (JS) / `Future` (Dart) represents a value that'll arrive later, with pending/fulfilled/rejected states. `async`/`await` is sugar over Promises: `await` pauses my function until the Promise settles and gives me the value, while the event loop keeps running other work. The event loop drains microtasks (Promise callbacks) before the next macrotask (`setTimeout`), which is why Promise continuations beat `setTimeout(0)`."

## Key Takeaways

- Async = **don't block the single thread**, not "type mismatch".
- **async/await is sugar over Promises**; an `async` function returns a Promise/Future.
- Event loop: **call stack (functions + locals) → web/platform APIs → micro before macro task queue**.
- **Local variables → stack; objects → heap.**

**Sources:** videos 5 (Dzto), 1 (OVN), 2 (aKMV), 4 (PVO5), 3 (0n8o). Related: [[01-javascript-core]] · [[04-flutter-and-dart]] · [[nodejs-backend-interview/02-async-promises-event-loop]].
