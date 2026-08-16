# (C) gemini-web2api — Pilot Methods Menu

**Wiki v232 · `Sophomoresty/gemini-web2api`**

> **Headline: ⚠️ pilot-AVOID as a tool. The entire payoff is READ-ONLY.**
>
> This is an honest menu, not a padded 24. Most of the value is in **reading** ~350 lines of protocol code and in **banking one security lesson** that is now confirmed twice. There is no version of "adopt this into your workflow" that survives contact with Google's terms.

⭐ **One-thing path: A1 → D9 → D10.**

---

## A — Read & learn (zero install, zero risk)

**⭐ A1 — Read the protocol path (~30 min).**
`gemini_web2api/gemini.py`, ~350 lines. Three things to take away:
1. **`make_sapisidhash()`** — Google's own web-client auth scheme, reconstructed from observation. This is what "the browser can do it, so a script can do it" looks like in practice.
2. **`_extract_texts_from_line()`** — how a `batchexecute` RPC stream (`wrb.fr` markers, nested JSON at `arr[0][2]`, text at `inner[4]`) gets parsed back into text.
3. **The pinned `bl` build ID** (`boq_assistant-bard-web-server_20260716.08_p0`) — the single line that makes the whole thing fragile.

The best short lesson in the corpus on *what your own private `/_/` endpoints look like to someone determined to wrap them.*

**A2 — Read the three API shapes.**
`server.py` translates one backend into OpenAI chat completions, the OpenAI **Responses** API (for Codex CLI) and Google's **native** `/v1beta` shape. A compact, readable reference for what "OpenAI-compatible" actually costs to implement.

**A3 — Read the landscape, not just the repo.**
`HanaokaYuzu/Gemini-API` (~3k★, the mature upstream, **rotates `__Secure-1PSIDTS`** where this does not), `Nativu5/Gemini-FastAPI`, `n0madic/go-gemini-web2api`, `gpt4free`. Useful calibration on how crowded and how commoditised this class is.

---

## B — Borrow the engineering lessons (zero install)

**B4 — "A pinned vendor build ID is an anti-pattern."**
Name it. Any integration that hardcodes an internal identifier of someone else's system (a build hash, an internal route version, an undocumented header) is on a countdown timer. Worth a line in the vault's integration notes.

**B5 — Private endpoints are a public API you didn't document.**
The generalisable lesson for hireui: your internal `/_/`-style routes are only as protected as their *authorisation*, never their obscurity. Anything a logged-in browser can call, a script can call with the same cookies. Pair with the standing **BOLA/authz** thread — this is the same failure family from the attacker's side.

