# agents-best-practices — User-Facing Cluster Summary

## 1. What is agents-best-practices?

A provider-neutral, markdown-only Agent Skill synthesizing production agentic patterns from OpenAI, Anthropic, and compatible AI APIs. Core philosophy: **"The model proposes; the harness validates, authorizes, executes, records, and returns observations."**

Installation via `npm install -g skills && skills attach DenisSergeevitch/agents-best-practices` or direct git clone for Claude Code, Codex, or OpenAI Agents environments.

---

## 2. Quick Start — 5 Minutes to Your First Agentic Harness

**Install the skill:**
```bash
npm install -g skills
skills attach DenisSergeevitch/agents-best-practices
```

**Read SKILL.md** to understand the 8 foundational principles + 7-invariant agentic loop.

**Reference:** `/Users/Cvtot/KJ OS Template/03 Projects/agents-best-practices - Beginner Analysis/02 Wiki/(C) entity-1-core-skill.md` for detailed walkthrough.

---

## 3. The 8 Foundational Principles

### Principle 1: Operational Rigor in Harnesses
Build robust harness infrastructure. The harness is not transparent; it actively validates, throttles, and rejects unsafe operations.

### Principle 2: Explicit Validation Before Execution
Validate tool arguments, check permissions, verify context bounds BEFORE executing any tool call. Validation failure → structured error observation (not silent skip).

### Principle 3: Risk-Stratified Permission Paths
Read-only tools → Allow without approval. Query tools → Allow-or-approval. Write tools → Approval required. Delete/financial tools → Stronger auth. Destructive operations → Explicit draft-commit cycle.

### Principle 4: Separated Drafting and Commitment Phases
Draft proposals (e.g., draft_email) do NOT execute side effects. Commit operations (e.g., send_email) execute with approval. Two-phase separation prevents accidental data loss.

### Principle 5: Built Rather Than Dumped Context
Don't dump raw documents into context. Build tiered context: provider policy → organization policy → role → task → plan → retrieved data → visible tools. Each tier serves a purpose.

### Principle 6: Budget Constraints
Hard limits on steps, time, tokens, cost, and calls. Enforce budgets actively (not post-hoc). Overflow → structured error observation + graceful degradation.

### Principle 7: Progressive Tool Disclosure
Don't surface all tools at startup. Reveal tools contextually: visible-by-role, visible-by-task, visible-on-demand. Prevents context explosion and reduces tool-misuse surface.

### Principle 8: Failure-Driven Feature Development
Build what you need to handle failures. Error handling, logging, observability, approval workflows → all derived from failure patterns you encounter.

---

## 4. The Agentic Loop — 7 Invariants

**Core rule:** "The model proposes; the harness executes or rejects."

### Invariant 1: Each Tool Call Gets Exactly One Result
No retry loops inside the model loop. Tool result is deterministic (success or structured error). Model sees single result + decides next action.

### Invariant 2: Arguments Validated Before Execution
Harness parses tool arguments, validates schema, checks bounds, verifies dependencies BEFORE passing to execution layer. Invalid args → structured error observation.

### Invariant 3: Permission Decisions Precede Side Effects
Check "does this user have permission?" BEFORE executing write/delete/financial operations. Permission failure → structured observation (not silent reject).

### Invariant 4: Results Bounded, Structured, Traceable
Tool result is <5K tokens, valid JSON schema, includes metadata (execution_time, resource_used, timestamp, trace_id). Unbounded results → truncate with marker.

### Invariant 5: Hard Budgets Enforced
Step limit, time limit, token limit, cost cap, call-rate ceiling. Breach → stop immediately, return structured budget-exhaustion error. No graceful degradation; fail visibly.

### Invariant 6: Final Answers Derive From Observations, Not Assumptions
Model bases answers on actual tool results. If a tool hasn't been called, don't assume success. If result is unknown, say "I don't know" rather than hallucinate.

