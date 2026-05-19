# Entity 1: agents-best-practices Core Skill

**Type:** T1 Assistant Skill | **Tier:** Provider-neutral agentic framework | **Format:** Markdown-only

---

## 1. What is it?

agents-best-practices is a markdown-only Agent Skill synthesizing production agentic patterns from OpenAI, Anthropic, and compatible APIs. **Core philosophy:** "The model proposes; the harness validates, authorizes, executes, records, and returns observations."

---

## 2. Who uses it?

- **Agentic developers:** Building harnesses, designing tools, implementing safety discipline
- **Agent operators:** Running autonomous agents at various autonomy levels (L0-L4)
- **Skill authors:** Packaging reusable agent procedures
- **LLM wiki builders:** Implementing systematic knowledge synthesis (Storm Bear vault context)

---

## 3. Core function

agents-best-practices defines the operational contract between model (inference layer) and harness (execution layer). It formalizes:

- **Execution separation:** Model proposes; harness executes or rejects
- **Safety governance:** 7 invariants ensuring reliable operation
- **Risk stratification:** Tool categories map to approval paths + budgets
- **Observability discipline:** Every decision + tool call traced and evaluated

---

## 4. Architecture

```
8 Foundational Principles
  ↓
7 Invariants (Agentic Loop)
  ↓
Autonomy Levels (L0-L4)
  ↓
Tool Design Framework (Risk Taxonomy)
  ↓
Planning Mode (Complex Task Orchestration)
  ↓
Security Threat Model (15 Categories)
  ↓
Implementation Pathway (15 Sequential Steps)
```

---

## 5. Key concepts

### The 7 Invariants (Agentic Loop)
1. Each tool call gets exactly one result
2. Arguments validated before execution
3. Permission decisions precede side effects
4. Results bounded, structured, traceable
5. Hard budgets enforced (steps, time, tokens, cost, calls)
6. Final answers derive from observations, not assumptions
7. Errors become structured observations

### The 8 Foundational Principles
1. Operational rigor in harnesses
2. Explicit validation before execution
3. Risk-stratified permission paths
4. Separated drafting and commitment phases
5. Built rather than dumped context
6. Budget constraints
7. Progressive tool disclosure
8. Failure-driven feature development

### Autonomy Levels (L0-L4)
- **L0:** Answer-only (no tools)
- **L1:** Draft-only (proposals; no execution)
- **L2:** Approval-gated (simple ops autonomous; risky ops gated)
- **L3:** Policy-bounded (tools within policies; budgets enforced)
- **L4:** Long-running objectives (multi-day with minimal supervision)

### Tool Design Framework
**Risk taxonomy:** Read-only (allow) → Query (allow/approval) → Draft (allow) → Write (approval) → Delete (approval+confirmation) → Financial (multi-auth) → Destructive (draft-commit)

**Key principle:** Narrow over broad (one responsibility per tool).

### Draft-Commit Pattern
Separate proposal from execution for high-risk operations:
- `draft_email(to, subject, body)` → returns draft_id + preview
- `send_email(draft_id)` → approval required; executes actual send

---

## 6. Design philosophy

**Operational rigor:** The harness is the primary locus of safety, not the model. Validation, permission checks, and budgets PRECEDE execution (not post-hoc mitigation).

**Failure-driven development:** Every feature derives from observing actual agent failures. Don't pre-optimize for hypothetical risks.

**Transparency:** Errors surface as structured observations (model sees errors; can decide on recovery). No silent failures.

**Scoped responsibility:** Model is responsible for proposing good actions. Harness is responsible for authorizing + executing them correctly.

---

## 7. Configuration & setup

**Installation (3 paths):**

1. **Skills CLI:** `npm install -g skills && skills attach DenisSergeevitch/agents-best-practices`
2. **Git clone:** `git clone https://github.com/DenisSergeevitch/agents-best-practices.git`
3. **Prompt-based:** Include SKILL.md content in system prompt (token cost; limited portability)

**Reference library (15 files):**
Each reference serves a governance purpose. Load on-demand (agent reads files as needed).

**Context tuning:**
- **Minimum context window:** 20K tokens (SKILL.md + core references)
- **Recommended:** 50K+ (full 15-reference library available)
- **With prompt caching:** Cache tool defs + static instructions (~30K tokens); vary only task-specific context

---

## 8. Integration with other entities

- **Entity 2 (Distribution Ecosystem):** Describes deployment paths + MCP connector validation
- **Entity 3 (Pattern Library):** Analyzes Pattern #84 integration + NEW OC-O candidate
- **Entity 4 (Storm Bear):** Recommends operational integration into vault agentic harness

