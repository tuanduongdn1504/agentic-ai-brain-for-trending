# What the videos miss — the OWASP API Security Top 10 (2023)

> **This is the headline finding of the whole topic.** The 7 techniques omit the class of vulnerability that actually dominates API breaches: **authorization.**

## Source

Verified against the OWASP API Security Top 10 2023 (full list + the API1/API3/API4/API5 pages).

## The official Top 10 (2023)

| # | Risk | In the 7 videos? |
|---|---|---|
| **API1** | **Broken Object Level Authorization (BOLA)** | ❌ Absent |
| **API2** | Broken Authentication | ⚠️ Rate-limit only (no token lifecycle) |
| **API3** | **Broken Object Property Level Authorization (BOPLA)** | ❌ Absent |
| **API4** | Unrestricted Resource Consumption | ⚠️ Partial (rate limiting; misses timeouts/quotas/payload caps) |
| **API5** | **Broken Function Level Authorization (BFLA)** | ❌ Absent |
| API6 | Unrestricted Access to Sensitive Business Flows | ❌ Absent |
| API7 | Server-Side Request Forgery (SSRF) | ❌ Absent |
| API8 | Security Misconfiguration | ⚠️ CORS/WAF touch this |
| API9 | Improper Inventory Management | ❌ Absent |
| API10 | Unsafe Consumption of APIs | ❌ Absent |

**Coverage ≈ 30%** — and the missing 70% includes the **top-ranked** risk.

## The category error

The videos mix two different worlds:

- **Traditional web-app vulns** (from the *classic* OWASP Top 10, for browser-rendered apps): **XSS, CSRF, SQL injection.** For pure JSON APIs these are either client-side concerns (XSS), architecture-dependent (CSRF only for cookies), or largely commoditized by ORMs/frameworks (SQLi).
- **Network/perimeter controls:** firewall, VPN.

What's absent is the **API-specific** risk class: **authorization** — API1 (BOLA), API3 (BOPLA), API5 (BFLA) — which together are the #1/#3/#5 ranked risks and the leading cause of real API data breaches. They're not just missing; the videos are **inversely prioritized** — spending airtime on the commoditized vulns while ignoring the dominant one.

## The three authorization gaps (with the recruitment-SaaS angle)

### API1 — Broken Object Level Authorization (BOLA) — the #1 risk
- **Attack:** manipulate an object id to read/modify another tenant's resource. `GET /api/candidates/123` → `…/456` succeeds because the code checked *authentication* (valid token) but not *ownership* (does this recruiter's company own candidate 456?).
- **hireui:** Recruiter at Company A enumerates ids to read Company B's candidates — interview notes, salary expectations, PII across companies. **None of the 7 techniques stop this.** Rate limiting doesn't; CORS doesn't; WAF doesn't; a firewall doesn't.
- **Fix:** every single-object GET/PATCH/DELETE verifies `resource.company_id === req.user.company_id` (and recruiter-scoping for notes). Tenant-scope queries at the data layer.

### API3 — Broken Object Property Level Authorization (BOPLA)
- **Attack:** the object is yours, but sensitive *fields* are exposed or mutable. Over-fetching (`salary_history`, `internal_score`, `background_check_id` in the payload) or mass-assignment (`PATCH {status:"hired"}` you shouldn't set).
- **hireui:** field-level masking on serialization; per-role update allow-lists.

### API5 — Broken Function Level Authorization (BFLA)
- **Attack:** a lower-privileged role calls a privileged *function*. A candidate hits `DELETE /api/jobs/123`; a recruiter hits `/api/admin/export-all-candidates`.
- **hireui:** role-guard every admin/privileged endpoint (`if role !== 'admin' → 403`). This is also where the video's "VPN for internal APIs" advice *actually* belongs ([[network-isolation-and-vpn]]).

## Also missing (secondary)

- **API2 Broken Authentication** beyond rate limiting: JWT expiry (`exp`), refresh-token rotation, revocation/blacklist on logout. (The videos treat rate limiting as the whole auth story.)
- **API4** beyond request-count: execution timeouts, payload/file-size caps, pagination enforcement, third-party spend caps.
- **API7 SSRF**, **API9 inventory/versioning**, **API10 unsafe third-party consumption** — unmentioned.

## Priority inversion, corrected

For a multi-tenant SaaS the real order is: **API1 BOLA ≫ API3 BOPLA ≫ API5 BFLA ≫ API2 auth-layer ≫ API4 quotas** — *then* the videos' hygiene techniques (injection, XSS, CORS correctness) as defense-in-depth, with CSRF/VPN mostly N/A.

## Key Takeaways

- **The videos' biggest failure is omission, not error:** authorization (BOLA/BOPLA/BFLA) — the dominant API-breach class — is entirely absent.
- The 7 conflate *web-app* vulns and *network* controls while skipping *API-specific* authorization.
- For hireui, **BOLA is the #1 architectural concern**, orthogonal to all 7 techniques and enforced at route handlers + tenant-scoped queries.
- Use the **OWASP API Security Top 10 2023** as the real checklist; treat the video's 7 as a partial subset.
