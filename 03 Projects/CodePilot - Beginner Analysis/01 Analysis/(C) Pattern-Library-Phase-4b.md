# (C) CodePilot — Pattern Library Phase 4b

**Subject:** `op7418/CodePilot` (v161). **Verdict:** GOAL-ALIGNED INCLUDE 4/4. **Ships into:** the v158-audit-CONFIRMED Pattern Library.

## PRIMARY — 1 NEW §C standalone (PROVISIONAL N=1, CORPUS-FIRST)

> **"Desktop GUI Client / Visual Front-End for a CLI Coding Agent"** — a full graphical desktop application that wraps a CLI coding agent (here Claude Code) so the user **chats, codes, browses files, runs git, and drives agent sessions visually** instead of through the terminal; characteristically bundles **multi-provider switching**, **session checkpoint/rewind**, **skills + MCP**, and (here) a **remote messaging bridge** + **persona-memory workspace**. **PROVISIONAL N=1** (v161 CodePilot). CORPUS-FIRST.

**Why this is a genuine new standalone, not an instance of an existing pattern (the discipline):**
- **vs v99 cmux** — cmux is a *native-desktop terminal multiplexer* that hosts multiple agent sessions in panes; it is still a terminal surface. CodePilot is a **GUI chat/code/file/git client** (a visual IDE-like front-end), not a terminal host. Different surface.
- **vs LV-C7 #22 management-GUIs** (cc-switch / CodexPlusPlus / ai-switcher) — those are *config/account switchers* (you launch them to change which provider/account an agent uses, then go back to the terminal). CodePilot is the place you *actually operate the agent*. It has a control dimension (provider/account config) but that is one feature of a broad client — filing it as a 4th #22 would repeat the v118-OpenHuman honest-downgrade error ("uses a desktop GUI" ≠ "is a management-GUI").
- **vs v150 Paseo** — Paseo is a cross-device multi-vendor *orchestration platform* that runs heterogeneous agents as orchestration units (+ an agent-of-agents skill suite). CodePilot is a single-machine *GUI client* you drive interactively; it aggregates providers but does not orchestrate agents-as-units.
- **vs v118 OpenHuman** — OpenHuman is a *general agentic desktop assistant* (118-service personal assistant + memory tree). CodePilot is specifically a **Claude-Code front-end / visual programming client** (Guizang: *可视化编程助手*).
- Would I register this absent the 9th-in-niche pressure? **Yes** — "the GUI client you operate Claude Code inside" is a genuinely distinct, named shape (Guizang's own tagline + the bonza.cn writeup both frame it as *Claude Code 的原生桌面 GUI*). External corroboration (NOT counted): the broader "GUI/desktop front-end for a CLI coding agent" genre is emerging.

**§28 / counts:** **1 new §C standalone (≤2 cap honored); 0 new CONFIRMED Library-vocab (stays 10); top-level pattern count UNCHANGED at 46.** Filing acts (rule-5): registry `06` §C row added + §F v161 note; `02b` v161 instance-strengthening notes (#18 #8 N+1, T4c N+1).

## SECONDARY — instance-strengthenings + observations (NOT new mints)
- **Pattern #18 #8 "Multi-Source LLM Aggregator" (CONFIRMED N=3) → N+1 instance** — CodePilot aggregates 17+ providers behind one client with mid-conversation model switching. Sub-archetype already CONFIRMED → instance-strengthening only. A **"GUI-client aggregator" sub-variant (8c?)** is *flagged for the audit*, NOT minted now (anti-inflation; 8a config-switcher v73/v117, 8b live-routing-proxy v112).
- **T4c "Operator-Notification/Control-Bridge via Messaging Platform" (v88 teleport) → N+1** — CodePilot's Telegram/Feishu/Discord/QQ/WeChat bridge is *remote control from your phone*, a step beyond v88's notification-bridge. T4c strengthening; the control-vs-notify distinction noted for the audit.
- **agentskills.io / skills.sh** — CodePilot's skills system + skills.sh marketplace is 57k-chain-adjacent (skills.sh is the same external service noted at v93 anthropics/skills). Instance note; NOT claimed as a clean 57k `npx skills add` implementer.
- **Agent-memory persona files** (`soul.md` / `user.md` / `claude.md` / `memory.md`) — adjacency to the agent-memory cluster (v66 agentmemory / v132 supermemory). **Declined** as a v94/v118/v134 corpus-recursive-Karpathy-LLM-wiki instance: this is per-assistant persona/memory, not a self-maintaining knowledge wiki. Observation.
- **LV-C3 Self-Referential-Methodology-Demonstration (SOFT)** — Guizang's launch claim that CodePilot was "built in a day, entirely AI-assisted (Opus 4.6 + Agent Teams + Claude Code)" = the tool built by the agents it fronts. SOFT (a launch claim, no in-repo generator stamp); observation, NOT counted (v131 SOFT-instance discipline).
- **Pattern #45 license sub-variant — BSL-1.1 with change-date** — source-available, commercial-gated, auto-converts to Apache 2.0 on 2029-03-16. A license shape not previously prominent in the corpus; observation, NOT minted.
- **op7418/Guizang corpus-recursive → 3rd appearance** (v105 guizang-social-card-skill + v83 open-design bundle + v161 CodePilot); **Pattern #19 Chinese-AI-KOL + WeChat-funnel sub-mechanism** N+1 (WeChat group + guizang.ai + X). Observation.
- **Electron stack** (vs the Swift-native-macOS cluster v99/v100/v154/v157/v159/v160) — cross-platform, heterogeneous; observation.
- **Pattern #66** local-SQLite-WAL + BYOK + on-machine-data privacy posture; **Pattern #82** quantitative-marketing ("17+ providers", "high-颜值"). Observations.
- **NOT #52** (5.9k★, ~115d ≈ 51★/d page-stated → SUSTAINED-MODERATE-HIGH *if* accurate, but API mocked §37.4 → no promotion). **NOT a top-level Pattern.**

## Counts after this ship
46 patterns (UNCHANGED) / **10 Library-vocab CONFIRMED** (UNCHANGED) / **1 NEW §C standalone** "Desktop GUI Client / Visual Front-End for a CLI Coding Agent" N=1 / tracked PROVISIONAL surface ≈24 → **≈25** (+1 standalone). Streak **GA:24·OG:11 [7 ov]**; §35 CLEAR.

## The blunt note (carried to the response)
CodePilot is NOT the redundant 9th menu-bar monitor — it varies the archetype (a full GUI client you operate Claude Code inside, not a watcher) and (a) PASSes on a known cultural-peer (Guizang). It mints one honest new standalone (the GUI-client front-end shape) and strengthens two confirmed patterns (#18 #8 aggregator, T4c bridge). But it is still the **9th consecutive "manage/monitor AI coding tools" ship with ZERO piloted** — varying the domain is good, piloting is still the unaddressed lever. CodePilot is itself a strong pilot candidate (BSL-1.1 free for personal use; it's a tool you'd actually use to drive Claude Code).
