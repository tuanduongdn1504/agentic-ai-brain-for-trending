# (C) Entity 1 — gsd-2 Core Product

## What it is

**gsd-2** = standalone TypeScript CLI coding agent built on the Pi SDK. Reads `.gsd/` directory state from disk, dispatches work to LLM in fresh context windows per task, advances autonomously through milestones with crash recovery / cost tracking / verification.

**One-line value proposition** (verbatim README): *"One command. Walk away. Come back to a built project with clean git history."*

## Tier classification

**T1 Agent-as-assistant — 15TH T1 entrant** (largest tier in corpus extends from N=14 post-v53). 15 T1 entrants now: ECC v1 / Superpowers v2 / gstack v3 / GSD-1 v5 / BMAD v11 / codymaster v12 / spec-kit v17 / agency-agents v18 / OMC v27 / claude-howto v32 / claude-code-best-practice v34 / claude-hud v35 / pi-mono v36 / aidevops v47 / vercel-labs v51 / oh-my-openagent v52 / **gsd-2 v54**.

(Note: counting may show 16 — vercel-labs v51 was 15th and oh-my-openagent v52 was 16th. gsd-2 v54 is **17th T1 in absolute count**. Brief said "extends to N=15" — this may have been miscounted in the brief. Honest verdict: gsd-2 extends T1 to N=17 if all prior T1 wikis are counted; brief stated N=15 which may have been provisional. Documenting discrepancy for operator review.)

**Sub-archetype**: **org-led successor-of-viral-flagship + Pi-SDK-vendoring + multi-component-with-cloud-tier-emergent**. Distinct from prior T1 sub-archetypes:
- Not solo (gsd-build org with at least 2 attributed maintainers across GSD-1+GSD-2 if TÂCHES≠Lex)
- Not corporate-official (gsd-build = independent org, not Microsoft/GitHub/Google)
- Not aggregator (claude-code-best-practice / claude-howto curate; gsd-2 BUILDS)
- Not single-purpose plugin (claude-hud display-layer)
- Not multi-runtime-orchestration (OMC v27 / oh-my-openagent v52)
- Not OpenCode-first (aidevops v47)

## 12-axis classification

| Axis | Value |
|------|------|
| Tier | T1 — 15th–17th entrant (count uncertainty per brief) |
| Archetype | Org-led + planned-successor-of-viral-flagship + Pi-SDK-vendoring |
| Scale tier | Cold-start-rapid-growth (6.6K / 46 days = 144 stars/day) |
| Primary lang | TypeScript ~95% + Rust (`@gsd/native`) |
| Packaging | npm `gsd-pi` + Dockerfile + managed RTK binary + 8 workspaces |
| Origin | Successor-of-viral-flagship (GSD-1 grew 8K→57.4K post-v5; gsd-2 = explicit planned successor) |
| Methodology | SDD continued + meta-prompting + context engineering + extension-first + state-machine-from-disk |
| Governance | Light at root (4 files only; NO AGENTS.md / CLAUDE.md / SECURITY / COC) + heavy contributor process via CONTRIBUTING + ADRs |
| Primitive count | YELLOW (~150-250) |
| i18n | EN + zh-CN docs/ subdirectory |
| Lineage | Pi SDK vendored from pi-mono v36 (4 of 7 packages) + GSD-1 self-lineage |
| Agent platforms | Standalone CLI primary + MCP server companion + 24 bundled extensions + OpenClaw-skill compatibility |

## What it does (core capabilities)

### Hierarchical work model
```
Milestone (4-10 slices) → Slice (1-7 tasks) → Task (1 context window)
```
**Iron rule**: a task must fit in one context window. If it can't, it's two tasks.

### Two execution modes
| Mode | Command | Use case |
|---|---|---|
| **Step** | `/gsd` or `/gsd next` | Pause-between-units wizard; on-ramp |
| **Auto** | `/gsd auto` | State-machine-driven autonomous; the highway |

