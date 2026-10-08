# 05 — React Native & mobile deployment

From the React Native candidate (video 4), who had **shipped 3 apps to Google Play** — so this is the most hands-on-deployment interview in the set. RN shares its JS/React model with [[01-javascript-core]], [[02-async-and-event-loop]], and [[03-react-and-hooks]]; this article covers the mobile-specific layer.

## The Android → Google Play pipeline (walk-through question)

A strong, ordered answer:

1. **Generate a keystore** (signing key) with `keytool` or Android Studio. It carries a unique **SHA-1 / SHA-256 fingerprint**. ⚠️ (Candidate called this "SHSH blobs / SH2" and admitted not understanding *why* — it's the app's cryptographic signature.)
2. **Build & sign** the app as an **Android App Bundle (`.aab`)** — Google's preferred distribution format (Play generates optimised per-device APKs from it; smaller downloads than a universal APK). ⚠️ (Candidate said ".abb, because Google recommends it's lighter" — right instinct, format is `.aab`.)
3. **Create the app** in **Google Play Console**; start on a **testing track** (Internal → Closed → Open) before Production to test the release flow.
4. **Upload the `.aab`** + required store assets: screenshots for multiple device sizes, description, content rating, privacy policy, etc.
5. **Submit for review.** Google's review runs automated + policy checks; expect **a few hours to ~2–3 days**, and be ready for **policy rejections** (deprecated APIs, permission misuse, ads/data policy) — fix and resubmit. First submissions commonly fail once or twice.
6. After approval, **promote** the testing release to Production.

**Load-bearing detail the candidate missed:** the keystore is **bound to the app forever** — lose it and you can't ship updates to that listing (unless enrolled in Play App Signing). Back it up.

## Fastlane (candidate hadn't heard of it — worth knowing)

- Open-source **automation for iOS + Android** build/sign/test/release, driven by Ruby "lanes". One `fastlane deploy` can build, run tests, bump the build number, and upload to Play / TestFlight.
- Signal it addresses: shipping 3 apps *by hand* each time is slow and error-prone — automate the pipeline.

## HTTP clients — Axios vs fetch

- **`fetch`** — built-in, zero-dependency; more boilerplate; no interceptors; manual JSON + error handling.
- **Axios** — library; cleaner API, **request/response interceptors** (attach auth tokens, retry, global error handling), timeouts, cancellation, automatic JSON. Preferred for production.
- Candidate knew Axios by name but used `fetch` "to keep it simple" — fine to start; switch to Axios once you need auth headers / global error handling. ⚠️ ("Isaac/IAC" in the captions = Axios.)

## REST vs GraphQL (for a mobile backend)

- **REST** = resource-based, fixed endpoints returning fixed shapes; simple to build/cache; can over- or under-fetch (multiple round-trips).
- **GraphQL** = single endpoint, the client asks for **exactly the fields it needs**; fewer round-trips; needs a GraphQL server + more setup; caching is *different* (persisted queries), not impossible.
- For a typical RN app, **REST + SQL is the standard and usually sufficient**; GraphQL shines with many clients / complex nested data (deeper taxonomy: [[api-types/_index]]). Candidate uses REST + MySQL and hadn't touched GraphQL — normal at junior level.

## React Native context (from the interview)

- Candidate's path: 2 yrs Java/Android → ~2–3 months serious RN; uses **Expo**-style tooling; prefers JS over TS for shipping speed (see the TS trade-off in [[01-javascript-core]]).
- Career framing that landed well: **specialise in one stack first (RN), then add native Kotlin/Swift** — depth before breadth. Interviewers value this over "I'll learn everything at once".

## Key Takeaways

- Play Store pipeline: **keystore (SHA fingerprint) → sign `.aab` → Console + testing track → upload assets → review (fix policy rejects) → promote to Production**; the keystore is permanent — back it up.
- Know **`.aab` vs APK** and that Google prefers the bundle.
- **Axios over fetch** in production for interceptors/auth/error handling.
- **REST + SQL** is fine for most RN backends; reach for GraphQL only when the fetch pattern justifies it.
- Automate releases with **Fastlane** once you ship repeatedly.

**Sources:** video 4 (PVO5). Related: [[01-javascript-core]] · [[03-react-and-hooks]] · [[api-types/_index]] · [[nodejs-backend-interview/04-rest-graphql-api-design]].
