# Bypass-403 Attempts Log

> Audit trail for every fetch that hit bot-detection. Per `(C) bypass-403-escalation.md` constitutional rule #3, every attempt MUST be logged regardless of outcome. Most-recent at top.

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
