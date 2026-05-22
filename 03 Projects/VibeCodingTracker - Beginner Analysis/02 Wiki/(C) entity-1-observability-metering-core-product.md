# (C) Entity 1 — Core product: AI-agent observability/metering + LiteLLM cost-attribution + 4-harness log-parsing + Rust-for-perf + Zero-Configuration auto-detection

**Type**: Core-product entity.

## What vct does (operationally)

The operator runs `vct` (in any shell). The tool:

1. **Auto-detects local logs** from supported harnesses (Claude Code + Codex + Copilot + Gemini) — no config files needed
2. **Parses each harness's native log format** — extracts session metadata, model usage, token counts, timestamps
3. **Resolves model names against LiteLLM pricing** via fuzzy matching (handles `gpt-4o-2024-11-20` → `gpt-4o`, `claude-opus-4-7` → `claude-opus-4` etc.)
4. **Computes real-time cost** per session, per harness, per model, per time window
5. **Outputs tabular or JSON results** (CLI-formatted; no GUI)

The tool is **operator-facing**, not agent-facing — operators run it on their own machine to see their own usage. It does **not** require integration with the harnesses themselves; it parses logs the harnesses already write to disk.

## Why Rust as primary language (97.1%)

vct selects **Rust** as the implementation language. Rationale (inferred):

1. **Performance** — log-parsing across hundreds of session files needs to be fast
2. **Memory efficiency** — README claims "<50 MB resident memory even with hundreds of sessions" — Rust's minimal-runtime + zero-cost-abstractions enable this
3. **Cross-platform distribution** — single binary via Cargo, no runtime dependency on operator's Node/Python version
4. **CLI-tool ergonomics** — Rust's `clap` crate ecosystem is well-developed for CLI tools

**CORPUS-FIRST Rust-primary T2 Service in v60+ window**. Prior T2 instances were TypeScript (v66 + v70) or Python (v85). Rust is a deliberate language choice signaling performance-sensitivity at the observability/metering layer.

This is a Library-vocab observation candidate "Rust as Performance-Sensitive T-Tier Language Choice" — but registering it would dilute Library-vocab layer with vague language-axis observations; held back at OC layer pending N=2.

## LiteLLM cost-attribution mechanism (CORPUS-FIRST)

LiteLLM (`BerriAI/litellm`) is an established Python library widely used for unified LLM API calls + pricing tables. vct uses it specifically for the **pricing-table component** with fuzzy matching:

### Why fuzzy matching matters

LLM model names evolve rapidly. Examples of name drift:

| Year-month | Model name pattern | Sample |
|---|---|---|
| 2023 | provider-version | `gpt-4` / `claude-2` |
| 2024 | provider-version-date | `gpt-4-1106-preview` / `claude-3-opus-20240229` |
| 2025 | provider-tier-version-date | `gpt-4o-2024-11-20` / `claude-opus-4` |
| 2026 | provider-tier-major-minor | `claude-opus-4-7` / `claude-sonnet-4-6` |

Exact-match pricing fails as names evolve. Fuzzy matching resolves variants to their canonical pricing entry.

### Daily-update mechanism

LiteLLM maintains a pricing JSON updated daily-or-near-daily via community + automated PRs. vct pulls this upstream data → no manual pricing-table maintenance for vct.

Library-vocab candidate **"Cost-Attribution-via-LiteLLM-Fuzzy-Model-Matching"** PROVISIONAL N=1 at v89. v95 N=2 watch — likely candidate as more AI-usage-trackers emerge.

## 4-harness log-parsing — Provider-Agnostic via Log-Parsing (Pattern #84 84c.1 NEW sub-sub-mechanism)

The 4 supported harnesses each write logs to standardized local paths. vct's auto-detection:

| Harness | Inferred log paths (per typical CLI tool conventions) |
|---|---|
| Claude Code | `~/.claude/` directory tree — sessions/conversations/transcripts |
| Codex | `~/.codex/` directory tree |
| Copilot | `~/.config/github-copilot/...` or `~/.copilot/...` |
| Gemini | `~/.gemini/` directory tree |

vct does NOT require the harnesses to know about vct. Each harness writes its native logs as part of normal operation; vct reads them passively.

This is a **NEW Pattern #84 84c.1 sub-sub-mechanism**: **"Provider-Agnostic via Log-Parsing at Observability Layer"** PROVISIONAL N=1, structurally distinct from existing 84c sub-sub-mechanisms:

| 84c sub-sub-mechanism | Mechanism | Layer | Provider-cooperation required |
|---|---|---|---|
| 84c.1 install-layer (repo-stored) | One tool deploys per-harness artifacts | Install | YES (harnesses must accept the artifact) |
| 84c.2 install-layer (CLI-generated) | One CLI generates harness-specific native formats | Install | YES |
| **84c.3 observability-layer (log-parsing)** | **One tool reads N harnesses' native logs** | **Observability** | **NO (harnesses agnostic to tool)** |

84c.3 represents a **complementary axis** of provider-agnosticism: read-only passive observability that requires zero vendor cooperation. This is structurally important because it shows the Pattern #84 84c sub-mechanism family extends beyond install-time configuration into runtime/post-runtime observation.

