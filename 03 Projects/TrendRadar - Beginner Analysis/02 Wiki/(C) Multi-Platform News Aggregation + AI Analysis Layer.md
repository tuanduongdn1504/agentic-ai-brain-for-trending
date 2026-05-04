# (C) Multi-Platform News Aggregation + AI Analysis Layer

> **Type:** Entity — core product
> **Parent:** [[(C) index]]
> **Sources:** [[(C) README bilingual + philosophy cluster summary]] §4-§5, [[(C) AI architecture + LiteLLM + 11 Platforms cluster summary]] §2-§6
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

TrendRadar's core product is **multi-platform news aggregation + AI analysis pipeline** — pulling from 11 CN news platforms + RSS feeds, filtering via natural-language interest configuration, analyzing via LiteLLM 100+ provider abstraction, and pushing to 9 channels in 3 modes (daily/current/incremental). The architecture is **consent-based information flow** (user selects keywords + platforms) in contrast to algorithmic push feeds. The AI layer uses LiteLLM — corpus-first multi-provider abstraction — enabling DeepSeek (default, cost-effective) / OpenAI / Gemini / Anthropic / self-hosted Ollama with fallback chains.

## 2. Key claims

1. **11 CN news platforms** — first CN-platform-focused bridge in corpus
2. **LiteLLM 100+ providers** — corpus-first multi-provider abstraction (Pattern #28 candidate)
3. **3 AI modes** — analysis + translation + filtering
4. **3 push modes** — daily / current / incremental (zero duplicates)
5. **9 push channels** — broadest multi-push in corpus
6. **Consent-based information flow** — user-selected keywords + platforms
7. **Natural-language interests** — `ai_interests.txt` config novelty
8. **Escape-algorithmic-control ethic** — anti-attention-economy stance

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 11 platforms | README verbatim | High |
| LiteLLM 100+ providers | README AI section | High |
| 3 push modes | README verbatim | High |
| 9 push channels | README verbatim | High |
| Natural-language interests | README v6.5.0 changelog | High |
| Escape-algorithm ethic | README philosophy section verbatim | High |

## 4. 11 CN news platforms

Bilingual full table:

| # | CN name | EN translation | Category |
|---|---------|---------------|----------|
| 1 | 知乎 | Zhihu | Q&A discussion |
| 2 | 抖音 | Douyin | Short video |
| 3 | 哔哩哔哩热搜 | Bilibili | Video/culture |
| 4 | 华尔街见闻 | Wall Street News CN | Financial |
| 5 | 贴吧 | Tieba | Community forums |
| 6 | 百度热搜 | Baidu Hot Search | General search |
| 7 | 财联社热门 | Cailian News | Financial breaking |
| 8 | 澎湃新闻 | The Paper | Journalism |
| 9 | 凤凰网 | Phoenix News | International |
| 10 | 今日头条 | Toutiao | AI-curated |
| 11 | 微博 | Weibo | Social/celebrity |

### Extensibility

`newsnow` API backend allows adding platforms beyond core 11. Configuration via YAML (no code changes).

### Corpus comparison — T4 bridge targets

| Framework | Bridge target | Source count |
|-----------|---------------|--------------|
| notebooklm-py v7 | NotebookLM | 1 service |
| gws v13 | Google Workspace | 11+ services (corporate) |
| graphify v16 | Local filesystem | Any content (solo) |
| **TrendRadar v19** | **CN news platforms** | **11 platforms (solo)** |

**TrendRadar is T4d (new quadrant):** solo-broad-external-platforms.

## 5. AI analysis pipeline

### 3-stage processing

```
Stage 1: AI Filter
  Input: news item + ai_interests.txt
  Output: relevance score + tags

Stage 2: AI Translation (optional)
  Input: filtered news + target language
  Output: translated content

Stage 3: AI Analysis
  Input: filtered news batch
  Output: sentiment + trend analysis + summary
```

### LiteLLM unified interface

```yaml
# Primary provider
model: "deepseek/deepseek-chat"

# Fallback chain
fallback_models:
  - "openai/gpt-4o-mini"
  - "gemini/gemini-1.5-flash"

# Optional: custom base URL (for self-hosted)
api_base: "http://localhost:11434"  # Ollama
```

### 100+ provider list (selective)

- DeepSeek (default — cost-effective CN provider)
- OpenAI (GPT-4o, GPT-4o-mini)
- Google Gemini (1.5 flash, 1.5 pro)
- Anthropic Claude (3.5 Sonnet)
- Self-hosted Ollama
- OpenAI-compatible APIs (OneAPI aggregators)

### Pattern #28 candidate

TrendRadar = first corpus framework with LiteLLM 100+ provider abstraction.

**Prediction:** More agent-frameworks adopt provider-abstraction layers (LiteLLM, LangChain ChatModels, OpenRouter) to decouple from specific vendors.

## 6. Push routing — 9 channels × 3 modes = 27 combinations

### Push modes

| Mode | Description | Use case |
|------|-------------|----------|
| **daily** | Daily summary aggregation | End-of-day digest |
| **current** | Real-time ranked hot topics | Breaking news monitoring |
| **incremental** | New items only (zero duplicates) | Continuous feed |

### Push channels

CN-ecosystem (3):
1. WeChat Work (企业微信)
2. Feishu/Lark (飞书)
3. DingTalk (钉钉)

International (6):
4. Telegram
5. Email (SMTP auto-detection 10+ providers)
6. ntfy (privacy-focused)
7. Bark (iOS native)
8. Slack
9. Generic webhook (Discord, Matrix, IFTTT)

### Multi-account support

All channels accept semicolon-separated URLs:
```yaml
WECOM_WEBHOOK_URL: "url1;url2;url3"
```

## 7. Natural-language interests (v6.5.0)

### User configuration

`ai_interests.txt` example:
```
I care about:
- AI agent frameworks
- Python web frameworks (FastAPI, Django, Flask)
- Chinese tech startup news
- Open-source LLM developments

I'm NOT interested in:
- Celebrity gossip
- Sports news
- Cryptocurrency speculation
```

### AI processing

1. Extract tags from natural language
2. Score each news item against tags
3. Apply negative-filter tags as exclusions
4. Rank news by relevance score
5. Route above-threshold to push channels

### Corpus novelty

**First natural-language-interest-as-filter** in Storm Bear corpus. Contrast:
- multica v15: Linear-style explicit keyword filtering
- graphify v16: structural graph queries
- spec-kit v17: constitution-as-governance (different purpose)

**Usability signal:** natural language lowers barrier vs regex/query languages.

## 8. Consent-based information flow (philosophy)

### Core claim

> *"Don't let algorithms dictate your information flow."*

### Mechanism

Instead of platform algorithms deciding what user sees:
1. User explicitly selects 11 platforms to monitor
2. User defines keyword filters (regex supported)
3. User writes natural-language interests (ai_interests.txt)
4. User sets push schedule (timeline.yaml)

**User-owned configuration = consent.**

### Tension with AI filtering

Critic's view: TrendRadar still uses AI to filter/score news → AI is algorithm. Is this consent?

**TrendRadar's implicit answer:**
- User-owned config = transparent algorithm
- Platform algorithms = opaque black-box
- Transparency + user control = consent, even if AI-mediated

**Philosophical stance:** Consent-via-ownership vs algorithm-agnosticism.

## 9. Worked example — CN-market investor workflow

### Scenario

VN investor monitoring CN tech markets for trading opportunities.

### Setup

```yaml
# config.yaml
platforms:
  - wall_street_cn   # Wall Street News CN
  - cailian          # Cailian financial news
  - zhihu            # Zhihu discussions
  - toutiao          # Toutiao curation

push_modes:
  - daily            # End-of-day summary
  - incremental      # Real-time breaking
```

```
# ai_interests.txt
I care about:
- Chinese tech company earnings
- US-China regulatory news
- Consumer tech product launches in CN
- EV market CN
- AI startup funding CN

I'm NOT interested in:
- Celebrity scandals
- Sports news
- Domestic politics (non-economic)
```

```yaml
# timeline.yaml
morning_brief:
  time: "07:00"
  platforms: [wall_street_cn, cailian]
  mode: daily
  
market_pulse:
  time: "every_2_hours"
  platforms: [cailian, toutiao]
  mode: incremental

evening_analysis:
  time: "18:00"
  all_platforms: true
  mode: daily
  ai_analysis: true  # Sentiment + trend
```

### Outcome

- Morning: yesterday's financial summary (08:00 JST equivalent)
- Every 2h: breaking news filtered by AI
- Evening: full-day analysis with sentiment
- Pushed to WeChat Work (corporate group) + Feishu (team)

## 10. Related concepts

- [[(C) 21+ MCP Tools + Agent Ecosystem Integration]] — agent-consumer layer
- [[(C) Solo-at-52K CN Ecosystem + Pattern 18 Regional Hypothesis]] — organizational context
- [[(C) T4 4-way + Pattern 9 Resolution D + 3 New Candidates + Storm Bear]] — tier meta

## 11. Cross-project comparison

### vs gws v13 (T4 corporate-broad)

| Aspect | gws v13 | TrendRadar v19 |
|--------|---------|----------------|
| Bridge target | Google Workspace | CN news platforms |
| Provider | Google official | sansan0 solo |
| Data type | Productivity | Trend/news |
| AI layer | Model Armor sanitization | LiteLLM 100+ providers |
| Scale | 25K | 52.1K (2×) |

### vs graphify v16 (T4 solo-broad-local)

| Aspect | graphify v16 | TrendRadar v19 |
|--------|--------------|----------------|
| Bridge target | Local filesystem | 11 CN news platforms |
| Content type | Extraction from files | Aggregation from APIs |
| Scope | Internal | External |
| Output | Knowledge graph | News push feed |
| Scale | 30K | 52.1K |

### vs notebooklm-py v7 (T4 solo-narrow)

| Aspect | notebooklm-py v7 | TrendRadar v19 |
|--------|------------------|----------------|
| Bridge target | NotebookLM single | 11 platforms |
| Scope | Narrow | Broad |
| Use case | Programmatic NotebookLM | News monitoring |
| Scale | ~300 | 52.1K (170×) |

## 12. Edges + failure modes

### Data source edges

- **CN platform geo-restrictions** — non-CN IPs may fail
- **Platform API changes** — 11 platforms × different policies
- **newsnow upstream** — single dependency

### AI layer edges

- **LiteLLM provider deprecation** — 100+ providers each drift
- **DeepSeek CN dependency** — geopolitical / service risk
- **Prompt injection** — user-editable ai_interests.txt
- **Cost escalation** — hourly × all modes × all users

### Push layer edges

- **Channel credential rotation** — 9 channels × token management
- **Rate limiting per channel** — WeChat Work daily limits
- **Multi-account misrouting** — semicolon URL parsing

## 13. References

- README.md + README-EN.md verbatim
- config file documentation
- Pattern #28 candidate formalization (PATTERN_LIBRARY.md)
- Parent: [[(C) index]]
- Cross-wiki: `../../googleworkspace-cli - Beginner Analysis/` (T4 peer)
- Cross-wiki: `../../graphify - Beginner Analysis/` (T4 peer)
- Cross-wiki: `../../notebooklm-py - Beginner Analysis/` (T4 peer)
