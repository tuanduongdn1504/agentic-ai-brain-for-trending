# C2 — 5 deep-analysis reports content + key findings

> Source cluster: `docs/en/01-05.md` (5 deep-dive reports; ~24 KB / 674 lines total)
> All claims below are per Sanbu's analysis of Claude Code v2.1.88 internals from publicly-available sources; not Anthropic-confirmed.

---

## 01 — Telemetry & Privacy

### Two-tier analytics pipeline

**First-Party Logging (1P) — Anthropic-direct:**
- Endpoint: `https://api.anthropic.com/api/event_logging/batch`
- Protocol: OpenTelemetry + Protocol Buffers
- Batch size: up to 200 events / 10s flush
- Retry: quadratic backoff up to 8 attempts, **disk-persisted to `~/.claude/telemetry/` for durability**
- Source path claimed: `src/services/analytics/firstPartyEventLoggingExporter.ts`

**Third-Party Logging (Datadog):**
- Endpoint: `https://http-intake.logs.us5.datadoghq.com/api/v2/logs`
- Scope: 64 pre-approved event types
- Token: `pubbbf48e6d78dae54bceaa4acf463299bf` (verbatim per Sanbu)

### What's collected (per event)

**Environment fingerprint** (`metadata.ts:417-452`):
- platform / arch / nodeVersion / terminal type
- installed package managers + runtimes
- CI/CD detection + GitHub Actions metadata
- WSL version / Linux distro / kernel version
- VCS type / Claude Code version + build time / deployment environment

**Process metrics** (`metadata.ts:457-467`):
- uptime / rss / heapTotal / heapUsed / CPU usage / memory arrays / external allocations

**User tracking** (`metadata.ts:472-496`):
- model in use / session ID / user ID / device ID
- account UUID / organization UUID / subscription tier (max/pro/enterprise/team)
- **repository remote URL hash (SHA256 first 16 chars)** ← server-side correlation across repos
- agent type / team name / parent session ID

**Tool inputs** (default truncated):
- Strings: 512 chars cap, 128 + ellipsis displayed
- JSON: 4,096 chars
- Arrays: max 20 items
- Nested objects: max 2 levels

**`OTEL_LOG_TOOL_DETAILS=1` env var enables FULL tool input capture** (overrides truncation).

**File extension tracking**: bash commands `rm/mv/cp/touch/mkdir/chmod/chown/cat/head/tail/sort/stat/diff/wc/grep/rg/sed` have file argument extensions extracted and logged.

### THE OPT-OUT PROBLEM

```typescript
// src/services/analytics/firstPartyEventLogger.ts:141-144
export function is1PEventLoggingEnabled(): boolean {
  return !isAnalyticsDisabled()
}
```

`isAnalyticsDisabled()` returns true ONLY for:
- Test environments
- Third-party cloud providers (Bedrock, Vertex)
- Global telemetry opt-out (**not exposed in settings UI**)

→ **No user-facing setting to disable first-party event logging** for direct Anthropic API users.

### GrowthBook A/B testing

Users assigned to experiment groups **without explicit consent**. Attributes sent: id / sessionId / deviceID / platform / organizationUUID / subscriptionType.

### Key takeaways

1. Hundreds of events per session
2. No opt-out for 1P (direct API users)
3. Persistence (failed events → disk → aggressive retry)
4. Third-party sharing (Datadog)
5. Tool detail backdoor (`OTEL_LOG_TOOL_DETAILS=1`)
6. Repo fingerprinting (SHA256 hash → server-side correlation)

---

## 02 — Hidden Features & Codenames

### Animal codename system

| Codename | Role | Evidence |
|----------|------|----------|
| **Tengu** (天狗) | Product/telemetry prefix; possibly model | `tengu_*` prefix on 250+ analytics events + feature flags |
| **Capybara** (水豚) | Sonnet-series; currently v8 | `capybara-v2-fast[1m]`; prompt patches for v8 issues |
| **Fennec** (耳廓狐) | Predecessor to Opus 4.6 | Migration: `fennec-latest` → `opus` |
| **Numbat** (袋食蚁兽) | Next model | Code comment: *"Remove this section when we launch numbat"* |

### Codename protection

