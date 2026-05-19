# v71 agents-best-practices Wiki — Commands & Routines

## LLM Wiki Routine v2.2

All work on this v71 wiki follows **LLM Wiki Routine v2.2** (codified 2026-05-14; FIFTH wiki built under v2.2). 

Routine documentation: `/Users/Cvtot/KJ OS Template/05 Skills/llm-wiki-routine-v2.2.md`

Key phases:
- **Phase 0:** Pre-computed classification, Pattern Library pre-check, corpus-firsts
- **Phase 1:** Foundational files (CLAUDE.md, COMMANDS.md, index, log)
- **Phase 2:** Open questions + iteration log
- **Phase 3:** Three cluster summaries (user-facing, contributor-facing, technical)
- **Phase 4:** Four entity pages (canonical 13-section format)
- **Phase 5:** Beginner guide (bilingual VN/EN, 400-700 lines)
- **Phase 6:** Vault state sync (CLAUDE.md update; separate session)

---

## Cross-Project References

### Pattern Library

**Pattern Library documentation:**
- Root shim: `/Users/Cvtot/KJ OS Template/PATTERN_LIBRARY.md`
- Chapter files: `/Users/Cvtot/KJ OS Template/_patterns/`
- State history: `/Users/Cvtot/KJ OS Template/_state/02-pattern-library-state-history.md`
- Recent additions: `/Users/Cvtot/KJ OS Template/_patterns/05-recent-additions.md`

**Patterns cited at v71:**
- Pattern #21 (SDD Methodology Emergence)
- Pattern #66 (Supply-Chain Isolation)
- Pattern #78 (Living-Domain-Standards Tracking)
- Pattern #83 (Honest-Deficiency-Disclosure Discipline)
- Pattern #84 (Cross-Vendor Ecosystem-Tolerance) — PRIMARY Phase 4b
- Pattern #52 (Sustained-Velocity sub-threshold test)
- Pattern #57 (corpus reference)
- NEW candidate OC-O (Agentic-Harness-Execution-Separation)

### Storm Bear Vault

**Storm Bear meta-entity classification:** CLAUDE.md § Storm Bear (Phase 0.9)

**Vault structure:**
- Root CLAUDE.md: `/Users/Cvtot/KJ OS Template/CLAUDE.md` (entry-point shim; post-refactor session 67)
- Vault state chapters: `/Users/Cvtot/KJ OS Template/_state/`
- Recent projects v61-v70: `/Users/Cvtot/KJ OS Template/_state/03c-projects-v61-v70.md`

### Sibling Corpus Subjects (v71 cross-references)

**To link in all entity pages + cluster summaries:**
- v66 agentmemory: `/Users/Cvtot/KJ OS Template/03 Projects/agentmemory - Beginner Analysis/`
- v65 claude-code-system-prompts: `/Users/Cvtot/KJ OS Template/03 Projects/claude-code-system-prompts - Beginner Analysis/`
- v64 claude-seo: `/Users/Cvtot/KJ OS Template/03 Projects/claude-seo - Beginner Analysis/`
- v62 codex-plugin-cc: `/Users/Cvtot/KJ OS Template/03 Projects/codex-plugin-cc - Beginner Analysis/`
- v63 andrej-karpathy-skills: `/Users/Cvtot/KJ OS Template/03 Projects/andrej-karpathy-skills - Beginner Analysis/`
- v61 cc-sdd: `/Users/Cvtot/KJ OS Template/03 Projects/cc-sdd - Beginner Analysis/`

---

## File Creation Order (Phase 1-6)

### Phase 1: Foundational Files
✓ CLAUDE.md (completed)
→ COMMANDS.md (this file)
→ 01 Analysis/(C) index.md
→ 02 Wiki/(C) log.md

### Phase 2: Open Questions + Iteration
→ 01 Analysis/(C) open questions.md
→ 01 Analysis/(C) iteration-log.md

### Phase 3: Cluster Summaries
→ 02 Wiki/(C) user-facing cluster summary.md
→ 02 Wiki/(C) contributor-facing cluster summary.md
→ 02 Wiki/(C) technical-distribution cluster summary.md

### Phase 4: Entity Pages (13-section canonical format)
→ 02 Wiki/(C) entity-1-core-skill.md
→ 02 Wiki/(C) entity-2-distribution-ecosystem.md
→ 02 Wiki/(C) entity-3-pattern-library.md
→ 02 Wiki/(C) entity-4-storm-bear.md

### Phase 5: Beginner Guide
→ 03 Published/(C) agents-best-practices - Huong dan cho nguoi moi.md

### Phase 4b PRIMARY: Pattern #84 Promotion
→ 01 Analysis/(C) Pattern-84-cross-vendor-ecosystem-tolerance-N3-promotion-evaluation.md

---

## Key Concepts (Quick Reference)

### agents-best-practices Core Philosophy

**Fundamental rule:** "The model never executes a tool directly. It emits a structured request. The harness executes or rejects it."

**8 Foundational Principles:**
1. Operational rigor in harnesses
2. Explicit validation before execution
3. Risk-stratified permission paths
4. Separated drafting and commitment phases
5. Built rather than dumped context
6. Budget constraints
7. Progressive tool disclosure
8. Failure-driven feature development

**7 Loop Invariants (execution separation):**
1. Each tool call gets exactly one result
2. Arguments parsed and validated before execution
3. Permission decisions occur before side effects
4. Results bounded, structured, traceable
5. Hard budgets for steps, time, tokens, cost, calls
6. Final answers derive from observations, not assumed success
7. Errors become structured observations

