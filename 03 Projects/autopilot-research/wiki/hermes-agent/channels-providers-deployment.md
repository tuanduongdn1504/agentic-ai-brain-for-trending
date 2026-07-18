# Hermes Agent — Channels, Providers & Deployment

## Source
`raw/2026-07-18-hermes-agent/` (esp. t2 NetworkChuck, t6 Elestio, t1 Phan Dong Giang) + official docs. Verified via `wf_06a79485-687` (C10–C14, C16 = CONFIRMED).

## Multi-channel gateway (C10 — CONFIRMED)
- One always-running process reachable from many chat surfaces: **Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI**.
- Docs claim **"20+ platforms"** (adds Teams, Matrix, Mattermost, SMS, DingTalk, Feishu/WeCom, QQ Bot, Home Assistant, Google Chat, BlueBubbles, …). The short 6–7 list is confirmed; the full 20+ enumeration is docs-stated (not independently counted). A full **TUI** (multiline editing, slash-command autocomplete, streaming tool output) is the local interface.

## Model providers (C14 — CONFIRMED)
- **Provider-agnostic:** Nous Portal, OpenRouter, OpenAI, or **any custom endpoint** — switch with `hermes model`, no code changes, no lock-in.
- **"300+ models"** is tied to the **Nous Portal subscription** (not a property of the free software) — scope it correctly.
- **Model-by-task cost discipline** (t1, sound advice): use strong models for planning/reasoning, cheap models (e.g. DeepSeek) for crawling/gathering; costs are trackable and models swappable per task. (Cf. [[claude-api-cost-optimization|claude-api-cost-optimization]] — the 13× model-choice cost lever.)

## Deployment & sandboxing (C13, C16 — CONFIRMED)
- **6 execution/terminal backends:** local, Docker, SSH, Singularity, Modal, **Daytona** (homepage lists 5; docs add Daytona — the 6-count is authoritative). Serverless backends (Daytona/Modal) **hibernate** → near-zero idle cost.
- Runs on anything from a **$5 VPS to a GPU cluster**; native desktop apps for macOS 12+/Windows 10-11/Linux.
- **Sandboxing is built-in** — the agent runs isolated by default (t8 contrasts this with OpenClaw, where "we had to sandbox it ourselves"). *(Security threat-model — subagent isolation, exfiltration surface — is undocumented; see [[caveats-and-corrections]].)*
- **Install:** `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash` (Linux/macOS/WSL2) or PowerShell one-liner; then `hermes setup --portal`. ~60s install per docs. Requires Python 3.11, Node.js, ripgrep, ffmpeg.

## Automation primitives (C11, C12 — CONFIRMED)
- **Built-in cron scheduler** — unattended daily reports, backups, audits, channel monitoring (a live cron bug was observed — see [[learning-loop-and-self-improving-skills]]).
- **Isolated parallel subagents + Python RPC** — spawn subagents with independent conversations; call tools via Python scripts.

## The anchor's VPS walkthrough (t1) — separate the durable advice from the vendor pitch
- **Durable, sound:** don't run an autonomous agent on your personal laptop (data-exposure risk); a **VPS keeps it always-on** independent of your machine. This is good operational advice.
- **Vendor-specific / promotional (do not treat as product facts):** the "≈200,000 VND/month VPS", the **Hostinger "AI-ready" template**, and the "free 1-year token" offer are the presenter's affiliate framing, not Hermes properties. The "AI-ready = no API key needed" claim is Hostinger-template-specific.

## Key Takeaways
- Deployment is genuinely flexible and **legible**: pick a channel, pick a provider, pick a backend — all swappable, all documented, MIT-free software.
- **Provider-agnosticism + pluggable backends is the operator-relevant strength** — you control where inference happens and where the agent runs (matters for data residency).
- Watch the scope traps: "300+ models" = Nous Portal subscription; "20+ platforms" = docs-stated; VPS/Hostinger pricing = affiliate framing, not Hermes facts.
