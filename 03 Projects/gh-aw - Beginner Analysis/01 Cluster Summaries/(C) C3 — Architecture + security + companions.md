# (C) Cluster 3 — Architecture + security + companion ecosystem

> **Wiki #48 · gh-aw** | **2026-04-25** | Sources: cmd/ + pkg/ (1,789 .go files) + actions/ + .github/workflows/ (201 paired) + specs/ (W3C-style security architecture) + .architecture.yml + SECURITY.md + SBOM + companion repos (gh-aw-firewall AWF + gh-aw-mcpg MCP Gateway + gh-aw-actions)

## Source-tree architecture

```text
gh-aw/
├── cmd/
│   ├── gh-aw/              # CLI entry point binary (the `gh aw` extension)
│   └── gh-aw-wasm/         # WASM variant of binary (corpus-first WASM at this scale + tier)
├── pkg/                    # 22 subdirs / 1,789 .go files
│   ├── actionpins          # Action SHA pinning
│   ├── agentdrain          # Agent output drain
│   ├── cli                 # Command implementations
│   ├── console             # Console formatting library
│   ├── constants           # Constants
│   ├── envutil             # Env utilities
│   ├── fileutil            # File utilities
│   ├── gitutil             # Git utilities
│   ├── logger              # Debug logger (DEBUG=* env-var)
│   ├── parser              # Markdown frontmatter parser (//go:embed JSON schemas)
│   ├── repoutil            # Repo utilities
│   ├── semverutil          # SemVer utilities
│   ├── sliceutil           # Slice utilities
│   ├── stats               # Stats library
│   ├── stringutil          # String utilities
│   ├── styles              # Styling
│   ├── testutil            # Test utilities
│   ├── timeutil            # Time utilities
│   ├── tty                 # Terminal handling
│   ├── types               # Type definitions
│   ├── typeutil            # Type utilities
│   └── workflow            # ⭐ workflow compilation (981+ Go files in this single subdir)
├── internal/               # Internal packages
├── actions/
│   ├── setup/              # Setup action (runtime file copying for .cjs and .sh)
│   │   ├── js/             # *.cjs source-of-truth (NOT embedded in binary)
│   │   └── sh/             # *.sh source-of-truth (NOT embedded in binary)
│   └── setup-cli/          # Setup-CLI action
├── docs/                   # Astro-built documentation site
│   ├── adr/                # Architecture Decision Records
│   ├── src/                # Astro site source
│   ├── enterprise-configuration.md
│   ├── interactive-run-mode.md
│   └── functional-patterns.md
├── specs/                  # W3C-style formal specifications (3 files)
│   ├── security-architecture-spec.md         # 130+ formal requirements (RFC 2119)
│   ├── security-architecture-spec-summary.md # Summary (this is what we read)
│   └── security-architecture-spec-validation.md
├── schemas/
│   └── agent-output.json   # JSON schema for agent output validation
├── scratchpad/             # 63 engineering-decision-record working notes
├── research/               # Research notes
├── skills/                 # 24 skill subdirs (Anthropic skill format)
├── socials/                # Community/social assets
├── scripts/                # Build/dev scripts
├── tools.go                # Go tools file
├── install-gh-aw.sh        # curl bash installer
└── .github/                # GitHub-specific config (201 paired workflows + agents + skills + smoke-tests + zizmor)
```

## Build system architecture (corpus-first observations)

### Runtime file copying (NOT embedded)

Verbatim from AGENTS.md:
> *"JavaScript and shell script files are NOT embedded in the binary."*

**Source-of-truth:**
- `actions/setup/js/*.cjs` (manually edited, committed to git)
- `actions/setup/sh/*.sh` (manually edited, committed to git)

**Runtime flow:** `actions/setup` action copies files from `actions/setup/js/` → `/tmp/gh-aw/actions` at runtime. Workflows access these directly.

= **CORPUS-FIRST runtime-file-copying-instead-of-go-embed-for-cjs-sh** at corporate-official tier. Distinct from typical Go-binary-embedding via `//go:embed`. Only JSON schemas (in `pkg/parser/schemas/`) are embedded; JS/shell explicitly excluded.

### //go:embed for JSON schemas

> *"ALWAYS REBUILD AFTER SCHEMA CHANGES: make build (Schema files are embedded in the binary using //go:embed directives, so changes require rebuilding the binary)."*

= JSON schemas embedded; CJS/shell deliberately NOT embedded. This split is novel architectural choice.

### .architecture.yml file-line-threshold manifest (CORPUS-FIRST)

