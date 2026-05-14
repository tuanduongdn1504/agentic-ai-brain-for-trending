# Cluster 3 — Ecosystem + CHANGELOG history

> **Sources:** CHANGELOG.md (607 lines, v1.0.0 → v1.9.9) + Ecosystem section (README + CLAUDE.md) + extensions/ folder

## The 5-product ecosystem-portfolio

Per the README's Ecosystem table:

| Product | Repo | Function | Strategic role |
|---|---|---|---|
| **claude-seo** | `AgriciDaniel/claude-seo` (this) | SEO analysis, audits, schema, GEO | **Core** product (anchor) |
| **claude-blog** | `AgriciDaniel/claude-blog` | Blog writing, optimization, scoring | Companion (consumes SEO findings via cross-skill chain) |
| **claude-banana** | `AgriciDaniel/banana-claude` | AI image generation via Gemini | **Dual-role**: standalone product + bundled as `seo-image-gen` extension |
| **codex-seo** | `AgriciDaniel/codex-seo` | Codex-first port (TOML agents, deterministic runners) | **Sister-platform port** (same SEO surface, Codex CLI host) |
| **FLOW** | `AgriciDaniel/flow` | Evidence-led SEO framework (41 prompts, CC BY 4.0) | **Author-original knowledge base** (powers `seo-flow` skill) |

Plus a 6th community-third-party reference:

| Product | Author | Function | Strategic role |
|---|---|---|---|
| **AI Marketing Claude** | zubair-trabzada | Copywriting / emails / social / ads / funnels / CRO | **Community** (post-audit marketing action from SEO findings) |

## Portfolio mechanics

### 5 distinct repositories, single author, single brand-domain

All 5 own-products live under `github.com/AgriciDaniel/` (same author). `agricidaniel.com` is the personal-brand domain. `claude-seo.md` is the dedicated product-marketing subdomain.

### Cross-product workflow (corpus-rare integrated demo)

The README documents a **5-step cross-product workflow** in the Ecosystem section:

```
1. /seo audit https://example.com         → identify content gaps + technical issues
2. /seo backlinks https://example.com     → analyze link profile + competitor gaps
3. /blog write "target keyword"           → create SEO-optimized blog post (Claude Blog product)
4. /seo image-gen hero "blog topic"       → generate hero image (banana extension)
5. /seo geo https://example.com/blog/post → optimize for AI citations
```

