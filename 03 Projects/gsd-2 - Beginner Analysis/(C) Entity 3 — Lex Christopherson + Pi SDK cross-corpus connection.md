# (C) Entity 3 — Lex Christopherson + Pi SDK cross-corpus connection

## Lex Christopherson (named author of gsd-2)

| Field | Evidence |
|---|---|
| **LICENSE copyright** | "Copyright (c) 2026 Lex Christopherson" (verbatim from `/tmp/gsd2-full/LICENSE`) |
| **ADR authorship** | `docs/dev/ADR-001-branchless-worktree-architecture.md` deciders: Lex Christopherson |
| **ADR authorship** | `docs/dev/ADR-003-pipeline-simplification.md` deciders: Lex Christopherson |
| **PRD authorship** | `docs/dev/PRD-branchless-worktree-architecture.md` Author: Lex Christopherson |
| **Filesystem path evidence** | `docs/dev/agent-knowledge-index.md` references `/Users/lexchristopherson/.gsd/docs/...` (developer's local path) |
| **External presence** | NOT verified externally in this wiki (would require Twitter / personal blog / LinkedIn search) |

## Authorship identity question (Lex Christopherson vs TÂCHES)

**TÂCHES** = author of GSD-1 (`gsd-build/get-shit-done`) per Storm Bear v5 wiki. Storm Bear v5 documented TÂCHES voice as distinctive: "solo developer who doesn't write code" + Spanish/French inflections + meta-prompting pedagogy framing.

**Three hypotheses**:

1. **Same person, different identity** — TÂCHES = Lex Christopherson under a personal-brand persona. Possible because: gsd-build org owns both repos / coherent product-line continuation / VISION says GSD-2 is "future" of GSD-1.

2. **Handed off within org** — TÂCHES handed GSD-2 development to Lex Christopherson (perhaps as second maintainer joining gsd-build org). Possible because: GSD-1 LICENSE author probably ≠ GSD-2 LICENSE author (would need to verify GSD-1 LICENSE) / GSD-2 voice is professional/neutral, not TÂCHES distinctive style / no TÂCHES mentions in GSD-2 README/VISION/CONTRIBUTING/docs.

3. **gsd-build is multi-maintainer org from start** — TÂCHES = co-founder/early-maintainer of gsd-build; Lex Christopherson = co-founder/maintainer focused on GSD-2 architecture. Possible because: gsd-build org name (not "TÂCHES org") suggests collective branding.

**Honest verdict**: Unknown without external verification. Document as-observed; do NOT assume identity continuity. Storm Bear v54 wiki names Lex Christopherson as gsd-2 author per primary repo evidence.

## Pi SDK cross-corpus connection

**Pi SDK origin**: Mario Zechner's `pi-mono` repo at github.com/badlogic/pi-mono (Storm Bear v36 wiki subject). pi-mono documents 7 packages in its monorepo:

| pi-mono package (v36) | Purpose | Vendored in gsd-2? |
|---|---|---|
| `pi-coding-agent` | Coding agent CLI | ✅ as `@gsd/pi-coding-agent` |
| `pi-ai` | Unified LLM API (20+ providers) | ✅ as `@gsd/pi-ai` |
| `pi-agent-core` | General-purpose agent core | ✅ as `@gsd/pi-agent-core` |
| `pi-tui` | Terminal UI library | ✅ as `@gsd/pi-tui` |
| `pi-web-ui` | Web components for AI chat interfaces | ❌ (gsd-2 has separate `web/` workspace) |
| `pi-mom` | Slack bot | ❌ (not gsd-2 concern) |
| `pi-pods` | GPU pod CLI for vLLM | ❌ (not gsd-2 concern) |

**4 of 7 vendored** (57% adoption). gsd-2 vendoring justification (per README):

> GSD is now a standalone CLI built on the [Pi SDK](https://github.com/badlogic/pi-mono), which gives it direct TypeScript access to the agent harness itself.

**Why vendor instead of npm dependency?**

Vendoring trade-offs:
- ✅ **Faster iteration** — gsd-2 can patch pi-* packages in-tree without coordinating upstream PRs to pi-mono
- ✅ **Isolation from upstream breaking changes** — pi-mono's 200+ releases in 8.5 months (v36 wiki observation) suggests aggressive iteration that could break downstream
- ✅ **Lockstep versioning** — all 4 vendored pi-* packages versioned 2.78.1 (matches gsd-2 root); easy to reason about compatibility
- ❌ **Divergence from upstream** — gsd-2's @gsd/pi-* will drift from @mariozechner/pi-* over time
- ❌ **Maintenance burden** — gsd-2 maintainer must manually pull pi-mono updates if desired
- ❌ **Supply-chain question** — what version of pi-mono was forked? When? What's the upstream-sync cadence?

**Strongest possible Pattern #57 evidence in corpus** (machine-readable metadata in package.json description):
- `@gsd/pi-coding-agent` package.json description: `"Coding agent CLI (vendored from pi-mono)"`
- `@gsd/pi-ai` package.json description: `"Unified LLM API (vendored from pi-mono)"`
- `@gsd/pi-agent-core` package.json description: `"General-purpose agent core (vendored from pi-mono)"`
- `@gsd/pi-tui` package.json description: `"Terminal User Interface library (vendored from pi-mono)"`

**Sub-variant 57d candidate**: machine-readable-vendoring-metadata. Distinct from 57a (narrative direct citation) / 57b (aggregator-mediated) / 57c (forward-citation-then-wiki). Searchable + deterministic + ungameable.

## Mario Zechner's role (per Pattern #19 archetype 2 candidate)

Mario Zechner = author of pi-mono v36 + libGDX (25K-star Java game-dev framework, 15+ years OSS). gsd-2 cites Pi SDK throughout README. **Question**: Does Mario become Pattern #19 archetype 2 5th individual-influence-node?

**Existing archetype 2 nodes** (per v53 corpus state):
1. Karpathy (autoresearch v10 + many touchpoints)
2. John Lam (spec-kit v17 SDD lineage)
3. Anthropic-team-cluster (Boris Cherny + Dex Horthy + Cat Wu via claude-code-best-practice v34)
4. Lance Martin (LangChain — aidevops v47 16-pattern lineage)

**Mario Zechner candidate (5th)?**
- **Argument for**: Pi SDK becomes corpus-substrate (consumed by 2 corpus wikis: pi-mono v36 = origin + gsd-2 v54 = downstream); influence is real
- **Argument against**: Mario IS the pi-mono v36 wiki subject (not an external-influence-node like Karpathy who is wiki subject of autoresearch v10 but methodology-influence-node for many others); Mario is corpus-presence as wiki subject + tool author, NOT external-methodology-influence-node
- **Honest verdict**: Different mechanism from Karpathy/Lam/Anthropic-team/Lance. Mario = tool-substrate-author, not methodology-influence-node. **Do NOT register as archetype 2 5th node**; document as observation.

## Pattern #18 sub-observation: Pi-SDK-as-runtime-substrate

Pattern #18 currently has 3-tier MCP layer formulation (Layer 1 MCP universal / Layer 2 OpenClaw+Hermes community-platform / Layer 3 per-runtime). Plus 3-runtime-primacy diversity (Claude-Code-primary majority + OpenCode-primary aidevops v47 + Codex-primary observed via oh-my-codex sibling).

**gsd-2 v54 NEW observational sub-variant**: **Pi-SDK-as-runtime-substrate** — Pi SDK becoming cross-project agent-runtime layer that other frameworks vendor or depend on.

**N=1 explicit (gsd-2 vendors Pi SDK)** + **N=1 origin (pi-mono v36 IS Pi SDK)** = N=2 corpus presence at substrate level. Distinct from Layer 1 MCP (universal protocol) / Layer 2 community-platform (OpenClaw + Hermes shared runtimes) / Layer 3 per-runtime (Claude Code-specific, OpenCode-specific, etc.).

**Pi SDK substrate properties**:
- TypeScript-native (vs MCP language-agnostic)
- Single-author origin (Mario Zechner) vs MCP multi-vendor consortium
- Vendorable as workspace packages (not just npm dependency)
- Provides agent-loop primitives that wrap any LLM provider

**Sub-variant status**: N=1 stale-flagged for v59. Promote to candidate only if 2nd corpus example of Pi-SDK substrate consumption emerges.

## RTK managed binary integration (Pattern #66 by-design strengthening)

Per README:
> GSD now provisions a managed [RTK](https://github.com/rtk-ai/rtk) binary on supported macOS, Linux, and Windows installs to compress shell-command output in `bash`, `async_bash`, `bg_shell`, and verification flows. **GSD forces `RTK_TELEMETRY_DISABLED=1` for all managed invocations.** Set `GSD_RTK_DISABLED=1` to disable the integration.

**Pattern #66 by-design sub-category strengthening** (joins gh-aw v48 W3C-style spec):
1. **Provisions** managed third-party binary (gsd-2 manages download + install lifecycle)
2. **Forces telemetry-disabled** even if RTK upstream has telemetry-on-by-default
3. **Provides opt-out** env var (`GSD_RTK_DISABLED=1`) for users who want to disable RTK entirely

**N=2 by-design data points** in Pattern #66 OBSERVATION-TRACK now:
- gh-aw v48 (corporate-official) = W3C-style Security Architecture Specification + AWF firewall + MCP Gateway
- gsd-2 v54 (org-led) = managed third-party binary + force-disable upstream telemetry + user opt-out

**Mechanism distinction**:
- gh-aw v48 = formal-specification + multiple-architectural-defenses
- gsd-2 v54 = third-party-binary-lifecycle-management + telemetry-discipline-by-default

**Sister to crawl4ai v29 event-based incident-response** (different sub-category — incident-response vs by-design).

## Cross-corpus citation density at gsd-2

gsd-2 has **highest cross-corpus citation density per wiki in 54 wikis**:

| Citation type | Source | Detail |
|---|---|---|
| Pi SDK | pi-mono v36 | 4 vendored packages with metadata |
| Get Shit Done | GSD-1 v5 | Predecessor with migration tool |
| RTK binary | rtk-ai/rtk (NOT corpus) | Managed third-party integration |
| GSD2 Config Utility | jeremymcs/gsd2-config (NOT corpus; ecosystem add-on) | Cited in Ecosystem section |
| MCP integration | Anthropic MCP standard (corpus-cross-cutting) | `@modelcontextprotocol/sdk` |
| Conventional Commits | conventionalcommits.org (NOT corpus) | CI enforcement |
| Keep a Changelog | keepachangelog.com (NOT corpus) | CHANGELOG format |

**3 corpus wikis directly cited** (Pi SDK + GSD-1 implicit + extensions referencing Anthropic MCP) — strongest cross-corpus density observed.

## Cross-references

- See `(C) Cluster 2` for full architecture + Pi SDK vendoring evidence
- See `(C) Entity 1` for core product capabilities
- See `(C) Entity 2` for gsd-build org + GSD-1 successor relationship
- See `(C) Entity 4` for Storm Bear meta — vault-architectural lessons
- See `00 OPEN-QUESTIONS.md` Q1-Q2 for authorship identity questions
