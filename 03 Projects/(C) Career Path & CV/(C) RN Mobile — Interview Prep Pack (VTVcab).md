# Interview Prep Pack — VTVcab · Mobile React Native Developer

**Candidate:** Dương Văn Tuấn · **Role:** OTT apps on Smart TV (WebOS) + DRM / payment / ads integration · **Location:** Đà Nẵng (on-site).

> **Language note:** VN interview will likely be **Vietnamese with English technical terms**. Answers below are in English (standard tech vocab) so you can speak them either way; the **behavioral / PSM-II section** has Vietnamese cues. Answer in whatever language the interviewer uses.
>
> **Honesty rule (non-negotiable):** where you have real experience → say it concretely (App Store apps, NodeMedia, crash root-causing, PSM II). Where you don't (WebOS, DRM, payment) → say "I haven't built X, here's the model and how I'd ramp." Interviewers trust a candidate who draws that line. Faking it is what gets caught.

---

## 0. Your 20-second positioning (open + close with this)

> "5 years building production React Native apps — I own products end-to-end from the client through API integration, with apps live on the App Store and Google Play. I've integrated live streaming with NodeMedia, so OTT is familiar territory. I'm a PSM II Scrum Master, so I bring product and team thinking, not just code. Smart-TV/WebOS is new to me, but it's React on the web underneath — my React fundamentals transfer directly, and I ramp fast with AI-assisted workflows I keep review-gated."

The three pillars: **shipped React apps · OTT-adjacent (NodeMedia) · product/team mind (PSM II).** The one honest edge: **WebOS/TV is new.**

---

## 1. React / JavaScript fundamentals

*(JD: "In-depth knowledge of React.js and its fundamentals", "Understanding of modern ECMAScript". This is your home turf — be crisp.)*

**Q: React Native vs React.js — what's the difference, and does your RN experience transfer to web/TV React?**
A: Same core — components, JSX, hooks, one-way data flow, the reconciliation/diffing model. The difference is the render target: React.js renders to the **DOM** (HTML/CSS in a browser); React Native renders to **native views** via a bridge. WebOS TV apps run in a browser engine, so they're **React.js on the web** — my component design, hooks, and state patterns transfer directly; what I'd learn is DOM/CSS layout for TV and the remote-control navigation model.

**Q: `useEffect` — how does it work, common mistakes?**
A: Runs after render; the dependency array controls when. Empty `[]` = once on mount; `[x]` = when `x` changes; no array = every render. Return a cleanup function for subscriptions/timers. Common bugs: missing deps (stale closures), an object/array dep that's recreated each render (infinite loop), and doing work that should be an event handler inside an effect.

**Q: State vs props? Controlled vs uncontrolled?**
A: Props = passed in, read-only to the child; state = owned and mutable by the component. Controlled component = value driven by React state (`value` + `onChange`); uncontrolled = the DOM holds the value (refs). Controlled is preferred for validation and single-source-of-truth.

**Q: Why keys in lists? Why not the array index?**
A: Keys let React match elements across renders so it only re-renders what changed. Index-as-key breaks on reorder/insert/delete — React reuses the wrong node, causing state/UI bugs. Use a stable unique id.

**Q: `useMemo` / `useCallback` / `React.memo` — when?**
A: `useMemo` caches an expensive computed value; `useCallback` caches a function identity so memoized children don't re-render; `React.memo` skips re-render when props are shallow-equal. Don't sprinkle everywhere — measure first; premature memoization adds complexity for no gain.

