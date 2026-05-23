# (C) Entity 1 — Core Product: 12-Plugin Legal Bundle + 60+ Agents + 5 Managed-Agent Cookbooks + 5-Distribution-Channel CORPUS-RECORD Matrix + 20+ MCP Enterprise-Connector CORPUS-RECORD Density + Cold-Start Interview + Practice-Profile Persistence + Community Skill Trust Layer 5-Gate + Legal Skill Design Framework + 3-Tier Liability Discipline + External-Plugin Partner-Vendor Directory

**Type**: Core-product entity
**Wiki version**: v92 (THIRD under routine v2.3 baseline)
**Sources**: cluster-1 (README + repo metadata), cluster-2 (Anthropic-direct-org context)

---

## Definition

`anthropics/claude-for-legal` is a **vendor-published reference implementation of multi-vertical legal-workflow plugin suite** by Anthropic PBC, organized as 12 vertical plugins (commercial + corporate + employment + privacy + product + regulatory + AI-governance + IP + litigation + law-student + legal-clinic + legal-builder-hub) containing 60+ named agents, with 5 managed-agent cookbooks (reg-monitor + renewal-watcher + docket-watcher + diligence-grid + launch-radar) executing via cron-style scheduled deployment, distributed across **CORPUS-RECORD 5-channel matrix** (Claude Cowork + Claude Code + Managed Agents API + Microsoft 365 + custom cloud), integrating **CORPUS-RECORD 20+ MCP enterprise-system connectors** (Slack + GDrive + CoCounsel + Box + Ironclad + DocuSign + iManage + Everlaw + CourtListener + Trellis + Aurora + Definely + Lawve AI + Courtroom5 + Descrybe + Solve Intelligence + TopCounsel + Linear + Atlassian Jira + Asana), built with **Cold-Start Interview Pattern** for practice-profile generation, **Practice-Profile Persistence at config layer** surviving plugin updates, **Community Skill Trust Layer 5-Gate Framework** (security review + allowlist + license gate + freshness gate + install log), **Legal Skill Design Framework** 9-parameter + 3-failure-mode QA, **3-Tier Liability/Attorney-Review Guardrail Discipline** ("draft for attorney review" + "do not represent Anthropic's legal positions" + `[verify]` citation flag), and **External-Plugin Partner-Vendor Directory Structure** (`external_plugins/cocounsel-legal/` = Thomson Reuters integration).

## Why this is a single entity

The 12-plugin × 60+-agent × 20+-connector × 5-distribution-channel architecture is **deliberately packaged as a unified bundle** under one repository with shared validation tooling (`scripts/`) + shared Plugin format standard + shared Community Skill Trust Layer + shared Legal Skill Design Framework + shared liability discipline. Treating sub-components as separate entities would lose the **vendor-published reference-implementation identity** which is the load-bearing property.

## Pattern Library implications

### Phase 4b PRIMARY at v92

**Pattern #84 84c.1 sub-sub-mechanism "Marketplace-Plugin-Install" N=3 PROMOTION-LOCKED-IN** via v2.3 §3 vehicle #1 (Pattern-promotion / sub-mechanism-formalization at N=3 threshold).

Evidence:
- N=1 at v85 ui-ux-pro-max-skill (`/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill`)
- N=2 at v90 academic-research-skills (`/plugin marketplace add Imbad0202/academic-research-skills`)
- N=3 at v92 claude-for-legal (`/plugin marketplace add <path-to-this-repo>` + `/plugin install <plugin>@claude-for-legal` with 12-plugin variant)

Promotion-criteria PASS:
- Criterion 1 corpus-first: PASS at v85 N=1 anchor
- Criterion 4 variant-within-sub-sub-mechanism: PASS at N=3 (single-plugin v85/v90 + multi-plugin-marketplace v92)
- Audit-administrative promotion at v95 recommended.

### Strengthening events at v92

| Pattern / Library-vocab | Type | Implication |
|---|---|---|
| **Pattern #84 84c.1 sub-sub-mechanism** | **N=3 PROMOTION-LOCKED-IN** (PRIMARY) | v95 administrative-formalization |
| v64 T1 sub-archetype "Domain-Vertical-Skill-Collection" | N=2 STRENGTHENING (v64 + v92) | v95 N=3 watch |
| Pattern #66 supply-chain awareness | STRONGEST single-subject density at v60+ window | Community Skill Trust Layer 5-gate framework |
| Pattern #83 Honest-Deficiency-Disclosure | Within-pattern strengthening at vendor-source scale | 3-tier liability framing |
| Pattern #18 sub-archetype B "one-binary-many-CLIENTS" | Within-pattern strengthening | Claude API + 5 distribution channels |
| Pattern #78 Living-Domain-Standards Tracking | Within-pattern strengthening | Regulatory feed monitoring + freshness gate |
| Pattern #57 sub-variant 57c-product | Within-pattern strengthening at intra-vendor ecosystem density | 4 Anthropic-product references at single subject |
| Pattern #52 HIGH-NOT-EXTREME sub-class | N+1 strengthening at pulse-window | ~234/d × 32d |

