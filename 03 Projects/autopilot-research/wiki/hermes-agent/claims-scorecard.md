# Hermes Agent — Claims Scorecard

## Source
Refute-first verification workflow **`wf_06a79485-687`** (44 agents, 0 errors, ~1.83M tokens): 8 source-gatherers → 22 merged claims (17 pre-registered + 5 gatherer-surfaced) → refute-first verifiers with **3-skeptic perspective panels on the 6 hype claims** → 2 completeness critics. Every verdict is grounded on **primary sources** (GitHub API ×2 endpoints, official README, site, docs) — transcripts and SEO blogs were treated as untrusted claim-sources.

## Tally
**22 claims → 13 CONFIRMED · 4 MISLEADING · 4 FALSE · 1 UNVERIFIABLE · 0 fabricated.**

## FALSE (4)
| ID | Claim | Correction |
|---|---|---|
| **H2** | "Hermes has ~22,000 stars / 142 contributors" (SEO blogs) | **216,731 stars** / 100+ contributors (2× GitHub API). The blogs undercount stars ~**10×** — stale/misread. |
| **H4** | "the **only** agent with a built-in learning loop" (first-party) | Self-contradicted by Hermes' own `hermes claw migrate`, which imports **memories + skills from OpenClaw** → OpenClaw also has a learning loop. Hermes' real edge is autonomous skill *creation*, not exclusivity. |
| **H5** | "launched **February 2026**" | Repo created **2025-07-22**; first public release **v0.2.0 on 2026-03-12**. No February release exists. (Panel split Mar-12 vs May-7; resolved to **Mar-12 v0.2.0** by direct releases-API check.) |
| **C17** | "Hermes **runs under Claude Code**" (AI LABS) | No such relationship — independent vendors; docs list no Claude Code integration. Real mechanism = **MCP interop both ways** (see [[claude-code-interop]]). |

## MISLEADING (4)
| ID | Claim | Correction |
|---|---|---|
| **H1** | "216K+ stars → most-starred agent repo, **everyone is switching to it**" | Star count **CONFIRMED (216,731)** and **plausibly the most-starred agent repo** (ahead of AutoGPT ~184K); but **"everyone is switching" is unsupported marketing** — no adoption/migration/DAU data in any primary source. |
| **H6** | "**no-code**, **easier than OpenClaw**" (anchor) | Fast **curl\|bash install** (~60s), but it's a developer CLI/TUI needing Python 3.11/Node/ripgrep/ffmpeg + config + keys. Official sources never say "no-code" or "easier than OpenClaw" (only a migration tool exists → implies parity, not ease-superiority). |
| **X1** | "fully automated **digital employee** working on your computer 24/7" | Local operation + 24/7 are real (desktop apps + VPS/serverless), but "digital employee" is anthropomorphic framing Nous doesn't use; 24/7 needs continuous hosting + token spend (cloud-dependent). |
| **X5** | learning loop = "**work→think→check→improve** circle" | Docs describe continuous autonomous skill creation + curated memory + user modeling — **not** a discrete 4-phase evaluation cycle. Presenter invented the procedural framing. |

## UNVERIFIABLE (1)
| ID | Claim | Note |
|---|---|---|
| **H3** | "By June 2026 Hermes overtook OpenClaw on OpenRouter — 224B vs 186B daily tokens" | No primary source (Nous/OpenRouter) corroborates it. Worse — **OpenRouter ranks *models*, not agent frameworks**; neither Hermes nor OpenClaw appears in current rankings (top: Tencent/Xiaomi/DeepSeek, trillions/week). Likely a **category error** + SEO stat. Do not cite. |

## CONFIRMED (13)
- **C7** MIT license + built by Nous Research (org verified). · **C16** Runs $5-VPS→GPU-cluster; MIT-free software, pay tokens+hosting; freemium Free/Plus/Super/Ultra.
- **C8** Persistent memory = FTS5 + LLM summarization + Honcho (Plastic Labs). · **C9** Autonomous skill creation + `/learn` + agentskills.io. *(quality-self-improvement contested — see [[learning-loop-and-self-improving-skills]].)*
- **C10** Multi-channel gateway (Telegram/Discord/Slack/WhatsApp/Signal/Email/CLI; docs "20+"). · **C11** Built-in cron scheduler. · **C12** Isolated parallel subagents + Python RPC.
- **C13** 6 backends (local/Docker/SSH/Singularity/Modal/Daytona). · **C14** Provider-agnostic (Nous Portal/OpenRouter/OpenAI/custom) + MCP; "300+ models" via Portal subscription. · **C15** `hermes claw migrate` imports OpenClaw settings/memories/skills/keys.
- **X2** Open source + free to download/use. · **X3** "Evolves over time / understands you better" — **confirmed for memory**; autonomous skill-quality evolution is contested. · **X4** Remembers your habits/preferences across sessions.

## Key Takeaways
- **The product is real and strong at the confirmed core** (MIT, memory, channels, providers, subagents, cron, migration). The verified feature set alone justifies attention.
- **Every marketing superlative failed** the refute-first pass (H1/H4/H5/H6/H3 + X1/X5). The pattern: accurate *capabilities*, inflated *framing*.
- **0 fabrications, 0 verifier misfires flagged** — a clean run. The one internal split (H5 date) was resolved by a direct primary-source check.
- Full evidence + the contradictions the critics found: [[caveats-and-corrections]]. Method + per-source detail: [[source-provenance]].