The workflow **chains 4 distinct products** (claude-seo / claude-blog / banana / claude-seo's geo) — direct evidence that the portfolio is **functionally coupled, not naming-coincidental**.

### Codex sister-port — DUAL-PLATFORM portfolio strategy

The README opens with a callout:

> *"Using Codex instead of Claude Code? Use Codex SEO, the Codex-first port of this project with Codex skills, TOML agents, plugin packaging, deterministic runners, and the same SEO workflow surface."*

`codex-seo` is a **deliberate platform-mirror** — same SEO command surface, ported to Codex's primitives:
- Codex skills (vs Claude Code skills)
- **TOML agents** (vs Markdown agents per Anthropic spec)
- Plugin packaging (Codex-native)
- Deterministic runners (Codex CLI distinction)

This is a **CORPUS-FIRST observation of single-author cross-vendor port** at the T1 augmentation level. Distinct from v62 codex-plugin-cc (OpenAI publishing FOR Claude Code = Pattern #18 Layer 2 cross-vendor-bridge sub-archetype). claude-seo + codex-seo = **solo-author parallel-port at single-author scale**, a different mechanism.

Pattern Library implication: **NEW Pattern #18 Layer 2 sub-archetype candidate at v64** — "solo-author-cross-vendor-parallel-port-as-separate-repo" (distinct from install-time-translator v61 / runtime-protocol-translation v60 / cross-vendor-bridge-as-plugin v62). Deferred to v66 for deliberation.

### Banana as DUAL-ROLE (standalone + bundled)

The Banana extension is shipped two ways:

1. **Standalone**: `github.com/AgriciDaniel/banana-claude` — separate Claude Code plugin
2. **Bundled extension**: `extensions/banana/install.sh` inside claude-seo

The README confirms: *"Already using standalone Claude Banana? The extension reuses your existing nanobanana-mcp setup."*

This is a **CORPUS-RARE re-bundling mechanism** — same author can install once for SEO use OR install standalone for general image gen. The extension layer **detects existing standalone install** to avoid duplicate MCP server.

### FLOW framework — author-original CC BY 4.0 knowledge

Per CHANGELOG v1.9.5 (2026-04-26):

> *"seo-flow: FLOW framework integration, Find → Leverage → Optimize → Win. 41 evidence-led AI prompts (CC BY 4.0) bundled as `skills/seo-flow/references/prompts/` (find:5, leverage:1, optimize:21, win:3, local:11)."*

FLOW is an **author-original methodology** (not external standard). The author created it, published it under CC BY 4.0 at a separate repo, and `seo-flow` skill consumes it via `scripts/sync_flow.py` GitHub-API sync.

**License hybrid**: FLOW prompts = CC BY 4.0 (author-created creative commons). claude-seo skill code = MIT. Per v1.9.5: *"Claude SEO's MIT license unchanged, applies to skill code only."*

This is a **dual-license author-portfolio** at single-author scale — the author owns both licenses simultaneously, which is corpus-rare. Compare with v59 AutoGPT's dual-license (MIT + PolyForm-Shield) which was corporate-stewardship; this is solo-author with CC content + MIT code.

## CHANGELOG v1.0.0 → v1.9.9 — version-source-drift incident history

The 607-line CHANGELOG documents **multiple skill-count-drift incidents** that drove the eventual CI manifest-guard discipline. This is the **strongest observed version-drift-incident-as-learning thread** in any corpus subject.

### v1.0.0 (2026-02-07) — Initial release
- 9 specialized skills + 6 subagents
- HowTo deprecated (Sept 2023) noted
- FAQ restricted (Aug 2023) noted
- SpecialAnnouncement deprecated (July 2025) noted
- INP-replaced-FID (March 12, 2024) noted
- E-E-A-T per September 2025 Quality Rater Guidelines

This release **already had the deprecation-aware schema discipline + versioned-external-standards discipline** that motivates the v64 NEW Pattern Library candidate "Living-Domain-Standards Tracking".

### v1.1.0 (2026-02-07) — CRITICAL security cascade
- 5 CVEs patched at floor minimums: urllib3 / lxml / Pillow / playwright / requests
- GEO major enhancement: AI crawler detection / llms.txt / RSL 1.0 / passage-level citability scoring (134-167 word optimum)
- E-E-A-T expanded: "now applies to ALL competitive queries, not just YMYL" (December 2025 core update)
- Schema additions: ConferenceEvent, PerformingArtsEvent, LoyaltyProgram

**Same-day v1.0.0 → v1.1.0** indicates security-driven hot-patch — the initial release shipped without floor-pinning CVEs.

### v1.2.0 (2026-02-19) — Install hardening + SSRF prevention
- SSRF: private-IP blocking in `fetch_page.py` + `analyze_visual.py`
- Path-traversal sanitization in `capture_screenshot.py`
- Install: removed `--break-system-packages`, switched to **venv-based pip install**
- Python deps now install to `~/.claude/skills/seo/.venv/` with `--user` fallback

### v1.3.0 (2026-03-06) — Extension system born
- `extensions/` directory convention introduced
- DataForSEO extension: 22 commands across 9 API modules
- plugin.json manifest for official plugin directory

This is the **Pattern Library extension-architecture-emergence moment** — extensions became first-class.

### v1.4.0 (2026-03-12) — Supply-chain hardening + GEO agent
- **Replaced `irm | iex` Windows PowerShell one-liner with `git clone + powershell -File`** as primary install — explicitly cites Claude Code's own security guardrails flagging the old pattern
- Install scripts pinned to specific release tag by default (vs `main`)
- GEO agent deployed (audit now spawns 7 parallel agents, was 6)
- `--googlebot` flag for Googlebot UA prerender detection (Issue #11 first phase)

### v1.5.0 (2026-03-19) — Frontmatter compliance
- `user-invokable` / `argument-hint` / `allowed-tools` added per Anthropic best practices
- **Em dash elimination (U+2014 → punctuation)** — explicitly *"to reduce AI detection signals"*
- HTML comments before frontmatter removed (8 files)
- Full Anthropic compliance audit pass

The em-dash-elimination is a **CORPUS-RARE adversarial-AI-detection-evasion discipline** — most subjects don't reason about AI-text-detection signals.

### v1.6.0 (2026-03-23) — Local SEO + Maps intelligence
- seo-local + seo-maps skills + agents added
- Sub-skill count 12 → 14 core
- Subagent count 7 → 9 core

### v1.6.1 (2026-03-27) — Marketplace + auto-discovery transition
- **Marketplace distribution**: `.claude-plugin/marketplace.json` for plugin marketplace submission (`/plugin marketplace add AgriciDaniel/claude-seo`)
- All 11 subagents standardized to `model: sonnet` + `maxTurns` (15-25)
- 12 discovery keywords added to plugin.json
- **Auto-discovery transition**: removed non-standard `entry_point` + per-file arrays; relies on `skills/*` + `agents/seo-*.md` directory discovery
- `allowed-tools` format: YAML arrays → comma-separated strings (17 files)

### v1.7.0 (2026-03-28) — Google APIs major addition
- 21 commands across 4 credential tiers
- 11 Python scripts (google_auth / gsc_query / pagespeed_check / etc.)
- 10 reference files
- **PDF report generator** (`scripts/google_report.py`) — WeasyPrint + matplotlib + post-generation review
- OAuth web credential flow (localhost:8085 callback)
- SSRF protection: `validate_url()` blocks private IPs/loopback/GCP metadata
- Hardcoded user paths removed
- Sub-skill count 14 → 15

### v1.7.1 (2026-03-30) — Install path hotfix
- `install.sh` broken path `seo/` → `skills/seo/` (h/t @hieu-e via #39)
- Install tag pinned to v1.7.1 (was stuck at v1.6.0)
- CI: syntax check expanded from 4 to 15 Python scripts

### v1.7.2 (2026-03-30) — Firecrawl + Backlinks
- Firecrawl extension: 4 commands (crawl/map/scrape/search) + **JS rendering for SPA/CSR** (partial Issue #11 mitigation)
- Backlink skill: `/seo backlinks` with 7-section analysis + health score (0-100)
- Backlink quality reference: 30 toxic link patterns + anchor text benchmarks by industry
- Excel export: `--format xlsx` in google_report.py (3 sheets: Summary/Queries/Pages)
- Sub-skill count 18 → 19

### v1.8.1 (2026-04-06) — Image SERP + tooling
- Google Images SERP via DataForSEO + cross-skill `/seo images serp <keyword>`
- Image File Optimization: `/seo images optimize <path>` for WebP/AVIF + IPTC/XMP + responsive variants
- **Image ranking factors table**: documents what matters (alt / filename / context) vs what doesn't (EXIF / IPTC)
- **Version mismatch fix**: unified all 19 SKILL.md + plugin.json + CLAUDE.md to v1.8.0 (was 1.7.0/1.7.2/1.8.0 three-way split) — **first explicit version-source-drift incident**

### v1.8.2 (2026-04-10) — Ukrainian i18n + supply-chain
- First i18n: Ukrainian localization (README + CONTRIBUTING + PRIVACY + SECURITY + INSTALLATION + TROUBLESHOOTING) — PR #50 by @edocltd
- Firecrawl extension section in README
- Install scripts re-pinned (v1.7.2 → v1.8.2) — explicit *"new curl-based installs now get the current release"*
- Version sync fixes across pyproject.toml + CITATION.cff + all 19 SKILL.md files
- README architecture counts corrected
- **Multiple version-drift fixes in one release**

### v1.9.0 (2026-04-14) — Pro Hub Challenge community release
- **5 new community-contributed skills/skills-enhancements:**
  - seo-cluster (Lutfiya Miller, Winner)
  - seo-sxo (Florian Schmitz)
  - seo-drift (Dan Colta — security-hardened: *"all curl usage eliminated, SSRF protection enforced"*)
  - seo-ecommerce (Matej Marjanovic)
  - seo-hreflang cultural profiles (Chris Muller — 4 cultural adaptation profiles: DACH / Francophone / Hispanic / Japanese)
- DataForSEO cost guardrails (Matej Marjanovic)
- **CONTRIBUTORS.md** added (community credits file)
- **AGENTS.md** added (multi-platform discovery — concept by Matej Marjanovic, rewritten for v1.9.0)
- Schema templates: Product (Full E-commerce) + ItemList (hub/pillar pages)
- 5 new commands (cluster / sxo / drift baseline/compare/history / ecommerce)
- Audit subagents 12 → 15 (max parallelism)
- All 23 SKILL.md stamped to v1.9.0
- *"5 out of 6 submissions scored Proficient or above"* — explicit community quality discipline

### v1.9.5 (2026-04-26) — FLOW integration
- 41 evidence-led AI prompts bundled (CC BY 4.0)
- `sync_flow.py` GitHub API sync with `--dry-run` + `--ref <sha>` pinning
- FLOW cross-references in seo-geo / seo-local / seo-content / seo-cluster

### v1.9.6 (2026-04-26) — 10 named VULN fixes (same day as v1.9.5)
- **VULN-A01 (HIGH)**: Bash removed from `seo-flow` agent tool grant — eliminates prompt-injection-to-shell attack surface
- **VULN-A02/A07 (MED/LOW)**: anonymous-first GitHub API in sync_flow; PAT only for 403-fallback
- **VULN-A03 (MED)**: `Path.resolve()` containment check in `record_write()` — blocks path-traversal
- **VULN-A04 (MED)**: `flow-prompts.lock` SHA-256 baseline; sync diffs against baseline
- **VULN-A05 (MED)**: "WebFetch is untrusted" security rule explicit in agent body
- **VULN-A06 (LOW)**: `gh` CLI absence degrades to anonymous (not hard-exit)
- **VULN-A08 (LOW)**: atomic file writes (tempfile + shutil.move) — no partial-write corruption
- **VULN-A09 (LOW)**: 5 MB / 15s caps on GitHub API responses
- **VULN-A10 (LOW)**: URL allowlist validates `api.github.com` over HTTPS — SSRF block
- **INFO-A14**: CC BY 4.0 attribution header on `prompts/README.md`
- Test count: 5 → 15

This is **the strongest single-release security discipline observed in any corpus subject** — 10 named VULNs with severity levels + 10 unit/integration tests covering them.

### v1.9.7 (2026-05-09) — Manifest reconciliation (Skill-count drift across 5 manifests)
- 5 manifests contradicted each other on sub-skill counts:
  - plugin.json: "20 core sub-skills"
  - marketplace.json: "21 core sub-skills"
  - CLAUDE.md line 7: "21 core sub-skills"
  - AGENTS.md line 8: "20 core sub-skills" + line 84: "23 skills"
  - README.md line 7: "21 core sub-skills"
- Reconciled to: *"24 sub-skills (20 core + 1 orchestrator + 1 framework integration + 2 extension mirrors)"*
- Sub-agent count drift: CLAUDE.md "16 core (+2 = 18 total)" vs AGENTS.md "15 core (+2 = 17 total)" — reconciled to 18
- CITATION.cff version stuck at 1.8.2 (6 minor versions behind) — bumped to 1.9.7
- dependabot.yml added (weekly pip + Actions updates)
- CODE_OF_CONDUCT.md added (Contributor Covenant 2.1)
- ci.yml `permissions:` block restricting GITHUB_TOKEN
- **Ukrainian translation retired** — drifted across v1.9.0 → v1.9.7 without maintenance signal; @edocltd retained in CONTRIBUTORS.md

### v1.9.8 (2026-05-09) — Skill-count drift RETURNED (PR #56 collision)
- PR #56 merged `seo-content-brief` as 21st core skill → manifest under-claimed by one
- Reconciled to "25 sub-skills (21 core + 1 orchestrator + 1 framework integration + 2 extension mirrors)"
- **`tests/test_manifest_consistency.py` added** — pytest suite that asserts:
  - plugin.json + marketplace.json claimed counts match on-disk
  - plugin.json + marketplace.json descriptions agree
  - README + CLAUDE + AGENTS all reference same count
  - plugin.json `version` + CITATION.cff `version` triangulate
- **CI gate**: `pytest tests/` runs on every push + PR
- `uninstall.sh` + `uninstall.ps1` switched to glob enumeration (was hardcoded v1.4.0-era list, missing 12 sub-skills + 11 agents)
- Marketplace metadata polish: `category: "marketing"` / `homepage: https://claude-seo.md` / 14 keyword array
- v1.9.8 entry **acknowledges 2 commits landed post-tag** (rolled forward)

### v1.9.9 (2026-05-11) — Final 1.x patch — 5-version-source atomic-bump discipline
*"Final 1.x patch release. v2 is in design; this release leaves the v1.x branch in a clean, well-documented, dependency-current state."*

*"Independently verified across 5 rounds of GPT-5.5 xhigh code review via the Codex CLI before each PR push."*

**Highlights:**
- **5 top-level version sources triangulate atomically to `1.9.9`**: plugin.json + marketplace.json + CITATION.cff + pyproject.toml + install.sh/install.ps1
- **24 in-tree skills + 3 extension SKILL.md files** all at 1.9.9
- **CI guard extended 9 → 13 assertions** with 4 new manifest-consistency tests:
  - `test_orchestrator_sub_skills_list_matches_disk` — Sub-Skills list == `set(skills/*) - {seo}`; no duplicates
  - `test_orchestrator_subagents_list_matches_disk` — Subagents list == `set(agents/seo-*.md)`; no duplicates
  - `test_skill_metadata_versions_match_plugin_json` — every SKILL.md `metadata.version` == plugin.json version (with `COMMUNITY_OVERRIDES` allowlist `{"seo-content-brief": "1.0.0"}`)
  - `test_marketplace_metadata_and_author_parity` — marketplace.json `metadata.description` includes both counts + matches plugin.json; plugin entry `author` parities plugin.json author for name/email/url
- **5 Dependabot floors bumped** as one batched PR after isolated-venv smoke-testing (playwright 1.56→1.59 / weasyprint 61→68.1 / openpyxl 3.1→3.1.5 / google-api-python-client 2.100→2.196 / google-auth-oauthlib 1.0→1.4) — explicit caveat: 1.4.0 drops Python 3.9, but `pyproject.toml` already requires `>=3.10`
- **Image audit (issue #41)**: `parse_html.py` now classifies lazy-loading mechanism in `lazy_method` field (5 values: `native | perfmatters | ewww | js-generic | none`) — sites running Perfmatters/EWWW/lazysizes/vanilla-lazyload/jQuery-lazy no longer mis-reported

**v2 deferrals explicit list (6 items):**
- #11 SPA/CSR audit support (7-phase implementation; PR #90 Limitations section remains patch-appropriate)
- #51 Subagent research persistence (cross-file output-contract change)
- #61 `google_report.py --type full` audit-schema handling (no regression baseline)
- #89 uv adoption (v2.x labeled)
- #53 seo-notebooklm skill (unofficial-wrapper credential code; v2 will define "experimental skills" tier)
- PR #46 macOS SSL via `pip-system-certs` (violates v1.9.9's no-new-deps non-goal)

## Manifest-consistency-as-CI-discipline — the corpus-strongest version-source story

The v1.7.x → v1.9.9 thread is a **2-month case study in version-source-drift learning**:

1. **v1.8.1**: First explicit version-source-drift incident named (3-way split 1.7.0/1.7.2/1.8.0)
2. **v1.8.2**: Multiple version sources updated in one release (mechanical fix)
3. **v1.9.7**: Second drift incident — 5-source contradiction on skill counts
4. **v1.9.8**: First **systematic test discipline**: `test_manifest_consistency.py` added; CI gate via `pytest tests/`
5. **v1.9.9**: CI guard **extended 9 → 13 assertions** with 4 new tests; **5-source atomic-bump** as release discipline; explicit "Independently verified across 5 rounds of GPT-5.5 xhigh code review via the Codex CLI"

This is the **strongest observed manifest-consistency-as-CI-pattern in the corpus**. Sister to v59 AutoGPT's manifest discipline but at much higher granularity. Pattern Library candidate consideration for v66: **"Manifest-Drift-As-First-Class-CI-Concern"** — when a project has 5+ version sources, drift between them becomes an emergent quality risk that requires systematic testing.

## Extensions architecture — opt-in MCP integration

`extensions/` directory contains 3 named install-helper subdirectories:

```
extensions/
  dataforseo/       # DataForSEO MCP install scripts (22 commands across 9 API modules)
  firecrawl/        # Firecrawl MCP install scripts (4 commands; JS rendering for SPA/CSR)
  banana/           # Banana MCP install scripts (sister product reuse)
```

Each extension has:
- `install.sh` (Unix install helper)
- `README.md` (extension-specific docs)
- `SKILL.md` files (extension mirrors in main `skills/` dir as `seo-dataforseo` / `seo-image-gen`)

**Extension-relevant CI discipline**: per v1.9.9, the 4 new manifest-consistency tests include `COMMUNITY_OVERRIDES` allowlist `{"seo-content-brief": "1.0.0"}` — that's the **community-contribution-allowed-to-skip-version-sync** discipline. Author-maintained skills bump together; community-contributed skills can lag at their own pace.

## Community contribution mechanism — Pro Hub Challenge

Per CHANGELOG v1.9.0 + CONTRIBUTORS.md (read indirectly via mentions):

> *"Pro Hub Challenge: Lutfiya Miller (Winner - Semantic Cluster Engine), Florian Schmitz (SXO Skill), Dan Colta (SEO Drift Monitor), Chris Muller (Multi-lingual SEO), Matej Marjanovic (E-commerce + Cost Config + Platform Support), Benjamin Samar (SEO Dungeon - reviewed)"*
>
> *"5 out of 6 submissions scored Proficient or above"*

This is a **gamified-community-contribution mechanism** — a curated challenge with named winner + ranked submissions + explicit quality bar ("Proficient or above"). It's run by **AI Marketing Hub** (skool.com community).

Contrast with:
- **mattpocock-skills v57**: solo-author, no community contribution mechanism
- **awesome-claude-skills v50**: open-curation aggregator (anyone submits via PR)
- **agent-skills-of-vercel v51**: corporate-internal curation (Vercel team)
- **cc-sdd v61**: solo-Japanese-author + Stack Pattern issue-based contributions

claude-seo's **"gamified-curated-challenge"** mechanism is a **NEW community-contribution sub-pattern observation** at v64. Pattern Library deliberation deferred to v66.

## Documentation index (per README)

- `docs/INSTALLATION.md` — full install walkthrough
- `docs/COMMANDS.md` — full commands reference
- `docs/ARCHITECTURE.md` — extended architecture (extensions section)
- `docs/MCP-INTEGRATION.md` — Ahrefs / Semrush / GSC / PageSpeed / DataForSEO MCP server setup
- `docs/TROUBLESHOOTING.md` — common issues

Plus dedicated marketing site `claude-seo.md` with blog + auto-generated release blog posts.

## Why this matters for Pattern Library

CHANGELOG-as-evidence-source contributes to **6 Pattern Library strengthenings + 2 NEW candidates** at v64 (full registration in Entity 4 + Phase 5):

1. **Pattern #19 ecosystem-portfolio-builder N=3** — 5 products portfolio
2. **Pattern #18 Layer 1 cross-IDE-coexistence at 5-platform scale**
3. **Pattern #18 Layer 2 NEW sub-archetype solo-author-cross-vendor-parallel-port** (codex-seo port)
4. **Pattern #59 Claude Code Plugin Marketplace at high-engagement-solo-individual scale**
5. **Pattern #52 EXTREME-VIRAL counter-evidence** (claude-seo NOT extreme; useful negative control)
6. **Pattern #28 progressive-disclosure at credential-tier scale** (Google 4-tier model)
7. **NEW T1 domain-vertical-skill-collection sub-archetype** (first SEO-vertical T1 in corpus)
8. **NEW Pattern Living-Domain-Standards Tracking** (deprecation-aware schemas with dates)

See Entity 4 for the full registration package.
