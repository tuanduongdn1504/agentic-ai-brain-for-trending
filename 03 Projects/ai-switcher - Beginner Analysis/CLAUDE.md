# ai-switcher — Beginner Analysis (project CLAUDE.md)

**Subject:** `hoangpm96/ai-switcher` ("AI Account Switcher") (v153 wiki ship, 2026-06-04).
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) WEAK (inferred-VN, not load-bearing) · (b) STRONG · (c) STRONG · (d) STRONG.
**Routine:** v2.6 (§31/§35/§37).
**Requested:** "build LLM wiki ... macOS app to manage multiple AI coding tools."

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis verdict + §35 + §37 + honest non-claims.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY LV-C7 → N=3 + 1 NEW standalone; registry 06 ACTUALLY edited.
- `02 Wiki/index.md` — the knowledge page.

## One-paragraph summary
**"A native macOS application for managing and switching between multiple accounts across AI coding tools from a single interface."** A **Tauri** (Rust 67.7% + React/TS) desktop control-plane for **Claude Code, Codex, and Antigravity IDE**: log in / switch / rename / remove **multiple accounts per tool**, **monitor quota** (5-hour & weekly for Claude/Codex, per-model for Antigravity), **auto-switch when an active account hits its quota**, keep **isolated CLI configs** per account (dedicated per-account commands), share chat sessions within projects, and **swap login tokens in Antigravity's GUI with an automatic IDE restart**. Squarely goal #1 (operating Claude Code + peer coding agents) and directly vault-applicable. Owner `hoangpm96` (Vietnamese name inferred, location undeclared); license **none yet** (author notes "add MIT before wider distribution"); `.dmg`, unsigned.

## Verdict rationale
- **(b) STRONG** = the load-bearing axis: a tool to operate/manage multiple AI coding agents (account + quota + auto-switch) is dead-center goal #1 AND a real Storm-Bear workflow need (running Claude Code across accounts/quotas). STRONG-not-STRONGEST = an account/quota utility *around* the agents, not the agent substrate or a methodology.
- **(a) WEAK** (not load-bearing) = `hoangpm96` reads Vietnamese (Hoàng/Phạm), a registered cultural-peer axis + a direct peer to Storm Bear — but **name-inferred, location undeclared** → held WEAK; (b) carries the include, so (a) is not relied on. Flagged honestly (the v151-audit rec-(ii) "require a solid (a) signal" is PENDING, not adopted).
- (c) STRONG (clean small Tauri arch: per-account config isolation + quota-aware auto-switch + token-swap/IDE-restart) — tempered by nascency (11 commits, no license, unsigned). (d) STRONG (LV-C7 family + #18 #8 adjacency + VN cluster + Antigravity corpus-recursive).

## §35 / streak
**§35 SATISFIED, NOT fully cleared** — a GOAL-ALIGNED v153 meets the §35.2 post-breach mandate (the next ship after the v151/v152 breach MUST be goal-aligned), but the window {v151 OG, v152 OG, **v153 GA**} = 2 OG is **still breached** → **v154 must ALSO be GOAL-ALIGNED** to fully clear (the v147 shape). NOT an override → override-frequency UNCHANGED (7-in-20 trailing; lifetime 10). Streak GA:15·OG:11 [7 ov] → **GA:16·OG:11 [7 ov]** (16th GOAL-ALIGNED PASS).

## Pattern Library
**PRIMARY: LV-C7 "Tauri-Desktop Management-GUI for a Coding Agent" → N=3** (v73 cc-switch + v117 CodexPlusPlus + v153 ai-switcher; a genuine 3rd *management-GUI* — exactly what the N=3 watch required, "a 3rd management-GUI, not just a 3rd Tauri app") → **PROMOTION-ELIGIBLE; recommend CONFIRMED at the overdue audit.** **SECONDARY: 1 NEW section-C standalone** "Multi-Account/Quota Manager with Auto-Switch-on-Quota-Exhaustion for AI coding tools" N=1 CORPUS-FIRST (distinct from cc-switch v73 provider-config-switch — that picks ONE provider; this juggles MULTIPLE accounts + monitors quota + auto-rotates on exhaustion). **§28: 1 new standalone (≤2) + 1 cluster strengthening; registry 06 ACTUALLY edited (rule-5).** NO Pattern Library state change to confirmed counts (46 patterns / 9 Library-vocab CONFIRMED). Observations (NOT minted): Pattern #18 #8 ADJACENT (account-switch vs provider-aggregate — the multi-account/provider/agent layer-taxonomy, flag for audit) + Pattern #84 cross-tool + Antigravity-as-managed-target corpus-recursive (v67 + v85) + VN cultural-peer cluster N+1 (inferred) + Pattern #29/#83 no-license-yet honest-disclosure + `.claude/` incidental + micro-scale NOT #52.

## Provenance (§37)
≈**13★** / 8 forks / **11 commits** / **license none yet** / Tauri (Rust 67.7% + TypeScript 22.0% + CSS 9.4%) / native macOS, `.dmg` unsigned — page-stated as of 2026-06 via WebFetch, **NOT independently API-verified §37.4** (env mocks the GitHub API). Micro-scale + nascent → **NOT a #52 claim.** Owner `hoangpm96` (VN inferred, undeclared).

## Pilot
**CONDITIONAL pilot** — genuinely useful for Storm Bear (multi-account Claude-Code + quota auto-switch is a real workflow), BUT no license yet + unsigned `.dmg` + micro-scale/11-commit nascency = trial only at fenced scope (read the repo / build from source on a scratch account; `install-snapshot` first). It joins the un-piloted goal-aligned backlog (v150 Paseo + v149 Scrapling + v144 headroom).

Shipped on branch `wiki/v153-ai-switcher` off main (at d0a9011, post-v152-ship). Not auto-merged — operator merges.