Build system uses `scripts/excluded-strings.txt` to scan for leaked codenames. Buddy system encodes colliding species name via `String.fromCharCode()` to avoid triggering canary — that colliding species is **capybara** (both pet species + model codename).

### Capybara v8 behavior issues

1. Stop sequence false trigger ~10% rate when `<functions>` at prompt tail
2. Empty tool_result causes zero output
3. Over-commenting → dedicated anti-comment prompt patches
4. **High false-claims rate: v8 = 29-30% FC vs v4's 16.7%**
5. Insufficient verification → "thoroughness counterweight" needed

### Feature flag obscured-naming convention

All feature flags use `tengu_` prefix + **random word pairs** to obscure purpose:

| Flag | Purpose |
|------|---------|
| `tengu_onyx_plover` | Auto Dream (background memory consolidation) |
| `tengu_coral_fern` | memdir |
| `tengu_moth_copse` | Another memdir switch |
| `tengu_herring_clock` | Team memory |
| `tengu_passport_quail` | Path feature |
| `tengu_slate_thimble` | Another memdir switch |
| `tengu_sedge_lantern` | Away Summary |
| `tengu_frond_boric` | Analytics killswitch |
| `tengu_amber_quartz_disabled` | Voice mode killswitch |
| `tengu_amber_flint` | Agent teams |
| `tengu_hive_evidence` | Verification agent |

Pattern: adjective/material + nature/object → external observers cannot infer feature purpose from flag name alone.

### Internal vs external user differences

Anthropic employees (`USER_TYPE === 'ant'`) get materially better treatment:

| Dimension | External | Internal (ant) |
|-----------|----------|----------------|
| Output style | "Be extra concise" | "Err on the side of more explanation" |
| False-claims mitigation | None | Capybara v8 patches |
| Numeric anchors | None | "≤25 words between tools, ≤100 words final" |
| Verification agent | None | Required for non-trivial changes |
| Comment guidance | Generic | Dedicated anti-over-comment prompt |
| Proactive correction | None | "If user has misconception, say so" |

### Internal-only tools

`REPLTool` / `SuggestBackgroundPRTool` / `TungstenTool` (perf monitoring panel) / `VerifyPlanExecutionTool` / Agent nesting (agents-spawning-agents).

### Hidden commands

| Command | Status | Description |
|---------|--------|-------------|
| `/btw` | Active | Side questions without interrupting |
| `/stickers` | Active | Order Claude Code stickers (browser open) |
| `/thinkback` | Active | 2025 Year in Review |
| `/effort` | Active | Set model effort level |
| `/good-claude` | Stub | Hidden placeholder |
| `/bughunter` | Stub | Hidden placeholder |

---

## 03 — Undercover Mode

### Definition

Safety system for official employees contributing to external/open-source repos. When active, hides internal-specific AI model info + attribution; instructs system to present contributions as if written by a human developer.

**Stated purpose**: prevent leakage of internal secrets + unreleased model names into open-source community.

### Activation logic

```typescript
// src/utils/undercover.ts:28-37
export function isUndercover(): boolean {
  if (process.env.USER_TYPE === 'ant') {
    if (isEnvTruthy(process.env.CLAUDE_CODE_UNDERCOVER)) return true
    // Auto: active unless positively confirmed internal repo
    return getRepoClassCached() !== 'internal'
  }
  return false
}
```

Properties:
- **Internal-only** (`USER_TYPE === 'ant'`)
- **Default ON in all repos except internal-allowlisted**
- **No force-OFF exists** — *"There is NO force-OFF. This guards against model codename leaks"*
- External builds: dead-code-eliminated by bundler; never executes

### Verbatim prompt injected into model

