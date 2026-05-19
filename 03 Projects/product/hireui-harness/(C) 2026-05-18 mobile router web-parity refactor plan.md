# (C) Mobile Router Web-Parity Refactor Plan — hireui

> **Date:** 2026-05-18
> **Target:** `/Users/Cvtot/monorepo/hireui/apps/mobile/app`
> **Scope:** Router-shell only — canonical web-parity paths + token-only auth guards + legacy compat redirects
> **Status:** Plan verified by Claude (this file). Implementation pending operator approval.
> **Prior context:** `(C) 2026-05-06 hireui harness evaluation + best practices.md` + `(C) 2026-05-06 v2 changes - integrating KJ OS concepts.md` (sibling files; harness-system review, not code refactor)

---

## Plan (as proposed)

### Summary

Refactor `apps/mobile/app` so HireUI mobile uses web-parity canonical paths, while borrowing Anspace's split between guest/public routes and protected authenticated routes.

Parity means matching `NAVIGATION_PATHS` without the Next.js `[locale]` segment. Example: web `/[locale]/account/sign-in` becomes mobile `/account/sign-in`; web `/[locale]/auth/candidate-management` becomes mobile `/auth/candidate-management`.

Auth routing will use token-only gating: check the mobile access token via `authAdapter.getAccessToken()`, not web `AuthProvider/useAuth` and not React Query session state.

### Key Changes

- Add a mobile route constants module mirroring the web route contract:
  - `/account/sign-in`
  - `/account/sign-up`
  - `/account/forgot-password`
  - `/account/reset-password`
  - `/account/set-password`
  - `/account/free-trial`
  - `/account/reset-mail`
  - `/account/check-mail`
  - `/account/check-login-mail`
  - `/authentication-result`
  - `/auth/candidate-management`
  - `/auth/jobs`
  - `/auth/company-owner/company-account`
  - `/auth/my-account/plans`

- Replace current canonical Expo routes:
  - `/(auth)/sign-in` → `/account/sign-in`
  - `/(auth)/sign-up` → `/account/sign-up`
  - `/(auth)/reset-password` → `/account/forgot-password`
  - `/(auth)/set-password` → `/account/set-password`
  - `/(auth)/create-company` → `/account/free-trial`
  - `/(auth)/pending-approval` → `/authentication-result`
  - `/(tabs)/candidates` → `/auth/candidate-management`

- Add token-only route guards:
  - Root `/` checks token.
    - token exists → redirect `/auth/candidate-management`
    - no token → redirect `/account/sign-in`
  - `/account/*` guest layout checks token.
    - token exists → redirect `/auth/candidate-management`
    - no token → render account stack
  - `/auth/*` protected layout checks token.
    - token exists → render protected router
    - no token → redirect `/account/sign-in`

- Preserve legacy mobile paths as compatibility redirects for this first pass:
  - `/(auth)/*` redirects to matching `/account/*` or `/authentication-result`
  - `/(tabs)` and `/(tabs)/index` redirect to `/auth/candidate-management`
  - Existing screen internals may keep old `router.push()` targets during this pass because redirects will bridge them.

- Keep HireUI's current Metro/Babel router config:
  - Preserve `EXPO_ROUTER_APP_ROOT`
  - Preserve explicit `projectRoot`
  - Preserve narrower `watchFolders`
  - Do not copy Anspace's whole-monorepo watch or `disableHierarchicalLookup = true`

### Route Mapping

- `/account/sign-in` renders `SignInScreen`
- `/account/sign-up` renders `SignUpScreen`
- `/account/forgot-password` renders `ResetPasswordScreen`
- `/account/reset-password` renders the current set-password/reset-password placeholder until full reset-password form exists
- `/account/set-password` renders `SetPasswordPlaceholderScreen`
- `/account/free-trial` renders `CreateCompanyPlaceholderScreen`
- `/authentication-result` renders `PendingApprovalPlaceholderScreen`
- `/auth/candidate-management` renders `CandidateListScreen`
- `/auth/candidate-management/[id]` renders `CandidateDetailScreen`
- `/candidate-drawer` remains a top-level transparent modal for candidate detail overlays
- `/auth/jobs`, `/auth/company-owner/company-account`, and `/auth/my-account/plans` keep existing mobile placeholder behavior for this pass

