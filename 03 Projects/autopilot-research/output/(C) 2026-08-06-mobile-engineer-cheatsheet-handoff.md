# Mobile Engineer Interview — Cheatsheet & Mock-Interview Handoff
### React Native · React · Flutter · JavaScript/Dart core
> Portable, self-contained brief for another agent/session. Anonymised + question-centric. No vault access needed.

---

## 0. What this is & how to use it

This is a **verified question bank + model-answer cheatsheet** distilled from **5 real Vietnamese mock/screening interviews** for mobile & front-end engineer roles (2 Flutter, 2 React/front-end, 1 React Native), all run by the same interviewer. It has two modes:

- **Cheatsheet mode:** the candidate studies §2–§9 (Q → tight model answer) + §10 (gotchas).
- **Mock-interview mode (agent):** follow §1 — fire questions by the candidate's stack, grade with the rubric, and *probe "why"* after every answer.

**Provenance caveat (state this to the user, don't hide it):** the source captions were doubly-garbled auto-transcription (Vietnamese ASR + machine translation); every technical term was reconstructed and independently verified, but this brief is *derived from real interviews*, not an official spec. Corrections the real interviews got wrong are marked ✅FIX. **This is study material, not a candidate's private record — no real candidate names are included.**

---

## 1. Agent protocol (mock-interview mode)

1. **Ask the candidate their target stack** (React Native / React / Flutter) and rough level (student / junior / ships-to-store).
2. **Always cover the shared core** regardless of stack: §2 JS/Dart core → §3 async → §8 Git/practice → §9 behavioral.
3. **Add the stack module:** React → §4; Flutter → §5; React Native → §6. (§7 CSS/HTML for front-end/React juniors.)
4. **Interviewer method to imitate:** broad concept → **"why?" follow-up** → **live coding** to expose recognise-vs-use gaps. Teach when they're stuck; reward thinking-out-loud + self-correction over confident-wrong recall.
5. **Grade each answer** did-not-know / partial / correct. For a junior/intern verdict, weight **coachability + reasoning** alongside correctness.
6. **End with the gotcha check (§10)** — the failure modes real candidates repeated.
7. **Fabrication guard:** if you don't know something, say so; never invent an "official" answer beyond §2–§10. Cite this brief as the source.

---

## 2. JavaScript / Dart core (ask for EVERY stack)

- **Data types.** JS 7 primitives: `number, string, boolean, null, undefined, bigint, symbol`; everything else is an object (reference type). Dart: `int, double (num), String, bool` + `List, Set, Map`. ⚠️ `final`/`const`/`static` are **modifiers, not types**.
- **`null` vs `undefined` (JS).** `undefined` = declared-not-assigned / no return (engine default). `null` = intentional empty you assign. `null` is valid JSON; `undefined` isn't.
- **`==` vs `===` (JS).** `==` coerces types (`2=='2'`→true); `===` doesn't (`2==='2'`→false). Always `===`.
- **✅FIX `const` vs `final` (Dart).** `const` = **compile-time** constant (value known at compile time, inlinable); `final` = assigned **once at runtime** (`final now = DateTime.now()` works, `const` version fails). **Both immutable.** (A real candidate had this backwards — don't.)
- **Higher-order functions.** Take/return a function: `map`, `filter`, `reduce`, `forEach`, `setTimeout`.
- **Array transforms + dedupe (live-coding favourite).** `map(fn)`→new array; `filter(p)`; `reduce((acc,x)=>…, init)`. **Dedupe: `[...new Set(arr)]`** (Dart `list.toSet().toList()`); sort desc `arr.sort((a,b)=>b-a)`. Reverse a string `s.split('').reverse().join('')`.
- **Spread/rest `...`.** Spread unpacks (`[...a,...b]`, `{...o1,...o2}`, clone, `fn(...args)`); rest collects (`function f(...args)`, `const [x,...rest]=arr`).
- **Shallow vs deep copy.** Shallow (spread/`Object.assign`) shares nested references; deep = independent (`structuredClone`, `JSON.parse(JSON.stringify())`, Lodash `cloneDeep`).
- **IIFE.** `(function(){…})()` — runs immediately; purpose = **private scope / no global pollution**.
- **ES6 (name 5–7).** `let`/`const`, arrow fns, template literals, destructuring, classes, default params, spread, `Promise`, modules, `for…of`.
- **TS vs JS.** TS = JS + static types, compiled to JS. Value = compile-time errors, IDE autocomplete, **prop types visible without opening the component**, safe refactors — matters most in a team.

## 3. Async & the event loop (ask for EVERY stack — highest-yield)

- **Why async.** Single-threaded runtime → don't block the thread on I/O → UI stays responsive. ⚠️ Async is **not** about "type mismatch" (a real candidate's wrong answer).
- **Promise (JS) / Future (Dart).** Object for a future value; states **pending → fulfilled | rejected**; `.then`/`.catch`/`.finally`; solves callback hell.
- **async/await.** `async` fn always returns a Promise/Future; `await` pauses the fn until it settles, event loop runs other work meanwhile. It's **syntactic sugar over Promises**, not a replacement; error handling via `try/catch`.
- **✅FIX Event loop.** **Call stack** holds function calls **+ local variables** (heap holds *objects*). Web/platform APIs (`setTimeout`, `fetch`) run outside the engine → hand callbacks to queues. Loop: stack empty → drain **all microtasks (Promise callbacks) FIRST** → then one **macrotask (`setTimeout`)** → repeat. (Why a resolved-Promise `.then` beats `setTimeout(…,0)`.)
- **Dart:** `Future<T>` = one async value; `Stream<T>` = many over time; `FutureBuilder` renders loading/error/data.

## 4. React module

- **Virtual DOM.** In-memory JS tree; on change, **diff vs previous** and **patch only changed nodes** in the Real DOM → faster than re-rendering everything.
- **JSX.** Sugar for `React.createElement(...)`.
- **Hooks (since React 16.8; before = class components).** `useState`, `useEffect`, `useMemo` (memoise a **value**), `useCallback` (memoise a **function**), `useReducer`, `useContext`, `useRef`.
- **`useEffect(fn, deps)` — 3 cases (ask this):** no array → every render; `[]` → once on mount (cleanup on unmount); `[a,b]` → on mount + when a/b change. Return = cleanup.
- **Lifecycle.** mount → update → unmount (hooks map onto `useEffect`).
- **SPA vs multi-page.** SPA = one shell, JS routing/rendering (React Router), fast nav; multi-page = server renders each page.
- **CSR vs SSR.** CSR = browser renders JS + fetches JSON; SSR = server sends ready HTML (faster first paint + SEO). ⚠️ SSR ≠ MVC (rendering strategy vs code organisation).
- **Also:** folder structure (`pages/components/hooks/services/store/utils/assets`), UI libs (Ant Design leaner vs Material comprehensive), Vue (single-file components) vs React (JSX), file upload (`FormData` + POST).

## 5. Flutter module

- **Widget.** Immutable description of UI; everything is a widget; compose a tree; `build()` returns widgets.
- **Stateless vs Stateful.** Stateless = immutable, `build()` only. Stateful = mutable state; `setState()` → rebuild.
- **✅FIX Lifecycle (methods on the `State` class; only `createState()` on the widget):** `initState()` (once) → `didChangeDependencies()` → `build()` (each render) → `didUpdateWidget()` → `dispose()` (cleanup).
- **BuildContext.** Handle to the widget's location in the tree; reach `Theme.of`, `Navigator.of`, inherited data.
- **Scaffold.** Material page skeleton (`appBar/body/floatingActionButton/drawer/bottomNavigationBar`); not required but convenient.
- **Container vs SizedBox.** SizedBox = size only (spacer/constraint); Container = size + decoration/padding/margin/alignment.
- **⚠️ ListView inside Column (asked a lot).** Both want unbounded height → overflow. Fix: `Expanded(child: ListView)` / `ListView(shrinkWrap:true)` / `SingleChildScrollView`.
- **Row/Column alignment.** MainAxisAlignment = primary axis; CrossAxisAlignment = perpendicular.
- **Navigation.** `Navigator.push(context, MaterialPageRoute(...))` / `pop`; modal via `showDialog`/`showModalBottomSheet` (returns a Future).
- **State management.** `setState` (local) → **Provider** (simple shared) → **GetX** (reactive, minimal) → **BLoC** (streams, testable, scales). Know **why** you'd go past `setState` (share state across screens).
- **Dart collections.** List (ordered, dupes), Set (unique — dedupe), Map (key→value); `map/where/sort/every`. Null ops `??`, `?.`, `??=`, `!`.
- **Pros/cons.** + one codebase, hot reload, good perf; − app size, smaller ecosystem, jank with poor state mgmt.

## 6. React Native + mobile deployment module

- **Android → Play Store pipeline (walk-through):** (1) **keystore** (signing key; **SHA-1/256 fingerprint**) via `keytool`/Android Studio; (2) build & sign as **`.aab`** (App Bundle, Google-preferred, smaller than APK); (3) Play Console app + **testing track** (Internal→Closed→Open) before Production; (4) upload `.aab` + screenshots/description/rating; (5) **review** (hours→~2-3 days; expect policy rejections — fix & resubmit); (6) promote to Production. **Keystore is permanent — back it up** (or use Play App Signing).
- **Fastlane.** Automates build/sign/test/upload (iOS+Android) via Ruby lanes; one command deploys. Ship-by-hand 3× = automate.
- **HTTP client.** Axios (interceptors for auth/retry/error, timeouts, cancel) vs fetch (built-in, more boilerplate); Axios for production.
- **REST vs GraphQL.** REST = fixed endpoints, simple, cache-friendly, may over/under-fetch; GraphQL = single endpoint, client picks fields, fewer round-trips, more setup. **REST + SQL is standard & sufficient for most RN apps.**
- **Career framing that scores:** specialise in RN first, then add native Kotlin/Swift — depth before breadth.

## 7. CSS / HTML / web (front-end & React juniors)

- **Flexbox (1D — row *or* column) vs Grid (2D — rows *and* columns).** The 1D/2D line is the answer.
- **`flex: 1`** = `flex-grow:1; flex-shrink:1; flex-basis:0` (grow to fill, share space equally).
- **CSS `position` values:** `static, relative, absolute, fixed, sticky`. ⚠️ `top/left/bottom/right` are **offset properties**, not position values.
- **`<td>`** = table data cell inside `<tr>` inside `<table>` (pairs with `<th>`).
- **Domain vs hosting.** Domain = human name → IP via **DNS** (lease); hosting = server/disk for files+DB (rent).

## 8. Git, testing & engineering practice (ask for EVERY stack)

- **Workflow.** `status → add → commit → pull (before push) → push`; new branch `git push -u origin <b>`.
- **checkout.** `-b` = create+switch (lowercase); ✅FIX `-B` = create-or-reset (force); `checkout -- <file>` discard; modern `git switch`/`restore`.
- **fetch vs merge vs pull.** fetch = download only (safe); merge = integrate (changes files); pull = fetch+merge.
- **rebase vs merge.** merge = merge commit + branchy history; rebase = replay commits → linear (`rebase -i` to squash/reword). **Don't rebase pushed/shared history.**
- **⚠️ Merge conflicts (RED FLAG check).** Same lines changed → markers `<<<< ==== >>>>`; resolve by **editing to the correct result, delete markers, `add`+`commit`**. **NEVER "rename the file to avoid it"** (a real candidate's answer — discards others' work).
- **`.gitignore`.** Untrack `node_modules/`, `.env`, `build/`, secrets.
- **PR.** feature branch → open PR → review → approve/changes → merge (squash/merge/rebase); the review gate before main.
- **Amend.** local `git commit --amend`; pushed → `--amend` + `push --force-with-lease` (risky, avoid on shared).
- **Testing.** Ladder: unit → integration → system → UAT → regression → release. **Unit test = one unit in isolation (mock deps)**; Jest/Vitest (JS/React), flutter_test (Flutter).
- **Clean code / SOLID / DRY.** SOLID = **S**ingle-responsibility · **O**pen/closed · **L**iskov · **I**nterface-segregation · **D**ependency-inversion (explain **S** well); DRY = one source of truth.
- **DevTools tabs.** Elements, Console, **Network** (API), Sources; React DevTools (tree/props/hooks); Flutter DevTools (inspector/perf).

## 9. Behavioral & interview craft (ask for EVERY stack — judgment, not clichés)

- **Self-intro:** ~60-90s, timeline + stack + what you built; lead with most relevant.
- **Strengths (5):** specific + evidence, not adjectives.
- **Weaknesses:** honest + concrete improvement action.
- **Career (1-2yr / 5yr):** **specialise-then-broaden** (deep in one stack → add another).
- **English:** honest calibration ("reading good, speaking rusty, here's my plan"), don't inflate.
- **Questions to ask:** onboarding/ramp, mentorship, team, how juniors level up, code-review culture (never "none").
- **Scenarios (lead with communicate/negotiate/escalate, NOT "all-nighter"):**
  - *Slacking teammate* → assume good intent → 1:1 understand the blocker → expectation → document → escalate.
  - *Two in conflict* → listen both, separate person from problem, decide on project goals, document.
  - *Deadline clash* → **flag to stakeholders early + negotiate scope**, then manage time; ownership ≠ silent sacrifice.
  - *Group hiring / not all in* → optimise individual fit; company has real constraints.
  - *No-mentor job* → self-rescue (clarify goals, peer mentors, docs) before escalation.
- **Meta:** for junior/intern roles, the interviewer buys **growth trajectory + coachability** — be honest about gaps + show the learning plan.

## 10. The gotcha list (fire these; real candidates repeatedly failed them)

1. Listing **modifiers as types** (`final`/`const`/`static`).
2. **Can't dedupe/transform an array** under pressure (forgets `Set`/spread).
3. **Names widgets instead of the lifecycle** (Flutter).
4. **"Fix" merge conflicts by renaming the file** (dangerous).
5. **Recognises but never used** spread / `?.` / a state-mgmt lib.
6. **Behavioral = "I'll work harder / all-nighter"** instead of communicate/negotiate/escalate.
7. **`const` vs `final` inverted** (Dart).
8. **Async = "type mismatch"** (wrong — it's non-blocking).
9. **CSS `position` values confused with offset properties**; **SSR confused with MVC**.
10. **Says "variables live in the heap"** (locals live on the **stack**).

## 11. Verified corrections carried in this brief (✅FIX)

- `const` (compile-time) vs `final` (runtime), both immutable — not inverted.
- Flutter lifecycle methods are on the **State** class; only `createState()` on the widget.
- Call **stack** holds local variables; **heap** holds objects.
- `git checkout -b` (create) vs `-B` (force create-or-reset).

---

*Derived from the `mobile-engineer-interview` wiki topic (5 verified interviews, ~166/170 items verified faithful). Study material only; anonymised. If asked something outside §2–§10, say you don't know rather than invent.*
