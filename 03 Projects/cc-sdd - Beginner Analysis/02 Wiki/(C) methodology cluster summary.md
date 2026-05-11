# Cluster 3 — Methodology / philosophy / version evolution

> **Sources:** docs/guides/spec-driven.md + docs/guides/why-cc-sdd.md + docs/guides/command-reference.md + CHANGELOG.md (v0.0.1 → v3.0.2).
> **Wiki:** cc-sdd v61.

---

## 1. Verbatim philosophy

From `why-cc-sdd.md`:

> *"explicit contracts at the right granularity let AI-driven development at team scale move faster, not slower"* — central thesis

> *"separating specification (the contract and pre-conditions) from design (the exploration space within those constraints)"* — core distinction

> *"If the discipline feels like overhead, your specs are probably too big"* — right-sizing principle

From `spec-driven.md`:

> *"writing more specs will not create independence"* (if the system has vague ownership or circular dependencies — architecture-as-foundation principle)

## 2. Why-cc-sdd positioning (when to use / when NOT)

**Optimal use cases:**
- Medium-grain decomposition into multiple shippable specs
- Multiple contributors (human or agent) requiring coordination
- Vertical-slice shipping with iterative learning
- Auditability requirements linking code changes to approved contracts

**When unnecessary:**
- Solo agent sessions
- Prototype work
- Contexts where "vibe coding" genuinely outpaces formal contracts

**Notable:** *"even within cc-sdd workflows, `/kiro-discovery` can legitimately conclude that no specification is needed"*.

**Observation:** This is **anti-vibe-with-pragmatic-acknowledgment** positioning — counter-evidence to Pattern #51's pure anti-vibe-pole formulation. cc-sdd doesn't claim SDD is universal; it claims SDD is right-sized for *team-scale + medium-grain + multi-contributor* contexts.

## 3. SDD methodology principles (4 core)

From `spec-driven.md`:

### 3.1 Boundary-First Approach
Specifications make responsibility boundaries + contracts explicit. Specs should clarify ownership, exclusions, allowed dependencies, and downstream revalidation needs.

### 3.2 Independent Delivery Units
Specs enable asynchronous progress where work can advance independently while maintaining architectural coherence. Supports targeted revalidation rather than broad system resynchronization.

### 3.3 Architecture as Foundation
SDD requires solid underlying architecture. *"Writing more specs will not create independence"* if the system has vague ownership or circular dependencies.

### 3.4 Spec-Centered with Mechanical Grounding
Markdown specifications express intent + boundaries. Tests, builds, linting, type checks provide execution-level validation.

**Observation:** Architecture-as-foundation (3.3) is corpus-first explicit acknowledgment that SDD is downstream of architectural discipline. Other corpus SDD frameworks (spec-kit v17 / OpenSpec v58 / GSD v5) implicitly assume architecture is solid; cc-sdd states the dependency.

## 4. SDD workflow phases (4 phases + 1 routing)

| Phase | Output | Note |
|---|---|---|
| Discovery | `brief.md` (+ `roadmap.md` if multi-feature) | Routes into 5 outcomes |
| Requirements | `requirements.md` | EARS-formatted acceptance criteria |
| Design | `research.md` (when investigation needed) + `design.md` (incl. File Structure Plan) | Architecture + Mermaid + FSP |
| Task Planning | `tasks.md` | P-wave priority + boundary markers + dependency annotations |
| Implementation | (commits + verification artifacts) | TDD + adversarial review + auto-debug |

5 discovery outcomes:
1. Extend existing spec
2. Implement directly (no new spec)
3. Single spec creation
4. Multi-spec decomposition
5. Mixed decomposition

## 5. Task decomposition strategy

From `spec-driven.md`:
- Tasks broken into **waves** (P0, P1, etc.) enabling parallel work
- Each task includes a **local Boundary marker**
- Implementation follows **Feature Flag TDD** (RED then GREEN) for incremental, safe delivery
- One-task-per-iteration discipline