```yaml
thresholds:
  file_lines_blocker: 2000   # BLOCKER violation
  file_lines_warning: 1000   # WARNING violation
  function_lines: 200        # WARNING for functions
  max_exports: 10            # INFO for high export count
```

= **CORPUS-FIRST explicit-architectural-threshold-manifest at root**. Not present in any of 47 prior corpus wikis. Likely consumed by lint/CI tooling for automated architectural-degradation detection.

### Lock file convention (CORPUS-FIRST at corporate-official tier)

- `.lock.yml` files = compiled workflow output (markdown spec → compiled GitHub Actions YAML)
- AGENTS.md mandate: *"NEVER ADD LOCK FILES TO .GITIGNORE — `.lock.yml` files are compiled workflows that must be tracked."*
- `.gitattributes` (created by `gh aw init`) marks `.lock.yml` as **generated** (collapsed in PR diffs)

= **CORPUS-FIRST track-the-compiled-output convention** at corporate-official tier. Distinct from typical Go-binary-build artifact pattern (Go binaries .gitignore'd).

## Compilation pipeline

```text
.md (markdown spec) ──[gh aw compile]──> .lock.yml (GitHub Actions workflow)
       │                                          │
       │                                          ├── triggers (on: ...)
       │                                          ├── permissions (read-only by default)
       │                                          ├── jobs:
       │                                          │   ├── activation (event handling)
       │                                          │   ├── agentic (LLM execution sandboxed)
       │                                          │   └── safe-output (sanitized write ops)
       │                                          └── secrets (GITHUB_TOKEN-scoped)
       └── frontmatter:
               engine: copilot|claude|codex|custom
               tools: { github: { toolsets: [default] } }
               network: { allowed: [...] }
               safe-outputs: { ... }
```

**Engine selection** in frontmatter routes the workflow to one of 5 supported engines:
- `copilot` — GitHub Copilot Coding Agent (uses GitHub MCP server for API access; cannot directly hit api.github.com)
- `claude` — Claude (via Anthropic API or Claude Code OAuth)
- `codex` — OpenAI Codex
- `custom` — extensible engine plugin

= **CORPUS-FIRST engine-selection-as-frontmatter-axis** at corporate-official tier. Distinct from native multi-provider (LiteLLM-style abstraction at multica v15 / TrendRadar v19) and verification-not-routing (aidevops v47): this is **runtime-engine-selection-with-per-engine-constraints** (e.g., Copilot engine cannot access api.github.com directly; Claude engine can).

## Security architecture (Pattern #66 OT strongest corpus data point)

**Reference:** `specs/security-architecture-spec-summary.md` (2026-01-29; v1.0.0 Candidate Recommendation)

### W3C-style formal specification

- **130+ formal requirements** using RFC 2119 keywords (MUST / SHALL / SHOULD / MAY)
- **70+ compliance tests** across 8 categories
- **6 comprehensive appendices** with diagrams, examples, best practices
- **3 conformance classes**: Basic (Level 1) / Standard (Level 2) / Complete (Level 3)
- **MIT-licensed specification** (allows external organizations to replicate the security model)
- **Target audience**: Security Engineers / Platform Engineers / Compliance Teams / Workflow Authors / Research Teams

### 7-layer defense-in-depth architecture

| Layer | Name | Function |
|-------|------|----------|
| 0 | Compilation-Time Validation | Schema, expressions, permissions validated before execution |
| 1 | Input Sanitization | @mentions / bot triggers / XML/HTML / URIs sanitized |
| 2 | Output Isolation | Separate read/write operations; safe-outputs sanitized |
| 3 | Network Isolation | Domain allowlisting, ecosystem IDs |
| 4 | Permission Management | Least privilege, role-based access |
| 5 | Sandbox Isolation | AWF/SRT containers, MCP isolation |
| 6 | Threat Detection | Prompt injection / secret leaks / malicious patches |

### 7 Security Guarantees (SG-01 through SG-07)

| ID | Guarantee |
|----|-----------|
| SG-01 | Untrusted input not directly interpolated into GitHub Actions expressions without sanitization |
| SG-02 | AI agents have no direct write access |
| SG-03 | Network access restricted to allowlists |
| SG-04 | Least-privilege permissions by default |
| SG-05 | Agent processes in isolated sandboxes |
| SG-06 | All actions produce auditable artifacts |
| SG-07 | Security failures prevent execution (fail-secure) |

### 8 Compliance Test categories (70+ tests total)

1. T-IS-001 to T-IS-008 — Input Sanitization Tests
2. T-OI-001 to T-OI-007 — Output Isolation Tests
3. T-NI-001 to T-NI-009 — Network Isolation Tests
4. T-PM-001 to T-PM-007 — Permission Management Tests
5. T-SI-001 to T-SI-007 — Sandbox Isolation Tests
6. T-TD-001 to T-TD-007 — Threat Detection Tests
7. T-CS-001 to T-CS-006 — Compilation-Time Security Tests
8. T-RS-001 to T-RS-008 — Runtime Security Tests

### SBOM (SPDX + CycloneDX)

From SECURITY.md:
- SBOMs auto-generated on every release; attached to GitHub releases as downloadable assets
- Both formats generated: `sbom.spdx.json` + `sbom.cdx.json`
- Local generation via syft: `make sbom`
- Includes: all direct + transitive Go deps, package versions, licenses, hashes, dependency relationships

= **CORPUS-FIRST dual-SBOM-format (SPDX + CycloneDX) generation at corporate-official tier**.

## Companion ecosystem (3 repos under github/* parent)

### `github/gh-aw-firewall` (Agent Workflow Firewall — AWF)

> *"Network egress control for AI agents, providing domain-based access controls and activity logging for secure workflow execution"*

= Layer 5 Sandbox Isolation implementation. Domain-based allowlisting + activity logs. Companion repo provides AWF as reusable infrastructure.

### `github/gh-aw-mcpg` (MCP Gateway)

> *"Routes Model Context Protocol (MCP) server calls through a unified HTTP gateway for centralized access management"*

= **CORPUS-FIRST MCP-gateway-as-unified-routing-infrastructure**. Strengthens Pattern #18 with N=1 Layer 0 observation: where pi-mono v36 / ollama v46 / aidevops v47 each documented MCP-server-set per-runtime, gh-aw introduces explicit gateway-layer abstraction above per-runtime MCP. If 2nd MCP-gateway emerges in corpus, Pattern #18 4-layer taxonomy extension proposal becomes structural-N=2 candidate at audit.

### `github/gh-aw-actions` (Shared GitHub Actions Library)

> *"Shared library of custom GitHub Actions used by compiled workflows, providing functionality such as MCP server file management"*

= reusable Actions infrastructure consumed by compiled `.lock.yml` workflows.

**Pattern #17 variant 2a strengthening:** github/* org now has 4-repo coordinated ecosystem (gh-aw + AWF + MCP Gateway + Actions library) under single corporate parent. Distinct from prior corporate-official sub-ecosystems:
- spec-kit v17 (T1, single-repo)
- magika v44 (Google Research, single-repo)
- markitdown v28 (Microsoft, T4 single-repo)

= 1st corpus 4-repo coordinated infrastructure-platform-companion at corporate-official tier.

## .github/workflows/ — 201 paired workflow files

```text
.github/workflows/
├── 100+ pairs of (workflow-name.md + workflow-name.lock.yml)
└── Each .md = source-of-truth markdown agentic workflow
   Each .lock.yml = compiled GitHub Actions YAML (must be tracked, never .gitignored)
```

**Sample workflow names** (from /bin/ls):
- `ace-editor` / `agent-performance-analyzer` / `agent-persona-explorer` / `agent-task-sessions`
- `agentic-observability-kit` / `agentic-optimization-kit`
- `ai-moderator` / `api-consumption-report` / `approach-validator`
- `archie` / `architecture-guardian` / `artifacts-summary` / `audit-workflows`
- `auto-close-parent-issues` / `auto-triage-issues`
- `aw-failure-investigator` / (~100+ more)

**Observation:** This is **gh-aw-meta-development workflow catalog**. 201 paired workflows are how the gh-aw team uses gh-aw to develop gh-aw — pure dogfooding. Distinct from "example workflows for users" (those exist separately in `githubnext/agentics` per `gh aw add githubnext/agentics` install command).

## .serena/ + .skill-optimizer/ subsystems

- `.serena/` — config for Serena agent integration (per `serena-tool.md` workflow)
- `.skill-optimizer/skill-optimizer.json` — daily skill-optimizer workflow config

= **CORPUS-FIRST autonomous-self-improvement workflow** at corporate-official tier. Daily workflow tunes `skills/*/SKILL.md` content using LLM evaluation against pass-rate target. Adjacent to aidevops v47 Pulse Supervisor philosophy but narrower scope.

## actionlint + zizmor (security linting stack)

`.github/`:
- `actionlint.yaml` — actionlint configuration (GitHub Actions linter)
- `zizmor.yml` — **zizmor** configuration (Trail of Bits security linter for GitHub Actions)

= 2-tool security-linting stack (actionlint + zizmor) — corpus-first at corporate-official tier with **zizmor** specifically (zizmor is the modern security-focused Actions linter from Trail of Bits, established 2024).

## 10+ corpus-first observations from Cluster 3

1. **CORPUS-FIRST W3C-style formal Security Architecture Specification** at corporate-official tier (130+ MUST/SHOULD requirements, 70+ tests, 3 conformance classes)
2. **CORPUS-FIRST 7-layer defense-in-depth architecture** explicitly enumerated
3. **CORPUS-FIRST 7 numbered Security Guarantees (SG-01-SG-07)** in formal spec
4. **CORPUS-FIRST 8-category compliance test taxonomy (70+ tests)**
5. **CORPUS-FIRST dual-SBOM-format (SPDX + CycloneDX) auto-generation per release** at corporate-official tier
6. **CORPUS-FIRST MCP Gateway as unified routing infrastructure** (Pattern #18 Layer 0 observation; companion repo)
7. **CORPUS-FIRST AWF (Agent Workflow Firewall) network egress control** at corporate-official tier (companion repo)
8. **CORPUS-FIRST 4-repo coordinated github-org infrastructure-platform-companion** (gh-aw + AWF + MCP Gateway + Actions library)
9. **CORPUS-FIRST `.architecture.yml` file-line/function-line/export-count thresholds manifest** at root
10. **CORPUS-FIRST WASM-binary-variant** (`cmd/gh-aw-wasm/`) alongside main Go binary at this scale + tier
11. **CORPUS-FIRST track-compiled-output `.lock.yml` convention** at corporate-official tier (gh-aw mandates `.lock.yml` files committed; never .gitignored)
12. **CORPUS-FIRST runtime-file-copying-instead-of-go-embed-for-cjs-sh** (split: //go:embed for JSON schemas; runtime-copy for `*.cjs` + `*.sh`)
13. **CORPUS-FIRST 5-engine-first-class-frontmatter-selection** (copilot/claude/codex/custom + extensibility)
14. **CORPUS-FIRST zizmor security linter integration** at corporate-official tier (Trail of Bits Actions linter)
15. **CORPUS-FIRST agent-targeted README HTML comment** routing agents to raw-md specs

## Pattern Library implications from Cluster 3

- **Pattern #66 OT MAJOR STRENGTHENING** — gh-aw provides corpus-strongest defense-in-depth data point: W3C-style spec + 7-layer architecture + 7 SG guarantees + 130+ formal requirements + 70+ compliance tests + SBOM + AWF firewall + MCP gateway + compile-time validation + zizmor + actionlint. **Pattern #66 was reclassified at v29 audit as event-based-incident-response OBSERVATION-TRACK** — gh-aw observation introduces architectural-defense-by-design framing structurally distinct from event-based response. **At next audit, OT scope review opportunity:** does Pattern #66 split into "event-based-incident-response (crawl4ai v29 inaugural)" + "architectural-defense-by-design (gh-aw v48 inaugural)"? Both observable, structurally distinct.
- **Pattern #18 Layer 0 strengthening** — MCP Gateway as unified routing infrastructure. Joins ollama v46 "Layer 0 runtime-bundled-launcher" as 2nd Layer-0-position observation at N=1 each. If 2nd MCP-gateway-pattern observation arrives, Layer 0 has 2 sub-types at N=2 = formulation-extension candidate.
- **Pattern #2 Distribution Evolution strengthening** — `gh extension install` + curl + brew = 3-surface (medium-corpus); compile-time-`.lock.yml`-tracked = first-class build artifact treatment.
- **Pattern #28 Multi-Provider strengthening** — engine-selection-as-frontmatter-axis sub-observation (within-pattern, not new candidate).
- **Pattern #19 archetype 2 methodology-lineage strengthening** — research-incubation-graduated-to-mainline (`githubnext/gh-aw` → `github/gh-aw` v0.40.1) + 4-researcher cluster CODEOWNERS.

## Counter-evidence + absences

- **No vendor lock-in to specific cloud** — gh-aw runs on standard GitHub Actions runners; AWF + MCP Gateway are open-source companion repos.
- **No commercial tier observed** — fully MIT, no premium gating. Pattern #31 Open-Core does NOT apply (gh-aw is corporate-official-fully-OSS, distinct archetype from commercial-startup-open-core wikis).
- **No academic-paper / arXiv** — despite GitHub Next research origins (Pattern #42 NOT applicable).
- **No CITATION.cff** — despite formal W3C-style spec.
- **No i18n** — EN-only at github-corporate-official tier (consistent with spec-kit v17).
