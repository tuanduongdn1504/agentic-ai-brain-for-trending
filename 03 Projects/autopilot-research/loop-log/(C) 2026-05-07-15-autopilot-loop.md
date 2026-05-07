# (C) Autopilot Loop — 2026-05-07-15 (drain top 2)

> **Status:** Complete ✅
> **Trigger:** Manual `/loop autopilot research drain queue` (top-2 mode chosen by operator)
> **Topics:** workflow-ai-coding + 10x-claude-code (queue items #1 + #2)
> **Started:** 2026-05-07 ~14:30
> **Ended:** 2026-05-07 ~15:30
> **Duration:** ~60 min wall-clock for both topics
> **Worktree:** `/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research`

---

## Phase 0 — Pre-flight ✅

| Check | Result |
|---|---|
| yt-dlp on PATH | ✅ |
| notebooklm in venv | ✅ v0.3.4 |
| AUTOPILOT_ROOT | ✅ |
| `notebooklm auth check` | ✅ valid |

---

## Phase 1 — Wiki state

- Articles before: 7 (`claude-code-hooks` × 6 + `_master-index`)
- Topics before: 1
- **`gaps_at_start = 2`** (both queue items represent gaps in current wiki)

---

## Phase 2 — Source ingestion

### Topic 1: Workflow for AI Coding

- yt-search query: `Workflow for AI Coding Matt Pocock Karpathy AI engineer`
- 20 results returned, 6 selected by relevance + diversity + recency:
  1. Matt Pocock — Full Walkthrough: Workflow for AI Coding (1:36:30)
  2. Matt Pocock — Software Fundamentals Matter More Than Ever (18:26)
  3. Ryan Lopopolo (OpenAI) — Harness Engineering (46:20)
  4. Barry Zhang & Mahesh Murag (Anthropic) — Don't Build Agents, Build Skills (16:22)
  5. AI LABS (re Boris) — Claude Code's Creator Does This (9:54)
  6. Greg Isenberg — Ralph Wiggum AI Agent (28:45)
- NotebookLM bundle: `ec93ea09-b589-4103-95a9-3fb2c13d5a2e`
- All 6 sources `ready` within ~5s

### Topic 2: How to 10x Claude Code

- yt-search queries: `How to 10x Claude code Tips Tricks` + `Sean Kochel Claude Code` + `Chase H AI Claude Code`
- 6 selected (all 5 named creators + 1 diversity):
  1. Sean Kochel — 15 Claude Code Tricks That Feel Like Cheating (21:59)
  2. Nate Herk — Andrej Karpathy Just 10x'd Everyone's Claude Code (17:46)
  3. Eric Tech — Claude Skills Explained (22:50)
  4. Boris Cherny @ Y Combinator — Inside Claude Code With Its Creator (50:10)
  5. Chase AI — 567 Hours of Claude Code Lessons in 20 Minutes (20:48)
  6. AI LABS — 10 Crazy Claude Code Tips (12:20)
- NotebookLM bundle: `d1d18b0b-ab85-4773-a999-98f36fb39cf5`
- All 6 sources `ready` within ~8s

---

## Phase 3 — Analysis (per topic)

For each topic: 1× `notebooklm summary` + 4× `notebooklm ask` (Trends / Outliers / Gaps / Key Takeaways).

- Topic 1: 5 calls, ~311 lines raw output → `raw/2026-05-07-workflow-ai-coding.md`
- Topic 2: 5 calls, ~301 lines raw output → `raw/2026-05-07-10x-claude-code.md`
- **Total NotebookLM API calls this loop: 10** (still well within 10/cycle budget per topic = 20 budget; used 10/20 = 50%)

---

## Phase 4 — Compile

### Topic 1 → `wiki/workflow-ai-coding/`

| File | Source section |
|---|---|
| `_index.md` | Topic index + sources + cross-links |
| `overview.md` | Ralph Wiggum loop frame + code-as-premium-asset thesis |
| `core-patterns.md` | 5 trend clusters: planning-first, autonomous loop, persistent memory, verification, infinite parallelization |
| `expert-disagreements.md` | 6 axes of disagreement (code-is-free vs code-is-expensive, plan-mode vs grill-me, compact vs clear, etc.) |
| `practical-takeaways.md` | 10 adoptable rules with attribution |
| `gaps-and-followups.md` | 5 gaps + 7 follow-up topics |

### Topic 2 → `wiki/10x-claude-code/`

| File | Source section |
|---|---|
| `_index.md` | Topic index + sources + cross-links |
| `overview.md` | Claude Code as orchestrator + Boris's surprises |
| `tactical-tricks.md` | 10 specific configurations ranked by adoption ease |
| `creator-disagreements.md` | 5 axes (Opus-everything vs model-switching, plan-mode lifespan, claude.md philosophy, browser strategy, terminal vs GUI) |
| `claude-md-philosophy.md` | Deep-dive: minimalist (Boris 2-line) vs documentary (AI LABS multi-file) vs skill-decomposed (Eric Tech) |
| `gaps-production.md` | 6 production gaps + 7 follow-up topics |

---

## Phase 5 — Cross-link

12 cross-links written into the topic articles:

- Topic 2 → Topic 1: 6 references (planning-first frame, infinite-parallelization, persistent-memory consensus, etc.)
- Topic 1 → claude-code-hooks: 1 reference (skills/hooks complement)
- Topic 2 → claude-code-hooks: 2 references (Exit Code 2 deep-dive, hook layer for production gaps)
- Topic 1 internal: 4 cross-references (overview ↔ core-patterns ↔ disagreements ↔ takeaways)
- Topic 2 internal: 5 cross-references (overview ↔ tricks ↔ disagreements ↔ claude-md-philosophy ↔ gaps)

`_master-index.md` updated with both new topic entries.

---

## Phase 6 — Audit

| Metric | Before | After | Δ |
|---|---|---|---|
| Articles | 7 | 19 | +12 |
| Topics | 1 | 3 | +2 |
| `(gap\|TODO\|missing\|stub)` markers | 0 | 0 | 0 |
| Wiki disk size | ~48 KB | ~120 KB | +72 KB |
| **`gaps`** | **2** (queue items 1+2) | **0** | **−2** |

**`gaps_closed_ratio = (2 − 0) / 2 = 1.0`** — both queued topics fully compiled with no `(gap)` markers in output.

---

## Phase 7 — Decide

| Stop condition | Threshold | Actual | Triggered? |
|---|---|---|---|
| `gaps_closed_ratio` | ≥ 0.5 | 1.0 | ✅ STOP |
| `cycles_completed` | ≥ 5 | 2 | — |
| `wall_clock` | ≥ 60 min | ~60 min | borderline |
| `notebooklm_calls` | ≥ 10/topic | 5/topic | — |
| Operator-requested top-2 only | — | yes | ✅ STOP |

**Stop reason:** operator selected drain-top-2 mode + `gaps_closed_ratio = 1.0`. Hand control back. No `ScheduleWakeup` (constitutional invariant #6).

---

## Surprises / lessons

1. **Cross-topic linking compounds value.** Topic 2 references Topic 1 six times; this would have been 0 if topics were drained independently. Bundling related topics in one drain session creates richer cross-links.
2. **`notebooklm summary` output truncated at first run.** Used `sed -n '/^[A-Z]/,$p'` to skip pre-content noise; worked for both summary and ask outputs. Worth codifying in skill.
3. **Boris Cherny YC interview was the highest-signal source for Topic 2.** As the creator of Claude Code, his contrarian takes (Plan Mode disappearing, 2-line `claude.md`, terminal-as-prototype) anchored the disagreement axes. Lesson: when researching a tool, find the creator's recent interview; it's worth 2-3 derivative tutorial videos.
4. **Topic 2 corpus surfaced production gaps strongly** — speakers admit the 10-min YouTube format doesn't suit production-scale topics (CI/CD, secrets mgmt, observability, IP). Confirms the "follow-up to autopilot" pattern: tactics from creators, production from conference talks + engineering blogs.
5. **`yt-dlp ytsearch` query needs cleaning** for special chars. First query with `@username` syntax returned zero results. Strip handles + retry.
6. **6-source bundles work well.** Quality didn't seem to need 8; budget didn't need 5. 6 is a sweet spot per topic.

---

## Suggested next actions (per Storm Bear prime directive)

1. **Spot-read the 12 articles** in Obsidian or any md viewer. Verify cross-links resolve. Check Vietnamese-mixed-output didn't sneak into English-source topics.
2. **Decide on remaining 4 queued topics** (Telegram bot, Claude Code SDK headless, MCP messaging, tunneling). They form a coherent "remote control Claude from phone" bundle. Drain them in a follow-up session for maximal cross-linking.
3. **Consider promoting `workflow-ai-coding` and `10x-claude-code` to Storm Bear curated wiki** if they hold up after a week's use. They map cleanly to the existing v60+ Pattern Library agenda.
4. **Calibrate v2.2 routine:** observed wall-clock for 2-topic drain = ~60 min. Reduce default `wall_clock_budget` for `/loop` mode from 60 to 90 (covers 2-3 topics) instead of 60 (covers only 1).
