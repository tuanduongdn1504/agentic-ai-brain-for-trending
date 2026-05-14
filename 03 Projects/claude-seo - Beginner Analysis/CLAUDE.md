# claude-seo — Beginner Analysis

> **Subject:** [`AgriciDaniel/claude-seo`](https://github.com/AgriciDaniel/claude-seo) — *"Universal SEO skill for Claude Code. 25 sub-skills + 18 sub-agents..."*
> **Wiki version:** v64
> **Build date:** 2026-05-13
> **Routine:** `llm-wiki-routine-v2.1` (Storm Bear vault)

---

## Phase 0 — Probe summary

### 12-axis classification

| Axis | Value |
|------|-------|
| **Tier** | **T1 Augmentation — NEW sub-archetype: domain-vertical-skill-collection** (first SEO-vertical T1 collection in 63-wiki corpus; distinct from prior T1 collections — general-purpose mattpocock-skills v57 / curated-meta awesome-claude-skills v50 / corporate-curated agent-skills-of-vercel v51 / single-artifact karpathy-skills v63) |
| **Archetype** | Solo individual (Agrici Daniel — "AI Workflow Architect"; agricidaniel.com; personal-brand portfolio) + 5 named community contributors via Pro Hub Challenge for v1.9.0 |
| **Scale tier** | Medium-high engagement (6,494 stars / 993 forks / 66 watchers / ~95 days = **~68 stars/day**; below Pattern #52 EXTREME-VIRAL threshold but **15.3% fork ratio signals high active-deployment intent** — corpus-rare for solo-individual T1) |
| **Primary lang** | Python (30 execution scripts) + Markdown (43 SKILL.md / AGENTS.md primitives) |
| **Packaging tool** | 3-way: (1) Claude Code plugin marketplace `/plugin marketplace add AgriciDaniel/claude-seo` + `/plugin install claude-seo@agricidaniel-seo`; (2) `bash install.sh` git-clone install; (3) PowerShell `install.ps1`; v1.9.9 latest (2026-05-11) with **5-version-source atomic-bump CI discipline** (per CHANGELOG v1.9.9) |
| **Origin story** | Solo-individual SEO-domain specialist building **5-product domain-vertical ecosystem**: claude-seo (core SEO) + claude-blog (content) + banana-claude (image gen) + codex-seo (Codex CLI port) + FLOW framework (CC BY 4.0, 41 AI prompts) |
| **Methodology** | SEO-domain methodologies cited as LIVING STANDARDS: Google Quality Rater Guidelines (Sept 2025) / Core Web Vitals (LCP/INP/CLS with INP-replaced-FID 2024-03-12 noted) / Generative Engine Optimization (AI Overviews + ChatGPT + Perplexity) / Schema.org with **explicit deprecation-aware schemas** (HowTo deprecated Sept 2023 / FAQ restricted Aug 2023 / SpecialAnnouncement deprecated July 2025) + FLOW framework (author-original) |
| **Governance file count** | **13+** (README + CLAUDE + AGENTS + CHANGELOG-607-line + CITATION.cff + CODEOWNERS + CODE_OF_CONDUCT + CONTRIBUTING + CONTRIBUTORS + LICENSE-MIT + PRIVACY + SECURITY + pyproject.toml + .devcontainer + tests/) — **full corporate-style governance from solo individual** |
| **Agent/skill count** | **43 primitives total** (25 sub-skills + 18 sub-agents); **LARGEST primitive-count in corpus T1 collection history** (vs mattpocock-skills v57 = 19 skills / agent-skills-of-vercel v51 = several / karpathy-skills v63 = 1) |
| **i18n coverage** | EN-only artifact documentation BUT functional-i18n via `seo-hreflang` skill (ISO 639-1 + ISO 3166-1 validation; cultural-profiles support); distinct i18n-as-function vs i18n-as-artifact distinction |
| **Intellectual influence cited** | Multiple: Google Quality Rater Guidelines / Core Web Vitals + INP (Google) / Schema.org (deprecation-aware) / FLOW framework (author-original, CC BY 4.0) / DataForSEO (extension) / Firecrawl (extension) / Banana-Claude (sister-product extension) / Ahrefs MCP / Semrush MCP |
| **Agent platforms supported** | **5 platforms** + 1 sister-port = **6-platform-reach**: Claude Code primary + Cursor + Cursor Cloud Agents + Google Antigravity + Gemini CLI (AGENTS.md explicit multi-platform) + Codex CLI port (separate `codex-seo` sister-repo) — **HIGHEST platform-count in corpus T1 history** |

### Tier placement decision

**T1 Augmentation — domain-vertical-skill-collection sub-archetype (NEW v64).**

Justified by:
- Plugin lives inside Claude Code (T1 surface) — verified by `/plugin install` path + auto-discovery from `~/.claude/plugins/.../skills/seo/`
- Function = skill augmentation for SEO domain (T1 function)
- **NEW sub-archetype within T1 Augmentation:** domain-vertical (all 43 primitives are SEO-domain; not general-purpose like mattpocock; not curated-meta like awesome-claude-skills; not single-artifact like karpathy)
- Author's own CLAUDE.md calls it "Tier 4 Claude Code skill" — that's the author's INTERNAL vocabulary for skill-collection-architecture-tier (3-layer architecture: directive/orchestration/execution), NOT the vault corpus T1-T5 tier system. **Vault tier classification stands at T1.**

**Alternative considered:** T1 with mattpocock-skills sibling classification (general-purpose multi-skill collection). REJECTED — claude-seo's 43 primitives are 100% SEO-domain; the vertical-specialization is the distinguishing feature, not the size.

### Phase 4b PRIMARY routing mode

**🎯 PRIMARY: Pattern #19 ecosystem-portfolio-builder N=3 strengthening — PROMOTION-ELIGIBLE at v66 mini-audit under criterion #2 structural-N=2 (already exceeded)**

Pattern #19 ecosystem-portfolio-builder sub-type was registered within already-CONFIRMED Pattern #19 at v63 EARLY mini-audit (gotalab N=1 baseline). v63 andrej-karpathy-skills brought N=2 (forrestchang karpathy-skills + Multica = 2-product portfolio). v64 claude-seo brings **N=3 cross-archetype with distinct portfolio shapes:**

| Subject | Wiki | Portfolio products | Strategic shape |
|---------|------|-------------------|-----------------|
| gotalab v61 | cc-sdd | cc-sdd + skillport + uxaudit + claude-code-marimo (4 products) | Solo-Japanese SDD/skills ecosystem |
| forrestchang v63 | karpathy-skills | karpathy-skills + Multica (2 products) | Viral-distillation + commercial-platform-play |
| **AgriciDaniel v64** | **claude-seo** | **claude-seo + claude-blog + banana-claude + codex-seo + FLOW framework (5 products)** | **SEO-vertical-domain ecosystem** |

**N=3 cross-archetype is structurally diverse:**
- gotalab: SDD methodology vertical
- forrestchang: behavioral-overlay viral + commercial platform
- AgriciDaniel: SEO-domain vertical

**Promotion-eligibility at v66:** mechanism repeatable across 3 distinct portfolio shapes. v66 mini-audit can promote ecosystem-portfolio-builder from sub-type-candidate to CONFIRMED sub-type within Pattern #19 under criterion #2 structural-unambiguity-at-N=2 (already at N=3).

### Secondary routing modes

- **Pattern #18 Multi-Platform 5-platform strengthening + sister-port pattern** — claude-seo supports 5 platforms (Claude Code + Cursor + Cursor Cloud + Antigravity + Gemini CLI) + separate Codex CLI port `codex-seo`. **HIGHEST platform-count in corpus T1 history**. Distinguishing mechanism: AGENTS.md explicitly multi-platform with per-platform invocation patterns; CLAUDE.md Claude-Code-specific. Cross-platform via SHARED-SKILL-CONTENT + PER-PLATFORM-DISPATCH-FILE pattern.
- **NEW T1 sub-archetype: domain-vertical-skill-collection N=1 stale-flagged** — first SEO-vertical T1 collection in corpus; un-stale criterion = 2nd domain-vertical T1 collection (e.g., hypothetical claude-legal / claude-medical / claude-finance). Watch for v65-v70 wikis.
- **NEW Pattern candidate: Living-Domain-Standards Tracking** — claude-seo codifies external-authority quality-criteria with **explicit deprecation-aware schemas** (e.g., "HowTo: Deprecated (Sept 2023)" / "FAQ: Restricted to gov/health (Aug 2023)" / "INP replaced FID 2024-03-12" / "Updated to September 2025 Quality Rater Guidelines"). Distinct from coding-methodology codification (SDD/TDD) — tracks living external standards with versioned absorption discipline. N=1 stale-flagged at v64.
- **Pattern #59 Claude Code Plugin Marketplace at solo-individual high-engagement scale** — solo + 6.5K stars + 15.3% fork ratio = high-engagement T1 sub-archetype distinct from EXTREME-VIRAL (Pattern #52) and from corporate-scale (codex-plugin-cc v62). Watch as Pattern #59 strengthening within already-confirmed Pattern #59.

### Phase 0.9 Storm Bear meta-entity check

**STRICT 1-of-4 inclusion check:**

| Criterion | Result | Evidence |
|---|---|---|
| (a) Author archetype peer | **FAIL** | Agrici Daniel = AI Workflow Architect + SEO-domain specialist + 5-product portfolio builder; not solo-Asian-diaspora-coach / not Scrum-coach / not solo-engineer-coach archetype. Solo-individual ≠ archetype-peer per Phase 0.9 STRICT discipline. |
| (b) Operational tool for vault | **WEAK PASS** | SEO-domain not directly vault-relevant (vault = LLM Wiki knowledge base, NOT marketing site). IF vault publishes wikis publicly (per public-release-decision-2026-04-28.md) AND wants SEO discoverability for vault content, claude-seo MIGHT be relevant. Speculative; current vault state is private GitHub repo. **Not directly deployable for vault Goal #2 ("build software with these tools") — SEO is not software-development tooling.** |
| (c) Methodology-influence-node | **WEAK PASS** | E-E-A-T / Quality Rater Guidelines / GEO / Living-Domain-Standards tracking — SEO-domain methodologies; could inform "how to make agentic AI content discoverable" if vault ever publishes outward marketing material. **Not coding-methodology** (SDD/TDD/etc.); domain-methodology of different category. |
| (d) In-corpus reference | **FAIL** | No explicit corpus-pattern citations. Lives in Claude Code plugin ecosystem (corpus-related domain) but doesn't cite vault patterns OR corpus-foundation individuals. Pattern #19 ecosystem-portfolio-builder sub-type connection is observational not authorial. |

**Decision: 0-of-4 strong PASS + 2-of-4 WEAK** → **SKIP Storm Bear meta-entity 4th slot.**

**Streak counter:** Storm Bear meta-entity 4-consecutive post-v60-RESTART (v60+v61+v62+v63) → v64 SKIP → **STREAK RESETS TO 0** post-v64-SKIP.

**9-instance Phase 0.9 post-amendment window v56-v64:** v56 PASS / v57 PASS / v58 PASS / v59 SKIP / v60 PASS / v61 PASS / v62 PASS / v63 PASS / **v64 SKIP** = **7 PASS / 2 SKIP = 77.8% INCLUDE rate**.

**Phase 0.9 STRICT discipline working as designed:** v64 SKIP demonstrates STRICT amendment correctly rejects subjects that don't truly satisfy operational-or-influence criteria for vault Goal #2. 2nd SKIP confirms amendment is appropriately calibrated (not over-inclusive).

**Entity slot reallocation post-SKIP:**
- Entity 1: claude-seo core artifact + architecture
- Entity 2: 5-product ecosystem-portfolio-builder (Pattern #19 N=3)
- Entity 3: T1 domain-vertical-skill-collection NEW sub-archetype + Living-Domain-Standards Tracking
- Entity 4: 5-platform multi-platform reach + Pattern Library implications (NO Storm Bear)

---

## Pattern Library implications (preview — Phase 5 will register)

**Direct strengthenings (within already-CONFIRMED or -CANDIDATE patterns):**

1. **Pattern #19 ecosystem-portfolio-builder sub-type N=3 strengthening — PROMOTION-ELIGIBLE at v66** (gotalab v61 + forrestchang v63 + AgriciDaniel v64; 3 distinct portfolio shapes)
2. **Pattern #18 Layer 1 cross-IDE-coexistence at 5-platform scale** — strengthens within Pattern #18 cross-platform observations; CLAUDE.md + AGENTS.md split as deliberate Claude-Code-vs-other-IDE discipline at 5-platform scale
3. **Pattern #59 Claude Code Plugin Marketplace at high-engagement solo-individual scale** — within already-confirmed Pattern #59; sub-variant: solo-individual with 15%+ fork ratio + 6K+ stars (medium-high engagement vs Pattern #52 EXTREME-VIRAL)
4. **Pattern #52 Extreme-Viral-Velocity counter-evidence** — claude-seo NOT extreme-viral (~68 stars/day below 300/day threshold); 95-day age in same observation window as karpathy-skills (102 days) and codex-plugin-cc (21 days at observation); supports velocity-source-archetype distinction (claude-seo = solo-individual-domain-specialist NOT in any 52a/52b/52c sub-archetype) — useful negative-control evidence at v64

**NEW top-level candidate registrations:**

5. **NEW T1 sub-archetype: domain-vertical-skill-collection N=1 stale-flagged at v64** — first SEO-vertical T1 collection; distinct from general-purpose (mattpocock) / curated-meta (awesome-claude-skills) / corporate-curated (vercel) / single-artifact (karpathy). Future un-stale via 2nd domain-vertical T1.
6. **NEW Pattern candidate: Living-Domain-Standards Tracking N=1 stale-flagged at v64** — agents codify external-authority quality-criteria with explicit deprecation-aware schemas + dated standards-version tracking. Distinct from coding-methodology codification. Candidate criteria: (a) explicit external-authority citation with date; (b) deprecation-tracking discipline; (c) versioned absorption of external-standards updates.

**Cross-wiki standards check:**

- **OpenClaw / Hermes runtime:** N/A (Python-execution + Markdown-skills; no runtime)
- **MCP:** YES — extensions integrate MCP servers (Ahrefs, Semrush, GSC, PageSpeed, DataForSEO via MCP)
- **AGENTS.md:** YES SHIPPED — explicit multi-platform format (Cursor / Cursor Cloud / Antigravity / Gemini CLI)
- **anthropics/skills protocol:** YES — SKILL.md format throughout; conforms to skills v62-corpus-validated frontmatter pattern
- **CLAUDE.md primitive:** YES — separate from AGENTS.md (Claude-Code-only)

---

## Sources ingested (Phase 2 will write cluster summaries)

1. README.md (398 lines) — overview + install + commands table (26+ slash commands) + features + architecture + ecosystem
2. CLAUDE.md (210 lines) — Claude-Code-specific project instructions; 25 sub-skills directory map
3. AGENTS.md (126 lines) — multi-platform Cursor/Antigravity/Gemini-CLI instructions
4. CHANGELOG.md (607 lines) — v1.0.0 → v1.9.9 release history; **CI-guard 13 assertions; 5-version-source atomic-bump discipline (v1.9.9 highlight)**
5. plugin.json + marketplace.json (~3.3KB combined) — Claude Code plugin marketplace metadata
6. skills/ directory (25 sub-skills auto-discovered)
7. agents/ directory (18 sub-agents auto-discovered)
8. Repo metadata via GitHub API (stars/forks/license/created/pushed/topics)

---

## Cross-wiki siblings (mandatory cross-references)

**Pattern #19 ecosystem-portfolio-builder N=3 peers:**
- [cc-sdd v61](../cc-sdd%20-%20Beginner%20Analysis/) — gotalab N=1 baseline (4-product Japanese SDD/skills ecosystem)
- [andrej-karpathy-skills v63](../andrej-karpathy-skills%20-%20Beginner%20Analysis/) — forrestchang N=2 (2-product viral + commercial)

**T1 Augmentation peers (skills collections at different sub-archetypes):**
- [mattpocock-skills v57](../mattpocock-skills%20-%20Beginner%20Analysis/) — 19-skill general-purpose collection
- [awesome-claude-skills v50](../awesome-claude-skills%20-%20Beginner%20Analysis/) — multi-skill curated-meta aggregator
- [agent-skills-of-vercel v51](../agent-skills-of-vercel%20-%20Beginner%20Analysis/) — corporate-curated collection
- [andrej-karpathy-skills v63](../andrej-karpathy-skills%20-%20Beginner%20Analysis/) — single-artifact behavioral collection

**Multi-platform peers:**
- [cc-sdd v61](../cc-sdd%20-%20Beginner%20Analysis/) — 8 platforms framework-scale (2 stable + 5 beta + 1 experimental)
- [andrej-karpathy-skills v63](../andrej-karpathy-skills%20-%20Beginner%20Analysis/) — 2 platforms single-skill manual-sync (Claude Code + Cursor)

**Plugin marketplace peers:**
- [codex-plugin-cc v62](../codex-plugin-cc%20-%20Beginner%20Analysis/) — corporate-scale OpenAI marketplace publication
- [oh-my-claudecode v27](../oh-my-claudecode%20-%20Beginner%20Analysis/) — N=1 Pattern #59 solo OMC
- [claude-hud v35](../claude-hud%20-%20Beginner%20Analysis/) — N=2 Pattern #59 solo marketplace-only

**MCP extension peers:**
- [shannon v45](../shannon%20-%20Beginner%20Analysis/) — AI-pentester with MCP
- [aidevops v47](../aidevops%20-%20Beginner%20Analysis/) — DevOps with MCP

---

## Build status

| Phase | Status |
|---|---|
| Phase 0 (probe) | ✅ COMPLETE |
| Phase 1 (scaffold) | ✅ COMPLETE |
| Phase 2 (sources) | ⏳ in progress (3 cluster summaries) |
| Phase 3 (entities) | pending (4 entity pages; NO Storm Bear per Phase 0.9 SKIP) |
| Phase 4a (beginner guide bilingual) | pending |
| Phase 4b (Pattern #19 N=3 promotion deliverable) | pending |
| Phase 5 (iteration log + Pattern Library update) | pending |
| Phase 6 (vault sync) | pending |
