# (C) Cluster B — AGENTS.md-authoritative + 3-layer governance + ~2665 primitives

**Sources:**
- `AGENTS.md` (3,038 bytes — root developer guide)
- `CLAUDE.md` (440 bytes — redirect shim)
- `AGENT.md` (420 bytes — singular alias redirect shim)
- `.agents/AGENTS.md` (~18KB — user guide deployed to `~/.aidevops/agents/`)
- `.agents/` directory (1,792 .md + 873 .sh = ~2,665 agentic primitives)
- CONTRIBUTING.md / SECURITY.md / CODE_OF_CONDUCT.md / CHANGELOG.md / CREDITS.md

**Audience:** Contributors + AI assistants reading framework code

## CORPUS-FIRST inversion: AGENTS.md as authoritative + CLAUDE.md as shim

### `CLAUDE.md` (440 bytes — full content):

```markdown
# AI DevOps Framework - Claude Redirect

**See [AGENTS.md](AGENTS.md) for the authoritative AI assistant guidance.**

This file exists for compatibility with Claude Code and other Anthropic tools that look for `CLAUDE.md`.

All instructions, documentation, and operational guidance are maintained in **AGENTS.md** as the single source of truth.
```

### `AGENT.md` (420 bytes — full content):

```markdown
# AI DevOps Framework - Agent Redirect

**See [AGENTS.md](AGENTS.md) for the authoritative AI assistant guidance.**

This file exists for compatibility with AI tools that look for `AGENT.md` (singular).

All instructions, documentation, and operational guidance are maintained in **AGENTS.md** as the single source of truth.
```

### `AGENTS.md` (3,038 bytes — opening):

> "AI DevOps Framework - Developer Guide
>
> ## Quick Reference
> - User Guide: `.agents/AGENTS.md` (deployed to `~/.aidevops/agents/`)
> - Commands: `./setup.sh` (deploy) | `.agents/scripts/linters-local.sh` (quality) | `.agents/scripts/version-manager.sh release [major|minor|patch]`
> - Config: Runtime-specific (see `.agents/AGENTS.md` 'Runtime-Specific References')
> - Quality: `.agents/prompts/build.txt`
>
> File Structure: `TODO.md` (tasks), `todo/` (plans, PRDs), `.agents/` (agents, tools, services, workflows, scripts)."

**3-layer governance hierarchy NEW formulation extension proposed for Pattern #22 at next mini-audit:**

| Layer | File | Size | Audience | Purpose |
|---|---|---|---|---|
| **Layer 0** (shim) | `CLAUDE.md` + `AGENT.md` | 440B + 420B | Anthropic Claude Code + singular-AGENT.md tools | Compatibility redirect — single line points to AGENTS.md |
| **Layer 1** (dev-guide) | `AGENTS.md` (root) | 3,038B | Contributors + AI dev assistants | Quick-ref + Two-AGENTS.md model + dev lifecycle + design principles + security + quality workflow + self-assessment protocol |
| **Layer 2** (user-guide) | `.agents/AGENTS.md` | ~18,000B | End-users (deployed to `~/.aidevops/agents/AGENTS.md` by setup.sh) | Full operational guide: runtime support, task lifecycle, model tiers, git workflow, agent routing, memory recall, security |

**Key quote (verbatim from `AGENTS.md` line 21-28):**

> "## Two AGENTS.md Files
>
> | File | Purpose | Audience |
> |---|---|---|
> | `~/Git/aidevops/AGENTS.md` | Development guide | Contributors |
> | `~/Git/aidevops/.agents/AGENTS.md` | User guide | Users of aidevops |
>
> The `.agents/AGENTS.md` is copied to `~/.aidevops/agents/AGENTS.md` by `setup.sh`."

**Pattern #22 corpus state pre-v47:**
- All prior 46 corpus subjects had CLAUDE.md as **primary or co-equal** with AGENTS.md (when AGENTS.md existed at all)
- v32 claude-howto v32 first 3-scope CLAUDE.md variant system (project / directory / personal)
- v37 bizos: AGENTS.md 327B minimum-viable + CLAUDE.md 11B `@AGENTS.md` alias (smallest in corpus)

**v47 aidevops establishes corpus-first AGENTS.md-AUTHORITATIVE-WITH-CLAUDE.md-AS-SHIM inversion:**
- `CLAUDE.md` 440B = compatibility shim (vs bizos 11B alias — aidevops shim explains why)
- `AGENT.md` 420B = singular-variant compatibility shim (corpus-first triple-file pattern)
- Total 3 redirect-files (CLAUDE.md / AGENT.md / `.agents/AGENTS.md` deployed) all point to AGENTS.md
- Verbatim "single source of truth" framing

