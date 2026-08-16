# (C) gemini-web2api — Deep Dive

**Wiki v232 · 2026-08-17 · subject `Sophomoresty/gemini-web2api`**
*Operator-requested (link arrived via Facebook; `fbclid` stripped).*

---

## 1. What it is, in one breath

`gemini-web2api` takes the **private RPC endpoint that the Gemini website itself calls** and re-exposes it on your machine as an **OpenAI-compatible API**. Point any OpenAI client — including a coding agent — at `http://localhost:8081/v1`, and it answers using Google's consumer Gemini web product rather than a paid Gemini API key.

- **Repo "About" (verbatim):** *"Convert Google Gemini web into OpenAI-compatible API. Zero auth, cross-platform, single file."*
- **README Features subtitle (verbatim):** *"Zero cost, cross-platform, single file."*

Both strings are real, in different places, and both are accurate to different facets — see §7.

**No API key to Google exists anywhere in this tool.** That is the whole point.

---

## 2. Provenance

| Field | Value |
|---|---|
| Repo | `Sophomoresty/gemini-web2api` |
| Author | **Sophomoresty** (靝悠Sol) — a disclosed individual, **NOT Anthropic** |
| License | MIT |
| Version | `1.1.0` (in `pyproject.toml`) — ⚠️ **no releases published** |
| Language | Python primary (breakdown NOT VISIBLE on the page) |
| Metrics | ~2.7k★ / ~607–627 forks / 6 contributors / 59 commits — **page-stated (§37.4)** |
| Trendshift | #42981 — "#12 Python Repo of the Day" (2026-05-31), "#7 JavaScript Repo of the Day" (2026-08-01) |
| Python | `>=3.8` |
| Deps | **none required**; optional `streaming` group = `httpx>=0.25` |

**Author identity — corrected by hand.** A first search characterised the author as a *"reverse engineer and penetration tester… offensive security tool developer."* The **verbatim GitHub bio does not say that**:

> *"SCU undergrad, based in Shanghai FDU. Started in Mechanical Engineering 🔧, detoured into graphic design & video editing 🎨, had an existential crisis 💀, pivoted to CS, and somehow ended up doing AI-powered reverse engineering 🤷. Jack of all trades, master of none."*

A profile summariser then read "SCU" as *Santa Clara University*. In context — Shanghai, **FDU = Fudan University**, Chinese-language repos and README, linux.do community credits — **SCU = Sichuan University (四川大学)**. Both the "penetration tester" framing and the "Santa Clara" reading are **discarded as confabulations**; only the verbatim bio is relied on.

**Author portfolio (a coherent archetype).** 59 public repos / 157 followers. The notable ones form a single theme — *circumventing an access gate to reach content or capability that is otherwise paid or restricted*:

| Repo | ★ | What it does |
|---|---|---|
| `gemini-web2api` | 2.7k | free Gemini web → OpenAI API (**this subject**) |
| `mediago` | 233 | downloads video from 90+ Chinese educational platforms |
| `bpc-fetch` | 196 | paywall bypass, 936 sites |
| `gemini-search-mcp` | 172 | *"Free MCP server for web search via Google AI Mode"* |
| `qmdec` | 75 | QQ Music file decryptor with auto-tagging |
| `typora-theme-Jinxiu` | 58 | Typora theme for academic writing |

⚠️ `gemini-search-mcp` is **the same move applied to search, delivered as an MCP server**. That is a landscape adjacency worth noting — but `gemini-web2api` itself **ships no MCP server**.

---

## 3. The mechanism (source-verified)

This is the part worth reading, and it is the sharpest single distinction from the corpus's prior instance of this class.

**It is pure HTTP protocol reverse-engineering. There is no browser anywhere in it.**

From `gemini_web2api/gemini.py` (~350 lines, utility-module design, no classes):

**3.1 The endpoint.** It calls Gemini's own internal `batchexecute`-family RPC:

