# Layer 4 — Network (tunneling, VPN, VPS)

How a Telegram message physically reaches the machine running Claude Code. Five competing options + Wolfgang's contrarian "don't tunnel at all" view.

## The reachability problem

Your Telegram bot listens on Telegram's servers. Your Claude Code runs on your laptop or home server. Telegram needs to reach Claude when a message arrives. Three architectural shapes:

1. **Outbound only** (most flexible) — Claude polls Telegram for new messages. Works behind any NAT/firewall. No inbound tunnel needed. **This is what `claude --channels` actually does** — confirms why Channels has zero networking config.
2. **Inbound webhook** — Telegram pushes to your machine. Requires public IP or tunnel. Lower latency.
3. **Hybrid via VPS** — Claude runs on a public-IP VPS. Telegram pushes there. You SSH in for monitoring.

For most operators, **Channels solves Layer 4 entirely** (outbound polling) and you can skip this article. Read on if:
- You need inbound webhooks (lower latency, advanced cases)
- You're running custom MCP servers that need inbound (Layer 3 § fastmcp pattern)
- You want phone access to your home machine for OTHER things (SSH, file sync, web UIs)

## Option 4A — Tailscale (recommended default for solo + private)

Mesh VPN. Each device gets a stable IP on a private overlay network. No port forwarding, no public exposure.

