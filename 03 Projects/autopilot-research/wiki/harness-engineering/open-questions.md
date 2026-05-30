# Open questions & hedges

> Lopopolo's explicit "I don't know yet", "TBD", and flagged gaps. Each is a target for subsequent research ingests. When evidence emerges, append a "Status update" block at the bottom of the relevant question — don't quietly resolve them.

## 1. Deployment of high-speed "Spark" models

> "I have not quite figured out how to use it yet" / "I'm not sure how to deploy spark"

GPT-5.3 Spark is a faster, lower-reasoning sibling. Lopopolo says it often exhausts context via auto-compaction before completing complex tasks. Gap: no operational pattern for routing tasks across reasoning tiers.
- *talk [54:00, 55:00]*
- **Where it'd resolve:** future Anthropic / OpenAI guidance on tiered model routing; benchmark showing task-class fit per tier

## 2. Multi-team / multi-human collaboration patterns

> "TBD we have not figured this out in a general way"

How should multiple humans + multiple agents coordinate? Lopopolo questions whether every team builds bespoke internal tooling or whether a standard pattern (issue tracker + Slack as the substrate?) will emerge.
- *talk [39:35]*
- **Where it'd resolve:** comparative study of teams running harness engineering at >1-team scale

## 3. Zero-to-one product scaffolding

> "definitely not there on being able to go from new product idea to prototype one shot"

Models can extend/refactor but struggle to translate raw mocks → playable software for net-new products with no precedent screens.
- *talk [55:41]*
- **Where it'd resolve:** Lovable/Bolt/Replit material (cited but distinguished from harness engineering); GPT-6+ release notes

## 4. Complex architectural refactoring

> "the gnarliest refactorings" — area Lopopolo still spends most human time on

Decomposing monoliths and redefining deep interfaces remains a steering-heavy task. Lopopolo says "expects to get better" — not a solved problem.
- *talk [55:41]*
- **Where it'd resolve:** demonstrated tooling that automates monolith decomposition; or, evidence the gap is fundamental

## 5. Limits of internalizing dependencies (claim #7 ceiling)

