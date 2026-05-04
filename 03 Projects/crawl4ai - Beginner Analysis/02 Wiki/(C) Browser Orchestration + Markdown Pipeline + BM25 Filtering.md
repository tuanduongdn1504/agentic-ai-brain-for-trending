# (C) Browser Orchestration + Markdown Pipeline + BM25 Filtering

> **Type:** Entity — technical architecture
> **Parent:** [[(C) index]]
> **Sources:** README §Features + code examples + architecture inference
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

crawl4ai's architecture combines **Playwright browser orchestration** (Chromium + Firefox + WebKit) + **markdown generation pipeline** (Clean + Fit + Citations) + **BM25 + cosine-similarity content filtering** (classical NLP) for web content → LLM consumption. DOM-based approach; LLM-agnostic extraction; hybrid classical+modern NLP filtering.

## 2. Browser orchestration

### 3 browser engines

- **Chromium** (default, widest compatibility)
- **Firefox** (Mozilla-based)
- **WebKit** (Safari-based)

### Browser management patterns

1. **Default browser:** auto-launch + auto-cleanup
2. **Managed browser:** user-owned, preserved across runs
3. **Remote browser control:** Chrome DevTools Protocol, scale-to-remote
4. **Profiler:** persistent profile with cookies/auth/settings

### Session lifecycle

```python
async with AsyncWebCrawler() as crawler:
    # Browser launched + context created
    result = await crawler.arun(url="https://example.com")
    # Browser closed + cleanup
```

### Multi-URL workflow

```python
async with AsyncWebCrawler() as crawler:
    for url in urls:
        result = await crawler.arun(url=url)
        # Reuse browser context across runs
```

## 3. Markdown generation pipeline

### Pipeline stages

```
Page HTML
  ↓ (parse)
DOM tree
  ↓ (markdown generation)
Raw Markdown
  ↓ (filter: Pruning OR BM25 OR Cosine)
Fit Markdown
  ↓ (citation injection)
Final Output
```

### Clean Markdown

- Headings preserved
- Lists + tables + code blocks
- Links as `[text](url)` or `[N]` citations
- Images as `![alt](src)`

### Fit Markdown (filtered)

Removes:
- Navigation / breadcrumbs
- Sidebars / ads
- Boilerplate footers
- Legal disclaimers
- Comments / social widgets

### Custom strategies

```python
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

class MyCustomMarkdownGen(DefaultMarkdownGenerator):
    def generate(self, html, options=None):
        # Custom logic
        return super().generate(html, options)
```

## 4. BM25 content filtering

### Algorithm

BM25 = probabilistic scoring of document-query relevance. Parameters:
- k1 (term frequency saturation, default 1.2-2.0)
- b (length normalization, default 0.75)

### Use case

```python
from crawl4ai.content_filter_strategy import BM25ContentFilter

bm25 = BM25ContentFilter(user_query="machine learning applications")
filter_config = CrawlerRunConfig(content_filter=bm25)
```

### When BM25 vs Cosine

| Scenario | Use |
|----------|-----|
| Exact keyword matches | BM25 |
| Semantic similarity | Cosine (embeddings) |
| Unknown user intent | Pruning (heuristic) |

### Why classical over LLM

- **Deterministic:** reproducible results
- **Cheap:** no LLM inference per page
- **Fast:** milliseconds vs LLM seconds
- **Works offline:** no API dependency

## 5. Cosine similarity filtering

Uses embeddings (sentence transformers or user-provided model):

```python
from crawl4ai.content_filter_strategy import CosineSimilarityFilter  # inferred naming

cosine = CosineSimilarityFilter(
    query="machine learning",
    threshold=0.7
)
```

**Vector similarity > threshold** → content kept.

## 6. Extraction strategies (architectural recap)

### 4 strategy types

| Strategy | File import | Use case |
|----------|-------------|----------|
| `JsonCssExtractionStrategy` | `from crawl4ai import JsonCssExtractionStrategy` | Schema-driven CSS |
| `JsonXPathExtractionStrategy` | `from crawl4ai import JsonXPathExtractionStrategy` | Schema-driven XPath |
| `LLMExtractionStrategy` | `from crawl4ai.extraction_strategy import LLMExtractionStrategy` | Natural language query |
| `CosineStrategy` | `from crawl4ai.extraction_strategy import CosineStrategy` | Semantic chunks |

