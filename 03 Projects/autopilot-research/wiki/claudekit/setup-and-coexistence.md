# Setup, permissions, coexistence

> Combined synthesis of `cli`, `permissions`, `hooks`, `ide-config`, `coexistence`, `migrate` source guides.

## Install

```bash
# Global CLI (requires Node.js)
npm install -g claudekit-cli
# or
bun add -g claudekit-cli

# Project initialization
cd your-project/
ck init
```

### Install modes

| Mode | Storage location | Use case |
|---|---|---|
| **Global** | `~/.claude/` | All projects share the same ClaudeKit setup |
| **Local** | `./.claude/` (project-relative) | Project-specific customizations |

### Authentication chain (in order tried)

1. `GITHUB_TOKEN` environment variable
2. `gh` CLI login state
3. OS Keychain credentials
4. Interactive prompt fallback

Required because ClaudeKit downloads kits from (possibly private) GitHub repos.

## Permission modes

### Auto Mode (recommended default)

Background classifier (Sonnet 4.6) reviews every action:
- ✅ Automatically allows safe ops (file reads, queries)
- ❌ Blocks dangerous ops (`curl | bash`, infrastructure changes)

**Caveat:** explicitly labeled "Research Preview". Not 100% reliable against hallucinations or destructive commands like `rm -rf`.

### Full Bypass (`bypassPermissions`)

Skips all confirmation prompts. **Only safe in isolated environments** (containers, VMs). Removes all safety rails.

### Custom Rules

Fine-grained allow/deny/ask rules in `settings.local.json`. Example:

```json
{
  "permissions": {
    "deny": ["Read(./.env)"],
    "ask": ["WebFetch(*)"],
    "allow": ["Read(./src/**)"]
  }
}
```

Specific tools or file paths get explicit rules.

## Hook orchestration

Hooks are shell commands triggered by Claude Code lifecycle events. Configured in `settings.json`.

### Hook capabilities

- **Context injection** — add project rules to every prompt automatically
- **Privacy blocking** — `privacy-block.cjs` denies sensitive file access pre-tool-use
- **State persistence** — `session-state.cjs` saves progress to `.claude/session-state/.last-state.md`
- **Project detection** — `session-init.cjs` loads correct env per project type
- **Auto-commit** — `git-manager` hook handles commits/PRs after approval

### Lifecycle events covered

- `SessionStart` — fires when session begins
- `PreToolUse` — before any tool execution (where privacy-block fires)
- `PostToolUse` — after tool execution
- `Stop` — when session ends or user stops

## IDE integration

Works with VS Code, Cursor, Windsurf (via the Claude Code extension).

```jsonc
// IDE settings.json
{
  "claude.environmentVariables": {
    "ANTHROPIC_BASE_URL": "http://localhost:9999/ccs",  // route through CCS
    "ANTHROPIC_MODEL": "claude-sonnet-4-6-20251001"     // or GLM, Kimi, etc.
  }
}
```

Routing IDE's Claude extension through **CCS** (Claude Code Switch) enables multi-provider usage while keeping ClaudeKit's command/hook/skill logic intact.

## Coexistence safety mechanics

ClaudeKit is designed to **not break existing Claude Code setups**:

### 1. Selective merging

Instead of overwriting `settings.json`, ClaudeKit performs a selective merge:
- Injects only its required hooks + MCP servers
- Preserves user's custom entries
- Maintains existing key-value ordering where possible

### 2. Protected files

Critical user files NOT touched by ClaudeKit:
- `CLAUDE.md` (user's behavioral instructions)
- `.gitignore`
- `.mcp.json` (MCP server config)
- `.ck.json` (user-level ClaudeKit pref)

### 3. Ownership tracking

`metadata.json` tracks which files are "ClaudeKit-owned":
- `ck update` only modifies its own files
- `ck init --fresh` resets only its own files
- User-modified files stay untouched

### 4. Conflict resolution

If a file conflict is detected during install/update, interactive mode prompts:
- Overwrite
- Smart merge (line-by-line)
- Skip

## Migration path

`ck migrate` ports ClaudeKit's intelligence layer to other AI tools.

### Supported targets

- **Cursor** — rules become `.cursorrules`
- **Windsurf**
- **Codex** (OpenAI CLI)
- **Droid**
- Several others

### Modes

| Flag | Behavior |
|---|---|
| `--install` | Manual selection of items to migrate |
| `--reconcile` | Auto-sync via checksums |
| `--dry-run` | Preview changes before any writes |

### What gets migrated

- Agent configurations (per-tool format)
- Skills (`SKILL.md` files adapted to target format)
- Rules (converted to target's native rule format)

### What does NOT get migrated

- Hooks (Claude-Code-specific concept; targets may have analog or none)
- Permissions config (target-specific)
- CCS routing (Claude-Code-only)

## Adoption decision matrix for Storm Bear users

| Your current state | Adopt ClaudeKit? | Why |
|---|---|---|
| Pure Claude Code, no harness | **Trial in 1 project** | Low-risk; explore command surface; decide based on `/ck:cook` reliability |
| Custom CLAUDE.md + a few hooks | **Adopt selectively** | Borrow command patterns; don't `ck init` if your existing setup works |
| Using harness-engineering practices | **Skip; learn from architecture** | ClaudeKit's individual-scale model conflicts with Symphony-style team workflow |
| Multi-tool stack (Cursor + Claude Code) | **Adopt for portability** | `ck migrate` is unique value-add — keep intelligence layer portable |
| Need ironclad enforcement | **Skip; add Hooks directly** | ClaudeKit's "Research Preview" auto-permission doesn't meet your bar |

For Storm Bear specifically (heavy wiki + research focus, multiple project-local CLAUDE.md files): **trial in 1 sandboxed project**, evaluate the command-borrow list from [[command-reference]], and adopt the highest-ROI patterns without committing the full framework.

## Key Takeaways

- **`ck init` is low-risk** — selective merging + protected files mean it doesn't destroy existing setup
- **Auto-permission mode is convenient but Research Preview** — not 100% safe; use VM/container for destructive work
- **`ck migrate` is portability superpower** — no other framework moves your intelligence layer this seamlessly
- **CCS multi-provider routing** is unique to ClaudeKit — Claude Code native doesn't have this
- **Coexistence model (selective merge + ownership tracking)** is itself an architectural pattern worth borrowing for any framework that overlays on top of native config
