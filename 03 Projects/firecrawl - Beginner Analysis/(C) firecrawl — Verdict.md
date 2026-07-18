# (C) Firecrawl — Verdict

*LLM Wiki v214 · 2026-07-17 · `firecrawl/firecrawl` (f.k.a. `mendableai/firecrawl`)*
*Verdict produced **INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions` — no workflow / no subagent (the ~205K shim overflows subagent context → prompt-too-long; the v200→v213 self-throttle). Source hand-fetched (repo page + raw README); identity + funding + landscape by WebSearch; collision + pattern-anchor by sanity-anchored hand-grep of `_state/` + `_patterns/`.*

---

## Verdict: **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG

### (a) Anthropic / cultural-peer author — **FAIL**
Firecrawl Inc. (formerly Mendable AI) is a YC-backed startup (founders Peffer / Ciarla / Silberstein Camara; ~$16.2M funded), **not Anthropic**. Per routine **§41**, (a) passes only on a declared-Anthropic affiliation or a registered (a)-7 vendor-direct source — no name/heritage/notability inference. A famous, well-funded OSS company is not an (a)-rescue. First **Firecrawl Inc. / Mendable AI** author → a **#19 19a** institutional data-point. Clean FAIL, no axis.

### (b) Goal-relevance — **STRONG (keys the tier)**
Firecrawl is canonical **web-data-ingestion substrate for agents/LLMs** — the layer that feeds RAG pipelines and grounds autonomous agents. It ships **first-class Claude support** (a first-party MCP server + a Firecrawl Skill for Claude Code) and is **directly pilotable** into the vault's own Claude Code (open-web research) and into hireui (candidate/company enrichment, behind fences). Web-data-for-agents is dead-center on Goal #1.

STRONG-not-STRONGEST because: (i) third-party; (ii) one of *many* web-scraping tools (Jina/crawl4ai/Spider/Apify…); (iii) Claude is one of several consumers (9 SDKs, MCP-agnostic); (iv) it is a *capability-augmentation layer* (it feeds the agent, it is not the agent). Cleanly GA — no §40 rescue needed; this is genuinely on-goal.

### (c) Substance / engineering — **STRONG**
A mature, world-canonical platform: 8 endpoints (scrape/search/crawl/map/extract/interact/agent/batch), 5 output formats, 9-language SDKs, a first-party MCP server, a self-hostable AGPL core + a paid cloud, 35 releases to v2.11.0, YC + $16.2M funding, 350k+ users. Caveats (see Deep Dive §9): **NOT source-cloned** (README/vendor-stated engineering); stars **page-stated §37.4** (NOT #52); vendor metrics ("96% of the web," "P95 3.4s") unverified; the hard part is anti-bot/proxy *infrastructure* not novel *AI*; AGPL network copyleft; web-scraping ToS/legal gray zone.

### (d) Cross-references — **STRONG**
Direct predecessor **crawl4ai v29**; adjacent **Scrapling v149**, **Agent-Reach v174** (§C), **markitdown v28**, **PixelRAG v211**, **browser-use v41 / Skyvern v24**, **camofox v179** (§C); the RAG/web-ingestion thread; #18 B1-MCP; #84 84c; the open-core/OSS-with-cloud thread; corpus-recursive dependency of rowboat v43 / awesome-llm-apps v201 / claude-seo v64; hireui web-data enrichment.

---

## Pattern outcome: **1 NEW §C standalone at N=2 (NOT corpus-first, NOT world-first)**

**"Web-Crawl / Web-Data-to-LLM-Ready-Markdown-&-Structured-Data Capability Layer for Agents"** — arbitrary-URL scrape/crawl/map/search/extract → clean Markdown + structured JSON + screenshots, handling JS-rendering/anti-bot/rotating-proxies/PDFs at scale; delivered as hosted API + self-hostable OSS service + multi-language SDKs + first-party MCP server + agent Skill.

**Anchors:** N=1 **crawl4ai v29** (`unclecode`, "LLM Friendly Web Crawler & Scraper," 64.4k★, Apache-2.0 — the un-registered pre-§C-registry first instance, credited) + N=2 **Firecrawl v214**.

### Why MINT (the load-bearing reasoning)
This is the exact **camofox v179 / codebase-memory-mcp v172 / Strix v190** precedent — a genuinely-distinct, recurring, *tool/capability-shaped* agent-capability whose **first corpus instance (crawl4ai v29) predates the §C registry** (verified: the §C rows are all v170+; there is **no** web-scraping/web-data §C standalone). The precedent is: mint the species row at **N=2**, crediting the pre-registry first instance (NOT corpus-first).

Consistency check — the §C registry already mints agent-**capability-layers** at this exact granularity: **Agent-Reach v174** (web read+search), **fff v194** (file search), **OfficeCLI v206** (office docs), **camofox v179** (stealth browser). A **web-crawl-to-LLM-data capability layer** is the same *kind* of thing, is **genuinely distinct** from all 42 existing rows, and is currently **§C-unrepresented**. Refusing to mint here while having minted Agent-Reach's sibling web-capability-layer would be inconsistent.

Firecrawl's distinctive delivery (hosted-API-service + 9 SDKs + MCP + Skill) vs crawl4ai's self-run library = **within-species variation** — recorded, **NOT separately minted** (the camofox v179 "don't draw the circle around the delivery form" discipline).

### ⚠️ Reviewable alternative (operator / ~v221 audit): **NO MINT**
"Web scraping is a decades-old, broad category captured at the tier/pattern level (crawl4ai v29 was a T4 subject touching patterns #47/#48/#64 without a §C row); Firecrawl is instance-strengthening only." This is a legitimate anti-inflation reading (§28). I **leaned MINT** on: (i) the camofox v179 pre-registry-first-instance precedent being directly on point; (ii) the Agent-Reach v174 sibling-web-capability-layer consistency; (iii) genuine §C-unrepresentedness; (iv) the LLM-era framing being specific (arbitrary-web → clean LLM-ready markdown/JSON as an agent-consumable service, handling JS/anti-bot at scale), not "web scraping writ large." **Either reading → counts 46/11 UNCHANGED.**

### ⚠️ NOT a palmier-pro v192 N=3 (recorded so it is not mis-filed)
Firecrawl ships a first-party MCP server, but its **primary function IS being an agent/LLM web-data tool** — it is **agent-tool-FIRST**. So its MCP server belongs to the **agent-tool-first #18 B1-MCP family** (google_workspace_mcp v140 / OfficeCLI v206), **NOT** the palmier-pro v192 **"Product-First Native Application Retrofitted with a First-Party MCP Server"** standalone (which the v212 audit scoped to *products whose primary function is NOT being an agent tool* — a video editor, a SQL GUI). Firecrawl fails that clause → not a v192 instance. (The v213 geti "NOT a v192 N=3" discipline, applied to the MCP vector this time.)

### N-count honesty
Anchored at **N=2** on the tight "web → LLM-ready markdown/data" species (crawl4ai v29 + Firecrawl v214). **Scrapling v149** (adaptive scraping *library*, LV#21 framing) is an *adjacent* web-scraping-family subject — whether it counts toward N=3 is an **audit question, NOT self-counted** (the recorded-not-self-incremented discipline). A fully-independent 3rd same-species instance (Jina Reader / ScrapeGraphAI / Spider — or Scrapling if the audit merges it) would take the row toward CONFIRMED; ⚠️ but the audit should weigh promote-vs-hold carefully given the category's breadth.

---

## Secondary observations (recorded, NOT minted)

- **#18 B1-MCP** — `firecrawl-mcp-server` = one server, many MCP clients → instance-strengthening → **N≈13** (was ≈12 at v212). Capability (the §C standalone) vs distribution-structure (#18 B1) are different axes → **no double-count** (the v140/v192/v212 precedent).
- **#84 84c** — cross-harness: a Firecrawl Skill (agentskills.io) for Claude Code/Antigravity/OpenCode + 9-language SDKs. **NO N-bump.** Cross-ref to the first-party-agent-skill-packaging thread (TimesFM v193 / OfficeCLI v206 / geti v213). Firecrawl ships the **fullest agent-nativity stack** (MCP server **and** Skill **and** SDKs) yet seen in the corpus.
- **Open-core / OSS-with-hosted-Pro-cloud-tier on an AGPL base** — the v78-ECC Library-vocab #13 candidate; data-point (meetily v196 / PilotDeck v175 / marketingskills-Magister v202).
- **#19 19a** — first Firecrawl Inc. / Mendable AI author.
- **Corpus-recursive DEPENDENCY** — rowboat v43 (stack), awesome-llm-apps v201 (app content), claude-seo v64 (scraping tool) all *used* Firecrawl before it became a subject (the GitNexus-v33-in-cortex-hub-v181 shape). **NOT #57** (that's influence-citation the other direction).
- **#66 supply-chain / dual-use** — AGPL-3.0 network copyleft (hireui-productization blocker); web scraping = ToS/robots.txt/copyright/GDPR gray zone (README pushes responsibility to the user); the cloud egresses your queries + scraped content (data-residency for candidate data); install = `pip install firecrawl-py` / self-host Docker.

### NON-claims
NOT **#52** (~152k★ page-stated §37.4; ~43k Aug-2025 press → velocity unestablishable). NOT **#57** (Firecrawl is upstream — it doesn't cite corpus subjects). NOT **world-first** (Jina/ScrapeGraphAI/Spider/Apify/Bright Data). NOT **corpus-first** (crawl4ai v29). NOT a **v192 N=3** (agent-tool-first). NOT a **new top-level pattern** (max #85). NOT **source-cloned** (flagged). NOT the **first web-scraping subject** (crawl4ai v29; Scrapling v149).

---

## Tier & streak

- **Tier T2 Service** — self-hosted service / hosted API; the **world-canonical flagship** of its class (the agentmemory v66 / codegraph v70 / Agent-Reach v174 / camofox v179 / CLIProxyAPI v207 family).
- **Counts UNCHANGED 46 top-level patterns / 11 CONFIRMED Library-vocab.** §C live standalones **42 → 43**; tracked PROVISIONAL surface **≈49 → ≈50**.
- **Streak GA:73 → GA:74** (60 consecutive goal-aligned ships v153→v214).
- **§35 CLEAR** — window {v212 GA, v213 GA, **v214 GA**} = 0 OG.

---

## Pilot (one-line)

**On-goal + directly pilotable, but read-only-safe first + fence the candidate data.** ⭐ **A1 → C11 → D16:** read the endpoint + agent-nativity design (zero install) → install `firecrawl-py` (or the MCP server / Skill) against a **public, non-sensitive** target to prove the loop → spec a hireui *public-web enrichment* slice on an `agent-*` branch (company-site → structured JSON), **gated by a data-residency + ToS review** (self-host to keep data local vs cloud egress; candidate PII never scraped without legal sign-off), per hireui's CONSTITUTION (I-2 / I-8 / GitNexus-first; no LLM spend yet → design/spec). Full 24-method menu in `(C) firecrawl — Pilot Methods Menu.md`.
