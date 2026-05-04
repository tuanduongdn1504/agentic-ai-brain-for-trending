# (C) Cluster — README + Team mode + 8 orchestration modes

> **Type:** Source cluster summary
> **Source:** README.md (25 KB, 567 lines)
> **Coverage:** Core product positioning, 8 orchestration modes, Team pipeline, CLI surface, skill library, installation, provider advisors
> **Parent:** [[(C) index]]

---

## 1. Summary

oh-my-claudecode (OMC) is a **teams-first multi-agent orchestration layer for Claude Code** — "Zero learning curve. Don't learn Claude Code. Just use OMC." Installation is 2-step (plugin marketplace add + install) or npm (`oh-my-claude-sisyphus@latest`). Core promise: multi-agent coordination without teaching users commands. Canonical surface at v4.1.7+ is **Team mode** (staged pipeline). v4.4.0+ adds tmux CLI workers (real `claude`/`codex`/`gemini` processes in split panes). v4.13.1 adds `cursor-agent` as 4th worker type.

## 2. 8 orchestration modes

| Mode | What it is | Best for |
|------|-----------|----------|
| **Team (canonical)** | Staged pipeline `team-plan → team-prd → team-exec → team-verify → team-fix (loop)` | Coordinated Claude agents on shared task list |
| **omc team (CLI)** | tmux CLI workers — real `claude`/`codex`/`gemini`/**`cursor-agent`** processes | Codex/Gemini/Cursor CLI tasks; on-demand spawn |
| **CCG** | Tri-model advisor synthesis (`/ask codex` + `/ask gemini`, Claude synthesizes) | Mixed backend+UI work |
| **Autopilot** | Autonomous execution single lead agent | End-to-end feature with minimal ceremony |
| **Ultrawork** | Maximum parallelism (non-team) | Burst parallel fixes/refactors |
| **Ralph** | Persistent mode with verify/fix loops (includes ultrawork) | Tasks must complete fully, no silent partials |
| **Pipeline** | Sequential staged processing | Multi-step transformations with strict ordering |
| **Ultrapilot (legacy)** | Deprecated compatibility alias | Existing workflows |

**Installation (marketplace-first):**
```
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
/plugin install oh-my-claudecode
```

**Installation (npm path):**
```
npm i -g oh-my-claude-sisyphus@latest
```

## 3. In-session skill surface

15+ workflow skills invocable via slash:

**Workflow:** `autopilot`, `ralph`, `ultrawork`, `team`, `ccg`, `ultraqa`, `omc-plan`, `ralplan`, `sciomc`, `external-context`, `deepinit`, `deep-interview`, `ai-slop-cleaner`, `self-improve`.

**Utilities:** `ask-codex`, `ask-gemini`, `cancel`, `note`, `learner`, `omc-setup`, `mcp-setup`, `hud`, `omc-doctor`, `omc-help`, `trace`, `release`, `project-session-manager`, `skill`, `writer-memory`, `ralph-init`, `configure-notifications`, `learn-about-omc`.

**Keyword triggers** (auto-detect): `"autopilot"` → autopilot, `"ralph"` → ralph, `"ulw"` → ultrawork, `"ccg"` → ccg, `"ralplan"` → ralplan, `"deep interview"` → deep-interview, `"deslop"` → ai-slop-cleaner, `"deep-analyze"` → analysis mode, `"tdd"` → TDD mode, `"deepsearch"` → codebase search, `"ultrathink"` → deep reasoning, `"cancelomc"` → cancel.

## 4. Team pipeline (canonical)

Stages: `team-plan → team-prd → team-exec → team-verify → team-fix (loop)`.

**Example:** `/team 3:executor "fix all TypeScript errors"` — spawns 3 executor agents.

**Enable native teams** in `~/.claude/settings.json`:
```json
{"env":{"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS":"1"}}
```

**Fix loop** bounded by max attempts. `team ralph` links both modes.

## 5. tmux CLI workers (v4.4.0+)

v4.4.0 removes Codex/Gemini MCP servers in favor of CLI-first architecture:

```
omc team 2:codex "review auth module for security issues"
omc team 2:gemini "redesign UI components for accessibility"
omc team 1:claude "implement the payment flow"
omc team status auth-review
omc team shutdown auth-review
```

Workers **spawn on-demand, die when task completes** — no idle resource usage. Requires `codex`/`gemini` CLIs + active tmux session.

**Platform tmux support:**
- macOS: `brew install tmux`
- Ubuntu/Debian: `sudo apt install tmux`
- Fedora/Arch standard
- **Windows native: psmux** (`winget install psmux`) — first Windows-native tmux-compatible binary in corpus
- Windows WSL2: tmux inside WSL

## 6. Provider Advisor (`omc ask` / `/ask`)

Run local provider CLIs, save markdown artifact under `.omc/artifacts/ask/`:

```
omc ask claude "review this migration plan"
omc ask codex --prompt "identify architecture risks"
omc ask gemini --prompt "propose UI polish ideas"
```

Canonical env vars: `OMC_ASK_ADVISOR_SCRIPT`, `OMC_ASK_ORIGINAL_TASK` (Phase-1 aliases `OMX_ASK_*` accepted with deprecation warnings).

## 7. Custom Skills architecture

Two scopes:

| | Project scope | User scope |
|---|---|---|
| Path | `.omc/skills/` | `~/.omc/skills/` |
| Shared with | Team (version-controlled) | All your projects |
| Priority | Higher (overrides user) | Lower (fallback) |

**Example skill:**
```yaml
---
name: Fix Proxy Crash
description: aiohttp proxy crashes on ClientDisconnectedError
triggers: ["proxy", "aiohttp", "disconnected"]
source: extracted
---
Wrap handler at server.py:42 in try/except ClientDisconnectedError...
```

**Management:** `/skill list | add | remove | edit | search`.
**Auto-learn:** `/learner` extracts reusable patterns with strict quality gates.
**Auto-inject:** Matching skills load into context automatically (no manual recall).

## 8. OpenClaw integration (Pattern #18 strengthening)

OMC forwards Claude Code session events to OpenClaw gateway for automated responses:

```
/oh-my-claudecode:configure-notifications
# → type "openclaw" → choose "OpenClaw Gateway"
```

**6 supported hook events:** `session-start`, `stop`, `keyword-detector`, `ask-user-question`, `pre-tool-use`, `post-tool-use`.

**Env vars:** `OMC_OPENCLAW=1`, `OMC_OPENCLAW_DEBUG=1`, `OMC_OPENCLAW_CONFIG`.

**Reply channel vars:** `OPENCLAW_REPLY_CHANNEL` (e.g., `discord`), `OPENCLAW_REPLY_TARGET`, `OPENCLAW_REPLY_THREAD`.

Reference gateway: `scripts/openclaw-gateway-demo.mjs` (relays OpenClaw → Discord via ClawdBot).

## 9. Notification tags

Telegram/Discord/Slack tags for stop callbacks:

```
omc config-stop-callback telegram --enable --token <bot_token> --chat <chat_id> --tag-list "@alice,bob"
omc config-stop-callback discord --enable --webhook <url> --tag-list "@here,123456789012345678,role:987654321098765432"
omc config-stop-callback slack --enable --webhook <url> --tag-list "<!here>,<@U1234567890>"
```

Telegram supports bare names → @names; Discord supports @here/@everyone/numeric IDs/role:ID; Slack supports `<@MEMBER_ID>`/`<!channel>`/`<!here>`/`<!everyone>`/`<!subteam^GROUP_ID>`.

## 10. 7-language README (i18n)

Links from README row 1: English | 한국어 | 中文 | 日本語 | Español | Tiếng Việt | Português. **Ties fish-speech v20** for broadest i18n in Storm Bear corpus.

**Vietnamese supported** — first T1 framework with native VN README in corpus (contrast BMAD v11 VN translation via 3rd party, codymaster v12 VN but English-first).

## 11. Key tech stack

- **TypeScript** (primary)
- **Claude Code plugin marketplace** — `/plugin marketplace add` (first in corpus)
- **npm package:** `oh-my-claude-sisyphus@latest` — **branding divergence** (repo: oh-my-claudecode; package: oh-my-claude-sisyphus)
- **tmux workers** — 4 runtime types (Claude + Codex + Gemini + Cursor-agent)
- **psmux** — Windows-native tmux compatibility
- **OpenClaw bridge** — 6 hook events, Discord/ClawdBot reference
- **MCP config** — `.mcp.json`
- **Multi-provider CLI** — Gemini CLI + Codex CLI + Cursor-agent

## 12. Cross-wiki signals

- **Pattern #18 Agent Runtime Standardization** — OpenClaw integration confirmed (Western-community 6th data point after codymaster v12 + paperclip v14 + multica v15 + graphify v16 + agency-agents v18)
- **Pattern #22 AGENTS.md** — 21 KB AGENTS.md (large end; cf. gws v13 209 lines corporate)
- **Pattern #28 Multi-Provider AI Support** — 3 native providers via CLI (Claude + Codex + Gemini + Cursor)
- **Pattern #20 Solo-Scale Ceiling** — 30K in 3.5 months (velocity factor addition)
- **Pattern #19 Multi-Lineage** — 5 inspiration sources + 2 Storm Bear corpus items

## 13. Edges + limitations

- **Zero open issues** — unusual for 30K-star 3.5-month repo. Either exceptionally active triage or new-repo curve effect.
- **npm branding divergence** — confusing for new users (`oh-my-claudecode` repo ≠ `oh-my-claude-sisyphus` npm)
- **Marketplace dependency** — requires Claude Code plugin flow; not standalone agent platform
- **tmux required** for CLI team mode — additional dep for non-tmux users
- **Documentation scattered** — docs at oh-my-claudecode.dev + docs/REFERENCE.md + docs/ARCHITECTURE.md + in-repo README + website
- **Korean-primary contributor pool** — VN users supported via i18n but governance primarily Korean

---

**Cluster signal:** OMC is a full meta-orchestration stack — not a feature addon, but a complete operating layer. 8 modes + 19 agents + 15+ skills + 4 runtimes = feature density ~2x prior largest T1 (agency-agents 144 agents but single-runtime-focus). Recursive corpus ref makes OMC unique in cited lineage.
