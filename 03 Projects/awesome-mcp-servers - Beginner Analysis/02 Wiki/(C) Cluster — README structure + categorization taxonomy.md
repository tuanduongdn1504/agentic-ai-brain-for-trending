# (C) Cluster — README structure + categorization taxonomy

**Sources summarized:**
- `README.md` (EN primary, ~45 KB markdown) — verbatim README fetched 2026-04-22 via `raw.githubusercontent.com/punkpeye/awesome-mcp-servers/main/README.md`
- Repository metadata via GitHub API (`api.github.com/repos/punkpeye/awesome-mcp-servers`) fetched 2026-04-22

**Scope:** This cluster summarizes HOW `awesome-mcp-servers` is organized as a directory — sections, taxonomy, legend system, server entry format, and 7-language i18n structure. Governance and community dynamics are covered in the sibling cluster `(C) Cluster — Aggregator governance + contribution + community.md`. Ecosystem / companion projects covered in `(C) Cluster — punkpeye ecosystem + companion projects.md`.

## 1. Repository metadata (API snapshot 2026-04-22)

| Field | Value |
|-------|-------|
| Full name | `punkpeye/awesome-mcp-servers` |
| Description | "A collection of MCP servers." |
| Stars | **85,323** (#4 in Storm Bear corpus: behind build-your-own-x 491K outside-scope / system-prompts-leaks 135K outside-scope / markitdown 114K / spec-kit 89.2K) |
| Forks | 9,365 (11.0% ratio) |
| License | MIT |
| Primary language | None (markdown-only content) |
| Default branch | `main` |
| Created | 2024-11-30 (~17 months old) |
| Pushed | 2026-04-15 |
| Size | 16,075 KB |
| Open issues | 839 |
| Subscribers (true watchers) | 6 |
| Topics | `ai`, `mcp` |
| Homepage | https://glama.ai/mcp/servers |

**Scale-growth rate:** ~5,000 stars/month sustained over 17 months. Distinct from awesome-design-md v25 extreme-velocity (9K stars/day over 20 days) — this is **sustained-community-viral**, not spike.

## 2. Top-level section taxonomy (in README order)

```
1. Language selection badges (7 languages)
2. Top-of-README references
   - "The State of MCP in 2025" report link (glama.ai blog)
   - "Awesome MCP Servers" web directory link (glama.ai/mcp/servers)
3. What is MCP? (1-paragraph definition)
4. Clients (pointer to companion repo + Glama Chat)
5. Tutorials (2 items: MCP Quickstart + Claude Desktop/SQLite video)
6. Community (Discord + r/mcp Reddit)
7. Legend (15-badge taxonomy — see §4)
8. Server Implementations (50+ categories — see §3)
```

## 3. Server Implementations — full 50+ category list (README order)

Alphabetical within README. Each category hosts a flat markdown list of server entries.

| # | Category | Indicative scope |
|---|----------|-----------------|
| 1 | Aggregators | Meta-servers that bundle multiple MCP servers (e.g., `1mcp/agent`, `Aganium/agenium`) |
| 2 | Aerospace | Space/aviation data (flight tracking, satellite) |
| 3 | Art & Culture | Museum APIs, cultural datasets |
| 4 | Architecture & Design | CAD tools, design-system bridges |
| 5 | Biology/Medicine | Bio databases, medical knowledge |
| 6 | Browser Automation | Playwright/Puppeteer/crawl4ai-adjacent (crawl4ai v29 is corpus peer) |
| 7 | Cloud Platforms | AWS/GCP/Azure management |
| 8 | Code Execution | Sandboxed code runners |
| 9 | Coding Agents | MCP servers that wrap coding agents (overlaps corpus T1 wikis) |
| 10 | Command Line | Shell/terminal bridges |
| 11 | Communication | Slack/Discord/Teams (Storm Bear pilot relevant — Scrum-ceremony integrations) |
| 12 | Customer Data Platforms | Segment/mParticle |
| 13 | Databases | Postgres/MySQL/Redis/vector-DBs (broad; high Storm Bear relevance for corpus queries) |
| 14 | Data Platforms | Snowflake/Databricks |
| 15 | Delivery | Shipping/logistics |
| 16 | Developer Tools | Generic dev-tool bridges |
| 17 | Data Science | Jupyter/pandas/R |
| 18 | Data Visualization | Chart/plot generators |
| 19 | Embedded Systems | IoT/microcontroller (per 📟 legend) |
| 20 | Education | LMS/course platform bridges |
| 21 | E-Commerce | Shopify/WooCommerce |
| 22 | Environment & Nature | Weather/climate data |
| 23 | File Systems | Local FS + cloud storage (high Storm Bear relevance — vault operations) |
| 24 | Finance & Fintech | Bank APIs, accounting |
| 25 | Gaming | Game-data APIs |
| 26 | Home Automation | Smart home bridges |
| 27 | Knowledge & Memory | Vector stores, knowledge graphs (Storm Bear corpus relevance) |
| 28 | Legal | Case law, contract DBs |
| 29 | Location Services | Maps/geocoding |
| 30 | Marketing | Analytics/campaign platforms |
| 31 | Monitoring | Datadog/Prometheus/Sentry |
| 32 | Multimedia | Audio/video processing |
| 33 | OS Automation | AppleScript/Windows automation |
| 34 | Product Management | **Jira / Linear / Asana (HIGH Storm Bear pilot relevance — Scrum metrics ingestion)** |
| 35 | Real Estate | Property data |
| 36 | Research | ArXiv/PubMed/Semantic Scholar |
| 37 | Search & Data Extraction | Google Search/Bing/Brave Search |
| 38 | Security | SIEM/vuln DBs |
| 39 | Social Media | Twitter/Reddit/LinkedIn |
| 40 | Sports | Sports data APIs |
| 41 | Support & Service Management | Zendesk/Intercom |
| 42 | Translation | Translation APIs |
| 43 | Text-to-Speech | TTS services (fish-speech v20 peer domain) |
| 44 | Travel & Transportation | Flights/transit |
| 45 | Version Control | **GitHub / GitLab / Bitbucket (HIGH Storm Bear pilot relevance — team activity metrics)** |
| 46 | Workplace & Productivity | Google Workspace / Microsoft 365 / Notion (gws v13 peer — corpus cross-link) |
| 47 | Other Tools | Catch-all |

**Estimated total servers:** ~1,200 entries across all categories. Aggregators alone has 60+. Browser Automation has 50+. Major utility categories (Databases, Communication, Version Control, Filesystem) each host 50-200+ entries. Long-tail categories (Sports, Aerospace, Legal) have 5-20 entries.

**Category organization observations:**
- **Alphabetical within README** (CONTRIBUTING enforces this — see governance cluster)
- **No sub-categories** (flat taxonomy; depth 1)
- **Breadth over depth** — preference to add new category vs squeeze into existing. Contrasts with build-your-own-x v8 (29 fixed categories) and awesome-design-md v25 (10 fixed categories).

## 4. Legend taxonomy (4-axis, 15 badges)

The legend system is a corpus-first **multi-axis classification vocabulary** embedded in a content aggregator. Each server entry can carry multiple badges.

### Axis 1: Official status (1 badge)
- 🎖️ — official implementation (vendor-authored)

### Axis 2: Programming language (8 badges)
- 🐍 — Python
- 📇 — TypeScript / JavaScript
- 🏎️ — Go
- 🦀 — Rust
- \#️⃣ — C#
- ☕ — Java
- 🌊 — C / C++
- 💎 — Ruby

### Axis 3: Scope / hosting (3 badges)
- ☁️ — Cloud Service
- 🏠 — Local Service
- 📟 — Embedded Systems

### Axis 4: Operating system (3 badges)
- 🍎 — macOS
- 🪟 — Windows
- 🐧 — Linux

**Novelty:** No sibling awesome-list-genre corpus wiki (build-your-own-x v8, awesome-design-md v25) has this depth of classification vocabulary. `awesome-mcp-servers` **is actively a taxonomy authority** for MCP server discoverability, not just a flat list.

## 5. Server entry format (from Aggregators sample)

Verified verbatim from README:

```
- [1mcp/agent](https://github.com/1mcp/agent) - A unified Model Context Protocol server implementation that aggregates multiple MCP servers into one.
- [tadas-github/a2asearch-mcp](https://github.com/tadas-github/a2asearch-mcp) - MCP server to search 4,800+ MCP servers, AI agents, CLI tools and agent skills.
- [Aganium/agenium](https://github.com/Aganium/agenium) - Bridge any MCP server to the agent:// network — DNS-like identity, discovery, and trust for AI agents.
```

**Standard per-entry format:**
```
- [{owner/repo}]({url}) {emoji-legends} - {one-line description}
```

**Emoji legends** are optional and placed between the link and the dash (observed usage varies; many entries have 0 legends, some have 3-5).

**Corpus-first observation:** Even within the aggregators category, `tadas-github/a2asearch-mcp` describes **"search 4,800+ MCP servers"** — suggesting the broader MCP-server universe is ~4x larger than what makes this curated list. `awesome-mcp-servers` is the **curated-subset directory**, not the full registry. This is a signal about curation discipline — gate exists.

## 6. i18n structure — 7-language README variants

From verbatim README top-of-file:

```markdown
[![ไทย](https://img.shields.io/badge/Thai-Click-blue)](README-th.md)
[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
```

**7 languages total:** Thai, English, Traditional Chinese, Simplified Chinese, Japanese, Korean, Brazilian Portuguese.

**Corpus comparison:**
| Wiki | i18n count | Languages |
|------|-----------|-----------|
| fish-speech v20 | 7 | EN/zh-CN/zh-TW/JA/KO/PT/RU |
| oh-my-claudecode v27 | 7 | EN/KO/ZH/JA/ES/VI/PT |
| LlamaFactory v22 | 7 | EN/zh-CN/JA/KO/RU/ES/FR |
| **awesome-mcp-servers v31** | **7** | **Thai/EN/zh-TW/zh-CN/JA/KO/PT-BR** |

**Ties largest i18n tier in corpus at 7 languages.** Unique inclusion: **Thai** — first Thai-README in corpus (Fiegel is Miami-based but maintains Thai — signal of Fiegel's personal network OR Thai MCP community demand).

## 7. References in the README to external resources

**Glama ecosystem (commercial companion of Fiegel):**
- `glama.ai/mcp/servers` — web directory synced with this repo
- `glama.ai/mcp/clients` — web directory synced with `awesome-mcp-clients` sibling
- `glama.ai/chat` — Glama Chat multi-modal AI client with MCP support
- `glama.ai/blog/2025-12-07-the-state-of-mcp-in-2025` — State-of-MCP report (**first corpus reference to an MCP-ecosystem-state industry report**)

**Upstream protocol:**
- `modelcontextprotocol.io` — Anthropic-maintained MCP spec site

**Sibling repos (same owner):**
- `punkpeye/awesome-mcp-clients` — client directory (6.4K stars)

**Community:**
- Discord server (invite link in README)
- r/mcp subreddit (Pattern #18 Western-community-platform — Discord + Reddit combo recurring in corpus)

## 8. Top-of-README positioning statement

Verbatim from §"What is MCP?":

> "MCP is an open protocol that enables AI models to securely interact with local and remote resources through standardized server implementations. This list focuses on production-ready and experimental MCP servers that extend AI capabilities through file access, database connections, API integrations, and other contextual services."

**Two key positioning claims:**
1. **"production-ready and experimental"** — curation spans maturity spectrum; not "only production" gate
2. **"extend AI capabilities"** — frames MCP as capability-extension (verb-oriented), not infrastructure (noun-oriented)

## 9. Relevance to Storm Bear (summary)

The categorization taxonomy is directly actionable for Storm Bear:
- **Categories with highest Scrum-coach utility:** Product Management / Version Control / Communication / Workplace & Productivity / Knowledge & Memory / Databases / File Systems
- **Categories to ignore for Storm Bear:** Gaming / Aerospace / Sports / Automotive-adjacent
- **Aggregators category** lets Storm Bear bundle 5-10 MCP servers behind one runtime endpoint — reduces config complexity
- **Legend badges** let Storm Bear filter: Python-only ☁️+🏠 preferences for VN cloud-infrastructure compatibility

See cross-wiki entity `(C) MCP Server Directory Structure + Categorization + Scale.md` and beginner guide for actionable Storm Bear subset.

## 10. Cross-references

- **Aggregator peers:** [[03 Projects/build-your-own-x - Beginner Analysis/02 Wiki/(C) index.md|build-your-own-x v8]] (human-education-aggregator) + [[03 Projects/awesome-design-md - Beginner Analysis/02 Wiki/(C) index.md|awesome-design-md v25]] (design-template-aggregator-for-AI-agents)
- **MCP-consumer wikis:** [[03 Projects/goclaw - Beginner Analysis/|goclaw v4]] / [[03 Projects/multica - Beginner Analysis/|multica v15]] / [[03 Projects/graphify - Beginner Analysis/|graphify v16]] / [[03 Projects/spec-kit - Beginner Analysis/|spec-kit v17]] / [[03 Projects/TrendRadar - Beginner Analysis/|TrendRadar v19]] / [[03 Projects/OpenHands - Beginner Analysis/|OpenHands v30]]
- **i18n peers:** fish-speech v20 / oh-my-claudecode v27 / LlamaFactory v22
- **Ecosystem-individual peer:** VoltAgent v25 awesome-design-md (commercial-funnel + parent framework)

---

_Part of Storm Bear LLM Wiki — 31st wiki. Written by Claude (C). Verified 2026-04-22._
