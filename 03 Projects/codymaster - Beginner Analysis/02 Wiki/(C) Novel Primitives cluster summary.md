# (C) Novel Primitives cluster summary — codymaster

> **Sources:** README.md §The Unified Brain + §Smart Spine + §Self-Healing + §Cloud Brain, plus SkillsBench research claim
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster these primitives

codymaster has **8+ distinct novel primitives** — more than any T1 peer (BMAD has 2, GSD has 1, Superpowers has 1, ECC/gstack have 0). Clustering them into one source summary avoids 8 separate summaries and preserves architectural cohesion: they're designed to work together, not as isolated features.

Clustered here:
1. 5-Tier Unified Memory
2. Smart Spine v4.6+
3. CodeGraph
4. `cm://` URI scheme
5. Context Bus
6. Self-Healing Skills (FIX/DERIVED/CAPTURED)
7. Cloud Brain (NotebookLM sync)
8. SkillsBench empirical research

## 2. 5-Tier Unified Memory

Inspired by cognitive-science memory models. codymaster claims:

| Tier | Role | Backing store |
|------|------|---------------|
| **Sensory** | Session context — ephemeral, current turn | In-memory only |
| **Working** | Cross-session scratchpad — recent-but-persistent | `cm-continuity` skill |
| **Long-term** | Durable knowledge with **Ebbinghaus decay** | `learnings.json` file |
| **Semantic** | Vector embeddings — meaning-level retrieval | `cm-deep-search` + `qmd` vector retrieval |
| **Structural** | AST-based codebase understanding | `cm-codeintell` → CodeGraph |

### Key claims
- **Ebbinghaus decay** — real forgetting curve applied to long-term memory (hot items stay, cold items fade)
- **Cross-session persistence** — working + long-term survive restart
- **Vector + structural + keyword** — three orthogonal retrieval modes (Semantic + Structural + SQLite FTS5 in Smart Spine)

### Verification gaps
- Ebbinghaus decay actual algorithm unknown (Q8) — could be simple LRU framed as Ebbinghaus, or real psychological decay model
- `qmd` vector engine not identified — likely proprietary or external
- Long-term `learnings.json` format not fetched

### Why it matters for T1 corpus
No T1 peer has explicit multi-tier memory. Most T1 frameworks live entirely in "Sensory" (session-only) or rely on Claude's built-in memory. codymaster's memory engineering = deepest in T1.

## 3. Smart Spine v4.6+

The coordination substrate underneath all skills. Per README:

- **SQLite + FTS5** — keyword search across skill metadata + context
- **Progressive context loading** — L0 / L1 / L2 tiers (load cheapest-first, escalate as needed)
- **Skill execution caching** — don't re-run the same skill with same inputs
- **`cm://` URI context requests** — skills request context by semantic URI, Smart Spine resolves
- **200k token budget pre-allocated by category** — fixed slot sizes per context type (code / docs / memory / tools)
- **Context bus** — real-time output sharing between chained skills within single execution
- **MCP server exposing 18 tools** — Smart Spine acts as MCP server to the host (Claude / Cursor / Gemini)

### Architectural observations
- **Progressive L0/L1/L2** mirrors deer-flow Skill System (T5) — convergent progressive-loading pattern
- **SQLite + FTS5 + vector + AST** = hybrid search stack. Richer than any T1 peer.
- **MCP server integration** — Smart Spine is not just internal orchestration; it exposes itself to the host runtime via MCP. Makes codymaster a **MCP provider**, not just consumer.
- **Pre-allocated token budget** — explicit budget discipline. GSD ("context rot") has similar concept; codymaster implements it with numeric allocation.

### Open questions
- L0/L1/L2 specifics (Q15)
- MCP 18 tools — what are they? Skill invocation? Memory read/write? Context bus access?
- Context bus = shared memory or pub/sub? Implementation detail matters for chained-skill reliability

## 4. CodeGraph

AST-based structural memory. Claim: **~95% token compression for full-codebase context** via `cm-codeintell`.

### How (inferred)
1. Parse codebase AST (likely tree-sitter or similar)
2. Build graph of symbols + relationships (functions call functions, classes extend classes, files import files)
3. When skill needs "full codebase context", serve graph summary instead of raw code → 95% fewer tokens
4. Skill can drill into specific nodes (specific function bodies) on demand

