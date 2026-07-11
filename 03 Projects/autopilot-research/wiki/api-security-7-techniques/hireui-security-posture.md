# hireui security posture — read-only recon (2026-07-11)

> Grounds the pilot menu in the real product instead of generic advice. From a **read-only** Explore pass over `/Users/Cvtot/monorepo/hireui` (Next.js App Router monorepo). This repo is the **frontend**; the API backend (`/api/v2/*`, `coreApiService`) is a **separate service** not in this tree — so many server-side controls are backend-team work.

## Posture map

| # | Area | Verdict | Evidence / note |
|---|---|---|---|
| 1 | **Auth model** | **Bearer/JWT in `Authorization` header** | Token in `localStorage`, `config.headers["Authorization"]="Bearer …"` (`httpServices.tsx:67`). Refresh via `withCredentials:true` → `/api/v2/auth/refresh` (backend httpOnly cookie). |
| 2 | ORM / DB | **N/A here** | Frontend-only; DB access is on the separate backend. Injection risk lives backend-side. |
| 3 | **Rate limiting** | **ABSENT** | No limiter in repo; the two API routes (`/api/verify-turnstile`, `/api/generate-vietqr`) are unguarded. Login lives on backend. |
| 4 | CORS | **Frontend headers commented out** | `next.config.mjs` `headers()` commented (`:114–126`); axios `withCredentials:true` ⇒ **backend** CORS+credentials config is what matters. |
| 5 | **BOLA / object authz** | **HIGH RISK — backend-dependent** | Fetch-by-bare-id everywhere, no client ownership check (`AccountLocation.service.tsx:23`, `Applicant.service.tsx:118`). All authz must be backend-enforced. |
| 6 | XSS surface | **LOW now** | No `dangerouslySetInnerHTML`, no user-HTML render, no sanitizer; `react-quill` present but **unused**. React auto-escapes. |
| 7 | **Security headers / CSP** | **ABSENT** | No CSP/HSTS/X-Frame-Options/nosniff; `headers()` commented out; no `helmet`. |
| 8 | WAF / edge / deploy | **Ambiguous** | `vercel.json` present (recon: active) **and** `appspec.yml` (AWS CodeDeploy) + Dockerfile/compose. **Confirm real prod edge.** |
| 9 | Input validation | **ABSENT / PARTIAL** | No zod/yup/class-validator. One unsafe interpolation: `searchLocation(name)` → `?name=${name}` (`AccountLocation.service.tsx:57`); siblings correctly use axios `params`. |
| 10 | Existing posture | **PARTIAL** | Sentry configured; no `SECURITY.md`; auth check is component-level (`AuthContext`), not route-guarded. |

## How the 7 techniques land on hireui (given Bearer/JWT)

| Technique | hireui priority | Why |
|---|---|---|
| Rate Limiting | **A (backend)** | Login brute-force + scraping; currently absent. |
| Injection | **A (backend)** | Parameterize on backend; fix one frontend URL-interpolation. |
| **Authorization (BOLA/BOPLA/BFLA)** | **A+ (backend)** | *Not in the videos*; #1 real risk for multi-tenant. |
| CORS | **B (backend)** | Allowlist correctness; not authz. |
| Internal-API isolation | **B (backend)** | Role-guard admin routes (public SaaS ⇒ no VPN). |
| Security headers / CSP | **B (frontend, cheap)** | Uncomment `headers()`; defense-in-depth for the localStorage-token XSS risk. |
| XSS | **C→ raised** | Low surface now, but localStorage token ⇒ any XSS = token theft. |
| CSRF | **Skip** | Bearer auth ⇒ N/A. Only the refresh cookie needs SameSite/HttpOnly/Secure. |
| VPN | **Skip** | Public SaaS. |
| WAF | **C (decision)** | Scaling/attack-driven; confirm edge first. |

## The two hireui-specific twists the videos can't see

1. **CSRF flips to "skip"** — Bearer tokens aren't auto-attached cross-site, so classic CSRF is N/A. The *one* seam is the `withCredentials:true` refresh endpoint → verify its cookie is `SameSite`+`HttpOnly`+`Secure`. ([[csrf-cookie-vs-token]])
2. **XSS flips to "raised"** — the auth token sits in `localStorage` (JS-readable by design), so any XSS = full account takeover, and `HttpOnly` **cannot** protect a deliberately-exposed token. Ship a **CSP** and consider in-memory token storage. ([[xss-httponly-and-csp]])

## Top 3 risks for this codebase

1. **BOLA (CRITICAL)** — fetch-by-id with no client-side ownership check; entirely backend-dependent. Audit every backend read/write for `resource.company_id === user.company_id`. → [[what-the-videos-miss-owasp-api-top-10]]
2. **Missing CSP + security headers (frontend, cheap)** — uncomment/configure `next.config.mjs` `headers()`. Especially valuable given the localStorage token.
3. **No input-validation layer + one unsafe URL interpolation** — add zod on API inputs; fix `searchLocation` to use axios `params`.

## Constraints (respect hireui's own rules)

This is a **proposal document in the vault**, not a change to hireui. Any actual work in hireui must follow **its** CONSTITUTION (I-2 agent-* branches, I-8 operator-only skills, GitNexus-first) + BMAD harness — see the operator's hireui memory. Cross-links: [[miai-cv-matching-agent]] (recruitment-domain audit), [[mosh-ai-powered-apps]] (the first-LLM-feature endpoint this secures).

## Key Takeaways

- hireui uses **Bearer/JWT (localStorage)** → **CSRF N/A, XSS amplified.**
- The repo is **frontend-only**; rate-limiting / injection / BOLA / CORS enforcement are **backend-team** work.
- Cheapest immediate frontend wins: **CSP headers** + the **`searchLocation` interpolation fix**.
- The dominant risk (**BOLA**) is invisible to all 7 video techniques and needs a backend authorization audit.
