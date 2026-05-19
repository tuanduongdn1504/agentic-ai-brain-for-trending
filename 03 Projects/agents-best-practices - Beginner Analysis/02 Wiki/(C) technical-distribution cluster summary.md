# agents-best-practices — Technical & Distribution Cluster Summary

For developers building, deploying, and integrating agents-best-practices across platforms.

---

## 1. Distribution Model

agents-best-practices is a skill package (not a source-code library). Three deployment paths:

### Path 1: Skills CLI (Recommended)
```bash
npm install -g skills
skills attach DenisSergeevitch/agents-best-practices
```

**Outcome:** Skill auto-discovered in Claude Code / Codex skill registry. References available for prompt context injection.

**Advantage:** Unified package management (npm registry); auto-discovery; version pinning.

**Drawback:** Requires Node.js 18+; npm infrastructure dependency.

### Path 2: Git Clone
```bash
git clone https://github.com/DenisSergeevitch/agents-best-practices.git
cp -r agents-best-practices/SKILL.md ~/.codex-skills/
cp -r agents-best-practices/references/ ~/.codex-skills/references/
```

**Outcome:** Skill + references locally available; agent can reference via file:// paths.

**Advantage:** No npm dependency; offline-capable; manual version control.

**Drawback:** Manual synchronization; discovery burden on developer.

### Path 3: Prompt-Based Installation
Include SKILL.md content directly in system prompt. Agent learns skill from prompt text.

**Outcome:** No installation needed; skill available immediately.

**Advantage:** Maximum portability; works across any agent platform.

**Drawback:** Token cost (entire skill in every request); less discoverable to agent; compaction challenges.

---

## 2. npm Installation & Dependencies

**package.json dependencies:**
```json
{
  "skills": "^1.2.0",
  "commander": "^11.0.0"
}
```

**Requirements:**
- Node.js 18+ (LTS)
- npm 9+ (for workspaces support)
- Git (for git clone fallback)

**Installation time:** ~30 seconds (skills CLI download) + ~5 seconds (package install).

**Disk footprint:** ~5 MB (SKILL.md + 15 reference files; markdown-only, no compiled code).

---

## 3. Multi-Platform Support

agents-best-practices targets 3 AI agent platforms. Compatibility notes:

### Claude Code (Anthropic)
**Status:** Tier 1 support (primary target)

**Features:**
- Skills CLI native integration
- File read/write tools available
- MCP connector support
- Prompt caching compatible

**Deployment:** `skills attach DenisSergeevitch/agents-best-practices` in Claude Code terminal.

### Codex (OpenAI)
**Status:** Tier 1 support (primary target)

**Features:**
- Skills CLI native integration
- Function-calling tools available
- No native MCP (use via HTTP bridge)

**Deployment:** `skills attach` in Codex terminal; auto-discover in function-calling prompt.

### OpenAI Agents
**Status:** Tier 2 support (secondary target)

**Features:**
- Prompt-based installation only (no native skills CLI)
- Tool use via function definitions
- No native MCP (define custom tools for MCP bridge)

**Deployment:** Copy SKILL.md + 15 references into agent system prompt manually.

**Compatibility matrix:**

| Feature | Claude Code | Codex | OpenAI Agents |
|---------|---|---|---|
| **Skills CLI** | ✓ | ✓ | ✗ |
| **File tools** | ✓ | ✓ | ✓ (custom) |
| **MCP native** | ✓ | ✗ | ✗ |
| **Prompt caching** | ✓ | ✓ | ✓ |
| **Token budget** | Minimal (discovery) | Minimal | Full (in-prompt) |
| **Setup friction** | Low | Low | Medium |

---

## 4. 15-Reference File Architecture

agents-best-practices = SKILL.md + 15 reference files. Each reference serves a governance purpose:

| File | Purpose | Size | Read-When |
|---|---|---|---|
| **agentic_loop.md** | 7-invariant loop formalization + step-by-step walkthrough | ~3KB | Understanding execution model |
| **8_principles.md** | 8 foundational principles detailed + examples | ~4KB | Design philosophy |
| **autonomy_levels.md** | L0-L4 progression + gating criteria + evaluation | ~3KB | Planning autonomy for task |
| **context_architecture.md** | 12-tier context model + tier ordering + refresh rates | ~4KB | Building context stack |
| **tool_design.md** | Risk taxonomy + narrow-over-broad principle + examples | ~3KB | Designing new tools |
| **planning_mode.md** | When to plan + plan structure + approval checkpoints | ~3KB | Complex task design |
| **security_threats.md** | 15-category threat model + mitigation per threat | ~5KB | Risk assessment |
| **implementation_pathway.md** | 15-step sequential build path + milestones | ~3KB | Project planning |
| **draft_commit_pattern.md** | Two-phase separation + examples + anti-patterns | ~2KB | High-risk operation design |
| **error_handling.md** | Error as observation + error structures + recovery | ~3KB | Debugging + recovery design |
| **observability.md** | Trace records + metrics + audit trail | ~3KB | Monitoring discipline |
| **prompt_caching.md** | Stable prefix strategy + cache boundaries + examples | ~3KB | Token optimization |
| **mcp_integration.md** | Staged exposure + validation + rate limiting | ~3KB | Connector architecture |
| **skills_connectors.md** | Skill structure + YAML frontmatter + progressive disclosure | ~2KB | Packaging new skills |
| **guardrails.md** | 7-layer defense + implementation + self-assessment | ~4KB | Security hardening |

**Total:** ~48KB markdown (scales efficiently with Claude Code + Codex context windows).

**Discovery pattern:** Agent has access to all 15 files; reads relevant files on-demand (reference lookup, not auto-loaded).

---

## 5. MCP Integration — Staged Exposure

agents-best-practices recommends 4-stage MCP tool loading pattern:

### Stage 1: List Available Tools
Harness lists MCP tool names only (no schemas).

```
Available tools:
- list_files
- read_file
- search_docs
- create_record
- approve_action
```

**Cost:** <100 tokens

### Stage 2: Search Tools
Agent can search tool index by name/category.

```
search(category="write") → [create_record, update_record, delete_record]
```

**Cost:** <200 tokens

### Stage 3: Load Full Schemas
Agent explicitly requests full schema for tools it wants to use.

```
load_schema("read_file") → {
  "name": "read_file",
  "description": "Read content from file...",
  "parameters": {...},
  "examples": [...]
}
```

**Cost:** <500 tokens per tool

### Stage 4: Execute Tools
Agent makes tool calls with full schema understanding.

```
read_file(path="/path/to/file") → result
```

**Cost:** Per-execution cost (tool-dependent)

**Benefit:** Context explosion prevented (full tool catalog not in initial context). Agents load tools contextually (only when needed).

---

## 6. Prompt-Caching Strategy

**Philosophy:** "Stable prefix, dynamic suffix."

### Stable Prefix (Cached)
These elements rarely change; cache them:

1. **Tool definitions** (read_file, write_file, search_docs, etc.)
2. **Static instructions** (8 principles, 7 invariants, autonomy levels, trust labels)
3. **Governance policies** (permission matrix, budget limits, approval workflows)
4. **Reference architectures** (context tiers, tool taxonomy, threat model)

**Token cost:** ~20-30K tokens (one-time cache write; amortized across many requests)

### Dynamic Suffix (Not Cached)
These elements change per request; don't cache:

1. **Active task** (current objective)
2. **Active plan** (current phase/step)
3. **Tool observations** (results from recent tool calls)
4. **Model history** (recent reasoning/decisions)
5. **Budget state** (remaining token budget, remaining cost budget)

**Token cost:** ~5-10K tokens per request (full cost; no cache savings)

### Cache Implementation

**Boundary:** Cache everything up to "Here is your current task..." line.

```
<system-prompt>
  <tool-definitions>...</tool-definitions>  ← CACHE
  <principles>...</principles>              ← CACHE
  <threat-model>...</threat-model>          ← CACHE
</system-prompt>

Here is your current task: ...             ← NOT CACHED
Task observations: ...                      ← NOT CACHED
Remaining budget: ...                       ← NOT CACHED
```

**Cache hit scenario:** 5 wiki-build tasks in sequence
- Task 1: full cost (~30K stable + 10K dynamic = 40K)
- Task 2-5: cache-hit cost (~10K dynamic only = 10K × 4)
- **Total savings:** 120K - (40K + 10K×4) = 40K tokens (25% reduction)