## Zero-Configuration auto-detection

vct auto-detects which harnesses are installed by checking for the existence of expected log directories. No `vct config init` step; no API keys needed (since vct only reads local logs, not vendor APIs).

This is **operator-friendly** at the cost of:
- vct silently ignores harnesses whose logs are in non-standard paths
- vct cannot track usage from cloud-based AI-agents that don't write local logs
- vct's "what harnesses am I tracking" answer is inferred, not declared

Library-vocab candidate **"Zero-Configuration via Auto-Detection at Observability Layer"** held at OC layer pending v95 N=2.

## CLI output formats

Based on typical Rust CLI tool conventions + README mentions:

| Output mode | Use case |
|---|---|
| Tabular (text) | Human-readable summary at terminal |
| JSON | Machine-readable for scripting / piping |
| (CSV inferred) | Spreadsheet export |

No web UI, no dashboard, no cloud sync. **Pure local CLI tool**. Aligns with the personal-productivity-tool profile.

## What Rust-for-perf + Zero-Configuration achieves jointly

The combination of Rust (perf) + Zero-Configuration (operator-friction-minimum) yields:

- **<50 MB resident memory** even with hundreds of sessions
- **Sub-second startup** (no Python/Node JIT warmup)
- **Single binary** (no runtime deps; Cargo install gives one executable)
- **Operator just runs it** — no learning curve, no config files, no API key setup

This is a deliberate **observability-at-zero-friction** design philosophy. Library-vocab candidate at OC layer "Observability-at-Zero-Friction Design Philosophy" pending v95 N=2.

## CORPUS-FIRST observations consolidated from this entity

1. **NEW T2 sub-archetype "AI-Agent Observability/Metering Tool"** PROVISIONAL N=1 (PRIMARY)
2. **CORPUS-FIRST Rust-primary T2 Service in v60+ window**
3. **CORPUS-FIRST LiteLLM cost-attribution mechanism in v60+ window**
4. **CORPUS-FIRST Provider-Agnostic via Log-Parsing at Observability Layer** = Pattern #84 84c.1 NEW sub-sub-mechanism 84c.3 candidate
5. **CORPUS-FIRST 5-distribution-channel matrix at single micro-scale subject**
6. **CORPUS-FIRST 3-locale Chinese-variant coverage at micro-scale**
7. **CORPUS-FIRST high-release-cadence at micro-scale anomaly** (59 releases + 397 commits + v0.10.2 in 5-mo + 8 stars)
8. **CORPUS-FIRST operator-facing T2 Service axis** (vs prior v66 + v70 + v85 all agent-facing T2)

## Pattern #57 sub-variant 57c-product MID density (4 corpus-subject overlaps)

vct cites 4 harnesses, of which 2 are direct corpus subjects and 2 are ecosystem-referenced:

| Harness | Status |
|---|---|
| Claude Code | v65 direct corpus subject |
| Codex | v62 direct corpus subject (T4 Bridge — codex-plugin-cc) |
| Copilot | Ecosystem-referenced (not in corpus directly) |
| Gemini | Ecosystem-referenced (referenced in v76 + v83 + v85) |

Pattern #57 sub-variant 57c-product MID density at 4 citations = matches v82 4-citation tier. Pattern #57 within-pattern strengthening.

## Pattern #82 within-pattern strengthening (quantitative-marketing)

vct README contains multiple quantitative-or-categorical claims:

- "<50 MB" resident memory
- "hundreds of sessions" scaling claim
- "Daily" pricing updates
- "Zero Configuration"
- 4 harnesses supported
- 5 distribution channels

Modest claim density but each claim is testable / verifiable. Pattern #82 quantitative-marketing within-pattern strengthening at observability-product surface (Library-vocab #9 Cross-Pattern Coupled-Design strengthening at 6+ pattern intersections in single MICRO-scale wiki).

## Pattern #66 supply-chain discipline within-pattern strengthening

vct ships:

- `Cargo.lock` (deterministic Rust dep resolution)
- `Cargo.toml` (declared deps)
- `Makefile` (build automation)
- `pre-commit-hooks` config (commit-time validation)
- `Dockerfile` (containerized build)
- `CLAUDE.md` (project context — interesting; vct uses Claude Code for development; eat-your-own-dogfood signal)

Pattern #66 supply-chain discipline at the **observability tool** layer is meaningful — vct is meant to be trusted with operator's local logs, so its own build-supply-chain hygiene matters more than for a typical CLI tool.

## What this entity does NOT cover

- **Per-harness log-format reverse-engineering detail** — wiki does not enumerate exact log paths or schemas per harness
- **Benchmark methodology** — README claims not measured/verified in this wiki
- **Comparison to other AI-usage-trackers** — wiki does not survey GitHub for sibling observability tools to validate "T2 Observability/Metering" novelty (N=1 status reflects in-corpus novelty only)
- **Pricing accuracy validation** — LiteLLM upstream accuracy not verified independently in this wiki

Mirrors the subject's own honesty discipline (Pattern #83 within-pattern). v90 audit may revisit if N=2 emergence or sibling observability tools surface in next wiki batch.