**Sub-variant within Pattern #22 proposed:** `agents-md-authoritative-with-claude-md-shim` (NEW; corpus-first at v47).

## `.agents/` primitive inventory (~2,665 + supplementary)

```
.agents/                          (38 entries top-level)
├── AGENTS.md                     (18KB user guide)
├── advisories/                   (security advisories)
├── aidevops/                     (architecture + setup + agent-sources docs)
├── aidevops.md                   (top-level aidevops agent file)
├── automate.md                   (automate domain agent)
├── bin/                          (binary helpers)
├── build-plus.md                 (Build+ default agent)
├── bundles/                      (7 project-type bundles: agent / cli-tool / content-site / infrastructure / library / schema / web-app)
├── business/                     (business domain subagents)
├── business.md                   (business domain agent)
├── commands/                     (22 commands: AGENTS.md + 13 aidevops-* domain prefix + 8 stand-alone)
├── configs/                      (60+ external service configs)
├── content/                      (content domain subagents)
├── content.md
├── custom/                       (user permanent private agents/scripts; survives updates)
├── health.md                     (health domain agent — corpus-first health agent at T1)
├── hooks/                        (11 git hooks: pre-push privacy/complexity/scope/dup-todo/credential-emission/canonical-on-main/gh-wrapper-guard/scope-guard + git_safety_guard.py + mcp_task_post_hook.py + task-id-collision-guard.sh)
├── legal.md                      (legal domain agent)
├── marketing-sales/              (marketing-sales subagents)
├── marketing-sales.md
├── plugins/                      (OpenCode plugin code: opencode-aidevops compaction plugin)
├── product/                      (product domain subagents)
├── product.md
├── prompts/                      (build.txt — primary system prompt, 80+KB)
├── reference/                    (extensive reference docs: agent-routing / auto-dispatch / auto-merge / customization / domain-index / dispatch-blockers / external-repo-submissions / large-file-split / memory-lookup / orchestration / parent-task-lifecycle / planning-detail / pre-dispatch-validators / pre-push-guards / repos-json-fields / reusable-workflows / routines / services / session / sync-pat-platforms / task-taxonomy / worker-diagnostics)
├── research.md
├── rules/                        (TTSR soft rule engine: e.g., no-edit-on-main, no-glob-for-discovery)
├── scripts/                      (873 helper shell scripts — CORPUS-RECORD)
├── seo/                          (60 SEO subagent files — Semrush + Ahrefs + DataForSEO + 40+ tools)
├── seo.md
├── services/                     (52 service integration definitions across 13 categories: accounting / analytics / communications / crm / database / document-processing / ecommerce / email / hosting / monitoring / networking / outreach / payments)
├── subagent-index.toon           (TOON-compressed routing table — 900+ agents by domain/purpose/dependency)
├── templates/                    (brief-template.md + workflow templates)
├── tests/                        (testing framework)
├── tools/                        (79 tool families across categories: ai-assistants / build-agent / build-mcp / mcp-toolkit / code-review / git / task-management / terminal / verification / video / voice / etc.)
└── workflows/                    (23 multi-step workflows: brief / full-loop / git-workflow / mission-orchestrator / pre-edit / etc.)
```

**Total agentic surface:**
- **1,792 markdown files** (instructions + agent definitions + subagent specs + tool docs + reference material)
- **873 shell scripts** (helpers + commands + hooks + automation)
- **= ~2,665 primitive files** before counting JSON configs / YAML / source code in `.opencode/` etc.

**Comparative corpus position:**

| Wiki | Primitive count | Tier |
|---|---|---|
| Standard wikis (e.g., codymaster v12 / claude-howto v32) | ~50-100 | GREEN |
| pi-mono v36 / DeepTutor v38 / bizos v37 / shannon v45 | ~120-200 | YELLOW |
| browser-use v41 / Ollama v46 | ~200-400 | RED |
| ruflo v42 | ~500+ | EXTREME (1st) |
| **aidevops v47** | **~2,665+** | **EXTREME (NEW CORPUS-RECORD; 5× ruflo)** |

## Top-level commands (22 in `.agents/commands/`)

```
AGENTS.md
aidevops-automate.md             (domain prefix)
aidevops-build-plus.md           (domain prefix)
aidevops-business.md             (domain prefix)
aidevops-content.md              (domain prefix)
aidevops-framework.md            (domain prefix)
aidevops-health.md               (domain prefix)
aidevops-legal.md                (domain prefix)
aidevops-marketing-sales.md      (domain prefix)
aidevops-product.md              (domain prefix)
aidevops-research.md             (domain prefix)
aidevops-seo.md                  (domain prefix)
aidevops.md                      (master)
automate.md
build-plus.md
business.md
content.md
health.md
legal.md
marketing-sales.md
product.md
research.md
seo.md
```