---

## 7. Reference Architecture — Multi-Component Integration

agents-best-practices skill + companion components:

```
Agent (Claude Code / Codex)
  ↓
Skill Loader (skills CLI or git-clone)
  ├─ SKILL.md (skill definition)
  └─ References/ (15 reference files)
  ↓
Harness (permission matrix, budgets, validation)
  ├─ Input validator (schema + bounds checking)
  ├─ Permission checker (role × action matrix)
  ├─ Tool executor (wrapped tool calls)
  ├─ Budget tracker (step, time, token, cost)
  └─ Trace logger (observable audit trail)
  ↓
Tool Layer
  ├─ Read tools (file read, search, query)
  ├─ Draft tools (draft_email, prepare_action)
  ├─ Write tools (create, update)
  └─ MCP connectors (staged-exposure tool loading)
  ↓
Storage + Execution
  ├─ Filesystem (local files)
  ├─ Databases (records, memory)
  └─ External APIs (via HTTP bridge)
```

**Data flow:** Agent proposes → Harness validates → Tool executes → Result returned to agent as observation.

---

## 8. MCP Connector Validation

**Before using MCP connector, validate 5 dimensions:**

### 1. Schema Validation
- Load connector schema
- Verify schema matches expected interface (does it have tool_name, description, parameters?)
- Check for unexpected fields (red flag: undocumented parameters)

### 2. Whitelist Validation
- Define which tools from connector you want to expose
- Example: Don't expose delete_file if not needed for task
- Load only whitelisted tools into context

### 3. Sandbox Validation
- Run connector in isolated environment
- Test with known inputs; verify outputs match description
- Watch for anomalies (tool behavior differs from description? unexpected side effects?)

### 4. Rate-Limit Validation
- Set per-connector call limit (e.g., max 5 calls/min to MCP_FILE_CONNECTOR)
- Prevent runaway loops from exhausting connector quota