```
https://gemini.google.com{account_prefix}/_/BardChatUi/data/
  assistant.lamda.BardFrontendService/StreamGenerate
```

with query params `bl`, `hl`, `_reqid`, `rt=c`. `account_prefix` becomes `/u/{auth_user}` for non-default Google accounts. This is the *same* endpoint the Gemini web page calls when you type into it.

**3.2 The auth reconstruction.** It reimplements Google's own web-client auth scheme:

- sends the raw `Cookie` header (loaded from file, mtime-cached)
- parses `SAPISID` out of those cookies
- computes and sends `Authorization: SAPISIDHASH {ts}_{h}`
- optionally sends the `at` XSRF token from `CONFIG["xsrf_token"]`

Key functions: `load_cookie()`, `make_sapisidhash()`, `_build_payload()`, `_extract_texts_from_line()`, `extract_response_text()`, `generate()`, `generate_stream()`.

**3.3 The response parse.** Google returns a wrapped, nested-JSON RPC stream. `_extract_texts_from_line()` scans for the `"wrb.fr"` marker, deserialises the nested JSON at `arr[0][2]`, pulls the text out of `inner[4]`, and regex-detects `BardErrorInfo` for errors.

**3.4 The mimicry.** Header-level only:

```
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
X-Same-Domain: 1
+ Referer / Origin matching the genuine Gemini web client
```

No patched browser, no fingerprint spoofing at the TLS or JS level.

**3.5 What it does *not* do — and this matters.** There is **no `__Secure-1PSIDTS` rotation**. Cookies are loaded statically from a file. The mature upstream library in this space (`HanaokaYuzu/Gemini-API`) rotates that short-lived token against `accounts.google.com/RotateCookies` roughly every 9 minutes precisely because Google expires it fast. `gemini-web2api` does not, so cookie sessions go stale and must be re-exported by hand.

---

## 4. The fragility, made concrete

`config.example.json` ships:

```json
"gemini_build": "boq_assistant-bard-web-server_20260716.08_p0"
```

That is a **hardcoded Google internal web-server build ID** (the `bl` query parameter). Google rotates it. When it moves, the tool needs a new one — which is exactly why the repo ships a browser extension whose entire job is to go and fetch the current one (§6).

So the dependency chain to keep this working is: a live Google session cookie (no auto-rotation) **+** a current `SNlM0e` XSRF token **+** a current `bl` build ID, all three harvested from a real logged-in Gemini page. **This is fragile by construction**, and the repo is honest enough to ship tooling for the refresh rather than pretend otherwise.

---

## 5. What it exposes

**Endpoints** (`gemini_web2api/server.py`, ~650 lines, stdlib `http.server`):

| Route | Shape |
|---|---|
| `POST /v1/chat/completions` | OpenAI chat completions |
| `GET /v1/models` | OpenAI models list |
| `POST /v1/responses` | **OpenAI Responses API — Codex CLI** |
| `GET /v1beta/models` | **Google native — Gemini CLI** |
| `POST /v1beta/models/{model}:generateContent` | Google native, non-streaming |
| `POST /v1beta/models/{model}:streamGenerateContent` | Google native, streaming |
| `GET /` | status |

No admin/management endpoints.

⚠️ **The on-goal tell:** `/v1/responses` exists for **Codex CLI** and `/v1beta/models` for **Gemini CLI**. The intended clients include **coding agents**. (Contrast v231 CoreOfPotato, whose shipped `caller_map` registered OpenClaw and OpenCode.) **Claude appears nowhere in this repo.**

**Models** (page/README-stated), with the web product's output ceilings:

| Model | ~Output limit |
|---|---|
| `gemini-3.6-flash` | ~12k chars |
| `gemini-3.5-flash-thinking` | ~20k chars |
| `gemini-3.5-flash-thinking-lite` | ~15k chars |
| `gemini-3.1-pro` | ~12k chars |
| `gemini-auto` | varies |
| `gemini-flash-lite` | ~10k chars |

