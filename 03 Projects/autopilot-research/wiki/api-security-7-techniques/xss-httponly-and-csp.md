# XSS — context-aware encoding, CSP, and the HttpOnly the video forgot

## Source

Video technique #7. Verified against the OWASP XSS Prevention, Content Security Policy, and DOM-based XSS Prevention cheat sheets + OWASP HttpOnly.

## What the video says (accurate parts)

- Stored XSS: an attacker puts `<script>` in a blog comment; it's saved and runs in every viewer's browser to steal their cookie. *(Textbook stored-XSS, correctly told.)*
- Fix: disable/escape special characters before displaying user content. *(Directionally correct — output encoding is the primary defense.)*

## Canonical corrections

**Verdict: OVERSIMPLIFIED.** "Escape special characters" is the seed of the right answer but skips most of the defense — including the layer that neutralizes the video's *own* example.

1. **HttpOnly cookies (major omission — self-defeating).** The video's whole payoff is "the injected JS steals the cookie." But a session cookie set **`HttpOnly`** is **unreadable by JavaScript** — `document.cookie` returns an empty string. HttpOnly directly neutralizes the demonstrated attack, yet the video never mentions it. (Also set `Secure` + `SameSite`.)
2. **Encoding must be context-aware.** "Escape special characters" isn't one operation: HTML body uses entity encoding (`&lt;`), HTML attributes differ, JavaScript context uses `\uXXXX`, URLs use percent-encoding, CSS uses hex. Using the wrong encoding for the context can *introduce* a hole. OWASP: encode **for the context where the data is output**.
3. **Framework auto-escaping is the real first layer.** React/Angular/Vue escape interpolated values by default; XSS in these apps usually means someone used an escape hatch (`dangerouslySetInnerHTML`, `v-html`, `[innerHTML]`). Manual escaping matters mainly at those hatches.
4. **Sanitize rich HTML — don't escape it.** For WYSIWYG/markdown content (CVs, job descriptions), escaping would break legitimate formatting; use a sanitizer (**DOMPurify**) that strips dangerous elements while keeping safe HTML.
5. **CSP is defense-in-depth.** A strict `Content-Security-Policy` (nonces/hashes, no inline scripts, restricted sources) limits damage even if encoding fails.
6. **Three XSS types.** Stored (shown), reflected (URL-driven), DOM-based (client-side sinks — fix with `textContent`, not `innerHTML`). The video shows only stored.
7. **Encode on OUTPUT, validate on INPUT** — they're different jobs.

## Correct model

Layered: **framework auto-escaping** → **context-aware output encoding** → **sanitize rich HTML (DOMPurify)** → **CSP** → **HttpOnly/Secure/SameSite cookies** (limit the blast radius of any XSS that slips through).

## hireui relevance — where the video's model breaks in a useful way

- **Recon finding:** the frontend has **no `dangerouslySetInnerHTML`**, no user-HTML rendering, and a `react-quill` dependency that's **imported nowhere** — current XSS surface is **low** (React auto-escapes).
- **But the amplifier the video can't see:** hireui stores the **auth JWT in `localStorage`**, which is **JS-readable by design**. So *any* future XSS = **full account/token theft**, and `HttpOnly` cannot protect a token you deliberately exposed to JS. This **raises**, not lowers, XSS priority for hireui — the opposite of the "API-only ⇒ XSS is low" reflex.
- **Actions:** (1) turn on a **CSP** (the Next.js `headers()` block is currently commented out — cheap, shippable now); (2) if any rich-text rendering of candidate content is ever added, mandate **DOMPurify**; (3) remove the unused `react-quill` dep or pin/justify it; (4) consider moving the access token to an in-memory store rather than `localStorage`.

## Key Takeaways

- **HttpOnly cookies neutralize the video's own cookie-theft demo** — and it's never mentioned.
- Output encoding must be **context-aware**; frameworks auto-escape; rich HTML needs **sanitization**, not escaping; **CSP** is the safety net.
- For hireui the twist is inverted: a **localStorage token makes XSS a token-theft risk**, so XSS deserves *more* attention, not less — and HttpOnly can't help there.
