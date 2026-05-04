# Core Product — Statusline renderer + 4 render lines + 38 config options

**Entity type:** Core product / technical architecture
**Subject:** `jarrodwatts/claude-hud` the statusline-rendering plugin itself
**First documented:** 2026-04-23 (v35 wiki creation)

---

## 1. One-sentence definition

claude-hud is a **Claude Code plugin** that consumes Claude Code's native statusline extension-point API, reads session state from stdin JSON + transcript JSONL + local config, and renders a ~2-5 line ANSI-formatted heads-up display to stdout every ~300ms.

## 2. Core metaphor

**HUD (heads-up display)** — borrowed from aviation / gaming. Pilots/players need at-a-glance awareness of critical state while hands stay on primary controls. For a Claude Code user, the analogous need is *awareness of context-budget, active tools, subagents, todos* while hands stay on conversational input.

The metaphor is apt: Claude Code users otherwise rely on `/context`, `/status`, or end-of-session artifact review to learn session state. claude-hud **surfaces that state continuously**, making it passive/ambient rather than active/query-driven.

## 3. Product scope boundaries

### In-scope (claude-hud does)
- Parse stdin JSON (model, context, tokens, rate limits, cwd, transcript path)
- Parse transcript JSONL (tool_use / tool_result pairs, Task calls = agents, TodoWrite calls = todos)
- Read local config files (user's `~/.claude/plugins/claude-hud/config.json`, plus CLAUDE.md + settings.json for counts)
- Get git status via `git` subprocess (branch, dirty, ahead/behind)
- Render ANSI-colored multi-line output to stdout
- Apply per-threshold colorization (green/yellow/red)

### Out-of-scope (claude-hud does NOT)
- Execute tools, modify files, send prompts
- Communicate with Anthropic API or any external service
- Scrape credentials, cache OAuth tokens, or read keychain (**explicitly stated by author** in README Troubleshooting)
- Persist state across invocations beyond a small context-cache
- Orchestrate subagents or workflows
- Provide methodology, teaching, or best-practice guidance

**This is a pure observer** — read-only on Claude Code state, write-only to terminal stdout.

## 4. Data flow

```
Claude Code process
    │
    │  (every ~300ms, Claude Code invokes plugin)
    ↓
claude-hud process (short-lived, stateless)
    │
    ├── Read stdin (JSON)
    │   └── model, context_window, rate_limits, transcript_path, cwd
    │
    ├── Read transcript_path (JSONL)
    │   └── tool_use + tool_result → tool activity
    │   └── Task calls → agent activity
    │   └── TodoWrite calls → todo list
    │
    ├── Read config files
    │   ├── ~/.claude/plugins/claude-hud/config.json (user HUD settings)
    │   ├── ~/.claude/settings.json (mcp count, hooks count)
    │   └── CLAUDE.md files in cwd + ancestors (rules count)
    │
    ├── Run git subprocess
    │   └── branch / dirty / ahead / behind
    │
    └── Render + write to stdout
        ↓
Claude Code displays statusline below user input
```

**Latency budget:** Each invocation must complete well under 300ms. Context-cache module (`src/context-cache.ts`) amortizes expensive calcs. Speed tracking (`src/speed-tracker.ts`) computes token/sec output rate.

## 5. Render surface — 4-5 lines maximum

### Default (2 lines, always)

**Line 1 — Project:** `[Opus] │ my-project git:(main*)`
- Model bracket (optionally provider-suffixed: `[Opus | Bedrock]`)
- Project path (configurable 1-3 directory levels)
- Git status (branch + dirty indicator + optional ahead/behind + optional file stats)

**Line 2 — Identity + Usage (merged by default):** `Context █████░░░░░ 45% │ Usage ██░░░░░░░░ 25% (1h 30m / 5h)`
- Context bar (threshold-colored: green <70% / yellow 70-85% / red >85%)
- Context percentage (or tokens, or remaining, or both)
- Usage bar for 5-hour subscriber rate limit
- Usage % + time remaining until reset
- Optional 7-day window when above threshold

### Optional lines (opt-in via `showTools` / `showAgents` / `showTodos`)

**Line 3 — Tools:** `◐ Edit: auth.ts | ✓ Read ×3 | ✓ Grep ×2`
- `◐` = running, `✓` = completed
- Running tools shown individually with target
- Completed tools aggregated by count

**Line 4 — Agents:** `◐ explore [haiku]: Finding auth code (2m 15s)`
- Agent type + model + description + elapsed time
- Multiple agents shown if running simultaneously

**Line 5 — Todos:** `▸ Fix authentication bug (2/5)`
- Current `in_progress` todo content
- Total completion count against total

### Compact mode (single-line override)

`lineLayout: "compact"` collapses to a single line, truncating aggressively based on terminal width. Useful for narrow terminals or users who want minimum footprint.

## 6. Configuration surface (~49 config keys)

**Categories:**
- Layout (6 keys): language / lineLayout / pathLevels / maxWidth / elementOrder / mergeGroups
- Git status (7 keys): enabled / showDirty / showAheadBehind / pushWarningThreshold / pushCriticalThreshold / showFileStats / branchOverflow
- Display toggles (25 keys): showModel / showContextBar / contextValue / showConfigCounts / showCost / showOutputStyle / showDuration / showSpeed / showUsage / usageBarEnabled / usageCompact / showResetLabel / timeFormat / sevenDayThreshold / externalUsagePath / externalUsageFreshnessMs / showTokenBreakdown / showTools / showAgents / showTodos / showSessionName / showClaudeCodeVersion / showMemoryUsage / showPromptCache / promptCacheTtlSeconds
- Colors (11 keys): context / usage / warning / usageWarning / critical / model / project / git / gitBranch / label / custom

**Presets (accessed via `/claude-hud:configure` guided flow):**
- **Full** — everything enabled
- **Essential** — activity lines + git
- **Minimal** — model + context bar only

Presets are starting points; per-element toggle follows.

## 7. Key source modules

| Module | Role |
|--------|------|
| `index.ts` | Entry point, orchestrates data flow |
| `stdin.ts` | Parse Claude Code's stdin JSON |
| `transcript.ts` | Parse transcript JSONL (tools/agents/todos) |
| `config.ts` | Load + validate user HUD config |
| `config-reader.ts` | Count CLAUDE.md / rules / MCPs / hooks |
| `git.ts` | Git status via subprocess |
| `context-cache.ts` | Cross-invocation cache for expensive calcs |
| `speed-tracker.ts` | Token output speed (tok/s) |
| `cost.ts` | Optional cost display |
| `memory.ts` | Optional system RAM usage |
| `external-usage.ts` | Fallback usage snapshot path |
| `i18n/` | Label tables (en, zh) |
| `render/` | Per-line renderers + ANSI color helpers |
| `utils/` | Width calc / truncation / ANSI helpers |

22 files across src/ + subdirs. **Zero runtime dependencies** (package.json has no `dependencies` field).

## 8. Technical distinctiveness vs corpus precedents

| Axis | claude-hud v35 | Prior corpus comparator |
|------|----------------|------------------------|
| Integration mode | **Statusline extension-point** | MCP server (most T4 bridges) / skill (graphify v16) / plugin command (oh-my-claudecode v27) / wrapper (deer-flow v9) |
| Runtime cadence | **~300ms invocation loop** | On-demand (most) / cron (TrendRadar v19) / long-running (OpenHands v30) |
| Lifecycle | **Stateless short-lived process** | Stateful (long-running agent harnesses) |
| Output surface | **Terminal stdout lines** | File writes / API responses / GUI (notebooklm-py's 3-surface includes CLI) |
| Write permissions | **None** (read-only observer) | Most corpus items write files/state |
| Dependency count | **0 runtime deps** | npm install dependency trees 10-100+ typical |

**This is a distinctly minimal integration pattern.** claude-hud demonstrates that Claude Code's extension-point surface can host ultra-small pure-observer plugins.

## 9. Value proposition (why it scaled to 20K in 3 months)

Hypothesized factors from Pattern #27 (Community-Viral Scale Path) signal:

1. **Immediate visible value** — user sees HUD within 5 minutes of install; benefit is obvious
2. **Zero-cost switching** — uninstall is as fast as install; no config persistence burden
3. **Addresses real pain** — context-window-exhaustion surprise is a common Claude Code failure mode
4. **Native distribution** — `/plugin marketplace add` is friction-minimal inside Claude Code session
5. **Visual screenshot sells itself** — one 2-line screenshot communicates the entire product in a README/social-post context
6. **Claude Code is rapidly adopting** — rising tide lifts utility plugins
7. **Author has social reach** — 1,075 GitHub followers + Twitter + blog (jarrodwatts.com)

No single factor alone explains 20K; the combination is sufficient.

## 10. Known limitations / honest caveats

From README + CHANGELOG:

- **Not for API-key-only users** — rate_limits data unavailable; usage display hidden
- **Bedrock/Vertex hide cost** — cloud provider billing differs from Anthropic direct
- **Memory usage is approximation** — OS cache counted as "used"
- **Prompt cache countdown is estimation** — based on transcript timestamp, not authoritative
- **Stale config silently falls back** — invalid JSON → defaults (no error, just quiet degradation)
- **~300ms cadence may lag on slow I/O** — git subprocess + JSONL parse + stdin parse must all complete

Author documents these explicitly in README; honest framing is consistent.

## 11. Cross-references

- Pattern #18 (Agent Runtime Standardization, CONFIRMED v15) — **NEW consumption mode**: extension-point-consumer (statusline API). Adds to prior MCP-consumer / skill-registration / plugin-install consumption modes.
- Pattern #20 (Solo-Scale Ceiling, CONFIRMED-REFINED v21) — NEW ROW "solo-Australian + narrow-utility-plugin + native-marketplace-distribution T1" (20K / 3.7mo).
- Pattern #27 (Community-Viral Scale Path, CONFIRMED v21) — 12th data point; native-plugin-marketplace-as-distribution sub-path.
- Pattern #59 (Plugin Marketplace Native, CANDIDATE v27) — **STRENGTHENS to N=2** at v35 (OMC + claude-hud); promotion-candidate at next mini-audit.
- Pattern #17 (Ecosystem-Layer Organizations, CONFIRMED v15) — observational: solo-one-hit-flagship within 144-repo portfolio (N=1 observational, not registered).
- Pattern #24 (SECURITY.md, CANDIDATE/STRENGTHENING) — 5th T1 data point.
- Pattern #12 (Governance-Depth Correlates with Organization) — **counter-evidence observation** (7 governance files on 3-month solo project); noted, not refined yet.

## 12. Open questions specific to Core Product

- Will the product stabilize at 4-5 render lines, or will users demand more optional lines (e.g., network latency, background agent queue)?
- If a 2nd extension-point consumer (non-statusline, e.g., a notification plugin) emerges in Claude Code ecosystem, do we refine Pattern #18 to track extension-point-type as sub-axis?
- Will npm publication ever become secondary install path, or will Jarrod commit fully to marketplace-only? (sub-variant 59b marketplace-only vs 59a marketplace-with-npm tracking.)

## 13. Provenance

- README.md analyzed 2026-04-23
- CLAUDE.md + CLAUDE.README.md analyzed 2026-04-23
- CHANGELOG.md 12 releases analyzed 2026-04-23
- GitHub API metadata fetched 2026-04-23

---

*(C) Claude-generated 2026-04-23 per routine v2.1 Phase 3.*
