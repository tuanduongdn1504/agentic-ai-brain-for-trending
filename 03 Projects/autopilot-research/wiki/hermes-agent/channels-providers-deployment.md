# Hermes Agent — Channels, Providers & Deployment

## Source
`raw/2026-07-18-hermes-agent/` (esp. t2 NetworkChuck, t6 Elestio, t1 Phan Dong Giang) + official docs. Verified via `wf_06a79485-687` (C10–C14, C16 = CONFIRMED).

## Multi-channel gateway (C10 — CONFIRMED)
- One always-running process reachable from many chat surfaces: **Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI**.
- ⚠️ **"20+ platforms" is DOWNGRADED to UNVERIFIABLE as of 2026-09-03 — do not cite it.** The README (fetched verbatim, 17,688 bytes, 2026-09-03) contains **no "N platforms" string at all** and enumerates only **8 entry points** across its three lists: **Telegram, Discord, Slack, WhatsApp, Signal, Email, Home Assistant, and the CLI/terminal UI**. The docs site that previously carried the "20+" figure is now a JavaScript skeleton to `curl` and cannot be read. Treat 8 as the confirmed floor and "20+" as a 2026-07-18 docs-assertion with no current corroboration.
- **WeChat is NOT a first-party platform.** The README lists `HermesClaw` under *community* projects — "Community WeChat bridge", by a third party (`AaronWong1999/hermesclaw`). Any source presenting WeChat/iMessage as built-in is wrong (graded FALSE — [[revisit-2026-09-03]]).
- A full **TUI** (multiline editing, slash-command autocomplete, streaming tool output) is the local interface.
- **Windows is native — corrected 2026-09-03.** A source claiming "Windows support requires WSL 2" is **FALSE**: the README ships a native PowerShell installer (`iex (irm https://hermes-agent.nousresearch.com/install.ps1)`). WSL2 is an alternative, not a requirement.

## Model providers (C14 — CONFIRMED)
- **Provider-agnostic:** Nous Portal, OpenRouter, OpenAI, or **any custom endpoint** — switch with `hermes model`, no code changes, no lock-in.
- **"300+ models"** is tied to the **Nous Portal subscription** (not a property of the free software) — scope it correctly.
- **Model-by-task cost discipline** (t1, sound advice): use strong models for planning/reasoning, cheap models (e.g. DeepSeek) for crawling/gathering; costs are trackable and models swappable per task. (Cf. [[claude-api-cost-optimization|claude-api-cost-optimization]] — the 13× model-choice cost lever.)

## Deployment & sandboxing (C13, C16 — CONFIRMED)
- **7 execution/terminal backends (was 6 — updated 2026-09-03):** local, Docker, SSH, Singularity, Modal, **Daytona**, and **Vercel Sandbox** (NEW). README v0.21.0 verbatim: *"Seven terminal backends — local, Docker, SSH, Singularity, Modal, Daytona, and Vercel Sandbox"*. Serverless backends (Daytona/Modal) **hibernate** → near-zero idle cost.
- Runs on anything from a **$5 VPS to a GPU cluster**. **Hermes Desktop** is a first-party in-tree GUI for macOS/Windows/Linux — now covered properly in [[hermes-desktop]]. ⚠️ The "macOS 12+/Windows 10-11" version floors previously stated here are **UNVERIFIED**: `apps/desktop/README.md` names the three platforms with no version floors, and a 2026-09-03 critic agent "confirmed" these numbers by reading *this line*, which is circular.
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
