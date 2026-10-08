# JavaScript Core — Map & Set, arrow vs normal functions

This article covers four foundational JavaScript concepts that reveal **key distinctions lost in casual usage**: when Map beats Object, why Set exists, the this-binding contract between arrow and normal functions, and why arrow functions dominate modern callbacks.

## Source

**Interview:** BE Interview Nguyễn Chánh Đạt (YouTube `6OYzD13GtKs`, uploaded 2026-06-17, ~63 min, Vietnamese)
**Raw extraction:** `raw/2026-07-31-nodejs-backend-interview.md`
**Questions covered:** Q1 (Map vs Object), Q2 (Set + dedup), Q3 (arrow vs normal this-binding), Q4 (arrow in `.map()`)

---

## Q1 — What is the `Map` data structure in JavaScript? How does it differ from `Object`?

**Asked:** How does Map compare to Object as a key-value store?

**Candidate answered:** Map is like an array of objects with key-value pairs; you set/get values by key. When pressed: both are key→value; Map has convenient methods (set/get).

**Interviewer taught:** Pushed on the distinction — with Map you index directly by the key; Object effectively forces string keys, "most of the time you must use a string."

**Canonical answer:** 
- **Map**: keys can be **any type** (objects, functions, NaN); preserves **insertion order**; has `.size`; **directly iterable** (`for..of`, `.entries()`, `.keys()`, `.values()`); optimized for frequent add/remove.
- **Object**: keys only **strings or Symbols**; carries a **prototype chain** (collision/injection risk); **not directly iterable** without `Object.keys()` / `.entries()`; best as a static record/struct with known shape.
- **Method set**: Map has `.set(k, v)`, `.get(k)`, `.has(k)`, `.delete(k)`, `.clear()`. Object uses bracket notation or `Object.defineProperty()`.
- **Rule of thumb**: unknown, dynamic, or non-string keys → Map; fixed known shape → Object.

**Gotcha / red flag:**
> ⚠️ Thinking "both are just key→value" misses the type-safety and collision-avoidance gap. Objects as maps are convenient when you control the keys; Maps are essential when keys come from untrusted input or are complex types.

---

## Q2 — What is the `Set` data structure? When do you use it?

**Asked:** Describe Set and a concrete use case.

**Candidate answered:** A collection of distinct elements. Use case: given an array with duplicates, get a unique array. (Correct.)

