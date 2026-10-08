# Top-3 STAR Scripts — spoken, ~60 seconds each

> Your three strongest real stories, folded into Situation → Task → Action → Result and paced for the room. **Memorize the *shape*, not the words** — S→T→A→R — then let it flow.
>
> **Legend:** `/` = short pause (comma) · `//` = full stop, breathe · **bold** = stress this word. The pauses double as accent aids — pause, breathe, and land the final consonants. Speak ~30% slower than feels natural.
>
> **Honest calibration:** these are true to your logs. Lead with mobile/React Native; native-iOS + backend at concept/bridge level, "ramping." Don't inflate — the OAuth and release stories are genuinely senior on their own.

---

## 1. The difficult bug — OAuth refresh-token on React Native  ⭐ *(your best "hard problem" story)*

*(S)* "Sure. // On **TalentAxis**, / I was integrating **multi-provider OAuth** — Google, LinkedIn, Microsoft, Apple — into our **React Native** app, / and login worked on web but **broke on mobile**. //
*(T)* My job was to get the **login and token-refresh** flow working on React Native. //
*(A)* Digging in, / I found the cause: / React Native's networking **drops the backend's HttpOnly refresh-token cookie**, / so the mobile app could never capture the refresh token. // Instead of guessing, / I built a **curl test matrix** to prove the exact server behavior — / how login delivers the token, / that cookie-replay refresh **works and is non-rotating**, / and that the endpoint **isn't device-scoped**. //
*(R)* So I turned a vague 'auth is broken' into a **precise, reproducible backend ask** — / return the refresh token in the login **body**, because RN drops the cookie. // The mobile side is **proven** — it lights up the moment the backend ships that. // The lesson I took: / **debug by evidence, not assumption**. //"

- **Emphasize:** the Action → the *test matrix*. That's the senior signal — you reproduced and proved behavior instead of guessing.
- **Likely follow-ups (prep these):** *"Why does RN drop the cookie?"* → RN's fetch/networking layer doesn't persist HttpOnly cookies the way a browser does — the JS side has no shared cookie jar. · *"Access token vs refresh token?"* → short-lived access token for requests, long-lived refresh token to get new ones. · *"Did it get resolved?"* → honest: the mobile half is done and proven; the backend body-delivery fix is the pending ask.

---

## 2. End-to-end ownership — shipping two apps + D-U-N-S  ⭐ *(your "ownership / production challenge" story)*

*(S)* "We had **two apps** to ship — **Space360** and **TalentAxis** — to both the App Store and Google Play, / and the company had **no developer accounts** yet. //
*(T)* I owned the **whole release path**, / from account setup to store approval. //
*(A)* First I set up the company **Apple and Google developer accounts** — / which meant getting a **D-U-N-S number** to verify the business through Dun and Bradstreet, / a multi-day process I coordinated end to end. // Then I built the **EAS Build and Submit** pipeline for **iOS and Android**, / TestFlight, / and version management across many builds. // I also handled **real Apple rejections** — / I added in-app **account deletion** for guideline 5.1.1, / hid external payment and signup on iOS for 3.1.1, / and added **Sign in with Apple** for 4.8. //
*(R)* The result: / **both apps are live**, / I shipped dozens of production builds, / and I know the store process **end to end** — from D-U-N-S to approval. //"

- **Emphasize:** "no developer accounts yet → I owned it from D-U-N-S to approval." That framing = ownership.
- **Likely follow-ups:** *"Walk me through the account-deletion fix"* → a Delete-Account flow that deletes the user's data via a Supabase edge function, revokes the Sign-in-with-Apple token, with a confirmation step + a screen recording for Apple. · *"How long did D-U-N-S take?"* → a few business days through Dun & Bradstreet. · *"iOS vs Android release differences?"* → keystore/`.aab` + testing tracks on Google Play; certificates/provisioning + TestFlight on iOS.

---

## 3. Architecture depth — the hireui frontend  ⭐ *(your "React/full-stack breadth" story)*

*(S)* "**hireui** is our **Next.js 14 App Router** frontend for the hiring platform, / and I work across its **architecture** — state, API, and auth. //
*(T)* A big part of my job is keeping that architecture clean as it grows. //
*(A)* The state strategy is **deliberate and layered**: / **React Query** for server state, / **light Redux** for auth UI, / **Zustand** for small UI state, / and **Context** for the session. // The rule is simple — / server data goes to React Query, / client data to a store — / so they never collide. // For the API, / there's a **centralized Axios layer** with interceptors that attach the token / and — the part I like — **queue requests during a token refresh**, / so we never fire parallel refreshes. // Access is gated by **role and feature-flag guards**, / and it ships as a **static export** for CDN-friendly hosting. //
*(R)* The result is a **clean separation**: / new contributors know exactly where to build, / server-versus-client state don't fight, / and auth refresh is **race-safe**. //"

- **Emphasize:** the *refresh-queue* detail and "server vs client state never collide" — those show you understand *why*, not just *what*.
- **Likely follow-ups:** *"Three state libraries — isn't that too many?"* → each has a distinct job (server / auth-UI / small-UI); Redux is intentionally light. · *"How does the refresh-queue actually work?"* → on a 401, hold new requests, run **one** refresh, then replay the queue with the new token. · *"Why static export?"* → simpler, CDN-friendly hosting; the trade-off is you lose Next's server-side image optimization, so we rely on pre-optimized/CDN assets.

---

## Rehearsal checklist
- [ ] Say each **out loud, timed** — aim ~60s. If you run past 75s, cut a clause, don't speed up.
- [ ] Land the **Result** sentence with a clear stop — that's what the interviewer remembers.
- [ ] For each, have the **one follow-up answer** ready (above) — that's where the real depth check happens.
- [ ] Nail the hard words: **React Native**, **HttpOnly**, **refresh token**, **D-U-N-S** ("dun and bradstreet"), **guideline**, **Axios**, **static export**.
- [ ] Record yourself once; if *you* stumble on a word, simplify it.

*One-thing rule: open the concept in a line, tell the STAR, close on the Result. Concept + real story = senior.*
