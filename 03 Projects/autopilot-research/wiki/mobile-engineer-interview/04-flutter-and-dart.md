# 04 — Flutter & Dart

From the two Flutter candidates (videos 1 & 2). Both were UI-strong but weak on Dart internals and state management — so this article doubles as *the list of things Flutter juniors most often get wrong*. Corrections are flagged ⚠️.

## Dart language

### Data types

- **Primitives/core:** `int`, `double` (both under `num`), `String`, `bool`. **Collections:** `List`, `Set`, `Map`. Plus `dynamic`, `Object`, `var` (inferred), `null` (with null-safety `?`).
- ⚠️ **Recurring mistake:** both candidates listed `final`/`const`/`static` as *data types*. They are **modifiers**, not types. Don't do this.

### `const` vs `final` (⚠️ one candidate had it exactly backwards)

- **`final`** = assigned **once at runtime**; the value can be computed at runtime (e.g. `final now = DateTime.now();` ✅). Can't be reassigned afterward.
- **`const`** = **compile-time constant**; the value must be known at compile time (`const DateTime.now()` ❌ fails). Stricter than `final`; `const` objects are canonicalised/inlinable.
- Both are immutable after assignment. Mnemonic: **every `const` is effectively `final`, but not vice-versa.** ⚠️ The video-2 candidate said "final allows updates, const is only-at-declaration" — inverted; the interviewer corrected him and asked him to re-study.

### Collections & higher-order methods

- **`List`** ordered, allows duplicates, index access `[i]`. **`Set`** unordered, unique (great for **dedup**: `list.toSet().toList()`). **`Map`** key→value.
- `map(fn)` transform → new `Iterable`; `where(pred)` filter; `sort([cmp])` in place (`list.sort((a,b)=>b.compareTo(a))` for descending); `every(pred)`/`any(pred)` predicate tests. Call `.toList()` to materialise.
- **Modify an array:** `add`, `addAll`, `remove`, `removeAt`, `insert`, or spread `[...list, x]`.

### Null-checking operators

`??` (null-coalescing: `a ?? b`), `?.` (safe navigation: `user?.name`), `??=` (assign-if-null), `!` (null assertion — use sparingly), `?:` (ternary). Dart 2.12+ is null-safe by default (`?` marks nullable).

### async/await & `Future`

See [[02-async-and-event-loop]] — Dart mirrors JS. `Future<T>` = eventual value; `Stream<T>` = many values over time.

## Flutter framework

### Widgets

- A **Widget** is an **immutable description** of part of the UI. *Everything* is a widget (text, buttons, layout). You compose a **tree**; `build()` returns widgets. Reuse by extracting/instantiating widget classes.

### StatelessWidget vs StatefulWidget

- **StatelessWidget:** immutable, no internal mutable state; `build()` depends only on constructor params. Use for static UI. Cheaper — prefer it when possible.
- **StatefulWidget:** holds mutable state in an associated **State** object; calling **`setState()`** marks it dirty and re-runs `build()`. Use when UI changes from internal state (input, timers, fetched data).

### ⚠️ The lifecycle (correction — methods live on the State class)

Only **`createState()`** is on the `StatefulWidget` itself. The lifecycle methods belong to the **`State`** class:

`createState()` → **`initState()`** (once, before first build — init vars, subscriptions; call `super.initState()`) → `didChangeDependencies()` → **`build()`** (every render / after `setState`) → `didUpdateWidget()` (parent rebuilt) → `deactivate()` → **`dispose()`** (cleanup — close streams/controllers). StatelessWidget has only `build()`. ⚠️ A model answer that lists `initState/build/dispose` as "StatefulWidget methods" is technically imprecise — they're **State** methods.

### `BuildContext`

- A handle to the widget's **location in the tree**. Used to reach `Theme.of(context)`, `Navigator.of(context)`, and inherited/scoped data. Passed into `build(BuildContext context)`. (Video-2 candidate couldn't explain it — a common foundational gap.)

### Layout widgets

- **`Scaffold`** — Material page skeleton: `appBar`, `body`, `floatingActionButton`, `drawer`, `bottomNavigationBar`. **Not required** — you can build with `Container`/`Column`/`Stack` — but it saves wiring standard patterns (and handles safe areas).
- **`Container` vs `SizedBox`** — `SizedBox` is only `width`/`height` (lightweight spacer/constraint). `Container` adds decoration (color, border, shadow), padding, margin, alignment. `Container` ≈ `SizedBox` + styling.
- **`Row`/`Column` alignment:** `MainAxisAlignment` = along the primary axis (Row→horizontal, Column→vertical); `CrossAxisAlignment` = the perpendicular axis. Values: `start`, `center`, `end`, `spaceBetween`, `spaceAround`, `spaceEvenly`.

### ⚠️ ListView inside a Column (asked in both Flutter interviews)

Both a `Column` and a `ListView` want **unbounded height** → **overflow / "unbounded height" error**. Fixes:
1. **`Expanded(child: ListView(...))`** — give the ListView the leftover space (best for scrolling lists).
2. **`ListView(shrinkWrap: true)`** — size to content (loses lazy-loading; ok for short lists).
3. Use **`SingleChildScrollView`** with a `Column` for simple non-lazy scrolling, or wrap in a fixed-height `SizedBox`.

### Navigation

- `Navigator.push(context, MaterialPageRoute(builder: …))` adds a screen to the stack; `Navigator.pop(context)` returns to the previous. `pushReplacement` swaps current; `pushAndRemoveUntil` clears the stack.
- **Modal:** `showDialog()` / `showModalBottomSheet()` overlay that blocks interaction and returns a `Future` with the result. (Video-2 candidate didn't know what a modal was — worth knowing.)

### State management (asked; neither candidate had used it)

- **`setState`** — built-in, local to one widget. Fine for small local state; doesn't share across screens.
- **Provider** — simplest shared-state solution (`ChangeNotifier` + `Consumer`); good first step, avoids prop-drilling.
- **GetX** — reactive, minimal boilerplate (`Get.put`/`Get.find`), auto-disposal; easiest to pick up.
- **BLoC** — event-driven via Streams; testable, scales to large apps; steepest curve.
- Knowing *when* to reach past `setState` (sharing state across screens) is the point — pick Provider or GetX to start.

### Flutter pros/cons (candidate gave a solid practical answer)

- **Pros:** one codebase for Android + iOS, **hot reload**, fast UI iteration, good performance. **Cons:** larger app size, smaller library ecosystem than native, learning curve; jank possible with poor state-management choices.

## Key Takeaways

- **`const` = compile-time, `final` = runtime, both immutable** — don't invert it, don't call them "types".
- Lifecycle methods (`initState`/`build`/`dispose`) are on the **State** class; only `createState()` is on StatefulWidget.
- **ListView-in-Column** overflow → `Expanded` / `shrinkWrap` — the most-asked Flutter layout gotcha.
- Know one state-management lib (Provider/GetX) and **why** you'd use it over `setState`.

**Sources:** videos 1 (OVN), 2 (aKMV). Corrections in [[caveats-and-corrections]]. Related: [[02-async-and-event-loop]] · [[05-react-native-and-mobile-deployment]].
