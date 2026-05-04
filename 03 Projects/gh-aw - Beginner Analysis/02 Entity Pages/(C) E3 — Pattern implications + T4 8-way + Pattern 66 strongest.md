# (C) Entity 3 — Pattern implications + T4 8-way + Pattern #66 OT strongest data point

> **Wiki #48** | **2026-04-25** | gh-aw extends T4 to N=8 with NEW T4i sub-archetype + provides corpus-strongest defense-in-depth data point for Pattern #66 OT + introduces research-incubation-to-mainline-graduation lineage pathway.

## 1. T4 Agent-as-bridge — 8 archetype variants now occupied

T4 is corpus's 2nd-largest tier (after T1 N=14). With gh-aw v48, T4 reaches N=8 with 8 distinct archetype variants:

| Variant | Wiki | Archetype | Tier-distinct trait |
|---------|------|-----------|--------------------|
| T4a | gws v13 | Corporate-broad-official (Google Workspace) | Bridge to AI-agent harnesses; broad utility |
| T4b | notebooklm-py v7 | Solo-narrow (NotebookLM-API) | Single-product narrow-bridge |
| T4c | graphify v16 | Solo-broad-local (code → knowledge graph) | Local-runtime knowledge-graph bridge |
| T4d | TrendRadar v19 | Solo-broad-external (CN news → AI + push channels) | Multi-region multi-channel bridge |
| T4e | markitdown v28 | Corporate-narrow-utility (Microsoft) | Single-purpose file→markdown utility |
| T4f | crawl4ai v29 | Solo-enterprise-scale (web → LLM-friendly markdown) | Solo at enterprise scale; OSS-anti-bot |
| T4g | GitNexus v33 | Solo-student-with-commercial (PolyForm) | Commercial tier with PolyForm Noncommercial |
| T4h | claude-context v40 | Commercial-ecosystem-startup (Zilliz) | Vector code-indexing + commercial SaaS funnel |
| **T4i NEW** | **gh-aw v48** | **GitHub-corporate-official-workflow-compiler** | **Markdown → CI YAML compilation pipeline** |

**Sub-archetype 2 corporate-official-at-T4 strengthening:** Now N=3 at T4 (gws v13 + markitdown v28 + gh-aw v48). Microsoft (T3+T4) + Google (T4) + GitHub (T1+T4) = 3 corporate-official orgs each spanning multiple tiers.

**Pattern #17 variant 2a sub-distinction sharpens at v48:**
- Microsoft = corporate-official-broad-platform (gws-equivalent style + AutoGen ecosystem)
- Google = corporate-official-broad-platform + corporate-research-OSS (per v45 mini-audit 2a/2b sub-distinction)
- GitHub = corporate-official-broad-platform (spec-kit T1 + gh-aw T4) + research-graduated-from-GitHub-Next (NEW v48)

**Counter-evidence to "corporate-official tier products are always single-product"**: GitHub now demonstrates 2-corpus-entry pattern with distinct tiers + companion sub-ecosystems.

## 2. Pattern #66 OT — gh-aw as corpus-strongest defense-in-depth data point

### Why this matters

Pattern #66 was registered at v29 crawl4ai as event-based-incident-response observation (post-supply-chain-incident response framing). At v29 audit it was reclassified as OBSERVATION-TRACK (event-based, not architectural-pattern).

**gh-aw v48 introduces structural-distinct observation: ARCHITECTURAL-DEFENSE-BY-DESIGN at corporate-official tier.**

### Observable defense-in-depth elements at gh-aw

| Element | Pattern #66 OT relevance |
|---------|--------------------------|
| W3C-style formal Security Architecture Specification (`specs/security-architecture-spec.md`, v1.0.0) | Most-formalized security spec in corpus |
| 7-layer defense-in-depth architecture (Layers 0-6) | Most-explicit layered architecture in corpus |
| 7 numbered Security Guarantees (SG-01 through SG-07) | First numbered-guarantee taxonomy in corpus |
| 130+ formal RFC 2119 requirements (MUST/SHALL/SHOULD/MAY) | Most-formalized requirements in corpus |
| 70+ compliance tests across 8 categories | Most-tested security-conformance in corpus |
| 3 conformance classes (Basic/Standard/Complete) | First conformance-class taxonomy in corpus |
| SBOM (SPDX + CycloneDX) auto-generation per release | First dual-SBOM-format corpus observation |
| AWF (Agent Workflow Firewall) companion repo for network egress | Companion-repo defense-in-depth-distribution |
| MCP Gateway companion repo for unified MCP routing | Layer 0 unified access management infrastructure |
| Compile-time validation (Layer 0) | Schema + expressions + permissions + actions validated before execution |
| SHA-pinned dependencies | Standard supply-chain hardening |
| Sandboxed execution + network isolation + input sanitization | All 3 explicit in user-facing README docs |
| Tool allow-listing + human approval gates | User-controllable safety boundaries |
| zizmor security linter integration | Modern Trail-of-Bits Actions linter |
| actionlint integration | Standard Actions linter |
| `.architecture.yml` file-line/function-line/export-count thresholds | Architectural-degradation detection |

