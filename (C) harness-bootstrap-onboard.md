# Harness Bootstrap Onboard

This file documents how to reproduce the current Storm Bear multi-provider harness on another Mac after pulling this repo.

It is intentionally local-machine oriented. The harness state lives in home-directory config files, not in Git:

- `~/.claude/settings.json`
- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `~/.gemini/settings.json`
- `~/.ping-island/bin/ping-island-bridge`
- `~/.ping-island/bridge-config.json`

Do not commit those dotfiles into this public vault. They can contain machine-specific paths, hook trust hashes, auth state, or provider/account assumptions.

## Target Behavior

After bootstrap, a fresh device should have the same provider coverage as this Mac:

| Provider | AgentPet | Ping-Island |
|---|---:|---:|
| Claude Code | 7 hooks | 10 hook keys |
| Codex | 7 hooks | 7 hooks |
| Antigravity/Gemini | 7 hooks | 7 hooks |

Codex hook trust is deliberately generated on each device. The script does not copy trusted hashes because they are machine-local trust state.

## Prerequisites

Install these first:

- Claude Code
- Codex CLI
- Antigravity IDE
- Obsidian
- AgentPet
- Ping Island
- `jq`

Expected app paths:

```bash
/Applications/AgentPet.app
/Applications/Ping Island.app
/Applications/Antigravity IDE.app
/Applications/Obsidian.app
```

Expected CLI paths after installation:

```bash
~/.local/bin/claude
~/.local/bin/codex
```

## First Run On A New Device

Clone the vault:

```bash
mkdir -p ~/Agentic
cd ~/Agentic
git clone https://github.com/tuanduongdn1504/agentic-ai-brain-for-trending.git
cd agentic-ai-brain-for-trending
```

Preview the bootstrap:

```bash
bash "scripts/(C) harness-bootstrap-onboard.sh" --dry-run
```

Apply it:

```bash
bash "scripts/(C) harness-bootstrap-onboard.sh" --yes
```

Optional verification:

```bash
bash "scripts/(C) harness-bootstrap-onboard.sh" --verify
```

## What The Script Does

- Backs up touched files under `~/.storm-bear-harness-backups/<timestamp>/`
- Writes the Ping-Island bridge wrapper at `~/.ping-island/bin/ping-island-bridge`
- Writes `~/.ping-island/bridge-config.json`
- Replaces the `.hooks` object in `~/.claude/settings.json`
- Replaces the `.hooks` object in `~/.gemini/settings.json`
- Replaces the `.hooks` object in `~/.codex/hooks.json`
- Ensures `~/.codex/config.toml` marks this repo path as trusted
- Does not copy auth tokens, API keys, model settings, or Codex hook trusted hashes

## Codex Trust Step

After applying the bootstrap, start Codex from the repo and approve the new hooks when prompted:

```bash
cd ~/Agentic/agentic-ai-brain-for-trending
codex
```

Then confirm trusted hashes exist:

```bash
rg -n "post_tool_use|subagent_stop|pre_tool_use|permission_request|session_start|user_prompt_submit|stop" ~/.codex/config.toml
```

## Verification Commands

Check JSON validity:

```bash
jq empty ~/.codex/hooks.json
jq empty ~/.claude/settings.json
jq empty ~/.gemini/settings.json
```

Check Codex hook matrix:

```bash
jq -r '.hooks | to_entries[] | .key as $event | .value[]? | .hooks[]? | [$event, .command] | @tsv' ~/.codex/hooks.json
```

Run Codex doctor:

```bash
codex doctor --summary --ascii --no-color
```

`TERM=dumb` can make `codex doctor` exit nonzero in noninteractive shells. That is not a harness failure by itself. The important checks are that config loads, auth is configured, and provider endpoints are reachable.

## Blunt Boundary

This bootstrap is for personal machine parity, not a managed product installer. If an app changes its hook schema, rerun verification before trusting the result.

Suggested next action: after running this on a new device, open Codex once, approve hook trust, then run `codex doctor --summary --ascii --no-color`.