### Test Plan

- Run GitNexus impact before editing router symbols and report risk.
- Add tests for route guard behavior:
  - root redirects to `/account/sign-in` when token missing
  - root redirects to `/auth/candidate-management` when token exists
  - account layout redirects authenticated users away from guest routes
  - auth layout redirects unauthenticated users to sign-in
- Add route compatibility tests:
  - legacy `/(auth)/sign-in` redirects to `/account/sign-in`
  - legacy `/(tabs)` redirects to `/auth/candidate-management`
- Run:
  - `pnpm --filter @talentaxis/mobile exec tsc --noEmit`
  - targeted Jest tests with `--no-watchman` if Watchman permissions fail

### Assumptions

- "Strict web parity" means matching web `NAVIGATION_PATHS` values after removing the Next.js `[locale]` segment.
- This pass is router-shell only: no full screen rewrites, no full i18n migration, and no complete placeholder coverage for every web route.
- Auth guard is intentionally token-only and does not fetch current user, roles, permissions, company status, or plan status yet.
- Existing old mobile routes stay temporarily as redirects so current screen navigation calls do not break.

---

## (C) Verification — Claude analysis 2026-05-18

> **Verdict:** Directionally sound, scope-disciplined, executable as drafted. ~75% complete — 3 HIGH-priority clarifications + 4 MEDIUM gaps to resolve before implementation. Plan is a good fit for the "minimal viable refactor + compatibility shim" archetype; well-aligned with vault discipline on explicit assumptions and conscious non-borrowing.

### Strengths (preserve)

