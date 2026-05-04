# (C) Cluster 3 — Governance + extensions + commercial-funnel

## Source files

| Source | Notes |
|---|---|
| LICENSE | MIT, Copyright **Lex Christopherson** 2026 |
| CONTRIBUTING.md | 432 lines — branching/commits/RFC/first-time-contributors discipline |
| CHANGELOG.md | 3,843 lines (Keep a Changelog format) — sampled top 100 lines covering v2.78.x |
| Root files | NO AGENTS.md / NO CLAUDE.md / NO SECURITY.md / NO CODE_OF_CONDUCT at root |
| `gsd-orchestrator/SKILL.md` | Agent skill exposing GSD-as-subprocess interface |
| `mintlify-docs/introduction.mdx` | Commercial-funnel doc site |

## Governance file inventory at root

| File | Present? | Size | Notes |
|---|---|---|---|
| README.md | ✅ | 873 lines | Comprehensive user-facing |
| VISION.md | ✅ | 37 lines | 5 principles + 5 PR-rejection categories |
| CONTRIBUTING.md | ✅ | 432 lines | Heavy contributor process discipline |
| CHANGELOG.md | ✅ | 3,843 lines | Keep a Changelog format; per-version detailed |
| LICENSE | ✅ | MIT | Copyright Lex Christopherson 2026 |
| AGENTS.md | ❌ | — | NOT at root |
| CLAUDE.md | ❌ | — | NOT at root |
| SECURITY.md | ❌ | — | NOT at root (security guidance in CONTRIBUTING + extensions/secure-env-collect) |
| CODE_OF_CONDUCT.md | ❌ | — | NOT at root |
| CITATION.cff | ❌ | — | NOT at root |
| `.github/` workflows | (not probed individually) | — | CI hooks mentioned: commit-msg + Conventional Commits + base64-scan + docs-prompt-injection-scan |

**Pattern #22 observation**: AGENTS.md is documented as a **user-facing config primitive** in README ("Place an `AGENTS.md` file in any directory to provide persistent behavioral guidance for that scope"). gsd-2's Pi core loads `AGENTS.md` automatically with `CLAUDE.md` as fallback. **But gsd-2 does NOT ship AGENTS.md for itself.** Counter-evidence at T1: agent-platforms can teach AGENTS.md without dogfooding it at root.

**Position vs corpus 4-template AGENTS.md ensemble**:
- 22a monolithic spec-kit / gh-aw → gsd-2 doesn't fit (no AGENTS.md at all)
- 22b minimum-viable-shim bizos v37 → gsd-2 doesn't fit
- 22c authoritative-with-shim aidevops v47 → gsd-2 doesn't fit
- 22d identical-mirror Vercel v51 → gsd-2 doesn't fit
- **gsd-2 = 22-absent at T1 framework that teaches AGENTS.md** — distinct sub-observation; do NOT register standalone (consolidation-forward)

## CONTRIBUTING discipline highlights (verbatim selection)

> We hold a high bar for what gets merged — not to be gatekeepers, but because every change ships to real users and stability matters.

Process steps:
1. **Check existing issues** before starting
2. **Claim the issue** — comment to get assigned BEFORE writing code
3. **No issue? Create one first** for new features (bug fixes for obvious problems can skip)
4. **Architectural changes require an RFC** via Architecture Decision Records (ADRs)

**First-time contributor gate** (verbatim):

> We are not a fan of drive-by first-time contributions. If this is your first PR to GSD-2, you **must** open an issue first describing the problem or feature, wait for a maintainer response, and link the issue in your PR. **First-time PRs that show up with no prior issue will be closed without review.** This is not optional — it exists because triaging unsolicited code from unknown contributors is more expensive than the contribution is worth.
>
> Once you have one merged PR, this requirement no longer applies to you.

**Pattern #69 observation**: This is **inverse-Pattern-#69** — gsd-2 has NO `lgtm` / `🤖🤖🤖` agent fast-track; instead uses **first-time contributor gate** that REJECTS drive-by PRs. Sister to gh-aw v48's "Traditional Pull Requests Are Not Enabled for non-Core team members" but at solo-org scale not corporate-official scale.

