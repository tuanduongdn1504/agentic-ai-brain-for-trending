# Fox Code — Mobile Interview Prep (Flutter/Dart · native concepts · SDKs)

> **The role (be clear-eyed):** Fox Code "Software Engineer" (mobile), Hải Châu Đà Nẵng — a **generalist, junior-friendly** role (6-month minimum) asking **Kotlin / Swift / Java / Dart "or relevant language"** + REST + Git + debugging/optimization. You have **5 years** and your core is **React Native**. So this pack does two jobs: (1) get you fluent on **Flutter/Dart** (your real native-cross-platform anchor here) + the SDK nice-to-haves, and (2) prep the **one behavioral question that decides this interview**: *"you're overqualified — why this role?"*
>
> **How to position (honest):** lead with **Flutter/Dart (real, Enouvo)** + **shipped apps** + **general mobile engineering**. Native **Kotlin/Swift/Java** = concept + platform-channel-bridge level (say so). "Or relevant language" covers your **JS/TS + RN** too. Don't oversell native depth — your strength is *breadth + reliability + shipping*, and that's genuinely valuable to a small team.
>
> **Companions:** the **Swift pack** (for the Swift dimension), the **Node/RN boards** (JS/general/REST/Git), the **STAR scripts** + **evidence bank** (real stories).

---

## ⭐ §0 — The question that decides this interview: *"Why this role, given your experience?"*

They **will** ask it (or think it). Your real driver is solid and legitimate: your current company is **downsizing**, so you're moving **proactively** toward a stable team where you can go deep, mentor, and strengthen your native/Flutter side. The skill is framing it **forward** (what you want) not **backward** (what you're fleeing) — and **never leading with "bankruptcy."**

**Ready-to-say (EN):** *"Over 5 years I've gone deep on React Native and shipped products end-to-end — two apps live on the stores, full release ownership. What I'm looking for now is a stable team where I can settle in for the long term, go deep, and mentor the people around me — and this stack also lets me strengthen my native and Flutter side, which I genuinely want to grow. I bring senior-level delivery and reliability, and I'm the kind of engineer who lifts a small team."*

**Ready-to-say (VN):** *"Qua 5 năm, em đã đi sâu về React Native và làm chủ sản phẩm end-to-end — 2 app đã lên store, tự chủ toàn bộ quy trình phát hành. Điều em tìm kiếm bây giờ là một đội ngũ ổn định để gắn bó lâu dài, đi sâu và mentor cho anh em — và stack ở đây cũng giúp em củng cố thêm mảng native/Flutter mà em thực sự muốn phát triển. Em mang lại năng lực senior và sự đáng tin cậy, và em là kiểu kỹ sư giúp nâng cả đội đi lên."*

- **If asked "why are you leaving / are you currently employed?"** → honest but forward-looking: *"My current company is going through restructuring/downsizing, so I'm looking early for a stable, long-term home where I can contribute at a senior level."* Say **"restructuring/downsizing,"** not "bankruptcy"; don't badmouth; moving **early/proactively** reads as *smart*, not forced.
- **Salary/level — negotiate UP (this is your leverage):** *"With 5 years and two shipped apps, I'd be contributing well above the junior band — so I'd like a level and package that reflect senior delivery and mentoring."* Over-qualified = leverage, not a problem.
- **The mentoring hook is real and rare** — you're **PSM II** and you've coached engineers (incl. a colleague to PSM II). A small team *wants* that. Lean on it.

---

## §1 — Flutter / Dart core  *(your primary language anchor for this role — real from Enouvo)*

