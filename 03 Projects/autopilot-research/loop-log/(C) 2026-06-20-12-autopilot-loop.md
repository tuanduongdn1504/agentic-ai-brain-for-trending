# (C) Autopilot Loop — 2026-06-20-12

> **Trigger:** manual (operator-submitted video + "double deep-dive into the original" + "show me many methods to apply")
> **Topic:** claude-skills (Ben AI "8 Claude Skills I Can't Live Without")
> **Started:** 2026-06-20 ~11:46 (+07) · **Ended:** ~12:30 (+07) · **Duration:** ~45m wall (incl. a session-limit pause)

## What ran

1. Identified video via WebFetch+WebSearch (Ben AI, `bXnRA3pJavE`); pulled full transcript via `yt-dlp --write-auto-subs` → deduped → `raw/(C) 2026-06-20-ben-ai-8-claude-skills.md`.
2. Mapped the 8 skills → their original resources.
3. Workflow `wf_884737d0-afa` (28 agents, 3 phases: research originals → draft+verify articles → synthesize crosswalk/provenance/pilot+critic).
   - **First run hit the Claude subscription session limit** mid-flight (resets 12pm Saigon); only 3/8 research agents finished. **Resumed at 12:01** with `resumeFromRunId` — 3 cached + the rest live. Completed: 7/8 research (the `mcp-builder` research agent failed "prompt too long"), 8/8 articles drafted+verified, crosswalk+provenance+pilot+critic.
4. Main-loop verification + librarian assembly (see corrections below).

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 (cold-start topic) | 1 video + 7 verified originals | 1 (topic itself) | 0 | 1.0 |

`gaps_closed_ratio = 1.0` (new topic fully compiled, 11 articles, all internal links resolve).

## Corrections applied during verify (Rule 12 — fail loud)

- **MCP Builder reversal (the big one):** the crashed `mcp-builder` research agent left the verifier guessing, and a draft wrongly declared MCP-Builder "FALSE/fabricated." I re-verified via GitHub API: **`mcp-builder` IS a real official Anthropic skill** (in `anthropics/skills`, alongside `skill-creator`/`pdf`/`pptx`/`frontend-design`/`claude-api`). Rewrote `original-mcp-builder-and-mcp.md` + fixed 5 other files. Ben's #8 claim holds.
- **"91,000 skills"** (Ben) → skills.sh now reports **788,224** — metric drift, not a contradiction. (Confirmed skills.sh = Vercel; its #1 skill *is* "find-skills" @2.1M installs, #2 "frontend-design" — corroborates Ben's #5/#6.)
- **Snyk "ToxicSkills" audit VERIFIED** (Feb 5 2026: 3,984 skills, 36.82% flawed, 13.4% critical) — kept in the security section.
- **"Cowork unverified"** flag removed — Cowork is real (vault has [[claude-cowork/_index]] + [[cowork-third-party-inference/_index]]); the agent just couldn't reach the URL.
- **Stripped fabrications:** a fake `globalFolderInstructions` settings key, an invented `vercel-labs/agent-browser` repo, a `$97/mo` price.
- **Pattern-Library jargon + broken links** ([[Pattern #18]], [[pattern/..]], [[hireui]], [[PATTERN_LIBRARY.md]], [[cc-sdd]]) neutralized — out of scope for this fast-cadence wiki; bare-topic links normalized to `/_index`.
- **Scope violation fixed:** the pilot/critic agents wrote the pilot file to **repo-root `/output/`** — moved to `03 Projects/autopilot-research/output/` and removed the stray dir.

## Artifacts

- `raw/(C) 2026-06-20-ben-ai-8-claude-skills.md` (transcript + extraction)
- `wiki/claude-skills/` — 11 files: `_index`, `overview`, `the-eight-meta-skills`, `original-anthropic-agent-skills`, `original-matt-pocock-grill-me`, `original-wikipedia-signs-of-ai-writing`, `original-skills-sh-marketplace`, `original-mcp-builder-and-mcp`, `original-prompt-engineering-best-practices`, `video-to-original-crosswalk`, `source-provenance`
- `output/(C) 2026-06-20-claude-skills-pilot-methods.md` — 22 ranked methods + skip-list + critic reframe
- `_master-index.md` + `_inventory.md` updated

## Stop reason

`gaps_closed_ratio` (1.0) ≥ target; single cold-start cycle; no backlog for this topic.

## Suggested next action

Pilot **C1 (Humanizer as the `(C)`-file gate)** + **B2 (Fact Checker in `bin/autopilot-drain.py`)** this week — both low-effort, high-discipline, and they compose with the existing prompt-evaluation harness. Then formalize skill #1 (Process Interviewer) by extending the brain-setup-pattern-v2 grill-me lineage into a reusable skill-authoring skill.
