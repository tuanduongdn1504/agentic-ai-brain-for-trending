# (C) 8-Stage Agent Pipeline

> **Source:** `docs/01-agent-loop.md` (lines 1-100 + stage details section), `docs/00-architecture-overview.md`, CLAUDE.md
> **Ingested:** 2026-04-18
> **Type:** Entity page (workflow concept) — building block #1 cho goclaw

---

## One-liner

**VI:** 8-Stage Agent Pipeline là **internal execution loop** của goclaw's agent — mỗi request chạy qua ContextStage → ThinkStage → PruneStage → ToolStage → ObserveStage → CheckpointStage → FinalizeStage (7 actual Stage classes, marketed as 8 conceptual stages). Khác với Sprint Pipeline (gstack) hay 7-Stage Workflow (Superpowers) — những cái đó là **developer workflow stages**; goclaw's là **low-level agent execution loop**.

**EN:** 8-Stage Agent Pipeline is goclaw's internal agent execution loop — 7 actual Stage classes (marketed as 8 conceptual). Operates at lower abstraction than gstack's Sprint Pipeline or Superpowers's 7-Stage Workflow — those are developer workflow stages; goclaw's is the agent's per-request think-act-observe cycle.

---

## Khi nào dùng concept này

**Hữu ích khi:**
- Hiểu cách goclaw execute 1 agent request internally
- Designing custom agent framework — xem pipeline pattern as template
- Compare abstraction levels với sibling frameworks
- Debug agent behavior (which stage failed?)

**Không cần để use goclaw cơ bản** — pipeline runs transparent. User chỉ thấy Think→Act→Observe externally.

---

## Comparison sibling

**KEY POSITIONING:** These are NOT equivalent — different abstraction levels.

| Axis | 8-Stage Pipeline (goclaw) | 7-Stage Workflow (Superpowers) | Sprint Pipeline (gstack) | Sequential Phases (ECC) |
|------|---------------------------|-------------------------------|--------------------------|-------------------------|
| **Abstraction level** | **Agent execution loop** (low-level, internal) | Developer workflow (high-level, external) | Developer workflow (high-level) | Developer workflow |
| **Who owns** | Agent runtime | Dev's sprint | Dev's sprint | Dev's sprint |
| **When runs** | Every LLM call | Every feature/PR | Every feature/PR | Every feature/PR |
| **Iteration count** | Max 20 per request | 1 per feature | 1 per sprint | 1 per cycle |
| **Pluggable** | ✅ Stages swappable | ❌ Hard-gated XML | ⚙️ Smart routing | ✅ Fully flexible |
| **Timeframe** | Seconds | Hours-days | Days | Varies |

→ **They're complementary.** goclaw's pipeline runs inside each agent invocation; Superpowers/gstack pipeline is the dev's work process.

---

## Sub-types: 7 Stage classes

### 1. ContextStage (Setup, runs once)

- Inject context via `WithAgentID()`, `WithUserID()`, `WithAgentType()`, `WithLocale()`, `WithTenantID()`
- Resolve per-user workspace (base + sanitized userID)
- Ensure per-user files exist (idempotent via `sync.Map` cache)
- Persist agent/user IDs on session

→ **Establishes execution context.** Single source of truth cho downstream stages.

### 2. ThinkStage (Iteration, most complex)

- Resolve workspace + context files dynamically
- Build system prompt (**15+ sections**)
- Inject conversation summary if exists
- Run history pipeline (`limitHistoryTurns → sanitizeHistory`)
- Filter tools through PolicyEngine (RBAC)
- Call LLM, record span with token counts
- Emit `chunk` events (streaming) or single response

→ **Where LLM call happens.** All pre-call prep + post-call output parsing.

### 3. PruneStage (Iteration, opt-in)

Enabled via `contextPruning.mode: "cache-ttl"`.

- Estimate token ratio vs context window
- **≥25%:** soft trim pass (keep first/last 3000 chars, replace middle with `"..."`)
- **≥50%:** hard clear pass (replace with placeholder)
- Run `sanitizeHistory` to fix broken tool_use/tool_result pairs after prune
- Trigger memory flush (synchronous) if compaction threshold exceeded

→ **Anthropic cache awareness** — default OFF to prevent silent prompt-cache invalidation.

### 4. ToolStage (Iteration)

- Execute single tool sequentially (no goroutine overhead)
- Execute multiple tools in parallel via goroutines, sort results by index
- Emit `tool.call` before, `tool.result` after
- Record tool span

→ **Parallelism when >1 tool.** Single-tool fast path avoids overhead.

### 5. ObserveStage (Iteration)

- Process tool result stream
- Handle `NO_REPLY` convention (silent completion)
- Append assistant message with tool call info

→ **Observation = packaging tool results for next LLM call.**

### 6. CheckpointStage (Iteration)

