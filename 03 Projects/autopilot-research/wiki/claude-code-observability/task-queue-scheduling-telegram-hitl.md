# Task Queue, Scheduling & Telegram Human-in-the-Loop

> Observability-first command center: task queue vs cron schedules; when to plan vs ad hoc; per-skill model assignment; Telegram approval gate as human-in-the-loop checkpoint. Source: Mansel Scheffel, "Claude Code + OpenTelemetry = Claude Command Center" [04:35]-[09:05], uploaded 2026-04-22, atomicOps consulting.

## Source

Raw file: `../../raw/2026-06-20-claude-code-otel-command-center.md`

Original resources:
- Video: https://youtu.be/dITtLiC9FzM (04:35-09:05 segment)
- [[../claude-cowork/_index]] — Anthropic's official agent conversation layer (replaces mission control)
- [[../telegram-remote-control-stack/_index]] — Telegram API + Claude Code integration stack (already pilot-verified 2026-05-08)
- [[../autonomous-loops-human-in-the-loop/_index]] — HITL architecture patterns (drafts-not-sends, scoped permissions)
- [[../claude-api-cost-optimization/_index]] — cache-hit-rate metric + prompt caching as #1 cost lever

---

## The Core Pattern: Schedule First, Ad Hoc with Reason

⚠️ **Creator's principle (video-only, unverified guidance):** "Plan your business life; schedule first, then ad hoc with concrete reasons."

The argument is operational:
- **Predictable work** (morning brief, weekly reports, daily monitoring) → cron schedule
- **Ad hoc work** (one-off research, urgent requests) → task queue with explicit justification
- Without this discipline, you create a pile of agents and tasks that you'll eventually have to manage or troubleshoot

**Why:** scheduled tasks run unattended; ad hoc tasks should be exceptions, not the default. This avoids "introducing a seven-layer microservice that absolutely doesn't need to exist" (creator phrase). Anthropic already built [[../claude-cowork/_index]] for interactive agent conversation; use Cowork for the agent front-layer instead.

---

## Scheduled Tasks (Cron Model)

### Setup

Via Claude Code IDE or Cowork:
1. Set **cron schedule** (e.g., daily at 09:00)
2. Name the skill command (e.g., `morning-brief-skill`)
3. Enable by default
4. The task runs unattended at the scheduled time

⚠️ **Creator's example (video-shown UI, unverified config details):** scheduling a "morning brief" skill at 09:00 daily; the exact UI/UX and form fields shown are his custom build, not part of official Claude Code.

### Key constraint: Cowork is easier than cron

The creator explicitly recommends: if you're in Cowork, just set a scheduled task there. If you're in the IDE, use cron. Don't build custom scheduling infrastructure when the tool already supports it.

---

## Task Queue (Ad Hoc Model)

### Two modes

**Interactive session:**
- Back-and-forth with the agent inside the command center panel
- Human stays engaged
- Example: drafting a document, iterating on code

**One-shot skill fire:**
- Fire a known skill once, no follow-up
- Example: "make me a gamma deck" or "run the security audit skill"
- Minimal context load since the skill is pre-built

### Model assignment per task (cost discipline)

⚠️ **Creator's framing (video-shown behavior, unverified system implementation):** "Don't run everything on Opus; assign Sonnet to a gamma deck because most of the AI work is done by the gamma agent itself."

**The principle:** Claude Code allows you to set a model per skill. Don't default to Opus everywhere.

**Cost reasoning:**
- **Context load**: each skill that runs on Opus increases token load + cost, even if it doesn't need Opus capability
- **Gamma decks example**: Gamma itself does heavy lifting (slides, layout). Claude (Sonnet) just coordinates inputs. Opus is overkill.
- **Effective constraint**: if the task is "delegate work to a specialized agent" (not "do the whole task yourself"), use Sonnet and let the agent handle the complexity

### Task priority

Set priority to order tasks in the queue if multiple are queued simultaneously.

---

## Telegram Approval Gate (Human-in-the-Loop)

### The pattern: requires-approval → Telegram notification → approve-from-phone

⚠️ **Creator's implementation (video-shown UI, custom-built):** the command center has a "requires-approval" checkbox. When checked, the task pauses and sends a Telegram message to the operator's phone asking for approval. The operator taps "approve" in Telegram, the task moves to "running" status.

**Mechanism:**
1. Task is queued with `requires-approval: true`
2. Command center sends a message to Telegram (via bot) → operator's phone
3. Operator taps approve/reject button (callback_query in Telegram API terms)
4. Task status updates to "running" (or "rejected")
5. Live session visible in the command center as it executes

