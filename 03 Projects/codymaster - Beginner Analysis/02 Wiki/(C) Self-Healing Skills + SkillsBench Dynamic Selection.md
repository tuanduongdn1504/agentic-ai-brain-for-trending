# (C) Self-Healing Skills + SkillsBench Dynamic Selection

> **Type:** Entity — novel ops primitive + empirical research
> **Parent:** [[(C) index]]
> **Sources:** [[(C) Novel Primitives cluster summary]] §6, §8-9
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

codymaster treats its 79 skills as **living, degrading artifacts** that require continuous maintenance. The Self-Healing system consists of: **`cm-skill-health`** (continuous audit), **`cm-skill-evolution`** (auto-repair via FIX/DERIVED/CAPTURED modes), **`cm-learning-promoter`** (auto-graduation of recurring patterns), and **advisory reports** (telemetry → diagnosis → repair). Paired with **SkillsBench** (empirical research claiming +18.6pp improvement via `selectTopSkills()` dynamic selection of 2-3 focused skills vs 4+ static), this is the **only T1 framework with both skill-level operational maturity and published empirical grounding**.

## 2. Key claims

1. **Self-Healing is a first-class concept** — 7+ skills dedicated to skill-lifecycle management (cm-skill-health, cm-skill-evolution, cm-skill-search, cm-skill-share, cm-skill-chain, cm-skill-index, cm-skill-mastery)
2. **Three repair modes:** FIX (patch), DERIVED (synthesize from precedent), CAPTURED (promote ad-hoc solution)
3. **Auto-graduation** — recurring tasks become permanent skills automatically via `cm-learning-promoter`
4. **Advisory loop:** metrics + handoff reports drive deliberate repair
5. **SkillsBench result: +18.6 percentage points** for dynamic 2-3 skill selection vs static 4+
6. **`selectTopSkills()`** is the critical function — determines which skills load per task
7. **First T1 framework with published empirical research**

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| Self-healing skill roster | README + skills/ folder listing | High |
| FIX/DERIVED/CAPTURED modes | README explicit | High (named) |
| Auto-graduation | README cm-learning-promoter | High (named) |
| SkillsBench +18.6pp | README claim | Medium (methodology not published) |
| `selectTopSkills()` implementation | README + Smart Spine architecture | Medium (code not inspected) |
| Advisory reports format | README names metrics + handoff | Medium |

## 4. How it works

### Self-Healing cycle

```
User invokes skill cm-X
    ↓
cm-X executes (may succeed or fail)
    ↓
Telemetry → cm-skill-health (audit)
    ↓
Health degrading?
    ├── No → continue
    └── Yes → cm-skill-evolution triggers:
              ├── FIX mode: patch cm-X directly
              ├── DERIVED mode: new skill from working precedent
              └── CAPTURED mode: formalize ad-hoc workaround as skill
    ↓
Recurring task pattern detected?
    └── cm-learning-promoter auto-graduates to permanent skill
    ↓
Advisory reports (metrics, handoff) surface state to user/maintainer
```

### FIX vs DERIVED vs CAPTURED — when each applies

| Mode | Trigger | Outcome |
|------|---------|---------|
| **FIX** | Skill failing but structure correct | Patch skill definition in place |
| **DERIVED** | Current skill broken; similar skill works | Generate new skill from working analog |
| **CAPTURED** | User solved task ad-hoc, pattern recurring | Formalize solution as new skill |

**Who decides the mode?** Not explicit in README. Candidates:
- Heuristic in `cm-skill-evolution` based on failure signature
- LLM reasoning (most plausible given agentic nature)
- User prompt (least likely given "self-healing" framing)

→ Open question Q16.

### Auto-graduation via `cm-learning-promoter`

Recurring tasks → permanent skills. Trigger unclear. Likely:
- Frequency threshold (e.g., 3+ invocations within N days)
- Success-rate threshold (e.g., task solved successfully 2+ times)
- User approval gate (possibly)

→ Open question Q17.

### SkillsBench research — `selectTopSkills()` dynamic selection

**Claim:** Loading 2-3 dynamically-selected skills beats 4+ statically-loaded skills by **+18.6 percentage points** on some benchmark metric.

**Interpretation:**
- Static loading = always same 4+ skills (user picks, or project-default)
- Dynamic = `selectTopSkills()` picks per task based on relevance ranking
- +18.6pp = improvement on success rate / quality metric (metric not specified)

**Why 2-3 wins:**
- Smaller context = more focus, less noise
- Task-appropriate > generic loadout
- Fewer skills means fewer cross-skill conflicts
- LLM attention is finite; more skills = diluted attention

**Skepticism:**
- Methodology not published (Q7) — internal benchmark could be biased toward codymaster's design choices
- No sample size, confidence interval, or distribution shown
- "+18.6pp" specificity suggests real measurement, but without methodology unverifiable

## 5. Worked examples

### Self-Healing example (FIX mode)

User runs `cm-safe-deploy`. Skill expects `.env.production` file. User's project has `.env.prod` (different naming).
- Telemetry captures "file not found: .env.production"
- `cm-skill-health` sees this failure pattern recur across users
- `cm-skill-evolution` triggers FIX: patch `cm-safe-deploy` to check both `.env.production` and `.env.prod`
- Next run succeeds for all users

### Self-Healing example (CAPTURED mode)

User manually writes a custom deploy script for their unusual Kubernetes setup, working around `cm-safe-deploy` limitations.
- Telemetry captures ad-hoc behavior
- `cm-skill-health` notes pattern
- `cm-learning-promoter` + `cm-skill-evolution` CAPTURED mode formalizes: new `cm-k8s-deploy` skill extracted from user's workaround
- Skill available in next session