- Increment iteration counter
- Check if max iterations reached → `BreakLoop`
- Check if context cancelled → `AbortRun`

→ **Safety valve** to prevent infinite loops (max 20 iterations).

### 7. FinalizeStage (Finalize, runs once)

- Run **7-step output sanitization pipeline**
- Flush buffered messages atomically
- Update session metadata (model, provider, token counts)
- Emit `run.completed` or `run.failed` event

→ **Uses background context if cancelled** — finalize runs regardless of cancellation.

---

## Anatomy: Flow diagram

```
Loop.Run(runRequest)
   ↓
pipeline_enabled? — NO → V2 monolithic (runLoop)
                — YES ↓
NewRunState (input, nil, model, provider)
   ↓
NewDefaultPipeline (8 stages)
   ↓
Pipeline.Run:
   ├─ Setup (once)
   │   └─ ContextStage
   │
   ├─ Iteration Loop (max 20)
   │   ├─ ThinkStage
   │   ├─ PruneStage (opt-in)
   │   ├─ ToolStage
   │   ├─ ObserveStage
   │   └─ CheckpointStage
   │
   └─ Finalize (once, bg context if cancelled)
       └─ FinalizeStage
   ↓
convertRunResult (pResult → RunResult)
   ↓
RunResult
```

### 8-stage marketing vs 7-class implementation

Marketing framing (README + CLAUDE.md):
```
context → history → prompt → think → act → observe → memory → summarize
```

Implementation mapping:
- **context** = ContextStage
- **history** = inside ThinkStage (`limitHistoryTurns → sanitizeHistory`)
- **prompt** = inside ThinkStage (build system prompt, 15+ sections)
- **think** = ThinkStage (LLM call)
- **act** = ToolStage
- **observe** = ObserveStage
- **memory** = PruneStage (triggers memory flush)
- **summarize** = FinalizeStage

→ **Marketing bundles history+prompt into "think"; implementation splits.** Both frames valid.

---

## Cơ chế

### Mechanism 1: Feature-flag V2/V3 migration

```go
if pipeline_enabled {
    return runViaPipeline(runRequest)
} else {
    return runLoop(runRequest)  // V2 legacy
}
```

Both paths implement **same external behavior**. Difference = internal architecture.

→ **Classic rewrite-without-disruption pattern.** Ship new architecture behind flag, migrate gradually.

### Mechanism 2: Pluggable callback system

Stages accept callbacks at each lifecycle point. Hooks system (`internal/hooks/`) leverages này:
- SessionStart
- UserPromptSubmit
- PreToolUse
- PostToolUse
- Stop
- SubagentStart / SubagentStop

→ **External code can inject into pipeline** without forking. Reusable pattern for extensibility.

### Mechanism 3: Bounded iteration

Max 20 iterations per `RunRequest`. Prevents:
- Infinite loops (LLM hallucinates repeated tool calls)
- Runaway cost (20 LLM calls = hard ceiling)
- Context window exhaustion

→ **Safety first.** Plus CheckpointStage cancellation propagation.

### Mechanism 4: Background context on cancellation

FinalizeStage runs với background context if main cancelled.

→ **Cleanup guarantee.** Agent state always finalized, even on abort.

### Mechanism 5: Span tracing throughout

Every stage records span (for OpenTelemetry OTLP export if enabled).

→ **Observability built-in.** Not retrofitted.

---

## Out-of-box behavior

**Default configuration:**
- V2 monolithic (backward compat default)
- Max 20 iterations
- Context pruning OFF (opt-in)
- No hooks installed (user must configure)
- Single tool serial, multi-tool parallel

**To enable V3 pipeline:**
```json5
// config.json5
agents: {
  defaults: {
    pipeline_enabled: true
  }
}
```

**To enable context pruning:**
```json5
agents: {
  defaults: {
    contextPruning: { mode: "cache-ttl" }
  }
}
```

---

## Configuration knobs

| Knob | Default | Range | Effect |
|------|---------|-------|--------|
| `pipeline_enabled` | `false` | bool | V2 legacy vs V3 pipeline |
| `contextPruning.mode` | none | `"cache-ttl"` | Enable PruneStage |
| Max iterations | 20 | hardcoded | Ceiling for iteration loop |
| Tool parallelism | auto | 1 tool serial, >1 parallel | Performance tradeoff |
| Hooks | none | lifecycle events | Extensibility |

---

## Recipes

### Recipe 1: Enable V3 pipeline

Edit `config.json5`:
```json5
agents: {
  defaults: {
    pipeline_enabled: true
  }
}
```

Restart goclaw. Verify qua LLM call span (should show stage breakdown).

### Recipe 2: Custom PreToolUse hook

Hook system (`internal/hooks/`) registers handlers matching events:

```json5
hooks: {
  PreToolUse: [{
    matcher: { regex: "exec|shell" },
    handler: { type: "http", url: "..." }
  }]
}
```

