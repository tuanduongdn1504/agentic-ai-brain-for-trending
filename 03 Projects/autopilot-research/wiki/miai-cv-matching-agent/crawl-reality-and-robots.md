# Crawl Reality: robots.txt vs Bot-Blocking (video claim REFUTED)

## Source

`job_crawls.py` + live curl probes (dive `crawlability` + refute-first verify, 2026-07-05).

## The claim and the verdict

- Video claim: Google Careers was chosen because *"họ không chặn, thoải mái crawl"* (they don't block, crawl freely), unlike VietnamWorks/TopCV/ITviec.
- **REFUTED (as stated):** `google.com/robots.txt` explicitly disallows the exact crawled path:
  - `Disallow: /about/careers/applications/jobs/results?page=`
  - `Disallow: /about/careers/applications/jobs/results/?*&page=` (+ a Yandex-specific blanket rule)
- **What IS true:** there is no *technical* barrier. Live probe: HTTP 200, ~1.38MB server-rendered HTML, 14 job links per page, pagination present, no Cloudflare/challenge. The author most likely conflated "curl returns 200" with "crawling is permitted" — robots.txt was never mentioned.

## The useful distinction

| Layer | Google Careers | VietnamWorks | TopCV | ITviec |
|---|---|---|---|---|
| robots.txt | **Disallows** the crawled path | 301 even on robots.txt | 301 (Cloudflare) | Permissive (`Allow: /`) |
| Technical enforcement | None (200 + full HTML) | Infrastructure-level redirects | **403 Cloudflare challenge** | **403 Cloudflare challenge** |

- ITviec is the striking case: robots.txt says yes, the bot manager says no — the two layers can diverge in either direction.
- The video's claim about VN job boards having anti-crawl protection is **CONFIRMED** (both directions of the comparison checked live).

## Practical rules extracted

- Always check robots.txt *and* probe enforcement — either alone misleads.
- robots.txt-disallowed ≠ technically blocked ≠ ToS-licensed: three separate questions (Google's careers-specific ToS could not be pinned down in a single public fetch; general automated-access clauses apply).
- For a demo, this is a pedagogy shortcut; for a product, crawling a disallowed path is a legal/reputational risk regardless of HTTP 200 — see [[recruitment-ai-regulatory-context]].
- For hireui the whole issue is moot: a recruitment SaaS **owns its job postings** — ingestion reads your own DB, no crawler needed ([[claude-stack-port]]).

## Key Takeaways

- The only refuted claim in the video, and a high-value one: absence of a 403 is not permission.
- Cloudflare-style bot management is now the default posture of VN job boards (TopCV, ITviec confirmed live; VietnamWorks blocks at the redirect layer).
- Spoofed browser User-Agent + httpx (as the repo does) works technically against Google Careers today — and is still contrary to robots.txt.
- The block-handling discipline in this project's CLAUDE.md (tiered escalation, never retry blindly) is the operational counterpart of this finding.
