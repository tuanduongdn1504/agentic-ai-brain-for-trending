# (C) README Summary

> **Source:** `00 Sources/get-shit-done/README.md` (927 lines, ~50KB) — **skim-first** (read foundational sections 1-475 + commands section)
> **Ingested:** 2026-04-18
> **Routine context:** Source #1 of 3 cho GSD project (Phase 2, 5th auto-execution)

---

## TL;DR

**VI:** GSD (Get Shit Done) là **"meta-prompting, context engineering and spec-driven development system"** cho 14+ AI coding harnesses. **Core positioning UNIQUE:** "Solves context rot — the quality degradation that happens as Claude fills its context window." Distribution qua npm (`npx get-shit-done-cc@latest`), **$GSD Solana token** + `@gsd_foundation`. **Largest scope của 4 Tier 1 frameworks:** 33 agents + 83 commands + 11 hooks. Author TÂCHES identifies as "solo developer who doesn't write code."

**EN:** GSD is meta-prompting + context engineering + spec-driven development for 14+ harnesses. Unique positioning: "Solves context rot." npm distribution + Solana token backing. Largest scope of Tier 1 frameworks (33 agents + 83 commands + 11 hooks).

---

## Core problem statement (distinctive)

> "Solves **context rot** — the quality degradation that happens as Claude fills its context window."

**Rest of Tier 1 frameworks don't explicitly name this problem:**
- ECC: "production-ready agent infrastructure"
- Superpowers: "discipline + methodology"
- gstack: "virtual engineering team"
- **GSD: "context rot solution"** ← narrowest, most specific

→ **Laser-focused positioning.** Unique vs siblings.

---

## 5-step workflow (core mechanism)

```
1. /gsd-new-project       → Questions → Research → Requirements → Roadmap
2. /gsd-discuss-phase N   → Capture preferences (CONTEXT.md)
3. /gsd-plan-phase N      → Research + atomic XML plans + verify
4. /gsd-execute-phase N   → Wave-based parallel execution, fresh 200k context per plan
5. /gsd-verify-work N     → Manual UAT + auto-diagnose failures
         ↓
   /gsd-ship N           → PR
   /gsd-complete-milestone → Archive + tag
   /gsd-new-milestone    → Next version
```

**Or:** `/gsd-next` auto-detects state + runs next step.

**Quick mode:** `/gsd-quick` cho ad-hoc tasks, composable flags (`--discuss`, `--research`, `--validate`, `--full`).

---

## 14 harnesses supported (most of any framework)

| Harness | Install flag | Install path |
|---------|--------------|-------------|
| Claude Code | `--claude` | `~/.claude/` or `./.claude/` |
| OpenCode | `--opencode` | `~/.config/opencode/` |
| Gemini CLI | `--gemini` | `~/.gemini/` |
| Kilo | `--kilo` | `~/.config/kilo/` or `./.kilo/` |
| Codex | `--codex` | `~/.codex/` or `./.codex/` |
| Copilot | `--copilot` | `~/.github/` or `./.github/` |
| Cursor CLI | `--cursor` | `~/.cursor/` or `./.cursor/` |
| Windsurf | `--windsurf` | `~/.codeium/windsurf/` or `./.windsurf/` |
| Antigravity | `--antigravity` | `~/.gemini/antigravity/` or `./.agent/` |
| Augment | `--augment` | `~/.augment/` or `./.augment/` |
| Trae | `--trae` | `~/.trae/` or `./.trae/` |
| Qwen Code | `--qwen` | `~/.qwen/` or `./.qwen/` |
| CodeBuddy | `--codebuddy` | `~/.codebuddy/` or `./.codebuddy/` |
| Cline | `--cline` | `~/.cline/` or `./.clinerules` |

**Plus:** `--all` cài tất cả một lần.

→ **14 harnesses** > gstack 10 > Superpowers 7 > ECC 5 > goclaw N/A (platform tier).

---

## Why It Works (4 mechanisms)

### 1. Context engineering (file structure)

| File | Purpose |
|------|---------|
| `PROJECT.md` | Vision, always loaded |
| `research/` | Ecosystem knowledge (stack/features/arch/pitfalls) |
| `REQUIREMENTS.md` | Scoped v1/v2 với phase traceability |
| `ROADMAP.md` | Where you're going |
| `STATE.md` | Decisions, blockers, position — cross-session memory |
| `PLAN.md` | Atomic task với XML structure, verification steps |
| `SUMMARY.md` | What happened, committed |
| `todos/`, `threads/`, `seeds/` | Captured ideas, persistent threads, forward-looking |

**"Size limits based on where Claude's quality degrades."**

### 2. XML prompt formatting

Every plan = structured XML optimized for Claude:
```xml
<task type="auto">
  <name>Create login endpoint</name>
  <files>src/app/api/auth/login/route.ts</files>
  <action>Use jose for JWT (not jsonwebtoken - CommonJS issues)...</action>
  <verify>curl -X POST ... returns 200 + Set-Cookie</verify>
  <done>Valid credentials return cookie, invalid return 401</done>
</task>
```

→ **"Precise instructions. No guessing. Verification built in."**