### NEW Library-vocab registrations at v92 (6 items + 1 sub-axis)

| Item | Status |
|---|---|
| **NEW (a)-7 sub-axis "Foundational-Vendor-Direct-Source"** | PROVISIONAL N=1 (v2.4 codification candidate) |
| Library-vocab "Cold-Start Interview Pattern with Practice-Profile Generation" | PROVISIONAL N=1 |
| Library-vocab "Practice-Profile Persistence at Config Layer Surviving Plugin Updates" | PROVISIONAL N=1 |
| Library-vocab "Community Skill Trust Layer with 5-Gate Framework" | PROVISIONAL N=1 |
| Library-vocab "3-Tier Liability/Attorney-Review Guardrail Discipline" | PROVISIONAL N=1 |
| Library-vocab "External-Plugin Partner-Vendor Directory Structure" | PROVISIONAL N=1 |
| Library-vocab "5-Distribution-Channel Matrix at Single Subject" (CORPUS-RECORD) | PROVISIONAL N=1 |
| Library-vocab "20+ MCP Enterprise-System Connector Density at Single Subject" (CORPUS-RECORD) | PROVISIONAL N=1 |

## Comparison to peer T1 vertical-skill-collection subjects

| Aspect | v64 claude-seo | v76 agent-skills-standard | v85 ui-ux-pro-max | v90 academic-research-skills | **v92 claude-for-legal** |
|---|---|---|---|---|---|
| Author/org | Patrick Tan (single-author) | Nguyen Huy Hoang (VN-solo) | nextlevelbuilder (VN-org) | Edward Wu (Taiwan-solo) | **Anthropic PBC (vendor itself)** |
| Vertical | SEO | Generic standards-layer | UI/UX design | Academic-research | **Legal (12 sub-verticals)** |
| Skill/agent count | ~24 skills | 259 skills × 20+ frameworks | 669+ codified elements | 4-sub-skill × 42-agent | **12-plugin × 60+ agents** |
| Distribution channels | git+symlink | npm CLI sync + MCP server | 18-platform skill.json | 3-channel (Marketplace + git+symlink + Codex) | **CORPUS-RECORD 5-channel** |
| MCP connector density | None at scale | 1 (MCP Transparent-Interception) | Not central | None at scale | **CORPUS-RECORD 20+** |
| Liability/disclosure framing | Honest-deficiency | None observed | None observed | 31% citation error-rate | **3-tier liability discipline** |
| Authorial status | Third-party single-author | Third-party VN-solo | Third-party VN-org | Third-party Taiwan-solo | **Foundational-vendor-direct-source** |

v92 sits at a **distinct structural point**: vendor-published-reference-implementation with foundational-vendor-direct-source status + CORPUS-RECORD distribution-channel + connector-density. Closest sub-archetype anchor = v64's "Domain-Vertical-Skill-Collection" but at vendor-published-multi-vertical-density scale.

## Functional fit for Storm Bear vault

**DIRECT functional-fit**: **INDIRECT** — Storm Bear not a lawyer; legal-vertical doesn't apply to vault use-cases.

**METHODOLOGY-INFLUENCE functional-fit**: **STRONG** — Multiple patterns ADAPT cleanly to vault routine v2.4:

| claude-for-legal pattern | Vault routine v2.4 adaptation candidate |
|---|---|
| Cold-start interview pattern | Wiki-build cold-start interview for new-project scaffolding |
| Practice-profile persistence at config layer | Routine-config persistence at `_state/` chapter level |
| Community Skill Trust Layer 5-gate | External-Pattern-contribution 5-gate discipline |
| 3-tier liability/attorney-review guardrail | Honest-disclosure 3-tier discipline at audit + wiki-ship boundary |
| External-plugin partner-vendor directory structure | External-resource-attribution-as-explicit-directory pattern |
| 5-distribution-channel matrix | Multi-distribution-deployment as Phase 0 classification axis enrichment |
| Scheduled-agent execution via managed-cookbooks | Scheduled-audit-cron cadence at routine v2.4 |

**Pilot ranking**: claude-for-legal **NOT a direct-utility pilot candidate**. **Methodology-influence Tier-1-special** for routine v2.4 evolution. Direct-utility pilot ranking unchanged from post-v91 (cc-switch #1 / claude-comstyle #2 / html-anything #3 / teleport #4 / VibeCodingTracker #5 / academic-research-skills #6 CONDITIONAL).

## Suggested next-action (vault application)

Do NOT install the full bundle. Instead, at v95 audit, evaluate which 2-3 patterns to ADAPT for routine v2.4 codification. **Recommended top-3 priority adaptations**:
1. **Cold-start interview pattern** for wiki-build new-project scaffolding (interactive seed-document → CLAUDE.md generation; 10-20 min)
2. **Practice-profile persistence at config layer** for routine-config persistence at `_state/` chapter level
3. **Community Skill Trust Layer 5-gate** for external-Pattern-contribution discipline

These three patterns map most directly to vault operational needs and would meaningfully enhance routine v2.4 capabilities.
