# Archon workflow primitives — the YAML schema ground truth

> Companion to [[archon-harness-builder-anchor]]. Source = the repo's own agent-facing skill references (`.claude/skills/archon/references/` — workflow-dag.md, parameter-matrix.md, variables.md, dag-advanced.md, good-practices.md), read via dive agent + main-loop SKILL.md full read. This is the **operational** article: everything a pilot needs to author a workflow.

## Source

- `.claude/skills/archon/SKILL.md` (15.9K chars, read in full in main loop) + references (~90K chars, dive `wf_8a0f2da5-1d0`)
- Canonical docs: https://archon.diy/guides/authoring-workflows/ + The Book of Archon (10 chapters, 4 parts: Orientation / Core Workflows / Customization / Advanced)

## The 7 node types (mutually exclusive — exactly one per node)

| Type | Field | AI? | Notes |
|---|---|---|---|
| Command | `command: name` | ✓ | loads `.archon/commands/name.md` prompt template |
| Prompt | `prompt: "..."` | ✓ | inline; full AI params (model, provider, hooks, mcp, skills, output_format, allowed/denied_tools, retry, effort, thinking, fallbackModel, betas) |
| Bash | `bash: "..."` | ✗ | stdout = node output; timeout ms (default 120000) |
| Script | `script: inline\|name` | ✗ | `runtime: bun` (.ts/.js) or `uv` (.py, + optional `deps:`) — runtime REQUIRED |
| Loop | `loop: {prompt, until, max_iterations, fresh_context, until_bash, interactive, gate_message}` | ✓ (inside) | `until` = promise-tag sentinel; `until_bash` exit-0 = done (deterministic exit!) |
| Approval | `approval: {message, capture_response, on_reject: {prompt, max_attempts 1-10}}` | ✗ | pauses for human; needs workflow-level `interactive: true` for web delivery |
| Cancel | `cancel: "reason"` | ✗ | terminate; typically gated with `when:` |

**Universal base fields:** `id`, `depends_on: []`, `when:` (condition — skips node), `trigger_rule: all_success | one_success | none_failed_min_one_success | all_done`, `idle_timeout` (default 300s on AI nodes).

**Variables:** `$ARGUMENTS` (user message), `$ARTIFACTS_DIR` (pre-created per-run artifact dir), `$BASE_BRANCH`, `$WORKFLOW_ID`, `$nodeId.output` (upstream output), `$REJECTION_REASON` (inside on_reject).

## The silent-failure catalog (the most transferable artifact)

Archon maintains a **12-case catalog of parameters that silently no-op** (`parameter-matrix.md`) — the repo treats misconfiguration as a first-class documentation object:

- **Loop nodes are structural controllers, not AI executors**: `model` / `provider` / `context` / `hooks` / `retry` on a loop node are IGNORED — AI config must live inside `loop.prompt` or at workflow level; fresh context is `loop.fresh_context: true`, not `context: fresh`.
- All AI params silently no-op on bash/script/approval/cancel nodes (warnings logged, execution continues).
- `interactive: true` on a node without workflow-level `interactive: true` = gate messages never reach the user (silent).
- Invalid `$nodeId.output` references resolve to **empty strings** with only a logged warning.
- Backticks in node outputs corrupt template-literal substitution in scripts → cryptic parse errors.
- **Codex provider ignores per-node hooks/MCP/skills entirely** — global `~/.codex/config.toml` + `.agents/skills/` instead. Per-node flexibility is Claude-only.
- `retry` on loop nodes = hard error (retry and iteration are mutually exclusive primitives).

## Codified good practices (the authors' own top rules)

