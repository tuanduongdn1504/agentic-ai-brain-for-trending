# Request lifecycle — from prompt to delivery

> How a typical ClaudeKit request flows through the system. Synthesized from `flowchart`, `how-ck-works`, `hooks`, and `inside-claudekit` source guides.

## The 4 phases

### Phase 1 — Initiation (user prompt + command selection)

User types a command in terminal, e.g., `/ck:cook "add a login button"`.

**User decision at this phase:** Speed vs Safety trade-off
- **Fast** path: `/ck:cook` for direct implementation
- **Safe** path: `/ck:plan` first, then `/ck:cook` after review — for complex features

System action: ClaudeKit identifies the requested Skill and loads its `SKILL.md` knowledge package.

### Phase 2 — Pre-execution (Hooks, the "underground" layer)

Hooks fire automatically before AI begins working. These are deterministic background scripts — NOT model decisions.

| Hook | What it does |
|---|---|
| `session-init.cjs` | Detect project type (Node, Python, etc.) + load env config |
| `session-state.cjs` | Check for previous session progress → resume context |
| `privacy-block.cjs` | Scan request for sensitive file access (`.env` etc.) → prompt user if triggered |

**User intervention:** if a privacy/security block fires, user manually approves to continue. Otherwise the user is invisible at this phase.

### Phase 3 — Execution (Agent coordination)

Workflow triggers a "team of specialists" — agents working sequentially:

| Phase | Agent | Output |
|---|---|---|
| 3.1 Research & Scouting | Scout / Researcher | Read project docs + existing code patterns; establish style baseline |
| 3.2 Planning | Planner | Create `plan.md` + break task into "phases" |
| 3.3 Implementation & Testing | Builder/Full-stack + Tester | Write code → run local tests immediately |
| 3.4 Quality Control | Reviewer | Audit changes vs OWASP + quality standards |

**Specific 6-phase pipeline for `/ck:fix`:**

```
Scout → Diagnosis → Routing → Fix → Verification → Prevention
```

| Phase | What happens |
|---|---|
| Scout | Gather evidence from logs + stack traces |
| Diagnosis | Root Cause Analysis (RCA) based on evidence, not guessing |
| Routing | Determine complexity → choose workflow |
| Fix | Implement changes |
| Verification | Run tests + add regression tests |
| Prevention | Document fix in journal or plan |

### Phase 4 — Output and Completion

System delivers results:
- Completed code changes
- Detailed Markdown report (e.g., `brainstorm-date.md`)
- Summary of tests passed

**User intervention at "Approval Gates":**
- After planning, before code applied → user can approve or request changes
- After implementation, before commit → user can review

After brainstorming, system asks: "Hỏi: tạo plan? → /plan" (suggest next command)

Once user satisfied, `git-manager` hook handles commits + PR automatically.

## Decision tree (Speed vs Safety)

```
User has a feature request
    │
    ▼
Complex / risky? ──── Yes ──► /ck:plan ──► review plan.md ──► /ck:cook ──► review code ──► commit
    │
    No
    │
    ▼
/ck:cook directly ──► review + commit
```

When a bug shows up mid-development:
```
Error log produced ──► pipe to logs.txt ──► /ck:fix logs.txt
    │
    ▼
6-phase pipeline runs ──► review fix ──► verify regression tests ──► commit
```

## Where the user steers vs where ClaudeKit steers

| Activity | Driver |
|---|---|
| Command selection | **User** (Mnilax Rule 1: think before coding equivalent) |
| Speed/Safety trade-off | **User** (per-task discretion) |
| Permission triggers | **Hooks** (deterministic; user only intervenes when triggered) |
| Agent sequencing within Workflow | **System** (Workflow definition controls order) |
| Multi-step pipeline state | **System** (Hooks persist; user reads checkpoints) |
| Approval gates (plan / commit) | **User** (explicit confirmation required by default) |
| Git operations | **System via `git-manager` hook** (after user approval) |

This is **structured delegation** — the user makes high-level decisions (what to build, how safely); the system executes the procedural steps with checkpoints for user verification. Different from Lopopolo's "Dark Factory" (no human pre-merge review) and from default Claude Code (every step prompts user).

## How this differs from default Claude Code

| Default Claude Code | ClaudeKit |
|---|---|
| User prompts → Claude responds → ad-hoc iteration | User invokes command → Workflow → structured phases → output |
| State lives in conversation context | State lives in `.claude/session-state/` files (durable) |
| Tool use decided per-prompt | Tool use governed by Workflow definition |
| User reviews each step | User reviews at gates only |
| Multi-step plans drift across sessions | Plans persist in `.claude/plans/` files |

## How this differs from harness-engineering (Symphony)

Symphony (per [[external|harness-engineering/symphony-architecture]]):
- Polls Linear for issues — **work source is external issue tracker**
- Spawns agents in worktrees — **per-issue isolation**
- No human pre-merge review — **fully autonomous**
- Multi-agent: Codex + Aardvark working together

ClaudeKit:
- User invokes commands — **work source is user prompt**
- Single Claude Code session — **shared context**
- Approval gates at major steps — **human in the loop**
- Single-agent per command (multi-agent only via explicit `/ck:team`)

Scale difference: Symphony for teams; ClaudeKit for individuals. Both use 4-pillar separation but Symphony emphasizes orchestration-at-scale, ClaudeKit emphasizes structured-delegation-per-task.

## Key Takeaways

- **4-phase lifecycle:** Initiation → Hooks → Agent execution → Output gates
- **Hooks are deterministic** — they handle the "boring" parts (init, state, privacy) WITHOUT involving the model. Direct implementation of Mnilax Rule 5 (model for judgment only)
- **`/ck:fix` 6-phase pipeline** is the most-structured workflow — Scout/Diagnosis/Routing/Fix/Verification/Prevention. Borrowable pattern.
- **User steers high-level + reviews at gates; system steers procedural steps** — middle ground between bespoke Claude Code (every step prompts) and Lopopolo's Dark Factory (zero human review)
- **State persists in `.claude/session-state/`** — multi-step plans survive sessions, addressing Mnilax Rule 10 (checkpoint discipline) infrastructurally
