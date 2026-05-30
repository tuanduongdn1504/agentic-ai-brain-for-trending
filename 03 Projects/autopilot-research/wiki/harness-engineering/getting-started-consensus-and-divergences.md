# Getting-started — 6-speaker consensus + divergences

What the 6-source 2026-05-30 "beginner introduction to harness engineering" drain bundles agree and disagree on. The N=6 cross-source signal is the most useful artifact from this drain for vault operators considering a starting-point workflow.

## Source

- Raw: [`raw/2026-05-30-harness-engineering-getting-started-beginner-intro.md`](../../raw/2026-05-30-harness-engineering-getting-started-beginner-intro.md)
- 6 speakers: Tù Bà Khuỳm (anchor) · John Kim (Meta) · AI with Avthar · Productive Dude · Maddy Zhang · Caleb Writes Code

## The consensus (where ≥4 of 6 speakers agree)

### 1. Plan-first methodology (N=5)

ALL major speakers except Caleb-on-his-8min-overview enforce a planning phase before code. Variants:

| Speaker | Frame |
|---|---|
| John Kim | "Plan Mode" almost exclusively at task start to verify assumptions |
| Maddy Zhang | "Plan Mode" before "Act Mode" — N=2 with John Kim |
| AI with Avthar | **PSB system** (Plan-Setup-Build) — 15 min planning before coding |
| Productive Dude | Tell AI to ask YOU clarifying questions first |
| Tù Bà Khuỳm | PRD/spec doc precedes code |
| Caleb Writes Code | PRD-first (mentioned briefly) |

Strongest cross-source signal in the drain. Adopt as default.

### 2. claude.md as "project brain" (N=6)

ALL speakers maintain a persistent `.md` file at project root containing:
- Tech-stack preferences
- Directory maps
- Project rules
- Tone / output conventions

(Tù Bà Khuỳm extends to SQLite — see his sibling article [[personal-repo-tu-ba-khuym-getting-started]] — but still maintains some Markdown.)

### 3. Validation loops via hooks (N=2-3)

**Maddy Zhang** is the strongest advocate; **John Kim** and **Avthar** reference compatible patterns. Hooks fire on file save → run build, tests, type-checkers → agent sees its own errors and self-corrects.

### 4. Git worktrees for parallelism (N=3)

**Avthar**, **John Kim**, **Maddy Zhang** all advocate `git worktree`. Allows multiple Claude sessions on different branches in isolated directories.

### 5. MCP as connectivity primitive (N=4)

**Productive Dude**, **Avthar**, **Tù Bà Khuỳm**, **Caleb Writes Code** all use MCP servers for external-tool access. **John Kim is the contrarian** (see §Divergences below).

### 6. Sub-agents for specialized atomic tasks (N=2)

**Caleb Writes Code** + **Maddy Zhang** both discuss specialist sub-agents (Security Reviewer, DB Specialist). Composes with [[../ai-operating-system/builder-orchestrator-executor-pattern]] from sister topic.

## The divergences (sharp disagreements)

### 1. Optimal `claude.md` length

| Speaker | Recommendation |
|---|---|
| **Maddy Zhang** (the conservative) | 100-200 lines MAX |
| **John Kim** (the moderate) | ~300 lines is fine |
| **Avthar** (the linker) | Keep main file lean; offload to `architecture.md`/`changelog.md`/`project_status.md` |
| **Tù Bà Khuỳm** (the outlier) | (Moved off Markdown — see SQLite approach) |

The disagreement spans **2-3× variance** on file length — significant. Empirical question worth measuring with vault operators' own workloads.

### 2. Session-cycling habit

| Position | Speakers |
|---|---|
| **`/clear` constantly** between unrelated tasks | Maddy Zhang, John Kim |
| **Resume sessions** + manage via automated doc updates | Avthar |

Direct disagreement on whether session history is an asset or a liability. The N=2 lean toward `/clear` is mild; not strongly settled.

### 3. MCP enthusiasm vs MCP skepticism

| Position | Speakers |
|---|---|
| **MCP-as-default** | Productive Dude, Avthar, Caleb, Tù Bà Khuỳm |
| **"Very very hard to NOT use MCPs"** | **John Kim** (Meta Staff Engineer) |

John Kim's anti-MCP stance is the corpus-strongest minority position. His reasoning (from raw §Outliers-2): MCPs "blow up your context window" and token usage. Prefers writing manual scripts for validation.

Worth flagging as candidate addition to [[contrarian-stances]] if not already covered there.

### 4. Memory storage: Markdown vs SQLite

| Position | Speakers |
|---|---|
| Markdown (`.md` files at all levels) | All 5 non-Tù Bà Khuỳm speakers |
| **SQLite (V2 harness)** | **Tù Bà Khuỳm** (CORPUS-FIRST) |

Strongest single-speaker divergence in the corpus. Detailed in [[personal-repo-tu-ba-khuym-getting-started]].

