# (C) aidevops core product

**Entity type:** Product / framework
**Tier:** T1 Agent-as-assistant — 14th entrant + NEW sub-archetype "OpenCode-first cross-domain multi-agent AI-DevOps platform"
**Author:** Marcus Quinn (`marcusquinn`)
**License:** MIT
**Version:** v3.11.0 (2026-04-25)
**Founded:** 9 November 2025 (5.5 months old)

## What it is (one-line)

An **OpenCode plugin and AI operations platform** for launching and managing development, business, marketing, and creative projects via 13 specialist AI agents with autonomous orchestration.

## What it isn't

- Not a methodology framework (≠ spec-kit v17 SDD / BMAD v11 BMM / GSD v5)
- Not a single-agent assistant (≠ ECC v1 Claude Code feature catalog)
- Not a tutorial/aggregator (≠ claude-howto v32 / claude-code-best-practice v34)
- Not a display-layer plugin (≠ claude-hud v35)
- Not Claude-Code-primary (uniquely OpenCode-first)
- Not a multi-runtime balanced orchestrator (≠ OMC v27 4-way Claude/Codex/Gemini/Cursor)
- Not a single-flagship monorepo (≠ pi-mono v36 7-package monorepo under one flagship)
- Not a SaaS reseller (auth pool rotates user-owned subscriptions)

## What it solves (verbatim from README)

> "Beyond single-task AI. Most AI coding tools handle one conversation, one repo, one task at a time. aidevops manages your entire operation — dispatching parallel AI agents across multiple repos, routing tasks to domain-specialist agents, and running autonomously for days on multi-milestone projects."

## Core architectural pillars

### 1. 13 specialist domain agents

Functional-domain orchestrators (NOT personality-driven):

| # | Agent | Domain |
|---|---|---|
| 1 | Build+ (default) | Code: research/discuss/implement/fix; intent detection |
| 2 | Automate | Workflow automation, scheduled tasks, cron, launchd |
| 3 | SEO | Search-optimization (60 subagents + 40+ tools: Semrush / Ahrefs / DataForSEO) |
| 4 | Marketing-Sales | Marketing campaigns + sales pipeline |
| 5 | Content | Content + media + writing |
| 6 | Legal | Legal advisory framing |
| 7 | Sales | Pipeline (subset of Marketing-Sales in some configs) |
| 8 | Research | Research-deep workflows + citations |
| 9 | Video | Video creation (Remotion / HeyGen / Veo 3) |
| 10 | Business | Business operations advisory |
| 11 | Accounts | Bookkeeping (QuickFile MCP) |
| 12 | Social Media | Cross-platform posting |
| 13 | Health | Health advisory (corpus-first health agent at T1) |

Each agent: dedicated `.agents/<domain>.md` + per-domain subagent directory (e.g., `.agents/seo/` 60 files) + per-agent MCP filtering (~12-20 tools each, multi-layer-action-space pattern).

### 2. Autonomous Pulse Supervisor (CORPUS-FIRST architectural primitive)

**Runs every 2 minutes via launchd. There is no human at the terminal.**

Per-cycle 9-phase operations: capacity check / merge ready PRs / fix failing PRs / detect stuck work / dispatch workers / advance missions / triage quality / sync TODOs / kill stuck workers.

**Verbatim:** *"The pulse is an LLM, not a script. It reads issue bodies, assesses context, and uses judgment."*

Operational intelligence: struggle-ratio (`messages / max(1, commits)`) + circuit breaker + dynamic concurrency (RAM-based) + stale assignment recovery + priority ordering.

Manual trigger: `opencode run "/pulse"`.

Spec: `.agents/scripts/commands/pulse.md`.

### 3. Mission orchestration (multi-day autonomous projects)

`/mission "<high-level goal>"` → scoped into milestones + features + acceptance criteria → pulse dispatches workers, validates milestones, tracks budget, advances automatically.

**Two execution modes:**
- **Full** — Worktree + PR per feature (production)
- **POC** — Direct commits, skip ceremony (prototypes)

State tracked in committed JSON file → next pulse picks up from last state.

### 4. Multi-Model Verification (CORPUS-FIRST cross-provider safety)

**High-stakes operations verified by second AI model from different provider before execution.**

| Risk | Examples | Action |
|---|---|---|
| **Critical** | `git push --force` to main, `DROP DATABASE`, production deploy | Blocked unless second model agrees |
| **High** | Force push feature, data migration, secret exposure | Warned, verification recommended |
| **Medium** | Bulk file deletion, config changes | Logged |
| **Low** | Normal edits, test runs | No verification |

**Why cross-provider?** *"Same-provider models share training data and failure modes. A Claude hallucination is unlikely to be reproduced by Gemini or GPT, and vice versa."*

Cost: cheapest model tier (haiku-equivalent). Configuration: `.agents/reference/high-stakes-operations.md`.

**Pattern #28 NEW SUB-AXIS proposal:** verification-not-routing as cross-provider-safety mechanism. Distinct from prior #28 routing/abstraction data points.

### 5. Project Bundles (auto-configuration)

