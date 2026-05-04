# E1 — Core archive: 5-doc Claude Code v2.1.88 internals + Numbat/KAIROS roadmap signals

> **Type:** Entity page (core product)
> **Subject:** `sanbuphy/learn-coding-agent` content body
> **Wiki #53**

---

## Identity

| Field | Value |
|-------|-------|
| Repo | sanbuphy/learn-coding-agent |
| README h1 title | "Claude Code Architecture Study" |
| Primary content | 5 deep-dive markdown reports + ~800-line README architecture documentation |
| Subject of study | Claude Code v2.1.88 internals |
| Author | Sanbu (sanbuphy) — solo CN researcher |
| Stars / Forks | 11,735 / **19,741** (CORPUS-RECORD 168.2% fork inversion) |
| License | None formal; README "Commercial use strictly prohibited" |
| Languages | EN + CN + JA + KO (quadrilingual) |
| Status | ABANDONED (last push 2026-04-01, 24 days stale at probe) |

---

## What it is

A research archive that documents internal architecture, telemetry behavior, hidden features, undercover-mode logic, remote-control mechanisms, and roadmap signals of Claude Code (Anthropic's CLI agent product). Compiled per the README "entirely from publicly available online references and discussions" — NOT a leak, NOT insider source, NOT direct decompilation claim.

The archive is composed of:

1. **README.md** (45 KB, ~800 lines) — Architecture overview with ASCII block diagrams covering: src/ directory tree, query lifecycle data flow, tool system + 40+ tool inventory, permission system, sub-agent + multi-agent + swarm, context management (autoCompact / snipCompact / contextCollapse), MCP integration (5 transports), bridge layer, session persistence (~/.claude/projects/<hash>/sessions/<id>.jsonl), feature flag system (21+ flags listed), state management (AppState store), 12 progressive harness mechanisms (s01-s12), 11 key design patterns
2. **5 deep-dive reports** (`docs/{en,ja,ko,zh}/01-05.md`) — Telemetry / Hidden features / Undercover / Remote control / Roadmap (full content summarized in C2 cluster summary)

---

## Top 6 substantive findings (per Sanbu's analysis)

### 1. Two-tier telemetry pipeline with no UI-exposed opt-out for direct API users

- 1P: `https://api.anthropic.com/api/event_logging/batch` (OTel + Protocol Buffers, batch 200/10s, disk-persisted retry to `~/.claude/telemetry/`)
- 3P: `https://http-intake.logs.us5.datadoghq.com/api/v2/logs` (64 pre-approved event types)
- Per-event payload includes: env fingerprint, process metrics, **SHA256 first-16-char repo URL hash** (server-side correlation), tool inputs (truncated by default; `OTEL_LOG_TOOL_DETAILS=1` env enables full capture), file extensions extracted from common bash file-ops
- `isAnalyticsDisabled()` returns true ONLY for test envs / Bedrock+Vertex / global telemetry-opt-out (not exposed in settings UI) → **direct Anthropic API users have no UI-exposed opt-out**
- GrowthBook A/B assignment without explicit consent (id / sessionId / deviceID / platform / orgUUID / subscriptionType sent)

### 2. Animal-codename system with active leak prevention

- Tengu (天狗) = product/telemetry prefix on 250+ flags + events
- Capybara (水豚) = current Sonnet-series at v8 (with documented 29-30% false-claims rate vs v4's 16.7%)
- Fennec (耳廓狐) = predecessor to Opus 4.6 (migration: `fennec-latest` → `opus`)
- **Numbat (袋食蚁兽) = next model** (per code comment: *"Remove this section when we launch numbat"*)
- Build-time canary scan via `scripts/excluded-strings.txt`; Buddy-system colliding species `capybara` constructed via `String.fromCharCode()` to evade canary

### 3. Internal vs external user dual-tier prompt system

Anthropic employees (`USER_TYPE === 'ant'`) get materially-different prompts + tool access:
- "Err on side of more explanation" (vs external "Be extra concise")
- Capybara v8 false-claims-mitigation patches
- Numeric anchors ("≤25 words between tools, ≤100 words final")
- Required verification agent for non-trivial changes
- Anti-over-comment dedicated prompt
- Internal-only tools: `REPLTool` / `SuggestBackgroundPRTool` / `TungstenTool` (perf monitor) / `VerifyPlanExecutionTool` / agent-nesting

→ External users get a strictly-inferior product per Sanbu's analysis.

### 4. Undercover mode — no force-OFF; AI authorship hidden in OSS commits

- Activation: `process.env.USER_TYPE === 'ant'` AND repo NOT internal-allowlisted (default ON in all external repos for Anthropic employees)
- **No force-OFF exists** (verbatim per Sanbu: *"This guards against model codename leaks"*)
- Injected prompt instructs model to write commits "as a human developer would"; NEVER include codenames / unreleased version numbers / "Claude Code" phrase / "Co-Authored-By" lines / any AI attribution
- **Implication**: Anthropic employees committing to public OSS via Claude Code produce commits that are AI-authored but appear human-authored; project maintainers + community cannot identify these contributions
- Verbatim Sanbu observation: *"Potentially violates open-source transparency norms regarding AI contributions"*
- Phrase *"Do not blow your cover"* explicitly frames model as undercover agent

### 5. Remote killswitch infrastructure with accept-or-die dialog

- `GET /api/claude_code/settings` polled every 1 hour (5 retries, 10s timeout)
- "Dangerous" remote-settings changes shown via blocking dialog → **user reject = `gracefulShutdownSync(1)` exits app**
- 6+ documented killswitches: bypass permissions / auto mode / fast mode / analytics sink (`tengu_frond_boric`) / agent teams (`tengu_amber_flint`) / voice mode (`tengu_amber_quartz_disabled`)
- `tengu_ant_model_override` GrowthBook flag can change default model + effort + system prompt + custom aliases for ant-only users
- **No user-consent layer for GrowthBook changes** (per Sanbu)

### 6. Roadmap signals — Numbat + KAIROS + voice + 17 unreleased tools

- **Numbat**: next-model codename confirmed via code comments
- **Opus 4.7 / Sonnet 4.8**: in development per undercover protected-strings list
- **KAIROS**: largest unreleased feature; transforms Claude Code into autonomous agent with `<tick>` heartbeats, `SleepTool` for pacing, `PushNotificationTool`, `SubscribePRTool` (GitHub PR webhook subscriptions), terminal-focus-aware behavior ("Unfocused: lean into autonomous action")
- **Voice mode**: push-to-talk fully implemented, OAuth-only, mTLS WebSocket, killswitch `tengu_amber_quartz_disabled`
- **17 unreleased tools** including `WebBrowserTool` (codename `bagel`) / `TerminalCaptureTool` / `WorkflowTool` / `MonitorTool` / `RemoteTriggerTool` / `TungstenTool` / `VerifyPlanExecutionTool` etc.
- **Buddy System (virtual pets)**: 18 species / 5 rarity tiers / 7 hats / 5 stats (DEBUGGING / PATIENCE / CHAOS / WISDOM / SNARK) / 1% shiny / deterministic from user-ID-hash
- **Dream Task**: background memory consolidation (`tengu_onyx_plover` flag)

→ Direction summary (per Sanbu): *"Claude Code is evolving from a coding assistant into an always-on autonomous development agent."*

---

## Architecture documentation (README content beyond 5 deep-dive reports)

The README also includes substantial Claude Code architecture documentation:

- Full src/ directory tree (~250 lines ASCII)
- Query lifecycle data flow (processUserInput → fetchSystemPromptParts → recordTranscript → query loop → tool execution → tool_result append → loop or yield)
- Tool interface lifecycle (validateInput / checkPermissions / call / isConcurrencySafe / isReadOnly / isDestructive / interruptBehavior + rendering + AI-facing prompt)
- 40+ tool inventory grouped (FILE OPS / SEARCH / EXECUTION / WEB / AGENT / MCP / SKILLS / INTERACTION / PLANNING / SYSTEM)
- Permission system (validateInput → PreToolUse hooks → permission rules → interactive prompt → checkPermissions → APPROVED → tool.call())
- Sub-agent architecture (FORK / REMOTE / IN-PROCESS TEAMMATE; spawn modes default/fork/worktree/remote; SWARM mode feature-gated with shared task board + isolated messages[])
- Context management (autoCompact summarize / snipCompact trim HISTORY_SNIP / contextCollapse restructure CONTEXT_COLLAPSE)
- MCP architecture (5 transports stdio/sse/http/ws/sdk + OAuth 2.0 + Cross-App Access XAA/SEP-990 + `mcp__<server>__<tool>` naming)
- Bridge layer (Claude Desktop / Web / Cowork ↔ CLI via JWT + work secret + capacityWake)
- Session persistence (`~/.claude/projects/<hash>/sessions/<id>.jsonl` append-only + resume / continue / fork-session)
- Feature flag system (Bun compile-time DCE + 21+ flags listed including KAIROS / VOICE_MODE / DAEMON / COORDINATOR_MODE / etc.)
- State management (AppState store with toolPermissionContext / fileHistory / attribution / verbose / mainLoopModel / fastMode / speculation)
- 12 progressive harness mechanisms s01-s12 (the loop / tool dispatch / planning / sub-agents / knowledge on demand / context compression / persistent tasks / background tasks / agent teams / team protocols / autonomous agents / worktree isolation)
- 11 key design patterns (AsyncGenerator streaming / Builder+Factory / Branded Types / Feature Flags+DCE / Discriminated Unions / Observer+State Machine / Snapshot State / Ring Buffer / Fire-and-Forget Write / Lazy Schema / Context Isolation)

This architecture documentation is the **substantive non-controversial portion** of the archive — useful as Claude Code internals reference for developers building competing harnesses.

---

## Cross-references

- **C1** — README + 5-doc structure + Claude Code v2.1.88 stats
- **C2** — 5 deep-analysis reports content (full summary)
- **C3** — Sanbu author profile + quadrilingual + research-only license + abandoned status
- **E2** — Pattern implications (#38 38b N=2 / #75 N=2 / #29 29-absent-4 / etc.)
- **E3** — Sanbu / sanbuphy.cn ecosystem
- **E4** — 42nd consecutive Storm Bear meta-entity (Claude Code operational caveats)

## Caveats (mandatory)

- All claims are per Sanbu's analysis based on publicly-available sources; not Anthropic-confirmed
- Studied version Claude Code v2.1.88 (current Claude Code may have changed in 25+ days)
- Repo abandoned 2026-04-01 — no follow-up; version-bound claims may be stale
- Research-only license blocks commercial re-use of THIS archive content (Storm Bear can READ but not REPACKAGE)
- Sanbu identity unknown beyond GitHub presence; cannot independently verify reverse-engineering methodology
