# (C) Autopilot Loop — 2026-07-05-18

> **Trigger:** manual operator session ("build knowledge from this video + double deep dive into the original resource + pilot methods")
> **Topic:** miai-cv-matching-agent (NEW topic)
> **Source:** https://www.youtube.com/watch?v=7gIwR5SwM_0 (Mì AI, 2026-07-04) + repo thangnch/MiAI_CV_Matching_AI_Agent
> **Started:** 2026-07-05 ~17:35 local
> **Ended:** 2026-07-05 ~18:4x local
> **Path:** 5 (yt-dlp VN auto-subs) + GitHub raw fetch + Workflow dive/verify

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 raw bundle (video transcript + 8 repo files) | 1 (cold-start: topic itself) | 0 | 1.0 |

- `gaps_closed_ratio` = **1.0** (cold-start topic fully compiled in one cycle)
- Stop reason: target ratio reached; single-topic operator burst complete

## Sources ingested

- `raw/2026-07-05-miai-cv-matching-agent.md` (~84KB: deduped ~35.4K-char VN transcript **read in full** + all 8 repo files **read in full** + metadata)
- Live originals fetched during dive/verify: LangChain 1.0 docs, OpenAI PDF/pricing docs, google.com/robots.txt + Google Careers page probe, vietnamworks/topcv/itviec probes, GitHub API (thangnch), miai.vn + nguyenchienthang.vn, law-firm sources for AEDT/EU-AI-Act/IL/CO/VN-PDPL, platform.claude.com embeddings page, claude-api skill reference

## Workflow

- **`wf_dd724957-cac`**: 9 dive agents + 8 refute-first verifiers = 17 agents, ~965K tokens, 255 tool calls
- **1 agent death**: dive `claude-stack` ("Prompt is too long" after loading the claude-api skill) → **main-loop takeover** closed the gap with first-party sources
- Verify outcomes: 1 video claim REFUTED (Google Careers crawling), 2 dive arithmetic corrections, 4 doc-precision PARTIALs, unverified effort-numbers stripped, 1 stale-verifier correction, garble-guard saves ×2 (EU deadline extension, Colorado replacement — both fresh-true claims that survived because they were searched)

## Wiki articles created

- `wiki/miai-cv-matching-agent/` — `_index.md` + 12 articles (overview, architecture-and-pipeline, langchain-v1-agent-stack, defensive-output-schema, crawl-reality-and-robots, matching-quality-vs-production, cost-economics, claude-stack-port, recruitment-ai-regulatory-context, code-audit, caveats-and-corrections, source-provenance)
- `wiki/_master-index.md` — UPDATED (new topic entry, newest-first)
- `raw/_inventory.md` — UPDATED (+1 row, status compiled)

## Pilot deliverable

- `output/(C) 2026-07-05-miai-cv-matching-agent-pilot-methods.md` — 22-method application menu; headline = hireui's first LLM feature (match-explanation service, Claude-stack, no-vector-DB v1, eval-first, AEDT-aware)

## Constitutional check

- Writes confined to `03 Projects/autopilot-research/` ✅ (scope clamp)
- Loop log written ✅ · metric Δ reported ✅ · no fabricated sources ✅ (agent death disclosed + gap closed from primary sources) · librarian discipline ✅ (master index + topic index + [[links]]) · no recursion ✅ · inventory row ✅

## Suggested next action

Pick a pilot from the menu — recommended: **A1+A2 (spec hireui's match-explanation feature on the Claude stack behind the Mosh A2 vendor seam) + B1 (recruiter-labeled eval set via the existing `evals/` harness)**. Also consider watching the Mì AI channel as a recurring VN first-party source (its LangGraph video 9Mv7jQxGyEY is a natural follow-up ingest).
