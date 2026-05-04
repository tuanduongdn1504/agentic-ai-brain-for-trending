# (C) 21+ MCP Tools + Agent Ecosystem Integration

> **Type:** Entity — agent integration layer + Pattern #30 candidate evidence
> **Parent:** [[(C) index]]
> **Sources:** [[(C) MCP Server + 21 Tools + Docker deployment cluster summary]] §2-§4
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

TrendRadar exposes **21+ MCP tools across 5 categories + 4 MCP Resources** via separated `trendradar-mcp` Docker service. This is the **corpus-first explicit 4-Resources MCP usage** (most corpus frameworks use MCP Tools only). Compatible with **Claude Desktop, Cursor, ChatGPT Desktop, Cherry Studio** (CN-ecosystem AI app — first corpus mention). TrendRadar's MCP-first + LiteLLM-first + NO OpenClaw/Hermes architecture reveals a **3-layer ecosystem stratification** (Pattern #30 candidate) — MCP transport is universal, LiteLLM provider abstraction is emerging, agent-runtime identifiers (OpenClaw/Hermes) are community-platform + regional-specific.

## 2. Key claims

1. **21+ MCP tools** across 5 categories — substantial MCP surface
2. **4 MCP Resources** (platforms, rss-feeds, dates, keywords) — first corpus explicit Resources
3. **Jina AI Reader integration** — ecosystem touchpoint
4. **Cherry Studio compatibility** — CN-ecosystem AI app (corpus-first)
5. **Pattern #30 candidate** — 3-layer ecosystem stratification
6. **Dual Docker separation** (trendradar-mcp as separate image)
7. **Agent-runtime-standards NEUTRAL** — no OpenClaw/Hermes adoption

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 21+ tools | README MCP section | High |
| 4 Resources | README MCP section | High |
| Jina AI Reader | README `read_article` tool | High |
| Cherry Studio | README verbatim | High |
| Dual Docker | README Docker section | High |
| No OpenClaw/Hermes | README integration list negative | High |

## 4. MCP tools full taxonomy (21+)

### Category 1: Basic Queries (3 tools)

**Purpose:** Retrieve news data.

| Tool | Input | Output |
|------|-------|--------|
| `get_latest_news` | none | Latest N items |
| `get_news_by_date` | date range | News in range |
| `get_trending_topics` | platform | Top topics |

### Category 2: Intelligent Search (2 tools)

**Purpose:** Search + relation.

| Tool | Input | Output |
|------|-------|--------|
| `search_news` | query + filters | Matched news |
| `find_related_news` | topic/URL | Related items |

### Category 3: Advanced Analysis (6 tools)

**Purpose:** AI-layer analysis.

| Tool | Input | Output |
|------|-------|--------|
| `analyze_topic_trend` | topic, period | Momentum curve |
| `analyze_data_insights` | dataset | Pattern detection |
| `analyze_sentiment` | topic/date | Sentiment analysis |
| `aggregate_news` | query | Multi-source summary |
| `compare_periods` | period1, period2 | Temporal contrast |
| `generate_summary_report` | scope | Exec report |

### Category 4: RSS Queries (3 tools)

**Purpose:** RSS-specific operations.

| Tool | Input | Output |
|------|-------|--------|
| `get_latest_rss` | feed URL | Latest RSS items |
| `search_rss` | query | RSS search |
| `get_rss_feeds_status` | none | Subscription health |

### Category 5: System Management (3+ tools)

**Purpose:** Service operations.

| Tool | Input | Output |
|------|-------|--------|
| `get_current_config` | none | Runtime config |
| `get_system_status` | none | Health |
| `resolve_date_range` | date string | Normalized range |
| `check_version` | none | Version info |
| `read_article` | URL | **Full article (Jina AI Reader)** |

### 4 MCP Resources

MCP distinguishes **Resources** (discoverable data sources) from **Tools** (callable actions).

