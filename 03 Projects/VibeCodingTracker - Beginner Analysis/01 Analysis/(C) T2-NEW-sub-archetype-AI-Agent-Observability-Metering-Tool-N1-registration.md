# (C) Phase 4b PRIMARY proposal — NEW T2 Service sub-archetype "AI-Agent Observability/Metering Tool" PROVISIONAL N=1 registration

**Wiki**: v89 VibeCodingTracker (Mai0313 / Wei Lee)
**Date**: 2026-05-22
**Decision target**: register NEW T2 Service sub-archetype "AI-Agent Observability/Metering Tool" PROVISIONAL N=1 at v89; v90 first-cycle stale-check; v95 N=2 watch.
**Confidence**: HIGH (corpus-first novelty + T2 Service tier reaches N=4 sub-archetype diversity which strengthens sub-archetype-layer formalization) / MEDIUM (sub-archetype N=1 sustainability unproven; observability/metering domain plausibly recurring)

---

## What is being proposed

Register a NEW T2 Service tier sub-archetype with PROVISIONAL N=1 status:

> **"AI-Agent Observability/Metering Tool"** — a T2 Service sub-archetype where the tool monitors AI-coding-assistant (or AI-agent) usage across multiple harnesses via log-parsing or API-instrumentation, computes real-time cost via pricing-table integration, and exposes results to the operator (NOT to agents) via CLI/dashboard. Operator-facing (NOT agent-facing). Read-only / passive (does NOT modify harness state).

## Why this matters

T2 Service tier had 3 sub-archetypes in v60+ window before v89:

| Wiki | Sub-archetype | Mechanism |
|---|---|---|
| v66 | agentmemory | Memory/Persistence backend for agents |
| v70 | codegraph | Code-Indexing / Knowledge-Graph for agents |
| v85 | ui-ux-pro-max-skill | Design-Skill / Design-Language Service |
| **v89** | **VibeCodingTracker** | **Observability/Metering — usage + cost-tracking** |

v89 introduces a **structurally distinct 4th sub-archetype** characterized by 5 properties:

1. **Operator-facing** (NOT agent-facing) — the developer/operator runs the tool to see THEIR usage; agents are passive subjects
2. **Read-only / passive** — tool does NOT modify harness state; only reads logs
3. **Multi-harness coverage via log-parsing** — supports N harnesses by parsing their respective native log formats; no vendor cooperation needed
4. **Cost-attribution integration** — typically integrates with an upstream pricing table (LiteLLM in v89's case) for cost computation
5. **Lightweight resource footprint** — observability tools should not significantly burden the host machine (v89's "<50 MB resident memory" claim)

These 5 properties define a coherent sub-archetype that future similar tools should be evaluated against.

## Why NOT a top-level Pattern

Sub-archetype layer is correct:

| Criterion for top-level Pattern | v89 status | Verdict |
|---|---|---|
| 1. Cross-tier N≥3 | N=1 within T2 Service tier only (single-tier) | FAIL |
| 2. Cross-author N≥2 | N=1 with 1 author | FAIL |
| 3. Cross-vertical | Single-vertical observability | FAIL |
| 4. Variant-within-pattern | Not yet (N=1) | FAIL |
| 5. Methodology-influence-node evidence | STRONG for sub-archetype | PASS |

**1 of 5 criteria PASS — sufficient for sub-archetype registration but NOT for top-level Pattern**. Sub-archetype is correct vehicle.

## Why NOT a Library-vocab observation

v89's contribution is a **structural sub-archetype** with definable membership criteria (the 5 properties above) and parent-tier T2 Service inheritance — not a methodology-vocabulary observation.

Library-vocab is for cross-cutting methodology / vocabulary items (e.g. v87's "Token-Economy-Quantification per Communication Style"). v89's observability/metering tool is structural sub-typing within an established tier. Sub-archetype is the correct vehicle.

(The Library-vocab observations associated with v89 — LiteLLM cost-attribution + multi-registry distribution + 3-locale Chinese-variant + high-release-cadence — are registered as **sister Library-vocab candidates at OC layer**, not as the PRIMARY.)

## Sub-archetype definition (formal)

**T2 Service sub-archetype: AI-Agent Observability/Metering Tool**

| Field | Definition |
|---|---|
| Parent tier | T2 Service |
| Membership criterion | A standalone tool that (a) monitors AI-coding-assistant or AI-agent usage across multiple harnesses, (b) computes cost or other resource-attribution metrics via integration with upstream pricing/measurement data, (c) presents results to the operator via CLI/dashboard/API, (d) operates passively without modifying harness state, (e) maintains lightweight resource footprint to avoid burdening the host. |
| Distinguishing from v66 agentmemory | v66 is agent-facing persistence; v89 is operator-facing read-only observability |
| Distinguishing from v70 codegraph | v70 is agent-queryable knowledge backend; v89 is post-hoc usage observation tool |
| Distinguishing from v85 ui-ux-pro-max-skill | v85 is agent-consumed design knowledge; v89 is operator-consumed observability data |
| Required properties | (1) Multi-harness coverage; (2) cost-or-resource-attribution mechanism; (3) operator-facing interface; (4) read-only / non-mutating; (5) lightweight footprint |
| Common-but-not-required | Multi-registry distribution; auto-detection / zero-configuration; lightweight runtime language (Rust / Go); pricing-table upstream integration |
| Anti-property (NOT) | Mutating harness state; agent-facing API; requiring vendor cooperation; cloud-only / SaaS-only deployment |

## Evidence at v89 (single anchor for sub-archetype N=1)

| Evidence dimension | Detail |
|---|---|
| Multi-harness coverage | 4 explicit harnesses (Claude Code + Codex + Copilot + Gemini) via log-parsing |
| Cost-attribution mechanism | LiteLLM fuzzy-model-matching pricing integration |
| Operator-facing interface | CLI (text tabular + JSON outputs) |
| Read-only / non-mutating | Parses logs that harnesses already write to disk; vendor cooperation not required |
| Lightweight footprint | README claims "<50 MB resident memory even with hundreds of sessions" + Rust 97.1% primary lang |

All 5 evidence dimensions confirmed via README + repo inspection. Sub-archetype membership PASS at v89.

## v95 N=2 watch criteria

The sub-archetype should reach N=2 within 5-wiki window (v89 + 5 = v94 target). Candidate evidence for N=2:

- Another AI-coding-assistant usage tracker (likely; enterprise AI-agent adoption is growing; observability tools follow demand)
- A different cost-attribution mechanism (e.g. direct vendor API instrumentation rather than LiteLLM upstream)
- A non-CLI observability interface (web dashboard / Grafana plugin / Prometheus exporter)
- A multi-operator / team-sharing variant (cloud sync + centralized dashboard)

If any of these emerge in v89-v94 window with similar 5-property membership, N=2 PROMOTION-ELIGIBLE.

## v90 audit formalization checklist

If the v90 audit accepts the sub-archetype registration:

1. **Add to T2 Service tier sub-archetype table** in `PATTERN_LIBRARY.md` Tier-Taxonomy section
2. **Re-anchor v89 entry** under the new sub-archetype heading
3. **Mark as PROVISIONAL** with v95 N=2 watch + v100 retire-check default
4. **Note T2 Service tier 4-sub-archetype diversity** as a structural observation (T2 is the 2nd-most-diverse tier in v60+ window after T1 Assistant Skill)
5. **Optional**: include adjacent observability watch criteria (e.g. tool-vs-tool comparison; vendor-direct telemetry vs log-parsing approaches; etc.)

## Risk acknowledgment

- **N=1 at sub-archetype layer is fragile** — if no future T2 Observability/Metering Tool instance emerges in next 10 wikis, v100 retire-check could downgrade
- **The 5 membership properties may be overspecified** — N=2 evidence may shed light on which properties are load-bearing vs incidental; v95 audit should re-evaluate the property set
- **The "operator-facing T2 axis" claim is novel** — v66 + v70 + v85 are all agent-facing; v89 introduces operator-facing as a NEW T2 dimension; this is an aggressive structural claim that may need v95 N=2 corroboration before becoming load-bearing

These risks support **PROVISIONAL** status throughout v90 + v95 windows.

## Sister Library-vocab candidates at OC layer (lower-weight)

| Library-vocab candidate | Evidence at v89 | Promotion target |
|---|---|---|
| "Cost-Attribution-via-LiteLLM-Fuzzy-Model-Matching" | CORPUS-FIRST | v90 stale + v95 N=2 watch |
| "Multi-Registry Distribution Discipline at Single Subject" | 5-channel matrix | v90 stale + v95 N=2 watch |
| "3-Locale-Chinese-Variant Coverage at Micro-Scale" | EN + zh-TW + zh-CN | v90 stale + v95 N=2 watch |
| "High-Release-Cadence at Micro-Scale" | 59 releases + 397 commits at 8 stars | v90 stale + v95 N=2 watch |
| "Rust as Performance-Sensitive T-Tier Language Choice" | CORPUS-FIRST T2 in Rust | Held at OC pending N=2 |
| "Observability-at-Zero-Friction Design Philosophy" | Auto-detection + no config + single binary | Held at OC pending N=2 |
| **"Engagement-Deficit-Extreme-With-Active-Forks" N=4** | v76 + v87 + v88 + v89 | **PROMOTION-ELIGIBLE STRONGER at v90** |
| **"Try-Once-and-Move-On Profile" N=4** | v79 + v87 + v88 + v89 | **PROMOTION-ELIGIBLE STRONGER at v90** |
| **"Coupled-Design Density Not Scale-Dependent" N=4** | v79 + v87 + v88 + v89 | **PROMOTION-ELIGIBLE STRONGER at v90** |

## Pattern #84 84c.1 NEW sub-sub-mechanism 84c.3 candidate (secondary)

v89 contributes a Pattern #84 84c.1 NEW sub-sub-mechanism candidate **"Provider-Agnostic via Log-Parsing at Observability Layer"** PROVISIONAL N=1. Distinct from prior 84c sub-sub-mechanisms (84c.1 install-layer repo-stored + 84c.2 install-layer CLI-generated):

| 84c sub-sub-mechanism | Layer | Vendor-cooperation required |
|---|---|---|
| 84c.1 repo-stored | Install | YES |
| 84c.2 CLI-generated | Install | YES |
| **84c.3 log-parsing-observability** | **Observability** | **NO** |

84c.3 represents a **complementary axis** of provider-agnosticism. v90 audit should evaluate this as a Pattern #84 sub-sub-mechanism extension.

## Pattern #19 sub-mechanism — NOT registered at v89

A candidate for Pattern #19 "Taiwan-or-Chinese-diaspora-corporate-engineer-with-deep-multi-agent-framework-engagement" exists at observational level but is NOT registered at v89 due to Pattern #19 graveyard discipline (12-candidate layer post-v88; adding 13th would worsen v90 CONSOLIDATION pressure). See Entity 3 for detail.

## Audit-queue implication

v89 contributes to v90 audit batch:

- 1 PRIMARY: T2 Service NEW sub-archetype "AI-Agent Observability/Metering Tool" first-cycle stale-check
- 6 NEW Library-vocab candidates (Cost-Attribution + Multi-Registry + 3-Locale-Chinese + High-Release-Cadence + Pattern #84 84c.3 + Rust-T2 held at OC)
- 3 Library-vocab N=4 STRENGTHENING items (Engagement-Deficit + Try-Once + Coupled-Design-Density-Not-Scale-Dependent — PROMOTION-ELIGIBLE STRONGER)
- 1 Asian-cluster CORPUS-RECORD verification (7-wiki density)
- 1 streak verification (4-consecutive-clean-PASS-post-OVERRIDE NEW CORPUS-RECORD)
- 0 Pattern #19 sub-mechanism candidate registrations (graveyard discipline)
- = **~7 NEW v89 carryovers + 3 N=4 strengthening** → v90 batch grows

Combined with v86 inherited 13 + v87 NEW 5 + v88 NEW 13 + v89 NEW 7 = **~38 items projected for v90 batch** = **EXCEEDS v86's 34-item CORPUS-RECORD**.

## Recommendation

**REGISTER at v89 wiki**: NEW T2 Service sub-archetype "AI-Agent Observability/Metering Tool" PROVISIONAL N=1 with HIGH-novelty + MEDIUM-evidence-sustainability.

**FIRST-CYCLE STALE-CHECK** at v90.

**N=2 WATCH** through v94 + v95.

**RETIRE-CHECK** at v100 if no N=2 emergence.

**DO NOT FOLD** into existing T2 sub-archetypes — operator-facing axis is structurally distinct from v66/v70/v85 agent-facing services.

---

## Sign-off

This proposal-document is the v89 Phase 4b PRIMARY artifact per routine v2.2 vehicle catalog. It accompanies the wiki entity pages (Entity 1 + Entity 2 + Entity 3) and the Pattern Library state-block updates in root CLAUDE.md.

Recommended state-block phrasing for root CLAUDE.md Pattern Library current-state section:

> *"v89 contributes 1 NEW T2 Service sub-archetype PROVISIONAL N=1 registration (AI-Agent Observability/Metering Tool — operator-facing read-only observability via log-parsing) + 6 secondary OC carryovers (LiteLLM cost-attribution + 5-distribution-channel + 3-locale Chinese-variant + high-release-cadence + Pattern #84 84c.3 + Rust-T2 OC) + 3 N=4 PROMOTION-ELIGIBLE STRONGER Library-vocab strengthenings (Engagement-Deficit + Try-Once + Coupled-Design-Density-Not-Scale-Dependent) + 4-consecutive-clean-PASS-post-OVERRIDE NEW CORPUS-RECORD streak EXTENSION + 7-wiki Asian-LOCATED cluster CORPUS-RECORD-HIGH extension + 0 Pattern #19 sub-mechanism candidates (graveyard discipline); T2 Service tier reaches N=4 sub-archetype diversity (v66 memory + v70 indexing + v85 design + v89 observability) — second-most-diverse tier in v60+ window; state unchanged at 46 confirmed / 28 active / 0.609 ratio; Library-vocab CONFIRMED stays at 3."*

Storm Bear's blunt-and-direct rule encourages explicit acknowledgment of weaknesses: this proposal is HIGH on sub-archetype novelty + T2-tier-diversity argument, but LOW-MEDIUM on N=1 sub-archetype sustainability; v100 retire-check is real risk if no T2 Observability/Metering Tool N=2 emerges in next 10 wikis.
