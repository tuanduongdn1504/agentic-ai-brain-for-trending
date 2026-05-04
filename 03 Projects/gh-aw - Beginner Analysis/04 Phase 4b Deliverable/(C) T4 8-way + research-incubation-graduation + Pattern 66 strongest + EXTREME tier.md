# (C) T4 8-way + research-incubation-graduation + Pattern #66 OT strongest data point + EXTREME-tier — gh-aw v48 Phase 4b deliverable

> **Wiki #48** | **2026-04-25** | Primary deliverable for v48 — extends T4 to N=8 with NEW T4i sub-archetype + introduces research-incubation-to-mainline-graduation lineage pathway + provides corpus-strongest defense-in-depth data point for Pattern #66 OT + 2nd EXTREME-tier primitive count after aidevops v47.

---

## Part 1 — T4 8-way taxonomy extension

### Pre-v48 T4 archetype variants (N=7)

| Variant | Wiki | Archetype | Scale | Year |
|---------|------|-----------|-------|------|
| T4a | gws v13 | Corporate-broad-official (Google Workspace) | 25K stars | 2025 |
| T4b | notebooklm-py v7 | Solo-narrow (NotebookLM Python API) | ~300 stars | 2024 |
| T4c | graphify v16 | Solo-broad-local (code → knowledge graph) | 30K stars | 2025 |
| T4d | TrendRadar v19 | Solo-broad-external-regional (CN news → AI-agent + push channels) | 52K stars | 2025 |
| T4e | markitdown v28 | Corporate-narrow-utility (Microsoft / AutoGen Team) | 114K stars | 2025 |
| T4f | crawl4ai v29 | Solo-enterprise-scale (web → LLM-friendly markdown) | 64K stars | 2024 |
| T4g | GitNexus v33 | Solo-student-with-commercial (PolyForm Noncommercial) | 28K stars | 2025 |
| T4h | claude-context v40 | Commercial-ecosystem-startup (Zilliz vector code-indexing) | 8.6K stars | 2025 |

### v48 T4 N=8 — gh-aw introduces NEW T4i sub-archetype

**T4i NEW: GitHub-corporate-official-workflow-compiler-for-CICD-bridge** (gh-aw v48)

