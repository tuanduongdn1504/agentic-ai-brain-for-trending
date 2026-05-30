# personal-repo — Tù Bà Khuỳm "getting started" (9th individual-scale sibling)

Operator-submitted Vietnamese-language beginner introduction by Tù Bà Khuỳm — the Vietnamese practitioner already cited in earlier siblings ([[personal-repo-overview]], [[personal-repo-patterns]]). This entry adds the **9th individual-scale sibling article** to the harness-engineering topic and surfaces a **corpus-first technical contribution**: SQLite-as-project-memory instead of Markdown.

## Source

- Raw: [`raw/2026-05-30-harness-engineering-getting-started-beginner-intro.md`](../../raw/2026-05-30-harness-engineering-getting-started-beginner-intro.md) (NotebookLM `4c7d51e4-b450-4504-933b-3bb4be28b393`)
- Anchor video: [Tù Bà Khuỳm — Bắt đầu Harness Engineering từ đâu? Từ đây!!](https://www.youtube.com/watch?v=gQLhchHmRKs) (2026-05-30, 469 views as of drain time, 26:04 duration)

## Why this sibling is distinct

The 8 prior individual-scale siblings span Hermes/Codex orchestration (Nemanja), mixed-effort-parallel + `/smell` (Zen), Herdr multiplexer (Hal Shin), router-multimodel (howznguyen), and more. Tù Bà Khuỳm's earlier appearance (2026-05-13 drain) established him as a Vietnamese-practitioner take on harness engineering ("personal-repo-continuation"). **This new 2026-05-30 video is positioned as the BEGINNER-INTRODUCTION**: how a Vietnamese-language operator should *enter* the harness-engineering discipline.

Distinguishing the 9th sibling from prior 8:

| Sibling | Distinctive contribution |
|---|---|
| 1-3 (personal-repo-overview/patterns/gaps) | Aggregation of 6-video bundle 2026-05-13 |
| 4 (tejas-kumar-anchor) | Definitional anchor — scale-invariant primitives |
| 5 (router-multimodel — howznguyen) | Router-mediated cross-vendor multi-model pattern |
| 6 (hermes-orchestrator — Nemanja) | Orchestrator-mediated cross-vendor pattern |
| 7 (zen-mixed-effort-parallel) | Catalog-driven `/smell` + `CLAUDE_CODE_EFFORT_LEVEL` |
| 8 (herdr-agent-multiplexer) | Terminal substrate as first-class agent state machine |
| **9 (tu-ba-khuym-getting-started)** | **SQLite-as-memory + beginner-introduction pedagogy** |

## CORPUS-FIRST contribution — SQLite-as-memory

Tù Bà Khuỳm presents the corpus's first non-Markdown approach to project memory.

**The prior consensus** (across ALL 8 earlier individual-scale siblings + 14 org-scale articles + 6 new sources in this drain): project memory lives in `.md` files — `CLAUDE.md` / `agents.md` / `soul.md` / `architecture.md` / `changelog.md` / `project_status.md`.

**Tù Bà Khuỳm's V2 harness diverges**: use a **local SQLite database** to store:
- Project **decisions** (with timestamp + rationale)
- Agent **action traces** (every tool call + result)
- Friction logs (identified problems + proposed fixes)

His stated rationale (from the raw, §Outliers-3):

> A database is more **precise** and **less prone to being ignored or filled incorrectly** by the agent compared to a text file.

This is structurally significant:
- **Markdown** trusts the agent to read + update correctly. Operator pays for token cost on every read; agent can mishandle structure.
- **SQLite** forces structured access via SQL queries. Schema enforces correctness. Agent reads via tool calls, not context-window inclusion. Token cost drops dramatically.

## Friction-tracking → backlog → harness refinement

Tù Bà Khuỳm explicitly frames the SQLite trace store as a **backlog generator**:

1. Agent executes tasks; every action is traced to SQLite
2. Operator reviews traces, identifies "friction" (slow / failed / suboptimal actions)
3. Friction entries become a **backlog for improving the harness itself**
4. Harness improvements are codified back into the agent's workflow

This is a **closed loop on harness quality** — the harness improves itself by analyzing its own failure modes. Distinct from but compatible with:
- Ross Mike's "build-via-failure" skill-authoring recipe (from [[../ai-operating-system/skills-architecture-progressive-disclosure]])
- The vault's autopilot-research routine (which improves itself via routine-v2.X codification candidates)

## Beginner-introduction pedagogy

The video is structured as "where to start" — explicitly targeting newcomers to harness engineering. Pedagogical structure (from raw, §Trends):

1. **Start with a PRD/spec doc** — define product goals + technical architecture before any code
2. **Mandate plan mode** — never let agent skip the planning phase
3. **Lean project-memory file** — keep `claude.md` (or SQLite schema) focused
4. **Validation loops via hooks** — agent catches its own mistakes
5. **Git worktrees for parallelism** — isolate concurrent work

This 5-step opening is largely consensus content (covered across [[anchor-bundle-overview]] and existing personal-repo siblings) — the value-add is the **Vietnamese-language pedagogical lens**, which is itself a corpus signal:

- Vietnamese practitioners are **a distinct, growing cohort** in the harness-engineering ecosystem (Tù Bà Khuỳm + howznguyen + others in vault state)
- Beginner-introductions in Vietnamese fill a market gap (most English-language tutorials assume programmer fluency)

## Specific tactical techniques highlighted

| Technique | Tù Bà Khuỳm's framing |
|---|---|
| PRD-first | "tài liệu thiết kế" (design document) precedes code — same as Avthar's PSB |
| Plan mode discipline | Use Plan Mode default — same as John Kim, Maddy Zhang |
| Lean memory | (his innovation here is SQLite, not lean-Markdown) |
| Validation hooks | Hooks fire on file save — same as Maddy Zhang |
| Trace storage | SQLite (corpus-first) — his V2 contribution |
| Friction backlog | Review traces → improve harness — corpus-first closed loop |

## Compare to existing personal-repo-continuation article

The earlier 2026-05-13 Tù Bà Khuỳm appearance ([[personal-repo-overview]] + related) was a **6-video bundle aggregation** including his content. The 2026-05-30 video is a **dedicated single-source talk**:
- 26:04 duration → more focused than the 6-video aggregation
- Direct exposition of V2 harness — less interpretation needed
- SQLite-as-memory was NOT in the earlier bundle's coverage — this is a **new technical position** since 2026-05-13

## Production-readiness gaps (specific to this video)

The video does NOT address:
- **SQLite schema migration** as the harness V2 evolves — what happens when the operator changes the trace schema?
- **Multi-machine sync** for SQLite — works for single-laptop operator; doesn't compose with team / cloud deployment
- **Cross-project memory** — one SQLite per project means no shared learnings across operator's portfolio
- **Backup / versioning** — SQLite files need git-LFS or equivalent

These compose with the broader gaps in [[personal-repo-gaps]].

## Key Takeaways

- **9th individual-scale sibling** added to harness-engineering topic (was 22 articles, now 23 with this + 1 framework-comparison sibling)
- **CORPUS-FIRST: SQLite-as-memory** — the first non-Markdown project-memory approach across 8 prior siblings + 14 org-scale articles
- **Closed loop on harness quality** — Tù Bà Khuỳm uses traces to generate a self-improvement backlog
- **Vietnamese-language pedagogical lens** is a corpus signal — distinct cohort, distinct presentation
- **Tù Bà Khuỳm's V2 is more technically opinionated than V1** — SQLite + friction-tracking did NOT appear in the 2026-05-13 bundle

## Related

- [[_index]] — topic entry
- [[personal-repo-overview]] — first appearance of Tù Bà Khuỳm in the corpus
- [[personal-repo-patterns]] — the broader individual-scale pattern set
- [[personal-repo-gaps]] — production-readiness gaps shared across individual-scale siblings
- [[getting-started-consensus-and-divergences]] — sister-article from same drain
- [[../ai-operating-system/memory-and-context-rot]] — sister-topic 6-level memory taxonomy (SQLite-as-memory would slot at ~level 4-5)
