# (C) ARCHITECTURE + CHANGELOG Summary

> **Sources:**
> - `docs/AGENTS.md` (agent reference, covered in README summary)
> - `docs/ARCHITECTURE.md` (not deep-read; inferred from README Why It Works section)
> - `CHANGELOG.md` (2222 lines) — **skim-first** (grep version headers + read latest 5 entries)
>
> **Ingested:** 2026-04-18
> **Routine context:** Source #3 of 3 (Phase 2)

---

## TL;DR

**VI:** Source #3 synthesizes: (1) **Agent Architecture** — thin orchestrators spawn specialized agents with fresh context windows (33 agents in folder, 21 categorized in docs); (2) **CHANGELOG skim** — 2,222 lines covering versions from early to v1.37.1 (2026-04-17); (3) **Distinctive ideas từ changelog** — Ingest Docs command, Agent size-budget enforcement, Spiking+Sketching, workstreams. Conservative-sounding "mature project" signals.

**EN:** Agent Architecture (thin orchestrators + 33 specialized agents) + CHANGELOG skim (2,222 lines, v1.37.1 latest). Mature project signals with disciplined release notes.

---

## Part 1: Agent Architecture (docs/AGENTS.md summary)

### Design principle

> "GSD uses a multi-agent architecture where thin orchestrators (workflow files) spawn specialized agents with fresh context windows. Each agent has a focused role, limited tool access, and produces specific artifacts."

**Match Superpowers's SDD pattern + gstack's `/autoplan` pattern.** Convergent architecture.

### 21 agents trong docs (categorized)

| Category | Count | Agents |
|----------|-------|--------|
| Researchers | 3 | project-researcher, phase-researcher, ui-researcher |
| Analyzers | 2 | assumptions-analyzer, advisor-researcher |
| Synthesizers | 1 | research-synthesizer |
| Planners | 1 | planner |
| Roadmappers | 1 | roadmapper |
| Executors | 1 | executor |
| Checkers | 3 | plan-checker, integration-checker, ui-checker |
| Verifiers | 1 | verifier |
| Auditors | 3 | nyquist-auditor, ui-auditor, security-auditor |
| Mappers | 1 | codebase-mapper |
| Debuggers | 1 | debugger |
| Doc Writers | 2 | doc-writer, doc-verifier |
| Profilers | 1 | user-profiler |

### 33 agents trong folder (discrepancy)

**Extras not in docs/AGENTS.md:**
- ai-researcher
- code-fixer
- code-reviewer
- debug-session-manager
- doc-classifier
- doc-synthesizer
- domain-researcher
- eval-auditor
- eval-planner
- framework-selector
- intel-updater
- pattern-mapper
- phase-researcher (in docs)

→ **12+ extras trong folder.** Docs lag behind code. **Flag as TODO: verify canonical count.**

### Thin orchestrator pattern

Orchestrators = workflow files (not agents). They:
1. Spawn agents với fresh context windows
2. Wait for results
3. Route to next step
4. Never do heavy lifting

**Result:** Main context stays 30-40% usage. Agents take burden.

→ **Match gstack's `/autoplan` auto-chain** + Superpowers's Pipeline callbacks.

### Fresh context = context engineering

Each executor agent gets **200k tokens purely for implementation, zero accumulated garbage**. Match "fresh subagent context" pattern across all Tier 1 frameworks.

---

## Part 2: CHANGELOG analysis (skim-first)

### Version statistics (from grep)

```bash
grep -E "^## \[" CHANGELOG.md
```

**Inferred versions** từ structure:
- Unreleased (in-progress changes)
- v1.37.1 — 2026-04-17 (latest release)
- v1.37.0 — 2026-04-17 (same day)
- v1.36.x — earlier
- Pattern: `v1.X.Y` semver, major-current = v1.37

→ **Mature enough for v1.37** but still sub-2. Active development. Match pace between Superpowers (v5.x) and gstack (v0.18).

### Latest release highlights (v1.37.0)

