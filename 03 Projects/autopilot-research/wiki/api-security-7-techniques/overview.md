# Overview — the 7 techniques and the video-vs-canonical scorecard

## Source

- **Operator-submitted (adaptation):** LetDiv "Học Lập Trình Đảm Bảo", *"7 Kỹ Thuật Bảo Mật API Bạn Phải Biết…"* — [XuzRt-BFIKU](https://www.youtube.com/watch?v=XuzRt-BFIKU), 2026-07-06, 7:03, ~9.6K views, VN.
- **Original resource (double-dive target):** Hayk Simonyan, *"API Security Explained: Rate Limiting, CORS, SQL Injection, CSRF, XSS & More"* — [FsB_nRGdeLs](https://www.youtube.com/watch?v=FsB_nRGdeLs), 2025-08-12, 8:41, **438K views**, 136K subs.
- Raw: [`raw/2026-07-11-api-security-7-techniques.md`](../../raw/2026-07-11-api-security-7-techniques.md). Canonical layer verified against OWASP / MDN / NIST / RFC / AWS-Cloudflare docs.

## The thesis (both videos)

> "APIs are like doors into your system. If you leave them unprotected, attackers can walk right in." — then 7 "proven techniques" any system should have.

Both videos are **defensive-technique explainers for a public API**, aimed at intermediate developers. They are clear, well-illustrated, and mostly technically *directionally* right. They are also a **teaching taxonomy, not a threat model** — and that gap is where the danger lives.

## The 7 techniques (in the videos' order)

| # | Technique | What the video says | Canonical verdict |
|---|---|---|---|
| 1 | **Rate Limiting** | Cap requests per user/IP; per-endpoint, per-IP, and overall scopes; stops brute-force + DDoS | MISLEADING (≠ DDoS; missing per-username bucket + shared store) |
| 2 | **CORS** | Controls which domains can call your API; without it, malicious sites trick browsers | MISLEADING (CORS is not a request-blocking security control) |
| 3 | **SQL/NoSQL Injection** | Fix = parameterized queries OR ORM safeguards | MISLEADING (ORM not automatic; NoSQL ≠ SQL fix) |
| 4 | **Firewall / WAF** | Gatekeeper matching attack patterns; use AWS WAF / Cloudflare | CORRECT-BUT-INCOMPLETE (evadable, ≠ complete, ≠ network firewall) |
| 5 | **VPN** | Put internal admin/HR/accounting APIs behind a private network | CORRECT-BUT-INCOMPLETE (network location ≠ identity) |
| 6 | **CSRF** | Fix = CSRF token + session cookie | CORRECT-BUT-INCOMPLETE (cookie-only; SameSite omitted) |
| 7 | **XSS** | Fix = escape/sanitize special characters before display | OVERSIMPLIFIED (context-encoding, CSP, HttpOnly omitted) |

## The scorecard (11 claims, refute-first)

- **0** claims fully correct-and-complete
- **5** CORRECT-BUT-INCOMPLETE (rate-limit scaling, WAF, VPN, CSRF, WAF-vendor, stored-XSS mechanics)
- **2** OVERSIMPLIFIED (XSS fix, "these 7 are sufficient")
- **4** MISLEADING (rate-limit=DDoS, CORS-as-control, per-IP+global-only, injection-one-fix)
- **0** REFUTED-as-outright-false — nothing the videos say is *invented*; the failures are all **omission and over-claim**.

Full table in [[caveats-and-corrections]].

## The two things that actually matter

1. **The single most dangerous omission — authorization.** None of the 7 mentions Broken Object Level Authorization (BOLA) or its siblings (BOPLA, BFLA). For a **multi-tenant recruitment SaaS** like hireui, a recruiter at Company A reading `GET /api/candidates/{id}` for Company B's candidate — because the code checks *authentication* but not *ownership* — is the #1 real-world breach class and none of the 7 techniques stop it. See [[what-the-videos-miss-owasp-api-top-10]].

2. **The 7 mix three different layers as if equal.** Network controls (firewall, VPN), browser mechanisms (CORS, CSRF), and app-code defenses (injection, XSS, rate limiting) address different threats at different layers. Presenting them as a flat "checklist any system needs" obscures which control stops which attack — and which ones are **N/A for your architecture** (e.g., CSRF for a Bearer-token API — [[csrf-cookie-vs-token]]).

## How to read this topic

Read [[what-the-videos-miss-owasp-api-top-10]] first (the headline), then [[cors-is-not-a-security-control]] and [[csrf-cookie-vs-token]] (the two sharpest conceptual corrections), then [[hireui-security-posture]] to see how it lands on the real product. The per-technique articles are the reference layer.

## Key Takeaways

- The video is a **faithful, well-made *summary*** of common API-hardening advice — and a **decent onboarding artifact** if paired with the caveats here.
- It is **not a threat model**: it under-weights authorization (the dominant risk) and over-weights commoditized web-app vulns (XSS/CSRF/SQLi) already handled by frameworks/ORMs.
- The correct mental upgrade: **authorization-first, defense-in-depth, architecture-aware** — decide which of the 7 apply to *your* auth model before implementing any of them.
