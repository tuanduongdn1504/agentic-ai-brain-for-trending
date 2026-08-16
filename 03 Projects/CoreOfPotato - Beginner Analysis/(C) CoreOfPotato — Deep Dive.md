# (C) CoreOfPotato — Deep Dive

> **v231** · subject `hwahao/CoreOfPotato` · built 2026-08-16 · operator-requested (link arrived via Facebook, `fbclid` stripped)
> ⚠️ **NOT source-cloned.** Everything below is verified by hand from the rendered repo page, raw files fetched individually (`README.md`, `CHANGELOG.md`, `DISCLAIMER.md`, `EASY_START.md`, `requirements.txt`, `setup_cloak.py`, `config.example.json`, `core/server.py`, `core/routes.py`, `core/drivers/grok.py`, `.github/workflows/ci.yml`), the commit list, the author profile, and independent WebSearch. The v200→v230 self-throttle applies (the ~205K shim overflows every subagent → no workflow, no subagent; this was hand-built inline).

---

## 1. What it actually is

`hwahao/CoreOfPotato` — repo description, verbatim:

> *"CoreOfPotato is an open-source API gateway and stealth browser automation framework. It bridges OpenAI-compatible clients with web AIs (Grok, Gemini, ChatGPT) via session multiplexing."*

Strip the marketing and the mechanism is blunt and easy to state:

**You log into your own free Grok / Gemini / ChatGPT accounts inside an anti-detect browser. CoreOfPotato keeps those tabs alive, drives them by scraping the chat UI's DOM, and re-exposes them to your local tools as an OpenAI-compatible `/v1/chat/completions` endpoint.**

It is a **free-tier harvester with an API face**. Not an API client — there is no API key to any model anywhere in it. The "models" are the vendors' consumer web apps, puppeted.

**Facts (page-stated §37.4 — the GitHub API is mocked in this environment):** MIT · Python · **~16★ / 3 forks** · **7 commits total** · v1.0.1 · first commit **2026-06-06**, last commit **2026-06-09** → **no activity in ~2 months** as of today.

---

## 2. Architecture (source-verified)

Three tiers: **client → aiohttp server → Playwright/Chromium contexts.**

```
your tool (OpenClaw / OpenCode / LangChain / curl)
      │  POST /v1/chat/completions   Authorization: Bearer OCtest
      ▼
core/server.py   (aiohttp)  ── /hub dashboard, /api/* admin
      │  nav_key = f"{caller}{modu}_{platform}"
      ▼
core/browser_mgr.py  ── worker pool: grok×3, gemini×1, chatgpt×2
      ▼
CloakBrowser (anti-detect Chromium)  ←── corpus subject v69
      ▼
grok.com · gemini.google.com/app · chatgpt.com   (your logged-in sessions)
```

### The endpoint is real
`core/server.py` registers, verbatim:

```python
app.router.add_post("/v1/chat/completions", self.api_chat_completions)
```