Current vendoring works at "low, medium" complexity — few thousand lines. **Datadog and Temporal cited as exceeding the ceiling** because they require massive scale and security posture.
- *talk [26:00, 27:00]*
- **Why it matters:** bounds the most disruptive operational claim (claim #7 in [[core-claims]])
- **Where it'd resolve:** Datadog/Temporal vendoring case study; or, security model for high-fidelity dependency replacement

## 6. Language-specific agent legibility

> "I wonder if any languages struggle more than others because of this... I don't know"

Open question whether some programming languages are inherently harder for agents to navigate. Hints that Elixir's process supervision is unusually agent-friendly, but no comparative claim.
- *talk [46:00]*
- **Where it'd resolve:** controlled experiments comparing agent productivity across languages; or, theoretical argument for legibility properties

## 7. Maintaining "pilot" context at scale

> "I have lost track very often of what the actual state of the code looks like because I'm not in the loop"

Personal admission: humans steering large agentic teams lose intimate context. How to preserve high-level "systems thinking" while not knowing the implementation?
- *talk [35:20]*
- **Where it'd resolve:** observability/visualization tooling for agentic codebase summaries; or, organizational patterns for splitting "pilot" attention

## 8. Automated QA for distribution artifacts

Gap in agents' ability to **smoke-test built artifacts** (Electron apps in their case) before promotion. Team admits "not invested any time in this".
- *podcast [38:09]*
- **Where it'd resolve:** agent-driven E2E test harnesses; existing patterns from Playwright + GH Actions worth surveying

## 9. Utility of "Plan Mode"

Skepticism of tools where agents propose a plan for human approval. Lopopolo flags risk that humans approve plans without reading → "encoding bad instructions".
- *podcast [31:00]*
- **Tension with [[external|workflow-ai-coding/_index]]** which presents plan-first as a mature pattern in Anthropic's stack
- **Where it'd resolve:** comparative data on plan-mode adoption + outcome quality

## 10. Defining "good job" success criteria

> Meta-epistemological question: how to systematically define a "good, acceptable job" across 500 minor decisions per patch when non-functional requirements are underspecified?
- *podcast [08:00]*
- **Where it'd resolve:** frameworks for encoding non-functional requirements for agents; possibly Anthropic Skills, possibly proprietary

---

## Open questions from 2026-05-30 sibling drain (SQLite-as-memory cluster)

Surfaced by Tù Bà Khuỳm's V2 harness ([[personal-repo-tu-ba-khuym-getting-started]] §Production-readiness gaps). Each is unaddressed in the source video and represents a real production-deployment concern.

## 11. SQLite schema migration for evolving harness memory

When operator changes the SQLite trace schema (adds columns / renames tables / changes types), what happens to the agent's existing memory? Markdown is forgiving (free-text changes); SQL schema is strict.
- *Source: Tù Bà Khuỳm 2026-05-30 V2 harness*
- **Where it'd resolve:** SQLite-specific migration tooling (Alembic, sqitch, etc.) integrated with the agent's tool calls; pattern for backward-compatible schema evolution
- **Why this matters:** Markdown's loose schema is feature, not bug — agent can read partial / malformed / outdated entries gracefully. SQLite's strictness means schema changes can BREAK agent reads until migration runs. Without explicit pattern, SQLite memory becomes brittle.

## 12. Multi-machine sync for SQLite memory

Tù Bà Khuỳm's SQLite memory lives on a single laptop. Markdown memory composes with git (cheap sync across machines). SQLite + git is awkward (binary file, merge conflicts, large diffs).
- *Source: Tù Bà Khuỳm 2026-05-30 V2 harness — implicitly assumed single-machine*
- **Where it'd resolve:** Litestream / Rclone for SQLite replication; or hybrid Markdown-text-for-instructions + SQLite-for-traces split where only Markdown syncs
- **Why this matters:** operator using multiple machines (laptop + desktop + cloud agent) cannot share SQLite memory cleanly. The pattern degrades to single-device unless explicit sync layer is added.

## 13. Cross-project memory sharing under SQLite-per-project assumption

One SQLite per project means **no shared learnings across operator's portfolio**. If operator learns a tactic in Project A, that tactic does NOT propagate to Project B's SQLite.
- *Source: Tù Bà Khuỳm 2026-05-30 V2 harness — single-project-scoped*
- **Where it'd resolve:** layered memory architecture — per-project SQLite + cross-project shared SQLite (like global git config); or central memory MCP server queryable from any project
- **Why this matters:** the value of SQLite-as-memory (precision, schema-enforced correctness) is offset by **per-project siloing**. Operators with many small projects pay the silo cost; operators with one big project don't.

## 14. Version control for agent memory (specifically SQLite + Markdown both)

Neither corpus addresses **how to roll back agent memory state** if the agent learned incorrect information. Markdown gets git history for free; SQLite needs `.db` snapshots + restore procedure.
- *Source: 2026-05-30 sibling drains (both [[personal-repo-tu-ba-khuym-getting-started]] §Production-readiness AND [[../claude-cowork/production-readiness-gaps]] §Gap 3)*
- **Where it'd resolve:** temporal-versioning-of-memory frameworks; possibly Dolt (versioned SQLite-like) or similar
- **Why this matters:** memory poisoning is a real attack/error mode in production agent systems. Without rollback, a single bad ingest corrupts the agent's memory permanently.

---

## How to extend

Each future research ingest that touches an open question should:
1. Add a `### Update YYYY-MM-DD` block under the relevant question
2. State what was learned + cite source
3. If the question is fully resolved, mark `## N. Question — RESOLVED YYYY-MM-DD` and link to the resolving article
4. Don't delete original framing — preserves audit trail of what we knew when
