# Cluster — User-facing README + install flow + 38 config options

**Sources:** `README.md` (18 KB, 379 lines) + README.zh.md (17 KB — zh port; sampled for parity check, not exhaustively read) + linked images (`claude-hud-preview-5-2.png` + `claude-hud-preview-16-9.png` — visual promo assets).

**Cluster purpose:** Captures what a user sees on day 0 — install workflow, product metaphor, configuration surface, visual promise.

---

## 1. Top-line framing

**Tagline (README first line):** *"A Claude Code plugin that shows what's happening — context usage, active tools, running agents, and todo progress. Always visible below your input."*

**Key verbs:** *shows*, *happening*, *always visible*. The product's pitch is **visibility** of internal Claude Code state that is otherwise opaque. The headline metaphor is **HUD** (heads-up display) — borrowed from aviation / gaming where pilots/players need at-a-glance awareness of critical state while hands stay on primary controls.

**Positioning contrast:** No methodology, no team, no workflow, no subagent library. Pure display-layer utility. Contrasts the 11 prior T1 corpus entrants which ALL position as broad-scope frameworks / methodologies / skill-libraries / tutorials / aggregators.

**Visual promise (embedded in README line 8):**
```
[Opus] │ my-project git:(main*)
Context █████░░░░░ 45% │ Usage ██░░░░░░░░ 25% (1h 30m / 5h)
```

2 lines default. That's the entire product surface in one screenshot.

---

## 2. 3-step install flow

```
Step 1: /plugin marketplace add jarrodwatts/claude-hud
Step 2: /plugin install claude-hud
Step 3: /claude-hud:setup
```

Then restart Claude Code. Done.

**Observations:**
- **Zero external dependencies to user** — no npm install, no pip install, no global binary, no shell script. The install happens *inside* Claude Code using Claude Code's own `/plugin` mechanism.
- **No homepage, no docs site** — all user documentation lives in README + two slash commands.
- **Auto-update model** — `/plugin` system handles updates; users never re-run `/claude-hud:setup`.

