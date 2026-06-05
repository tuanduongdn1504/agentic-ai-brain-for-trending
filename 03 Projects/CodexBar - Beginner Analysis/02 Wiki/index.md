# (C) steipete/CodexBar (v159 wiki)

> **Status: GOAL-ALIGNED INCLUDE 3/4** ((a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG). A native-macOS menu-bar usage/quota/cost monitor for **40+ AI coding providers** (Claude Code + Codex + Cursor + Gemini + Copilot + 35 more) — the most mature, most popular, and broadest-coverage instance of the corpus's just-CONFIRMED **"AI-Agent Observability / Status-Surface Tool"** sub-archetype. **A clean strengthening of the metering sub-flavor → N=5; 0 new mints** (exactly as the v158 audit's forward-note predicted — this is the honest outcome for a 7th-in-niche subject). See `01 Analysis/`.

**Repo:** https://github.com/steipete/CodexBar · **Owner:** `steipete` (Peter Steinberger) · **License:** MIT
**Tagline:** *"Every AI coding limit, in your menu bar."* / repo: *"Show usage stats for OpenAI Codex and Claude Code, without having to login."*
**Site:** https://codexbar.app

## What it is
A **privacy-first macOS menu-bar app that surfaces your AI-coding usage limits across 40+ providers** without logging into each one. It reuses the sessions your tools already have — OAuth/device flows, API keys, CLI credentials, browser cookies (opt-in), local config + local JSONL logs — and renders usage meters, reset countdowns, credit balances, spend/cost, and session/weekly/monthly quota windows directly in the menu bar. A bundled `codexbar` CLI exposes the same data to scripts/CI.

## Providers it monitors (40+ — broadest in the corpus)
**Claude (Code)** · **OpenAI Codex** · Cursor · Gemini · GitHub Copilot · Grok · GroqCloud · AWS Bedrock · OpenRouter · Deepgram · ElevenLabs · +~30 others. *(For comparison: v157 ClaudeBar = 10 tools, v158 ai-token-monitor = 3. CodexBar's 40+ is the corpus-broadest provider coverage.)*

## Core features (from the README)
- **Usage meters with reset countdowns** + session / weekly / monthly quota windows.
- **Credit balances + spend/cost** where the provider exposes them; configurable local cost scans for Codex and Claude.
- **Per-provider menu-bar icons** (or a merged single icon with a switcher); usage bars; **incident status badges**; optional notifications + refresh cadence (manual / 1m / 2m / 5m / 15m).
- **Bundled `codexbar` CLI** for scripts/CI (`codexbar cost --provider codex|claude|both`); macOS + Linux CLI builds.
- **Privacy-first:** on-device parsing by default; browser cookies opt-in; no passwords stored; no filesystem crawling (reads only known locations).

## Architecture (the instructive part)
- **Swift 99.2% / SwiftUI / WidgetKit**, macOS 14+ (Sonoma), Swift Package Manager, Swift 6.2+; SwiftFormat + SwiftLint.
- **Per-provider adapters** over a refresh-loop / status-polling design (documented in an extensive `docs/`).
- **Token storage** in `~/.codexbar/config.json` with restrictive permissions; Keychain integration; optional Full Disk Access only for Safari cookies.
- **Local JSONL-log parsing** for Codex/Claude cost — the same observability mechanism as v89 VibeCodingTracker + v158 ai-token-monitor (reads what your tools already write; no agent reconfiguration).
- **Sparkle auto-updates**; Homebrew cask (`brew install --cask steipete/tap/codexbar`) + CLI tap + AUR.

## Where it sits in the corpus
- It is the **metering/quota sub-flavor (a)** of the **CONFIRMED (v158 audit) "AI-Agent Observability / Status-Surface Tool" sub-archetype** → brings that sub-flavor to **N=5** (v89 VibeCodingTracker + v109 cclog-cli + v157 ClaudeBar + v158 ai-token-monitor + v159 CodexBar) and the sub-archetype overall to **N=8.**
- **Near-twin of v157 ClaudeBar** — both native-Swift menu-bar quota monitors; ClaudeBar covers 10 tools, CodexBar 40+ and is far more mature (14.3k★ / 2,507 commits / 70 releases vs 1.2k★).
- It **OBSERVES** (reads/surfaces state) — so it is *not* an LV-C7 management-GUI (#22; v73/v117/v153, which *control* an agent's config/accounts). Different layer (observe-vs-control).
- **0 new mints** — a clean instance-strengthening of an already-confirmed sub-archetype (the honest outcome; the v158 audit explicitly flagged that v159 should mint nothing new rather than manufacture novelty).

## Provenance (§37)
≈**14.3k★** / 1.1k forks / 44 watchers / 38 open issues / **2,507 commits** / **70 releases** (latest v0.32.4, Jun 2 2026) / MIT / Swift 99.2% / macOS 14+.
*Page-stated as of 2026-06 via WebFetch of the rendered repo + codexbar.app — **NOT independently API-verified (§37.4)**; this environment mocks the GitHub API.* **Created date NOT shown** → velocity unestablished → **NOT a Pattern #52 claim** (despite 14.3k★ being large — the most-popular observability-cluster member, but age-unverified). Owner `steipete` = **Peter Steinberger** (@steipete; PSPDFKit founder; prominent Apple/AI-coding developer; Vienna/Austria — a notable author, but **not** a cultural-peer and **not** an (a)-7 vault-substrate vendor → see (a) note).

## Why it's goal-aligned (and a strong pilot)
- **On goal #1:** it observes the coding agents (their usage/cost/quota), not an app that merely calls an LLM.
- **Directly vault-applicable:** for heavy Claude Code use, "how much budget is left across all my providers, and warn me before I'm rate-limited" is a concrete workflow win — and it reads existing sessions with no agent reconfiguration.
- **Strong pilot candidate:** MIT + very mature (2,507 commits / 70 releases) + Sparkle + Homebrew; `brew install --cask steipete/tap/codexbar`, reversible, `install-snapshot` first. Arguably the most directly-useful and most-polished of the v153–v159 niche. ⚠️ **This is the 7th "manage/monitor AI coding tools" ship in a row (v153–v159), with ZERO piloted.** The v158 audit just banked the structural value (2 confirmations); the genuinely high-value next move is to **pilot one** (CodexBar/ClaudeBar/ai-token-monitor are the most useful) or **vary the subject domain** — not catalogue a v160.

## §35 note
A goal-aligned v159 keeps the ceiling clear: window {v157 GA, v158 GA, v159 GA} = 0 OG (seven consecutive goal-aligned ships v153→v159). Streak GA:21·OG:11 → **GA:22·OG:11 [7 ov]** (22nd goal-aligned PASS; not an override).
