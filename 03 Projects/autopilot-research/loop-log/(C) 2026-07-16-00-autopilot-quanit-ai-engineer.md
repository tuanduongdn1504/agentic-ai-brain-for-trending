# (C) Autopilot Loop — 2026-07-16-00

> **Trigger:** /loop autopilot research (operator-submitted single video)
> **Topic:** quanit-becoming-ai-engineer-2026
> **Source:** https://www.youtube.com/watch?v=RcF6ofU2nLs (Quân IT, "Becoming An AI engineer in 2026")
> **Started:** 2026-07-16
> **Ended:** 2026-07-16
> **Status:** COMPLETE ✅

## Pipeline (modern path 1 — captions, no NotebookLM)

1. yt-dlp `vi-orig` auto-subs → `vtt-to-md.py` → `raw/2026-07-16-quanit-becoming-ai-engineer-2026.md` (483 cues / 41 paragraphs) — **DONE** (full VN transcript read in main loop)
2. Adversarial verification Workflow `wf_0f3ff851-bd2` (10 agents, 0 errors, 0 empty, ~396K tokens) — **DONE**
3. Compile `wiki/quanit-becoming-ai-engineer-2026/` (12 files) — **DONE**
4. Final verify vs transcript + cross-link resolution (16/17 exist; career-ops external) — **DONE**
5. Metric + inventory update + master-index + promotion check — **DONE**

## Metric

- New topic (cold-start for this subject): `gaps_at_start = 1` (the topic itself) → `gaps_at_end = 0` (12 articles, 0 stubs, 0 TODO markers, all local cross-links verified present).
- **`gaps_closed_ratio` = 1.0** — target (≥0.5) met. Single cycle; stop reason = topic fully compiled, no unprocessed raw remaining for this topic.

## Sources ingested

- `raw/2026-07-16-quanit-becoming-ai-engineer-2026.md` (yt-dlp `vi-orig`, 1 video, 25 KB)

## Wiki articles created

- `wiki/quanit-becoming-ai-engineer-2026/_index.md` (NEW)
- `.../overview.md`, `.../anti-hype-framing.md`
- `.../pillar-1-fundamentals-not-internals.md`, `.../pillar-2-the-stack-around-ai.md`, `.../pillar-3-seventy-percent-is-normal-engineering.md`, `.../pillar-4-learn-by-building.md`
- `.../claims-scorecard.md`, `.../caveats-and-corrections.md`, `.../critical-appraisal.md`, `.../hireui-pilot.md`, `.../source-provenance.md`
- `wiki/_master-index.md` (UPDATED — new topic prepended at top)
- `output/(C) 2026-07-16-quanit-becoming-ai-engineer-2026-pilot-methods.md` (NEW)
- `raw/_inventory.md` (UPDATED — Status compiled)

## Scorecard

10 checkable claims: **8 CONFIRMED / 1 MISLEADING / 0 FALSE / 0 FABRICATED / 1 UNVERIFIABLE.** High-integrity talk. MISLEADING = researcher pay "a few million/yr" (median ~$1–1.5M). UNVERIFIABLE = "Dodas" chatbot incident (phenomenon real, brand unidentifiable).

## Rule-12 fail-loud

- Stripped 2 agent-introduced errors before ship: fabricated `vNNN` version numbers (Storm Bear artifacts) + unverified "Ryan Lopopolo" authorship. Logged in `caveats-and-corrections.md`.
- `career-ops` cross-link is Storm Bear-only (not local) → marked `[[external|...]]`, not shipped as a broken local link.

## Top unclosed gaps / follow-ups

1. Talk omits deployment/observability + failure-mode-literacy — covered as caveats, not deep articles (fine for an advice topic).
2. Pillar-2 stack is 2023–24 orthodoxy — cross-referenced to agent-memory-architecture / mosh-ai-powered-apps for the 2026 update rather than re-explained.
3. hireui pilot Tier A is a zero-code, this-week action — the real next step if the operator wants to break the 0-deployed streak.

## Suggested next action

Not committed to git (per operator convention — wikis ship on a branch, operator merges). Offer: commit on `autopilot-research`. Separately, the standing promotion check — this topic pairs with `hoidanit-fullstack-vibe-coding` + `ai-engineering` as a potential VN-practitioner / AI-engineer-career cluster for Storm Bear promotion once it has 2+ audit cycles.
