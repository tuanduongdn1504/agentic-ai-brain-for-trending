# agentmemory — Beginner Analysis

> **Subject:** [`rohitg00/agentmemory`](https://github.com/rohitg00/agentmemory) — *"Persistent memory for AI coding agents, powered by iii-engine's three primitives."* Tagline: *"Your coding agent remembers everything. No more re-explaining."*
> **Wiki version:** v66
> **Build date:** 2026-05-14
> **Routine:** `llm-wiki-routine-v2.2` (Storm Bear vault — first wiki built under v2.2; v66 EARLY-OPERATOR-ELECTED mini-audit was v2.2's first audit)

---

## Phase 0 — Probe summary

### 13-axis classification (v2.2)

| Axis | Value |
|------|-------|
| **Tier** | **T2 Service** — persistent memory engine that runs as a long-lived server (ports 3111 REST / 3113 viewer), delivering memory-as-a-service via MCP (51 tools) + REST (107 endpoints). Strong **T4-bridge-adjacent** characteristics (one memory server shared across 15+ agent platforms) but the *core function* is a service, not a bridge. First **dedicated agent-memory-system** in the 65-wiki corpus. |
| **Archetype** | **Solo-community / founder-personal** — Rohit Ghumare (`ghumare64@gmail.com`), solo individual engineer. Ships GOVERNANCE.md + MAINTAINERS.md (community *aspiration*) but currently solo-authored. |
| **Scale tier** | **Medium (5-20K)** — 7,900 stars / 675 forks / 23 subscribers / 28 open issues / 51 PRs / 301 commits / 34 releases |
| **Primary lang** | **TypeScript 82.4%** (+ HTML 8.7% / JS 6.7% / CSS 1.5% / Python 0.7%) |
| **Packaging tool** | **npm** — `npx @agentmemory/agentmemory` (one-command startup) |
| **Origin story** | **Individual-author-lineage + built-on-iii-engine platform foundation** — solo engineer builds a memory engine *entirely* on the [iii-engine](https://github.com/iii-hq/iii) platform's primitives |
| **Methodology** | **NONE named** — but the **4-tier memory consolidation** model (Working → Episodic → Semantic → Procedural) is a memory-architecture concept explicitly *"inspired by human sleep consolidation"* + Ebbinghaus forgetting curve |
| **Governance file count** | **Extensive (11 files)** — README / CHANGELOG / CONTRIBUTING / CODE_OF_CONDUCT / DESIGN / GOVERNANCE / MAINTAINERS / SECURITY / AGENTS / ROADMAP / LICENSE — **BUT quality caveat: `DESIGN.md` is contaminated boilerplate** (288 lines of an unrelated "Lamborghini design system" — see Finding #1 below). Governance *depth* is partly theatrical. |
| **Agent/skill count** | **31-100** — 51 MCP tools (10 core + extended) + 12 auto-capture hooks + 4 skills + 6 resources + 3 prompts |
| **i18n coverage** | **EN-only** (README, AGENTS.md, all docs) |
| **Intellectual influence cited** | **Research-paper-chain** — Ebbinghaus forgetting curve + human sleep consolidation + **LongMemEval-S (ICLR 2025)** benchmark; competitive-comparison table cites **mem0** (53K⭐) + **Letta/MemGPT** (22K⭐) — neither yet in corpus |
| **Agent platforms supported** | **15+ explicitly named** ("32+" claimed): Claude Code (deepest — 12 hooks + MCP + skills) / Cursor / Claude Desktop / Cline / Roo Code / Windsurf / Gemini CLI / OpenCode / Codex CLI (6 hooks) / Hermes / OpenClaw / Goose / Aider / Kilo Code / pi / + any MCP-or-HTTP agent |
| **NEW v2.2: Living-Domain-Standards Tracking** | **NO** — does not codify external authoritative standards with versioned/deprecation-aware discipline |

### Velocity-screen + engagement-signal (v2.2)

| Metric | Value | Flag |
|---|---|---|
| **repo_age_days** | **≈ 35 days** — first release `[0.8.0]` 2026-04-09 per CHANGELOG (used as proxy; exact creation date not retrievable — `gh` CLI absent + GitHub API rate-limited from build environment) | within 90-day window |
| **stars_per_day** | **≈ 226/day** (7,900 / ~35) | **HIGH velocity — just below the 300/day EXTREME-VIRAL auto-flag**; Pattern #52 OBSERVATIONAL watch candidate |
| **fork_ratio** | **0.085** (675 / 7,900) | moderate — below the 0.15 HIGH active-deployment threshold |
| **watchers/stars** | **0.0029** (23 / 7,900) | **VERY LOW** — drive-by-stars-dominant signal |
| **open_issues/stars** | **0.0035** (28 / 7,900) | low |

**Engagement profile: drive-by-stars-dominant.** High star velocity + very low watcher ratio + moderate fork ratio + low issue ratio = viral attention outpacing deep engagement. Corroborated by Finding #1 (DESIGN.md contamination) + Finding #4 (6 CRITICAL/HIGH vulns fixed at v0.8.2, the 2nd-ever version).

### Tier placement decision

**T2 Service.** Justified by:
- Runs as a **long-lived server process** (ports 3111 REST / 3113 viewer) — infrastructure, not a one-shot tool
- Delivers **memory-as-a-service** consumed by agents via MCP (51 tools) + REST (107 endpoints)
- Not an agent/assistant itself (not T1), not a methodology/education resource (not T3), not *primarily* a bridge (not T4 — though it has strong bridge characteristics), not an end-user application (not T5)

**Alternative considered — T4 Bridge:** REJECTED as primary. agentmemory *does* bridge 15+ agents to a shared memory, but the bridging is a *consequence* of the service design, not the core function. codex-plugin-cc v62 (T4) exists *to* bridge; agentmemory exists to *remember* and reaches broadly as a side effect. Noted as T4-bridge-adjacent.

**Alternative considered — T1 Augmentation:** REJECTED. agentmemory ships Claude Code hooks + skills + a plugin, which *looks* T1, but those are thin client-adapters over a backend service. The substance is the server, not the augmentation surface.

### Phase 4b PRIMARY routing mode

**🎯 PRIMARY: NEW Pattern candidate proposal-document — "Platform-Primitive Foundation" (N=1, stale-flagged)**

**The corpus-first structural observation:** agentmemory is built *entirely* on another platform's primitives. The README states it plainly — *"agentmemory **is already a running iii instance**. It uses iii primitives exclusively."* It rolls **none** of its own infrastructure:

| Concern | agentmemory delegates to iii primitive | What it would normally roll itself |
|---|---|---|
| HTTP serving | HTTP Triggers | Express.js / Fastify |
| Storage + vectors | KV State | SQLite / Postgres + pgvector |
| Real-time streams | Streams | SSE / Socket.io |
| Process supervision | Worker Supervision | pm2 / systemd |
| Observability | OTEL Integration | Prometheus / Grafana |
| Plugin system | Function Registry | Custom plugin system |

This is distinct from "uses a framework as a dependency" (every TS project does that) — agentmemory **self-identifies as an instance of the host platform** and is extended via the host platform's own CLI (`iii worker add iii-pubsub` / `iii-cron` / `iii-queue` / `iii-sandbox`). N=1 in the 65-wiki corpus. Stale-flagged at registration; un-stale criterion = a 2nd subject built entirely-on-another-platform's-primitives with self-as-instance framing.

**Phase 4b deliverable:** formal proposal-document at `01 Analysis/(C) Pattern-NN Platform-Primitive Foundation N=1 registration proposal.md` per v2.2 proposal-document discipline.

### Secondary routing modes

- **Pattern #18 Agent Runtime Standardization — NEW sub-archetype: cross-agent shared-backend memory.** agentmemory supports 15+ platforms not via parallel per-platform config files (Pattern #18 Layer 1 coexistence) nor via protocol translation (Layer 2), but via **one shared backend service that all agents connect to**. A genuinely new mechanism within the most-refined pattern in the library (9+ refinements). Distinct sub-archetype candidate.
- **Pattern #8 Research-Benchmark Integration — first memory-retrieval-domain benchmark in corpus.** LongMemEval-S (ICLR 2025), 95.2% R@5, with explicit competitive-comparison table (vs mem0 68.5% / Letta-MemGPT 83.2%). Prior corpus benchmarks were ML-classification (magika v44), pentesting (shannon v45 XBOW), agent-task (Skyvern/OpenHands) — memory-retrieval is a new benchmark domain.
- **Pattern #28 Multi-Provider AI Support — STRONG dual-axis instance.** Multi-provider on TWO independent axes: LLM (Anthropic / Gemini / OpenRouter / MiniMax, auto-detected, *no default*) AND embeddings (free local `all-MiniLM-L6-v2` default / OpenAI / Voyage / Cohere / Gemini). Vendor-diversity-as-helpful-not-required, both axes.
- **NEW observational candidate: AI-Generated-Repo Artifact Contamination + viral-velocity-outpacing-quality-maturity.** See Findings #1-#5. A 35-day-old repo at ~226 stars/day ships a contaminated DESIGN.md, 6 CRITICAL/HIGH vulns at v0.8.2, AGENTS.md doc-skew, and a README/ROADMAP claim tension. Structural observation about vibe-coded repos riding viral waves faster than quality matures.
- **Pattern #83 Honest-Deficiency-Disclosure Discipline — MIXED partial evidence (NOT clean N=3).** CHANGELOG carries "honest caveats" (CJK tokenization gap, iii-engine v0.11.6 incompatibility); ROADMAP has an explicit "Known Limitations Being Addressed" section. BUT the README simultaneously *over-claims* (markets "memories shared across all agents" as current while ROADMAP lists cross-agent sharing as a Q3 2026 *candidate*). Disclosure discipline exists in contributor-facing docs but not user-facing marketing — a mixed signal, registered as partial/counter-nuance evidence, not a clean strengthening.
- **Pattern #57 Recursive Corpus Reference — 57c-product adjacency.** agentmemory's deepest integration target is Claude Code (THE most-corpus-cited product per v65); it ships `.claude-plugin/` + 12 Claude Code hooks. Also a structural sibling to vault project **graphify** (knowledge-graph builder) — agentmemory's triple-stream search includes a knowledge-graph traversal stream.
- **Pattern #12 Governance-Depth — counter-evidence nuance.** 11 governance files *looks* like heavy/mature governance, but DESIGN.md contamination + AGENTS.md version-skew show governance *file count* ≠ governance *substance*. Useful counter-evidence that Pattern #12's file-count proxy can be gamed by scaffolding.

### Phase 0.9 Storm Bear meta-entity check

**STRICT 1-of-4 inclusion check:**

| Criterion | Result | Evidence |
|---|---|---|
| (a) Author archetype peer | **PASS** | Rohit Ghumare = solo individual engineer shipping an open-source tool with personal-email attribution. Structural peer to Storm Bear (solo developer + Scrum coach building + publishing a personal vault). Not corporate / not large-team / not pseudonymous / not academic. |
| (b) Operational tool for vault | **STRONG PASS** | agentmemory is *literally* persistent memory for Claude Code — the **primary operating substrate of the Storm Bear vault** (this very wiki is being built in Claude Code). The vault already maintains a `memory/` directory + CLAUDE.md working memory by hand; agentmemory's deepest integration (12 hooks + MCP + skills) would automate exactly that. **Most directly-deployable subject in recent corpus** — not speculative-operational, direct-operational. |
| (c) Methodology-influence-node | **PASS** | The 4-tier consolidation model (Working/Episodic/Semantic/Procedural) + Ebbinghaus decay + triple-stream RRF search are memory-architecture methodologies *directly applicable* to how the vault organizes its own `memory/` system and CLAUDE.md working memory. Could inform routine v2.3 memory-discipline design. |
| (d) In-corpus reference | **PASS** | Integrates deeply with Claude Code (most-corpus-cited product, v65). Structural **sibling to vault project graphify** (knowledge-graph builder — agentmemory's graph search stream is the same primitive family). Cross-corpus reference detected on two axes. |

**Decision: 4-of-4 STRICT PASS → STRONG INCLUDE** (criterion (b) is STRONG; (a)(c)(d) are clear-PASS). Conservatively categorized **STRONG INCLUDE** rather than STRONGEST — criterion (d) is structural-sibling, not the "documents THE most-corpus-cited product's internals" depth that earned v65 its STRONGEST rating. Still, **4/4 STRICT PASS is the strongest *breadth* of Phase 0.9 criteria-coverage in the post-amendment window** (v65 was 3/4; most prior PASSes were 1-2/4).

**Streak counter:** v64 SKIP (RESET) → v65 STRONG PASS (streak 1) → **v66 STRONG PASS (streak advances to 2)**.

**10-instance Phase 0.9 post-amendment window v57-v66:** v57 PASS / v58 PASS / v59 SKIP / v60 PASS / v61 PASS / v62 PASS / v63 PASS / v64 SKIP / v65 PASS / **v66 PASS** = **8 PASS / 2 SKIP = 80% INCLUDE rate** (held steady from v65).

### Entity slot allocation

- **Entity 1** — agentmemory core artifact: 4-tier memory engine + triple-stream RRF search + 51 MCP tools + 12 auto-capture hooks + privacy-by-design (what it IS / what it DOES)
- **Entity 2** — Platform-Primitive Foundation (**PRIMARY Pattern Library deliverable**): built-entirely-on-iii-engine, the corpus-first structural observation; most-referenced cross-link target
- **Entity 3** — Distribution + ecosystem + quality-maturity tension: 15+ platform integrations, iii-engine relationship, npm distribution, REST/MCP surfaces, AND the viral-velocity-vs-quality findings (DESIGN.md contamination, 6 early vulns, doc skew, README/ROADMAP tension)
- **Entity 4** — **Storm Bear meta-entity**: pilot candidacy (highest-relevance pilot subject in recent corpus) + vault memory-architecture relevance + Phase 0.9 4/4-STRICT-PASS evidence

---

## Phase 0 Findings (carry into Phase 2/3 — verbatim-sourced)

**Finding #1 — `DESIGN.md` content contamination (verified, not a fetch bug).** agentmemory's `DESIGN.md` contains 288 lines of *"Design System Inspired by Lamborghini"* — a UI/brand design-system document (color palettes, LamboType typeface, Bootstrap grid) with **zero relation** to the memory engine. Confirmed via two independent WebFetch calls + a raw `curl` of the file bytes. This is a real committed artifact, not a tooling glitch. Strong **vibe-coded / AI-generated-scaffolding** signal — a "generate a DESIGN.md" task in a template pipeline produced the wrong artifact and it was committed without review.

**Finding #2 — README over-claims vs ROADMAP honesty.** README markets *"One server, memories shared across all agents"* + *"Multi-agent support: MCP + REST + leases + signals"* as current capability. ROADMAP lists *"cross-agent memory sharing"* as a **Q3 2026 candidate** and *"Single-agent isolation"* as a **current known limitation**. Marketing surface is ahead of implementation surface.

**Finding #3 — AGENTS.md version-skew.** AGENTS.md self-labels *"Current Scope (v0.8.9): 44 MCP tools, 104 REST endpoints"*; README (v0.9.12) says 51 MCP tools, 107 endpoints. Contributor docs are not synced to the release cadence — ironic for a project whose AGENTS.md itself documents a strict multi-file-sync discipline (adding an MCP tool = 7 files; a version bump = 6 files).

**Finding #4 — 6 CRITICAL/HIGH vulns fixed at v0.8.2 (the 2nd-ever version).** CHANGELOG documents v0.8.2 fixing: [CRITICAL] Stored XSS in viewer, [CRITICAL] RCE via `curl | sh` in CLI startup, [HIGH] default `0.0.0.0` binding exposing the memory store to the local network, [HIGH] unauthenticated mesh sync, [MEDIUM] path traversal in Obsidian export, [MEDIUM] incomplete secret redaction. The initial public releases shipped with serious holes; they were fixed fast, but the holes existed and were public.

**Finding #5 — disciplined CHANGELOG + ROADMAP despite the above.** CHANGELOG follows Keep-a-Changelog v1.1.0 + SemVer v2.0.0, tracks breaking changes explicitly (v0.10 iii-engine pin, v0.9.2 default-provider→noop, v0.8.8 LLM-compression-was-default-"burning tokens"), and carries honest caveats. ROADMAP is concrete (V1.0 Q1 2027, quarterly themes, explicit "Known Limitations", SaaS "deliberately excluded"). The contributor-facing discipline is genuinely good — which is what makes Findings #1-#4 a *quality-maturity-lag* story rather than a *low-effort-repo* story.

**Finding #6 — privacy-by-design is a real architectural choice.** API keys, secrets, and `<private>`-tagged content are stripped before storage. `AGENTMEMORY_SECRET` bearer token protects REST endpoints. This is a credible security posture *in the v0.9.x design* — notable given Finding #4's v0.8.2 history (the team learned).

---

## Sources ingested (Phase 2 will write 3 cluster summaries)

1. **README.md** — full overview: tagline + 4-tier architecture + triple-stream search + 51 MCP tools + 12 hooks + 15+ platform table + iii-engine foundation + REST API + config + competitive-comparison table
2. **package.json** — `@agentmemory/agentmemory` v0.9.12 / Apache-2.0 / author Rohit Ghumare / deps: `@anthropic-ai/claude-agent-sdk` ^0.2.56 + `@anthropic-ai/sdk` ^0.39.0 + `iii-sdk` ^0.11.2 + `zod` ^4 + `dotenv` + `@clack/prompts`
3. **AGENTS.md** — contributor guidance: multi-file-sync discipline (MCP tool = 7 files, version bump = 6 files) + input-validation-at-boundaries + content-addressable fingerprinting + tsdown build + 699+ tests (v0.8.9 skew)
4. **CHANGELOG.md** — Keep-a-Changelog format / first version [0.8.0] 2026-04-09 / v0.8.2 6-vuln security batch / breaking-change tracking / 827 tests at v0.9.2 / honest caveats
5. **ROADMAP.md** — V1.0 Q1 2027 / Q2 Depth (multimodal) / Q3 Breadth (cross-agent sharing, OpenSSF) / Q4 Trust (SSO/RBAC/external security review) / explicit known limitations / SaaS out-of-scope
6. **DESIGN.md** — ⚠️ **CONTAMINATED** — 288 lines of unrelated "Lamborghini design system" content; NOT usable as agentmemory architecture source (see Finding #1)
7. **Repo tree + metadata** — 11 governance files / dirs: src, test, plugin, packages/mcp, integrations, examples/python, benchmark, website, assets, .claude-plugin, .codex-plugin / 7,900 stars / 675 forks / 301 commits / 34 releases

---

## Cross-wiki siblings (mandatory cross-references)

**Knowledge-graph / memory-primitive sibling:**
- [graphify](../graphify%20-%20Beginner%20Analysis/) — knowledge-graph builder; agentmemory's triple-stream search includes a knowledge-graph traversal stream (shared primitive family)

**Claude-Code-host integration peers:**
- [claude-code-system-prompts v65](../claude-code-system-prompts%20-%20Beginner%20Analysis/) — Claude Code internals reference; agentmemory ships `.claude-plugin/` + 12 Claude Code hooks
- [codex-plugin-cc v62](../codex-plugin-cc%20-%20Beginner%20Analysis/) — also ships a `.codex-plugin/`; cross-vendor plugin packaging sibling
- [free-claude-code v60](../free-claude-code%20-%20Beginner%20Analysis/) — T2-adjacent infrastructure/proxy sibling

**T2 service / multi-platform peers:**
- [n8n v56](../n8n%20-%20Beginner%20Analysis/) — T2 service (workflow automation); MCP-server-trigger comparison
- [cc-sdd v61](../cc-sdd%20-%20Beginner%20Analysis/) — multi-platform support sibling (8 platforms via install-time translation vs agentmemory's shared-backend mechanism)

---

## Build status

| Phase | Status |
|---|---|
| Phase 0 (probe) | ✅ COMPLETE |
| Phase 1 (scaffold) | ✅ COMPLETE |
| Phase 2 (sources — 3 cluster summaries) | ✅ COMPLETE |
| Phase 3 (entities — 4 pages, Storm Bear meta-entity INCLUDED per Phase 0.9 4/4 STRICT PASS) | ✅ COMPLETE |
| Phase 4a (beginner guide — bilingual VN/EN) | ✅ COMPLETE |
| Phase 4b (Platform-Primitive Foundation N=1 registration proposal — Pattern #85) | ✅ COMPLETE |
| Phase 5 (iteration log + Pattern Library update — `_patterns/03` + `_patterns/05`) | ✅ COMPLETE |
| Phase 6 (vault sync — root CLAUDE.md + PATTERN_LIBRARY.md + GOALS.md) | ✅ COMPLETE |

**v66 agentmemory wiki — BUILD COMPLETE 2026-05-14.** 11 project files + 4 vault-state updates (`_patterns/03-active-candidates.md`, `_patterns/05-recent-additions.md`, root `CLAUDE.md`, `PATTERN_LIBRARY.md`, `GOALS.md`). Housekeeping flag raised: PATTERN_LIBRARY.md + GOALS.md shims drifted v60/v55 → v66 — counts synced, narrative re-write deferred to v68 housekeeping.