→ **Every tool use logged** to external system before execution.

### Recipe 3: Debug stage-level failure

If agent behaves oddly, check span trace:
```bash
# With OTel enabled (WITH_OTEL=1)
# Open Jaeger UI: http://localhost:16686
# Filter by service "goclaw"
# See stage-level spans với timings + errors
```

→ Identifies which stage failed (ThinkStage LLM error, ToolStage execution error, etc.)

### Recipe 4: Force context pruning cho long sessions

If agent runs long sessions + hits context limits:

```json5
agents: {
  defaults: {
    contextPruning: { mode: "cache-ttl" }
  }
}
```

**Caveat:** Invalidates Anthropic prompt cache. Trade-off: longer sessions vs cache efficiency.

---

## Advanced patterns

### Pattern: Stage composition

Stages are interfaces. Custom stages can replace defaults:

```go
// Conceptual — not verified API
customPipeline := pipeline.New().
    WithContext(MyContextStage{}).
    WithThink(DefaultThinkStage{}).
    WithTool(MyCustomToolStage{}).
    ...
```

→ **Reusable abstraction** cho agent framework builders.

### Pattern: Conditional PruneStage

PruneStage only runs when enabled. Flag-gated to zero-cost when off.

→ **Graceful degradation** — feature doesn't penalize non-users.

### Pattern: Event emission at stage boundaries

`chunk`, `tool.call`, `tool.result`, `run.completed`, `run.failed` events. Emits via `DomainEventBus`.

→ **Downstream consumers** (channels, UI, consolidation workers) all decouple via events.

---

## Combination với building blocks khác

### + 3-Tier Memory
PruneStage (Stage 5/Memory) triggers consolidation workers in `internal/consolidation/`. [[(C) 3-Tier Memory + Knowledge Vault]] detail.

### + Agent Teams
Team lead's agent also runs 8-stage pipeline. When team lead delegates → child agent runs own pipeline. Nested pipelines.

### + Multi-Tenant Architecture
ContextStage injects tenant ID via `WithTenantID()`. All downstream stages tenant-aware.

### + Hooks System
Hooks inject at stage boundaries. PreToolUse → before ToolStage. PostToolUse → after. Extensibility layer.

### Cross-project: vs Superpowers 7-Stage Workflow
**Different layer.** Superpowers's stages = dev workflow (brainstorm → ship). goclaw's stages = agent runtime. Can coexist: dev uses Superpowers's workflow to ship gstack skills; those skills run inside goclaw's pipeline via ACP provider.

### Cross-project: vs gstack Sprint Pipeline
Same layer difference as above. Sprint Pipeline = dev's sprint; 8-Stage Pipeline = agent's execution.

---

## Anti-patterns

❌ **Confuse với dev workflow stages** — goclaw's pipeline ≠ Superpowers's 7 stages. Different abstraction level.

❌ **Enable PruneStage without need** — invalidates Anthropic prompt cache. Only enable if hitting context limits.

❌ **Assume V2 = V3** — same external behavior, but V3 pluggable. V2 legacy. New projects = use V3.

❌ **Hardcode iteration count >20** — 20 is hard ceiling cho safety. Higher = risk runaway cost.

❌ **Skip CheckpointStage cancellation checks** — no cancel prop = agents ignore user abort.

❌ **Miss FinalizeStage on cancellation** — finalize runs with background context. Don't skip.

❌ **Forget stage-level hooks are optional** — hooks fire if registered. If you expect PreToolUse logging but no hook registered, no logs.

---

## Cross-references

- [[(C) 3-Tier Memory + Knowledge Vault]]
- [[(C) Multi-Tenant Architecture]]
- [[(C) Agent Teams and Orchestration]]
- [[(C) README summary]] — high-level features list
- [[(C) CLAUDE.md + Architecture summary]] — 11 distinctive patterns
- [[(C) Key Docs deep dive]]
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) The 7-Stage Workflow.md` — dev workflow comparison (different abstraction level)
- Cross-project: `../../gstack - Beginner Analysis/02 Wiki/(C) Sprint Pipeline.md` — sprint pattern comparison

## Citations

- `docs/01-agent-loop.md` lines 1-100 (V3 pipeline architecture + stage breakdown)
- `docs/00-architecture-overview.md` lines 37-95 (Core Engine diagram)
- CLAUDE.md key pattern #5 (pipeline details)
- Discrepancy noted: marketing "8 stages" vs implementation "7 Stage classes"

## TODO

- ⏸ Read full `docs/01-agent-loop.md` lines 100+ (orchestration modes section)
- ⏸ Verify exact Stage interface signature in Go source (`internal/pipeline/`)
- ⏸ Document default `NewDefaultPipeline()` implementation
- ⏸ Understand "V2 monolithic" path — why legacy? Will V2 be removed?
