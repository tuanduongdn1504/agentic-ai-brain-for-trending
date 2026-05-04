# crawl4ai - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`unclecode/crawl4ai`](https://github.com/unclecode/crawl4ai) — **"🚀🤖 Open-source LLM Friendly Web Crawler & Scraper."**

**64,417 stars (#7 corpus — between BMAD v11 45K and agency-agents v18 82.9K), 6,598 forks (10.2%), Apache-2.0, Python, main-branch, created 2024-05-09 (~24 months old), pushed 2026-04-20, 150 MB, 74 open issues, homepage crawl4ai.com**. Author: **unclecode** (solo — 3rd solo-enterprise-scale in corpus after graphify v16 30K + agency-agents v18 82.9K). **Cloud API Closed Beta launching soon** (Pattern #31 Open-Core candidate). PyPI: `pip install crawl4ai`. Current version: **v0.8.6**.

**Scope status: T4 Agent-as-bridge — 6TH T4 entrant.** T4 becomes 2nd-largest tier (N=6) after T1 (N=9).

**Tagline:** *"Crawl4AI turns the web into clean, LLM ready Markdown for RAG, agents, and data pipelines. Fast, controllable, battle tested by a 50k+ star community."*

**Origin story (README verbatim):**
> *"In 2023, I needed web-to-Markdown. The 'open source' option wanted an account, API token, and $16, and still under-delivered. I went turbo anger mode, built Crawl4AI in days, and it went viral. Now it's the most-starred crawler on GitHub."*

**Core product — web → LLM-friendly markdown/JSON extraction:**

| Feature category | Highlights |
|------------------|------------|
| **Markdown generation** | Clean + Fit markdown (heuristic noise removal) + citations + BM25 filtering |
| **Structured data extraction** | LLM-driven + CSS/XPath + JSON schemas + chunking (topic/regex/sentence) + cosine similarity |
| **Browser integration** | Chromium + Firefox + WebKit + managed browsers + persistent profiler + session mgmt + proxy + hooks |
| **Crawling & scraping** | Media (images/audio/video/srcset) + dynamic JS + screenshots + raw data + iframe + lazy load + infinite scroll |
| **Deployment** | Docker + FastAPI server + JWT auth + API gateway + cloud-ready |
| **Anti-bot (v0.8.5)** | **3-tier detection + proxy escalation + Shadow DOM flattening + consent popup removal** |
| **Stealth mode** | Mimic real users to avoid bot detection |

**Key architecture signals:**
- **Playwright-based** (`python -m playwright install --with-deps chromium`)
- **`crwl` CLI** (short alias) + `crawl4ai-setup` + `crawl4ai-doctor`
- **LLM-agnostic** — supports all LLMs (open-source + proprietary)
- **BYO extraction strategies** — CSS / XPath / LLM / JSON schemas
- **Pre-release versions** via `pip install crawl4ai --pre`
- **v0.8.6 security hotfix** — replaced `litellm` with `unclecode-litellm` fork due to PyPI supply-chain compromise (**corpus-first documented supply-chain incident response**)

**Sponsorship tiers (4-tier monetization):**
| Tier | Price | Benefits |
|------|-------|----------|
| 🌱 Believer | $5/mo | Join movement |
| 🚀 Builder | $50/mo | Priority support + early access |
| 💼 Growing Team | $500/mo | Bi-weekly syncs + optimization |
| 🏢 Data Infrastructure Partner | $2000/mo | Full partnership + dedicated support |

**Commercial path:** Open-Source Now → **Cloud API Closed Beta Soon** (Pattern #31 Open-Core candidate, 3rd corpus data point potentially after fish-speech v20 + Skyvern v24).

**v2 Routine 12-axis classification:**

| Axis | Value |
|------|-------|
| **Tier** | **T4 Agent-as-bridge (6TH entrant)** |
| **Archetype** | **Solo-enterprise-scale-web-utility-with-open-source-anti-bot** (NEW T4 variant) |
| **Scale tier** | **64K stars** (solo, viral; 3rd solo-enterprise-scale corpus point) |
| **Primary lang** | Python |
| **Packaging** | pip + Docker + PyPI |
| **Origin story** | Solo developer 2023 "turbo anger mode" after commercial alternative ($16/scrape) — viral |
| **Methodology** | Playwright-based browser crawling + LLM-agnostic extraction + BM25/cosine filtering |
| **Governance files** | README-heavy + Apache-2.0 (no visible SECURITY.md from probe; check needed) |
| **Feature count** | 6 feature categories + 30+ sub-features |
| **i18n** | EN only |
| **Intellectual influence** | None cited explicitly (community-viral no-lineage per Pattern #19 archetype 3) |
| **Agent platforms** | Compatible with RAG/agents/pipelines via markdown + JSON output |

**Tier placement rationale:** T4 Agent-as-bridge — web content → LLM markdown bridge. Conceptual parallel with v28 markitdown (files → markdown); crawl4ai is webpages → markdown/JSON. Not agent framework (not T1); not educational (not T3); not standalone autonomous agent (not T5).

**T4 extends to N=6** (from N=5 post-v28). 6 distinct archetype variants now; T4 most-archetype-diverse tier.

**v29 pattern implications preview:**
- **Pattern #27 Community-Viral Scale Path 7th data point** — 64K/24 months = ~90 stars/day, solo-organic
- **Pattern #20 Solo-Scale Ceiling dictionary** — 3rd solo-enterprise-scale row (graphify 30K + agency-agents 82.9K + crawl4ai 64K — solo ceiling ~80K observable)
- **Pattern #29 License-Category Diversity** — 3rd Apache-2.0 (gws v13 + HF v26 + crawl4ai v29)
- **Pattern #28 Multi-Provider AI Support 5th data point** — LLM-agnostic extraction accepts all LLMs
- **Pattern #47 Vision-DOM-Free Browser Automation (candidate N=1 Skyvern v24)** — crawl4ai is DOM-based (CSS/XPath), NOT vision. **Refines #47 as vision-specific (not all browser automation).** Distinguishes Skyvern's vision approach from crawl4ai's DOM approach.
- **Pattern #48 Proprietary Anti-Bot Commercial Moat (candidate N=1 Skyvern v24)** — crawl4ai has **open-source anti-bot detection** (3-tier + proxy escalation). **Distinguishes #48 as specifically proprietary.** crawl4ai open-source anti-bot = distinct pattern.
- **Pattern #31 Open-Core Commercial Entity (CONFIRMED v24)** — Crawl4AI Cloud API closed beta launching soon = **3rd data point pending** (after fish-speech 39 AI INC + Skyvern-AI)
- **NEW candidates at v29:**
  - **#64 Open-Source Anti-Bot Detection** — 3-tier detection + proxy escalation + Shadow DOM + consent popup removal. Open-source counterpart to #48 proprietary-anti-bot-moat.
  - **#65 4-Tier Sponsorship Monetization** — $5/$50/$500/$2000 structured sponsorship tiers as solo-project monetization. Distinct from LLC (BMAD), open-core (fish-speech/Skyvern), donation-only (OMC GitHub Sponsors general).
  - **#66 Supply-Chain Security Incident Response** — `unclecode-litellm` fork response to upstream compromise. First corpus documented supply-chain incident.

## Claude's Role

Claude là wiki maintainer, chạy bằng routine `llm-wiki-routine-v2.md` (**29th auto-execution, 11th v2 routine execution**):

- **Ingest sources via WebFetch + API probe** — README (1,219 lines) comprehensive
- **Cross-reference với 28 sibling wikis** — primarily T4 peers (markitdown v28 / gws v13 / notebooklm-py v7 / graphify v16 / TrendRadar v19) + Skyvern v24 (Pattern #47 + #48 validation)
- **Phase 4b = T4 6-way comparison + Pattern #47 + #48 refinement + 3 new candidates + Pattern #31 promotion candidate**
- **Beginner angle** — Python developer + RAG/agent workflow; Storm Bear Scrum research + corpus extension

**Prime directive:** Outcome = wiki + T4 extends to N=6 + Pattern #47 + #48 refinement (distinguishing vision vs DOM + proprietary vs open-source) + 3 new candidates + Pattern #31 3rd data point noted.

## Process — routine `llm-wiki-routine-v2.md`

7 phases. 11th v2 routine execution. Phase 4b = T4 6-way + pattern refinements + Pattern #31 pending promotion evidence.

## Key People

- **unclecode** — solo author, NLP researcher background (grad school), Amstrad childhood
- **Cross-project:** 28 sibling wikis. This is 29th = T4 N=6 extension + solo-enterprise-scale 3rd data point.

## Folder Structure

```
crawl4ai - Beginner Analysis/
├── CLAUDE.md
├── 00 Sources/
├── 01 Analysis/
├── 02 Wiki/
├── 03 Published/
├── 04 Reviews/
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ VN + 13-section format
- **Cross-reference 28 siblings MANDATORY** — especially T4 peers + Skyvern v24 (browser-automation peer)
- **Pattern Library direct update** — 3 new candidates + Pattern #47 + #48 refinement + Pattern #31 3rd data point

## Current Status

> **Last updated:** 2026-04-22
> **Status:** 🟡 Routine v2 auto-execute IN PROGRESS — 29th LLM Wiki, 11th v2 execution, T4 N=6 extension, solo-enterprise-scale 3rd data point

### Expected milestones

- [x] Phase 0 Pre-flight (probe + guard 1.07:1 not blocking at 2:1 threshold)
- [x] Phase 1 Scaffold
- [ ] Phase 2 Source ingestion (3 clusters)
- [ ] Phase 3 Entity pages (4)
- [ ] Phase 4a Beginner guide
- [ ] Phase 4b T4 6-way + Pattern #47/#48 refinement + 3 new candidates
- [ ] Phase 5 Iteration log v29
- [ ] Phase 6 Vault updates