```
## UNDERCOVER MODE — CRITICAL

You are operating UNDERCOVER in a PUBLIC/OPEN-SOURCE repository. Your commit
messages, PR titles, and PR bodies MUST NOT contain ANY Anthropic-internal
information. Do not blow your cover.

NEVER include in commit messages or PR descriptions:
- Internal model codenames (animal names like Capybara, Tengu, etc.)
- Unreleased model version numbers (e.g., opus-4-7, sonnet-4-8)
- Internal repo or project names (e.g., claude-cli-internal, anthropics/…)
- Internal tooling, Slack channels, or short links (e.g., go/cc, #claude-code-…)
- The phrase "Claude Code" or any mention that you are an AI
- Any hint of what model or version you are
- Co-Authored-By lines or any other attribution

Write commit messages as a human developer would — describe only what the code
change does.

GOOD:
- "Fix race condition in file watcher initialization"
- "Add support for custom key bindings"

BAD (never write these):
- "Fix bug found while testing with Claude Capybara"
- "1-shotted by claude-opus-4-6"
- "Generated with Claude Code"
- "Co-Authored-By: Claude Opus 4.6 <…>"
```

### Attribution masking

```typescript
function maskModelCodename(baseName: string): string {
  // e.g. capybara-v2-fast → cap*****-v2-fast
  const [codename = '', ...rest] = baseName.split('-')
  const masked = codename.slice(0, 3) + '*'.repeat(Math.max(0, codename.length - 3))
  return [masked, ...rest].join('-')
}
```

### Implications (verbatim)

- Code is written by AI but commits appear human-authored
- No "Co-Authored-By: Claude" attribution
- No "Generated with Claude Code" markers
- Project maintainers + community **cannot identify AI-generated contributions**
- *"Potentially violates open-source transparency norms regarding AI contributions"*
- Phrase *"Do not blow your cover"* frames AI as undercover agent

---

## 04 — Remote Control & Killswitches

### Remote managed settings

- Endpoint: `GET /api/claude_code/settings`
- Polling: every **1 hour** (`POLLING_INTERVAL_MS = 60 * 60 * 1000`); 5 retries; 10s timeout
- **Eligibility**: Console users (API key) all eligible; OAuth users only Enterprise/C4E + Team subscribers

### Accept-or-die dialog

```typescript
// src/services/remoteManagedSettings/securityCheck.tsx:67-73
export function handleSecurityCheckResult(result: SecurityCheckResult): boolean {
  if (result === 'rejected') {
    gracefulShutdownSync(1)  // Exit with code 1
    return false
  }
  return true
}
```

When remote settings contain "dangerous" changes, blocking dialog shown. **Reject = app exits with code 1**.

### Graceful degradation

If remote server unreachable → cached settings from disk used. Once applied, persist even when server down.

### Feature flag killswitches (6+ documented)

| Killswitch | Mechanism | Effect |
|------------|-----------|--------|
| Bypass Permissions | Statsig gate | Disables permission bypass capabilities |
| Auto Mode Circuit Breaker | `autoModeCircuitBroken` state | Prevents re-entry to auto mode |
| Fast Mode | `/api/claude_code_penguin_mode` | Permanently disable fast mode for user |
| Analytics Sink | `tengu_frond_boric` flag | Stop all analytics output remotely |
| Agent Teams | `tengu_amber_flint` | Requires both env var AND flag |
| Voice Mode | `tengu_amber_quartz_disabled` | Emergency off |

### Model override system

`tengu_ant_model_override` GrowthBook flag can:
- Set default model
- Set default effort level
- Append to system prompt
- Define custom model aliases

### Penguin mode (fast mode)

`GET /api/claude_code_penguin_mode` — if API indicates disabled, **permanently disabled for user** (state persists). Multiple flags: `tengu_penguins_off` / `tengu_marble_sandcastle`.

### Summary table

| Mechanism | Scope | User Consent |
|-----------|-------|--------------|
| Remote managed settings | Enterprise/Team | Accept or exit |
| GrowthBook feature flags | All users | None |
| Killswitches | All users | None |
| Model override | Internal (ant) | None |
| Fast mode control | All users | None |

---

## 05 — Future Roadmap

### Numbat — next model

```typescript
// src/constants/prompts.ts:402
// @[MODEL LAUNCH]: Remove this section when we launch numbat.
```

**Numbat** (袋食蚁兽) = upcoming model. Comment indicates output efficiency section will be revised → suggests Numbat may have better native output control.

### Future versions

`opus-4-7` and `sonnet-4-8` named in undercover-mode protected-strings list (codename leak prevention).

### Codename evolution chain

