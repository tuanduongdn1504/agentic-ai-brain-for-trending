# claude-code-system-prompts — Beginner Analysis

> **Subject:** [`Piebald-AI/claude-code-system-prompts`](https://github.com/Piebald-AI/claude-code-system-prompts) — *"All parts of Claude Code's system prompt, 24 builtin tool descriptions, sub agent prompts (Plan/Explore/Task), utility prompts. Updated for each Claude Code version."*
> **Wiki version:** v65
> **Build date:** 2026-05-13
> **Routine:** `llm-wiki-routine-v2.1` (Storm Bear vault)

---

## Phase 0 — Probe summary

### 12-axis classification

| Axis | Value |
|------|-------|
| **Tier** | **T1 Augmentation — NEW sub-archetype: reverse-engineering-reference-archive** (first reference-archive T1 in 64-wiki corpus; distinct from prior T1 sub-archetypes — general-purpose mattpocock-skills v57 / curated-meta awesome-claude-skills v50 / corporate-curated agent-skills-of-vercel v51 / single-artifact karpathy-skills v63 / domain-vertical-skill-collection claude-seo v64). Functionally **observes T1 host (Claude Code) without being a T1 augmentation in the producer sense** — but consumed AS T1-reference by users. Structural caveat: classification within T1 preserves taxonomic continuity; tier-taxonomy review for potential T-Reference category pre-registered v66 audit. |
| **Archetype** | **Corporate-org Piebald-AI** + commercial-product portfolio (Piebald commercial agentic IDE at piebald.ai + tweakcc local-patching tool + claude-code-system-prompts open-source reference) |
| **Scale tier** | Medium-high engagement (**10,176 stars / 1,811 forks / ~176 days = ~57.8 stars/day**; below Pattern #52 EXTREME-VIRAL 300+/day threshold; **17.8% fork ratio = CORPUS-RECORD active-deployment intent at this scale** — exceeds claude-seo v64 15.3%) |
| **Primary lang** | JavaScript (`tools/updatePrompts.js` extraction script, 19.5 KB) + Markdown (293 system-prompt files) |
| **Packaging tool** | None for the archive (reference-only; not installable); related tool **tweakcc** is separately packaged for local-installation patching |
| **Origin story** | Corporate-org **Piebald-AI** builds **Piebald** (commercial agentic IDE at piebald.ai); `claude-code-system-prompts` is **open-source reverse-engineering reference** released 2025-11-18 as auxiliary to commercial product portfolio; **updated within minutes of each Claude Code release** |
| **Methodology** | **Reverse-engineering reference-archive methodology** — automated extraction from compiled npm package (`@anthropic-ai/claude-code`) via `tools/updatePrompts.js`; **CHANGELOG-as-absorption-ledger discipline tracking 176 versions** (127 full + 49 no-change placeholder) with per-version commit links + token-count deltas + per-prompt-change descriptions |
| **Governance file count** | **Minimal** — README.md (69 KB) + CLAUDE.md (1.6 KB) + LICENSE (1 KB) + CHANGELOG.md (211 KB) + system-prompts/ (293 files) + tools/updatePrompts.js — **stark contrast with claude-seo v64's 13+ governance files**; reference-archive subjects need minimal governance |
| **Agent/skill count** | **293 system-prompt files** extracted (110+ unique prompts; some same prompt with version variants). 6 categories: **~30 Agent Prompts** (sub-agents + creation assistants + slash commands + utilities) + **~50 Data templates** (SDK references + Managed Agents docs + Claude API references in C# / Go / Java / PHP / Python / Ruby / TypeScript / cURL) + **~50 System Prompts** (main system prompt fragments — communication style / harness / memory / plan mode / etc.) + **~40 System Reminders** (per January 2026 update) + **~50 Tool Descriptions** (Bash / Edit / Read / Write / Grep / Glob / TodoWrite / WebFetch / WebSearch / TaskCreate / Skill / etc. + extensive Bash sub-rules) + **~25 Skill prompts** |
| **i18n coverage** | EN-only artifact documentation (corpus-typical for reverse-engineering archives) |
| **Intellectual influence cited** | **Anthropic Claude Code** (extracted FROM Claude Code's compiled source); NO external methodology influences — this is a pure observational/extraction archive. Reverse-engineering is the primary intellectual stance. Sister-related to **system-prompts-leaks v21** (Pattern #21 N=1 baseline) but at much larger scale + continuous-versioning discipline. |
| **Agent platforms supported** | **Reference for Claude Code only** — single-platform observational archive. Sister tool **tweakcc** applies patches to local Claude Code installation. |

### Tier placement decision

**T1 Augmentation — reverse-engineering-reference-archive sub-archetype (NEW v65).**

Justified by:
- Lives in Claude Code ecosystem (T1 surface focus)
- Function = reference for understanding T1 host's internals (observational, not augmentation in producer sense)
- **NEW sub-archetype within T1 Augmentation:** reverse-engineering reference archive — distinct from all prior T1 sub-archetypes (each prior was a SKILL collection FOR Claude Code; this is OBSERVATION ABOUT Claude Code)

**Structural caveat:** The functional category is genuinely distinct — this subject **does not augment** Claude Code (no skills / no plugins / no install path). It DOCUMENTS Claude Code's internals as reference. Pure observability layer.

**Alternative considered 1:** T5 Library/SDK with sub-archetype reference-archive (provides observability primitive). REJECTED — reference archive is consumed by humans as documentation, not by code as library.

**Alternative considered 2:** NEW tier "T-Reference" or "T6 Meta". DEFERRED — tier expansion requires operator approval at audit; pre-register v66 audit for tier-taxonomy review.

**Author's own framing:** README opens with "All parts of Claude Code's various system prompts and their associated token counts as of [Claude Code v2.1.140]" — explicitly archival/observational framing.

### Phase 4b PRIMARY routing mode

**🎯 PRIMARY: Pattern #78 Living-Domain-Standards Tracking N=2 STRENGTHENING — PROMOTION-ELIGIBLE at v67 (potentially accelerated to v66 mini-audit)**

Pattern #78 was registered N=1 stale-flagged at v64 (claude-seo). v65 provides **CORPUS-FIRST 1-wiki un-stale-via-N=2-evidence cycle** — fastest un-stale cycle in 64-wiki corpus history (sister mechanism to v62→v63 1-wiki counter-evidence cycle for Pattern #76).

**Cross-archetype N=2 evidence:**

| Subject | Wiki | External authority tracked | Sub-mechanism |
|---|---|---|---|
| **claude-seo** | v64 | Google Quality Rater Guidelines + Schema.org + Core Web Vitals + ISO 639/3166 codes | **78a multi-vendor-industry-domain-standards** |
| **claude-code-system-prompts** | v65 | Anthropic Claude Code system prompts (176-version archive) | **78b single-vendor-product-internals-archive** |

**3 criteria evaluation for v65:**
1. ✅ Explicit external-authority citation with date: "Claude Code v2.1.140 (May 12th, 2026)"
2. ✅ Deprecation-tracking discipline: CHANGELOG tracks `**NEW:**` / `**REMOVED:**` markers per version
3. ✅ Versioned absorption ledger: 211 KB CHANGELOG literally embodies the discipline (176 versions documented with per-version token-deltas + change descriptions)

**Promotion-eligibility at v67 stale-check window (could be accelerated to v66 audit):**
- Criterion #2 structural-unambiguity-at-N=2: 2 distinct sub-mechanisms (78a vs 78b) = SATISFIED with margin
- Criterion #3 cross-archetype: corporate-Piebald-AI v65 + solo-AgriciDaniel v64 = 2 distinct archetypes
- Criterion #4 mechanism specificity: 3 criteria specifiable; sister-criterion candidate evidence to come

### Secondary routing modes

- **Pattern #21 System Prompts Leaks N=2 strengthening at CORPUS-RECORD scale** — sister to v21 system-prompts-leaks N=1; v65 is at 10K stars vs ? at v21 + **continuous-versioning** (177 versions) vs one-time leak. Different mechanism: v21 was leak/exfiltration; v65 is **extraction-from-compiled-binary discipline as ongoing practice**. Sub-variant 21b: continuous-extraction-versus-one-time-leak. **POTENTIAL UN-STALE for Pattern #21** if currently stale; depends on Pattern #21 current status.
- **Pattern #57 Recursive Corpus Reference — STRONGEST 57c instance ever observed** — Claude Code is THE most-corpus-cited product across 64 prior wikis (every T1 + many T4/T5 subjects reference Claude Code as host). v65 documents THE most-referenced product's internals = corpus-recursive at MAXIMUM DEPTH. Strongest 57c instance to date (sister to v63 Karpathy LLM-Wiki-pattern corpus-foundation-individual inheritance, but at PRODUCT-LEVEL not individual-level).
- **NEW Pattern candidate: Continuous-Reverse-Engineering Reference Archive (NEW v65 N=1 stale-flagged)** — corporate-org maintains reference archive of closed-source-product internals with continuous-versioning discipline. Distinct from one-time leak (Pattern #21 v21 system-prompts-leaks) AND from documentation-by-authoring. 3 criteria: (a) third-party (not vendor) archive; (b) continuous-versioning per upstream release; (c) extraction-from-compiled-source (not vendor cooperation). N=1 stale-flagged at v65; un-stale criterion = 2nd subject matching all 3 criteria.
- **Pattern #19 ecosystem-portfolio-builder N=4 strengthening at corporate-org archetype** — Piebald-AI = 4th example after gotalab solo-Japanese v61 / forrestchang solo-engineer-commercial v63 / AgriciDaniel solo-individual-SEO-vertical v64. Piebald-AI portfolio: Piebald commercial + claude-code-system-prompts + tweakcc. **N=4 across 4 distinct author archetypes solidifies v66 promotion verdict** (was N=3 at v64; now N=4 with corporate-org type added).
- **Pattern #66 Supply Chain Awareness OBSERVATION-TRACK extension** — Piebald-AI explicit "extracted reference material, not modifiable source code" + "Editing files here does not change Claude Code's behavior" warnings = meta-supply-chain awareness at reference-archive level (educates users about what the archive IS NOT).

### Phase 0.9 Storm Bear meta-entity check

**STRICT 1-of-4 inclusion check:**

| Criterion | Result | Evidence |
|---|---|---|
| (a) Author archetype peer | **FAIL** | Piebald-AI = corporate-org with commercial agentic IDE product (Piebald at piebald.ai). NOT solo-individual / solo-Asian-diaspora / solo-Scrum-coach archetype-peer per Phase 0.9 STRICT discipline. |
| (b) Operational tool for vault | **STRONG PASS** | Storm Bear vault uses **Claude Code as PRIMARY OPERATING SUBSTRATE** (LLM Wiki Routine v2.1 runs ON Claude Code; this very wiki is being built in Claude Code right now). Having direct documentation of Claude Code's actual 110+ system prompts IS deeply operational: enables understanding why Claude Code behaves as it does in specific situations + informs vault routine adjustments + reveals deprecated/changed behaviors across 176 versions. **Corpus-rare STRONG operational PASS** — most subjects (b) are speculative-operational; this is direct-operational. |
| (c) Methodology-influence-node | **STRONG PASS** | Claude Code's actual system prompts **SHAPE how LLM Wiki Routine v2.1 must be designed** (every routine instruction must work within Claude Code's prompt envelope; understanding what's in that envelope = direct methodology-influence-source). Sister to v63 Karpathy LLM-Wiki-pattern inheritance but at **PRODUCT-LEVEL not individual-level**. The vault routine's design choices (Phase 0.9 STRICT / 4-entity discipline / direct-write velocity) are all bounded by Claude Code's prompt-envelope behaviors. |
| (d) In-corpus reference | **STRONGEST PASS in 64-wiki corpus history** | Claude Code is THE most-referenced product across 64 prior corpus wikis (every T1 wiki — mattpocock v57 / awesome-claude-skills v50 / agent-skills-of-vercel v51 / karpathy-skills v63 / claude-seo v64 / cc-sdd v61 / codex-plugin-cc v62 references Claude Code; many T4 wikis — free-claude-code v60 translates TO Claude Code; many T5 wikis cite Claude Code). v65 = **direct documentation of THE most-referenced product**. **Corpus-recursive at MAXIMUM DEPTH possible.** |

**Decision: 0-of-4 explicit (a) FAIL + 3-of-4 STRONG PASS (b)(c)(d) → STRONGEST INCLUDE in 9-instance post-amendment Phase 0.9 window history.**

**Streak counter:** Storm Bear meta-entity 4-RESET to 0 at v64 SKIP → v65 STRONG PASS → **STREAK RESTARTS at 1 post-v64-RESET.**

**10-instance Phase 0.9 post-amendment window v56-v65:** v56 PASS / v57 PASS / v58 PASS / v59 SKIP / v60 PASS / v61 PASS / v62 PASS / v63 PASS / v64 SKIP / **v65 STRONG PASS** = **8 PASS / 2 SKIP = 80% INCLUDE rate** (up from 77.8% at v64). v65 also represents **STRONGEST 3-of-4 STRICT PASS in window history** (most prior PASSes had 1-2 STRONG criteria; v65 has 3 STRONG + only (a) FAIL).

**Phase 0.9 STRICT discipline validation:** v65 demonstrates STRICT amendment correctly INCLUDES subjects that are deeply operational + methodology-relevant + corpus-recursive even when (a) author-archetype-peer fails. Calibration **healthy** — neither over-strict nor over-inclusive.

**Entity slot allocation post-INCLUDE:**
- Entity 1: claude-code-system-prompts core artifact + 293-prompt-file extraction architecture
- Entity 2: Pattern #78 N=2 strengthening + 1-wiki un-stale-via-N=2-evidence cycle (PRIMARY Pattern Library deliverable)
- Entity 3: Piebald-AI corporate-org + Pattern #19 N=4 + Pattern #57 strongest-instance + ecosystem (Piebald commercial + tweakcc)
- Entity 4: **Storm Bear meta-entity — corpus-recursive reference at maximum depth + Phase 0.9 STRONGEST-INCLUDE evidence**

---

## Pattern Library implications (preview — Phase 5 will register)

**Direct strengthenings (within already-CONFIRMED or -CANDIDATE patterns):**

1. **Pattern #78 Living-Domain-Standards Tracking N=2 strengthening — PROMOTION-ELIGIBLE at v67 (or accelerated v66)** — claude-seo v64 78a-multi-vendor + claude-code-system-prompts v65 78b-single-vendor-product = N=2 cross-archetype with 2 distinct sub-mechanisms
2. **Pattern #21 System Prompts Leaks N=2 strengthening at corpus-record scale** — extension of v21 system-prompts-leaks N=1; v65 at 10K stars with continuous-versioning discipline (176 versions) vs v21 one-time leak; sub-variant 21b continuous-extraction-versus-leak; **potential UN-STALE for Pattern #21**
3. **Pattern #57 Recursive Corpus Reference 57c STRONGEST instance** — Claude Code = THE most-corpus-cited product across 64 wikis; v65 documents THE most-referenced product's internals = corpus-recursive at maximum depth; sister to v63 Karpathy corpus-foundation-individual inheritance but at PRODUCT-level
4. **Pattern #19 ecosystem-portfolio-builder N=4 strengthening at corporate-org archetype** — Piebald-AI corporate-org 4th example (after gotalab solo-Japanese + forrestchang solo-engineer-commercial + AgriciDaniel solo-individual-SEO-vertical); strengthens v64 N=3 PROMOTION-ELIGIBLE to N=4 with 4 distinct archetypes
5. **Pattern #66 Supply Chain Awareness OBSERVATION-TRACK extension** — Piebald-AI meta-supply-chain awareness disclosures (educates users about what the archive IS NOT)
6. **Pattern #18 N/A** — single-platform reference archive (not multi-platform); useful counter-evidence for Pattern #18 cross-platform breadth — reference archives don't need multi-platform reach

**NEW top-level candidate registrations:**

7. **NEW Pattern candidate: Continuous-Reverse-Engineering Reference Archive N=1 stale-flagged at v65** — corporate-org maintains reference archive of closed-source-product internals with continuous-versioning discipline. 3 criteria: (a) third-party (not vendor) archive; (b) continuous-versioning per upstream release ("within minutes"); (c) extraction-from-compiled-source (not vendor cooperation). Distinct from one-time leak (Pattern #21 v21) AND from documentation-by-authoring (typical T1 docs). Un-stale criterion: 2nd subject matching all 3 criteria. Re-evaluate v68 (+3 wikis).

**Observational candidates (NOT formal registrations at v65):**

8. **Tier-Taxonomy Review observational candidate** — claude-code-system-prompts is FIRST corpus subject that genuinely doesn't fit T1-T5 producer schema cleanly. Pre-register v66 audit deliberation: introduce T6 Reference/Meta tier? OR extend T1 with reference-archive sub-archetype as v65 elected (current default)?
9. **1-wiki-un-stale-via-N=2-evidence-cycle observational** — sister to v62→v63 1-wiki counter-evidence cycle for Pattern #76 (2026-05-07 → 2026-05-08); v64→v65 1-wiki un-stale cycle for Pattern #78 (2026-05-13 → 2026-05-13 same day; FASTEST un-stale cycle in corpus history). Pattern Library candidate: "rapid-pattern-evolution observational track" — when patterns register and immediately receive corpus evidence to evolve

**Cross-wiki standards check:**

- **OpenClaw / Hermes runtime:** N/A (reference archive; no runtime)
- **MCP:** referenced AS subject (Chrome browser MCP tools + Computer Use MCP) — observed, not consumed
- **AGENTS.md:** NO — single-platform reference (Claude Code only)
- **anthropics/skills protocol:** SKILL prompts extracted (~25 skill prompts) — provides ground-truth reference for what Anthropic skill spec looks like at v2.1.140
- **CLAUDE.md primitive:** YES — repo's own CLAUDE.md (1.6 KB) explicitly addresses "For AI agents working with this repository" warning that files are extracted-not-modifiable

---

## Sources ingested (Phase 2 will write cluster summaries)

1. **README.md** (69 KB, 405 lines) — comprehensive overview + 293-file inventory across 6 categories (Agent Prompts / Data / System Prompt / System Reminders / Tool Descriptions / Skills) + token-count per file + per-file descriptions
2. **CLAUDE.md** (1.6 KB) — minimal project instructions; "For AI agents" warning about extracted-not-modifiable status
3. **CHANGELOG.md** (211 KB, 1896 lines) — 176 version entries (127 full + 49 no-change placeholder) since v2.0.14; per-version commit links + token-deltas + per-prompt-change descriptions
4. **system-prompts/** directory — 293 prompt files (110+ unique prompts; YAML frontmatter with Claude Code version + template variables)
5. **tools/updatePrompts.js** (19.5 KB) — automated extraction script; demonstrates extraction methodology
6. **LICENSE** (1 KB) — MIT
7. Repo metadata via GitHub API (10,176 stars / 1,811 forks / 118 subscribers / created 2025-11-18 / pushed 2026-05-13)

---

## Cross-wiki siblings (mandatory cross-references)

**Pattern #78 Living-Domain-Standards Tracking N=2 peers:**
- [claude-seo v64](../claude-seo%20-%20Beginner%20Analysis/) — 78a multi-vendor industry domain standards baseline

**Pattern #21 System Prompts Leaks lineage:**
- [system-prompts-leaks v21](../system-prompts-leaks%20-%20Beginner%20Analysis/) — Pattern #21 N=1 baseline; one-time leak archive predecessor (in `_state/05-projects-v1-v29.md`)

**Pattern #19 ecosystem-portfolio-builder N=4 peers:**
- [cc-sdd v61](../cc-sdd%20-%20Beginner%20Analysis/) — gotalab solo-Japanese N=1
- [andrej-karpathy-skills v63](../andrej-karpathy-skills%20-%20Beginner%20Analysis/) — forrestchang solo-engineer-commercial N=2
- [claude-seo v64](../claude-seo%20-%20Beginner%20Analysis/) — AgriciDaniel solo-individual-SEO-vertical N=3

**T1 Augmentation peers (skills collections at different sub-archetypes):**
- [mattpocock-skills v57](../mattpocock-skills%20-%20Beginner%20Analysis/) — 19-skill general-purpose
- [awesome-claude-skills v50](../awesome-claude-skills%20-%20Beginner%20Analysis/) — curated-meta aggregator
- [agent-skills-of-vercel v51](../agent-skills-of-vercel%20-%20Beginner%20Analysis/) — corporate-curated
- [andrej-karpathy-skills v63](../andrej-karpathy-skills%20-%20Beginner%20Analysis/) — single-artifact behavioral
- [claude-seo v64](../claude-seo%20-%20Beginner%20Analysis/) — domain-vertical-skill-collection

**Claude-Code-host backend bridge peer:**
- [free-claude-code v60](../free-claude-code%20-%20Beginner%20Analysis/) — translates TO Claude Code's Anthropic Messages API (consumes Claude Code's surface) — sister observational stance to v65 (which extracts FROM Claude Code's compiled binary)

**Corporate-org plugin marketplace peer:**
- [codex-plugin-cc v62](../codex-plugin-cc%20-%20Beginner%20Analysis/) — OpenAI publishes for Claude Code (cross-vendor cooperation) — observational sister to v65 (Piebald-AI publishes ABOUT Claude Code)

---

## Build status

| Phase | Status |
|---|---|
| Phase 0 (probe) | ✅ COMPLETE |
| Phase 1 (scaffold) | ✅ COMPLETE |
| Phase 2 (sources) | ⏳ in progress (3 cluster summaries) |
| Phase 3 (entities) | pending (4 entity pages; **INCLUDE Storm Bear meta-entity** per Phase 0.9 STRONG PASS) |
| Phase 4a (beginner guide bilingual) | pending |
| Phase 4b (Pattern #78 N=2 promotion deliverable) | pending |
| Phase 5 (iteration log + Pattern Library update) | pending |
| Phase 6 (vault sync) | pending |
