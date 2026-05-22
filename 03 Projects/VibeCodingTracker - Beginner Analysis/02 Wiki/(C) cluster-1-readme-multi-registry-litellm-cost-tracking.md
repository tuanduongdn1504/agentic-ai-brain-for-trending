# (C) Cluster 1 — README + multi-registry distribution + LiteLLM cost-tracking + 4-harness log-parsing

**Source**: [`README.md`](https://github.com/Mai0313/VibeCodingTracker/blob/main/README.md) (English primary) + `README_zh-TW.md` (Traditional Chinese) + `README_zh-CN.md` (Simplified Chinese) + repo file structure + release metadata (fetched 2026-05-22).

## What the product is

`VibeCodingTracker` (`vct`) is a **CLI observability/metering tool** that monitors AI coding assistant usage across multiple harnesses. It reads each harness's local logs, attributes usage to specific models, and computes real-time cost using LiteLLM's daily-updated pricing data with fuzzy model-name matching.

Tagline: *"Lightweight, fast, zero-config. Tracks Claude Code, Codex, Copilot, and Gemini."*

Core promise: **operator runs `vct`** → immediately sees usage totals + cost breakdown per harness + per model + per time window, with no manual configuration or API-key setup (the tool parses local log files; the harnesses do not need to know vct exists).

## CORPUS-FIRST T2 Service sub-archetype "AI-Agent Observability/Metering Tool"

This is a **NEW T2 Service sub-archetype** distinct from prior T2 instances:

| T2 Service sub-archetype | Wiki anchor | Mechanism |
|---|---|---|
| Memory/Persistence | v66 agentmemory | Agent state persistence backend |
| Code-Indexing/Knowledge-Graph | v70 codegraph | Pre-indexed knowledge graph queryable by agents |
| Design-Skill / Design-Language | v85 ui-ux-pro-max-skill | UI/UX skill bundle with codified design system |
| **Observability/Metering** | **v89 VibeCodingTracker** | **Usage + cost observability across multi-harness AI-agent ecosystem via log-parsing** |

**T2 Service tier reaches N=4 sub-archetype diversity at v89**. This is structurally significant — T2 tier has shown the most sub-archetype proliferation in the v60+ window, with 4 distinct sub-archetypes registered across 4 wikis.

PRIMARY observation for Phase 4b proposal-document.

## 4-harness log-parsing — Pattern #84 84c.1 NEW sub-sub-mechanism candidate

vct supports 4 explicit harnesses by parsing their respective local log formats:

| Harness | Log location (inferred from CLI tool patterns) | Corpus subject |
|---|---|---|
| Claude Code | `~/.claude/...` log/conversation files | v65 |
| Codex | `~/.codex/...` session logs | v62 |
| Copilot | (GitHub Copilot local logs) | (ecosystem) |
| Gemini | `~/.gemini/...` CLI logs | (ecosystem; referenced in v76+v83+v85 corpus) |

**4 explicit harness corpus-subject overlaps** — Pattern #57 sub-variant 57c-product MID density (vs v85 10 CORPUS-RECORD high; v88 5 mid; v83 7; v82 4 = matches v82 4-citation tier).

**Pattern #84 84c.1 NEW sub-sub-mechanism candidate "Provider-Agnostic via Log-Parsing at Observability Layer"** PROVISIONAL N=1 — distinct from prior 84c.1 sub-sub-mechanisms:

| 84c sub-sub-mechanism | Layer | Wiki anchor |
|---|---|---|
| 84c.1 install-layer (repo-stored multi-harness directories) | Install | v75 / v83 / v85 |
| 84c.2 generation-layer (CLI-generates-native-formats) | Install | v76 + v85 |
| **84c.3 observability-layer (Provider-Agnostic via Log-Parsing)** | **Observability** | **v89 VibeCodingTracker (NEW)** |

The observability-layer mechanism is fundamentally **inverse to install-layer mechanisms**: install-layer mechanisms make ONE tool work across N harnesses by deploying tool-specific artifacts to each harness; observability-layer mechanism reads N harnesses' native logs WITHOUT requiring any modification to the harnesses themselves. The harnesses are agnostic to vct's existence.

This represents a **complementary axis of provider-agnosticism** — install-side (vendor cooperation required) vs observability-side (no vendor cooperation required; passive log-parsing).

## CORPUS-FIRST LiteLLM cost-attribution

vct integrates with **LiteLLM** for daily-updated pricing data + fuzzy model-name matching. This is **CORPUS-FIRST cost-attribution mechanism in v60+ window**:

- **LiteLLM** = `BerriAI/litellm` widely-adopted Python library that maintains daily-updated pricing tables for 100+ LLM providers
- **Fuzzy model-name matching** = vct doesn't require exact model-name match; it resolves `gpt-4o-2024-11-20` against `gpt-4o` family pricing, etc.
- **Daily-updated** = no manual pricing-table maintenance needed; LiteLLM upstream handles price drift

Library-vocab candidate **"Cost-Attribution-via-LiteLLM-Fuzzy-Model-Matching"** PROVISIONAL N=1. Notable because it solves a real problem: pricing changes frequently (multiple per month across vendors), and exact-match pricing fails as model names evolve (`gpt-4-1106-preview` → `gpt-4-turbo` etc.).

## 5-distribution-channel matrix — CORPUS-FIRST in v60+ window

vct ships through **5 distinct package channels**:

| Channel | Package name | Distribution surface |
|---|---|---|
| **npm (unscoped)** | `vibe-coding-tracker` | Node.js / npm ecosystem |
| **npm (scoped)** | `@mai0313/vct` | Author-scoped npm namespace |
| **PyPI** | `vibe_coding_tracker` | Python pip ecosystem |
| **Cargo** | `vibe_coding_tracker` | Rust ecosystem |
| **Docker** | Provided Dockerfile | Containerized deployment |

**CORPUS-FIRST 5-distribution-channel matrix at single micro-scale subject** in v60+ window. Comparable subjects:

| Wiki | Distribution channels |
|---|---|
| v75 impeccable | File-copy across 14 harnesses (1 channel: source) |
| v76 agent-skills-standard | npm CLI + manifest (2 channels) |
| v82 huashu-design | `npx skills add` shorthand + git (2 channels) |
| v83 open-design | source + Docker + Electron + Vercel (4 channels) |
| v85 ui-ux-pro-max-skill | npm + Claude Marketplace + git + manual symlink (4 channels) |
| **v89 VibeCodingTracker** | **npm × 2 + PyPI + Cargo + Docker (5 channels)** = **NEW CORPUS-RECORD-HIGH at micro-scale** |

The 2-npm-names variant (unscoped + scoped) within the 5-channel matrix is itself a sub-pattern — author maintains both a discoverable short name and an author-scoped namespace.

Library-vocab candidate **"Multi-Registry Distribution Discipline at Single Subject"** PROVISIONAL N=1.

## 3-locale Chinese-variant coverage

vct ships **3 README locales**:

| File | Locale |
|---|---|
| `README.md` | English primary |
| `README_zh-TW.md` | Traditional Chinese (Taiwan / Hong Kong) |
| `README_zh-CN.md` | Simplified Chinese (Mainland China) |

**CORPUS-FIRST EN + zh-TW + zh-CN 3-locale at micro-scale subject** in v60+ window. The Traditional + Simplified Chinese split serves both Taiwan/HK and China-Mainland readers — meaningful distinction in Chinese-speaking markets given differing script + technical vocabulary conventions.

Comparable subjects:
- v77 easy-vibe: 13-locale at curriculum scale (mega-scale + community-org)
- v82 huashu-design: EN + zh single-Chinese (Simplified only)
- v87 claude-comstyle: EN + VN bilingual
- **v89 VibeCodingTracker**: EN + zh-TW + zh-CN 3-locale at micro-scale (NEW)

Library-vocab candidate **"3-Locale-Chinese-Variant Coverage at Micro-Scale Subject"** PROVISIONAL N=1.

## HIGH release-cadence anomaly at micro-scale

vct project metrics:
- **59 total releases** since project start
- **397 commits** on main branch
- **v0.10.2 latest** released 2026-05-21 (1 day before this wiki build)
- ~5-month project lifetime (inferred from v0.10.2 + semantic-versioning convention)
- **8 stars + 3 forks**

Derived ratios:
- **~12 releases/month average** = HIGH release-cadence
- **~79 commits/month average** = HIGH active-development
- **~7-releases-per-star** = anomalously HIGH (most repos at this star count have <5 releases lifetime)
- **~50-commits-per-star** = anomalously HIGH active-development density

This is a **micro-scale subject with mega-scale active-development signature**. Sister observation to Library-vocab "Coupled-Design Density Not Scale-Dependent" (v79 + v87 + v88 anchors); v89 strengthens that observation to N=4 with a different axis (release-cadence + commit-density rather than coupled-design density).

Library-vocab candidate **"High-Release-Cadence at Micro-Scale"** PROVISIONAL N=1.

Possible explanations:
- Author is **senior tech corporate engineer** (Google SWE) with disciplined release habit
- Tool is **personal-productivity tool** used by author himself (eat-your-own-dogfood); release cadence reflects internal demand
- Project may be **funnel-driven** with planned scaling (Wei Lee may anticipate broader adoption + is investing release-discipline ahead of demand)

## Quantitative-marketing claims — Pattern #82 within-pattern strengthening

README states:

> *"Ultra-Lightweight" — memory footprint under ~50 MB of resident memory even with hundreds of sessions*

> *"Zero Configuration" — automatically detects and processes logs from Claude Code, Codex, Copilot, and Gemini*

> *"Smart Pricing" — integrates with LiteLLM for daily pricing updates with fuzzy model matching*

3 quantitative-or-qualitative claims at product positioning level + 4-harness coverage + 5-distribution claim. Pattern #82 within-pattern strengthening at observability product surface.

## What is NOT in the README

- **No telemetry / metrics about real-world deployment** — claims are author-asserted, not measured-and-published
- **No per-harness fidelity benchmarks** — what % of usage events does vct miss / mis-attribute?
- **No multi-user / team-sharing model** — single-machine local-log-parsing pattern only
- **No cloud sync / centralized dashboard** — local CLI only
- **No web UI / chart visualization** — CLI output formats (tables, JSON) only
- **No API for external integrations** — CLI is the interface
- **No alerting / threshold notifications** (e.g. "you've used $X today")

These absences match **personal-productivity-tool profile**. Operator should evaluate if team-sharing or alerting are required before adoption.

## Storm Bear direct-applicability (synthesis)

Storm Bear runs intensive Claude Code usage (23+ wikis + audits in routine v2.2 window through v89; recent days have averaged ~1-2 wikis/day cadence). Cost-observability is meaningful actionable metric:

| Metric | Current operator visibility | With vct |
|---|---|---|
| Per-session cost | Unknown (operator pays Anthropic monthly) | Per-session attribution available |
| Per-model usage | Unknown (Opus vs Sonnet vs Haiku mix) | Per-model breakdown available |
| Daily/weekly/monthly trends | Unknown without manual log review | Aggregated trends available |
| Cross-harness consolidation | Unknown if any Codex/Gemini usage | Unified view across 4 harnesses |

**Pilot adoption candidate Tier-1 position #4**:
- Cost-of-trial: ~5 min via `cargo install vibe_coding_tracker` OR `npm install -g vibe-coding-tracker` OR `pip install vibe_coding_tracker` OR `docker run mai0313/vct`
- Reversible-via-uninstall
- Zero infrastructure friction
- No state mutation to vault content
- Read-only log-parsing (vct does not modify any harness state)

If operator wants cost-observability to inform pricing decisions or session-budget discipline, vct is a low-risk pilot.