### Auto mode pipeline (12 numbered guarantees per README)
1. **Fresh session per unit** — Every task/research/planning step gets clean 200k-token context
2. **Context pre-loading** — Dispatch prompt includes inlined task plans + slice plans + prior task summaries + dependency summaries + roadmap excerpts + decisions register
3. **Git isolation** — `git.isolation: worktree | branch | none` per milestone; squash-merge to main on completion
4. **Crash recovery** — Lock file tracks current unit; survives session death via session forensics + parallel orchestrator state persistence with PID liveness detection; headless mode auto-restart with exponential backoff (default 3 attempts)
5. **Provider error recovery** — Transient errors (rate limits, 500/503, overloaded) auto-resume; permanent errors (auth, billing) pause for review; fallback chain retries transient before model-switching
6. **Stuck and artifact detection** — Sliding-window detector identifies repeated dispatch patterns + multi-unit cycles; missing-artifact path uses bounded retries (3 max) before pausing
7. **Timeout supervision** — Soft timeout warns LLM to wrap up; idle watchdog detects stalls; hard timeout pauses
8. **Cost tracking** — Per-unit token usage + cost captured by phase/slice/model; budget ceilings can pause auto mode
9. **Adaptive replanning** — After each slice completes, roadmap is reassessed; slices reordered/added/removed
10. **Verification enforcement** — `verification_commands` (lint/test) auto-run after task; auto-fix retries on failure
11. **Milestone validation** — `validate-milestone` gate compares roadmap success criteria vs actual results before sealing
12. **Escape hatch** — Press Escape to pause; conversation preserved; resume via `/gsd auto`

### Context engineering artifacts on disk

12 named artifacts in `.gsd/` directory (see `(C) Cluster 2` for full list). Source-of-truth = disk; in-memory state does not survive cross-sessions.

### Git strategy
- Branch-per-slice with squash merge
- Sequential commits within slice
- One squash commit per milestone on main
- Worktree torn down after merge
- Git bisect works
- Individual milestones revertable
- Commit messages auto-generated from task summaries

### HTML reports
- Self-contained HTML reports in `.gsd/reports/` after milestone completion
- Per-report sections: project summary + progress tree + slice dependency graph (SVG DAG) + cost/token metrics with bar charts + execution timeline + changelog + knowledge base
- Auto-generated `index.html` shows all reports with progression metrics
- No external dependencies (CSS + JS inlined; printable to PDF)

### Headless mode (CI / cron / scripts)
```bash
gsd headless --timeout 600000               # Run auto mode in CI
gsd headless new-milestone --context spec.md --auto  # Full milestone from spec
gsd headless next                            # One unit at a time (cron-friendly)
gsd headless query                           # Instant JSON snapshot, no LLM, ~50ms
gsd headless dispatch plan                   # Force a specific pipeline phase
```
Exit codes: `0` complete / `1` error/timeout / `2` blocked. Auto-restart on crash with exponential backoff.

### Multi-session orchestration
File-based IPC in `.gsd/parallel/` for coordinating multiple GSD workers across milestones. Build orchestrators that spawn/monitor/budget-cap a fleet of GSD workers.

### Two-terminals workflow (recommended)
- Terminal 1: `gsd` → `/gsd auto` (let it build)
- Terminal 2: `gsd` → `/gsd discuss` (steer architecture) / `/gsd status` (check progress) / `/gsd queue` (queue next milestone)

Both terminals read+write same `.gsd/` files. Decisions in terminal 2 picked up at next phase boundary — no need to stop auto mode.

## Provider support

**20+ built-in providers** via Pi SDK: Anthropic / Anthropic Vertex AI / OpenAI / Google Gemini / OpenRouter / GitHub Copilot / Amazon Bedrock / Azure OpenAI / Google Vertex / Groq / Cerebras / Mistral / xAI / HuggingFace / Vercel AI Gateway + more.

**OAuth / Max plans**: Claude Max + Codex + GitHub Copilot via Pi OAuth flow (no API key needed). README has **explicit ⚠️ ToS warning** for Google Gemini OAuth (resulted in account suspensions; use Gemini API key instead).

**Per-phase model selection** (verbatim YAML):
```yaml
models:
  research: openrouter/deepseek/deepseek-r1
  planning:
    model: claude-opus-4-7
    fallbacks:
      - openrouter/z-ai/glm-5
  execution: claude-sonnet-4-6
  completion: claude-sonnet-4-6
```

## Token optimization (cost discipline)

`token_profile: budget | balanced | quality` single preference coordinates 3 mechanisms:
- **Profile selection** — `budget` (40-60% savings) / `balanced` (10-20%, default) / `quality` (0%)
- **Complexity-based routing** — heuristic classifier (sub-millisecond, no LLM calls) routes simple/standard/complex tasks to appropriate model tiers
- **Budget pressure** — graduated downgrading at 50% / 75% / 90% of budget ceiling

