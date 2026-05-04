# gsd-2 - Beginner Analysis

54TH LLM Wiki for Storm Bear vault. Subject: `gsd-build/gsd-2` ("The evolution of Get Shit Done — now a real coding agent"). 14th+ v2.1-era execution. T1 extends to N=15.

## Claude's Role

Wiki maintainer running routine `llm-wiki-routine-v2.1.md`. Build 13 deliverables + Phase 5 + Phase 6 vault root sync.

## Probe data

| Field | Value |
|------|------|
| Repo | `gsd-build/gsd-2` |
| Stars | 6,619 |
| Forks | 677 (10.2%) |
| Open issues | 199 |
| License | **MIT** (Copyright **Lex Christopherson**, 2026) |
| Lang | TypeScript primary + Rust (`@gsd/native` N-API) |
| Created | 2026-03-11 (~46 days) |
| Pushed | 2026-04-26 (today) |
| Latest version | **v2.78.1** (78 minor versions in 46 days = ~1.7/day) |
| Topics | context-engineering, meta-prompting, spec-driven-development |
| Repo size | 97 MB raw / ~33 MB extracted |
| Org | **gsd-build** (created 2026-02-09; 8 public repos; gsd.build / contact@gsd.build) |
| Discord | discord.com/invite/nKXTsAcmbT |
| Crypto | $GSD Solana token (Dexscreener badge in README) |

## Authorship correction (vs brief assumption)

Brief assumed **TÂCHES** (GSD-1 author per v5 wiki). Repo evidence shows:
- LICENSE copyright = **Lex Christopherson** (2026)
- 3 ADR docs `/docs/dev/ADR-*` author/decider = **Lex Christopherson**
- Internal paths reference `/Users/lexchristopherson/.gsd/`
- Zero "TÂCHES" mentions in README/VISION/CONTRIBUTING/docs

**Honest verdict:** GSD-2 named author = Lex Christopherson per primary repo evidence. TÂCHES → Lex Christopherson identity-mapping is **unverified speculation**. Could be: (a) same person under different identity; (b) GSD-1 owner (TÂCHES) handed off to GSD-2 maintainer (Lex); (c) gsd-build org has multiple maintainers. **Document as-observed; do NOT assume identity continuity.**

## v2.1 12-axis classification

| Axis | Value |
|------|------|
| Tier | **T1 Agent-as-assistant — 15TH T1 entrant (largest tier in corpus)** |
| Archetype | **Org-led (gsd-build) + planned-successor-of-viral-flagship + Pi-SDK-vendoring + multi-component-with-cloud-tier** |
| Scale tier | Cold-start-rapid-growth (6.6K / 46 days = 144 stars/day; parent-product-amplified — GSD-1 viral 57.4K growth feeds GSD-2 adoption) |
| Primary lang | TypeScript (~95%) + Rust (`@gsd/native` N-API for performance) |
| Packaging | npm `gsd-pi` global + Dockerfile + planned managed RTK binary + workspaces (8 packages) |
| Origin | **Successor-of-viral-flagship** (GSD-1 grew 8K→57.4K post-v5 wiki; GSD-2 = explicit planned successor with migration roadmap) |
| Methodology | SDD continued + meta-prompting + context engineering + extension-first principle + state-machine-from-disk |
| Governance | **Light at root** (4 files: README 873 lines + VISION 37 lines + CONTRIBUTING 432 lines + CHANGELOG 3,843 lines + LICENSE) — **NO AGENTS.md / NO CLAUDE.md / NO SECURITY.md / NO CODE_OF_CONDUCT at root** |
| Primitive count | **~150-250** (8 packages + 24 bundled extensions + 35 skills + 13 agents + ~50 commands + Studio Electron app + workflows + ADRs) → **YELLOW** (similar to pi-mono v36 / shannon v45) |
| i18n | **EN + zh-CN** (`docs/zh-CN/` directory exists; verify scope) |
| Lineage | **Pi SDK vendored from pi-mono v36 wiki subject** (4 of 7 pi-mono packages: pi-coding-agent + pi-ai + pi-agent-core + pi-tui — verified via package.json `description: "vendored from pi-mono"` in all 4) + GSD-1 self-lineage + Mario Zechner methodology cited via Pi SDK link |
| Agent platforms | Standalone CLI primary + MCP server companion (`@gsd-build/mcp-server`) + 21 in-source bundled extensions + 1 extracted extension workspace + Daemon for background process (`@gsd-build/daemon`) + Studio Electron desktop |

## Phase 0.5 pattern pre-check

### STRENGTHENING (no new candidates registered — extends 17→18-streak NEW LONGEST)

1. **Pattern #57 Recursive Corpus Reference 6th data point CORPUS-FIRST EXPLICIT VENDORED-FROM-PI-MONO METADATA** — gsd-2's 4 pi-* packages each have `"description": "vendored from pi-mono"` in package.json + README cites Pi SDK link. **Strongest possible Pattern #57 evidence to date** — explicit vendoring acknowledgment in machine-readable metadata, not just narrative citation. Sub-variant **57d explicit-vendored-package-metadata** observation (N=1; stale-flag for v59).

