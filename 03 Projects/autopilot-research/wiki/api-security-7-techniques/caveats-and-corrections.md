# Caveats & corrections — the Rule 12 ledger

> The videos say nothing *invented* — but every checked claim needed a caveat. **0 fully-correct · 5 correct-but-incomplete · 2 oversimplified · 4 misleading · 0 refuted-as-false** (11 claims, refute-first). This is a fail-loud ledger, not a takedown: the videos are a useful taxonomy that stops one caveat too early on each point.

## Claim-by-claim verdict table

| # | Claim (paraphrased) | Verdict | The caveat |
|---|---|---|---|
| 1 | Rate limiting protects you from being taken down by thousands of req/min (DDoS) | **MISLEADING** | App-layer only; volumetric DDoS needs upstream CDN/Shield. OWASP: "cannot be one-step solutions." |
| 2 | Per-IP + a global limit is the fix for distributed attacks | **CORRECT-BUT-INCOMPLETE** | Needs a **per-username** bucket too; per-IP is "defeated by residential proxies"; needs a **shared store**. |
| 3 | CORS controls who can call your API / stops malicious sites | **MISLEADING** | CORS gates *reading responses* in a browser, not *sending requests*; non-browser clients ignore it; that scenario is CSRF. |
| 4 | Injection is fixed by parameterized queries **or** ORM | **MISLEADING** | Parameterized is #1; ORM only if you never escape it; **NoSQL injection is a different attack** the SQL fix doesn't cover. |
| 5 | A WAF gatekeeper blocks attack patterns; use AWS/Cloudflare | **CORRECT-BUT-INCOMPLETE** | Evadable signatures; ≠ complete; ≠ network firewall; can't see logic/authz flaws. |
| 6 | Put internal APIs behind a VPN | **CORRECT-BUT-INCOMPLETE** | Network location ≠ identity (NIST Zero Trust); still need authn/authz; cloud = VPC+IAM. |
| 7 | CSRF = CSRF token + session cookie | **CORRECT-BUT-INCOMPLETE** | Only for **cookie** auth; Bearer/JWT immune; **SameSite** is the omitted modern primary defense. |
| 8 | XSS = escape special characters before display | **OVERSIMPLIFIED** | Needs context-aware encoding + framework auto-escape + sanitization + CSP + **HttpOnly**. |
| 9 | Stored XSS in a comment steals viewers' cookies | **CORRECT-BUT-INCOMPLETE** | True mechanism, but **HttpOnly** cookies neutralize the theft — unmentioned. |
| 10 | AWS/Cloudflare are the way to add a firewall (vs building one) | **CORRECT-BUT-INCOMPLETE** | Managed > custom is right, but WAF ≠ full firewall/defense-in-depth. |
| 11 | These 7 are a sufficient/standard API-security set | **OVERSIMPLIFIED** | Omits the OWASP API Top-10 authorization trio (BOLA/BOPLA/BFLA) — the dominant real risk. |

## The single most important correction

**Authorization (BOLA/BOPLA/BFLA) is absent from all 7 techniques** and is the #1 real-world API-breach class — and hireui's top risk as multi-tenant SaaS. Full treatment: [[what-the-videos-miss-owasp-api-top-10]].

## Two conceptual corrections worth internalizing

- **CORS is not a security control** — it's a relaxation of the same-origin policy governing *response reading*. [[cors-is-not-a-security-control]]
- **CSRF is a cookie-auth problem** — Bearer/JWT APIs (like hireui) are immune; decide before you implement. [[csrf-cookie-vs-token]]

## What the videos genuinely get right (credit where due)

- The **taxonomy and vocabulary** are sound; the illustrative examples (`--` bypass, bank CSRF, comment XSS, botnet rate-limit evasion) are textbook-correct.
- **"Use managed WAF, don't build your own"** is clean advice.
- The videos **correctly acknowledge per-IP limiting's botnet weakness** — they just prescribe an incomplete remedy.
- Fidelity of the LetDiv adaptation to Hayk's original is **high** — no new errors introduced in translation.

## Sourcing / verification notes (Rule 12 honesty)

- **No verifier misfires requiring override** on this topic (contrast several prior topics). The refute-first pass produced consistent, well-sourced verdicts across 11 claims.
- **ByteByteGo hypothesis discarded via evidence, not assumed** — I initially suspected a ByteByteGo origin; the provenance dive showed Hayk cites no one and ByteByteGo's own framework differs. Recorded so the guess isn't mistaken for fact later. [[source-provenance]]
- **hireui posture** is from a **read-only** recon of the frontend repo; backend-side claims (rate limiting, ORM, BOLA enforcement) are marked backend-dependent, **not verified**, because that code isn't in this tree. [[hireui-security-posture]]
- **Not verified:** exact hireui production edge (Vercel vs AWS — both configs present); whether the backend reflects CORS origins with credentials; backend JWT `exp`/rotation.

## Key Takeaways

- The failure mode is **omission and over-claim**, not fabrication — a decent starter set that stops one caveat short each time.
- **Authorization is the missing headline**; CORS-as-control and CSRF-for-all-auth are the two sharpest conceptual errors.
- Treat the videos as **onboarding vocabulary**, then upgrade to the **OWASP API Top 10 2023** as the real checklist.