**Autonomy Levels (L0-L4):**
- L0: Answer-only (no tool calls)
- L1: Draft-only (proposals, no side effects)
- L2: Approval-gated action
- L3: Policy-bounded autonomy
- L4: Long-running objectives

**Key quotes:**
- "Most agent failures are not caused by insufficient autonomy. They are caused by weak harness boundaries."
- "Prompt-only safety is insufficient."
- "The best context is not the largest but the smallest context that lets the model choose the correct next action."
- "Move up autonomy levels only when evals show the simpler level is insufficient."

### Pattern Library Integration (v71)

**Pattern #84 PRIMARY:** Cross-Vendor Ecosystem-Tolerance, N=3 promotion evaluation
- v71 represents NEW sub-archetype (84c: Provider-Agnostic-By-Design)
- Differs from v62/v65 ecosystem-tolerance (which are ecosystem-norm evidence)
- Evaluation format: `01 Analysis/(C) Pattern-84-cross-vendor-ecosystem-tolerance-N3-promotion-evaluation.md`

**Pattern #78 SECONDARY:** Living-Domain-Standards Tracking, N=3 within-pattern strengthening
- Agents-best-practices integrates 3-vendor triple-standard: OWASP + NIST + MCP spec 2025-11-25

**NEW candidate OC-O:** Agentic-Harness-Execution-Separation (7-invariant formalization of model-proposes/harness-disposes separation)

---

## Storm Bear Usage (v71 MODERATE 2/4)

**Application path:** Directly deployable as Claude Code skill for Storm Bear's vault agentic work

**Methodology influence:** 7-invariant loop architecture informs future routine v2.3 refinement

**Recommended reading:**
- Autonomy levels (L0-L4) as vault task-safety gating
- Context tier 12-tier architecture (applies to vault context management)
- Planning mode for non-trivial vault tasks
- Draft-commit pattern for multi-step vault operations

**Skill installation:**
```bash
npm install -g skills
skills attach DenisSergeevitch/agents-best-practices
```

---

## Engagement Signal Sub-Investigation

**Metadata for v72+ evaluation:**

| Signal | Value | Interpretation |
|---|---|---|
| Stars | 821 | Small scale; 4-day-old repo |
| Stars/day | 205.25 | HIGH (below Pattern #52 >300; above median T1) |
| Forks | 72 | Healthy community engagement |
| Fork ratio | 0.088 | Healthy (>0.05 threshold) |
| Watchers | 4 | Low; auto-watch only likely |
| Open issues | 4 | Minimal (0.0049 ratio; not a support burden) |
| Subscribers | 4 | Very low; passive audience |
| Age | 4 days | Too young for sustained classification; re-evaluate at v72+ |
| Engagement trend | Explosive growth | Consistent 200+ stars/day suggests viral adoption or cross-platform linking |

**v72+ follow-up:** Track sustained velocity at v72+ audit to determine if Pattern #52 candidate (>300 stars/day sustained-moderate-high threshold).

---

## Velocity Note (Corpus Context)

**Velocity classification at v71:** HIGH-velocity-NOT-EXTREME
- 205.25 stars/day at 4-day window
- Below Pattern #52 >300 threshold
- Above corpus median T1 (~50 stars/day)
- Too young for "sustained" classification; wait for 2-4 week window

**Comparison:**
- v68 zero: 1,050 stars/day (CORPUS 2nd-HIGHEST)
- v69 CloakBrowser: 172.7 stars/day (sub-threshold control case)
- v71 agents-best-practices: 205.25 stars/day (NEW sub-threshold control case joining v69)
- v63 andrej-karpathy-skills: ~1,186 stars/day (CORPUS RECORD)

**Recommendation for v72:** Monitor agents-best-practices velocity. If sustained >300 stars/day at v72 audit, initiate Pattern #52 evaluation batch.

---

## Phase 0.9 Storm Bear Meta-Entity

**Recommendation:** MODERATE INCLUDE (2/4 PASS)

**Rationale:**
- (b) PASS: Directly installable Claude Code skill; applicable to vault agentic harness work
- (c) PASS: Methodology influence recognized (7-invariant loop informs routine v2.3 refinement)
- (a) FAIL: Author Eastern European; not demographic match
- (d) FAIL: No explicit corpus-subject URL citation (Pattern #57 threshold not met)

**Usage:** Read SKILL.md + 15 references for context-architecture and planning-mode sections. Test autonomy levels (L0-L4) for vault task safety-gating. Integrate draft-commit pattern into routine v2.3 design for multi-step vault operations.

---

## Deferred to Phase 6 (Vault Sync)

The following state updates are deferred to Phase 6 (separate session) because they modify vault-level files:

- Update `/Users/Cvtot/KJ OS Template/_state/03c-projects-v61-v70.md` to rename chapter to `03c-projects-v61-v71.md` and append v71 agents-best-practices entry
- Update `/Users/Cvtot/KJ OS Template/CLAUDE.md` weekly update section with v71 wiki-ship summary
- Update `/Users/Cvtot/KJ OS Template/PATTERN_LIBRARY.md` state block (44→44 confirmed, 30→30 active, OC count 21→22 if OC-O registered)
- Update `/Users/Cvtot/KJ OS Template/_patterns/05-recent-additions.md` with v71 wiki-ship narrative and Phase 4b primary (Pattern #84 N=3 evaluation + OC-O candidate)

---

## Next Command

```bash
# Phase 1: Foundational files complete
# Phase 2: Begin open questions and iteration log
cd "/Users/Cvtot/KJ OS Template/03 Projects/agents-best-practices - Beginner Analysis/01 Analysis"
# See: 01 Analysis/(C) open questions.md, (C) iteration-log.md
```
