# Entity 4: Storm Bear Meta-Entity Integration

**Type:** Meta-operational integration | **Classification:** MODERATE 2/4 INCLUDE | **Deployment:** Claude Code skill for vault autonomous harness | **Influence Path:** Routine v2.2-v2.3 methodology refinement

---

## 1. What is it?

Storm Bear integration point for agents-best-practices within the LLM Wiki vault operating system. agents-best-practices as reusable Claude Code skill providing execution-separation discipline + autonomy-level governance for v2.2-v2.3 wiki-build routine. Operational relevance: Direct applicability to hireui-harness coding tasks (Claude Code skill library expansion for agent tools). Methodology relevance: 7-invariant loop + autonomy levels inform routine refinement (Phase 0.9 INCLUDE evaluation criteria b+d).

---

## 2. Who uses this entity?

- **Vault operators (Storm Bear):** Running autonomous wiki-build routine v2.2 with governance guardrails
- **Claude Code skill designers:** Implementing agents-best-practices patterns in agent harness tools
- **Methodology researchers:** Evaluating how agents-best-practices influences LLM Wiki Routine v2.3 codification
- **Pilot candidates:** agents-best-practices proposed as companion skill to agentmemory (fenced-pilot sequence)

---

## 3. Core function

Provide execution-separation discipline + autonomy-level gating for Storm Bear's autonomous wiki-build harness. agents-best-practices formalizes the operational contract between Claude Code skill (inference layer proposing actions) and vault harness (execution layer validating, approving, executing, recording). Integration enables vault-level permission matrices (role × action → approval required), hard budgets (step limit, time limit, token limit, cost cap), and structured error observations (errors become data, not silent failures).

---

## 4. Architecture

```
Storm Bear Vault Level
  ├─ Wiki-Build Harness (execution layer)
  │  ├─ Permission Matrix (role × action → approval)
  │  ├─ Budget Controller (step/time/token/cost limits)
  │  └─ Trace Recorder (every decision logged)
  │
  ├─ Claude Code Skill (inference layer)
  │  └─ agents-best-practices governance module
  │     ├─ 7-invariant loop (proposal validation)
  │     ├─ Autonomy levels (L0-L4 task gating)
  │     ├─ Risk taxonomy (tool classification)
  │     └─ Error-as-observation (decision visibility)
  │
  └─ Integration Points
     ├─ Planning Mode (complex wiki tasks → objective-aware phases)
     ├─ Draft-Commit Pattern (Phase 6 vault sync → two-phase approval)
     ├─ Context Architecture (12-tier model for compaction discipline)
     └─ Observability (trace grading per wiki-build step)
```

---

## 5. Key concepts

### Execution-Separation in Vault Context

**Model (Claude Code skill) proposes; harness executes or rejects.**

