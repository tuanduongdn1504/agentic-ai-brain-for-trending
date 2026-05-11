# Failure modes + recovery

> Combined synthesis of `fix-logs`, `session-recovery`, error-handling sections across the 21 source guides.

## Common failure modes ClaudeKit users hit

### 1. Rate limits / account bans

- AI providers hit usage limits mid-session → flow freezes
- Using certain tools with Google accounts can trigger **permanent bans for ToS violation**
- Multiple accounts under same upstream pool share quota — CCS routing does NOT solve this

### 2. Context bloat (>100K tokens)

- Sessions exceeding 100K tokens become sluggish or unstable
- **`/resume` does NOT help** — "moves the problem rather than fixes it"
- Recovery: `/export` essential conversation to text → start fresh session → paste curated context

This is the operational consequence of Mnilax Rule 6 (token budgets) being violated.

### 3. Circular logic / infinite loops

- If bug-fix attempt fails **3 times**, system recognizes "wicked problem" or architectural deadlock
- Stops to prevent token waste — does NOT spiral

This is the deterministic implementation of Mnilax Rule 10 (checkpoint discipline) + Rule 12 (fail loud) — system knows when to give up.

### 4. Session timeouts

- Terminal closed or connection lost for **>10 minutes** → session times out
- Recovery depends on what was persisted (see below)

## Error log capture pattern

ClaudeKit doesn't react to in-memory errors — it requires **evidence-based** diagnosis from log files.

```bash
# Standard capture pattern
npm run dev 2>&1 | tee logs.txt

# Then feed to /ck:fix
/ck:fix logs.txt
```

The **debugger agent reads the last 30 lines of the log file first** — most recent failure prioritized over older noise.

## `/ck:fix` 6-phase diagnostic pipeline

When triggered with a log file, structured pipeline runs:

| Phase | Action |
|---|---|
| **Scout** | Gather evidence from logs + stack traces |
| **Diagnosis** | Root Cause Analysis (RCA) based on evidence, NOT guessing |
| **Routing** | Determine complexity → choose fix workflow |
| **Fix** | Implement the change |
| **Verification** | Run tests + add regression tests for this specific bug |
| **Prevention** | Document fix in journal or plan |

This is the most-structured failure-recovery workflow in the entire ClaudeKit surface. Borrowable pattern even outside ClaudeKit.

## State persistence — what survives

The `session-state.cjs` hook automatically saves to `.claude/session-state/.last-state.md`:

| State | Persisted? |
|---|---|
| Current implementation plan | ✅ |
| Todo items + progress context | ✅ |
| Subagent outputs | ✅ |
| Git branch + commit status | ✅ |
| Full conversation log | ✅ (via Claude Code native session log) |
| In-memory variables / process state | ❌ |
| Cross-CCS-account session | ❌ |

## Recovery workflows

### Healthy context → `/resume`

When session is intact (not bloated, not timed out):

```bash
# Restores last session by ID or name
/resume <session-id>
```

Full context restored from `.claude/session-state/.last-state.md`.

### Provider hit rate limit → `ccs <profile> --resume`

CCS-specific recovery:

```bash
ccs glm --resume    # switch to GLM provider, continue same task
ccs kimi --resume   # or Kimi
```

Allows finishing task even if primary provider locked out. CCS keeps the task context, only swaps the inference engine.

### Bloated context → `/export` + fresh start

When session >100K tokens, `/resume` doesn't help:

```bash
/export current-task.md   # export essential conversation
# Start new session
# Paste curated relevant pieces into fresh context
```

User curates what's essential — system can't auto-determine this.

## What CANNOT be recovered

### CCS sub-account isolation

CCS profiles (e.g., "work" vs "personal") use **different `CLAUDE_CONFIG_DIR` paths** — completely isolated:

```
~/.claude-work/      # work profile
~/.claude-personal/  # personal profile
```

- Cannot `/resume` across profiles
- Must manually copy `.jsonl` session files to bridge
- Trade-off: clean separation vs cross-profile continuity

### In-flight model state

If session crashes mid-tool-use (e.g., long-running `/ck:cook`), only the LAST checkpoint survives. Work between last checkpoint and crash is lost. Mitigation: smaller checkpoints (per Mnilax Rule 10).

### Permanent provider bans

ToS-violation bans are not recoverable via the tool. User must contact provider directly.

## Failure-mode coverage relative to Mnilax 12 rules

Mapping which rules ClaudeKit implements via infrastructure vs leaves to the user:

| Mnilax rule | ClaudeKit implementation | Status |
|---|---|---|
| Rule 1 (Think before coding) | `/ck:brainstorm`, `/ck:plan` enforce thinking phase | ✅ Implemented |
| Rule 2 (Simplicity first) | None — only enforced via CLAUDE.md text | ⚠️ User responsibility |
| Rule 3 (Surgical changes) | Approval gates prompt before commits | ✅ Implemented |
| Rule 4 (Goal-driven) | `/ck:cook` requires success criteria | ✅ Implemented |
| Rule 5 (Model for judgment only) | Hooks ARE the deterministic layer (no model decision) | ✅ Architecturally implemented |
| Rule 6 (Token budgets) | Soft limit at 100K; halts at 3 failed attempts | ⚠️ Partial — no hard per-task budget |
| Rule 7 (Surface conflicts) | None | ⚠️ User responsibility |
| Rule 8 (Read before write) | `/ck:scout` is the explicit "read" command | ✅ Implemented |
| Rule 9 (Tests verify intent) | `/ck:test` + Tester agent — but doesn't enforce intent semantics | ⚠️ Partial |
| Rule 10 (Checkpoint) | `session-state.cjs` persists per-step state | ✅ Implemented |
| Rule 11 (Convention conformance) | None — only enforced via CLAUDE.md text | ⚠️ User responsibility |
| Rule 12 (Fail loud) | 3-attempt halt for wicked problems; explicit "Research Preview" labeling | ✅ Implemented |

**Score:** 7 of 12 fully implemented via infrastructure; 3 partial; 2 left to user. Strong but not complete coverage.

## Key Takeaways

- **3-attempt halt** is the most-borrowable failure-discipline pattern (Mnilax Rule 12 in code form)
- **State persistence works for predictable disruptions** (timeout, restart, provider switch) but NOT for context bloat — there's no auto-summarization at 100K
- **CCS sub-account isolation** is a hard wall — by design, but causes friction for cross-account work
- **`/ck:fix` 6-phase pipeline** is the most-structured workflow in ClaudeKit and stand-alone borrowable
- ClaudeKit implements 7 of 12 Mnilax rules infrastructurally — Rules 2, 7, 11 still require user discipline via CLAUDE.md text
