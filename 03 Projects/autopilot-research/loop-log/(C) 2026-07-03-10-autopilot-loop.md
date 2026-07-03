# (C) Autopilot Loop — 2026-07-03-10

> **Trigger:** operator-submitted single video (interactive session; "build knowledge from this video + double deep dive into the original resource + pilot methods")
> **Topic:** pocock-real-feature-build — Matt Pocock "Building a REAL feature with Claude Code: every step explained" (hX7yG1KVYhI)
> **Started:** 2026-07-03T10:12+07:00
> **Ended:** 2026-07-03T11:20+07:00 (approx)
> **Duration:** ~68m

## Phase trace

1. **Phase 0 pre-flight:** yt-dlp present (ffmpeg absent → VTT parsed directly, known-good path). Video identified: Matt Pocock first-party upload, 2026-03-18, 44:16, 162,785 views. Inventory row appended (`Status: raw`).
2. **Phase 2 ingest (Path 5):** `--write-auto-subs --sub-langs en` VTT → `clean_vtt.py` dedupe → ~50K-char transcript **read in full** → `raw/2026-07-03-pocock-real-feature-build.md` (54K with header).
3. **Deep-dive (operator-ask extension):** Workflow `wf_8897fa8d-c95` — **15 agents** (7 deep-dive gatherers: cvm-repo / cvm-harness / skills-repo / sandcastle / aihero / ddd / cc-features + 7 adversarial REFUTE-first verifiers + completeness critic); ~880K subagent tokens, 400 tool calls, ~7.6 min wall-clock. **+ operator `gh api` ground-checks** (skills repo metadata, ubiquitous-language + domain-modeling skill fetches).
4. **Phase 3 compile:** 11 wiki files written (below); master index entry appended; raw file marked compiled; inventory row updated to `compiled`.
5. **Phase 5 audit:** gaps_at_start = 1 (cold-start new topic) → gaps_at_end = 0 for the topic itself. Known residual gaps flagged in wiki (Jaman attribution unverified; video-era `.sandcastle` internals unrecoverable — drift documented).
6. **Phase 7:** this log + git commit on `autopilot-research` branch.

## Verifier-misfire incident (logged per standing discipline)

The ddd-verifier REFUTED two true facts: (a) declared `/ubiquitous-language` skill non-existent — it exists at `skills/deprecated/ubiquitous-language/` (caught by completeness critic cross-referencing the skills-repo dossier; settled by operator `gh api` tree grep + file fetch); (b) declared mattpocock/skills "impossible before June 2026" from the v1.0.0 release *tag* — `created_at` = 2026-02-03. **New misfire sub-type: release-tag-as-creation-date confusion.** The same verifier correctly caught real dossier errors (53K★→154.5K★, arXiv mischaracterization, 2 unreachable-cited sources) — mixed-quality verdicts within one agent; per-claim ground-checking remains mandatory for existence claims.

## Sources ingested

- `raw/2026-07-03-pocock-real-feature-build.md` (yt-dlp, 1 video, first-party)
- Originals: github.com/mattpocock/course-video-manager (repo + `.sandcastle/` + `CONTEXT.md` + `.claude/skills/` + settings + `api.feedback.ts`) · github.com/mattpocock/skills (37 skills; grill-me/to-prd/to-issues/ubiquitous-language/domain-modeling) · @ai-hero/sandcastle (npm + GitHub timeline) · aihero.dev (five-daily-skills article + cohort) · Evans DDD 2003 (+ 2026 prior-art scan) · Claude Code docs/changelog (Explore, /btw, AskUserQuestion, devcontainers)

## Wiki articles created

- wiki/pocock-real-feature-build/_index.md (NEW topic)
- wiki/pocock-real-feature-build/overview.md
- wiki/pocock-real-feature-build/grill-me-in-practice.md
- wiki/pocock-real-feature-build/ubiquitous-language-for-llms.md
- wiki/pocock-real-feature-build/prd-and-issues-pipeline.md
- wiki/pocock-real-feature-build/sandcastle-ralph-afk-loop.md
- wiki/pocock-real-feature-build/qa-plan-and-feedback-loop.md
- wiki/pocock-real-feature-build/course-video-manager-as-artifact.md
- wiki/pocock-real-feature-build/the-originals.md
- wiki/pocock-real-feature-build/caveats-and-corrections.md
- wiki/pocock-real-feature-build/source-provenance.md
- wiki/_master-index.md (UPDATED — added topic)
- raw/_inventory.md (UPDATED — row raw→compiled)
- output/(C) 2026-07-03-pocock-real-feature-build-pilot-methods.md (26 methods + skip-list + critic reframe)

## Final metric

- `gaps_closed_ratio` = 1.0 (cold-start: topic gap opened and closed within the run)
- Stop reason: single-topic operator ask complete (compile + pilot menu shipped)

## Top unclosed threads

1. "Jaman" day-shift/night-shift attribution — reported-only; no fetchable source.
2. The video-era `.sandcastle` internals (pre-package) — superseded in-repo; drift table documented in caveats-and-corrections.
3. Matt's separate ~96-min AI-Engineer-2026 workshop — still uncompiled (third Pocock source; candidate future topic).

## Suggested next action

Run pilot composition #1 from the menu: **A1 + A2 in one session** — grill→`CONTEXT.md` glossary→PRD→issues on the hireui Candidate-Detail refactor (zero install, composes with cc-sdd #1 and the running v189 loop pilot). Alternatively queue the AI-Engineer-2026 workshop video as the third Pocock topic.
