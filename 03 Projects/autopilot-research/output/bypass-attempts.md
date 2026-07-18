# Bypass-403 Attempts Log

> Audit trail for every fetch that hit bot-detection. Per `(C) bypass-403-escalation.md` constitutional rule #3, every attempt MUST be logged regardless of outcome. Most-recent at top.

---

## 2026-07-18 20:xx — herdr-bundle — youtube.com/watch (yt-dlp caption fetch ×8)

- **Block type:** YouTube **HTTP 429 "Too Many Requests" + "Sign in to confirm you're not a bot"** on the webpage/player fetch that precedes caption download. NOT a Cloudflare-page block — this is YouTube's account/bot gate against yt-dlp, so the HTML-page tiers in `(C) bypass-403-escalation.md` (curl → Playwright → stealth → Camoufox) DO NOT APPLY. The correct ladder for yt-dlp is its own cookie/client options.
- **Trigger context:** lightweight calls (`ytsearch25:` search + metadata `--print`) succeeded; only the heavier webpage+player fetch for subtitles tripped the gate. Same pipeline worked ~6h earlier (vercel-eve) → freshly-accumulated per-IP rate limit, not a permanent block.
- **yt-dlp Tier 0 (native cookies):** `--cookies-from-browser chrome` → extracted 3,356 cookies, solved the JS challenge via deno, gate cleared. SUCCESS. Fetched 6 of 8 transcripts (t1-t6).
- **Re-block on tail:** after 6 rapid cookie'd fetches the 429 re-accumulated; t7 (Better Stack) + t8 (Fru Dev) died mid-fetch. 2nd attempt (gentler: `--sleep-requests 3 --retries 3`) died the same way.
- **Decision (per prime directive — don't repeat the same mistake twice):** stopped at 2 attempts; shipped on the 6 landed transcripts (bundle range is 5-8; healthy). Did NOT escalate to browser-scrape / Claude-in-Chrome for 2 marginal sources — primary ground truth + t1/t2/t4 tmux/cmux comparisons cover their angles.

### Outcome
- Tier reached: yt-dlp native cookies (`--cookies-from-browser chrome`) — a NEW ladder rung distinct from the HTML-page tiers.
- Outcome: partial success — 6/8 transcripts.
- Output: `raw/2026-07-18-herdr/t1-t6.md`.
- Method retained: n/a (no install; browser cookies are ambient).
- **Lesson for next YouTube 429:** START with `--cookies-from-browser <browser>`; space requests (`--sleep-requests`) to avoid tail re-block; for >5-video bundles, fetch in 2 batches with a cooldown between. Candidate to codify as a yt-dlp-specific mini-ladder in `(C) bypass-403-escalation.md` (currently HTML-only).

---

## 2026-05-09 15:05 — openai-symphony-spec — https://openai.com/index/open-source-codex-orchestration-symphony/

- **Block type:** Cloudflare-class with **deeper backend gating**. Initial navigation succeeds (HTTP 200) but client-side `/backend/gate/...` calls return 403 → Next.js error component renders ("This page couldn't load"). Different failure mode from harness-engineering blog (which let backend gates through).
- **Tier 0 (curl):** ATTEMPTED — 403 (same as harness-engineering blog).
- **Tier 1 (Playwright vanilla, calibrated):** ATTEMPTED. HTTP 200 navigation but body contains only the Next.js 404 component (`h1='This page couldn't load'`, `articles=0`, `body_text_len=70`). Diagnostic: 21 of 106 responses are non-200; specifically `/backend/gate/...` endpoints return 403 even after navigation succeeds.
- **Tier 2 (Playwright + playwright-stealth 2.0.3):** ATTEMPTED. Same outcome as Tier 1 — fingerprint stealth doesn't help because the backend gate check appears to be deeper than browser fingerprint.
- **Wayback fallback:** archive.org/wayback/available returned `archived_snapshots: {}` — URL too new (12 days old, likely never crawled). Direct Wayback fetch 429 (rate-limited).
- **Tier 3-4:** NOT attempted. Pivoted instead.

### Outcome

- **Tier reached:** 2 (failed)
- **Outcome:** PIVOT — bypass deferred indefinitely. Pivoted to ingesting 3 community Symphony implementations on GitHub (no Cloudflare). 3 independent reproductions = stronger evidence than the single missing spec.
- **Output:** `raw/2026-05-09-symphony-community-synthesis.md` + new wiki article [[../wiki/harness-engineering/symphony-architecture]]
- **Method retained:** `playwright-stealth 2.0.3` installed in venv (~50KB) — kept; useful for any future Tier 2 attempt
- **Notes:**
  - **New failure-mode pattern detected:** OpenAI sometimes wraps article content with backend `/backend/gate/...` endpoints that have stricter Cloudflare protection than the page navigation. Tier 1+2 bypass the static page but not the dynamic content. **For OpenAI URLs that fail Tier 2 like this, suggest the article requires login OR the page was unpublished.**
  - **Pivot strategy worth codifying:** when an "open-source spec" page is blocked, search GitHub for community implementations FIRST before escalating to Tier 3+ — community reproductions often provide better triangulation than the original artifact.
  - **Skill calibration:** add a Phase 5.5 "Pivot heuristic" that says "if URL claims to point to open-source content but bypass fails ≥Tier 2, search GitHub for org-OR-community-named repos matching the topic before escalating to Tier 3."

---

## 2026-05-09 14:25 — openai-blog-harness-engineering — https://openai.com/index/harness-engineering/

- **Block type:** Cloudflare-class. `accept-ch` header in 403 response reveals OpenAI uses Client Hints challenge. Both crude and realistic Chrome UAs returned 403 + ~9KB challenge body.
- **Tier 0 (curl):** ATTEMPTED with full Chrome headers including `Sec-Ch-Ua-*` Client Hints. Result: HTTP 403, 0 bytes. Cloudflare TLS fingerprint or JS challenge — curl can't pass.
- **Tier 1 (Playwright vanilla):** ATTEMPTED. First try with `wait_until="networkidle"` → 45s timeout (Cloudflare-protected SPAs never networkidle). Second try with `wait_until="domcontentloaded"` + 8s wait → **HTTP 200, 489KB Next.js page, real title**. SUCCESS.
- **Tier 2-4:** not needed.

### Outcome

- **Tier reached:** 1
- **Outcome:** success
- **Output:** `raw/2026-05-09-openai-blog-harness-engineering.md` (extracted via `bin/html-to-clean-md.py` — readability-lxml + pandoc + custom regex strip; 227 lines / 21 KB clean article body)
- **Subsequent action:** uploaded as text source to existing NotebookLM `d772d58b-ff6c-41c5-aec1-7cd83637226e` (notebook now has 3 sources). NotebookLM URL-add ALSO got Cloudflare-blocked initially — ingested "Just a moment..." challenge page; deleted that bad source and used file upload instead.
- **Method retained:** Playwright vanilla already installed via notebooklm-py — no install delta. `readability-lxml` added (small Python pkg, ~200KB) — kept (useful for any future HTML→md cleanup).
- **Notes:**
  - **Calibration finding:** `wait_until="domcontentloaded"` + N-second wait beats `networkidle` for Cloudflare-protected sites. Saved into `bin/fetch-tier1.py` defaults.
  - **NotebookLM URL ingest is NOT a viable path for Cloudflare-blocked sites** — its fetcher hits the same wall. Always fetch via Tier 1+ and upload as file/text source instead.
  - This attempt validated the escalation skill end-to-end on first invocation. Next 2-3 invocations will further calibrate the tier-skip thresholds.

---

## How retain decisions are made

- **Tier 3 (Obscura):** keep installed if log shows ≥2 Obscura-tier successes in past 30 days
- **Tier 4 (Camoufox):** keep installed if log shows ≥3 Camoufox-tier successes in past 7 days; otherwise uninstall + verify via `install-snapshot`

Current state (2026-05-09): no Tier 3 or 4 installs to date. All bypasses solved at Tier 1.
