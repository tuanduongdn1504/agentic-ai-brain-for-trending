# Entity 2 — 5-product ecosystem-portfolio (Pattern #19 N=3 strengthening)

> **Type:** Pattern Library primary deliverable
> **Pattern Library implication:** Pattern #19 ecosystem-portfolio-builder sub-type N=3 strengthening — **PROMOTION-ELIGIBLE at v66 mini-audit**
> **Cross-references:** [Cluster 3 ecosystem section](./cluster-3-ecosystem-and-changelog.md) / Pattern #19 in `_patterns/03-active-candidates.md`

## The 5 products

| # | Product | Repo | Role | License |
|---|---|---|---|---|
| 1 | **Claude SEO** (this) | `AgriciDaniel/claude-seo` | Core SEO analysis | MIT |
| 2 | **Claude Blog** | `AgriciDaniel/claude-blog` | Blog writing + SEO scoring | MIT |
| 3 | **Claude Banana** | `AgriciDaniel/banana-claude` | AI image generation (Gemini) | MIT |
| 4 | **Codex SEO** | `AgriciDaniel/codex-seo` | Codex CLI port of claude-seo | MIT |
| 5 | **FLOW** | `AgriciDaniel/flow` | 41 evidence-led SEO prompts | CC BY 4.0 |

**+ 1 community-third-party** (named in Ecosystem table): AI Marketing Claude (`zubair-trabzada/ai-marketing-claude`) — copywriting / emails / social / ads / funnels / CRO.

## Portfolio mechanics — 4 mechanisms beyond mere naming

### Mechanism 1: Functional cross-product chain in README

The README documents a **5-step workflow that chains 4 products**:

```
1. /seo audit https://example.com      → claude-seo (gaps + technical issues)
2. /seo backlinks https://example.com  → claude-seo (link profile + competitor gaps)
3. /blog write "target keyword"        → CLAUDE-BLOG (separate product)
4. /seo image-gen hero "blog topic"    → BANANA (extension OR standalone)
5. /seo geo https://example.com/.../  → claude-seo (AI-citation optimization)
```

Steps 3 + 4 invoke **separate products** (claude-blog + banana). The workflow is **functional, not branding** — operator gets distinct value from each product.

### Mechanism 2: Banana DUAL-ROLE (standalone + bundled extension)

Banana is shipped two ways:
1. Standalone Claude Code plugin: `AgriciDaniel/banana-claude`
2. Bundled extension inside claude-seo: `extensions/banana/install.sh`

The README explicitly handles the case where user has standalone install: *"Already using standalone Claude Banana? The extension reuses your existing nanobanana-mcp setup."*

**Re-bundling-with-existing-detection** is corpus-rare. Sister-product reuse at MCP-server level.

### Mechanism 3: Codex sister-port — DUAL-PLATFORM strategy

`codex-seo` is **same SEO surface, ported to Codex CLI primitives**:

| Aspect | claude-seo | codex-seo |
|---|---|---|
| Host | Claude Code | Codex CLI |
| Agent format | Markdown SKILL.md | **TOML agents** |
| Plugin packaging | Anthropic plugin spec | Codex-native |
| Runners | Python scripts | **Deterministic runners** |
| Workflow surface | 26 `/seo` commands | Same commands |
| Author | Agrici Daniel | Agrici Daniel |

This is a **CORPUS-FIRST observation: single-author parallel-port at T1 augmentation level**. Distinct from:
- **v62 codex-plugin-cc** (OpenAI publishes FOR Claude Code = cross-vendor-bridge)
- **karpathy-skills v63 manual-sync** (single-skill across 2 platforms via same SKILL.md)
- **cc-sdd v61** (install-time-format-translator for 8 platforms via same repo)

**Pattern #18 Layer 2 NEW sub-archetype candidate at v64**: "solo-author-cross-vendor-parallel-port-as-separate-repo" — author maintains parallel repos for distinct vendor primitives. Deferred to v66 for deliberation.

### Mechanism 4: FLOW framework — author-original CC BY 4.0 with cross-skill sync