**Features:** streaming (SSE, via optional `httpx`), OpenAI-format **tool / function calling**, image input (URL or base64), Gemini's native web search.

⚠️ **A caveat the README states plainly:** *"Without a paid subscription cookie, `gemini-3.1-pro` routes to the same Flash model."* You do not get Pro for free — you get Flash silently relabelled.

---

## 6. Architecture, and the "single file" claim

The repo ships **two implementations of the same thing**:

- `gemini_web2api.py` at root — **1,108 lines / 45.9 KB**, self-contained, stdlib + optional `httpx`. The "single file" claim is substantiated.
- `gemini_web2api/` package — 8 modules: `__init__.py`, `__main__.py`, `config.py`, `gemini.py`, `models.py`, `multimodal.py`, `server.py`, `tools.py`.

⚠️ Its header does not state whether the single file is generated from the package or hand-maintained alongside it. Either way, **two copies of a protocol implementation in one repo is a drift risk** — recorded as an observation, not asserted as a defect.

Also present: `tests/`, `.github/workflows/` (**only `docker.yml`** — CI builds a Docker image; the tests are **not gated in CI**), `Dockerfile`, `docker-compose.local.yml`, `cloudflare/`, `gemini-cookie-sync-extension/`, `README.md` + `README_CN.md`.

**The browser extension** (`gemini-cookie-sync-extension/` — `manifest.json`, `popup.html`, `popup.js`, `README.txt`, `SETUP.md`): extracts the **XSRF token (`SNlM0e`)** and the **`gemini_bl` build value** from a live Gemini session and writes them to a local `gemini-auth.json`. Its own README carries a genuinely good warning:

> the auth file *"represents the real Google session and must be treated as secret. Do not send it, print it, or commit it to Git."*

**The Cloudflare Worker** (`cloudflare/worker.js` + `README.MD`): a serverless edge deployment of the same proxy across Cloudflare's ~300+ locations, with credentials (`COOKIE_STRING`, SAPISID, custom API keys) stored as **Cloudflare dashboard environment variables**, and — per its docs — browser-fingerprint rotation. Its README also warns: *"Cookie 等同于你的 Google 账号凭证"* (*"cookies are equivalent to your Google account credentials"*).

⚠️ Running this path puts **your live Google session credentials into a third-party edge platform**, and moves the traffic off your IP — which is what makes it effective against rate-limiting, and what makes it a materially larger commitment than running it locally.

---

## 7. "Zero auth" vs "Zero cost" — resolved, and it is *not* drift

The two taglines differ, so this was checked by hand (the v231 lesson, where a CHANGELOG that said *"Open-source release of CoreNexus"* turned out to be genuine artifact contamination). Here the check comes back **clean** — both strings are real and both are accurate to a different facet:

- **"Zero auth"** — two senses, both true: (i) the proxy's *own* API key is optional, and (ii) **anonymous Gemini access works without a Google account** for the Flash-tier models.
- **"Zero cost"** — you pay Google nothing; the free consumer tier is the substrate.

README, verbatim: *"Optional API keys: `api_keys` empty = no authentication required; with keys configured, validates as OpenAI Bearer Key"* and *"Anonymous access works for all models, but `gemini-3.1-pro` without authentication routes to Flash instead."*

**This anonymous path is the genuinely notable claim.** v231 required you to log into your *own* accounts. This can serve Gemini Flash with **no account at all** — which inverts the risk profile (§8.2).

---

## 8. Security & risk (`#66`) — read this section

### 8.1 The install is benign

`pip install httpx` (optional) + `python gemini_web2api.py`. Stdlib-first, MIT, **no `curl|bash`, no compiled binary, no postinstall script, no telemetry**. This is a **materially safer install than v231**, which pulled a black-box precompiled Chromium from an anonymous vendor.

The risk here is **not** supply chain. It is the runtime posture and the legal/account exposure.

### 8.2 The risk asymmetry (worth stating precisely)

