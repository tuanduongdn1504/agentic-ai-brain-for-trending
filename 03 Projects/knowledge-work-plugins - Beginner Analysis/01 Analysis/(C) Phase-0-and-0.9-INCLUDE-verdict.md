# Phase 0 + Phase 0.9 STRICT INCLUDE verdict — knowledge-work-plugins v104

**Subject**: [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)
**Date**: 2026-05-28
**Routine**: v2.3.1
**Verdict**: **STRONGEST INCLUDE 4/4** with (a)(c) STRONGEST + (b)(d) STRONG

---

## Phase 0: Tier classification

**Tier**: T1 Assistant Skill / Vendor-Built Multi-Vertical Knowledge-Work Plugin Bundle

Distinct from v92 claude-for-legal (single-domain legal + 12 sub-plugins), v95 claude-plugins-official (Anthropic-managed marketplace with external-plugin submissions), v93 anthropics/skills (SKILL.md spec + template reference), v102 claude-cookbooks (Jupyter notebook patterns reference).

**Sub-distinction proposal**: Within (a)-7 Foundational-Vendor-Direct-Source cluster, NEW sub-typology candidate "Vendor-Built-In-House Multi-Vertical Plugin Bundle at Single Repo" — vendor builds all plugins in-house bundled in single repo across cross-vertical scope; distinct from v95 marketplace-curated external-submissions, v92 single-domain-multi-plugin, v93 spec-reference, v102 cookbook-reference.

---

## Phase 0.9: STRICT INCLUDE 4-criteria evaluation

### (a) Cultural-peer / Storm Bear-axis cluster — STRONGEST PASS

**(a)-7 Foundational-Vendor-Direct-Source 4-of-4 criteria**:

| Criterion | Evidence | Verdict |
|---|---|---|
| Anthropic PBC primary org | `anthropics/knowledge-work-plugins` | ✅ PASS |
| Claude product upstream of corpus | Claude Cowork product direct + Claude Code compatible | ✅ PASS |
| Anthropic-authoritative knowledge-work patterns source | "11 plugins built and inspired by our own work" | ✅ PASS |
| `anthropics/*` primary GitHub org | Confirmed | ✅ PASS |

**(a) verdict**: STRONGEST via (a)-7 4-of-4 criteria PASS = (a)-7 cluster N=5 STRONGER POST-PROMOTION STRENGTHENING (v92 + v93 + v95 + v102 + **v104**).

---

### (b) Cost-of-trial × functional-fit — STRONG PASS

**Cost-of-trial**: LOW (`claude.com/plugins` direct install for Cowork OR `/plugin marketplace add` + install for Claude Code; ~3-5 min reversible)

**Functional-fit**: PARTIAL DIRECT
- DIRECT-applicable verticals for Storm Bear Scrum coaching: Productivity + Operations + Engineering + Product-Management + Human-Resources
- INDIRECT or N/A verticals: Sales + Customer-Support + Finance + Legal + Bio-Research + Enterprise-Search + Marketing + Data + Design + Small-Business + Partner-Built + PDF-Viewer

**(b) verdict**: STRONG (LOW cost × PARTIAL DIRECT applicability with ~5/17 verticals applicable; selective install per vertical = reduces low-relevance overhead). STRONG not STRONGEST because most verticals are N/A for Storm Bear specific role.

---

### (c) Methodology-influence-node / corpus-novelty — STRONGEST PASS

**Methodology-novelty axes**:

1. **(a)-7 cluster N=5 STRONGER POST-PROMOTION STRENGTHENING** — extends cluster to 5-instance at foundational-vendor-direct-source axis (administrative-only at v105 audit; no further promotion needed since (a)-7 already at formal (a) sub-axis post v96)
2. **NEW sub-distinction within (a)-7 cluster** "Vendor-Built-In-House Multi-Vertical Plugin Bundle" vs "Marketplace-Curated External Submissions" (v95) vs "Cookbook Reference" (v102) vs "SKILL.md Spec Reference" (v93) vs "Single-Domain-Multi-Plugin" (v92) = 5-variant sub-typology now mature within (a)-7
3. **CORPUS-FIRST README-claim-vs-actual-count divergence at Anthropic-direct-org subject** (README states "11 plugins" but actual content = 17 vertical + 1 admin + 1 partner-built + 1 pdf-viewer = ~19 subplugin directories; README under-claims actual content) — Pattern #82 NEGATIVE-EVIDENCE under-claiming variant CORPUS-FIRST observation
4. **CORPUS-FIRST `partner-built/` top-level integration directory at Anthropic-direct-org subject** — vendor-curated partner-vendor-submission directory at separate scope from main vertical-plugins (observational; structurally distinct from v95 `external_plugins/` per-plugin integration which was per-plugin not per-meta-bundle)
5. **CORPUS-FIRST CONNECTORS.md artifact at per-subplugin scope** in v60+ window (each vertical-plugin ships own CONNECTORS.md = MCP-connector documentation discipline at sub-package level)
6. **CORPUS-FIRST `pdf-viewer/` viewer-utility-plugin at vendor-direct-org-bundle scope** in v60+ window (single-purpose utility-plugin in multi-vertical bundle)
7. **Per-subplugin LICENSE + root LICENSE combination** (knowledge-work-plugins has root LICENSE Apache 2.0 + per-subplugin LICENSE files = distinct from v95 "No-Root-LICENSE Per-Subplugin-Delegation" Library-vocab; v104 = "Root LICENSE + Per-Subplugin LICENSE Combination" NEW Library-vocab variant)
8. **Pattern #57 sub-variant 57k Standards-Conformance-Layer Chain N=6 STRONGEST POST-PROMOTION STRENGTHENING via 8-implementer chain extension** (v76 → v93 → v98 → v99 → v100 → v102 → v103 → **v104**; arc-velocity 8-implementer-in-10-calendar-days continues unusually-fast but does not accelerate further from v103 7-implementer-in-9)
9. **17-vertical scope at single Anthropic-direct-org subject** = NEW CORPUS-RECORD vertical-count at single subject (exceeds v92 claude-for-legal 12-vertical legal-domain prior record by ~42%)
10. **Anthropic-direct-org pace observation**: 5 Anthropic-direct-org subjects in 12 calendar days (v92 2026-05-23 → v104 2026-05-28 = 5-of-12 calendar days = ~42% Anthropic-direct-org rate at recent corpus) = corpus-novel observational density for foundational-vendor-direct-source axis

**(c) verdict**: STRONGEST — 5+ corpus-firsts + (a)-7 N=5 STRENGTHENING + NEW sub-distinction within (a)-7 cluster + Pattern #82 NEGATIVE-EVIDENCE corpus-novel under-claiming variant + CORPUS-RECORD vertical-count.

---

### (d) Corpus-recursive ties / methodology-influence chain — STRONG PASS

**Direct corpus-recursive ties**:

1. **(a)-7 Foundational-Vendor-Direct-Source cluster N=5** = 5 Anthropic-direct-org subjects (v92 + v93 + v95 + v102 + v104)
2. **Pattern #57 sub-variant 57k Standards-Conformance-Layer Chain N=6 STRONGEST** via 8-implementer chain extension at agentskills.io standard
3. **Library-vocab #12 LLM-routing artifacts**: 17 subplugin `skills/` directories + root `.claude-plugin/` = multi-subplugin distribution density
4. **Pattern #45 sub-typology variant** "Root + Per-Subplugin LICENSE Combination" distinct from v95 sub-typology "No-Root-LICENSE Per-Subplugin-Delegation"
5. **NEW Anthropic-direct-org INTER-bundle multi-team observation**: 5 Anthropic-direct-org subjects in cluster represent distinct teams (Claude for Legal team + Agent Skills team + Plugin Marketplace team + Cookbook team + Knowledge Work team) = NEW corpus-novel meta-observation "Authoritative-Vendor 5-Team Concurrent-Direct-Source-Product Discipline" extending v102's "Two-Role Foundational-Vendor Implementation Discipline"

**(d) verdict**: STRONG — multiple corpus-recursive ties at sub-axis + sub-variant + Library-vocab + sub-typology layers; STRONG not STRONGEST because corpus-recursive observations are extensions of already-PROMOTED items, not standalone event class.

---

## Overall verdict: STRONGEST INCLUDE 4/4