```
Fennec (耳廓狐) → Opus 4.6 → [Numbat?]
Capybara (水豚) → Sonnet v8 → [?]
Tengu (天狗) → telemetry/product prefix
```

### `@[MODEL LAUNCH]` checklist

20+ markers in codebase listing what to update on launch:
- Default model names (`FRONTIER_MODEL_NAME`)
- Model family IDs / knowledge cutoff dates / pricing tables / context window configs / thinking mode flags / display name mappings / migration scripts

### KAIROS — autonomous agent mode

Largest unreleased feature. Transforms Claude Code from reactive assistant → proactive autonomous agent.

System prompt excerpt (verbatim per Sanbu):

```
You are running autonomously.
You will receive <tick> prompts that keep you alive between turns.
If you have nothing useful to do, call SleepTool.
Bias toward action — read files, make changes, commit without asking.

## Terminal focus
- Unfocused: The user is away. Lean heavily into autonomous action.
- Focused: The user is watching. Be more collaborative.
```

KAIROS-associated tools:
- `SleepTool` (KAIROS / PROACTIVE)
- `SendUserFileTool` (KAIROS)
- `PushNotificationTool` (KAIROS / KAIROS_PUSH_NOTIFICATION)
- `SubscribePRTool` (KAIROS_GITHUB_WEBHOOKS)
- `BriefTool` (KAIROS_BRIEF)

### Voice mode

Push-to-talk fully implemented but feature-flag-gated.
- OAuth-only (no API key / Bedrock / Vertex)
- mTLS WebSocket
- Killswitch: `tengu_amber_quartz_disabled`

### 17 unreleased tools

| Tool | Flag | Description |
|------|------|-------------|
| WebBrowserTool | `WEB_BROWSER_TOOL` | Browser automation (codename: bagel) |
| TerminalCaptureTool | `TERMINAL_PANEL` | Terminal panel capture/monitoring |
| WorkflowTool | `WORKFLOW_SCRIPTS` | Predefined workflow scripts |
| MonitorTool | `MONITOR_TOOL` | System/process monitoring |
| SnipTool | `HISTORY_SNIP` | History snipping/truncation |
| ListPeersTool | `UDS_INBOX` | Unix domain socket peer discovery |
| RemoteTriggerTool | `AGENT_TRIGGERS_REMOTE` | Remote agent triggering |
| TungstenTool | ant-only | Internal performance monitoring |
| VerifyPlanExecutionTool | VERIFY_PLAN env | Plan execution verification |
| OverflowTestTool | `OVERFLOW_TEST_TOOL` | Context overflow testing |
| SubscribePRTool | `KAIROS_GITHUB_WEBHOOKS` | GitHub PR webhook subs |

### Coordinator Mode + Buddy System (Virtual Pets) + Dream Task

- **Coordinator Mode** — `COORDINATOR_MODE` flag — multi-agent coordination with shared state + messaging
- **Buddy System** — 18 species / 5 rarity tiers / 7 hats / 5 stats (DEBUGGING / PATIENCE / CHAOS / WISDOM / SNARK) / 1% shiny / deterministic from user-ID-hash
- **Dream Task** — `tengu_onyx_plover` — background memory consolidation subagent

### Three directions summary (verbatim)

1. New Models: Numbat (next), Opus 4.7, Sonnet 4.8 in development
2. Autonomous Agent: KAIROS — unattended operation, proactive actions, push notifications
3. Multi-modal: Voice ready, browser tool waiting, workflow automation coming

> *"Claude Code is evolving from a coding assistant into an always-on autonomous development agent."*

---

## Cluster takeaway

These 5 reports are the substantive core of the archive. They document:
1. **Telemetry without UI-exposed opt-out** for direct API users
2. **Dual-tier user system** (ant vs external) with materially-different prompts + tools
3. **Undercover mode with no force-OFF** — Anthropic-employees auto-strip AI attribution in OSS commits
4. **Remote killswitches** — hourly polling can disable any feature for any user without consent
5. **Roadmap signals** — Numbat next + KAIROS autonomous mode + voice + 17 unreleased tools

Each report is short (~110-167 lines EN) but information-dense. Quadrilingual EN+CN+JA+KO at parity. **Operationally relevant to Storm Bear vault as Claude Code daily-use caveat reference.**
