# (C) TrendRadar — Hướng dẫn cho người mới / Beginner's Guide

> **Repo:** [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) — 52.1K ⭐, 23.3K forks, **GPL-3.0**
> **Tagline:** *"⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts"*
> **Philosophy:** *"告别无效刷屏，只看真正关心的新闻资讯"* (Escape algorithmic scrolling, see only news you care about)
> **Wiki:** `(C) index` — 19th LLM Wiki in Storm Bear corpus
> **Audience:** VN developers + Scrum coaches + CN-market-exposed businesses

---

## Part 1 — TrendRadar là gì? / What is TrendRadar?

### 🇻🇳 Tiếng Việt

**TrendRadar** là hệ thống **aggregate + AI-analyze + push** tin tức từ **11 CN platforms** (Zhihu, Weibo, Baidu, Bilibili, Tencent News, Phoenix, Toutiao, etc.) + RSS feeds. Output được gửi qua **9 channels** (WeChat Work, Feishu, DingTalk, Telegram, Email, ntfy, Bark, Slack, generic webhook).

**Triết lý cốt lõi:** Thay vì để algorithm quyết định bạn xem gì, TrendRadar cho phép bạn **chọn keywords + platforms + interests** (consent-based). AI lọc + phân tích + dịch + tóm tắt → push tới bạn.

