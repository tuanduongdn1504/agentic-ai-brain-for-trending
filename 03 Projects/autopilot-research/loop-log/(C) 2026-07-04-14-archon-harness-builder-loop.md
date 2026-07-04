# (C) Autopilot Loop — 2026-07-04-14 — archon-harness-builder (harness-engineering DEEPEN)

> **Trigger:** operator-submitted URL (interactive session; "build knowledge from this video + double deep dive original resource + pilot methods")
> **Topic:** harness-engineering — NEW platform layer (harness builder)
> **Started:** 2026-07-04 ~13:55 · **Ended:** 2026-07-04 ~15:10 · **Duration:** ~75m main loop + ~7.5m workflow wall-clock

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 video (full transcript) + repo primary sources (README/skill/CHANGELOG/tree in full) + 16-agent dive/verify | 1 (roadmap Tier-5 #9 open, platform layer absent) | 0 closed-as-asked (4 new follow-up candidates registered) | ~1.0 on the asked gap |

## Sources ingested

- `raw/srx9iwnjK2M/` — transcript.txt (163,214 chars, read in full in main loop) + transcript-timed.txt + description.txt
- `raw/2026-07-04-archon-harness-builder.md` — consolidated ingest header (compiled)
- Main-loop primary fetches: coleam00/Archon README (19,993 chars), `.claude/skills/archon/SKILL.md` (15,867 chars), CHANGELOG head (v0.5.0/v0.4.x), full repo tree (1,453 paths), repo metadata (22,699★)
- Workflow `wf_8a0f2da5-1d0`: 16 agents (6 dives: yaml-schema / default-workflows / docs-book-security / dogfood-maintainer / pivot-history / ecosystem-positioning + 10 refute-first verifiers incl. discard-as-garble guard verbatim), ~815K tokens, 324 tool calls, 0 agent deaths

## Wiki articles created/updated

- `wiki/harness-engineering/archon-harness-builder-anchor.md` (NEW — platform-layer anchor + 17-row verification ledger + 4-entry misfire log)
- `wiki/harness-engineering/archon-workflow-primitives.md` (NEW — 7 node types, silent-failure catalog, security model)
- `wiki/harness-engineering/archon-default-workflows-and-dogfood.md` (NEW — 20 defaults, adversarial-dev = Pattern #76 3rd stratum, maintainer dark-factory-with-brakes)
- `wiki/harness-engineering/harness-economics-and-tos-timeline.md` (NEW — ToS timeline pinned 2026-07-04, rate limits, cost ladder, advisor tool)
- `wiki/harness-engineering/terminology.md` (UPDATED — Dark factory attribution: Shapiro 2026-01-23 coinage, 3 independent usages, StrongDM instance)
- `wiki/harness-engineering/research-roadmap.md` (UPDATED — Tier-5 #9 partial completion + 4 new candidates: Omnigent / dark-factory-experiment watch / Book of Archon / persist_session economics)
- `wiki/harness-engineering/_index.md` (UPDATED — 24→28 articles, platform-layer section)
- `wiki/_master-index.md` (UPDATED — harness-engineering entry extended)

## Headline findings

1. **Harness vs harness-builder** — first corpus treatment of a builder-of-harnesses platform; "first open-source harness builder" defensible-as-coined-category (no OSS competitor self-identifies as builder).
2. **Corporate evidence base fully verified:** Stripe Minions 1,300 AI-PRs/wk (human-reviewed, Goose fork) / StrongDM 32,200-line zero-review factory / Shopify Roast is OSS / Claude Code 2026-03-31 sourcemap leak (v2.1.88).
3. **Two attribution corrections:** 6.7→70 "study" = Can Bölük Hashline edit-format benchmark (task-success, Grok Code Fast 1, 68.3%) — NOT PR-acceptance; dark-factory codebase-sense coined by Dan Shapiro (2026-01-23), not Lopopolo — our own terminology entry updated.
4. **ToS timeline pinned:** Boris Cherny 04-03 restriction → reinstate-with-catch → Agent-SDK credits plan PAUSED (support #15036540 fetched today): SDK/third-party usage currently draws from subscription limits; multi-user prohibited. Policy flipped 3× in 3 months → pilot rule: re-check before deploy.
5. **archon-adversarial-dev** = negotiator→generator→attacker hard-gate state machine — Pattern #76 3rd mechanism stratum (queue v66).
6. **Post-video velocity:** Pi (@earendil-works) + Copilot + OpenCode + MiniMax providers landed; visual builder shipped; per-user credential vault; live-built GSD workflow never shipped.

## Agent-misfire log (main-loop overrides)

1. verify:cole-channel "214K inflated, 204K per tracker" → OVERRIDDEN by yt-dlp `channel_follower_count=214000`.
2. verify:cole-channel could not find the intro video → main-loop channel listing: qMnClynCAmM, 2026-04-08 CDT (Wednesday-evening = 04-09 UTC upload; day-conflict resolved deterministically).
3. verify:cole-channel "no DIYSmartCode identity" → `gh api users/leex279` name = "DIY Smart Code" (45 contributions) = Thomas.
4. README-vs-tree defaults count: 20 files vs "19" in README (table omits archon-test-loop-dag) — documented, not a misfire but an upstream off-by-one.

## Final metric

- `gaps_closed_ratio` ≈ 1.0 on the operator-asked gap (platform layer + Tier-5 #9 builder side). Stop reason: single-source ingest complete + pilot deliverable shipped.

## Suggested next action

Run **A1** from `output/(C) 2026-07-04-archon-harness-builder-pilot-methods.md` — the Archon-vs-cc-sdd comparison-pilot on 2-3 real hireui issues (~1h setup) — it resolves the standing adopt-vs-build fork AND the 0-deployed-pilots pressure in one move. Zero-install same-week alternatives: B1 (pre-registered claim contracts) + B2 (deterministic link-check ship-gate).
