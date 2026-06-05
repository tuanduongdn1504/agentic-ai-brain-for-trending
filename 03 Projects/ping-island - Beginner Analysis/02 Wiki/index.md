# (C) erha19/ping-island (v160 wiki)

> **Status: GOAL-ALIGNED INCLUDE 3/4** ((a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG). A native-macOS **notch / Dynamic-Island** command center that surfaces the *moments an AI coding agent needs you* — approvals, input requests, reviews — across 13 tools, lets you act in place, and routes focus back to the source. **Unlike v159 CodexBar (a clean metering instance, 0 mints), ping-island is genuinely additive:** it mints a **new 3rd sub-flavor (c) — "attention / approval-interrupt-routing surface"** — of the observability sub-archetype confirmed at the v158 audit. NOT metering, NOT a desktop-pet. See `01 Analysis/`.

**Repo:** https://github.com/erha19/ping-island · **Owner:** `erha19` (no name/affiliation/location disclosed) · **License:** Apache 2.0
**Tagline:** *"A Dynamic Island-style command center for managing all your AI coding agents on macOS."*
**Site:** https://erha19.github.io/ping-island/

## What it is
An **attention-first** macOS surface for multi-agent coding. It stays compact until a session **needs action** (tool-call approval, an input/follow-up prompt, a review, an intervention), then expands from the **notch / Dynamic Island** (or menu bar) with the session's context and one-click **approve / deny / answer** controls — and **routes focus back** to the originating terminal or IDE window. The framing (verbatim): it treats agent approvals and input requests as **"actionable focus interrupts"** routed back to the source, *"rather than read-only dashboards."* That last phrase is the whole point — it is explicitly **not** a usage/cost monitor.

## Agents it works with (13)
Claude Code · OpenAI Codex · Gemini CLI · Hermes Agent · Qwen Code · Kimi CLI · OpenClaw · OpenCode · Cursor · Qoder · CodeBuddy · WorkBuddy · GitHub Copilot.

## How it integrates (the instructive part)
- **Managed hook files** — installs Claude-style JSON hooks into each client's config (`~/.claude/settings.json`, `~/.qwen/settings.json`, …), a Hermes plugin (`~/.hermes/plugins/ping_island/`), and OpenClaw gateway hooks. The same hooks-integration mechanism as v156 clawd-on-desk.
- **Live `codex app-server` WebSocket** monitoring for Codex sessions.
- **SSH tunnel forwarding as a *core* workflow** (not a sidecar): bootstraps a `PingIslandBridge` onto remote hosts, rewrites their hooks to target it, and forwards remote agent activity into your local notch. Corpus-first as a first-class workflow element.
- **IDE extensions** (VS Code-compatible) + multi-client transcript backfill (e.g. reads `~/.openclaw/agents/main/sessions/` so the UI shows full context).
- Cosmetic layer: per-client animated mascots + sound packs (OpenPeon/CESP-compatible + an 8-bit pack) — secondary, not the primary display.

## Where it sits in the corpus
- It is a member of the **CONFIRMED (v158 audit) "AI-Agent Observability / Status-Surface Tool" sub-archetype** — but it mints a **NEW 3rd sub-flavor (c): "attention / approval-interrupt-routing surface (notch/Dynamic-Island-first, focus-return + SSH-forwarding)"** — PROVISIONAL N=1, CORPUS-FIRST.
  - Distinct from **(a) metering/quota** (v89/v109/v157/v158/v159 — read-only usage/cost numbers): ping-island surfaces *actionable interrupts*, not metrics.
  - Distinct from **(b) ambient/affective pet** (v154/v155/v156): the mascot is cosmetic; the core is triage + focus-routing, not an affective character.
- **Light-control affordance, but NOT LV-C7 #22:** approving/denying *the agent's own permission prompts* + answering its inputs is a pass-through of the agent's requests (the same kind of permission affordance v156 clawd-on-desk had as a sub-feature) — **not** managing provider/config/accounts (cc-switch/CodexPlusPlus/ai-switcher). It OBSERVES + ROUTES; it does not CONTROL the agent's configuration.
- **Forming external genre (NOT in corpus, not counted, noted):** "Dynamic Island for AI coding agents" is becoming its own micro-genre — CodeIsland, xisland, Vibe Island all exist — which corroborates that sub-flavor (c) is a real emerging class, not a one-off. Promotion-eligible at a genuine in-corpus N=2.

## Provenance (§37)
≈**832★** / 89 forks / 1 watcher / 3 open issues / **433 commits** / latest **v0.21.1** (Jun 5 2026) / Apache 2.0 / **Swift 6.1 (98.5%)** + Shell / native macOS 14+ (Xcode project).
*Page-stated as of 2026-06 via WebFetch of the rendered repo + erha19.github.io/ping-island — **NOT independently API-verified (§37.4)**; env mocks the GitHub API.* Created date NOT shown → velocity unestablished → **NOT a Pattern #52 claim.** Owner `erha19` — the repo discloses no real name, affiliation, or location (so **no cultural-peer inferred from the handle** — the v139 / v151-(a)-rescue discipline).

## Why it's goal-aligned (and a strong pilot)
- **On goal #1, and arguably the most *useful* of the niche:** the thing that actually breaks multi-agent flow is "an agent is blocked waiting on my approval/input and I didn't notice" — ping-island targets exactly that, and handles it in place. For heavy parallel Claude Code + Codex use, that's a concrete workflow win, not a dashboard.
- **Strong pilot candidate:** Apache-2.0 + mature (433 commits / v0.21.1) + `brew install --cask ping-island`, reversible, `install-snapshot` first. ⚠️ It installs managed hooks into your agents' config files — so snapshot `~/.claude/settings.json` (etc.) first and review what it writes.
- ⚠️ **8th consecutive "monitor/manage AI coding tools" subject (v153–v160), ZERO piloted.** This one mints a real sub-flavor (unlike v159), so it advances the Pattern Library — but the high-value move remains a **pilot** (ping-island or CodexBar/ClaudeBar) or a **goal-#1 subject outside the monitor niche.**

## §35 note
A goal-aligned v160 keeps the ceiling clear: window {v158 GA, v159 GA, v160 GA} = 0 OG (eight consecutive goal-aligned ships v153→v160). Streak GA:22·OG:11 → **GA:23·OG:11 [7 ov]** (23rd goal-aligned PASS; not an override).