2. **Pattern #58 Branding-Package Divergence NEW sub-variant 58e successor-repo-not-rename observation** — gsd-2 = NEW repo (not rename of get-shit-done) with explicit migration roadmap in VISION.md ("GSD-2 is the future. The goal is to eventually migrate GSD-1 users to GSD-2"). Distinct from 58a rename-without-npm-rename (OMC v27) / 58b rebrand-with-transitional-preserve (ruflo v42) / 58c rebrand-repo-keep-npm-package (omo v52) / 58d feature-deprecation (shannon v45). **Sub-variant 58e N=1 observational; stale-flag for v59.**

3. **Pattern #21 SDD Methodology Emergence UN-STALE candidate at next mini-audit** — currently STALE since v25 audit (registered v17 spec-kit + GSD v5 lineage at N=2 single-tier T1). gsd-2 v54 explicitly continues SDD framework. Cross-org N=4 if counted: GSD-1 v5 + spec-kit v17 + aidevops v47 (SDD elements) + gsd-2 v54. **Propose UN-STALE at next mini-audit; needs operator decision on whether aidevops counts.**

4. **Pattern #18 Agent Runtime Standardization NEW Layer observational sub-variant Pi-SDK-as-runtime-substrate** — gsd-2 vendors 4 pi-* packages = Pi SDK becoming cross-project runtime substrate. Pi SDK now consumed by 2 corpus wikis (pi-mono v36 = origin + gsd-2 v54 = downstream consumer). **Sub-variant Pi-SDK-substrate N=1 explicit dependency observation; sister to corpus-existing MCP universal layer.**

5. **Pattern #37 Crypto-Donation-Funded 2ND DATA POINT** — $GSD Solana token at gsd-2 (commercial framework with active development) joins system-prompts-leaks v21 (prompt-leak archive). **N=2 with mechanism divergence**: v21 = leak-archive-monetization-via-multi-channel-donations + Solana token; v54 = framework-monetization-via-token-attached-to-active-product. Different use-cases for token-at-OSS-scale. Strengthen Pattern #37 observation; do NOT promote (mechanism unclear).

6. **Pattern #17 variant 1 Ecosystem-Layer Organizations 19th+ data point** — gsd-build org has **8 public repos** (gsd-2 + get-shit-done + likely + others to verify). Multi-component architecture: gsd-2 monorepo itself contains daemon + mcp-server + studio Electron + 4 vendored pi-* + native Rust + rpc-client + 24 bundled extensions. **Strong variant 1 strengthening at org-level + project-level.**

7. **Pattern #19 archetype 2 methodology-lineage observation** — Pi SDK creator **Mario Zechner** (from pi-mono v36) becomes 5th individual-influence-node candidate via gsd-2's explicit Pi SDK dependency. Joins Karpathy + John Lam + Anthropic-team-cluster + Lance Martin. **However: Mario Zechner already corpus-known via pi-mono v36 wiki (he IS a wiki subject). N=2 corpus presence (pi-mono direct + gsd-2 dependency) but as wiki-subject not external-influence-node — different mechanism.** Document as observation; do NOT register standalone (consolidation-forward).

8. **Pattern #27 Community-Viral Scale Path strengthening** — 6,619 stars / 46 days = ~144 stars/day at cold-start with parent-product-amplification (GSD-1 viral driving GSD-2 adoption). **Cold-start-with-parent-amplification observational sub-path.** Distinct from prior Pattern #27 sub-paths (corporate-amplified / Korean-community-amplified / Pakistani-multi-channel / VN-diaspora-pedagogical / aggregator-amplified-commercial / etc.).

9. **Pattern #22 AGENTS.md negative observation** — gsd-2 has **NO AGENTS.md / NO CLAUDE.md at root** despite 24 bundled extensions + 35 skills + 13 agents + extensive workflow tooling. README documents AGENTS.md as a **user-facing config primitive** ("Place an `AGENTS.md` file in any directory to provide persistent behavioral guidance for that scope") but does not ship one for the gsd-2 repo itself. **Counter-evidence sub-observation: T1 agent-platforms can teach AGENTS.md without dogfooding it at root.** Pattern #22 22-absence sub-observation at T1.

10. **Pattern #2 Distribution Evolution** — npm `gsd-pi` (only npm name; bin = `gsd` / `gsd-cli` / `gsd-pi`) + Dockerfile + managed RTK binary integration + workspaces. 4-surface distribution (medium-narrow at T1; lighter than pi-mono v36's 11-platform binaries).

11. **Pattern #50 Commercial-Funnel Companion Platform observational** — gsd.build domain + Discord + GSD daemon + GSD Studio Electron app + mintlify-docs site = multi-component infrastructure. Whether commercial-cloud-tier emerges is unclear (no Pro tier observed in README). Document as observational watch; do NOT count as data point yet.

