# (C) Pattern #85 Platform-Primitive Foundation — N=1 registration proposal

> **Phase 4b PRIMARY deliverable — v66 agentmemory wiki**
> **Type:** NEW top-level candidate registration (not a promotion proposal — N=1 cold-start)
> **Proposed number:** Pattern #85 (highest existing candidate is #84 Cross-Vendor Ecosystem-Tolerance)
> **Status sought:** CANDIDATE, N=1, stale-flagged
> **Routine:** `llm-wiki-routine-v2.2` Phase 4b proposal-document discipline
> **Date:** 2026-05-14

---

## 1. Current status

**None — this is a new registration.** No existing confirmed or candidate pattern captures the observation. The overlap pre-check (§5) confirms <70% overlap with the nearest existing patterns (#17, #18, #2). This document proposes registering Pattern #85 as a CANDIDATE at N=1 with a stale-flag, per routine v2.2 N=1-cold-start discipline.

## 2. Proposed candidate definition

> **Pattern #85 — Platform-Primitive Foundation (CANDIDATE, N=1, stale-flagged):** A framework or service is built *entirely* on another platform's primitives — delegating *all* infrastructure concerns (HTTP serving / storage / streams / process supervision / observability / extension system) to the host platform — and signals this relationship structurally by (a) self-identifying as "a running instance" of the host, (b) counting its own internals in the host's units, and (c) exposing extensibility through the host's CLI rather than its own plugin system. Distinct from ordinary framework-dependency by the *exclusivity* of the delegation and the *self-as-instance* framing. Carries an intrinsic **coupling-risk**: when the foundation ships a breaking change, the instance takes the blast across its whole substrate at once.

### 4 registration criteria

A subject counts as evidence only if it exhibits **all 4**:

1. **Exclusive infrastructure delegation** — no self-rolled HTTP framework, DB/storage layer, stream layer, process supervisor, or observability stack
2. **Self-as-instance framing** — the project describes itself as *being* an instance of the host platform, not merely *using* it
3. **Host-unit self-description** — the project counts its own internals in the host platform's vocabulary
4. **Host-CLI extensibility** — the project is extended via the host's tooling, not via its own plugin/extension system

## 3. N=1 evidence — agentmemory v66 (4-criteria evaluation)

| Criterion | Verdict | Verbatim / structural evidence |
|---|---|---|
| **1. Exclusive infrastructure delegation** | ✅ PASS | README "iii Engine Foundation" maps every concern to an iii primitive: HTTP Triggers (replaces Express/Fastify) / KV State (replaces SQLite/Postgres+pgvector) / Streams (replaces SSE/Socket.io) / Worker Supervision (replaces pm2/systemd) / OTEL Integration (replaces Prometheus/Grafana) / Function Registry (replaces custom plugin systems). `package.json` has **6 runtime deps, none of which is an HTTP framework or DB driver** — the entire infrastructure stack is the single `iii-sdk ^0.11.2` line. The "0 external databases" headline claim is a *consequence* of this. |
| **2. Self-as-instance framing** | ✅ PASS | README, verbatim: *"agentmemory **is already a running iii instance**. It uses iii primitives exclusively."* package.json description: *"Persistent memory for AI coding agents, powered by iii-engine's three primitives."* The project never says "uses iii" — it says it *is* an iii instance. |
| **3. Host-unit self-description** | ✅ PASS | README: *"118 source files · ~21,800 LOC · 800 tests · **123 functions · 34 KV scopes**."* The last two units are iii-engine's own vocabulary — Function Registry entries and KV State scopes — not modules and tables. |
| **4. Host-CLI extensibility** | ✅ PASS | Extension is via iii-engine's CLI, not an agentmemory plugin system: `iii worker add iii-pubsub` / `iii-cron` / `iii-queue` / `iii-sandbox`. The upgrade path for new capability is the *host's* command, not the project's. |

**All 4 criteria PASS → agentmemory v66 is clean N=1 evidence.**

## 4. Structural distinctiveness — why this is a real observation, not a restatement

The candidate is **not** "this project has a big dependency." Every TypeScript project depends on frameworks. The structural claim rests on the **4-part conjunction**: exclusivity + self-as-instance framing + host-unit self-description + host-CLI extensibility. A project can have one or two of these (many projects lean heavily on, say, Next.js) without being a Platform-Primitive Foundation. agentmemory has all four, simultaneously, and states them explicitly.

The diagnostic trait that separates a true Platform-Primitive Foundation from a heavy-dependency project is **the coupling-risk made visible**: agentmemory pins `iii-sdk ^0.11.2` and the CHANGELOG records it had to *stay* pinned because iii-engine v0.11.6+ broke it (*"users on v0.11.6+ must downgrade until refactor completes"*). A heavy-dependency project absorbs an upstream break in one subsystem; a Platform-Primitive Foundation project takes it across the whole substrate. **The coupling-risk is part of the definition, not a footnote** — it is how a future auditor confirms the pattern rather than a near-miss.

## 5. Overlap pre-check (routine v2.2 Phase 0.6)

| Existing pattern | Overlap estimate | Distinction |
|---|---|---|
| **#17 Ecosystem-Layer Organizations** | ~25% | #17 is an *organizational/commercial* archetype (an org operating as an ecosystem layer with a commercial platform). #85 is a *technical-architecture* observation about one project's substrate choice. Different axis. agentmemory is not an ecosystem-layer *organization* — it's a solo project that happens to be built on a platform. |
| **#18 Agent Runtime Standardization** | ~30% | #18 is about how a project reaches *multiple agent runtimes* (coexistence / translation / shared-backend). #85 is about what a project is *built on*. agentmemory exhibits both, **separately** — its shared-backend mechanism is a #18 sub-archetype (registered separately at v66); its iii-foundation is #85. Orthogonal. |
| **#2 Distribution Evolution** | ~10% | #2 is about packaging/delivery channels (npx, brew, etc.). #85 is about the runtime substrate. agentmemory's `npx` distribution is #2; its iii-foundation is #85. |
| "uses a framework as a dependency" | n/a | Not a pattern. The 4-part conjunction (§2) is what distinguishes #85 from universal framework-dependency. |

**Conclusion: no >70% overlap.** Registers as a NEW top-level candidate. Per Phase 0.6 decision rule, option (a)-(d) evaluated: not (a) strengthen-existing (no host pattern), not (b) variant-within-pattern, not (c) meta-pattern-consolidation — **(d→register as new)**: register as new top-level candidate.

## 6. Why N=1 and not promotable yet

Per routine v2.2 promotion criteria, a candidate needs one of:
1. Structural N=2 (2 structurally-distinct instances)
2. Structural-unambiguity-at-N=2
3. Cross-archetype N=2/N=3
4. Mechanism-specificity at default ≥3-cross-tier
5. Sister-archive structural-N=2
6. NEW (v2.2): cross-archetype-as-6th-dimension

agentmemory is **N=1**. None of the promotion criteria can be met at N=1. Registration as a stale-flagged CANDIDATE is the correct disposition — this is a cold-start, and consolidation-forward discipline says register-and-wait, not promote-on-enthusiasm.

**Honest disclosure:** the observation is *vivid* (the README states it plainly, the package.json proves it) which creates promotion-enthusiasm pressure. Resisting that is the discipline. One striking N=1 is still N=1.

## 7. Stale-flag + un-stale criterion

**N=1 stale-flagged at v66.**

- **Un-stale criterion:** a 2nd corpus subject meeting **all 4** registration criteria (§2). Partial matches (e.g. exclusive delegation but no self-as-instance framing) do *not* un-stale — they are logged as near-miss observations.
- **Stale-check schedule:** **v68** (+2 wikis) and **v71** (+5 wikis), per default N=1 stale-check cadence.
- **Retire-if-still-N=1 trigger:** if still N=1 at v71, evaluate for retirement-via-absorption or observation-track demotion at the v71-window audit.

**Plausible un-stale subjects** (the candidate is NOT iii-specific):
- Other projects built entirely on iii-engine (iii-hq ecosystem)
- Projects built entirely on Cloudflare Workers + Durable Objects with self-as-instance framing
- Projects built entirely on a BaaS substrate (Supabase / Convex) that count themselves in the BaaS's units and extend via the BaaS CLI
- Projects built entirely on Deno Deploy / Val Town primitives

## 8. Sub-taxonomy decision

**No sub-taxonomy at registration.** At N=1 there is no structural diversity to taxonomize. If a 2nd instance arrives, the natural first sub-axis would be **host-platform type** (general-compute-platform like iii-engine vs edge-runtime like Workers vs BaaS like Supabase) — but that is a v68+ deliberation, explicitly deferred. Registering sub-taxonomy at N=1 would be premature fragmentation.

## 9. Cross-pattern coupled-design note (Library-vocabulary item #9)

At agentmemory v66, Pattern #85 (Platform-Primitive Foundation) **co-occurs** with the Pattern #18 shared-backend-service sub-archetype: the iii-foundation is *what makes* the one-server-many-clients mechanism cheap to build (iii's HTTP Triggers + KV State + Streams give the multi-client backend for free). This is an **observational coupling, not a necessary one** — a shared-backend service could be built on self-rolled infrastructure. Logged per Library-vocabulary item #9 (cross-pattern coupled-design correlations); not a promotion argument for either pattern.

## 10. Recommended verdict

**REGISTER Pattern #85 Platform-Primitive Foundation as CANDIDATE, N=1, stale-flagged.**

- Add to `_patterns/03-active-candidates.md` with the §2 definition + 4 criteria + §3 N=1 evidence + §7 stale-flag.
- Update `_patterns/05-recent-additions.md` v66 block.
- Active-candidate count: 26 → **27**. Ratio: 27:43 = **0.628:1** (was 0.605:1) — still healthy, buffer 0.322 below the 0.95:1 mini-audit trigger.
- Pre-register v68 + v71 stale-checks.

**No acceleration consideration applies** — acceleration is for promotion, not registration. This is a cold-start.

## 11. Audit checklist (for v68 stale-check operator)

At v68, the operator should:
- [ ] Check whether any v67-v68 wiki subject meets all 4 Pattern #85 criteria → un-stale to N=2 if so
- [ ] If un-staled: evaluate promotion criteria 1-6; consider host-platform-type sub-taxonomy
- [ ] If still N=1: preserve stale-flag, carry to v71
- [ ] Re-check the coupling-risk diagnostic — did agentmemory's iii-engine pin resolve, or did the coupling-risk materialize further? (informs whether coupling-risk stays in the definition)
- [ ] Cross-check against the v66 NEW observational candidate (AI-Generated-Repo Artifact Contamination) — unrelated, but both are v66 cold-starts on the same stale-check cadence

## 12. Evidence document cross-references

- **Entity 2 — Platform-Primitive Foundation:** `../02 Wiki/entity-2-platform-primitive-foundation.md` (full evidence sections 1-5, verbatim sources)
- **Cluster 3 — iii-engine foundation + distribution:** `../02 Wiki/cluster-3-iii-foundation-and-distribution.md` (source-level detail)
- **Entity 1 — agentmemory core:** `../02 Wiki/entity-1-agentmemory-core.md` (what the project does, for context)
- **CLAUDE.md Phase 0 probe:** `../CLAUDE.md` (Phase 4b PRIMARY pre-registration)
- **Primary sources:** agentmemory README.md (iii Engine Foundation section), package.json (6-dependency manifest), CHANGELOG.md (iii-engine v0.11.2 pin / v0.11.6 incompatibility)
