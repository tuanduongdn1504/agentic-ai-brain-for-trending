# CodexPlusPlus (Codex++) — Project Context

**Subject:** [`BigPizzaV3/CodexPlusPlus`](https://github.com/BigPizzaV3/CodexPlusPlus) — "An enhanced tool for CodexApp… 一个CodexApp的增强工具."
**Wiki version:** v117 (Routine v2.4).
**Status:** SHIPPED 2026-05-29. **STRONG INCLUDE 4/4** ((c)(d) STRONG, (a) inferred-PASS China-Mainland, (b) MODERATE). First clean PASS after the v116 Sana OVERRIDE.

## One-line

External CDP-injection enhancement harness + Tauri 2 management tool for OpenAI's Codex App — adds API-provider switching (rewrites `~/.codex/config.toml`), session management, plugin unlocks, user-script injection, Zed/worktree features — without modifying the Codex install. Rust + Tauri 2 + React; Windows + macOS. Solo China-Mainland dev; ~8,077★ / ~23 days / ~351/d EXTREME-VIRAL pulse; license unresolved.

## Pattern Library impact

**PRIMARY: Pattern #18 sub-archetype #8 "Multi-Source LLM Aggregator" → 8a config-switcher N+1, pushing #8 to N=3 → PROMOTION-ELIGIBLE** (v73 cc-switch 8a + v112 freellmapi 8b + v117 CodexPlusPlus 8a). Promotion is an audit decision (~v119–v120). Honest caveat: provider-switching is one feature of a broader harness; both 8a instances are Tauri-2 desktop (check for stack-coincidence before promoting).

**SECONDARY:** Pattern #18 B2 CDP-variant N+1; Pattern #52 EXTREME-VIRAL pulse N+1; Pattern #83 declared-but-unresolved-license N+1; Pattern #66 supply-chain note; China-Mainland sub-cluster (6 by-event). **ZERO new Library-vocab minted** (§28) — 2 observations filed into LV-C2 (relay-economy) + LV-C7 (Tauri-desktop-harness).

State UNCHANGED at ship (46 confirmed / ~25 active / 8 Library-vocab CONFIRMED). Streak "44+2\*" → "45+2\*".

## Files

- `02 Wiki/index.md` — the wiki page.
- `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` — STRONG INCLUDE 4/4 gate decision.
- `01 Analysis/(C) Pattern-Library-Phase-4b-Pattern-18-8a-config-switcher-N3.md` — primary + secondaries.

## ⚠️ Pilot note

NOT a Tier-1 vault pilot — Codex-specific, routes away from Claude, license unresolved, real supply-chain caveat (CDP injection + middle-layer API routing + relay sponsors). Study-value high; if ever piloted: `install-snapshot` first + throwaway key + inspect `config.toml`.