**Điểm nổi bật:**
- **52.1K stars** (#4 trong corpus) — solo maintainer CN (sansan0)
- **GPL-3.0** — first copyleft in Storm Bear corpus
- **LiteLLM 100+ AI providers** (DeepSeek default, + OpenAI, Gemini, Anthropic, self-hosted Ollama)
- **21+ MCP tools** for agent integration (Claude Desktop, Cursor, ChatGPT Desktop, Cherry Studio)
- **Bilingual CN+EN** docs (README + README-EN)
- **GitHub Actions cron** = primary deployment (hourly default)
- **Dual Docker images** (trendradar + trendradar-mcp separated)

### 🇬🇧 English

TrendRadar is a multi-platform news aggregation system with AI analysis, multi-channel push, and MCP agent integration. Solo-maintained in CN-ecosystem at 52.1K stars. First GPL-3.0 in Storm Bear corpus. Distinguishes via consent-based information flow vs algorithmic push.

---

## Part 2 — Corpus firsts at v19

| Signal | TrendRadar | Corpus context |
|--------|------------|----------------|
| **First GPL-3.0** | ✅ | Prior: MIT / Apache-2.0 / ISC |
| **First LiteLLM 100+ providers** | ✅ | Pattern #28 candidate |
| **First 11-CN-news-platform bridge** | ✅ | CN-ecosystem focus |
| **First 9-channel multi-push** | ✅ | Broadest push integration |
| **First MCP Resources explicit** | ✅ | 4 Resources (platforms, rss-feeds, dates, keywords) |
| **First dual-Docker separation** | ✅ | crawler + MCP images |
| **First GitHub Actions primary deployment** | ✅ | Hourly cron |
| **First Cherry Studio mention** | ✅ | CN desktop AI app |
| **First Jina AI Reader integration** | ✅ | Ecosystem touchpoint |
| **First engagement-throttle governance** | ✅ | 7-day check-in requirement |
| **First "escape algorithmic control" philosophy** | ✅ | Anti-attention-economy |

---

## Part 3 — Tier placement

**T4 "Agent-as-bridge"** — bridges 11 CN news platforms → agents via MCP.

**T4 4-way comparison (v19 extends v16's 3-way):**

```
                 Narrow        Broad (local)  Broad (external)
Solo       notebooklm-py    graphify v16    TrendRadar v19 🆕
           (NotebookLM)     (local FS 30K)  (CN news 52.1K)
           
Corporate                                   gws v13
                                            (Workspace 25K)
```

**TrendRadar** occupies **4th T4 quadrant** (solo-broad-external-platforms).

→ Pattern #9 Resolution D (multi-axial tier bifurcation) strengthens.

---

## Part 4 — Cài đặt / Installation

### 🇻🇳 3 deployment options

#### Option A: Local Docker (recommended cho VN users)

```bash
# Clone repo
git clone https://github.com/sansan0/TrendRadar.git
cd TrendRadar

# Setup .env với credentials
cp docker/.env.example docker/.env
# Edit docker/.env — add webhook URLs, AI API key, etc.

# Run
docker compose -f docker/docker-compose.yml up -d
```

#### Option B: GitHub Actions (recommended cho persistent cloud)

1. Fork repo
2. Add GitHub Secrets:
   - `FEISHU_WEBHOOK_URL` (hoặc other push channels)
   - `AI_API_KEY` + `AI_PROVIDER` (e.g., "deepseek/deepseek-chat")
   - `S3_BUCKET_NAME`, `S3_ACCESS_KEY_ID`, `S3_SECRET_ACCESS_KEY`, `S3_ENDPOINT_URL`
3. Enable Actions on fork
4. Update `.github/workflows/crawler.yml` cron as needed (default hourly)
5. **Remember:** check in every 7 days để prevent Actions deactivation

#### Option C: pip local

```bash
pip install trendradar  # Hypothetical — verify package name
trendradar init
trendradar run
```

### 🇬🇧 Configuration files

```yaml
# config.yaml
platforms:
  - zhihu
  - weibo
  - baidu_hot
  - bilibili_hot
  # ... up to 11 platforms
  - rss  # RSS feeds

ai:
  provider: "deepseek/deepseek-chat"
  analysis_enabled: true
  translation_enabled: false
  filter_enabled: true
  
push:
  channels:
    - feishu
    - wecom
  modes:
    - daily
    - incremental
```

```
# ai_interests.txt
I care about:
- AI agent frameworks
- Python web development
- CN tech startup news

I'm NOT interested in:
- Celebrity gossip
- Sports
```

```yaml
# timeline.yaml (v6.0.0+)
morning_brief:
  cron: "0 7 * * *"
  platforms: [wall_street_cn, cailian]
  mode: daily
  
hourly_pulse:
  cron: "0 * * * *"
  platforms: all
  mode: incremental
```

---

## Part 5 — Cách dùng / Usage patterns

### 🇻🇳 Pattern A: Personal news digest

1. Setup config.yaml với platforms bạn quan tâm
2. Write ai_interests.txt in natural language
3. Configure 1-2 push channels (e.g., Telegram bot)
4. Run hourly cron
5. Receive AI-filtered + analyzed news summaries

### 🇬🇧 Pattern B: Enterprise monitoring

1. Deploy Docker on company VPS
2. Configure WeChat Work + Feishu push for team groups
3. Setup S3 storage for cross-instance sharing
4. AI analysis mode → sentiment + trend reports
5. Multi-account delivery (各部门 — different teams)

### Pattern C: Agent-consumer

1. Deploy trendradar-mcp Docker image
2. Connect Claude Desktop / Cursor / ChatGPT Desktop via MCP
3. Agent can query via 21+ MCP tools:
   - `get_latest_news`, `analyze_sentiment`, `compare_periods`, etc.
4. Agent synthesizes + presents to user

---

## Part 6 — 11 CN platforms + AI layer

### Platforms

| Platform | CN | Category |
|----------|-----|----------|
| Zhihu | 知乎 | Q&A discussion |
| Douyin | 抖音 | Short video |
| Bilibili | 哔哩哔哩热搜 | Video/culture |
| Wall Street News CN | 华尔街见闻 | Financial |
| Tieba | 贴吧 | Forums |
| Baidu Hot | 百度热搜 | Search trending |
| Cailian | 财联社热门 | Financial breaking |
| The Paper | 澎湃新闻 | Journalism |
| Phoenix News | 凤凰网 | International |
| Toutiao | 今日头条 | AI-curated |
| Weibo | 微博 | Social |

### AI layer via LiteLLM

```yaml
ai:
  model: "deepseek/deepseek-chat"  # Default (cost-effective)
  # Alternatives:
  # model: "openai/gpt-4o-mini"
  # model: "gemini/gemini-1.5-flash"
  # model: "anthropic/claude-3-5-sonnet"
  
  fallback_models:
    - "openai/gpt-4o-mini"
    - "gemini/gemini-1.5-flash"
```

### 3 AI modes

1. **Analysis** — sentiment + trend detection
2. **Translation** — multi-language
3. **Filtering** — natural-language interests via ai_interests.txt

---

## Part 7 — 21+ MCP tools for agents

### 5 categories

**Basic Queries (3):** get_latest_news, get_news_by_date, get_trending_topics

**Intelligent Search (2):** search_news, find_related_news

**Advanced Analysis (6):** analyze_topic_trend, analyze_sentiment, compare_periods, aggregate_news, analyze_data_insights, generate_summary_report

**RSS Queries (3):** get_latest_rss, search_rss, get_rss_feeds_status

**System Management (3+):** get_current_config, get_system_status, resolve_date_range, check_version, read_article (Jina AI Reader)

### 4 MCP Resources

- `platforms`, `rss-feeds`, `available-dates`, `keywords`

### Agent clients supported

- **Claude Desktop** (Anthropic)
- **Cursor** (IDE)
- **ChatGPT Desktop** (OpenAI)
- **Cherry Studio** (CN desktop AI — first corpus mention)

---

## Part 8 — Pattern #18 regional evidence

### 🇻🇳 Lý thú: TrendRadar không dùng OpenClaw/Hermes

Storm Bear corpus đã track OpenClaw (5 wikis) + Hermes (3 wikis) — là emerging agent runtime standards. **TrendRadar không mention cả hai.**

### Giả thuyết (Pattern #18 refinement)

OpenClaw/Hermes có thể là **Western community-platform specific**. CN ecosystem có parallel infrastructure:
- Transport: MCP (universal, both regions)
- Provider abstraction: LiteLLM (universal)
- Runtime ID: Western uses OpenClaw/Hermes; CN uses direct MCP + LiteLLM

### 🇬🇧 Implication

Pattern #18 may be regional. Storm Bear vault's intellectual lineage / framework tracking may be Western-biased. TrendRadar is first corpus data point suggesting parallel CN infrastructure.

---

## Part 9 — Storm Bear relevance (VN operator)

### 🇻🇳 Đánh giá cho Scrum coach

**Relevance level:** 🟡 **Medium-low** — không direct VN market fit; useful for pattern observation.

**Signal points:**
- ❌ **CN-primary** — VN Scrum teams không dùng Zhihu/Weibo daily
- ✅ **Bilingual CN+EN** — team có EN comfort ok
- ❌ **GPL-3.0** — enterprise commercial derivative constraint
- ✅ **Docker deployment** — DevOps-familiar
- ❌ **11 CN news platforms** — VN tech teams không subscribe
- ✅ **21+ MCP tools** — useful for agent integration exploration
- ✅ **LiteLLM** — pattern value (provider abstraction)
- ❌ **Solo maintainer** — bus-factor at 52.1K scale
- ✅ **Hourly cron** — fits sprint rhythm

### When TrendRadar IS relevant for VN

- **Cross-border trade** (VN-CN import/export firms)
- **CN tech market research** (tracking CN trends cho VN users)
- **Agent ecosystem exploration** (MCP + LiteLLM pattern study)
- **CN-VN-facing companies** (e.g., VN branches of CN companies)

### When TrendRadar NOT relevant

- Pure VN-market Scrum teams
- English-only enterprise
- Commercial derivative development (GPL restriction)

### Scrum ceremony mapping

| Ceremony | Use case |
|----------|----------|
| Daily standup | Push: incremental mode breaking news |
| Sprint planning | Query: analyze_topic_trend for relevant topics |
| Sprint review | Report: generate_summary_report with sentiment |
| Retro | Compare: compare_periods (this sprint vs last) |

---

## Part 10 — 4-week learning roadmap

### Week 1: Local deployment

- Day 1-2: Docker setup, run locally
- Day 3-4: Configure 2-3 platforms, 1 push channel
- Day 5-7: Observe output quality, tune ai_interests.txt

### Week 2: AI + filtering

- Day 8-10: Try different LiteLLM providers (DeepSeek vs OpenAI vs Gemini)
- Day 11-12: Refine natural-language interests
- Day 13-14: Setup 3 push modes (daily, current, incremental)

### Week 3: MCP integration

- Day 15-17: Deploy trendradar-mcp Docker
- Day 18-19: Connect Claude Desktop / Cursor / Cherry Studio
- Day 20-21: Test 21+ MCP tools via agent

### Week 4: GitHub Actions production

- Day 22-24: Fork to your GH account, configure Secrets
- Day 25-26: Deploy to Actions, 7-day check-in setup
- Day 27-28: Evaluate fit vs continuing local Docker

---

## Part 11 — Tradeoffs + limitations

### Strengths

- ✅ **52.1K scale** = active community
- ✅ **LiteLLM 100+ providers** = flexibility
- ✅ **21+ MCP tools** = strong agent integration
- ✅ **9 push channels** = broad distribution
- ✅ **Consent-based flow** = user control
- ✅ **Bilingual CN+EN** = international accessible
- ✅ **3 deployment modes** = flexible ops
- ✅ **Active development** = v6.6.1, recent updates
- ✅ **Modular config** = easy customization

### Limitations

- ❌ **Solo bus-factor** at 52.1K scale
- ❌ **CN-platform geo-restrictions** — non-CN IPs may fail
- ❌ **GPL-3.0** — commercial derivative constraint
- ❌ **Hourly AI cost** — can escalate at scale
- ❌ **11 platform maintenance** — upstream changes burden
- ❌ **Docker requires setup** — not zero-config
- ❌ **No SECURITY.md** observed — implicit security
- ❌ **Prompt injection risk** — user-editable ai_interests.txt

---

## Part 12 — References + next action

### Wiki pages

- [[(C) index]]
- [[(C) README bilingual + philosophy cluster summary]]
- [[(C) AI architecture + LiteLLM + 11 Platforms cluster summary]]
- [[(C) MCP Server + 21 Tools + Docker deployment cluster summary]]
- [[(C) Multi-Platform News Aggregation + AI Analysis Layer]]
- [[(C) 21+ MCP Tools + Agent Ecosystem Integration]]
- [[(C) Solo-at-52K CN Ecosystem + Pattern 18 Regional Hypothesis]]
- [[(C) T4 4-way + Pattern 9 Resolution D + 3 New Candidates + Storm Bear]]

### Cross-wiki siblings

- T4 peers: notebooklm-py v7, gws v13, graphify v16 (4-way comparison)
- Solo-scale peers: graphify v16 (30K), agency-agents v18 (82.9K)
- CN-ecosystem peers: deer-flow v9, multica v15
- Pattern #18 contrast: spec-kit v17 (corporate NO OpenClaw), agency-agents v18 (Western-solo YES OpenClaw)

### Official

- Repo: https://github.com/sansan0/TrendRadar
- Docker: wantcat/trendradar + wantcat/trendradar-mcp
- Jina AI Reader: reader.jina.ai
- LiteLLM: github.com/BerriAI/litellm

### 🎯 Suggested next action (Storm Bear)

**Primary:** Still recommend **running graphify on vault** (pending from v16, ~30-60 min + $5-20 Claude API).

**Secondary:** TrendRadar is **pattern observation target more than pilot tool**. Pattern #30 (3-layer ecosystem stratification) warrants 1-2 more data points before strong recommendation.

**If TrendRadar pilot desired:** Use for **CN-market-exposed businesses only**. 4-week roadmap above.

---

**Wiki 19/19 — T4 extended to N=4 (all 4 archetype quadrants) + first GPL-3.0 + 3 new pattern candidates (#28 LiteLLM / #29 GPL-3.0 / #30 3-layer ecosystem) + Pattern #18 regional refinement. Routine `llm-wiki-routine-v2.md` first execution.**
