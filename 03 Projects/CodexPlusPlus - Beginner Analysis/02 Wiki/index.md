# CodexPlusPlus (Codex++) — Wiki (v117)

> `BigPizzaV3/CodexPlusPlus` · **"An enhanced tool for CodexApp, striving to make Codex better to use and more comfortable / 一个CodexApp的增强工具，努力让Codex变得更好用更舒服."** · An external enhancement launcher + management tool for OpenAI's **Codex App** that injects features via the **Chromium DevTools Protocol (CDP)** *without modifying the original install* — adding API-provider switching, session management, plugin unlocks, and user-script injection.

**(C) Claude-generated wiki page.** Fetched 2026-05-29 (GitHub API + README + user profile). Routine v2.4, wiki #117. Phase 0.9 **STRONG INCLUDE 4/4** — (c)(d) STRONG, (a) inferred-PASS (China-Mainland), (b) MODERATE. First clean PASS after the v116 Sana OVERRIDE.

---

## Identity

| Field | Value |
|---|---|
| Repo | [`BigPizzaV3/CodexPlusPlus`](https://github.com/BigPizzaV3/CodexPlusPlus) |
| What | **External CDP-injection enhancement harness + management tool for OpenAI Codex App** |
| Tier / archetype | **T2 Service / desktop enhancement-harness** (sibling to v73 cc-switch Tauri provider-manager; "external harness via CDP injection" architecture) |
| Stars / forks | **8,077★ / 537 forks** (fork_ratio **0.066**) |
| Subscribers / open issues | 15 / **181 open** (very high issue velocity on a 23-day-old repo) |
| Created / pushed | 2026-05-06 / 2026-05-29 (**~23 days** old at fetch) |
| Velocity | **~351 stars/day → Pattern #52 EXTREME-VIRAL pulse-class** (>300/d; 23-day window « 90d so a *pulse*, NOT Multi-Month-Sustained) |
| License | **Not specified** (GitHub API SPDX = none). README carries a license *badge* but no resolvable LICENSE file detected → **Pattern #83 declared-but-unresolved-license** territory. ⚠️ treat as unlicensed until confirmed. |
| Language | **Rust ~65%** (Rust 1.85+) + JS/TS frontend |
| Stack | **Tauri 2.x + React** frontend; NSIS Windows installer; macOS Intel x64 + Apple Silicon arm64 DMGs |
| Distribution | GitHub Release binaries + in-app auto-update (both the silent launcher and the management tool self-update) |
| Platforms | **Windows x64 + macOS (Intel + Apple Silicon)**; no Linux |
| Default branch / homepage | `main` / none |
| Author | **BigPizzaV3** (`owner.type: User`) — solo dev, **inferred China-Mainland** (QQ group 1103050832 + Alipay/WeChat donations + Chinese-Mainland API-relay sponsors); profile bare (no name/location/bio); account created 2025-10-11 (~7.6 mo); 11 repos / 55 followers |

## What it is

Codex++ is a **wrapper around OpenAI's Codex desktop app** that adds quality-of-life and power-user features the native app lacks — *without touching Codex's own files*. It does this with a clean two-binary design:

- **`Codex++`** — a silent launcher that starts Codex and injects enhancement scripts via CDP, no UI shown.
- **`Codex++ 管理工具`** (Management Tool) — a Tauri 2 + React control panel for configuration, diagnostics, and updates.

The injection mechanism is the interesting part: rather than patching the Codex binary or its `app.asar`, it launches Codex with the **Chromium DevTools Protocol** open and injects JavaScript into the running renderer. This is the same external-harness-via-CDP idea seen in v69 CloakBrowser, applied here as a *non-invasive enhancement layer* (uninstall = delete the launcher; Codex itself is untouched).

## Feature set

- **API-provider switching (the headline).** Through the management tool you set a Base URL + API key; Codex++ writes the provider config into `~/.codex/config.toml` so Codex routes requests to a **custom OpenAI-compatible endpoint** while *preserving the official ChatGPT login state*. Includes provider-metadata sync before switching suppliers. **This is a config-switcher aggregator** — the same mechanism as v73 cc-switch (which does it for Claude Code).
- **Session management** — delete sessions (native UI has no delete button), Markdown export, project relocation.
- **Plugin entry unlock** — restores plugin access for API-Key-mode users.
- **Custom user-script injection** at startup.
- **Timeline viewing**, **Zed Remote Development integration**, **Git worktree creation** from upstream branches with automatic remote fetch.
- **Auto-update** via GitHub Releases; Windows single-instance enforcement; macOS Dock-icon hiding.

## Ecosystem & economics

The README credits multiple **API-relay-service sponsors** (JOJO Code, AIGoCode, PackyCode, others) and takes Alipay/WeChat donations. This situates Codex++ inside the **Chinese-Mainland "API relay / middle-layer" economy** — third-party services that resell or route access to frontier coding-agent APIs, often more cheaply than official channels. The provider-switching feature is the natural client for that economy.

## ⚠️ Honest supply-chain caveat

Using Codex++ means trusting an **external launcher that injects code into your Codex renderer via CDP and rewrites `~/.codex/config.toml` to route your API traffic through custom/middle-layer endpoints** — and the project is funded by API-relay sponsors. That's a real credential/supply-chain consideration, not a dealbreaker for studying it, but a genuine one for any pilot. License is also unresolved (badge present, no SPDX). If piloting: snapshot first (`install-snapshot`), use a throwaway key, and read what gets written to `config.toml`.

## Why it's in the corpus

Clean **STRONG INCLUDE 4/4** (no criterion fails):
- **(a) PASS (inferred)** — solo China-Mainland dev (community-signal inference, not declared profile; consistent with the v100 tisfeng / v98 / v99 inference-tolerant precedents). Extends the China-Mainland sub-cluster (v82+v83+v91+v94+v100+**v117** = 6 by-event).
- **(b) MODERATE** — it's a *Codex* tool, not Claude; routes **away** from Claude. Real value is architectural study + conditional-if-you-use-Codex utility, not core vault work. Honestly MODERATE (mirrors v112 freellmapi).
- **(c) STRONG** — genuinely instructive reference architecture: non-invasive CDP-injection harness + provider-switching middle-layer + dual silent-launcher/management-tool design.
- **(d) STRONG** — high connectivity: direct sibling to **v73 cc-switch** (Tauri 2 config-switcher provider-manager) and **v62 codex-plugin-cc** (Codex tooling); Pattern #18 #8 8a config-switcher + sub-mechanism B2 CDP-variant; v69 CloakBrowser CDP; China-Mainland cluster; Pattern #52 pulse.

## Pattern Library contribution (summary)

- **PRIMARY: Pattern #18 sub-archetype #8 "Multi-Source LLM Aggregator" → 8a config-switcher N+1, pushing #8 to N=3 → PROMOTION-ELIGIBLE** (v73 cc-switch 8a + v112 freellmapi 8b + **v117 CodexPlusPlus 8a**). Honest caveat: for Codex++ provider-switching is *one feature of a broader harness*, not its whole identity.
- SECONDARY: Pattern #18 sub-mechanism **B2 CDP-variant** N+1 (CDP injection harness; cf. v69); **Pattern #52 EXTREME-VIRAL pulse** N+1 (~351/d × 23d); **Pattern #83 declared-but-unresolved-license** N+1; **Pattern #66 supply-chain** note (CDP injection + middle-layer routing + relay sponsors); China-Mainland sub-cluster + Tauri-2-desktop-harness cluster observations (v73+v117) filed per §28, **zero new standalone Library-vocab minted**.
- **Honest non-claims:** NOT a Claude tool; NOT in the agentskills.io chain; (a) is INFERRED; (b) is MODERATE; NOT a Pattern #52 promotion (pulse); the #18 #8 promotion is an *audit decision*, not asserted here; **no Pattern Library state change** at ship.

---

*See `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` and `01 Analysis/(C) Pattern-Library-Phase-4b-Pattern-18-8a-config-switcher-N3.md`.*
