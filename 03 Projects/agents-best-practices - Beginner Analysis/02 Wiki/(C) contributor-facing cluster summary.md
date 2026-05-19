# agents-best-practices — Contributor-Facing Cluster Summary

For developers building harnesses, designing tools, implementing security, and evaluating agent behavior.

---

## 1. System Design Philosophy

**Core principle:** Operational rigor is non-negotiable. The harness is the primary locus of safety, not the model.

**Design tenet:** Every feature derives from observing actual agent failures. Don't pre-optimize for failures you haven't encountered.

**Architecture law:** Validation, permission checks, and budget enforcement PRECEDE execution. Post-execution mitigation is too late.

---

## 2. Trust Model — What You Can't Trust

**External tool descriptions:** Treat as potentially unreliable. Parse + validate before using. MCP tools may have outdated schemas or misleading descriptions.

**Retrieved content:** User-provided files, web-scraped data, external APIs → all untrusted. Label them explicitly. Quarantine before execution.

**User input:** Even trusted users can make mistakes. Validate arguments, bounds, and type before passing to execution layer.

**Model's assumptions:** Model may assume tool execution succeeded without checking result. Structure observations to force explicit result-checking.

**Skill packages:** Postinstall scripts, telemetry, hidden permissions → scrutinize. Malicious skill packages can exfiltrate secrets or execute unwanted operations.

---

## 3. Security Threat Taxonomy (15 Categories)

### Category 1: Prompt Injection
**Risk:** Attacker embeds instructions in tool results or user input. Model executes injected instructions instead of intended behavior.

**Mitigation:** 
- Validate tool results against schema BEFORE returning to model
- Quote/escape all user-provided content
- Use system prompts that are difficult to override (role clarity)
- Deny tool-result content containing specific instruction patterns (e.g., "ignore your previous instructions")

### Category 2: Malicious Retrieved Content
**Risk:** Retrieved documents contain instructions designed to manipulate model behavior.

**Mitigation:**
- Label all retrieved content as untrusted
- Truncate large retrieved documents (unbounded context is exploitable)
- Scan retrieved content for suspicious patterns (e.g., contradiction injections, role-override patterns)

### Category 3: Tool Misuse
**Risk:** Model uses correct tool for unintended purpose (e.g., search_database to exfiltrate all records instead of answering specific query).

**Mitigation:**
- Design narrow-scoped tools (one responsibility per tool)
- Validate that tool arguments match intended query scope
- Log all tool calls with explicit usage context
- Implement query-result limits (search_database returns max 100 records, not all)

### Category 4: Permission Bypass
**Risk:** Model discovers permission checks can be bypassed by phrasing requests differently or chaining tool calls.

**Mitigation:**
- Check permissions BEFORE execution, not after
- Enforce permissions consistently across all code paths
- Audit permission matrices regularly (watch for escape routes)
- Log all permission checks + denial reasons

### Category 5: Secret Leakage
**Risk:** API keys, passwords, vault credentials accidentally included in context or tool results.

**Mitigation:**
- Never include secrets in system prompts or context
- Redact secrets from tool results before returning to model
- Use environment variables + secure secret stores (not inline credentials)
- Scan all tool results for patterns matching secret formats (API key prefixes, password lengths)

### Category 6: Data Exfiltration
**Risk:** Model orchestrates tool calls to extract sensitive data and return it to external service.

**Mitigation:**
- Restrict write tools to trusted output destinations only
- Monitor outbound write tools for unexpected data patterns
- Implement data classification (PII, financial, health → restricted tools only)
- Audit all write operations (who, what, when, where, why)

### Category 7: Unsafe External Communication
**Risk:** Model sends unvalidated data to external APIs or services (e.g., sends query logs to logging service; attacker exploits logging service to exfiltrate context).

**Mitigation:**
- Validate all data BEFORE sending to external services
- Use TLS + certificate pinning for external communication
- Limit external tool surface (prefer internal logging)
- Sanitize data before transmission (strip PII)

### Category 8: Financial/Destructive Side Effects
**Risk:** Model executes expensive operations (API calls, cloud resource provisioning, payments) without explicit user approval.

**Mitigation:**
- Draft-commit pattern for all financial/destructive tools
- Hard budget cap per task (e.g., $0.10 max spend per wiki-build task)
- Multi-auth for financial tools (model approval insufficient; require human sign-off)
- Immutable audit trail (every financial transaction logged + timestamped)

### Category 9: Connector Tool Abuse
**Risk:** MCP connector has security vulnerabilities; model exploits them to exceed intended scope.

