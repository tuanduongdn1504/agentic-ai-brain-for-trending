# NEW deep-dive: Last 30 Days + Firecrawl (the research/data tools)

> Two ways to feed real-world data into an agent — multi-platform engagement-ranked research, and bot-resistant web scraping.

---

## Last 30 Days — `mvanhorn/last30days-skill`

### Verified facts (gh api, 2026-06-29)
- **47,530★** · **MIT** · Python · created **2026-01-23** · pushed 2026-06-28 · not archived.
- Author **Matt Van Horn** (`mvanhorn`, GitHub since 2010). 1,012 test *cases* across ~134 test files; 60% coverage gate (84% measured).

### What it is
An open-source agent skill that researches any topic across **13+ sources** — Reddit, X/Twitter, YouTube, TikTok, Instagram, Hacker News, Polymarket, GitHub, Bluesky, Threads, Pinterest, web, Perplexity — and **ranks by real engagement** (upvotes, view counts, prediction-market odds) rather than editorial curation, then **dedupes** the same story across platforms and emits a **cited synthesis brief** (HTML + markdown).

### How it works (7 steps)
topic → **entity resolution** (disambiguate handles/repos/subreddits) → parallel multi-query expansion across enabled sources → engagement scoring → cross-source dedup/clustering → AI synthesis with inline citations → grounded follow-up Q&A. Free core (Reddit, HN, Polymarket, GitHub) needs **no auth**; TikTok/Instagram/YouTube-transcripts need an optional **ScrapeCreators** key (10K free calls) or yt-dlp; it degrades gracefully to web-only. Strict anti-slop formatting laws (mandatory inline citations, no trailing source lists).

### Claims — verdicts
- **"Was the #1 repo on GitHub" → CONFIRMED.** Trendshift archive: #1 GitHub Trending **Mar 25, 2026** (Python) and **Mar 26, 2026** (all languages); README badge corroborates. (The stage-1 agent flagged this UNVERIFIED for lack of a date; the adversarial pass *found* the dates.)
- **Sources (Reddit/X/YouTube/TikTok/Reels/HN/Polymarket) → CONFIRMED.**
- **"Deep research beyond web search" + "great for daily briefings" → CONFIRMED.**
- **"Cheaper alternative to spamming /deep-research" → UNVERIFIED.** That framing is **the video's, not the docs'** — the README never mentions `/deep-research` or token comparisons. The cost advantage (free core sources) is real, but it's not positioned as a `/deep-research` substitute.

### Operator relevance
Genuinely interesting for the **autopilot-research ingestion phase**: it automates the multi-platform research that the vault currently does by hand (and via yt-pipeline). Engagement-ranked, recency-bounded ("last 30 days") community sentiment is a *different signal* than the YouTube-bundle drains. **Low-friction pilot** (MIT, free core, install via `/plugin marketplace add mvanhorn/last30days-skill`). **Not** a hireui-product fit (recruitment SaaS has no market-sentiment feature). Cross-links: [[multi-agent-orchestration/_index]] (it *is* a multi-source research agent), [[deep-research]]-style harness, [[autopilot-research-routine]] ingestion.

---

## Firecrawl — `firecrawl/firecrawl`

### Verified facts (gh api, 2026-06-29)
- **141,085★** · **AGPL-3.0** (SDKs MIT) · TypeScript · created **2024-04-15** · pushed 2026-06-29 · not archived.
- Maker: **Firecrawl** (formerly **Mendable AI** — Mendable was *shut down* and the team *pivoted* to Firecrawl; not a rebrand, not a fork). PyPI `firecrawl-py` still credits Mendable.

### What it is
A web-scrape/crawl/extract API that turns pages into LLM-ready markdown/JSON. **Six endpoints:** Scrape, Crawl (multi-page), Map (discover all URLs), Search (web search + full content), Extract (NL → structured data), Interact (AI-driven page manipulation: click/scroll/type). Two editions: **paid cloud** + **open-source self-host** (AGPL-3.0, Docker).

### How it works
Cloud uses a proprietary **"Fire-engine"** component for rotating proxies + anti-bot evasion (Cloudflare/DataDome) + JS rendering. Self-host (Docker) includes basic fetch + Playwright. Claude Code integration via three paths: `firecrawl-cli`, `firecrawl-skills` (agent skills), and an MCP server (`npx -y firecrawl-mcp`). Python SDK `firecrawl-py` (MIT).

### Claims — verdicts
- **"Best for bot-protected pages" → PARTIAL/CONFIRMED for the cloud edition only.** Fire-engine is real and proven at scale — but **cloud-only**.
- **"Open-source gives much of the same functionality" → REFUTED.** `SELF_HOST.md` is explicit: *"self-hosted instances do not have access to Fire-engine, which includes advanced features for handling IP blocks, robot detection."* The single most differentiating feature is **absent self-hosted** — a material gap, not "much of the same."
- **"96% web coverage" → UNVERIFIED.** Vendor-stated; third-party Scrapeway (June 2026) found **~63%** success on real sites; Firecrawl's own blog claims >80% on "benchmark evaluations." Treat 96% as a marketing figure.
- **"Does more than scrape (interact, discover, crawl)" → CONFIRMED.** **"Above standard Claude Code WebFetch" → CONFIRMED** (JS rendering, proxy rotation, batch, interaction) — but WebFetch is simpler for a single easy page.

### Operator relevance
Medium, **conditional on a hireui recruitment-data feature**. If candidate/job scraping (LinkedIn/Indeed for context) enters scope, Firecrawl is the bot-resistant option (cloud, ~$0.006/page) and composes with [[multi-agent-orchestration/_index]] as a screening-agent's data layer. **AGPL-3.0 is a copyleft flag** for hireui — self-hosting the AGPL core in a proprietary SaaS triggers network-copyleft obligations (the SDKs are MIT; the cloud API avoids it). For the *vault*, Firecrawl-MCP is a cleaner ingestion path than ad-hoc scraping when a page is bot-protected — sibling to the vault's `bypass-403-escalation` skill. Cross-links: [[self-hosted-devops-oss/_index]] (self-host trade-offs + copyleft caution), [[multi-agent-orchestration/_index]], [[graphify-codebase-graph/_index]] (its Pass-3 LLM-over-docs is a related "ingest the web" pattern).

---

## Cross-links

- [[multi-agent-orchestration/_index]] — both feed a research/screening agent
- [[self-hosted-devops-oss/_index]] — Firecrawl self-host + the AGPL caution
- [[autopilot-research-routine]] — Last 30 Days as an ingestion source
- [[claude-code-plugins-stack/source-provenance]] — the #1-trending confirmation + Firecrawl self-host refutation
