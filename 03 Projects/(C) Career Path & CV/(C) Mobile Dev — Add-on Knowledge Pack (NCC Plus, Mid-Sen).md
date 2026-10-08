# Add-on Knowledge Pack — NCC Plus · Mobile Developer (Mid/Sen)

**Company:** NCCPLUS Vietnam (NccSoft) — a 10+ year software **outsourcing** firm, 350+ engineers, multi-office (incl. Đà Nẵng), **international clients incl. Japan**. Founded 2014.
**Role:** Mobile Developer (Mid/Sen) · **Fully remote** · **≥3 years** · framework-agnostic (Flutter / React Native / Kotlin / Swift) · team-lead expected · **Intermediate English (speaking/writing) required**.

> **This is a companion to your VTVcab prep pack.** The React/JS fundamentals, Redux, REST, debugging, and PSM-II sections there **still apply**. This pack covers only what NCC asks that VTVcab didn't — so you don't re-study what you already have.

---

## 0. How NCC differs from VTVcab — and why it's an *easier, more senior* fit

| Dimension | VTVcab | NCC Plus |
|---|---|---|
| Seniority | implied junior/mid (6mo–2yr) | **Mid/Sen, ≥3 yrs** → your 5 yrs fits cleanly, no "over-experienced" awkwardness |
| Framework | React Native only | **Flutter / RN / Kotlin / Swift — any** → play your **dual RN + Flutter** card |
| Domain | narrow (OTT/Smart TV) | broad (client projects across many domains) → no niche gap |
| Leadership | not asked | **"Able to take on a team leader role"** → your **PSM II + mentoring** is a direct hit |
| English | not stated | **Intermediate English required** → the one real gate for you (see §7) |
| Work model | on-site Danang | **fully remote** → your PSM-II remote-native strength applies |

**The reframe:** at NCC you're not a stretch candidate — you're **squarely Mid/Sen**. Your two differentiators over a typical applicant are (1) **RN *and* Flutter both in production**, and (2) **team-lead/Scrum-Master credibility**, which they explicitly want. Lead with those.

**Your honest bridges to their world (outsourcing + microservices + international):**
- You've integrated a RN client against a **Django/FastAPI microservices** backend (TalentAxis) → real microservices-context experience (as the client, honest about that).
- 5 yrs across **RN, Flutter, REST, GraphQL, CI (Jenkins), Docker, SonarQube** → the full-lifecycle, multi-stack profile an outsourcer staffs on varied client projects.
- **PSM II + mentoring + internship-program leadership** → ready to lead a small team on a client project.

---

## 1. Local storage  *(NCC required — "Local storage … experience")*