### 5. Version Validation
- Pin connector version (don't auto-upgrade)
- Review changelog before updating
- Test new version in staging before production deployment

---

## 9. Implementation Pathway — 15 Steps

**Build harness + integrate agents-best-practices in this order:**

1. **Event state** — Define events that trigger harness (user_input, tool_result, timer_tick, error)
2. **Manual loops** — Hardcode harness behavior before adding model; verify works
3. **Single-agent tools** — Design 3-5 initial tools (read_file, write_file, search)
4. **Tool result validation** — Wrap tools; validate results match schema
5. **Permission matrices** — Define role × action → approval logic
6. **Approval workflows** — Implement escalation (tool call → harness checks permission → escalate if needed)
7. **Hard budgets** — Add step limit (50 max), time limit (5 min max), cost tracking
8. **Event tracing** — Log every decision + tool call + result
9. **Planning mode** — Add objective-aware mode (plan before execution for complex tasks)
10. **Memory management** — Implement task-context window (keep last 20 tool calls in context; older calls → compacted summary)
11. **Auto-compaction** — Compress history while preserving objective + plan + approval state
12. **Prompt caching** — Cache tool defs + static instructions; vary only task-specific context
13. **Skill attachment** — Load agents-best-practices as reference (15 files available on-demand)
14. **MCP connectors** — Add staged-exposure MCP tool loading (list → search → load → execute)
15. **Subagent coordination** — If delegating to other agents, synchronize context + define subagent contract

**Validation per step:**
- Step 1-3: Manual test (run harness without model; verify event handling + tool execution works)
- Step 4-8: Harness-only test (add model but restrict to L0/L1 autonomy; verify validation + permission logic)
- Step 9-12: Full-feature test (enable planning mode + compaction + caching; verify correctness + efficiency)
- Step 13-15: Integration test (attach skill references; enable MCP connectors; test multi-platform deployment)

---

## 10. Skills & Connectors — Packaging New Skills

**Skill package structure:**

```
agents-best-practices/
├── SKILL.md              (skill definition + YAML frontmatter)
├── README.md             (usage guide)
└── references/
    ├── agentic_loop.md
    ├── 8_principles.md
    ├── ... (13 more reference files)
    └── guardrails.md
```

**SKILL.md YAML frontmatter:**

```yaml
---
name: agents-best-practices
version: 1.0.0
author: DenisSergeevitch
description: |
  Provider-neutral agentic harness design skill.
  Synthesizes Anthropic + OpenAI + OWASP + NIST patterns.
dependencies:
  - Claude Code (recommended)
  - Codex (compatible)
  - OpenAI Agents (compatible with prompt-based install)
targets:
  - agentic_harness_design
  - safety_governance
  - tool_design
  - planning_discipline
minimum_context: 20000  (minimum context window to use this skill effectively)
cost_per_use: ~5000 tokens  (typical token cost when skill referenced in single request)
---
```

**Progressive disclosure in SKILL.md:**

- **On skill discovery:** Name + description only (2-3 lines)
- **On skill selection:** Core instructions + 8 principles + 7 invariants (2-3KB)
- **On-demand reference:** Full 15-file library available (agent loads files as needed)

**Benefit:** Agent can adopt skill incrementally (start with principles; deepen to threat model + MCP integration as needed).

---

## 11. Context Compaction Discipline

**Compaction goal:** Reduce context size while preserving agent decision-making capability.

**Preserves (never remove):**
- Objective (why are we doing this?)
- Plan (what are the phases/steps?)
- Approval state (which decisions have been approved?)
- Resources inspected (which files have we read?)
- Key facts (what did we learn?)
- Artifacts created (which new files did we create?)
- Tool calls/results (recent 10-20 tool calls + results)
- Errors/fixes (what went wrong? how did we fix it?)
- Open questions (what don't we know?)
- Pending tasks (what's left to do?)
- Next step (what's the immediate next action?)

**Removes (safe to discard):**
- Duplicate prose (same concept explained multiple ways)
- Old logs (tool calls from >30 minutes ago)
- Stale branches (decisions we didn't pursue)
- Irrelevant exploration (tools we tried but didn't use)
- Intermediate results (tool-call chains where only final result matters)

**Compaction example:**

```
# Before compaction (15KB)
Agent: "I'll read the README file to understand project structure"
Tool: read_file(path="/project/README.md")
Result: "# Project Name... [full 5KB README content]"
Agent: "I found the project structure. Now I'll read SKILL.md..."
Tool: read_file(path="/project/SKILL.md")
Result: "[full 8KB SKILL.md content]"
Agent: "SKILL.md shows 8 principles and 7 invariants..."

# After compaction (3KB)
[COMPACTED HISTORY]
Phase 1: Read README + SKILL.md
Key findings:
- Project structure: 8 principles + 7-invariant agentic loop
- Corpus position: v71 T1 Agent Skill
- Pattern integrations: Pattern #84, Pattern #78, NEW OC-O candidate
Status: README + SKILL.md analyzed; moving to Phase 2 (analyze 15 references)
Next: Load autonomy_levels.md + context_architecture.md references
```

**Compaction trigger:** After every phase completion OR context >80K tokens.

---

## 12. Observability & Monitoring

**Trace record template:**

```json
{
  "trace_id": "v71-wiki-build-001",
  "phase": "Phase 3 (cluster summaries)",
  "timestamp": "2026-05-19T13:00:00Z",
  "model": "claude-haiku-4-5",
  "context_size": 95000,
  "tool_call": {
    "name": "Write",
    "arguments": {
      "file_path": "/Users/Cvtot/KJ OS Template/03 Projects/.../user-facing-cluster.md",
      "content_size": 18000
    },
    "execution_time_ms": 320,
    "result": "success"
  },
  "permissions": {
    "checked": true,
    "approval_required": false,
    "decision": "auto_approve"
  },
  "budgets": {
    "steps_used": 15,
    "steps_remaining": 35,
    "tokens_used": 95000,
    "tokens_remaining": 5000,
    "cost_usd": 0.0045,
    "cost_remaining": 0.0955
  }
}
```

**Metrics dashboard:**

| Metric | Target | Current | Trend |
|--------|--------|---------|-------|
| Tool success rate | >95% | 98% | ↑ (improving) |
| Approval latency | <10s | 3.5s | ↓ (good) |
| Budget utilization | <80% | 72% | → (stable) |
| Error rate | <5% | 2% | ↓ (improving) |
| Loop detection | >0% of overruns caught | 100% | → (stable) |
| Cost per task | <$0.10 | $0.0045 | ↓ (under budget) |

---

## 13. Multi-Platform Deployment Strategy

### Deploy to Claude Code (Primary)
```bash
npm install -g skills
skills attach DenisSergeevitch/agents-best-practices
# Now available in Claude Code: skill activates automatically
```

### Deploy to Codex (Primary)
```bash
git clone https://github.com/DenisSergeevitch/agents-best-practices.git
# Copy SKILL.md + references to Codex skill registry
cp agents-best-practices/SKILL.md ~/.codex/skills/
# Use in function-calling prompt
```

### Deploy to OpenAI Agents (Secondary)
```
# Copy SKILL.md content into system prompt manually
# Reference 15 files as separate context blocks
# No native skills CLI; prompt-based integration only
```

### Deploy Offline (All platforms)
```bash
git clone https://github.com/DenisSergeevitch/agents-best-practices.git
# Use local file:// references for SKILL.md + references
# Works without npm + without internet
```

---

## 14. Prompt-Caching at Scale

**Scenario:** Build 5 wikis in sequence (v71-v75).

**Without caching:**
- v71 wiki: 30K stable + 10K dynamic = 40K tokens
- v72 wiki: 30K stable + 10K dynamic = 40K tokens
- v73 wiki: 30K stable + 10K dynamic = 40K tokens
- v74 wiki: 30K stable + 10K dynamic = 40K tokens
- v75 wiki: 30K stable + 10K dynamic = 40K tokens
- **Total:** 200K tokens

**With caching:**
- v71 wiki: 30K stable (cache write) + 10K dynamic = 40K tokens
- v72 wiki: 0K cached + 10K dynamic = 10K tokens (cache hit!)
- v73 wiki: 0K cached + 10K dynamic = 10K tokens (cache hit!)
- v74 wiki: 0K cached + 10K dynamic = 10K tokens (cache hit!)
- v75 wiki: 0K cached + 10K dynamic = 10K tokens (cache hit!)
- **Total:** 80K tokens (60% savings!)

**Implementation:** Use Anthropic SDK prompt caching (cache_control="ephemeral" on stable sections).

---

## 15. Advanced Integration — Subagent Coordination

**Scenario:** LLM Wiki builder (agent 1) delegates to pattern-analysis specialist (agent 2).

**Coordination contract:**

```
Agent 1 → Agent 2:
{
  "task": "Evaluate Pattern #84 promotion criteria",
  "context": {
    "pattern_name": "Cross-Vendor Ecosystem-Tolerance",
    "current_status": "CANDIDATE at N=2",
    "new_evidence": [v62_codex_plugin, v65_claude_code_system_prompts, v71_agents_best_practices],
    "evaluation_framework": "5 promotion criteria: cross-corpus, sub-variants, consistent mechanism, corpus integration, actionability"
  },
  "constraints": {
    "max_steps": 20,
    "max_time_ms": 300000,
    "max_tokens": 50000
  },
  "expected_output": {
    "verdict": "PROMOTE | DEFER | REJECT",
    "reasoning": "...",
    "sub_typology_registration": "84c Provider-Agnostic-By-Design (if applicable)"
  }
}

Agent 2 → Agent 1:
{
  "verdict": "PROMOTE",
  "reasoning": "N=3 with 2 distinct archetypes meets criterion 1 + 2; consistent mechanism (reduce friction) meets criterion 3; corpus integration + actionability meet criteria 4+5",
  "sub_typology_registration": "84c Provider-Agnostic-By-Design",
  "confidence": 0.92,
  "evidence_summary": {...}
}
```

**Validation:** Agent 1 verifies Agent 2's output matches expected_output schema before integrating result.

---

## Related Resources

**For deeper dives:**
- Cluster 1 (User-Facing): Installation, 8 principles, autonomy levels, context architecture
- Cluster 2 (Contributor-Facing): Security threats, guardrails, observability, permission matrices
- Entity-2 (Distribution Ecosystem): Multi-platform deployment specifics
- Entity-3 (Pattern Library): Corpus integration + ecosystem standards

**Industry standards:**
- MCP specification 2025-11-25 (connector standards)
- Anthropic SDK documentation (prompt caching APIs)
- OpenAI agents guide (function-calling specifications)