### 3. Multi-agent orchestration (thin orchestrators pattern)

| Stage | Orchestrator | Agents |
|-------|--------------|--------|
| Research | Coordinates, presents | **4 parallel researchers** (stack/features/arch/pitfalls) |
| Planning | Validates, manages iter | Planner + checker loop until pass |
| Execution | Groups into waves | Executors implement parallel, **fresh 200k context each** |
| Verification | Presents, routes | Verifier + debuggers |

> "The orchestrator never does heavy lifting. It spawns agents, waits, integrates results."

**Result:** "Entire phase runs... your main context window stays at 30-40%. Work happens in fresh subagent contexts."

→ **Match gstack's Conductor philosophy** (subagents fresh context) + Superpowers's SDD.

### 4. Atomic git commits

Each task = own commit immediately after completion.

```
abc123f docs(08-02): complete user registration plan
def456g feat(08-02): add email confirmation flow
```

> "Git bisect finds exact failing task. Each task independently revertable."

**Match:** gstack's "Always bisect commits" convention.

---

## Wave execution (parallel task grouping)

```
WAVE 1 (parallel)   →   WAVE 2 (parallel)   →   WAVE 3
Plan 01 | Plan 02       Plan 03 | Plan 04       Plan 05
User    | Product       Orders  | Cart          Checkout
Model   | Model         API     | API           UI
```

**Rules:**
- Independent plans → same wave → parallel
- Dependent plans → later wave → wait for deps
- File conflicts → sequential or same plan

**"Vertical slices" parallelize better than "horizontal layers"** — interesting insight for plan decomposition.

→ **Novel mechanism cho atomic task orchestration.** Most explicit of 4 Tier 1 frameworks.

---

## Author: TÂCHES voice

**"I'm a solo developer. I don't write code — Claude Code does."**

Quote worth preserving:

> "Other spec-driven development tools exist; BMAD, Speckit... But they all seem to make things way more complicated than they need to be (sprint ceremonies, story points, stakeholder syncs, retrospectives, Jira workflows) or lack real big picture understanding of what you're building. I'm not a 50-person software company. I don't want to play enterprise theater. I'm just a creative person trying to build great things that work."
>
> "So I built GSD. The complexity is in the system, not in your workflow."
>
> "That's what this is. No enterprise roleplay bullshit. Just an incredibly effective system for building cool stuff consistently using Claude Code."
>
> — **TÂCHES**

**Target audience:** "People who want to describe what they want and have it built correctly — without pretending they're running a 50-person engineering org."

→ **Anti-enterprise-theater positioning.** Similar attitude to gstack's founder-voice, but different framing (solo creator vs YC CEO).

---

## Built-in quality gates

README mentions:
- Schema drift detection (flags ORM changes missing migrations)
- Security enforcement anchored to threat models
- Scope reduction detection (prevents planner silently dropping requirements)

→ **Defensive discipline built-in.** Match Superpowers's discipline ethos.

---

## Distribution model: npm-first

**One command install:** `npx get-shit-done-cc@latest`

**Non-interactive:** `--claude --global` or `--all --global` etc.

**"Recommended: Skip Permissions Mode":**
```bash
claude --dangerously-skip-permissions
```

> "This is how GSD is intended to be used — stopping to approve `date` and `git commit` 50 times defeats the purpose."

**Alternative:** Granular permissions list trong `.claude/settings.json`.

→ **Friction-low design.** Assume user wants full automation.

---

## Commands: 83 trong `commands/gsd/` + core sections

**Core workflow (13 commands):** new-project, discuss-phase, plan-phase, execute-phase, verify-work, ship, next, fast, audit-milestone, complete-milestone, new-milestone, forensics, milestone-summary

**Workstreams (5):** list/create/switch/complete/status — parallel milestone work

**Multi-project workspaces (3):** new/list/remove — isolated worktrees

**Spiking & Sketching (4):** spike, sketch, spike-wrap-up, sketch-wrap-up — **throwaway experiments before planning**

**UI Design (2):** ui-phase (design contract), ui-review (6-pillar audit)

**Navigation (5):** progress, next, help, update, join-discord, manager

**Brownfield (1):** map-codebase — for existing codebases

**Phase Management (5):** add/insert/remove-phase, list-phase-assumptions, plan-milestone-gaps

**Session (3):** pause-work, resume-work, session-report

**Code Quality (5):** review, secure-phase, pr-branch, audit-uat, docs-update

**Backlog & Threads (4):** plant-seed (forward-looking ideas), add-backlog (999.x parking), review-backlog, thread (cross-session)

**Utilities (10+):** settings, set-profile, add-todo, check-todos, debug, do, note, quick, health, stats, profile-user

→ **Most commands của Tier 1** (GSD 83 > gstack 31 (23 specialists + 8 tools) > Superpowers 14 skills > ECC 79 commands).

---

## 33 Specialized Agents (folder) — docs/AGENTS.md claims 21

