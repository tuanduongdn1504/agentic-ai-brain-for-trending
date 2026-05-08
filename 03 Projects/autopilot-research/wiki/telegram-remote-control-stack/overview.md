# Overview — Telegram Remote-Control Stack

## The operator goal

Send a message from your phone (in Telegram) → trigger an action in Claude Code/Desktop running at home → receive results back in Telegram. While AFK. Securely. Without babysitting.

This is the explicit goal stated by every Telegram-focused creator in the bundle (Chris Verzwyvelt, Mervin Praison, Kumo Explains, Developers Digest, NetworkChuck × 2). The phrasing varies — "always-on AI agent", "remote terminal", "Forever Terminal" — but the mechanism converges on one stack:

```
┌──────────────────────────────────────────────────────────────────┐
│                     YOUR PHONE                                   │
│                  (Telegram app)                                  │
└──────────────────────┬───────────────────────────────────────────┘
                       │
                  encrypted
                  internet
                       │
┌──────────────────────▼───────────────────────────────────────────┐
│  LAYER 1 — Interface       (telegram bot / discord / native)     │
│  see: layer-1-interface-telegram                                 │
└──────────────────────┬───────────────────────────────────────────┘
                       │
                  message →
                  command
                       │
┌──────────────────────▼───────────────────────────────────────────┐
│  LAYER 2 — Engine          (headless Claude Code SDK + ralph)    │
│  see: layer-2-engine-headless-claude-code                        │
└──────────────────────┬───────────────────────────────────────────┘
                       │
                  tool calls
                  via MCP
                       │
┌──────────────────────▼───────────────────────────────────────────┐
│  LAYER 3 — Integration     (MCP plugins / channels / fastmcp)    │
│  see: layer-3-mcp-integration                                    │
└──────────────────────┬───────────────────────────────────────────┘
                       │
                  network
                  reachability
                       │
┌──────────────────────▼───────────────────────────────────────────┐
│  LAYER 4 — Network         (tailscale / tunnel / VPN / VPS)      │
│  see: layer-4-network-tunneling                                  │
└──────────────────────────────────────────────────────────────────┘
```

Each layer has multiple competing implementations. The 4 articles below the stack diagram each go deep on one layer's options + trade-offs.

## What changed in 2026 — Channels + Remote Control

Two Anthropic-native features dropped that compressed the stack significantly:

1. **Claude Code Channels** (the `--channels` flag with `claude-code-telegram-plugin-official` and Discord equivalent) — turns Layer 1+3 into a single official integration. Before: build your own bot with python-telegram-bot or fastmcp. After: one plugin install + BotFather token. Chris Verzwyvelt explicitly calls Channels the **"OpenClaw killer"**.
2. **Native Remote Control** (the `/remote-control` command) — resume your laptop's Claude Code session directly inside the **native Claude mobile app**. No VPN, no tunnel, no bot. Anthropic handles the bridge. NetworkChuck calls this "a glimpse into the future".

These two features overlap functionally but solve different problems:
- **Remote Control** = manual interaction. Resume a session, type, see output. Replaces SSH-from-phone.
- **Channels** = automated reaction. Bot listens for events (CI failure, GitHub PR comment, cron). Fires Claude. No human in the loop.

Developers Digest articulates this distinction clearly: Remote Control is *manual*, Channels are *reactive*. You may want both.

## Decision matrix — pick your path

The 4 layers each have ≥3 competing options. Picking the right combination depends on 4 variables:

| Variable | Options |
|---|---|
| **Team size** | solo / small team (≤5) / org |
| **Privacy needs** | strict (no third-party tunnel) / standard / public-OK |
| **Availability needs** | best-effort / 99% / 99.9% |
| **Budget** | free-tier only / <$50/mo / >$100/mo |

Four common combinations:

### Recipe A — solo + best-effort + free-tier (most common starting point)
- **Layer 1:** Telegram bot via Claude Code Channels official plugin
- **Layer 2:** Claude Code on your Mac/PC (laptop OK; lid-open with `caffeinate`)
- **Layer 3:** native Channels integration (no separate MCP server needed)
- **Layer 4:** Tailscale (free tier) for phone↔home reachability OR `/remote-control` (no tunnel)
- **Cost:** $0/month
- **Limitation:** machine must be on; signal drops break sessions; no audit log

### Recipe B — solo + 99% + <$50/mo (always-on)
- **Layer 1:** Telegram bot via Channels
- **Layer 2:** Claude Code on a VPS (Hostinger ~$5/mo per NetworkChuck) OR Mac Mini at home
- **Layer 3:** Channels + Telegram MCP for proactive monitoring
- **Layer 4:** Cloudflare Tunnel + UFW + Fail2Ban + SSH keys + tmux for session persistence
- **Cost:** ~$5-30/month VPS + Anthropic API
- **Validation:** see [[operator-recipes]]

### Recipe C — small team + strict-privacy + 99.9%
- **Layer 1:** Discord bot (channel-scoped, multi-user) OR self-hosted Telegram client
- **Layer 2:** Claude Code on a private homelab server
- **Layer 3:** Custom `fastmcp` server (Samir Kharel pattern) for IAM hooks
- **Layer 4:** Tailscale or Twingate (Zero Trust overlay, no public surface)
- **Cost:** depends on hardware; Anthropic API
- **Validation:** Wolfgang's local-first stance — see [[layer-4-network-tunneling]] § contrarian view

### Recipe D — observation-only (NO command execution from phone)
- **Layer 1:** Telegram bot (one-way notifications only)
- **Layer 2:** Claude Code as monitoring sidecar (no auto-execute)
- **Layer 3:** Stop Hooks (see [[../claude-code-hooks/_index|Claude Code hooks]]) that fire to Telegram on events
- **Layer 4:** any — outbound only
- **Cost:** $0
- **Use case:** "tell me when build fails" — no remote control, just remote awareness

## Critical safety knobs

Across every bundle, three security knobs come up:

1. **Allow-list immediately after pairing** — `/telegram:access-policy allow-list` (Chris Verzwyvelt: "lock this baby down"). Prevents random Telegram users from controlling your terminal once your bot's username leaks.
2. **Auto-approve mode is a footgun** — Kris Torrington advocates auto-approving all tool calls for convenience. Kumo Explains keeps manual approval. **If the agent can run arbitrary shell commands AND auto-approves, anyone with bot access has root on your machine.** Pair auto-approve with strict allow-list AND command scoping.
3. **Cap autonomous loops** — Developers Digest warns autonomous loops must have `max_iterations` to prevent runaway token burn. See [[layer-2-engine-headless-claude-code]] § Ralph loop safety.

## How to read the rest

- Pick the layer most uncertain to you and read that article first.
- [[operator-recipes]] has end-to-end recipes if you'd rather skip layer theory.
- [[gaps-production]] is the exit ramp if you're going beyond solo/team scale.
