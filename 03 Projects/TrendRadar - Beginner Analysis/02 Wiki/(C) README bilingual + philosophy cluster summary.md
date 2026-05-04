# (C) README bilingual + philosophy cluster summary — TrendRadar

> **Sources:** README.md + README-EN.md + README-MCP-FAQ.md (bilingual CN+EN)
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

Positioning, philosophy, feature versioning. Bilingual CN-primary + EN translation. Together they reveal TrendRadar's distinct operator-oriented ethic.

## 2. Core positioning (verbatim bilingual)

### CN (primary)

> *"告别无效刷屏，只看真正关心的新闻资讯"*
> (Stop meaningless scrolling, see only news you truly care about)

### EN

> "⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts"

### Mission expansion

> *"本项目以轻量，易部署为目标"*
> (Lightweight and easy deployment as core goal)

## 3. Escape-algorithmic-control philosophy (corpus-first)

### Key philosophical positions

1. **Consent-based information** — user explicitly selects keywords + platforms (not algorithmic push)
2. **Escape algorithmic control** — *"don't let algorithms dictate your information flow"*
3. **Activity-based resource fairness** — 7-day check-in prevents silent resource waste
4. **Privacy-first** — supports self-hosted ntfy/Bark servers
5. **Modular extensibility** — enable/disable features via simple YAML toggles

### 7-day check-in governance (verbatim)

