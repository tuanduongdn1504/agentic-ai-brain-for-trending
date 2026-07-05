---
source: manual single-video ingest (path 5 yt-dlp) + GitHub double deep-dive (path 3 curl/API)
topic: harness-engineering (DEEPEN — individual-scale 10th sibling, first-party VN talk + public factory repo pair)
generated: 2026-07-05
video: https://www.youtube.com/watch?v=LaIZ4yRd7mA
video_title: "AI Harness Engineering | Góc nhìn cá nhân và quick demo | FPT HCM 28/06/2026"
channel: TNT (@TNT-nz5be, UCwKqGtDYF1aLiMKI8SwZCXg) — personal channel of Trung Tran
duration: 46:17
views_at_fetch: 1,993 (2026-07-05)
uploaded: 2026-06-28
repo: https://github.com/trannamtrung1st/ai-engineering-learning (master; created 2026-06-24; TS; 6★; no license)
project: projects/ai-harnessed_we-event-app
workflow: wf_3740e2d5-2b4 (22 agents, ~1.55M tokens, 520 tool calls; 6 dives + 3 external verifiers + 12 refute-first claim verifiers + completeness critic)
---

# TNT / Trung Tran — AI Harness Engineering (FPT HCM talk + we-event factory repo)

Combined raw for the 2026-07-05 DEEPEN pass on `harness-engineering`.

## Contents

1. **Full cleaned VN transcript** (1,055 lines, ~46K chars): `2026-07-05-tnt-we-event-repo-extracts/transcript-clean.md` (original VTT alongside).
2. **Repo extracts** (18 files, fetched 2026-07-05): `2026-07-05-tnt-we-event-repo-extracts/repo/` — HARNESS-DESIGN.md, ai-harness README (12.7KB), 4 agent prompts (implementer/reviewer/tester/testgen), ralph-loop.json, testgen-loop.json, ralph-once.sh, pick-next-slice.sh, guardrails.md (55KB "Ralph Signs"), progress.md (35KB append-only run ledger), models.json, package.json, human-review-checklist.md, context-map.json, brds prompt.md, commits page 1.
3. Wiki articles produced: see `wiki/harness-engineering/` — tnt-cursor-cli-factory-anchor, tnt-we-event-harness-mechanics, tnt-factory-run-empirics, tnt-vs-corpus-positioning.

## Speaker (verified)

Trung Tran (trannamtrung1st, HCMC, "Techaholic", 70 public repos). Works at **Web Synergies** (Singapore; Yokogawa subsidiary — caption garble "Western Synergy" CORRECTED by verify agent per discard-as-garble guard), IoT/DX domain, full-stack engineer, ~1 year applying AI at work. Explicit non-expert framing ("góc nhìn cá nhân", not a standard to copy).

## Talk skeleton (timestamps)

- 00:00–14:26 personal framing: the 4 guiding questions (is it correct vs looks-correct / consistency across runs / regression-safe enhancement / detecting unintended changes); prompt → context → harness trend; agent coding as 2026 trend; goal-first harness definition (harness checks, machine-readable feedback, loop-until-correct); "how to make AI right first time" reframed to "how does the system detect wrong, feed back, and converge".
- 14:26–22:18 demo app We Event (event lifecycle Draft→Published→RegistrationOpen→…→Completed; personas OrganizerAdmin/Participant; docs-only start: brds + technical + ui-ux).
- 22:18–47:00 live factory demo: `aih:` commits every 15–30 min; reverts cover-image feature, re-runs loop live; agent picks `web-event-cover-image` slice from whole-app-backlog, implements, browser-tests 9/9 via Playwright MCP, reviewer evaluates with minor observations, commits. Q&A: harness itself vibe-coded then understood incrementally; structure portable / content per-project; Cursor + Auto model on ~$200/yr plan; validation vs evaluation distinction; token-optimization honestly unanswered ("mình cũng không trả lời được").