Per README's v1.37.0 Highlights:
1. **Spiking & Sketching** — `/gsd-spike` + `/gsd-sketch` commands
2. **Agent size-budget enforcement** — XL: 1600, Large: 1000, Default: 500 line-count limits; CI surfaces violations
3. **Shared boilerplate extraction** — mandatory-initial-read + project-skills-discovery extracted to reference files

→ **Discipline evolution.** Compressing agent prompts + deduplicating boilerplate = signal of matured codebase.

### Unreleased changes (head of CHANGELOG)

**Added:**
- `/gsd-ingest-docs` command — scan ADRs/PRDs/SPECs/DOCs, bootstrap `.planning/` setup from them
  - Parallel classification (gsd-doc-classifier)
  - Synthesis with precedence rules + cycle detection (gsd-doc-synthesizer)
  - Three-bucket conflicts report (INGEST-CONFLICTS.md: auto-resolved/competing-variants/unresolved-blockers)
  - Hard-block on LOCKED-vs-LOCKED ADR contradictions
  - v1 caps at 50 docs per invocation

**Fixed:**
- Installer now installs `@gsd-build/sdk` automatically (resolves `command not found: gsd-sdk` errors)
- Adds `--no-sdk` flag to opt out, `--sdk` to force reinstall

→ **Sophisticated ingest story:** reminds của Storm Bear vault's skill `llm-wiki-ingest`! Convergent concept (import scattered docs → structured knowledge).

### Changelog discipline signals