Folder `agents/gsd-*`:
- Researchers: 3 (project, phase, ui)
- Analyzers: 2 (assumptions, advisor)
- Synthesizers: 1 (research-synthesizer)
- Planners: 1 (planner)
- Roadmappers: 1 (roadmapper)
- Executors: 1 (executor)
- Checkers: 3 (plan, integration, ui)
- Verifiers: 1 (verifier)
- Auditors: 3 (nyquist, ui, security)
- Mappers: 1 (codebase-mapper)
- Debuggers: 1 (debugger)
- Doc Writers: 2 (doc-writer, doc-verifier)
- Profilers: 1 (user-profiler)
- **Plus 12 more** in folder but not listed in docs (framework-selector, domain-researcher, code-fixer, code-reviewer, eval-auditor, eval-planner, intel-updater, pattern-mapper, doc-classifier, doc-synthesizer, debug-session-manager, ai-researcher, nyquist-auditor) — **folder/docs discrepancy**

→ **33 > docs/AGENTS.md's 21.** Possibly docs lag behind code.

---

## 11 Hooks

`hooks/` folder:
- `gsd-check-update.js` + worker
- `gsd-context-monitor.js` — **context rot detection!**
- `gsd-phase-boundary.sh`
- `gsd-prompt-guard.js`
- `gsd-read-guard.js`
- `gsd-read-injection-scanner.js` — **prompt injection detection**
- `gsd-session-state.sh`
- `gsd-statusline.js`
- `gsd-validate-commit.sh`
- `gsd-workflow-guard.js`

→ **Hook philosophy = blocking + detection.** Match gstack's `/careful` + Superpowers's HARD-GATE patterns.

---

## $GSD Solana token + gsd_foundation

**Unique của 5 projects:** crypto token backing.

- Token: `$GSD` on Solana
- Foundation: `@gsd_foundation` (X/Twitter)
- Discord community
- Dexscreener link embedded in README badges

→ **First of 5 projects với crypto backing.** Funding model distinctive.

**Implications:**
- Potential commercial stake (token holders = investors?)
- Community incentive mechanism
- Unclear how token relates to framework features

**TODO:** Investigate token tokenomics (not source-verified this session).

---

## Trusted by claim

> "Trusted by engineers at Amazon, Google, Shopify, and Webflow."

Plus 3 testimonials quoted:
- "If you know clearly what you want, this WILL build it for you. No bs."
- "I've done SpecKit, OpenSpec and Taskmaster — this has produced the best results for me."
- "By far the most powerful addition to my Claude Code. Nothing over-engineered. Literally just gets shit done."

→ **Social proof-heavy.** More than gstack's Karpathy+OpenClaw citations.

---

## Cross-connection to sibling projects

| Aspect | ECC | Superpowers | gstack | goclaw | **GSD** |
|--------|-----|-------------|--------|--------|---------|
| Tier | 1 (assistant) | 1 | 1 | 2 (service) | **1** |
| Core framing | Perf optimization | Methodology | Virtual team | Platform | **Context rot solution** |
| Scope | 185+48+79 | 14+1 | 23+8+1 | 23+1+7 channels | **33+83+11** |
| Harnesses | 5 | 7 | 10 | N/A (self-hosted) | **14** |
| Distribution | plugin+manual | marketplace+git | npm+git+setup | Docker+binary | **npm only** |
| Language | JS/TS | JS/TS | TS (Bun) | Go | **TypeScript + Vitest** |
| License | MIT | MIT | MIT | CC BY-NC 4.0 | **MIT** |
| Token/commercial | Plugin + paid products | None | YC recruiting | CC BY-NC | **$GSD Solana token** |
| VN support | ❌ | ❌ | ❌ | ✅ Zalo+VI | ❌ (4 langs, no VN) |

→ **GSD slot in Tier 1:** largest scope, most harnesses, narrowest problem framing, only với crypto token.

---

## Open questions resolved

- ✅ Q1: Context rot = "quality degradation as Claude fills context window" — file structure + wave execution + fresh 200k contexts address it
- ✅ Q4: 14 harnesses — same symlink/install pattern, but via npm not setup script
- ✅ Q10: Thin orchestrators spawn agents fresh context — convergent với gstack + Superpowers SDD

## Open questions raised

- ⏸ $GSD token tokenomics — commercial implications for users?
- ⏸ 33 folder vs 21 docs agent count — canonical source?
- ⏸ `docs/superpowers/specs/` folder — GSD integrates với obra/superpowers?
- ⏸ TypeScript SDK usability standalone?
- ⏸ 83 commands — maintenance burden? Compare với 79 ECC commands deprecated

---

## Cross-references

- [[(C) USER-GUIDE summary]]
- [[(C) ARCHITECTURE + CHANGELOG summary]]
- [[(C) index]]
- [[(C) log]]
- Cross-project: all 3 Tier 1 sibling README summaries
- Cross-project: goclaw summary (Tier 2 contrast)

## Citations

- `README.md` lines 1-475 (sections Why I Built, Getting Started, How It Works, Why It Works)
- `README.md` lines 558-690 (Commands reference)
- `docs/AGENTS.md` (21 agent overview, lines 1-40)
- Folder listings: `agents/` (33 files), `commands/gsd/` (83 files), `hooks/` (11 files)