- **Anonymous mode:** exposes *no account of yours*. There is nothing for Google to ban. The pressure lands entirely on Google (IP-level throttling / blocking) — which the Cloudflare Worker path is designed to spread out.
- **Cookie mode:** exposes a **real Google account**, with **no token rotation**, and the cookies sit in a file (or in Cloudflare env vars).

### 8.3 ⚠️ The shipped network posture — source-verified

Three findings, each read from the source:

1. **`config.example.json`: `"host": "0.0.0.0"`** — binds to **all interfaces**, not loopback. (v231, for all its faults, bound `127.0.0.1`.)
2. **`server.py`: the auth check fails OPEN** —
   ```python
   keys = CONFIG.get("api_keys") or []
   if not keys: return True
   ```
   No keys configured ⇒ **every request is authorised**. And this is not an accident: the README *advertises* `api_keys` empty as a supported mode.
3. **`server.py`: unconditional wildcard CORS** —
   ```
   Access-Control-Allow-Origin: *
   Access-Control-Allow-Methods: GET, POST, OPTIONS
   Access-Control-Allow-Headers: *
   ```

Put together: **a service that can spend your Gemini entitlement (and, in cookie mode, holds your live Google session) binds to every interface, accepts any origin, and authorises everything when unconfigured.**

⚠️ **Stated fairly:** the shipped `config.example.json` *does* set `"api_keys": ["sk-gemini"]` — so the example is not auth-off. But `sk-gemini` is a **hardcoded default credential** in a public repo (the same shape as v231's `admin-token-change-me`), and the zero-key mode is documented and advertised, with the code failing open into it.

### 8.4 Other runtime notes

- `"log_requests": true` in the example config — **your prompts are written to local logs by default**.
- `auth_user`, `xsrf_token`, `cookie_file`, `proxy` all default `null` (anonymous).
- The browser extension reads live Google session material out of your browser.

### 8.5 ⚠️ No ToS / ban / legal disclaimer anywhere

Neither `README.md` nor `README_CN.md` carries a disclaimer, a terms-of-service note, a legal warning, or an account-ban caution. The only operational caution is:

> *"Google may throttle high-frequency requests; server auto-retries but sustained high load may result in blocking."*

Credential-hygiene warnings **do** exist — in the extension README and the Cloudflare README. But on the legal/ToS question the repo is silent. This is **weaker disclosure than v231**, which at least shipped a DISCLAIMER conceding account-ban risk.

**Independently of what the repo says:** using an undocumented internal endpoint of a consumer product, with a reconstructed auth header and a spoofed User-Agent, to serve programmatic traffic, is squarely against the spirit and near-certainly the letter of Google's terms.

---

## 9. Landscape — decisively **not** world-first

This is a **saturated fork-and-port ecosystem**, not a novel artifact:

| Project | Note |
|---|---|
| `gpt4free` / `g4f` | the world-canonical umbrella for free-AI-access harvesting |
| `HanaokaYuzu/Gemini-API` | ~3k★ — the **mature upstream** reverse-engineered Python library; **rotates `__Secure-1PSIDTS`** |
| `Nativu5/Gemini-FastAPI` | 646★ — OpenAI-compatible wrapper over the above |
| `ntthanh2603/gemini-web-to-api` | 193★ |
| `XxxXTeam/geminiweb2api` | 54★ |
| `n0madic/go-gemini-web2api` | a zero-dependency **Go** port |
| `cyberanrhy/gemini-web2api`, `one880808/gemini-web2api` | same-name forks/derivatives |
| a JS/Cloudflare-Workers port | edge-runtime variant |
| GitHub topic `gemini-proxy` | the genre has its own topic |

**`gemini-web2api` is genuinely independent of the mature upstream** — the `pyproject.toml` declares **zero required dependencies**, so it is not a wrapper around `HanaokaYuzu/Gemini-API`; it is its own protocol implementation. That is a real point in its favour. It is simply not first.

### 9.1 ⚠️ Two landscape findings that matter to this vault

**(i) The class already targets Claude.** `cyberanrhy/gemini-claude-web2api` — *"OpenAI-compatible proxy for Gemini **and Claude** Web APIs. Free AI access via cookie auth — no API key needed."* The identical technique is being applied to **claude.ai's own web UI**. This is the single strongest reason the class deserves the vault's attention: it is an **active harvesting/abuse vector against Anthropic's consumer product**, not just Google's.

**(ii) A corpus subject has already absorbed this as a product category.** OmniRoute (**corpus v208**) issue **#2378** requested *"a `gemini-web` provider… similar to existing `chatgpt-web`, `grok-web`, and `copilot-web` implementations"* — and it was **closed by PR #2380**. So a multi-provider gateway already in the corpus ships **four** web-UI-harvesting providers. The issue cites `HanaokaYuzu/Gemini-API`, `Nativu5/Gemini-FastAPI`, `XxxXTeam/geminiweb2api`, `ntthanh2603/gemini-web-to-api` — **it does not cite this subject**, so this is a *landscape* link, **not** a `#57` recursion.

---

## 10. Where it sits against the corpus

| Subject | Entitlement harvested | Mechanism |
|---|---|---|
| **v207 CLIProxyAPI** | CLI-tool **OAuth subscriptions** (Claude Code, Codex, Gemini CLI…) | OAuth reverse-engineering |
| **v208 OmniRoute** | same (a TypeScript **port** of v207) + now a `gemini-web` provider | same |
| **v231 CoreOfPotato** | free consumer **web-chat sessions** (Grok/Gemini/ChatGPT) | **anti-detect browser + DOM scraping** |
| **v232 gemini-web2api** | free consumer **web-chat entitlement** (Gemini) | **direct HTTP protocol RE** (no browser) |

The v207/v208 pair and the v231/v232 pair harvest **different kinds of entitlement**. Within the v231/v232 pair, the *goal* is identical and the *mechanism* is completely different — UI automation versus protocol reverse-engineering. That cross-mechanism independence is what makes v232 a strong second instance rather than a repeat.

Adjacent threads: `opencode-antigravity-auth` v67 (single-provider OAuth bridge) · `cc-switch` v73 (config switching) · `freellmapi` v112 (free-tier stacking) · `CodexPlusPlus` v117 (reseller relays) · `ai-switcher` v153 (multi-account rotation) · `CloakBrowser` v69 / `camofox-browser` v179 (anti-detection — v232 touches this only at the header level, **no N-bump**).

---

## 11. Honest bottom line

`gemini-web2api` is a **small, clever, genuinely independent piece of protocol reverse-engineering**: ~350 lines of stdlib Python that reconstruct Google's own `SAPISIDHASH` auth, speak its private `batchexecute` RPC, and translate three API shapes (OpenAI chat, OpenAI Responses, Gemini native) on top. It is far better engineered than the corpus's previous instance of this class.

It is also: **not world-first** (a crowded ecosystem with a more mature upstream), **fragile by construction** (a pinned Google build ID, no cookie rotation), **unreleased** (0 releases, tests not in CI), **undisclosed** on the legal question, and **shipped with an open-by-default network posture** on a service that can hold your Google credentials.

The value to this vault is **read-only**: the protocol path is a short, excellent lesson in what a private web endpoint looks like to someone determined to wrap it — and the broken-authentication triad is now a *confirmed recurring* pattern in this class, which makes it genuinely useful red-team material.

---

*Verification: source hand-fetched (repo page, `README.md`, `README_CN.md`, `pyproject.toml`, `config.example.json`, `gemini_web2api/gemini.py`, `gemini_web2api/server.py`, `gemini_web2api.py`, the package/extension/cloudflare/workflow trees, releases page, Trendshift, author profile). Identity, landscape and the OmniRoute-v208 link verified by independent WebSearch. **NOT source-cloned.** Two confabulations caught and discarded (the "penetration tester" characterisation; "SCU = Santa Clara University"). Corpus collision by sanity-anchored hand-grep — see the Verdict.*
