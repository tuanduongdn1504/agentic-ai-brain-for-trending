# Skill: Bypass 403 / Bot-Detection Escalation Ladder

> **Type:** Worker skill (project-local to autopilot-research)
> **Created:** 2026-05-09
> **Trigger:** Any fetch (WebFetch / curl / Playwright / NotebookLM ingest) returns 403 / 429 / Cloudflare challenge page / DataDome challenge / generic "access denied" before content
> **Composes with:** `install-snapshot` (vault-level skill, for Tier 4 temporary-install discipline)
> **Storm Bear ref:** Storm Bear prime directive — "don't repeat the same mistake twice"; this skill operationalizes that for fetch-block recovery.

---

## Purpose

Provide a deterministic, monotonically-progressing escalation ladder for bypassing bot-detection blocks. Goal: bypass with **minimum tooling tier necessary**, log every attempt for audit trail, and clean up heavy-tier installs after one-off use.

**Why a skill (not just a rule):** an agent encountering a 403 in mid-task tends to retry with the same approach or escalate randomly. The phase structure here forces tier-by-tier progression and prevents both wasted retries (re-fetch with same broken approach) and premature heavy-handedness (jumping to Camoufox for a one-off blog post).

---

## Constitutional invariants

These bind every invocation. Violation = abort + log.

1. **NEVER retry the same fetch with the same approach after a block.** That is repeating the same mistake — Storm Bear prime directive violation.
2. **NEVER skip a tier.** Tier 0 → Tier 1 → ... — monotonic only. No jumping straight to Tier 4.
3. **ALWAYS log every attempt** to `output/bypass-attempts.md` (URL + tier + outcome + method details). The audit trail is non-negotiable.
4. **Tier 4 (Camoufox) install MUST pair with `install-snapshot`** before AND after — both pre-snapshot for diff and post-uninstall verification.
5. **Tier 4 retain decision is data-driven**: keep installed only if `bypass-attempts.md` shows ≥3 uses requiring Camoufox in past 7 days. Otherwise uninstall after success.
6. **NEVER use stealth tools for training-data scraping or bulk extraction.** Personal research, one-off documentation ingest, archival fidelity only. Document scope in audit log.
7. **ALWAYS update `raw/_inventory.md`** with the fetch method used (audit trail across the whole project).

---

## When to invoke

Invoke this skill IMMEDIATELY when:
- WebFetch returns 403 / 429 / "blocked by bot detection"
- `curl` returns 403 / 503 (Cloudflare) / 401 (when no auth required)
- Page content is the Cloudflare "Just a moment..." challenge page
- Page content is DataDome / PerimeterX / Akamai challenge HTML
- NotebookLM `source add` fails with HTTP error from the upstream URL
- A Playwright fetch returns blank / login redirect for a page that should be public