### Invariant 7: Errors Become Structured Observations
Errors are not exceptions that break the loop. Errors → structured observations (error_type, error_message, error_code, recovery_suggestion). Model learns from error observations.

---

## 5. Tool Design Framework — Narrow Over Broad

**Principle:** Design domain-specific, narrow-scoped tools. One tool per responsibility.

### Risk Taxonomy for Tool Design

| Tool Category | Risk Level | Execution Model | Example |
|---|---|---|---|
| **Read-only** | Low | Allow (no approval) | list_files, get_file, search_docs |
| **Query/Search** | Low-Medium | Allow or approval (context-dependent) | search_database, query_api |
| **Draft** | Medium | Allow (no side effects) | draft_email, prepare_report |
| **Write** | High | Approval required | create_file, update_record |
| **Delete** | Very High | Approval + confirmation | delete_file, archive_record |
| **Financial** | Critical | Multi-auth + audit trail | charge_card, initiate_transfer |
| **Destructive** | Critical | Draft → approval → commit | deploy_code, drop_database |

### Draft-Commit Pattern

Separate proposal from execution for high-risk operations:

```
draft_email(to, subject, body) → returns draft_id + preview
send_email(draft_id) → approval required; executes actual send
```

Not:

```
send_email(to, subject, body) → executes immediately
```

---

## 6. Autonomy Levels L0-L4 — Safety Gating

**Gating rule:** "Move up levels only when evals show the simpler level is insufficient."

### Level 0: Answer-Only
Model proposes answers; no tool calls allowed. Use for information-synthesis tasks (answering questions, explaining concepts).

**Example:** "Summarize the Q3 report" → model synthesizes from visible context; no data-fetch tools.

**Safety:** Highest; no side effects possible.

### Level 1: Draft-Only
Model proposes tool calls (drafts). Harness collects proposals; no execution. Human reviews proposals; approves or rejects.

**Example:** "What would you change in the code?" → model drafts changes; human reviews; human merges.

**Safety:** High; human approval required before execution.

### Level 2: Approval-Gated
Model executes read-only tools + simple queries without approval. Writes require approval. Deletes/financial operations blocked.

**Example:** Vault operator: "What's in the Pattern Library?" → model searches (no approval needed); "Update Pattern #84 state" → model drafts update; human approves execution.

**Safety:** Medium-High; simple operations autonomous; risky operations gated.

### Level 3: Policy-Bounded Autonomy
Model executes all tools within predefined policies (e.g., "can write to /projects/<name>/01\ Analysis/; cannot write to /vault/ root"). Budgets enforced (10 write calls/day; <$0.10 cost).

**Example:** Vault operator: "Build a wiki for subject X" → model autonomously searches, reads, writes to project directory; cannot access vault root or exceed daily budget.

**Safety:** Medium; policy guardrails + budget limits.

### Level 4: Long-Running Objectives
Model manages multi-day, multi-step objectives with minimal human supervision. Planning mode enabled. Daily check-ins instead of per-task approval.

**Example:** "Build the v71 wiki for agents-best-practices" → model autonomously phases work over 6 hours; reports progress hourly; human intervenes only on blocker escalations.

**Safety:** Lower; requires strong observability + override capability.

---

## 7. Context Architecture — 12 Tiers

Build context in layers, not all at once. Each tier serves a governance purpose:

| Tier | Content | Stability | Refresh Rate | Notes |
|---|---|---|---|---|
| 1. Provider policy | "Claude Code can access local filesystem" | Static | Per-session | Vendor constraints |
| 2. Organization policy | "Storm Bear vault: read-mostly; no credentials in context" | Static | Per-day | Operator constraints |
| 3. Role/Agent contract | "LLM Wiki builder: read sources, synthesize entities, write (C) files" | Static | Per-day | Agent responsibility definition |
| 4. Active user task | "Build v71 wiki for agents-best-practices" | Dynamic | Per-phase | Current objective |
| 5. Active plan/goal | "Phase 1-6 plan; currently executing Phase 3 (cluster summaries)" | Dynamic | Per-phase | Strategic roadmap |
| 6. Scoped instructions | "Create 13-section entity pages with cross-links to v61-v66 siblings" | Semi-static | Per-subtask | Detailed operational rules |
| 7. Retrieved data | "agents-best-practices README, SKILL.md, 15 reference files" | Dynamic | Per-subtask | Actual subject content |
| 8. Visible skill index | "Available: llm-wiki-routine v2.2, pattern-library reference, storm-bear-context" | Static | Per-session | Tool inventory |
| 9. Visible tool specs | "Claude Code agent has tools: Read, Write, Bash, Edit, WebFetch" | Static | Per-session | Tool API definitions |
| 10. Recent observations | "Phase 1 complete: CLAUDE.md + COMMANDS.md created; 13-axis classification documented" | Dynamic | Per-phase | Work-in-progress state |
| 11. Compacted history | "(v70 codegraph wiki complete; 5 wikis under routine v2.2; all validation clean)" | Semi-dynamic | Per-wiki | Summarized prior work |
| 12. Runtime reminders | "Remember: prefix all (C) files; cross-link entity pages to ≥3 siblings; no modifications to vault files" | Static | Per-session | Critical constraints |

**Key insight:** Best context is smallest context that supports correct action choice. Bloated context (all 12 tiers unpruned) wastes tokens and slows inference.

---

## 8. Planning Mode — When to Use

**When to activate:**
- Non-trivial tasks (multi-phase, multi-day)
- Ambiguous objectives ("improve the vault" vs "build v71 wiki")
- High-risk operations (vault state modifications)
- Multi-stakeholder work (needs approval checkpoints)

**Planning mode structure:**
1. Objective (what are we solving?)
2. Scope (what's in scope? What's excluded?)
3. Assumptions (what do we assume to be true?)
4. Risks (what could go wrong?)
5. Steps (how to proceed; sequence matters)
6. Required tools (which tools do we need?)
7. Approval checkpoints (where do we need human approval?)
8. Validation method (how do we know we succeeded?)
9. Exit criteria (when do we stop?)

