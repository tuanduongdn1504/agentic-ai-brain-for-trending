# (C) Autopilot Loop — 2026-06-29-14

> **Trigger:** manual (operator-submitted video + "double deep-dive into the original resource + show me many methods to apply to my working flow")
> **Topic:** how-we-claude-code (Anthropic "How we Claude Code" workshop — agent-native spec + verification)
> **Started:** 2026-06-29T14:30+07:00 (approx)
> **Ended:** 2026-06-29T15:25+07:00 (approx)
> **Duration:** ~55m
> **Path:** 5 (yt-dlp) + direct primary-source `gh api`/WebFetch + adversarial Workflow

## What the operator asked

1. Build knowledge from the video. 2. **Double deep-dive into the original resource.** 3. **Pilot — show many methods to apply to my working flow.**

## What the video actually was

A **Vietnamese dub** ([ATsbgIRA0Fw](https://www.youtube.com/watch?v=ATsbgIRA0Fw), BizMate AI) of Anthropic's **"How we Claude Code"** workshop ([IlqJqcl8ONE](https://www.youtube.com/watch?v=IlqJqcl8ONE), Arno / Applied AI, 2026-05-23). The dub links the original directly; the **English original is the authoritative source** (full transcript pulled + read). The originals the workshop is built on: **Thariq Shihipar's** HTML blog + `ThariqS/html-effectiveness` repo + the **`anthropics/cwc-workshops`** repo (phase-3 verification engine) + Sutton's *Bitter Lesson*.

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 raw (2 videos: dub + original) + 5 originals deep-dived | 1 (cold start — topic itself) | 0 | 1.0 |

`gaps_closed_ratio` = **1.0** (cold-start: first cycle created the entire topic + provenance + pilot menu).

## Sources ingested

- `raw/2026-06-29-how-we-claude-code-anthropic-workshop.md` — full English transcript (verbatim, json3-parsed) + VN description + originals map + repo tree.
- Primary sources deep-dived (not stored as raw, fetched live): claude.com blog · `gh api` on `anthropics/cwc-workshops/how-we-claude-code/**` (every `phase-3-verify/src/verify/*` file) · `ThariqS/html-effectiveness` + companion site · official Claude Code docs · Sutton *Bitter Lesson* (training-grounded; cert blocked direct fetch).

## Verification

- **Workflow `wf_109aca29-27c`** — 16 agents (6 deep-dive extractors + 9 adversarial verifiers + 1 synthesis). 717K subagent tokens, 320 tool calls, ~8 min. 1 verifier (c9, the Opus 4.7→4.8 claim) failed ("prompt too long") — fact already known from operator env.
- **⚠️ Rule-7 override logged:** 4 of 9 verifiers (c1, c3, c4, c5) misfired — they grepped the *local filesystem* (`/Users/Cvtot/...`) instead of the GitHub repo and falsely "refuted"/"uncertain"-ed the framework's existence, the Todo-app fact, and the recorder. Overridden by the primary-source extracts (`gh api`/WebFetch) + the operator's own repo-tree read. Documented in `wiki/how-we-claude-code/source-provenance.md`.

## Wiki articles created (10 files — NEW topic)

- `wiki/how-we-claude-code/_index.md` (NEW)
- `wiki/how-we-claude-code/overview.md` (NEW)
- `wiki/how-we-claude-code/pillar-1-interview-and-bitter-lesson.md` (NEW)
- `wiki/how-we-claude-code/pillar-2-html-specs-over-markdown.md` (NEW)
- `wiki/how-we-claude-code/pillar-3-agent-native-verification.md` (NEW)
- `wiki/how-we-claude-code/verification-framework-deep-dive.md` (NEW — the centerpiece double-deep-dive)
- `wiki/how-we-claude-code/the-originals-thariq-and-repos.md` (NEW)
- `wiki/how-we-claude-code/claude-code-primitives.md` (NEW)
- `wiki/how-we-claude-code/caveats-and-when-not-to-use-html.md` (NEW — critic layer)
- `wiki/how-we-claude-code/source-provenance.md` (NEW)
- `wiki/_master-index.md` (UPDATED — added topic #30)
- `raw/_inventory.md` (UPDATED — new row, status compiled)

## Pilot deliverable

- `output/(C) 2026-06-29-how-we-claude-code-pilot-methods.md` — **18 ranked methods** across hireui-Goal-#2 / autopilot+Storm-Bear-vaults / personal-Claude-Code / Scrum-coaching + skip-list + critic reframe. **Headline:** the phase-3 verify framework is a *deployable artifact* → copy into hireui = the cleanest "actual pilot deployment" Goal-#2 evidence (attacks the "8 pilots / 0 deployed" bottleneck); all three pillars land on the in-flight Candidate Detail refactor; composes with the #1 cc-sdd pilot.

## Final metric

- `gaps_closed_ratio` = **1.0**
- Stop reason: cold-start topic fully compiled in 1 cycle + pilot menu delivered (operator ask satisfied).

## Top-3 unclosed gaps

1. **Thariq's blog text not re-fetched by the verifier** (c1 "uncertain" was a tooling miss); the extract agent fetched it, but a future audit could re-confirm the exact title/URL directly.
2. **`window.__verify_replay` route component** not in the fetched file set (used by `record.ts`) — fetch `phase-3-verify/src/verify/harness/ReplayPage.tsx` if the recorder needs full documentation for a hireui port.
3. **No empirical token/engagement numbers** (HTML vs Markdown) from the workshop — would be closed by the hireui A4/A2 pilots actually measuring it.

## Suggested next action

Create an `agent-*` branch in hireui, copy `cwc-workshops/how-we-claude-code/phase-3-verify/src/verify/` into `apps/web/src/verify/`, and stand up pilot method **A4** on `CandidateStats` (3 fixtures + 2 invariants + 1 probe) — target: probe-fails-others-pass on `bun run verify`. Offer stands to draft the `CandidateStats.verify.ts` spec against the real component. **Not committed to git yet** — awaiting operator review (consistent with prior uncommitted loop-logs).