**Branch + commit conventions**:

| Branch type | Use |
|---|---|
| `feat/` | New functionality |
| `fix/` | Bug or defect correction |
| `refactor/` | Code restructuring, no behavior change |
| `test/` | Adding/updating tests |
| `docs/` | Documentation only |
| `chore/` | Dependencies, tooling, housekeeping |
| `ci/` | CI/CD configuration |

Commits enforce **Conventional Commits** (commit-msg hook locally + CI on push).

## CHANGELOG cadence

**78 minor versions in 46 days** = ~1.7/day. Sample of v2.78.0 (released 2026-04-25) shows **40+ items** in single release across 5 categories (Added / Fixed). v2.78.1 hot-fix on same day for `claude-code-cli` issues.

**Velocity observation**: This is **fastest minor-version cadence in corpus** (vs ruflo v42 ~12 alpha/month + ECC v1 / Superpowers v2 / spec-kit v17 weekly cadence). Suggests aggressive iteration discipline + mature CI/CD pipeline + small-PR culture.

**Conventional Commits enforced + CHANGELOG auto-generated** (per `scripts/generate-changelog.mjs` in scripts dir).

## Commercial-funnel observation (Pattern #50 watch)

**Multi-component infrastructure suggesting commercial-tier emergence**:

| Component | Purpose | Commercial-tier potential |
|---|---|---|
| **gsd.build** | Domain (homepage) | ✅ branded domain |
| **contact@gsd.build** | Org email | ✅ org-level commercial contact |
| **Discord** (1.4K+ members estimated) | Community | ✅ community channel |
| **`@gsd-build/daemon`** | Background process for project monitoring + Discord integration | ⚠️ "Discord integration" suggests potential team/cloud-tier hook — observational |
| **`@gsd-build/mcp-server`** | MCP server exposing GSD orchestration tools to external MCP clients | ✅ infrastructure for headless/cloud orchestration |
| **`@gsd/studio`** Electron desktop | React 19 + Zustand + electron-vite | ⚠️ private workspace v0.0.0; could be incubation Pro-tier UI or OSS |
| **`gsd-orchestrator/SKILL.md`** | Agent skill for orchestrating GSD as subprocess | ✅ enables multi-agent / cloud orchestration |
| **`mintlify-docs/`** | Mintlify documentation site | ✅ commercial-quality doc infrastructure |
| **`web/` workspace** | Browser-based project management + real-time progress | ✅ web UI that could be hosted SaaS |
| **`vscode-extension/`** | VS Code chat participant + sidebar dashboard + RPC integration | ✅ deep IDE integration |
| **GitHub Sync extension** | Auto-sync milestones to GitHub Issues + PRs + Milestones | ✅ team collaboration enabler |
| **Remote Questions extension** | Route decisions to Slack/Discord in headless/CI | ✅ team coordination feature |

**Verdict**: gsd-2 has **multi-component infrastructure consistent with future commercial-cloud-tier emergence** but does NOT currently advertise paid tier in README. Pattern #50 status = **observational watch**, NOT counted as N=2/N=3 data point until commercial-tier surfaces.

## $GSD Solana token (Pattern #37 2nd data point)

