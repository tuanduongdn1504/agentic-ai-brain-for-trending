# (C) Linear-Analog Task Management for Agents

> **Type:** Entity — core product + positioning
> **Parent:** [[(C) index]]
> **Sources:** [[(C) README + zh-CN summary]] §2; [[(C) CLAUDE + AGENTS + CONTRIBUTING cluster summary]] §2 (role definition)
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

multica's core product positioning (from CLAUDE.md) is **"similar to Linear but with agents as first-class citizens"** — applying Linear's issue-tracking UX paradigm to AI agent orchestration. The key abstraction is the **issue** (task) with an **atomic lifecycle** (enqueue → claim → start → complete/fail) and real-time WebSocket-driven progress updates. This is the **first Linear-analog in Storm Bear corpus** and represents a novel framing for T2 platform: take a proven human-team collaboration UX paradigm and substitute agents.

## 2. Key claims

1. **Linear-analog UX** — issues + boards + assignments + comments (Linear primitives) applied to agents
2. **Issue-as-task** — work units are issues, same as Linear
3. **Atomic lifecycle state machine** — enqueue → claim → start → complete/fail (explicit states)
4. **Real-time progress** via WebSocket
5. **Agent assignment** — tasks route to agents (not humans)
6. **Blocker reporting** — agents can signal human intervention needed
7. **Comments** — agents can discuss tasks (cross-agent + human)
8. **Board view** — kanban-style visualization
9. **Multi-workspace** — each workspace has its own issues + agents + settings
10. **First Linear-analog in corpus** — prior frameworks use different UX patterns

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| Linear-analog framing | CLAUDE.md role definition verbatim | High |
| Issue-based workflow | README Features | High |
| Atomic lifecycle states | README + CLAUDE.md | High |
| WebSocket real-time | CLAUDE.md architecture section | High |
| Multi-workspace isolation | README + CLAUDE.md | High |

## 4. How it works — task lifecycle

### State machine

```
┌─────────────┐
│  enqueue    │  ← User/heartbeat creates task
└──────┬──────┘
       ↓
┌─────────────┐
│   claim     │  ← Agent claims task (atomic)
└──────┬──────┘
       ↓
┌─────────────┐
│   start     │  ← Agent begins execution
└──────┬──────┘
       ↓
       ↓── progress updates via WebSocket ──→ UI
       ↓── blocker? → comment + request human ──
       ↓
┌─────────────┐         ┌──────────┐
│  complete   │   OR    │   fail   │
└─────────────┘         └──────────┘
```

**Atomic state transitions** — each state is a discrete event. No partial states.

**Parallel to paperclip v14 invariants:**
- paperclip: "atomic checkout semantics" (invariant 2)
- multica: atomic lifecycle (enqueue → claim → start → complete/fail)

Both enforce atomicity architecturally.

### Claim semantics

