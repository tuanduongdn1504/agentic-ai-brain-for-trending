# CSRF — the cookie-vs-token applicability flip

## Source

Video technique #6. Verified against the OWASP CSRF Prevention Cheat Sheet, OWASP SameSite page, MDN CSRF, and PortSwigger's CSRF material.

## What the video says (accurate parts)

- CSRF tricks a logged-in user's browser into making an unwanted request. Example: you're logged into your bank (session cookie); a malicious site submits a hidden money-transfer; the bank sees a valid cookie and executes it.
- Fix: a **CSRF token** checked alongside the session cookie — the request is allowed only if both the cookie *and* a matching token are present.

**Verdict: CORRECT-BUT-INCOMPLETE** — the fix is right *for cookie auth*, but the video never states the precondition, and omits the modern primary defense.

## The load-bearing precondition the video never says

**CSRF only exists when the browser AUTO-ATTACHES credentials.** That means **cookie/session auth**. The whole attack depends on the browser silently sending the session cookie on a cross-site request.

- **APIs authenticated with a Bearer token in the `Authorization` header (JWT/OAuth) are immune to classic CSRF** — the browser does **not** auto-attach the `Authorization` header cross-site; the app's JS must add it explicitly, which `evil.com` cannot do for your token.
- Consequence: a developer on a **Bearer-token API who implements CSRF tokens is doing unnecessary work**; a developer on a **cookie API who implements only a CSRF token but forgets SameSite** is missing the now-primary defense.

## The modern defense stack the video omits

1. **SameSite cookies (primary now).** `SameSite=Lax` is the default in modern Chrome/Edge/Opera; it blocks cookies on cross-site POST/PUT/DELETE. `Strict` blocks all cross-site sends. This is the **first line** for cookie auth.
2. **Anti-CSRF (synchronizer) tokens** — still valuable, complementary.
3. **Double-submit cookie** pattern.
4. **Origin / Referer validation** and **Fetch Metadata** headers.
5. Never perform state changes on `GET`.

## Correct model

```
Is the API authenticated via cookies the browser auto-sends?
 ├── No (Bearer/JWT in Authorization header) → CSRF is N/A. Skip CSRF tokens. Guard XSS instead.
 └── Yes (session cookie) → SameSite=Lax|Strict (primary) + anti-CSRF token (defense-in-depth)
                           + Origin/Referer check + no state-changing GETs.
```

## hireui relevance — a clean applicability call

- **Recon finding:** hireui authenticates the API with **JWT Bearer tokens in the `Authorization` header** (stored in `localStorage`; `httpServices.tsx:67`). → **CSRF is N/A for the main API. Skip CSRF tokens.** This is a real time-saver and a crisp illustration of *decide-before-implement*.
- **The one seam:** the token **refresh** endpoint uses `withCredentials: true` → `/api/v2/auth/refresh` (a cookie). That single cookie-based flow *is* potentially CSRF-relevant → **check the refresh cookie is `SameSite=Lax/Strict` + `HttpOnly` + `Secure`.**
- **Trade-off the video would miss:** putting the auth token in `localStorage` (not a cookie) *removes* CSRF but *amplifies* XSS — see [[xss-httponly-and-csp]]. You can't use `HttpOnly` to protect a token you deliberately expose to JS.
- **Document the decision** in an ADR: "Bearer-token API ⇒ no CSRF tokens; revisit if we adopt cookie sessions." (Pilot method B3.)

## Key Takeaways

- **CSRF is a cookie-auth problem.** Bearer/JWT APIs are immune by design.
- **SameSite is the modern primary defense** the video skips; tokens are complementary.
- For hireui: **skip CSRF tokens** (Bearer auth) — but lock down the one cookie seam (refresh) with SameSite/HttpOnly/Secure.
- Choosing localStorage tokens trades CSRF risk for XSS risk — mind the other side.
