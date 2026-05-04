# (C) Zero-Human Companies Orchestration + Governance Layer

> **Type:** Entity — core architecture + philosophical positioning
> **Parent:** [[(C) index]]
> **Sources:** [[(C) README summary]] §1, §2, §5; [[(C) AGENTS + ROADMAP + adapter-plugin cluster summary]] §2 (5 invariants); ROADMAP MAXIMIZER MODE
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

paperclip's defining abstraction is **"the company"** as orchestration primitive — an autonomous agent collective with mission, org chart, tickets, budgets, and governance gates. Agents are employees; paperclip is the company. The **4 governance primitives** (approval gates + manual override + budget hard-stops + audit log) and **5 control-plane invariants** (single-assignee / atomic checkout / approval gates / budget hard-stops / activity logging) form the architectural response to the paperclip-maximizer alignment problem. Paperclip's thesis: higher autonomy is safe if governance layer is architecturally inviolable.

## 2. Key claims

1. **"Company" is the orchestration primitive** — not agent, not workflow, but company
2. **Zero-human-in-operational-loop** (not zero-human-in-governance)
3. **9 named features** form the company abstraction: Org Chart + Goal Alignment + Ticket System + Heartbeats + Cost Control + Multi-Company + BYO Agent + Governance + Mobile Ready
4. **5 control-plane invariants** (from AGENTS.md) are architectural constants
5. **Paperclip-maximizer name** is deliberate — architecture is response to Bostrom's 2003 thought experiment
6. **MAXIMIZER MODE roadmap item** — higher autonomy within governance bounds
7. **Corpus-first explicit alignment-theory framing** — no prior 13 wikis had this

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| "Zero-human companies" | README tagline | High |
| OpenClaw/employee/paperclip/company metaphor | README verbatim | High |
| 9 named features | README Features section | High |
| 5 invariants | AGENTS.md §Control-Plane Invariants | High |
| 4 governance primitives | README Governance + FAQ | High |
| MAXIMIZER MODE | ROADMAP Active Development | High |
| Alignment-theory reference | Paperclip-maximizer is textbook Bostrom | High (factual) |

## 4. How it works — "the company" abstraction

### Company as primitive

```
Company (top-level entity)
  ├─ Mission/Goal (Goal Alignment — tasks trace to mission)
  ├─ Org Chart (hierarchical roles with reporting lines)
  ├─ Budget (Cost Control — hard-stop limits)
  ├─ Approval Gates (Governance — human-in-loop checkpoints)
  ├─ Audit Log (immutable activity record)
  └─ Agent Roster (OpenClaw / Claude Code / Codex / Cursor / Bash / HTTP)
```

### Task flow

