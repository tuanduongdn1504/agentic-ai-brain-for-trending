# (C) Autopilot Loop — 2026-07-15-11

> **Trigger:** manual (`/loop`-style, operator-submitted single video)
> **Topic:** pocock-writing-great-skills — Matt Pocock, "Building Great Agent Skills: The Missing Manual" (`UNzCG3lw6O0`)
> **Started:** 2026-07-15 (main-loop session, Opus 4.8)
> **Ended:** 2026-07-15
> **Path:** 5 (yt-dlp only; no NotebookLM)

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 (yt-dlp transcript) | 1 (topic itself) | 0 | 1.0 |

Cold-start for a new topic; single-cycle compile. `gaps_closed_ratio = 1.0` (topic fully compiled, 11 wiki files + pilot deliverable, no stubs, all cross-links resolve).

## Sources ingested

- `raw/2026-07-15-pocock-writing-great-skills.md` (yt-dlp EN auto-captions, deduped, ~597 transcript lines + metadata header; ~29K)

## Verification

- Workflow `wf_d267ed85-320` — 20 agents (5 dives + 14 refute-first verifiers + 1 completeness critic), all Haiku 4.5; ~833K tokens, 245 tool calls, **0 errors / 0 empty**, ~7.9 min.
- ~12 Opus main-loop anchors: `gh api` (both repos + tree + `SKILL.md`/`GLOSSARY.md` fetches + a definitive count of user/model-invoked across all 40 `SKILL.md`), `WebFetch` (Anthropic `code.claude.com/docs/en/skills`, agentskills.io, superpowers README), `WebSearch` (World's Fair 2026 dates, aihero.dev).
- **5 Rule-12 main-loop overrides** of over-strict Haiku verdicts (CL2, CL3, CL6, CL7, CL14) + 1 dive token-mechanic reversal — same skill/docs-lag failure mode as local-ai / google-ai-studio / codesistency.

## Wiki articles created

- `wiki/pocock-writing-great-skills/_index.md` (NEW)
- `wiki/pocock-writing-great-skills/overview.md` (NEW)
- `wiki/pocock-writing-great-skills/the-skill-checklist.md` (NEW)
- `wiki/pocock-writing-great-skills/trigger-invocation-and-superpowers.md` (NEW)
- `wiki/pocock-writing-great-skills/disable-model-invocation-mechanism.md` (NEW)
- `wiki/pocock-writing-great-skills/steering-leading-words-and-legwork.md` (NEW)
- `wiki/pocock-writing-great-skills/talk-vs-published-skill.md` (NEW)
- `wiki/pocock-writing-great-skills/claims-scorecard.md` (NEW)
- `wiki/pocock-writing-great-skills/caveats-and-corrections.md` (NEW)
- `wiki/pocock-writing-great-skills/hireui-and-vault-pilot.md` (NEW)
- `wiki/pocock-writing-great-skills/source-provenance.md` (NEW)
- `wiki/_master-index.md` (UPDATED — added topic at top, newest-first)
- `raw/_inventory.md` (UPDATED — added 2026-07-15 row, status compiled)
- `output/(C) 2026-07-15-pocock-writing-great-skills-pilot-methods.md` (NEW — pilot menu A–D)

## Final metric

- `gaps_closed_ratio` = **1.0**
- **Scorecard (14 claims): 13 CONFIRMED / 1 CORRECT-BUT-INCOMPLETE / 0 MISLEADING / 0 FALSE / 0 FABRICATED** — cleanest content-rich talk in the corpus.
- Stop reason: single-cycle cold-start compile complete; target ratio (0.5) exceeded.

## Corpus-firsts / notable

- Corpus' **4th dedicated Matt Pocock topic**; **first how-to-*build*-skills manual** (a meta-tool for the vault's own skill layer).
- **Cleanest content-rich scorecard in the corpus** (13/14 CONFIRMED, 0 misleading/false/fabricated) — beats github-copilot-cli-agents' 6/8.
- **Sharpest agentskills.io data point yet:** `disable-model-invocation` is an official Claude Code field but a **Claude-Code extension**, not in the portable 6-field open standard.
- **5 Rule-12 overrides** in one topic (tied for corpus-high with google-ai-studio's Haiku-docs-lag batch) — all skill/docs-lag over-strictness, incl. a load-bearing miscount (verifier said 50/50; actual 23/40).

## Top-3 unclosed gaps

1. `2PRD`→`to-spec` naming history is a documented *correspondence*, not a git-proven rename (no `2prd` trace remains) — flagged honestly in [[pocock-writing-great-skills/talk-vs-published-skill]]; would need git archaeology to close.
2. "AI coding crash course" is a forward-looking plan (aihero.dev currently has the narrower "AI SDK v6 Crash Course") — recheck in a few months.
3. Pilot not yet run — A1 (run `writing-great-skills` over the autopilot routine) is spec'd but undeployed; adds to the standing 0-deployed pilot backlog.

## Suggested next action

Run **pilot A1** this week (`npx`/clone `writing-great-skills` → invoke over the ~1,200-line `autopilot-research-routine.md`; deletion-test the cuts) — the lowest-friction pilot in the corpus. Then decide the D1 portability ADR (Claude-Code-extension vs agentskills.io-core) for the vault's skills. Commit decision for this ship: files are on the `autopilot-research` branch working tree, awaiting operator's `git commit`.