### Dart language
- **Null safety:** `String?` (nullable) vs `String` (non-null); `!` force-unwrap, `?.` null-aware, `??` default, `late` (initialized-before-use), `required` named params. *(≈ TS strict null / Swift optionals.)*
- **`Future` vs `Stream`:** `Future<T>` = **one** async value (like a JS Promise); `Stream<T>` = **many** values over time (like an event emitter / observable). `async/await` for Futures; `await for` / `.listen()` for Streams. `FutureBuilder`/`StreamBuilder` render loading→data→error in the UI. *(You used Future/Stream + FutureBuilder at Enouvo.)*
- **Isolates (Dart concurrency):** Dart is single-threaded per isolate; heavy work runs in a **separate isolate** with **its own memory**, communicating by **message passing** (no shared state) — different from JS (single thread + event loop) and from real OS threads. Use `compute()` for a quick isolate.
- **Other:** `mixin`/`with` (share behavior without inheritance), **extension methods**, `factory` constructors, `const` constructor (compile-time, canonicalized) vs `final` (set-once at runtime) — *both immutable* (don't invert this, same as Swift `const`/`final`).

### Widgets
- **Everything is a widget** — an immutable description of UI; you compose a tree; `build()` returns widgets.
- **StatelessWidget** (immutable, `build()` only) vs **StatefulWidget** (a `State` object holds mutable state; `setState()` → rebuild).
- **Three trees:** Widget (config) → Element (instance) → RenderObject (layout/paint). **Keys** let Flutter match elements across rebuilds (needed when reordering/inserting list items with state).
- **BuildContext** = the widget's location in the tree (`Theme.of(context)`, `Navigator.of(context)`, inherited data).

### Lifecycle *(methods on the `State` class — only `createState()` is on the widget)*
`createState()` → `initState()` (once) → `didChangeDependencies()` → `build()` → `didUpdateWidget()` → `setState()`/rebuild → `deactivate()` → `dispose()` (cleanup: cancel timers/streams/controllers). *(Same shape as I gave you for iOS — memorize it.)*

### State management *(know the ladder + why you climb it)*
`setState` (local) → **InheritedWidget/Provider** (shared) → **Riverpod** (compile-safe Provider) → **BLoC/Cubit** (streams, testable, scales) → **GetX** (reactive, minimal — *you used this*). **Why past `setState`:** share state across screens, testability, avoid prop-drilling. *(≈ your RN Redux/Zustand/React Query reasoning.)*

### Performance *(common interview probe)*
- Use **`const` constructors** so Flutter skips rebuilding unchanged subtrees.
- **`ListView.builder`** (lazy) not a `Column` of mapped children; **`shrinkWrap`/`Expanded`** to fix the classic **"ListView inside Column → unbounded-height overflow"**.
- Keep `build()` cheap; split widgets so `setState` rebuilds a small subtree; `RepaintBoundary` for expensive paints; profile with **Flutter DevTools** (widget rebuild counts, frame timeline, target 60/120 FPS).

### Navigation & platform channels
- **Navigation:** `Navigator.push/pop(MaterialPageRoute…)`, named routes, or **go_router**/Navigator 2.0 for declarative/deep-linking.
- **Platform channels (`MethodChannel`)** — call **native Kotlin/Swift** from Dart when a feature isn't in a plugin. *This is your honest bridge to the native ask:* "I go to native via platform channels when needed." *(You've touched the native layer — CocoaPods/visionOS, native modules.)*

### Testing
- **Unit** (`test`), **Widget** (`testWidgets` + `WidgetTester` — pump + find + expect), **Integration** (`integration_test`). Mocks with **Mockito/Mocktail** (*you used Mocktail*). *(Test pyramid: many unit > widget > few integration.)*

---

## §2 — General mobile engineering  *(the generalist core — you're strong here)*

- **REST API integration:** `dio`/`http` in Flutter (interceptors, timeouts, retries) — *≈ your Axios work*; parse JSON to typed models (`fromJson`/`toJson`, or `json_serializable`); handle status codes + errors; **JWT** auth + refresh.
- **Local storage:** `SharedPreferences` (small key-value, ≈ UserDefaults/AsyncStorage) · **SQLite** (`sqflite`) for structured data · **flutter_secure_storage** (Keychain/Keystore) for tokens/secrets — *never plain prefs for secrets*.
- **App lifecycle:** `AppLifecycleState` (resumed/inactive/paused/detached) — pause work when backgrounded (battery).
- **Offline/caching, error handling, retry/backoff, optimistic UI** — talk to how you keep an app resilient on flaky networks.

---

## §3 — The SDK nice-to-haves *(they list these — know each in 2 sentences)*