### Pattern #66 OT scope-review opportunity at next audit

gh-aw observation introduces **architectural-defense-by-design at corporate-official tier** structurally distinct from crawl4ai's **event-based-incident-response observation**.

**Audit-decision option for next mini-audit:**
- **Option A:** Pattern #66 OT splits into 2 distinct OTs:
  - "#66a Event-based-incident-response (crawl4ai v29 inaugural)" — N=1 OT
  - "#66b Architectural-defense-by-design (gh-aw v48 inaugural)" — N=1 OT
- **Option B:** Pattern #66 OT broadens scope to include both event-based + by-design, retains umbrella framing.
- **Option C:** Pattern #66 OT sub-divides into N=2 sub-observation taxonomy, awaits N=3+ in either bucket before promotion.

**Recommendation:** Option C (sub-divide into 2 sub-observations within OT umbrella, await further data points). gh-aw is unique enough that its observation deserves explicit sub-categorization, but premature to fork into 2 separate OTs at single observation each.

### Pattern Library accommodation note

This is **NOT a new active candidate** registration. Per consolidation-forward discipline + Phase 0.6 overlap pre-check at v48: gh-aw observation strengthens existing Pattern #66 OT, with sub-categorization opportunity flagged for next mini-audit.

## 3. Pattern #18 Layer 0 — MCP Gateway as unified routing infrastructure

### Background

Pattern #18 Agent Runtime Standardization has 8 refinements as of v47, including 3-layer formulation:
- Layer 1 MCP universal (Claude Code / Cursor / OpenClaw / Hermes / Codex / etc.)
- Layer 2 OpenClaw + Hermes community-platform-scoped (Western community standard)
- Layer 3 per-runtime-specific
- Plus 8th refinement runtime-primacy-choice sub-observation (v47 aidevops)

ollama v46 introduced **Layer 0 runtime-bundled-launcher observation** (`ollama launch <runtime>` 33-file cmd/launch/ subsystem).

### gh-aw v48 introduces 2nd Layer 0 observation

**MCP Gateway (`gh-aw-mcpg`)** = Layer 0 unified-routing-infrastructure for MCP servers. Routes MCP server calls through a unified HTTP gateway for centralized access management.

**Structural similarity + difference vs ollama Layer 0:**
- **ollama v46**: Layer 0 = runtime-bundled-launcher (1 ollama binary launches 10+ agent runtimes; vertical integration)
- **gh-aw v48**: Layer 0 = unified-routing-gateway (1 gh-aw-mcpg gateway routes calls to many MCP servers; horizontal aggregation)

Both are **Layer 0** in the sense of "below per-runtime layer", but architecturally distinct: vertical (ollama) vs horizontal (gh-aw).

### Promotion proposal at next mini-audit

If Pattern #18 4th-layer-formalization is proposed, the formulation could be:
- **Layer 0a runtime-bundled-launcher** (ollama N=1) — vertical aggregation
- **Layer 0b unified-routing-gateway** (gh-aw-mcpg N=1) — horizontal aggregation