⚠️ **Unverifiable implementation detail:** the creator's exact command center UI (the panel that shows "pending approval", the Telegram message format, the status change animation) is his custom build. However, the **pattern itself is standard**: Telegram API exists (send_message, callback_query), Claude Code integration via Channels is in public beta, and Stop Hooks can pause execution. See [[../telegram-remote-control-stack/_index]] for setup recipes.

### Why requires-approval matters

Operational reasons:
- **Runaway loop mitigation**: human veto checkpoint before a task burns tokens or does unintended work
- **Unintended autonomy**: if a task is ad hoc (not scheduled), requires-approval makes it deliberate ("did I mean to start this?")
- **Cost discipline**: high-token or high-risk tasks (e.g., "email 100 leads") should ask for approval first
- **Integration with monitoring**: because the command center shows live sessions, approval → execution → completion forms a complete audit trail

### Cross-link: HITL + observability

See [[../autonomous-loops-human-in-the-loop/_index]] for broader HITL framing (drafts-not-sends, scoped permissions, alignment-positive autonomy). The Telegram approval gate is **one specific HITL checkpoint** — the decision point right before execution. Cost-optimization discipline applies: while waiting for approval, check the cache-hit-rate metric (see [[../claude-api-cost-optimization/_index]]) to understand token efficiency before you approve.

---

## Live Sessions & Monitoring

### Observing task execution

Once a task is approved and running:
1. The command center shows **live sessions** (creator terminology: "router session" + "worker session"; this is his custom implementation)
2. ⚠️ **Creator's live-tail behavior (video-shown, custom UI):** the "live tail with grep" is shown as a custom panel in the command center. The mechanism is standard: Claude Code exports session transcripts to local JSONL logs; grepping the transcript is deterministic. However, the exact grep-in-GUI integration is his build.
3. Session history: all completed sessions appear in a "recent sessions" panel with session ID, model, duration

### Session metadata captured

- Session ID
- Model used (Sonnet, Opus, Haiku)
- Duration
- Task name
- Queued tasks show: "pending" → (Telegram approval) → "running" → "completed"

---

## Skill Cost Metrics (Integration with Observability)

Once a task completes, it feeds into cost tracking via OpenTelemetry:

- **Skill activations** (OTEL metric: `skill_activated` event): how many times the skill was invoked in the last 24 hours
- **Tokens per skill** (OTEL metric: `claude_code.token.usage` with `skill.name` attribute): exact token breakdown by model and skill
- **Cost per run** (OTEL metric: `claude_code.cost.usage` with `skill.name` attribute): how much a single skill execution cost (aggregate vs per-run)
- **MCP/tool latency + error rate** (OTEL event: `tool_result` with `duration_ms` and `success` attributes): understand which integrations are slow or flaky

⚠️ **Creator's example (video-shown data, unverified):** the creator's "AI news monitor" skill ran 23 times in a day and used 32 million tokens. Seeing that number, he audited the skill, simplified it, and cut token use drastically. This is his specific operational case; your metrics will differ.

**Observability → decision → efficiency:** the metric aggregation enables auditing without access to a native in-product cost dashboard (see [[../claude-code-observability]] for config details).

See [[../mcp-and-skill-cost-metrics]] and [[../claude-api-cost-optimization/_index]] for metric details and cache-hit-rate monitoring discipline.

---

## Key Takeaways

- **Schedule the predictable, ad hoc the exception**: cron schedules run unattended; task queue is for deliberate one-offs. Without this discipline, you accumulate unmanageable agents.
- **Use Cowork for agent conversation, not custom mission control**: Anthropic built [[../claude-cowork/_index]] for the interactive front-layer. Don't reinvent.
- **Per-skill model assignment is cost discipline**: assign Sonnet to coordinator tasks, Opus to complex reasoning. Don't default to Opus everywhere.
- **Telegram approval is a human veto checkpoint**: `requires-approval: true` pauses a task and pings your phone. Approve = continue. This pattern mitigates runaway loops and makes ad hoc work deliberate.
- **Observability feeds operational decisions**: task queues + live sessions show execution in real time; completed sessions feed cost metrics; cost metrics reveal which skills are inefficient. Without this feedback, you can't improve.
- **HITL approval + cache monitoring compound**: while a task waits for Telegram approval, read its transcript to check cache hit rate (see [[../claude-api-cost-optimization/_index]]). Approval becomes an informed decision, not a rubber stamp.
- **The creator's exact UI is custom; the primitives are standard**: requires-approval → Telegram → approve-from-phone is a real pattern (Telegram API, Claude Channels beta, Stop Hooks). The specific dashboard UI, panel layouts, form fields, and live-tail-with-grep integration shown in the video are his unreleased build. The architecture is reproducible; the exact look-and-feel is not.