### Why it matters
- **Token budget pressure is the #1 constraint** in agentic coding (GSD named this "context rot")
- Most T1 frameworks solve via selective loading (read only the files you need) — **reactive**
- codymaster solves via structural compression — **proactive, always-available high-level map**

### Skepticism
- "95% compression" claim unverified — benchmark methodology unclear
- For small codebases the overhead of building/maintaining graph may exceed token savings
- AST-only misses semantic understanding (what does this function actually DO?) — graph is topology, not meaning

### T1 comparison
- GSD: explicit context-rot framing, recommends curation workflows
- BMAD: Scale-Adaptive picks appropriate planning depth
- codymaster: structural compression via CodeGraph
- ECC/SP/gstack: no explicit strategy

→ codymaster has **the most engineered solution to context-rot in T1**.

## 5. `cm://` URI scheme + Context Bus

### `cm://` URI scheme
Skills request context by **semantic URI** (e.g., `cm://codegraph/function/handle_signup` or `cm://memory/longterm/ebbinghaus_hot`), resolved by Smart Spine.

Advantages over file-path-based context requests:
- Semantic (what you need) vs physical (where it lives)
- Abstracts over multi-tier memory (same URI works whether cached in Working or in Structural)
- Enables re-resolution if backend storage changes

### Context Bus
Real-time output sharing between chained skills within single execution. If skill A produces output at step 1, skill B can consume it at step 2 without file intermediate.

**Implementation guess:** shared in-process dict keyed by URI, or streaming pub/sub. README doesn't specify.

### Why both matter
codymaster's skill chain execution has **stateful continuity mid-execution** — unlike most T1 frameworks where each skill invocation is fresh and stateless.

## 6. Self-Healing Skills (FIX/DERIVED/CAPTURED)

codymaster's most ops-centric novel primitive. Per README:

- **`cm-skill-health`** — audits skill quality continuously
- **`cm-skill-evolution`** — repairs via 3 modes:
  - **FIX** — direct patch to failing skill
  - **DERIVED** — generate new skill from working precedent
  - **CAPTURED** — capture ad-hoc solution and formalize as permanent skill
- **`cm-learning-promoter`** — auto-graduates recurring tasks to permanent skills
- **Advisory reports** (`metrics`, `handoff`) drive deliberate repair loops

### Interpretation
codymaster treats skills as **living artifacts that degrade** (due to context drift, tool changes, user feedback) and need continuous maintenance. Unusual level of operational maturity.

### Open questions
- FIX vs DERIVED vs CAPTURED — who decides? Heuristic? LLM? User prompt? (Q16)
- Auto-graduation trigger — frequency threshold? Success-rate threshold? User approval? (Q17)

### T1 comparison
- **Unique to codymaster.** No T1 peer has skill-evolution primitives.
- Closest analog: GSD's context-rot spec mentions "re-calibrate", but doesn't codify repair modes
- BMAD's skill validator is **structural** (schema check), not **behavioral** (functional health)

**Caveat:** for a 38-star project with 79 skills, self-healing may be *necessary* because manual maintenance of 79 artifacts by a solo author is infeasible. Self-Healing = operational survival, not just elegance.

## 7. Cloud Brain (NotebookLM sync)

`cm-notebooklm` syncs high-value patterns to Google NotebookLM for:
- **Cross-machine "soul"** — work on laptop, same brain available on desktop
- **Auto-generated podcasts** — NotebookLM's audio overview feature on codymaster learnings
- **Flashcards** — spaced repetition for human retention

### What's new
- First T1 framework to integrate **T4 bridge tier** (NotebookLM-adjacent) as built-in primitive
- `cm-notebooklm` skill parallels `notebooklm-py` (Storm Bear wiki v7 T4 entrant) — convergent tooling
- Cross-machine persistence via cloud = enterprise use case

### Open questions
- Privacy model: user Google account required? Enterprise SSO? (Q9)
- Does codymaster support multiple brains per user (project-scoped) or one brain per user?

### Storm Bear angle
If Storm Bear pilots codymaster, Cloud Brain could bridge laptop (coaching) + desktop (development) workflows. Potentially eliminates the T4 separate notebooklm-py install.

## 8. SkillsBench empirical research (+18.6pp)

README claims:

> *"2–3 focused skills yield +18.6 percentage points over 4+ statically loaded skills via `selectTopSkills()` dynamic selection"*

### Interpretation
- codymaster ran a benchmark: loading 2-3 skills dynamically (selected per task) vs 4+ skills statically (always loaded)
- Dynamic wins by 18.6 points on some success metric
- Implementation: `selectTopSkills()` function in Smart Spine picks top-ranked skills for current task

### Why this matters
**First T1 framework with published empirical research.** No peer has benchmark data supporting design choices.

### Verification
- Methodology not published in README (Q7)
- "18.6pp" precision suggests real measurement, not marketing
- Benchmark dataset unknown — could be internal codymaster tasks (biased) or open codebase (more credible)

### Design implication
codymaster intentionally constrains skill selection. 79 available → 2-3 active per task. Smart Spine's `selectTopSkills()` is critical path — if selection is wrong, user gets worse results than a single well-chosen skill.

**Risk:** selectTopSkills() is a black box; user can't always tell why certain skills were chosen/rejected.

## 9. Advisory Loop

Telemetry → diagnosis → repair cycle, visible in:
- `cm-skill-health` audit reports (skill quality metrics)
- Advisory reports (`metrics`, `handoff`) — structured data that informs repair decisions
- Deliberate repair loop — user or agent reviews, approves FIX/DERIVED/CAPTURED

### Parallel to Karpathy's autoresearch (v10)
autoresearch's `results.tsv` structured metrics log → iteration on metric decisions. codymaster's advisory reports are similar: structured telemetry drives deliberate changes.

**Storm Bear action item:** codymaster's advisory report format = candidate template for Storm Bear routine v2 metrics log (pending action from v10).

## 10. Integration — how the primitives work together

From README, a typical execution:

1. User invokes skill (e.g., `cm-tdd new-feature`)
2. Smart Spine receives request, checks **skill execution cache** (primitive #2)
3. If miss: Smart Spine asks `selectTopSkills()` (primitive #8) to choose 2-3 skills for task
4. Selected skills request context via `cm://` URI (primitive #4) — Smart Spine resolves from 5-Tier Memory (primitive #1) or CodeGraph (primitive #3)
5. Skills execute, share output via **Context Bus** (primitive #5)
6. Execution complete → telemetry flows to `cm-skill-health` (primitive #6)
7. If pattern recurrent → `cm-learning-promoter` auto-graduates to permanent skill
8. High-value patterns → `cm-notebooklm` syncs to Cloud Brain (primitive #7)

**One cohesive architecture.** Not 8 bolted-on features — interdependent design.

## 11. Maturity assessment

### Signals of maturity
- Coherent architecture (primitives interlock)
- Empirical research (SkillsBench +18.6pp)
- Version discipline (v4.6+, v5.1, v6.0 rolling channels)
- Multi-platform distribution (8+ runtimes)
- 120 commits + 11 tags

### Signals of immaturity
- 38 stars = tiny community
- Solo maintainer (Tody Le) = bus factor 1
- Marketing vs reality gap (79 skills, 11 commands) = documentation discipline not strict
- No published benchmark methodology = SkillsBench claim unverified

→ **Technically sophisticated + community-immature.** Unusual combination. Typically a framework is mature on both dimensions or neither.

**Hypothesis:** codymaster is **heavily dogfooded by its author** (Tody Le's own projects). Depth comes from actual use. Breadth/polish comes from community-at-scale, which codymaster hasn't reached.

## 12. Cross-references

- [[(C) README + VN summary]] — scale claims + VN author context
- [[(C) Skills + Commands + Lifecycle cluster summary]] — how primitives compose into user-facing workflows
- [[(C) 5-Tier Memory + Smart Spine + CodeGraph]] — entity page deep-dive (planned Phase 3)
- [[(C) Self-Healing Skills + SkillsBench Dynamic Selection]] — entity page deep-dive (planned Phase 3)

## Open questions surfaced

- SkillsBench methodology (Q7)
- Ebbinghaus implementation (Q8)
- FIX/DERIVED/CAPTURED decision logic (Q16)
- Auto-graduation triggers (Q17)
- L0/L1/L2 progressive loading specifics (Q15)
- MCP 18 tools inventory (new — Q28)
- Context Bus implementation (shared dict vs pub/sub) (new — Q29)
- Cloud Brain privacy model (Q9)
