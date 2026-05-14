# Entity 1 — claude-seo core artifact + 3-layer architecture

> **Type:** Foundation entity (what the plugin IS)
> **Cross-references:** [Cluster 1 commands](./cluster-1-readme-and-commands.md) / [Cluster 2 architecture](./cluster-2-architecture-and-skill-system.md)

## Identity

| Field | Value |
|---|---|
| **Full name** | Claude SEO — Universal SEO Analysis Skill for Claude Code |
| **Author** | [Agrici Daniel](https://agricidaniel.com/about) — "AI Workflow Architect" |
| **Repo** | [`github.com/AgriciDaniel/claude-seo`](https://github.com/AgriciDaniel/claude-seo) |
| **License** | MIT (+ CC BY 4.0 carve-out for bundled FLOW 41 prompts) |
| **Current version** | v1.9.9 (2026-05-11) — final 1.x patch; v2 in design |
| **First release** | v1.0.0 (2026-02-07) — ~95 days at v64 wiki ship |
| **Stars / forks / watchers** | 6,494 / 993 / 66 |
| **Stars-per-day** | ~68 (medium-high engagement; **15.3% fork ratio = corpus-rare high active-deployment**) |
| **Topics (GitHub)** | claude-code / skill / seo / ai-search / generative-engine-optimization / e-e-a-t / structured-data / schema-markup / core-web-vitals / search-console / ahrefs-mcp / semrush-mcp / local-seo / cultural-seo |

## Function

A **Tier-1 Claude Code plugin** providing 26 `/seo` slash commands for SEO analysis covering:

- **Technical SEO** (9 categories) — crawlability / indexability / security / performance / mobile / structured data / canonicals / redirects / hreflang
- **Content quality** — E-E-A-T (September 2025 Quality Rater Guidelines), readability, thin content detection
- **Schema markup** — JSON-LD detection / validation / generation with deprecation awareness
- **Sitemap architecture** — analysis + generation with industry templates
- **Image optimization** — alt text / filename / lazy-loading / WebP/AVIF / IPTC/XMP / image SERP
- **AI search (GEO)** — AI Overviews / ChatGPT / Perplexity / passage citability
- **Local SEO + Maps** — GBP / NAP / citations / reviews / geo-grid / competitor radius
- **International SEO** — hreflang + 4 cultural adaptation profiles (DACH / Francophone / Hispanic / Japanese)
- **Google APIs** — GSC / PageSpeed / CrUX / Indexing / GA4 + PDF report generation
- **Backlinks** — Moz / Bing Webmaster / Common Crawl / DataForSEO
- **Semantic clustering + SXO + Drift monitoring + E-commerce** (community v1.9.0)
- **Strategic planning + Programmatic SEO + Competitor pages** (with hard-limit quality gates)
- **FLOW framework integration** — 41 evidence-led prompts (CC BY 4.0)

## The 3-layer architecture (author's vocabulary)

Per `CLAUDE.md` line 1-14:

```
Layer 1: Directive            CLAUDE.md (210 lines, Claude Code) + AGENTS.md (126 lines, multi-platform)
Layer 2: Orchestration        skills/seo/SKILL.md (routing) + skills/seo/references/ (12 on-demand)
Layer 3: Execution            skills/seo-*/SKILL.md (24) + agents/seo-*.md (18) + scripts/*.py (30)
```

The author calls the architecture "Tier 4" — **this is the author's internal vocabulary for the 3-layer skill-collection-architecture-tier, NOT the Storm Bear vault corpus T1-T5 tier system.** Vault classifies as **T1 Augmentation**.

## Install paths (3-way)

1. **Plugin marketplace** (Claude Code 1.0.33+): `/plugin marketplace add AgriciDaniel/claude-seo` → `/plugin install claude-seo@agricidaniel-seo`
2. **Unix manual**: `git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git && bash claude-seo/install.sh`
3. **Windows manual**: `git clone ... && powershell -ExecutionPolicy Bypass -File claude-seo\install.ps1`

**Explicitly rejected**: `irm | iex` PowerShell one-liner — cited Claude Code security guardrails flagging as supply-chain risk. Sister to `curl ... | bash` rejection in v1.4.0 CHANGELOG.

## Skill discovery model

Per Anthropic plugin spec (v1.6.1 transition):

- `skills/*/SKILL.md` — auto-discovered by directory presence
- `agents/seo-*.md` — auto-discovered by prefix glob
- `plugin.json` does NOT list per-file paths (removed in v1.6.1)

Install paths:
- Plugin install → `~/.claude/plugins/.../skills/seo/` etc.
- Manual install → `~/.claude/skills/seo/` etc.

## Python execution layer

- **Virtualenv**: `~/.claude/skills/seo/.venv/` (created during install; `--user` fallback per v1.2.0)
- **Requirements file**: `requirements.txt` persisted to skill dir for user retry (v1.2.0)
- **Python requirement**: 3.10+ (was 3.8+ initially; corrected v1.4.0)
- **30 tracked + 2 dev-only scripts** — all with docstrings, CLI, JSON output (per Development Rules)

## Security posture (mature)

| Category | Implementation |
|---|---|
| **SSRF protection** | `validate_url()` in google_auth.py — blocks private IPs / loopback / GCP metadata. ALL scripts that accept user URLs must call it. |
| **Credentials** | Never committed: `.env` / `client_secret*.json` / `oauth-token.json` / `service_account*.json` in `.gitignore`. Stored at `~/.config/claude-seo/` (user-space). |
| **OAuth** | Never stores `client_secret` in token file — reads from `client_secret.json` at runtime. |
| **No hardcoded paths** | `os.path.dirname(os.path.abspath(__file__))` everywhere; **enforced** (per v1.7.0 cleanup pass). |
| **Atomic writes** | tempfile + shutil.move (v1.9.6 VULN-A08) — no partial-write corruption. |
| **URL allowlist** | GitHub API requests in sync_flow.py validated as `api.github.com` over HTTPS (v1.9.6 VULN-A10). |
| **Response caps** | 5 MB + 15s timeout on GitHub API (v1.9.6 VULN-A09). |
| **Path traversal** | `Path.resolve()` containment in `record_write()` (v1.9.6 VULN-A03). |
| **Tool grants** | seo-flow agent had Bash removed (v1.9.6 VULN-A01) — eliminates prompt-injection-to-shell. |
| **WebFetch trust model** | Agent body warns: "WebFetch is untrusted" — don't execute or relay verbatim (v1.9.6 VULN-A05). |
| **CI gate** | `pytest tests/` runs every push + PR; manifest-consistency tests (13 assertions at v1.9.9). |

**10 named VULNs in single release (v1.9.6)** = strongest single-release security discipline observed in corpus.

## Canonical report generator — opinionated single-source

`scripts/google_report.py` is mandated for ALL SEO reports per CLAUDE.md Report Generation Rules:

| Aspect | Choice |
|---|---|
| Format | A4 PDF via WeasyPrint |
| Charts | matplotlib at 200 DPI, 85% width, max-height 120mm |
| Style | White title page, navy `#1e3a5f` accent, Times New Roman |
| Color palette | Navy `#1e3a5f` (headers) / dark gold `#b8860b` (accents) / forest green `#2d6a4f` (pass) / warm amber `#d4740e` (warnings) / deep red `#c53030` (fail) / warm cream `#faf9f7` (backgrounds) |
| Structure | Title page → TOC with scores → Executive Summary → Data sections → Recommendations → Methodology |
| Banned CSS | `page-break-inside: avoid` (causes WeasyPrint white gaps) |
| Quality gate | `_review_pdf()` runs automatically; verify `"status": "PASS"` before presenting |
| Format variants | PDF (default) / HTML / xlsx / `all` (since v1.7.2) |
| Branding | "Powered by Google APIs" logo on title page when using Google data |

**Cross-skill enforcement rule** (CLAUDE.md):
> *"After completing ANY analysis command (audit, page, technical, content, schema, geo, local, maps), offer: 'Generate a PDF report? Use `/seo google report`'"*

This is the **single strongest opinionated-output-discipline observed in the corpus** — most subjects describe output formats casually; claude-seo enforces a brand-consistent, bug-free, automatically-reviewed PDF pipeline as a project invariant.

## Hooks (`hooks/hooks.json`)

PostToolUse schema validation hooks declared. Minimal mention in CLAUDE.md; CHANGELOG v1.9.6 confirms hooks exist as quality gates.

## Quality gates — hard-limit anti-Goodhart discipline

| Quality gate | Threshold |
|---|---|
| Local SEO location pages | Warning at **30+** / hard stop at **50+** |
| Programmatic SEO pages | Warning at **100+** / **HARD STOP at 500+** without audit |
| Thin content per page type | Detection in seo-content + seo-page |
| Doorway page prevention | Flagged by seo-technical |
| Schema deprecation | Auto-detect HowTo / FAQ / SpecialAnnouncement obsolescence |
| SPA/CSR rendering | Transparent disclosure as Limitation (issue #11) — seo-visual + Firecrawl partial mitigation |

The **"HARD STOP at 500+ programmatic pages"** is corpus-rare anti-Goodhart-law discipline — the plugin **refuses to mass-generate** even when it mechanically could. This is the same discipline that motivated the hireui I-2 invariant after the 2026-05-06 anspace incident; claude-seo bakes it in by default.

## Key Principles (CLAUDE.md verbatim)

1. **Progressive Disclosure** — Metadata always loaded, instructions on activation, resources on demand. **Pattern #28 evidence.**
2. **Industry Detection** — Auto-detect SaaS / e-commerce / local / publisher / agency.
3. **Parallel Execution** — Full audits spawn up to **15 subagents simultaneously**. **CORPUS-LARGEST T1 audit parallelism observed.**
4. **Extension System** — DataForSEO MCP / Firecrawl MCP / Banana MCP — opt-in, graceful degradation.

## Limitations (transparent honest disclosure)

The README **proactively discloses** the SPA/CSR limitation in a dedicated section + links to GitHub issue #11 as tracked v2.0 epic:

> *"Sites that render content client-side without server-side rendering will produce false-negative findings on content, schema, headings, and meta in most subagents."*

Workaround offered: `seo-visual` subagent uses Playwright when available; Firecrawl extension provides JS rendering for full mitigation.

**Honest-deficiency-disclosure** = corpus-rare discipline. Most subjects describe capabilities not gaps.

## Compatibility / migration discipline (v1.9.9)

CHANGELOG v1.9.9 has explicit compatibility section:

- No breaking changes (patch release per SemVer)
- Sub-Skills numbered list renumbered (seo-content-brief inserted, seo-firecrawl moved to extensions subsection)
- Third-party docs that hard-coded "skill 21 is seo-firecrawl" would need updating — explicitly called out
- `/seo audit` does NOT persist subagent findings between runs (intentional v1.x contract; v2 revisits per #51)

**Migration-impact-disclosure discipline** = corpus-rare.

## Why this entity matters for Pattern Library

- **Pattern #18 Layer 1 cross-IDE-coexistence at 5-platform scale** — CLAUDE.md vs AGENTS.md split as the architectural mechanism
- **Pattern #28 progressive-disclosure across 4 dimensions** — skill metadata / on-demand references / Google API credential tiers / extension opt-in
- **NEW Pattern candidate: Manifest-Drift-As-First-Class-CI-Concern** — 5-version-source atomic-bump CI discipline with 13 assertions (v1.9.9)
- **Strongest single-release security discipline** (v1.9.6 — 10 named VULNs) — corpus benchmark

Continue to [Entity 2 — ecosystem-portfolio (Pattern #19 N=3)](./entity-2-ecosystem-portfolio-n3.md) for portfolio-level analysis.