**Claim is single-assignee** (implied by atomic lifecycle — paperclip makes this explicit invariant #1). Only one agent owns a task at a time.

### Real-time progress

WebSocket pushes updates from Go backend to Next.js/Electron clients. Per CLAUDE.md: *"WS events invalidate queries — they never write to stores directly."*

This means:
- Agent produces progress update
- Go server receives via daemon
- Server broadcasts WebSocket event
- Client receives, invalidates TanStack Query cache
- Query refetches, UI updates

**Not:** "WebSocket pushes data to UI directly" (which is the lazier pattern; multica avoids).

## 5. Worked example — task lifecycle

**Scenario:** User assigns "Implement JWT authentication" task to Claude Code agent in multica workspace.

```
1. User creates issue
   ├─ Title: "Implement JWT authentication"
   ├─ Description: (full requirements)
   ├─ Workspace: "backend-team"
   ├─ Assign: claude-code-agent-1
   ├─ State: enqueue
   └─ Stored in PostgreSQL 17

2. Agent daemon (local) polls multica cloud
   ├─ Receives task via WebSocket
   └─ Agent claims task (atomic DB update)
       └─ State: claim

3. Agent starts Claude Code session
   ├─ Reads codebase (local file system)
   ├─ Implements changes
   ├─ State: start
   └─ WebSocket updates: "Reading auth.ts..."
                          "Writing jwt-middleware.ts..."
                          "Running tests..."
                          "PR drafted: #123"

4. Agent completes
   ├─ State: complete
   ├─ Final output stored (PR link, code diff, test results)
   └─ WebSocket notifies all subscribers

5. User reviews via dashboard
   └─ Approves or adds comment for follow-up
```

**Human role:** policy (assign, approve, comment). Execution = agent.

**Parallel to paperclip philosophy:** zero-human in operational loop, human-in-policy-loop.

## 6. Edges + failure modes

### Lifecycle edges
- **Orphaned claim** — agent crashes after claiming but before completing; task stuck. Mitigation: timeout-based reclaim.
- **Duplicate claim** — race condition if atomic semantics fail. Mitigation: DB-level locking (Postgres SELECT FOR UPDATE).
- **Partial fail** — agent completes 80%, fails 20%. Current state machine: binary complete/fail. No partial state. Potential limitation.

### WebSocket edges
- **Disconnection** — user's client drops WS. Mitigation: query refetch on reconnect.
- **Write conflicts** — multiple clients editing simultaneously. CLAUDE.md disallows writes from WS → prevents some conflicts.
- **Scalability** — many concurrent WebSockets = Go backend load. gorilla/websocket chosen for efficiency.

### Multi-workspace edges
- **Workspace leakage** — bug in company-scoping → cross-tenant data leak. paperclip makes this invariant; multica has workspace isolation but no explicit invariant language.
- **Workspace switching** — from CLAUDE.md: `setCurrentWorkspace(slug, uuid)` = singleton source of truth.

### Agent failure
- **Model unavailable** — Claude Code API down, agent can't execute. Mitigation: mark task fail, notify user.
- **Output quality** — agent produces bad code. No explicit quality gate (unlike paperclip's approval gates). **Lighter governance** per Multica vs Paperclip positioning.

## 7. Related concepts

- [[(C) Electron Desktop + Multi-Platform Architecture]] — dual-app cross-platform UX
- [[(C) skills-lock + Ecosystem Cross-Pollination]] — how skills extend agent capabilities
- [[(C) T2 2-way Validation + Pattern #9 Platform-Tier Refinement + Storm Bear]] — tier context

## 8. Cross-project comparison

### vs Linear (inspiration)

| Aspect | Linear (original) | multica (analog) |
|--------|--------------------|------------------|
| Users | Humans | Agents (+ human oversight) |
| Issues | Bug/feature tickets | Agent tasks |
| Assignment | To humans | To agents |
| Workflow | Manual state transitions | Atomic automated transitions |
| Comments | Team discussion | Agent status + human feedback |
| Board | Sprint planning | Agent workload visualization |

**multica = "Linear for agents"** — Clean analog.

### vs T2 peer (goclaw v4)

| Aspect | goclaw (v4) | multica (v15) |
|--------|-------------|---------------|
| Task abstraction | Multi-tenant agent platform | Linear-analog issues |
| UX paradigm | Custom | Linear-inspired |
| Real-time | Implicit | WebSocket explicit |
| Multi-tenancy | Multi-Tenant | Multi-workspace |
| Atomic lifecycle | Implicit | Explicit states |

→ multica has **more opinionated UX** (Linear paradigm) vs goclaw's generic platform framing.

### vs T5 paperclip (explicit competitor)

| Aspect | paperclip (v14) | multica (v15) |
|--------|-----------------|---------------|
| Abstraction | Company + Org Chart | Workspace + Issues (Linear) |
| Governance | Heavy (5 invariants + 4 primitives) | Lightweight |
| Target user | Solo operator (multi-user roadmap) | Teams (multi-user native) |
| Deployment | Self-hosted primary | Cloud-first + self-hosted |
| UX complexity | Custom company-chart | Familiar Linear-style |

→ multica is **lighter + more team-collaboration-focused**. paperclip heavier + more autonomous-oriented.

### vs T1 frameworks (different tier but worth noting)

- BMAD workflows — structured methodology; multica issues are more fluid
- codymaster cm-sprint-bus — sprint coordination skill; multica has sprint via issues/boards natively
- GSD agents — context rot spec; multica doesn't explicitly address

## 9. Open questions

- Issue sub-types supported? (bug/feature/task distinction?) (new — Q36)
- Custom issue fields? (Linear-style) (new — Q37)
- Agent-to-agent delegation? (Can agent A create issue for agent B?) (new — Q38)
- Slack/Discord integration for notifications? (Q16 partial)
- Retry logic on agent failure? (new — Q39)

## 10. Decision log

- **Initial (v0.1-0.2):** atomic lifecycle established
- **v0.2.6 current:** Linear-analog UX stable
- **Future:** "compound skills" may evolve into skill marketplace (parallel to BMAD v6.3 community module browser)

## 11. Storm Bear relevance

### Linear familiarity

VN dev teams frequently use Linear or similar (Jira, ClickUp). Linear-analog UX = low onboarding friction for Scrum teams.

### Scrum ceremony fit

Issues + boards + assignments = Scrum primitives. multica's atomic lifecycle could map to:
- **enqueue** = backlog grooming
- **claim** = sprint commitment
- **start** = sprint execution
- **complete** = sprint review

BUT: multica assigns to AGENTS not humans. Tension for Scrum coaching which focuses on human team dynamics.

### Storm Bear engagement options

1. **Personal productivity** — use multica for Storm Bear own backlog with agents as helpers (not for client teams)
2. **Reference study** — how does Linear paradigm translate to agents? Useful mental model for any agent-orchestration pilot
3. **Hybrid team pilot** — ONE team experiments with multica for agent-augmented workflow (humans + agents both assigned issues)

### NOT recommended
- Full Scrum team replacement (framing tension)
- Client coaching engagements as primary tool (philosophical mismatch)

## 12. Migration / adoption notes

- **From Linear:** conceptual overlap = easy mental model transfer
- **From Jira:** heavier governance → multica is lighter
- **From paperclip:** more collaborative + less autonomous-focused
- **Fresh adoption:** Homebrew install → `multica login` → create workspace → assign tasks

## 13. References

- README §What is Multica? + §Features
- CLAUDE.md §Role Definition (Linear analog)
- Parent: [[(C) index]]
- Cross-wiki T2: `../../goclaw - Beginner Analysis/02 Wiki/(C) 8-Stage Pipeline.md`
- Cross-wiki T5 (competitor): `../../paperclip - Beginner Analysis/02 Wiki/(C) Zero-Human Companies Orchestration + Governance Layer.md`
