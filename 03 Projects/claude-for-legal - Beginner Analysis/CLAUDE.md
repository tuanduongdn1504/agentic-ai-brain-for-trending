# (C) claude-for-legal — Beginner Analysis project context

> **Routine:** `llm-wiki-routine-v2.3` (THIRD execution under v2.3 production-baseline; v90 = first, v91 = second, v92 = this build)
> **Subject:** [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal)
> **Subject tagline:** *"A suite of plugins for legal workflows — reference agents, skills, and data connectors for the legal workflows we see most: in-house commercial, privacy, product, corporate, employment, litigation, regulatory, AI governance, IP, and the learning side of the practice (law school clinics and students)."*
> **Ship date:** 2026-05-23
> **Streak**: **"26+1*"** target (26 PASS v65-v83 + v85 + v87-v92 + 1 OVERRIDE v84 = 7-consecutive-clean-PASS post-v84 OVERRIDE = NEW CORPUS-RECORD streak EXTENDS by 1 wiki)

## CRITICAL CORPUS-FIRST observation

**This is the FIRST Anthropic-direct-org subject as PRIMARY analysis in v60+ window.** Prior corpus has cited Anthropic-authored skills (v75 impeccable extended `anthropics/frontend-design`, Pattern #84 84c referenced `anthropics/skills`, v82+v83 design-skill cluster reverse-engineered Anthropic Claude Design) — but NEVER analyzed an Anthropic-owned repo as the SUBJECT of a wiki. v92 closes that gap. This carries **methodological-source-authoritative status** distinct from third-party derivative subjects.

## Phase 0 fetch snapshot

| Metric | Value |
|---|---|
| Created | 2026-04-21 (32 days old at fetch) |
| Last push | 2026-05-22 |
| Stars | 7,491 |
| Forks | 1,200 |
| Watchers (subscribers) | 82 |
| Open issues | 46 |
| Open PRs | 34 |
| Network | 1,200 |
| Commits | 29 on main |
| Repo size | 404 KB |
| License | Apache-2.0 © 2026 Anthropic PBC |
| Primary languages | Python 67.2% + Shell 32.8% |
| Velocity | ~234 stars/day at 32-day pulse-window = **HIGH-NOT-EXTREME Pattern #52 sub-class N+1 strengthening** |
| Homepage | (none specified) |
| Description | *"A suite of plugins for legal workflows"* |

## Owner / org

- **Org**: `anthropics` (Anthropic PBC = the company that makes Claude itself)
- **Org-status**: **FOUNDATIONAL-VENDOR-DIRECT-SOURCE** — the vendor whose substrate (Claude API + Claude Code + Claude Cowork + Managed Agents API + Microsoft 365 add-in) ALL prior corpus subjects depend on
- **Phase 0.9 (a) implications**: existing v2.3 §9 6-axis (a) taxonomy is designed for THIRD-PARTY cultural-peer discrimination — does NOT cleanly handle foundational-vendor case → **NEW (a)-7 sub-axis "Foundational-Vendor-Direct-Source" PROVISIONAL** registered at v92 as v2.4 codification candidate

## Classification snapshot

- **Tier**: T1 Assistant Skill (multi-vertical legal-domain plugin bundle)
- **Sub-archetype anchor**: closest fit = v64 claude-seo T1 "Domain-Vertical-Skill-Collection" but at MUCH higher density (12-plugin × 60+-agent × 20+-connector × 5-distribution); v92 = N=2 STRENGTHENING for v64's T1 sub-archetype (extends evidence-base from 1-instance to 2-instance)
- **Vertical**: Legal workflows (10 practice-domain verticals + law-school + builder-hub)
- **Licensing**: Apache-2.0 © Anthropic PBC (Pattern #45 within-pattern; foundational-vendor-licensing-direct-source)
- **Locale**: English-primary (no multi-locale i18n observed; US-jurisdiction-anchored via "in-house commercial, privacy..." description)

## Architecture details

### 12-Plugin Vertical Bundle

| # | Plugin | Practice domain |
|---|---|---|
| 1 | commercial-legal | In-house commercial contracts |
| 2 | corporate-legal | Corporate transactions + governance |
| 3 | employment-legal | Employment law + workplace |
| 4 | privacy-legal | Data protection + DSAR + DPA |
| 5 | product-legal | Product-launch legal review |
| 6 | regulatory-legal | Regulatory compliance + NPRM |
| 7 | ai-governance-legal | AI governance + responsible-AI |
| 8 | ip-legal | IP / trademark / copyright |
| 9 | litigation-legal | Litigation + discovery + docket |
| 10 | law-student | Bar prep + IRAC + Socratic |
| 11 | legal-clinic | Law school clinic operations |
| 12 | legal-builder-hub | Community skill marketplace |

### 60+ Named Agents Across 12 Plugins

Sample (full inventory in entity-1):
- commercial: NDA Triager + Amendment Tracer + Renewal Watcher (scheduled) + Deal Debrief
- corporate: Tabular Diligence Review + Board Consent Drafter + Closing Checklist Driver
- privacy: DSAR Responder + DPA Reviewer + PIA Generator + Privacy Triager
- litigation: Claim Chart Builder + Docket Watcher (scheduled) + Demand Letter Drafter + Deposition Prep
- law-student: Bar Prep Coach + Socratic Drill Sergeant + IRAC Grader + Case Briefer

### 5-Distribution-Channel Matrix (CORPUS-RECORD)

1. **Claude Cowork** plugin marketplace (60-second install per README)
2. **Claude Code** plugin marketplace via `/plugin marketplace add <path-to-this-repo>` + `/plugin install <plugin>@claude-for-legal`
3. **Claude Managed Agents API** via `/v1/agents` endpoint + `scripts/deploy-managed-agent.sh <cookbook>`
4. **Claude for Microsoft 365** (Word + Excel + PowerPoint + Outlook sidebar)
5. **Custom cloud deployment** (Vertex AI / Bedrock / internal gateway)

This is **CORPUS-RECORD 5-distribution-channel matrix at single subject** (exceeds v83 open-design 4-method + v90 3-channel records).

### 20+ MCP Enterprise-System Connectors

Slack + Google Drive + CoCounsel Legal (Thomson Reuters) + Box + Ironclad + DocuSign + iManage + Everlaw + CourtListener + Trellis + Aurora + Definely + Lawve AI + Courtroom5 + Descrybe + Solve Intelligence + TopCounsel + Linear + Atlassian Jira + Asana

**CORPUS-RECORD MCP enterprise-connector density** — 20+ at single subject is highest in v60+ window. Library-vocab "20+ MCP Enterprise-System Connector Density" PROVISIONAL N=1 candidate (or Pattern #18 sub-mechanism strengthening).

### 5 Managed-Agent-Cookbooks (scheduled execution)

| Cookbook | Purpose |
|---|---|
| reg-monitor | Regulatory feed monitoring |
| renewal-watcher | Contract renewal tracking |
| docket-watcher | Court docket monitoring |
| diligence-grid | M&A diligence tracking |
| launch-radar | Product launch monitoring |

Cron-style frontmatter on agent markdown files; deployed via `scripts/deploy-managed-agent.sh`.

### Cold-Start Interview Pattern

Per-plugin interactive setup (10-20 min) that reads seed documents and generates initial CLAUDE.md practice-profile. Quick-start alternative ~2 minutes. Re-runnable for incremental updates.

**Library-vocab "Cold-Start Interview Pattern with Practice-Profile Generation" PROVISIONAL N=1**.

### Community Skill Trust Layer (5-gate)

1. **Security review**: hidden-content scan + injection detection + structural trust check
2. **Allowlist**: restrictive-by-default source gate
3. **License gate**: deployment-context-aware (personal / firm-internal / product-embedding)
4. **Freshness gate**: tracks reference-content verification window
5. **Install log**: auditable record of installations

**Pattern #66 supply-chain-awareness STRONGEST single-subject N+1 strengthening at v60+ density**.

**Library-vocab "Community Skill Trust Layer with 5-Gate Framework" PROVISIONAL N=1**.

### Practice-Profile Persistence Layer

Path: `~/.claude/plugins/config/claude-for-legal/<plugin>/CLAUDE.md`

Survives plugin updates. Re-runnable cold-start interview for incremental updates. Connector swap via `.mcp.json`. Skill forking via markdown editing.

**Library-vocab "Practice-Profile Persistence at Config Layer Surviving Plugin Updates" PROVISIONAL N=1**.

### 3-Tier Liability/Attorney-Review Guardrail Discipline

Tier 1 — Output framing:
> *"Every output from these plugins is a draft for attorney review — not legal advice, not a legal conclusion, not a substitute for a lawyer."*

Tier 2 — Organizational disclaimer:
> *"These plugins do not represent Anthropic's legal positions."*

Tier 3 — Citation verification:
> Citations from research connectors tagged with source; unverified citations flagged `[verify]`. Research-connector requirement: *"Everything else is better with one, and citations are unverified without one."*

**Library-vocab "3-Tier Liability/Attorney-Review Guardrail Discipline" PROVISIONAL N=1** + Pattern #83 Honest-Deficiency-Disclosure within-pattern strengthening at vendor-source-authoritative scale.

### External-Plugin Partner-Vendor Directory Structure

`external_plugins/cocounsel-legal/` = Thomson Reuters CoCounsel Legal Research integration as **explicit partner-vendor plugin directory** at top-level repo tree. Corpus-novel partner-vendor-integration-as-explicit-directory pattern.

**Library-vocab "External-Plugin Partner-Vendor Directory Structure (explicit `external_plugins/` directory)" PROVISIONAL N=1**.

### Legal Skill Design Framework

9 parameters + 3 failure modes for QA of community-contributed skills. Validation: `bash scripts/test-cookbooks.sh` dry-runs managed-agent cookbooks before push.

## Phase 0.9 STRICT verdict (applying routine v2.3 §9 + §10 + NEW (a)-7)

### (a) Cultural-peer / cluster-extension — METHODOLOGICAL EDGE-CASE

The v2.3 §9 6-axis (a) taxonomy was designed for THIRD-PARTY cultural-peer discrimination. Anthropic-direct-org subject doesn't fit any of (a)-1 through (a)-6 cleanly:

| Existing sub-axis | v92 fit |
|---|---|
| (a)-1 direct-author-peer | N/A — Anthropic = vendor not peer |
| (a)-2 native-VN-fluency | N/A |
| (a)-3 product-locale-inclusion | N/A — English-only |
| (a)-4 community-org | NO — Anthropic is foundational vendor not community-org |
| (a)-5 multi-org-founder | N/A |
| (a)-6 cluster-extension | NEUTRAL — doesn't extend Asian cluster or any existing cluster |

**NEW (a)-7 "Foundational-Vendor-Direct-Source" PROVISIONAL sub-axis registration at v92**:

**Definition**: The subject is owned by the foundational substrate-vendor (Anthropic in this case) whose product layer ALL prior corpus subjects depend on. Methodological-influence is source-authoritative not derivative.

**v92 fit at (a)-7**: **STRONGEST PASS** — Anthropic-direct-org = foundational vendor + corpus-first-direct-org-as-subject + reference-implementation-for-all-prior-derivative-subjects.

**v2.4 codification candidate**: Register (a)-7 sub-axis formally in routine v2.4 + define handling protocol for foundational-vendor-direct-source subjects (likely with special-status flag that (a) becomes informational-not-gating because methodology-influence at (c) is intrinsically supreme).

### (b) Cost-of-trial × functional-fit

- **Cost-of-trial**: **LOW** (`/plugin marketplace add <path>` + `/plugin install <plugin>@claude-for-legal` ≤5-min reversible per plugin; 60-sec install in Claude Cowork)
- **Functional-fit (direct)**: **INDIRECT** — Storm Bear vault is wiki-curation + Scrum-coaching, NOT legal-workflow; not a lawyer subject-matter use-case
- **Functional-fit (methodology)**: **STRONG** — Cold-start interview pattern + Practice-profile persistence + Community Skill Trust Layer 5-gate framework + Skill Design Framework 9-parameter QA are HIGHLY APPLICABLE to vault wiki-curation framework + routine v2.4 codification work

**(b) verdict**: **STRONG PASS** (LOW cost × INDIRECT-direct-fit + STRONG-methodology-fit). Functional-fit weaker than v91 DIRECT but stronger than v90's pure-INDIRECT because methodology layer transfers cleanly.

### (c) Methodology / corpus-contribution

- 12-vertical legal-plugin × 60+-agent × 20+-connector × 5-distribution architecture
- 5 managed-agent cookbooks with scheduled-execution (cron-style frontmatter)
- Cold-start interview pattern (corpus-novel)
- Practice-profile persistence at config layer (corpus-novel)
- Community Skill Trust Layer 5-gate framework (corpus-novel; Pattern #66 STRONGEST single-subject density)
- Legal Skill Design Framework 9-parameter + 3-failure-mode QA (corpus-novel)
- 3-tier liability/attorney-review guardrail discipline (corpus-novel)
- External-plugin partner-vendor directory structure (corpus-novel)
- CORPUS-RECORD 5-distribution-channel matrix (exceeds v83 4-method)
- CORPUS-RECORD 20+ MCP enterprise-connector density at single subject
- **FOUNDATIONAL-VENDOR-DIRECT-SOURCE methodology-influence-node status** — distinct from all prior derivative subjects

**(c) verdict**: **STRONGEST PASS** — multi-corpus-first observations + foundational-vendor source-authoritative-status. Highest single-wiki methodology-influence density in v60+ window post-v78 ECC.

### (d) Corpus-overlap / cross-wiki density

- **Pattern #84 84c.1 sub-sub-mechanism "Marketplace-Plugin-Install" N=3 PROMOTION-LOCKED-IN** (v85 N=1 + v90 N=2 + **v92 N=3** = N=3 promotion-threshold per v2.3 §1-§2; CONFIRMED-eligible at v95 audit administrative)
- **v64 claude-seo T1 sub-archetype "Domain-Vertical-Skill-Collection" N=2 STRENGTHENING** (v64 anchor + v92 N=2; v95 N=3 watch via future-subject)
- **Pattern #18 sub-archetype B "one-binary-many-CLIENTS" within-pattern strengthening** (Claude API + 5 distribution channels)
- **Pattern #66 supply-chain awareness STRONGEST single-subject density at v60+ window** (Community Skill Trust Layer 5-gate framework)
- **Pattern #83 Honest-Deficiency-Disclosure** strengthening via 3-tier liability framing
- **Pattern #78 Living-Domain-Standards Tracking** within-pattern strengthening at legal-jurisdiction-tracking (regulatory feed monitoring + freshness gate)
- **Pattern #57 sub-variant 57c-product corpus-citation density** strengthening at Anthropic-product-ecosystem citation layer (Claude Cowork + Claude Code + Managed Agents API + Microsoft 365 = 4 Anthropic-product references at single subject)
- MCP standard + 20+ enterprise-connector references

**(d) verdict**: **STRONG PASS** — Pattern #84 84c.1 N=3 PROMOTION-LOCKED-IN is the major (d) contribution; multi-pattern strengthening across at least 7 patterns. Not STRONGEST because no direct corpus-recursive citation chain.

### Overall verdict

**STRONGEST INCLUDE 4/4** with **(a)(c) STRONGEST + (b)(d) STRONG**.

Stronger verdict than v91 (which was STRONGEST 4/4 with (a)(b)(d) STRONGEST). v92 = 2-of-4-STRONGEST verdict balanced at different axes; methodologically novel (a)-7 sub-axis introduction.

**Streak**: **"26+1*"** NEW CORPUS-RECORD — 7-consecutive-clean-PASS post-v84 OVERRIDE. 28-instance window v65-v92 = 27 PASS + 1 OVERRIDE = **96.4% INCLUDE rate** (uptick from v91's 96.3%).

## Override-frequency check

1-in-28 = well below 2-in-20 / 3-in-30 v2.3-trigger. Discipline holds.

## Phase 4b PRIMARY decision

**PRIMARY**: **Pattern #84 84c.1 sub-sub-mechanism "Marketplace-Plugin-Install" N=3 PROMOTION-LOCKED-IN** via v2.3 §3 Phase 4b vehicle #1 (Pattern-promotion / sub-mechanism-formalization at N=3 threshold).

**Justification**: Pattern #84 84c.1 was registered as sub-sub-mechanism at v85 (N=1 anchor), strengthened at v90 (N=2 PROMOTION-ELIGIBLE), and now at v92 reaches **N=3 PROMOTION-LOCKED-IN threshold** per v2.3 §1-§2 promotion ladder (criterion 4 variant-within-sub-mechanism + criterion 1 corpus-first PASS). Administrative-promotion at v95 audit recommended.

**Proposal-document**: `01 Analysis/(C) Pattern-84-84c-1-Marketplace-Plugin-Install-N3-PROMOTION-LOCKED-IN.md`

## SECONDARY pattern observations

1. **NEW Phase 0.9 (a)-7 sub-axis "Foundational-Vendor-Direct-Source" PROVISIONAL N=1** — methodological framework extension; v2.4 codification candidate
2. **v64 claude-seo T1 sub-archetype "Domain-Vertical-Skill-Collection" N=2 STRENGTHENING** (v64 + v92; v95 N=3 watch)
3. **Pattern #66 supply-chain awareness STRONGEST single-subject density** via Community Skill Trust Layer 5-gate
4. **Pattern #83 within-pattern strengthening** via 3-tier liability framing
5. **Pattern #18 within-pattern strengthening** + Pattern #78 + Pattern #57 sub-variant 57c (Anthropic-product-ecosystem citation density)
6. **6 NEW Library-vocab PROVISIONAL N=1**:
   - Cold-Start Interview Pattern with Practice-Profile Generation
   - Practice-Profile Persistence at Config Layer Surviving Plugin Updates
   - Community Skill Trust Layer with 5-Gate Framework
   - 3-Tier Liability/Attorney-Review Guardrail Discipline
   - External-Plugin Partner-Vendor Directory Structure
   - 5-Distribution-Channel Matrix at Single Subject (CORPUS-RECORD)
7. **Library-vocab "20+ MCP Enterprise-System Connector Density at Single Subject" PROVISIONAL N=1** OR Pattern #18 sub-mechanism strengthening at MCP-connector-aggregation axis
8. **Pattern #52 HIGH-NOT-EXTREME sub-class N strengthening** at pulse-window (~234/d × 32d)

## Pilot ranking impact

Pre-v92 ranking (top 6 Tier-1):

1. cc-switch (v73)
2. claude-comstyle (v87)
3. html-anything (v91) — DIRECT vault-utility at multi-surface-output
4. teleport (v88)
5. VibeCodingTracker (v89)
6. academic-research-skills (v90 CONDITIONAL)

Post-v92 ranking — claude-for-legal is **NOT a vault pilot candidate** for direct-utility (Storm Bear not a lawyer; legal-vertical doesn't apply). But methodology-influence value is STRONGEST in v60+ corpus for routine v2.4 evolution.

**Methodology-influence pilot recommendation** (separate from direct-utility ranking): claude-for-legal patterns to ADAPT for vault routine v2.4:
1. **Cold-start interview pattern** — could become "Wiki-Build cold-start interview" for routine v2.4 (interactive seed-document → CLAUDE.md generation)
2. **Practice-profile persistence at config layer** — could become "Routine-config persistence" pattern
3. **Community Skill Trust Layer 5-gate** — could inform vault external-plugin / community-Pattern-contribution discipline
4. **3-tier liability/attorney-review guardrail** — could inform vault "honest-disclosure" discipline at audit + ship boundary

**No change to direct-utility pilot ranking**; methodology-influence is supplementary.

## v95 audit batch additions from v92

- **Pattern #84 84c.1 N=3 PROMOTION administrative-formalization** (PRIMARY at v92; CONFIRMED-administrative at v95)
- **NEW (a)-7 sub-axis "Foundational-Vendor-Direct-Source" PROVISIONAL N=1** first-cycle stale-check + v2.4 codification candidate
- **v64 T1 sub-archetype "Domain-Vertical-Skill-Collection" N=2 STRENGTHENING** (v64 + v92; v95 N=3 watch)
- 6 NEW Library-vocab PROVISIONAL N=1 first-cycle stale-checks
- Pattern #66 supply-chain CORPUS-RECORD single-subject density verification
- Pattern #83 + Pattern #18 + Pattern #57 + Pattern #78 within-pattern strengthening verification
- **First Anthropic-direct-org-as-subject methodological-edge-case audit-class consideration** (NEW audit class candidate?)
- Combined with v90 ~8-10 + v91 ~12-13 = **v95 projected batch ~25-30 items** (above post-codification baseline but well below v90 audit 43-item CORPUS-RECORD; healthy)

## Routine v2.4 codification debt

v92 contributes ~4-5 NEW v2.4 candidates:
1. NEW (a)-7 sub-axis "Foundational-Vendor-Direct-Source" formalization
2. Phase 0.9 evaluation protocol for foundational-vendor subjects (likely (a) informational-not-gating + (c) special-status)
3. 5-distribution-channel matrix as Phase 0 classification axis enrichment
4. Community Skill Trust Layer 5-gate as Pattern #66 sub-mechanism formalization candidate
5. Cold-start interview pattern as Phase 0 protocol enrichment for routine v2.4

Combined with v90's ~3-4 + v91's ~3-4 = **~10-13 v2.4 candidates accumulated**. Well below ~50-candidate v2.4-trigger but trending.

## Routine v2.3 production-baseline validation at v92

**THIRD wiki under v2.3** (v90 = first, v91 = second). v2.3 sections applied at v92:

| v2.3 § | Amendment | Application at v92 |
|---|---|---|
| §1-§2 | Library-vocab observational-layer promotion ladder | Pattern #84 84c.1 N=3 PROMOTION-LOCKED-IN per criterion 4 + 1 |
| §3 | Phase 4b 9-vehicle catalog | Vehicle #1 Pattern-promotion / sub-mechanism-formalization at N=3 selected for PRIMARY |
| §4 | 3-layer Pattern hierarchy with sub-sub-mechanism layer | Pattern #84 84c.1 sub-sub-mechanism N=3 = first sub-sub-mechanism layer promotion-event in v60+ window |
| §7 | Override-frequency thresholds | 1-in-28 well below trigger |
| §9 | 6-axis Phase 0.9 (a) taxonomy | **METHODOLOGICAL EDGE-CASE EXPOSED — NEW (a)-7 sub-axis required for Anthropic-direct-org foundational-vendor subjects; v2.4 codification candidate registered** |
| §10 | Cost-of-trial sub-axis | LOW cost × INDIRECT-direct-fit + STRONG-methodology-fit = STRONG (b) verdict |
| §14 | Pattern #52 5-variant sub-class taxonomy | HIGH-NOT-EXTREME pulse-class N+1 at ~234/d × 32d |
| §21 | Cultural-cluster CORPUS-RECORD protocol | N/A — Anthropic-direct-org not Asian cluster; structurally orthogonal |

**v2.3 baseline-validation verdict at v92**: **CLEAN third-execution WITH FLAGGED METHODOLOGICAL GAP** — routine v2.3 §9 6-axis (a) taxonomy does NOT cleanly handle Anthropic-direct-org foundational-vendor subjects. Handled gracefully via NEW (a)-7 sub-axis PROVISIONAL registration as v2.4 codification candidate. v2.3 framework is RESILIENT to novel-edge-case (didn't break; required minor extension that v2.4 should formalize).

This is the FIRST v2.3 §9-amendment-needed observation since codification 2026-05-22. Worth tracking: if v92-v94 reveals further (a)-axis gaps, accelerate v2.4 codification before v95 audit.

## Time

Single-session execution.

## Next-action recommendation

Build cluster pages + entity pages + Phase 4b proposal-document + Phase 5 vault sync per routine.
