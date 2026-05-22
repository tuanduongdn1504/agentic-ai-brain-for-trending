# (C) Phase 4b PRIMARY proposal — NEW T4 Bridge sub-archetype "Operator-Notification-Bridge via Messaging Platform" PROVISIONAL N=1 registration + T4 Bridge tier sub-typology formalization candidate at v90 audit

**Wiki**: v88 teleport (thith / Truong Hong Thi)
**Date**: 2026-05-22
**Decision target**: register NEW T4 Bridge sub-archetype "Operator-Notification-Bridge via Messaging Platform" PROVISIONAL N=1 at v88; **propose T4 Bridge tier sub-typology formalization at v90 audit** with 3-variant taxonomy (T4a cross-vendor cooperation + T4b credential-bridge + T4c operator-notification-bridge).
**Confidence**: HIGH (corpus-first novelty at sub-archetype layer + N=3 at parent-tier layer enabling formalization) / MEDIUM (sub-archetype N=1; sustainability unproven)

---

## What is being proposed

**Registration at v88**: NEW T4 Bridge sub-archetype with PROVISIONAL N=1 status, capturing the pattern observed in `thith/teleport`:

> **"Operator-Notification-Bridge via Messaging Platform"** — a T4 Bridge sub-archetype where the bridge connects AI coding agents (running on operator's local machine) to the operator's mobile/remote messaging channel (Telegram in v88) for out-of-band session-handoff: agent sends brief progress summaries, listens for reply-based instructions, resumes work autonomously.

**Proposal at v90 audit**: **T4 Bridge tier reaches N=3** (v62 + v67 + v88) enabling **sub-typology formalization** with 3-variant taxonomy:

| Sub-archetype | Wiki anchor | Mechanism | Bridge-direction |
|---|---|---|---|
| **T4a Cross-Vendor Cooperation** | v62 codex-plugin-cc | One harness embeds another vendor's tool | Vendor ↔ Vendor |
| **T4b Credential-Bridge** | v67 opencode-antigravity-auth | OAuth/auth flow between two services | Service ↔ Service |
| **T4c Operator-Notification-Bridge via Messaging Platform** | **v88 teleport** | Agent ↔ Operator via external messaging channel | **Agent ↔ Human** |

The 3-variant taxonomy spans the full Bridge axis: vendor-to-vendor + service-to-service + agent-to-human. Structurally complete coverage of the bridge-tier semantic space.

## Why this matters

T4 Bridge tier has had 2 instances prior to v88 (v62 + v67), each registering as a corpus-first sub-archetype but never formalized as a sub-typology. v88 reaches N=3, which is the standard threshold for sub-typology formalization (per Pattern #84 84a/b/c precedent at v72 + Pattern #18 sub-archetype B with B1/B2/B3 protocol-variants at v72).

The 3 sub-archetypes are **semantically distinct and span a complete bridge-axis**:

- **T4a (vendor-vendor)**: bridge enables one vendor's tool to operate inside another vendor's harness
- **T4b (service-service)**: bridge enables authentication / data flow between two backend services
- **T4c (agent-human)**: bridge enables the agent to reach the operator out-of-band

A 4th variant (e.g. "agent-to-agent" T4d if multiple agents collaborate across distinct platforms) is plausible but not yet evidenced. The current 3-variant taxonomy is complete for the present corpus.

## Why register at v88 (not defer entirely to v90)

Two-stage approach is recommended:

1. **At v88 wiki ship**: register NEW sub-archetype "Operator-Notification-Bridge via Messaging Platform" PROVISIONAL N=1 — capture the discovery and provisional naming
2. **At v90 audit**: formalize T4 Bridge tier sub-typology with 3-variant taxonomy (administrative-only if accepted; uses v88 wiki content as evidence anchor)

This split matches v85 + v86 precedent (Pattern #52 N=2 sub-class registered at v85 wiki + administrative-only PROMOTION at v86 audit).

## Why NOT a top-level Pattern

Sub-archetype layer is correct:

| Criterion for top-level Pattern | v88 status | Verdict |
|---|---|---|
| 1. Cross-tier N≥3 | N=3 within T4 Bridge tier only (single-tier) | FAIL (no cross-tier) |
| 2. Cross-author N≥2 | N=3 with 3 distinct authors (Anthropic-internal + Opencode authors + Truong) | PASS |
| 3. Cross-vertical | T4 Bridge sub-archetypes are all within Bridge vertical | FAIL |
| 4. Variant-within-pattern | 3-variant taxonomy emerges | PASS |
| 5. Methodology-influence-node evidence | STRONG for sub-typology formalization | PASS |

**2 of 5 criteria PASS — sufficient for sub-typology formalization but NOT for top-level Pattern promotion**. Sub-archetype is the correct vehicle.

## Why NOT a Library-vocab observation

T4c "Operator-Notification-Bridge" is **structural** (a sub-archetype with definable membership criteria + parent-tier-T4-Bridge inheritance), not a methodology-vocabulary item:

- Membership criterion: agent connects to operator's external messaging channel for out-of-band session-handoff
- Distinct from T4a + T4b membership criteria
- Sub-archetype inherits from T4 Bridge tier structural definition

Library-vocab is for methodology-vocabulary observations (e.g. v87's "Token-Economy-Quantification per Communication Style"). Sub-archetype is for structural sub-types within an existing tier. v88 = structural.

## Sub-archetype definition (formal)

**T4c Operator-Notification-Bridge via Messaging Platform**

| Field | Definition |
|---|---|
| Parent tier | T4 Bridge |
| Membership criterion | A standalone tool that connects (a) AI coding agents running locally on operator's machine, with (b) operator's external messaging channel (Telegram in v88; potentially Slack / Discord / email / SMS in future N), for the purpose of out-of-band session-handoff (agent-initiated status + operator-reply-based-resumption). |
| Distinguishing from T4a | T4a bridges vendor ↔ vendor (e.g. Codex inside Claude Code); T4c bridges agent ↔ human |
| Distinguishing from T4b | T4b bridges service-credentials (OAuth between services); T4c bridges status-and-instruction messages |
| Required properties | (1) Agent-initiated send capability; (2) Operator-reply-receive capability; (3) Out-of-band relative to the agent's local execution context; (4) Trigger-phrase-based invocation (natural language acceptable) |
| Common-but-not-required | Multi-harness support; zero-or-minimal dependencies; sibling/global config install; auto-execution-mode prerequisite |
| Anti-property (NOT) | Full-session-mirror (real-time conversation streaming); remote-control (operator issues all commands); permission-dialog-bridging (requires synchronous user interaction) |

## Evidence at v88 (single anchor for sub-archetype N=1)

| Evidence dimension | Detail |
|---|---|
| Bridge nature | thith/teleport explicitly connects Claude Code / Codex / Gemini / Cursor / Antigravity agents to operator's Telegram chat |
| Out-of-band scope | README states "while developers are away" — bridge is for the away-from-machine scenario |
| Agent-initiated | Agent sends progress updates triggered by "ping me on Telegram when done" |
| Operator-reply-resumption | Agent listens for replies; resumes work with new instructions |
| Bridge-direction agent ↔ human | Telegram operator is the human counterparty; not a vendor or service |
| Not full-session-mirror | README explicit "conversation stays local + only brief updates and concise replies transit" |
| Not remote-control | README explicit "out-of-band oversight, not remote-control" |

All 7 evidence dimensions confirmed via README + corpus-context cross-reference. T4c sub-archetype membership PASS at v88.

## v90 audit formalization checklist

If the v90 audit accepts T4 Bridge sub-typology formalization, the audit should:

1. **Register 3-variant taxonomy** (T4a + T4b + T4c) with N=1 each
2. **Re-anchor v62 + v67 + v88 entries** in the Pattern Library Tier-Taxonomy section under the new sub-typology
3. **Mark sub-typology as PROVISIONAL** until N=2 emerges in any sub-archetype (most likely T4c via Slack / Discord / email variants)
4. **Schedule v95 stale-check** for the formalization decision
5. **Optional**: include sister sub-archetype watch criteria (e.g. T4d "Agent-to-Agent Multi-Platform Cooperation" — speculative but possible)

## Risk acknowledgment

- **N=1 at sub-archetype layer is fragile** — if no future T4c instance emerges (no Slack / Discord / etc. messaging bridge in next 10 wikis), v100 retire-check could downgrade
- **3-variant taxonomy may be incomplete** — there could be Bridge sub-archetypes not yet observed; formalization at N=3 could lock in a premature taxonomy
- **Parent-tier T4 Bridge itself remains thin** — only 3 instances in 88-wiki corpus; not a high-prevalence tier
- **Sub-typology formalization is administrative not promotion-criteria-PASS** — should not be over-weighted in v90 batch

These risks support **PROVISIONAL** status throughout v90 + v95 windows.

## Sister Library-vocab candidates at OC layer (lower-weight)

v88 also contributes several Library-vocab observations at OC layer accompanying the PRIMARY:

| Library-vocab candidate | Evidence | Promotion target |
|---|---|---|
| "Zero-External-Dependency Bridge-Tool" | CORPUS-FIRST in v60+ window | v90 stale + v95 N=2 watch |
| "Clone-as-Sibling-Directory Install Pattern" | CORPUS-FIRST in v60+ window | v90 stale + v95 N=2 watch |
| "Canonical-Snippet Auto-Insertion across N Global Config Files" | CORPUS-FIRST 3-file simultaneous insertion | Pattern #84 84c.2 strengthening |
| "Multi-Language Natural-Language-Trigger for Bridge Functionality" | CORPUS-FIRST multi-language trigger phrases | v90 stale + v95 N=2 watch |
| "Local-Conversation-Plus-Bridge-Summaries Design Philosophy" | CORPUS-FIRST design philosophy at agent-bridge layer | v90 stale + v95 N=2 watch |
| "Auto-Execution-Mode Prerequisite for Out-of-Band Operation" | CORPUS-FIRST autonomy-level prerequisite at bridge layer | v90 stale + v95 N=2 watch |
| **"Engagement-Deficit-Extreme-With-Active-Forks"** | **v76 + v87 + v88 = N=3** | **v90 PROMOTION-ELIGIBLE** |
| **"Try-Once-and-Move-On Profile"** | **v79 + v87 + v88 = N=3** | **v90 PROMOTION-ELIGIBLE** |

The two PROMOTION-ELIGIBLE Library-vocab items (Engagement-Deficit + Try-Once) deserve v90 audit attention; both reach N=3 cross-wiki cross-author and could be promoted to CONFIRMED Library-vocab administrative-only at v90.

## Pattern #21 sub-variant strengthening (secondary)

v88 contributes a Pattern #21 sub-variant 21b candidate "Out-of-Band Session Handoff via Messaging Platform" — complements v73 cc-switch's 21a "Session-Handoff-Via-README-Checkpoint". Pattern #21 sub-variant layer reaches N=2 with 2-distinct-mechanism axes (manual-sync vs automated-async). Future v95 N=3 watch.

## Pattern #19 sub-mechanism strengthening + graveyard CONSOLIDATION proposal

v88 contributes Pattern #19 sub-mechanism candidate "VN-Web3-Founder-Building-Agent-Tooling" — but this WORSENS Pattern #19's PROVISIONAL N=1 graveyard from 11 to 12 candidates (11 still at N=1).

**Strong recommendation for v90 audit**: include a **Pattern #19 CONSOLIDATION proposal** that collapses 5 VN-related sub-mechanism candidates into a single "VN-Community Multi-Profile-Type" sub-mechanism CONFIRMED N=5 with sub-variants for profile-type-diversity. See Entity 3 for detail.

## Audit-queue implication

v88 contributes to v90 audit batch:

- 1 PRIMARY: T4 Bridge tier sub-typology formalization
- 6 Library-vocab carryovers
- 1 Pattern #21 sub-variant carryover
- 1 Pattern #19 sub-mechanism carryover (with consolidation proposal)
- 2 PROMOTION-ELIGIBLE Library-vocab items (Engagement-Deficit + Try-Once)
- 1 cluster-extension verification (6-wiki Asian + 5-wiki VN)
- 1 streak-record verification (3-consecutive-clean-PASS-post-OVERRIDE)
- = **~13 NEW v88 carryovers** to v90 batch

Combined with v86 inherited 13 + v87 NEW 5 + v88 NEW 13 = **~31 items projected for v90 batch** — approaching v86's 34-item CORPUS-RECORD.

## Recommendation

**REGISTER at v88 wiki**: NEW T4 Bridge sub-archetype "Operator-Notification-Bridge via Messaging Platform" PROVISIONAL N=1 with HIGH-novelty + MEDIUM-evidence-at-sub-archetype-layer + HIGH-evidence-at-parent-tier-layer.

**PROPOSE at v90 audit**: T4 Bridge tier sub-typology formalization with 3-variant taxonomy (T4a cross-vendor + T4b credential + T4c operator-notification); administrative-only if accepted.

**FIRST-CYCLE STALE-CHECK** at v90 + N=2 watch through v95 + retire-check at v100 if no T4c N=2 emergence.

---

## Sign-off

This proposal-document is the v88 Phase 4b PRIMARY artifact per routine v2.2 vehicle catalog. It accompanies the wiki entity pages (Entity 1 + Entity 2 + Entity 3) and the Pattern Library state-block updates in root CLAUDE.md.

Recommended state-block phrasing for root CLAUDE.md Pattern Library current-state section:

> *"v88 contributes 1 NEW T4 Bridge sub-archetype PROVISIONAL N=1 registration (Operator-Notification-Bridge via Messaging Platform) + 8 secondary OC carryovers (6 Library-vocab + Pattern #21 sub-variant 21b + Pattern #19 sub-mechanism candidate) + 2 N=3 PROMOTION-ELIGIBLE Library-vocab strengthenings (Engagement-Deficit-Extreme + Try-Once-and-Move-On) + 3-consecutive-clean-PASS-post-OVERRIDE NEW CORPUS-RECORD streak; T4 Bridge tier reaches N=3 (v62 + v67 + v88) enabling sub-typology formalization candidate at v90 audit (3-variant taxonomy T4a + T4b + T4c); state unchanged at 46 confirmed / 28 active / 0.609 ratio; Library-vocab CONFIRMED stays at 3."*

Storm Bear's blunt-and-direct rule encourages explicit acknowledgment of weaknesses: this proposal is HIGH on sub-typology formalization opportunity but LOW-MEDIUM on T4c sub-archetype N=1 sustainability; v100 retire-check is real risk if no T4c N=2 emerges.