### SkillsBench selection example

Task: "Refactor this function to use async/await"
- Static loading (4+ skills): cm-tdd + cm-clean-code + cm-code-review + cm-debugging + cm-security-gate — all always present
- Dynamic loading (2-3 skills via `selectTopSkills()`): cm-clean-code + cm-code-review — most task-relevant
- Benchmark result: dynamic +18.6pp on whatever success metric

## 6. Edges + failure modes

### Self-Healing
- **Cascade failure** — if `cm-skill-health` itself degrades, nothing detects the rot
- **Overly aggressive FIX** — may patch skill to please current failure but break other users
- **DERIVED hallucination** — synthesizing new skills from "similar working precedent" may fail silently with LLM errors
- **CAPTURED privacy** — user's ad-hoc solutions may contain secrets, context they don't want graduated to shared skill
- **Auto-graduation runaway** — thousands of auto-graduated skills over time; namespace pollution

### SkillsBench
- **+18.6pp unverified** — without methodology, could be cherry-picked benchmark
- **selectTopSkills() black box** — user can't always tell why certain skills chosen/rejected
- **Selection fragility** — if ranking is off for one task, user gets worse than no-selection

### Advisory loop
- **Report overload** — metrics + handoff reports may become noise if too frequent
- **Interpretation burden** — reports surface state but user must act

## 7. Related concepts

- [[(C) 79 Skills 8 Domains + 11 Commands Architecture]] — skills being healed/selected
- [[(C) 5-Tier Memory + Smart Spine + CodeGraph]] — infrastructure behind cm-skill-health telemetry
- [[(C) VN-Author Native + Tody Le + Storm Bear Peer-Relevance]] — solo author necessitates self-healing

## 8. Cross-project comparison

### vs T1 peers — none have self-healing

| Framework | Skill evolution? | Empirical research? |
|-----------|------------------|---------------------|
| **codymaster** | ✅ FIX/DERIVED/CAPTURED + auto-graduation | ✅ SkillsBench +18.6pp |
| BMAD | Skill validator (structural, not behavioral) | ❌ |
| GSD | Context rot conceptual framework | ❌ |
| gstack | ❌ | ❌ |
| Superpowers | ❌ | ❌ |
| ECC | ❌ | ❌ |

→ **codymaster unique on both axes.**

### vs Karpathy autoresearch (T5)
- autoresearch: val_bpb metric + results.tsv + keep/revert iteration
- codymaster: advisory reports + FIX/DERIVED/CAPTURED iteration
- **Convergent discipline:** both ground iteration in structured metrics + deliberate decisions

→ codymaster is the **only T1 framework bringing T5-Karpathy-level metrics discipline** into the agent-as-assistant space.

### vs deer-flow Sub-Agent System (T5)
- deer-flow: parallel fan-out, no self-healing
- codymaster: self-healing, no fan-out
- Complementary primitives; both reference-worthy

## 9. Open questions

- SkillsBench methodology — benchmark, dataset, metric? (Q7)
- FIX vs DERIVED vs CAPTURED decision logic? (Q16)
- Auto-graduation triggers? (Q17)
- Cascade failure protection — what watches the watcher? (new — Q38)
- CAPTURED privacy controls? (new — Q39)
- How to disable auto-graduation if user prefers manual? (new — Q40)

## 10. Decision log

- **Pre-Self-Healing era** (v1-v3): skills were static markdown
- **Self-Healing introduced** (version unclear, likely v4.x): first auto-repair primitives
- **Auto-graduation** (likely v5.x): cm-learning-promoter
- **SkillsBench research** (recent): empirical grounding for dynamic selection
- **Future:** possibly user-controllable thresholds, audit logs, rollback

## 11. Storm Bear relevance

### Operational lessons for Storm Bear vault routine

codymaster's self-healing parallels what Storm Bear routine v2 could adopt:

1. **Skill health audit** — periodic review of (C) wiki pages for staleness, broken cross-references, outdated claims
2. **FIX/DERIVED/CAPTURED modes** applied to wiki entity pages:
   - FIX: patch stale claim when new evidence surfaces
   - DERIVED: new entity page from similar existing template
   - CAPTURED: ad-hoc note → formalized (C) entity after pattern repeats
3. **Auto-graduation** — recurring Storm Bear patterns (cross-project references, T1 comparison) could auto-promote to standalone entities
4. **Advisory reports** — Storm Bear iteration logs already parallel codymaster's metrics format

### Routine v2 action items (from this entity)

- [ ] Add "wiki health audit" as post-Phase-6 check: orphan pages, broken links, stale Phase 0 claims
- [ ] Codify FIX/DERIVED/CAPTURED modes for wiki page iteration
- [ ] Define auto-graduation rules for recurring cross-wiki patterns
- [ ] SkillsBench-style dynamic selection: when Storm Bear answers a query, select 2-3 most relevant (C) pages vs dumping whole wiki

### Direct use pilot

Pilot `cm-skill-health` on Storm Bear vault itself. Treat vault (C) pages as skills; see if audit surfaces useful findings. Low-risk, high-potential signal.

## 12. Migration / adoption notes

- Self-Healing runs in background — user doesn't invoke directly
- Advisory reports visible via `cm` CLI commands (exact form TBD — Q3)
- To disable: not documented; likely requires manual edit to skill config
- To inspect: SQLite DB contents + learnings.json — observable

## 13. References

- README.md §Self-Healing Skills
- README.md SkillsBench claim
- [[(C) Novel Primitives cluster summary]]
- Parent: [[(C) index]]
- Cross-wiki meta: `../../autoresearch - Beginner Analysis/02 Wiki/(C) val_bpb Metric + Evaluation Fairness.md` (empirical grounding parallel)