**Related corpus subjects:**
- **v66 agentmemory:** Agent memory system (operational sister-service; complements harness design with memory layer)
- **v65 claude-code-system-prompts:** Cross-vendor agentic patterns (Pattern #84 co-evidence; different format but overlapping scope)
- **v62 codex-plugin-cc:** Cross-vendor tool integration (Pattern #84 co-evidence; tool-tolerance implementation)
- **v64 claude-seo:** Pattern #78 predecessor (living-domain-standards starting point)
- **v63 andrej-karpathy-skills:** High-velocity skill precedent (reference for adoption speed)
- **v61 cc-sdd:** Pattern #21 predecessor (SDD methodology foundation)

---

## 9. Typical workflow

**Phase 1: Understanding (1-2 hours)**
1. Read SKILL.md (5 min) → understand 8 principles + 7 invariants
2. Read 8_principles.md (10 min) → detailed principle explanations
3. Read agentic_loop.md (10 min) → step-by-step loop walkthrough
4. Read autonomy_levels.md (15 min) → understand L0-L4 progression

**Phase 2: Design (2-4 hours)**
5. Classify your tools (risk taxonomy) → map tools to approval paths
6. Design permission matrix (role × action → approval_required)
7. Define budget limits (step limit, time limit, token limit, cost cap)
8. Read planning_mode.md (10 min) → understand when to plan

**Phase 3: Implementation (4-8 hours)**
9. Build harness (validation → permission check → execution → trace)
10. Test at L0/L1 autonomy (answer-only + draft-only modes)
11. Read security_threats.md (20 min) → identify your top 3 threats
12. Implement guardrails (input validation, context labeling, schema enforcement)
13. Test at L2/L3 autonomy (approval-gated + policy-bounded)
14. Read observability.md (10 min) → set up trace logging
15. Monitor + iterate (evaluate errors; add guardrails for patterns you see)

---

## 10. Tradeoffs

**Strengths:**
✓ Comprehensive safety framework (15 threat categories covered)
✓ Operational rigor (validation + permission + budgets all enforced)
✓ Provider-agnostic (Claude Code + Codex + OpenAI Agents compatible)
✓ Well-structured (7 invariants + 8 principles + 15 references provide clear mental model)
✓ Failure-driven (features derived from real failure patterns, not theoretical risks)

**Limitations:**
✗ Requires harness implementation (not a library; guides design, doesn't auto-execute)
✗ Token cost (full reference library = 48KB markdown; compaction required for long-running tasks)
✗ Autonomy levels require evaluation discipline (moving from L0→L1→L2→L3→L4 requires data + assessment)
✗ Learning curve (8 principles + 7 invariants + 15 references = ~6 hours to master)
✗ No code examples (markdown-only; developers must translate principles to their language/framework)

---

## 11. Pattern library impact

**Pattern #78 (Living-Domain-Standards) N=3 strengthening:**
Integrates MCP spec 2025-11-25 + OWASP AI Security Cheat Sheet + NIST AI RMF + Anthropic suite + OpenAI suite.

**Pattern #83 (Honest-Deficiency-Disclosure) within-pattern:**
Explicitly states "prompt-only safety is insufficient" as core deficiency disclosure (83b methodology).

**Pattern #21 (SDD Methodology Emergence) within-pattern:**
Formalizes 7-invariant loop + autonomy levels + planning mode as prescriptive agentic system design.

**Pattern #66 (Supply-Chain Isolation) within-pattern:**
"Malicious skill packages" as threat category (66d) + connector validation discipline.

**NEW candidate OC-O (Agentic-Harness-Execution-Separation):**
7-invariant loop formalizes model-proposes/harness-disposes separation as architectural governance principle.

**Corpus-firsts:**
1. First explicit model-proposes/harness-disposes execution-separation formalization
2. First 15-reference-file structured reference library within single skill
3. First explicit autonomy-level taxonomy (L0-L4) as safety framework
4. First provider-agnostic skill synthesizing BOTH OpenAI + Anthropic equally
5. First 15-category security threat model in agent skill context
6. First draft-commit pattern formalization as architectural principle
7. First OWASP + NIST + MCP-spec triple-standard integration
8. First 12-tier context architecture taxonomy

---

## 12. Related corpus subjects

| Subject | Relation | Key Difference |
|---------|----------|-----------------|
| v66 agentmemory | Sister service (T2 Service) | Memory system vs harness design; complementary |
| v65 claude-code-system-prompts | Pattern #84 co-evidence | Cross-vendor documentation vs unified framework |
| v62 codex-plugin-cc | Pattern #84 co-evidence | Tool-tolerance implementation vs harness design |
| v64 claude-seo | Pattern #78 predecessor | Pattern #78 starting point; v71 completes N=3 |
| v63 andrej-karpathy-skills | High-velocity precedent | Single artifact vs 15-reference library |
| v61 cc-sdd | Pattern #21 predecessor | SDD foundation vs 7-invariant formalization |
| agent-skills-of-vercel (older) | Similar archetype | Multi-vendor skills distribution; older era |
| claude-code-best-practice (older) | Format precedent | Best-practices format; v71 deeper methodology |

---

## 13. Next steps

**For beginners:** Start with SKILL.md + 8_principles.md. Understand the mental model before implementing.

**For harness builders:** Read autonomy_levels.md + tool_design.md. Map your tools to the risk taxonomy + approval paths.

**For operators:** Read planning_mode.md + security_threats.md. Determine your top 3 threats; implement guardrails for those.

**For corpus researchers:** Refer to Entity-3 (Pattern Library) for Pattern #84 N=3 analysis + OC-O candidacy assessment.

**For Storm Bear:** See Entity-4 (Storm Bear meta-entity) for vault integration recommendations + methodology influence analysis.

**Engagement decision:** Read open questions (30 items in 01 Analysis/) to identify knowledge gaps; prioritize based on deployment timeline.