Know the options **across frameworks** (they're agnostic) and *when* to use each — the interview point is judgment, not memorizing APIs.

**The decision:** key-value vs structured vs secure.
- **Key-value / small prefs:** RN → `AsyncStorage` (or **MMKV**, much faster, synchronous); Flutter → `shared_preferences`; native → `UserDefaults` (iOS) / `SharedPreferences` (Android).
- **Structured / relational (lots of records, queries):** SQLite everywhere — RN → `react-native-sqlite`/WatermelonDB/**op-sqlite**; Flutter → `sqflite`/**Drift**; **Hive/Isar** (Flutter NoSQL, fast); native → **Core Data** (iOS) / **Room** (Android).
- **Secure (tokens, credentials):** **Keychain** (iOS) / **Keystore** (Android) — RN `react-native-keychain`/`expo-secure-store`; Flutter `flutter_secure_storage`. **Never** put auth tokens in plain AsyncStorage/shared_preferences.

**Your honest anchor:** "I've done offline persistence and token storage in production RN apps; on Flutter I've used the sqflite/shared_preferences side. I pick the store by data shape — key-value for prefs, SQLite for relational offline data, Keychain/Keystore for secrets."

**Likely Q — "How do you build offline-first?"** → local store as source of truth + a sync layer: write locally, queue mutations, sync to the API on reconnect, resolve conflicts (last-write-wins or version/updated_at). Mention optimistic UI.

---

## 2. Asynchronous programming  *(NCC required — cross-framework)*

They accept any stack, so know the async model in **each** in one sentence:
- **JS/RN:** event loop + Promises + `async/await`; `Promise.all` for parallel; careful with unhandled rejections.
- **Dart/Flutter:** **`Future`** (single async value) vs **`Stream`** (many values over time); `async/await`, `async*`/`yield` for streams; **`isolate`** for true parallelism (Dart is single-threaded — CPU-heavy work goes to an isolate).
- **Kotlin:** **coroutines** (`suspend` funcs, `launch`/`async`, structured concurrency, `Dispatchers.IO/Main`) + **Flow** (cold async streams).
- **Swift:** `async/await`, `Task`, actors; **Combine** (publishers/subscribers) for reactive streams.

**The senior point (say this):** "The common thread is: never block the UI thread. Do I/O and heavy work off-main, model streams of events (WebSocket, sensor, live data) as streams/Flow/Combine, and use structured concurrency so tasks are cancellable and don't leak." *(Your NodeMedia live-streaming + your crash root-causing both touch this — cite them.)*

**Common gotcha Qs:** race conditions (guard shared state), cancellation (cancel in-flight requests on unmount/dispose — memory leaks otherwise), and debouncing/throttling user-driven async (search-as-you-type).

---

## 3. Push notifications & cloud messaging  ⚠️ *(NCC required — your biggest genuinely-new area; study this most)*

You have Firebase but not deep push. Learn the model — it's asked explicitly.

**The architecture (know this cold):**
1. App registers with the OS → gets a **device token** (**FCM token** on Android/cross-platform; **APNs token** on iOS).
2. App sends the token to **your backend**, which stores it per user/device.
3. Backend sends a message to **FCM** (Firebase Cloud Messaging) / **APNs** (Apple Push Notification service); the push provider delivers to the device.
4. The OS/app displays or handles it.

**The three delivery states (the classic interview trap):**
- **Foreground** — app is open; *you* handle/display it (the OS won't auto-show it), e.g. an in-app banner.
- **Background** — app is backgrounded; OS shows the notification; tapping it opens/deep-links the app.
- **Killed/terminated** — behavior differs: a **notification message** still shows via the OS; a **data-only message** may not wake a killed app reliably (esp. iOS).

**Notification vs data messages (FCM):**
- **Notification message** = FCM auto-displays it (title/body) — simple.
- **Data message** = delivered to your app code to handle (custom logic, silent updates) — more control, less guaranteed when killed.
- Often you send **both**.

**iOS specifics:** requires **APNs** (FCM proxies to APNs on iOS), an **APNs auth key/cert**, explicit **user permission** prompt, and capabilities (Push Notifications, Background Modes). Silent pushes are rate-limited by Apple.

**Tools:** Firebase Cloud Messaging (standard), **OneSignal** (higher-level, analytics), **Expo Notifications** (if Expo — which you use), Notifee (rich local notifications).

**Your honest line:** "I've worked with Firebase and Expo, so I know the token → backend → FCM/APNs flow and the foreground/background/killed handling. I haven't built a large-scale segmented-campaign system, but the mechanics and the iOS APNs/permission specifics I'm solid on and can implement."

**Deep-linking pairs with this** — tapping a push should route to the right screen (universal links / app links + a deep-link router). Worth a sentence.

---

## 4. Flutter refresh  ✅ *(you have it — NCC lists it FIRST; make it a strength, not a footnote)*

Many RN devs can't do Flutter. You can — dust it off so you can talk it fluently.

- **Everything is a widget**; **Stateless** vs **Stateful**; the widget tree + element tree + render tree; `build()` is called often → keep it cheap.
- **State management** (know 2–3): **Provider**, **Riverpod**, **Bloc/Cubit** (event→state, very common on client projects), **GetX** *(you've used GetX — say so)*. Pick by team preference; Bloc for large apps, Provider/Riverpod for most.
- **Async:** `FutureBuilder` / `StreamBuilder` to build UI from Futures/Streams; `setState` vs a state-mgmt solution.
- **Navigation:** Navigator 2.0 / `go_router`.
- **Platform channels** — call native (Kotlin/Swift) code from Dart when a plugin doesn't exist.
- **Performance:** `const` constructors, `ListView.builder` (lazy), avoid rebuilding whole subtrees, `RepaintBoundary`.

**Your line:** "I've shipped Flutter/Dart with GraphQL and GetX at Enouvo, so I'm comfortable in both ecosystems — I can be productive whichever stack a client project uses, RN or Flutter."

---

## 5. Mobile system design  *(NCC — "Participate in system design", Mid/Sen expectation)*

At Mid/Sen they'll ask you to *design*, not just implement. Have a structure:

**When asked "design a [feature/app]":** clarify requirements → data model → API/contract → local storage & caching → state management → offline/sync → error/loading/empty states → performance (pagination, lazy loading, image caching) → security (token storage, cert pinning) → observability (crash/analytics) → CI/CD & release.

**Reusable patterns to name:**
- **Layered architecture:** UI → state/logic → repository → data source (API + cache). Keeps UI dumb, logic testable.
- **Repository pattern** — single source of truth; UI doesn't know if data came from network or cache.
- **Pagination** — cursor vs offset; infinite scroll with a windowed list.
- **Caching** — memory + disk; stale-while-revalidate; cache invalidation.
- **Feature modularization** — for large/team codebases (relevant to leading a team).

**Your anchor:** end-to-end ownership of TalentAxis/Space360 (client → API → release) is exactly this — narrate one as a design story.

---

## 6. The backend / infra "nice-to-have" cluster  ⚠️ *(concept-level — be honest, show the bridge)*

NCC's nice-to-haves are backend/infra because they build full systems. You don't need depth — you need to **not be blank** and to **show your honest bridge**. One or two sentences each:

- **Microservices / distributed systems** — ✅ *your real bridge*: "I integrated the TalentAxis RN client against a **Django/FastAPI microservices** backend — I know the client side of a microservices system: multiple services, separate endpoints, auth across them, handling partial failures gracefully."
- **CI/CD (Docker, Kubernetes)** — ✅ partial: "I've used **Docker** and **Jenkins CI** with **SonarQube** quality gates, plus OTA release pipelines. **Kubernetes** I know conceptually (container orchestration — scaling, self-healing, rolling deploys) but haven't operated."
- **Redis (NoSQL)** — concept: "In-memory key-value store — used for caching, sessions, rate-limiting, pub/sub. I've used PostgreSQL and Firebase; Redis I understand the use-cases for."
- **Kafka (message queue)** — concept: "Distributed event-streaming/message queue — decouples producers and consumers, handles high throughput, event-driven architectures. Concept-level for me."
- **High-load app development** — concept: "Scaling for many users — caching layers, CDN, DB read replicas, horizontal scaling, load balancing, backpressure. On the mobile side: pagination, request dedup/debounce, efficient list rendering, offline caching to reduce server load."
- **Cloud-based development** — "AWS/GCP/Azure basics — where the backend runs, storage (S3), serverless functions, managed DBs. My focus has been mobile, but I integrate against cloud backends daily."
- **Open-source CMS/CRM/E-commerce** — "I've built product apps (recruitment, property management); I understand integrating a mobile client against a CMS/commerce backend."

**The honesty frame (rehearse):** "Several of these are backend/infra — I'm a mobile engineer, so they're concept-level for me, not hands-on. What I bring is a mobile dev who *understands the system he integrates with* — I've worked against microservices, used Docker/CI, and I ramp fast on infra when a project needs it."

---

## 7. English requirement  ⚠️ *(the ONE real gate — NCC serves international/Japanese clients)*

"Intermediate English (speaking/writing)" is **load-bearing** here (unlike VTVcab) — outsourcing means client communication, often in English.

- **Be honest about your level** (you know it; I don't). If you're intermediate+ → good, say so plainly and don't over-worry.
- **They likely test it** — expect part of the interview in English, or a short English self-intro. **Prepare your 20-second intro in English** and be ready to describe a project in English (you already have the VTVcab pack's English talking points — reuse them).
- **If your speaking is weaker than your writing:** say "I'm confident reading/writing technical English and in written async communication; my speaking is intermediate and improving." Honesty + a plan beats bluffing.
- **Your real asset:** you use **Claude Code and English technical docs daily** → your technical-English reading/writing is genuinely strong. Frame it that way.

**Prep:** rehearse (a) English self-intro, (b) one project walkthrough in English, (c) "why NCC / why remote outsourcing" in English. 30 min out loud.

---

## 8. Honest gap-handling scripts *(NCC-specific)*

- **Kubernetes / Kafka / Redis:** "Concept-level — I know what they're for and the problems they solve, not hands-on operations. I'm a mobile engineer who understands the backend I integrate with, and I ramp fast."
- **Native Kotlin/Swift depth (if probed):** "My production depth is RN and Flutter; I've worked with Swift/SwiftUI foundations and native modules. For a native-only project I'd need a short ramp, but cross-platform is where I'm strongest."
- **High-load / distributed systems:** "From the mobile side — pagination, caching, request efficiency. Backend-side scaling I understand conceptually; I've integrated against microservices in production."
- **English speaking (if weaker):** the §7 script.
- **Team-lead experience (turn it up, don't hedge):** "As a PSM II Scrum Master I've led an Innovation team, run mentorship and an internship program, and driven delivery — I'm comfortable leading a small dev team, unblocking people, and owning technical decisions."

---

## 9. Smart questions to ask NCC *(shows you understand the outsourcing model)*

1. "For this role, is it a **fixed product team or client project rotation**? Which stacks do current projects use — Flutter, RN, or native?"
2. "How large is the team I'd lead, and what does the team-lead responsibility include — technical decisions, mentoring, client communication?"
3. "How much **direct client contact** does a mobile lead have, and in what language — English, Japanese, Vietnamese?"
4. "How is **fully-remote** structured — core hours, timezone overlap with international clients, async practices?"
5. "What does the mobile CI/CD and release pipeline look like across projects?"
6. "What's the growth path from Mid/Sen — tech lead, architect, or engineering management?"

---

## 10. Fast-study checklist *(before an NCC interview — prioritized)*

- [ ] **English:** rehearse self-intro + 1 project walkthrough out loud (§7) — **highest priority gate**.
- [ ] **Push notifications** (§3): FCM/APNs flow + foreground/background/killed + notification-vs-data — **your biggest new technical area**.
- [ ] **Flutter refresh** (§4): widgets, Bloc/Riverpod/GetX, Future/StreamBuilder — **make your dual-stack a headline**.
- [ ] **Local storage** (§1) + **async models** (§2) across frameworks — 20 min each.
- [ ] **Team-lead framing** (§8): 1–2 STAR stories on leading/mentoring/unblocking.
- [ ] **Infra cluster** (§6): one honest sentence each + your microservices bridge — 20 min.
- [ ] **System design** (§5): rehearse designing TalentAxis or Space360 as a design story.
- [ ] Reuse from the **VTVcab pack**: React/JS fundamentals (if a JS project), REST, debugging, PSM-II behavioral.
- [ ] Have **App Store links + GitHub** ready.

---

## 11. What to change on your CV/cover letter for NCC *(if you apply here too)*

Your existing RN CV works with **4 reframes** — say the word and I'll produce an NCC-tailored VN+EN CV + cover + 1-page packet:
1. **Elevate Flutter** to co-headline with React Native (they list Flutter first; it's a differentiator).
2. **Add a team-lead / mentoring line** near the top (PSM II + led Innovation team + mentorship program) — they ask for it.
3. **Add push notifications + local storage + offline** to skills (from your Firebase/Core Data/offline work).
4. **Drop the OTT/Smart-TV framing**, add an **English-comfort + remote** line, and reframe the summary around "Mid/Sen cross-platform engineer, RN + Flutter, ready to lead."

---

*Bottom line: NCC is a **cleaner, more senior fit** than VTVcab — you're squarely Mid/Sen, your RN+Flutter dual stack and PSM-II leadership are exactly what they want, and it's remote. The only real gate is **English** (prepare it), and the only genuinely-new technical study is **push notifications**. Everything else you either have or can honestly frame as concept-level.*
