# (C) Autopilot Loop — 2026-07-01-11

> **Trigger:** manual (operator-submitted single video + "double deep-dive into the original resource" + "show me many methods for my apply")
> **Topic:** open-design (`nexu-io/open-design` — open-source Claude Design alternative)
> **Started:** 2026-07-01 ~11:05 (+07)
> **Ended:** 2026-07-01 ~12:2x (+07)
> **Duration:** ~75 min (main-loop compile; workflow ~8.5 min of that in background)

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 video (transcript) + 10 originals deep-dived | 1 (new topic = cold-start gap) | 0 | 1.0 |

Cold-start: topic `open-design` did not exist. One cycle created the full topic (11 articles + index + pilot menu). `gaps_closed_ratio = 1.0`.

## Sources ingested

- `raw/2026-07-01-open-design.md` — yt-dlp English auto-subs of QOqWZzecjuY (CodingMenace "Open Design in 20 Minutes"), deduped ~4,200-word transcript, read in full. NO NotebookLM.
- **Originals deep-dived** (via Workflow `wf_4a91a8b2-2bb`, 13 agents, ~633K subagent tokens, 219 tool calls; + operator `gh api`/WebFetch ground-checks): nexu-io/open-design + alchaincyf/huashu-design + OpenCoworkAI/open-codesign + multica-ai/multica + op7418/guizang-ppt-skill + lewislulu/html-ppt-skill + VoltAgent/awesome-design-md + bergside/awesome-design-skills + heygen-com/hyperframes + Anthropic's Claude Design product.

## Wiki articles created/updated

- `wiki/open-design/_index.md` (NEW)
- `wiki/open-design/overview.md` (NEW)
- `wiki/open-design/architecture-and-byoa.md` (NEW)
- `wiki/open-design/design-md-as-source-of-truth.md` (NEW)
- `wiki/open-design/features-and-workflow.md` (NEW)
- `wiki/open-design/install-and-setup.md` (NEW)
- `wiki/open-design/huashu-design-deep-dive.md` (NEW)
- `wiki/open-design/the-originals.md` (NEW)
- `wiki/open-design/open-design-vs-claude-design.md` (NEW)
- `wiki/open-design/caveats-and-safety.md` (NEW)
- `wiki/open-design/source-provenance.md` (NEW)
- `wiki/_master-index.md` (UPDATED — appended `## open-design` entry)
- `raw/_inventory.md` (UPDATED — +1 table row [newest-first] + 1 coverage-summary bullet)
- `output/(C) 2026-07-01-open-design-pilot-methods.md` (NEW — 24 ranked methods)

## Final metric

- `gaps_closed_ratio` = **1.0** (cold-start topic fully created in one cycle)
- Stop reason: target_ratio reached (single-video manual ingest complete; no backlog)

## Verification summary (anti-fabrication)

- **13-agent workflow** (8 original/main deep-dives → 3 adversarial skeptics + 1 hireui-application → 1 synthesis critic). Every factual claim grounded in `gh api` / WebFetch of primary sources.
- **Critic over-flag OVERRIDDEN:** the synthesis critic (5.5/10 conservative) flagged "Claude Design existence unverified" as CRITICAL #1 — but the dedicated skeptic HAD verified it, and the operator independently confirmed via WebFetch of the Anthropic announcement + TechCrunch/VentureBeat. **Claude Design is REAL** (Anthropic Labs, 2026-04-17, Opus 4.7, cloud-only, Pro/Max/Team/Enterprise). Same verifier-misfire pattern seen in pocock/how-we-claude-code topics.
- **Corrections captured** (in `caveats-and-safety.md` + `source-provenance.md`): guizang-ppt = AGPL-3.0 upstream (README calls bundled copy "MIT" — conflict); multica = NOASSERTION; "no telemetry" = opt-in PostHog; "SSRF protection" unconfirmed in code; plugin/skill counts inflated/moving; open-codesign is the true "first"; install is pnpm now (video used npm); HyperFrames-integration / `.zip`-import / creative-media-providers not code/doc-confirmed.
- **Star velocity** (73,468★/64d) assessed **organic** (smooth curve, 30 named contributors, <2% bots) with a disclosed **$1,000/MR "Fellows"** accelerant.

## Top-3 unclosed gaps (for a future pass)

1. **HyperFrames integration is README-described, not code-audited** — a source-tree grep of `nexu-io/open-design` for `heygen-com/hyperframes` imports would confirm shipped-vs-roadmap.
2. **DESIGN.md schema parity** — VoltAgent's 9 sections and Open Design's 9 sections differ; a side-by-side of both live schemas would sharpen `design-md-as-source-of-truth.md`.
3. **Claude Design `.zip` import + creative-media providers (Suno/MJ/etc.)** — shown in video / hero alt-text but not in repo docs; verify in a live install (would fold into the A2 pilot).

## Suggested next action

Ship this on a branch (per operator convention: wiki ships go on `wiki/vNNN-<slug>` off `main`, no auto-merge). Then, for **Goal #2**, start the pilot headline: **B2 → A1** (steal the Brand Asset Protocol + codify hireui's Candidate-Detail tokens as a portable `DESIGN.md` SoT — zero install, fixes the drift root-cause), open the **A13 "Design-System-as-Code" ADR**, and book a Week-2 checkpoint for the **A2 sandbox Open-Design pilot** (M0 install hygiene first). See `output/(C) 2026-07-01-open-design-pilot-methods.md`.