When building v71 wiki:
- **Skill proposes:** "Create entity-1-core-skill.md with these 13 sections"
- **Harness validates:** (Before execution) Does agent have WRITE permission to /02 Wiki/? Is task within Step 25 limit? Token budget OK?
- **Harness checks permission:** (Approval matrix lookup) LLM Wiki Builder role + Write /projects/*/02\ Wiki/ action → Medium risk → Auto-approve (within scope)
- **Harness executes:** Writes file
- **Harness records:** Trace log entry: {tool: Write, timestamp, file_path, content_size, permission_check: PASS, budget_check: PASS, cost_usd: 0.0015}
- **Skill sees observation:** "File created successfully; 1,245 words written; token cost $0.0015; step 8/50"

If validation failed (e.g., permission denied):
- **Skill sees structured error:** {error_code: PERMISSION_DENIED, attempted_action: "Write /CLAUDE.md (vault root)", recovery_suggestion: "Phase 6 only; requires human approval"}
- **Skill can decide recovery:** Try alternative file, escalate to human, log for audit

### Autonomy Levels for Wiki-Build Tasks

**L0 (Answer-only):** Skill generates wiki-build analysis without tool execution (research phase).

**L1 (Draft-only):** Skill proposes file contents but cannot execute writes (draft entities, query questions, iteration plans).

**L2 (Approval-gated):** Simple reads/writes auto-approved; risky writes (Phase 6 vault sync) require human approval before execution.

**L3 (Policy-bounded):** Tools execute within policies (write to /02 Wiki/ only; don't modify CLAUDE.md or PATTERN_LIBRARY.md; hard step limit 50).

**L4 (Long-running objectives):** Multi-day wiki builds with minimal supervision; only high-risk operations escalated.

**Gating rule per agents-best-practices:** Move up levels only when evals show current level insufficient. v71 wiki builds run at **L2 (approval-gated)** for foundational files + clusters + entities; Phase 6 vault sync requires **L2→L3 transition** with human approval gate (not yet executed; deferred to Phase 6 session).

### Risk-Stratified Tool Taxonomy

Tools in vault-harness context:

| Category | Tools | Approval Path |
|---|---|---|
| Read-only | Read project files / Search wiki | Auto-allow (no side effects) |
| Query | WebFetch / Web search | Auto-allow (safe, informational) |
| Draft | Write to /02 Wiki/ within project | Auto-allow (project scope) |
| Write | Modify /03 Projects/ structure | Auto-approval (within role) |
| Write-sensitive | Modify /CLAUDE.md (root) | Human approval (vault root) |
| Delete | Remove project files | Human approval + confirmation (irreversible) |
| Financial | API costs >$0.10 | Human approval (budget cap) |

v71 wiki build uses **Read + Query + Draft + Write categories only** (no sensitive/destructive operations). Phase 6 vault sync will require **Write-sensitive approval** (modifying vault-root PATTERN_LIBRARY.md + CLAUDE.md chapters).

### Context Architecture for Compaction

12-tier context model ensures vault-critical information survives compaction:

**Preserved during compaction:** Objective (v71 wiki build), plan (Phase 0-6 roadmap), approval state (which human decisions made), resources (corpus subjects read), key facts (velocity, corpus-firsts, promotion verdict), artifacts (files created), open questions, next step.

**Removed during compaction:** Duplicate prose, old logs, stale branches, irrelevant exploration, failed attempts, exploratory reasoning.

Example: After creating entity-1 page, compaction logs show "Removed: 3 exploratory entity-structure iterations; preserved: final 13-section format decision + rationale; next: entity-2."

### Planning Mode for Complex Tasks

**When to activate:** Multi-step objectives requiring phase synchronization (wiki builds, routine v2.2 codification, pilot deployments).

**Structure:** Objective → Phases → Risks per phase → Approval checkpoints → Validation per phase → Exit criteria.

v71 wiki-build planning:
- **Objective:** Build comprehensive wiki for agents-best-practices v71 contribution to Pattern Library
- **Phases:** 0 (pre-compute) → 1 (foundational) → 2 (analysis) → 3 (clusters) → 4 (entities) → 5 (beginner guide) → 4b (Pattern evaluation) → 6 (vault sync)
- **Risks:** Token context-thrashing (mitigation: 50K token budgets per phase), permission errors (mitigation: pre-check role matrix), file conflicts (mitigation: (C) prefix convention), cross-reference drift (mitigation: link validation checklist)
- **Checkpoints:** Phase 1 completeness → Phase 3 cluster quality → Phase 4 entity cross-linking → Phase 4b Pattern verdict → Phase 6 approval gate
- **Validation:** Quality check per phase (13 sections present, cross-links valid, word counts adequate, no placeholders)
- **Exit criteria:** All files present + all cross-links valid + Pattern Library state ready for sync + beginner guide deployed

### Draft-Commit Pattern for Phase 6

**High-risk operations (Phase 6 vault sync) use two-phase separation:**

**Phase 6a (Draft):** Generate proposed changes
- Prepare updated `_state/03c-projects-v61-v71.md` with new v71 entry
- Prepare proposed PATTERN_LIBRARY.md changes (OC count updates, audit batch notes)
- Prepare proposed CLAUDE.md weekly update § amendments
- Human reviews drafts in staging area (not committed yet)

**Phase 6b (Commit):** Execute with approval
- Human approves changes via explicit gate ("Approve Phase 6 sync? Y/N")
- Harness executes file mutations
- Trace log records all mutations with timestamps
- Vault operator verifies mutations successful (git diff, file validation)

**Separation rationale:** Phase 6 mutations are irreversible (committed to vault state). Two-phase prevents accidental state corruption.

---

## 6. Design philosophy

**Operational rigor as vault requirement:** The vault harness is the locus of safety. Model (skill) proposes; harness disposes. Validation precedes execution.

**Autonomy-level progression as deployment gate:** Don't jump to L3 (policy-bounded) until L2 (approval-gated) evals pass consistently. v71 wiki runs at L2; Phase 6 vault sync requires explicit human L2→L3 transition approval.

**Budget discipline as non-negotiable:** 50K tokens per phase, 50 steps per phase, $1.00 cost cap per wiki-build. If approaching limits, compaction + re-check required.

**Errors as vault observations:** Silent failures corrupt vault state. agents-best-practices enforces structured error visibility (error_code, error_message, recovery_suggestion, trace_id). Vault operator sees every failure and decides on recovery.

---

## 7. Configuration & integration into vault

**Installation into Claude Code harness:**

```bash
# Path 1: Skills CLI (recommended for vault)
npm install -g skills
skills attach DenisSergeevitch/agents-best-practices

# Path 2: Git clone (vault git-tracked fallback)
git clone https://github.com/DenisSergeevitch/agents-best-practices.git
cp -r agents-best-practices/SKILL.md /Users/Cvtot/KJ\ OS\ Template/05\ Skills/
cp -r agents-best-practices/references/ /Users/Cvtot/KJ\ OS\ Template/05\ Skills/agents-best-practices-refs/
```

**Vault-level CLAUDE.md skill reference (Section: Pattern references):**

Add entry to `_state/01-skill-references.md`:
```markdown
## Skill 6: agents-best-practices (v71)

**Purpose:** Execution-separation discipline for wiki-build harness
**Type:** T1 Assistant Skill (markdown-only governance framework)
**Integration:** Claude Code skill; 7-invariant agentic loop + autonomy levels L0-L4
**Tier:** T1 (core agent framework)
**Platforms:** Claude Code (primary) + Codex (compatible) + OpenAI Agents (compatible)
**Dependency:** 15-reference file library (48KB markdown; prompt-cache compatible)

**Key exports:**
- 7-invariant agentic loop (proposal validation)
- Autonomy levels L0-L4 (task-gating discipline)
- Risk-stratified tool taxonomy (approval path mapping)
- 15-category security threat model
- Draft-commit pattern (high-risk operations)

**Storm Bear vault integration:**
- Permission matrix (role × action → approval)
- Budget constraints (step/time/token/cost limits)
- Error-as-observation discipline
- Context compaction guardrails
- Observability trace grading
```

**Permission matrix for vault automation:**

```yaml
# /Users/Cvtot/KJ OS Template/CLAUDE.md (or delegated to harness config)
permissions:
  role: LLM-Wiki-Builder
  actions:
    - action: Read /03-Projects/*/02-Wiki/
      risk: Low
      approval_required: false
      note: "Analysis phase; read-only"
      
    - action: Write /03-Projects/*/02-Wiki/(C)_*.md
      risk: Medium
      approval_required: false
      note: "Project-scoped wiki files within convention"
      
    - action: Modify /CLAUDE.md (vault root)
      risk: High
      approval_required: true
      note: "Phase 6 only; vault-root mutation"
      
    - action: Modify /PATTERN_LIBRARY.md
      risk: High
      approval_required: true
      note: "Pattern state sync; state mutation"
      
    - action: Delete /03-Projects/*/02-Wiki/
      risk: Very-High
      approval_required: true
      note: "Irreversible; requires human confirmation"

