# Entity 3 — Distribution, ecosystem & the quality-maturity tension

> **Type:** Ecosystem entity + NEW observational candidate
> **Cross-references:** [Cluster 2 governance](./cluster-2-contributor-docs-and-governance.md) / [Cluster 3 distribution](./cluster-3-iii-foundation-and-distribution.md) / [Entity 1 core](./entity-1-agentmemory-core.md)

## Two stories, one repo

agentmemory is, simultaneously:
1. A **genuinely well-architected** memory engine with a research-paper-grade benchmark, a disciplined CHANGELOG, and a concrete ROADMAP.
2. A **35-day-old viral repo** that ships a contaminated governance file, fixed 6 CRITICAL/HIGH vulns at version 0.8.2, and over-claims in its README.

Both stories are true. This entity holds them together — because the *interesting* observation is not "is it good or bad," it's **what a repo looks like when viral velocity outpaces quality maturity.**

## The shared-backend distribution mechanism

agentmemory reaches 15+ agent platforms — but the *mechanism* is a NEW Pattern #18 sub-archetype (full analysis in Cluster 3):

| Mechanism | Corpus example | How |
|---|---|---|
| Layer 1 — **coexistence** | claude-seo v64 | parallel per-platform config files (CLAUDE.md + AGENTS.md + ...) |
| Layer 2 — **translation** | free-claude-code v60 (runtime), cc-sdd v61 (install-time) | translate one artifact into each platform's format |
| **NEW — shared-backend-service** | **agentmemory v66** | **one server, every platform is a client** |

The README's phrase is the mechanism name: *"One server, memories shared across all agents."* The physical footprint is `integrations/` (per-platform configs) + `.claude-plugin/` + `.codex-plugin/` (lifecycle-hook adapters) + `packages/mcp/` (the MCP server) — all thin clients pointing at one backend.

**Distribution:** `npx @agentmemory/agentmemory` — one command, launches server (3111) + viewer (3113). Apache-2.0, `tsdown`-built, Node ≥20, needs the `iii-engine` binary or Docker.

## The quality-maturity tension — five findings

### Finding #1 — DESIGN.md is contaminated boilerplate

`DESIGN.md` contains **288 lines of an unrelated "Design System Inspired by Lamborghini"** (color palettes, the "LamboType" typeface, "nocturnal luxury" brand copy). Zero relation to the memory engine. Verified via two WebFetches + a raw `curl`. A real committed artifact — the most likely story is an AI-scaffolding pipeline producing the wrong file and it being committed unreviewed.

### Finding #2 — README over-claims vs ROADMAP honesty

README sells *"memories shared across all agents"* as current; ROADMAP lists *"cross-agent memory sharing"* as a **Q3 2026 candidate** and *"single-agent isolation"* as a **current known limitation**. The marketing surface leads the implementation surface.

### Finding #3 — AGENTS.md version-skew

AGENTS.md self-labels *"Current Scope (v0.8.9): 44 MCP tools, 104 REST endpoints"*; README (v0.9.12) says 51 tools, 107 endpoints. The doc that *codifies* a strict multi-file-sync discipline (tool addition = 7 files; version bump = 6 files) is itself out of sync.

### Finding #4 — 6 CRITICAL/HIGH vulns at v0.8.2

The second-ever released version fixed: CRITICAL Stored XSS, CRITICAL RCE (`curl|sh` in CLI startup), HIGH `0.0.0.0` default binding, HIGH unauthenticated mesh sync, MEDIUM path traversal, MEDIUM incomplete secret redaction. Fixed within days — but shipped, public, in a tool that ingests everything an agent does.

### Finding #5 — yet the CHANGELOG and ROADMAP are genuinely disciplined

Keep-a-Changelog v1.1.0 format, explicit breaking-change tracking, the candid *"was default, burning tokens"* admission, honest caveats (CJK tokenization gap), a concrete quarterly ROADMAP, SaaS *"deliberately excluded."* The author *can* write good docs — which is what makes Findings #1-#4 a *maturity-lag* story, not a *low-effort* story.