1. **Keep a Changelog format** explicit (link: https://keepachangelog.com/en/1.1.0/)
2. **Ticket references in commits** — `(#2387)`, `(#2385)` — issue tracker integration
3. **Detailed entry style** — not just "fixed bug", but "Resolves X errors that affected every /gsd-* command after Y"

→ **Most disciplined CHANGELOG style của 5 projects.** Match gstack's user-facing tone.

---

## Part 3: Distinctive mechanisms (from README's "Why It Works")

### Context engineering (already covered in README summary)

Size-limited files based on Claude quality degradation thresholds.

### XML prompt formatting

Task artifacts use XML structure — not just markdown:
```xml
<task type="auto">
  <name>...</name>
  <files>...</files>
  <action>...</action>
  <verify>...</verify>
  <done>...</done>
</task>
```

→ **Unique vs siblings.** ECC/Superpowers/gstack use markdown. GSD chose XML cho LLM parsing precision.

### Multi-agent orchestration

| Stage | Orchestrator | Agents |
|-------|--------------|--------|
| Research | Coordinates | 4 parallel researchers |
| Planning | Validates | Planner + checker loop |
| Execution | Waves | Executors parallel, fresh context |
| Verification | Presents | Verifier + debuggers |

### Atomic git commits

Match gstack + Superpowers discipline. Each task = own commit.

### Modular design

- Add phases to milestone
- Insert urgent work between phases
- Complete milestones, start fresh
- Adjust plans without rebuilding

---

## Part 4: `.planning/` directory anatomy

```
.planning/
├── PROJECT.md           (vision)
├── REQUIREMENTS.md      (v1/v2 scoped + phase traceability)
├── ROADMAP.md           (where you're going)
├── STATE.md             (cross-session memory — decisions, blockers)
├── research/            (ecosystem knowledge)
├── phases/
│   └── {N}/
│       ├── CONTEXT.md       (from /gsd-discuss-phase)
│       ├── RESEARCH.md      (from /gsd-plan-phase)
│       ├── {N}-{M}-PLAN.md  (atomic plans)
│       ├── {N}-{M}-SUMMARY.md
│       ├── UAT.md           (from /gsd-verify-work)
│       └── VERIFICATION.md
├── todos/               (captured ideas)
├── threads/             (persistent cross-session context)
├── seeds/               (forward-looking với trigger conditions)
├── spike-{N}/           (throwaway experiments)
├── sketch-{N}/          (throwaway UI mockups)
├── quick/{N-desc}/      (quick mode artifacts)
├── workstreams/         (parallel milestone work)
└── config.json          (project settings)
```

→ **Namespaced by design.** Clean project root. All GSD artifacts contained.

---

## Distinctive patterns

### Pattern 1: Size-budget enforcement cho agents

v1.37.0 added tiered line-count limits (XL: 1600, Large: 1000, Default: 500). **CI surfaces violations.**

→ **Quality gate at repo level**, không just runtime.

**Reusable for Storm Bear:** Wiki entity pages could have line-count budget (vault's 13-section format already produces ~300-400 line entity pages — in-range).

### Pattern 2: Shared boilerplate extraction (reference files)

v1.37.0 extracted:
- Mandatory-initial-read logic
- Project-skills-discovery logic

Into reference files. "Reducing duplication across a dozen agents."

→ **DRY for agent prompts.** Match gstack's preamble-resolver pattern + ETHOS injection.

### Pattern 3: Ingest Docs mechanism (Unreleased)

`/gsd-ingest-docs` reads repo containing ADRs/PRDs/SPECs/DOCs, bootstraps `.planning/` from them.

**Match Storm Bear's skill `llm-wiki-ingest`!** Both read scattered docs → structured wiki.

**Differences:**
- GSD: input = project docs, output = `.planning/` structure, automated
- Storm Bear: input = source repo + docs, output = wiki pages, Claude-orchestrated

→ **Convergent pattern.** Worth deeper investigation cho cross-project learning.

### Pattern 4: Conflicts engine

`/gsd-ingest-docs` và `/gsd-import` share "conflict-detection contract" (`references/doc-conflict-engine.md`).

**3-bucket conflict classification:**
- Auto-resolved
- Competing-variants
- Unresolved-blockers

**Hard-block on LOCKED-vs-LOCKED ADR contradictions.**

→ **Mature conflict handling.** Most explicit of 5 projects.

### Pattern 5: 50-doc cap per invocation (v1 safety)

Unreleased `/gsd-ingest-docs` caps at 50 docs to prevent runaway context. Safety-first engineering.

→ **Match goclaw's max 20 iterations.** Bounded processing.

### Pattern 6: ADR (Architecture Decision Record) awareness

Changelog mentions "LOCKED-vs-LOCKED ADR contradictions" — GSD first-class aware của ADR concept.

→ **Formal architecture doc concept.** Sophisticated.

---

## Open questions resolved

- ✅ Q11: Compare với SpecKit/OpenSpec/Taskmaster — TÂCHES explicitly positions against them ("They make it complicated. GSD keeps complexity in the system, not workflow.")
- ✅ Q2: 33 vs 21 agent count — **folder lag/extras.** 33 is actual, 21 is docs subset. Need to verify which is canonical.

## Open questions raised

- ⏸ Full CHANGELOG (2222 lines) — only latest 5 versions read. Major version migrations missed?
- ⏸ docs/ARCHITECTURE.md full read — not done this session
- ⏸ ADR LOCKED/WIP state model — full spec?
- ⏸ "Conflict-detection contract" reference file — reusable logic?
- ⏸ SDK `@gsd-build/sdk` — standalone npm package, what API?

---

## Cross-references

- [[(C) README summary]] — foundational
- [[(C) USER-GUIDE summary]] — deep workflow
- [[(C) index]]
- [[(C) log]]
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) Release Notes overview.md` — CHANGELOG patterns
- Cross-project: vault skill `llm-wiki-ingest.md` — compare `/gsd-ingest-docs` mechanism

## Citations

- `docs/AGENTS.md` lines 1-40 (21 agent categorization)
- `agents/` folder listing (33 files)
- `CHANGELOG.md` Unreleased + v1.37.x entries (lines 1-40)
- README "Why It Works" section (lines 473-555)

## TODO

- ⏸ Deep-read docs/ARCHITECTURE.md — currently unread
- ⏸ Full CHANGELOG version grep — full timeline
- ⏸ `references/doc-conflict-engine.md` — reusable conflict pattern
- ⏸ `@gsd-build/sdk` npm package — standalone capabilities
- ⏸ Compare `/gsd-ingest-docs` vs Storm Bear's `llm-wiki-ingest` skill — meta-learning opportunity