**Q: The virtual DOM / reconciliation?**
A: React builds a lightweight tree of the UI, diffs the new tree against the previous one, and applies the minimal set of real changes. Keys + component identity drive the diff. (On RN it's the same idea against the native view tree.)

**JavaScript / ECMAScript quick-fire:**
- **Closures:** a function remembering the scope it was created in — basis of hooks and module privacy.
- **`==` vs `===`:** `===` no type coercion; always prefer it.
- **`var`/`let`/`const`:** `var` = function-scoped + hoisted; `let`/`const` = block-scoped; `const` = no reassignment (object contents still mutable).
- **Event loop:** single-threaded; call stack + microtask queue (promises) + macrotask queue (timers). Microtasks drain before the next macrotask.
- **Promises / async-await:** async-await is syntactic sugar over promises; `await` pauses the async fn, not the thread. Always `try/catch` or `.catch()`.
- **ES6+:** destructuring, spread/rest, arrow fns (lexical `this`), template literals, modules (`import/export`), optional chaining `?.`, nullish coalescing `??`, `async/await`.
- **`this`:** depends on call-site; arrow functions capture `this` lexically (why they're used in class handlers / callbacks).

---

## 2. Redux / state management

*(JD lists "Flux, and Redux". You have Redux — own it.)*

**Q: Explain Redux / the Flux pattern.**
A: One-way data flow. A single **store** holds state; you dispatch an **action** (a plain object describing what happened); a **reducer** is a pure function `(state, action) => newState` that returns the next state immutably; the UI subscribes and re-renders. Flux is the general pattern (unidirectional flow, dispatcher → store → view); Redux is the popular single-store implementation of it.

**Q: Why immutability in reducers?**
A: React/Redux detect change by reference equality. Mutating state in place breaks change detection (components don't re-render / time-travel debugging breaks). You return new objects/arrays (spread, or Redux Toolkit's Immer which lets you "mutate" a draft safely).

**Q: Redux Toolkit vs classic Redux?**
A: RTK is the modern default — `configureStore`, `createSlice` (reducers + actions together), Immer built in, thunks included. Cuts boilerplate massively. Classic Redux is the same model with hand-written action types/creators.

**Q: Middleware — thunk vs saga?**
A: Middleware sits between dispatch and the reducer for side effects (async, logging). **Thunk** = dispatch a function for async logic (simple, most common). **Saga** = generator-based, better for complex orchestration/cancellation. For most apps, thunk (or RTK Query) is enough.

**Q: When do you NOT reach for Redux?**
A: Local UI state → `useState`. Cross-cutting but simple → Context. Server data → React Query / RTK Query (caching, refetch). Redux earns its place when you have complex, shared, frequently-updated client state. *(You can cite React Query and Zustand from your real stack here.)*

---

## 3. REST APIs

*(JD: "Familiarity with JavaScript, REST APIs". You integrate these daily — give real examples.)*

**Q: REST principles / HTTP methods / status codes?**
A: Resources addressed by URL, stateless requests, standard verbs: **GET** (read), **POST** (create), **PUT/PATCH** (update — PUT replace, PATCH partial), **DELETE**. Status families: 2xx success (200 OK, 201 Created, 204 No Content), 3xx redirect, 4xx client error (400 bad request, 401 unauthenticated, 403 forbidden, 404 not found, 409 conflict, 429 rate-limited), 5xx server error.

**Q: How do you handle auth in the client?**
A: JWT — store the access token, send it in `Authorization: Bearer`, refresh on 401 with a refresh token; never hard-code secrets in the app. *(You've done JWT + REST against Django/FastAPI microservices — say that.)*

**Q: How do you handle errors, loading, retries, and caching on the client?**
A: Centralize an API client (axios interceptors or a fetch wrapper) for auth headers + error mapping; per-request loading/error state (or React Query, which gives caching, dedup, retry, and background refetch out of the box); exponential backoff for transient failures; pagination/infinite scroll for lists.

**Q: REST vs GraphQL — when each?**
A: REST = simple, cacheable, resource-oriented; GraphQL = client asks for exactly the fields it needs, one round-trip for nested data (good for complex screens, avoids over/under-fetching). *(You've used both — GraphQL on Flutter at Enouvo, REST at CVTOT.)*

---

## 4. Smart TV / WebOS  ⚠️ *(new to you — concept + ramp, be honest)*

**Say up front:** "I haven't built for WebOS yet — here's what I understand and how I'd get productive fast."

**What WebOS is:** LG's Linux-based **web-centric** TV OS. Apps are built with **web tech (HTML/CSS/JS, commonly React)** and packaged as `.ipk`, submitted to the **LG Content Store**. LG provides **webOS TV SDK / CLI (`ares-*` tools)** and JS APIs (`webOSTV.js`) for system services (device info, DRM, media). Legacy apps used the **Enyo** framework; modern ones use React/plain web.

**The three things that are genuinely different from mobile:**
1. **Remote-control navigation, not touch.** No tap/scroll — **D-pad / spatial navigation**: focus moves up/down/left/right, OK to select, Back to go up. You manage a **focus engine** and visible focus states. (Libraries: LG's SpatialNavigation, or `@noriginmedia/react-spatial-navigation`.)
2. **10-foot UI + constrained hardware.** Big, legible layouts viewed from across the room; TVs have **weaker CPU/GPU and less RAM** than phones → performance and memory discipline matter (virtualized lists, lazy images, avoid heavy re-renders — *this is where your crash/perf root-causing experience is relevant*).
3. **Media playback + DRM are first-class.** TV apps live around a video player (see §5–6).

**Your honest ramp line:** "It's React on a browser engine, so my component/state/hooks skills carry over directly. What I'd learn is the D-pad focus model, the webOS SDK/media APIs, and TV performance limits — a few weeks to be productive given my React and streaming background."

---

## 5. OTT / streaming  ✅ *(your NodeMedia bridge — lead with it)*

**Q: What's OTT and what's the anatomy of a streaming app?**
A: OTT = delivering video "over the top" of the internet, no cable box. The pipeline: **ingest/encode → package (HLS/DASH) → CDN → player on device**. The player fetches a **manifest** (`.m3u8` for HLS, `.mpd` for DASH) that lists segments at multiple bitrates.

**Q: Adaptive bitrate (ABR)?**
A: The stream is encoded at several resolutions/bitrates; the player measures bandwidth + buffer and switches rendition on the fly to avoid stalls. HLS and MPEG-DASH are the two standards.

**Q: Which players?**
A: On web/TV: **Shaka Player**, **hls.js**, **dash.js**, **video.js**. They handle manifest parsing, ABR, and (with EME) DRM.

**Your bridge:** "At CVTOT I integrated **live streaming with NodeMedia** — I've worked with the client-side of a live video pipeline, stream setup, and playback. So the streaming mental model (ingest → deliver → play, buffering, latency) is familiar; VOD/HLS-DASH on TV is an extension of that."

---

## 6. DRM (Digital Rights Management)  ⚠️ *(concept-level — honest)*

**Say:** "I understand the model; I haven't implemented a DRM integration."

**The model:**
- DRM encrypts the video; only an authorized device with a valid **license** can decrypt and play.
- Three big systems by platform: **Widevine** (Google — Android/Chrome/many TVs), **PlayReady** (Microsoft — Windows/some TVs), **FairPlay** (Apple — Safari/iOS/tvOS). TV apps often need **multi-DRM**.
- **How it plugs in on web/TV:** the browser exposes **EME (Encrypted Media Extensions)**; the **CDM (Content Decryption Module)** does the decryption; the player (Shaka/dash.js) requests a **license from a license server** using a challenge, gets a key, decrypts. Content is fetched from the CDN, the license from the license server — two separate flows.
- **Vendors** you might hear: Widevine (direct), or aggregators like Axinom, PallyCon, EZDRM, BuyDRM.

**Your honest line:** "I'd own the client integration — wiring the player to the EME/CDM and the license server, handling license errors and secure playback — and lean on the DRM vendor's SDK. My API-integration background makes that a natural fit."

---

## 7. Payment integration  ⚠️ *(no experience — be fully honest; you told me so)*

**Say plainly:** "I haven't integrated a payment gateway directly — but I know the model and my API-integration track record means I ramp fast, safely."

**The model (know this much):**
- **Never handle raw card data yourself** — you'd fail PCI-DSS. You integrate a **gateway** (client collects via the gateway's SDK/hosted field → gateway returns a **token** → your backend charges the token). The app deals in tokens, not card numbers.
- **Webhooks** notify your backend of async payment events (success/fail/refund) — verify their signature; don't trust the client alone.
- **Idempotency keys** prevent double-charging on retries.
- For TV/OTT specifically: subscriptions/entitlements, in-app-purchase or store billing, and platform rules (LG Content Store billing, or a gateway).
- VN context: gateways like **VNPay, MoMo, ZaloPay** alongside international ones (Stripe, etc.).

**Your honest line:** "It's a new area for me. I'd start by owning the client-side integration against the gateway SDK and the webhook-driven state on the backend side I've done API integration for. I'd be upfront that I'd need to learn the payment/PCI specifics carefully — money bugs are unforgiving."

---

## 8. Troubleshooting & debugging  ✅ *(the JD wants it; you have a real story)*

**Q: Walk me through debugging a hard bug.**
A: *(Your real story — the crash reduction at Enouvo.)* "I inherited an app with frequent crashes. I reproduced consistently, read the crash logs/stack traces to find the pattern, isolated the root cause rather than patching symptoms, fixed it, and added guards/tests so it wouldn't regress. Crash rate dropped materially." [FILL: add a number if you have one — e.g. crash-free sessions %].

**Toolbelt:** React DevTools (component tree, props, re-renders), Flipper / RN debugger, Chrome DevTools for web/TV, source maps for prod stack traces, performance profiler for re-render/jank, Sentry/crashlytics for field crashes. **Method:** reproduce → isolate → root-cause → fix → guard against regression.

---

## 9. PSM-II / teamwork / product mindset  ✅✅✅ *(their "what makes you better" list IS you — lean hard here)*

*(Cách trả lời: dùng STAR — Tình huống → Nhiệm vụ → Hành động → Kết quả. Đây là điểm mạnh nhất của bạn; đừng khiêm tốn quá.)*

**Q: Tell me about your Agile / Scrum experience.**
A: "I'm a **PSM II** Scrum Master — I served as Scrum Master for an Innovation team at Enouvo: facilitated ceremonies, removed impediments, coached the team with the Product Owner. Now as an engineer at CVTOT I still drive delivery on Scrum. So I understand sprints, backlog, and cross-functional delivery from both the SM and developer seat."

**Q: A time you handled conflict / disagreement in the team? (Cách xử lý mâu thuẫn)**
A: [FILL: a real STAR story — e.g. a scope/priority disagreement you resolved by facilitating a conversation, not deciding for people. Emphasize listening + finding shared goal.] Frame: "As a Scrum Master I'm trained to surface the disagreement, keep it about the work not the person, and let the team + PO decide with data."

**Q: What does 'product mindset' mean to you? (Tư duy sản phẩm)**
A: "Building the *right* thing, not just building things right. I ask *why* a feature matters to the user and the business before I build it, I flag when a simpler solution gets 80% of the value, and I care that it ships and works for real users — which is why I've owned apps all the way to the App Store, not just to 'done on my machine'."

**Q: How do you communicate / work in a team? (Giao tiếp & teamwork)**
A: "Clearly and early — I raise blockers before they become fires, document engineering practices so the team isn't dependent on me, and I mentor juniors (I ran an internship/mentorship program). Remote or on-site, I over-communicate rather than under."

**Q: How do you use AI tools without cutting corners?**
A: "I use Claude Code and custom Claude Skills every day for high-velocity pair programming, but I keep **code review, tests, and security decisions in my own hands** — the AI drafts, I own the judgment. That's how I move fast without shipping things I don't understand."

---

## 10. Honest gap-handling scripts *(rehearse these — they turn weaknesses into trust)*

- **Enzyme (in JD):** "I test with **React Native Testing Library and Jest** — same goal as Enzyme (component testing), Enzyme's the older equivalent. I can pick it up quickly if the codebase uses it."
- **Webpack (in JD):** "I've worked with bundlers — Metro on React Native, Vite on our React web monorepo. Webpack is the same category; the concepts (entry, loaders, code-splitting) transfer."
- **WebOS / Smart TV:** "New to me, but it's React on the web underneath — the unknowns are the D-pad focus model and the webOS media/SDK APIs, not the fundamentals."
- **Payment / DRM:** "Concept-level, no hands-on integration yet — I'd own the client-side wiring and be careful with the security specifics."
- **Your 5-yr experience vs a mid-level posting:** "I bring senior delivery habits — end-to-end ownership, Scrum leadership, mentoring — and I'm genuinely excited about the OTT/TV domain, which is new and interesting to me."

---

## 11. Smart questions to ask them *(shows product + engineering seriousness)*

1. "Is the TV app built in **React (web) on WebOS**, or React Native targeting TV? What does the current stack look like?"
2. "Which **DRM** system(s) and license/CDN vendors are you on?"
3. "For payment — is it the **LG Content Store billing**, or a gateway (VNPay/MoMo/international)?"
4. "How's the team structured — is there a dedicated Scrum team, and where does this role sit between the TV app, the mobile app, and backend?"
5. "What are the biggest technical challenges right now — performance on low-end TVs, DRM, latency, something else?"
6. "How do you measure success for this role in the first 3–6 months?"

---

## 12. Prep checklist

- [ ] Rehearse the **20-sec positioning** (§0) out loud, VN + EN.
- [ ] Have a crisp **NodeMedia live-streaming** story ready (your OTT bridge).
- [ ] Have the **crash-reduction** debugging STAR story ready (add a metric if you can).
- [ ] Have **2 PSM-II / teamwork STAR stories** ready (conflict + product decision).
- [ ] Skim **WebOS** (D-pad navigation, `.ipk`, LG Content Store, webOSTV.js) — 30 min so the terms aren't new.
- [ ] Skim **OTT playback** (HLS vs DASH, ABR, Shaka Player) — 30 min.
- [ ] Skim **DRM** (Widevine/PlayReady/FairPlay, EME/CDM, license server) — 20 min.
- [ ] Rehearse the **gap-handling scripts** (§10) so they come out calm, not defensive.
- [ ] Pull up your **App Store links** + **GitHub** ready to show.
- [ ] Prepare **your questions** (§11) — pick 3.

---

*Honest overall: this is a role you're genuinely qualified for. Your real gaps (WebOS, DRM, payment) are domain-specific and rampable on top of solid React/JS/REST fundamentals — the interview is won by (1) crisp fundamentals, (2) the NodeMedia + shipped-apps evidence, (3) your PSM-II product/team strength, and (4) drawing the honesty line cleanly on what's new.*
