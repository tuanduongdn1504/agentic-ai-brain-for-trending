# CodexBar — Beginner Analysis (project CLAUDE.md)

**Subject:** `steipete/CodexBar` (v159 wiki ship, 2026-06-05).
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.
**Routine:** v2.6 (§31/§35/§37). **Ships into the v158-audit-CONFIRMED Pattern Library** (audit ran first, at operator election).

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis verdict + §35 + §37 + honest non-claims.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY clean strengthening (metering sub-flavor → N=5, sub-archetype → N=8) + 0 new standalones; observations only.
- `02 Wiki/index.md` — the knowledge page.

## One-paragraph summary
**"Every AI coding limit, in your menu bar."** A privacy-first **native-macOS menu-bar app** (Swift 99.2% / SwiftUI / WidgetKit, macOS 14+, MIT) by **Peter Steinberger (`steipete`)** that surfaces usage meters + reset countdowns + credit balances + spend/cost + session/weekly/monthly quota windows for **40+ AI coding providers** (Claude Code + Codex + Cursor + Gemini + Copilot + Grok + Bedrock + OpenRouter + 30 more) — the **broadest provider coverage in the corpus.** It reuses existing sessions (OAuth/device flows, API keys, CLI creds, opt-in browser cookies, local config + local JSONL logs; no passwords stored, no FS crawling), ships a bundled `codexbar` CLI for scripts/CI, and updates via Sparkle / Homebrew cask. v0.32.4; 14.3k★ / 2,507 commits / 70 releases — the most mature + popular member of the observability cluster.

## Verdict rationale
- **(b) STRONG** = real-time usage/cost/quota across Claude Code + Codex + 40+ providers = goal #1 + a real heavy-Claude-Code workflow. **STRONG-not-STRONGEST** = an observability utility *around* the agents.
- **(a) FAIL** = steipete is a **notable** Apple/AI-dev (PSPDFKit founder, Vienna) but **not** a cultural-peer and **not** an (a)-7 vault-substrate vendor. Notable ≠ (a) PASS; **no axis minted** (v139 discipline). Prominence = a (d)-connectivity note. (b) carries the include.
- (c) STRONG (Swift/SwiftUI/WidgetKit/SPM + 40+ adapters + bundled CLI + Sparkle + extensive docs; 2,507c/70 releases). (d) STRONG (observability sub-archetype N=8 / metering N=5 + Swift-native-macOS cluster + #84 cross-tool 40+ BROADEST + JSONL-parsing + near-twin to v157 ClaudeBar).

## §35 / streak
**§35 STAYS CLEAR** — window {v157 GA, v158 GA, v159 GA} = 0 OG (7 consecutive goal-aligned ships v153→v159). NOT an override → override-frequency UNCHANGED (lifetime 10). Streak GA:21·OG:11 [7 ov] → **GA:22·OG:11 [7 ov]** (22nd GOAL-ALIGNED PASS).

## Pattern Library
**PRIMARY: clean instance-strengthening — metering/quota sub-flavor (a) → N=5** (v89+v109+v157+v158+v159); **"AI-Agent Observability / Status-Surface Tool" sub-archetype → N=8.** The sub-archetype was **CONFIRMED at the v158 audit** (run just before this ship); CodexBar is a clean post-confirmation instance — most mature/popular/broadest, **but introduces no new structure.** **§28: 0 new standalones** — exactly the outcome the v158 audit forward-note predicted (do NOT manufacture a mint for a 7th-in-niche entry). **NO confirmed-count change (46 patterns / 10 Library-vocab CONFIRMED).** Observations (NOT minted): broadest-provider-coverage (40+ vs ClaudeBar 10 / ai-token-monitor 3); steipete notable-author (d)-connectivity NOT (a); Swift-native-macOS cluster N+1; JSONL-parsing #84 84c.1; Sparkle; bundled-CLI companion; near-twin v157 ClaudeBar; NOT LV-C7 (observes ≠ controls); NOT #18 #8; AGENTS.md/.agents/skills = thin internal tooling NOT product (v122). NOT a #52 claim (14.3k★ but creation date not shown → velocity unestablished; API mocked §37.4).

## Provenance (§37)
≈**14.3k★** / 1.1k forks / 44 watchers / 38 issues / **2,507 commits** / **70 releases** (v0.32.4, Jun 2 2026) / MIT / Swift 99.2% / macOS 14+ — page-stated as of 2026-06 via WebFetch + codexbar.app + DeepWiki, **NOT independently API-verified §37.4** (env mocks the GitHub API). Created date NOT shown → velocity unestablished → **NOT a #52 claim.** Owner `steipete` = Peter Steinberger (@steipete, PSPDFKit founder, Vienna).

## Pilot
**Strong pilot candidate — arguably the best of the seven** (MIT, very mature 2,507c/70 releases, Sparkle + `brew install --cask steipete/tap/codexbar`, reversible; `install-snapshot` first). For heavy Claude Code use, "budget left across all providers + rate-limit warnings" is a real workflow win, and it reads existing sessions with no agent reconfiguration. ⚠️ **This is the 7th "manage/monitor AI coding tools" ship in a row (v153–v159), ZERO piloted.** The v158 audit banked the structural value (2 confirmations); the high-value next move is **pilot one** (CodexBar/ClaudeBar/ai-token-monitor) or **vary the domain** — not a v160 in the niche.

Shipped on branch `wiki/v159-codexbar` stacked on `wiki/audit-v158` (off main at c3ca247=v158). Not auto-merged — operator merges the stack in order: audit → v159.