## 30+ slash commands

| Command | What it does |
|---|---|
| `/gsd` | Step mode (default) |
| `/gsd next` | Explicit step mode |
| `/gsd auto` | Autonomous mode |
| `/gsd quick` | Skip planning overhead |
| `/gsd stop` | Stop auto mode gracefully |
| `/gsd steer` | Hard-steer plan documents during execution |
| `/gsd discuss` | Discuss architecture (works alongside auto mode) |
| `/gsd rethink` | Conversational project reorganization |
| `/gsd mcp` | MCP server status |
| `/gsd status` | Progress dashboard |
| `/gsd queue` | Queue future milestones |
| `/gsd prefs` | Model selection / timeouts / budget |
| `/gsd migrate` | Migrate v1 `.planning` → `.gsd` |
| `/gsd help` | Categorized command reference |
| `/gsd mode` | Switch solo/team workflow mode |
| `/gsd workflow` | List/run/install/info/validate workflow plugins |
| `/gsd start <template>` | Launch bundled workflow template (bugfix, release, etc.) |
| `/gsd forensics` | Full-access auto-mode debugger |
| `/gsd cleanup` | Archive completed milestones |
| `/gsd doctor` | Runtime health checks |
| `/gsd keys` | API key manager (list/add/remove/test/rotate/doctor) |
| `/gsd logs` | Browse activity/debug/metrics logs |
| `/gsd export --html` | Generate HTML report |
| `/worktree` (`/wt`) | Git worktree lifecycle |
| `/voice` | Toggle real-time speech-to-text |
| `/exit` / `/kill` / `/clear` | Session control |
| `Ctrl+Alt+G` | Toggle dashboard overlay |
| `Ctrl+Alt+V` | Toggle voice transcription |
| `Ctrl+Alt+B` | Show background shell processes |
| `gsd config` / `gsd update` / `gsd headless` / `gsd --continue` (`-c`) / `gsd --worktree` (`-w`) / `gsd sessions` | Top-level commands |

## Bundled extensions (24)

See `(C) Cluster 3` for full table. Highlights:
- **Browser Tools** — Playwright + form intelligence + intent-ranked element finding + visual diffing + prompt injection detection
- **MCP Client** — Native `@modelcontextprotocol/sdk` integration
- **Voice** — macOS + Linux real-time STT
- **Universal Config** — Discovers MCP servers + rules from other AI coding tools
- **GitHub Sync** — Auto-sync milestones to GitHub Issues/PRs/Milestones
- **TTSR** — Tool-triggered system rules (conditional context injection based on tool usage)

## Bundled agents (13 specialist subagents on disk)

`debugger / doc-writer / git-ops / javascript-pro / planner / refactorer / researcher / reviewer / scout / security / tester / typescript-pro / worker`

(README cites only 5; documentation drift between README and disk reality.)

## 35 skills

Bundled in `src/resources/skills/`. Mix of methodology (TDD / decompose-into-slices / write-milestone-brief) + tooling (lint / test / forensics) + frontend (frontend-design / react-best-practices / accessibility / core-web-vitals) + meta (create-skill / create-gsd-extension / create-mcp-server / create-workflow).

## Distribution

- **npm**: `npm install -g gsd-pi` (single-name; bin aliases gsd / gsd-cli / gsd-pi)
- **Docker**: `Dockerfile` at root + `docker/` directory with sandbox config
- **VS Code Extension**: `vscode-extension/` workspace (chat participant + sidebar)
- **Studio Electron desktop**: `studio/` workspace (private v0.0.0)
- **Web UI**: `web/` workspace (browser-based project management)
- **Managed RTK binary**: auto-provisioned for shell-output compression on macOS/Linux/Windows

## Engines

`Node >= 22.0.0` (Node 24 LTS recommended). README has special guide for Homebrew users to pin LTS instead of dev releases.

## Cross-references

- See `(C) Cluster 1-3` for source detail
- See `(C) Entity 2` for gsd-build ecosystem + GSD-1 successor relationship
- See `(C) Entity 3` for Pi SDK cross-corpus deep-dive
- See `(C) Entity 4` for Storm Bear meta-entity
