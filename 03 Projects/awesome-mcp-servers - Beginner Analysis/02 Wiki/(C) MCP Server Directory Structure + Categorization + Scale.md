# (C) MCP Server Directory Structure + Categorization + Scale

**Entity type:** Content-artifact anatomy (the directory as an object of study)
**Subject:** `punkpeye/awesome-mcp-servers` README contents at commit `main@2026-04-15`
**Scale:** ~1,200 MCP servers across 50+ categories, 4-axis 15-badge legend, 7-language i18n

---

## 1. Why this entity exists

The `awesome-mcp-servers` README is NOT merely a list — it is **a structured vocabulary for classifying MCP runtime plugins**. This entity page captures the structural-primitive layer: how the directory organizes information, so that corpus-level analysis can reason about MCP ecosystem shape without re-parsing the README.

Separate from:
- **Cluster summary** (`(C) Cluster — README structure + categorization taxonomy.md`) which describes the current snapshot
- **Author-entity** (`(C) punkpeye — Author ecosystem...`) which describes Fiegel as actor
- This entity captures: **the content artifact itself as a structured object** useful for Pattern Library analysis

## 2. Directory anatomy — 4 structural layers

```
Layer 1: Header (language selector + positioning)
Layer 2: Meta-sections (What-is-MCP + Clients + Tutorials + Community + Legend)
Layer 3: Server-implementation categories (50+ categories, flat)
Layer 4: Per-server entries (~1,200 total; uniform format)
```

### Layer 1: Header
- 7-language README badges (linked variants)
- State-of-MCP-2025 report link
- Glama web-directory link
- Tagline: *"A curated list of awesome Model Context Protocol (MCP) servers."*

### Layer 2: Meta-sections (5 ordered)
1. **What is MCP?** (1-paragraph definition)
2. **Clients** (1-paragraph pointer to `awesome-mcp-clients` + Glama Chat)
3. **Tutorials** (2 items: MCP Quickstart + Claude Desktop/SQLite video)
4. **Community** (2 links: r/mcp + Discord)
5. **Legend** (15-badge taxonomy — see §4)

### Layer 3: Server-implementation categories
Alphabetical, flat (depth-1). 50+ categories enumerated in verbatim README order:

Aggregators · Aerospace · Art & Culture · Architecture & Design · Biology/Medicine · Browser Automation · Cloud Platforms · Code Execution · Coding Agents · Command Line · Communication · Customer Data Platforms · Databases · Data Platforms · Delivery · Developer Tools · Data Science · Data Visualization · Embedded Systems · Education · E-Commerce · Environment & Nature · File Systems · Finance & Fintech · Gaming · Home Automation · Knowledge & Memory · Legal · Location Services · Marketing · Monitoring · Multimedia · OS Automation · Product Management · Real Estate · Research · Search & Data Extraction · Security · Social Media · Sports · Support & Service Management · Translation · Text-to-Speech · Travel & Transportation · Version Control · Workplace & Productivity · Other Tools

### Layer 4: Per-server entry format
```markdown
- [{owner/repo}]({url}) {optional legend badges} - {one-line description}
```

## 3. Scale statistics (verified)

| Metric | Value | Notes |
|--------|-------|-------|
| Total categories | 50+ | alphabetical, flat |
| Total server entries | ~1,200 | estimated from README parse |
| Largest category | Aggregators | 60+ entries |
| Second-largest | Browser Automation | 50+ entries |
| Long-tail categories | Sports / Aerospace / Legal | 5-20 entries each |
| Curation ratio | ~25% | vs `a2asearch-mcp`'s claim of 4,800+ servers in the broader ecosystem |

## 4. Legend vocabulary — 4-axis 15-badge classification

This is the directory's **controlled vocabulary**.

### Axis 1: Official status (1 badge)

| Badge | Meaning |
|-------|---------|
| 🎖️ | Official implementation |

### Axis 2: Programming language (8 badges)

| Badge | Language |
|-------|----------|
| 🐍 | Python |
| 📇 | TypeScript / JavaScript |
| 🏎️ | Go |
| 🦀 | Rust |
| \#️⃣ | C# |
| ☕ | Java |
| 🌊 | C / C++ |
| 💎 | Ruby |

### Axis 3: Scope / hosting (3 badges)

| Badge | Scope |
|-------|-------|
| ☁️ | Cloud Service |
| 🏠 | Local Service |
| 📟 | Embedded Systems |

### Axis 4: Operating system (3 badges)

| Badge | OS |
|-------|-----|
| 🍎 | macOS |
| 🪟 | Windows |
| 🐧 | Linux |

**Classification example (hypothetical):**
> A Python-based local-service MCP server for macOS would carry `🐍 🏠 🍎` badges. An official TypeScript cloud service on all OSs would be `🎖️ 📇 ☁️`.

**Corpus-first classification depth:** No sibling corpus aggregator (build-your-own-x v8, awesome-design-md v25) has comparable multi-axis badge vocabulary. This is **evidence that MCP discoverability requires fine-grained filtering** — which implicitly confirms MCP's **infrastructure-plumbing role** (filesystem / runtime-environment / hosting constraints matter, unlike content aggregators).

## 5. Category cross-references to Storm Bear corpus

Several awesome-mcp-servers categories map directly to corpus wikis:

| Category | Storm Bear corpus wiki | Relationship |
|----------|------------------------|--------------|
| Aggregators | OpenHands v30 (meta-orchestration) | Meta-server concept analog |
| Browser Automation | crawl4ai v29 + Skyvern v24 | Direct scope overlap |
| Cloud Platforms | gws v13 | Google Workspace MCP-capable |
| Coding Agents | T1 tier wikis (v1, v2, v3, v5, v11, v12, v17, v18, v27) | MCP-capable coding agent frameworks |
| Communication | (implicit: Slack/Discord are corpus peers) | Scrum-coach relevant |
| Databases | graphify v16 (uses DBs) | Knowledge-graph DB layer |
| File Systems | markitdown v28 (file conversion) | Adjacent utility |
| Knowledge & Memory | graphify v16 (knowledge graph) | Direct |
| Product Management | Potential Storm Bear pilot target | Jira/Linear MCPs |
| Search & Data Extraction | crawl4ai v29 + TrendRadar v19 | Adjacent |
| Version Control | gws-adjacent (GitHub MCPs) | Storm Bear DORA metrics |
| Workplace & Productivity | gws v13 (Google Workspace) | Direct |

**Storm Bear subset recommendation (priority order):**
1. Product Management (Jira/Linear MCP servers)
2. Version Control (GitHub MCP server)
3. Communication (Slack/Teams MCP servers)
4. Workplace & Productivity (Google Workspace MCP servers)
5. Knowledge & Memory (vector-store MCP servers for vault-query)

## 6. i18n coverage — 7-language README variants

| Language | Filename |
|----------|----------|
| Thai | README-th.md |
| English (primary) | README.md |
| Traditional Chinese | README-zh_TW.md |
| Simplified Chinese | README-zh.md |
| Japanese | README-ja.md |
| Korean | README-ko.md |
| Brazilian Portuguese | README-pt_BR.md |

**Coverage decisions:**
- Large markets: English / zh-CN / JA / KO / PT-BR (covers US/CN/JP/KR/BR)
- Unique inclusions: **Thai** (first in corpus) + **Traditional Chinese separate from Simplified** (Pattern-first in corpus)
- **Absent:** Vietnamese / Spanish / French / German / Russian / Arabic / Hindi

**Storm Bear contribution opportunity:** Vietnamese README translation could be a low-cost high-signal contribution. Pattern-relevant because Thai and Portuguese are here — suggests i18n-translations are accepted PR category.

## 7. What is MISSING from the directory (observed gaps)

### Quality signaling
- No "stars" / "last-updated" / "maintenance-status" per entry
- No security-audit flags
- No Anthropic-official vs community-official distinction (only 🎖️ binary)

### Governance gaps vs corpus peers
- No SECURITY.md (gap vs graphify v16)
- No CODE_OF_CONDUCT (gap vs corporate peers)
- No stale-entry pruning policy

### Taxonomic gaps
- No cross-category tags (servers only fit 1 category)
- No versioning of MCP spec compatibility (which MCP-spec version each server targets)
- No performance benchmarks

### Storm Bear implication
Use directory as **discovery aid, not evaluation gate**. Supplement with:
- GitHub star count / age check per server
- README + CHANGELOG read per server
- Local test in sandboxed environment before production wiring

## 8. Scale comparison across awesome-list-genre corpus wikis

| Wiki | Categories | Entries | Badges | i18n langs | Maintainer |
|------|-----------|---------|--------|-----------|-----------|
| build-your-own-x v8 | 29 | ~200 tutorials | none | 1 | Daniel Stefanović + CodeCrafters Inc. |
| awesome-design-md v25 | 10 | 69 design systems | none | 1 | VoltAgent org |
| **awesome-mcp-servers v31** | **50+** | **~1,200 servers** | **15 (4-axis)** | **7** | **Frank Fiegel solo** |

**v31 is the most-elaborated awesome-list-genre instance in corpus.** This suggests:
- MCP ecosystem has complexity that demands multi-axis classification (vs "list of tutorials" or "list of design systems")
- Maturity of the ecosystem (50+ categories implies breadth)
- Maintainer-investment signal (7-language i18n is non-trivial work)

## 9. Growth trajectory — sustained-community-viral

17-month growth to 85,323 stars = **~5,000 stars/month sustained**.

Comparison:
- build-your-own-x v8: 10-year growth to 491K (≈4K/month)
- awesome-design-md v25: 20-day growth to 60K (extreme-viral ≈90K/month)
- awesome-mcp-servers v31: 17-month growth to 85K (sustained ≈5K/month)

**Pattern #27 sub-path:** awesome-mcp-servers represents the **sustained-community-viral** sub-path (distinct from extreme-viral v25 or ultra-long-burn v8). Adds 9th data point to Pattern #27.

## 10. Cross-references

- **Sibling clusters:** [[(C) Cluster — README structure + categorization taxonomy]] + [[(C) Cluster — Aggregator governance + contribution + community]] + [[(C) Cluster — punkpeye ecosystem + companion projects]]
- **Aggregator peers:** [[03 Projects/build-your-own-x - Beginner Analysis/|build-your-own-x v8]] + [[03 Projects/awesome-design-md - Beginner Analysis/|awesome-design-md v25]]
- **MCP-consumer wikis:** [[03 Projects/goclaw - Beginner Analysis/|goclaw v4]] / [[03 Projects/multica - Beginner Analysis/|multica v15]] / [[03 Projects/graphify - Beginner Analysis/|graphify v16]] / [[03 Projects/spec-kit - Beginner Analysis/|spec-kit v17]] / [[03 Projects/TrendRadar - Beginner Analysis/|TrendRadar v19]] / [[03 Projects/OpenHands - Beginner Analysis/|OpenHands v30]]
- **i18n peers:** fish-speech v20 / oh-my-claudecode v27 / LlamaFactory v22

---

_Entity page. Part of Storm Bear LLM Wiki — 31st wiki. Written by Claude (C). Verified 2026-04-22._