13 domain agents × 2 namespaces (`aidevops-` prefix + bare) = 22 entries + master `aidevops.md` + AGENTS.md user guide.

## Slash commands (69 documented)

Per `.agents/AGENTS.md` Quick Reference: "69 slash commands for common workflows" + per `.agents/scripts/commands/` discovery rule.

Resolution order (per `.agents/AGENTS.md` §"Slash Command Resolution"):
1. `scripts/commands/<command>.md` — standalone command docs (most)
2. `workflows/<command>.md` — workflow-based commands

Examples cited in AGENTS.md user guide:
- `/onboarding` — interactive setup wizard
- `/full-loop` — Ralph-loop iterative execution
- `/define`, `/new-task` — task creation
- `/mission` — multi-day autonomous project scoping
- `/runners` — batch dispatch
- `/cross-review` — multi-model parallel review with diff + judge
- `/route` — cost-aware model routing
- `/compare-models` (live) / `/compare-models-free` (offline)
- `/score-responses` — model output evaluation
- `/patterns` — pattern tracker
- `/recall`, `/remember` — memory operations
- `/setup-git` — per-repo git platform setup
- `/log-issue-aidevops` — issue filing with diagnostic gathering
- `/preflight` — workflow-based command
- `/pulse` — manual supervisor trigger
- `/release-issue <N>` — fallback issue release
- `/routine` — operational routine management
- `/tech-stack` — URL technology detection
- `/budget-analysis` — burn-rate review

(Not exhaustive; ~69 total.)

## Quality discipline (8 external platforms; corpus-record)

**Configuration files committed:**
- `.bandit` (Python security linting config)
- `.codacy.yml` (Codacy multi-tool analysis config)
- `.codefactor.yml` (CodeFactor grading config)
- `.coderabbit.yaml` (CodeRabbit AI review config — 5KB)
- `.markdownlint-cli2.jsonc` + `.markdownlint.json` (markdown linting)
- `.qlty/` directory (Qlty quality platform config)
- `.qltyignore` (Qlty exclusions)
- `.secretlintrc.json` + `.secretlintignore` (secretlint config)
- `.shellcheckrc` (ShellCheck config — 2.7KB)
- `sonar-project.properties` (SonarCloud config — 9KB)

**README badge stack (visible verification):**
- GitHub Actions Code Quality Analysis workflow
- SonarCloud Quality Gate
- CodeFactor grade
- Qlty maintainability
- Codacy Grade
- CodeRabbit AI Reviews
- License: MIT
- Copyright: Marcus Quinn 2025-2026

**Pre-push hooks (11 — installed via `install-pre-push-guards.sh install`):**
- `canonical-on-main-guard.sh`
- `complexity-regression-pre-push.sh`
- `credential-emission-pre-push.sh`
- `credential-transcript-scrub.py`
- `gh-wrapper-guard-pre-push.sh`
- `git_safety_guard.py` (Claude Code PreToolUse — blocks main/master edits)
- `mcp_task_post_hook.py`
- `pre-push-dup-todo-guard.sh`
- `privacy-guard-pre-push.sh` (blocks private repo slugs in public commits)
- `scope-guard-pre-push.sh` (blocks out-of-scope file changes per brief Files Scope)
- `task-id-collision-guard.sh`

**Bypass:** `git push --no-verify` (all) or per-hook flags (privacy / complexity / scope / dup-todo).

**CI-side gates:**
- **Qlty Regression Gate** — fails if PR introduces net increase in `qlty smells`
- **Qlty New-File Smell Gate** — fails if newly-added files ship with smells
- **Function-complexity gate** — >100 lines requires pre-planned refactor
- **Workflow Cascade Vulnerability Lint** — flags label-event + cancel-in-progress combinations
- **Task-ID collision check**
- **Parent-task keyword check** (For/Ref vs Closes)

**Governance counter-evidence to Pattern #12 v42 3-factor model:**
- aidevops = solo + 5.5-month-old + 212 stars (cold-start) + 8-tool external platform stack + 11 pre-push hooks + 6+ CI gates
- v42 3-factor predicts maturity-ambition+philosophy+scale; aidevops shows **maintainer-philosophy DOMINATES** (Marcus is Jersey UK senior dev with 8-year prior OSS track record)
- Maturity-ambition factor visible (3.11.0 in 5.5 months = production-ready ambition)
- Scale-tier factor MINIMAL (212 stars) — yet governance heaviest-per-bracket in corpus
- 4th counter-evidence wiki strengthening v42 refined formulation (claude-hud v35 / pi-mono v36 / ruflo v42 / aidevops v47)

## Self-improving + self-healing architecture

(README §"Self-Improving Agent System" + §"Pulse Supervisor")