### 5. Parallelism strategy: Starcraft-juggling vs Git worktrees

| Position | Speakers |
|---|---|
| **Multiple terminal instances** "Starcraft-style" (manual juggling) | John Kim |
| **Git worktrees** (structured isolation) | Avthar, Maddy Zhang |

Functionally different — Starcraft-juggling uses unconstrained context-switching; worktrees enforce file-system isolation. Worktrees are probably the right default for most operators; Starcraft-juggling may suit a single Meta-Staff-Engineer-scale operator running many concurrent projects.

### 6. UI: Artifacts only vs Inline visualizations

| Position | Speakers |
|---|---|
| **Artifacts only** — turn off inline visualizations | Productive Dude |
| **Use inline visualizations** — quick dashboarding | Most others (implicit) |

Minor disagreement; mostly aesthetic preference.

## CORPUS-FIRST findings (this drain)

1. **Tù Bà Khuỳm's SQLite-as-memory** (detailed in [[personal-repo-tu-ba-khuym-getting-started]])
2. **GCAO framework** (Productive Dude) — Goal / Context / Action / Output structure for individual prompts
3. **DBS framework** (Productive Dude) — Direction / Blueprints / Solutions for building Skills
4. **PSB system** (AI with Avthar) — Plan / Setup / Build project-lifecycle structure
5. **Maddy Zhang's "100-200 line claude.md ceiling"** — tightest documented constraint in the corpus on instruction-layer size

## Competing prompting frameworks (corpus-first)

For the first time in the harness-engineering corpus, **3 distinct competing proprietary frameworks** emerge in one drain:

| Framework | Source | Scope | Letters |
|---|---|---|---|
| **GCAO** | Productive Dude | Individual prompt structure | Goal · Context · Action · Output |
| **DBS** | Productive Dude | Skill creation | Direction · Blueprints · Solutions |
| **PSB** | AI with Avthar | Project lifecycle | Plan · Setup · Build |

All 3 are **3-4 letter acronyms with creator-branding**. The pattern itself is corpus-signal: harness-engineering content creators are at the **proprietary-framework branding** maturity stage.

The vault's own equivalents (per state files):
- [[../../wiki/claude-md-12-rules/_index]] — 12-rule CLAUDE.md (Mnilax extension of Karpathy + Forrest Chang's 4-rule template)
- Routine v2.2 — 8-phase orchestration

The vault's frameworks are **rules + phases**, not 3-letter acronyms — closer to engineering discipline than to marketing branding.

## Implications for the vault

The vault's autopilot-research project + Storm Bear vault discipline already satisfies most consensus items:

| Consensus item | Vault status |
|---|---|
| Plan-first methodology | ✓ via routine v2.2 Phase 0-1 |
| `claude.md` as project brain | ✓ at vault + project levels |
| Validation loops via hooks | Partial — git hooks not formalized |
| Git worktrees for parallelism | ✓ heavily used (kind-shockley + KJ-OS-autopilot are concurrent worktrees) |
| MCP for external tools | ✓ Multiple MCP integrations |
| Specialist sub-agents | Partial — vault uses agent-tool routinely, less formalized |

The vault's posture is **closest to Maddy Zhang's** (lean claude.md + structured separation) and **furthest from John Kim's** (the vault uses MCP heavily).

## Promotion candidacy

This drain + the existing harness-engineering topic (23 articles after this commit) is approaching **promotion-to-Storm-Bear** criteria:
- Anchored on Anthropic first-party docs + Lopopolo + Tejas Kumar + multiple individual-scale practitioners
- Cross-cohort coverage (org-scale + individual-scale + Vietnamese cohort + Indian cohort)
- Demonstrable cross-source consensus on 6 patterns
- Sharp disagreement axes documented

Recommend audit at next mini-audit cadence (v66+).

## Key Takeaways

- **6 consensus items** + **6 divergence axes** mapped — covers the corpus's beginner-vs-advanced spectrum
- **Plan-first methodology** is the strongest single signal (N=5 of 6 speakers)
- **John Kim's anti-MCP stance** is the corpus's strongest contrarian — worth adding to [[contrarian-stances]] if not already
- **3 competing prompting frameworks** (GCAO / DBS / PSB) emerge in one drain — proprietary-branding maturity stage
- **The vault's discipline is closest to Maddy Zhang's posture** — lean Markdown + structured separation

## Related

- [[_index]] — topic entry
- [[personal-repo-tu-ba-khuym-getting-started]] — sister-article from same drain
- [[contrarian-stances]] — candidate add: John Kim anti-MCP stance
- [[anchor-bundle-overview]] — broader anchor-source overview
- [[personal-repo-patterns]] — cross-cutting individual-scale patterns
- [[../claude-md-12-rules/_index]] — vault's equivalent framework
- [[../ai-operating-system/instruction-layer-markdown-files]] — sister-topic claude.md hierarchy
