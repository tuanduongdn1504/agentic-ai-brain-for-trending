# Entity 2 — Platform-Primitive Foundation

> **Type:** PRIMARY Pattern Library deliverable — NEW candidate registration, corpus-first, N=1 stale-flagged
> **Cross-references:** [Cluster 3 iii-foundation](./cluster-3-iii-foundation-and-distribution.md) / [Entity 1 core](./entity-1-agentmemory-core.md) / [Phase 4b registration proposal](../01%20Analysis/(C)%20Pattern%20Platform-Primitive%20Foundation%20N=1%20registration%20proposal.md)

## The observation in one sentence

agentmemory is **built entirely on another platform's primitives, self-identifies as "a running instance" of that platform, counts itself in the platform's units, and is extended through the platform's own CLI** — a structural relationship distinct from "uses a framework as a dependency," and corpus-first across 65 wikis.

## The evidence (all verbatim-sourced)

### 1. Self-identification as an instance

README, "iii Engine Foundation" section:

> *"agentmemory **is already a running iii instance**. It uses iii primitives exclusively."*

The package.json description echoes it: *"Persistent memory for AI coding agents, powered by iii-engine's three primitives."* The project does not describe itself as *using* iii — it describes itself as *being* an iii instance.

### 2. Every infrastructure concern is delegated

| Concern | iii primitive | What agentmemory would otherwise roll |
|---|---|---|
| HTTP serving | HTTP Triggers | Express.js / Fastify |
| Storage + vectors | KV State | SQLite / Postgres + pgvector |
| Real-time streams | Streams | SSE / Socket.io |
| Process supervision | Worker Supervision | pm2 / systemd |
| Observability | OTEL Integration | Prometheus / Grafana |
| Plugin / extension system | Function Registry | Custom plugin system |

The README annotates each primitive with the thing it *"replaces"* — so the "0 external databases" headline claim is not a feature, it is a *consequence*: there is no database because KV State **is** the database, and KV State belongs to iii.

### 3. The dependency manifest proves it

`package.json` has **six runtime dependencies**. No HTTP framework, no DB driver, no ORM, no vector-DB client, no process manager, no metrics library. The entire infrastructure stack is the single line `"iii-sdk": "^0.11.2"`. The other five deps are application-level (2 Anthropic SDKs, a prompt wizard, dotenv, zod). A 107-endpoint REST server with triple-stream search and an OTEL trace surface having a six-line `package.json` is **only possible because the substrate is borrowed wholesale**.

### 4. It counts itself in the platform's units

README: *"118 source files · ~21,800 LOC · 800 tests · **123 functions · 34 KV scopes**."*

A normal project counts modules and database tables. agentmemory counts **iii Function Registry entries** and **iii KV State scopes**. Its internal vocabulary *is* the host platform's vocabulary.

### 5. Even extensibility belongs to the platform

You extend agentmemory by running iii-engine's CLI, not by installing an agentmemory plugin:

```bash
iii worker add iii-pubsub    # multi-instance fan-out
iii worker add iii-cron      # scheduled lifecycle
iii worker add iii-queue     # durable retries
iii worker add iii-sandbox   # isolated execution
```

This is the strongest single piece of N=1 evidence: **the project's own extension surface is the platform's, not its own.**

## Why this is distinct from existing patterns (overlap pre-check)

Per routine v2.2 Phase 0.6 candidate-overlap pre-check — checked against the confirmed + candidate list for >70% overlap:

| Existing pattern | Overlap? | Distinction |
|---|---|---|
| **Pattern #17 Ecosystem-Layer Organizations** | <70% — REJECT overlap | #17 is an *organizational/commercial* archetype (an org that operates as an ecosystem layer with a commercial platform). Platform-Primitive Foundation is a *technical-architecture* observation about a single project's substrate choice. Different axis entirely. |
| **Pattern #18 Agent Runtime Standardization** | <70% — REJECT overlap | #18 is about how a project reaches *multiple agent runtimes*. Platform-Primitive Foundation is about what a project is *built on*. agentmemory exhibits both, separately — the shared-backend mechanism is a #18 sub-archetype; the iii-foundation is this candidate. Orthogonal. |
| **Pattern #2 Distribution Evolution** | <70% — REJECT overlap | #2 is about packaging/delivery (`npx`, brew, etc.). This candidate is about the runtime substrate, not the distribution channel. |
| "uses a framework as a dependency" | not a pattern | Every TS project depends on frameworks. The distinction is *self-as-instance framing* + *exclusive delegation of all infrastructure* + *extension via host CLI* + *counting in host units*. The 4-part conjunction is what makes it a candidate, not the mere presence of a big dependency. |