**Self-healing (verbatim):** "When something breaks, diagnose the root cause, create tasks, and fix it. Every error is a live test case for a permanent solution."

**Self-improving phases:**
| Phase | Description |
|---|---|
| Review | Analyze memory for success/failure patterns (`memory-helper.sh`) |
| Refine | Generate and apply improvements to agents |
| Test | Validate in isolated OpenCode sessions |
| PR | Contribute to community with privacy filtering |

**Safety guardrails:**
- Worktree isolation for all changes
- Human approval required for PRs
- Mandatory privacy filter (secretlint + pattern redaction)
- Dry-run default, explicit opt-in for PR creation
- Audit log to memory

**Session mining (corpus-first explicit):** "extracts learnings from past sessions automatically" — converts conversational sessions into permanent learnings stored in memory (SQLite FTS5 + opt-in semantic search via `memory-helper.sh recall/store`).

## Memory system (3-layer; corpus-first explicit)

(`.agents/AGENTS.md` §"Memory Recall" + README §"Conversational Memory & Entity System")

| Layer | Storage | Purpose |
|---|---|---|
| **Layer 0** | Immutable raw log | All session transcripts preserved |
| **Layer 1** | Tactical summaries | Per-session digests + tone profile + idle detection |
| **Layer 2** | Strategic entity profiles | Versioned cross-channel relationship continuity (people / agents / services tracked across Matrix / SimpleX / email / CLI) |

**Entity memory** (`entity-helper.sh`) + **Conversational memory** (`conversation-helper.sh`) shared SQLite.

**Session databases:**
- OpenCode: `~/.local/share/opencode/opencode.db` (SQLite session + message tables)
- Claude Code: `~/.claude/projects/` (per-project JSONL transcripts)

**MANDATORY discipline (verbatim from `.agents/AGENTS.md` line 314-319):**

> "Run before any non-trivial task (code change, PR review, debugging, design):
>
> ```bash
> memory-helper.sh recall --query '<1-3 keywords>' --limit 5
> ```
>
> Store at session end: `memory-helper.sh store --content '<lesson>' --confidence high|medium|low`."

## Branch protection + worker autonomy

(`.agents/AGENTS.md` §"Auto-Dispatch and Completion" — extensive coverage)

**Default rule:** Workers NEVER edit TODO.md. Code changes need worktree + PR.

**Main-branch planning exception (headless sessions only):** TODO.md / `todo/*` / README.md may be committed direct to main by **headless workers** (pulse / CI / routines) — NOT interactive sessions.

**Worker triage responsibility:** Workers dispatched against auto-generated issue bodies are the triagers (3-outcome rule: falsify-and-close / implement-and-PR / escalate-with-recommendation).

**`origin:` label semantics (corpus-first explicit at T1):**
- `origin:worker` (headless dispatch via pulse)
- `origin:interactive` (user session)
- `origin:worker-takeover` (handover after idle interactive)
- Mutually exclusive; managed by `set_origin_label` from `shared-constants.sh`

**Auto-merge timing matrices:**
- `origin:interactive` from OWNER/MEMBER → 4-10 min after green CI
- `origin:worker` (worker-briefed) → 9-criterion checklist with cryptographic approval gate

**Cryptographic approval (corpus-first):** `sudo aidevops approve issue <number>` — SSH-signed approval comment. Workers cannot forge it (private key root-only). Setup once with `sudo aidevops approve setup`.

## Custom system prompt (`.agents/prompts/build.txt`)

**Verbatim from `.agents/AGENTS.md`:** "Based on upstream OpenCode with aidevops-specific overrides for tool preferences, professional objectivity, and per-model reinforcements for weaker models."

**Upstream prompt base:** `anomalyco/Claude` `anthropic.txt @ 3c41e4e8f12b` (CREDITS.md citation).

**Pattern #19 archetype 2 methodology-lineage observation:** aidevops cites BOTH **Lance Martin (LangChain)** for design patterns AND **anomalyco/Claude** for prompt template AND **mngr (imbue-ai)** for ratchet/review patterns. Multi-source methodology lineage.

## Cross-references

- **Pattern #22** AGENTS.md Industry Standard — 3-layer governance hierarchy formulation extension proposal NEW
- **Pattern #12** Governance-Depth refined v42 3-factor — counter-evidence N=4 strengthening
- **Pattern #18** Agent Runtime Standardization — per-agent MCP filtering + 7-tier model routing
- **Pattern #28** Multi-Provider AI Support — 4-provider auth pool (Anthropic / OpenAI / Cursor / Google) NEW data point
- **Pattern #57** Recursive Corpus Reference — 4th data point CREDITS.md cites VoltAgent v25 + Google Stitch v25

---

*(C) Generated by Claude — Cluster B summary for v47 aidevops*
