# (C) Autopilot Loop — 2026-06-29-13

> **Trigger:** interactive `/loop`-style request ("build knowledge from this video + double deep-dive into the original resource + show me many methods for my apply")
> **Topic:** ai-engineering (Chip Huyen's *AI Engineering* book, via Anas Riad's 41-min summary video)
> **Started:** 2026-06-29T13:30+07:00 (approx)
> **Ended:** 2026-06-29T13:50+07:00 (approx)
> **Duration:** ~80m (incl. ~5m background verification workflow)

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 video + book primary-sources | 1 (topic = gap) | 0 | 1.0 |

`gaps_closed_ratio = 1.0` (cold-start NEW topic; all 12 files created + indexed + cross-linked; no stub/TODO markers left; no uncompiled cited source).

## Source identification

- **Video (entry point):** `geQqpO_AFMo` — Anas Riad, "AI Engineering in 41 Minutes: From Demo to Production" (2026-06-17, 41:54, 17,381 views). Full English auto-subs pulled via yt-dlp, deduped to ~7,400 words, **read in full**.
- **Original resource (the deep-dive target):** Chip Huyen, *AI Engineering: Building Applications with Foundation Models* (O'Reilly, Dec 2024, 534pp, 10 chapters). The video is a faithful chapter-walkthrough; the book is the load-bearing original.

## Sources ingested

- `raw/2026-06-29-ai-engineering-chip-huyen.md` (yt-dlp transcript + video description + metadata header; 45K)
- Primary sources fetched directly (no NotebookLM): `github.com/chiphuyen/aie-book` `chapter-summaries.md` + `ToC.md`, `oreilly.com` product page, `huyenchip.com/books/`.

## Verification (adversarial)

- **Workflow `wf_508f1c32-b7b`** — 15 agents: 5 deep-dive finders (book TOC/metadata · author · GitHub repo · related-video+creator · skipped-chapter theses) + **9 independent skeptics** (each re-verifying one load-bearing fact from scratch) + 1 completeness critic. 520K subagent tokens, 174 tool calls, ~5 min. One skeptic (Claypot/NVIDIA bio) failed StructuredOutput; fact independently CONFIRMED by the author-identity finder → no gap.
- **Plus** a direct primary-source fetch of Huyen's chapter summaries to ground the chapters the video skipped (closed the only finder flag).

### Corrections logged (Rule 12 fail-loud) → `wiki/ai-engineering/source-provenance.md`

1. ❌ REFUTED: `huyenchip.com/ai-engineering` 404s — companion is the GitHub repo `chiphuyen/aie-book` + `huyenchip.com/books/`.
2. ⚠️ Anas Riad = credible third-party summarizer (Cardiff data-scientist, ~7.5K subs), **NOT Chip Huyen / not official O'Reilly** (verdict PARTIAL).
3. ⚠️ "Most-read book on O'Reilly" = author-reported, not independently confirmed.
4. ⚠️ Related video `18sMYvzqhTU` = Anas Riad's summary of Huyen's *first* book (*Designing ML Systems*) — the two pair up.
5. ⚠️ Skipped-chapter (Ch.7–10) theses initially from third-party blogs → re-grounded in Huyen's own `chapter-summaries.md`.

### Verified CONFIRMED (high confidence)

- Book metadata (title/publisher/dates/pages/ISBN), the **exact 10-chapter TOC**, author bio (NVIDIA/Snorkel/Netflix/Claypot→Voltron 2024, Stanford CS329S, prior book *Designing ML Systems* 2022), repo `chiphuyen/aie-book` (16.3K★).

## Wiki articles created (12 files — NEW topic `ai-engineering`)

- `wiki/ai-engineering/_index.md` (NEW)
- `wiki/ai-engineering/overview.md` (NEW)
- `wiki/ai-engineering/foundation-models.md` (NEW — Ch.1–2)
- `wiki/ai-engineering/evaluation.md` (NEW — Ch.3–4)
- `wiki/ai-engineering/prompt-engineering-and-guardrails.md` (NEW — Ch.5)
- `wiki/ai-engineering/rag.md` (NEW — Ch.6 part 1)
- `wiki/ai-engineering/agents-and-memory.md` (NEW — Ch.6 part 2)
- `wiki/ai-engineering/finetuning-dataset-inference.md` (NEW — Ch.7–9, the skipped chapters)
- `wiki/ai-engineering/production-architecture-and-feedback.md` (NEW — Ch.10)
- `wiki/ai-engineering/book-author-and-video.md` (NEW — the originals + identities)
- `wiki/ai-engineering/source-provenance.md` (NEW — verification ledger)
- `wiki/_master-index.md` (UPDATED — added `## ai-engineering` topic entry)
- `raw/_inventory.md` (UPDATED — +1 row at top + coverage bullet)

## Deliverable (the operator's "many methods for my apply" ask)

- `output/(C) 2026-06-29-ai-engineering-pilot-methods.md` — **21 ranked methods** across 4 flows (A hireui-Goal-#2 / B autopilot+Storm-Bear-vaults / C personal-Claude-Code+prompt-eval / D Scrum-coaching) + a 3-step Start-Here sequence + skip-list + critic's reframe.

## Final metric

- `gaps_closed_ratio` = **1.0** (cold-start NEW topic fully compiled + indexed + cross-linked)
- Stop reason: single-cycle cold-start complete; target_ratio (0.5) exceeded.

## Top unclosed gaps / follow-ups

1. **Promotion candidacy:** this is a foundational, cross-cutting topic with 12 files and N=1 authoritative source (the canonical book). Consider for `output/promotion-candidates.md` at next audit — it's the conceptual parent of prompt-evaluation, claude-api-cost-optimization, cowork-third-party-inference, and multi-agent-orchestration.
2. **Deeper Ch.3/4/10 fetch:** the wiki uses Huyen's chapter *summaries*; a future pass could fetch fuller excerpts (e.g. the eval-pipeline 3-step detail, the AI-as-judge limitations subsection) if the operator wants Ch.3/4/10 at full depth for the hireui build.
3. **Inventory reconciliation:** the pre-existing coverage-summary counters ("41 rows / 38 compiled") were already internally inconsistent before this run (flagged 2026-06-04); not reconciled here (out of scope) — a dedicated reconciliation pass is still pending.

## Suggested next action

**This week (Goal #2):** start the headline pilot from the methods file — pick the smallest real hireui AI feature and **write its eval FIRST** (Ch.4 success criteria + 10–30 graded real examples into `evals/`), *before* any prompt. That is the single move that converts "N pilots / 0 deployed" into measured Goal #2 evidence. Parallel low-effort win: read Ch.3, 4, 10 from the free repo `chapter-summaries.md` to close the production-half gaps the video skipped.

**Optional:** `git add "03 Projects/autopilot-research/" && git commit` on the `autopilot-research` branch (consistent with every prior topic ship; not auto-merged to main) — awaiting operator confirmation.