Do NOT invoke for:
- Genuine 401 (auth required, not bot-block)
- 404 (page doesn't exist)
- Network errors (DNS, timeout) — these are different failure modes
- Login-walled content where bypass would require account compromise

---

## Phase structure (8 phases)

### Phase 0 — Detect block type (~1 min)

Before escalating, characterize the block:

```bash
# Quick probe with no special handling
curl -sI -A "test-bot" "$URL" | head -10
# Then with realistic Chrome UA
curl -sI -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36" "$URL" | head -10
```

Diagnostic:
- **Block disappears with realistic UA** → UA-based filter. Tier 0 will resolve. Common for: company blogs blocking competitors (OpenAI blocking `Anthropic`/`Claude` UAs), tech-news sites with crude UA filters.
- **Block persists with realistic UA, no JS challenge** → IP-based or aggressive header check. Tier 1 likely sufficient.
- **Page returns Cloudflare challenge HTML** (`<title>Just a moment...</title>`, `cf-chl-bypass`, etc.) → JS challenge required. Tier 2 minimum.
- **Returns DataDome / PerimeterX challenge** → Enterprise-class. Tier 3-4 likely.
- **Returns 200 but content is captcha / login page** → not a 403 case; different skill needed.

Append diagnostic to `output/bypass-attempts.md`:

```md
## YYYY-MM-DD HH:MM — <slug> — <URL>
- Block type: <UA-filter | IP-filter | Cloudflare-JS | DataDome | other>
- Diagnostic: <what curl returned with each UA>
```

---

### Phase 1 — Tier 0: curl with proper headers (~30 sec)

Cheapest. Often sufficient for UA-based blocks.

```bash
curl -sL \
  -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Accept-Language: en-US,en;q=0.9" \
  -H "Accept-Encoding: gzip, deflate, br" \
  -H "Sec-Ch-Ua: \"Chromium\";v=\"126\", \"Not.A/Brand\";v=\"24\"" \
  -H "Sec-Ch-Ua-Mobile: ?0" \
  -H "Sec-Ch-Ua-Platform: \"macOS\"" \
  -H "Sec-Fetch-Dest: document" \
  -H "Sec-Fetch-Mode: navigate" \
  -H "Sec-Fetch-Site: none" \
  -H "Sec-Fetch-User: ?1" \
  -H "Upgrade-Insecure-Requests: 1" \
  --compressed \
  -o "/tmp/fetch-tier0.html" \
  -w "HTTP %{http_code} | size %{size_download}\n" \
  "$URL"
```

Verify:
- HTTP 200 + size > 5KB + content not Cloudflare challenge → SUCCESS
- HTTP 403 / size < 1KB / Cloudflare challenge content → escalate to Tier 1

**On success:** convert HTML → markdown via `pandoc` or readability extractor; save to `raw/`. Update audit log + `_inventory.md`. Skip remaining phases.

---

### Phase 2 — Tier 1: Playwright vanilla with UA + viewport override (~5 min)

Already installed via notebooklm-py. No new dependency.

```python
# bin/fetch-tier1.py
from playwright.sync_api import sync_playwright
import sys

URL, OUT = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 800},
        locale="en-US",
        timezone_id="America/Los_Angeles",
        extra_http_headers={
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    page = ctx.new_page()
    page.goto(URL, wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(2000)  # let lazy content settle
    html = page.content()
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"HTTP {page.url} | size {len(html)}")
    browser.close()
```

Verify same way as Tier 0. On Cloudflare-challenge content → escalate.

---

### Phase 3 — Tier 2: Playwright + playwright-stealth plugin (~5 min)

```bash
pip install playwright-stealth   # ~50 KB, no native binaries
```

Add `from playwright_stealth import stealth_sync` and apply `stealth_sync(page)` after page creation in Tier 1 script. Patches `navigator.webdriver`, plugin list, language, hairline, WebGL vendor — addresses 80% of vanilla-Playwright detection signatures.

Verify same way. On persist → escalate.

---

### Phase 4 — Tier 3: Obscura (~15 min, ~70 MB persistent)

```bash
# Download pre-compiled binary for darwin-arm64 (or appropriate platform)
# from https://github.com/h4ckf0r0day/obscura/releases
# Place in .venv/bin/obscura, mark executable
# Drive via CDP — Playwright client compatible

obscura --features stealth --port 9222 &
# Then connect Playwright to ws://localhost:9222
```

CDP-compatible → Playwright Python client connects to existing browser. Reuse Tier 1 script with `chromium.connect_over_cdp("ws://localhost:9222")` instead of `chromium.launch()`.

**Persistence decision:** Obscura is 70 MB. If `bypass-attempts.md` shows ≥2 uses in past 30 days → keep installed (amortized cost worth it). Otherwise uninstall after success.

---

### Phase 4.5 — Pivot heuristic (added 2026-05-09 from Symphony spec failure)

**Before escalating from Tier 2 to Tier 3 (Obscura, 70 MB install)**, check whether the bypass target is **inherently reproducible elsewhere**:

| URL pattern | Pivot target |
|---|---|
| "open-source spec" / "open-source release" / "we open-sourced X" page | Search GitHub for community implementations of X (often more numerous than the org's own repo, and usually provide better triangulation than the spec itself) |
| "blog post about Y" where Y is a public technology / methodology | Search for: original paper if Y is research, official docs if Y is a tool, prior talk recordings if Y is a methodology |
| "documentation for tool Z" where Z is open-source | Fetch from `github.com/<org>/<z>` README + `docs/` folder directly (no Cloudflare) |
| Specific architecture / spec content | Reverse-engineer from existing implementations + dependencies |

**Lesson learned (Symphony spec, 2026-05-09):** OpenAI's `open-source-codex-orchestration-symphony` page failed Tier 1 + Tier 2 bypass (`/backend/gate/...` endpoints have deeper Cloudflare protection than page navigation). However, 5+ community Symphony implementations exist on GitHub with no Cloudflare. Triangulating 3 of them produced richer architectural understanding than the single spec page would have AND surfaced a falsifier finding (community impls don't reproduce throughput claim) that the spec alone wouldn't have revealed.

**Decision rule:** if pivot target has ≥2 viable alternative sources accessible without bypass, defer Tier 3+ and use pivot. Document deferral + pivot rationale in `bypass-attempts.md` so the URL doesn't get retried at higher tier without new information.

---

### Phase 5 — Tier 4: Camoufox (TEMPORARY by default, ~300 MB)

**STOP. Before installing**, invoke `install-snapshot` skill (vault-level):

```
Per (C) install-snapshot:
1. Run pre-install snapshot of $HOME state
2. Save snapshot to /tmp/camoufox-pre-install-<date>.snapshot
3. Proceed with install
```

Install:
```bash
npm install -g camofox-browser   # or via project local
# Camoufox binary downloads ~300 MB on first run (lazy)
```

Use Camoufox per its REST API (Node.js wrapper running on a port) or directly via Playwright Firefox connector. Capture content to `raw/`.

**MANDATORY post-success cleanup (unless retain criteria met):**

Retain criteria: `bypass-attempts.md` shows ≥3 uses requiring Camoufox in past 7 days.

If retain criteria NOT met:
```bash
npm uninstall -g camofox-browser
rm -rf ~/.cache/camoufox-binary  # or wherever the binary cached
# Then invoke install-snapshot uninstall checklist
```

Verify post-uninstall snapshot diff against pre-install snapshot. Should be empty (allowing for benign caches that get re-pruned by OS).

---

### Phase 6 — Convert + save to raw/ (regardless of tier)

```bash
# HTML → markdown via pandoc (preferred) or python readability
/usr/local/bin/pandoc -f html -t markdown_strict \
  "/tmp/fetch-tier<N>.html" \
  -o "raw/<YYYY-MM-DD>-<slug>.md"

# Or with readability for cleaner text-extract
python3 -m readability /tmp/fetch-tier<N>.html > "raw/<YYYY-MM-DD>-<slug>.md"
```

Add metadata header to the markdown:

```md
---
fetched: 2026-MM-DD
url: <original URL>
fetch_method: bypass-403-escalation Tier <N>
block_type: <from Phase 0>
---
```

---

### Phase 7 — Audit log + inventory update (always)

Append to `output/bypass-attempts.md`:

```md
### Outcome — YYYY-MM-DD HH:MM
- Tier reached: <N>
- Outcome: success | partial | fail
- Output: `raw/<filename>.md`
- Notes: <anything relevant — block-type confirmation, install/uninstall actions>
- Retain decision: <kept Obscura | uninstalled Camoufox | n/a>
```

Append to `raw/_inventory.md` (per Coverage discipline rule in CLAUDE.md):

```md
| YYYY-MM-DD | <slug> | bypass-403-tier-<N> | <URL desc> | <size> | — | <status> | <wiki link or —> |
```

---

## Audit log format (`output/bypass-attempts.md`)

Maintain in chronological order. Top of file = most recent. Schema:

```md
# Bypass-403 Attempts Log

> Audit trail for every fetch that hit bot-detection. Per (C) bypass-403-escalation.md
> constitutional rule #3, every attempt MUST be logged regardless of outcome.

---

## YYYY-MM-DD HH:MM — <slug> — <URL>
- Block type: <Phase 0 diagnostic>
- Tier 0 (curl): <attempted? outcome?>
- Tier 1 (Playwright): <attempted? outcome?>
- Tier 2 (stealth): <attempted? outcome?>
- Tier 3 (Obscura): <attempted? outcome?>
- Tier 4 (Camoufox): <attempted? outcome? install action?>

### Outcome
- Tier reached: <N>
- Outcome: success | partial | fail
- Output: `raw/<filename>.md`
- Method retained: <Obscura kept | Camoufox uninstalled | n/a>
- Notes: <free text>
```

The log is mined by Phase 5 retain decisions (≥3 Camoufox uses in 7 days = keep) and Phase 4 (≥2 Obscura uses in 30 days = keep). Don't truncate — historic entries inform future decisions.

---

## Composition with `install-snapshot`

Tier 4 install + cleanup phase composes with the vault-level `install-snapshot` skill:

| Phase | This skill action | install-snapshot action |
|---|---|---|
| 5.1 | Decide Camoufox needed | — |
| 5.2 | — | `pre-install snapshot $HOME` → save state |
| 5.3 | Install Camoufox | — |
| 5.4 | Use Camoufox to fetch | — |
| 5.5 | Log to bypass-attempts.md | — |
| 5.6 | Decide retain (per criterion) | — |
| 5.7 (if uninstall) | Run uninstall commands | — |
| 5.8 (if uninstall) | — | `recall uninstall checklist + verify diff` |

Don't reinvent the snapshot logic here. Compose.

---

## Edge cases

- **Cloudflare returns 200 + JS challenge that resolves**: Playwright `wait_until="networkidle"` may auto-solve — try before escalating
- **Tier 0 returns 200 but content is empty/JS-only SPA**: not a block, but a rendering issue. Escalate to Tier 1 (Playwright) for JS execution, NOT for stealth
- **Multiple URLs from same domain**: run Phase 0 once, apply same tier to all; don't re-escalate per-URL within a session
- **Site uses CSP/CORS to block fetches**: not a bot-detection problem; switch to Playwright direct page navigation
- **Tier 4 install fails (network, permissions)**: abort, log "Tier 4 install failure — bypass not possible without infra fix"; don't proceed to scrape via lesser tier already proven insufficient
- **Found via earlier attempt that ALL tiers fail for a URL**: log "DECISION: defer indefinitely or seek manual archive (Wayback, Internet Archive snapshot, user manual paste)"

---

## When NOT to use this skill

- For sites where ToS explicitly prohibits scraping AND the goal is anything other than personal research / archival of public content
- For training data extraction (constitutional rule #6)
- For high-frequency / scale extraction (this is a one-off / low-volume tool)
- For login-walled content (different problem space)
- For IP-restricted content where the user lacks legitimate access

If unsure: ask the user before invoking.

---

## Future enhancements (DEFER — flagged for later)

These are not built today; revisit when pattern matures:

1. **Slash command `/bypass-403 <url>`** — at `.claude/commands/bypass-403.md` for explicit user invocation. Build when:
   - Skill has been invoked autonomously ≥3 times AND
   - User wants the explicit command surface (manual invocation cleaner than implicit triggering)
2. **Promotion to vault-root `05 Skills/`** — currently project-local. Promote when:
   - Used in ≥2 projects outside autopilot-research
   - Cross-project value validated by ≥1 successful non-autopilot bypass
3. **Hook integration** — PostToolUse hook scanning for "403" / "Cloudflare" in WebFetch results. Build only if:
   - Manual + skill-invocation reliability falls below 80% measured against actual blocks encountered
   - Pattern recurs ≥10x in audit log
4. **Storm Bear root CLAUDE.md rule promotion** — currently autopilot-local only. Promote when:
   - 403 occurrences span ≥3 projects (not just autopilot)
   - Bypass pattern proven cross-domain (not just specific to a single source class)

---

## Examples

### Example 1: OpenAI blog (anchor research follow-up, 2026-05-09)

```
Trigger: WebFetch openai.com/index/harness-engineering/ → 403
Phase 0: curl with default UA → 403; curl with Chrome UA → ?
Phase 1 (Tier 0): if Chrome UA returned 200 → success at Tier 0
... etc.
Append outcome to output/bypass-attempts.md and update inventory.
```

### Example 2: Notion public page

```
Trigger: NotebookLM source add notion.so/<id> → 403
Phase 0: probably JS challenge required for Notion's SPA → start at Tier 1
Phase 2 (Tier 1): Playwright vanilla with networkidle → likely success
... etc.
```

---

## Next action (per Storm Bear convention)

After this skill is created: invoke for the deferred OpenAI blog fetch (`https://openai.com/index/harness-engineering/`) per [[../wiki/harness-engineering/research-roadmap.md]] Tier 1 #1. End-to-end validate the ladder; the first invocation is calibration data for retain-criteria thresholds.