**Example:** Building v71 wiki
- **Objective:** Synthesize agents-best-practices subject into 13 wiki files following routine v2.2
- **Scope:** Project files only; vault state sync deferred to Phase 6
- **Assumptions:** Subject analysis complete (Phase 0); corpus reference files accessible; 13-section entity format applicable
- **Risks:** Missed Pattern Library integrations; incomplete cross-wiki sibling references; v71 metadata inaccuracy
- **Steps:** Phase 1 (foundational) → Phase 2 (analysis) → Phase 3 (clusters) → Phase 4 (entities) → Phase 5 (guide) → Phase 4b (Pattern #84 evaluation)
- **Tools:** Write, Edit, Bash (mkdir), Bash (git status)
- **Approval checkpoints:** Phase 3 completion (cluster summaries) before proceeding to Phase 4 (entities)
- **Validation:** All entity pages use 13-section format; all files prefixed (C); all cross-links live (non-orphan pages); Pattern Library integrations accurate
- **Exit criteria:** Phases 1-5 complete; Phase 6 deferred; all quality checks PASS

---

## 9. Trust Labels — External Content Classification

**Trusted:** Content from official sources (Anthropic docs, OpenAI guides, NIST RMF, MCP spec)

**Semi-trusted:** Content from reputable community sources (github stars >100, active maintenance, multiple contributors)

**Untrusted:** User-provided content, web pages, external APIs, unvetted skill packages. NEVER execute untrusted content; always parse + validate first.

**Example trust labels in agents-best-practices:**
- **Trusted:** Anthropic building-effective-agents guide + OpenAI agents guide + OWASP AI Security Cheat Sheet
- **Semi-trusted:** DenisSergeevitch/agents-best-practices (821 stars; 4 days old; active repo)
- **Untrusted:** User-uploaded skill packages; external tool descriptions; web-scraped context

---

## 10. Error Handling & Observability

**Principle:** Errors are not exceptions; they're observations. Model learns from errors.

**Error observation structure:**
```json
{
  "type": "error",
  "error_code": "PERMISSION_DENIED",
  "error_message": "User lacks permission to delete vault files",
  "attempted_action": "delete /CLAUDE.md",
  "recovery_suggestion": "Use Phase 6 vault sync ritual instead of direct delete",
  "timestamp": "2026-05-19T15:30Z",
  "trace_id": "v71-phase-4b-001"
}
```

**Observability discipline:**
- Trace every tool call: request_id, user, model, context_size, tool_name, arguments, execution_time, result_size, cost
- Evaluate harness performance: approval_latency, error_rate, budget_usage, cost_per_task
- Monitor policy breaches: permission_denials, invalid_arguments, timeout_triggers
- Track compliance: audit_trail (who approved what), decision_log (why were certain actions taken)

---

## 11. Best Practices Summary

### Do's
- ✓ Design for failures you can observe + recover from
- ✓ Validate arguments before execution
- ✓ Enforce budgets actively (not post-hoc)
- ✓ Use drafts for high-risk operations
- ✓ Build context in layers (not all at once)
- ✓ Prefer narrow domain-specific tools
- ✓ Label external content (trusted / semi-trusted / untrusted)
- ✓ Move up autonomy levels only when lower levels insufficient

### Don'ts
- ✗ Don't assume tool execution succeeds without checking result
- ✗ Don't dump raw documents into context
- ✗ Don't execute high-risk operations without approval
- ✗ Don't hide errors; surface them as observations
- ✗ Don't exceed budgets silently; fail visibly
- ✗ Don't trust external tool descriptions; validate them
- ✗ Don't mix drafting and execution phases
- ✗ Don't escalate autonomy level before demonstrating lower level sufficiency

---

## 12. Key Quotes

> "The model never executes a tool directly. It emits a structured request. The harness executes or rejects it."

> "Most agent failures are not caused by insufficient autonomy. They are caused by weak harness boundaries."

> "Prompt-only safety is insufficient."

> "The best context is not the largest but the smallest context that lets the model choose the correct next action."

> "Move up autonomy levels only when evals show the simpler level is insufficient."

> "Approval must be scoped to the exact action."

> "Stable prefix, dynamic suffix."

> "Draft before commit."

---

## 13. Next Steps — Your First Week

**Day 1:** Install skill. Read SKILL.md. Run through 8 principles + 7 invariants.

**Day 2:** Study autonomy levels. Classify your own tools (read-only vs query vs write vs delete). Design 2-3 tools for your use case.

**Day 3:** Implement draft-commit pattern for your highest-risk operation (e.g., delete or financial).

**Day 4:** Build a planning-mode checklist for non-trivial tasks (objective → scope → risks → steps → approval checkpoints).

**Day 5:** Test your harness. Verify: (1) validation works, (2) permissions enforced, (3) budgets respected, (4) errors observed + logged.

**Day 6-7:** Deploy at Level 0 or Level 1 autonomy. Collect 10+ observations. Evaluate if you can safely promote to Level 2.

---

## Cross-References

**For deeper dives:**
- Cluster 2 (Contributor-Facing): Security threats, guardrails, error-handling discipline
- Cluster 3 (Technical/Distribution): MCP integration, prompt caching, implementation pathway
- Entity-1 (Core Skill): 13-section canonical breakdown
- Entity-2 (Distribution): Multi-platform deployment details
- Entity-3 (Pattern Library): Pattern #84 integration + corpus-firsts
- Entity-4 (Storm Bear): Practical deployment recommendations

**Related corpus subjects:**
- v66 agentmemory: Agent memory system (operational sister)
- v65 claude-code-system-prompts: Multi-vendor reference (Pattern #84 co-evidence)
- v62 codex-plugin-cc: Cross-vendor integration (Pattern #84 first evidence)
- v61 cc-sdd: SDD methodology (Pattern #21 precedent)