7 built-in bundles auto-detect project type → set model tier + quality gates + agent routing:
- `web-app` (sonnet, full lint/test/build/a11y)
- `library` (sonnet, full + API docs)
- `cli-tool` (sonnet, ShellCheck + test)
- `content-site` (haiku, Lighthouse + SEO)
- `infrastructure` (sonnet, ShellCheck + security scan)
- `agent` (opus, agent review + prompt quality)
- `schema` (sonnet, schema-specific)

Resolution: explicit > `.aidevops.json` > auto-detection from marker files.

### 6. Cost-aware 7-tier model routing

`local → haiku → flash → sonnet → pro → opus → grok`

Per-task complexity. CLI: `/route` + `model-routing.md` + `budget-tracker-helper.sh` (append-only cost log) + `/budget-analysis` (burn-rate review).

### 7. Auth pool (4-provider OAuth rotation)

| Provider | Auth | Subscription tier |
|---|---|---|
| Anthropic | OpenCode native OAuth | Claude Pro / Max |
| OpenAI | OAuth | ChatGPT Plus / Pro |
| Cursor | Local IDE state read + gRPC proxy | Cursor Pro |
| Google AI | OAuth ADC bearer token | Google AI Pro / Ultra / Workspace |

LRU rotation. Per-provider cooldowns. Auto-rotate on 429. Failure isolation (Google failure ≠ Anthropic failure).

CLI: `aidevops model-accounts-pool [add|status|check|rotate|reset-cooldowns|list]`.

### 8. 30+ external service integrations + 20 MCP servers

(See Cluster A summary for full enumeration.)

Per-agent MCP filtering: tools disabled globally, enabled per-agent → zero context overhead when unused. Bun-installed globally for ~0.1s startup vs 2-3s npx.

### 9. Self-healing + self-improving

| Phase | Action |
|---|---|
| Self-heal | Diagnose root cause → create tasks → fix. Every error = live test case. |
| Self-improve | Review memory patterns → refine agents → test in isolation → contribute via PR |

**Session mining:** extracts learnings from past sessions automatically (SQLite FTS5 + opt-in semantic search via `memory-helper.sh recall/store`).

### 10. Ralph loops + git worktree parallel agents

