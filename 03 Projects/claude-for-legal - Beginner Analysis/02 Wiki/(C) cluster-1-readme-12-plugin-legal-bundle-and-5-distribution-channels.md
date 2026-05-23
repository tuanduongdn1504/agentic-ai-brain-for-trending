# (C) Cluster 1 — README + Repo Metadata: 12-Plugin Legal Bundle + 60+ Agents + 5 Managed-Agent Cookbooks + 5-Distribution-Channel CORPUS-RECORD Matrix + 20+ MCP Enterprise-Connector CORPUS-RECORD Density + Cold-Start Interview + Community Skill Trust Layer 5-Gate + 3-Tier Liability Discipline

**Source**: https://github.com/anthropics/claude-for-legal (README + GitHub API metadata)
**Fetched**: 2026-05-23 (Phase 0 + Phase 2 ingestion)
**Wiki version**: v92 (THIRD under routine v2.3 baseline)

---

## 1. Subject self-positioning

Repo description: *"A suite of plugins for legal workflows."*

Tagline: *"Reference agents, skills, and data connectors for the legal workflows we see most — in-house commercial, privacy, product, corporate, employment, litigation, regulatory, AI governance, IP, and the learning side of the practice (law school clinics and students)."*

The product positions itself as a **reference implementation of multi-vertical legal-workflow plugin suite published by Anthropic itself**. Distinct from third-party plugin authors — this is Anthropic publishing reference agents/skills for legal professionals.

## 2. Repository metrics

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
| Commits on main | 29 |
| Repo size | 404 KB |
| Velocity | ~234 stars/day pulse-window |

**~234 stars/day at 32-day pulse-window** places v92 at HIGH-NOT-EXTREME Pattern #52 sub-class — within the 150-300/d band but at upper-mid range. Pattern #52 sub-class N+1 strengthening at pulse-class duration; not multi-month-sustained EXTREME-VIRAL.

## 3. License + Tech stack

- **License**: Apache-2.0 © 2026 Anthropic PBC
- **Primary languages**: Python 67.2% + Shell 32.8%
- **Workspace structure**: monorepo with 12-plugin-directory tree + `managed-agent-cookbooks/` + `external_plugins/` + `scripts/` validation tooling
- **Validation tooling**: `scripts/validate.py` + `scripts/orchestrate.py` + `scripts/lint-tool-scope.py` + `scripts/test-cookbooks.sh` + `scripts/deploy-managed-agent.sh`

## 4. 12-Plugin Vertical Bundle

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

This is **higher vertical-density than v64 claude-seo** (SEO-only single-vertical-domain). The 12-vertical density represents **N=2 STRENGTHENING for v64's T1 sub-archetype "Domain-Vertical-Skill-Collection"** — v92 establishes 2-instance evidence-base for this sub-archetype.

Each plugin follows a standard directory structure:
```
<plugin>/
  .claude-plugin/plugin.json
  CLAUDE.md               # template practice profile
  README.md
  skills/                 # each is a /<plugin>:<skill> slash command
  agents/                 # scheduled agents (if any)
  hooks/                  # pre- and post-tool hooks
```

## 5. 60+ Named Agents Across 12 Plugins

Full inventory (sample shown; complete list in source):

**commercial-legal**: Vendor Agreement Reviewer + NDA Triager + Amendment Tracer + Renewal Watcher (scheduled) + Deal Debrief (scheduled) + Playbook Monitor (scheduled) + Escalation Router

**corporate-legal**: Tabular Diligence Review + Issue Extractor + Board Consent Drafter + Material Contracts Schedule Builder + Entity Compliance Tracker + Closing Checklist Driver + Integration Runbook + Data Room Watcher (scheduled)

**employment-legal**: Termination Reviewer + Hire Reviewer + Worker Classification Screener + Leave Tracker (scheduled) + Investigation Lead + Policy Drafter + International Expansion Planner + Wage & Hour Q&A

**privacy-legal**: DSAR Responder + DPA Reviewer + PIA Generator + Privacy Triager + Privacy Reg Gap Checker + Privacy Policy Monitor

**product-legal**: Launch Reviewer + Marketing Claims Checker + "Is this a problem?" Triage + Launch Watcher (scheduled)