### Composability

Strategies compose:
```python
config = CrawlerRunConfig(
    extraction_strategy=JsonCssExtractionStrategy(schema),
    content_filter=BM25ContentFilter(query),
    chunking_strategy=SentenceChunking(),
)
```

## 7. Hooks architecture

### Lifecycle events (6 inferred)

1. **before_crawl** — before any navigation
2. **before_goto** — before URL load
3. **after_goto** — after page load (before extraction)
4. **before_extraction** — before content extraction
5. **after_extraction** — after extraction (before save)
6. **on_error** — any exception

### String API (config-driven)

```python
config = CrawlerRunConfig(
    before_goto_hook="await page.set_extra_http_headers({'User-Agent': 'custom'})"
)
```

### Function API (programmatic)

```python
async def my_hook(page, context, **kwargs):
    await page.wait_for_selector(".loaded-indicator")

config = CrawlerRunConfig(before_extraction_hook=my_hook)
```

## 8. Caching

### Cache modes

```python
from crawl4ai import CacheMode

CacheMode.ENABLED       # use cache, write cache (default)
CacheMode.DISABLED      # no cache read or write
CacheMode.READ_ONLY     # read cache, no writes
CacheMode.WRITE_ONLY    # always fetch, cache result
CacheMode.BYPASS        # fetch fresh, don't cache
```

### Cache backend

Filesystem-based (cache directory configurable).

### Why caching matters

- Re-runs during development don't re-fetch
- Deterministic testing
- Polite crawling (don't re-hammer servers)

## 9. Proxy configuration

```python
from crawl4ai import BrowserConfig, CrawlerRunConfig

browser_config = BrowserConfig(
    proxy="http://user:pass@proxy.example.com:8080",
)

async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun(url="https://example.com")
```

**Proxy escalation** (v0.8.5 anti-bot):
- Automatic proxy rotation when anti-bot detected
- Proxy pool configuration
- Chained proxies

## 10. Lazy load + infinite scroll handling

### Lazy load

crawl4ai waits for images to fully load via:
- Network idle wait
- Image-specific wait
- Custom hook for lazy-load trigger

### Infinite scroll

Simulates scroll events:
```python
config = CrawlerRunConfig(
    simulate_scroll=True,
    max_scrolls=5,  # stop after N scrolls
    scroll_delay=500,  # ms between scrolls
)
```

Handles:
- Twitter-like feeds
- E-commerce product listings
- Forum archives

## 11. Screenshot + raw data + iframe

### Screenshot

```python
result = await crawler.arun(
    url=url,
    screenshot=True
)
# result.screenshot contains PNG bytes
```

### Raw HTML input

```python
result = await crawler.arun(url="raw:<html>...custom HTML...</html>")
```

### Local file input

```python
result = await crawler.arun(url="file:///path/to/local.html")
```

### IFrame content

Automatic nested iframe extraction.

## 12. Related concepts

- [[(C) Cluster — Anti-bot detection + DOM extraction + LLM-agnostic integration]]
- [[(C) Open-Source Anti-Bot Detection + Pattern 47 48 Refinement]]
- [[(C) T4 Extends to N=6 + Storm Bear Web-Research Applicability + Meta]]
- Pattern #28 Multi-Provider AI Support (confirmed v25)
- Pattern #47 Vision-DOM-Free Browser Automation (candidate, REFINED at v29)

## 13. References

- README.md Features section
- Code examples in `Quick Start` + `Advanced Usage Examples`
- Inferred architecture from imports

## Edges + limitations

- **Browser install heavy** — Playwright + Chromium ~300 MB
- **DOM brittleness** — selectors break on site redesign
- **Cache directory size** — grows large over extensive crawling
- **Hook async/sync mixing** — both APIs can confuse

---

**Browser orchestration + markdown pipeline + BM25 filtering = crawl4ai's core architecture. Playwright-based DOM approach (distinct from vision). Hybrid classical NLP (BM25/cosine) + modern LLM extraction. Hooks at every step for customization.**