- (a) **STRONGEST** via (a)-7 4-of-4 criteria PASS (Anthropic PBC direct + Claude Cowork upstream + canonical knowledge-work patterns source + anthropics/* org)
- (b) STRONG LOW cost-of-trial × PARTIAL DIRECT functional-fit (~5/17 verticals applicable)
- (c) **STRONGEST** 5+ corpus-firsts + (a)-7 N=5 STRENGTHENING + NEW sub-distinction within (a)-7 cluster + CORPUS-RECORD 17-vertical scope + Pattern #82 NEGATIVE-EVIDENCE under-claiming
- (d) STRONG corpus-recursive ties across multiple patterns + Library-vocab + NEW 5-team-concurrent-direct-source meta-observation

**Streak**: 36 PASS (v65-v83 + v85-v100 + v102-v104) + 1 OVERRIDE (v84) = **"36+1*"** NEW CORPUS-RECORD = first 17-consecutive milestone post-v84 OVERRIDE
**INCLUDE rate**: 38-instance window v65-v104 = 37 PASS + 1 OVERRIDE = **97.4% INCLUDE rate** (precise 97.37%; uptick from v103 97.30%)
**Strength categorization v65-v104**: STRONGEST × 17 + STRONG × 13 + MODERATE × 4 + WEAK × 5 + OVERRIDE × 1 (STRONGEST extends lead by 4 over STRONG)

---

## Phase 4b PRIMARY identification

**PRIMARY**: (a)-7 Foundational-Vendor-Direct-Source sub-axis **N=5 STRONGER POST-PROMOTION STRENGTHENING with NEW sub-distinction within (a)-7 cluster** via Phase 4b vehicle #3 within-pattern strengthening proposal-document. v92 anchor + v93 N=2 + v95 N=3 PROMOTION at v96 + v102 N=4 STRENGTHENING + **v104 N=5 STRONGER STRENGTHENING** with 5-variant sub-typology emerging within cluster.

**5-variant sub-typology within (a)-7 cluster** (NEW corpus observation; v2.4 codification candidate):
1. **Single-Domain-Multi-Plugin** (v92 claude-for-legal — 12 legal-vertical plugins)
2. **SKILL.md Spec + Template Reference** (v93 anthropics/skills — authoritative reference for agentskills.io standard)
3. **Marketplace-Curated External Submissions** (v95 claude-plugins-official — Anthropic-managed marketplace accepting external-plugin submissions)
4. **Cookbook Reference** (v102 claude-cookbooks — Jupyter notebook canonical patterns)
5. **Vendor-Built-In-House Multi-Vertical Plugin Bundle** (v104 knowledge-work-plugins — 17 vertical-plugins all-Anthropic-built in single repo)

**SECONDARY observations held at OC layer per cascade-discipline**:
- Pattern #57 sub-variant 57k 8-implementer chain extension (post-PROMOTION strengthening; arc-velocity stable)
- CORPUS-FIRST README-claim-vs-actual-count divergence (Pattern #82 NEGATIVE-EVIDENCE under-claiming variant)
- CORPUS-FIRST `partner-built/` top-level integration directory at Anthropic-direct-org subject
- CORPUS-FIRST CONNECTORS.md per-subplugin artifact
- CORPUS-FIRST `pdf-viewer/` viewer-utility-plugin in vendor-bundle
- NEW Library-vocab "Root LICENSE + Per-Subplugin LICENSE Combination" distinct from v95
- CORPUS-RECORD 17-vertical scope at single Anthropic-direct-org subject
- NEW corpus-novel meta-observation "Authoritative-Vendor 5-Team Concurrent-Direct-Source-Product Discipline" (extends v102 two-role observation to 5-team observation)
- Anthropic-direct-org cluster pace: 5-of-12-calendar-days = ~42% rate at recent corpus

---

## Honest dissent / caveats

- **(a)-7 N=5 is post-PROMOTION administrative-only**: sub-axis already at formal (a) status post v96 PROMOTION; v104 evidence is cluster-strengthening not pattern-promotion event
- **5-variant sub-typology within (a)-7 cluster is corpus-novel observation**: framing-decision required at v105 audit — is this a v2.4 codification candidate or just an observational tracking-axis?
- **(c) STRONGEST verdict load-bearing**: 5+ corpus-firsts pressure-test required at v105 audit; some claims (`partner-built/`, `pdf-viewer/`, CONNECTORS.md, README-under-claiming) are observational and may be downgraded if pressure-tested as ad-hoc-coined
- **Pattern #82 NEGATIVE-EVIDENCE under-claiming**: rare in corpus (most Pattern #82 instances are over-claiming); v104 = README "11 plugins" vs actual ~19 directories = first clean under-claiming evidence in v60+ window; v2.4 codification candidate for Pattern #82 sub-variant taxonomy expansion
- **(b) STRONG via PARTIAL DIRECT not STRONGEST**: knowledge-work-plugins covers 17 verticals; only ~5 directly applicable to Storm Bear Scrum coaching role; selective install needed
- **Anthropic-direct-org pace 5-in-12-calendar-days**: corpus-novel velocity observation; could indicate (a) Anthropic ramping up open-source-publication cadence OR (b) Storm Bear self-selection bias toward Anthropic subjects at recent ships OR (c) recent Anthropic product launches (Claude Cowork) driving plugin publication surge; framing-decision at v105 audit
