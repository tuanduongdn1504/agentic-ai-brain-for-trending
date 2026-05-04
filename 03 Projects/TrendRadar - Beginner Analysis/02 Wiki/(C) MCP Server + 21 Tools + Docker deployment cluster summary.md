# (C) MCP Server + 21 Tools + Docker deployment cluster summary — TrendRadar

> **Sources:** README MCP section + Docker configs + GitHub Actions workflow + 9 push channels documentation
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

TrendRadar's **distribution architecture** = MCP server (agent consumer interface) + Docker deployment + 9 push channels + scheduled execution. Together they form the runtime surface that distinguishes TrendRadar as T4 bridge.

## 2. 21+ MCP tools (full categorization)

### Basic Queries (3 tools)

| Tool | Purpose |
|------|---------|
| `get_latest_news` | Fetch latest news items |
| `get_news_by_date` | Date-range news retrieval |
| `get_trending_topics` | Top trending across platforms |

### Intelligent Search (2 tools)

| Tool | Purpose |
|------|---------|
| `search_news` | Keyword/semantic news search |
| `find_related_news` | Find news related to specific topic |

### Advanced Analysis (6 tools)

| Tool | Purpose |
|------|---------|
| `analyze_topic_trend` | Topic momentum over time |
| `analyze_data_insights` | Cross-platform pattern detection |
| `analyze_sentiment` | Sentiment analysis of coverage |
| `aggregate_news` | Multi-source aggregation |
| `compare_periods` | Temporal comparison |
| `generate_summary_report` | Executive-summary generation |

### RSS Queries (3 tools)

| Tool | Purpose |
|------|---------|
| `get_latest_rss` | Latest RSS feed items |
| `search_rss` | RSS-specific keyword search |
| `get_rss_feeds_status` | RSS subscription health |

### System Management (3+ tools)

| Tool | Purpose |
|------|---------|
| `get_current_config` | Runtime config query |
| `get_system_status` | Service health check |
| `resolve_date_range` | Date-string parsing helper |
| `check_version` | Version info |
| `read_article` | **Jina AI Reader integration** — full article content retrieval |

### 4 MCP Resources (v2 novel concept)

- `platforms` — list of supported platforms
- `rss-feeds` — RSS subscription inventory
- `available-dates` — date-range coverage
- `keywords` — user keyword config

**MCP Resources** are discoverable data sources (vs MCP Tools which are callable actions). TrendRadar exposes both.

## 3. MCP architecture context

### Pattern #18 refinement evidence

TrendRadar has **21+ MCP tools** — substantial MCP surface — BUT does NOT mention OpenClaw or Hermes.

**Analysis:**
- OpenClaw/Hermes are agent-runtime identifiers (not MCP-layer)
- MCP is transport protocol (Anthropic-origin, cross-agent-platform)
- LiteLLM is provider abstraction (implementation layer)