1. **Scope discipline** — "router-shell only, no full screen rewrites, no full i18n migration" is the single most valuable line in the plan. It prevents scope creep that would turn a 1-PR refactor into a multi-sprint project.
2. **Token-only auth pragmatism** — explicitly NOT using `AuthProvider/useAuth` or React Query session state. This is the minimal-viable-check pattern; matches vault preference for thin-shell first passes.
3. **Conscious non-borrowing from Anspace** — explicit rejection of whole-monorepo watch + `disableHierarchicalLookup = true`. Non-borrowing called out, not silently omitted. Matches "honest disclosure" discipline (vault Pattern #83 promotion-eligible at v68).
4. **GitNexus impact analysis baked into test plan** — matches vault fact-verification protocol (Concept 12 in the v2 hireui evaluation).
5. **Explicit Assumptions section** — 4 assumptions stated upfront, including the "router-shell only" boundary and the deliberate non-fetching of user/roles/permissions.

### Concerns — must resolve before execution

#### HIGH (3)

**H1. `/account/reset-password` vs `/account/set-password` collision**
Both routes reference "the current set-password/reset-password placeholder". Route Mapping says:
- `/account/reset-password` renders "the current set-password/reset-password placeholder until full reset-password form exists"
- `/account/set-password` renders `SetPasswordPlaceholderScreen`

If both render the same placeholder, why two paths in the constants module? If they differ, the difference isn't documented. Web likely has different intents (forgot-password flow vs admin-initiated set-password flow). **Operator clarification required:** confirm whether these are intended-distinct flows that just share a placeholder for now, or whether the constants module should drop one.

**H2. Token-only guard doesn't address expiry / revocation**
`authAdapter.getAccessToken()` returns whatever's on disk. It says nothing about validity. Stale or revoked tokens will pass the layout guard, then fail at first API call. The plan needs an explicit contract for the 401 case:

- Suggested addition: "On API 401, clear token via `authAdapter.clearAccessToken()` + redirect to `/account/sign-in`."
- Without this, users with expired tokens land on `/auth/candidate-management`, see API errors, and have no path back to sign-in except force-quit.

**H3. Package name unverified — `@talentaxis/mobile`**
Test plan specifies `pnpm --filter @talentaxis/mobile exec tsc --noEmit`. The v1 / v2 hireui harness evaluations (2026-05-06) reference `apps/mobile` with no `@talentaxis` namespace. Either:
- (a) the package was renamed between 2026-05-06 and now,
- (b) the plan was drafted by an agent that didn't verify against `apps/mobile/package.json`, or
- (c) the namespace was always there and the evaluation docs just used the path shorthand.

**Verify before execution:** `cat /Users/Cvtot/monorepo/hireui/apps/mobile/package.json | grep '"name"'`. If mismatch, fix the test command before it lands in CI.

#### MEDIUM (4)

**M1. Implementation order is implicit**
Sequence matters to avoid breaking navigation mid-PR. Suggested explicit order:

1. Add route-constants module (zero behavior change)
2. Add new route files in `apps/mobile/app/account/` and `apps/mobile/app/auth/` (parallel to old; render same screens)
3. Add token-only layout guards on new layouts
4. Add compatibility redirects on legacy `/(auth)/*` and `/(tabs)/*` paths
5. (Defer to follow-up PR) migrate internal `router.push()` calls to canonical paths

This sequencing means each step is independently mergeable + revertable. The plan implies but doesn't state.

**M2. Anspace borrowing under-cited**
"Borrowing Anspace's split between guest/public routes and protected authenticated routes" — but no file paths cited and no description of the split mechanism. To verify the borrowing is correct, the plan should cite specific Anspace files (likely under `/Users/Cvtot/monorepo/anspace-space-manager/apps/mobile/app/`) and describe what mechanism Anspace uses for the split (route group folders? `_layout.tsx` guards? both?). Without this, "borrowing" is unverifiable.

**M3. Deep links / push notifications not addressed**
Old paths `/(auth)/sign-in` and `/(tabs)/candidates` may be embedded in:
- Push notification payloads from the hireui backend
- Email magic links for password reset
- Web → mobile handoffs (e.g., "open in app" deep links)
- Shared URLs sent by users to other users

The compatibility redirects handle in-app navigation, but deep link parsing on cold-start may not route through the same code path. **Plan should add a check** for `apps/mobile/app/_layout.tsx` or wherever Expo Router handles deep-link parsing, and verify redirects work for cold-start deep links.

**M4. Legacy redirect removal has no trigger condition**
"First pass" with no retirement gate becomes permanent. Suggested addition:

> "Legacy redirects are retired when (a) all internal `router.push()` calls migrate to canonical paths AND (b) backend logs show zero hits on legacy paths for 2 consecutive sprints. Until both conditions met, redirects stay."

Without this, technical debt accumulates silently.

#### LOW (3) — defer but note

**L1. Test coverage gaps:**
- No test for token-expiry mid-session (`getAccessToken()` returns valid token, then API returns 401)
- No test for deep-link-with-token cold start (`/auth/candidate-management/<id>` opened from push notification when token exists)
- No test for `/candidate-drawer` modal interaction with the new `/auth/candidate-management/[id]` route — does the drawer overlay on top of detail, or replace it?

**L2. i18n implication unspoken**
Web has `[locale]` segment; mobile strips it. Users with non-default locale preferences have undefined post-refactor behavior. Acceptable for a router-shell pass, but the assumption should be explicit: "mobile is single-locale for now; locale-aware mobile is a follow-up effort."

**L3. Placeholder density observation**
Of 14 new routes in the constants module, ~7 are placeholders:
- `set-password`, `free-trial`, `authentication-result` (new placeholder routes)
- `auth/jobs`, `auth/company-owner/company-account`, `auth/my-account/plans` (keep existing placeholder behaviour)
- `reset-password` (placeholder pending full form)

This pass establishes the router shell; substantive screen work is queued behind it. Not a blocker, but worth flagging as a forecast: each placeholder is a future PR.

### Pattern fit observations (vault context)

- Plan resembles the **"minimal viable refactor + compatibility shim"** archetype — sound, well-documented in vault corpus.
- Explicit Assumptions section parallels vault Pattern #83 Honest-Deficiency-Disclosure (promotion-eligible at v68 audit, N=3 evidence).
- GitNexus-impact-before-edit matches v2 hireui evaluation Concept 12 (fact-verification protocol).
- Conscious non-borrowing matches Pattern #66 meta-supply-chain-awareness sub-category — selectively rejecting upstream defaults with stated rationale.

### Not verified (could not verify from this folder)

- Actual contents of `/Users/Cvtot/monorepo/hireui/apps/mobile/app/` — cannot confirm current route structure matches what plan describes as "replaced"
- Actual contents of `/Users/Cvtot/monorepo/anspace-space-manager/apps/mobile/app/` — cannot confirm what plan is "borrowing" from
- `apps/mobile/package.json` name field — see H3
- Whether `authAdapter.getAccessToken()` exists at the path implied — plan assumes the adapter is in place
- Whether `NAVIGATION_PATHS` module exists on the web side with the route values listed

These should be verified by the executing agent before implementation, not blockers for saving the plan.

---

## Suggested Next Actions (Storm Bear prime directive)

Ordered by leverage:

### 1. Resolve the 3 HIGH concerns (15 min total)

- **H1:** ask operator whether `/account/reset-password` vs `/account/set-password` are intended-distinct flows or a constants-module redundancy
- **H2:** decide and document the 401-handling contract (suggest: clear token + redirect to sign-in)
- **H3:** `cat /Users/Cvtot/monorepo/hireui/apps/mobile/package.json | grep '"name"'` — verify the test command's filter

### 2. If H1-H3 resolve cleanly, execute the plan in 5 sequenced PRs (per M1)

Each independently mergeable + revertable. Estimated total: 1-2 days of implementation + review.

### 3. Add the M4 retirement trigger to the plan before merge

Single line in the Compatibility Redirects section: "Retire when internal `router.push()` migration complete AND zero legacy-path hits for 2 sprints."

### 4. Schedule a follow-up to address L-series

After router-shell PR lands: token-expiry test, deep-link cold-start verification, i18n single-locale documentation, `/candidate-drawer` interaction test.

---

## Cross-references

- **Sibling refactor docs:** `(C) 2026-05-06 hireui harness evaluation + best practices.md`, `(C) 2026-05-06 v2 changes - integrating KJ OS concepts.md`
- **Sibling project:** `03 Projects/product/anspace-harness/` (same harness pattern)
- **Source skill (constitutional invariants):** `05 Skills/(C) project-code-analysis-harness.md`
- **Routine (current):** routine v2.2 codified 2026-05-14 (supersedes v2.1)
- **Hireui repo:** `/Users/Cvtot/monorepo/hireui`
- **Anspace repo (mobile reference):** `/Users/Cvtot/monorepo/anspace-space-manager`

---

## Metadata

- **Plan source:** Pasted by operator 2026-05-18 (origin unknown — likely drafted in a hireui-side Claude session)
- **Verification by:** Claude, vault session 2026-05-18
- **Verification confidence:** Medium-high — plan-internal review only. Source-of-truth verification (against actual hireui + anspace mobile code) deferred to executing agent.
- **Authoritative state:** This is a verified proposal, not commitment. Operator decides whether to execute.

---

## (C) Resolutions Log — 2026-05-18 (post-verification, same-day)

Append-only log of how HIGH concerns get resolved against actual hireui source code. Each entry includes verification method + source citations so the resolution is auditable.

### H1 RESOLVED — `/account/reset-password` vs `/account/set-password` are distinct flows

**Verification method:** Read hireui web source files directly.

**Sources cited:**
- `/Users/Cvtot/monorepo/hireui/src/core/helper/constants.tsx` (NAVIGATION_PATHS + API_ERROR_CODES)
- `/Users/Cvtot/monorepo/hireui/src/app/[locale]/(account-layout)/account/reset-password/page.tsx`
- `/Users/Cvtot/monorepo/hireui/src/app/[locale]/(account-layout)/account/set-password/page.tsx`

**Findings:**

Both pages render the same `<SetNewPassword>` component but with a different `trigger` prop — a shared-component-with-variant-prop pattern, NOT redundancy.

| Route | Component invocation | User flow |
|-------|---------------------|-----------|
| `/account/reset-password` | `<SetNewPassword trigger="forgotPassword" />` | User clicks "forgot password" → email link → set new password |
| `/account/set-password` | `<SetNewPassword trigger="signUp" />` | User signs up → email verify link → set password first time |

Backend distinction confirmed in same constants file via `API_ERROR_CODES`:
- `FAILED_VERIFY_SET_PASSWORD: "failed_verify_set_password"` (signup flow)
- `FAILED_VERIFY_RESET_PASSWORD: "failed_reset_password"` (forgot-password flow)

Two distinct backend error codes for two distinct flows — confirms distinction at every layer.

**Important quirk discovered (not in original plan):**

`/account/reset-password` does NOT appear in `NAVIGATION_PATHS` on web. The constant has only:
- `FORGOT_PASSWORD: "/account/forgot-password"` (entry-point form where user types email)
- `SET_NEW_PASSWORD: "/account/set-password"` (signup completion target)

The `reset-password` page file exists ONLY to receive email deep links — web app code never navigates to it internally. Backend emits an email containing the URL, user clicks, lands on the page.

**Plan updates required:**

1. **Keep 14 entries** in mobile route constants module — distinction is real.
2. **Mirror the trigger-prop pattern on mobile.** Route Mapping should be amended:
   - `/account/reset-password` renders `SetNewPasswordPlaceholderScreen` with `trigger="forgotPassword"`
   - `/account/set-password` renders `SetNewPasswordPlaceholderScreen` with `trigger="signUp"`
   - Mobile placeholder screen should accept the trigger prop now (cheap) so the future "full reset-password form" PR doesn't need to re-shape the component contract.
3. **NEW open question for operator (H1-followup):** Does mobile need to handle the email deep link to `/account/reset-password`? Two scenarios:
   - **Yes** — backend emits a universal link that resolves to mobile app for mobile users. Keep route in mobile constants AND build a real page (placeholder for now). 14 entries.
   - **No** — backend always routes password-reset emails to the web app, even for mobile users. Then `/account/reset-password` doesn't need to be in mobile constants OR as a mobile page. Drop to 13 entries.

   Web treats this as a page-file-only (deliberately NOT in NAVIGATION_PATHS), which is consistent with either answer — needs product / backend confirmation. Until decided, **plan should ship with 14 entries** (safer default — easier to remove later than add later).

### H2 RESOLVED — token expiry / 401 handling contract

**Resolution method:** Operator decision 2026-05-18 — approved suggested contract verbatim.

**Contract (authoritative):**
- On any API 401 response → call `authAdapter.clearAccessToken()` → redirect to `/account/sign-in`
- Encoded in a single Axios / fetch wrapper response interceptor (NOT per-screen handling)

**Plan updates required:**
1. Add a Test Plan entry for the 401 contract:
   - "On API 401 mid-session from a protected `/auth/*` route: token cleared from storage + user lands on `/account/sign-in`"
2. Implementation note for executing agent: locate the existing Axios / fetch wrapper in `apps/mobile/` (likely under `src/services/` or `src/api/`) and attach the response interceptor there. Don't sprinkle 401 handling across screens.
3. Edge case to test: 401 received while user is on the root `/` redirect screen (token-existed-but-stale-at-cold-start). Interceptor should still clear + redirect cleanly, not loop.

### H3 RESOLVED — package name confirmed `@talentaxis/mobile`

**Verification method:** `grep -n '"name"' /Users/Cvtot/monorepo/hireui/apps/mobile/package.json`

**Result:** Line 2 of `apps/mobile/package.json`: `"name": "@talentaxis/mobile"`

**Verdict:** Test command in plan is correct as drafted. `pnpm --filter @talentaxis/mobile exec tsc --noEmit` will resolve. No plan change required.

### M1 RESOLVED — explicit 5-step implementation sequence

**Resolution method:** Plan-internal design (no external code verification needed).

**Sequence (each step independently mergeable + revertable):**

1. **Route constants module** — create `apps/mobile/src/constants/routes.ts` mirroring web `NAVIGATION_PATHS` (minus locale). Zero behavior change. Establishes typed routes for the Expo `typedRoutes` experiment already enabled in `app.json`.
2. **New canonical route files** — add `apps/mobile/app/account/*` and `apps/mobile/app/auth/*`. Each renders the same screens currently under `(auth)/*` and `(tabs)/*`. NEW + OLD coexist; no guard yet. Root `app/_layout.tsx` gains `<Stack.Screen name="account" />` and `<Stack.Screen name="auth" />` entries.
3. **Token-only layout guards** — add `app/account/_layout.tsx` (kick authenticated users to `/auth/candidate-management`) and `app/auth/_layout.tsx` (kick unauthenticated users to `/account/sign-in`). Use `authAdapter.getAccessToken()` only.
4. **Legacy compatibility redirects** — convert old `(auth)/*` and `(tabs)/*` files to `<Redirect />` components pointing at the new canonical paths. Internal `router.push()` calls keep working through the redirect bridge.
5. **Internal navigation migration** (DEFER to follow-up PR) — replace string literals in `router.push()` calls with constants from step 1. After this, legacy redirects from step 4 become unused (precondition for M4 retirement gate).

**Rationale:** Each step is a small, reviewable PR that can roll back without breaking others. Steps 1-4 fit in a single sprint; step 5 is mechanical sweep work.

### M2 RESOLVED — Anspace borrowing mechanism cited with critical distinction

**Verification method:** Read Anspace mobile layout files directly.

**Sources cited:**
- `/Users/Cvtot/monorepo/anspace-space-manager/apps/mobile/app/_layout.tsx` (root Stack with route groups + top-level auth screens)
- `/Users/Cvtot/monorepo/anspace-space-manager/apps/mobile/app/(tabs)/_layout.tsx` (PUBLIC/GUEST guard: `if (user) <Redirect href="/(client)" />`)
- `/Users/Cvtot/monorepo/anspace-space-manager/apps/mobile/app/(client)/_layout.tsx` (PROTECTED guard: `<ProtectedRoute allowedRoles={[CLIENT, ADMIN, STAFF]} fallbackPath="/(tabs)" />`)

**Anspace mechanism:**

1. Two route groups: `(tabs)` for public/marketing tabs (home, blog, pricing, find-agreement, contact), `(client)` for protected app tabs (dashboard, properties, finance, settings).
2. Each group's `_layout.tsx` enforces its own guard:
   - `(tabs)` guard: if authenticated user exists → redirect to `(client)` (don't show marketing to logged-in users)
   - `(client)` guard: `ProtectedRoute` component with role-based check; on fail → fallback to `(tabs)`
3. Auth screens (`auth/signin`, `auth/signup`, `auth/forgot-password`) live as TOP-LEVEL Stack.Screens in the root layout, OUTSIDE both groups.

**CRITICAL DISTINCTION — what hireui borrows vs does NOT borrow:**

| Element | Borrow? | Reason |
|---------|---------|--------|
| Structural split (separate guest + protected route groups with per-layout guards) | ✅ YES | Sound pattern, matches plan intent |
| Group naming with parentheses `(client)` / `(tabs)` | ❌ NO | Plan uses regular folders `account/` and `auth/` — these become URL segments, unlike Anspace's URL-hidden route groups |
| Auth-check mechanism (`useAuth().user` + `<ProtectedRoute>` role check) | ❌ NO | Plan explicitly rejects this; uses token-only via `authAdapter.getAccessToken()`. Anspace fetches user + roles; hireui Phase-1 does not |
| Three-screen auth split (signin/signup/forgot-password as top-level) | ❌ NO | Hireui puts all account flows under `/account/*` subtree with one shared layout guard |
| Top-level transparent-modal pattern | ✅ YES (already adopted) | `candidate-drawer` in hireui root layout already uses this — same pattern as Anspace's `drawer` |

The plan's "borrowing the split" claim is accurate, but borrowing is **structural only**, not the auth mechanism. This entry makes the boundary explicit so the executing agent does not accidentally drag in Anspace's `useAuth + ProtectedRoute` shape.

### M3 RESOLVED — deep link cold-start verified; no `app.json` change required

**Verification method:** Read `/Users/Cvtot/monorepo/hireui/apps/mobile/app.json`.

**Findings:**

| Config | Value | Implication for refactor |
|--------|-------|---------------------------|
| `scheme` | `"talentaxis"` | Custom-scheme deep links (`talentaxis://account/sign-in`) auto-route to file structure via expo-router |
| `plugins[]` includes `"expo-router"` | yes | File-system routing handles all in-app navigation including custom-scheme deep links automatically |
| `extra.router` | `{}` (empty) | No hardcoded route overrides — clean |
| iOS `associatedDomains` / Android `intentFilters` | NOT configured | No HTTPS universal links / app links yet — all email deep links currently target the WEB app, not mobile |
| `experiments.typedRoutes` | `true` | Type-safety for route constants module (Step 1 of M1) will work out of the box |

**Conclusion:**
- **No `app.json` change required for this refactor.** Renaming route folders is sufficient; Expo Router resolves new paths automatically.
- Custom-scheme cold start (`talentaxis://account/...`) WILL work post-refactor for any client that uses the scheme.
- HTTPS email deep links (password-reset emails, signup verify emails) currently route to the web app, not mobile — this **reinforces the leaning toward "scenario No"** for the H1-followup (mobile likely doesn't receive email deep links until universal links are added later).

**Action item for executing agent (deferred):** when universal links get configured for mobile in a follow-up sprint, the iOS `associatedDomains` + Android `intentFilters` must list the NEW canonical paths (`/account/reset-password`, `/account/set-password`), not the legacy `/(auth)/*`. Add to follow-up backlog.

### M4 RESOLVED — explicit legacy-redirect retirement trigger

**Resolution method:** Operator decision — default conservative gate adopted (operator can override if needed).

**Retirement contract (authoritative for the plan):**

Legacy compatibility redirects (Step 4 of M1 sequence) are retired when ALL of the following hold:

1. **Internal-callsite migration complete** — verifiable via grep:
   ```bash
   grep -rn '/(auth)/\|/(tabs)/' /Users/Cvtot/monorepo/hireui/apps/mobile/app /Users/Cvtot/monorepo/hireui/apps/mobile/src
   # Expected: zero matches
   ```
2. **External-callsite quiet for 2 consecutive sprints** — backend telemetry shows zero hits on legacy paths from deep links / push notifications / shared URLs for at least 2 sprints (≈4 weeks). Requires backend to log path access on legacy paths when the app reports them.
3. **Operator explicit approval** — retirement is its own PR with the above evidence attached, not auto-triggered.

Without BOTH conditions 1 AND 2 met, redirects stay. Default state is "keep redirects" — failsafe biased toward compatibility over cleanup.

---

## (C) Final Status — 2026-05-18 (post-MEDIUM closure)

All HIGH + MEDIUM concerns resolved or explicitly scoped. Plan is ready for execution hand-off.

| Tier | Count | Resolved | Outstanding |
|------|-------|----------|-------------|
| HIGH (H1–H3) | 3 | 3 | 0 |
| MEDIUM (M1–M4) | 4 | 4 | 0 |
| LOW (L1–L3) | 3 | 0 | 3 (acceptable as PR-review items, not pre-kickoff blockers) |
| H1-followup (email deep link to mobile) | 1 | 0 — leaning "scenario No" per M3 evidence | 1 (verify with backend; non-blocking) |

**Hand-off readiness:** The executing agent in `/Users/Cvtot/monorepo/hireui` should be able to start the 5-step PR sequence (per M1) using this document as the authoritative spec. The 3 LOW items + 1 H1-followup question can be addressed during PR review without blocking kickoff.

**Authoritative state pointer:** This is the verified + closed plan. Next change to this file should be a Resolutions Log entry resolving the H1-followup (operator + backend confirmation), or post-execution learnings appended after the implementation PRs land. Do NOT edit prior sections.
