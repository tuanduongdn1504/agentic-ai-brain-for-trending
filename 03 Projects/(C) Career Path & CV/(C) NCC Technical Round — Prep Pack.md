# NCC Plus — Technical Round · Prep Pack (React Native / Mobile)

> You passed the English gate. This round is about **depth**, and it likely runs in **Vietnamese or bilingual with an engineer** — so speak in whichever language is easier and focus on being *correct and concrete*. Anchor every answer to a **real thing you built** (TalentAxis, Space360, the visionOS build fix, the Apple rejection, NodeMedia, the crash fix).

**Honesty rule (same as always):** where you have real depth (React Native, JS, release, Flutter) → be specific. Where you don't (deep native Kotlin/Swift, backend infra like K8s/Kafka) → say "concept-level, here's the model, and here's my real bridge." Interviewers trust that.

---

## Contents
1. React Native core *(highest priority — this IS the role)*
2. JavaScript / TypeScript fundamentals
3. Mobile engineering (lifecycle, memory, push, security, release, Flutter)
4. CS & Clean Code (mid/senior)
5. Backend / full-stack awareness (the JD nice-to-haves)
6. System design (a mid/senior favorite)
7. Live-coding readiness
8. Questions to ask + gap-handling scripts

---

# 1. React Native core

### 1.1 Architecture — the Bridge vs the New Architecture ⭐ *(the #1 senior RN question in 2026)*
**Old architecture (the "Bridge"):** JS thread and Native thread communicated **asynchronously** over a bridge, passing **JSON-serialized** messages. Problems: serialization overhead, async-only (couldn't call native synchronously), and a bottleneck under heavy traffic (e.g. fast scrolling).

**New Architecture (default since RN 0.76, standard in 2026):**
- **JSI (JavaScript Interface)** — a C++ layer that lets JS hold **direct references** to native objects and call them **synchronously**, no JSON serialization. Replaces the bridge.
- **Fabric** — the new **rendering** system; the shadow tree is in C++, enabling concurrent React features and faster, more consistent layout.
- **TurboModules** — native modules are **lazy-loaded** (loaded when first used, not all at startup) and typed.
- **Codegen** — generates the C++ glue from your TypeScript spec files, giving type safety across the JS↔native boundary.
- **Hermes** — the default JS engine (AOT bytecode, lower memory, faster startup) — replaced JSC.

**How to say it:** "The old bridge was async and serialized everything to JSON, which was the bottleneck. The New Architecture uses JSI so JS can call native directly and synchronously, Fabric for rendering, TurboModules for lazy typed native modules, and Hermes as the engine. I've worked with Expo, which handles the New Architecture for me."

### 1.2 The threading model
- **JS thread** — runs your React/JS code and business logic.
- **Native/UI (main) thread** — renders native views, handles touches. **Never block it** (jank).
- **Shadow thread** — computes layout (Yoga/Flexbox).
Heavy work on the JS thread (big loops, JSON parsing) freezes the UI even though the native thread is free. Solution: chunk work, move it off the critical path (`InteractionManager.runAfterInteractions`), or use Reanimated worklets (run on the UI thread).

### 1.3 Rendering — reconciliation, keys
React builds a tree, **diffs** new vs previous, and applies the minimal change. **Keys** let it match list items across renders — index-as-key breaks on reorder/insert/delete (wrong item reused → state/UI bugs). Use a stable unique id.

### 1.4 Hooks — the deep version
- **useEffect(fn, deps):** runs after render; deps control when; return a cleanup for subscriptions/timers. Bugs: missing deps → **stale closures**; unstable object/array deps → infinite loop.
- **useMemo / useCallback:** cache a value / a function identity to avoid re-computation or re-rendering memoized children. Don't over-use — measure first. *(Note: React 19's **React Compiler** can auto-memoize, reducing the need for these by hand — worth mentioning as "the direction things are going.")*
- **useRef:** a mutable value that persists across renders **without** causing a re-render; also for DOM/native refs.
- **Rules of hooks:** only call at the top level, only in React functions — because React tracks them by call order.
- **Custom hooks:** extract reusable stateful logic (e.g. `useDebounce`, `useFetch`).

**Stale-closure trap (a favorite question):** an effect/callback captures the value of a variable from the render it was created in. If deps are wrong, it uses an old value. Fix: add the dep, or use a ref, or the functional updater `setX(prev => …)`.

