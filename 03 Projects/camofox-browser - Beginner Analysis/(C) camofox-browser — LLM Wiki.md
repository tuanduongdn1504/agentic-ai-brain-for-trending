# (C) camofox-browser — LLM Wiki

> **Subject:** `jo-inc/camofox-browser` (npm `@askjo/camofox-browser` / `camofox-browser`) · v1.11.2 · MIT · © 2025 Jo, Inc
> **Ship:** v179 (2026-06-22) · **Tier:** T2 Service · **Verdict:** GOAL-ALIGNED INCLUDE 3/4 [(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG]
> **Source of truth:** cloned at commit `ce3a3b0`; all facts below are source-verified (not README-parroted). Verdict + collision record → `01 Analysis/`.
> **Browsable HTML companion (built during intake):** https://claude.ai/code/artifact/460aa60d-afd0-403b-9289-b2e33aeb40f4

---

## 1. What it is (one paragraph)

camofox-browser is an **anti-detection headless-browser automation server built for AI agents**. README tagline: *"Anti-detection browser server for AI agents, powered by Camoufox."* It wraps **Camoufox** (a Firefox fork that spoofs fingerprints at the C++ level) behind an **Express REST API** (37 routes) and an **OpenClaw agent plugin** (11 tools), and — crucially for the LLM use-case — it serves **token-efficient accessibility snapshots with stable element refs (`e1`, `e2`, …)** instead of raw HTML, so an agent can `click` / `type` against a ref rather than re-parsing a DOM. Per-user **session isolation**, proxy + GeoIP, a lazy/idle browser lifecycle, Prometheus/Sentry telemetry, and one-command Docker/Railway/Fly deploy round it out. It is built by **Jo, Inc** (askjo.ai), the team behind a consumer "personal AI agent" product.

**Mental model:** *Playwright-MCP's accessibility-tree interaction model, fused with an anti-detect browser, exposed as a multi-tenant HTTP service that any agent can drive.*

---

## 2. Why it exists (the problem it solves)

Three problems stacked:

1. **Agents get blocked.** Vanilla headless Chromium/Playwright is trivially fingerprinted and bot-walled. camofox delegates the hard part (fingerprint evasion) to **Camoufox/Firefox at the C++ level** — the agent never touches that complexity.
2. **Raw HTML burns tokens and breaks.** Feeding an LLM a full DOM is expensive and brittle. camofox returns a **windowed accessibility snapshot** (`lib/snapshot.js`: `MAX_SNAPSHOT_CHARS = 80000` ≈ ~20K tokens, with pagination so nav refs appear in every chunk) and **stable element refs** the agent re-uses across calls.
3. **Multi-tenant browser state is hard.** One browser process, many users, each needing isolated tabs/cookies/profiles without leaking into each other — handled by the session/tab hierarchy below.

---

## 3. Architecture

### 3.1 Process & object model
- **One server process** (`server.js`, 6,133 lines, ESM) running Express.
- **One lazily-launched Camoufox browser** (via `camoufox-js` + `playwright-core`), started on first request, **shut down when idle**, relaunched on demand.
- Hierarchy: **Browser → per-user Session → Tabs**. Sessions are keyed by `userId`; tabs live under a session; refs live under a tab.

### 3.2 Request lifecycle (typical agent flow)
```
POST /start            → ensure browser + create/refresh the user session
POST /tabs (or /tabs/open) → open a tab at a URL (search macros allowed)
GET  /tabs/:tabId/snapshot → accessibility snapshot + element refs (e1,e2…)
POST /tabs/:tabId/click    → act on a ref (or CSS selector)
POST /tabs/:tabId/type     → type into a ref
POST /tabs/:tabId/extract  → pull structured content
GET  /tabs/:tabId/screenshot → pixels when refs aren't enough
POST /stop             → tear down the session
```
`POST /act` is the high-level "do this action" entry; the granular `/tabs/:tabId/*` routes are the explicit verbs.

### 3.3 Lifecycle timers (source-verified defaults, `lib/config.js`)
| Concern | Env var | **Code default** | Notes |
|---|---|---|---|
| Session inactivity | `SESSION_TIMEOUT_MS` | **`600000` (10 min)** | ⚠️ see §7 doc-vs-code |
| Tab inactivity | `TAB_INACTIVITY_MS` | `300000` (5 min) | idle tabs reaped |
| Handler timeout | `HANDLER_TIMEOUT_MS` | `30000` | per-request ceiling |
| Navigate timeout | `NAVIGATE_TIMEOUT_MS` | `25000` | |
| Build-refs timeout | `BUILDREFS_TIMEOUT_MS` | `12000` | snapshot ref build |
| Max sessions | `MAX_SESSIONS` | `50` | |
| Max tabs / session | `MAX_TABS_PER_SESSION` | `10` | |
| Max tabs global | `MAX_TABS_GLOBAL` | `50` | |
| Max concurrent / user | `MAX_CONCURRENT_PER_USER` | `3` | in-flight gate (`lib/inflight.js`) |
| Native-mem restart | `NATIVE_MEM_RESTART_THRESHOLD_MB` | `300` | self-heal |
| Browser-RSS restart | `BROWSER_RSS_RESTART_THRESHOLD_MB` | `1500` | self-heal |
| Port | `CAMOFOX_PORT` / `PORT` | `9377` | |

### 3.4 Edges
- **Fly.io machine routing** (`lib/fly.js`) — wakes/targets a specific Fly machine.
- **Cloudflare Worker** (`workers/crash-reporter`) — the telemetry sink (see §6).

---

## 4. HTTP API — 37 routes (source-verified)

**Lifecycle:** `POST /start` · `POST /stop` · `GET /health` · `GET /` · `GET /metrics` (Prometheus) · `POST /pressure/cleanup`

**Sessions:** `DELETE /sessions/:userId` · `POST /sessions/:userId/cookies` · `GET|DELETE /sessions/:userId/traces` · `GET|DELETE /sessions/:userId/traces/:filename`

**Tabs (collection):** `GET /tabs` · `POST /tabs` · `POST /tabs/open` · `DELETE /tabs/:tabId` · `DELETE /tabs/group/:listItemId`

**Tab actions:** `POST /tabs/:tabId/navigate` · `/click` · `/type` · `/press` · `/scroll` · `/back` · `/forward` · `/refresh` · `/wait` · `/viewport` · `/evaluate` · `/extract`

**Tab reads:** `GET /tabs/:tabId/snapshot` · `/screenshot` · `/links` · `/images` · `/downloads` · `/stats`

**Top-level convenience:** `GET /snapshot` · `POST /navigate` · `POST /act`

**Search macros** (`lib/macros.js`) — pass `@google_search`, `@youtube_search`, `@amazon_search`, `@reddit_search`, `@wikipedia_search`, `@twitter_search`, `@yelp_search`, `@spotify_search`, `@netflix_search`, `@linkedin_search`, `@instagram_search` as a URL and it expands to the site's search query.

OpenAPI spec ships at `openapi.json` (regenerated by `scripts/generate-openapi.js`).

---

## 5. The 23 `lib/` modules (grouped)

- **Core browser:** `launcher.js` (browser/session/tab lifecycle), `camoufox-executable.js` (resolve/fetch the Camoufox binary), `snapshot.js` (accessibility snapshot + windowing/refs), `extract.js`, `macros.js`, `resources.js`.
- **I/O on a tab:** `cookies.js`, `downloads.js`, `images.js`, `tracing.js` (Playwright traces).
- **Infra/ops:** `config.js` (all `process.env` centralized for auditability), `inflight.js` (per-user concurrency gate), `proxy.js` (proxy + GeoIP), `tmp-cleanup.js`, `request-utils.js`, `fly.js`.
- **Observability:** `metrics.js` (Prometheus via `prom-client`), `reporter.js` (crash/hang telemetry), `sentry.js`.
- **Surface:** `auth.js` (bearer/API-key gating), `openapi.js`, `plugins.js` (sub-plugin loader + event bus), `persistence.js`.

---

## 6. OpenClaw plugin — 11 agent tools

Manifest `openclaw.plugin.json` (id `camofox-browser`; *"Anti-detection browser automation for AI agents using Camoufox (Firefox-based)"*; v1.11.2). `plugin.ts` → compiled `plugin.js`. Tools:

`camofox_create_tab` · `camofox_navigate` · `camofox_snapshot` (accessibility snapshot + refs) · `camofox_click` (by ref or CSS) · `camofox_type` · `camofox_scroll` · `camofox_screenshot` · `camofox_evaluate` (run JS in the page) · `camofox_list_tabs` · `camofox_close_tab` · `camofox_import_cookies` (gated behind `CAMOFOX_API_KEY`).

> The plugin is **OpenClaw-native**, but the underlying REST API is **agent-agnostic** — any agent (incl. Claude Code via shell/HTTP) can drive the same server.

---

## 7. ⚠️ Documentation vs. code discrepancy (faithfully flagged)

The README states **two** places that sessions expire after **30 minutes**:
- env table (README L625): `SESSION_TIMEOUT_MS … 1800000 (30min)`
- prose (README L661): *"Sessions auto-expire after 30 minutes of inactivity."*

But the **shipped code default** is **10 minutes**: `sessionTimeoutMs: parseInt(process.env.SESSION_TIMEOUT_MS) || 600000` (`lib/config.js:87`). Unless you explicitly set `SESSION_TIMEOUT_MS=1800000`, sessions reap at 10 min, not 30. **Trust the code default; set the env var if you want 30.**

---

## 8. Security surface (and the dual-use caveat)

- **Auth (`lib/auth.js`, manifest envVars):** `CAMOFOX_ACCESS_KEY` = global `Authorization: Bearer <key>` on every route except `/health` (recommended whenever exposed beyond localhost); `CAMOFOX_ADMIN_KEY`; `CAMOFOX_API_KEY` gates cookie import (disabled when unset).
- **Arbitrary code in pages:** `camofox_evaluate` / `POST /tabs/:tabId/evaluate` run JS in the page context, and `POST /sessions/:userId/cookies` imports cookies — both powerful; lock them down before any non-local exposure.
- **Telemetry is opt-out:** anonymized crash/hang reports go to a Cloudflare Worker; disable with `CAMOFOX_CRASH_REPORT_ENABLED=false` (see §6/§9).
- **Supply chain:** `postinstall` runs `scripts/postinstall.js` and `npx camoufox-js fetch` downloads a **browser binary** at install — run `npm-security-check` + `install-snapshot` first.
- **Dual-use:** this is an anti-detection/evasion tool. Driving logged-in or bot-walled sites may violate ToS and risk account bans — use disposable accounts and authorized targets. (Unlike CloakBrowser v69, the repo ships **no explicit Acceptable-Use enumeration** in its MIT license.)

---

## 9. Deploy & ops

- **Local:** `git clone … && npm i && npm start` (port 9377); or `npm run fetch-bin` first to pre-pull Camoufox.
- **Docker:** `Dockerfile` (+ `Dockerfile.ci`), `Makefile`, `run.sh`.
- **Railway:** `railway.toml`. **Fly:** machine-aware via `lib/fly.js`.
- **Build/release:** `build.ps1`, `release.sh`, `scripts/sync-version.js` (keeps `package.json` / `openclaw.plugin.json` / `openapi.json` in lockstep on `npm version`).
- **Tests (Jest, ESM):** `npm test` (unit), `test:e2e`, `test:plugins`, `test:live` (gated by `RUN_LIVE_TESTS=1`).
- **Stack:** Express 4 · `playwright-core` ^1.58 · `camoufox-js` >=0.10 · `prom-client` · `swagger-jsdoc` · Node ESM.
- **Sub-plugins (`plugins/`):** `persistence` · `vnc` (live view) · `youtube`. Loaded by `lib/plugins.js` over an internal event bus.

---

## 10. Corpus placement (for the wiki maintainer)

- **Closest sibling:** **CloakBrowser v69** — the corpus's first purpose-built stealth browser, but a *Chromium/ungoogled-chromium SDK + Playwright drop-in (CDP)*. camofox is the **N=2** anti-detect browser: a *Firefox/Camoufox **server** for **AI agents*** (REST + OpenClaw plugin + token-efficient snapshots). Same species, different engine **and** different delivery shape.
- **Adjacencies:** browser-use v34 / Skyvern v24 (agent browser *automation*, stealth-as-a-feature) · Agent-Reach v174 (web/social *read+search* capability layer for agents) · crawl4ai v29 (LLM-friendly crawler library) · Scrapling v149 (undetectable scraping library, Library-vocab #21).
- **Pattern outcome:** 1 NEW §C Library-vocab standalone at **N=2** ("Anti-Detect / Stealth Browser…"), crediting CloakBrowser v69's priority; counts unchanged 46/10. Full reasoning → `01 Analysis/(C) v179 camofox-browser — Verdict & Collision-Check Record.md`.

---
*Built inline (no multi-agent workflow — see vault memory `feedback_wiki_verify_independently_check_collisions`). Facts source-verified from the clone at `ce3a3b0`; the CloakBrowser-collision scoping verified by hand-grep over `_state/` + `_patterns/`.*