- **Push Notifications (FCM / APNs):** Firebase Cloud Messaging for both platforms; iOS requires **APNs** under the hood. Know **notification vs data messages**, the three delivery states — **foreground / background / killed** (killed + data-only needs a background handler), token registration, and permission prompts. *(You've done push + a deep-link OAuth bridge on your RN apps.)*
- **Firebase suite:** **Auth** (email/social sign-in), **Firestore** (NoSQL realtime DB), **Analytics** (events + screen tracking), **Crashlytics** (crash reporting — symbolicated stack traces), **Remote Config** (feature flags). *(You've used Firebase + Supabase.)*
- **In-App Purchase (IAP):** `in_app_purchase` plugin over iOS **StoreKit** + Android **BillingClient**; product types = **consumable / non-consumable / subscription**; **validate receipts server-side**; App Store rule: don't offer external payment for digital goods (Guideline 3.1.1 — *you handled this*).
- **Ads (AdMob):** `google_mobile_ads`; banner / interstitial / rewarded; load-then-show; respect frequency + UX.
- **Analytics:** log events + screen views; funnel/retention basics.

---

## §4 — Debugging · optimization · testing · Git · Agile *(overlaps your existing packs — quick hits)*

- **Debugging/optimization:** reproduce → Flutter DevTools (CPU/memory/frame timeline, rebuild counts) → root-cause → fix → verify. Crashlytics/Sentry for prod crashes. *(Your crash-reduction + evidence-first debugging stories apply — see STAR script #1.)*
- **Git:** feature branches, conventional commits, PR review; resolve conflicts by **editing to the correct result + deleting markers**, never renaming the file (red flag). *(You have Husky/commitlint discipline.)*
- **Agile/Scrum:** you're **PSM II** — this is a strength most candidates don't have; mention it lightly (don't overshadow the engineering).

---

## §5 — Your real anchors for THIS role *(lead with these — all true)*

| They ask about… | Anchor to |
|---|---|
| **Flutter/Dart** | Enouvo: cross-platform Flutter/Dart apps + GraphQL, GetX, Future/Stream/FutureBuilder, Mocktail tests, Jenkins CI + SonarQube gates |
| Shipping / releases | two apps live on App Store + Google Play (RN), full EAS pipeline, D-U-N-S, Apple review fixes |
| REST API + JWT | RN apps against microservices; the OAuth refresh-token investigation (STAR #1) |
| Firebase / push / SDKs | push + deep-link bridge on the RN apps; Firebase + Supabase |
| Debugging / optimization | crash root-causing; evidence-first debugging (curl test matrix) |
| Native (Kotlin/Swift/Java) | **honest:** concept + platform-channel bridge; basic Swift (I've been studying it); I drop to native when a plugin doesn't exist |
| AI tooling | Claude Code + Cursor daily (a real edge on a small team's velocity) |

**Honest gap-handling scripts:**
- *"How strong is your native Kotlin/Swift?"* → *"My production depth is React Native and Flutter/Dart. Native I work at the bridge level — platform channels, native modules, build/toolchain issues — and I've been deepening Swift. I ramp fast."*
- *"Real-time chat / heavy IAP?"* → *"I've done push, deep linking, auth, and store releases; a full chat or complex IAP I'd learn quickly — here's how I'd approach it…"* (reason it out; don't fake it).

---

## §6 — The 10 questions to drill *(out loud, each ending with a real anchor)*

1. **Why this role given your experience?** *(§0 — rehearse this the hardest.)*
2. Dart **`Future` vs `Stream`** — and where you used each.
3. Flutter **StatelessWidget vs StatefulWidget + the State lifecycle** (`initState`→`dispose`).
4. **State management** — `setState` vs Provider/GetX/BLoC, and *why* you'd go past `setState`.
5. **Performance** — `const`, `ListView.builder`, the ListView-in-Column overflow, DevTools.
6. **How do you call native code from Flutter?** (`MethodChannel` / platform channels.)
7. **How do you integrate a REST API + handle JWT/refresh?** (→ your OAuth story.)
8. **Push notifications** — foreground/background/killed, notification vs data messages, APNs.
9. **How do you debug a crash / a slow screen?** (evidence-first; DevTools; Crashlytics.)
10. **`const` vs `final` in Dart** (both immutable; const = compile-time). *(Don't invert it.)*

---

*Bottom line: you're over-qualified and off your RN axis here — so this interview is won on **breadth + reliability + a genuine reason for wanting it**, not on out-native-ing a native specialist. Nail §0 (the "why this role" answer) and lead every technical answer with a real Flutter or shipping anchor. And be honest with yourself first: if there's no real reason you want this over your current role, the best prep is to skip it.*