**Observation:** P-wave + Boundary + Feature-Flag-TDD = three corpus-first explicit task-level primitives in single framework.

## 6. EARS-format requirements (corpus-first explicit reference)

EARS = Easy Approach to Requirements Syntax. cc-sdd `requirements.md` uses EARS-formatted acceptance criteria.

**Observation:** First time corpus has explicit named requirements-format reference. spec-kit v17 has structured requirements but no EARS naming. EARS is industry-standard requirements syntax (predates AI agents — comes from systems engineering / aerospace requirements practice).

**Future research:** Should EARS-format be its own Pattern Library candidate? N=1 currently. Stale-flag at registration if registered standalone.

## 7. Command reference (v2.x lineage — superseded by Skills in v3.0)

**Steering commands (2):**
- `/kiro:steering` — creates/updates project memory (structure.md, tech.md, product.md)
- `/kiro:steering-custom` — interactive specialized domain steering files

**Spec workflow commands (5):**
- `/kiro:spec-init <project-description>` — initialize feature spec
- `/kiro:spec-requirements <feature-name>` — EARS-format requirements
- `/kiro:spec-design <feature-name> [-y]` — technical design + Mermaid + FSP
- `/kiro:spec-tasks <feature-name> [-y]` — task breakdown + P-waves
- `/kiro:spec-impl <feature-name> [task-numbers]` — TDD execution

**Validation commands (3 — optional):**
- `/kiro:validate-gap` — brownfield codebase analysis
- `/kiro:validate-design` — design review with GO/NO-GO
- `/kiro:validate-impl` — implementation validation

**Status & utility (1):**
- `/kiro:spec-status <feature-name>` — progress display

## 8. Command syntax migration (v2.x colon → v3.0 dash)

- v2.x: `/kiro:steering`, `/kiro:spec-init`, etc. (colon-separated)
- v3.0: `/kiro-discovery`, `/kiro-impl`, etc. (dash-separated; Skills mode)