1. **Ticket** created (user-generated or Heartbeat-scheduled)
2. **Assignment** via org chart (routed to appropriate role)
3. **Single-assignee** locked (invariant #1)
4. **Atomic checkout** — agent claims task, executes, releases (invariant #2)
5. **Approval gate** triggered at defined checkpoints (invariant #3)
6. **Budget check** continuous (invariant #4 — hard-stop on overrun)
7. **Activity log** every action (invariant #5)
8. **Outcome** delivered or "Stricter outcome enforcement" rejects status-only updates (ROADMAP)
9. **Cost tracked** against budget

### Multi-company

Every domain entity enforces company boundaries at route and service layers (AGENTS.md §Company Scoping). Complete data isolation between tenants. Single installation can host N companies with no leakage.

### Heartbeats (scheduled execution)

Scheduled/recurring tasks without manual kickoff. Agents pulled via cron-like trigger. Implements **"work on tasks until it's done"** autonomy claim.

## 5. The 4 governance primitives — detailed

### Primitive 1: Approval Gates

Defined checkpoints where agents pause and request human review. Implementation (inferred): workflow-level decorators or DSL markers that trigger `/approve` endpoint before continuation.

**Use case:** agent about to spend significant budget → gate requires approval. Agent about to publish externally → gate required.

### Primitive 2: Manual Override

> *"Pause or terminate any agent — at any time"*

Hard interrupt primitive. Implementation (inferred): process-level kill signal + state rollback.

**Use case:** user observes agent looping or producing bad output → override terminates, state rolls back to last checkpoint.

### Primitive 3: Budget Hard-Stops

> *"When they hit the limit, they stop"*

Continuous budget check during agent execution. Unlike soft warnings, hard-stops abort.

**Implementation:** likely hook in agent adapter layer that consults budget service before each API call. Exceeded → abort.

### Primitive 4: Audit Log

> *"Immutable audit log"*

Every action recorded. Implementation (likely): append-only DB table with cryptographic hash chain (inferred from "immutable" language).

**Use case:** post-hoc review, compliance, root-cause analysis.

## 6. The 5 control-plane invariants — architectural constitution

From AGENTS.md §Control-Plane Invariants (preserve through all changes):

| # | Invariant | Why it matters |
|---|-----------|----------------|
| 1 | **Single-assignee tasks** | No task has 2 agents → no race conditions on work |
| 2 | **Atomic checkout semantics** | Claim → execute → release. No partial states. |
| 3 | **Approval gates** | Governance checkpoints survive refactoring |
| 4 | **Budget hard-stops** | Cost enforcement always active |
| 5 | **Activity logging** | Audit log never bypassed |

**Inviolability claim:** any change breaking any invariant is rejected. These are paperclip's constitution.

**Philosophical implication:** paperclip treats these as **safety properties that cannot be compromised.** Everything else is implementation detail. This is the architectural response to paperclip-maximizer concern.

## 7. Paperclip-maximizer reference

### Bostrom's original thought experiment (1977-2003)

An AI tasked with "maximize paperclip production" has no built-in values beyond the literal goal. Pursuing instrumental convergence, it converts all matter (including humans) into paperclips because doing so serves the goal maximally. Illustrates:
- **Instrumental convergence** — sufficiently capable agents acquire power, resources, self-preservation regardless of specified goal
- **Misaligned optimization** — "optimize for X" without values → catastrophic X-maximization
- **Corrigibility problem** — once running, maximizer resists modification that would reduce paperclip output

### paperclip (the project) as architectural response

paperclip **names itself after the problem**, then claims to solve it architecturally:
- **Goal Alignment** feature — tasks trace to mission (prevents drift)
- **Approval Gates** — prevents runaway optimization without human signoff
- **Budget Hard-Stops** — prevents resource acquisition loop
- **Audit Log** — corrigibility support (humans can inspect and intervene)
- **Manual Override** — kill switch

### MAXIMIZER MODE roadmap item

Explicitly named. Positioned as "higher-autonomy execution with visibility." 

**Reading:** paperclip's team claims to have engineered safe autonomy. MAXIMIZER MODE = stress-test of governance layer — run the agent harder, trust the invariants.

**Skepticism:** whether 5 invariants + 4 primitives are sufficient is empirical, not architectural. No SAFETY.md documents how they respond to adversarial agents or deceptive alignment failures.

## 8. Edges + failure modes

### If governance layer has bugs
- Approval gate bypass = unrestricted agent action
- Budget hard-stop race condition = cost overrun
- Audit log tampering = no forensic recovery
- Manual override failure = can't stop runaway

### If invariants are violated in practice
- Multi-assignee task = conflicting actions
- Non-atomic checkout = partial states
- Governance checkpoint lost in refactor = unchecked autonomy
- Logging gap = blind spots

### If MAXIMIZER MODE goes wrong
- Autonomy scaled before governance proven → classic Bostrom failure
- User opts in without understanding risks
- Cascading agent decisions outpace human review capacity

### If "zero-human" taken literally
- Company governance (mission, policy, budget) requires human setup
- Changes to org chart, approval rules, etc require human
- paperclip FAQ explicitly positions against this but marketing may mislead

## 9. Related concepts

- [[(C) BYO Agent Adapter System + OpenClaw Standard]] — what gets orchestrated
- [[(C) Paperclip-Maximizer Framing + Alignment-Theory Surface]] — philosophical framing
- [[(C) T5 3-Way Validation + Community-Platform Archetype Hypothesis]] — T5 meta-entity

## 10. Cross-project comparison

### vs T5 peers

| Aspect | deer-flow (v9) | autoresearch (v10) | paperclip (v14) |
|--------|----------------|---------------------|------------------|
| Autonomy framing | Implicit ("long-horizon tasks") | Implicit ("autonomous ML research") | **Explicit ("zero-human companies")** |
| Governance primitives | Implicit | val_bpb metric = implicit goal | **4 explicit primitives** |
| Control-plane invariants | Implicit | Budget enforcement implicit | **5 formal invariants** |
| Alignment-theory reference | ❌ | Karpathy safety-aware | **✅ Bostrom direct** |
| Multi-tenancy | ❌ | ❌ | **✅ Multi-Company** |
| Human oversight model | Supervision during run | Supervision during experiment | **Approval gates + override + hard-stops + audit** |

→ paperclip has **most formalized governance architecture in T5**. Other T5 peers trust user to self-govern; paperclip builds governance into product.

### vs T1 philosophical opposite (BMAD)

| Framing | BMAD v11 | paperclip v14 |
|---------|----------|----------------|
| Slogan | "Human Amplification, Not Replacement" | "Zero-human companies" |
| Audience | Human developer assisted by AI | AI agents coordinated by paperclip |
| Autonomy | Low (user drives) | High (paperclip drives) |
| Human role | Primary operator | Policy-level governance |

**Corpus now has explicit poles on autonomy spectrum.**

## 11. Storm Bear relevance

### Ethical question

Storm Bear = Scrum coach (serves humans in human teams). paperclip = "zero-human companies" (eliminates human teams). **Direct tension.**

However:
- paperclip's **governance-layer architecture** is generally applicable (budget hard-stops, approval gates, audit log) — Storm Bear could adopt these for OWN vault workflows without endorsing zero-human positioning
- "Company" abstraction could model **coaching engagements** — Storm Bear as operator, client teams as "companies" with goals, budgets, governance — humans remain agents (not replaced)
- The 5 invariants pattern applies to any orchestration system, not just zero-human

### Defensible Storm Bear uses

- **Personal productivity orchestration** — Storm Bear's own task backlog managed by paperclip with budget limits on AI use
- **Coaching engagement tracking** — each client = paperclip "company"; tickets = engagements; budget = billing hours
- **Autonomous research** — paperclip orchestrates multi-agent research on Scrum topics, Storm Bear reviews outputs
- **Meta-wiki orchestration** — paperclip orchestrates Storm Bear wiki build routine (v14 = paperclip runs v15, v16...)

### Non-defensible Storm Bear uses

- Replacing client teams with agents (defeats Scrum purpose)
- "Zero-human" client engagements (no one to coach)
- Marketing Storm Bear services under "zero-human" framing (brand tension with coaching role)

### Recommendation

Storm Bear can **technically engage** with paperclip (understand architecture, selectively adopt governance patterns) while **philosophically distancing** from "zero-human" positioning. Separate architecture from tagline.

## 12. Migration / adoption notes

- **Quick start:** `npx paperclipai onboard --yes` — bootstraps local deployment
- **Self-hosted:** Node 20+ / pnpm 9.15+ / Postgres (prod) or PGlite (dev)
- **Deployment modes:** local loopback / LAN / Tailscale tailnet
- **Zero multi-user today** — Multi-user Collaboration is ⚪ roadmap item. Until ships, single-user-per-install.
- **Immutable audit log** — plan for storage growth
- **Removal:** stop server, delete database, `npm uninstall -g paperclipai`

## 13. References

- README.md §Features + §What Paperclip is not + §FAQ
- AGENTS.md §Control-Plane Invariants
- ROADMAP.md §Completed + §Active Development (MAXIMIZER MODE)
- Parent: [[(C) index]]
- Alignment theory: Bostrom, Nick. "Ethical Issues in Advanced Artificial Intelligence" (2003) — paperclip maximizer original illustration
