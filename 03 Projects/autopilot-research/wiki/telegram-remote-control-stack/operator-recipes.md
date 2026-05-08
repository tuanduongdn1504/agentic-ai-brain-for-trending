# Operator Recipes — 4 end-to-end concrete builds

Skip the layer-by-layer theory. These are 4 complete recipes you can adopt today, copy-paste-style. Each names every tool, every command, every config file.

## Recipe A — Solo + best-effort + free-tier (the 30-min starter)

**Goal:** message your Mac/PC from Telegram, get Claude Code to run a command, see the output. No always-on guarantee. No public exposure.

### Stack
| Layer | Choice |
|---|---|
| 1. Interface | Telegram + Claude Code Channels official plugin |
| 2. Engine | Claude Code in warm `--channels` mode |
| 3. Integration | Native Channels plugin (no separate MCP) |
| 4. Network | None needed — Channels uses outbound polling |

### Steps (verified pilot 2026-05-08 — see [[setup-recipe-a]] for full deviations)

```bash
# Prereqs (verify ALL before starting):
command claude --version       # must NOT show "native binary not installed"
command bun --version          # REQUIRED — plugin's MCP server is server.ts
command brew --version         # for installing Bun cleanly

# If bun missing:
command brew install oven-sh/bun/bun

# 1. Open Telegram, DM @BotFather, send /newbot, follow prompts
#    Save the API token (looks like: 8123456789:AAH-Abcdef...)

# 2. Add the marketplace (REQUIRED — not implicit)
command claude plugin marketplace add anthropics/claude-plugins-official

# 3. Install plugin
command claude plugin install telegram@claude-plugins-official
command claude plugin list   # verify enabled

# 4. Configure with bot token
command claude     # opens REPL
# inside REPL:
> /telegram:configure 8123456789:AAH-Abcdef...
# exit REPL: /quit

# 5. Launch Channels listener (warm session)
command claude --channels plugin:telegram@claude-plugins-official

# 6. Verify Bun MCP server actually started (in a 2nd terminal)
command ps aux | command grep -E "(bun|server\.ts)" | command grep -v grep
# expect: 1 line for `bun server.ts` AND 1 for `bun run --cwd ... start`

# 7. From Telegram, find @your_bot, send any message
#    Receive a 6-character pairing code (e.g., 76a7e5)
#    Back in Claude REPL:
> /telegram:access pair 76a7e5

# 8. LOCK DOWN IMMEDIATELY
> /telegram:access policy allowlist
> /telegram:access show     # verify dmPolicy: allowlist
```

### Test
From Telegram, message: `pwd` — bot should reply with the working dir of your `claude --channels` process within ~5-10 sec.

### ⚠️ The 5 deviations from internet tutorials

Older tutorials (Chris Verzwyvelt, Kumo Explains, even some 2026 Q1 blog posts) reference commands that **don't work** with the current 2.1.x Claude Code + plugin v0.0.6. See [[setup-recipe-a]] § Deviations for the full list. Quick summary:

1. Plugin name is `telegram@claude-plugins-official`, not `claude-code-telegram-plugin-official`
2. Marketplace must be added explicitly: `claude plugin marketplace add anthropics/claude-plugins-official`
3. **Bun runtime is a hard prereq** — without it, banner shows "Listening" but server never starts (silent failure)
4. Native Claude binary postinstall sometimes fails — fix with `npm install -g @anthropic-ai/claude-code --include=optional`
5. Pair syntax is `/telegram:access pair <code>` (single command), not `/telegram:access pair` then prompt
6. Lock-down is `/telegram:access policy allowlist` (no hyphen, no spaces), not `/telegram:access-policy allow-list`

The pilot caught all of these — see [[setup-recipe-a]] for the full debug story.

### Use cases this fits
- Hobby projects, personal experiments
- "Check on my long-running build from the coffee shop"
- Solo dev, machine on at home/office

### Limitations
- Mac sleeps when lid closes — message-while-asleep gets dropped
- No audit log
- Bot token in plain-text config
- If your IP changes (DHCP), the polling reconnects but there's a gap

## Recipe B — Solo + 99% + ~$10/month (the always-on)

**Goal:** Telegram remote-control runs reliably even when your laptop is off, on a $5-10/mo VPS, with hardened security.

### Stack
| Layer | Choice |
|---|---|
| 1. Interface | Telegram via Channels |
| 2. Engine | Claude Code on VPS, tmux for session persistence |
| 3. Integration | Channels + 1-2 specific MCPs (e.g., GitHub) |
| 4. Network | VPS + SSH-key + UFW + Fail2Ban |

### Steps

```bash
# 1. Provision VPS
#    Hostinger / DigitalOcean / Linode — Ubuntu 22.04, 1 vCPU, 1GB RAM
#    Save the IP

# 2. From your laptop, copy your SSH public key to the VPS
ssh-copy-id user@<vps-ip>

# 3. SSH in
ssh user@<vps-ip>

# 4. Harden (NetworkChuck's checklist)
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22
sudo ufw enable

sudo nano /etc/ssh/sshd_config
# Set: PermitRootLogin no
#      PasswordAuthentication no
sudo systemctl restart ssh

sudo apt update && sudo apt install -y fail2ban tmux unattended-upgrades
sudo dpkg-reconfigure --priority=low unattended-upgrades

# 5. Install Claude Code
#    Follow Anthropic's current install instructions for Linux
#    Authenticate (will need browser flow — use ssh -L for port forward, or auth on the VPS via web)

# 6. Set up Telegram bot (same as Recipe A: BotFather → token → /telegram:configure)

# 7. Launch in tmux for persistence
tmux new -s claude
claude --channels
# Ctrl-B then D (detach)

# 8. Lock down
#    Reattach: tmux attach -t claude
#    Run /telegram:access-policy allow-list inside Claude

# 9. (Optional) Auto-restart on reboot
#    Create a systemd service that runs `tmux new-session -d -s claude 'claude --channels'`
#    on boot. Without this, a VPS reboot leaves your bot offline until manual restart.
```

