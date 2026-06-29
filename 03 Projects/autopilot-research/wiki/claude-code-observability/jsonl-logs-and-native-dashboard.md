# JSONL Logs & Native Cost/Usage Views

> **Overview:** Claude Code writes session transcripts as append-only JSONL files at `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl`. Each line captures every message, tool call, usage tokens (input/output/cache), model, timestamp. Native `/cost`, `/stats`, `/status` commands + statusline expose subscription vs. API billing. Community tools like ryoppippi/ccusage parse JSONL for cost breakdowns. JSONL = exact per-session replay, local, free, any plan. OpenTelemetry = real-time dashboards, needs pipeline, Max/Pro only.
>
> **Source video:** Mansel Scheffel, "Claude Code + OpenTelemetry = Claude Command Center" (2026-04-22, atomicOps). Key timestamps: [01:50] (JSONL + OTEL intro), [02:17] (dashboard overview), [10:27] (news monitor example — creator's personal datapoint: "32 million tokens across 23 sessions").

## Source

**Raw file:** `/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/2026-06-20-claude-code-otel-command-center.md`

**First-party sources fetched:**
- Claude Code official docs: sessions, JSONL format, token fields, retention
- `github.com/ryoppippi/ccusage` (16.4k stars, MIT) — JSONL parser + cost reporting
- `github.com/hydai/ccstat` — Rust JSONL parser, performance reimplementation
- Community tools: `claude-code-log`, `claude-code-transcripts`, `@kimuson/claude-code-viewer`
- Claude Cowork JSONL path/metadata — **creator's video claim only, NOT confirmed in first-party docs** (see Cowork section below; all Cowork specifics here are video-sourced)

---

## JSONL Storage & Format

### File paths

- **Claude Code:** `~/.claude/projects/<URL-encoded-project-path>/<session-id>.jsonl`
  - Example: `~/.claude/projects/file%3A%2F%2F%2FUsers%2Fstormsmith%2Fmonorepo%2Fhireui/550e8400-e29b-41d4-a716-446655440000.jsonl`
- **Claude Cowork:** `~/Library/Application Support/Claude/local-agent-mode-sessions/<session-id>.jsonl` (separate directory; **unconfirmed path from video — verify in your system**)

### Retention & cleanup

- **Default retention:** 30 days
- **Configure:** set `cleanupPeriodDays` in `~/.claude/settings.json` to override
- **Disable JSONL entirely:** set `CLAUDE_CODE_SKIP_PROMPT_HISTORY` env var OR use `--no-session-persistence` in headless mode
- **Relocate:** set `CLAUDE_CONFIG_DIR` env var to store `~/.claude/` elsewhere (e.g., mounted network drive for server deployments)

### Line structure (each message is one JSON object per line)

Every line is a complete, valid JSON object. Common fields across all line types:

```json
{
  "type": "user|assistant|tool_result",
  "uuid": "550e8400-e29b-41d4-a716-446655440000",
  "timestamp": "2026-06-20T14:35:22.123Z",
  "sessionId": "unique-session-id",
  "cwd": "/absolute/path/to/project",
  "gitBranch": "main",
  "version": "1.0"
}
```

### Assistant message line (includes token usage)

```json
{
  "type": "assistant",
  "uuid": "550e8400-e29b-41d4-a716-446655440001",
  "timestamp": "2026-06-20T14:35:30.456Z",
  "sessionId": "unique-session-id",
  "cwd": "/absolute/path",
  "gitBranch": "main",
  "version": "1.0",
  "message": {
    "content": [{"type": "text", "text": "Response text"}],
    "usage": {
      "input_tokens": 1234,
      "output_tokens": 567,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 100
    },
    "model": "claude-3-5-sonnet-20241022"
  }
}
```

**Token fields (all appear in `message.usage`):**
- `input_tokens` — non-cached input tokens consumed
- `output_tokens` — tokens generated this turn
- `cache_creation_input_tokens` — new prompt cache written (first use of a cache segment)
- `cache_read_input_tokens` — tokens served from existing prompt cache (bills ~**0.1×** a fresh input token — i.e. ~90% off; cache *creation* bills ~1.25× the base input rate)

### Tool calls & results

- **Tool use block:** assistant message contains `tool_use` block with unique ID (`id: "tool_use_<uuid>"`)
- **Tool result:** user message references the tool_use ID via `tool_use_id: "tool_use_<uuid>"` + result content
- Example:
  ```json
  {"type": "assistant", "message": {"content": [{"type": "tool_use", "id": "tool_use_abc123", "name": "bash", "input": {"command": "ls"}}]}}
  {"type": "user", "message": {"content": [{"type": "tool_result", "type": "tool_use_id", "tool_use_id": "tool_use_abc123", "content": "file1.txt\nfile2.txt"}]}}
  ```

---

## Native Commands: `/cost`, `/stats`, `/status`, Statusline

### `/cost` — API billing view

- Shows **session-level API billing** (separate from subscription usage)
- Reflects tokens actually charged to your Anthropic API account
- Distinct from `/usage`/`/stats` (subscription quota) — the API credit pool is separate from the Pro/Max subscription quota
- Useful for: tracking per-project billing splits, monitoring API spend on a developer account

### `/stats` — subscription usage

- Shows **Pro or Max plan quota** and current consumption
- Displays limits (e.g., "8M tokens / 4M remaining today" for Max)
- Separate view from `/cost` — only appears if on a paid subscription plan
- Useful for: monitoring plan ceiling, understanding when to upgrade or wait for reset

### `/status` — session/environment status

- Model name + account/auth + environment status
- Context window percentage used (e.g., `67% of 200K`)
- ⚠️ `/status` as a *cost* view is **unconfirmed** — for session cost use `/cost`, and for token/plan usage use `/usage`. (`/status` exists, but its exact contents vary by version.)

### Statusline (persistent footer)

- Customizable 1-line display at bottom of Claude Code editor
- Can show: model, git branch, session cost, context usage %
- Example: `[main] @ sonnet | 4.2K tokens | $0.021 this session`
- **Configuration:** (unconfirmed — check current version docs for exact settings.json keys)

---

## Community JSONL Parsers

### ryoppippi/ccusage (most popular)

**GitHub:** `https://github.com/ryoppippi/ccusage`  
**Stars:** 16.4k (as of 2026-06)  
**License:** MIT  
**Language:** Python + CLI  

**What it does:**
- Reads all JSONL files in `~/.claude/projects/` (recursively)
- Aggregates token + cost breakdown by:
  - **Model** (Opus, Sonnet, Haiku usage separately)
  - **Project** (via encoded directory path)
  - **Time window** (daily, weekly, monthly, all-time)
- Outputs: CSV, JSON, or human-readable table
- Supports: filtering by date range, project name, model

**Example output:**
```
Model              Tokens     Cost
claude-3-opus      1,234,567  $45.23
claude-3-sonnet    3,456,789  $12.34
claude-3-haiku     234,567    $0.45
---
Total: 4,925,923 tokens, $58.02
```

**Command examples:**
```bash
ccusage                           # all-time summary
ccusage --daily                   # daily breakdown (last 30 days)
ccusage --monthly                 # monthly breakdown
ccusage --project hireui          # filter by project name
ccusage --json                    # output JSON
ccusage --csv > costs.csv         # export to CSV
```

### hydai/ccstat (Rust reimplementation)

**GitHub:** `https://github.com/hydai/ccstat`  
**Language:** Rust  
**Purpose:** performance-optimized version of ccusage (faster JSONL parsing for large archives)

---

## Claude Cowork JSONL

⚠️ **Unconfirmed from first-party docs** — creator mentioned this in video but official documentation availability unverified.

**Expected behavior (from video):**
- Cowork stores JSONL in different directory: `~/Library/Application Support/Claude/local-agent-mode-sessions/`
- Uses same JSONL format as Claude Code (identical line structure)
- Stores separate JSON metadata files alongside JSONL:
  - `title` — agent name or task title
  - `folders` — workspace folders Cowork had access to
  - `processName` — the Cowork process ID
- Implication: **ccusage may need separate path config to capture Cowork sessions** (doesn't auto-discover the `~/Library` path)

**Gotcha:** if you run both Claude Code and Cowork, you need to point your cost-tracking tool to BOTH paths to get complete picture.

---

## JSONL vs. OpenTelemetry: When to Use Each

| Dimension | JSONL | OpenTelemetry |
|-----------|-------|---------------|
| **Replay fidelity** | Exact per-session transcript | Real-time aggregate metrics |
| **Storage** | Local files only | Requires backend pipeline (Grafana + Prometheus, or managed SaaS) |
| **Cost tracking** | Free (local files) | Varies by backend |
| **Plan availability** | Any plan (free, Pro, Max, enterprise) | Max + Pro only (as of June 2026) |
| **Latency** | Historical only (read after session ends) | Real-time dashboards |
| **Use case** | Audit trail, offline analysis, per-session cost | Live dashboards, team billing, observability stack |

**Decision tree:**
- **Starting out / individual dev:** use JSONL + ccusage (no dependencies, works immediately)
- **Team with infra budget:** invest in OTEL backend (Grafana) for shared dashboards
- **Both:** use JSONL for replay/audit + OTEL for real-time dashboards (complementary)

---

## Gotchas & Limitations

### Default 30-day cleanup

JSONL files auto-delete after 30 days (unless configured otherwise). If you want a cost archive:
- Set `cleanupPeriodDays: 365` in settings to retain 1 year
- Or export via ccusage periodically: `ccusage --csv > archive-$(date +%Y-%m-%d).csv`

### Project path encoding breaks on physical moves

Claude Code URL-encodes your project directory path in the JSONL filename. If you physically move a project:
- Old JSONL files stay in `~/.claude/projects/old-encoded-path/`
- New sessions create new directory with new encoding
- Sessions don't link to old history automatically

**Workaround (v2.1.169+):** use Claude Code's `/cd` command to change projects within a session (maintains session history).

### ccusage reads local JSONL only

ccusage has no visibility into:
- Anthropic's server-side overhead (invisible in token counts)
- Batch API usage (if you switch to Batch later)
- Shared team dashboards on your Anthropic account page

**Implication:** ccusage cost may diverge from official Anthropic bill. Use it for budgeting trends; check Anthropic's account page for ground truth.

### Cowork JSONL directory differs from Claude Code

If using both, cost-tracking tools may miss Cowork sessions unless you:
- Symlink `~/Library/Application Support/Claude/local-agent-mode-sessions/` → `~/.claude/projects/` (not recommended — causes confusion)
- **Better:** configure your tool to read both paths (ccusage may have a `--cowork-path` flag or config option — unconfirmed)

### `/cost` vs `/usage`/`/stats` are distinct views

`/cost` reports **session API cost/tokens** (most relevant if you use a metered API key), while `/usage` and `/stats` report **subscription** token usage against your Pro/Max plan limits. If you run on both an API key and a subscription, track both — they're separate pools. ⚠️ (The exact split/labels evolve across Claude Code versions; verify in your installed version.)

---

## Key Takeaways

- **JSONL files are your audit trail.** Every message, tool call, and token count lands in `~/.claude/projects/`. Default 30-day retention — configure `cleanupPeriodDays` if you need longer history.
- **Token fields matter:** `cache_read_input_tokens` bill ~0.1× a fresh `input_tokens` (~90% off), so cache hit rate is your #1 cost lever.
- **ccusage is the standard parser** (16.4k stars). Run `ccusage --daily` to see cost by model and project. Works offline, no setup required beyond installing it.
- **Native `/cost` and `/stats` are separate.** `/cost` = API billing; `/stats` = subscription usage quota. Monitor both if you're on a paid plan.
- **Cowork uses identical JSONL format** but stores in a different directory (`~/Library/Application Support/Claude/...`). Cost-tracking tools may need dual-path config to capture Cowork sessions.
- **JSONL excels at per-session replay and offline analysis.** OpenTelemetry excels at real-time dashboards and team sharing. Start with JSONL; add OTEL if you outgrow it.
- ⚠️ **Unconfirmed from video:** exact Cowork JSONL path, Cowork metadata file structure, ccusage Cowork-path flag — verify against current docs before relying on these for production.

---

## Related

- [[overview]] — situate JSONL in the broader observability landscape
- [[claude-code-opentelemetry]] — OTEL backends, dashboards, Max/Pro metering
- [[cost-cache-token-metrics]] — cache hit rate as primary cost lever, token anatomy
- [[../claude-api-cost-optimization/_index]] — cache strategy + cost control patterns
- [[../telegram-remote-control-stack/_index]] — task queue + approval loop as observability event source
- [[../harness-engineering/_index]] — observability as a harness property