**Interviewer taught:** (Minimal teaching provided; candidate's answer was sound.)

**Canonical answer:**
- **Set**: collection of **unique values** (any type); insertion-ordered; **iterable** (`for..of`); ~O(1) `.add(v)`, `.has(v)`, `.delete(v)`, `.clear()`.
- **Canonical uses**: 
  - **Dedup an array**: `const unique = [...new Set(arr)]` (destructure the Set back to an array).
  - **Fast membership testing**: `if (set.has(item))` is O(1) vs array `.includes()` which is O(n).
  - **Set algebra**: intersection, union, difference using filter/forEach.
- **WeakSet**: holds objects only, doesn't prevent garbage collection (for private state or membership registries).

---

## Q3 — Difference between arrow functions and normal functions?

**Asked:** Explain the difference between arrow and normal functions, especially regarding `this`.

**Candidate answered:** Explained `this` binding but **inverted it**: claimed arrow-function `this` points to the object from the class, and a normal function's `this` "belongs to the class." (Wrong.)

**Interviewer taught:** "That's a bit backwards, but okay." (Noted the inversion but did not fully re-teach on camera — a gap this guide closes.)

**Canonical answer (corrects the candidate):**
- **Arrow functions do NOT have their own `this`**. They **capture `this` lexically** from the enclosing scope **at definition time** (the scope in which the arrow was written, not where it's called).
- **Normal functions get `this` from the call-site**:
  - Method call: `obj.method()` → `this === obj`
  - Plain call: `func()` → `this === undefined` (strict) or `globalThis` (sloppy)
  - Constructor call: `new Foo()` → `this === the new instance`
  - Explicit: `func.call(ctx)` / `.apply(ctx)` / `.bind(ctx)` → `this === ctx`
- **Other arrow differences**:
  - No `arguments` object (use rest params `...args` instead)
  - No `.prototype` property (not a constructor)
  - Cannot be used with `new` (will throw)

**Example—the `this` trap:**
```js
class UserService {
  name = "UserService";
  
  // Normal function — this is call-site dependent
  getName() {
    const fn = function() { return this.name; };
    return fn(); // plain call → this === undefined (strict) → ERROR
  }
  
  // Arrow function — this is lexically bound to the class instance
  getNameArrow() {
    const fn = () => this.name;
    return fn(); // arrow sees surrounding this → "UserService"
  }
}

const svc = new UserService();
svc.getNameArrow(); // "UserService" ✓
svc.getName();      // undefined (or error in strict mode) ✗
```

**Gotcha / red flag:**
> ⚠️ The candidate inverted this completely. A junior might claim "arrow functions set this to the object they're called on" (wrong) or "normal functions inherit this from their parent scope" (also wrong). The truth: **arrow = lexical, normal = dynamic (call-site)**.

---

## Q4 — Why do people use arrow functions (not normal functions) as the callback to `.map()`?

**Asked:** Why are arrow functions preferred in `.map()` callbacks?

**Candidate answered:** Could not answer.

**Interviewer taught:** "Don't overthink; I'll come back to it." (Never fully resolved on camera.)

**Canonical answer (the intended answer):**
- **(1) Lexical `this`** — if `.map()` is called inside a method, the arrow callback **preserves the surrounding `this`**, avoiding the classic "lost `this`" bug. Normal function callbacks reset `this` to `undefined` (strict) or the global object.
- **(2) Conciseness** — arrow syntax is shorter, especially for one-liners: `arr.map(x => x * 2)` vs `arr.map(function(x) { return x * 2; })`.
- **(3) Implicit return** — single-expression arrows auto-return: `(x, y) => x + y` vs `function(x, y) { return x + y; }`.
- **Not about performance** — arrow and normal functions compile to the same bytecode.

**Example—the `this` preservation:**
```js
class Processor {
  multiplier = 2;
  
  processArray(arr) {
    // Arrow callback keeps surrounding this (the Processor instance)
    return arr.map(x => x * this.multiplier);
    
    // Normal callback would lose this → undefined → ERROR
    // return arr.map(function(x) { return x * this.multiplier; }); // ✗
  }
}

new Processor().processArray([1, 2, 3]); // [2, 4, 6] ✓
```

**Gotcha / red flag:**
> ⚠️ Saying "arrow functions are faster" or "arrows work better with callbacks" without naming **lexical `this`** misses the real reason — it's the this-binding, not performance or style.

---

## Key takeaways

- **Map vs Object**: use Map when keys are non-string types or unknown at definition time; Object for fixed static shapes.
- **Set = dedup + fast membership**: `new Set(arr)` for unique values; O(1) `.has()` vs O(n) `.includes()`.
- **Arrow `this` is lexical**: captured from the surrounding scope at definition time; cannot be rebound with `.call()/.apply()/.bind()`.
- **Normal function `this` is dynamic**: determined by the call-site (method, constructor, explicit binding, or global/undefined in strict mode).
- **Arrow callbacks preserve `this`**: essential for callbacks inside class methods; avoid the "lost `this`" bug without `.bind()`.
- **Arrow functions have no `arguments`, no `.prototype`, cannot be used with `new`**: they are lighter, simpler, unsuitable as constructors.
- **Implicit return in one-liner arrows**: `(x) => x * 2` is valid; multi-statement arrows need braces and explicit `return`.

---

## Interviewer red flags (what to avoid saying)

- ❌ "Map and Object are basically the same; Map is just more convenient." (Misses type-safety and prototype-collision gaps.)
- ❌ "Arrow functions set `this` to the calling object" or "normal functions inherit `this` from their parent scope." (Inverted; see Q3 example.)
- ❌ "Use arrow functions for performance." (Not the reason; it's about lexical `this` and readability.)
- ❌ "I can't distinguish between Map and Object in real code; I just use Object for everything." (Fragile — non-string keys will silently coerce.)

---

## Cross-links

- [[02-async-promises-event-loop]] — callbacks and promise chains rely on correct `this`-binding.
- [[05-dependency-injection]] — class methods often need `this` to refer to the instance; injected dependencies depend on it.
- [[06-testing-git-docker]] — understanding `this` is critical for unit-testing class methods with mocked callbacks.