**Archetype-defining traits:**
1. Corporate-official (github/* org direct ownership)
2. Workflow-compiler bridge function (markdown → executable CI/CD YAML)
3. CICD-execution-runtime (GitHub Actions as substrate)
4. Engine-selection-as-frontmatter axis (5+ engines: copilot/claude/codex/custom/extensible)
5. Research-incubation-graduated provenance (githubnext → github mainline at v0.40.1)

**Distinct from prior T4 archetype variants:**
- vs T4a gws (corporate-broad-Google-Workspace bridge to AI-agent harnesses): gh-aw's bridge function is markdown→CICD, not workspace-API-bridge
- vs T4b-d solo variants: gh-aw is corporate-official, not solo
- vs T4e markitdown (Microsoft narrow-utility file→markdown): gh-aw's bridge is markdown→executable-CI YAML, not file-format-conversion
- vs T4f crawl4ai (solo-enterprise-scale web→LLM-friendly): gh-aw is corporate-official-fully-OSS without commercial tier
- vs T4g GitNexus (solo-student-with-commercial PolyForm): gh-aw is fully MIT, no commercial gating
- vs T4h claude-context (commercial-ecosystem-startup): gh-aw is corporate-official non-commercial

### T4 corporate-official sub-archetype now N=3

| Variant | Parent | Scope |
|---------|--------|-------|
| T4a gws v13 | Google | Corporate-broad-Workspace-bridge |
| T4e markitdown v28 | Microsoft / AutoGen Team | Corporate-narrow-utility-file-converter |
| **T4i NEW gh-aw v48** | **GitHub (graduated from GitHub Next)** | **Corporate-official-workflow-compiler** |

= 3 corporate-official orgs (Microsoft + Google + GitHub) each with T4 entries. Pattern #17 variant 2a sub-distinction:
- Microsoft: 2a corporate-official-broad-platform (gws-equivalent style + AutoGen ecosystem)
- Google: 2a corporate-official-broad-platform (gws T4a) + 2b corporate-research-OSS (magika v44)
- **GitHub**: 2a corporate-official-broad-platform (spec-kit v17 T1 + gh-aw v48 T4) + research-graduated-from-GitHub-Next (NEW v48)

**Pattern #17 variant 2a sub-distinction sharpens at v48:**

| Sub-variant | Org | Wikis | N |
|-------------|-----|-------|---|
| 2a corporate-official-broad-platform-mainline | Microsoft, Google, GitHub | gws v13 + ai-agents-for-beginners v6 + markitdown v28 + spec-kit v17 + gh-aw v48 | 5 |
| 2b corporate-research-OSS | Google Research | magika v44 | 1 |
| 2c (NEW v48 candidate?) corporate-official-research-graduated-to-mainline | GitHub | gh-aw v48 | 1 |

**Decision: DO NOT register 2c sub-variant.** Per consolidation-forward discipline + Phase 0.6 overlap pre-check: gh-aw's research-graduation status is **strengthening-observation within 2a** at github-corporate-official tier, not new sub-variant. If 2nd research-graduated-corpus-entry observed (e.g., a future Microsoft Research → Microsoft mainline framework), then 2c sub-variant promotion-candidate can emerge.

## Part 2 — Research-incubation-to-mainline-graduation lineage pathway (Pattern #19 archetype 2 strengthening)

### gh-aw migration timeline (corpus-first)

```
2025-08-12 (8.5 months ago)
   │
   ├── githubnext/gh-aw repo created
   │   │
   │   ├── Authored under GitHub Next research org
   │   ├── 4-researcher-cluster CODEOWNERS: Don Syme + Eric Aftandilian + Peli de Halleux + Krzysztof Cieślak
   │   └── Iteration on agentic-workflow-compiler concept
   │
2026-02-03 (2.5 months ago)
   │
   ├── v0.40.1 release: Migration githubnext/gh-aw → github/gh-aw
   │   │
   │   ├── CHANGELOG: "Move from githubnext/gh-aw to github/gh-aw.
   │   │              If you were a former user of the githubnext Agentic Workflows
   │   │              you might have to re-register the extension to reflect the
   │   │              new location."
   │   │
   │   └── Sub-ecosystem coordinated: 3 companion repos (AWF + MCP Gateway + Actions library)
   │
2026-04-14 (11 days ago)
   │
   └── v0.68.3 latest release
       │
       └── ~28 versions since v0.40.1 graduation; active iteration cadence
```

### Significance for Pattern #19

**Pattern #19 archetype 2 methodology-lineage** has 5 distinct lineage-cluster types observable post-v48:

1. Karpathy-individual (autoresearch v10 + Storm Bear vault foundation + graphify v16 + rowboat v43 implicit)
2. John Lam-individual (spec-kit v17 cited)
3. Anthropic-team-cluster (claude-howto v32 + claude-code-best-practice v34 + aidevops v47)
4. Research-paper-chain (LlamaFactory v22 + DeepTutor v38 + magika v44)
5. **GitHub Next research-org-cluster** (NEW v48; gh-aw v48)

= 5-cluster-type taxonomy now structurally rich. Storm Bear corpus's pattern-detection methodology spans 5 distinct lineage-cluster archetypes.

### CODEOWNERS = the 4-researcher cluster

```text
# This repository is maintained by:
- @dsyme @eaftan @pelikhan @krzysztof-cieslak
```

| Maintainer | Identity | Notable role | Corpus presence |
|------------|----------|--------------|-----------------|
| @dsyme | **Don Syme** | F# language creator (originally Microsoft Research; joined GitHub Next) | **CORPUS-FIRST** |
| @eaftan | Eric Aftandilian | Engineering lead | CORPUS-FIRST |
| @pelikhan | **Peli de Halleux** | "Peli's Agent Factory" namesake; researcher | **CORPUS-FIRST** |
| @krzysztof-cieslak | **Krzysztof Cieślak** | Ionide (F# IDE for VS Code) creator | **CORPUS-FIRST** |

### Architectural significance of Don Syme + Krzysztof Cieślak presence

- **Don Syme** = original F# language creator. F# is functional-first with strong type system. His presence at gh-aw CODEOWNERS suggests serious-language-design DNA in the markdown-spec-compiler architecture.
- **Krzysztof Cieślak** = original Ionide author (F# language extension for VS Code). Reinforces F#/functional-design influence.

**Direct evidence:** `scratchpad/functional-patterns.md` engineering-decision-record exists in repo. Plausibly direct documentation of F#-influenced code-organization philosophy applied to Go.

### Comparison to Anthropic-team-cluster lineage (claude-howto v32 + v34 + v47)

| Cluster | Members | Org | First citation wiki | Subsequent strengthening wikis |
|---------|---------|-----|---------------------|-------------------------------|
| Anthropic-team-cluster | Boris Cherny + Dex Horthy + Cat Wu (+ Lance Martin LangChain at v47) | Anthropic | claude-howto v32 | claude-code-best-practice v34 + aidevops v47 |
| **GitHub Next research-org-cluster** | **Don Syme + Eric Aftandilian + Peli de Halleux + Krzysztof Cieślak** | **GitHub Next → github mainline** | **gh-aw v48** | **Awaits 2nd corpus entry from this cluster** |

**Pattern #19 archetype 2 strengthening at v48:** 2nd named-research-cluster lineage-type (parallel to Anthropic-team-cluster). Cluster-as-lineage-node is now N=2 distinct cluster-types (counting both Anthropic-team-cluster + GitHub Next research-org-cluster as separate cluster-type observations).

## Part 3 — Pattern #66 OT MAJOR STRENGTHENING — corpus-strongest defense-in-depth data point

### Pre-v48 Pattern #66 OT state

Pattern #66 was registered at v29 crawl4ai as **Supply-Chain Security Incident Response** observation (post-`unclecode-litellm` fork response framing). At v29 audit it was reclassified as OBSERVATION-TRACK (event-based, not architectural-pattern).

**At v48 close: Pattern #66 OT has 1 observation only (crawl4ai v29).** gh-aw v48 introduces structurally-distinct observation.

### gh-aw v48 introduces architectural-defense-by-design observation

**Defense-in-depth observable elements at gh-aw:**

| Element | Detail |
|---------|--------|
| **W3C-style formal Security Architecture Specification** | `specs/security-architecture-spec.md` v1.0.0 Candidate Recommendation, 2026-01-29 |
| **130+ formal RFC 2119 requirements** | MUST / SHALL / SHOULD / MAY |
| **70+ compliance tests across 8 categories** | T-IS / T-OI / T-NI / T-PM / T-SI / T-TD / T-CS / T-RS |
| **3 conformance classes** | Basic (Level 1) / Standard (Level 2) / Complete (Level 3) |
| **7-layer defense-in-depth architecture** | Layer 0 Compilation-Time Validation → Layer 6 Threat Detection |
| **7 numbered Security Guarantees** | SG-01 through SG-07 |
| **SBOM dual-format auto-generation** | SPDX + CycloneDX per release; via syft tool |
| **AWF (Agent Workflow Firewall)** | Companion repo for network egress control |
| **MCP Gateway** | Companion repo for unified MCP routing |
| **gh-aw-actions** | Shared library of SHA-pinned Actions |
| **Compile-time validation (Layer 0)** | Schema + expressions + permissions + actions validated before execution |
| **`.architecture.yml` thresholds** | File-line BLOCKER (2000) + WARNING (1000) + function-line + max-exports |
| **zizmor security linter** | Trail-of-Bits Actions linter integrated |
| **actionlint** | Standard Actions linter integrated |

### Comparison to crawl4ai v29 Pattern #66 inaugural observation

| Dimension | crawl4ai v29 (event-based) | gh-aw v48 (architectural-defense-by-design) |
|-----------|---------------------------|--------------------------------------------|
| Trigger | Reactive: post-`unclecode-litellm` fork response | Proactive: by-design at v1.0.0 spec |
| Scope | Single supply-chain incident response | Multi-layer architectural framework |
| Formality | Event log + fork action | W3C-style spec + 130+ MUST requirements |
| Companion infrastructure | None | 3 companion repos (AWF + MCP Gateway + Actions) |
| Compliance testing | Implicit | 70+ explicit compliance tests across 8 categories |
| Conformance levels | Implicit | 3 explicit classes (Basic / Standard / Complete) |
| Architectural distinction | Reactive | Proactive |

**These are structurally distinct sub-types within Pattern #66 OT scope.**

### Recommended Pattern Library audit decision (NEXT mini-audit)

**Option A:** Pattern #66 OT splits into 2 distinct OTs:
- #66a Event-based-incident-response (crawl4ai v29 inaugural; N=1)
- #66b Architectural-defense-by-design (gh-aw v48 inaugural; N=1)

**Option B:** Pattern #66 OT broadens scope to include both event-based + by-design framings; retains umbrella.

**Option C (RECOMMENDED):** Pattern #66 OT sub-divides into 2 sub-observations within umbrella, awaits N=3+ in either bucket before promotion to architectural pattern.

**Rationale for Option C:** gh-aw is unique-enough at corporate-official tier that its observation deserves explicit sub-categorization, but premature to fork into 2 separate OTs at single observation each. Within-OT sub-categorization preserves data and permits future consolidation.

### Pattern #66 OT scope-review framework for next mini-audit

```
Pattern #66 — Supply-Chain Security
├── Sub-observation A: Event-based-incident-response
│   └── crawl4ai v29 (post-unclecode-litellm-fork response)
└── Sub-observation B: Architectural-defense-by-design
    └── gh-aw v48 (W3C-style spec + 7-layer defense-in-depth + 4-repo decomposition)
```

If 2nd observation in either sub-bucket arrives, sub-bucket can promote to OT-distinct or remain unified.

## Part 4 — Pattern #18 Layer 0 — MCP Gateway as horizontal-aggregation observation

### Background: Pattern #18 layer formulation post-v47

Pattern #18 Agent Runtime Standardization has 8 refinements as of v47, including:
- **Layer 1 MCP universal** (Claude Code / Cursor / OpenClaw / Hermes / Codex / etc.)
- **Layer 2 OpenClaw + Hermes community-platform-scoped** (Western community standard)
- **Layer 3 per-runtime-specific**

**ollama v46 introduced Layer 0 runtime-bundled-launcher observation** (`ollama launch <runtime>` 33-file cmd/launch/ subsystem; 1 ollama binary launches 10+ agent runtimes — vertical aggregation).

### gh-aw v48 introduces 2nd Layer 0 observation

**MCP Gateway (`gh-aw-mcpg`)** = Layer 0 unified-routing-infrastructure for MCP servers. Routes MCP server calls through unified HTTP gateway for centralized access management. **Horizontal aggregation** (1 gateway routes calls to many MCP servers).

### Layer 0 sub-type taxonomy candidate

| Sub-type | Wiki | Mechanism | N |
|----------|------|-----------|---|
| **Layer 0a runtime-bundled-launcher** (vertical aggregation) | ollama v46 | 1 binary launches multiple agent runtimes | 1 |
| **Layer 0b unified-routing-gateway** (horizontal aggregation) | gh-aw v48 (gh-aw-mcpg) | 1 gateway routes calls to multiple MCP servers | 1 |

= structural-N=2 across 2 distinct sub-types (analogous to Pattern #17 variant sub-distinctions).

### Decision: DO NOT register Layer 0 sub-types as new active candidates at v48

Per consolidation-forward discipline + Phase 0.6 overlap pre-check at v48: Layer 0 sub-types are **strengthening-observation within Pattern #18** scope. If 2nd vertical-aggregation OR 2nd horizontal-aggregation observation arrives, sub-type promotion-candidate emerges.

**At next mini-audit:** Pattern #18 4-layer formal-statement-update proposal:
- Layer 0a runtime-bundled-launcher (ollama v46 N=1)
- Layer 0b unified-routing-gateway (gh-aw v48 N=1)
- Layer 1 MCP universal (12+ wikis)
- Layer 2 OpenClaw + Hermes community-platform (multiple wikis)
- Layer 3 per-runtime-specific (multiple wikis)

= 8th refinement of Pattern #18 (most-refined pattern in library at v47; v48 holds at 8 refinements with sub-observation rather than new refinement).

## Part 5 — Pattern #22 AGENTS.md sub-variant counter-evidence

### Pre-v48 sub-variant landscape

| Sub-variant | Source wiki | Description |
|-------------|-------------|-------------|
| (Generic) AGENTS.md present at root, often with CLAUDE.md alias | Multiple | Standard convention |
| 22a comprehensive-large at T1 tutorial (209-line) | claude-howto v32 | T1 tutorial-companion |
| (no-AGENTS.md observation) at T1 solo | claude-code-best-practice v34 | Counter-evidence to "T1 always uses AGENTS.md" |
| **22c authoritative-with-shim** | aidevops v47 | AGENTS.md primary + CLAUDE.md/AGENT.md redirect-shims (3-layer hierarchy: shims + root + nested) |

### gh-aw v48 introduces counter-evidence to 22c

**gh-aw at github-corporate-official tier:**
- AGENTS.md 49.8 KB at root (CORPUS-LARGEST)
- **NO CLAUDE.md at root** (no shim)
- **NO AGENT.md at root** (no shim)
- **PURE AGENTS.md-only** convention

= **Counter-evidence narrowing 22c authoritative-with-shim to solo-multi-runtime-platform scope.**

### Refinement framing for next mini-audit

**Pattern #22 sub-variants post-v48 counter-evidence:**

- (Generic AGENTS.md present) — multiple wikis
- (AGENTS.md absent at T1 solo) — counter-evidence (claude-code-best-practice v34)
- 22c authoritative-with-shim → **NARROWED scope: solo-multi-runtime-platform pattern** (aidevops v47 inaugural)
- (NEW) AGENTS.md-only at corporate-official tier — convention observed (spec-kit v17 + gh-aw v48; N=2 corpus consistency)

**Decision: DO NOT register new sub-variant at v48.** Strengthen 22c by narrowing scope at next mini-audit. Consolidation-forward discipline.

## Part 6 — Pattern #69 Agent-PR Fast-Track inverse observation

### Pre-v48 Pattern #69

- 69a `🤖🤖🤖` contributor opt-in (awesome-mcp-servers v31 inaugural)
- 69b `lgtm`/`lgtmi` maintainer-approval (pi-mono v36 inaugural)

### gh-aw v48 inverse observation

**CONTRIBUTING.md verbatim:**
> *"🚫 Traditional Pull Requests Are Not Enabled for non-Core team members: If you are not part of the core team, please do not create pull requests directly. Instead, you create detailed agentic plans in issues, discuss with the team, and a core team member will create and implement the PR for you using agents."*

= Inverse-protocol: non-core PRs **rejected by default**, agentic-plans-in-issues channel community contribution. Core team executes plans via Copilot agent or local agents. Contributors credited in README community-contribution attribution section (which is why README is 86% attribution by line count = ~860 of 988 lines).

### Pattern #69 enrichment (within-pattern observation)

Pattern #69 sub-variants now span "contribution-pathway-friction-axis":
- **Low-friction fast-track** (69a opt-in `🤖🤖🤖`; 69b approval `lgtm`/`lgtmi`)
- **High-friction plan-only** (gh-aw v48 inverse: non-core PR block + agentic-plan-in-issue convention)

Within-pattern observation; sub-classification opportunity at next mini-audit. **DO NOT register new sub-variant at v48.**

## Part 7 — EXTREME-tier primitive count (2nd in corpus after aidevops v47)

### Probe results

- **Total Go files:** 1,805 (1,789 in `pkg/` + cmd/ + internal/ + actions/)
- **Total markdown files:** 1,224 (.md across repo)
- **Skill subdirs:** 24 (`skills/`)
- **pkg/ subdirs:** 22
- **Workflow files:** 201 paired (.md + .lock.yml)
- **Scratchpad notes:** 63 engineering-decision-records
- **Docs files:** 22 (`docs/`)
- **Specs files:** 3 (`specs/`)
- **Governance files at root:** 12+ (LICENSE / README / AGENTS / CONTRIBUTING / DEVGUIDE / SECURITY / SUPPORT / DEADCODE / SKILL / CHANGELOG / CODEOWNERS / CODE_OF_CONDUCT / `.architecture.yml`)

**Total primitive count: ~3,200+** (1,805 .go + 1,224 .md + supporting directories).

### EXTREME-tier comparison

| Wiki | Primitive count | Tier |
|------|-----------------|------|
| ECC v1 | ~7-8 (compressed across 7 separate wiki pages — corpus outlier) | EXTREME (retroactive) |
| Most wikis v6-v34 | <50 | GREEN |
| pi-mono v36 | ~150-200 | YELLOW |
| bizos v37 | ~150-180 | YELLOW |
| DeepTutor v38 | ~120-150 | YELLOW |
| shannon v45 | ~120-150 | YELLOW |
| browser-use v41 | ~200+ | RED (1st RED) |
| ollama v46 | ~250-400 | RED (2nd RED) |
| ruflo v42 | ~500+ | EXTREME (1st EXTREME) |
| **aidevops v47** | **~2,665+** | **EXTREME (2nd EXTREME, expanded)** |
| **gh-aw v48** | **~3,200+** | **EXTREME (3rd EXTREME, NEW CORPUS-RECORD)** |

### Compression strategy applied

4-entity allocation preserved via aggressive citation-not-replication:
1. **Core product entity** — gh-aw CLI + 5-engine support (cites README/AGENTS.md)
2. **Companion ecosystem entity** — 4-repo sub-ecosystem + GitHub Next research-cluster lineage (cites companion repo docs)
3. **Pattern implications entity** — T4 8-way + Pattern #66 strongest + EXTREME tier (cites Pattern Library)
4. **Storm Bear meta entity** — 37th consecutive (cites prior meta entities + vault state)

**5 follow-up deep-dive wikis flagged for routine v2.2:**
- gh-aw — Engine Architecture Deep Dive (5-engine support)
- gh-aw — Skills System Deep Dive (24 specialized skill subdirs)
- gh-aw — Security Architecture Spec Deep Dive (W3C-style 130+ requirements)
- gh-aw — Companion Ecosystem Deep Dive (AWF + MCP Gateway + Actions library)
- gh-aw — Workflow Catalog Deep Dive (201 paired .md/.lock.yml workflows)

### Velocity expectation

EXTREME tier ~3-3.5h (per aidevops v47 precedent).

## Part 8 — 9 corpus-firsts at corporate-official tier

1. **Markdown-as-source-truth-compiled-to-CI** at corporate-official tier
2. **5-engine first-class frontmatter selection** (copilot/claude/codex/custom + ext)
3. **Track-the-compiled-output `.lock.yml` convention** (mandate; never .gitignored)
4. **W3C-style formal Security Architecture Specification** (130+ MUST/SHOULD; 70+ tests; 3 conformance classes)
5. **MCP Gateway as unified routing infrastructure** (Pattern #18 Layer 0 horizontal-aggregation observation)
6. **AWF (Agent Workflow Firewall) network egress control** at corporate-official tier
7. **24-skill engineering-domain-focused library** at corporate-official tier (each skill = engineering surface)
8. **Daily skill-optimizer self-improvement workflow** at corporate-official tier (`.skill-optimizer/`)
9. **Architectural-threshold manifest at root** (`.architecture.yml` file-line/function-line/export-count)

## Part 9 — Pattern Library impact summary at v48 close

### Strengthenings (8+ patterns):

| Pattern | Strengthening |
|---------|---------------|
| #2 Distribution Evolution | 3-surface install (gh ext + curl + brew); `.lock.yml` track-compiled-output convention |
| #12 Governance-Depth refined v42 3-factor | 5th counter-evidence to "solo→light" — corporate + heavy 12+ files |
| #17 variant 2a corporate-official | github org now 2-corpus-entry spanning T1+T4 + 4-repo sub-ecosystem coordinated under single parent |
| #18 Layer 0 | N=1 horizontal-aggregation observation (MCP Gateway); pairs with ollama v46 vertical-aggregation Layer 0 N=1 |
| #19 archetype 2 methodology-lineage | research-incubation-graduated-to-mainline pathway corpus-first; GitHub Next 4-researcher cluster as 5th lineage-cluster-type |
| #22 AGENTS.md | counter-evidence narrowing 22c sub-variant scope to solo-multi-runtime-platform |
| #28 Multi-Provider | engine-selection-as-frontmatter-axis sub-observation |
| #66 OT Supply-Chain | MAJOR — corpus-strongest architectural-defense-by-design data point at corporate-official tier |
| #69 Agent-PR Fast-Track | inverse-observation (non-core PR block + agentic-plan-in-issue convention) |

### New active candidates: 0

(Target met: **12-CONSECUTIVE-WIKI ZERO-REGISTRATION STREAK v37-v48 — NEW LONGEST in corpus history**, extends v47 11-streak.)

### New OBSERVATION-TRACKs: 0

### Pattern Library state preserved

- Pre-v48: 37 confirmed + 19 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active. Ratio **19:37 = 0.513:1**.
- Post-v48: **37 confirmed + 19 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active. Ratio 19:37 = 0.513:1 PRESERVED 12TH CONSECUTIVE CYCLE.**
- 0.437 buffer below 0.95:1 mini-audit trigger preserved (largest in corpus history maintained).

## Part 10 — Strategic implications + recommendations

### Audit-decision options for next mini-audit

**Option 1 (RECOMMENDED minimum scope):** Apply Pattern #66 OT sub-categorization (event-based vs by-design within umbrella) per Part 3 Option C.

**Option 2 (medium scope):** + Pattern #18 4-layer formal-statement-update with Layer 0 sub-types (a vertical-aggregation + b horizontal-aggregation).

**Option 3 (broader scope):** + Pattern #22 22c sub-variant scope-narrowing (solo-multi-runtime-platform-specific) + Pattern #19 archetype 2 5-cluster-type taxonomy formalization.

### Storm Bear vault implications

**v27 diagnostic HIGH bundle BLOCKING-RECOMMENDATION ESCALATED to 28 SESSIONS DEFERRED** at v48.

gh-aw provides **3rd corpus reference template** for vault CLAUDE.md refactor (item #1 of v27 HIGH bundle):
- spec-kit v17 — corporate-official methodology framework reference
- aidevops v47 22c — solo-multi-runtime authoritative-with-shim reference
- **gh-aw v48** — corporate-official AGENTS.md-only at corpus-largest scale (49.8 KB)

3 templates available; STRONGLY RECOMMENDED execute v27 HIGH bundle before v49 (~6-8h investment + 3 reference templates). Hybrid alternative: 30-min mini-audit at v48 (Pattern #66 + #18) followed by v27 HIGH bundle (~7-9h total).

### Pilot ranking unchanged at v48

Top-11 unchanged. gh-aw is **NOT in top-11** (domain mismatch + security-binding deployment friction).

Top-11 Storm Bear pilot ranking post-v48:
1. claude-hud v35 (5-min install + 1-week eval)
2. claude-howto v32 (self-onboarding meta-ROI)
3. spec-kit v17 (methodology reference)
4. browser-use v41 (Jira/Linear scraping)
5. pi-mono v36 (Claude Code alternative + multi-provider escape)
6. claude-context v40 (vault semantic-search direct pilot)
7. OMC v27 (multi-runtime orchestration)
8. aidevops v47 (AGENTS.md + 8-tool quality stack templates)
9. claude-code-best-practice v34 (82-tip aggregation)
10. markitdown v28 (Scrum doc ingestion)
11. crawl4ai v29 (web research)

## Cross-references

- `(C) E1 — gh-aw core product.md` — core product entity
- `(C) E2 — Companion ecosystem + GitHub Next research lineage.md` — companion ecosystem entity
- `(C) E3 — Pattern implications + T4 8-way + Pattern 66 strongest.md` — pattern implications entity
- `(C) E4 — Storm Bear meta 37th consecutive.md` — Storm Bear meta entity
- `01 Cluster Summaries/(C) C1-C3.md` — cluster summaries

**Sister wiki cross-references:**
- spec-kit v17 (sister github/* corpus T1 entry)
- aidevops v47 (recent EXTREME-tier comparison + 22c counter-evidence)
- ollama v46 (Pattern #18 Layer 0 vertical-aggregation precedent; gh-aw introduces horizontal-aggregation Layer 0)
- crawl4ai v29 (Pattern #66 OT inaugural event-based; gh-aw introduces by-design distinction)
- claude-howto v32 + claude-code-best-practice v34 + aidevops v47 (Anthropic-team-cluster precedent for 4-researcher GitHub Next cluster parallel)

## Status

**v48 wiki complete. 9th v2.1-era routine execution — all 5 discipline mechanisms exercised cleanly.** 12-CONSECUTIVE-WIKI ZERO-NEW-CANDIDATES STREAK extended (v37-v48 — NEW LONGEST in corpus history). Pattern Library ratio preserved at 19:37 = 0.513:1 (12th consecutive cycle). EXTREME-tier primitive count NEW CORPUS-RECORD (~3,200+). 37th consecutive Storm Bear meta-entity preserved.