FLOW is:
- **Author-original methodology** (Find → Leverage → Optimize → Win — the author's own framework)
- **CC BY 4.0 licensed prompts** (41 prompts: 5 find / 1 leverage / 21 optimize / 3 win / 11 local)
- **Separate repo** at `AgriciDaniel/flow`
- **Consumed by `seo-flow` skill** via `scripts/sync_flow.py` (GitHub API sync; `--dry-run` + `--ref <sha>` pinning)
- **Cross-skill referenced from** seo-geo / seo-local / seo-content / seo-cluster

**Dual-license at single-author scale**: claude-seo skill code = MIT; FLOW prompts = CC BY 4.0. Author owns both licenses simultaneously. Corpus-rare.

## Pattern #19 ecosystem-portfolio-builder N=3 cross-archetype evidence

Pattern #19 sub-type was **registered within already-CONFIRMED Pattern #19 at v63 EARLY mini-audit (2026-05-07)** with gotalab v61 as N=1 baseline. **N=2 strengthening came at v63 andrej-karpathy-skills ship (2026-05-09)** with forrestchang's 2-product portfolio. v64 claude-seo brings **N=3 cross-archetype**:

| Subject | Wiki | Author | Portfolio products | Strategic shape | Distinct portfolio aspect |
|---|---|---|---|---|---|
| **gotalab** | v61 cc-sdd | Solo-Japanese | cc-sdd + skillport + uxaudit + claude-code-marimo (**4**) | SDD methodology vertical | Multi-skill vertical at solo-Asian-diaspora archetype |
| **forrestchang** | v63 karpathy-skills | Solo-engineer + Multica founder | karpathy-skills + Multica (**2**) | Viral-distillation + commercial platform | Source-celebrity-distillation × commercial platform |
| **AgriciDaniel** | v64 claude-seo | Solo-individual + AI Workflow Architect | claude-seo + claude-blog + banana-claude + codex-seo + FLOW (**5**) | **SEO-vertical-domain ecosystem with sister-platform port + dual-license** | **CORPUS-LARGEST single-author portfolio observed; CORPUS-FIRST single-author cross-vendor parallel-port; dual-license MIT + CC BY 4.0 at single-author scale** |

### 3 distinct portfolio shapes — structural diversity

- **gotalab**: SDD methodology + skill-collection vertical
- **forrestchang**: behavioral-overlay viral + commercial platform
- **AgriciDaniel**: SEO-domain vertical with cross-vendor port + framework-as-content

**No two portfolios share strategic shape.** This is **structural-diversity-at-N=3** which is the strongest possible evidence for promotion under criterion #2 (structural-unambiguity-at-N=2 already exceeded).

### Promotion-eligibility analysis at v66

Per Pattern Library promotion criteria (`_patterns/02-promotion-criteria.md` — referenced):

**Criterion #2 — structural-unambiguity-at-N=2:**
- Need: mechanism repeatable across 2 distinct subjects with **non-coincidental sub-mechanism**
- Have: **N=3 with 3 distinct portfolio shapes** = far exceeds threshold

**Criterion #3 — cross-archetype evidence:**
- Need: at least 2 distinct author archetypes
- Have: solo-Japanese (gotalab) + solo-engineer-with-commercial-arm (forrestchang) + solo-individual-with-cross-vendor-port (AgriciDaniel) = **3 distinct archetypes**

**Criterion #4 — mechanism specificity:**
- All 3 subjects exhibit: (a) multiple products in same author's GitHub org, (b) functional or strategic coupling, (c) public ecosystem narrative (README ecosystem section / portfolio-builder claim)
- **Mechanism is specifiable**: "single author publishes ≥2 functionally-coupled products under shared brand/org with explicit cross-product narrative"

**Promotion verdict at v66 (predicted):** **PROMOTE sub-type from candidate to CONFIRMED** under Pattern #19. Criterion #2 + #3 + #4 all satisfied.

### Potential v66 sub-archetype 3-axis deliberation

The 3 portfolio shapes might themselves form a 3-axis sub-taxonomy:

- **19a methodology-portfolio** (gotalab) — multiple skill products vertical-by-methodology
- **19b viral-and-commercial-portfolio** (forrestchang) — viral distillation + commercial platform
- **19c domain-vertical-with-cross-vendor-portfolio** (AgriciDaniel) — domain ecosystem + dual-platform port + dual-license

OR they may consolidate to a single sub-type with 3 instances. v66 audit decides.

## Sister-product strategy as Pattern Library implication

The **cross-product mechanism** has 4 distinct sub-mechanisms observable at v64:

| Sub-mechanism | claude-seo evidence | Cross-corpus presence |
|---|---|---|
| **Cross-product workflow chain** | 5-step README workflow | Pattern #19 N=3 |
| **Re-bundle existing standalone as extension** | Banana dual-role | NEW v64 observation |
| **Solo-author cross-vendor parallel-port** | codex-seo | NEW v64 observation (Pattern #18 Layer 2) |
| **Author-original framework as CC BY 4.0 with sync-from-separate-repo** | FLOW + sync_flow.py | NEW v64 observation |

The last 3 are corpus-firsts at v64. The Pattern #19 N=3 promotion alone is strongest evidence; the 3 corpus-firsts are observational at this stage.

## Personal brand + domain integration

| Asset | URL |
|---|---|
| **Personal brand site** | `agricidaniel.com` |
| **Product marketing site** | `claude-seo.md` (dedicated subdomain) |
| **Blog** | `agricidaniel.com/blog` — "deep dives on AI marketing automation" |
| **YouTube channel** | `youtube.com/@AgriciDaniel` — tutorials + demos (with embedded `/seo audit` demo gif in README) |
| **GitHub org** | `github.com/AgriciDaniel` (all 5 products live here) |
| **Release blog automation** | `/release-blog` slash command auto-publishes to `claude-seo.md/blog/` with cover image / SEO metadata / FAQ schema / internal linking / sitemap+llms.txt updates / Vercel deployment / Google indexing |

The **`/release-blog` meta-command** is corpus-first: the plugin **ships a self-marketing pipeline that auto-publishes its own releases to its own marketing site with full SEO+indexing automation**. Sister to oh-my-claudecode v27's mini-blog mechanism but at much higher automation.

Pattern Library candidate consideration for v66: **"Self-Marketing Release Pipeline as Plugin Meta-Command"** — observational at v64.

## Community ecosystem layer (post-portfolio)

Beyond the 5-product own-portfolio, claude-seo participates in a **broader community ecosystem**:

| Reference | Type |
|---|---|
| AI Marketing Claude (`zubair-trabzada/ai-marketing-claude`) | Community sister-product (third-party author) |
| AI Marketing Hub Pro Hub Challenge | Gamified-curated community contribution mechanism (5 named v1.9.0 contributors) |
| Ahrefs MCP (`@ahrefs/mcp`) | Official commercial MCP server |
| Semrush MCP | Official commercial MCP server |
| GSC MCP / PageSpeed MCP / DataForSEO MCP | Community MCP servers |

The **layered ecosystem** (own-portfolio + community + commercial MCP) is corpus-rare richness for a solo-individual product.

## Why this entity is the v64 Pattern Library PRIMARY deliverable

**Pattern #19 ecosystem-portfolio-builder N=3 strengthening promotion-eligibility** is the **strongest single Pattern Library implication** of v64 wiki ship. All other implications (Pattern #18 strengthenings + 2 NEW candidates) are secondary or observational.

Phase 5 will register:
- Strengthening note within Pattern #19 entry (`_patterns/03-active-candidates.md` or `_patterns/04-confirmed-patterns.md` depending on Pattern #19's exact confirmed-vs-candidate status post-v63)
- Pre-registered v66 audit item: "Pattern #19 ecosystem-portfolio-builder sub-type N=3 promotion deliberation"
- Cross-link to this entity page as evidence-document

See [Entity 4 — multi-platform + Pattern Library implications](./entity-4-multi-platform-and-patterns.md) for the full v64 Pattern Library package.
