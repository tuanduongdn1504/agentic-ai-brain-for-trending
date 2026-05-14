# Cluster 1 — README + 26 commands + features

> **Sources:** README.md (398 lines) + plugin.json + marketplace.json

## What claude-seo is

A **Tier-1 Claude Code plugin** for SEO analysis built around 26 `/seo` slash commands. The README's opening sentence (398 lines total) describes it as covering: "technical SEO, on-page analysis, content quality (E-E-A-T), content briefs, schema markup, image optimization, sitemap architecture, AI search optimization (GEO), local SEO, maps intelligence, semantic topic clustering, search experience optimization (SXO), SEO drift monitoring, e-commerce SEO, international SEO with cultural profiles, FLOW framework integration, Google SEO APIs (Search Console, PageSpeed, CrUX, GA4), PDF report generation, and strategic planning."

This is **the largest scope-statement of any T1 collection in the 63-wiki corpus** — comparable to mattpocock-skills v57 (general-purpose 19-skill) but **100% SEO-domain vertical**.

## Three install paths

| Method | Audience | Command |
|---|---|---|
| Plugin marketplace (Claude Code 1.0.33+) | Default for Claude Code users | `/plugin marketplace add AgriciDaniel/claude-seo` then `/plugin install claude-seo@agricidaniel-seo` |
| Manual Unix/macOS/Linux | Bash + git clone | `git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git && bash claude-seo/install.sh` |
| Manual Windows | PowerShell | `git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git && powershell -ExecutionPolicy Bypass -File claude-seo\install.ps1` |

