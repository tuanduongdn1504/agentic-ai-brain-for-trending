# Security & Privacy

> Two omissions the videos share: an **unhardened public dashboard**, and the fact that "local-first" stops at OmniRoute — your prompts still go **upstream** to free providers that log/train on them.

## Source
OmniRoute `ENVIRONMENT.md` / `.env.example` / `REMOTE-MODE.md` (code-inspected by verifier); t1 + t4 walkthroughs; t7 (OpenRouter data warning); Workflow verdicts `selfhost-vps-security` + `privacy-data-residency` (both CORRECT-BUT-INCOMPLETE, high).

## 1. VPS security defaults are unsecured (and walkthroughs skip hardening)
The DEVKIT AI (t1) and Real World Devs (t4) VPS setups stand up a working dashboard but **omit every hardening step**. OmniRoute's shipped defaults:
- **Default password `CHANGEME`** — often never changed on camera.
- **Plaintext HTTP** on `0.0.0.0:20128` — **no TLS**; the docs themselves say "prefer HTTPS or a Tailnet."
- **`REQUIRE_API_KEY=false`** by default — API auth off.
- **`AUTH_COOKIE_SECURE=false`** — session cookies lack the secure flag.

**Net effect:** login credentials, session tokens, and *all your provider API keys* transit and are reachable in cleartext over the public internet. Anyone who finds the port gets the dashboard.

**Minimum hardening (do all of these):**
- set a strong random `INITIAL_PASSWORD`; set `REQUIRE_API_KEY=true`; set `AUTH_COOKIE_SECURE=true`;
- put it behind **HTTPS/TLS** (reverse proxy with a cert), **or**
- keep it **private-only** — bind to `127.0.0.1`, or reach it via **Tailscale / SSH tunnel** rather than a public port.

## 2. "Local-first" ≠ private end-to-end
OmniRoute genuinely keeps **its own** state local (encrypted SQLite keys/usage/history, no telemetry, no account). t3 is right about *that* layer. But your prompt doesn't stop at OmniRoute — it goes **out to the free upstream provider**, and free tiers are where the data risk lives:
- **Gemini free tier** explicitly uses conversations to improve Google's services.
- **DeepSeek** is China-based (data-residency + jurisdiction concerns).
- **OpenRouter free models** — t7 quotes the on-screen warning verbatim: *"all prompts and outputs are logged to improve the provider's model. So don't upload anything personal and confidential."*
- Most free tiers log inputs/outputs per their ToS; several are **KYC-gated**.

So "complete privacy" is true only of the local hop. **Whatever source code or data you route through a free tier may be logged and trained on.**

## 3. Credential concentration
OmniRoute becomes a **single store of many providers' keys** (and, if you go there, OAuth tokens). That's a high-value target: an exposed dashboard or a compromised box leaks *all* of them at once. Encryption-at-rest helps; an open port + default password defeats it.

## hireui / operator implications
- **Never** route candidate data, résumés, or hireui source through OmniRoute's free tiers — it collides directly with the [[external|Storm Bear: hireui candidate-LLM legibility ADR]] (residency, auditability, EU AI Act Annex III) and the free-tier training/logging above.
- If ever used for **non-sensitive, operator-side** experimentation, it must be **private-network-only + hardened**, paid keys only, no Path C. See [[hireui-relevance]].

## Key Takeaways
- Default deploy = **HTTP, `CHANGEME`, no API auth, insecure cookies** on a public port; videos skip hardening. Lock it down or keep it private-only.
- **Local-first ≠ private:** free upstream providers (Gemini/DeepSeek/OpenRouter) **log and train on** your prompts — don't send anything confidential.
- OmniRoute concentrates many keys/tokens in one place — protect the box accordingly.
- Related: [[how-it-works-setup-and-clients]] · [[hireui-relevance]] · [[claims-scorecard]]
