# (C) Autopilot Loop — 2026-07-14-01 (teach-skill-ai-tutor)

> **Trigger:** interactive `/loop` request (operator: "Can I start build knowledge from other video with loop?" → single-URL follow-up `K3UXUOJ3ac0`)
> **Topic:** teach-skill-ai-tutor (NEW topic)
> **Started:** 2026-07-14T00:55:00+07:00 (approx.)
> **Ended:** 2026-07-14T01:41:00+07:00
> **Duration:** ~46m

## Pre-flight: duplicate + scope check

- Video ID `K3UXUOJ3ac0` not found anywhere in `wiki/_master-index.md` or `raw/_inventory.md` — not a duplicate.
- Existing `wiki/claude-skills/` topic covers a different set of 8 Claude meta-skills (Ben AI) — no overlap with a "teach" skill. Scoped as a **NEW topic**, with cross-links added to `claude-skills` once the Matt Pocock connection surfaced during verify.

## Source

- Video `K3UXUOJ3ac0` — Tự Học Cùng AI (VN community/self-study channel), *"Hướng dẫn cài Skill 'teach' và tạo lộ trình học theo năng lực"* (2026-06-28, 18:35).
- Path 5 (yt-dlp-only). `vi-orig` auto-captions → `sed`/`grep`/`awk` dedupe (python3 denied under this session's sandbox, consistent with the prior session's note) → ~1.6K-word transcript, **read in full in the main loop**. `--write-info-json` pulled the description (independently confirms the 6-concept/3-layer English terminology in the presenter's own words). No NotebookLM.

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 (video) + 5-dive/5-verify/1-critic Workflow + 5 main-loop follow-up fetches | 1 (topic itself, cold-start) | 0 | 1.0 |

`gaps_closed_ratio` = **1.0** — cold-start topic, fully compiled to 8 wiki files in one cycle.

## Verification workflow

- **Workflow `wf_5eb1dd9c-596`** — 11 agents (5 first-party dives + 5 refute-first verifiers, paired per-claim + 1 completeness critic). ~441K tokens, 138 tool calls, ~3.5 min wall-clock. **0 errors, 0 empty results.**
- **Main-loop follow-up (Rule 12 — fail loud):** the completeness critic flagged two concerns rather than letting the workflow's own verdicts stand unchecked: (1) whether `learn.chatgpt.com` is genuinely OpenAI's own docs domain — resolved by directly `WebFetch`ing `developers.openai.com/codex/{pricing,skills}` and observing both 308-redirect to `learn.chatgpt.com`, confirming it as OpenAI-controlled; (2) the free-tier contradiction between the workflow's own verify verdict (FALSE) and several third-party aggregator summaries surfaced during a fresh main-loop `WebSearch` (suggesting free access was real) — resolved by fetching the actual OpenAI pricing page directly, which explicitly excludes Free from Codex CLI (Go, $8/month, is the minimum). The main loop also independently `WebFetch`ed `github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md` directly (rather than trusting a Haiku dive's summary) and confirmed the near-verbatim 6-concept + 3-layer match itself — this became the headline finding.
- **No agent deaths or verifier misfires** in this run; the main-loop follow-up was precautionary verification, not error correction.

## Scorecard (5 claims)

**2 CONFIRMED / 1 CORRECT-BUT-INCOMPLETE / 0 MISLEADING / 2 FALSE / 0 FABRICATED.** Full table: [wiki/teach-skill-ai-tutor/claims-scorecard.md](../wiki/teach-skill-ai-tutor/claims-scorecard.md).

Headline: the "teach" skill is (near-certainly) Matt Pocock's public `mattpocock/skills` Agent Skill, redistributed via a private VN Facebook group with zero attribution in the video — the **third** corpus appearance of Pocock's work (after `claude-skills`'s Process Interviewer / grill-me lineage, and the vault's own Pattern-Library tracking of the repo). Separately, OpenAI Codex CLI's Skills feature is confirmed real and on the same `agentskills.io` spec as Claude Code + GitHub Copilot CLI — a third vendor on the literal spec.

## Sources ingested

- raw/2026-07-14-teach-skill-ai-tutor.md (header + description + full VN transcript)

## Wiki articles created/updated

- wiki/teach-skill-ai-tutor/_index.md (NEW)
- wiki/teach-skill-ai-tutor/overview.md (NEW)
- wiki/teach-skill-ai-tutor/codex-skills-feature-verified.md (NEW)
- wiki/teach-skill-ai-tutor/matt-pocock-provenance.md (NEW)
- wiki/teach-skill-ai-tutor/codex-free-tier-fact-check.md (NEW)
- wiki/teach-skill-ai-tutor/donella-meadows-source.md (NEW)
- wiki/teach-skill-ai-tutor/claims-scorecard.md (NEW)
- wiki/teach-skill-ai-tutor/source-provenance.md (NEW)
- wiki/_master-index.md (UPDATED — new topic entry, inserted at top per newest-first convention)
- wiki/codex/_index.md (UPDATED — added a Related-topics cross-link noting the Skills-feature gap this topic fills)
- wiki/github-copilot-cli-agents/agent-skills-shared-standard.md (UPDATED — added a third-vendor-on-the-literal-spec section for Codex CLI)
- wiki/claude-skills/_index.md (UPDATED — added a cross-link noting Matt Pocock's second corpus appearance)
- raw/_inventory.md (UPDATED — new row appended in Phase 0 as `raw`, updated to `compiled` in Phase 7)

## Pilot angle

Deliverable: `output/(C) 2026-07-14-teach-skill-ai-tutor-pilot-note.md`. Headline: the persistent-files-as-memory pattern (mission/note/resource/learning-record files instead of chat history) is a directly reusable pattern for any future hireui onboarding/tutoring feature; the Matt-Pocock-provenance finding is a reminder to check unattributed "community" skill packages against `mattpocock/skills` before treating them as novel.

## Suggested next action

Per the vault's standing pilot-deployment backlog (root CLAUDE.md: 8+ ranked pilots accumulated, 0 deployed), the next highest-leverage move remains **deploying an already-ranked pilot** rather than accumulating further research passes. This topic is a small, cleanly-scoped addition (fact-check + one recurring-provenance data point) — nothing here rises to pilot-queue priority on its own.
