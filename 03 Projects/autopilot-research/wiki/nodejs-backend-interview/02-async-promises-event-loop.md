# Async Model — Promises, async/await, promisify, the event loop

Promises and async/await are the backbone of non-blocking Node.js. Understanding why Promises exist, how they interact with the event loop's microtask queue, and how to convert callback-based APIs is crucial for writing performant, readable async code and passing the interview.

## Source

**Interview:** BE Interview Nguyễn Chánh Đạt (YouTube 6OYzD13GtKs, 2026-06-17, ~63 min, Vietnamese).
**Extraction:** `raw/2026-07-31-nodejs-backend-interview.md`.
**Questions covered:** Q5 (Promise problems), Q6 (Promise + event loop), Q7 (async/await), Q8 (promisify).

---

### Q5 — What problems does the Promise mechanism solve?

**Asked:** What problems does the Promise mechanism solve? Can you do the same with callbacks?

**Candidate answered:** Promises handle async ordering — when code needs data from an async function, the code after it waits until it finishes. With callbacks, the code becomes messy and nested (callback hell).

**Interviewer taught:** Confirmed the callback-hell problem: "using too many callbacks makes the code messy."

**Canonical answer:**

Promises solve **four critical problems** with raw callbacks:

1. **Callback hell / Pyramid of doom** — deeply nested callbacks become hard to read and maintain.
2. **Inversion of control (trust)** — with callbacks, you pass control to another function and hope it calls your callback: at the right time (not early/late), the right number of times (not 0 or 2+), with the right value, and handles errors. Promises formalize this contract.
3. **Unified error handling** — callbacks require error-first conventions and manual propagation; Promises have `.catch()` for all rejection paths.
4. **Composability** — `Promise.all/race/allSettled/any` compose multiple async operations; callbacks require manual coordination.

Promises give a **first-class object** representing a future value, with a clean chainable API (`.then()/.catch()/.finally()`). They are the foundation `async/await` is built on.

**Gotcha / red flag:**
> ⚠️ Don't say "Promises are faster than callbacks" — they're not. The win is **readability + safety**, not performance.

---

### Q6 — How is a Promise handled in the event loop? (microtask vs macrotask queue)

**Asked:** How is a Promise handled in the event loop? The interviewer noted: "this one's a bit hard."

**Candidate answered:** Struggled; improvised a muddled example involving recursion, a for-loop creating promises, and resolving values. Admitted he'd read about the event loop but couldn't explain it. The interviewer left it as homework.

**Interviewer taught:** Redirected repeatedly to "the JavaScript **event loop** specifically," but did not fully teach the answer on camera.

**Canonical answer:**

The event loop has **two queues**:

- **Microtask queue** — `.then()` / `.catch()` / `.finally()` callbacks, and code after `await`, as well as `queueMicrotask()` and `process.nextTick()` (Node-specific).
- **Macrotask queue** — timers (`setTimeout`, `setInterval`), I/O callbacks, `setImmediate()` (Node), rendering.

**Execution order (each cycle):**

1. Execute all **synchronous code** on the call stack.
2. Call stack empties → event loop checks **microtask queue**.
3. **Drain ALL microtasks** (not just one) before moving on.
4. Take ONE **macrotask** from the macrotask queue.
5. Potentially **render** if needed.
6. Go back to step 2.

**In Node specifically:**

- `process.nextTick()` callbacks run **before all other microtasks** (even Promise `.then()`).
- The **libuv event loop** has phases: timers → pending → poll → check (`setImmediate`) → close, with microtasks drained **between phases**.

**Key implication:** Promise reactions always run **before timers**, even if the timer was registered first.

**Example:**

```js
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
console.log('4');
```

Output: `1, 4, 3, 2` — the Promise `.then()` (microtask) runs before the timer (macrotask).

**Gotcha / red flag:**
> ⚠️ Don't confuse "Promise reactions are async" with "they run later". They run on the **next microtask flush**, which is very soon (after the call stack is clear) — not after all other code.

---

### Q7 — What is async/await fundamentally? Convert an async/await function to .then() form.

**Asked:** What is `async`/`await` fundamentally? The interviewer asked the candidate to convert an `async function getData(): Promise<void>` (with `const data = await fetch(...)`) into `.then()` form.

**Candidate answered:** "async is a Promise." (Correct.) The candidate then converted the sample to roughly the right `.then()` form.

**Interviewer taught:** Confirmed the answer; no major correction.

**Canonical answer:**