> *"7 天都忘了签到，或许这些资讯对你来说并非刚需。适时的暂停，能帮你从信息流中抽离，给大脑留出喘息的空间。"*
> 
> (If you forget to check in for 7 days, perhaps these news items aren't essential. Timely pauses help extract from information flow, giving your brain breathing space.)

**Novel in corpus:** Engagement-throttling-as-feature. Most corpus frameworks maximize usage; TrendRadar explicitly limits it.

### Philosophical corpus comparison

| Framework | Philosophy |
|-----------|-----------|
| BMAD v11 | *"Human Amplification, Not Replacement"* |
| paperclip v14 | *"Zero-human companies"* |
| multica v15 | *"Your next 10 hires won't be human"* |
| spec-kit v17 | Anti-"vibe coding" |
| agency-agents v18 | Personality-driven specialists |
| **TrendRadar v19** | **Escape algorithmic control + consent-based + engagement-throttle** |

**Unique corpus contribution:** anti-attention-economy ethic. Distinct from autonomy-framing-spectrum (Pattern #13).

## 4. Feature versioning (mature project with clear cadence)

### 2025 versions

- **v2.0.0 (2025/07/27):** Three push modes (daily/current/incremental)
- **v3.0.0 (2025/10/20):** MCP (Model Context Protocol) AI analysis server
- **v3.5.0 (2025/12/03):** Multi-account push support
- **v4.0.0 (2025/12/13):** Multi-storage backend (SQLite + S3-compatible)
- **v4.5.0 (2025/12/30):** RSS/Atom subscription source

### 2026 versions (rapid iteration)

- **v4.6.0 (2026/01/01):** RSS HTML display
- **v4.7.0 (2026/01/02):** Regex expression + display name aliases
- **v5.0.0 (2026/01/10):** Five-region content restructuring + AI analysis embedding
- **v5.2.0 (2026/01/17):** AI multi-language translation
- **v5.3.0 (2026/01/19):** LiteLLM migration (unified AI interface)
- **v5.4.0 (2026/01/23):** Independent AI analysis mode control
- **v5.5.0 (2026/01/28):** Visual configuration editor
- **v6.0.0 (2026/02/09):** Unified scheduling system + timeline.yaml + 5 preset templates
- **v6.5.0 (2026/03/12):** AI intelligent news filtering (natural language interests)
- **v6.6.0 (2026/03/28):** HTML report enhancements + dark mode + keyboard shortcuts
- **v6.6.1 (current):** Minor fixes

**Velocity:** ~15 minor versions across 3 months early 2026. **Very active project.**

## 5. Target users (verbatim)

From README:
> "Investors, self-media creators, corporate PR, average users interested in current events"

**Breakdown:**
- **Investors** — financial news monitoring (Wall Street News CN + Cailian)
- **Self-media creators** — content inspiration from trending topics
- **Corporate PR** — brand mention monitoring across platforms
- **General users** — curated news without doom-scrolling

## 6. Bilingual coverage (CN-primary + EN)

### Files present

| File | Language | Purpose |
|------|----------|---------|
| README.md | CN | Primary docs |
| README-EN.md | EN | English translation |
| README-MCP-FAQ.md | CN | MCP questions |
| README-MCP-FAQ-EN.md | EN | MCP questions EN |

### Corpus bilingual comparison

- deer-flow v9: zh-CN README (partial)
- multica v15: zh-CN README (translation quality mixed)
- graphify v16: CJK-trio (en + ja + ko + zh-CN)
- **TrendRadar v19: bilingual CN/EN at primary docs + MCP-FAQ**

TrendRadar has **bilingual-parallel strategy** — both languages are first-class, not primary/secondary split.

## 7. GPL-3.0 license — corpus-first copyleft

### License choice context

Prior corpus licenses:
- MIT: ECC, Superpowers, gstack, GSD, BMAD, multica, paperclip, graphify, spec-kit, agency-agents, + deer-flow, autoresearch
- Apache-2.0: gws (v13 Google corporate)
- ISC: codymaster (v12 VN solo)
- **GPL-3.0: TrendRadar (v19 first)**

### Why GPL-3.0?

GPL-3.0 is **strong copyleft** — derivative works must be GPL. Implications:
- Commercial forks must release source
- Prevents closed-source commercialization
- Positions TrendRadar as **community-preservation commitment**
- Consistent with "escape algorithmic control" ethic — won't become another ad-tech-aggregator

**Pattern candidate #29: GPL-3.0 in agent-space** — first corpus data point. May remain rare-but-distinctive like Pattern #14 (alignment-theory in paperclip).

## 8. Feature summary (non-versioned)

### News aggregation core

- 11 CN platforms (native support)
- RSS/Atom feeds (v4.5.0+)
- newsnow API backend (extensible)

### AI layer

- LiteLLM (100+ providers via unified interface)
- AI analysis + translation + filtering
- Natural language interest descriptions (`ai_interests.txt`)
- Customizable prompts (`ai_analysis_prompt.txt`, `ai_translation_prompt.txt`)

### Push layer

- 9 channels
- 3 modes (daily / current / incremental)
- Multi-account support (semicolon-separated URLs)

### MCP integration

- 21+ MCP tools across 5 categories
- 4 MCP Resources (platforms, rss-feeds, dates, keywords)
- Separate Docker image (trendradar-mcp)

### Deployment

- pip local
- Docker (dual image)
- GitHub Actions scheduled (cron)
- GitHub Pages HTML output

### Storage

- Local SQLite
- S3-compatible cloud
- Configurable via config.yaml

## 9. Scrum/enterprise applicability signals

### Positive signals

- **Corporate PR** explicitly named target user
- **Multi-account push** — team-level delivery
- **S3 storage** — enterprise-ready data persistence
- **Timeline scheduling** — meeting rhythms (daily/weekly sprint cadences)
- **Keyword filtering** — industry-specific monitoring

### Negative signals

- **GPL-3.0** — enterprise legal concern for derivatives
- **CN platforms primary** — VN/US enterprises may not need
- **Solo maintainer** — bus-factor at 52.1K
- **No formal SLA** — community-scale support

**Net:** useful for CN-market enterprises / VN with CN data needs (e.g., trading firms, import/export, CN-market research).

## 10. Edges + philosophical tensions

### Consent-based vs AI-driven

Framework claims "escape algorithmic control" but uses AI for filtering + analysis. Tension:
- User sets keywords → AI matches → algorithm decides what's relevant
- Is this really consent, or delegation to a "better" algorithm?
- **Resolution:** TrendRadar argues user-owned configuration = consent, vs opaque platform algorithms

### 7-day check-in ethic vs scale

52.1K users × 7-day check-in = massive enforcement burden. Does it actually prevent waste or just create friction?

### Multi-push channel complexity

9 push channels = 9 integration points to maintain. Solo maintainer at scale.

## 11. Corpus-first observations

- **First GPL-3.0** in corpus
- **First LiteLLM 100+ provider abstraction** (Pattern #28 candidate)
- **First "escape algorithmic control" philosophy**
- **First engagement-throttling-as-feature** (7-day check-in)
- **First bilingual-parallel CN+EN at primary docs**
- **First 11-CN-platform bridge** in corpus
- **First dual-Docker-image deployment** (separated crawler + MCP service)

## 12. Cross-references

- [[(C) AI architecture + LiteLLM + 11 Platforms cluster summary]] — technical substrate
- [[(C) MCP Server + 21 Tools + Docker deployment cluster summary]] — distribution + agent integration
- [[(C) Multi-Platform News Aggregation + AI Analysis Layer]] (entity)

## 13. Open questions

- Q3: Why GPL-3.0 specifically? (copyleft ethic documented but not formally stated)
- Q5: 7-day check-in rationale — solo rate-limit or philosophical?
- Q10: User demographics — CN vs international?
