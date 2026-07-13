# (C) Autopilot Loop — 2026-07-13-20

> **Trigger:** interactive `/loop` request (operator: "Can I start build knowledge from other video with loop?" → single-URL follow-up `GdvKNwMcfd0`)
> **Topic:** github-copilot-cli-agents (NEW topic)
> **Started:** 2026-07-13T20:00:00+07:00
> **Ended:** 2026-07-13T20:50:00+07:00
> **Duration:** ~50m

## Pre-flight: duplicate + scope check

- Video ID `GdvKNwMcfd0` not found anywhere in `wiki/_master-index.md` or `raw/_inventory.md` — not a duplicate.
- Scoped against existing topics with adjacent framing (`system-thinking-ai-coding`, `harness-engineering`, `multi-agent-orchestration`, `claude-code-skills-stack`, `jsm-six-file-context`, `google-antigravity-skills`) — all thematically nearby (agentic-scaling guardrails, AGENTS.md/skills conventions) but none GitHub-Copilot-CLI-specific. Decision: **NEW topic**, not a deepening pass — this is the corpus' first GitHub-Copilot-CLI-native subject.

## Source

- Video `GdvKNwMcfd0` — AI Engineer (`@aiDotEngineer`, the ai.engineer conference's official channel) — Chris Noring (Microsoft Cloud Developer Advocate), *"From Writing Code to Designing Systems: How the Developer Role is Changing"* (2026-07-11, 23:05, ~8,487 views at ingest).
- Path 5 (yt-dlp-only). EN auto-captions → `sed`/`uniq` dedupe (rolling-caption redundancy + word-level karaoke `<c>` tags) → 656-line / 4,272-word transcript, **read in full in the main loop** across two reads. No NotebookLM.

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 (video) + 8-dive/8-verify/1-critic Workflow + 2 main-loop independent checks | 1 (topic itself, cold-start for this subject) | 0 | 1.0 |

`gaps_closed_ratio` = **1.0** — cold-start topic, fully compiled to 11 wiki files in one cycle.

## Verification workflow

- **Workflow `wf_a1693ef8-4dc`** — 17 agents (8 first-party dives + 8 refute-first skeptics + 1 completeness critic). ~688K tokens, 232 tool calls, ~5.3 min wall-clock. **0 errors, 0 empty results.**
- Agents ran on Haiku 4.5.
- **Confabulation caught by the critic itself, then resolved by main-loop takeover (Rule 12 — fail loud):** the coding-agent verifier claimed a "July 2026" GA date backed by a specific press-release quote; the parallel dive agent for the same feature explicitly reported it could find no such announcement anywhere in GitHub's changelog. The critic flagged this exact contradiction unprompted. Main-loop independent WebSearch + WebFetch (outside the workflow) found the real changelog entry — GA **2025-09-25** — and the suspect quote/date is excluded from the wiki entirely.
- **One claim-mapping correction made in the main loop** (not a sub-agent error): the workflow's own claim C6 attributed a "vendors including Anthropic agree to support this" framing to the AGENTS.md guardrail. Re-checking the transcript directly showed that specific line is about **Skills**, not AGENTS.md — corrected before writing the wiki (see [wiki/github-copilot-cli-agents/source-provenance.md](../wiki/github-copilot-cli-agents/source-provenance.md)).
- Two unverified specifics (GitHub issue #6235's exact reaction count; the `argument-hint` field's exact regression-issue citation) were independently spot-checked but returned inconsistent numbers across two checks — **quarantined as "plausible, not asserted as fact"** rather than stated precisely, per this project's discard-as-garble discipline.

## Scorecard (8 claims)

**6 CONFIRMED / 2 CORRECT-BUT-INCOMPLETE / 0 MISLEADING / 0 FALSE / 0 FABRICATED** — an unusually high-integrity talk once the one workflow-artifact confabulation is corrected. Full table: [wiki/github-copilot-cli-agents/claims-scorecard.md](../wiki/github-copilot-cli-agents/claims-scorecard.md).

## Sources ingested

- raw/2026-07-13-github-copilot-cli-agents.md (header + transcript summary)

## Wiki articles created/updated

- wiki/github-copilot-cli-agents/_index.md (NEW)
- wiki/github-copilot-cli-agents/overview.md (NEW)
- wiki/github-copilot-cli-agents/agents-md-guardrail.md (NEW)
- wiki/github-copilot-cli-agents/agent-skills-shared-standard.md (NEW)
- wiki/github-copilot-cli-agents/custom-agents-vs-subagents.md (NEW)
- wiki/github-copilot-cli-agents/copilot-cli-and-delegate.md (NEW)
- wiki/github-copilot-cli-agents/coding-agent-issue-to-pr.md (NEW)
- wiki/github-copilot-cli-agents/mcp-servers-in-copilot.md (NEW)
- wiki/github-copilot-cli-agents/claude-code-parity-and-gaps.md (NEW)
- wiki/github-copilot-cli-agents/claims-scorecard.md (NEW)
- wiki/github-copilot-cli-agents/caveats-and-corrections.md (NEW)
- wiki/github-copilot-cli-agents/source-provenance.md (NEW)
- wiki/_master-index.md (UPDATED — new topic entry, inserted at top per newest-first convention)
- raw/_inventory.md (UPDATED — new row, Status: compiled; coverage-summary footer left untouched per established 2026-07-13 precedent — already stale since ~2026-05-23, selective bump would worsen accuracy)

## Pilot angle

Deliverable: `output/(C) 2026-07-13-github-copilot-cli-agents-pilot-menu.md`. Headline: test whether a **Claude Code Routine with a GitHub-event trigger** can replicate the "open an issue → walk away → get a draft PR" workflow Chris demoed on Copilot — the nearest working substitute on the Claude side, since no literal "assign issue to agent" button exists yet for Claude Code.

## Top unclosed gap (follow-up)

- Whether Chris Noring's talk was a featured/scheduled AI Engineer conference session or independently-produced channel content was not fully confirmed (he doesn't appear on the conference's public "featured speakers" page) — doesn't affect the technical verification, flagged for completeness only.

## Suggested next action

Per the vault's standing pilot-deployment backlog (root CLAUDE.md: 8+ ranked pilots accumulated, 0 deployed), the next highest-leverage move remains **deploying an already-ranked pilot** rather than accumulating further research passes. If continuing research instead, the Routines-with-GitHub-triggers pilot spec'd above is a genuinely testable, low-cost next step that would also generate real evidence (not just research) toward Goal #2.