**Linux-specific caveat documented:** `/tmp` often tmpfs → plugin install fails with `EXDEV: cross-device link not permitted`. Workaround: `mkdir -p ~/.cache/tmp && TMPDIR=~/.cache/tmp claude`. Attributed to Claude Code platform issue (anthropics/claude-code#14799).

**Windows-specific caveat documented:** Setup may fail with "no JavaScript runtime found"; fix via `winget install OpenJS.NodeJS.LTS`.

**Observation:** Platform-specific workarounds in README (rather than buried in TROUBLESHOOTING) signals author takes onboarding friction seriously.

---

## 3. Product surface — 4 render lines

### Default (2 lines, always shown)

```
Line 1:  [Opus] │ my-project git:(main*)
Line 2:  Context █████░░░░░ 45% │ Usage ██░░░░░░░░ 25% (1h 30m / 5h)
```

**Line 1 elements:** Model bracket + provider label when identified (e.g., `Bedrock`, `Vertex`) + project path (configurable 1-3 directory levels) + git branch + dirty indicator (`*`).

**Line 2 elements:** Context bar (green→yellow→red ≤70/70-85/>85) + usage rate limits (5-hour and 7-day windows from subscriber rate_limits stdin field).

### Optional lines (enable via `/claude-hud:configure`)

```
Line 3:  ◐ Edit: auth.ts | ✓ Read ×3 | ✓ Grep ×2            ← Tools activity
Line 4:  ◐ explore [haiku]: Finding auth code (2m 15s)        ← Agent status
Line 5:  ▸ Fix authentication bug (2/5)                       ← Todo progress
```

**All opt-in.** The README emphasizes that default is 2-line minimalism; users pile on based on need.

---

## 4. Configuration surface (~38 options)

README contains a detailed options table. Categories:

| Category | Options (abbreviated) | Count |
|----------|----------------------|-------|
| **Layout** | `language` (en/zh), `lineLayout` (expanded/compact), `pathLevels` (1-3), `maxWidth`, `elementOrder[]`, `display.mergeGroups[]` | 6 |
| **Git status** | `gitStatus.enabled`, `showDirty`, `showAheadBehind`, `pushWarningThreshold`, `pushCriticalThreshold`, `showFileStats`, `branchOverflow` | 7 |
| **Display toggles** | `showModel`, `showContextBar`, `contextValue` (percent/tokens/remaining/both), `showConfigCounts`, `showCost`, `showOutputStyle`, `showDuration`, `showSpeed`, `showUsage`, `usageBarEnabled`, `usageCompact`, `showResetLabel`, `timeFormat`, `sevenDayThreshold`, `externalUsagePath`, `externalUsageFreshnessMs`, `showTokenBreakdown`, `showTools`, `showAgents`, `showTodos`, `showSessionName`, `showClaudeCodeVersion`, `showMemoryUsage`, `showPromptCache`, `promptCacheTtlSeconds` | 25 |
| **Colors** | `context`, `usage`, `warning`, `usageWarning`, `critical`, `model`, `project`, `git`, `gitBranch`, `label`, `custom` | 11 |

**Total: ~49 distinct config keys** when counted exhaustively. Product exposes fine-grained control but defaults to sensible 2-line minimal output.

**Presets mechanism (exposed via `/claude-hud:configure` guided flow):**
- **Full:** Everything enabled (tools/agents/todos/git/usage/duration)
- **Essential:** Activity lines + git status
- **Minimal:** Core only (model name + context bar)

After preset selection, users can toggle individual elements. **Preview before saving** is explicit UX promise.

**Manual config location:** `~/.claude/plugins/claude-hud/config.json`. Direct editing preserved by `/claude-hud:configure` for advanced settings (custom colors, thresholds, memory/promptCache options that aren't in guided flow).

---

## 5. Technical data sources (spelled out in README)

**Native token data from stdin JSON** (not estimated):
- `model.display_name` — current model
- `context_window.used_percentage` — native accurate, matches `/context`
- `context_window.current_usage.input_tokens` — current tokens
- `context_window.context_window_size` — max context (scales to 1M)
- `rate_limits.five_hour.used_percentage` / `resets_at` — subscriber rate-limit window
- `rate_limits.seven_day.used_percentage` / `resets_at` — 7-day window
- `transcript_path` — path to session JSONL

**Transcript parsing:**
- `tool_use` blocks → tool name, target, start time
- `tool_result` blocks → completion, duration
- Running tools = `tool_use` without matching `tool_result` (matched by id)
- `TodoWrite` calls → todo list
- `Task` calls → agent info

**Configuration count:**
- MCP count from `~/.claude/settings.json` (mcpServers)
- Hooks count from `~/.claude/settings.json` (hooks)
- Rules count from CLAUDE.md files in cwd + ancestors

**Usage limit caveats (honest framing):**
- Requires Claude Code subscriber rate_limits data on stdin
- NOT available for API-key-only users (they see pay-per-token, no rate-limit concept)
- AWS Bedrock displays `Bedrock`, hides usage
- Google Vertex displays `Vertex`, hides cost estimates
- "ClaudeHUD never falls back to credential scraping or undocumented API calls" — author-stated boundary (important trust signal)

**Fallback snapshot mechanism (for edge cases):**
- `display.externalUsagePath` — path to local JSON snapshot from proxy or other tool
- `display.externalUsageFreshnessMs` — max age (default 5 min) before ignored
- Stdin always wins when both sources exist

---

## 6. "How It Works" architecture blurb (README)

```
Claude Code → stdin JSON → claude-hud → stdout → displayed in your terminal
           ↘ transcript JSONL (tools, agents, todos)
```

**Key characteristic (README-asserted):** Updates every ~300ms. Uses Claude Code's native statusline API. **No separate window, no tmux required, works in any terminal.**

This is a distinctive technical positioning: **embedded in Claude Code's process lifecycle**, not a separate observer. Contrast with TrendRadar v19 (external cron service), crawl4ai v29 (external Playwright browser), or OpenHands v30 (containerized sandbox).

---

## 7. Troubleshooting section

README lists 4 common failure modes:

1. **Config not applying** — invalid JSON silently falls back to defaults; regenerate via `/claude-hud:configure`
2. **Git status missing** — verify in git repo; check `gitStatus.enabled`
3. **Tool/agent/todo lines missing** — hidden by default, must enable; also only shown when activity exists
4. **HUD not appearing after setup** — restart Claude Code; on macOS quit fully and `claude` again

**Observation:** All 4 troubleshooting items are install/config issues, NOT usage issues. The product surface is small enough that usage-level bugs are rare.

---

## 8. Explicit caveats and boundary conditions

**Features opt-in with explicit note:**
- `display.showMemoryUsage` — *"fully opt-in and only renders in `expanded` layout. It reports approximate system RAM usage from the local machine, not precise memory pressure inside Claude Code or a specific process. The number may overstate actual pressure because reclaimable OS cache and buffers can still be counted as used memory."*
- `display.showCost` — *"fully opt-in. ClaudeHUD prefers the native `cost.total_cost_usd` field that Claude Code provides on stdin when it is available. If that field is absent or invalid for a direct Anthropic session, ClaudeHUD falls back to the existing local transcript-based estimate so the cost line still works on older payloads."*
- `display.showPromptCache` — *"fully opt-in. When enabled, ClaudeHUD looks at the timestamp of the last assistant response in the local transcript and shows a live countdown until the prompt cache expires. The default TTL is 5 minutes (`300` seconds). Set `display.promptCacheTtlSeconds` to `3600` if you want a 1-hour Max-style window."*

**Author voice observation:** Honest framing — author explicitly documents approximations, hides uncertain data rather than showing misleading estimates (Bedrock/Vertex cost hidden rather than shown as `$0.00`). This is trust-signal language patterns typical of Anthropic-aligned security-conscious authorship.

---

## 9. Requirements

- Claude Code v1.0.80+
- macOS/Linux: Node.js 18+ or Bun
- Windows: Node.js 18+

**Minimal dependency story** — single runtime, no database, no external service, no secondary tool.

---

## 10. Star history + social proof

README includes Star History chart embed. No metrics beyond stars claimed. No case studies, no user testimonials, no adoption list. **Honest scoping** — the product sells itself via screenshot + install-friction minimal.

---

## Key observations for downstream phases

1. **Product is narrow and pure-utility** — no methodology, no teaching, no framework. Display-layer plugin genre.
2. **Configuration is heavy but defaulted sane** — 38+ options but 2-line default is the pitch.
3. **Install is Claude-Code-native-only** — `/plugin marketplace` is the sole install path. Corpus-first T1 for pure-marketplace distribution (oh-my-claudecode had npm companion).
4. **Technical story: stdin parser + transcript parser + 4 render functions** — small, comprehensible, well-scoped.
5. **Author voice: honest, approximation-aware, security-conscious** — matches Anthropic-aligned community norms. Bedrock/Vertex hidden rather than misleading; explicit "never falls back to credential scraping" statement.
6. **Distinctive UX: `/claude-hud:configure` guided flow** — in-Claude slash command for config-mutation vs README-only documentation. 2 slash commands total.
7. **Bilingual EN+zh (opt-in zh)** — pattern distinct from 4-language auto-exposed (claude-howto) or bilingual parallel (TrendRadar); Chinese is opt-in-via-config.
8. **Output surface is 4-5 lines maximum** — structurally bounded; impossible for surface to sprawl.
9. **The product pitch IS "visibility of Claude Code internal state"** — which means downstream analysis should highlight: (a) Claude Code runs every ~300ms statusline invocation (platform feature), (b) that stdin JSON *contains* rich state (platform feature), (c) claude-hud assembles that state into human-readable form (product feature). Value is surfacing, not computing.

---

*(C) Claude-generated 2026-04-23 per routine v2.1 Phase 2.*