### 1.5 State management — when each
- **Local `useState`** — component-only UI state.
- **Context** — low-frequency cross-cutting values (theme, auth). ⚠️ Context re-renders *all* consumers on change — don't use it for high-frequency state.
- **Redux (Toolkit)** — complex, shared, frequently-updated client state; middleware (thunk) for async; Immer for immutable updates. *(You've used Redux — say so.)*
- **Zustand** — lightweight global store, less boilerplate than Redux. *(You've used it.)*
- **React Query / TanStack Query** — **server** state: caching, dedup, background refetch, retries. The rule: "React Query for server data, a store for client data." *(You've used it.)*
**Answer shape:** "I pick by complexity and by client-vs-server. Server data → React Query. Big shared client state → Redux Toolkit or Zustand. Simple → local state."

### 1.6 Performance ⭐ *(they'll definitely ask)*
- **Re-renders:** memoize with `React.memo`, `useMemo`, `useCallback`; avoid inline objects/arrows as props; split components so state changes don't re-render the whole screen.
- **Lists:** use **FlatList/FlashList**, not `.map` in a ScrollView. Optimize with `keyExtractor`, `getItemLayout` (skips measurement), `windowSize`, `maxToRenderPerBatch`, `removeClippedSubviews`. FlashList (Shopify) is faster for big lists.
- **Images:** resize/cache (`expo-image` or FastImage), avoid huge images, lazy-load.
- **Animations:** use **Reanimated** (runs on the **UI thread** via worklets) + Gesture Handler, not the JS-thread `Animated` API, for 60fps.
- **Startup:** Hermes, lazy-load screens, defer heavy work with `InteractionManager`.
- **Profiling:** React DevTools Profiler, Flipper, the JS thread FPS monitor. **Measure before optimizing.**

### 1.7 Networking
Central API client (axios interceptors or a fetch wrapper) for auth headers + error mapping; **React Query** for caching/retry/refetch; handle loading/error/empty; exponential backoff; pagination (cursor or offset). *(You integrated against Django/FastAPI microservices at TalentAxis — cite the multi-service auth handling.)*

### 1.8 Native modules & bridging *(anchor: your visionOS/CocoaPods story)*
When a JS library doesn't exist for a native capability, you write a **native module** (TurboModule) in Kotlin/Swift and expose it to JS via Codegen. In Flutter the equivalent is a **platform channel**.
**Your real story:** "I've hit the native layer in practice — once a `pod install` failed with an obscure `visionos` error in a native module. It was a **toolchain version mismatch** (CocoaPods too old for the new platform key), not app code — I updated the toolchain and reinstalled the modules. On React Native, native build failures are usually **version/toolchain** issues, not your JS."

### 1.9 Local storage
Key-value → MMKV (fast) or AsyncStorage; structured → SQLite (op-sqlite / WatermelonDB) or Hive/Isar on Flutter; secrets → **Keychain (iOS) / Keystore (Android)** via `expo-secure-store` — **never** plain-store tokens. Offline-first: local DB as source of truth, queue mutations, sync on reconnect, resolve conflicts (updated_at / last-write-wins).

### 1.10 Expo vs bare, EAS, OTA *(anchor: your release stories)*
- **Expo managed** — fastest DX, config plugins, EAS Build/Submit/Update, no native code unless you need it. **Bare/prebuild** — full native access. Expo's **prebuild** generates native projects from config; you can eject when needed. *(You use both Expo and bare — say it.)*
- **OTA updates** — ship JS/asset changes without a store review (Expo Updates / your Stallion setup). Limit: can't change native code OTA.
- **EAS Submit** automates store upload vs **manual** (Transporter / Play Console). *(You owned the full pipeline incl. the D-U-N-S company-account setup — a strong "end-to-end ownership" story.)*

### 1.11 Testing & debugging
Unit/logic → **Jest** + **React Native Testing Library** (test behavior, not implementation); e2e → **Detox** or **Maestro**; crash/field → **Sentry / Crashlytics** with source maps. Debug with Flipper, React DevTools, native logs. *(Anchor: your crash-reduction story — reproduce → stack trace → root cause → fix → test to prevent regression.)*

---

# 2. JavaScript / TypeScript fundamentals

- **Event loop:** single-threaded; call stack + **microtask** queue (Promises) + **macrotask** queue (timers). Microtasks drain before the next macrotask. (Classic Q: predict the log order of sync + `setTimeout` + `Promise.then`.)
- **Promises / async-await:** async-await is sugar over Promises; `await` pauses the async function, not the thread; `Promise.all` for parallel; always handle rejection.
- **Closures:** a function remembering its creation scope — the basis of hooks and module privacy (and the stale-closure bug).
- **`this`:** depends on call-site; arrow functions capture `this` lexically.
- **Prototypes:** JS inheritance via the prototype chain; `class` is sugar over it.
- **`var`/`let`/`const`:** `var` function-scoped + hoisted; `let`/`const` block-scoped; `const` = no reassignment (object contents still mutable).
- **ES6+:** destructuring, spread/rest, modules, optional chaining `?.`, nullish `??`, template literals.
- **TypeScript:** `type` vs `interface` (interface for object shapes/extension, type for unions/aliases); **generics** (reusable typed functions/components); utility types (`Partial`, `Pick`, `Omit`, `Record`); why TS = catch errors at compile time, better refactoring/DX. *(You use TS daily — be confident here.)*

---

# 3. Mobile engineering

- **App lifecycle:** foreground/background/inactive; iOS `AppState`, Android activity lifecycle; handle backgrounding (pause timers, save state), resume (refetch). Push behavior differs by state (see below).
- **Memory / leaks:** unremoved listeners/timers, retained closures, large images. In RN, always clean up in `useEffect` return. Native: retain cycles (iOS ARC), context leaks (Android).
- **Push notifications (FCM/APNs):** device token → your backend → FCM (→ APNs on iOS) → device. Handle **foreground / background / killed**; **notification** vs **data** messages; iOS needs APNs key + user permission. Deep-link on tap. *(You've used Firebase/Expo notifications — present as working knowledge; a big campaign system = "I'd ramp.")*
- **Security (OWASP Mobile):** store tokens in Keychain/Keystore, not plain; HTTPS + optional **certificate pinning**; don't hard-code secrets; obfuscate; validate on the server. *(Space360 handled Sign-in-with-Apple + token revocation on account deletion — a real security-aware story.)*
- **Release process:** App Store review guidelines (account-deletion requirement, business-model clarity, privacy), Google Play Data Safety, versioning (bump build number each upload), TestFlight/Internal Testing. *(Your Space360 rejection → account-deletion fix → TalentAxis first-pass is a top-tier real story — use it for "tell me about a production challenge.")*
- **Flutter (your 2nd stack):** everything is a widget; Stateless vs Stateful; state mgmt Bloc/Riverpod/Provider/**GetX** (you used GetX); `Future`/`Stream` + `FutureBuilder`/`StreamBuilder`; isolates for parallelism; platform channels for native. **RN vs Flutter:** RN = JS/React, renders to native views via JSI; Flutter = Dart, draws its own UI with Skia/Impeller. Say: "I'm productive in both — I pick per the project/client."

---

# 4. CS & Clean Code (mid/senior)

- **Big-O (know the common ones):** O(1) hash lookup, O(log n) binary search, O(n) scan, O(n log n) good sort, O(n²) nested loop. Be ready to state the complexity of your solution in a coding task.
- **Data structures:** array vs linked list, hash map (O(1) avg), set, stack/queue, tree; when to reach for a map to de-dup or index.
- **OOP vs functional:** RN/React leans functional (pure components, immutability, hooks); OOP still relevant for native/services. Know both.
- **SOLID (name + one line each):** Single-responsibility, Open/closed, Liskov substitution, Interface segregation, Dependency inversion.
- **Clean Code (they list it):** meaningful names, small functions, single responsibility, avoid deep nesting, no magic numbers, comments explain *why* not *what*, DRY (but not premature abstraction). You've used **SonarQube** quality gates — cite that.
- **Design patterns (know a few):** Singleton, Observer (≈ pub/sub, React state), Factory, Strategy, Repository (data source abstraction — you'd use this to hide network-vs-cache from the UI).

---

# 5. Backend / full-stack awareness *(the JD nice-to-haves + the "full-stack" question)*

Concept-level is fine; show the **bridge** from your real work.
- **REST / HTTP:** methods (GET/POST/PUT/PATCH/DELETE), status families (2xx/3xx/4xx/5xx), statelessness, idempotency. Auth: **JWT** (access + refresh), OAuth2 basics.
- **GraphQL:** client asks exactly the fields it needs, one round-trip for nested data; vs REST's fixed resources. *(You used GraphQL on Flutter.)*
- **Databases:** SQL (PostgreSQL — relational, ACID) vs NoSQL (document/key-value); **Redis** = in-memory cache/sessions/rate-limiting/pub-sub; when to cache.
- **Microservices / distributed:** independent services, separate DBs, communication over HTTP/gRPC/queues; failure isolation. *(Your real bridge: "I integrated the TalentAxis client against a Django/FastAPI microservices backend — I know the client side of a microservices system: multiple services, cross-service auth, handling partial failures.")*
- **Message queue (Kafka):** decouples producers/consumers, high-throughput event streaming — concept-level.
- **Docker / K8s / CI-CD:** Docker = containerize; K8s = orchestrate/scale/self-heal; CI/CD = automate build/test/deploy. *(You've used Docker + Jenkins CI + SonarQube — real. K8s = concept-level.)*
- **Git:** branching (feature branches, trunk-based), PRs, rebase vs merge, resolving conflicts.
**The honest full-stack answer (their Q2):** "My depth is mobile/React Native, but I already work across the stack — REST/GraphQL, Supabase/Firebase, React on the web, Docker, CI. So I'm growing toward full-stack; I want to deepen backend step by step while keeping mobile as my core."

---

# 6. System design *(a mid/senior favorite — have a framework)*

**When asked "design [a feature/app]," go in this order:**
1. **Clarify** requirements + scale + constraints.
2. **Data model** + **API contract**.
3. **Local storage & caching** (offline-first?).
4. **State management** approach.
5. **Sync / offline** strategy (queue + conflict resolution).
6. **UI states** (loading/error/empty), **pagination**, image handling.
7. **Performance** (list virtualization, memoization, caching).
8. **Security** (token storage, cert pinning).
9. **Observability** (crash/analytics), **CI/CD**, release.

**Worked example — "design a chat feature":** WebSocket (or FCM) for realtime; local SQLite as source of truth; optimistic send + queue when offline; pagination (cursor) for history; dedup by message id; delivery/read receipts; encrypt at rest for sensitive data. **Reusable patterns to name:** repository pattern (UI doesn't know network vs cache), stale-while-revalidate, optimistic UI. *(Anchor: narrate TalentAxis or Space360 as a design story — client → API → cache → release.)*

---

# 7. Live-coding readiness *(if the round includes coding — be ready to think aloud)*

**Think-aloud method:** restate the problem → clarify inputs/outputs/edge cases → state approach + complexity → code → test with an example → discuss improvements.

**Common JS/algorithm exercises (know the approach):**
- Reverse a string / array; check palindrome.
- Find duplicates / first non-repeating char → use a **hash map/Set** (O(n)).
- FizzBuzz.
- Two-sum → hash map (O(n)).
- Debounce / throttle **implementation** (very common for RN — search-as-you-type):
  ```js
  function debounce(fn, delay) {
    let t;
    return (...args) => {
      clearTimeout(t);
      t = setTimeout(() => fn(...args), delay);
    };
  }
  ```
- Flatten an array; group by key; deep clone.

**Common React/RN component exercises:**
- A **counter** (useState).
- A **debounced search** that fetches and renders a list (useState + useEffect + a custom `useDebounce` + FlatList) — the classic RN interview build.
- A **fetch-and-render list** with loading/error states (or React Query).
- A **todo** (add/toggle/remove, keys).
- A form with validation.

**If asked to optimize a slow list:** FlatList + keyExtractor + getItemLayout + memoized item component + windowSize — say these.

---

# 8. Questions to ask them + gap-handling scripts

**Ask (shows seniority + product sense):**
1. "Do teams use **React Native, Flutter, or native** — and does it change by client project?"
2. "Is the New Architecture (Fabric/TurboModules) rolled out on current projects, or still the bridge?"
3. "How big is the team I'd help lead, and how much **client communication** is involved?"
4. "What does the mobile **CI/CD and release** pipeline look like across projects?"
5. "Biggest current technical challenge — performance, offline, native integration?"

**Honest gap-handling (rehearse — turns weakness into trust):**
- **Deep native Kotlin/Swift:** "My production depth is React Native and Flutter. I've hit the native layer for build/toolchain issues and native modules, and I've shipped with Swift foundations. For a native-only project I'd need a short ramp; cross-platform is where I'm strongest."
- **K8s / Kafka / Redis:** "Concept-level — I know what they solve, not hands-on ops. I'm a mobile engineer who understands the backend I integrate with; I ramp fast."
- **DSA under pressure:** "I reason through it — clarify, pick a data structure, state the complexity. I may not have every algorithm memorized, but I can work to a correct, reasonable solution and improve it."
- **High-load/scaling:** "From the mobile side — pagination, caching, request dedup, efficient lists. Backend scaling I understand conceptually; I've integrated against microservices in production."

---

## Priority order to study
1. **§1 React Native core** — especially **1.1 architecture, 1.4 hooks, 1.5 performance** (highest-probability senior questions).
2. **§2 JS/TS fundamentals** — event loop, closures, async, TS generics.
3. **§7 live-coding** — do the debounced-search build + debounce impl once by hand.
4. **§3 mobile** — anchor your real stories (release, visionOS, crash, NodeMedia).
5. **§5 backend + §4 CS** — concept-level + bridges.
6. **§6 system design** — rehearse designing Space360/TalentAxis as a design story.

*Anchor everything to real work. A mid/senior round is won less by reciting definitions and more by "here's how I actually did X, and here's the trade-off I made." You have the projects to do that — use them.*
