# (C) Autopilot Loop — 2026-07-21-13

> **Trigger:** `/loop autopilot research` (manual, session-bound) — operator-submitted anchor
> **Topic:** api-types (API architecture styles / types taxonomy)
> **Anchor:** `RsgyCswZBGA` — LetDiv "7 Loại API Bạn Phải Biết" (VN)
> **Started:** 2026-07-21 ~13:36 +07
> **Ended:** 2026-07-21 ~13:58 +07
> **Duration:** ~22 min wall-clock (ingest ~3 min + verify/draft workflow ~5 min + main-loop finalize)

## Phase trace

- **Phase 0 (preflight):** scope OK; yt-dlp OK; notebooklm-py 0.3.4 (venv) OK; NotebookLM auth OK (17 cookies, SID present). Collision-checked: no existing API-taxonomy topic (`api-security-7-techniques` = OWASP, `claude-api-cost-optimization` = pricing are different). Cold-start new topic.
- **Phase 1 (wiki state):** 70 topics pre-run. `gaps_at_start = 1` (the topic itself, cold start).
- **Phase 2 (ingest):** queued in `topics-queue.md` with anchor → `bin/autopilot-drain.py --max 1`. Dry-run first (selection preview, no NotebookLM spend). Real drain: anchor force-include validated **PASS (1/1, 100%)** → 6/6 sources added + ready → NotebookLM bundle `ed17cc3d-952c-4fe0-9572-27a418d0f390` → 1 summary + 4 asks → `raw/2026-07-21-api-types-explained-rest-soap-graphql-grpc-websock.md` (18KB). Queue entry moved to Completed.
- **Phase 3–4 (compile + verify + cross-link):** Workflow `wf_640f115f-0a8` — **25 agents** (11 refute-first WebSearch claim-verifiers + 1 corpus-collision grep + 12 article drafters + 1 completeness critic). **0 errors / 0 empty / 0 skipped.** ~1.28M tokens, 158 tool calls, ~5.2 min (all Haiku 4.5). Main loop (Opus): QA'd article prose (spot-read overview + grpc-and-rpc), deterministically fixed 4 files' link defects (moshi- typo, external-mislabels on local topics, escaped `\|`), authored the 4 synthesis files, **filesystem-validated all 157 wiki-links** (0 unresolved).
- **Phase 5 (audit):** 16 files, no stubs, all links resolve, critique found **0 unverified claims**. `gaps_at_end = 0`. (Critique's "missing articles" — HATEOAS, AsyncAPI, gRPC-Web — are advanced/optional follow-ups, logged in [[../wiki/api-types/beyond-the-video]], not stub-gaps.)
- **Phase 6 (decide):** stop — target ratio reached + topic complete.
- **Phase 7 (log + inventory):** `_master-index.md` updated (topic #71, newest-first); `_inventory.md` row appended (Status: compiled); this log written.

## Metric

- `gaps_at_start = 1`, `gaps_at_end = 0`
- **`gaps_closed_ratio = 1.0`** (cold-start topic fully created) — stop reason: target reached.

## Scorecard (verification)

**12 verdicts: 5 CONFIRMED / 7 CORRECT-BUT-INCOMPLETE / 0 MISLEADING / 0 FALSE / 0 UNVERIFIABLE.** Technically-honest beginner-explainer profile. Headline caveats: gRPC "7–10× faster" is payload/throughput-specific; "SOAP for banking" is legacy-incumbent not preferred-for-new; GraphQL caching "different not harder"; tRPC TypeScript-only. Corpus-collision: CONFIRMED no collision (genuinely new).

## Sources ingested

- `raw/2026-07-21-api-types-explained-rest-soap-graphql-grpc-websock.md` (6 videos: LetDiv VN anchor + Codist + Learn with Whiteboard + Ulbi TV RU + Be A Better Dev + ByteByteGo; NotebookLM `ed17cc3d…`)

## Wiki articles created (16, all NEW)

`wiki/api-types/`: _index · overview · selection-framework · http-semantics-and-rest-conventions · rest-and-web-api · soap · graphql · grpc-and-rpc · websocket-and-realtime · webhook · beyond-the-video · critical-appraisal · hireui-relevance · claims-scorecard · caveats-and-corrections · source-provenance

## Top unclosed gaps (optional follow-ups, not stubs)

1. Advanced REST (HATEOAS / hypermedia) + async-event APIs (AsyncAPI) — deferred as low-impact for v1.
2. hireui: cost-per-API-choice + observability/compliance-logging strategy — Phase-2 concerns, not decision-blockers (noted in [[../wiki/api-types/hireui-relevance]]).
3. gRPC-Web bridge (browser connectivity) — mentioned, not deep.

## Suggested next action

Topic is complete on branch `autopilot-research` (uncommitted). Review `wiki/api-types/_index.md`; if good, commit on this branch (don't merge to main — you merge). Optional deepen: if you want production depth, queue a follow-up anchored on an API-security/gateway talk to expand [[../wiki/api-types/beyond-the-video]].
