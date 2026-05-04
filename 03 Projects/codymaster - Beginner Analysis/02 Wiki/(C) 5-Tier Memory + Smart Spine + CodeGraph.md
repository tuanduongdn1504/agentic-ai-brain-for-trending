# (C) 5-Tier Memory + Smart Spine + CodeGraph

> **Type:** Entity — architecture / novel-primitives cluster
> **Parent:** [[(C) index]]
> **Sources:** [[(C) Novel Primitives cluster summary]] §2-5, §10
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

codymaster's "Unified Brain" is a 3-layer architecture: **5-Tier Memory** (Sensory/Working/Long-term/Semantic/Structural) as storage substrate, **Smart Spine v4.6+** (SQLite+FTS5+progressive loading+cm:// URI scheme+MCP server) as coordination engine, and **CodeGraph** (AST-based structural memory, ~95% token compression) as codebase abstraction. Together they claim the deepest memory/context engineering in T1 — exceeding GSD's "context rot solution" and BMAD's Scale-Adaptive in architectural ambition.

## 2. Key claims

1. **5-Tier memory** — Sensory / Working / Long-term / Semantic / Structural, distinct storage backends
2. **Ebbinghaus decay** on Long-term tier (learnings.json)
3. **Smart Spine = SQLite + FTS5 + L0/L1/L2 progressive loading + cm:// URI + context bus + MCP 18 tools + 200k budget**
4. **CodeGraph = AST-based, ~95% token compression**
5. **`cm://` URI scheme** for semantic context requests
6. **MCP server** — Smart Spine exposes itself to host via MCP (codymaster is MCP provider, not just consumer)
7. **Pre-allocated 200k token budget** by category (code/docs/memory/tools)
8. **Context Bus** for real-time skill-to-skill output sharing

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 5-tier naming + structure | README §The Unified Brain | High |
| Ebbinghaus decay | README — explicit | Medium (implementation unverified) |
| Smart Spine capabilities | README §Smart Spine | High (listed in detail) |
| CodeGraph compression 95% | README | Medium (no benchmark published) |
| cm:// URI scheme | README | Medium (spec not found) |
| MCP 18 tools | README | Medium (tools not enumerated) |
| 200k budget allocation | README | High |

## 4. How it works

### 5-Tier Memory detail

| Tier | Backing | Persistence | Retrieval |
|------|---------|------------|-----------|
| Sensory | In-memory (session) | Current turn only | Direct |
| Working | `cm-continuity` state | Cross-session | URI-keyed |
| Long-term | `learnings.json` + Ebbinghaus | Durable with decay | Decay-weighted |
| Semantic | `cm-deep-search` vector (qmd) | Durable | Similarity |
| Structural | CodeGraph AST | Durable + auto-refresh | Graph traversal |

### Smart Spine flow

```
Skill request:
  ↓
Smart Spine
  ├─ cm:// URI resolver
  ├─ FTS5 keyword search
  ├─ Selectivity: selectTopSkills() picks 2-3
  ├─ Progressive loading L0 → L1 → L2 escalation
  ├─ Budget enforcer (200k total, per-category slots)
  ├─ Skill execution cache (skip re-runs)
  └─ Context bus (mid-execution output sharing)
       ↓
     Skill output → telemetry → cm-skill-health
```

### CodeGraph build

1. `cm-codeintell` traverses repo
2. Parse via AST tooling (likely tree-sitter)
3. Extract: symbols, declarations, imports, call graph, inheritance
4. Serialize to graph structure (likely SQLite tables — Smart Spine already uses SQLite)
5. Serve via `cm://` queries (e.g., `cm://codegraph/function/handle_signup`)
6. Claim: when skill needs "give me the codebase", return graph summary → ~5% of raw-code tokens

### cm:// URI examples (inferred)

```
cm://memory/working/current-sprint
cm://memory/longterm/tdd-patterns
cm://codegraph/function/handle_signup
cm://codegraph/file/src/auth.ts
cm://skills/cm-tdd/template
cm://telemetry/cm-safe-deploy/last-run
```

## 5. Worked example

**Scenario:** User asks Claude (via codymaster) to refactor `handle_signup` across 50-file codebase

Without codymaster:
- Claude reads many files, burns ~100k tokens, may miss related functions

With codymaster Smart Spine:
1. Skill request: `refactor handle_signup`
2. `selectTopSkills()` chooses `cm-autopilot` + `cm-clean-code`
3. `cm://codegraph/function/handle_signup` returns signature + callers + callees (small payload)
4. Skill inspects callers → decides `handle_signup` used in 7 places
5. Requests each caller context via `cm://codegraph/file/<path>` (drill-down)
6. Edits emitted, context bus carries intermediate state
7. Post-execution: `cm-skill-health` logs telemetry

**Net effect:** Same refactor, dramatically less token usage (claim: ~95% savings for structural navigation).

## 6. Edges + failure modes

### CodeGraph
- **Small codebase penalty** — graph build overhead may exceed compression savings for <10-file projects
- **Stale graph** — if user edits outside codymaster, graph diverges until `cm-codeintell` refresh
- **AST limits** — graph shows topology (what calls what) not semantics (what does it DO). LLM still needs to read function bodies for meaning-level work.

