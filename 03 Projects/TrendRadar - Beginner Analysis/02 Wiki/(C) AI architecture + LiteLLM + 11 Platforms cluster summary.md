# (C) AI architecture + LiteLLM + 11 Platforms cluster summary — TrendRadar

> **Sources:** README AI section + LiteLLM integration details + 11 platform data sources
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

TrendRadar's technical substrate = (a) 11 CN news platform crawlers, (b) AI layer via LiteLLM with 100+ provider abstraction, (c) filtering/analysis/translation pipeline. Together they define the data-to-insight transformation.

## 2. 11 CN news platforms (verbatim)

| # | Platform (CN) | Platform (EN) | Category |
|---|---------------|---------------|----------|
| 1 | 知乎 | Zhihu | Q&A / long-form discussion |
| 2 | 抖音 | Douyin (TikTok CN) | Short video trending |
| 3 | 哔哩哔哩热搜 | Bilibili Hot Search | Video/culture |
| 4 | 华尔街见闻 | Wall Street News CN | Financial |
| 5 | 贴吧 | Tieba/Baidu Tieba | Community forums |
| 6 | 百度热搜 | Baidu Hot Search | General search trending |
| 7 | 财联社热门 | Cailian News | Financial breaking |
| 8 | 澎湃新闻 | The Paper | News journalism |
| 9 | 凤凰网 | Phoenix News | International perspective |
| 10 | 今日头条 | Toutiao | AI-curated news |
| 11 | 微博 | Weibo | Social/celebrity trends |

**Coverage domains:**
- **Social/viral:** Weibo, Douyin, Bilibili (3)
- **Financial:** WSJ CN, Cailian (2)
- **Journalism:** The Paper, Phoenix, Toutiao (3)
- **Q&A:** Zhihu (1)
- **Forums:** Tieba (1)
- **Search:** Baidu Hot Search (1)

### Additional platforms via newsnow API

Extensible — newsnow API backend means TrendRadar can pull from platforms not in core 11 list.

### Corpus context

- **First 11-CN-platform bridge** in Storm Bear corpus
- Contrast with gws v13: 11+ Google Workspace services (different data type — productivity vs trends)
- Contrast with graphify v16: local filesystem (no external platform dependency)
- Contrast with notebooklm-py v7: single NotebookLM service

## 3. LiteLLM — 100+ provider abstraction (Pattern #28 candidate)

### Architecture

TrendRadar doesn't implement AI providers individually. Instead uses **LiteLLM** library — unified interface for 100+ LLM providers.

### Primary providers

| Provider | Model examples | Positioning |
|----------|---------------|-------------|
| **DeepSeek** | `deepseek/deepseek-chat` | **Default, cost-effective** |
| **OpenAI** | `openai/gpt-4o`, `openai/gpt-4o-mini` | Mainstream quality |
| **Google Gemini** | `gemini/gemini-1.5-flash`, `gemini-1.5-pro` | Google ecosystem |
| **Anthropic** | `anthropic/claude-3-5-sonnet` | Premium reasoning |

### Custom deployments

- **Self-hosted Ollama** — local LLM
- **OpenAI-compatible APIs** — any provider mimicking OpenAI
- **OneAPI and similar aggregators** — proxy layers

### Configuration syntax

```yaml
model: "deepseek/deepseek-chat"
fallback_models:
  - "openai/gpt-4o-mini"
  - "gemini/gemini-1.5-flash"
```

### Pattern #28 candidate — Multi-Provider AI Abstraction

> "**Pattern #28 — Multi-Provider AI Abstraction via LiteLLM-style Libraries:** Agent-space frameworks increasingly adopt provider-abstraction layers (LiteLLM, OneAPI, LangChain ChatModels) to decouple framework from specific AI vendor. This enables:
> - User choice of cost/quality tradeoff
> - Vendor-switching without code changes
> - Support for self-hosted models (Ollama)
> - Resilience to provider outages via fallback chains"

**TrendRadar v19 = first corpus observation.** Pattern prediction: more frameworks will adopt as ecosystem matures.

**Distinct from Pattern #18 (runtime standardization):**
- Pattern #18 = agent runtime identifiers (OpenClaw, Hermes) — framework naming conventions
- Pattern #28 = provider abstraction (LiteLLM, OneAPI) — implementation-layer decoupling
- Both are ecosystem-maturity signals but operate at different layers

## 4. AI analysis layer (v5.0.0+)

### Three AI modes

1. **AI Analysis** — auto-generate trend summaries with sentiment analysis
2. **AI Translation** — multi-language translation of news items
3. **AI Smart Filtering** — natural language interest descriptions → tag extraction → relevance scoring

### Configuration files

| File | Purpose |
|------|---------|
| `ai_analysis_prompt.txt` | Analyst role definition + output format |
| `ai_translation_prompt.txt` | Translation style customization |
| `ai_interests.txt` | Natural language interest descriptions for filtering |
| `ai_filter/` | Internal AI filtering prompt templates |
| `custom/` | User extensions |

### Prompt-as-config pattern

Users customize AI behavior via text files:
- No code changes required
- Prompts version-controlled alongside code
- Parallels spec-kit v17 `memory/constitution.md` pattern (governance-as-file)