= structural-N=2 across 2 distinct sub-types (analogous to Pattern #17 variant sub-distinctions). **Defer to next mini-audit per consolidation-forward discipline at v48.**

## 4. Research-incubation-to-mainline-graduation pathway (Pattern #19 archetype 2 strengthening)

### gh-aw migration timeline (corpus-first observation)

```text
2025-08-12 → githubnext/gh-aw repo created (research project under github research org)
   ↓ ~6 months as research project
2026-02-03 → v0.40.1 — repo migrates from githubnext/gh-aw to github/gh-aw (mainline graduation)
   ↓ ~2.5 months mature in mainline
2026-04-14 → v0.68.3 latest release
2026-04-25 → Storm Bear v48 wiki snapshot
```

### Pattern #19 archetype 2 strengthening

archetype 2 = methodology-lineage. gh-aw introduces **research-org-incubation-graduated-to-mainline** as observable origin pathway sub-type. Distinct from:
- Methodology-cited-as-influence (e.g., John Lam at spec-kit v17)
- Methodology-shared-across-frameworks (e.g., SDD spec-kit + GSD)
- Methodology-as-research-paper-chain (e.g., LlamaFactory v22 ACL 2024)

**4-research-cluster CODEOWNERS** (Don Syme + Eric Aftandilian + Peli de Halleux + Krzysztof Cieślak) is structurally similar to Anthropic-team-cluster (Boris Cherny + Dex Horthy + Cat Wu observed across claude-howto v32 + claude-code-best-practice v34 + aidevops v47): a coordinated team-cluster lineage rather than single-individual-author-lineage.

### 5-cluster-type lineage taxonomy as of v48

| Cluster type | Wiki count | Members (single or cluster) |
|--------------|------------|------------------------------|
| Karpathy-individual | 4 (autoresearch v10 + Storm Bear vault foundation + graphify v16 + rowboat v43 implicit) | Andrej Karpathy |
| John Lam-individual | 1 (spec-kit v17) | John Lam |
| Anthropic-team-cluster | 3 (claude-howto v32 + claude-code-best-practice v34 + aidevops v47) | Boris Cherny + Dex Horthy + Cat Wu (+ Lance Martin LangChain at v47) |
| Research-paper-chain | 3+ (LlamaFactory v22 + DeepTutor v38 + magika v44) | Multi-paper-citation networks |
| **GitHub Next research-org-cluster (NEW v48)** | 1 (gh-aw v48) | Don Syme + Eric Aftandilian + Peli de Halleux + Krzysztof Cieślak |

= 5-cluster-type lineage taxonomy now observable across corpus. Pattern #19 archetype 2 is structurally rich.

## 5. Pattern #22 AGENTS.md sub-variant counter-evidence

### Pre-v48 Pattern #22 sub-variants

- (Generic) AGENTS.md present at root, often with CLAUDE.md alias
- (claude-howto v32) Comprehensive 209-line AGENTS.md companion to T1 tutorial
- (claude-code-best-practice v34) AGENTS.md absent at T1 solo (counter-evidence to "T1 always uses AGENTS.md")
- **(aidevops v47) Sub-variant 22c authoritative-with-shim** — AGENTS.md primary + CLAUDE.md/AGENT.md redirect-shims (3-layer hierarchy: shims + root + nested)

### gh-aw v48 introduces counter-evidence to 22c

**gh-aw at github-corporate-official tier:**
- **AGENTS.md 49.8 KB at root (CORPUS-LARGEST)**
- **NO CLAUDE.md at root** (no shim)
- **NO AGENT.md at root** (no shim)
- **PURE AGENTS.md-only** convention

= **counter-evidence narrowing 22c authoritative-with-shim to solo-multi-runtime-platform scope**. At github-corporate-official tier the convention is **AGENTS.md-only** (spec-kit v17 + gh-aw v48 both pure AGENTS.md-only).

### Counter-evidence framing

- aidevops v47 22c sub-variant = solo-multi-runtime-platform pattern (Marcus Quinn targeting OpenCode + Claude + Codex + Gemini multi-runtime; needs shims because users may have any runtime)
- gh-aw v48 = github-corporate-official-multi-engine pattern (engine selection in workflow frontmatter, not in agent-runtime; one workflow, one engine; AGENTS.md targets gh-aw-developer agents, not multi-runtime users)

**Pattern Library implication:** 22c is narrower than originally proposed at v47. Its scope is "frameworks targeting multi-runtime ecosystems" not "frameworks where AGENTS.md is authoritative". gh-aw's AGENTS.md is authoritative but doesn't need shims because gh-aw is single-runtime-from-developer-perspective (you develop gh-aw on github.com using Copilot agent).

## 6. Pattern #69 Agent-PR Fast-Track Governance — inverse observation

### Pre-v48 Pattern #69

- Sub-variant 69a `🤖🤖🤖` contributor opt-in (awesome-mcp-servers v31)
- Sub-variant 69b `lgtm`/`lgtmi` maintainer-approval (pi-mono v36)

### gh-aw v48 inverse observation

**CONTRIBUTING.md verbatim:**
> *"🚫 Traditional Pull Requests Are Not Enabled for non-Core team members: If you are not part of the core team, please do not create pull requests directly. Instead, you create detailed agentic plans in issues..."*

= inverse-protocol: non-core PRs **rejected by default**, agentic-plans-in-issues channel community contribution. Core team executes plans via Copilot agent or local agents. Contributors credited in README community-contribution attribution section (which is why README is 86% attribution by line count).

### Pattern #69 enrichment (within-pattern observation, not new candidate)

Pattern #69 sub-variants now span:
- **Fast-track allow** (69a opt-in `🤖🤖🤖` / 69b approval `lgtm`/`lgtmi`)
- **Fast-track block** (gh-aw inverse: non-core PR block + agentic-plan-in-issue convention)

These are 3 points on a "contribution-pathway-friction-axis", spanning low-friction-fast-track to high-friction-plan-only. Within-pattern observation; sub-classification opportunity at next mini-audit.

## 7. Pattern Library impact summary at v48 close

### Strengthenings (8+ patterns):

| Pattern | Strengthening |
|---------|---------------|
| #2 Distribution Evolution | 3-surface install (gh ext + curl + brew) + `.lock.yml` track-compiled-output convention |
| #12 Governance-Depth refined v42 3-factor | 5th counter-evidence to "solo→light" — corporate + heavy 12+ files |
| #17 variant 2a corporate-official | github-org now has 2 entries spanning T1+T4 + 4-repo sub-ecosystem coordinated under single parent |
| #18 Layer 0 | N=1 observation (MCP Gateway as horizontal-aggregation unified-routing-gateway; companion to ollama v46 vertical-aggregation runtime-bundled-launcher) |
| #19 archetype 2 methodology-lineage | NEW research-org-incubation-graduated-to-mainline pathway observable + 5th cluster-type GitHub Next |
| #22 AGENTS.md | counter-evidence narrowing 22c sub-variant scope (gh-aw at corporate-official tier = AGENTS.md-only, no shims) |
| #28 Multi-Provider | engine-selection-as-frontmatter-axis sub-observation |
| #66 OT Supply-Chain | MAJOR — corpus-strongest architectural-defense-by-design data point at corporate-official tier |
| #69 Agent-PR Fast-Track | inverse-observation (non-core PR block + agentic-plan-in-issue) |

### New active candidates: 0

(Target met: 12-CONSECUTIVE-WIKI ZERO-REGISTRATION STREAK v37-v48 — NEW LONGEST in corpus history, extends v47 11-streak.)

### New OBSERVATION-TRACKs: 0

### Pattern Library state preserved

- Pre-v48: 37 confirmed + 19 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active. Ratio **19:37 = 0.513:1**.
- Post-v48: **37 confirmed + 19 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active. Ratio 19:37 = 0.513:1 PRESERVED 12TH CONSECUTIVE CYCLE.**
- 0.437 buffer below 0.95:1 mini-audit trigger preserved (largest in corpus history maintained).

## 8. Key conclusions

1. **T4 extends to N=8** with NEW T4i agentic-workflow-compiler-for-CICD-bridge sub-archetype. T4 is corpus's 2nd-largest tier (after T1 N=14).
2. **Pattern #66 OT MAJOR STRENGTHENING** — gh-aw provides corpus-strongest defense-in-depth data point + introduces architectural-defense-by-design observation distinct from crawl4ai's event-based-incident-response. Sub-categorization opportunity at next audit.
3. **Pattern #18 Layer 0 strengthening** — MCP Gateway as horizontal-aggregation Layer 0 (companion to ollama vertical-aggregation Layer 0); structural-N=2 sub-type taxonomy candidate.
4. **Pattern #19 archetype 2 strengthening** — research-incubation-to-mainline-graduation pathway corpus-first; GitHub Next 4-researcher cluster as 5th lineage-cluster-type observable.
5. **Pattern #22 counter-evidence** narrows 22c sub-variant scope to solo-multi-runtime-platform pattern; github-corporate-official tier convention is AGENTS.md-only.
6. **0 new active candidates** — 12-streak NEW LONGEST consolidation-forward discipline application.
7. **EXTREME-tier primitive count (~3,200+)** — 2nd in corpus after aidevops v47 (~2,665+); confirms EXTREME tier informal-discipline applicable beyond solo-multi-runtime archetype.

## 9. Cross-references

- **spec-kit v17** (sister github/* corpus T1 entry; same parent org)
- **aidevops v47** (recent EXTREME-tier comparison + 22c counter-evidence + 4-influence-node graph extended)
- **awesome-mcp-servers v31** (Pattern #18 ancestor; gh-aw introduces MCP Gateway as Layer 0 horizontal-aggregation)
- **ollama v46** (Pattern #18 Layer 0 vertical-aggregation precedent; gh-aw is horizontal-aggregation companion)
- **claude-howto v32 + claude-code-best-practice v34** (Anthropic-team-cluster precedent for 4-researcher-cluster lineage parallel)
- **graphify v16, markitdown v28, claude-context v40** (T4 sibling archetype variants)
- **crawl4ai v29** (Pattern #66 OT inaugural event-based-incident-response observation; gh-aw introduces architectural-defense-by-design distinction)