**Ralph loop** (Pattern #19 archetype 2 methodology-lineage data point) = iterative AI-development loop until complete. CLI: `/full-loop` + `full-loop-helper.sh`.

**Git worktree parallel:** Each agent works on its own branch in separate directory → no merge conflicts. `wt switch -c {type}/{name}`.

### 11. Voice Bridge (Apple Silicon ~6-8s round-trip)

`Mic → Silero VAD → Whisper MLX → OpenCode → Edge TTS → Speaker`

CLI: `voice-helper.sh talk`. Engines swappable. **Corpus-first explicit voice-input-to-AI-coding-agent at T1.**

### 12. Conversational memory + entity system (3-layer)

| Layer | Storage | Purpose |
|---|---|---|
| Layer 0 | Immutable raw log | All session transcripts |
| Layer 1 | Tactical summaries | Per-session digests |
| Layer 2 | Strategic entity profiles | Cross-channel relationship continuity |

Entity memory: people / agents / services tracked across Matrix / SimpleX / email / CLI with versioned profiles.

## Distribution (5 surfaces)

| Channel | Command | Notes |
|---|---|---|
| **npm** | `npm install -g aidevops && aidevops update` | Recommended; verified provenance |
| **Bun** | `bun install -g aidevops && aidevops update` | Fast alternative |
| **Homebrew** | `brew install marcusquinn/tap/aidevops && aidevops update` | macOS/Linux |
| **Direct (curl)** | `bash <(curl -fsSL https://aidevops.sh/install)` | aidevops.sh hosted installer |
| **Manual** | `git clone https://github.com/marcusquinn/aidevops.git ~/Git/aidevops && ~/Git/aidevops/setup.sh` | Source-based |

Setup script: clones/updates repo to `~/Git/aidevops` + deploys to `~/.aidevops/agents/` + installs `aidevops` CLI + configures AI assistants automatically + offers Oh My Zsh + Tabby/Zed/Git CLI guidance.

## Key CLI surface

```bash
aidevops status               # Check what's installed
aidevops doctor               # Detect duplicate installs + PATH conflicts
aidevops update               # Update framework + check registered projects
aidevops auto-update          # Manage update polling (every 10 min)
aidevops init [features]      # Initialize in any project
aidevops features             # List available features
aidevops repos                # List/add/remove registered projects
aidevops detect               # Scan for unregistered projects
aidevops upgrade-planning     # Upgrade TODO.md/PLANS.md to latest templates
aidevops update-tools         # Check + update installed tools
aidevops uninstall            # Remove

aidevops security             # ALL checks (posture/hygiene/supply chain)
aidevops security posture     # Interactive setup
aidevops security scan        # Secret + supply chain scan
aidevops security scan-pth    # Python .pth file audit (LiteLLM March 2026 IoC)

aidevops secret               # Manage secrets (gopass + AI-safe)
aidevops skill add/list/check/update/scan/remove   # Imported skills
aidevops sources add/list/sync   # Private agent repo sources
aidevops model-accounts-pool [add|status|rotate|reset-cooldowns]
aidevops approve issue <N>    # Cryptographic SSH-signed approval
aidevops upgrade-planning [--dry-run|--force]
aidevops check-workflows      # Detect drift in framework workflows
aidevops sync-workflows [--apply]   # Resync drifted workflows
aidevops detect               # Scan for unregistered aidevops projects
```

`aidevops init` features: `planning`, `git-workflow`, `code-quality`, `time-tracking`, `beads`.

## Quality gate stack (8 external platforms — corpus-record)

Configuration files committed at root: `.bandit` / `.codacy.yml` / `.codefactor.yml` / `.coderabbit.yaml` / `.markdownlint*.json*` / `.qlty/` / `.qltyignore` / `.secretlintrc.json` + `.secretlintignore` / `.shellcheckrc` / `sonar-project.properties`.

Pre-push hooks (11): canonical-on-main / complexity-regression / credential-emission / credential-transcript-scrub.py / gh-wrapper-guard / git_safety_guard.py / mcp_task_post_hook.py / pre-push-dup-todo / privacy-guard / scope-guard / task-id-collision.

CI gates: Qlty Regression / Qlty New-File Smell / Function-complexity / Workflow Cascade / Task-ID Collision / Parent-task Keyword.

## Primitive count: EXTREME (~2,665+; corpus-record)

| Primitive | Count |
|---|---|
| `.md` files in `.agents/` | **1,792** |
| `.sh` files in `.agents/` | **873** |
| Top-level `.agents/` entries | 38 |
| Specialist domain agents | 13 |
| Top-level `.agents/commands/` files | 22 |
| `.agents/workflows/` workflows | 23 |
| `.agents/tools/` tool families | 79 |
| `.agents/services/` service integrations | 52 |
| `.agents/bundles/` bundles | 7 |
| `.agents/hooks/` git hooks | 11 |
| External service integrations | 30+ |
| MCP integrations | 20 |
| Imported skills | 6+ |
| Quality gate platforms (external) | 8 |
| Top-level governance files | 12+ (README/AGENTS/AGENT/CLAUDE/LICENSE/CONTRIBUTING/SECURITY/CODE_OF_CONDUCT/CHANGELOG/CREDITS/TODO/TERMS/MODELS/MODELS-PERFORMANCE/VERSION/.gitignore/.gitattributes/+8 quality configs) |
| Slash commands | ~69 |

**Total: ~2,665+ agentic primitives. NEW CORPUS-RECORD (5× ruflo v42 ~500+).**

## Pattern Library impact summary

| Pattern | Action | Notes |
|---|---|---|
| **#18** Agent Runtime Standardization | Strengthening + sub-observation | OpenCode-as-primary T1 plugin (CORPUS-FIRST); per-agent MCP filtering 12-20 tools |
| **#19** Intellectual Lineage archetype 2 | Strengthening | Lance Martin (LangChain) 4th individual-influence-node + multi-source methodology lineage strongest-evidence wiki |
| **#22** AGENTS.md Industry Standard | Formulation extension proposal | 3-layer governance hierarchy (CLAUDE.md+AGENT.md shims → root AGENTS.md dev-guide → `.agents/AGENTS.md` user-guide) NEW; AGENTS.md-authoritative-with-CLAUDE.md-shim sub-variant CORPUS-FIRST |
| **#28** Multi-Provider AI Support | Formulation extension proposal | Cross-provider VERIFICATION-not-routing as safety axis NEW; 4-provider OAuth pool data point |
| **#57** Recursive Corpus Reference | 4th data point | CREDITS.md cites VoltAgent v25 + Google Stitch v25 referenced; base rate 4/47 = 8.5% |
| **#17** Ecosystem-Layer variant 1 | Strengthening | 18th data point (Marcus 20-repo solo-multi-publisher) |
| **#20** Solo-Scale Ceiling | NEW T1 row | "Cold-start-with-mature-framework-surface (212 / 5.5mo)" |
| **#29** MIT | Strengthening | 39th MIT observation |
| **#12** Governance-Depth refined v42 3-factor | Strengthening | 4th counter-evidence wiki (philosophy-dominates) |
| **#51** Vibe-Coding Spectrum | Confirmed strengthening | Anti-vibe-pole structural-discipline data point |
| **#2** Distribution Evolution | Strengthening | 5-surface npm/Bun/Homebrew/curl/manual |
| **#27** Community-Viral Scale Path | Counter-evidence observational | Cold-start-mature-surface; not viral |

**0 new active candidates. 0 new OBSERVATION-TRACKs. 11-streak zero-registration achieved.**

## Cross-references

- See **(C) Cluster A — README + 13-domain coverage + autonomous supervisor**
- See **(C) Cluster B — AGENTS.md-authoritative + 3-layer governance + ~2665 primitives**
- See **(C) Cluster C — Marcus Quinn ecosystem + OpenCode-first + commercial positioning**
- See **(C) T1 14-way + OpenCode-first sub-archetype + Pattern implications**
- See **(C) Storm Bear meta-entity v47 — 36th consecutive**

---

*(C) Generated by Claude — Core product entity for v47 aidevops*