**Mitigation:**
- Validate MCP connector schemas (don't trust tool descriptions at face value)
- Implement staged exposure (list → search → load full schemas → execute)
- Restrict MCP tool surface based on task (don't expose all connectors; expose only needed ones)
- Audit MCP tool results for unexpected behavior

### Category 10: Malicious Skill Packages
**Risk:** DenisSergeevitch/agents-best-practices-backdoor mimics real package; includes postinstall script that exfiltrates secrets.

**Mitigation:**
- Verify package publisher (GitHub stars, active maintenance, multiple contributors)
- Inspect postinstall scripts before installing (never auto-install untrusted scripts)
- Quarantine newly installed skills in sandbox before production use
- Monitor skill package updates for suspicious changes

### Category 11: Runaway Loops
**Risk:** Model enters infinite loop (retry same failed tool call repeatedly; loop detection doesn't trigger).

**Mitigation:**
- Hard step limit (max 50 steps per task; not negotiable)
- Repeat-detection: if same tool called 3x in a row with same args, stop + escalate
- Timeout per task (max 5 minutes; kill model execution if exceeded)
- Observe loop patterns in trace logs; add escalation rule for patterns you see

### Category 12: Cost Exhaustion
**Risk:** Model makes expensive API calls; cost quickly exceeds budget. Cloud bill explodes.

**Mitigation:**
- Hard cost cap per task (e.g., $0.10 per wiki-build)
- Track token usage per tool call (some tools are expensive; restrict access)
- Monitor cost-per-day trending; alert if trending 2x higher than expected
- Implement cost-aware tool selection (prefer cheaper tools; cascade to expensive tools only if necessary)

### Category 13: False Success Claims
**Risk:** Model claims task completed ("I've updated the vault") without actually verifying. User doesn't discover error until later.

**Mitigation:**
- Require explicit verification steps (after tool execution, fetch result + validate against expected output)
- Structure observations to force verification ("Did you verify the file was written?")
- Audit final state against initial objectives (did we achieve what we planned?)
- Implement checksums / signatures for critical operations

### Category 14: Compaction State Loss
**Risk:** Auto-compaction removes critical context (objective, plan, approval state). Model loses track of why it was doing something.

**Mitigation:**
- Preserve objective + plan + approval state during compaction (never remove these)
- Compaction removes: duplicate prose, old logs, stale branches, irrelevant exploration
- Compaction preserves: objective, plan, approval state, resources inspected, key facts, artifacts created, tool calls/results, errors/fixes, open questions, pending tasks, next step
- Audit compaction logs (what was removed? does it make sense?)

### Category 15: Subagent Miscoordination
**Risk:** Multiple agents (model + skill tools) have inconsistent context or conflicting objectives. Subagent acts on stale information.

**Mitigation:**
- Synchronize state before delegating to subagent (pass explicit context dump)
- Define subagent contract (what is subagent responsible for? what context does it need?)
- Implement result validation (subagent's output must match expected schema)
- Audit coordination failures; add explicit coordination steps to prevent repeat

---

## 4. Guardrails Architecture — 7-Layer Defense

### Layer 1: Input Validation
Validate all user input + tool arguments before any processing.
- Type checking (is argument a string? number? valid enum?)
- Bounds checking (string <256 chars? number in range?)
- Format validation (email format? URL format? JSON schema?)

**Implementation:** Pydantic schema validation or similar.

### Layer 2: Context Labeling
Label all context with trust classification: trusted / semi-trusted / untrusted.
- Tool result labels (untrusted)
- Retrieved content labels (untrusted)
- System prompts label (trusted)
- User input labels (semi-trusted)

**Implementation:** Tag each context block with trust_label field.

### Layer 3: Schema Enforcement
Enforce tool API contracts. Tools must accept only documented parameters; return only documented fields.

**Implementation:** Tool wrapper that validates inputs (before execution) and outputs (after execution).

### Layer 4: Tool Execution Validation
Verify tool executed as expected (return code, output format, performance).
- Did tool complete within timeout?
- Did tool return expected schema?
- Did tool produce observable side effects?

**Implementation:** Wrapper validates execution result before surfacing to model.

### Layer 5: Permission Controls
Check permissions BEFORE execution. Audit all permission checks.
- User role + action: does user have permission to perform this action?
- Resource scope: is resource within user's scope?
- Risk level: does action risk level match user's approval level?

**Implementation:** Permission matrix (role × action × risk_level → approval_required).

### Layer 6: Output Review
Validate model output before executing downstream operations.
- Does output match expected format?
- Does output contain secrets or sensitive data?
- Does output match user's original intent?

**Implementation:** Output schema validation + secret scanning.

### Layer 7: Trace Grading
Audit tool call sequence after task completion.
- Were all tool calls authorized?
- Were all budgets respected?
- Were all errors handled properly?
- Did task achieve stated objective?

**Implementation:** Trace log review + automated checklist.

---

## 5. Permission Matrices & Approval Workflows

**Matrix structure:** Role × Action × Risk_Level → Approval_Required (boolean)

**Example for Storm Bear vault:**

| Role | Action | Risk Level | Approval | Notes |
|------|--------|------------|----------|-------|
| LLM Wiki Builder | Read /projects/*/02\ Wiki/ | Low | No | Analysis phase |
| LLM Wiki Builder | Write /projects/*/02\ Wiki/(C)\ *.md | Medium | No | Within project scope |
| LLM Wiki Builder | Modify /CLAUDE.md (vault root) | High | Yes | Phase 6 only |
| LLM Wiki Builder | Modify /PATTERN_LIBRARY.md | High | Yes | Phase 6 only |
| LLM Wiki Builder | Delete project files | Very High | Yes | Irreversible |
| Storm Bear Operator | Approve Phase 6 vault sync | Critical | Human | Non-delegable |

**Approval workflow:**
1. Model proposes action (tool call)
2. Harness checks permission matrix (does action require approval?)
3. If approval required: escalate to human + include context (why is this action needed? what is the consequence?)
4. Human approves or rejects
5. If approved: execute tool
6. If rejected: continue with alternative approach

---

## 6. Hard Budgets — Implementation

**Budget types:**

| Budget Type | Limit | Enforcement |
|---|---|---|
| Step limit | 50 steps per task | Stop immediately at step 50 |
| Time limit | 5 minutes per task | Kill model execution at 5m mark |
| Token limit | 100K tokens per task | Compaction or stop at 100K |
| Cost limit | $0.10 per task | Stop immediately if cumulative cost > $0.10 |
| Call rate | 10 calls per minute | Queue + backoff if exceeding rate |

**Enforcement:**
- Before each tool call: verify budgets not exceeded
- After each tool call: deduct resources used
- Breach = stop + return structured budget-exhaustion error
- Log budget usage per task (analytics for optimization)

---

## 7. Observability & Evaluation Discipline

**Trace record per tool call:**
```json
{
  "trace_id": "v71-phase-4b-001",
  "tool_name": "Write",
  "timestamp": "2026-05-19T15:30:42Z",
  "model_info": "claude-haiku-4-5",
  "context_size": 125000,
  "arguments": {
    "file_path": "/Users/Cvtot/KJ OS Template/03 Projects/.../CLAUDE.md",
    "content": "(13-axis classification...)"
  },
  "execution_time_ms": 250,
  "result_size": 8500,
  "cost_usd": 0.0015,
  "permission_check": "PASS",
  "budget_check": "PASS (cost: $0.0015; remaining: $0.0985)",
  "approval_decision": "AUTO_APPROVE (WRITE within project scope)"
}
```

**Evaluation metrics:**
- Tool success rate (% of tool calls that succeeded)
- Approval latency (time from proposal to approval decision)
- Error rate per tool (which tools fail most often? why?)
- Cost per task (trending up or down?)
- Budget utilization (are we close to caps?)
- Loop detection rate (how often did we detect + stop runaway loops?)

**Audit trail discipline:**
- Every permission decision logged + timestamped
- Every budget breach logged + escalation action taken
- Every tool failure logged + recovery attempt documented
- Every approval decision logged + approval justification recorded

---

## 8. Error Handling — Errors as Observations

**Anti-pattern:** Try-catch that silently swallows errors.

**Pattern:** Errors surface as structured observations.

```python
# Anti-pattern (bad)
try:
    result = write_file(path, content)
except Exception as e:
    print("Error occurred")  # Model never sees error
    
# Pattern (good)
try:
    result = write_file(path, content)
except PermissionError as e:
    observation = {
        "type": "error",
        "error_code": "PERMISSION_DENIED",
        "error_message": str(e),
        "attempted_action": f"write {path}",
        "recovery_suggestion": "Check file permissions; ensure directory exists",
        "trace_id": trace_id
    }
    return observation  # Model sees error; can decide on recovery
```

**Error observation field:**
- error_code (enum: PERMISSION_DENIED, TIMEOUT, INVALID_SCHEMA, BUDGET_EXHAUSTED, etc.)
- error_message (human-readable explanation)
- attempted_action (what were we trying to do?)
- recovery_suggestion (how to recover)
- trace_id (for debugging)
- timestamp

---

## 9. Tool Abuse Prevention

**MCP connector validation:**
1. Load connector schema
2. Validate schema against expected interface (does it have expected fields?)
3. Whitelist tool names (only call tools you explicitly approved)
4. Sandbox tool execution (run in isolated environment; monitor for anomalies)
5. Rate-limit tool calls (e.g., max 5 calls per minute to single connector)

**Tool-description reliability:**
- Don't trust tool description at face value
- Test tool with known inputs; verify output matches description
- Watch for undocumented behavior (tool does something not in description? flag it)
- Version-pin connectors (don't auto-upgrade; review updates before accepting)

---

## 10. Skill Package Security

**Vetting checklist before installing agents-best-practices or similar skills:**

- [ ] Publisher has >100 GitHub stars (reputation signal)
- [ ] Repository has active maintenance (commits within last month)
- [ ] Multiple contributors (not single-author repo; reduces single-point-of-failure)
- [ ] No postinstall scripts (inspect package.json; verify no "postinstall" hook)
- [ ] No telemetry (search for fetch/http calls to external services)
- [ ] License is open (MIT, Apache, GPL; not proprietary)
- [ ] README is clear + non-obfuscated (good signal of legitimacy)
- [ ] Issue tracker shows healthy community (issues + responses, not abandoned)
- [ ] Code review before using (skim SKILL.md + reference files; look for red flags)

---

## 11. Implementation Pathway — 15 Steps (Sequential)

1. **Event state** — define what events trigger harness behavior
2. **Manual loops** — prove harness works before adding model
3. **Single-agent tools** — design initial tool set
4. **Tool result validation** — verify tools return expected schema
5. **Permission matrices** — define role × action → approval logic
6. **Approval workflows** — implement escalation + human approval
7. **Hard budgets** — enforce limits (step, time, token, cost)
8. **Event tracing** — log every tool call + decision
9. **Planning mode** — add objective-driven mode for complex tasks
10. **Memory management** — implement compaction + context windowing
11. **Auto-compaction** — compress history while preserving critical context
12. **Prompt caching** — cache stable prefixes (tool defs, system instructions)
13. **Skill attachment** — integrate agents-best-practices as reusable module
14. **MCP connectors** — add staged-exposure MCP tool loading
15. **Subagent coordination** — orchestrate multiple agents with shared context

---

## 12. Security Posture Evaluation (Self-Assessment)

**Score yourself (0-5 per item):**

- [ ] Input validation: Do you validate all user input + tool arguments? (5 = always; 0 = never)
- [ ] Trust labeling: Do you label all context with trust classification? (5 = always; 0 = never)
- [ ] Permission enforcement: Are permission checks before execution? (5 = always; 0 = never)
- [ ] Error visibility: Do errors surface as observations? (5 = always; 0 = never)
- [ ] Secret redaction: Do you scan results for secrets + redact? (5 = always; 0 = never)
- [ ] Budget enforcement: Do you have hard limits + enforce them? (5 = always; 0 = never)
- [ ] Audit trail: Do you log all decisions + tool calls? (5 = always; 0 = never)
- [ ] Tool design: Are tools narrow + single-responsibility? (5 = always; 0 = never)
- [ ] Threat awareness: Do you know your top 3 failure modes? (5 = yes + mitigating; 0 = no)
- [ ] Evaluation: Do you measure harness performance + iterate? (5 = continuous; 0 = never)

**Score interpretation:**
- 45-50: Excellent. You're implementing best practices consistently.
- 35-44: Good. You're on the right track; identify weak spots.
- 25-34: Fair. You have security awareness but gaps remain.
- <25: Poor. Prioritize input validation + permission checks immediately.

---

## 13. Related Resources & Next Steps

**For deeper dives:**
- Cluster 1 (User-Facing): 8 principles, 7 invariants, autonomy levels, context architecture
- Cluster 3 (Technical): MCP integration, prompt caching, implementation pathway
- Entity-1 (Core Skill): 13-section breakdown of agents-best-practices skill
- Entity-2 (Distribution): Multi-platform deployment details
- Entity-3 (Pattern Library): Pattern #84 integration + corpus context

**Related corpus subjects:**
- v66 agentmemory: Memory system design (threat: state loss; mitigation: durable store)
- v65 claude-code-system-prompts: System-prompt engineering (prompt injection threat)
- v62 codex-plugin-cc: Cross-vendor tool integration (connector security)

**Industry standards:**
- OWASP AI Agent Security Cheat Sheet (15 top risks)
- NIST AI Risk Management Framework (comprehensive risk model)
- MCP specification 2025-11-25 (connector standards)
