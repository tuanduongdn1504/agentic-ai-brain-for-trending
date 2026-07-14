# (C) Autopilot Loop — 2026-07-14-01

> **Trigger:** interactive `/loop` request (operator: "Can I start build knowledge from other video with loop?" → single-URL follow-up `PY7xIxybYNc`)
> **Topic:** pydantic-ai-2 (NEW topic)
> **Started:** 2026-07-14T00:40:00+07:00
> **Ended:** 2026-07-14T01:20:00+07:00
> **Duration:** ~40m

## Pre-flight: duplicate + scope check

- Video ID `PY7xIxybYNc` not found anywhere in `wiki/_master-index.md` or `raw/_inventory.md` — not a duplicate.
- No existing "pydantic-ai" or "capability" wiki topic (`grep -il "pydantic" wiki/`). Presenter Cole Medin **is** already in-corpus twice (`harness-engineering/archon-harness-builder-anchor.md`, `harness-engineering/_index.md` authoritative anchor) — scoped as a **NEW topic** (framework release, not a deepening of harness-engineering) rather than folding into that topic, since the subject matter (an AI *agent framework's* API design) is distinct from harness-engineering's agentic-coding-workflow focus.

## Source

- Video `PY7xIxybYNc` — Cole Medin (@ColeMedin, 216K subs), *"Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities"* (2026-07-10, 15:00, ~19,575 views at ingest).
- Path 5 (yt-dlp-only). EN auto-captions → `grep`/`sed`/`awk` dedupe (the project's `python3 -c` inline-script fallback — see Tooling note below) → ~2.6K-word transcript, **read in full in the main loop**. No NotebookLM.
- Description links pulled from `yt-dlp --write-info-json` (ground truth, not garbled captions): sponsor `nimbalyst.com`, `dynamous.ai/ai-native-engineering-org`, demo repo `github.com/coleam00/orbit-support-agent`, launch article `pydantic.dev/articles/pydantic-ai-v2`, official repo `github.com/pydantic/pydantic-ai`.

## Tooling note

`python3 -c "..."` and `python3 script.py` were both denied/killed (exit 137) under this session's permission settings when run against files in `/tmp`. Switched to the vault's own scratchpad directory and, when that still failed for `python3`, fell back to the project's established `grep`/`sed`/`awk` VTT-cleaning pattern (already an allow-listed pattern in `.claude/settings.local.json` from a prior session) — worked cleanly. Recorded here in case a future loop hits the same `python3` denial.

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 (video) + 7-dive/10-verify/1-critic Workflow + 1 main-loop follow-up fetch | 1 (topic itself, cold-start) | 0 | 1.0 |

`gaps_closed_ratio` = **1.0** — cold-start topic, fully compiled to 10 wiki files in one cycle.

## Verification workflow

- **Workflow `wf_01eb5573-0b3`** — 18 agents (7 first-party dives + 10 refute-first verifiers + 1 completeness critic). ~737K subagent tokens, 171 tool calls, ~5 min wall-clock. **0 errors, 0 empty results.**
- **Contradiction caught by the critic, resolved by main-loop follow-up (Rule 12 — fail loud):** one dive found Monty's own README still says "will (soon) be used to implement codemode," while a verifier found a separate package (`pydantic-ai-harness`) marketing Code Mode + Monty as already shipped. The critic flagged this tension unprompted rather than letting both stand silently. Main-loop WebFetch of `pydantic.dev/docs/ai/harness/code-mode/` + `github.com/pydantic/pydantic-ai-harness` resolved it: Code Mode/Monty ships in `pydantic-ai-harness` v0.6.0 (released 2026-07-09, one day before the video), separately from core `pydantic-ai` — Monty's README is simply stale. Full writeup: [wiki/pydantic-ai-2/lean-core-vs-harness-and-monty.md](../wiki/pydantic-ai-2/lean-core-vs-harness-and-monty.md).
- **One critic self-inconsistency noted, not corrected silently:** the critic's own claim tally mislabeled the OVERSIMPLIFIED claim's index and dropped one CORRECT_BUT_INCOMPLETE claim from its count (9 vs the actual 10). The underlying verify ledger itself was complete and correct (10/10 logged) — only the critic's own summary arithmetic slipped. Recorded in [wiki/pydantic-ai-2/claims-scorecard.md](../wiki/pydantic-ai-2/claims-scorecard.md) rather than silently fixed, per fail-loud discipline.
- **One concern the critic raised turned out to be unfounded:** whether Cole himself made the "just like skills in Claude Code, Codex, GitHub Copilot" comparison, or a verifier added it from external sources. Confirmed from the full transcript (read directly in the main loop, independent of the workflow) that Cole says this on-screen — not a verifier addition.

## Scorecard (10 claims)

**2 CONFIRMED / 6 CORRECT-BUT-INCOMPLETE / 1 MISLEADING / 1 OVERSIMPLIFIED / 0 FALSE / 0 FABRICATED.** Full table: [wiki/pydantic-ai-2/claims-scorecard.md](../wiki/pydantic-ai-2/claims-scorecard.md).

## Sources ingested

- raw/2026-07-14-pydantic-ai-2.md (header + full transcript)

## Wiki articles created/updated

- wiki/pydantic-ai-2/_index.md (NEW)
- wiki/pydantic-ai-2/overview.md (NEW)
- wiki/pydantic-ai-2/capability-primitive-and-mcp-framing.md (NEW)
- wiki/pydantic-ai-2/progressive-disclosure-and-skills-lineage.md (NEW)
- wiki/pydantic-ai-2/lean-core-vs-harness-and-monty.md (NEW)
- wiki/pydantic-ai-2/v1-to-v2-composability-claim.md (NEW)
- wiki/pydantic-ai-2/langchain-crewai-comparison.md (NEW)
- wiki/pydantic-ai-2/nimbalyst-sponsor-fact-check.md (NEW)
- wiki/pydantic-ai-2/claims-scorecard.md (NEW)
- wiki/pydantic-ai-2/source-provenance.md (NEW)
- wiki/_master-index.md (UPDATED — new topic entry, inserted at top per newest-first convention)
- wiki/harness-engineering/archon-harness-builder-anchor.md (UPDATED — noted Cole Medin's 3rd corpus appearance)
- wiki/github-copilot-cli-agents/agent-skills-shared-standard.md (UPDATED — added the 3-way Skills-spec-vs-independent-convergence comparison)
- raw/_inventory.md (UPDATED — new row, Status: compiled; coverage-summary footer left untouched per established 2026-07-13 precedent — already stale since ~2026-05-23, selective bump would worsen accuracy)

## Pilot angle

Deliverable: `output/(C) 2026-07-14-pydantic-ai-2-pilot-note.md`. Headline: the **capability** pattern (bundle instructions + tools + hooks + settings into one reusable, progressively-disclosed unit) is a useful *conceptual* pattern for structuring hireui's planned Match-Explain LLM feature — not a code-level adoption candidate, since Pydantic AI is Python-only and hireui is TypeScript.

## Suggested next action

Per the vault's standing pilot-deployment backlog (root CLAUDE.md: 8+ ranked pilots accumulated, 0 deployed), the next highest-leverage move remains **deploying an already-ranked pilot** rather than accumulating further research passes. This topic adds a design-pattern reference rather than a new pilot candidate — treat it as input to whichever LLM-feature pilot gets built, not a queue addition of its own.
