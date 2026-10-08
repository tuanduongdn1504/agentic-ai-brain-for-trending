# Real Experience Evidence Bank — theory ↔ your real work

> **Purpose:** interview answers land twice as hard when you pair the concept with a real thing you did. This maps the theory (from your RN / Node / Swift prep packs) to **genuine accomplishments extracted from your work logs** — so you can say *"The theory is X. I actually did X when…"*
>
> **All secrets redacted.** No passwords, tokens, keys, or colleagues' personal data are in this file (see the rotation warning you were given — rotate them). App Store IDs below are public.

**How to use it:** answer the concept in one line → then attach the anchor: *"…and I did exactly this on TalentAxis / Space360 / hireui."* Concept + real anchor = senior. Concept alone = junior.

---

## The 10 evidence blocks

### 1. Mobile release & deployment engineering  ⭐ *(your strongest, most concrete asset)*
**What you actually did:** Owned the full release pipeline for **two shipped apps** — **Space360** (App Store `id6760685791` + Google Play, v1.0.x through ~build 21) and **TalentAxis mobile** (App Store `id6775423029`, v0.1.x through ~build 14). EAS Build + EAS Submit for **both iOS and Android**, **local *and* cloud** builds (`.ipa`, `.aab`, `.apk` splits), TestFlight distribution, App Store Connect + Google Play Console, **build-number/version management** across many submissions, staging/preview/production EAS profiles, Fastlane.
**Proves (RN Prep Pack §12 deployment):** the keystore→`.aab`→Play-Console→TestFlight pipeline, "end-to-end ownership."
**Say it like this:** *"I own the mobile release pipeline for two live apps — EAS Build/Submit for iOS and Android, TestFlight and App Store Connect, Google Play, version management, both local and cloud builds. I've shipped dozens of production builds."*

### 2. Company developer accounts + D-U-N-S  ⭐ *(ownership beyond code)*
**What you actually did:** Set up the **company Apple Developer Program (organization) + Google Play** accounts, including the **D-U-N-S business verification** through Dun & Bradstreet for the company entity — a multi-day (2–5 business day) process you researched, submitted (business license), and coordinated to completion, then completed the Apple org enrollment.
**Proves (RN Prep Pack §12 "what does end-to-end ownership mean"):** the D-U-N-S story is literally in your prep — now with real dates.
**Say it like this:** *"I even set up the company developer accounts — getting a company Apple/Google account needs a D-U-N-S number to verify the business, a multi-day process through Dun & Bradstreet that I owned end to end, then the Apple organization enrollment."*

### 3. App Store review-guideline compliance  ⭐ *(the "handled a rejection" story, real ticket IDs)*
**What you actually did:** Handled **real App Store review requirements**: implemented **in-app Account Deletion** (Guideline 5.1.1(v)) — including a Supabase `delete-account` edge function; **hid external payment/subscription + signup on iOS** (Guideline 3.1.1(v)); added **Sign in with Apple** (Guideline 4.8). Multiple resubmit cycles, got approved.
**Proves (RN Prep Pack §4 "a time something didn't go as planned"):** the Space360 rejection → account-deletion fix story, now concrete.
**Say it like this:** *"I've handled real App Store rejections — added in-app account deletion (5.1.1), hid external payment and signup on iOS (3.1.1), and implemented Sign in with Apple (4.8). I know Apple's guidelines from the resubmit trenches, not from a doc."*