**regulatory-legal**: Reg Feed Watcher (scheduled) + On-demand Reg Check + Policy Diff + Gap Tracker + Policy Redrafter + NPRM Comment Tracker

**ai-governance-legal**: AI Use Case Triager + AI Impact Assessor + Vendor AI Reviewer + AI Reg Gap Checker + AI Policy Monitor

**ip-legal**: Trademark Clearance Screener + Cease & Desist Drafter + DMCA Takedown + OSS Compliance Checker + FTO Triager + Infringement Triager + IP Clause Reviewer + IP Portfolio Tracker + IP Renewal Watcher (scheduled)

**litigation-legal**: Claim Chart Builder + Docket Watcher (scheduled) + Demand Letter Drafter + Demand Intake + Demand Received Triage + Subpoena Triage + Chronology Builder + Deposition Prep + Brief Section Drafter + Privilege Log Reviewer + Legal Hold + Matter Intake + Matter Briefing + Portfolio Status + Outside Counsel Status

**law-student**: Bar Prep Coach + Socratic Drill Sergeant + IRAC Grader + Case Briefer + Outline Builder + Cold Call Prep + Exam Forecaster + Legal Writing Critic + Flashcard Drillmaster + Study Planner

**legal-clinic**: Clinic Intake + Case Memo Scaffold + Research Roadmap + Clinic Deadline Tracker + Case Status Summarizer + Client Letter Drafter + Student Ramp + Semester Handoff + Supervisor Review Queue

**legal-builder-hub**: Skill Registry Browser + Skill Installer + Skill QA + Community Skill Recommender + Community Skill Updater + Registry Sync (scheduled)

**Agent inventory observations**:
- **60+ named agents** is mid-range LDS density in v60+ window (below v85 669+ codified-elements + v76 259-skill records but above most subjects)
- **"Scheduled" agents** marked in inventory (e.g., Renewal Watcher / Docket Watcher / IP Renewal Watcher) connect to Managed-Agent-Cookbooks system

## 6. 5 Managed-Agent-Cookbooks (Scheduled Execution)

| Cookbook | Purpose | Deployment |
|---|---|---|
| reg-monitor | Regulatory feed monitoring | `scripts/deploy-managed-agent.sh reg-monitor` |
| renewal-watcher | Contract renewal tracking | `scripts/deploy-managed-agent.sh renewal-watcher` |
| docket-watcher | Court docket monitoring | `scripts/deploy-managed-agent.sh docket-watcher` |
| diligence-grid | M&A diligence tracking | `scripts/deploy-managed-agent.sh diligence-grid` |
| launch-radar | Product launch monitoring | `scripts/deploy-managed-agent.sh launch-radar` |

Deployment via `ANTHROPIC_API_KEY` env var + Managed Agents API `/v1/agents` endpoint. Cron-style frontmatter on agent markdown files. Validation via `bash scripts/test-cookbooks.sh` dry-runs before push.

**Subagent delegation (preview)**: Single-level delegation via `callable_agents` mechanism. Event routing: Orchestrator routes `handoff_request` events via custom orchestration layer.

## 7. 5-Distribution-Channel Matrix (CORPUS-RECORD)

| Channel | Mechanism | Install path |
|---|---|---|
| **Claude Cowork** | Plugin marketplace | Browse plugins → Install (60-sec install) OR upload custom plugin zip |
| **Claude Code** | Plugin marketplace | `/plugin marketplace add <path-to-this-repo>` + `/plugin install <plugin>@claude-for-legal` |
| **Claude Managed Agents API** | API endpoint deployment | `export ANTHROPIC_API_KEY=...` + `scripts/deploy-managed-agent.sh <cookbook>` |
| **Claude for Microsoft 365** | AppSource add-in (Word/Excel/PowerPoint/Outlook) | Tracked changes output + Excel export with citation columns |
| **Custom cloud deployment** | Vertex AI / Bedrock / internal gateway | Separate `claude-for-msft-365-install` tooling |

**5-distribution-channel matrix at single subject = CORPUS-RECORD** exceeding v83 open-design's 4-distribution-method record (source + Docker + Desktop Electron + Vercel) and v90 academic-research-skills's 3-channel matrix (Marketplace + git+symlink + Codex sibling).

