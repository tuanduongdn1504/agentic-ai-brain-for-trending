# (C) Pattern Library mini-audit — v167 (2026-06-16)

**Trigger:** operator-requested (the overdue ~v167 audit), with a specific factual question to verify — *"verify wiki v153–v166 to be related topic macOS app to manage multiple AI coding tools, right?"*
**Window:** v159 → v166 (since the v158 audit), with a full re-verification sweep of the whole v153→v166 "operating-AI-coding-agents" run.
**Method:** attempted as a fan-out Workflow (14 subject-verifiers + 5 audit-analyzers + adversarial pass); **the workflow died on launch — every subagent exceeded the 200K context limit** (see Finding 7). Re-run in the main loop (Opus 4.8 [1M context]) with **8 live WebFetch spot-checks** of the rendered repos (v157/v158/v156/v161/v162/v163 this session + v165/v166 verified at their ships) — so this is **NOT a memory-only audit; classification was empirically ground-truthed**.
**Branch:** `wiki/audit-v167`, stacked on `wiki/v166-ai-agent-session-center` (so it sees v166). NOT merged.

---

## HEADLINE

1. **The operator's framing is directionally right but factually too narrow on BOTH axes.** v153–v166 are **not** "macOS apps to manage multiple AI coding tools." Empirically: **only 5 of 14 are macOS-only**; the rest are cross-platform (Electron/Tauri), **web**, **Linux+macOS TUI**, or **multi-surface incl. iOS**. And they are **not all "manage/monitor"** — they split into **5 distinct shapes**. The accurate umbrella is the corpus's own: **"tools for *operating* AI coding agents."** "Multiple tools" *is* mostly accurate (13/14 work across several agents). (Finding 1.)
2. **Both deferred N=2 promotion buckets HOLD at N=2 — no clean 3rd appeared.** Session-multiplexer species (cmux v99 + AoE v162) and orchestration-platform standalone (Paseo v150 + ai-maestro v163) each stay N=2; v164/v165/v166 are all observability, not multiplexer/orchestration. **Anti-inflation: do NOT promote without a clean 3rd.** (Findings 2–3.)
3. **Observability sub-archetype counts VERIFIED at N=12** = (a) metering 6 + (b) ambient/affective 5 + (c) attention-routing 1. The arithmetic is clean; v166's placement in (b) is defensible with a new "web-dashboard-hybrid" sub-note. (Finding 4.)
4. **Bookkeeping clean:** 46 confirmed patterns / 10 CONFIRMED Library-vocab UNCHANGED; streak GA:29·OG:11 [7 ov]; §35 CLEAR (14 consecutive GA v153→v166). **Override-review DISCHARGED a 7th time; no 4th governor. No §28 retires** (June-burst items all <30 days). (Findings 5–6.)
5. **NEW INFRA finding (the real new deliverable): the root `CLAUDE.md` shim alone (~210K tokens with tool defs) exceeds the 200K subagent context limit** → workflow/subagent use is now *blocked*, not just degraded. The v57/session-67 infrastructure block has recurred. This **upgrades the standing shim-rebuild recommendation (v162 rec iii) from "nice-to-have, pending sign-off" to "infrastructure-blocking."** (Finding 7.)
6. **The lever, louder than ever: 14 consecutive in-niche ships, ZERO piloted.** The catalogue is mature; the next high-value move is a pilot or a domain-shift, not a v167-in-niche.

**State after this audit: 46 confirmed patterns / 10 CONFIRMED Library-vocab — UNCHANGED. Streak UNCHANGED (audit ≠ ship): GA:29·OG:11 [7 ov]. §35 CLEAR. 0 promotions, 0 retires, 0 new mints.**

---

## FINDING 1 — the v153→v166 map (answers the operator's question)

**Empirically verified (live WebFetch where marked ✓; corpus-entry otherwise):**

