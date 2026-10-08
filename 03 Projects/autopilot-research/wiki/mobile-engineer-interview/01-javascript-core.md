# 01 — JavaScript core

The language layer under React and React Native. Asked (in JS or Dart form) in every interview. Model answers below are the verified canonical ones; where a candidate got it wrong it's noted.

## Data types — primitives vs objects

- **7 primitives:** `number`, `string`, `boolean`, `null`, `undefined`, `bigint`, `symbol`. Immutable, no methods of their own (JS auto-boxes for `.method()`).
- **Objects (reference types):** `object`, `array`, `function`, `Date`, etc. Held by reference.
- The strong candidate (video 5) nailed all 7 primitives and the primitive/object split — a clean answer. Weaker candidates listed **modifiers as types** (see Dart `final`/`const`/`static` in [[04-flutter-and-dart]]) — a recurring mistake.

## `null` vs `undefined`

- `undefined` = a variable declared but not assigned, or a function with no `return`. The engine's default "absence".
- `null` = an **intentional** empty value you assign yourself.
- Practical framing that scored well: `null` is a valid JSON value (safe to send to an API/DB); `undefined` is **not** valid JSON.

## `==` vs `===`

- `==` (loose) does **type coercion**: `2 == '2'` → `true`.
- `===` (strict) does **not**: `2 === '2'` → `false`.
- Best practice: always `===` to avoid coercion bugs.

## Higher-order functions

- A function that **takes a function as an argument or returns a function**. Examples: `map`, `filter`, `reduce`, `forEach`, `setTimeout`. The backbone of React patterns and functional array work.
- The very-junior candidate (video 3) had never heard the term — a common early gap; know the definition + name three examples.

## Array transforms — `map` / `filter` / `reduce`, and dedup

- `map(fn)` → **new** array of transformed values (doesn't mutate). `filter(fn)` → new array of matches. `reduce(fn, init)` → folds to a single value via an accumulator `(acc, cur, i, arr)`.
- `map` vs a `for` loop: `map` is declarative and **returns an array**; a `for` loop is control flow that returns nothing by default (you `push` manually) and can mutate.
- **Remove duplicates (asked in videos 1, 2, 4):** `[...new Set(arr)]` — `Set` dedupes, spread turns it back into an array. Alternatives: `arr.filter((x,i)=>arr.indexOf(x)===i)`. Two candidates learned `Set`+spread *during* the interview — drill this until it's reflexive.
- **Reverse a string (video 4):** `str.split('').reverse().join('')` (or `[...str].reverse().join('')`).
- **Palindrome (video 4):** `const c = s.toLowerCase().replace(/[^a-z0-9]/g,''); return c === [...c].reverse().join('')`.

## Spread / rest `...`

- **Spread** unpacks an iterable: merge `[...a, ...b]` / `{...o1, ...o2}`, clone `[...arr]`, add `[...arr, x]`, pass args `fn(...args)`.
- **Rest** collects: `function f(...args)`, `const [first, ...rest] = arr`.
- Several candidates recognised `...` but had never used it — recognising ≠ using is exactly what Tuấn's live coding exposes.

## Shallow vs deep copy

- **Shallow:** copies the top level only; nested objects/arrays still **share references** (spread and `Object.assign` are shallow).
- **Deep:** recursively independent copy. Tools: `structuredClone(obj)` (modern), `JSON.parse(JSON.stringify(obj))` (loses functions/dates), or a library (Lodash `cloneDeep`).

## IIFE (Immediately Invoked Function Expression)

- `(function(){ /* … */ })();` — defined and run at once.
- **Purpose:** create a private scope / avoid polluting the global scope / run setup once. (The candidate knew *what* it does but missed *why* — the scope-privacy point is the answer's core.)

## ES6 essentials (asked as "what's new in ES6?")

`let`/`const` (block scope), arrow functions, template literals, destructuring, classes, default params, **spread/rest**, `Promise`, modules (`import`/`export`), `for…of`. For RN/React the daily-drivers are arrow functions, destructuring, template literals, `const`/`let`, spread. A strong answer names 5–7.

## TypeScript vs JavaScript

- TS is a **superset of JS that adds static typing**, compiled to JS. Benefits: compile-time error catching, IDE autocomplete, self-documenting component props, safer refactors.
- The team-maintainability answer that landed (video 4): in TS you **see a component's prop types immediately**; in plain JS you open the component and read each prop by hand. Costly at scale.
- "I use JS for speed" is a defensible *solo* trade-off but weakens in a team — modern RN/React projects ship `.tsx`.

## Key Takeaways

- Know the **7 primitives**, `null`≠`undefined`, and `===` over `==` cold.
- **Array transforms + `Set`/spread dedup + string reverse** come up repeatedly in live coding — make them reflexive.
- Be able to *use* spread, higher-order functions, and destructuring, not just recognise them.
- TS's value is **types = documentation + safety in a team**, not just "you declare types".

**Sources:** videos 5 (Dzto), 4 (PVO5), 3 (0n8o), 2 (aKMV) — `raw/2026-08-06-mobile-engineer-interview.md`. Related: [[02-async-and-event-loop]] · [[03-react-and-hooks]] · [[nodejs-backend-interview/01-javascript-core]].
