# (C) Agent Teams and Orchestration

> **Source:** README.md (line 70, 236-244), `docs/11-agent-teams.md` (skim — team model), CLAUDE.md (orchestration pattern #11)
> **Ingested:** 2026-04-18
> **Type:** Entity page (orchestration concept) — building block #4 cho goclaw

---

## One-liner

**VI:** Agent Teams and Orchestration là **multi-agent primitive của goclaw** — team có Lead + Members, shared Task Board + Mailbox, 3 orchestration modes (auto/explicit/manual), 3 delegation modes (sync/async/bidirectional), token-aware work distribution, `BatchQueue[T]` generic cho result aggregation. **First-class multi-agent architecture** — khác với 3 siblings (nơi multi-agent là one-off dispatch).

**EN:** Agent Teams and Orchestration is goclaw's multi-agent primitive — Lead + Members, shared Task Board + Mailbox, 3 orchestration modes, 3 delegation modes, token-aware work distribution. First-class multi-agent vs 3 siblings' one-off dispatch.

---

## Khi nào dùng concept này

**Hữu ích khi:**
- Hiểu cách goclaw coordinate multi-agent workflows
- Deploying team workflows (vd: "researcher + writer + reviewer" crew)
- Compare với gstack's `/pair-agent` + Superpowers's SDD dispatching
- Design your own multi-agent orchestration

**Overkill nếu:** single agent single task. Không cần team infrastructure cho simple Q&A bot.

---

## Comparison sibling

| Axis | ECC | Superpowers | gstack | **goclaw** |
|------|-----|-------------|--------|------------|
| Multi-agent paradigm | 48 specialized (call one-off) | SDD dynamic spawn | 23 specialists | **Structured team (Lead + Members)** |
| Task persistence | N/A | N/A | `/learn` skill session | **`subagent_tasks` PG table + `team_workspace`** |
| Task board | N/A | N/A | N/A | **Shared Kanban-style task board** |
| Inter-agent comm | Task tool ad-hoc | Status protocol (DONE/CONCERNS/BLOCKED) | `/pair-agent` browser share | **Mailbox (DMs + broadcasts)** |
| Delegation modes | 1 (sync) | 1 (dispatch) | 1 (spawn) | **3 (sync / async / bidirectional)** |
| Orchestration modes | 1 (manual) | 1 (SDD) | `/autoplan` smart | **3 (auto / explicit / manual)** |
| Result aggregation | Manual | `DONE` status | Manual | **`BatchQueue[T]` generic** |

→ **goclaw most structured.** Treats multi-agent as production architecture, not one-off.

---

## Sub-types: 3 orchestration modes

### Mode 1: Auto

- System decides work distribution
- Lead agent analyzes task, spawns members automatically
- Best for: well-known problem domains

### Mode 2: Explicit

- Lead agent explicitly delegates via tool calls
- Members claim tasks from board
- Best for: novel problems where coordination is critical

### Mode 3: Manual

- User explicitly directs which agent does what
- Full control, minimal automation
- Best for: high-stakes situations, debugging

---

## Sub-types: 3 delegation modes

### Mode A: Sync (wait)

- Lead delegates → blocks waiting for result
- Simple composition: result of A feeds B
- Token-aware: lead counts subtask tokens in own budget

### Mode B: Async (fire-and-forget)

- Lead delegates → continues without waiting
- Result arrives via event / mailbox / task board
- Use cases: parallel research, independent sub-tasks

### Mode C: Bidirectional

- Lead delegates, both parties can message
- Interactive workflow: member can ask clarifying questions
- Uses Mailbox for back-and-forth

---

## Anatomy: Team structure

```
┌────────────────────────────────────────────┐
│  Agent Team                                │
│                                            │
│  Lead Agent                                │
│  • Orchestrates work                       │
│  • Creates tasks on Task Board             │
│  • Delegates to members                    │
│  • Synthesizes member results              │
│                                            │
│  Member Agent A    Member Agent B    ...   │
│  • Claims tasks from board                 │
│  • Executes independently                  │
│  • Reports results back                    │
└────────────────────────────────────────────┘
           ↓
┌────────────────────────────────────────────┐
│  Shared Resources (PostgreSQL)             │
│                                            │
│  Task Board                                │
│  • Tasks: create/claim/complete            │
│  • Columns (Kanban-style)                  │
│  • Persistence: `subagent_tasks` table     │
│                                            │
│  Mailbox                                   │
│  • Direct messages between agents          │
│  • Broadcast to all team members           │
└────────────────────────────────────────────┘
```

### Team identity

Team = first-class entity:
- Has UUID (DB/FK/events)
- Has team_key (logs/paths/UI) — dual-identity pattern
- Has workspace directory
- Has RBAC scope (members + observers)

### Task anatomy (inferred)

```sql
CREATE TABLE subagent_tasks (
  id UUID PRIMARY KEY,
  team_id UUID NOT NULL,
  tenant_id UUID NOT NULL,
  lead_agent_id UUID NOT NULL,
  assigned_to_agent_id UUID NULL,
  status TEXT,  -- pending/claimed/in_progress/completed/failed
  description TEXT,
  result JSONB,
  created_at TIMESTAMPTZ,
  completed_at TIMESTAMPTZ
);
```

→ **Durable task board.** Persists across agent restarts.

---

## Cơ chế

### Mechanism 1: BatchQueue[T] generic

From CLAUDE.md key pattern #11:
> "Orchestration: Delegate tool for inter-agent task delegation with agent_links, 3 delegation modes (auto/explicit/manual), token-aware work distribution. BatchQueue[T] generic for result aggregation"

**Concept (inferred):**
```go
// Pseudo-code
type BatchQueue[T any] struct { ... }

func (q *BatchQueue[T]) Submit(task T) <-chan Result[T]
func (q *BatchQueue[T]) Collect() []Result[T]
```

Lead spawns N children, collects results via BatchQueue, aggregates.

→ **Type-safe multi-child orchestration.** Go 1.18+ generics leveraged.

### Mechanism 2: Scheduler lanes

`internal/scheduler/` has 4 lanes:
- **main** — primary agent execution
- **subagent** — child agents spawned from delegation
- **cron** — scheduled tasks
- **team** — team coordination tasks

Per-session serialization prevents races within a lane. Lanes run parallel.

→ **Bounded concurrency với per-domain fairness.**

### Mechanism 3: Per-edition rate limiting

`MaxSubagentConcurrent`, `MaxSubagentDepth`:
- Lite: lower (e.g., 2 concurrent, depth 2)
- Standard: higher (e.g., 10 concurrent, depth 5)

Tenant-scoped concurrency.

→ **Prevents runaway recursion.** Agent can't spawn infinite children.

### Mechanism 4: Subagent lifecycle

`internal/subagent/`:
- Spawn
- Roster (active children tracking)
- Task persistence (durable)
- Announce queue (producer-consumer for event fan-out)
- Auto-retry on failure

→ **Production-grade lifecycle management.**

### Mechanism 5: Token-aware work distribution

Lead knows token budget. Distributes to children proportionally.

→ **Cost awareness built-in.** Not retrofitted.

### Mechanism 6: Hook integration

Subagent lifecycle events:
- `SubagentStart`
- `SubagentStop`

Hooks can intercept for:
- Audit logging
- Cost tracking
- External notifications

---

## Out-of-box behavior

**Default configuration:**
- Teams disabled until user creates one (via admin dashboard or API)
- Default rate limits per edition
- Task board accessible via `team_tasks` tool
- Mailbox accessible via `message` tool

**To create a team:**
```http
POST /v1/teams
Authorization: Bearer <tenant-admin-token>
{
  "name": "ResearchCrew",
  "lead_agent_id": "uuid-of-lead",
  "members": ["uuid-of-researcher", "uuid-of-writer"]
}
```

**Agent tools for teams:**
- `team_tasks` — CRUD on task board
- `spawn` — spawn new subagent
- `delegate` — delegate task to member
- `message` — send to mailbox

---

## Configuration knobs

| Knob | Default | Effect |
|------|---------|--------|
| `teams.max_members` | unlimited (Standard) / 5 (Lite) | Team size cap |
| `MaxSubagentConcurrent` | per-edition | Parallel child ceiling |
| `MaxSubagentDepth` | per-edition | Recursion ceiling |
| `team.default_orchestration_mode` | `explicit` | Auto/explicit/manual |
| `mailbox.retention_days` | tbd | Message history cleanup |

---

## Recipes

### Recipe 1: Research crew pattern

Setup:
- Lead: "CrewLead" — orchestrator
- Member 1: "Researcher" — reads web, summarizes
- Member 2: "Writer" — drafts doc từ research
- Member 3: "Reviewer" — critiques draft

Flow:
1. User: "Write report on AI agent frameworks"
2. Lead creates tasks:
   - Task 1: "Research ECC/Superpowers/gstack/goclaw"
   - Task 2: "Draft initial report from research"
   - Task 3: "Review draft for accuracy"
3. Delegate (async for 1, sync for 2-3):
   - Researcher runs task 1 in background
   - Writer waits for 1, then runs 2
   - Reviewer waits for 2, then runs 3
4. Lead aggregates final report via `BatchQueue[T]`

### Recipe 2: Interactive bidirectional delegation

Lead → Member (bidirectional):
- Lead: "Research Karpathy's LLM Wiki pattern"
- Member: "I found 3 sources. Want priority: blog post, video, or paper?"
- Lead: "Blog post first, then paper"
- Member: returns research prioritized

### Recipe 3: Parallel async research

Lead spawns 5 researchers async:
```
Task 1: Research ECC
Task 2: Research Superpowers
Task 3: Research gstack
Task 4: Research goclaw
Task 5: Research OpenClaw
```

All run parallel. Lead collects via `BatchQueue[T]`.

### Recipe 4: Monitor team activity

Via admin dashboard:
- See active tasks
- See mailbox traffic
- Per-agent metrics (completion rate, error rate)

Or subscribe to `SubagentStart/Stop` hooks for external monitoring.

### Recipe 5: Debug team deadlock

If team stuck:
1. Check task board — any claimed but not completed?
2. Check mailbox — pending messages waiting for response?
3. Check scheduler lanes — team lane bottlenecked?
4. Check `MaxSubagentDepth` — hit recursion cap?

---

## Advanced patterns

### Pattern: Team as long-lived entity

Team persists beyond single request. Multiple sessions can use same team.

→ **Stateful orchestration.** Not ephemeral.

### Pattern: Task Board as shared state

Kanban-style task board = visible shared state. All members see board.

→ **Human-inspectable.** Admin dashboard shows board.

### Pattern: BatchQueue[T] for structured result collection

Generic type-safe aggregation. Avoids stringly-typed results.

→ **Go idiomatic** post-generics.

### Pattern: Agent links (permission edges)

"Delegate tool for inter-agent task delegation with agent_links" — links = explicit permission edges.

Without link: A can't delegate to B.
With link: A → B delegation allowed.

→ **RBAC for agent-to-agent.** Prevents unauthorized delegation.

### Pattern: Dual-identity extends to teams

Same pattern as agents: team_id (UUID, DB/FK) + team_key (UI/logs).

→ **Consistency across entity types.**

### Pattern: Cost safeguards in hooks

Hook system has "cost safeguards" category. Team spawning = cost event. Can inject caps.

→ **Financial control built-in.**

---

## Combination với building blocks khác

### + 8-Stage Agent Pipeline
Each agent (lead, member) runs its own 8-stage pipeline. Nested.

### + 3-Tier Memory + Knowledge Vault
Team has shared workspace memory + vault. Plus per-member private memory.

### + Multi-Tenant Architecture
Teams belong to tenant. Tenant isolation applies.

### + Channels
Channel messages can trigger team work. E.g., Telegram → team crew drafts response.

### + Skills Runtime
Team members can invoke skills. Skills shared or member-specific.

### Cross-project: + Superpowers SDD
Superpowers's SDD = dynamic dispatch, no persistent team. goclaw's teams = persistent crew.

**Use case split:**
- Superpowers: ephemeral multi-agent work (1 sprint, disband after)
- goclaw: long-lived crews (research team always on-call)

### Cross-project: + gstack Conductor parallel sprints
gstack runs 10-15 parallel sprints via Conductor (external). goclaw runs structured teams via built-in scheduler.

**Different parallelism models:**
- gstack: external isolation (separate Claude Code sessions)
- goclaw: internal lanes (shared server, scheduler-coordinated)

---

## Anti-patterns

❌ **Spawn subagents without depth limit** — infinite recursion. Respect `MaxSubagentDepth`.

❌ **Skip agent_links** — implicit trust. Explicit permission edges prevent unauthorized delegation.

❌ **Use async when sync needed** — order-dependent tasks with async = chaos. Sync for dependencies.

❌ **Ignore BatchQueue[T]** — manual aggregation = boilerplate + bugs. Use generic.

❌ **Treat team as ephemeral** — team is persistent entity. Create once, reuse.

❌ **Cross tenant in team** — team belongs to 1 tenant. Don't create cross-tenant teams (security violation).

❌ **Spawn beyond `MaxSubagentConcurrent`** — schedule serial if already at max. Don't force.

❌ **Forget hook cost safeguards** — unlimited team spawning = cost runaway. Configure caps.

---

## Cross-references

- [[(C) 8-Stage Agent Pipeline]] — per-agent execution
- [[(C) 3-Tier Memory + Knowledge Vault]] — shared team memory
- [[(C) Multi-Tenant Architecture]] — tenant boundary
- [[(C) README summary]] — team feature overview
- [[(C) CLAUDE.md + Architecture summary]] — orchestration pattern #11
- [[(C) Key Docs deep dive]] — team model detail
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) Subagent-Driven Development.md` — different orchestration model
- Cross-project: `../../gstack - Beginner Analysis/02 Wiki/(C) Specialist Roles.md` — role-based comparison

## Citations

- README.md line 70 (Agent Teams feature bullet)
- README.md lines 236-244 (Multi-Agent Orchestration section)
- CLAUDE.md key pattern #11 (Orchestration)
- CLAUDE.md `internal/subagent/` module description
- CLAUDE.md `internal/scheduler/` 4-lane description
- `docs/11-agent-teams.md` lines 1-50 (team model + mermaid diagram)

## TODO

- ⏸ Read full `docs/11-agent-teams.md` (717 lines) for complete task board API
- ⏸ Verify `subagent_tasks` schema in `migrations/`
- ⏸ Check `BatchQueue[T]` signature in `internal/orchestration/`
- ⏸ Test: create test team với 2 members, run recipe #1 — verify flow works
- ⏸ Compare with OpenAI Swarm / Google's multi-agent patterns