| Resource | Content |
|----------|---------|
| `platforms` | List of supported news platforms |
| `rss-feeds` | User's RSS subscriptions |
| `available-dates` | Date-range with data coverage |
| `keywords` | User's keyword config |

**Corpus first:** TrendRadar is the only corpus framework with explicit MCP Resources documented. Most use MCP Tools only.

## 5. MCP-compatible agents

### Verbatim from README

- **Claude Desktop** — Anthropic native MCP client
- **Cursor** — IDE-integrated MCP
- **ChatGPT Desktop** — OpenAI Desktop app
- **Cherry Studio** — **CN AI app, corpus-first mention**

### Cherry Studio analysis

**Cherry Studio** = Chinese-ecosystem desktop AI app. Parallels Claude Desktop but for CN users.

Significance:
- First corpus mention of CN-ecosystem MCP client
- Signals Pattern #30 regional-ecosystem hypothesis
- CN users have parallel MCP client ecosystem to Western
- **TrendRadar designed for bilingual CN+EN deployment**

## 6. Pattern #30 candidate — 3-Layer Agent Ecosystem Stratification

### Formal observation

Looking across corpus at v19 with TrendRadar data:

```
┌─────────────────────────────────────────┐
│ LAYER 3: Agent Runtime Standards        │
│ OpenClaw (5 wikis) / Hermes (3 wikis)   │
│ Community-platform specific (Pattern#18)│
│ Regional: Western community-platform    │
│ NOT UNIVERSAL                           │
├─────────────────────────────────────────┤
│ LAYER 2: Provider Abstraction           │
│ LiteLLM (TrendRadar v19 first)          │
│ Pattern #28 candidate                    │
│ 100+ providers unified                   │
│ EMERGING STANDARD                        │
├─────────────────────────────────────────┤
│ LAYER 1: Transport Protocol             │
│ MCP (Model Context Protocol)            │
│ Multiple wikis mention (not tracked)    │
│ Anthropic-origin, cross-agent-platform   │
│ UNIVERSAL EMERGING                       │
└─────────────────────────────────────────┘
```

### Pattern #30 formal statement

> "**Pattern #30 — 3-Layer Agent Ecosystem Stratification:** As agent ecosystem matures, distinct standardization layers emerge with different dynamics:
> 
> 1. **Transport layer (MCP):** Universal standard emerging across platforms
> 2. **Provider abstraction (LiteLLM):** Emerging standard for multi-provider decoupling
> 3. **Runtime identifiers (OpenClaw/Hermes):** Community-platform + regional specific
> 
> Frameworks can adopt some layers without others. TrendRadar adopts layers 1+2, skips 3. spec-kit v17 uses layer 1 but custom per-provider integration (not LiteLLM). Early corpus frameworks use none."

### Prediction

- v20+ will show more LiteLLM adoption (Layer 2)
- Pattern #18 remains community-platform-specific (Layer 3)
- MCP (Layer 1) universal across all new frameworks

## 7. Jina AI Reader integration

### What is Jina AI Reader

Jina AI's `reader` service fetches + parses web articles → clean markdown.

### TrendRadar usage

`read_article` MCP tool calls Jina AI Reader to fetch full article content beyond headline-level.

### Ecosystem signal