**3-layer corpus ecosystem emerging:**
1. **Transport layer:** MCP (Model Context Protocol) — corpus-wide emerging standard
2. **Provider layer:** LiteLLM / OneAPI — multi-provider abstraction (Pattern #28 candidate)
3. **Runtime layer:** OpenClaw / Hermes — community-platform-specific (Pattern #18 refined)

**Pattern #30 candidate — Layered Agent Ecosystem Standards:**

> "As agent ecosystem matures, distinct layers emerge with different standardization dynamics. MCP is becoming universal transport; LiteLLM-style provider abstraction is emerging; runtime-standards (OpenClaw/Hermes) are community-platform-specific and regional."

### MCP-compatible agents (verbatim from README)

- **Claude Desktop** — Anthropic native
- **Cursor** — IDE-integrated
- **ChatGPT Desktop** — OpenAI native
- **Cherry Studio** — CN AI app (corpus-first mention)

**Cherry Studio** = CN-ecosystem AI app, parallels Claude Desktop's role in Western market. Signals Pattern #30 regional-ecosystem hypothesis.

## 4. Dual Docker architecture

### Two separate images

**Image 1: `wantcat/trendradar`**
- Primary crawler + push service
- Runs scheduled news collection
- Handles 9 push channel routing
- Required for all deployments

**Image 2: `wantcat/trendradar-mcp`**
- MCP AI analysis service
- Runs MCP protocol server
- Separated from crawler for isolation
- Optional (only needed for agent integration)

### Why separated

- **Independent scaling** — MCP agents vs crawler workload different
- **Failure isolation** — crawler issues don't break MCP
- **Security boundary** — MCP server more exposed than internal crawler
- **Optional deployment** — users without agent use don't run MCP

**Corpus first:** First separated-service Docker in corpus. Contrast:
- multica v15: single-app multi-component
- paperclip v14: local server (not dual-image)
- deer-flow v9: single Docker

## 5. 9 push channels (full matrix)

### CN-ecosystem channels (3)

| Channel | Use case | CN audience fit |
|---------|----------|-----------------|
| **WeChat Work** (企业微信) | Corporate CN | High |
| **Feishu/Lark** (飞书) | CN + international enterprise | High |
| **DingTalk** (钉钉) | CN enterprise | High |

### Cross-border channels (6)

| Channel | Use case | Geography |
|---------|----------|-----------|
| **Telegram** | Personal messaging | International |
| **Email** | Universal | Global |
| **ntfy** | Self-hosted push | Privacy-focused |
| **Bark** | iOS native | Apple-users |
| **Slack** | Workplace | Western enterprise |
| **Generic webhook** | Custom (Discord, Matrix, IFTTT) | Developer-controlled |

### Multi-account support

All channels support semicolon-separated URLs:
```yaml
FEISHU_WEBHOOK_URL: "url1;url2;url3"
```
→ Single message to multiple recipients.

### Email SMTP auto-detection (10+ providers)

- Gmail, QQ, 163, Outlook, Yahoo, Zoho, Sina, 126, 139, iCloud
- TrendRadar auto-configures based on email domain

### Corpus comparison

- **TrendRadar 9 channels** = broadest multi-push in corpus
- multica v15: Linear-analog built-in
- paperclip v14: no multi-push
- spec-kit v17: no push channels
- graphify v16: no push channels

**Push-channel specialization** = T4/application-tier specific. T1 frameworks don't need push.

## 6. GitHub Actions deployment (primary)

### Workflow details

**File:** `.github/workflows/crawler.yml`

**Trigger:**
```yaml
schedule:
  - cron: "0 * * * *"  # Hourly
```

**Environment:**
- Fresh Ubuntu per run
- Python setup + dependencies
- Executes `main.py`

**Activity requirement:**
- GitHub Actions deactivates after 60 days of repo inactivity
- TrendRadar requires "Check In" workflow every 7 days to keep active
- **7-day check-in = Actions fairness compliance** (explained in philosophy)

### Required secrets

| Secret | Purpose |
|--------|---------|
| Webhook URLs (FEISHU_WEBHOOK_URL, etc.) | Push channels |
| AI_API_KEY, AI_PROVIDER | LiteLLM config |
| S3_BUCKET_NAME, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY, S3_ENDPOINT_URL | Cloud storage |

### Cloud storage requirement

GitHub Actions uses fresh Ubuntu → no persistence between runs. **S3-compatible storage REQUIRED** for Actions deployment.

Local SQLite works only for local Docker / pip deployments.

## 7. Deployment modes comparison

| Mode | Persistence | Scaling | Use case |
|------|-------------|---------|----------|
| **Local pip** | SQLite | Single-user | Development / personal |
| **Local Docker** | SQLite or S3 | Single-host | Homelab |
| **GitHub Actions** | S3 required | Hourly | Production scheduled |
| **VPS Docker + cron** | SQLite or S3 | Cron-customizable | Custom production |

**GitHub Actions = primary production mode** documented in README. Unique in corpus as primary deployment method.

## 8. manage.py command interface

```bash
docker exec -it trendradar python manage.py <command>
```

### Commands

| Command | Purpose |
|---------|---------|
| `status` | Service health |
| `run` | Trigger immediate crawl |
| `logs` | View execution logs |
| `config` | View/edit config |
| `files` | List output files |
| `start_webserver` | Launch HTML viewer |
| `stop_webserver` | Stop HTML viewer |

### Environment variable overrides

All config.yaml values can be overridden via env vars for containerized deployment.

## 9. HTML report viewer (v6.6.0+)

### Features

- Wide layout
- Dark mode
- Keyboard shortcuts (Tab navigation)
- Reading progress indicator
- Copy-on-hover

**Local self-hosted vs GitHub Pages:**
- Docker: serves HTML via `start_webserver` command
- GitHub Actions: publishes HTML to GitHub Pages

## 10. Security + validation architecture

### SECURITY considerations

No dedicated SECURITY.md observed in top-level probe, but implicit security features:

- **Webhook URLs in env vars** (not hardcoded)
- **AI API keys via secrets** (not exposed)
- **7-day activity window** (prevents abandoned-deployment resource waste)
- **Dual Docker separation** (MCP exposure isolated)
- **User-controlled prompts** — risk of prompt injection via `ai_interests.txt`

### Corpus comparison

- graphify v16: explicit SECURITY.md
- spec-kit v17: SECURITY.md + AI-disclosure policy
- agency-agents v18: SECURITY.md
- **TrendRadar v19: implicit security (no SECURITY.md observed in probe)** — potential gap at 52K scale

## 11. Edges + failure modes

### MCP integration edges

- **21+ tools maintenance** — each tool × MCP protocol changes
- **Jina AI Reader dependency** — third-party service availability
- **MCP client compatibility drift** — Claude Desktop vs Cursor vs Cherry Studio differ

### Docker edges

- **Dual-image coordination** — versioning both images aligned
- **wantcat Docker Hub account** — single-account dependency
- **S3 credentials in GitHub Actions** — secret rotation burden

### GitHub Actions edges

- **7-day check-in failure** — Actions deactivates silently
- **Cron reliability** — Actions scheduling can drift/skip
- **Public repo = public Actions logs** — privacy leak risk
- **Rate limiting at scale** — 52K users × scheduled executions

## 12. Cross-references

- [[(C) README bilingual + philosophy cluster summary]] — positioning
- [[(C) AI architecture + LiteLLM + 11 Platforms cluster summary]] — data + AI layer
- [[(C) 21+ MCP Tools + Agent Ecosystem Integration]] (entity)

## 13. Corpus-first observations

- **First dual-Docker-image separation** (crawler vs MCP service)
- **First GitHub-Actions-primary deployment** for agent framework
- **First 9-channel multi-push** (7-channel tier)
- **First Jina AI Reader integration** (ecosystem touchpoint)
- **First MCP Resources (not just Tools)** explicit usage
- **First Cherry Studio mention** (CN AI app ecosystem)
- **First "activity-window governance"** (7-day check-in)
- **Most CN-ecosystem push channels** (WeChat Work + Feishu + DingTalk simultaneously)

## 14. Pattern implications

- **Pattern #28 (Multi-Provider AI Abstraction)** — LiteLLM first corpus
- **Pattern #30 (Layered Agent Ecosystem Standards)** — MCP transport + LiteLLM provider + OpenClaw/Hermes runtime = 3 distinct layers
- **Pattern #18 refined** — TrendRadar's MCP-first + LiteLLM-first architecture bypasses agent-runtime identifiers entirely. Suggests alternate path to agent-integration that doesn't require Pattern #18 standards.