## The synthesis — viral-velocity-outpacing-quality-maturity

Lay the engagement profile next to the findings:

| Signal | Value | Reading |
|---|---|---|
| stars/day | ~226 | viral attention |
| watchers/stars | 0.0029 | **very low** — drive-by stars, not committed followers |
| fork_ratio | 0.085 | moderate deployment intent |
| issues/stars | 0.0035 | low — few users engaged enough to file issues |
| repo age | ~35 days | no time for quality to catch up |
| DESIGN.md | contaminated | unreviewed governance scaffolding |
| v0.8.2 | 6 vulns | shipped-then-fixed security holes |

**The structural observation:** a repo can acquire 7,900 stars in 35 days faster than it can mature its quality surface. The stars are real (the idea is good, the benchmark is compelling); the **drive-by-stars-dominant** profile (near-zero watcher ratio) means most of those stars are bookmarks, not deployments. Meanwhile the contaminated DESIGN.md, the early vuln batch, the doc-skew, and the README/ROADMAP gap are all symptoms of the *same* root cause: **the project is being pulled forward by attention faster than a solo author can harden it.**

## NEW observational candidate — AI-Generated-Repo Artifact Contamination

**Registered as an observational candidate** (not a formal top-level candidate at N=1 — per consolidation-forward discipline):

> **AI-Generated-Repo Artifact Contamination (observational):** Repos that scaffold their governance/documentation surface with AI assistance can ship *plausible-looking-but-substantively-wrong* artifacts (e.g. a DESIGN.md describing an unrelated project). File-count-based maturity proxies — notably Pattern #12 Governance-Depth — over-credit such repos, because they count files without reading them. agentmemory v66 is the corpus-first *provably-contaminated* governance file.

**Why observational, not formal:** N=1, and it needs a 2nd instance before the structural claim is safe. **Bundled with it** is the broader *viral-velocity-outpacing-quality-maturity* observation — also observational, also N=1-clean, also routed consolidation-forward. Both queued for the v68/v69 stale-check.

**Counter-evidence value:** this finding is *useful against* Pattern #12 — it shows the governance-file-count proxy is gameable by scaffolding. An auditor seeing "11 governance files" should now ask "have they been read?"

## Cross-pattern signals from this entity

- **Pattern #18 — NEW sub-archetype: shared-backend-service** — 3rd multi-platform mechanism alongside Layer 1 coexistence + Layer 2 translation. Registered as a sub-archetype within the most-refined pattern in the library.
- **NEW observational candidate — AI-Generated-Repo Artifact Contamination** + viral-velocity-outpacing-quality-maturity. N=1, consolidation-forward, v68/v69 stale-check.
- **Pattern #12 Governance-Depth — counter-evidence** — file count ≠ governance substance; the proxy is gameable.
- **Pattern #81 Manifest-Drift-As-First-Class-CI-Concern** — agentmemory *names* its multi-file-sync surface in AGENTS.md, then AGENTS.md itself drifts. "Names-the-drift-and-drifts-anyway" sub-observation.
- **Pattern #83 Honest-Deficiency-Disclosure — MIXED** — disciplined CHANGELOG/ROADMAP vs over-claiming README. Partial/counter-nuance evidence, **not** a clean N=3 strengthening.
- **Pattern #52 EXTREME-VIRAL — OBSERVATIONAL watch** — ~226 stars/day is below the 300/day flag, but the quality-maturity-lag profile is what extreme velocity produces. v69 sustained-velocity re-check flag.
- **Pattern #66 Supply Chain Awareness** — privacy-by-design (secrets stripped pre-storage) + v0.8.2 as a visible learning event.

## Why this entity matters

Entity 1 says what agentmemory *does*; Entity 2 says what's *structurally novel* about it. **Entity 3 says what's structurally novel about its *condition*** — a repo caught mid-stride between a strong idea and a hardened product. For the Storm Bear pilot decision (Entity 4), this entity is the **risk register**: the architecture is sound, but the project is 35 days old, recently had an RCE, and ships unreviewed files. Deploy accordingly.