budget_limits:
  per_phase:
    step_limit: 50
    time_limit: 5m
    token_limit: 50000
    cost_cap: $1.00
  per_wiki_build:
    total_steps: 200
    total_time: 30m
    total_tokens: 200000
    total_cost: $5.00
```

**Hard budgets enforcement (vault harness config):**

```python
# Pseudo-code for vault harness
class WikiBuildBudgets:
    def __init__(self):
        self.phase_steps = 0
        self.phase_tokens = 0
        self.phase_cost = 0
        self.total_steps = 0
        self.total_cost = 0
    
    def check_before_tool_call(self, tool_name, estimated_tokens):
        # Pre-execution check
        if self.phase_steps >= 50:
            raise BudgetExhausted("Phase step limit reached")
        if self.phase_cost + estimated_tokens * COST_PER_TOKEN > 1.00:
            raise BudgetExhausted("Phase cost limit reached")
        if self.total_steps >= 200:
            raise BudgetExhausted("Wiki-build step limit reached")
    
    def record_tool_execution(self, tool_name, tokens_used, cost):
        self.phase_steps += 1
        self.phase_tokens += tokens_used
        self.phase_cost += cost
        self.total_steps += 1
        self.total_cost += cost
        # Log to trace for audit
```

---

## 8. Integration with other entities

- **Entity 1 (Core Skill):** Defines 7-invariant loop + autonomy levels + risk taxonomy; Entity 4 applies these to vault operations
- **Entity 2 (Distribution):** agents-best-practices deployed via skills CLI into Claude Code harness; Entity 4 documents vault-specific installation
- **Entity 3 (Pattern Library):** documents corpus-wide integration; Entity 4 focuses on Storm Bear operational instance
- **v66 agentmemory:** Sister operational integration; complements agents-best-practices (harness governance + memory system for long-task persistence)

**Related vault files:**
- `_state/01-skill-references.md` — skill definition shim (update with agents-best-practices entry post-Phase 6)
- `05 Skills/llm-wiki-routine-v2.2.md` — routine definition (references agents-best-practices principles in v2.2-v2.3 codification notes)
- `/CLAUDE.md` (this vault root) — weekly update § should reference agents-best-practices integration point post-Phase 6

---

## 9. Typical workflow (Vault operator)

**Pre-wiki (Phase 0):**
1. Review agents-best-practices corpus pre-check (within corpus, governance patterns align with v2.2)
2. Verify skills CLI installed: `skills list | grep agents-best-practices`
3. If not installed, run: `npm install -g skills && skills attach DenisSergeevitch/agents-best-practices`
4. Confirm skill available to Claude Code harness

**During wiki-build (Phases 1-5):**
1. Harness loads agents-best-practices skill context on startup
2. Skill context provides governance guardrails (autonomy-level gating, risk taxonomy, error-as-observation)
3. Each wiki phase checked against permission matrix:
   - Phase 1-3: Auto-allow (within project scope, no vault mutation)
   - Phase 4: Check cross-links (read validation only)
   - Phase 5: Auto-allow (published artifact, no mutation)
4. Budget tracking: observe phase_steps, phase_tokens, phase_cost displayed after each phase
5. Error handling: if tool fails, harness surfaces structured error; operator decides on recovery or escalation

**Phase 6 (Vault sync, approval-gated):**
1. Harness generates draft Phase 6 mutations:
   - `_state/03c-projects-v61-v71.md` (new v71 entry)
   - PATTERN_LIBRARY.md updates (OC count, audit batch notes)
   - CLAUDE.md weekly update § amendments
2. Human (vault operator) reviews draft changes (read staging area files)
3. Human approves via explicit gate: "Ready to commit v71 state sync? Type 'APPROVE' to proceed"
4. Harness commits mutations if approved; logs all changes to trace
5. Operator verifies: `git diff HEAD~1` confirms expected mutations only

**Post-wiki (logging & audit):**
1. Trace log review: all 200 steps, $5.00 cost, 200K tokens accounted for
2. Quality audit: 13-section canonical format verified for all entity pages
3. Cross-link validation: all inter-wiki links tested (read + grep search confirms all refs exist)
4. Pattern Library audit checklist (from entity-3): 5 promotion criteria for Pattern #84 verified PASS
5. Archive trace log to `04 Reviews/(C) 2026-05-19 v71-agents-best-practices wiki-build trace.md`

---

## 10. Tradeoffs

**Strengths:**
✓ Harness-native governance (7-invariant loop directly applicable to vault automation)
✓ Autonomy-level progression matches v2.2 maturity model (L0 analysis → L1 drafting → L2 approval-gated)
✓ Risk taxonomy maps clearly to vault permission matrix (read-only allow → write-sensitive require-approval)
✓ Error-as-observation discipline prevents silent vault corruption
✓ Budget enforcement prevents token runaway (critical for multi-wiki pipelines)
✓ Draft-commit pattern provides safety for Phase 6 state mutations

**Limitations:**
✗ Requires harness implementation (agents-best-practices provides discipline, not auto-execution)
✗ Permission matrix requires operator curation (must define role × action table for vault)
✗ Autonomy-level gating requires evaluation discipline (must assess evals before L2→L3 transition)
✗ Budget enforcement requires monitoring (operator must check phase budgets, not automated yet)
✗ Compaction discipline is manual (operator must preserve objective/plan/approval-state during context cuts)

---

## 11. Methodology influence on routine v2.2-v2.3

**v2.2 integration (current):**
- 7-invariant loop validates wiki-build harness design (each phase gets exactly one result; arguments validated before tool execution; permission checks precede mutations; budgets enforced)
- Autonomy levels L0-L4 informed v2.2 phase structure (Phase 0 analysis = L0 answer-only; Phase 1-5 = L1-L2 with approval gates; Phase 6 = L2 with explicit human approval)
- Risk taxonomy integrated into Phase 0 pre-check (corpus classification = risk assessment)
- Error-as-observation discipline applies to wiki-build error handling (all tool failures surface as structured observations)

**v2.3 refinement candidates (deferred to v75-v80 natural cadence):**
- **Sub-agent coordination:** Multiple skill-loads (agents-best-practices + agentmemory) require synchronization protocol (define skill-load order, context-sharing format)
- **Compaction trigger formalization:** When to initiate context compaction? agents-best-practices suggests: "Before 75% token budget consumed" or "After 30 steps completed" — formalize as v2.3 heuristic
- **Permission matrix standardization:** v2.2 is ad-hoc per wiki; v2.3 should define vault-wide matrix (reusable across all future wikis)
- **Trace grading automation:** v2.2 manual audit checklist; v2.3 should automate trace-log review (detect pattern violations, flag anomalies)
- **Autonomy-level automatic progression:** v2.2 requires human L2→L3 approval; v2.3 could auto-promote if evals consistently PASS (requires data-driven confidence threshold)

**Pattern influence:** agents-best-practices establishes operational-rigor discipline that v2.3 formalizes across future routine versions. First wiki-builds v71+ will collect data on (1) how often budgets hit limits, (2) which permission matrix entries trigger escalations, (3) which error-patterns repeat. Data informs v2.3 codification (Oct 2026 natural cadence).

---

## 12. Related corpus subjects

| Subject | Relation | Integration Method |
|---|---|---|
| v66 agentmemory | Sister operational service | Complementary skill: agents-best-practices (harness) + agentmemory (memory) = complete agent stack |
| v65 claude-code-system-prompts | Cross-vendor pattern docs | agents-best-practices synthesizes patterns from v65 + OpenAI docs + OWASP + NIST |
| v62 codex-plugin-cc | Cross-vendor tool integration | agents-best-practices risk taxonomy applies to connector validation (Category 9) |
| v64 claude-seo | Pattern #78 predecessor | agents-best-practices integrates Pattern #78 triple-vendor standards |
| v61 cc-sdd | Pattern #21 predecessor | agents-best-practices formalizes SDD methodology (7-invariant formalization) |
| routine-v2.2 | Vault routine | agents-best-practices provides governance discipline for v2.2 execution-layer design |

---

## 13. Next steps

**Immediate (Phase 6, vault-operator decision):**
- Decide: Deploy agents-best-practices skill via skills CLI or git clone into vault harness?
- Install skill + verify `skills list` shows agents-best-practices
- Define vault-wide permission matrix (role × action table for vault harness)
- Set budget caps: per-phase limits (50 steps, 50K tokens, $1.00) and per-wiki limits (200 steps, 200K tokens, $5.00)

**v71+ wiki-build practice (Phase 1-5):**
- Before each phase, check permission matrix + budget state
- Observe autonomy level (L0/L1/L2) at phase start; verify appropriate for task scope
- If approaching budget limits, pause and initiate compaction (preserve objective/plan/approval state)
- Log all tool calls to trace (enable post-wiki audit)

**Phase 6 (vault-state sync):**
- Generate Phase 6 draft mutations (see Entity-3 for checklist)
- Human reviews + approves via explicit gate (not automatic)
- Execute mutations with harness validation + trace logging
- Verify mutations: `git diff HEAD~1` confirms expected changes only

**v2.3 codification (v75-v80 natural cadence):**
- Collect data from v71+ wiki-builds: budget hit-rates, permission escalations, error-patterns, compaction frequency
- Formalize permission matrix standardization (vault-wide reusable template)
- Design sub-agent coordination protocol (agents-best-practices + agentmemory)
- Design trace-grading automation (replace manual checklist)
- Evaluate autonomy-level auto-promotion criteria (L2→L3 confidence threshold)

**Pilot candidacy (v71+):**
- agents-best-practices qualifies as **operational tool for vault** (criterion b PASS: direct applicability to hireui-harness Claude Code skill work)
- agents-best-practices qualifies as **methodology influence** (criterion d PASS via routine v2.2-v2.3: 7-invariant loop + autonomy levels inform future routine versions)
- Recommended pilot sequence: **codegraph FIRST (read-only, lower-risk, reversible via `codegraph uninit`) → agentmemory SECOND (persistent memory, higher-risk) → agents-best-practices THIRD (harness governance, depends on agentmemory success)**
- Pilot timeline: v71-v73 exploratory (no pilot), v74-v77 pilot-ready (codegraph + agentmemory candidate gates passed), v78+ full deployment window

---

## 14. Storm Bear deployment path (OPTIONAL section; metadata)

**Phase 0.9 classification: MODERATE 2/4 INCLUDE**

Criteria assessment:
- **(a) Eastern European developer demographic:** FAIL — agents-best-practices by DenisSergeevitch (Russian-speaking, likely Eastern European but not explicitly identified; no demographic match vs criterion expectation of Karpathy-adjacent archetype)
- **(b) Operational tool for Storm Bear vault:** PASS — Direct applicability to Claude Code skill governance for v2.2-v2.3 wiki-build harness
- **(c) Methodology influence on routine:** PASS — 7-invariant loop + autonomy levels → routine v2.2-v2.3 codification candidates (future methodology enrichment)
- **(d) Corpus-subject corpus-recursive relationship:** FAIL — No explicit corpus-subject URL in agents-best-practices (no vault/Storm Bear citations); Pattern Library discussion is generic, not recursive

**Verdict:** MODERATE 2/4 INCLUDE — criteria (b) + (c) PASS; criteria (a) + (d) FAIL. Qualifies as vault operational tool + methodology influence path without corpus recursion. Recommended: deploy as stable skill reference in v2.2-v2.3 routine; defer full pilot until v74+ (post-agentmemory pilot validation).

**Usage recommendation:**
- Install via skills CLI into Claude Code harness (v2.2 wiki-builds and future routine automation)
- Pin version to latest stable release (currently no official versioning; commit hash pinning recommended)
- Define vault-specific permission matrix + budgets (operators must customize per vault structure)
- Include in skill reference library (`_state/01-skill-references.md` post-Phase 6)

**Timeline:**
- v71 Phase 6: agents-best-practices skill installed + permission matrix defined + budget caps set
- v72+: Data collection on budget utilization, permission escalations, error-patterns
- v75-v80: v2.3 codification incorporating agents-best-practices discipline standardization

---

## 15. Key decisions & rationale

**Decision 1: Classify as T1 assistant skill, not T2 service or T4 bridge**

Rationale: agents-best-practices is markdown-only governance framework (no runtime binary, no service backend, no cross-system connector). Tier classification: T1 (foundational skill for harness design). Integration method: skill-as-context (load into system prompt or skills CLI).

**Decision 2: Recommend skills CLI deployment over git clone**

Rationale: skills CLI provides automatic discovery in Claude Code + Codex environments (lower friction). Git clone is fallback for offline use. Prompt-based integration adds ~35K token overhead (not recommended for long-running vault automation).

**Decision 3: Defer full pilot until v74+ (post-agentmemory)**

Rationale: agents-best-practices provides harness governance; agentmemory provides memory persistence. Deploying both together (v2.2 full-stack) is higher-risk than deploying either alone. Sequence: codegraph pilot (v71-v73, read-only) → agentmemory pilot (v74, memory layer) → agents-best-practices pilot (v75, harness governance). Sequential validation reduces compound risk.

**Decision 4: Vault-operator must customize permission matrix**

Rationale: agents-best-practices provides reference permission matrix; Storm Bear vault structure is unique (folder layout, role definitions, approval workflows). Operator must translate reference matrix to vault-specific config. Automation deferred to v2.3.

**Decision 5: Phase 6 requires explicit human approval gate (draft-commit pattern)**

Rationale: Phase 6 mutations (modifying CLAUDE.md, PATTERN_LIBRARY.md, `_state/` chapters) are irreversible and vault-critical. Two-phase separation (draft → review → commit) prevents accidental state corruption. Automation deferred to v2.3 (after 5+ wikis of data on approval frequency).

