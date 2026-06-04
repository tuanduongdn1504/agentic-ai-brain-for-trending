# (C) hoangpm96/ai-switcher — "AI Account Switcher" (v153 wiki)

> **Status: GOAL-ALIGNED INCLUDE 3/4** ((a) WEAK inferred-VN · (b) STRONG · (c) STRONG · (d) STRONG). A native-macOS control-plane for operating multiple AI coding agents — squarely goal #1 and directly vault-applicable. **CONDITIONAL pilot** (no license yet + unsigned + nascent). See `01 Analysis/` for the verdict + Pattern-Library Phase 4b.

**Repo:** https://github.com/hoangpm96/ai-switcher · **Owner:** `hoangpm96` (Vietnamese, inferred) · **License:** none yet (author: "add MIT before wider distribution")
**Tagline:** *"A native macOS application for managing and switching between multiple accounts across AI coding tools from a single interface."*

## What it is
A **desktop control-plane for your AI coding agents.** Instead of hand-editing CLI configs or re-authenticating when you hit a usage limit, ai-switcher gives one macOS UI to manage **multiple accounts across Claude Code, Codex, and Antigravity IDE** — and rotates them automatically when an account runs out of quota.

The tools it manages:
- **Claude Code** (CLI)
- **Codex** (CLI)
- **Antigravity IDE** (GUI)

## Core capabilities
- **Multi-account per tool** — log in, switch, rename, remove accounts for each tool.
- **Quota monitoring** — track usage limits per account: **5-hour & weekly** windows for Claude Code & Codex; **per-model** quota for Antigravity.
- **Auto-switch on quota exhaustion** — when the active account hits its limit, automatically rotate to a fresh one (the headline feature — keeps an agent session productive across accounts).
- **Isolated CLI configs** — each account gets a dedicated, isolated config + per-account commands, so switching never clobbers another account's state.
- **Shared chat sessions** — share sessions across accounts within a project.
- **Antigravity token-swap + IDE restart** — swap login tokens in Antigravity's GUI and restart the IDE automatically.

## Architecture (the instructive part)
- **Built with Tauri** (Rust 67.7% + React/TypeScript 22.0% + CSS 9.4%) — a **native macOS** app (not Electron), distributed as a `.dmg`.
- The clean mechanics worth borrowing: **per-account config isolation** (dedicated commands so accounts never collide), **quota-aware auto-rotation** (monitor → switch on exhaustion), and **token-swap-with-IDE-restart** for a GUI tool (Antigravity) that has no clean CLI-config seam.
- **Unsigned** build: first launch needs a right-click-open or terminal bypass (the author hasn't set up code-signing/notarization yet).

## Where it sits in the corpus
- It's the **3rd "Tauri-desktop management-GUI for another coding agent"** (after **v73 cc-switch** — Claude Code provider/config switcher; **v117 CodexPlusPlus** — Codex management harness). That trio is the Library-vocab **LV-C7** cluster, now at **N=3 → promotion-eligible**. ai-switcher is the first of the three to manage **accounts + quota** rather than provider/config.
- Adjacent to (but distinct from) the **Multi-Source LLM Aggregator** pattern (cc-switch / freellmapi / CodexPlusPlus): those route *providers*; ai-switcher rotates *accounts* by quota. Different layer.
- **Antigravity** shows up again as a managed target (cf. v67 opencode-antigravity-auth, v85 ui-ux-pro-max).

## Provenance (§37)
≈**13★** / 8 forks / **11 commits** / **license: none yet** / Tauri (Rust 67.7% + TypeScript 22.0% + CSS 9.4%) / native macOS `.dmg` (unsigned).
*Page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified (§37.4)**; this environment mocks the GitHub API.* Micro-scale + nascent (11 commits) → **NOT a Pattern #52 claim.** Owner `hoangpm96` (Vietnamese inferred, location undeclared).

## Why it's goal-aligned (and a real pilot candidate)
- **On goal #1:** the subject's whole purpose is to *operate* Claude Code + peer coding agents (account/quota/auto-switch) — not an app that merely calls an LLM.
- **Directly vault-applicable:** Storm Bear runs Claude Code; juggling multiple accounts and not losing a session to a quota wall is a genuine workflow need.
- **CONDITIONAL pilot, though:** no license yet + unsigned `.dmg` + 11-commit nascency = trust-carefully. Trial at fenced scope only — read the repo or build from source on a scratch account, `install-snapshot` first, reversible. It joins the still-un-piloted goal-aligned backlog (v150 Paseo, v149 Scrapling, v144 headroom).

## §35 note
A goal-aligned v153 **satisfies** the §35 mandate after the v151/v152 off-goal breach, but does **not fully clear** it — window {v151 OG, v152 OG, v153 GA} = 2 OG still breached → **v154 must also be goal-aligned** to clear. Streak GA:15·OG:11 → **GA:16·OG:11 [7 ov]**.