### 4. OAuth + auth-token deep debugging  ⭐⭐ *(your best senior-engineering story — current TalentAxis work)*
**What you actually did:** Integrating **multi-provider OAuth** (Google, LinkedIn/PKCE via expo-auth-session, Microsoft, Apple) into the React Native app. The hard part: **React Native's networking drops the backend's HttpOnly refresh-token cookie**, so the refresh token was invisible to mobile. You **proved the exact server behavior with a reproducible curl test matrix** — login token-delivery + casing, refresh cookie-replay (200, **non-rotating**), **device-scoping** (found it's device-agnostic), rotation — and turned a vague "auth is broken" into a **sharp, evidence-backed backend ask** ("`/auth/login` must return the refresh token in the body because RN drops the HttpOnly cookie").
**Proves (RN §3 "difficult technical problem" + Node board §auth/JWT/refresh-rotation + "debug by evidence"):** this is textbook senior debugging — reverse-engineering an API's real behavior with a repeatable harness instead of guessing.
**Say it like this:** *"On TalentAxis I integrate OAuth into React Native. The blocker was subtle: RN drops the backend's HttpOnly refresh-token cookie, so mobile couldn't capture the refresh token. Instead of guessing, I built a curl test matrix that proved the login delivery shape, that cookie-replay refresh works and is non-rotating, and that the endpoint isn't device-scoped — then handed the backend a precise, reproducible ask. That evidence-first approach is how I debug."*

### 5. Monorepo + build-system engineering
**What you actually did:** Set up a **pnpm workspace monorepo** sharing a **Vite web app's `src` with an Expo mobile app** via a web-bridge for shared logic. Debugged the **EAS build failures from package-manager/lockfile mismatches** (a stray `package-lock.json` made EAS install with npm → `expo` never installed → wrong SDK) — fixed by removing stray lockfiles, pinning `"packageManager": "pnpm@…"`, and setting `nodeLinker: hoisted`. Pinned `react-native-worklets` for Reanimated 4 compat; guarded Metro `watchFolder`/alias with `existsSync`.
**Proves (Node board §Node scaling/tooling + RN §Expo vs bare, EAS):** real build-system + monorepo depth.
**Say it like this:** *"I set up a pnpm monorepo where the Expo app reuses the Vite web app's source, and I've debugged the gnarly EAS build failures — lockfile/package-manager mismatches, Reanimated/worklets version pinning, Metro config guards."*

### 6. Native toolchain debugging  *(the visionOS story — real & dated)*
**What you actually did:** Fixed a native iOS build failure — `pod install` → `undefined method 'visionos'` in `react-native-safe-area-context` — a **toolchain version mismatch** (CocoaPods too old for the new visionOS platform key) compounded by a broken Homebrew on a new macOS. Traced it, updated CocoaPods, cleaned/relinked Homebrew, reinstalled the native modules (switched `react-native-linear-gradient` → `expo-linear-gradient`). Also set up the Android side (JDK 8→21 Temurin, `ANDROID_HOME`, `local.properties`, SDK).
**Proves (RN §1.8 native modules):** "native build errors are usually toolchain/version, not your app code."
**Say it like this:** the visionOS story from your RN pack — now you can date it and name the exact fix.

### 7. hireui frontend architecture  *(React/Next.js/full-stack breadth)*
**What you actually did:** Work on **hireui**, a **Next.js 14 App Router** frontend (TypeScript strict), **static export**, Ant Design + Tailwind + SCSS-modules, **multi-store state strategy** (TanStack **React Query** for server state, **Redux Toolkit** light, **Zustand** for small UI state, React **Context** for auth), a **centralized Axios layer** with interceptors doing **token-refresh with request queuing**, **role-based + feature-flag guards**, a **service-per-domain API layer**, next-intl i18n, Sentry, Playwright/Vitest/Jest/Storybook, Docker/supervisord/AWS CodeDeploy.
**Proves (Node board §state mgmt / API layer / auth; RN §state, §API):** you can speak to a real, sophisticated frontend architecture — *why* React Query for server state vs Redux/Zustand for client, and a real refresh-token-queuing interceptor.
**Say it like this:** *"On hireui (Next.js 14 App Router) I work across a deliberate multi-store strategy — React Query for server state, light Redux, Zustand for UI — a centralized Axios layer that queues requests during token refresh, and role + feature-flag guards."*

### 8. Backend-adjacent / Supabase  *(the "growing full-stack" proof)*
**What you actually did:** Deployed **Supabase edge functions** (e.g. `delete-account`) via the Supabase CLI (link + deploy), used Supabase **auth** (updateUser, signup, password reset), **storage/S3**, and consumed a **microservices** backend (user/hire/payment/scheduler/auto/comm services) from the client. On the web you've built with a **FastAPI + SQLite** service (claude-agentic-os).
**Proves (Node board §backend, DB, auth; the "full-stack" question):** honest, real full-stack bridge — *"mobile/RN core, but I deploy edge functions, integrate microservices, and I've built a small backend myself."*
**Say it like this:** *"My core is mobile/React Native, but I integrate against microservices, deploy Supabase edge functions, and I've built a small FastAPI+SQLite backend — so I'm genuinely growing full-stack."*

### 9. Git workflow & quality gates
**What you actually did:** SSH-key + signed-commit setup, Jira-ticket-linked branch naming (`feature/…-<TICKET>`, `hotfix/…`), conventional commits (`feat:`/`chore:` + ticket ID) enforced by **Husky + lint-staged + commitlint + pre-commit hooks**, a machine-enforced **branch-policy hook**, ESLint (Airbnb) + Prettier, PR review flow.
**Proves (mobile brief §8 Git flow + the merge-conflict red flag; SOLID/DRY):** real, disciplined workflow.
**Say it like this:** *"Feature branches linked to Jira tickets, conventional commits enforced by Husky/commitlint, PR review before merge — and I resolve conflicts by editing to the correct result, never by renaming files."*

### 10. AI-first / agent tooling  *(your differentiator — real, not hype)*
**What you actually did:** Daily **Claude Code** + custom skills; **GitNexus** MCP (code-graph, incl. debugging its native-addon `dlopen` failure across projects); harness/agent setup; **AgentShield** security scans of your agent config (graded, acted on findings); built two OSS agentic projects (agentic-ai-brain, claude-agentic-os).
**Proves (all packs' AI-first differentiator; the honest guardrail):** you use AI at a level most candidates don't — *with* judgment.
**Say it like this:** *"I use Claude Code and custom skills every day, I run code-graph tooling and even security-scan my own agent config — but I keep review, tests, and security decisions in my own hands."*

---

## Quick-reference: topic → your real anchor *(attach one to every answer)*

| When they ask about… | Anchor to |
|---|---|
| App Store release / deployment | Space360 + TalentAxis EAS Build/Submit, TestFlight, ~35 prod builds |
| A hard bug / debugging | the OAuth HttpOnly-refresh-token investigation (curl test matrix) |
| A production challenge | the Space360 Apple rejection → account-deletion fix |
| End-to-end ownership | the company D-U-N-S + developer-account setup |
| Native / build issues | the visionOS/CocoaPods toolchain fix |
| State management / API layer | hireui: React Query + Redux + Zustand + Axios refresh-queue |
| Full-stack / backend | Supabase edge functions + microservices + FastAPI/SQLite (claude-agentic-os) |
| Auth / JWT / refresh tokens | the RN cookie-vs-body refresh-token work on TalentAxis |
| Monorepo / tooling | pnpm workspace (Vite web + Expo mobile), EAS lockfile debugging |
| Git / workflow | Jira-linked branches, Husky/commitlint, PR review |
| AI-first | Claude Code daily, GitNexus, AgentShield, 2 OSS agentic projects |

---

*Honest calibration (unchanged): lead with mobile/React Native, present native-iOS and backend at concept/bridge level, "ramping." Everything above is drawn from your own work logs — don't inflate it, but don't undersell it either: the OAuth-debugging and release-engineering stories are genuinely senior. Rotate the leaked credentials.*