**SSE streaming is genuinely implemented** (`stream = body.get("stream", False)` → an async generator over `submit_job_streaming()` emitting `text/event-stream`). *(Note for the record: `core/routes.py` contains only the `/api/*` admin surface — the OpenAI route lives in `server.py`. I checked the second file before calling that a discrepancy; it isn't one.)*

### "NaModu" — the session key
Auth doubles as the session identifier. A **6-character key** = a 2-char registered *caller* prefix + a 4-char *module* tag, e.g. `OCtest`. It is read from the request body `user`, or a `Bearer` header, or `x-user`, then run through `validate_user()`, which checks the prefix against a registered map. The shipped `config.example.json` registers exactly two callers:

```json
"caller_map": { "OC": "OpenClaw", "CD": "OpenCode" }
```

⚠️ **That is the most on-goal line in the repository.** The intended clients are **coding agents**, not chat apps. The whole system exists to feed a coding agent free inference.

The key then becomes the routing key: `nav_key = f"{caller}{modu}_{platform}"` maps a caller to a specific browser tab, so `OCtest` always lands in the same conversation → **conversation continuity without an API's conversation state.** That is the "session multiplexing" in the tagline, and it is the one genuinely clever idea here.

### Conversation-URL lifecycle
Three cache strategies: **fixed** (never expires), **time-based** (default 30 min), **usage-based** (default 10 uses, the shipped default). This is a real design decision — a long-lived web conversation accumulates context and eventually degrades or hits a cap, so the URL is recycled.

### Drivers
`core/drivers/` = `base.py`, `chatgpt.py`, `gemini.py`, `grok.py`. New platforms are added by subclassing `BaseDriver` and registering it. **There is no `claude.py`.**

`grok.py`, source-verified: `class GrokDriver(BaseDriver)`, a union of fallback selectors (`textarea, div[contenteditable="true"], #prompt-textarea, [role="textbox"]…`), `type_human_like(editor_selector, prompt)`, then `await asyncio.sleep(random.uniform(0.5, 1.2))` before submitting, `dismiss_cookie_consent()`, and completion detection by polling every 0.25 s until `stable_count >= 8` — **i.e. "the answer is finished when the text stops changing for about two seconds."**

That heuristic is the honest heart of the thing. It works, and it is brittle by construction: a vendor CSS refactor, a slow token, or a UI A/B test breaks it. It is worth reading precisely *because* it shows you what you buy with a real API contract.

### Stealth
`requirements.txt` is three lines:

```
aiohttp>=3.9.0
playwright>=1.40.0
cloakbrowser>=0.3.31
```

`setup_cloak.py` pip-installs `cloakbrowser`, calls `cloakbrowser.ensure_binary()` to download its Chromium build, reads `binary_info()`, and writes the path into `config.json` as `browser.executable_path`. So "stealth" = **point Playwright at CloakBrowser's patched Chromium instead of stock Chromium.** (This also resolves an apparent gap: `config.example.json` has no `stealth`/`cloak` key — `executable_path` *is* the cloak hook.)

Headless is a toggle, and the docs are candid that it mostly doesn't work: *"headless mode triggers bot protections on Grok and ChatGPT, causing them to fail or timeout."* Headed is the default. You watch the browser type.

### Ops surface
A local dashboard at `/hub` (slot status, key management, logs), `/api/*` admin routes, log export/retention, a load-test harness, and real CI (`ci.yml`: Python **3.9**, `ruff check .`, `playwright install --with-deps chromium`, `pytest`).

---

## 3. ⚠️ The corpus-recursive dependency: CloakBrowser = **v69**

**CoreOfPotato is built on a corpus subject, and openly says so.** The v1.0.0 CHANGELOG entry credits *"Complete integration with CloakBrowser for advanced stealth browser automation."*

I did **not** assume this from the shared name (the v207 lesson — `eceasy/cli-proxy-api` ↔ cortex-hub v181 was verified, not inferred). Verified independently: PyPI `cloakbrowser` is *"a drop-in Playwright replacement with source-level fingerprint patches… a thin wrapper around a custom-built Chromium binary… auto-downloads the binary… from **CloakHQ**."* That is **corpus subject v69** — CloakHQ's purpose-built stealth Chromium, recorded in the corpus as delivered *"as a Python/JS SDK + Playwright drop-in via CDP."* Exact match on author, engine, and delivery shape.

So the dependency chain is: **v231 CoreOfPotato → v69 CloakBrowser.** Because it is *credited* rather than silently vendored, this is a genuine **Pattern #57** corpus-recursive citation — stronger than cortex-hub v181's silent GitNexus v33 bundling, and the same shape as page-agent v199 → browser-use v41 and OmniRoute v208 → CLIProxyAPI v207.

---

## 4. Who built it

**`hwahao`** — GitHub bio, verbatim:

> *"An ordinary worker with no coding skills. I'm unemployed and forced to adapt, hoping that what I do will prove my capabilities."*

Location **Ha Noi, Viet Nam**. **Two public repositories**: CoreOfPotato, and a fork of AutoGPT. Not Anthropic; no company; no website.

Read that against the artifact: 7 commits over 4 days producing an aiohttp gateway, a driver registry, a dashboard, a load-test harness, GitHub Actions CI, ruff, pytest, CONTRIBUTING, DISCLAIMER, and a changelog in Keep-a-Changelog format. Four of those seven commits are `fix(ci):` — Python 3.9 typing compatibility and ruff errors, i.e. code that did not run until CI told it so.

And one verified tell: **the CHANGELOG's v1.0.0 entry reads "Open-source release of CoreNexus."** Not "Core of Potato." I re-fetched with a targeted yes/no-and-quote question specifically to rule out a summarizer artifact (the v193 false-drift lesson) — **the string is literally in the file.**

The honest reading: this is **an AI-generated / vibe-coded project by a self-taught non-programmer**, shipped as a portfolio piece by someone explicitly trying to prove employability. That is not a slight — it is a data point about who is now able to ship infrastructure, and it is the corpus's first subject authored by a self-described non-coder. It is also why the residual name of some other scaffold survives in the changelog.

*(Corpus note: "AI-Generated-Repo Artifact Contamination" was registered as an observational candidate at **v69** — the same wiki as this subject's dependency — but was never carried into the pattern registry. CoreOfPotato is a textbook instance. Recorded as a cross-reference for the audit, not self-incremented.)*

---

## 5. What it is **not** (the honest boundaries)

| Claim | Reality |
|---|---|
| World-first | **No.** `gpt4free` / `g4f` is the world-canonical flagship of reverse-engineered free-provider aggregation, including browser automation, and precedes this by years. There are whole `gpt4free` and `free-ai` GitHub topics. |
| Corpus-first | For the *surface*, yes — no prior corpus subject browser-automates consumer web-chat UIs into an API. But the corpus already holds the neighbouring family (v73, v112, v117, v153, v67, v207, v208). |
| An N=3 of the CLIProxyAPI v207 standalone | **No.** That row is scoped to *"Re-Exposes **CLI-Tool OAuth Subscriptions**."* CoreOfPotato re-exposes **free consumer web-UI sessions scraped through a browser** — a different source mechanism. It does **not** satisfy v207's pending promotion trigger. |
| An instance of the stealth-browser standalone (v69/v179) | **No** — it is a *consumer* of that class, not a member. |
| Claude-supporting | **No.** No `claude.py` driver; Claude appears nowhere. |
| Ships an MCP server | **No.** |
| Viral (#52) | **No.** ~16★ / 3 forks, page-stated, and stale since June 9. |

---

## 6. ⚠️ Risk — the section that matters

**This is the most fenced subject since CLIProxyAPI v207, and arguably harder-fenced.** v207 at least rode official OAuth flows. This one drives consumer UIs behind an anti-detect browser *specifically to evade the bot protection the vendors deployed to stop it.*

1. **ToS + account ban.** OpenAI, Google and xAI all prohibit automated/scripted access to the consumer web apps and circumvention of rate limits. The repo's own `DISCLAIMER.md` concedes it, disclaiming liability for *"damages, consequences, or account bans resulting from the use of this software"* and calling itself *"strictly for educational and personal use."*
2. **A black-box binary.** `setup_cloak.py` downloads a **pre-compiled Chromium from CloakHQ** — an anonymous vendor. Independent commentary on the package flags exactly this: a black box running with your logged-in AI sessions.
3. **It ships with authentication off.** Verified in both the config and the code:
   ```json
   "security": { "admin_token": "admin-token-change-me", "cors_origins": ["*"], "require_auth": false }
   ```
   and `require_admin` **allows the request when no token is configured**. The gateway holds live authenticated sessions to your personal AI accounts and, out of the box, will serve **any local process and any web origin** that can reach `127.0.0.1:2809`. Host binding is local-only by default, which is the one thing standing between this and a very bad afternoon.
4. **Credentials at rest.** `./data/browser_profiles` persists your logged-in browser profiles — session cookies for your Google/OpenAI/xAI accounts — on disk.
5. **Abandonment.** No commits in two months on a project whose entire premise is keeping up with three vendors' UI changes. UI-scraping rots fast.

---

## 7. What is actually worth taking

The product is not the value. Three things are:

1. **The security anti-pattern, as a live specimen.** `require_auth: false` + `cors_origins: ["*"]` + "no token configured ⇒ allow" + a service holding authenticated sessions is a textbook broken-authentication finding — and it composes directly with the vault's live **api-security / BOLA** thread. Read it as a red-team exercise, not as a tool.
2. **The vendor-seam shape.** `BaseDriver` + a driver registry + per-platform worker pools is a clean, legible seam. It is the same lesson as meetily v196's `generate_summary()`, AIRI v210's `xsAI`, and lobehub v222 — abstract the 90 % that is shared, special-case the 10 % that genuinely differs.
3. **Why an API contract is worth paying for.** "The answer is done when the text stops changing for two seconds" is a perfectly reasonable engineering response to having no contract at all. Holding that next to a real streaming API is the cheapest possible argument for the line the vault already draws: **official, paid keys.**

---

## 8. Ledger

| Axis | Call |
|---|---|
| (a) Anthropic-affiliated | **FAIL** — disclosed individual, Hanoi VN, not Anthropic (§41; a shared VN locale with the operator is **not** an (a)-rescue) |
| (b) Goal-relevance | **MODERATE** — keys the tier (⚠️ STRONG and OFF-GOAL both recorded reviewable) |
| (c) Substance | **MODERATE** |
| (d) Connectivity | **STRONG** |

**GOAL-ALIGNED INCLUDE 3/4. NO MINT.** Counts **46/11 UNCHANGED**; §C live standalones **47** unchanged. Full reasoning in *(C) CoreOfPotato — Verdict*.