1. **Determinism-first:** "Reserve AI nodes for reasoning tasks. Use `bash:`/`script:` for anything with a verifiable answer — tests, JSON parsing, file reads, git state checks." (= vault Rule 5 "if code can answer, code answers" — independent convergence.)
2. **`output_format` (JSON Schema) on every node whose output a downstream `when:` reads** — pattern-matching free-form AI text in conditionals is a named anti-pattern.
3. **Fresh context forces artifact-driven design:** with `context: fresh`, state moves ONLY via files; commands must explicitly read `$ARTIFACTS_DIR`. (= the blank-slate/artifact-handoff discipline of [[external|pocock-agentic-workflow/_index]] and GSD, here enforced by the engine.)
4. Bash interpolation of `$nodeId.output` is **auto-shell-quoted** (injection-safe); bun/TS script bodies are NOT — use direct assignment, never template interpolation.

## Architecture + security model (docs dive)

- 5 components: **Orchestrator** (routing) → **Platform Adapters** (`IPlatformAdapter`: Web/CLI/Slack/Telegram/Discord/GitHub/Gitea) → **AI Providers** (`IAgentProvider` streaming `AsyncGenerator<MessageChunk>`: Claude/Codex/Pi + community OpenCode/Copilot) → **Isolation Providers** (WorktreeProvider, `~/.archon/workspaces/<owner>/<repo>/worktrees/<branch>/`, adoption-pattern reuse) → **DB** (SQLite default / Postgres; 18 `remote_agent_*` tables).
- **Env stripping:** `stripCwdEnv()` removes ALL keys from CWD `.env*` files before any module reads `process.env` — the target repo's secrets never reach the agent. Setup wizard collects API keys **in a separate terminal so the coding agent never sees them** (stream-demonstrated).
- **Credentials:** AES-256-GCM at rest, auto-provisioned key `~/.archon/credential-key` (0600); never logged, never returned by API.
- **The big trade-off, stated plainly in docs:** Archon runs the Claude Agent SDK in **`bypassPermissions` mode** (unattended remote execution) — the deployment boundary IS the security boundary; per-node `allowed_tools`/`denied_tools` (e.g., read-only reviewer `[Read, Grep, Glob]`) is the mitigation. **Explicitly NOT multi-tenant** ("single-developer tool").
- Platform allow-lists silently reject unauthorized users; GitHub webhooks HMAC-verified; `X-Archon-User` header spoofing is a documented reverse-proxy footgun.
- Telemetry: PostHog, categorical-only, custom workflow names redacted to `"custom"`, honors `DO_NOT_TRACK`, CI auto-disabled.

## Key Takeaways

- The schema is small (7 node types + DAG fields) but the **engineering weight is in the failure documentation** — a 12-case silent-no-op catalog and a good-practices file written *for the agent that authors workflows*, not for humans. That inversion (docs as agent context) is the same move as [[anthropic-large-codebases-anchor]]'s CLAUDE.md hierarchy and the skill-first docs of [[external|claude-skills/_index]].
- `until_bash` on loop nodes is the standout primitive: a **deterministic exit condition for an AI loop** — the loop cannot lie about being done if the test suite is the judge. This is the strongest single answer this corpus has to Ralph-loop compounding error.
- Approval nodes with `on_reject.prompt` = **rework-on-rejection built into the gate** (feedback loops without abandoning the run) — matches the pause/resume relay the video demoed.
- Security posture is honest: `bypassPermissions` + worktree + env-stripping + tool allow-lists, single-developer trust model. Any team pilot must treat the Archon host as a privileged CI runner, not a shared service.
- For our vault: `raw/` → wiki compile pipelines map cleanly onto bash-node + prompt-node + `until_bash` loop shapes — see the pilot menu (`output/(C) 2026-07-04-archon-harness-builder-pilot-methods.md`).

## Cross-links

[[archon-harness-builder-anchor]] · [[archon-default-workflows-and-dogfood]] · [[harness-economics-and-tos-timeline]] · [[external|claude-code-hooks/_index]] (hooks event model reused per-node) · [[external|elicit-verifiable-agent-dsl/architecture-curator-interpreter]] (contrast: ÆPL makes the *plan* checkable; Archon makes the *process* checkable — complementary verifiability layers)
