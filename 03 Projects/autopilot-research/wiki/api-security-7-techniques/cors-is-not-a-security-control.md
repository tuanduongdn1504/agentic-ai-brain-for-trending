# CORS is not a security control — the load-bearing correction

## Source

Video technique #2. Verified against MDN "Cross-Origin Resource Sharing", the W3C CORS spec, and the OWASP CSRF / HTML5-Security cheat sheets.

## What the video says

> "CORS controls which domains can call your API from a browser. Without proper CORS, malicious websites could trick users' browsers into making requests on their behalf." (LetDiv: only `letdiv.com` may call the API; everything else is blocked.)

**Verdict: MISLEADING.** This is the single most common CORS misconception, and it's baked into the framing.

## What CORS actually is

- CORS is a **relaxation** of the browser's **Same-Origin Policy (SOP)**, not an access control you add on top of it. By default SOP already stops a page on `evil.com` from *reading* a response from `your-api.com`. CORS is how a server *opts in* to letting specific other origins read its responses.
- **CORS does NOT block the request from being sent or processed.** The cross-origin request still travels to your server and your server still executes it (runs the query, writes the row). The browser then inspects the response's `Access-Control-Allow-Origin` header and — if the calling origin isn't allowed — **hides the response body from the calling page's JavaScript**. The side effect already happened.
- **CORS is browser-only.** `curl`, Postman, mobile apps, and any server-to-server caller **ignore CORS entirely**. It offers zero protection against a non-browser attacker.
- So CORS is a **response-visibility** mechanism for legitimate browser UX — **not** authentication, **not** authorization, **not** a request firewall.

## The conflation the video makes

"Malicious sites tricking a logged-in user's browser into making requests" is **CSRF**, and the defense is **CSRF tokens + SameSite cookies** ([[csrf-cookie-vs-token]]) — *not* CORS. The video attributes CSRF's threat to CORS's mechanism. They are orthogonal.

## CORS can itself be a vulnerability

A **permissive/misconfigured** CORS policy is an OWASP-recognized weakness (a symptom of API8 Security Misconfiguration):
- `Access-Control-Allow-Origin: *` **with** `Access-Control-Allow-Credentials: true` is disallowed by the spec (browsers reject it) — but the dangerous real-world pattern is **reflecting the request's `Origin` back** with `Allow-Credentials: true`, which effectively allows *any* origin to read authenticated responses → cross-origin credential/data leakage.

## Correct model

- **CORS = a browser convenience** that decides who may *read* your responses in a browser.
- **The real security boundary is server-side authn + authz on every route.** If a request is authenticated and authorized, it should succeed regardless of CORS; if it isn't, it should fail regardless of CORS.
- Set CORS to an **explicit allowlist** of your known frontends. Never `*` on authenticated endpoints; never reflect arbitrary origins with credentials.

## hireui relevance

- **Recon finding:** the frontend's Next.js `headers()` is commented out; the axios client sends `withCredentials: true`, so the **backend's** CORS + credentials configuration is what matters. If the backend reflects `Origin` with `Allow-Credentials: true`, that's a real leak vector for candidate data.
- **Action:** verify backend CORS is an explicit allowlist (`https://hireui.app`, staging) — and independently, treat the **token-validation + BOLA checks** as the actual boundary. Document in code that CORS is *not* authorization so no one relaxes it thinking the browser will save them.

## Key Takeaways

- **CORS loosens SOP; it does not tighten security.** It controls *reading responses*, not *sending requests*.
- **Non-browser clients bypass CORS** — it's not a defense against attackers.
- The "malicious site tricks the browser" scenario is **CSRF**, defended by SameSite + tokens, not CORS.
- A permissive CORS config is itself a vulnerability. Allowlist your origins; keep auth server-side.
