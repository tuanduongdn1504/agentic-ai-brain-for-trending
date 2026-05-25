# v95 Phase 0 + Phase 0.9 STRICT INCLUDE Verdict

**Subject**: [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
**Routine version**: v2.3 (SIXTH WIKI UNDER ROUTINE v2.3 PRODUCTION-BASELINE)
**Verdict date**: 2026-05-25

---

## Phase 0 — Classification

### Subject metadata (GitHub API verified 2026-05-25)

| Field | Value |
|---|---|
| Repo | anthropics/claude-plugins-official |
| Owner | **Anthropic PBC** (organization id 76263028) — THIRD Anthropic-direct-org subject in v60+ window |
| Created | 2025-11-20 |
| Last push | 2026-05-24 (1 day before fetch — actively maintained) |
| Age | **186 days** (~6.2 months) |
| Stars | **27,357** |
| Forks | **2,912** |
| Watchers (subscribers) | **189** (CORPUS-RECORD-HIGH for Anthropic-direct-org subjects in v60+: v92 82 + v93 899 + v95 189; v93 dominates) |
| Open issues | **700** (CORPUS-RECORD-HIGH for Anthropic-direct-org subjects in v60+: v92 46 + v93 871 + v95 700) |
| License | **NULL** (no root LICENSE file) — README delegates: "Please see each linked plugin for the relevant LICENSE file" |
| Primary language | Python |
| Size | 4,157 KB |
| Homepage | https://code.claude.com/docs/en/plugins |
| Topics | `claude-code`, `mcp`, `skills` |
| Discussions | Disabled |
| Wiki | Disabled |
| Has pages | False |

### Tier classification

**T1 Plugin Marketplace** — distribution-infrastructure-anchor at vendor-source-authoritative scope. Distinct from prior T1 instances (assistant skills + plugins) because this is the **marketplace itself** through which prior Anthropic-direct-org subjects are distributed.

### Velocity (Pattern #52 classification)

27,357 stars / 186 days = **~147.1 stars/day** = **Pattern #52 SUSTAINED-MODERATE-HIGH sub-class** upper-edge (25-150/d band; 147/d sits at the 150/d boundary). N+1 strengthening for SUSTAINED-MODERATE-HIGH sub-class (joining v75 impeccable + v77 easy-vibe + v81 taste-skill + v82 huashu-design).

### License (Pattern #45 NEW sub-typology candidate)

**No root LICENSE file** + README explicit delegation "Please see each linked plugin for the relevant LICENSE file" = NEW sub-typology candidate **"No-Root-License-with-Per-Subplugin-LICENSE-Delegation"** PROVISIONAL N=1, distinct from existing Pattern #45 sub-typologies 45a/45b/45c/45d/45e + Pattern #29 absent-LICENSE + Pattern #83 sub-mechanism 83f.4 README-Declared-but-no-LICENSE-file (v79 anchor). At foundational-vendor-direct-source scale this is corpus-novel.

### Plugin directory structure

- **`/plugins`** (internal Anthropic-developed): **36 plugins** — agent-sdk-dev / clangd-lsp / claude-code-setup / claude-md-management / code-modernization / code-review / code-simplifier / commit-commands / csharp-lsp / cwc-makers / example-plugin / explanatory-output-style / feature-dev / **frontend-design** / gopls-lsp / hookify / jdtls-lsp / kotlin-lsp / learning-output-style / lua-lsp / math-olympiad / mcp-server-dev / mcp-tunnels / php-lsp / playground / plugin-dev / pr-review-toolkit / pyright-lsp / ralph-loop / ruby-lsp / rust-analyzer-lsp / security-guidance / session-report / **skill-creator** / swift-lsp / typescript-lsp
- **`/external_plugins`** (third-party partner repos): **15 plugins** — asana / context7 / discord / fakechat / firebase / github / gitlab / greptile / imessage / laravel-boost / linear / playwright / serena / **telegram** / terraform
- **`.claude-plugin/marketplace.json`**: marketplace manifest with ~40+ additional `git-subdir` / `url` source entries pulling in partner plugins (42Crunch + Adobe + Salesforce + Endor + Aikido + Airtable + many more)

**Combined ecosystem scale**: ~51 directory subfolders + many more partner-marketplace.json references = corpus-novel marketplace-density at Anthropic-vendor-direct-source scope.

---

## Phase 0.9 STRICT INCLUDE Gate

### Criterion (a) — Author-cultural-peer evidence

**(a)-7 Foundational-Vendor-Direct-Source: N=3 PROMOTION-LOCKED-IN**

v92 claude-for-legal (PROVISIONAL N=1 anchor; 2026-05-23) + v93 anthropics/skills (N=2 STRENGTHENING; 2026-05-23) + **v95 claude-plugins-official (N=3 PROMOTION-LOCKED-IN; 2026-05-25)**

Cross-axis spread at N=3 promotion (per routine v2.3 §2):
- **Cross-author**: 3 distinct teams within Anthropic PBC (legal team v92 + agent-skills-spec team v93 + developer-relations / plugin-marketplace team v95)
- **Cross-vertical**: 3 distinct verticals (legal-workflow / agent-skills-standard-reference-implementation / plugin-marketplace-distribution-infrastructure)
- **Cross-scale**: 3-tier scale stratification (7K v92 + 139K v93 + 27K v95 = mid + mega + mid)

(a)-7 sub-axis **CONFIRMED** at v95 with administrative-promotion to formal Phase 0.9 (a) sub-axis at v96 audit recommended.

**Verdict (a)**: **STRONGEST** via (a)-7 N=3 PROMOTION-LOCKED-IN.

### Criterion (b) — Vault-deployability + cost-of-trial

**This IS the marketplace.** Storm Bear's daily Claude Code use already invokes claude-plugins-official under the hood whenever any Anthropic plugin or external plugin is installed via `/plugin install {name}@claude-plugins-official`.

**Cost-of-trial**: **MINIMUM** — already-installed-by-default via Claude Code plugin system. No incremental install cost.

**Direct functional fit**:
- 36 internal Anthropic plugins available immediately incl. `claude-md-management` (highly applicable to vault `CLAUDE.md` shim work) + `skill-creator` (directly applicable to routine v2.3 → v2.4 codification work) + `session-report` (potentially useful for vault session-handoff discipline) + `frontend-design` (CORPUS-RECURSIVE — Anthropic's foundational design skill that v75 + v82 + v83 all reference)
- 15+ external partner plugins incl. `telegram` (corpus-recursive to v88 teleport operator-notification-bridge) + `linear` (corpus-recursive to v62/v88) + `github` + `playwright`

**Existing-infrastructure-overlap**: **YES** — already-loaded in Claude Code default marketplace.

**Verdict (b)**: **STRONGEST** — MINIMUM cost (zero install) + multiple DIRECT operator-applicable plugins (claude-md-management + skill-creator + session-report + frontend-design) + existing-infrastructure-overlap maximum.

### Criterion (c) — Methodology-influence-node value

**Distribution-infrastructure-anchor at vendor-source-authoritative scope**:
- v93 anthropics/skills publishes its `document-skills` + `example-skills` sub-marketplace through claude-plugins-official's broader plugin-ecosystem
- v92 claude-for-legal's 12-plugin legal bundle is distributed via Anthropic's plugin marketplace infrastructure (this repo)
- v75 impeccable + v82 huashu-design + v83 open-design all extend / reverse-engineer / position-against Anthropic's `frontend-design` skill — which is HERE at `/plugins/frontend-design/`
- v88 teleport sibling-pattern: claude-plugins-official's `external_plugins/telegram/` is the Anthropic-vetted Telegram integration

This creates a **corpus-recursive distribution-layer anchor**: v95 is the upstream of multiple prior corpus subjects = methodology-influence at maximum depth within the marketplace-distribution scope.

**Other methodology-influence observations**:
- **CORPUS-FIRST two-tier plugin-marketplace structure at Anthropic-vendor-direct-source** (internal `/plugins/` + external partner `/external_plugins/` directories + marketplace.json `git-subdir` / `url` source references for many additional partners)
- **CORPUS-FIRST explicit external-plugin-submission process** via `clau.de/plugin-directory-submission` form (NEW Library-vocab "External-Plugin-Submission-Process via Vendor-Curated Form" PROVISIONAL N=1)
- **CORPUS-FIRST "Anthropic-managed" curated-marketplace framing** at vendor-source-authoritative scope (distinct from third-party-curated marketplaces precedent)
- **CORPUS-FIRST 700-open-issues at Anthropic-direct-org subject** (highest engagement-density in (a)-7 cluster)
- **CORPUS-FIRST no-root-LICENSE with per-subplugin-LICENSE-delegation at foundational-vendor-direct-source scale** (Pattern #45 sub-typology candidate)
- **CORPUS-FIRST 36-internal-plugin + 15-external-directory + 40+-marketplace.json-source-references combined ecosystem-density**
- **CORPUS-FIRST schema-referenced marketplace.json** (`$schema` at https://anthropic.com/claude-code/marketplace.schema.json)

**Verdict (c)**: **STRONGEST** — distribution-infrastructure-anchor for corpus-recursive chain + 7+ corpus-novel methodology axes + curated-marketplace + 36-internal-plugin density at Anthropic-direct-source.

### Criterion (d) — Pattern-density at corpus scale

**Pattern strengthening events at v95**:

| Pattern | Strengthening |
|---|---|
| **Phase 0.9 (a)-7 sub-axis** | **N=3 PROMOTION-LOCKED-IN** (v92+v93+v95) — PRIMARY |
| **Pattern #84 84c.1 Marketplace-Plugin-Install** | N=6 POST-PROMOTION STRENGTHENING (v85+v90+v92+v93+v94+v95) — the subject IS the marketplace |
| **Pattern #52 SUSTAINED-MODERATE-HIGH sub-class** | N+1 strengthening at upper-edge (~147/d × 186d) |
| **Pattern #45** | NEW sub-typology candidate "No-Root-License-with-Per-Subplugin-LICENSE-Delegation" PROVISIONAL N=1 |
| **Pattern #57 sub-variant 57c-product** | within-pattern strengthening at INTRA-VENDOR ecosystem-citation density (~36 Anthropic-internal-plugin citations in single subject) |
| **Pattern #66 supply-chain awareness** | within-pattern strengthening (explicit "trust a plugin before installing" disclaimer + "Anthropic does not control what MCP servers, files, or other software are included in plugins" honest-deficiency) |
| **Pattern #83 Honest-Deficiency-Disclosure** | within-pattern strengthening at vendor-source-authoritative scale (educational-disclaimer + cannot-verify-third-party + per-plugin-LICENSE-delegation) |
| **Pattern #18 sub-archetype B "one-binary-many-CLIENTS"** | within-pattern (Claude Code plugin system distributes to N developer environments) |
| **Pattern #82 quantitative-marketing** | LOWER-density within-pattern (README is intentionally minimal at vendor-source-authoritative scope; CONTRAST observation) |

**Library-vocab N+1 events at v95**:
- **PRIMARY**: (a)-7 N=3 PROMOTION-LOCKED-IN
- **NEW Library-vocab "Two-Tier Plugin Directory (Internal + External + Marketplace.json) at Vendor-Authoritative Scope"** PROVISIONAL N=1
- **NEW Library-vocab "External-Plugin-Submission-Process via Vendor-Curated Form (clau.de/plugin-directory-submission)"** PROVISIONAL N=1
- **NEW Library-vocab "Anthropic-Managed Curated-Marketplace Framing"** PROVISIONAL N=1
- **NEW Library-vocab "No-Root-LICENSE with Per-Subplugin-LICENSE-Delegation at Foundational-Vendor-Direct-Source Scale"** PROVISIONAL N=1 (also Pattern #45 sub-typology candidate)
- **NEW Library-vocab "Schema-Referenced Marketplace.json with $schema URL"** PROVISIONAL N=1
- **NEW Library-vocab "Distribution-Infrastructure-Anchor for Corpus-Recursive Chain"** PROVISIONAL N=1 (captures v95's role as upstream of v92 + v93 + frontend-design lineage)

**Verdict (d)**: **STRONGEST** — N=3 PROMOTION-LOCKED-IN PRIMARY + Pattern #84 84c.1 N=6 + multi-Pattern strengthening across 8+ patterns + 6 NEW Library-vocab PROVISIONAL + Pattern #45 NEW sub-typology candidate.

---

## INCLUDE Verdict

**STRONGEST INCLUDE 4/4 with ALL FOUR axes STRONGEST**

| Axis | Verdict |
|---|---|
| (a) Author-cultural-peer | **STRONGEST** (a)-7 N=3 PROMOTION-LOCKED-IN |
| (b) Vault-deployability | **STRONGEST** MINIMUM cost (zero-install already-loaded) + multi-DIRECT applicability |
| (c) Methodology-influence-node | **STRONGEST** distribution-infrastructure-anchor + 7+ corpus-novel methodology axes |
| (d) Pattern-density | **STRONGEST** N=3 PROMOTION PRIMARY + Pattern #84 84c.1 N=6 + 6 NEW Library-vocab + Pattern #45 NEW sub-typology |

**SECOND all-4-STRONGEST verdict in 2-wiki window since v93** (v94 was STRONGEST 4/4 with (b)(c) STRONGEST + (a)(d) STRONG — NOT all-4-STRONGEST).

**Streak**: extends to **"29+1*"** (29 PASS v65-v83 + v85 + v87-v95 + 1 OVERRIDE v84) NEW CORPUS-RECORD = **10-consecutive clean PASS post-v84 OVERRIDE** = first 10-consecutive milestone post-OVERRIDE.

**Override-frequency**: 1-in-31 (well below 2-in-20 / 3-in-30 v2.3 §7 redesign trigger thresholds; v2.3 redesign trigger COMFORTABLY UNRESOLVED).

**INCLUDE rate**: 31-instance window v65-v95 = 30 PASS + 1 OVERRIDE = **96.8% INCLUDE rate** uptick from v94's 96.7%.

**Strength categorization v65-v95**: STRONGEST × 14 + STRONG × 8 + MODERATE × 4 + WEAK × 5 + OVERRIDE × 1 (STRONGEST extends lead by 6 over STRONG + by 9 over WEAK).

---

## Audit-deferral note (v2.3 §11 + §12 + §13)

v95 was the **projected natural-cadence audit window** per post-v94 state-block ("v95 projected batch ~35-45 items"). Operator elected wiki-ship at v95 = **1-WIKI-DEFERRAL** trigger condition. CRITICAL trigger threshold (2+ consecutive deferrals) NOT YET reached but at-risk if v96 also ships wiki.

**v96 audit batch projection updated**: v90 ~8-10 + v91 ~12-13 + v92 ~10 + v93 ~10 + v94 ~12-15 + **v95 ~14-16 NEW** = **~66-74 items** projected at v96 = **NEW CORPUS-RECORD audit batch projected** (would surpass v90's 43-item prior record by 23+ items if executed at v96).

**Operator-attention recommendation**: Strongly consider executing v96 as audit-only (not wiki-ship) to address the carry-over backlog before it grows further. Audit-class assignment at v96 would be **1-WIKI-DEFERRAL-CARRY-OVER + AUDIT-BATCH-CORPUS-RECORD + PROMOTION-DRIVEN** (since (a)-7 N=3 administrative promotion is queued + Pattern #84 84c.1 N=3 administrative promotion from v92 still queued).

---

## Pilot ranking impact

**Tier-1 actionable pilot ranking insertion (post-v95)**:

| Rank | Subject | Axis |
|---|---|---|
| #1 | Understand-Anything v94 | Vault-wiki-visualization (`/understand-knowledge` literally designed for Karpathy-pattern wikis) |
| **#2 NEW** | **claude-plugins-official v95** | Direct vault-applicable plugins: `claude-md-management` + `skill-creator` + `session-report` + `frontend-design` (CORPUS-RECURSIVE) — already-installed-by-default = MINIMUM cost-of-trial |
| #3 DISPLACED | cc-switch v73 | Multi-provider portability |
| #4 DISPLACED | anthropics/skills v93 | Multi-format publishing |
| #5 DISPLACED | claude-comstyle v87 | Communication-style composition |
| #6 DISPLACED | html-anything v91 | Markdown → multi-surface output |
| #7 DISPLACED | teleport v88 | Telegram MCP session-handoff |
| #8 DISPLACED | VibeCodingTracker v89 | Cost-observability |
| #9 DISPLACED | academic-research-skills v90 | Academic-research pipeline CONDITIONAL |
| #10 DISPLACED | agent-skills-standard v76 | Standards-layer codification |

**Recommended IMMEDIATE pilot trial path** (~5 min for first-batch):
```
/plugin install claude-md-management@claude-plugins-official
/plugin install skill-creator@claude-plugins-official
/plugin install session-report@claude-plugins-official
```

Expected outcome: `claude-md-management` directly applicable to the ~22KB root CLAUDE.md shim work; `skill-creator` directly applicable to routine v2.3 → v2.4 codification work; `session-report` may help with vault session-handoff discipline.

**Methodology-influence Tier-1-special multi-track position #4 NEW**:
- #1: v92 claude-for-legal anchor (foundational-vendor-direct-source legal methodology)
- #2: v93 anthropics/skills (SKILL.md spec + template authoritative)
- #3: v94 Understand-Anything (Karpathy-wiki-pattern-analysis tool — third corpus-recursive event class)
- **#4 NEW**: v95 claude-plugins-official (distribution-infrastructure-anchor for corpus-recursive chain)

---

## Phase 4b PRIMARY analysis

See [(C) (a)-7-Foundational-Vendor-Direct-Source-N3-PROMOTION-LOCKED-IN.md](./%28C%29%20%28a%29-7-Foundational-Vendor-Direct-Source-N3-PROMOTION-LOCKED-IN.md) for the full proposal-document.

---

**Next action**: file Phase 4b PRIMARY proposal-document → build wiki entry pages → update vault state (`_state/03c-projects-v61-v94.md` rename to `v61-v95.md` + append v95 entry; root CLAUDE.md shim update with v95 narrative + streak "29+1*" + audit-deferral note).
