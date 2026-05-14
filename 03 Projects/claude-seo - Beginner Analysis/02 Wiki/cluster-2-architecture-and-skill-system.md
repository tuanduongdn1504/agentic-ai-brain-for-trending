# Cluster 2 — Architecture + skill system

> **Sources:** CLAUDE.md (210 lines, Claude-Code-specific) + AGENTS.md (126 lines, multi-platform) + plugin.json + marketplace.json + skills/ tree

## The 3-layer architecture (author's vocabulary)

The author's CLAUDE.md opens with: *"This repository contains Claude SEO, a Tier 4 Claude Code skill for comprehensive SEO analysis across all industries. It follows the Agent Skills open standard and the **3-layer architecture (directive, orchestration, execution)**."*

**Important vocabulary note**: The author's **"Tier 4"** is the AUTHOR'S internal vocabulary for skill-collection-architecture-tier (3-layer architecture). **It is NOT the Storm Bear vault corpus T1-T5 tier system.** The vault classifies claude-seo as **T1 Augmentation** (skill collection inside Claude Code surface). Both vocabularies coexist; this wiki uses corpus T1.

### Layer 1: Directive
- **CLAUDE.md** (210 lines, Claude-Code-specific) — project rules, security, report generation, ecosystem links
- **AGENTS.md** (126 lines, multi-platform) — Cursor / Cursor Cloud / Antigravity / Gemini CLI invocation patterns

### Layer 2: Orchestration
- **`skills/seo/SKILL.md`** — main orchestrator with routing table for 26 slash commands
- **`skills/seo/references/`** — 12 on-demand knowledge files (loaded progressively, not eagerly)

### Layer 3: Execution
- **`skills/seo-*/SKILL.md`** — 24 sub-skill SKILL.md files (auto-discovered)
- **`agents/seo-*.md`** — 18 sub-agent definitions (auto-discovered, invoked via Agent tool not Bash)
- **`scripts/*.py`** — 30 tracked Python scripts (+ 2 dev-only)

## Auto-discovery via Anthropic plugin spec

Per CLAUDE.md, **plugin.json deliberately omits per-skill/per-agent file-path arrays**. Instead:

- `skills/*/SKILL.md` files are auto-discovered by Claude Code
- `agents/seo-*.md` files are auto-discovered by Claude Code

This is the **directory-auto-discovery pattern** that Anthropic's plugin spec endorses. The CHANGELOG v1.6.1 (2026-03-27) explicitly notes this transition: *"Removed non-standard `entry_point` field and individual file-path arrays for `skills`/`agents`. All 17 skills and 11 agents now rely on directory auto-discovery per Anthropic plugin spec."* (counts have grown to 25/18 since.)

**Cross-corpus relevance**: this confirms Pattern #18 sub-archetype "auto-discovery-via-directory-convention" as a stable T1 mechanism (also observed in mattpocock-skills v57 / awesome-claude-skills v50 / agent-skills-of-vercel v51).

## CLAUDE.md vs AGENTS.md — the multi-platform split

A **deliberate architectural separation** that distinguishes claude-seo from the karpathy-skills v63 single-skill manual-sync approach:

### CLAUDE.md (210 lines) — Claude Code specific
- Architecture tree
- Commands table (26 slash commands with `/seo` namespace)
- Development Rules (kebab-case naming / under-500-line SKILL.md / Agent tool not Bash / venv at `~/.claude/skills/seo/.venv/`)
- Security Rules (URL validation / no committed credentials / no hardcoded paths / config at `~/.config/claude-seo/`)
- **Report Generation Rules** (canonical generator = `scripts/google_report.py`; matplotlib 200 DPI + WeasyPrint A4 PDF + specific color palette navy #1e3a5f + Times New Roman; post-generation `_review_pdf()` quality gate)
- Cross-skill enforcement rule: *"After completing ANY analysis command, offer: 'Generate a PDF report? Use `/seo google report`'"*

### AGENTS.md (126 lines) — Multi-platform Cursor / Antigravity / Gemini CLI
- Quick Reference table (26 commands — same as CLAUDE.md)
- **Cursor-specific section**: *"Cursor reads this file automatically. All SKILL.md files contain the full analysis logic as natural language instructions. Python scripts in `scripts/` provide execution capabilities."*
- **Cursor Cloud gotchas** explicitly documented:
  - SSL certificates may not resolve for some domains — investigate the cert issue rather than disabling verification
  - PATH may not include Python venv → use full path `~/.claude/skills/seo/.venv/bin/python`
  - Screenshots save to `/tmp/` not CWD → check absolute paths
- **Antigravity-specific**: discovers project via `plugin.json` at repo root; install path `~/.gemini/antigravity/plugins/claude-seo/`
- Same Architecture tree + Key Principles + Credits

### The split discipline

AGENTS.md says explicitly: *"For Claude Code users: see CLAUDE.md instead."*
CLAUDE.md implicitly assumes Claude Code only.

This is **per-platform-file-routing** — each platform reads its native file (Claude Code → CLAUDE.md; Cursor → AGENTS.md; Antigravity → AGENTS.md). **The skill content lives in SKILL.md files (shared), but the platform-invocation guidance lives in the platform-specific top-level file.**

This is a **distinct mechanism from karpathy-skills v63's manual-sync** (which keeps single SKILL.md file synced across 2 platforms). claude-seo's mechanism is:

- **SHARED skill content** (SKILL.md files = same across platforms)
- **PER-PLATFORM dispatch file** (CLAUDE.md vs AGENTS.md = different per platform; describe HOW to invoke)

Pattern #18 implication: this is a **NEW Layer 1 sub-archetype** ("shared-content-with-per-platform-dispatch-file"), distinct from Layer 2's "format-translation-installer" (cc-sdd v61) and "runtime-protocol-translation" (free-claude-code v60). See Entity 4 for full Pattern #18 analysis.

## 25 sub-skills inventory

Per CLAUDE.md architecture tree:

**Orchestrator (1):**
- `seo/SKILL.md` — main entry + routing + core rules + 12 on-demand reference files

**Core analysis sub-skills (21):**
- `seo-audit/` — Full site audit with parallel agents
- `seo-page/` — Deep single-page analysis
- `seo-technical/` — Technical SEO (9 categories)
- `seo-content/` — E-E-A-T and content quality
- `seo-content-brief/` — Content brief generation (community PR #56, v1.9.7)
- `seo-schema/` — Schema.org markup detection/generation
- `seo-sitemap/` — XML sitemap analysis/generation
- `seo-images/` — Image optimization analysis
- `seo-geo/` — AI search / GEO optimization
- `seo-local/` — Local SEO (GBP, citations, reviews, map pack) — v1.6.0
- `seo-maps/` — Maps intelligence (geo-grid, GBP audit, reviews, competitors) — v1.6.0
- `seo-plan/` — Strategic SEO planning by industry
- `seo-programmatic/` — Programmatic SEO at scale
- `seo-competitor-pages/` — Competitor comparison pages
- `seo-hreflang/` — International SEO / hreflang (cultural profiles by Chris Muller v1.9.0)
- `seo-google/` — Google SEO APIs (with `references/` 10 API reference files) — v1.7.0
- `seo-backlinks/` — Backlink profile analysis (Moz / Bing / Common Crawl / verify) — v1.7.2
- `seo-cluster/` — Semantic topic clustering (Lutfiya Miller, Pro Hub Challenge Winner v1.9.0)
- `seo-sxo/` — Search Experience Optimization (Florian Schmitz v1.9.0)
- `seo-drift/` — SEO drift monitoring with SQLite + 17 comparison rules (Dan Colta v1.9.0)
- `seo-ecommerce/` — E-commerce SEO (Matej Marjanovic v1.9.0)

**Framework integration (1):**
- `seo-flow/` — FLOW framework integration (41 evidence-led CC BY 4.0 prompts; v1.9.5)

**Extension mirrors (2):**
- `seo-dataforseo/` — Live SEO data via DataForSEO MCP (extension)
- `seo-image-gen/` — AI image generation for SEO assets (extension)

**Total: 25 sub-skills** = 21 core + 1 orchestrator + 1 framework integration + 2 extension mirrors

## 18 sub-agents inventory

Per CLAUDE.md `agents/` listing:

**Core analysis agents (15):**
- `seo-technical.md` — Crawlability, indexability, security
- `seo-content.md` — E-E-A-T, readability, thin content
- `seo-schema.md` — Structured data validation
- `seo-sitemap.md` — Sitemap quality gates
- `seo-performance.md` — Core Web Vitals, page speed
- `seo-visual.md` — Screenshots, mobile rendering (Playwright)
- `seo-geo.md` — AI crawler access, GEO, citability (added v1.4.0)
- `seo-local.md` — GBP, NAP, citations, reviews, local schema (added v1.6.0)
- `seo-maps.md` — Geo-grid, GBP audit, reviews, competitor radius (added v1.6.0)
- `seo-google.md` — Google API analyst (CrUX, GSC, GA4) (added v1.7.0)
- `seo-backlinks.md` — Backlink profile analyst (added v1.7.2)
- `seo-cluster.md` — Semantic clustering analysis (added v1.9.0)
- `seo-sxo.md` — Search experience optimization (added v1.9.0)
- `seo-drift.md` — SEO drift monitoring (added v1.9.0)
- `seo-ecommerce.md` — E-commerce SEO analysis (added v1.9.0)

**Framework integration (1):**
- `seo-flow.md` — FLOW prompt application (added v1.9.5; security-hardened in v1.9.6 with 10 VULN fixes)

**Extension mirror agents (2):**
- `seo-dataforseo.md` — DataForSEO data analyst
- `seo-image-gen.md` — SEO image audit analyst

**Total: 18 sub-agents** = 15 core + 1 framework integration + 2 extension mirrors

**Audit pipeline parallelism**: orchestrator spawns **up to 15 subagents simultaneously** during `/seo audit` (was 12 pre-v1.9.0; expanded with seo-cluster + seo-sxo + seo-drift + seo-ecommerce). All agents declare `model: sonnet` and `maxTurns` (15-25) per v1.6.1 standardization.

## 30 Python scripts — execution layer

Per CLAUDE.md, the `scripts/` directory holds **30 tracked + 2 dev-only**:

**Credential management (2):**
- `google_auth.py` — OAuth / SA / API key / 4-tier detection
- `backlinks_auth.py` — Moz / Bing API credential management

**Backlink APIs (4):**
- `moz_api.py` — Moz Link Explorer (DA/PA, spam, domains, anchors)
- `bing_webmaster.py` — Bing Webmaster Tools
- `commoncrawl_graph.py` — Common Crawl web graph parser (PageRank, in-degree)
- `verify_backlinks.py` — Backlink existence verification

**Google APIs (10):**
- `pagespeed_check.py` / `crux_history.py` / `gsc_query.py` / `gsc_inspect.py` / `indexing_notify.py` / `ga4_report.py` / `google_report.py` / `youtube_search.py` / `nlp_analyze.py` / `keyword_planner.py`

**Page/HTML utilities (4):**
- `fetch_page.py` (UA rotation; Googlebot detection v1.4.0)
- `parse_html.py` (lazy-load detection v1.9.9: 5 mechanisms)
- `capture_screenshot.py` (Playwright)
- `analyze_visual.py`

**SEO drift (4):**
- `drift_baseline.py` / `drift_compare.py` (17 rules / 3 severity levels) / `drift_report.py` / `drift_history.py` — all with SQLite persistence

**E-commerce + DataForSEO (3):**
- `dataforseo_costs.py` — Cost estimation + budget tracking
- `dataforseo_merchant.py` — Google Shopping / Amazon
- `dataforseo_normalize.py` — Response normalization

**FLOW framework sync (1):**
- `sync_flow.py` — GitHub API sync of CC BY 4.0 prompts with `--dry-run` and `--ref <sha>` pinning + 10 security hardenings v1.9.6

**Dev-only (2, gitignored):**
- `mobile_analysis.py` (gitignored)

**Total: ~30 scripts** (CLAUDE.md says "30 tracked + 2 dev-only").

## Development Rules (CLAUDE.md verbatim)

- Keep SKILL.md files under **500 lines / 5000 tokens** (matches Anthropic guidance)
- Reference files focused and under **200 lines**
- Scripts must have **docstrings, CLI interface, and JSON output**
- Follow **kebab-case** naming for skill directories
- Agents invoked via **Agent tool, never via Bash**
- Python dependencies install into **`~/.claude/skills/seo/.venv/`**
- Test with **`python -m pytest tests/`** after changes (if applicable)

These are corpus-standard Anthropic-spec-compliance rules — consistent with mattpocock-skills v57 / agent-skills-of-vercel v51 / cc-sdd v61.

## Security Rules (CLAUDE.md verbatim)

- **Never commit credentials**: `.env`, `client_secret*.json`, `oauth-token.json`, `service_account*.json` all in `.gitignore`
- **URL validation**: All scripts that accept user URLs **must call `validate_url()`** from `google_auth.py` — blocks private IPs, loopback, and GCP metadata endpoints (SSRF protection)
- **OAuth tokens**: Never store `client_secret` in the token file — read from `client_secret.json` at runtime
- **No hardcoded paths**: Use `os.path.dirname(os.path.abspath(__file__))` for relative paths, never `/home/username/...`
- **Config location**: `~/.config/claude-seo/google-api.json` + `~/.config/claude-seo/backlinks-api.json` (user-space, NOT in repo)

**Security maturity**: claude-seo's security rules are **enforced via CI manifest-guard** (13 assertions per CHANGELOG v1.9.9), and the v1.9.6 release shipped **10 named VULN fixes** (VULN-A01 through VULN-A10) for the seo-flow agent. This is a **CORPUS-RARE explicit-vulnerability-IDs discipline** — most subjects describe security as a category, not as numbered findings with severity levels.

## Report Generation Rules — opinionated canonical generator

CLAUDE.md mandates `scripts/google_report.py` as the **single canonical report generator** with:

- **Dependencies**: matplotlib≥3.8.0 (charts) + weasyprint≥61.0 (HTML→PDF) — both in requirements.txt
- **Format**: A4 PDF via WeasyPrint + matplotlib charts at 200 DPI
- **Style**: Clean white title page, navy (#1e3a5f) accent, Times New Roman body font
- **Color palette** (named hex values):
  - Navy `#1e3a5f` (headers)
  - Dark gold `#b8860b` (accents)
  - Forest green `#2d6a4f` (pass)
  - Warm amber `#d4740e` (warnings)
  - Deep red `#c53030` (fail)
  - Warm cream `#faf9f7` (backgrounds)
- **Structure**: Title page → TOC with scores → Executive Summary → Data sections → Recommendations → Methodology
- **Charts**: 85% width / max-height 120mm / captions on every chart / saved to `charts/` at 200 DPI
- **`page-break-inside: avoid` is BANNED** (causes white gaps in WeasyPrint — verified bug-avoidance rule)
- **Post-generation review**: `_review_pdf()` runs automatically (checks empty images / thin sections / duplicates)
- **Gate**: Before presenting any PDF to user, **verify review passes (`"status": "PASS"`)**
- **Cross-skill enforcement**: After completing ANY analysis command, offer "Generate a PDF report? Use `/seo google report`"
- **Google logo** on title page when using Google API data ("Powered by Google APIs")

**This level of report-generation prescriptive-discipline is unique in the T1 corpus** — most subjects describe output formats casually; claude-seo enforces a brand-consistent, bug-free, automatically-reviewed PDF pipeline as a project invariant.

## Plugin manifest (plugin.json + marketplace.json)

`.claude-plugin/plugin.json` — current version **1.9.9** (per CHANGELOG 2026-05-11):
- Skills + agents: auto-discovered (no per-file paths)
- Keywords: 14 (added in v1.9.8 marketplace polish)
- Author: name / email / URL (parity-enforced with marketplace.json per CI assertion `test_marketplace_metadata_and_author_parity`)

`.claude-plugin/marketplace.json`:
- `metadata.description`: includes both "25 sub-skills" + "18 sub-agents" counts (CI-enforced parity with plugin.json)
- `plugins[0].description`: same canonical phrasing
- `category: "marketing"`
- `homepage: https://claude-seo.md`

**CI manifest-guard (13 assertions, per CHANGELOG v1.9.9):** ensures plugin.json + marketplace.json + all SKILL.md frontmatter `metadata.version` + Sub-Skills/Subagents lists ALL agree on counts and version. Drift between any 2 sources fails CI. This is the **strongest manifest-consistency discipline observed in the corpus**.

## Hooks (`hooks/hooks.json`)

`hooks/hooks.json` declares **PostToolUse schema validation hooks**. CLAUDE.md mentions this minimally; the v1.9.6 security release notes confirm hooks exist as part of quality gates.

## Key Principles (CLAUDE.md verbatim)

1. **Progressive Disclosure**: Metadata always loaded, instructions on activation, resources on demand
2. **Industry Detection**: Auto-detect SaaS / e-commerce / local / publisher / agency
3. **Parallel Execution**: Full audits spawn up to 15 subagents simultaneously
4. **Extension System**: DataForSEO MCP for live data, Firecrawl MCP for site crawling, Banana MCP for AI image generation

Principle #1 is **Pattern #28 progressive-disclosure** in action — claude-seo doesn't load all 25 skills + 18 agents + 30 scripts into context eagerly. Each gets loaded on-demand per command invocation. This is consistent with mattpocock-skills v57 / cc-sdd v61 / agent-skills-of-vercel v51.

Principle #3 (15-parallel-subagent ceiling) is **CORPUS-LARGEST parallel-agent-spawn in any T1 audit pipeline** observed to date.

## Release Blog Post automation

CLAUDE.md final section describes a `/release-blog` slash command that generates a release blog post on `https://claude-seo.md/blog/`:
- Cover image generation (via banana extension presumably)
- SEO metadata
- FAQ schema
- Internal linking
- Sitemap/llms.txt updates
- Vercel deployment
- Google indexing

**This is a corpus-first observation: the plugin ships a meta-command that self-promotes its own releases on its own marketing site.** Sister to oh-my-claudecode v27 mini-blog mechanism but at higher automation level (full deploy + indexing pipeline). Pattern Library candidate consideration deferred to v66 — observational at this stage.