**Observation:** Syntax migration may reflect Agent Skills mode constraints (some platforms don't permit colons in slash command names) OR stylistic preference. Worth confirming via repo discussion / issue tracker.

## 9. Version evolution (CHANGELOG highlights)

| Version | Date | Major change |
|---|---|---|
| v0.0.1 | (early) | Initial 8 core commands |
| v1.0.0 | 2025 | Established 8 core commands; supports Claude Code, Cursor, Gemini CLI, Codex CLI |
| v1.1.0 | 2025 | +3 validation commands (validate-gap/design/impl); Cursor official |
| v2.0.0 | 2025-11-09 | **Template unification**: removed OS-specific dirs; single `commands/` structure; +Research.md template; interactive CLI installer |
| v2.0.5 | 2026-01-08 | +Greek language (13 total) |
| v2.1.0 | 2026-02-01 | **+OpenCode (8th platform)**; updated recommended models (Claude Opus 4.5 / GPT-5.2 / Gemini 3 Flash) |
| v2.1.1 | 2026-02-02 | OpenCode slash command frontmatter fix; vitest security update |
| v3.0.0 | 2026-04-10 | **Major architectural shift**: Agent Skills mode as primary install target across 8 platforms; +`/kiro-discovery`, `/kiro-spec-batch`, `/kiro-impl`; deprecated command-based installs; removed Codex prompts mode + Ralph Loop dependency |
| v3.0.1 | 2026-04-11 | "team-scale AI-driven development" → "AI-driven development at team scale"; character encoding fix; path security hardening |
| v3.0.2 | 2026-04-13/14 | Removed Amazon book reference; fixed missing `description` field in Codex template |

**Observation:** 7 months from v0.0.1 to v3.0.2 (October 2025 estimate based on v2.0.0 dated 2025-11-09 + earlier alpha releases). 3 major releases (v1, v2, v3) in 6 months — high-velocity development. v3.0 Skills-mode shift = **architectural pivot from command-based to skills-based**.

## 10. Major architectural shifts

### Skills Mode Introduction (v3.0.0)
- From command-based dispatch → native subagent dispatch
- Long-running autonomous implementation with reviewer separation
- Per-platform Skills format translation at install time
- Deprecated command-based installs (still available but not primary)

### Template Unification (v2.0.0)
- Eliminated OS-specific directories (`os-mac` / `os-windows`)
- Single `commands/` structure with actual file extensions
- Interactive CLI installer

### Steering System Evolution
- Single steering file → entire `steering/` directory loaded as project-wide rules
- Reflects industry trend toward multi-file context (CLAUDE.md → CLAUDE.md + AGENTS.md + custom files)

## 11. Deprecation events

- v3.0.0 deprecated **command-based installs** (still available, not primary)
- v3.0.0 removed **Codex prompts mode**
- v3.0.0 removed **Ralph Loop dependency** (Ralph Loop = unknown external project; needs investigation — may be a research-paper-chain or community-tool reference; potential corpus-historical-foundational sub-path candidate per Pattern #27 v59 AutoGPT)
- v3.0.2 removed **Amazon book reference** (cleanup — possibly original Kiro IDE methodology citation)

## 12. Corpus-first observations

- **Architecture-as-foundation explicit acknowledgment** — corpus-first explicit dependency-statement that SDD requires solid underlying architecture
- **EARS-format requirements explicit naming** — corpus-first
- **File Structure Plan as design.md sub-section** — corpus-first explicit FSP primitive
- **P-wave parallel-execution annotation** — corpus-first explicit wave-priority + concurrency-safety annotation
- **5-outcome discovery routing** — corpus-first explicit discovery routing model with named outcomes
- **Anti-vibe-with-pragmatic-acknowledgment** — corpus-first nuance on Pattern #51 spectrum
- **Command-syntax migration (colon → dash) at major-version boundary** — corpus-first observation of syntax-migration-as-architectural-marker

## 13. Absences (vs prior corpus subjects)

- ❌ NO 9-article constitution (vs spec-kit v17)
- ❌ NO formal AI-disclosure policy (vs spec-kit v17 — Pattern #23 stale)
- ❌ NO marketplace ecosystem (vs spec-kit v17)
- ❌ NO research-paper-chain (vs autoresearch / LlamaFactory)
- ❌ NO Karpathy / Bostrom / John Lam citation
- ❌ NO ML-training infrastructure
- ❌ NO crypto / blockchain integration
- ❌ NO MCP-server primitive (sibling skillport has this)

## 14. Pattern advancement check

- **Pattern #21 SDD Methodology Emergence un-stale** — methodology cluster confirms cc-sdd is independent SDD-centered framework with full SDD vocabulary (boundary-first / contracts / mechanical-grounding / EARS / FSP / P-waves / TDD)
- **Pattern #51 Vibe-Coding spectrum NUANCE** — counter-evidence-driven refinement (anti-vibe-with-pragmatic-acknowledgment sub-pole at v61)
- **Pattern #18 sub-archetype: agent-platform-format-translation-installer** — install-time translation across 8 platforms strengthens N=1 registration candidate
- **Pattern #19 first-mover-authority-without-lineage** — gotalab ecosystem-portfolio (cc-sdd + skillport + uxaudit + claude-code-marimo) all independent of cited methodology lineage
- **Pattern #27 community-viral corpus-historical-foundational** — Ralph Loop deprecation is potential N=1 reference point if Ralph Loop turns out to be community-foundational (research needed)

## 15. Length / granularity note

`spec-driven.md` + `why-cc-sdd.md` are concise (~50-100 lines each estimated based on extracted content). `command-reference.md` is denser (~150 lines estimated — full command surface). CHANGELOG.md is comprehensive (covers v0.0.1 → v3.0.2 with detail per release).

Layered documentation pattern: high-level (README) → philosophy (why-cc-sdd) → methodology (spec-driven) → reference (skill-reference + command-reference) → history (CHANGELOG). Reflects mature documentation discipline for a 6-month-old project.
