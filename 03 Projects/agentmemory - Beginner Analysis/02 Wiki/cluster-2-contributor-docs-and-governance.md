# Cluster 2 — Contributor docs + governance

> **Sources:** AGENTS.md, CHANGELOG.md, ROADMAP.md, the 11-file governance set, repo tree

## The 11-file governance set

agentmemory ships an **extensive** governance surface (Phase 0 Axis 8 = "7+ / extensive"):

```
README.md  CHANGELOG.md  CONTRIBUTING.md  CODE_OF_CONDUCT.md
DESIGN.md  GOVERNANCE.md  MAINTAINERS.md  SECURITY.md
AGENTS.md  ROADMAP.md  LICENSE
```

For a **35-day-old, solo-authored, pre-1.0 project**, 11 governance files is conspicuously heavy — it signals an *aspiration* to community maturity (GOVERNANCE.md + MAINTAINERS.md presuppose a governance structure and a maintainer roster that a solo project doesn't yet have). This is the setup for Cluster 2's central finding.

## ⚠️ Finding #1 — DESIGN.md is contaminated boilerplate

**`DESIGN.md` does not describe agentmemory.** It contains **288 lines of an unrelated "Design System Inspired by Lamborghini"** — a UI/brand design-system document: true-black color palettes (`#000000`, Lamborghini Gold `#FFC000`), the "LamboType" custom Neo-Grotesk typeface, Bootstrap grid notes, "nocturnal luxury" brand philosophy. **Zero** relation to memory tiers, consolidation, retrieval, or iii-engine.

This was **verified three ways**: two independent WebFetch calls and a raw `curl` of the file's bytes — all returned the same Lamborghini content. It is a real committed artifact, not a tooling glitch.

**Interpretation:** This is a **strong vibe-coded / AI-generated-scaffolding signal**. The most likely story: a template/agent pipeline was asked to "generate a DESIGN.md", produced the wrong artifact (or carried one over from a different scaffold), and it was committed without a human reading it. The governance set *looks* mature (11 files); one of those files is provably unreviewed.

**Corpus significance:** A new observational candidate — **AI-Generated-Repo Artifact Contamination**. The structural claim: repos that scaffold their governance surface with AI assistance can ship *plausible-looking-but-wrong* governance files, and file-count-based maturity proxies (Pattern #12 Governance-Depth) will over-credit them. agentmemory is the corpus-first clean instance of a *provably-contaminated* governance file.

## Finding #6 — but the CHANGELOG and ROADMAP are genuinely disciplined

The contamination story is *not* "low-effort repo." The contributor-facing docs that the author clearly *did* write are good:

### CHANGELOG.md — Keep-a-Changelog discipline

- Follows **Keep a Changelog v1.1.0** + **Semantic Versioning v2.0.0**
- Entries categorized into Added / Changed / Fixed / Security / Performance
- GitHub issue/PR references with contributor attribution
- **First version: `[0.8.0]` — 2026-04-09** ("Initial 0.8.x release") — this is the Phase 0 repo-age anchor (~35 days at v66 wiki ship)
- An `[Unreleased]` section with a performance-benchmarking harness in progress

### Finding #4 — the v0.8.2 six-vulnerability security batch

The CHANGELOG documents **six vulnerabilities fixed in `v0.8.2`** — the *second-ever* released version:

| Severity | Vulnerability |
|---|---|
| **CRITICAL** | Stored XSS in viewer via unsafe inline handlers |
| **CRITICAL** | RCE via `curl \| sh` in CLI startup |
| **HIGH** | Default `0.0.0.0` binding exposing the memory store to the local network |
| **HIGH** | Unauthenticated mesh sync missing `Authorization` header validation |
| **MEDIUM** | Path traversal in Obsidian export via unvalidated `vaultDir` |
| **MEDIUM** | Incomplete secret redaction missing token format patterns |

The initial public releases shipped with **two CRITICALs (one of them RCE)** and the memory store bound to all interfaces by default. They were caught and fixed within days — but they were public, in a memory tool that ingests everything an agent does. This is the second leg of the viral-velocity-outpacing-quality story (the first being DESIGN.md).

### Breaking-change honesty

The CHANGELOG tracks breaking changes explicitly and with candor:

- **v0.10** — iii-engine pinned to `v0.11.2`; *"users on v0.11.6+ must downgrade until refactor completes"* (an honest admission the project is behind its own foundation's releases)
- **v0.9.2** — default LLM provider changed to `noop`; subscription-fallback now requires `AGENTMEMORY_ALLOW_AGENT_SDK=true`
- **v0.8.10** — SessionStart context injection + PreToolUse enrichment made opt-in via `AGENTMEMORY_INJECT_CONTEXT`
- **v0.8.8** — LLM compression made opt-in via `AGENTMEMORY_AUTO_COMPRESS=true` — the changelog says it *"was default, burning tokens"*

That last entry is the tell: the project is willing to write "we shipped a default that burned your tokens, we fixed it" in its own changelog. **827 tests passing as of v0.9.2.** Honest caveats are documented (CJK tokenization still needs a segmenter; the iii-engine v0.11.6 incompatibility is tracked separately).

### ROADMAP.md — concrete and bounded

| Quarter | Theme | Contents |
|---|---|---|
| **Q2 2026** | Depth | Multimodal memory (image storage), governance documentation, additional connectors (filesystem shipped; GitHub planned) |
| **Q3 2026** | Breadth | **Multi-agent hook parity, cross-agent memory sharing**, community maintainer onboarding, OpenSSF alignment, knowledge-graph queries |
| **Q4 2026** | Trust | Enterprise: SSO, audit exports, RBAC, external security review |
| **V1.0** | Q1 2027 | REST + MCP surface freeze ("any break requires a major-version tag"), LTS branch `v1.x` with 12-month security commitments |

**Explicitly out of scope:** *"A cloud-hosted agentmemory SaaS"* and commercial licensing — *"deliberately excluded."* (Consistent with the Apache-2.0 license and the solo-community archetype.)

**Known limitations being addressed (the honest part):** single-agent isolation, limited connector ecosystem, missing enterprise deployment guides, performance-SLO documentation gaps.

## Finding #2 — README over-claims vs ROADMAP honesty

Put Cluster 1 and Cluster 2 side by side:

| Surface | Claim about cross-agent memory |
|---|---|
| **README** (Cluster 1) | *"One server, memories shared across all agents"* / *"Multi-agent support: MCP + REST + leases + signals"* — stated as **current capability** |
| **ROADMAP** (this cluster) | *"cross-agent memory sharing"* listed as a **Q3 2026 candidate**; *"single-agent isolation"* listed as a **current known limitation** |

The marketing surface is **ahead of** the implementation surface. This isn't dishonesty — the ROADMAP *is* the honest correction — it's that the two docs were written for different audiences and not reconciled. The contributor-facing doc tells the truth the user-facing doc oversells.

## Finding #3 — AGENTS.md version-skew

**AGENTS.md** is the contributor guide for AI coding agents working *on* agentmemory. Its content is genuinely useful:

- **Multi-file-sync discipline** — *"Adding MCP tools requires changes across 7 files"* (tools registry, server handlers, REST endpoints, test assertions, ...); *"Version bumps necessitate coordinated updates to 6 separate files."*
- **Boundary-validation discipline** — input validation at system boundaries (MCP handlers, REST endpoints), field whitelisting in REST handlers
- **Conventions** — `Promise.all` parallelism where feasible, content-addressable fingerprinting for deduplication, capture timestamps once
- **Build/test** — `tsdown` compiles TS → `dist/`; all tests must pass before PRs

But AGENTS.md **self-labels "Current Scope (v0.8.9): 44 MCP tools, 104 REST endpoints, 50+ internal functions, 12 hooks"** — while the README (v0.9.12) says **51 MCP tools, 107 endpoints**. The contributor doc is several versions behind the release cadence.

**The irony:** AGENTS.md is the very document that *codifies* a strict multi-file-sync discipline (a tool addition touches 7 files; a version bump touches 6) — and AGENTS.md itself is the file that fell out of sync. The discipline is documented faster than it is followed. This is **Pattern #81 Manifest-Drift-As-First-Class-CI-Concern** evidence from the *opposite* direction: agentmemory *names* the drift surface explicitly but still drifts.

## Pattern Library signals from Cluster 2

- **NEW observational candidate: AI-Generated-Repo Artifact Contamination** (Finding #1) — DESIGN.md is the corpus-first provably-contaminated governance file; file-count maturity proxies over-credit AI-scaffolded repos.
- **Pattern #12 Governance-Depth — counter-evidence nuance** — 11 files looks heavy/mature; DESIGN.md contamination + AGENTS.md skew show file *count* ≠ governance *substance*. The proxy is gameable by scaffolding.
- **Pattern #81 Manifest-Drift-As-First-Class-CI-Concern** — agentmemory's AGENTS.md explicitly names the multi-file-sync surface (7 files / 6 files) yet AGENTS.md itself drifts. Names-the-drift-and-drifts-anyway sub-observation.
- **Pattern #83 Honest-Deficiency-Disclosure Discipline — MIXED partial evidence** — CHANGELOG ("was default, burning tokens"; CJK caveat) + ROADMAP ("Known Limitations") are genuinely honest; but README over-claims (Finding #2). Disclosure discipline is real in contributor docs, absent in user-facing marketing. Registered as partial / counter-nuance evidence, **not** a clean N=3 strengthening of the v64+v65 N=2 candidate.
- **Pattern #66 Supply Chain Awareness** — privacy-by-design (secrets/`<private>` stripped before storage) + the v0.8.2 security batch as a *learning* event = a project that took a credibility hit on security and visibly corrected.
- **Pattern #52 EXTREME-VIRAL-VELOCITY — OBSERVATIONAL watch** — ~226 stars/day on a 35-day-old repo is just below the 300/day auto-flag, but the *quality-maturity-lag profile* (Findings #1-#4) is exactly what extreme velocity tends to produce. Watch-flag for v69 sustained-velocity re-check.