### Why it shines
- **Private** — your phone and home machine can talk; nobody else can.
- **Free tier generous** — 100 devices, 3 users for personal use.
- **Mobile app excellent** — runs in the background on iOS/Android, just-works.
- **No upload limits** — unlike Cloudflare Tunnels (Thomas Wilde's stated reason for picking Tailscale).

### Setup (5 min)
```bash
# On home machine
brew install tailscale
sudo tailscale up

# On phone
# Install Tailscale app, sign in with same Google/GitHub account.

# Now the home machine is reachable at e.g. 100.64.0.5 from your phone
# Telegram bot listening on home machine; you SSH/curl from phone via Tailscale IP
```

### Best fit
- Solo operator, all-personal use
- Stricter privacy than Cloudflare Tunnel
- Combination of Telegram remote-control + ad-hoc SSH/file access

## Option 4B — Cloudflare Tunnel (recommended for public-facing)

Cloudflare hosts a tunnel endpoint; your home machine establishes outbound connection to it. External users (or Telegram) hit the public Cloudflare URL, which routes to your machine.

### Why it shines (logicBase Labs, Thomas Wilde)
- **No port forwarding** required — works behind any NAT
- **No public IP exposure** — Cloudflare's IP is the public face
- **Free tier** for personal use
- **Cloudflare Access** for Zero Trust auth (email-based gating before requests reach your tunnel)

### Setup
```bash
# On home machine
brew install cloudflared
cloudflared tunnel login
cloudflared tunnel create my-tunnel
cloudflared tunnel route dns my-tunnel myapp.mydomain.com
cloudflared tunnel run my-tunnel
```

### Best fit
- Public-facing service (your bot or a webhook URL must be public)
- You already use Cloudflare for DNS
- You want Zero Trust auth layer (Cloudflare Access)

### Watch-outs (Craylor)
- **"Not for beginners"** — DNS management has a learning curve
- Dependency on Cloudflare's ToS — they can revoke
- Per-account upload limits on free tier (this is why Wilde prefers Tailscale)

## Option 4C — Twingate (Zero Trust overlay)

NetworkChuck's recommendation. Similar to Tailscale (mesh) but with stricter Zero Trust policy enforcement.

### Why it shines
- **Per-resource auth** — phone can reach only `home-machine:22` (SSH), not the rest of the home network
- **Replaces traditional VPN** for many use cases
- Works through any NAT

### Setup
- Sign up Twingate account
- Install agent on home machine, register as "resource"
- Install client on phone, sign in
- Configure resource policies (which user can reach what)

### Best fit
- Team scenario where multiple operators have different access levels
- Tighter security than Tailscale's full-mesh-trust

### Trade-off
- Less plug-and-play than Tailscale
- Free tier more limited
- Setup learning curve for multi-resource policies

## Option 4D — VPS + tmux (NetworkChuck's "Forever Terminal")

The cloud-host approach. Don't tunnel home; just put Claude on a VPS.

### Stack
- **Hostinger / DigitalOcean / Linode VPS** (~$5/mo for small)
- **tmux** keeps sessions alive across SSH disconnects
- **UFW firewall** allows port 22 only
- **Fail2Ban** brute-force protection
- **SSH key auth** (password disabled)
- **Terminus** mobile app for SSH from phone

### Setup (NetworkChuck's outline)
```bash
# 1. Provision VPS
# 2. SSH in, install: tmux, ufw, fail2ban, claude-code
sudo ufw allow 22
sudo ufw enable
# 3. Disable password auth in /etc/ssh/sshd_config
# 4. Install fail2ban
# 5. Install Claude Code, configure Channels plugin
# 6. tmux new -s claude
#    claude --channels
#    Ctrl-B D (detach)
# 7. From phone: SSH via Terminus, attach session
```

### Why it shines
- **Truly always-on** — VPS doesn't sleep, doesn't lose power
- **Wherever access** — works from any internet, no tunnel needed
- **Low cost** — $5/mo + Anthropic API

### Trade-offs
- **Code lives on someone else's machine** — privacy loss if working on sensitive code
- **Ongoing maintenance** — patching, monitoring, security
- **No GPU** — if your work uses local ML/file caching, VPS may not fit

## Option 4E — Wolfgang's local-first contrarian view

Wolfgang explicitly argues **AGAINST** third-party tunnels.

### His argument
- Cloudflare Tunnels mean **data egresses your home network** every time someone reaches the service
- Tunnels create **dependencies on the third party** — Cloudflare misconfiguration risks, persistent internet requirement
- Better to use **DNS-01 verification** with a reverse proxy + valid SSL, keeping all traffic local until explicitly needed

### His stack
- **Nginx Proxy Manager** as reverse proxy
- **DNS-01 challenge** for Let's Encrypt SSL (no public-facing endpoint needed)
- **Wildcard cert** covering all subdomains
- Phone reaches home via **Tailscale** or self-hosted VPN (NOT Cloudflare Tunnel)

### Why it matters for Telegram remote-control
If you're worried about a third party (Cloudflare, Twingate, even Tailscale) being a man-in-the-middle for your Telegram bot's outbound calls, Wolfgang's stack minimizes the trust surface. The Telegram messages still go through Telegram's servers (unavoidable), but the rest of the stack stays in your control.

## Tooling matrix

| Tool | Pattern | Best for | Free tier |
|---|---|---|---|
| **Tailscale** | mesh VPN | solo + private + personal | 100 devices, 3 users |
| **Cloudflare Tunnel** | outbound tunnel + public face | public webhook, team | yes (personal) |
| **Twingate** | Zero Trust overlay | team + per-resource auth | limited |
| **ngrok** | quick public tunnel | dev/demo only | yes (warning: random URL on free) |
| **VPS + SSH** | move work off home | always-on, no tunnel | $5/mo + |
| **Self-hosted VPN (WireGuard, OpenVPN)** | DIY private tunnel | privacy maximalist | free (your hardware) |

## Hardening (NetworkChuck's checklist for VPS)

If running Layer 4D (VPS):

```bash
# 1. UFW firewall, deny by default, allow only 22
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22
sudo ufw enable

# 2. Disable root login + password auth
# Edit /etc/ssh/sshd_config:
PermitRootLogin no
PasswordAuthentication no

# 3. SSH key auth
ssh-copy-id user@vps   # from your laptop, before disabling passwords!

# 4. Fail2Ban
sudo apt install fail2ban
sudo systemctl enable fail2ban

# 5. Automatic security updates
sudo apt install unattended-upgrades
sudo dpkg-reconfigure --priority=low unattended-upgrades
```

This is the minimum hygiene. Add log aggregation + uptime monitoring for production. See [[gaps-production]].

## Container layer (Techno Tim)

Techno Tim's overlay: run everything in **Docker** with **pinned versions** (not `latest`). Reasons:
- Reproducibility — `1.21.5-alpine` builds the same forever
- Stability — `latest` may not have gone through your testing
- Forensics — pinned version = you know what code ran when an incident happened

This applies to your Telegram bot, MCP servers, reverse proxy, etc. The Claude Code process itself is harder to containerize cleanly (per current Anthropic guidance) — keep it on the host.

## When to skip Layer 4 entirely

If you're using `claude --channels` for the Telegram interface AND not running custom inbound webhooks AND not needing phone-to-machine access for other reasons — you don't need this layer. Channels' outbound polling handles reachability.

This is the simplest setup. Default to it. Add Layer 4 complexity only when you hit a specific need.

## Cross-references

- [[overview]] § decision matrix — which Layer 4 fits your recipe
- [[layer-1-interface-telegram]] — Channels' outbound model that obviates this layer for many setups
- [[operator-recipes]] — concrete recipes that include each Layer 4 choice
- [[gaps-production]] § HA + secrets + observability — what's missing across all options
