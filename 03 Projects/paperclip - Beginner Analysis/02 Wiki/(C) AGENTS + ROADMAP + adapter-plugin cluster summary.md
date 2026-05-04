# (C) AGENTS + ROADMAP + adapter-plugin cluster summary — paperclip

> **Sources:** AGENTS.md (contributor guidelines) + ROADMAP.md (product trajectory) + adapter-plugin.md (extensibility refactor)
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

Three governance + trajectory documents. Together they answer:
- **AGENTS.md** — how do contributors build paperclip? (engineering contract)
- **ROADMAP.md** — where is paperclip going? (product direction + MAXIMIZER MODE)
- **adapter-plugin.md** — how does extensibility evolve? (in-flight refactor)

Clustered because they complement the README's "what is" with the "how built + where going + how extensible" dimensions.

## 2. AGENTS.md — engineering contract

### Core framing (verbatim from AGENTS.md)

> *"Paperclip is a control plane for AI-agent companies"*

**Control plane** is precise technical terminology — the layer that manages (orchestrates, authorizes, monitors) rather than executes. Kubernetes-adjacent framing.

### Essential reading order for contributors

Contributors are told to read (in order):
1. GOAL doc
2. PRODUCT doc
3. V1 implementation specs (`doc/SPEC-implementation.md`)
4. Development setup
5. Database structure

**Rigor:** contributors must understand product vision before touching code. Formal onboarding.

### Repository structure (stated)

- **Express API server** — core backend
- **React UI** — dashboard
- **Drizzle schemas** — DB abstraction
- **Shared type definitions** — monorepo types package
- **Agent adapters** — Claude, Codex, Cursor, etc
- **Documentation** — doc/ and docs/ folders

### Key engineering constraints

#### Constraint 1 — Company Scoping
> *"Every domain entity must enforce company boundaries at the route and service layers."*

Multi-tenancy enforced at architectural level, not optional. Data leakage between companies = critical bug.

#### Constraint 2 — Contract Synchronization
> *"Schema changes require updates across database, shared types, server routes, and UI clients — no partial updates."*

DB schema changes ripple through entire stack. Contributors must update all 4 layers atomically.

#### Constraint 3 — Control-Plane Invariants
> *"Preserve single-assignee tasks, atomic checkout semantics, approval gates, budget hard-stops, and activity logging."*

**5 invariants that MUST be preserved in all changes:**
1. Single-assignee tasks (no task has 2 agents)
2. Atomic checkout (agent claims task → executes → releases, no interruption)
3. Approval gates (governance checkpoints survive refactoring)
4. Budget hard-stops (cost limit enforcement always active)
5. Activity logging (audit log never bypassed)

**Interpretation:** these 5 primitives are paperclip's constitution. Everything else is implementation detail. Changes breaking any invariant are rejected.

### Development workflow

```bash
pnpm install && pnpm dev          # start with embedded PGlite
pnpm test                          # unit tests
pnpm test:e2e                      # Playwright E2E
pnpm db:generate                   # after schema changes
pnpm typecheck                     # before PR
pnpm build                         # verify build
```

### PR requirements

Every PR must fill `.github/PULL_REQUEST_TEMPLATE.md` with:
- **Thinking path** — reasoning captured
- **Changes** — what was done
- **Verification steps** — how to confirm it works
- **Risks** — what might break
- **Model attribution** — which AI helped (if any)
- **Completed checklist**

**"Model attribution"** is notable — acknowledges AI-generated contributions formally. Parallels BMAD's AI-generated code standards.

### Fork noted

HenkDz/paperclip — externalized Hermes adapter branch (removes built-in Hermes dependencies, allows plugin-based registration via Adapter Manager).

**Implication:** Hermes was previously built-in. Refactor-in-progress moves it out. adapter-plugin.md covers this work.

## 3. ROADMAP.md — product trajectory

### Completed milestones (✅)

Per ROADMAP:
- **Plugin system** for optional capabilities
- **Support for external agent workers** ("bring your own agent") — BYO Agent
- **Organization import/export** via `companies.sh`
- **Configuration through AGENTS.md files** — per-company agent config
- **Skill discovery and management** — skills/ system
- **Native scheduled routines** — Heartbeats
- **Enhanced budget controls and visibility**
- **Review/approval workflows as first-class features** — governance primitives

### Active development (⚪)

- **Multi-user collaboration** — moving from solo-operator to team-supervision. Enterprise prereq.
- **Sandboxed/cloud agent execution environments** — untrusted-agent isolation
- **Stronger artifact and work product visibility** — audit/review UX
- **Durable memory and knowledge systems** — cross-task persistent memory (parallel to codymaster v12 5-Tier Memory)
- **Stricter outcome enforcement rather than status updates** — force agents to produce deliverables, not just "in progress"
- **MAXIMIZER MODE** — higher-autonomy execution with visibility
- **Work queues for continuous intake** — support/triage/backlog as ongoing pipelines
- **Self-organizing capabilities within governance bounds** — agents reorganize team structure dynamically

### MAXIMIZER MODE — the direct alignment-theory feature

**Why it matters:**
- Name directly references paperclip-maximizer (Bostrom)
- Roadmap positions it as "higher-autonomy execution"
- "Within governance bounds" qualifier = the response to maximizer failure mode