---

## Cross-Links to Related Topics

- [[../claude-code-observability]] — complete OTEL metric/event catalog + configuration reference
- [[../claude-cowork/_index]] — official Anthropic agent conversation layer (recommended instead of custom mission control)
- [[../telegram-remote-control-stack/_index]] — Telegram API integration + Layer 1-3 architecture (setup recipes, Layer 2 headless engine, MCP messaging)
- [[../autonomous-loops-human-in-the-loop/_index]] — HITL patterns (drafts-not-sends, scoped permissions, human veto checkpoints)
- [[../claude-api-cost-optimization/_index]] — cache-hit-rate as #1 cost lever (#1 silent killer: timestamp in system prompt)
- [[../claude-skills]] — skill registration + cost-per-skill metrics
- [[../harness-engineering]] — observability as a harness property (deterministic + telemetry complement)
- [[../claude-code-hooks]] — Stop Hooks as execution checkpoints (complement to HITL Telegram approval)
- [[../mcp-and-skill-cost-metrics]] — tool latency + MCP error rates from OTEL events

---

## Gotchas & Caveats

1. **Creator's UI is unreleased code**: the command center dashboard (task queue panel, Telegram notification format, live-session viewer, skill-cost breakdown, live-tail-with-grep) is his custom build. You cannot clone it 1:1 without his source code. However, the **PRIMITIVES** (cron scheduling, per-skill model assignment, Telegram bot API, requires-approval flag, OTEL metrics export, session JSONL logs) are standard and documented.

2. **Telegram approval is a pattern, not a tool**: the creator shows his implementation. To build your own: (a) set up a Telegram bot (BotFather), (b) integrate Claude Code via Channels (public beta), (c) use a Stop Hook to pause before send, (d) send a callback message via Telegram API. See [[../telegram-remote-control-stack/_index]] for detailed setup.

3. **OTEL metrics are opt-in**: telemetry is NOT enabled by default. You must set `CLAUDE_CODE_ENABLE_TELEMETRY=1` to export metrics. See [[../claude-code-observability]] for complete environment variable reference.

4. **Live sessions require real-time transcript access**: the creator's "live tail with grep" assumes Claude Code exports session transcripts to disk as they run (JSONL format to `~/.claude/sessions/`). This is the native session-log feature, not a special dashboard. Grepping it is manual, not UI-driven. See [[../jsonl-logs-and-native-dashboard]] for transcript access patterns.

5. **Skill cost is approximate**: `claude_code.cost.usage` metric is an estimate based on OTEL event token counts. The authoritative bill comes from Claude API provider (Claude Console, Bedrock, Vertex). Use OTEL for operational insights, not billing reconciliation.

6. **Cowork vs cron scheduling**: the creator recommends Cowork for ease. If you're in the IDE, cron is fine. Don't build custom task scheduling when both tools exist.

7. **No native in-product dashboard**: Anthropic's official docs do NOT document a built-in in-GUI dashboard, `/cost` command, or statusline fed by OTEL. All dashboards must be built externally in Grafana, Datadog, Prometheus, or other OTLP backends.

---

## Unverified Claims (Flagged for Future Validation)

- ⚠️ "Requiring approval → Telegram → phone approval" is shown in the video but depends on the creator's custom build. The pattern (Telegram API + Stop Hook + Channels integration) is real; the exact dashboard UI is not.
- ⚠️ "Live tail with grep" is shown as a real-time panel in the command center. The actual mechanism (read session JSONL, grep it, display results) is standard; the UI integration is custom.
- ⚠️ "Router session + worker session" is the creator's terminology and architecture. The concept (a task orchestrator that dispatches between worker agents) is common; his exact implementation is custom.
- ⚠️ "Most of the AI work is done by the gamma agent itself" — the creator's reasoning for assigning Sonnet to gamma-deck tasks. Not verified against Gamma documentation or independent user data.
- ⚠️ "News monitor skill ran 23 times and used 32 million tokens" — creator's specific operational data from his custom dashboard. Cannot be independently verified without access to his environment.
