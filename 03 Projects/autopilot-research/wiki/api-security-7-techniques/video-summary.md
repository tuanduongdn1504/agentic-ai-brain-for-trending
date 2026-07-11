# Video summary — annotated walkthrough (both videos)

## Source

Both videos share an identical structure. Timestamps below are (Hayk original / LetDiv adaptation). Full transcripts in [`raw/2026-07-11-api-security-7-techniques.md`](../../raw/2026-07-11-api-security-7-techniques.md).

## Chapter map

| Hayk | LetDiv | Section |
|---|---|---|
| 0:00 | 0:00 | Intro — "APIs are like doors into your system" |
| 0:18 | 0:24 | Rate Limiting |
| 2:39 | 2:33 | CORS |
| 4:05 | 3:06 | SQL & NoSQL Injection |
| 4:45 | 3:52 | Firewalls |
| 5:21 | 4:23 | VPNs |
| 6:24 | 4:49 | CSRF |
| 7:17 | 5:56 | XSS |

## What each section says (and the one-line correction)

- **Intro** — Unprotected APIs let attackers read user data or take over the system. *(Fair framing.)*
- **Rate Limiting** — Cap requests per client per time window. Hayk: per-endpoint (a `/comments` limit), per-user/IP (block IP "D" at the 101st request), and an **overall** limit for DDoS because an attacker can spin up bots each with its own IP. LetDiv adds concrete numbers ("20 requests / 5 min on the video-upload API"). → *Rate limiting handles application-layer abuse, not volumetric DDoS; the correct distributed defense also needs a per-**username** bucket and a shared store.* [[rate-limiting]]
- **CORS** — "Controls which domain can call your API from a browser… without proper CORS, malicious websites could trick users' browsers into making requests." LetDiv localizes the allowed origin to `letdiv.com`. → *CORS does not block the request or stop a non-browser attacker; it governs whether the browser lets the calling page read the response.* [[cors-is-not-a-security-control]]
- **SQL & NoSQL Injection** — User input concatenated into a query; the `--` comment bypasses the password check; worst case = drop all data. Fix = "parameterized queries or ORM safeguards." → *Parameterized queries are #1; ORMs aren't automatic; NoSQL injection is a different attack the SQL fix doesn't cover.* [[injection-sql-and-nosql]]
- **Firewalls** — A WAF is the "gatekeeper" that matches requests against known attack signatures (suspicious SQL keywords, strange HTTP methods); use AWS WAF / Cloudflare rather than building your own. → *Correct as far as it goes; WAF is evadable signature-based L7 defense-in-depth, not complete, and ≠ a network (L3/L4) firewall.* [[firewall-and-waf]]
- **VPNs** — Internal APIs (admin dashboard, HR, accounting) should be reachable only inside the private network. → *True but incomplete: network location is not identity (NIST Zero Trust); you still need authn/authz on internal APIs; cloud SaaS uses VPC + IAM, not a legacy VPN.* [[network-isolation-and-vpn]]
- **CSRF** — A malicious site uses your bank's session cookie to submit a hidden money-transfer; fix = CSRF token checked alongside the session cookie. → *Only applies to cookie/session auth; Bearer-token APIs are immune; SameSite cookies are the modern primary defense the video omits.* [[csrf-cookie-vs-token]]
- **XSS** — A `<script>` in a blog comment is stored and runs in other users' browsers to steal their cookies; fix = escape/disable special characters before display. → *Directionally right but incomplete: context-aware encoding, framework auto-escaping, CSP, and — crucially — **HttpOnly cookies**, which would neutralize the video's own cookie-theft example.* [[xss-httponly-and-csp]]

## What LetDiv changed from Hayk

- **Localization:** CORS example domain → `letdiv.com`; concrete rate-limit numbers added (20 req / 5 min upload).
- **CTA swap:** Hayk's "apply for my mentorship program" → LetDiv's "check out our Full Stack / Backend course."
- **No new technical content**, and **no attribution** to Hayk in the LetDiv description (it links only to LetDiv's own course/blog). See [[source-provenance]].
- **Fidelity:** high. LetDiv did not introduce technical errors beyond those already in the original; the omissions are inherited.

## Key Takeaways

- The two videos are the **same lesson** — verifying one verifies both.
- Every section is a **useful pointer** but a **dangerous stopping point**: each needs the caveat attached in the linked article.
- The value of watching is **vocabulary and intuition**, not a shippable checklist.