| v | subject | platform | macOS-only? | primary function (shape) | multi-tool? |
|---|---|---|---|---|---|
| v153 | ai-switcher | native-macOS (Tauri) | **yes** | **control** — account/quota management-GUI (LV-C7 #22) | yes (3) |
| v154 | agentpet | native-macOS (Swift) | **yes** | observe — ambient pet | yes (7) |
| v155 | openpets | Electron x-platform | no | observe — ambient pet (MCP) | yes |
| v156 | clawd-on-desk | Electron (Win/macOS/Linux) ✓ | no | observe — ambient pet (hooks) | yes (11+) |
| v157 | ClaudeBar | native-macOS ✓ | **yes** | observe — quota metering | yes (10) |
| v158 | ai-token-monitor | Tauri (macOS+Win; Linux untested) ✓ | no | observe — token metering + social leaderboard | yes (3) |
| v159 | CodexBar | native-macOS (Swift) | **yes** | observe — metering (40+ providers) | yes (40+) |
| v160 | ping-island | native-macOS (Swift notch) | **yes** | observe → **attention/approval-routing** (sub-flavor c) | yes (13) |
| v161 | CodePilot | Electron+Next.js (mac/Win/Linux) ✓ | no | **GUI client / visual front-end** (multi-model desktop client) | yes (17+) |
| v162 | agent-of-empires | Linux+macOS, TUI+web ✓ | no | **host / multiplex sessions** (tmux) | yes (13) |
| v163 | ai-maestro | macOS+Linux+Win, local/cloud, web ✓ | no | **orchestrate multi-agent** (A2A messaging) | yes (7) |
| v164 | oc-claw | Tauri (macOS+Windows) | no | observe — ambient pet | yes (7) |
| v165 | lazyagent | Go TUI + macOS menu-bar + HTTP API + iOS | no | observe — monitor + transcript-maintenance | yes (9) |
| v166 | ai-agent-session-center | **web / "any device"** ✓ | **no** | observe — 3D-robot dashboard + light queue/approval | yes (3) |

**Platform tally:** macOS-only = **5/14** (v153, v154, v157, v159, v160). NOT macOS-only = **9/14** (cross-platform Electron/Tauri ×5, web ×1, Linux+macOS TUI ×1, web-platform ×1, Go-multi-surface+iOS ×1).
**Function tally (5 shapes):** observability (observe/monitor, incl. v160 attention-routing) = **10/14** · control/management-GUI = **1** (v153) · GUI-client/front-end = **1** (v161) · host/multiplex = **1** (v162) · orchestrate = **1** (v163).

**Verdict on the framing:**
- ❌ **"macOS app"** — wrong for the majority (9/14 are not macOS-only; v166 is a web app, v162 is a Linux+macOS TUI, v163 is a self-hosted web platform, v161/v155/v156/v158/v164 are Electron/Tauri cross-platform, v165 is multi-surface incl. iOS).
- ⚠️ **"to manage"** — too narrow. 10/14 are **observe** (a watcher, not a manager); only **1** (v153) is strictly account/config **control**; and **3** (v161 GUI-client, v162 host/multiplex, v163 orchestrate) are neither observe nor manage.
- ✅ **"multiple AI coding tools"** — mostly accurate (13/14 operate across several agents).
- ✅ **the true common thread** — they are all **"tools for operating AI coding agents"** (the corpus's own umbrella). That is the accurate one-liner.

**Minor refinement (not a correction):** v161 CodePilot's *live* tagline reads *"A multi-model AI agent desktop client — connect any AI provider, extend with MCP & skills, control from your phone"* — broader than the corpus's §C-standalone name "Desktop GUI Client / Visual Front-End for a CLI Coding Agent." The standalone holds (it IS an Electron desktop GUI client wrapping Claude Code + peers), but the framing leans more "multi-model agent client" than "front-end for a single CLI agent." Recorded for refinement at a future N=2.

---

## FINDING 2 — Session-Hosting Multiplexer species → HOLD at N=2

cmux (v99, native-desktop terminal multiplexer) + agent-of-empires (v162, cross-platform TUI+web, **tmux + git-worktree-per-agent, hosts/spawns each session itself** ✓ re-verified). = **N=2.** No clean 3rd in v163–v166: v163 orchestrates (agents-as-units), v164/v165 observe, **v166 OBSERVES-not-hosts** (verified at its ship: hooks are "purely observational"; the user launches the CLIs; node-pty terminals attach/display). **HOLD at N=2, PROMOTION-ELIGIBLE at N=3.** Do not promote without a clean 3rd (the v158 don't-generalize-to-fit discipline).

## FINDING 3 — Multi-Vendor Orchestration Platform standalone → HOLD at N=2

Paseo (v150, cross-device agent-of-agents via skill-suite) + ai-maestro (v163, multi-machine **agent-to-agent messaging mesh** + memory + code-graph ✓ re-verified "OS for AI-first orgs"). = **N=2**, two sub-flavors recorded inside. No 3rd in v164–v166 (all observability). Clean distinction from the multiplexer species: a multiplexer *hosts human-driven sessions*; an orchestration platform runs *agents as units / agent-to-agent*. **HOLD at N=2, PROMOTION-ELIGIBLE at N=3.**

## FINDING 4 — Observability sub-archetype counts VERIFIED at N=12

CONFIRMED at the v158 audit. Current instance lists:
- **(a) metering / quota / usage** — N=6: v89, v109, v157, v158, v159, v165.
- **(b) ambient / affective status-surface** — N=5: v154, v155, v156, v164, **v166**.
- **(c) attention / approval-interrupt-routing** — N=1: v160.
- 6 + 5 + 1 = **12.** ✓ arithmetic clean. No double-count (the v158 desktop-pet-standalone→(b) reconcile stands).

**v166 placement call (recorded):** v166 is counted in (b) because its run-state-driven 3D-robot avatars are the primary signature — but it is the **first web-delivered / 3D-robot / dashboard-hybrid (b) instance** (vs the desktop-pet delivery of v154/v155/v156/v164), and it co-hosts dashboard panels (terminals/logs/queue) + (c)-style approve/deny + a light prompt-queue. **DECISION: add a "web-dashboard-hybrid" sub-note under (b)** — it does NOT split (b) and does NOT mint a new sub-flavor (a 4th "dashboard/mission-control" sub-flavor would inflate, the v160/v165 discipline). Sub-flavor **(c) stays N=1** (only v160) — promotion-eligible at N=2, nothing owed.

## FINDING 5 — Bookkeeping VERIFIED

- **Counts:** 46 confirmed top-level patterns / **10 CONFIRMED Library-vocab** (since #22 LV-C7 promoted at v158) — UNCHANGED.
- **Streak:** GA:29 · OG:11 [7 ov] (v166 = 29th goal-aligned PASS). §35 CLEAR — window {v164 GA, v165 GA, v166 GA} = 0 OG; **14 consecutive goal-aligned ships v153→v166**.
- **Tracked PROVISIONAL Library-vocab surface ≈ 26** — UNCHANGED (v166 added 0 standalones).

## FINDING 6 — Override-review DISCHARGED (7th time) + NO §28 retires

- **Override-frequency:** 10 lifetime overrides; 7-in-20 forward (v127+v139+v142+v145+v146+v148+v152); 3 logged `[ceiling-override]` (v146/v148/v152). Common-cause **RE-CONFIRMED (7th confirmation): intake-channel off-goal capture via the override door, NOT a Phase-0.9 criteria defect.** Strong positive signal: **v153→v166 = 14 consecutive GA, zero overrides** — when subject-selection is goal-aligned, no governor fires. **NO 4th governor; NO criteria redesign.**
- **§28.3 time-aware auto-retire** (retire a live N=1 §C standalone only after BOTH ≥15 wikis AND ≥30 days without strengthening). Live N=1 standalones (MemoryBench v132 ~06-01, Bi-Temporal-Fact v134 ~06-02, Social-Leaderboard v158 06-05, Desktop-GUI-Client v161 06-05, Agent-Session-Transcript-Maintenance v165 06-15, …) all shipped in the v126→v166 June burst (2026-06-01 → 06-15). As of **2026-06-16**, the oldest is ~15 days — **under the 30-day floor**. **NO retires** (the 30-day floor exists precisely to protect burst-shipped items). Orchestration-platform standalone is now N=2 (v150+v163), not a retire candidate.

## FINDING 7 — NEW: shim now exceeds subagent context limit (INFRA-BLOCKING)

The fan-out workflow for this audit **failed at launch — all 20 subagents returned "Prompt is too long · ~213,772 tokens (limit 200,000)"** before executing a step. Cause: workflow subagents auto-load `CLAUDE.md` as project instructions, and the shim + tool definitions now total ~210K tokens — **the shim alone blows the subagent context budget.** This is the **v57 / session-67 infrastructure block recurring** ("584KB / ~146K tokens — too large for any agent to read without context-thrashing"); the shim was refactored to ~7KB then, and v57→v166 accumulation has regrown it past the subagent ceiling.

**Consequence:** workflows / subagents are currently **non-viable** for this vault (main-loop Opus 1M-context still works, which is why this audit completed solo). **This upgrades the standing shim-rebuild recommendation:**

> **Rec (iii) [v162] — UPGRADED from PENDING-nice-to-have → INFRASTRUCTURE-BLOCKING.** A dedicated shim-rebuild/compaction session is now required to restore subagent/workflow capability. The live PL-state header + Weekly Update have grown to dozens of full per-ship paragraphs inline; these should be compacted to one-line pointers (the detail already lives in `_state/03c-projects-v61-v166.md` + `04 Reviews/`), the same move made at session 67/68 and the hello-agents Ch-9 compaction.

---

## STANDING RECOMMENDATIONS (still PENDING operator sign-off — carried, not auto-adopted)

- **(i) off-goal-intake lever** [v151] — re-baseline the override trigger OR make the corpus-knowledge-outlier track the default for off-goal subjects. *(Moot across v153→v166 — 14 consecutive GA, zero off-goal — but unresolved for the next off-goal subject.)*
- **(ii) (a)-rescue tightening** [v151] — require a *solid* (a) signal (declared/located or registered (a)-7), not a name/heritage inference. *(Applied de-facto across v159–v166: every (a) was FAILed honestly — steipete/erha19/rainnoon/nahime0/coding-by-feng — so the discipline is holding even un-codified.)*
- **(iii) dedicated shim-rebuild session** [v162] — **now UPGRADED to infrastructure-blocking (Finding 7).** Recommend doing this BEFORE the next ship or audit, so subagents/workflows work again.

## THE LEVER (unchanged, louder)

**14 consecutive "tool for operating AI coding agents" ships (v153→v166), ZERO piloted.** The catalogue in this niche is mature and structurally complete: the observability sub-archetype is CONFIRMED with 3 sub-flavors (N=12), and two adjacent N=2 buckets (multiplexer, orchestration) are mapped and waiting on a clean 3rd. v164/v165/v166 minted ~nothing new (v164 0, v165 1 capability standalone, v166 0) — diminishing returns are now explicit. The genuinely high-value next moves:
- **Pilot one** — agent-of-empires (v162) is closest to Storm Bear's own workflow (run parallel Claude Code agents across branches); ai-token-monitor (v158) / CodexBar (v159) are the most directly useful monitors; agentpet (v154) / ping-island (v160) the lightest trials.
- **Vary the domain** — a goal-#1 subject *outside* the operate-agents niche.
- **Do the shim-rebuild** (Finding 7) — now a prerequisite for restoring workflow/subagent capability.

## Fact-verification status

**ADVANCED (not merely HELD) on classification.** 8 subjects re-fetched live this session (v156/v157/v158/v161/v162/v163 in this audit + v165/v166 at their ships) via WebFetch of the rendered repos — **0 hard corrections**, 1 minor framing-refinement (v161, see Finding 1). The rendered-page WebFetch works even though the GitHub **API** is mocked (§37.4) — so platform/function/tagline are verifiable, but **stars / fork-counts / creation-dates remain API-mocked-unverifiable** (hence no #52 claims across this run). Cadence reset: next natural audit ~v171–v172 (or operator-elected / trigger-forced).

*(Authoritative state head = the root shim's PL-state banner. This doc is the full record; pattern-layer notes filed to `_patterns/02b` (observability (b) sub-note) + `_patterns/06` §F (v167-audit clause).)*