### Smart Spine
- **SQLite concurrency** — better-sqlite3 is synchronous; multi-skill parallel execution needs careful locking
- **`cm://` URI resolution failures** — undefined URIs = error path; graceful fallback to standard file paths?
- **L0/L1/L2 tier boundaries** — if L0 is insufficient and L1 is expensive, escalation policy matters
- **MCP server stability** — Smart Spine exposing 18 MCP tools means host invokes it; if Spine crashes, host may hang

### 5-Tier Memory
- **Ebbinghaus decay** — if algorithm mis-tuned, hot patterns get pruned or stale patterns retained
- **Semantic tier (qmd vector)** — vector DB freshness; embeddings stale after model updates?
- **learnings.json** — single file = merge conflicts if multi-machine (hence Cloud Brain NotebookLM sync)

### Context Bus
- **Chain failures** — if skill A in chain fails, does downstream skill B get partial state?
- **Concurrent writes** — multi-producer context bus = race conditions possible

## 7. Related concepts

- [[(C) 79 Skills 8 Domains + 11 Commands Architecture]] — consumers of this brain
- [[(C) Self-Healing Skills + SkillsBench Dynamic Selection]] — `selectTopSkills()` is in this entity
- [[(C) VN-Author Native + Tody Le + Storm Bear Peer-Relevance]] — who designed this

## 8. Cross-project comparison

### vs GSD (context rot)
- **GSD:** conceptual framework — "context rot is the problem; curate workflows"
- **codymaster:** engineered solution — CodeGraph + progressive loading + pre-allocated budget
- Verdict: GSD defines problem rigorously, codymaster solves it concretely. Complementary.

### vs BMAD (Scale-Adaptive)
- **BMAD:** Scale-Adaptive picks planning depth heuristic
- **codymaster:** Multi-tier memory + progressive loading picks everything (planning, code, memory)
- Verdict: codymaster broader; BMAD targeted.

### vs deer-flow (T5 Skill System progressive loading)
- **deer-flow:** progressive loading for skill ingestion at T5 level
- **codymaster:** progressive loading for context at T1 level
- Verdict: **convergent design** across tiers. Same primitive (progressive loading) solving different problems.

### vs Karpathy autoresearch (T5 structured metrics)
- **autoresearch:** results.tsv structured log
- **codymaster:** advisory reports (metrics/handoff) parallel concept
- Verdict: **parallel to autoresearch metrics design** — codymaster brings T5 discipline into T1.

## 9. Open questions

- Ebbinghaus algorithm real vs metaphor? (Q8)
- 95% CodeGraph compression benchmark? (new — Q35)
- MCP 18 tools inventory? (new — Q28)
- cm:// URI spec published? (new — Q15)
- Context Bus implementation? (new — Q29)
- L0/L1/L2 tier definitions? (Q15)
- Qmd vector engine — proprietary or open? (new — Q36)
- Smart Spine version history — v4.6+ current; what was v4.0? (new — Q37)

## 10. Decision log

- **Early versions (v1-v3 era):** probably simpler memory model
- **v4.x:** Smart Spine introduced (v4.6+ mentioned in README = current stable)
- **v5-v6:** CodeGraph + Cloud Brain added
- **Future trajectory:** unknown; self-healing of Smart Spine itself could emerge

## 11. Storm Bear relevance

### Architectural lessons for Storm Bear vault

codymaster's brain architecture offers templates for Storm Bear vault improvements:

1. **5-Tier memory model** — Storm Bear wiki = Long-term tier; Storm Bear chats = Sensory/Working. Could formalize wiki as "structured long-term", unstructured notes as "working".
2. **Ebbinghaus decay** — Storm Bear vault has no decay model (everything retained forever). codymaster's approach = let cold items fade, hot items persist. Could inform vault pruning strategy.
3. **Structural memory (CodeGraph analog)** — Storm Bear vault's cross-reference graph is already AST-adjacent (links between (C) pages). Formalizing this as first-class data = codymaster-inspired enhancement.
4. **cm:// URI scheme** — vault could adopt `vault://` URI scheme for semantic queries (`vault://t1-comparison/latest`, `vault://open-questions/unresolved`).
5. **Pre-allocated token budget** — Storm Bear wiki builds don't enforce budget. codymaster pre-allocates. Routine v2 candidate.

### Direct use
- `cm-continuity` could serve Storm Bear session-continuity needs
- `cm-deep-search` could search Storm Bear vault semantically (if pointed at vault)
- `cm-notebooklm` already invokes NotebookLM — parallel to Storm Bear's v7 notebooklm-py wiki

## 12. Migration / adoption notes

- Brain is mostly invisible to user — skills consume it, user sees outputs
- Adoption barrier = trusting black-box memory. Start with small project to observe behavior.
- Debug path: if skill behaves unexpectedly, inspect `learnings.json` + Smart Spine SQLite DB directly

## 13. References

- README.md §The Unified Brain + §Smart Spine
- Parent: [[(C) index]]
- Cross-wiki: `../../get-shit-done - Beginner Analysis/02 Wiki/(C) Context Rot Solution.md` (GSD's conceptual framing)
- Cross-wiki: `../../deer-flow - Beginner Analysis/02 Wiki/(C) Skill System (Progressive Loading).md` (T5 convergent pattern)