The README explicitly rejects the `irm | iex` PowerShell one-liner pattern: *"Claude Code's own security guardrails flag `irm ... | iex` as a supply chain risk."* This is a **CORPUS-RARE explicit supply-chain-risk reasoning** in install docs (most T1 collections don't surface this concern).

## The 26 commands — full table

The README lists 26 slash commands organized by analysis type:

| Category | Commands | Count |
|---|---|---|
| **Page/site analysis** | `audit` / `page` / `technical` / `content` / `schema` / `sitemap` (incl. `generate`) / `images` (with `serp` + `optimize` subcommands) / `geo` | 8 |
| **Strategic planning** | `plan` (SaaS/local/ecommerce/publisher/agency) / `programmatic` / `competitor-pages` | 3 |
| **Local + Maps** | `local` / `maps` (with subcommands) | 2 |
| **International** | `hreflang` | 1 |
| **Google APIs** | `google` (GSC / PageSpeed / CrUX / Indexing / GA4) + `google report` (PDF/HTML) | 1 (multi-sub) |
| **Backlinks** | `backlinks` / `backlinks setup` / `backlinks verify` | 3 |
| **Community-contributed v1.9.0** | `cluster` / `sxo` / `drift baseline\|compare\|history` / `ecommerce` | 6 |
| **Extensions** | `firecrawl` / `dataforseo` / `image-gen` | 3 |

Total: **26 surface commands** — comparable density to professional SaaS SEO products (Ahrefs / Semrush) but exposed as natural-language slash commands inside Claude Code.

## Features the README highlights

### Core Web Vitals (CURRENT metrics — versioned-with-history discipline)

- **LCP** (Largest Contentful Paint): Target < 2.5s
- **INP** (Interaction to Next Paint): Target < 200ms
- **CLS** (Cumulative Layout Shift): Target < 0.1

The README *explicitly* notes: *"INP replaced FID on March 12, 2024. FID was removed from all Chrome tools on September 9, 2024."*

This is **deprecation-aware standards tracking** with specific dates — a corpus-rare discipline that motivates the NEW Pattern Library candidate "Living-Domain-Standards Tracking" (see Entity 3).

### E-E-A-T Analysis (versioned external authority)

*"Updated to September 2025 Quality Rater Guidelines"* — Experience / Expertise / Authoritativeness / Trustworthiness. The version-date is explicit, which is again rare in T1 docs.

### Schema Markup — deprecation-aware

The README spells out **3 specific deprecation events with dates**:

- **HowTo: Deprecated (Sept 2023)** — was rich-result-eligible, now no longer
- **FAQ: Restricted to gov/health sites (Aug 2023)** — narrowed from general-use
- **SpecialAnnouncement: Deprecated (July 2025)** — most recent deprecation

This is the **strongest deprecation-aware-schema discipline observed in the corpus to date** (62 prior wikis; no prior subject tracks 3 specific schema deprecations with dates).

### AI Search Optimization (GEO)

Targets 4 surfaces: Google AI Overviews / ChatGPT web search / Perplexity / "Other AI-powered search". This is the **GEO discipline that motivates Pattern Library tracking** of Generative Engine Optimization as a distinct discipline from classical SEO.

### Google SEO APIs — 4-tier credential model

| Tier | Auth | APIs unlocked |
|------|------|------|
| **0** | API key | PSI / CrUX / CrUX History |
| **1** | + OAuth/SA | + GSC / URL Inspection / Indexing |
| **2** | + GA4 config | + GA4 organic traffic |
| **3** | + Ads token | + Keyword Planner |

The 4-tier ladder is a **progressive-disclosure credential model** — users get value at Tier 0 without setup friction, and unlock more capabilities as they configure more credentials. This is corpus-relevant to Pattern #28 progressive-disclosure (extends to credentials, not just code/docs).

### Local SEO + Maps Intelligence

- Google Business Profile (GBP) optimization
- NAP (Name/Address/Phone) consistency auditing
- Citation + review analysis
- Geo-grid rank tracking + competitor radius mapping

### Quality Gates — hard-limit discipline

- **Warning at 30+ location pages**
- **Hard stop at 50+ location pages** (per programmatic-SEO discipline)
- **Programmatic SEO**: Warning at 100+ pages, **HARD STOP at 500+ without audit**

The "HARD STOP" wording (vs "warning") is a **CORPUS-RARE explicit anti-Goodhart-law discipline** — the plugin refuses to mass-generate pages without operator audit, even when it could mechanically produce them. Compare with the 2026-05-06 anspace Goodhart-incident in Storm Bear vault history — that incident motivated the I-2/I-8 hireui invariants. claude-seo bakes the same discipline into the audit pipeline by default.

## Architecture (high level — Cluster 2 has detail)

```
~/.claude/plugins/.../skills/seo/      # Main orchestrator
~/.claude/plugins/.../skills/seo-*/    # 25 sub-skills (auto-discovered)
~/.claude/plugins/.../agents/seo-*.md  # 18 sub-agents (auto-discovered)
```

The README's tree is compact (4 lines); the project CLAUDE.md ([Cluster 2](./cluster-2-architecture-and-skill-system.md)) has the 122-line architecture tree.

## Limitations — transparent honest disclosure

Verbatim from README:

> *"Sites that render content client-side without server-side rendering will produce false-negative findings on content, schema, headings, and meta in most subagents. The orchestrator and most subagents fetch raw HTML rather than executing JavaScript, so a single-page application that hydrates content in the browser will appear empty to the auditor."*

The README **proactively discloses the SPA/CSR limitation** and links to GitHub issue #11 as the tracked v2.0 epic. This is **honest-deficiency-disclosure discipline** — the plugin tells you what it CAN'T do, with a roadmap pointer. Corpus-rare (most T1 plugins describe capabilities not gaps).

Workaround offered: the `seo-visual` subagent uses Playwright when available to verify SPA renderings. Partial mitigation, not full coverage.

## Extensions section — 3 named MCP-server integrations

| Extension | What | MCP server |
|---|---|---|
| **DataForSEO** | Live SERP / keyword / backlinks / on-page / content / business listings / AI visibility / LLM mentions — 22 commands across 9 API modules | DataForSEO MCP (commercial; requires account) |
| **Banana (AI Image Gen)** | Generate SEO images (OG / hero / product / infographics) via Claude Banana Creative Director pipeline | `nanobanana-mcp` (sister product) |
| **Firecrawl** | Full-site crawling + URL discovery | Firecrawl MCP |

**MCP integration philosophy**: Extensions are **opt-in** with install-helper scripts (`./extensions/<name>/install.sh`). Plugin works **without** any extension — extensions enrich, don't gate, core functionality. This is **graceful-degradation discipline** at the extension boundary, matching the 4-tier Google credential model at the API boundary.

The README also names **Ahrefs MCP** (`@ahrefs/mcp`) and **Semrush MCP** as community-server integrations beyond the 3 named extensions.

## Ecosystem section — sister products

The README has an "Ecosystem" table naming 6 sister products:

| Skill | Function | Connection |
|---|---|---|
| Claude SEO (this) | SEO analysis, audits, schema, GEO | **Core** |
| Claude Blog | Blog writing, optimization, scoring | Companion (consumes SEO findings) |
| Claude Banana | AI image generation via Gemini | **Shared** (also bundled as extension) |
| Codex SEO | Codex-first port (TOML agents, deterministic runners) | **Port** (sister platform) |
| AI Marketing Claude | Copywriting / emails / social / ads / funnels / CRO | **Community** (third-party by zubair-trabzada) |
| FLOW | Evidence-led SEO framework (41 AI prompts, CC BY 4.0) | Knowledge base (powers `seo-flow` prompts) |

This is **Pattern #19 ecosystem-portfolio-builder evidence at maximum visibility** — the README itself markets the portfolio. See Entity 2 for full N=3 strengthening analysis.

Workflow example from README:
```
1. /seo audit https://example.com         → identify gaps + issues
2. /seo backlinks https://example.com     → link profile + competitor gaps
3. /blog write "target keyword"           → SEO-optimized post (sister product)
4. /seo image-gen hero "blog topic"       → hero image (banana extension)
5. /seo geo https://example.com/blog/post → AI-citation optimization
```

The workflow **chains 4 distinct products** (claude-seo / claude-blog / banana-claude / claude-seo's geo) — direct evidence that the portfolio is functionally coupled, not just naming-related.

## Community Contributors (v1.9.0) — Pro Hub Challenge

Five named contributors from AI Marketing Hub's Pro Hub Challenge:

| Contributor | Contribution |
|---|---|
| **Lutfiya Miller** (Winner) | Semantic Cluster Engine → `seo-cluster` |
| **Florian Schmitz** | SXO Skill → `seo-sxo` |
| **Dan Colta** | SEO Drift Monitor → `seo-drift` |
| **Chris Muller** | Multi-lingual SEO → `seo-hreflang` enhancements |
| **Matej Marjanovic** | E-commerce + DataForSEO Cost Config → `seo-ecommerce` + cost guardrails |

This is a **gamified-community-contribution mechanism** (a curated challenge with a winner) — distinct from awesome-claude-skills v50's "anyone can submit" curation OR mattpocock-skills v57's solo-author model. **NEW community-contribution sub-pattern observation** at v64 (potentially registers as Pattern Library candidate at v66).

## Author + branding

Built by **Agrici Daniel** (agricidaniel.com — "AI Workflow Architect"). The README footer links:
- Blog: deep dives on AI marketing automation
- YouTube channel: tutorials + demos (with embedded `/seo audit` demo gif)
- All open-source tools: github.com/AgriciDaniel

This is **personal-brand-portfolio-builder** authorship signature — sister to v63 forrestchang (Multica founder), v61 gotalab (solo-Japanese), v60 Alishahryar1 (solo-individual). See Entity 2 for Pattern #19 N=3 cross-archetype analysis.