**Library-vocab "5-Distribution-Channel Matrix at Single Subject" PROVISIONAL N=1** (CORPUS-RECORD).

## 8. 20+ MCP Enterprise-System Connectors (CORPUS-RECORD Density)

| Category | Connectors |
|---|---|
| Collaboration | Slack, Google Drive, Box |
| Legal Research | CoCounsel Legal (Thomson Reuters), CourtListener, Lawve AI, Solve Intelligence, Descrybe |
| Contract Management | Ironclad, Definely, DocuSign, iManage |
| Litigation Tools | Everlaw, Trellis, Aurora, Courtroom5 |
| Specialized Legal | TopCounsel |
| Project Management | Linear, Atlassian Jira, Asana |

**20+ MCP enterprise-system connectors at single subject = CORPUS-RECORD density** in v60+ window. Exceeds all prior subjects.

**Library-vocab "20+ MCP Enterprise-System Connector Density at Single Subject" PROVISIONAL N=1** (CORPUS-RECORD).

Pattern #18 sub-archetype "shared-backend-service" sub-mechanism B "one-binary-many-CLIENTS" within-pattern strengthening at MCP-connector-aggregation axis.

## 9. Cold-Start Interview Pattern

Per-plugin interactive setup (10-20 min) that reads seed documents and generates initial CLAUDE.md practice-profile.

Invocation:
```bash
/commercial-legal:cold-start-interview
/privacy-legal:cold-start-interview
/corporate-legal:cold-start-interview
```

Quick-start alternative: ~2 minutes (with refinement later). Re-runnable for incremental updates via command re-invocation.

**Library-vocab "Cold-Start Interview Pattern with Practice-Profile Generation" PROVISIONAL N=1** (corpus-novel methodology pattern).

## 10. Practice-Profile Persistence Layer

Path: `~/.claude/plugins/config/claude-for-legal/<plugin>/CLAUDE.md`

Persistence properties:
- **Survives plugin updates** — installation upgrades preserve practice-profile
- **Re-runnable cold-start interview** for incremental updates via command re-invocation
- **Connector swap** via `.mcp.json` edits at practice-profile-level
- **Skill forking** via markdown-based skill editing
- **Custom agent scheduling** via markdown with cron-style frontmatter

**Library-vocab "Practice-Profile Persistence at Config Layer Surviving Plugin Updates" PROVISIONAL N=1** (corpus-novel persistence pattern).

## 11. Community Skill Trust Layer (5-Gate Framework)

Per `legal-builder-hub` plugin (community skill marketplace):

| Gate | Mechanism |
|---|---|
| 1. Security review | Hidden-content scan + injection detection + structural trust check |
| 2. Allowlist | Restrictive-by-default source gate |
| 3. License gate | Deployment-context-aware (personal / firm-internal / product-embedding) |
| 4. Freshness gate | Tracks if reference content (regulations + statutes) passed verification window |
| 5. Install log | Auditable record of what's installed + from where + under what license |

**Pattern #66 supply-chain-awareness STRONGEST single-subject density at v60+ window** — 5-gate framework is most comprehensive supply-chain-discipline observation in corpus.

**Library-vocab "Community Skill Trust Layer with 5-Gate Framework" PROVISIONAL N=1** (corpus-novel framework).

## 12. 3-Tier Liability/Attorney-Review Guardrail Discipline

**Tier 1 — Output framing**:
> *"Every output from these plugins is a draft for attorney review — not legal advice, not a legal conclusion, not a substitute for a lawyer. They are built with guardrails that reflect that: source attribution on every citation, conservative defaults on privilege and subjective legal calls, jurisdiction assumptions surfaced, and explicit gates before anything is filed, sent, or relied on. A lawyer reviews, verifies, and takes professional responsibility for anything that leaves the building. These plugins make that review faster; they do not replace it."*

**Tier 2 — Organizational disclaimer**:
> *"These plugins do not represent Anthropic's legal positions. They are tools that help lawyers analyze issues. Where a skill includes a checklist item, a suggested framework, a risk flag, or a characterization of case law or regulatory guidance, that is an aid to the reviewing attorney's own analysis, not a statement of Anthropic's view of the law."*

