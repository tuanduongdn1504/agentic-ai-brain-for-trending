# Study guide & gaps — the fastest path to interview-ready

Ranked by **how often it was asked across the 5 interviews × how often candidates failed it**. Drill the top block first. Each item: the question → a 20-second model answer → a drill.

## Tier 1 — asked in 3+ interviews AND frequently failed (drill these first)

### 1. Transform an array / remove duplicates (live coding)
- **Q:** "Add / sort / dedupe this array." Asked in 3 interviews; candidates froze or forgot the API.
- **Answer:** dedupe `[...new Set(arr)]`; sort desc `arr.sort((a,b)=>b-a)`; transform `arr.map(x=>…)`; filter `arr.filter(p)`. Dart: `list.toSet().toList()`, `list.sort((a,b)=>b.compareTo(a))`.
- **Drill:** from a blank editor, in 60s: dedupe, sort descending, and map-double an array. Repeat until reflexive.

### 2. async / await + the event loop
- **Q:** "What is async/await? Why async? How does the event loop work?" Asked in all 5; one candidate confused async with "type mismatch".
- **Answer:** single thread → don't block on I/O. Promise/Future = pending→fulfilled→rejected. `async/await` is **sugar over Promises**; `await` pauses the function, event loop runs other work. Loop: call stack empty → drain **microtasks (Promises)** → one **macrotask (setTimeout)**.
- **Drill:** predict the log order of a `console.log` + `setTimeout(…,0)` + `Promise.resolve().then(…)` snippet. ([[02-async-and-event-loop]])

### 3. `const` vs `final` (Dart) / type modifiers vs types
- **Q:** Asked in both Flutter interviews; one candidate had it **backwards**.
- **Answer:** `const` = compile-time constant; `final` = assigned once at runtime; both immutable. `final`/`const`/`static` are **modifiers, not data types**.
- **Drill:** say aloud why `final now = DateTime.now()` works but `const now = DateTime.now()` doesn't.

### 4. Widget lifecycle + StatelessWidget vs StatefulWidget (Flutter)
- **Q:** Asked in both Flutter interviews; candidates listed widget *names* instead of lifecycle methods.
- **Answer:** Stateless = immutable, `build()` only. Stateful = mutable state; `setState()` → rebuild. Lifecycle (on the **State** class): `initState()` (once) → `build()` (each render) → `dispose()` (cleanup). Only `createState()` is on the StatefulWidget.
- **Drill:** name the 3 core State methods and when each fires. ([[04-flutter-and-dart]])

### 5. Merge conflicts + rebase vs merge (Git)
- **Q:** Asked in videos 1 & 2; **both** candidates gave a dangerous answer (one "renames the file").
- **Answer:** conflict = same lines changed; resolve by editing the `<<<< ==== >>>>` markers, then `git add`+`commit`. **Never rename to dodge it.** rebase = linear history (replay commits); merge = merge commit; don't rebase shared/pushed history.
- **Drill:** describe out loud the 5 steps to resolve a conflict. ([[07-git-testing-and-engineering-practice]])

## Tier 2 — asked in 2+ interviews (know cold)

- **`==` vs `===`** — strict avoids coercion; always `===`. ([[01-javascript-core]])
- **`null` vs `undefined`** — intentional-empty vs default-absence; `null` is valid JSON.
- **Data types** — JS 7 primitives; Dart `int/double/String/bool` + `List/Set/Map`.
- **ListView inside a Column** — unbounded-height overflow → `Expanded` / `shrinkWrap`. ([[04-flutter-and-dart]])
- **Container vs SizedBox** — Container = SizedBox + decoration.
- **Higher-order functions** — take/return a function; `map/filter/reduce`. ([[01-javascript-core]])
- **spread `...`** — merge/clone/add; be able to *use* it, not just recognise it.
- **HTTP client** — Axios (interceptors) vs fetch (built-in). ([[05-react-native-and-mobile-deployment]])
- **Behavioral: strengths/weaknesses, career plan, team conflict** — specialise-then-broaden; communicate-not-all-nighter. ([[08-behavioral-and-interview-craft]])

## Tier 3 — stack-specific depth

- **React:** Virtual DOM diff/patch · hooks + **useEffect's 3 dependency-array cases** · useMemo (value) vs useCallback (function) · SPA vs CSR/SSR. ([[03-react-and-hooks]])
- **Flutter:** BuildContext · MainAxis/CrossAxis · navigation push/pop · state mgmt (Provider/GetX/BLoC). ([[04-flutter-and-dart]])
- **React Native / mobile:** Play Store pipeline (keystore→`.aab`→review) · Fastlane · REST vs GraphQL. ([[05-react-native-and-mobile-deployment]])
- **CSS:** Flexbox (1D) vs Grid (2D) · `flex:1` shorthand · `position` values vs offset props. ([[06-css-html-and-web-fundamentals]])

## The recurring failure modes (don't be these)

1. **Modifiers listed as types** (`final`/`const`/`static`).
2. **Can't transform an array under pressure** — forgets `Set`/spread.
3. **Names widgets instead of explaining the lifecycle.**
4. **"Fixes" merge conflicts by renaming the file.**
5. **Recognises but has never used** spread / `?.` / a state-mgmt lib.
6. **Behavioral default = "I'll work harder / pull an all-nighter"** instead of communicate/negotiate/escalate.
7. **Confuses async with type issues; confuses CSR/SSR with MVC; confuses `position` values with offset properties.**

## The 5-hour plan

1. **Tier 1** (2h) — code the array drills + say the async/const-final/lifecycle/conflict answers out loud.
2. **Your stack's article** (1.5h) — React *or* Flutter *or* RN, plus [[01-javascript-core]] + [[02-async-and-event-loop]] (shared by all).
3. **[[07-git-testing-and-engineering-practice]] + [[08-behavioral-and-interview-craft]]** (1h) — Git hygiene + scenario answers.
4. **Mock** (0.5h) — have someone (or the [[hireui-relevance|cheatsheet agent]]) fire Tier-1 questions and probe "why".

**Sources:** cross-interview synthesis of all 5 videos. Back to [[_index]].