- **`async` keyword** makes a function **always return a Promise**. Any return value is **wrapped** in a resolved Promise; a `throw` becomes a **rejected Promise**.
- **`await` keyword** **suspends** the async function until the awaited Promise settles. While suspended, control returns to the event loop. Once the Promise settles, the async function **resumes** with the resolved value (or throws on reject).
- **Underneath, it is syntactic sugar** over `.then()` chains — conceptually a **generator + Promise state machine** (older transpilers used generators; modern engines like V8 implement it **natively**, not by transforming to generators).

**Conversion example:**

```js
// async/await form
async function getData() {
  const data = await fetch('/api/data');
  const json = await data.json();
  console.log(json);
  return json;
}

// Equivalent .then() form
function getData() {
  return fetch('/api/data')
    .then(data => data.json())
    .then(json => {
      console.log(json);
      return json;
    });
}
```

**Sequential vs parallel:**

```js
// Sequential (awaits happen one after another)
const a = await promise1();
const b = await promise2();

// Parallel (both fire immediately, then wait for both)
const [a, b] = await Promise.all([promise1(), promise2()]);
```

**Gotcha / red flag:**
> ⚠️ Don't use sequential awaits when you mean to parallelize. `await a; await b` **serializes** and doubles latency. Use `Promise.all` for independent operations.

---

### Q8 — How do you promisify a callback-style API?

**Asked:** If a function is NOT promise-based (callback-style), how do you make it promise-based?

**Candidate answered:** Didn't understand at first. After the interviewer rephrased, agreed you must **wrap** the callback function inside your own Promise.

**Interviewer taught (rich teaching):** 

- Early Node APIs were **callback-based, not promise-based** (e.g., `fs.readFile` took a callback).
- To modernize, you **wrap the callback fn in a Promise**.
- The **`fs` module HAS a promise API** (`import * as fs from 'fs/promises'` — no callbacks, returns Promises directly).
- The **`net` / networking module does NOT** — network programmers must **promisify** callback functions.
- There's a **design reason** `net` stays callback-based (likely efficiency for high-concurrency scenarios).
- Converting callback code to Promises "involves a lot": **call stack** behavior, **stack overflow** from recursion, and *when callbacks get pushed onto the call stack* — "a bit magical" and uncomfortable for someone coming from C/C++/Python/Java.

**Canonical answer:**

Promisify wraps an **error-first callback** (Node convention: `(err, result) => ...`) inside a Promise:

```js
const readFileP = (path) => new Promise((resolve, reject) =>
  fs.readFile(path, (err, data) => err ? reject(err) : resolve(data))
);
```

Node ships **`util.promisify`** for exactly this:

```js
import { promisify } from 'util';
import fs from 'fs';

const readFileP = promisify(fs.readFile);
readFileP('/path/to/file').then(data => console.log(data));
```

**Modern Node APIs:**

- **`fs/promises`** — fully promise-native; import `import * as fs from 'fs/promises'` and all methods return Promises.
- **`timers/promises`** — `setTimeout` as a Promise: `import { setTimeout } from 'timers/promises'`.
- **`net` / `http`** — stay **EventEmitter**-based and callback-heavy (no promise API). You **must wrap them** if you want Promises.

**Key rule:** **Error-first convention** — callbacks take `(err, result)`. If `err` is null, call succeeded; otherwise it failed. Promisify checks the `err` parameter and rejects the Promise if truthy.

**Gotcha / red flag:**
> ⚠️ Not all callbacks are error-first (e.g., array `.map()` callback is just `(item) => ...`). Promisify works for error-first **only**. Read the API docs to be sure.

---

## Key takeaways

- **Promises solve callback hell and inversion-of-control problems** — they provide a first-class object for a future value with a clean API and built-in composition.
- **Microtask queue (Promises) drains before macrotask queue (timers)** — Promise reactions are prioritized over `setTimeout`, even if the timer was registered first.
- **`async` always returns a Promise; `await` suspends and resumes** — it's syntactic sugar over `.then()` chains.
- **Sequential `await` serializes; use `Promise.all` to parallelize** independent operations.
- **Promisify wraps error-first callbacks in a Promise** — Node's `util.promisify` automates this. `fs/promises` exists; `net` does not.
- **`fs/promises` is modern; `net`, `http`, and streams stay callback/EventEmitter-based** — you'll promisify the latter often.

---

## Interviewer red flags (what to avoid saying)

- **"Promises are faster than callbacks"** — wrong reason. The win is readability and error handling, not speed.
- **"Promise reactions run at the end of the event loop"** — imprecise. They run on the **next microtask flush**, which is very soon (before macrotasks).
- **"I'll use `await` everywhere instead of `Promise.all`"** — causes unnecessary serialization. Parallelize independent operations.
- **"I'll promisify this EventEmitter API with `util.promisify`"** — `promisify` only works on error-first callbacks. For EventEmitter, wrap with Promises manually or use `.on('event', ...)` with a resolve/reject gate.