12. **Pattern #66 Supply-Chain Awareness OBSERVATION-TRACK strengthening** — gsd-2 forces `RTK_TELEMETRY_DISABLED=1` for managed RTK binary invocations + provides `GSD_RTK_DISABLED=1` opt-out. **Architectural-defense-by-design sub-variant** (Pattern #66 by-design sub-category, joins gh-aw v48 W3C-style spec). N=2 by-design data points now.

### REJECTIONS (consolidation-forward; NOT registered)

- **RTK-binary-managed-third-party** — observational only; route to Pattern #2 + Pattern #66 sub-observations (not new candidate)
- **Cross-corpus pi-SDK vendoring** — route to #57 + #18 strengthening (already covered above)
- **v2.78 aggressive minor versioning** — route to #27 within sub-observation (corporate-velocity at cold-start; not new pattern)
- **VISION.md as primary first-class governance** — observational at T1 (gsd-2 has VISION.md but spec-kit v17 + others have similar; not corpus-first)
- **Lex Christopherson vs TÂCHES identity question** — DO NOT register; it's a verification observation, not a pattern

### TARGET

- **0 new active candidates**
- **0 new OBSERVATION-TRACKs**
- **All findings → within-existing-pattern strengthening or sub-observations**
- **Extends 17-streak (v37-v53) to 18-streak (v37-v54) NEW LONGEST in corpus history**

## Phase 0.9 Storm Bear meta-entity check (per routine v2.1 per-wiki applicability)

**YES** — 37th consecutive Storm Bear meta-entity (v10-v54 unbroken streak preserved). Justification:
1. **SDD methodology directly relevant** to vault wiki-routine maintenance
2. **State-machine-from-disk pattern** (gsd-2 reads `.gsd/STATE.md` each loop iteration) is direct architectural template for vault routine v2.1 → v2.2 evolution
3. **Extension-first principle** (VISION.md verbatim "If it can be an extension, it should be") = direct vault skill-architecture lesson (currently 4 vault skills in `05 Skills/`; should new patterns become standalone skills vs CLAUDE.md additions?)
4. **Single-writer control plane** discipline = vault has single-writer assumption (operator + Claude) but no formal lock; gsd-2 v2.78 closes "single-writer-v3 control plane gaps" — relevant pattern reference
5. **Worktree forensics + telemetry + journal events** = potential vault iteration-log-v2 enhancement (currently iteration logs are narrative; gsd-2 emits structured events)

## Primitive-count flagging (v2.1 informal discipline)

**YELLOW** (~150-250 primitives across 8 packages + 24 extensions + 35 skills + 13 agents + ~50 commands + 4 ADRs + Studio + workflows + 8-doc dev guides). Compression strategy:
- 4-entity allocation (Core product / Architecture+Pi-SDK-vendoring / gsd-build ecosystem+GSD-1-successor / Storm Bear meta)
- Lossy compression accepted: per-extension details / per-skill enumeration / per-command flag listing → cite-not-replicate
- Studio Electron app + native Rust bindings cited briefly (not deep-dived)
- Velocity expectation: ~2h 30min within YELLOW +25-33% tolerance band

## Folder Structure

```
gsd-2 - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── 00 INDEX.md
├── 00 LOG.md
├── 00 OPEN-QUESTIONS.md
├── (C) Cluster 1 — README + VISION + positioning.md
├── (C) Cluster 2 — Architecture + 8-package monorepo + Pi-SDK vendoring.md
├── (C) Cluster 3 — Governance + extensions + commercial-funnel.md
├── (C) Entity 1 — gsd-2 Core Product.md
├── (C) Entity 2 — gsd-build Ecosystem + GSD-1 successor relationship.md
├── (C) Entity 3 — Lex Christopherson + Pi SDK cross-corpus connection.md
├── (C) Entity 4 — Storm Bear meta-entity (37th consecutive).md
├── (C) Beginner guide bilingual VN+EN.md
├── (C) Phase 4b — T1 N=15 + Pattern strengthening + cross-corpus + corpus-firsts.md
└── (C) Iteration log v54.md
```

## Key constraints

- **NEVER fabricate** — Lex Christopherson vs TÂCHES question handled honestly per repo evidence
- **(C) prefix** on AI-generated files
- **Bilingual VN+EN** beginner guide
- **⚠️ ethical framing** for $GSD Solana token + supply-chain awareness for managed RTK binary
- **Phase 6 MANDATORY** — vault root sync (CLAUDE.md state block + project entry + GOALS.md Session 65)

## Strategic flag

**v27 diagnostic HIGH bundle escalates to 34 SESSIONS DEFERRED** (v28-v54). 6.8× routine v2.1 5-session threshold. gsd-2's lack of root AGENTS.md is consistent with existing 4-template ensemble (22a-22d) — does NOT add new vault refactor template. Operator-facing vault work (item #1 vault CLAUDE.md refactor) remains overwhelmingly next-highest-ROI action.
