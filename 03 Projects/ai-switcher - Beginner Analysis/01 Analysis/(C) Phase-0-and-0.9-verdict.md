# (C) hoangpm96/ai-switcher ("AI Account Switcher") — Phase 0 + Phase 0.9 STRICT verdict (v153)

**Subject:** `hoangpm96/ai-switcher` — https://github.com/hoangpm96/ai-switcher
**Date:** 2026-06-04 · **Routine:** v2.6 (§31 + §35 + §37)
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) WEAK (inferred-VN, not load-bearing) · (b) STRONG · (c) STRONG · (d) STRONG.

---

## Phase 0 — scope gate
**On-goal.** ai-switcher is *"a native macOS application for managing and switching between multiple accounts across AI coding tools from a single interface"* — the tools being **Claude Code, Codex, and Antigravity IDE**. Goal #1 is "master Claude and autonomous agents for software development"; a control-plane that **operates** those coding agents (account + quota + auto-switch) is squarely in scope, and directly applicable to how Storm Bear runs Claude Code. Contrast the off-goal v123/v152 shape (an app that merely *uses* an LLM) — here the subject's whole purpose is to manage the coding agents themselves.

## Phase 0.9 STRICT — four axes

### (a) Cultural-peer / geographic — **WEAK** (inferred; NOT load-bearing)
- Owner `hoangpm96` — the handle reads **Vietnamese** (Hoàng / Phạm; `96` = likely birth-year). Vietnamese is a **registered cultural-peer axis** (the v76 HoangNguyen0403 / v80 / v85 VN cluster) and a **direct peer to Storm Bear** (Vietnamese). BUT **location is undeclared** on the page and there is no affirmative VN-located signal → **name-inferred only.**
- **Call:** held a **WEAK (a)-PASS on inferred-VN cultural-peer**, explicitly **NOT load-bearing** ((b) carries the GOAL-ALIGNED include). Recorded honestly — the v151-audit recommendation (ii) ("require a *solid* (a) signal, not a name-heritage inference") is **PENDING operator sign-off, not adopted**, so an inferred-VN PASS is still within current rules; if (ii) is adopted, this downgrades to (a) FAIL with no effect on the verdict (it's a goal-aligned include either way).

### (b) Goal-relevance — **STRONG** (load-bearing)
A native control-plane for **operating multiple AI coding agents** — multi-account login/switch per tool (Claude Code, Codex, Antigravity), quota monitoring (5h/weekly for Claude & Codex; per-model for Antigravity), **auto-switch when an account hits its quota**, isolated CLI configs, token-swap + IDE-restart for Antigravity. This is dead-center goal #1 (operating Claude Code + peer agents) AND a real Storm-Bear workflow need. **STRONG-not-STRONGEST** = an account/quota *utility around* the agents, not the agent substrate (Claude itself) or a methodology — the v140/v143/v144 calibration for connector/utility subjects.

### (c) Instructive engineering — **STRONG** (tempered by nascency)
A clean small **Tauri** (Rust 67.7% + React/TS 22% + CSS 9.4%) desktop app with genuinely instructive mechanics: **per-account config isolation** (dedicated per-account CLI commands), **quota-aware auto-switch** (monitor → rotate on exhaustion), **token-swap-with-IDE-restart** for Antigravity's GUI, shared chat sessions within projects. Tempered: micro-scale (11 commits), **no license yet**, unsigned `.dmg`. Net STRONG on the design ideas.

### (d) Corpus connectivity — **STRONG**
- **LV-C7 "Tauri-Desktop Management-GUI for a Coding Agent" → N=3** (v73 cc-switch + v117 CodexPlusPlus + v153 ai-switcher) — a genuine 3rd *management-GUI* (a Tauri desktop control-plane that manages *another* coding agent's accounts/config), exactly the "3rd management-GUI, not just a 3rd Tauri app" the N=3 watch required.
- **Pattern #18 #8 Multi-Source LLM Aggregator — ADJACENT, not counted** (account-switch + quota-rotate vs provider-aggregate; the multi-account/provider/agent layer-taxonomy, flagged for the audit).
- **Antigravity-as-managed-target corpus-recursive** (v67 opencode-antigravity-auth + v85 ui-ux-pro-max's antigravity harness) + Pattern #84 cross-tool (Claude Code + Codex + Antigravity) + VN cultural-peer cluster (inferred).

---

## §35 — Soft Off-Goal-Rate Ceiling — **SATISFIED, NOT fully cleared**
- The ceiling was **breached** after v152 (window {v150 GA, v151 OG, v152 OG} = 2 OG). §35.2 mandates the next ship be GOAL-ALIGNED — **v153 GA SATISFIES that mandate.**
- BUT the rolling-3-ship window after v153 = **{v151 OG, v152 OG, v153 GA} = 2 OG → STILL technically BREACHED** (the v147 shape). **Full clearance requires v154 ALSO GOAL-ALIGNED** (window would become {v152 OG, v153 GA, v154 GA} = 1 OG ≤ 1).
- **NOT an override** → override-frequency triggers UNCHANGED (still 7-in-20 trailing from v152; lifetime overrides 10 UNCHANGED; the next audit's mandated override review stands but v153 adds nothing).

## §37 — Fact-provenance
≈**13★** / 8 forks / **11 commits** / **license: none yet** ("add MIT or similar before wider distribution") / Tauri (Rust 67.7% + TypeScript 22.0% + CSS 9.4%) / native macOS `.dmg` (unsigned; right-click/terminal bypass on first launch) (page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified §37.4**; env mocks the GitHub API). Micro-scale + nascent (11 commits) → **NOT a Pattern #52 claim.** Owner `hoangpm96` (VN inferred, location undeclared).

## Streak (v2.6 §32)
GA:15 · OG:11 [7 ov] → **GA:16 · OG:11 [7 ov]** (16th GOAL-ALIGNED PASS; NOT an override; "49+3\*" frozen @v125).

## Pattern Library — see `(C) Pattern-Library-Phase-4b.md`
**PRIMARY** LV-C7 → N=3 (PROMOTION-ELIGIBLE) + **SECONDARY** 1 NEW standalone (account/quota auto-switch). §28: 1 new standalone (≤2) + 1 cluster strengthening; **registry 06 ACTUALLY edited** (rule-5). NO confirmed-count change (46 / 9).

## Pilot
**CONDITIONAL pilot** — genuinely useful (multi-account Claude-Code + quota auto-switch is a real Storm-Bear workflow), but **no license yet + unsigned + micro-scale (11 commits)** = trial at fenced scope only (read repo / build-from-source on a scratch account; `install-snapshot` first; reversible). Joins the un-piloted goal-aligned backlog (v150 Paseo + v149 Scrapling + v144 headroom).

## Honest non-claims
- (b) genuinely STRONG, held **not** STRONGEST (utility-around-agents, not the substrate) — not inflated.
- (a) is WEAK/inferred (name-only, location-undeclared) and **not load-bearing** — flagged, not laundered to a firm PASS.
- LV-C7 → N=3 is a genuine 3rd *management-GUI* (the watch's exact bar); promotion is the **audit's** call, filed not asserted.
- Pattern #18 #8 is ADJACENT, **not** counted (account vs provider layer).
- NOT a #52 claim (13★/11 commits; metrics not API-verified).
- 1 new standalone + 1 cluster strengthening; NO new top-level Pattern; NO confirmed-count change (46 / 9).