Another ecosystem-layer org (per Pattern #17):
- Jina AI publishes `reader.jina.ai` as free service
- Multiple agent frameworks could adopt (similar to anthropics/skills)
- **First corpus framework to formally integrate Jina AI Reader**

### Pattern #17 addition

TrendRadar adds Jina AI to ecosystem-layer-orgs list:
- nextlevelbuilder (goclaw + multica contribution)
- anthropics/skills
- vercel-labs/agent-skills
- **Jina AI (reader.jina.ai)** — new addition at v19

## 8. Dual Docker architecture

### Image separation rationale

```
┌─────────────────────────┐      ┌─────────────────────────┐
│ wantcat/trendradar      │      │ wantcat/trendradar-mcp  │
│ (primary crawler)       │      │ (MCP service)           │
│                         │      │                         │
│ - Scheduled collection  │      │ - 21+ MCP tools         │
│ - Push routing          │      │ - Jina AI integration   │
│ - Data storage          │      │ - Agent interface       │
│ - REQUIRED              │      │ - OPTIONAL              │
└─────────────────────────┘      └─────────────────────────┘
         │                                 │
         └──────────┬──────────────────────┘
                    ↓
            Shared SQLite / S3
```

### Why separated

1. **Independent scaling** — agents vs crawler different workloads
2. **Failure isolation** — crawler issues ≠ MCP down
3. **Security boundary** — MCP exposed, crawler internal
4. **Optional deployment** — users without agents don't run MCP

### Corpus-first

**First separated-service Docker** in corpus. Previous:
- multica v15: web + desktop separated but NOT Docker-level
- paperclip v14: single Docker
- deer-flow v9: single Docker

TrendRadar v19 = first to separate at Docker image level.

## 9. MCP tool usage patterns (inferred)

### Pattern A: Agent as reader

```
User to agent: "What's trending on Weibo today about AI?"
Agent MCP call: get_trending_topics(platform="weibo")
Agent MCP call: search_news(query="AI", platform="weibo", date="today")
Agent response: summary + links
```

### Pattern B: Agent as analyst

```
User to agent: "How has coverage of [topic] changed over last month?"
Agent MCP call: compare_periods(topic, period1, period2)
Agent MCP call: analyze_sentiment(topic, period=last_month)
Agent MCP call: generate_summary_report(topic)
Agent response: analytical report
```

### Pattern C: Agent as researcher

```
User to agent: "Research [topic] across sources"
Agent MCP call: search_news(topic, all_platforms=true)
Agent MCP call: find_related_news(top_result)
Agent MCP call: read_article(deepest_source_url)  # Jina AI
Agent response: synthesized research
```

## 10. Edges + failure modes

### MCP protocol edges

- **21+ tools × protocol evolution** — Anthropic MCP spec changes
- **Client compatibility drift** — Claude Desktop vs Cursor vs Cherry Studio
- **Resource discovery** — less mature than Tools; clients may not discover

### Integration edges

- **Jina AI Reader dependency** — third-party service availability
- **Cherry Studio CN-only deployment** — regional client
- **Dual Docker coordination** — version alignment

### Usage edges

- **Tool combinations** — 21+ tools × combinations = complex interactions
- **Rate limiting** — 21+ tools × 52K users could saturate
- **Cost surge** — advanced analysis tools each = LLM call

## 11. Related concepts

- [[(C) Multi-Platform News Aggregation + AI Analysis Layer]] — what gets exposed
- [[(C) Solo-at-52K CN Ecosystem + Pattern 18 Regional Hypothesis]] — organizational
- [[(C) T4 4-way + Pattern 9 Resolution D + 3 New Candidates + Storm Bear]] — tier meta

## 12. Cross-project comparison

### MCP surface across corpus

| Framework | MCP Tools | MCP Resources | Server mode |
|-----------|-----------|---------------|-------------|
| GSD v5 | Mentioned | — | — |
| multica v15 | — | — | — |
| graphify v16 | 4 tools (query, get_node, neighbors, shortest_path) | — | Built-in |
| spec-kit v17 | — | — | Per-agent custom |
| agency-agents v18 | — | — | Per-platform |
| **TrendRadar v19** | **21+ tools (5 categories)** | **4 Resources** | **Separated Docker** |

**TrendRadar largest MCP surface in corpus by 5×.**

## 13. Open questions

- Q7: Why no OpenClaw? (CN ecosystem parallel? LiteLLM-agnostic design?)
- Q11: Full newsnow API platform list?
- Q13: MCP Resources client support breadth?
- Q15: LiteLLM adoption prediction for corpus?
- Q23: CN ecosystem uses different runtime identifiers corpus doesn't track?

## 14. References

- README MCP section
- Pattern #30 formal statement (PATTERN_LIBRARY.md candidate)
- Jina AI Reader: reader.jina.ai
- Parent: [[(C) index]]
