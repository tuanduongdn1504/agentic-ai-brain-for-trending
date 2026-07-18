# (C) Autopilot Loop — 2026-07-18-14

> **Trigger:** /loop (manual, operator-submitted URL → full topic bundle)
> **Topic:** vercel-eve — **NEW topic** (collision check clean: `m8VC2SV2igM` never ingested; no prior vercel/production-agent topic)
> **Anchor:** https://www.youtube.com/watch?v=m8VC2SV2igM (Cole Medin) — force-included
> **Scope elected by operator:** Full topic bundle (yt-search 5-8 videos)
> **Started:** 2026-07-18 ~14:0x ICT
> **Ended:** 2026-07-18 ~14:5x ICT
> **Duration:** ~50 min main-loop (incl. one ~5.5-min background verification workflow)

## Pre-flight

- Coast clear: no active /loop, cron, scheduled task, or TaskList entries. Queue pending section empty.
- Branch `autopilot-research` (holds 2 unmerged prior topics: copywriting `14071d0`, kimi-k3 N=3 `5525f6e`). This ship stacks on top; operator merges.
- Env verified: yt-dlp 2026.06.09 ✅; NotebookLM auth valid (17 cookies) — not needed (bundle small).

## Source selection

- `yt-dlp "ytsearch20:Vercel Eve agent framework"` → 20 candidates. Scored relevance/credibility/recency/diversity; selected **7** with anchor force-included. Dropped: sub-100-view micro-channels, a 1h43m redundant "full course", 2 non-EN duplicates.

## Sources ingested (7 YouTube + primary grounding)

- `raw/2026-07-18-vercel-eve/` — 7 transcripts (t1 Cole Medin anchor · t2 Syntax · t3 Sonny Sangha · t4 Elie Steinbock · t5 Rob Shocks · t6 Infisical · t7 openclaw) + `_sources.md`. ~29.1K words. `en` captions → `bin/vtt-to-md.py`, read in full.
- Primary grounding: Vercel blog `introducing-eve`, `github.com/vercel/eve` README (Apache-2.0), changelog.

## Analysis workflow

- **`wf_e215817b-a5d`** (`vercel-eve-verify`) — 5 phases, **40 agents, 0 errors / 0 empty / 0 skipped**, ~1.58M tokens, 52 tool calls, ~5.5 min: 7 digests → consolidate (30 claims) → refute-first verify (30) → synthesize → **independent completeness critic** (returned NEEDS-REVISION; mandated caveats folded into the wiki).
- Main-loop Opus anchors (independent of workflow): verified license (Apache-2.0), launch (2026-06-17 Ship London), status (public preview/beta), the 10 primitives, the durable-WDK/HITL/evals/credential-brokering mechanics, and the corrected deployment stat — against Vercel's blog + README + changelog + corroborating search.

## Verification result

- **30 load-bearing claims: 14 CONFIRMED · 10 CORRECT-BUT-INCOMPLETE · 4 UNVERIFIABLE · 1 FALSE · 1 MISLEADING · 0 fabricated.**
- **FALSE:** openclaw's "<3%→29% in 6 months" → Vercel says "a year ago" (≈1 yr).
- **MISLEADING:** Rob Shocks' "completely open / manual security" → creds-brokering + sandboxing are framework-managed by default.
- **UNVERIFIABLE (do-not-quote):** $3/10K "Vercel Connect" pricing · `eve build`→Nitro self-host · sandbox fallback order · "scales to millions."
- **Bias handled:** anchor (Cole Medin) disclosed a Vercel collaboration → treated as Vercel-adjacent; cross-checked vs Syntax (independent) + primary docs. Errors originated from promotional/small-channel sources, not the skeptical one — healthy cross-source spread.

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 7 | 1 (new topic) | 0 (10-file topic; scorecard + caveats close the fact-check gap) | ~1.0 |

## Wiki files created/updated (12)

- **New (10):** `wiki/vercel-eve/` — `_index` · `what-is-eve-directory-is-an-agent` · `primitives-and-file-structure` · `production-features` · `deployment-and-claude-code-plugin` · `vendor-lock-in-and-competitive-landscape` · `claims-scorecard` · `caveats-and-corrections` · `sources-and-stances` · `hireui-translation`.
- **Librarian (2):** `wiki/_master-index.md` (vercel-eve registered, newest-at-top) · `raw/_inventory.md` (row raw→compiled).
- **Provenance:** `raw/2026-07-18-vercel-eve/` (7 transcripts + `_sources.md`).

## Final metric

- `gaps_closed_ratio` = **~1.0** (new-topic gap closed with a full verified 10-file topic).
- **Stop reason:** single-cycle bundle complete (Phase 6 cond. 1 target-ratio + cond. 5 no unprocessed sources).

## Suggested next action

- **Operator reviews + merges `autopilot-research` → `main`** when ready (not auto-merged, per standing rule). Branch now carries 3 unmerged topics: copywriting `14071d0`, kimi-k3 N=3 `5525f6e`, and this vercel-eve ship.
- **Highest-value deepenings:** (1) **Vercel "Passport" + shadow-AI governance** (adjacent, compliance-relevant, gap flagged); (2) **Mastra head-to-head** (vendor-neutral rival). Re-visit at Eve **GA** for data-residency/audit/pricing/self-host.
- **hireui:** no candidate-facing adoption (data-residency blocker + beta + no audit). BORROW now: credential-brokering, evals-as-deploy-gate, `needsApproval` HITL, filesystem legibility into the Mosh A2 seam + agent-nativity spec. See `wiki/vercel-eve/hireui-translation.md`.
