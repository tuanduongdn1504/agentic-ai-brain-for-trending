# (C) Autopilot Loop — 2026-07-05-16

> **Trigger:** manual operator request (interactive session; "build knowledge from this video + double deep dive into the original resource + pilot menu")
> **Topic:** harness-engineering DEEPEN — TNT (Trung Tran) Cursor-CLI factory, individual-scale 10th sibling
> **Started:** 2026-07-05T16:10+07:00 (approx)
> **Ended:** 2026-07-05T17:15+07:00 (approx)
> **Duration:** ~65m main loop + ~7m background workflow

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 2 (video + repo) | 1 (topic gap: no auditable individual-scale factory; roadmap "more first-party factory evidence") | 0 closed-of-scope (4 new watch-list items opened) | 1.0 on scoped gap |

## Sources ingested

- `raw/2026-07-05-tnt-harness-fpt-talk-and-we-event-repo.md` (combined raw: metadata + talk skeleton + manifest)
- `raw/2026-07-05-tnt-we-event-repo-extracts/` — transcript-clean.md (1,055 lines, read IN FULL in main loop per first-party practice) + original VTT (416KB) + `repo/` 18 files (HARNESS-DESIGN.md, ai-harness README, 4 agent prompts, ralph-loop.json, testgen-loop.json, ralph-once.sh, pick-next-slice.sh, guardrails.md, progress.md, models.json, package.json, human-review-checklist.md, context-map.json, brds prompt.md, commits page 1)
- Video: https://www.youtube.com/watch?v=LaIZ4yRd7mA (TNT, 2026-06-28, 46:17, 1,993 views at fetch)
- Repo: https://github.com/trannamtrung1st/ai-engineering-learning (master @ 2026-07-05)

## Verification

- Workflow `wf_3740e2d5-2b4`: 22 agents, ~1.55M tokens, 520 tool calls — 6 dives (scripts / backlog-config / docs-layer / git-history / siblings / app-quality) + 3 external verifiers (cursor-cli / identity / lineage) + 12 refute-first claim verifiers + completeness critic.
- **REFUTED before publication (7 dive misfires):** drift-check-once-per-loop (actually every iteration); Vitest runners (actually Node native `--test`); talk-says-docs-AI-generated (talk doesn't say it); context-map-paths-validated (they are NOT — recorded as weakness); testgen-docs-map auto-regenerated (manual); Playwright-specs-codegen-owned rule (doesn't exist in prompt); all-9-docs-present claim (per-path check, tree-verified instead).
- **Garble corrected via search-before-discard:** "Western Synergy" → **Web Synergies** (Singapore, Yokogawa subsidiary). Also: "cơ sơ"→Cursor, "play MCB"→Playwright MCP, "slide/lá c"→slice, "$200/yr"→$192/yr Cursor Pro annual.
- **Confirmed load-bearing:** Cursor Auto "unlimited on all paid plans / does not cost credits" (official docs); 16.6-min median slice cadence (matches talk's 15–30 min); 40.5% overnight commits; zero human app-code commits in 687; demo slice commit `161edee`; identity + FPT event + personal channel.
- Critic blocking gaps: resolved in main loop (docs-presence via tree listing; hesd-vs-we-event attribution separated in articles; ralph-once.sh read in full in main loop).
- Known dive drift: docs-layer agent analyzed the hesd docs family instead of we-event — findings attributed to hesd explicitly in [[tnt-factory-run-empirics]]; we-event docs inventoried from tree (39 docs + 66 test-case JSONs).

## Wiki articles created/updated

- wiki/harness-engineering/tnt-cursor-cli-factory-anchor.md (NEW)
- wiki/harness-engineering/tnt-we-event-harness-mechanics.md (NEW)
- wiki/harness-engineering/tnt-factory-run-empirics.md (NEW)
- wiki/harness-engineering/tnt-vs-corpus-positioning.md (NEW)
- wiki/harness-engineering/_index.md (UPDATED — count 28→32, extension note, new section, Sources 30–31)
- wiki/_master-index.md (UPDATED — harness-engineering entry extended; promotion candidacy upgraded to "firm")
- raw/_inventory.md (UPDATED — +1 row)

## Final metric

- `gaps_closed_ratio` = 1.0 on the scoped gap (auditable individual-scale factory evidence — previously absent, now the topic's most complete run ledger)
- Stop reason: single-source operator-directed ingest complete (not a multi-cycle autonomous run)

## Top unclosed follow-ups (watch-list)

1. **hesd vs hesd_bmad outcome** — the in-the-wild adopt-vs-build A/B is early (hesd_bmad scaffolded, result unknown). Re-check repo ~2 weeks (pushed as recently as 2026-07-05).
2. The FPT workshop's *other* session (a requirements-phase harness-generating tool demo) — unidentified; possible sibling source if published.
3. we-check-app harness deltas only partially mapped (SLICE_DEFER removal, skills enrichment) — full diff worth a pass if the topic goes to promotion audit.
4. Cursor `-p` hang issue + Auto-lane ToS stability — economics claims are date-stamped 2026-07-05; re-verify before any pilot that depends on the Auto lane.

## Suggested next action

Pilot from the menu delivered in-session (headline: port fingerprint-drift gate + forbidden-patterns gate to hireui BMAD harness; run the A/B the way Trung runs hesd vs hesd_bmad). Queue Pattern #76 4th-stratum + #21-unbranded + #55-VN evidence at v66 mini-audit.