**Design thesis (inferred):** if you can engineer bulletproof governance (approval gates + budget hard-stops + audit log), then higher autonomy is safe. MAXIMIZER MODE = stress-test of governance layer.

**Open question (Q5, Q6):** how literal? Feature naming alone is a safety signal (or ironic posturing).

### Notable trajectory

> *"Paperclip is still moving quickly"*

> *"No version targets or specific release dates"*

Intentional trajectory looseness. Open-source + community-driven prioritization. Fits community-platform archetype hypothesis.

## 4. adapter-plugin.md — extensibility refactor

### What's happening

paperclip's adapter system is **moving from hardcoded to runtime-registered**:

**Before:** adapters like Claude / Codex / Cursor / OpenClaw compiled into server binary
**After:** adapters dynamically registered at runtime via mutable registries

**Benefits:**
- New adapters without server rebuild
- Plugin manifest system can contribute adapters
- Server becomes "source of truth for is this adapter actually registered"

### Technical pattern

**Mutable registries on both server + UI layers:**
- Server registry = authoritative (queries confirm registration)
- UI registry = synchronized from server
- `/detect-model` routes — runtime model detection per adapter
- `adapterType` — taxonomy for adapter categorization

### Scope (explicit limitation)

> *"Avoids touching plugin manifest / plugin loader adapter contributions"*

The adapter-plugin.md refactor is **Phase 1**. Future phase will integrate with plugin manifest system (not visible in doc).

### Why this matters

**For extensibility:**
- Plugin authors can contribute adapters without server-level contributions
- Runtime model detection = better UX (user sees available adapters)
- Removes hardcoded Hermes (per fork note in AGENTS.md)

**For architecture:**
- Aligns with "thin core + extensible edges" thesis from ROADMAP
- Runtime registration = architectural maturity signal
- Mutable registries = non-trivial state management

## 5. The three documents as unified vision

Combining AGENTS.md + ROADMAP.md + adapter-plugin.md reveals paperclip's **architectural thesis**:

1. **Thin core with 5 invariants** (AGENTS.md) — single-assignee tasks / atomic checkout / approval gates / budget hard-stops / activity logging
2. **Extensible edges via plugins + adapters** (ROADMAP + adapter-plugin.md) — everything beyond invariants is pluggable
3. **Governance-first autonomy trajectory** (ROADMAP MAXIMIZER MODE) — higher autonomy ONLY WITHIN governance bounds

**Unified pattern:** paperclip claims to solve the alignment problem architecturally. Invariants are inviolable. Everything else is user-configurable extensibility.

**Skepticism:** "Solve alignment architecturally" is ambitious. Whether the 5 invariants are sufficient to prevent maximizer failure modes is empirical question, not engineering claim.

## 6. Comparison to corpus — engineering discipline

| Project | Contributor docs | Roadmap | Extensibility |
|---------|------------------|---------|---------------|
| **paperclip (v14)** | **AGENTS.md + PR template + 5 invariants** | **ROADMAP.md explicit with MAXIMIZER MODE** | **Runtime adapter registration (in refactor)** |
| gws (v13) | AGENTS.md 209 lines + tri-file | — | Dynamic Discovery at runtime |
| BMAD (v11) | AGENTS.md 3 rules minimal + CONTRIBUTING | CHANGELOG 5-phase | Module ecosystem (BMM/BMB/TEA/BMGD/CIS) |
| codymaster (v12) | `.claude-plugin/` manifest | Self-Healing implies | Plugin marketplace emerging |
| deer-flow (v9) | AGENTS.md substantial | — | Skill System progressive loading |

→ paperclip matches gws v13 in documentation rigor, exceeds peers in **governance-as-architecture** (5 invariants as constitution).

## 7. Control-plane invariants as design pattern

The 5 invariants from AGENTS.md §Control-Plane Invariants are **routine v2 candidate for Storm Bear vault**:

For vault analog:
1. **Single-assignee wiki** — one wiki per topic, no duplication
2. **Atomic publish** — wiki builds are complete or rolled back
3. **Approval gates** — user reviews before published/ folder updates
4. **Budget hard-stops** — routine v2 ~2h budget enforcement (already in backlog)
5. **Activity logging** — iteration logs (already present)

**Storm Bear has 2/5 approximated (4, 5). paperclip pattern suggests adding 1/2/3.**

## 8. Open questions surfaced

- Hermes adapter — what is it? Why externalized? (new — Q29)
- 5 invariants inviolable or aspirational? Violated in practice? (Q12)
- MAXIMIZER MODE implementation timeline? (Q5)
- Plugin manifest vs adapter refactor — when merge? (Q20)
- "Stricter outcome enforcement" — how measured? (Q24)
- Multi-user collaboration — prereq for enterprise adoption? (Q25)
- Docker packaging production-grade? (Q27)

## 9. Cross-references

- [[(C) README summary]] — user-facing positioning
- [[(C) Skills + Architecture + package.json cluster summary]] — tech-stack detail
- [[(C) Zero-Human Companies Orchestration + Governance Layer]] (Phase 3 entity) — invariants deep-dive
- [[(C) BYO Agent Adapter System + OpenClaw Standard]] (Phase 3 entity) — adapter refactor detail