**Conclusion:** no >70% overlap. Registers as a NEW top-level candidate.

## Proposed candidate definition

> **Platform-Primitive Foundation (CANDIDATE, N=1, stale-flagged):** A framework or service is built *entirely* on another platform's primitives — delegating *all* infrastructure concerns (HTTP / storage / streams / supervision / observability / extension) to the host platform — and signals this relationship structurally by (a) self-identifying as "a running instance" of the host, (b) counting its own internals in the host's units, and (c) exposing extensibility through the host's CLI rather than its own. Distinct from ordinary framework-dependency by the *exclusivity* of the delegation and the *self-as-instance* framing.

**4 registration criteria** (a subject must exhibit all 4 to count as evidence):
1. **Exclusive infrastructure delegation** — no self-rolled HTTP / DB / streams / supervision / observability
2. **Self-as-instance framing** — the project describes itself as *being* an instance of the host, not *using* the host
3. **Host-unit self-description** — internals counted in the host platform's vocabulary
4. **Host-CLI extensibility** — extended via the host's tooling, not the project's own plugin system

**N=1 evidence:** agentmemory v66 (built entirely on iii-engine; all 4 criteria met — see evidence sections 1-5 above).

## The built-in tension — coupling risk

Platform-Primitive Foundation is a power move *and* a liability, and agentmemory already shows the liability:

- `package.json` pins `iii-sdk: ^0.11.2`
- The CHANGELOG (Cluster 2) records: **iii-engine pinned to v0.11.2 because v0.11.6+ broke agentmemory** — *"users on v0.11.6+ must downgrade until refactor completes"*

When the foundation moves, the instance must move with it or freeze. A project that rolls its own infrastructure can absorb a breaking upstream change in one subsystem; a Platform-Primitive Foundation project takes the blast across its whole substrate at once. **This coupling-risk is intrinsic to the candidate and should be part of its definition** — it is the trait that would let an auditor distinguish a true Platform-Primitive Foundation from a project that merely leans heavily on one dependency.

## Stale-flag + un-stale criterion

**N=1 stale-flagged at v66.** Per routine v2.2 N=1-cold-start discipline:
- **Un-stale criterion:** a 2nd corpus subject meeting all 4 registration criteria (exclusive delegation + self-as-instance + host-unit self-description + host-CLI extensibility).
- **Stale-check schedule:** v68 (+2 wikis) and v71 (+5 wikis), per default N=1 stale-check cadence.
- **Plausible un-stale subjects:** other projects built on iii-engine; projects built entirely on Cloudflare Workers / Durable Objects with self-as-instance framing; projects built entirely on a BaaS (Supabase / Convex) substrate. The candidate is *not* iii-specific — iii-engine is just the N=1 host.

## Pattern Library implications snapshot

- **NEW candidate: Platform-Primitive Foundation** — N=1 (agentmemory v66), stale-flagged, 4 registration criteria, coupling-risk built into the definition. Full proposal: [Phase 4b registration proposal](../01%20Analysis/(C)%20Pattern%20Platform-Primitive%20Foundation%20N=1%20registration%20proposal.md).
- **Cross-pattern coupled-design observation** — Platform-Primitive Foundation co-occurs with the Pattern #18 shared-backend sub-archetype (Entity 3) in agentmemory: the iii-foundation is *what makes* the one-server-many-clients mechanism cheap to build. Observational coupling, not necessary — registered per Library-vocabulary item #9.
- **Overlap pre-check passed** — <70% overlap with Patterns #17, #18, #2.

## Why this entity matters

This is the **PRIMARY Pattern Library deliverable of the v66 wiki** — the corpus-first structural observation that justified building this wiki under the routine's "corpus-first observation → Phase 4b PRIMARY" discipline. Entity 1 describes what agentmemory does; **Entity 2 describes the one thing about it that the corpus has never seen before.** It is the most-referenced cross-link target of the v66 wiki, and the Phase 4b proposal-document is its formal registration artifact.