## 5. AI smart filtering (v6.5.0) — natural language interests

### User workflow

1. User writes natural language description in `ai_interests.txt`:
   ```
   I care about AI agent frameworks, Python web frameworks,
   and CN tech startup news. I'm NOT interested in celebrity gossip
   or sports news.
   ```

2. AI extracts tags: `AI_agents, Python_web, CN_tech_startups, NEGATIVE:celebrity, NEGATIVE:sports`

3. News items scored against tags → filtered output

### Novel in corpus

**First framework with natural-language-interest-as-filter** in corpus. Contrast:
- graphify v16: structural queries via graph
- multica v15: Linear-style keyword filtering
- spec-kit v17: constitution-as-governance (different purpose)

## 6. AI pipeline sequence

```
Data sources (11 platforms + RSS)
         ↓
Crawler layer (Python)
         ↓
SQLite/S3 storage
         ↓
AI Filter (ai_interests.txt → relevance score)
         ↓
AI Translation (if enabled, target language)
         ↓
AI Analysis (sentiment, trends, summaries)
         ↓
Push Router (9 channels × mode selection)
         ↓
User devices
```

**Stages are isolated** — architectural discipline (parallels graphify v16's 7-stage pipeline, paperclip v14 5 invariants).

## 7. Five push modes (three active + two inferred)

Active:
- **daily** — daily summary aggregation
- **current** — real-time ranked hot topics
- **incremental** — new items only (zero duplicates)

Inferred (from multi-timeline.yaml):
- **scheduled** — timeline-driven custom intervals
- **triggered** — event-triggered (not confirmed)

## 8. AI provider cost tradeoffs

### Default DeepSeek rationale

DeepSeek is:
- CN-origin (geopolitical fit for CN platform focus)
- Cost-effective (~10× cheaper than GPT-4)
- Accepts Mandarin content fluently
- Supports OpenAI-compatible API

**Pragmatic choice** — not quality-maximizing, but cost-optimized for hourly scheduled runs.

### When to switch provider

- **Financial analysis** — Anthropic Claude (rigorous reasoning)
- **Translation** — Gemini (multilingual strength)
- **Cost-sensitive** — DeepSeek default OR self-hosted Ollama

### Fallback chain

LiteLLM supports `fallback_models` — if primary fails, try next. Resilience built-in.

## 9. Storage architecture

### Two modes

**Local SQLite:**
- Zero-config
- Single-user deployment
- Easy backup

**S3-compatible cloud:**
- Multi-instance deployment (GitHub Actions)
- AWS S3 / Cloudflare R2 / Backblaze B2 / minio compatible
- Required for Actions deployment (persistence across fresh Ubuntu)

### Dual index.html output

- `output/` directory for Docker mounting
- Root directory for GitHub Pages deployment

## 10. Corpus architectural comparison

### TrendRadar vs other T4 frameworks

| Aspect | notebooklm-py v7 | gws v13 | graphify v16 | TrendRadar v19 |
|--------|------------------|---------|--------------|----------------|
| Data source | NotebookLM web API | Google Workspace APIs | Local filesystem | 11 CN news platforms + RSS |
| AI layer | — (passthrough) | Model Armor sanitization | Claude extraction | LiteLLM 100+ providers |
| Storage | NotebookLM | Workspace | Local graph.json | SQLite / S3 |
| Scheduling | On-demand | On-demand | --watch mode | GitHub Actions cron |
| Agent integration | Skill | Skills | Skill | 21+ MCP tools |

**TrendRadar unique:** scheduled-execution + multi-provider-abstraction + regional-platform-focus.

## 11. Edges + failure modes

### Data source edges

- **CN platforms block non-CN IPs** — deployment region matters
- **Platform rate limiting** — 11 platforms = 11 different policies
- **Platform API changes** — crawler maintenance ongoing burden
- **RSS feed staleness** — upstream RSS feeds abandoned

### AI layer edges

- **LiteLLM provider deprecation** — 100+ providers, each can change API
- **Cost runaway** — hourly execution × AI analysis × 52K users if all enabled = significant API spend
- **Prompt injection** — user-controlled `ai_interests.txt` could inject adversarial prompts
- **Model hallucination** — AI summaries may misrepresent trends

### Storage edges

- **S3 cost** — cloud storage at scale
- **SQLite concurrency** — single-writer limit
- **Storage growth** — unbounded accumulation without retention policy

## 12. Cross-references

- [[(C) README bilingual + philosophy cluster summary]] — positioning
- [[(C) MCP Server + 21 Tools + Docker deployment cluster summary]] — integration layer
- [[(C) Multi-Platform News Aggregation + AI Analysis Layer]] (entity)

## 13. Corpus-first observations

- **First LiteLLM 100+ provider abstraction** (Pattern #28 candidate)
- **First 11-CN-news-platform bridge**
- **First natural-language-interest filter** (`ai_interests.txt`)
- **First hourly-GitHub-Actions-scheduled** agent framework
- **First dual-Docker-image** (crawler + MCP separated)
- **First fallback-model chain** (LiteLLM-provided)
- **First customizable-AI-prompt pattern** (3 separate prompt files)
