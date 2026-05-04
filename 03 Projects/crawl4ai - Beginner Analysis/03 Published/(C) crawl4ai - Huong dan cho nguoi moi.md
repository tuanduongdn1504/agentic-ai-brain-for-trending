# (C) crawl4ai — Hướng dẫn cho người mới / Beginner's Guide

> **Project:** [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
> **Tagline:** *"🚀🤖 Open-source LLM Friendly Web Crawler & Scraper"*
> **Audience:** Python developer xây RAG / agent pipelines cần scrape web content
> **Language:** Bilingual VN/EN
> **Complexity:** Thấp-trung — pip install + 1 lệnh. Nâng cao: anti-bot tiers + browser profiles + LLM extraction.

---

## 1. crawl4ai là gì? / What is crawl4ai?

**VN:** crawl4ai là Python web crawler + scraper do **unclecode** (solo developer) xây. Convert webpages sang clean Markdown cho LLM consumption. Playwright-based (Chromium + Firefox + WebKit). Apache-2.0 license. 64K stars.

**EN:** crawl4ai is a Python web crawler + scraper by solo developer unclecode. Converts web content to LLM-friendly Markdown. Playwright-based. Apache-2.0.

**Key stats:**
- **64,417 GitHub stars** (#7 corpus)
- **Apache-2.0 license**
- **Python**
- **Current version:** v0.8.6 (security hotfix)
- **PyPI:** `pip install crawl4ai`
- **Homepage:** crawl4ai.com
- **Discord:** discord.gg/jP8KfhDhyN

## 2. Tại sao dùng crawl4ai? / Why crawl4ai?

### Use cases

- **RAG pipelines** — fetch web content → embed → vector DB
- **AI agent workflows** — provide fresh web context
- **Data pipelines** — scheduled crawls + extraction
- **Research** — academic scraping + content aggregation
- **Content monitoring** — track website changes

### Distinguishing features

- ✅ **Open-source anti-bot detection** (3-tier + proxy escalation + Shadow DOM)
- ✅ **DOM-based extraction** (CSS / XPath / JSON schemas — fast + cheap)
- ✅ **LLM-agnostic** (all LLMs via LiteLLM fork)
- ✅ **BM25 + cosine filtering** (classical NLP for content pruning)
- ✅ **3 browser engines** (Chromium + Firefox + WebKit)
- ✅ **Docker + FastAPI deployment** ready
- ✅ **MIT-style license** (Apache-2.0, commercial-friendly)

## 3. Cài đặt / Installation

### Quick install

```bash
pip install -U crawl4ai
crawl4ai-setup
crawl4ai-doctor
```

### Browser setup

```bash
python -m playwright install --with-deps chromium
```

### Pre-release

```bash
pip install crawl4ai --pre
```

### Docker

```bash
docker pull unclecode/crawl4ai:latest
docker run -p 8080:8080 unclecode/crawl4ai
```

## 4. Sử dụng cơ bản / Basic usage

### CLI — quick crawl

```bash
# Basic crawl to markdown
crwl https://www.nbcnews.com/business -o markdown

# Deep crawl (BFS, max 10 pages)
crwl https://docs.crawl4ai.com --deep-crawl bfs --max-pages 10

# LLM-based extraction
crwl https://example.com/products -q "Extract all product prices and titles"
```

### Python API

```python
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://www.nbcnews.com/business")
        print(result.markdown)

asyncio.run(main())
```

## 5. Advanced — Structured extraction với CSS schema

```python
import asyncio
from crawl4ai import AsyncWebCrawler, JsonCssExtractionStrategy
import json

schema = {
    "name": "Article",
    "baseSelector": "article",
    "fields": [
        {"name": "title", "selector": "h1", "type": "text"},
        {"name": "author", "selector": ".author", "type": "text"},
        {"name": "date", "selector": ".date", "type": "text"},
    ]
}

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://news.site/article-list",
            extraction_strategy=JsonCssExtractionStrategy(schema)
        )
        articles = json.loads(result.extracted_content)
        for article in articles:
            print(article['title'])

asyncio.run(main())
```

## 6. Advanced — LLM-based extraction

```python
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import LLMExtractionStrategy

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://docs.example.com/api",
            extraction_strategy=LLMExtractionStrategy(
                provider="openai/gpt-4o",
                api_token="your-api-key",
                instruction="Extract all API endpoints with their HTTP methods and descriptions",
                schema={"endpoints": [{"path": "str", "method": "str", "description": "str"}]}
            )
        )
        print(result.extracted_content)

asyncio.run(main())
```

## 7. Advanced — Content filtering với BM25

```python
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_filter_strategy import BM25ContentFilter

async def main():
    bm25 = BM25ContentFilter(user_query="machine learning applications")
    config = CrawlerRunConfig(content_filter=bm25)

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://blog.site.com/long-article",
            config=config
        )
        # result.fit_markdown = filtered version keeping only BM25-relevant parts
        print(result.fit_markdown)

asyncio.run(main())
```

## 8. Advanced — Anti-bot + proxy

```python
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

browser_config = BrowserConfig(
    proxy="http://user:pass@proxy.example.com:8080",
    stealth=True,  # anti-bot mimicking
)

async def main():
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://protected-site.com",
            config=CrawlerRunConfig(
                simulate_scroll=True,
                max_scrolls=5,
            )
        )
        print(result.markdown)

asyncio.run(main())
```

**v0.8.5 adds 3-tier automatic anti-bot** — escalates proxies/fingerprints/sessions when detected.

## 9. Lộ trình 2 tuần cho beginner / 2-week roadmap

### Tuần 1: Basics

- Day 1: `pip install crawl4ai` + `crawl4ai-setup` + test `crwl` command
- Day 2: Basic Python API (AsyncWebCrawler + arun)
- Day 3: Multi-URL crawl + observe markdown output
- Day 4: Try CSS extraction với JsonCssExtractionStrategy
- Day 5: Deep crawl (BFS) + max_pages
- Weekend: Scrape 2-3 real sites bạn quan tâm

### Tuần 2: Advanced

- Day 8: LLM extraction với OpenAI API key
- Day 9: BM25 content filtering
- Day 10: Browser profiles + session management
- Day 11: Anti-bot stealth mode
- Day 12: Docker deployment test
- Day 13: Integrate với RAG pipeline (crawl → embed → vector DB)
- Day 14: Write summary của crawl4ai capabilities

## 10. Storm Bear use cases — MEDIUM-HIGH relevance

**Storm Bear = Scrum coach + developer.** Use cases:

### Use case 1: Client research

```bash
crwl https://clientcompany.com --deep-crawl bfs --max-pages 20 -o markdown \
  > /vault/clients/target-research.md
```

### Use case 2: Competitor analysis

```python
# Scrape competitor Scrum-coaching consultancies
# Extract services + pricing + testimonials
```

### Use case 3: Scrum community monitoring

```bash
crwl https://www.scrumalliance.org/articles --deep-crawl bfs --max-pages 50 \
  -q "Extract article titles, authors, dates"
```

### Use case 4: Corpus wiki extension

crawl4ai + markitdown v28 = **complete ingestion pipeline:**
- Web → crawl4ai → markdown
- PDF/Office → markitdown → markdown
- Audio → markitdown → markdown

All converted content → Storm Bear vault.

### Use case 5: Scheduled monitoring

```bash
# Cron job
0 9 * * * /usr/bin/crwl https://important-site.com -o /vault/daily/$(date +%Y%m%d).md
```

## 11. Ưu điểm / Pros

- ✅ **Apache-2.0 pure OSS** — commercial use OK
- ✅ **64K stars** — active community + sustained development
- ✅ **Solo author unclecode** — direct communication via Discord
- ✅ **3 browser engines** — Chromium + Firefox + WebKit
- ✅ **Comprehensive anti-bot OSS** — 3-tier + proxy escalation + Shadow DOM
- ✅ **LLM-agnostic** — all providers via LiteLLM fork
- ✅ **Hybrid classical + LLM filtering** — BM25/cosine + LLM extraction
- ✅ **CLI + Python + Docker** — 3 deployment surfaces
- ✅ **`crwl` short CLI alias** — ergonomic
- ✅ **Active development** — v0.8.6 recent security hotfix

## 12. Caveats / Nhược điểm

- ⚠️ **Solo author bus factor** — unclecode single point of failure at 64K scale
- ⚠️ **Playwright heavy install** — ~300 MB for Chromium
- ⚠️ **v0.8.6 supply-chain incident** — litellm upstream compromise (forked to unclecode-litellm)
- ⚠️ **DOM brittleness** — selectors break on site redesigns
- ⚠️ **Cloud API not yet launched** — commercial tier closed beta only
- ⚠️ **English-only README** — no VN/CN translations
- ⚠️ **Legal/ethical ToS compliance** — user responsibility (tool doesn't enforce)
- ⚠️ **Learning curve for advanced features** — 6 feature categories + 30+ sub-features

## 13. References

- [GitHub: unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
- [Homepage: crawl4ai.com](https://crawl4ai.com)
- [PyPI: crawl4ai](https://pypi.org/project/crawl4ai/)
- [Docs: docs.crawl4ai.com](https://docs.crawl4ai.com/)
- [Discord](https://discord.gg/jP8KfhDhyN)
- [GitHub Sponsors](https://github.com/sponsors/unclecode)
- [Colab example](https://colab.research.google.com/drive/1SgRPrByQLzjRfwoRNq1wSGE9nYY_EE8C)

**Storm Bear wiki cross-refs:**
- [[(C) Browser Orchestration + Markdown Pipeline + BM25 Filtering]]
- [[(C) Open-Source Anti-Bot Detection + Pattern 47 48 Refinement]]
- [[(C) Solo-Enterprise-Scale 3rd Corpus Data Point + 4-Tier Sponsorship + Pattern 31 Candidate]]
- [[(C) T4 Extends to N=6 + Storm Bear Web-Research Applicability + Meta]]
- v28 markitdown (complementary ingestion utility)
- v24 Skyvern (Pattern #47 + #48 peer)

---

**crawl4ai v29 = T4 bridge framework #6. Solo-enterprise-scale (3rd corpus data point). Storm Bear pilot priority #5 (direct web research utility). Composable với markitdown v28 for 3-format ingestion pipeline. Apache-2.0 + pip + 1 CLI command = zero-friction adoption. Solo author caveat + supply-chain incident = awareness needed.**
