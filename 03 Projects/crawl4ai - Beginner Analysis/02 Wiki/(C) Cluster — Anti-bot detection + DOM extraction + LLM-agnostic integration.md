# (C) Cluster — Anti-bot detection + DOM extraction + LLM-agnostic integration

> **Type:** Source cluster summary
> **Sources:** README v0.8.5 anti-bot highlights + extraction strategies section + LLM integration
> **Coverage:** Anti-bot architecture (3-tier + proxy + Shadow DOM), DOM-based extraction (CSS/XPath/JSON schema), LLM-agnostic integration, BM25/cosine filtering
> **Parent:** [[(C) index]]

---

## 1. Summary

crawl4ai's v0.8.5 introduced **3-tier anti-bot detection + proxy escalation + Shadow DOM flattening + consent popup removal** — open-source counterpart to Skyvern v24's proprietary anti-bot commercial moat (Pattern #48 candidate). Extraction strategy is **DOM-based** (CSS/XPath/LLM/JSON schemas) — distinguishes from Skyvern v24's **vision-based approach** (Pattern #47 candidate). **LLM-agnostic** integration (supports all LLMs via BYO). BM25 + cosine similarity for content filtering.

## 2. 3-tier anti-bot detection architecture (v0.8.5)

### Tier structure

README v0.8.5 highlight:
> *"Automatic 3-tier anti-bot detection with proxy escalation, Shadow DOM flattening, deep crawl cancellation, config defaults API, consent popup removal, and critical security patches."*

### Inferred tier architecture (details in v0.8.5 release notes)

**Tier 1 — baseline (most requests):**
- Standard Playwright request
- Default headers + user-agent
- Normal rate limiting

**Tier 2 — escalation (detection observed):**
- Proxy rotation
- Enhanced headers + fingerprint randomization
- Slower pacing

**Tier 3 — maximum evasion (strong anti-bot):**
- Managed browser with user profile
- Stealth mode
- Proxy chaining
- Session persistence

**Shadow DOM flattening** — web-scraping-specific technique: modern sites use Shadow DOM to encapsulate components; flattening exposes content to selectors.

**Consent popup removal** — handles GDPR/cookie banners automatically.

### Stealth mode (separate feature)

README Additional Features:
> *"Stealth Mode: Avoid bot detection by mimicking real users."*

## 3. Pattern #48 Anti-Bot Commercial Moat — REFINEMENT at v29

### Pattern #48 as registered at v24 (Skyvern)

> **#48 (N=1): Proprietary-Anti-Bot Commercial Moat** (Skyvern v24 gates anti-bot to paid Cloud tier; OSS version basic).

### crawl4ai counter-example

crawl4ai v0.8.5 has **comprehensive open-source anti-bot**:
- 3-tier detection
- Proxy escalation
- Shadow DOM flattening
- Consent popup removal
- Stealth mode

**Not commercial-moat-gated.** All anti-bot features Apache-2.0 OSS.

### Refinement needed

**Pattern #48 original formulation too broad.** Refine to:
> **#48 REFINED: Proprietary Anti-Bot COMMERCIAL Moat.** Specifically proprietary anti-bot gated to paid tier as commercial differentiator. crawl4ai demonstrates OSS anti-bot is viable; moat-specificity is commercial-gating, not anti-bot capability itself.

### Related: new candidate #64

**Pattern candidate #64 Open-Source Anti-Bot Detection** — counterpart pattern for OSS anti-bot. Distinct from #48 (proprietary) + distinct from basic anti-bot (many tools have some). N=1 crawl4ai v29.

## 4. DOM-based extraction architecture

### 4 extraction strategies

| Strategy | Mechanism | Use case |
|----------|-----------|----------|
| **CSS selectors** | `div.content > p` | Structured pages (product listings, tables) |
| **XPath** | `//article[@class='main']` | Complex hierarchical selection |
| **LLM-driven** | User query → LLM extracts | Unstructured or narrative content |
| **JSON schemas** | Schema-based template | Repetitive patterns (product grids) |

### Python API example (CSS-based JsonCssExtractionStrategy)

```python
from crawl4ai import AsyncWebCrawler, JsonCssExtractionStrategy
import json

schema = {
    "name": "Product",
    "baseSelector": ".product-card",
    "fields": [
        {"name": "title", "selector": "h2", "type": "text"},
        {"name": "price", "selector": ".price", "type": "text"},
    ]
}

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com/products",
            extraction_strategy=JsonCssExtractionStrategy(schema)
        )
        print(json.loads(result.extracted_content))
```

### Why DOM-based (vs vision-based)

**DOM advantages:**
- Faster (no LLM inference per page)
- Deterministic (same selectors = same results)
- Cheaper (no API costs for extraction)
- Scalable (millions of pages)

**DOM disadvantages:**
- Breaks when site restructures
- Can't handle pure-image content
- Requires HTML structure understanding

### vs Skyvern v24 vision-based

| Dimension | crawl4ai (DOM) | Skyvern (Vision) |
|-----------|----------------|------------------|
| Approach | CSS/XPath selectors | LLM sees screenshots |
| Cost per page | ~$0 (no LLM) | ~$0.01-0.10 (LLM inference) |
| Speed | Fast (ms) | Slower (seconds) |
| Robustness to UI change | Brittle | Resilient |
| Handles pure-image content | No | Yes |
| Handles dynamic JS | Requires hooks | Natural |

**Architecturally orthogonal** — different tradeoffs.

## 5. Pattern #47 Vision-DOM-Free Browser Automation — REFINEMENT

### Pattern #47 as registered at v24

> **#47 (N=1): Vision-DOM-Free Browser Automation** (Skyvern v24 uses vision instead of XPath/CSS selectors).

### crawl4ai counter-observation

crawl4ai is DOM-based (CSS + XPath + JSON schemas). **Not vision.** Yet crawl4ai is successful web crawler at 64K stars.

### Refinement needed

**Pattern #47 scope tightens:**
> **#47 REFINED: Vision-Based Browser Automation as ALTERNATIVE to DOM.** Not "vision-DOM-free" as if vision is replacement for all browser automation. Vision is one approach (Skyvern v24); DOM remains dominant approach (crawl4ai v29 + most web scrapers). Both valid tradeoff paths.

**Reformulated statement:**
> **#47 Vision-Based Browser Automation Paradigm** — framework uses LLM vision as primary interaction mechanism for browser automation (Skyvern v24). Alternative to DOM-based approach (CSS/XPath selectors used by crawl4ai, Playwright, Selenium, etc.). Trade-offs: vision more robust to UI changes but costly; DOM faster but brittle.

## 6. LLM-agnostic integration

### All LLMs supported

README verbatim:
> *"🤖 LLM-Driven Extraction: Supports all LLMs (open-source and proprietary) for structured data extraction."*

### Via litellm (v0.8.5 and prior) / unclecode-litellm (v0.8.6+)

crawl4ai uses **LiteLLM abstraction** (or fork `unclecode-litellm` post-security-incident) for multi-provider support.

**Providers via LiteLLM:**
- OpenAI (GPT-4o, GPT-4-turbo, etc.)
- Anthropic (Claude)
- Azure OpenAI
- AWS Bedrock
- Google Gemini
- Cohere
- Open-source via Ollama
- 100+ providers

### Pattern #28 Multi-Provider AI Support — 5th data point

| # | Wiki | Mechanism | Variant |
|---|------|-----------|---------|
| 1 | TrendRadar v19 | LiteLLM routing | Abstraction-library |
| 2 | multica v15 | Native BYO 8 models | Native BYO |
| 3 | Skyvern v24 | Native BYO 8+ providers | Native BYO |
| 4 | markitdown v28 | `llm_client` DI + Azure DocIntel | DI contract |
| 5 | **crawl4ai v29** | **LiteLLM fork (unclecode-litellm)** | **Abstraction-library (forked)** |

**Pattern #28 strengthens at 5 data points.**

## 7. BM25 + cosine similarity content filtering

### BM25 (Best Matching 25)

**Classical information retrieval algorithm.** Scores document relevance for query. Used in crawl4ai:

```python
from crawl4ai.content_filter_strategy import BM25ContentFilter

# Filter crawled content by BM25 relevance to user query
bm25_filter = BM25ContentFilter(user_query="machine learning")
```

### Cosine similarity

**Vector similarity for semantic matching.** Used for:
- Finding relevant content chunks
- Semantic extraction (vs exact keyword)
- Query-relevance scoring

### Pruning content filter

```python
from crawl4ai.content_filter_strategy import PruningContentFilter

# Remove noise (ads, boilerplate) via heuristics
pruning_filter = PruningContentFilter()
```

### "Fit Markdown" derivation

**Fit Markdown** = Clean Markdown + filter (BM25 / Cosine / Pruning) applied.

### Why classical methods instead of LLM-only

- **Cost:** BM25/cosine are deterministic, free per page
- **Speed:** milliseconds vs LLM seconds
- **Reproducibility:** same input → same output
- **Fallback:** works without LLM client configured

**LLM extraction remains available** for cases classical methods insufficient.

## 8. Chunking strategies

crawl4ai supports 3 chunking approaches:

| Strategy | Mechanism |
|----------|-----------|
| **Topic-based** | Semantic boundary detection |
| **Regex** | Pattern-based splits |
| **Sentence-level** | Linguistic sentence boundaries |

### Use cases

- LLM context window limits (chunk → process separately)
- Semantic search (chunk-level embeddings)
- RAG pipelines (retrieve relevant chunks)

## 9. Hooks architecture

README §Crawling:
> *"🛠️ Customizable Hooks: Define hooks at every step to customize crawling behavior (supports both string and function-based APIs)."*

### Hook lifecycle events (inferred)

- Before crawl
- After page load
- Before extraction
- After extraction
- On error
- Before save

### Customization API

**String-based** (configuration):
```python
config = CrawlerRunConfig(
    before_load_hook="sleep(1)",
)
```

**Function-based** (programmatic):
```python
async def my_hook(page, context):
    await page.wait_for_selector(".loaded")

config = CrawlerRunConfig(
    before_load_hook=my_hook,
)
```

## 10. Session management

Persistent browser profiler:
- Save authentication state
- Preserve cookies
- Multi-step crawling (login → fetch → extract)
- Session reuse

### Use case

```python
# Create session
profile = await crawler.create_profile("mysession")
await profile.login("https://site.com/login", credentials)

# Reuse session later
result = await crawler.arun(
    url="https://site.com/dashboard",
    profile_name="mysession"
)
```

## 11. Scalability deployment

### Docker + FastAPI

- Optimized Docker image
- FastAPI REST server
- JWT token authentication
- API gateway one-click deploy

### Cloud configurations

- AWS-ready (README mentions)
- Generic cloud deployments
- Horizontal scaling via Docker orchestration

### Cloud API Closed Beta

- Managed hosted version launching soon
- Commercial tier
- Pattern #31 Open-Core candidate (3rd data point after fish-speech + Skyvern)

## 12. Cross-wiki signals

- **Pattern #47 REFINEMENT** — vision-specific (not DOM-free)
- **Pattern #48 REFINEMENT** — proprietary-commercial-specific (not anti-bot-generic)
- **Pattern #28 Multi-Provider AI Support 5th data point** — LLM-agnostic via LiteLLM
- **Pattern #31 Open-Core 3rd data point PENDING** — Cloud API closed beta
- **Pattern candidate #64 Open-Source Anti-Bot Detection** — NEW at v29
- **Pattern candidate #66 Supply-Chain Security Incident Response** — unclecode-litellm fork
- Classical NLP (BM25/cosine) + modern LLM integration = hybrid-approach

## 13. Edges + limitations

- **Anti-bot tier details** not fully documented in README (requires v0.8.5 release notes)
- **LiteLLM supply-chain** — one-time incident; may recur with other deps
- **DOM fragility** — site redesigns break selectors
- **Shadow DOM flattening edge cases** — some sites may not flatten cleanly
- **Hooks API complexity** — string + function APIs could confuse beginners
- **Cloud API commercial terms** unclear until launch
- **Chunking + filtering compose** — learning curve for optimal pipeline

---

**Cluster signal:** crawl4ai's DOM-based + open-source-anti-bot + LLM-agnostic architecture refines two Pattern candidates (#47, #48) by providing counter-examples. Validates DOM approach as primary web-scraping paradigm. Registers new Pattern candidates #64 (OSS anti-bot) and #66 (supply-chain incident response).