### From your phone

- **Terminus app** (or any SSH client) for direct VPS shell access
- **Telegram** for Claude Code remote-control via the bot

### Cost
- VPS: $5-10/month
- Anthropic API: usage-based (~$10-50/month for moderate use)
- Total: ~$15-60/month

### Limitations
- Code lives on rented hardware — privacy loss for sensitive projects
- Manual systemd setup needed for auto-restart on reboot
- API token still in plain-text config

## Recipe C — Small team + private + 99.9% (the homelab)

**Goal:** team of 3-5 share remote-control to a home-server-hosted Claude Code. No third-party tunneling. Per-user access scoping.

### Stack
| Layer | Choice |
|---|---|
| 1. Interface | Discord (User-ID + Channel-ID scoping) |
| 2. Engine | Claude Code on a dedicated home server (Mac mini / NUC / micro-server) |
| 3. Integration | Custom `fastmcp` server for IAM hooks + audit logging |
| 4. Network | Tailscale (no Cloudflare, no public surface) |

### Steps

```bash
# 1. Dedicated home server (Mac mini sufficient — Chris Verzwyvelt's recommendation)
#    Wired ethernet, UPS for power resilience, scheduled wake-from-sleep if Mac

# 2. Install Tailscale on the server AND every team member's phone
sudo tailscale up
# Each phone: install Tailscale app, sign in with team's Tailscale account

# 3. Install Claude Code, set up Discord bot
#    Discord developer portal: enable "Message Content Intent"
#    /discord:configure with bot token

# 4. Configure access.json with team User IDs + Channel IDs
#    e.g., #claude-prod restricted to 2 senior engineers
#          #claude-dev open to whole team

# 5. Custom fastmcp server for IAM (optional but recommended)
#    Wraps the Discord plugin
#    Adds: per-command permission checks, audit log to file/Datadog
#    See: layer-3-mcp-integration § Flavor 3B

# 6. tmux + systemd auto-restart (as Recipe B)

# 7. Periodic backups of audit logs + agents.md to private cloud
```

### Why Tailscale (not Cloudflare)
Wolfgang's argument applies: data stays on your network. No third-party in the path between team phone and home server (other than Tailscale's coordination plane, which doesn't see traffic content).

### Why Discord (not Telegram)
Channel-scoping. `#claude-prod` can be senior-only; `#claude-dev` can be team-wide. Telegram's allow-list is User-ID-only, so you can't easily say "everyone can use the dev bot but only seniors can use prod".

### Cost
- Hardware: one-time ~$500-1500
- Tailscale: free for personal team use (≤3 users); ~$5/user/month for more
- Anthropic API: shared, depends on team usage
- Total ongoing: ~$0-30/month + API

### Limitations
- One physical server = single point of failure (mitigate with hardware redundancy or hot standby)
- Custom fastmcp server is dev work to build/maintain (~1 day initial + ongoing)
- Team has to install Tailscale on every device (one-time onboarding friction)

## Recipe D — Observation-only (NO command execution from phone)

**Goal:** receive Telegram notifications when Claude finishes tasks or hits errors — but the phone CANNOT execute commands. Pure read-only awareness.

### Stack
| Layer | Choice |
|---|---|
| 1. Interface | Telegram bot (one-way notifications) |
| 2. Engine | Claude Code as monitoring sidecar with Stop Hooks |
| 3. Integration | Stop Hooks fire to a Telegram webhook |
| 4. Network | Outbound only — no inbound needed |

### Steps

```bash
# 1. Create a Telegram bot via BotFather (same as Recipe A)
#    Save the token + your personal chat ID (use @userinfobot to find your chat ID)

# 2. Create a notify script
cat > ~/.claude/notify-telegram.sh <<'EOF'
#!/bin/bash
TOKEN="YOUR_BOT_TOKEN"
CHAT_ID="YOUR_CHAT_ID"
MESSAGE="$1"
curl -s -X POST "https://api.telegram.org/bot${TOKEN}/sendMessage" \
  -d "chat_id=${CHAT_ID}" \
  -d "text=${MESSAGE}"
EOF
chmod +x ~/.claude/notify-telegram.sh

# 3. Wire as a Claude Code hook
#    See: ../claude-code-hooks/_index for hook lifecycle events
#    Pattern: register a Stop hook that calls notify-telegram.sh with the relevant message

# 4. Run Claude Code normally (not --channels)
claude
# Long task; on completion, Stop hook fires; phone gets a Telegram message
```

### Why this fits a paranoid operator
- Bot token only allows OUTBOUND messages from your machine — even if leaked, nobody can use it to control your machine
- Bot has no chat-back capability
- Whole stack is opt-out by default — simple to disable
- No allow-lists to manage, no auto-approve risks, no tunnels

### Limitations by design
- You can't issue commands from the phone — only see notifications
- Adding a "reply to fix" flow would graduate this to Recipe A (and re-introduces the security model of Recipe A)

## Cross-references

- [[overview]] — the 4-layer architecture and decision matrix
- [[layer-1-interface-telegram]] — interface details for Recipes A/B/C
- [[layer-2-engine-headless-claude-code]] — Stop Hooks for Recipe D
- [[layer-3-mcp-integration]] — fastmcp custom servers for Recipe C
- [[layer-4-network-tunneling]] — Tailscale vs VPS vs Cloudflare comparison
- [[gaps-production]] — when these recipes hit limits, what to upgrade
