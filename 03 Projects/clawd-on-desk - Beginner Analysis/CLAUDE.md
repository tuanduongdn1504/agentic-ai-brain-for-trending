# clawd-on-desk — Beginner Analysis (project CLAUDE.md)

**Subject:** `rullerzhou-afk/clawd-on-desk` ("Clawd on Desk") (v156 wiki ship, 2026-06-05).
**Verdict:** **GOAL-ALIGNED INCLUDE 4/4** — (a) PASS-MODERATE (inferred-China-Mainland) · (b) STRONG · (c) STRONG · (d) STRONG.
**Routine:** v2.6 (§31/§35/§37).
**Requested:** "build LLM wiki ... macOS app to manage multiple AI coding tools."

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis verdict + §35 + §37 + honest non-claims.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY: desktop-pet-status-surface standalone → N=3 (NO new standalone); registry 06 edited.
- `02 Wiki/index.md` — the knowledge page.

## One-paragraph summary
**"A pixel desktop pet that watches Claude Code, Codex, Cursor & other AI coding agents — so you don't have to."** An **Electron** (JavaScript 92.4%) cross-platform (Win/macOS/Linux) desktop companion: a pixel-art pet with **12 animated states** (idle/thinking/typing/building/subagent-groove/multi-subagent-juggling/error/happy/notification/sweeping/carrying/sleeping) driven by **agent hooks + log-polling** (NO MCP) across **11+ agents** (Claude Code full via hooks+HTTP-permission, Codex, Copilot, Gemini, Antigravity, Cursor Agent, CodeBuddy, Kiro, Kimi, Qwen, opencode, Pi, OpenClaw, Hermes); **multi-agent coexistence** (independent sessions tracked simultaneously); a **permission bubble** to approve/deny tool requests from the pet UI. Goal-aligned (watches + lightly controls coding agents). Creators @rullerzhou-afk (鹿鹿) + @YOIMIYA66; AGPL-3.0 (code; artwork rights reserved); v0.8.1; 3.7k★. Acknowledges visual inspiration from `clawd-tank` (marciogranzotto) + LINUX DO community.

## Verdict rationale
- **(b) STRONG** = watches Claude Code + 11 agents via hooks + a permission-approve/deny bubble + multi-agent session dashboard = goal #1 + vault-applicable. **STRONG-not-STRONGEST** = an ambient companion + permission surface *around* the agents, not the substrate.
- **(a) PASS-MODERATE** = creator handle **鹿鹿** (Chinese characters) + LINUX DO (a Chinese dev community) = a reasonably solid **inferred-China-Mainland** cultural-peer signal (firmer than a latin-handle guess; location undeclared → MODERATE). Not load-bearing.
- (c) STRONG (Electron + hooks + HTTP-permission + log-polling fallback + 12 states + multi-agent coexistence; **1,123 commits / 25 releases / 3.7k★** = most mature+popular of the pet trio). (d) STRONG (desktop-pet-status-surface standalone N=3 + Pattern #84 cross-tool [11+ agents, broadest in corpus] + Chinese cluster + Hermes/Antigravity/OpenClaw corpus-recursive refs).

## §35 / streak
**§35 STAYS CLEAR** — window {v154 GA, v155 GA, v156 GA} = 0 OG (4 consecutive goal-aligned ships v153→v156). NOT an override → override-frequency UNCHANGED (7-in-20 trailing; lifetime 10). Streak GA:18·OG:11 [7 ov] → **GA:19·OG:11 [7 ov]** (19th GOAL-ALIGNED PASS).

## Pattern Library
**PRIMARY: "Ambient/Affective Multi-Agent Status Surface (reactive desktop-pet UI)" → N=3** (v154 agentpet + v155 openpets + v156 clawd-on-desk) → **PROMOTION-ELIGIBLE → recommend CONFIRMED at the overdue audit.** Three independent instances across **three integration mechanisms**: socket-daemon/CLI-wrapper (v154) · MCP (v155) · **hooks + log-polling** (v156) — the 3-mechanism spread settles the v155 "one-class-vs-two" question toward **one class, multiple integration mechanisms.** NEW affordance note: v156 adds a **permission-approve/deny bubble** (a light *control* affordance beyond pure observation) — a sub-feature, not a separate mint. **§28: 0 new standalones** (a strengthening, not a mint); registry 06 §C row updated N=2→N=3 (rule-5). NO confirmed-count change (46 patterns / 9 Library-vocab CONFIRMED). Observations (NOT minted): Pattern #84 cross-tool (11+ agents = broadest in corpus) + hooks/log-polling integration (3rd mechanism) + permission-bubble-as-control-affordance + Chinese cultural-peer cluster N+1 (inferred) + clawd-tank visual-lineage + LINUX-DO community-distribution + Hermes/Antigravity/OpenClaw corpus-recursive refs + Pattern #45 split-license (AGPL code + artwork-reserved) + micro-no: 3.7k★ but velocity unestablished → NOT #52.

## Provenance (§37)
≈**3.7k★** / 367 forks / **1,123 commits** / **25 releases** (latest v0.8.1, May 27 2026) / AGPL-3.0 (code; artwork rights reserved) / JavaScript 92.4% (+ HTML/CSS/Python/Shell) / Electron (Win/macOS/Linux) — page-stated as of 2026-06 via WebFetch, **NOT independently API-verified §37.4** (env mocks the GitHub API). Creation date unstated → velocity unestablished → **NOT a #52 claim** (most-starred of the pet trio: 3.7k vs 968 vs 40). Creators @rullerzhou-afk (鹿鹿) + @YOIMIYA66.

## Pilot
**Pilot candidate** (most mature/popular pet — 3.7k★/v0.8.1; hooks-based so plugs into Claude Code via hooks + HTTP permission). ⚠️ But this is the **4th "manage/monitor AI coding tools" ship in a row (v153/v154/v155/v156), 3 of them desktop-pets, ZERO piloted.** The catalogue is now ripe (the pet-surface standalone is at the N=3 promotion threshold) — the highest-value next move is the **overdue audit** (to bank the N=3 promotions) or a **pilot**, not a v157.

Shipped on branch `wiki/v156-clawd-on-desk` (stacked on the unmerged v155 branch). Not auto-merged — operator merges.