**B6 — Read the risk asymmetry.**
Anonymous mode exposes *no account* (nothing to ban; pressure lands on Google's IP throttling). Cookie mode exposes a **real Google account with no token rotation**. A clean small case study in how the same tool has two completely different threat models depending on configuration.

**B7 — Zero-dependency as a design stance.**
A stdlib-only Python service with one *optional* dependency is an unusually small supply-chain surface. Contrast v231's black-box Chromium download. Worth remembering when choosing what hireui depends on.

---

## C — Hands-on (⚠️ only if you have a specific reason; nothing here is recommended)

**C8 — Read the code from a pinned clone, don't run it.**
`git clone` + checkout a pinned commit + read. No execution. This is the only "hands-on" step I'd endorse.

*Everything below is documented for completeness and carries the full fence in §Fence. I do not recommend running any of it.*

**C9 — Anonymous-mode smoke test on a throwaway VM.** No Google account involved, so nothing of yours is exposed — but it is still unauthorised programmatic use of a consumer product. If run: `api_keys` set to a real value, `host` changed to `127.0.0.1`, CORS narrowed, `log_requests: false`, pinned commit.

**C10 — DO NOT run cookie mode.** It puts a live, non-rotating Google session in a file behind an open-by-default listener.

**C11 — DO NOT deploy the Cloudflare Worker.** It stores your Google session credentials as third-party edge environment variables and exists specifically to spread traffic across ~300 locations to defeat rate limiting. That is the most committed version of this and the least defensible.

---

## D — hireui / Goal #2 (the real payoff)

**⭐ D9 — Bank the broken-auth triad as a *confirmed recurring* check.**
This is the sharpest transferable finding of the ship. Two independent projects in this class — v231 CoreOfPotato and v232 gemini-web2api — each ship a local service holding live AI-account credentials with:

- **auth that fails open** when unconfigured (`if not keys: return True`),
- **wildcard CORS** (`Access-Control-Allow-Origin: *`),
- and here, **binding `0.0.0.0`** rather than loopback,
- plus a **hardcoded default credential** in the shipped example (`sk-gemini`; v231's was `admin-token-change-me`).

One instance is an anecdote. **Two independent instances is a pattern.** Write it into hireui's API-security work as a standing check:

> *A local or internal service holding authenticated credentials MUST require auth by default; MUST NOT wildcard CORS; MUST NOT treat "no key configured" as "allow"; MUST NOT bind `0.0.0.0` by default; MUST NOT ship a working default credential.*

Then red-team hireui's own local/dev/admin surfaces against exactly that list. Composes directly with the standing **BOLA / api-security** thread (the #1 hireui risk).

**⭐ D10 — Reinforce the "official paid keys only" ADR, now with a 4th instance.**
hireui's rule — *"official, paid API keys per vendor ToS; never web-UI scraping, never subscription re-exposure, never free-tier harvesting"* — now has **four** confirming anti-pattern instances: v207 (CLI OAuth subscriptions), v208 (a port of v207), v231 (browser-automated web UIs), **v232 (protocol-RE'd web UI)**. v232 is the first that works **with no account at all**, which is worth recording: the temptation here is cheaper and lower-friction than any prior instance, and therefore more likely to be reached for.

**D11 — "Never route candidate data through a harvested consumer AI session."**
Into the candidate-LLM legibility ADR. A harvested consumer session has no data-processing agreement, no retention terms you can point at, and — in this tool — **request logging on by default**. For candidate PII that is disqualifying on its face.

**D12 — Add "log_requests"-class defaults to the hireui config review.**
A service that writes prompt content to local logs *by default* is a small, common, easily-missed leak. Check hireui's own logging defaults against the same question: what user content ends up on disk without anyone choosing it?

---

## E — Vault-meta

**F13 — File the §C mint + both reviewable alternatives for the overdue audit.**
The new N=2 standalone, the NO-MINT alternative, and — most importantly — **alternative (B): generalising the v207 row to "re-exposes a non-API consumer entitlement."** That one is deliberately **not self-executed** because it would silently fire v207's promotion-to-CONFIRMED trigger. The audit owns that decision.

**F14 — Record the "AI-Generated-Repo Artifact Contamination" negative control.**
v231 instantiated that candidate axis textbook-style (the "CoreNexus" CHANGELOG). v232's apparent tagline discrepancy looked identical and **came back clean**. A negative control is worth as much as the positive one for a candidate axis the audit may resurrect.

**F15 — Watch the Claude-targeting variant.**
`cyberanrhy/gemini-claude-web2api` applies this technique to **claude.ai**. That is the axis worth tracking — not the Gemini vertical.

---

## ⚠️ Fence (if anything here is ever run)

- **Anonymous mode only.** Never supply real Google account cookies.
- **Throwaway VM**, never the daily machine.
- **Before the first request:** set a real `api_keys` value · change `host` to `127.0.0.1` · narrow CORS · set `log_requests: false`.
- **Never** deploy the Cloudflare Worker with real credentials.
- **Never** install the cookie-sync browser extension into a browser holding real Google sessions.
- **Never** point it at hireui, candidate data, or anything under the hireui CONSTITUTION (I-2 `agent-*` branches / I-8 operator-installs / GitNexus-first).
- **Pin the commit** — there are no releases.
- hireui stays on **official, paid API keys**.

---

## Bottom line

**Read `gemini.py`. Bank the security check. Reinforce the ADR. Do not run it.**

The corpus value here is not a tool — it is (i) a second, mechanically independent instance that makes the web-UI-harvesting species real, (ii) a second specimen of a broken-authentication triad that is now worth red-teaming your own work against, and (iii) confirmation that this technique has already been pointed at Claude.
