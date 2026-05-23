# (C) anthropics/skills — Beginner Analysis project context

> **Routine:** `llm-wiki-routine-v2.3` (FOURTH execution under v2.3 production-baseline; v90 = first, v91 = second, v92 = third, v93 = this build)
> **Subject:** [anthropics/skills](https://github.com/anthropics/skills)
> **Subject tagline:** *"Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks."*
> **Ship date:** 2026-05-23
> **Streak**: **"27+1*"** target (27 PASS v65-v83 + v85 + v87-v93 + 1 OVERRIDE v84 = 8-consecutive-clean-PASS post-v84 OVERRIDE = NEW CORPUS-RECORD streak EXTENDS by 1 wiki)
> **Special-status flag**: **RETROSPECTIVE SUBJECT — first-time analysis of long-cited corpus reference; Anthropic-direct-org #2 (v92 anchor + v93 = N=2 STRENGTHENING for NEW (a)-7 sub-axis "Foundational-Vendor-Direct-Source")**

## CRITICAL CORPUS observations

**v93 is the SECOND Anthropic-direct-org subject in v60+ window** (v92 anchor). This provides:

1. **NEW (a)-7 sub-axis N=2 STRENGTHENING** — validates the v92 PROVISIONAL N=1 registration; v95 audit N=3 watch sets clear promotion-ladder progression; v2.4 codification now has concrete evidence-base to formalize the sub-axis
2. **Retrospective-Promotion-from-Cited-to-Subject** — `anthropics/skills` was referenced at v71 + Pattern #84 84c references + v76 agent-skills-standard implementation of agentskills.io standard; v93 promotes from cited-only to subject-analyzed (corpus-novel sub-class)
3. **Pattern #84 84c.1 sub-sub-mechanism N=4 POST-PROMOTION STRENGTHENING** — extends v92's N=3 PROMOTION-LOCKED-IN to N=4 (with v93's 2-plugin sub-distribution: `document-skills` + `example-skills`)
4. **Pattern #52 Multi-Month-Sustained EXTREME-VIRAL sub-class N=3 strengthening** — 571 stars/day × ~244 days at fetch meets the >300/d × 90+d threshold; v78 N=1 + v85 N=2 + v93 N=3 post-promotion

## Phase 0 fetch snapshot

| Metric | Value |
|---|---|
| Created | 2025-09-22 (~244 days at fetch = ~8 months) |
| Last push | 2026-05-19 |
| Stars | 139,442 |
| Forks | 16,451 |
| Watchers (subscribers) | 899 |
| Open issues | 871 |
| Open PRs | 625 |
| Network | 16,451 |
| Commits on main | 36 |
| Repo size | 3,734 KB |
| License (declared) | "None specified" at GitHub API; README mixed: Apache-2.0 for many skills + source-available for docx/pdf/pptx/xlsx document-skills |
| Primary languages | Python 84.4% + HTML 12.4% + Shell 1.9% + JavaScript 1.3% |
| Velocity | ~571 stars/day at 244-day pulse-window = **Pattern #52 Multi-Month-Sustained EXTREME-VIRAL sub-class N+1 strengthening** (>300/d × 90+d threshold satisfied) |
| Topics | `agent-skills` |
| External service | `skills.sh/anthropics/skills` badge |
| Discussions | ENABLED (corpus-novel for vendor-direct-org subjects) |

## Owner / org

- **Org**: `anthropics` = Anthropic PBC (foundational-vendor-direct-source)
- **(a)-7 status**: N=2 (v92 claude-for-legal anchor + v93 anthropics/skills = N=2 STRENGTHENING)
- **Cross-corpus context**: This repo is the AUTHORITATIVE SKILL FORMAT REFERENCE for the corpus — SKILL.md spec defined here at `./spec/`; template at `./template/`; v76 agent-skills-standard (HoangNguyen0403) implements the same agentskills.io standard; Pattern #84 84c references this repo at multiple wikis

## Classification snapshot

- **Tier**: T1 Assistant Skill (Anthropic's reference implementation of Claude Skills with spec definition + template + 100+ example skills across 4 categories)
- **Sub-archetype**: closest fit = the v64 claude-seo / v92 claude-for-legal T1 sub-archetype "Domain-Vertical-Skill-Collection" but at a **different layer** — v93 is multi-domain (not single-vertical or multi-vertical-within-domain); v93 is **vendor-reference-implementation across all-domains** (Creative & Design + Development & Technical + Enterprise & Communication + Document Skills). v93 = "Vendor-Reference Multi-Domain Skill Collection" potential NEW sub-archetype distinct from "Domain-Vertical-Skill-Collection"
- **Licensing**: **CORPUS-NOVEL mixed-licensing within single repo** — many skills Apache-2.0 (open source) + docx/pdf/pptx/xlsx source-available (not open source); GitHub API reports "None specified" (because the mixed-licensing doesn't fit a single LICENSE file)
- **Locale**: English-primary (Anthropic's product-default; no multi-locale i18n)

## Architecture details

### Repository structure

```
anthropics/skills/
├── .claude-plugin/
├── skills/              ← 100+ example skills across 4 categories
│   ├── docx/            ← Document creation skill (SOURCE-AVAILABLE)
│   ├── pdf/             ← PDF manipulation skill (SOURCE-AVAILABLE)
│   ├── pptx/            ← PowerPoint skill (SOURCE-AVAILABLE)
│   ├── xlsx/            ← Excel skill (SOURCE-AVAILABLE)
│   ├── [Creative & Design skills]
│   ├── [Development & Technical skills]
│   └── [Enterprise & Communication skills]
├── spec/                ← Agent Skills SPECIFICATION (vendor-authoritative)
├── template/            ← Skill TEMPLATE (template-skill)
├── .gitignore
├── README.md
└── THIRD_PARTY_NOTICES.md   ← CORPUS-NOVEL artifact at top-level
```

### 4 Skill Categories

1. **Creative & Design** — art, music, design skills
2. **Development & Technical** — testing web apps, MCP server generation
3. **Enterprise & Communication** — communications, branding
4. **Document Skills** — docx + pdf + pptx + xlsx (source-available; "power Claude's document capabilities under the hood")

### Distribution channels

- **Claude Code Plugin Marketplace**: `/plugin marketplace add anthropics/skills` → registers as `anthropic-agent-skills` marketplace
- **2-plugin sub-distribution**: `document-skills` and `example-skills`
- **Direct install commands**: `/plugin install document-skills@anthropic-agent-skills` + `/plugin install example-skills@anthropic-agent-skills`
- **Claude.ai**: Example skills available to paid plans automatically
- **Claude API**: Pre-built skills + custom skills upload via Skills API Quickstart

**Pattern #84 84c.1 N+1 evidence-base extends**: v85 N=1 + v90 N=2 + v92 N=3 PROMOTION-LOCKED-IN + **v93 N=4 POST-PROMOTION STRENGTHENING** with 2-plugin sub-marketplace variant.

### SKILL.md format specification

Minimum required frontmatter:
```yaml
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---
```

Two required fields:
- `name` — Unique identifier (lowercase, hyphens for spaces)
- `description` — Complete description of skill purpose + usage triggers

This is the **vendor-authoritative skill format definition** that prior corpus subjects (v76 agent-skills-standard + Pattern #84 84c references at multiple wikis) align with.

### THIRD_PARTY_NOTICES.md at top-level

Corpus-novel artifact at repo root — explicit third-party-notices file at top-level. Distinct from in-skill-folder NOTICE.md (v75 impeccable pattern). Provides repo-level attribution discipline.

**Library-vocab "Top-Level THIRD_PARTY_NOTICES.md File at Repo Root" PROVISIONAL N=1**.

### Mixed-Licensing within Single Repo

| Skill set | License |
|---|---|
| Many skills in `skills/` | Apache-2.0 (open source) |
| `skills/docx`, `skills/pdf`, `skills/pptx`, `skills/xlsx` | Source-available (NOT open source) |

GitHub API reports "None specified" because mixed-licensing doesn't fit a single root LICENSE file.

**CORPUS-NOVEL mixed-licensing within single repo at foundational-vendor-direct-source subject**.

**Library-vocab "Mixed Licensing (Apache-2.0 + Source-Available) within Single Repo" PROVISIONAL N=1**.

### Reference to agentskills.io Standard

README notes: *"This repository contains Anthropic's implementation of skills for Claude. For information about the Agent Skills standard, see [agentskills.io](http://agentskills.io)."*

Implications:
- agentskills.io = external Agent Skills standard
- anthropics/skills = Anthropic's authoritative reference implementation of this standard
- v76 agent-skills-standard (HoangNguyen0403) implements the same standard at third-party scope
- **Corpus loop closure**: v76 derived FROM the standard that v93 implements at source-authoritative scope

**Library-vocab "Standard-Authoritative-Reference-Implementation via External Standard Site (agentskills.io)" PROVISIONAL N=1**.

### External Service Badge (skills.sh)

README displays `skills.sh/anthropics/skills` badge — external service tracking skills metadata. Corpus-novel external-skills-tracking-service reference.

**Library-vocab "External Skills-Metadata Tracking Service (skills.sh)" PROVISIONAL N=1**.

### Notion Partner Skill (ecosystem precedent)

README highlights *"Notion Skills for Claude"* as awesome example skill from partner. Establishes precedent for **partner-skill ecosystem highlighting at vendor-authoritative repo**.

### Educational/Demonstration disclaimer

> *"These skills are provided for demonstration and educational purposes only. While some of these capabilities may be available in Claude, the implementations and behaviors you receive from Claude may differ from what is shown in these skills. These skills are meant to illustrate patterns and possibilities. Always test skills thoroughly in your own environment before relying on them for critical tasks."*

Pattern #83 Honest-Deficiency-Disclosure within-pattern strengthening at vendor-source-authoritative scale (distinct from v92's 3-tier-liability-attorney-review framing but in same disclosure-discipline family).

## Phase 0.9 STRICT verdict (applying routine v2.3 §9 + §10 + NEW (a)-7)

### (a) — STRONGEST via NEW (a)-7 N=2 STRENGTHENING

| Sub-axis | v93 fit | Verdict |
|---|---|---|
| (a)-1 direct-author-peer | N/A — Anthropic = vendor not peer | N/A |
| (a)-2 native-VN-fluency | English-only | N/A |
| (a)-3 product-locale-inclusion | English-only | N/A |
| (a)-4 community-org | Anthropic foundational vendor not community-org | NO |
| (a)-5 multi-org-founder | Single-org subject | N/A |
| (a)-6 cluster-extension | N/A | NEUTRAL |
| **(a)-7 NEW Foundational-Vendor-Direct-Source** | **STRONGEST PASS at N=2 STRENGTHENING (v92 anchor + v93 = 2nd Anthropic-direct-org subject in v60+ window)** | **STRONGEST** |

**(a) verdict**: **STRONGEST PASS via NEW (a)-7 N=2 STRENGTHENING**.

### (b) — STRONGEST via LOW cost × STRONG functional-fit

- **Cost-of-trial**: LOW (`/plugin marketplace add anthropics/skills` + `/plugin install document-skills@anthropic-agent-skills` ≤5-min reversible)
- **Functional-fit (direct)**: STRONG — `document-skills` (docx/pdf/pptx/xlsx) directly applicable to vault publishing flow (vault wiki markdown → docx/pdf via document-skills installed); `example-skills` provides reference-patterns directly adaptable to vault wikis as skill-format templates
- **Functional-fit (methodology)**: STRONGEST — SKILL.md spec at `./spec/` is vendor-authoritative reference for any vault-skill formalization work + template-skill at `./template/` directly usable as starting point for vault custom skills + agentskills.io standard reference closes the v76 agent-skills-standard methodology chain at source

**(b) verdict**: **STRONGEST PASS** (LOW cost × STRONG direct-fit + STRONGEST methodology-fit). This is **STRONGER than v92 (b) STRONG** because v93 has direct-utility (document-skills + example-skills installable for vault content creation) where v92 was indirect (legal-vertical).

### (c) — STRONGEST via foundational-vendor + spec-authority + corpus-loop-closure

- Foundational-vendor-direct-source methodology-influence-node status (extending v92 anchor)
- **SKILL.md spec definition at `./spec/`** = vendor-authoritative skill format reference
- **Template-skill at `./template/`** = reference-template for skill creation
- Mixed-licensing within single repo (Apache-2.0 + source-available) — corpus-novel
- 4-category multi-domain skill collection (Creative & Design + Development & Technical + Enterprise & Communication + Document Skills)
- agentskills.io standard reference + Anthropic's authoritative-reference-implementation positioning
- THIRD_PARTY_NOTICES.md top-level artifact (corpus-novel)
- skills.sh external metadata-tracking service reference
- Notion partner-skill ecosystem precedent
- Pattern #83 Honest-Deficiency-Disclosure educational-disclaimer
- **Corpus loop closure**: v76 agent-skills-standard implemented the standard that v93 IS the authoritative reference for

**(c) verdict**: **STRONGEST PASS** — multi-corpus-novel observations + spec-authority + foundational-vendor source-authoritative status + corpus loop closure with v76.

### (d) — STRONGEST via multi-pattern N+1 strengthening + retrospective-closure

- **Pattern #84 84c.1 sub-sub-mechanism N=4 POST-PROMOTION STRENGTHENING** (v85 N=1 + v90 N=2 + v92 N=3 PROMOTION-LOCKED-IN + **v93 N=4 with 2-plugin sub-marketplace variant**)
- **Pattern #52 Multi-Month-Sustained EXTREME-VIRAL sub-class N=3 strengthening** (v78 N=1 + v85 N=2 + v93 N=3 post-promotion; the sub-class was CONFIRMED-administratively at v86 audit with v78+v85 N=2 evidence; v93 extends to N=3)
- **NEW (a)-7 sub-axis N=2 STRENGTHENING** (v92 anchor + v93 = N=2)
- **v76 agent-skills-standard retrospective-context closure** — Hoang's standards-layer derived from / aligned with agentskills.io standard that v93 IS authoritative reference for; reverses the methodology-direction (v76 → standard ← v93)
- **Pattern #66 supply-chain** mixed-licensing observation strengthening (Apache-2.0 + source-available within single repo)
- **Pattern #83** within-pattern strengthening via educational-demonstration disclaimer
- **NEW Library-vocab "Retrospective-Promotion-from-Cited-to-Subject"** PROVISIONAL N=1 (corpus-novel — `anthropics/skills` was cited at v71 + Pattern #84 84c references + v76 implementation but never subject-analyzed)
- 8-month-old subject with sustained ~571/d velocity (long-window observation distinct from pulse-window subjects)

**(d) verdict**: **STRONGEST PASS** — multi-pattern N+1 strengthening across at least 5 patterns + retrospective-closure + first all-N≥3 multi-pattern at single subject in v60+ window.

### Overall verdict

**STRONGEST INCLUDE 4/4 with ALL FOUR axes STRONGEST**.

**This is the FIRST all-4-STRONGEST verdict since v76** (10+ wiki gap; v76 was last all-4-STRONGEST at agent-skills-standard 2026-05-19). v93 may be the STRONGEST INCLUDE in v60+ corpus.

**Streak**: **"27+1*"** NEW CORPUS-RECORD — 8-consecutive-clean-PASS post-v84 OVERRIDE. 29-instance window v65-v93 = 28 PASS + 1 OVERRIDE = **96.6% INCLUDE rate** (uptick from v92's 96.4%).

## Override-frequency check

1-in-29 = well below 2-in-20 / 3-in-30 v2.3-trigger. Discipline holds.

## Phase 4b PRIMARY decision

**PRIMARY**: NEW (a)-7 sub-axis **"Foundational-Vendor-Direct-Source" N=2 STRENGTHENING** registration via v2.3 §3 Phase 4b vehicle #7 (Library-vocab observational-layer registration / strengthening).

**Justification**: The v92 PROVISIONAL N=1 (a)-7 registration was the structural-novelty observation. v93 provides the **validation evidence** that the sub-axis is real and recurring (not a v92 one-off edge-case). N=2 STRENGTHENING at v93 sets clear promotion-ladder progression and provides the concrete evidence-base for **v2.4 codification of (a)-7 sub-axis formal definition**.

**Why (a)-7 strengthening, not Pattern #84 84c.1 N=4 strengthening, as PRIMARY**:
- Pattern #84 84c.1 was already PROMOTION-LOCKED-IN at v92 PRIMARY; v93 N=4 is post-promotion strengthening (administrative not novelty)
- NEW (a)-7 sub-axis is methodologically-novel and unresolved (v2.4 codification candidate)
- v93's primary corpus-contribution is **resolving the methodological gap** flagged at v92
- Pattern #52 N=3 sub-class also post-promotion (CONFIRMED at v86); v93 strengthens existing CONFIRMED state

**Proposal-document**: `01 Analysis/(C) (a)-7-Foundational-Vendor-Direct-Source-N2-STRENGTHENING.md`

## SECONDARY pattern observations

1. **Pattern #84 84c.1 sub-sub-mechanism N=4 POST-PROMOTION STRENGTHENING** (v85+v90+v92+v93; supports v95 audit STRONGER PROMOTION-CONFIRMED)
2. **Pattern #52 Multi-Month-Sustained EXTREME-VIRAL sub-class N=3 strengthening** (v78+v85+v93; sub-class CONFIRMED at v86 audit)
3. **v76 agent-skills-standard retrospective-context closure** — v76 implements agentskills.io standard; v93 IS the standard's authoritative reference implementation
4. **NEW Library-vocab "Retrospective-Promotion-from-Cited-to-Subject" PROVISIONAL N=1** (`anthropics/skills` cited at multiple prior wikis without subject-analysis; v93 promotes from cited-only to subject-analyzed)
5. **NEW Library-vocab "Mixed Licensing (Apache-2.0 + Source-Available) within Single Repo" PROVISIONAL N=1** (corpus-novel within foundational-vendor-direct-source subject)
6. **NEW Library-vocab "Standard-Authoritative-Reference-Implementation via External Standard Site (agentskills.io)" PROVISIONAL N=1**
7. **NEW Library-vocab "SKILL.md Spec + Template at Vendor-Authoritative Repo" PROVISIONAL N=1** (`./spec/` + `./template/` at vendor-authoritative subject)
8. **NEW Library-vocab "Top-Level THIRD_PARTY_NOTICES.md File at Repo Root" PROVISIONAL N=1**
9. **NEW Library-vocab "External Skills-Metadata Tracking Service (skills.sh)" PROVISIONAL N=1**
10. **Pattern #66 supply-chain mixed-licensing observation strengthening** within single repo (corpus-novel)
11. **Pattern #83** within-pattern strengthening via educational-demonstration disclaimer
12. **Pattern #57 sub-variant 57c-product** intra-vendor ecosystem citation density strengthening (Claude Code + Claude.ai + Claude API + 4 Anthropic-product references — same N+1 axis as v92)

## Pilot ranking impact

v93 is **DIRECT-UTILITY pilot candidate at HIGH-RELEVANCE** because:
- `document-skills` install directly enables vault markdown → docx/pdf/pptx/xlsx publishing
- `example-skills` provides reference-templates for vault custom skill creation
- LOW cost-of-trial (`/plugin marketplace add anthropics/skills` ≤5-min reversible)
- Apache-2.0 for most example-skills (license-permissive)
- Source-available docx/pdf/pptx/xlsx (reference-utility even if not strict open-source)

**Pilot ranking impact**: v93 inserts at **Tier-1 position #2** — DIRECT vault-utility at multi-format-publishing layer (above html-anything v91's web-output focus; below cc-switch only because cc-switch is single-binary install).

Pre-v93 ranking:
1. cc-switch (v73)
2. claude-comstyle (v87)
3. html-anything (v91)
4. teleport (v88)
5. VibeCodingTracker (v89)
6. academic-research-skills (v90 CONDITIONAL)
7. agent-skills-standard (v76)

Post-v93 ranking:
1. cc-switch (v73)
2. **anthropics/skills v93 NEW** — DIRECT vault-utility at multi-format-publishing layer + vendor-authoritative reference-implementation
3. claude-comstyle (v87) DISPLACED from #2 → #3
4. html-anything (v91) DISPLACED from #3 → #4
5. teleport (v88) DISPLACED from #4 → #5
6. VibeCodingTracker (v89) DISPLACED from #5 → #6
7. academic-research-skills (v90 CONDITIONAL) DISPLACED from #6 → #7
8. agent-skills-standard (v76) DISPLACED from #7 → #8

**Methodology-influence Tier-1-special** ALSO applies (multi-track classification per v92 NEW methodology-influence-track):
1. claude-for-legal (v92)
2. **anthropics/skills (v93) NEW** — SKILL.md spec authoritative + template-skill reference

## v95 audit batch additions from v93

- **NEW (a)-7 sub-axis N=2 STRENGTHENING** evidence + v2.4 codification formalization-trigger (PRIMARY)
- **Pattern #84 84c.1 N=4 post-promotion strengthening** verification (v95 STRONGER PROMOTION-CONFIRMED)
- **Pattern #52 N=3 sub-class strengthening** verification (sub-class CONFIRMED at v86; v93 = N=3 post-promotion)
- **v76 agent-skills-standard retrospective-context closure** documentation
- **NEW Library-vocab "Retrospective-Promotion-from-Cited-to-Subject" PROVISIONAL N=1** first-cycle stale-check
- **5 OTHER NEW Library-vocab PROVISIONAL N=1** first-cycle stale-checks (Mixed-Licensing + Standard-Authoritative-Reference + SKILL.md Spec at Vendor + THIRD_PARTY_NOTICES.md + skills.sh External Service)
- Pattern #66 supply-chain mixed-licensing observation cycle
- Pattern #83 within-pattern + Pattern #57 sub-variant 57c verification

Combined with v90 ~8-10 + v91 ~12-13 + v92 ~10 + v93 ~10 = **v95 projected batch ~30-35 items** (above post-codification baseline 8-10 but well below v90 audit 43-item CORPUS-RECORD; healthy trending toward upper-end).

## Routine v2.4 codification debt

v93 contributes 1 critical v2.4-codification-trigger:
- **NEW (a)-7 sub-axis N=2 STRENGTHENING validation evidence** — converts (a)-7 from PROVISIONAL-needs-validation to NEAR-PROMOTION-ELIGIBLE; v2.4 codification can now formalize (a)-7 with anchor + N=2 strengthening evidence

Plus 5 NEW Library-vocab candidates + retrospective-subject-promotion observational sub-class.

Combined with v90 ~3-4 + v91 ~3-4 + v92 ~4-5 = **~13-16 v2.4 candidates accumulated**. Still below ~50-trigger but the **(a)-7 validation event** may justify an early mini-codification on the (a) taxonomy specifically.

**Recommendation**: At v95 audit, evaluate whether to execute v2.4 mini-codification focused on (a) taxonomy formalization (formalize (a)-7 + (a)-6 internal strength-gradient + (a) general strength-gradient and sub-axis-applicability rules).

## Routine v2.3 production-baseline validation at v93

**FOURTH wiki under v2.3** (v90 = first, v91 = second, v92 = third). v2.3 sections applied at v93:

| v2.3 § | Amendment | Application at v93 | Validation result |
|---|---|---|---|
| §1-§2 | Library-vocab observational-layer promotion ladder | (a)-7 N=2 STRENGTHENING per §1-§2 promotion ladder | ✅ CLEAN |
| §3 | Phase 4b 9-vehicle catalog | Vehicle #7 Library-vocab observational-layer strengthening selected for PRIMARY | ✅ CLEAN |
| §4 | 3-layer Pattern hierarchy with sub-sub-mechanism layer | Pattern #84 84c.1 N=4 post-promotion strengthening | ✅ CLEAN |
| §7 | Override-frequency thresholds | 1-in-29 well below trigger | ✅ CLEAN |
| §9 | 6-axis Phase 0.9 (a) taxonomy + NEW (a)-7 PROVISIONAL | **(a)-7 N=2 STRENGTHENING evidence** — v92 flagged-gap now validated as recurring-pattern (not edge-case); supports v2.4 codification | ✅ **VALIDATED** |
| §10 | Cost-of-trial sub-axis | LOW × STRONG direct-fit + STRONGEST methodology-fit = STRONGEST (b) verdict | ✅ CLEAN |
| §14 | Pattern #52 5-variant sub-class taxonomy | Multi-Month-Sustained EXTREME-VIRAL N=3 post-promotion strengthening (~571/d × 244d) | ✅ CLEAN |
| §20 | Density-not-scale-correlated finding | 139K★ mega-scale + active engagement (871 issues + 625 PRs + 899 watchers) continues scale-correlation hypothesis accumulation | ✅ CLEAN |
| §21 | Cultural-cluster CORPUS-RECORD protocol | N/A — Anthropic-direct-org foundational-vendor structurally orthogonal | ✅ CLEAN |

**v2.3 baseline-validation verdict at v93**: **CLEAN fourth-execution WITH §9-GAP-VALIDATION-EVIDENCE** — the v92-flagged methodological gap is now validated as recurring-pattern (not edge-case) by v93 N=2 evidence. Routine v2.3 framework continues to be RESILIENT. **v2.4 codification of (a)-7 sub-axis formal definition is now evidence-ready**.

## Special-status flag: RETROSPECTIVE SUBJECT

v93 = first-time analysis of a long-cited corpus reference. `anthropics/skills` was previously referenced at:
- v71 agents-best-practices (referenced as ecosystem context)
- Pattern #84 84c references at multiple wikis (as anchor-pattern reference)
- v76 agent-skills-standard (implementation alignment via agentskills.io standard)
- Pattern #84 84c.1 sub-sub-mechanism at v85 + v90 + v92 (as `/plugin marketplace add` mechanism reference)

**Retrospective-Promotion-from-Cited-to-Subject** = corpus-novel observational sub-class. Library-vocab PROVISIONAL N=1.

Similar precedent: v78 ECC corpus-recursive revisit (re-analysis of v1 subject) — but v78 was RE-analysis of already-subject-analyzed v1 wiki; v93 is FIRST-TIME analysis of cited-only reference. Different sub-class.

## Time

Single-session execution.

## Next-action recommendation

Build cluster pages + entity pages + Phase 4b proposal-document + Phase 5 vault sync per routine.