README banner badge:
> [![$GSD Token](badge)](https://dexscreener.com/solana/dwudwjvan7bzkw9zwlbyv6kspdlvhwzrqy6ebk8xzxkv)

**Single Solana token** at gsd-2 commercial framework. Different from Pattern #37 N=1 source (system-prompts-leaks v21 multi-channel donations + Solana token at prompt-leak-archive). Mechanism divergence:
- **v21 mechanism**: leak-archive + 6-channel donation diversification + crypto-token = monetization-via-content-controversy
- **v54 mechanism**: commercial-framework + direct-token-attached-to-active-product = monetization-via-product-velocity

**Conservative interpretation**: N=2 strengthening with mechanism divergence flag; do NOT promote (mechanisms differ enough to question whether they're same pattern).

## RTK managed binary (corpus-first observation)

README verbatim:
> GSD now provisions a managed [RTK](https://github.com/rtk-ai/rtk) binary on supported macOS, Linux, and Windows installs to compress shell-command output in `bash`, `async_bash`, `bg_shell`, and verification flows. **GSD forces `RTK_TELEMETRY_DISABLED=1` for all managed invocations.** Set `GSD_RTK_DISABLED=1` to disable the integration.

**Pattern #66 observation strengthening**: Architectural-defense-by-design sub-variant. gsd-2:
1. **Provisions** managed third-party binary (not pip/cargo install — gsd-2 manages download/install)
2. **Forces telemetry-disabled** even if RTK upstream has telemetry-on-by-default
3. **Provides opt-out** env var for users who want to disable RTK entirely

**Sister to gh-aw v48** W3C-style Security Architecture Specification (by-design defense) + **distinct from crawl4ai v29** event-based incident-response observation. Pattern #66 by-design sub-category now N=2.

**Supply-chain awareness sub-observation**: First corpus example of **OSS framework managing third-party binary lifecycle with telemetry-discipline-by-default**. Distinct from corpus precedents:
- shannon v45 = warns about authorization for security-testing
- gh-aw v48 = W3C spec + AWF firewall + MCP Gateway
- gsd-2 = managed third-party binary + force-disable upstream telemetry + user opt-out

## `gsd-orchestrator/SKILL.md` — agent skill exposing GSD-as-subprocess

This is **GSD-2's reflexive answer to its own architecture**: a skill (in agent-skill format with YAML frontmatter + openclaw metadata) that teaches OTHER agents how to orchestrate gsd-2 as a subprocess.

**Verbatim YAML metadata**:
```yaml
name: gsd-orchestrator
description: >
  Build software products autonomously via GSD headless mode. Handles the full
  lifecycle: write a spec, launch a build, poll for completion, handle blockers,
  track costs, and verify the result. Use when asked to "build something",
  "create a project", "run gsd", "check build status", or any task that
  requires autonomous software development via subprocess.
metadata:
  openclaw:
    requires:
      bins: [gsd]
    install:
      kind: node
      package: gsd-pi
      bins: [gsd]
```

**Pattern #18 observation**: gsd-2 ships an OpenClaw-format skill (per `metadata.openclaw` field) — confirms Pi SDK + OpenClaw runtime compatibility. Same Layer 0 / Layer 1 ecosystem as pi-mono v36 (which also targets OpenClaw alongside Claude Code).

## Mintlify docs site (commercial-quality docs infrastructure)

`mintlify-docs/introduction.mdx` opens with `<CardGroup cols={2}>` React-component cards: "Autonomous execution / Clean git history / Cost control / Crash recovery". This is **professional commercial-style documentation** distinct from typical README-only T1 frameworks.

**Pattern reference**: Joins claude-howto v32 (DeepWiki integration) + claude-context v40 (DeepWiki) + claude-code-best-practice v34 + bizos v37 (in-app `/guide` 800-line TSX) as corpus T1+T4 examples of dedicated documentation infrastructure. **gsd-2 = first Mintlify-specific docs site in corpus.**

## Decoupling architecture (v2.78 cmux ↔ gsd)

CHANGELOG v2.78.0 explicitly: *"cmux ↔ gsd decoupling — static cross-imports replaced with a shared `cmux-events` contract and dynamic imports, isolating extension boundaries."*

This is **architectural pattern reference**: cross-extension communication via **shared event contract module + dynamic imports**, not direct imports. Sister to vault routine v2.1 → v2.2 enhancement opportunity (decouple skill-to-skill via event contract).

## Topological extension load order (v2.78 Kahn's algorithm)

CHANGELOG: *"Topological extension load order — Kahn's-algorithm sort with surfaced `ExtensionLoadWarning`s, so dependent extensions resolve deterministically and misconfigurations are visible instead of silent."*

**First explicit Kahn's-algorithm extension load ordering in corpus**. Reference for vault skill-loading order (currently undefined / Claude loads in alphabetical order).

## Cross-references

- See `(C) Cluster 1` for README headline + VISION
- See `(C) Cluster 2` for 8-package monorepo + Pi SDK vendoring evidence
- See `(C) Entity 4` for Storm Bear meta — vault-architectural lessons from gsd-2