**Tier 3 — Citation verification**:
- Citations from research connectors: tagged with source
- Unverified citations: flagged `[verify]`
- Research-connector requirement: *"Everything else is better with one, and citations are unverified without one."*

**Library-vocab "3-Tier Liability/Attorney-Review Guardrail Discipline" PROVISIONAL N=1** (corpus-novel discipline at Anthropic-direct-org scale).

Pattern #83 Honest-Deficiency-Disclosure within-pattern strengthening at vendor-source-authoritative scale.

## 13. External-Plugin Partner-Vendor Directory Structure

`external_plugins/cocounsel-legal/` = Thomson Reuters CoCounsel Legal Research integration as **explicit partner-vendor plugin directory** at top-level repo tree.

This is corpus-novel **partner-vendor-integration-as-explicit-directory pattern** — distinct from in-tree-bundled-skills (v83 nexu-io bundled op7418/guizang skill) or out-of-tree-citation-only references.

**Library-vocab "External-Plugin Partner-Vendor Directory Structure (explicit `external_plugins/` directory)" PROVISIONAL N=1**.

## 14. Legal Skill Design Framework

9 parameters + 3 failure modes for QA of community-contributed skills. Validation tooling: `bash scripts/test-cookbooks.sh` dry-runs managed-agent cookbooks before push.

Referenced registries: *"LegalOps Consulting's `lpm-skills`"* and *"Lawvable"*.

## 15. Anthropic-Product-Ecosystem Citation Density

| Anthropic product cited | Role at v92 |
|---|---|
| Claude Cowork | Plugin marketplace install channel |
| Claude Code | Plugin marketplace install channel |
| Claude Managed Agents API | Scheduled-agent deployment endpoint |
| Claude for Microsoft 365 | Word/Excel/PowerPoint/Outlook sidebar |
| Model Context Protocol (MCP) | Open standard for connector integrations |

**4 Anthropic-product-ecosystem references at single subject** = Pattern #57 sub-variant 57c-product strengthening at vendor-product-ecosystem citation density. Distinct from prior cross-vendor citations (e.g., v83 16-harness multi-target) — this is INTRA-VENDOR ecosystem density.

## 16. Status Claims + Repo Activity

- **Repo activity**: 29 commits on main + 46 open issues + 34 open PRs = moderate active development
- **No published release** yet (32 days old; pre-1.0 reference implementation)
- Plugin marketplace listing implies stable-enough for distribution but pre-versioned

## 17. Summary

This cluster establishes the **product structural surface**:

- 12-plugin legal-vertical bundle (commercial + corporate + employment + privacy + product + regulatory + AI-governance + IP + litigation + law-student + legal-clinic + legal-builder-hub)
- 60+ named agents across 12 plugins
- 5 managed-agent cookbooks (reg-monitor + renewal-watcher + docket-watcher + diligence-grid + launch-radar) with cron-style scheduled execution
- **CORPUS-RECORD 5-distribution-channel matrix** (Claude Cowork + Claude Code + Managed Agents API + Microsoft 365 + custom cloud)
- **CORPUS-RECORD 20+ MCP enterprise-connector density**
- Cold-start interview pattern with practice-profile generation (corpus-novel)
- Practice-profile persistence at config layer surviving plugin updates (corpus-novel)
- Community Skill Trust Layer 5-gate framework (corpus-novel; Pattern #66 STRONGEST single-subject density)
- Legal Skill Design Framework 9-parameter + 3-failure-mode QA
- 3-tier liability/attorney-review guardrail discipline (corpus-novel at Anthropic-direct-org scale)
- External-plugin partner-vendor directory structure (corpus-novel)
- 4 Anthropic-product-ecosystem references at single subject (Pattern #57 57c intra-vendor strengthening)
- Apache-2.0 © Anthropic PBC; Python 67.2% + Shell 32.8%

**Phase 4b PRIMARY contribution**: This cluster's most significant finding for Phase 4b is the third instance of `/plugin marketplace add` install-command, which **promotes Pattern #84 84c.1 sub-sub-mechanism to N=3 PROMOTION-LOCKED-IN threshold**.

See cluster-2 for Anthropic-direct-org context and foundational-vendor-source positioning. Entity pages for Pattern Library implication detail.
