# (C) Autopilot Loop — 2026-07-15-15

> **Trigger:** manual (`/loop`-style, operator-submitted single video)
> **Topic:** adaptive-engineering-beyond-harness — Rajiv Chandegra, "Beyond the Harness: A Journey Towards Adaptative Engineering" (`qdZzND79mcg`)
> **Started:** 2026-07-15 (main-loop session, Opus 4.8)
> **Ended:** 2026-07-15
> **Path:** 5 (yt-dlp only; no NotebookLM)

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 (yt-dlp transcript) | 1 (topic itself) | 0 | 1.0 |

Cold-start for a new topic; single-cycle compile. `gaps_closed_ratio = 1.0` (topic fully compiled — 11 wiki files + pilot deliverable; no stubs; all internal cross-links resolve).

## Sources ingested

- `raw/2026-07-15-adaptive-engineering-beyond-harness.md` (yt-dlp EN auto-captions → `vtt-to-md.py` dedupe → 78 `[mm:ss]` paragraphs + metadata header; ~14K). Full transcript read in main loop.

## Verification

- Workflow `wf_993219c1-885` — 14 agents (11 refute-first fact-checkers + corpus-xref + thesis-critique + completeness-critic), all Haiku 4.5; ~519K tokens, 123 tool calls, **0 errors / 0 empty**, ~144s.
- 2 Opus main-loop WebSearch ground-checks of the most consequential findings (event correction + Pi repo move), per the vault's independent-identity-verification discipline.
- **No verifier misfires.** The only machine-claim adjustment: softened the completeness critic's "contradicts talk" framing on `AGENTS.md`/`CLAUDE.md` to "correct-with-caveat" after re-reading the transcript (speaker hedged "…or the Claude.md if you're using Claude code").

## Wiki articles created

- `wiki/adaptive-engineering-beyond-harness/_index.md` (NEW)
- `wiki/adaptive-engineering-beyond-harness/overview.md` (NEW)
- `wiki/adaptive-engineering-beyond-harness/the-two-paradigms.md` (NEW)
- `wiki/adaptive-engineering-beyond-harness/complexity-science-foundations.md` (NEW)
- `wiki/adaptive-engineering-beyond-harness/adaptive-engineering-mechanics.md` (NEW)
- `wiki/adaptive-engineering-beyond-harness/failure-modes.md` (NEW)
- `wiki/adaptive-engineering-beyond-harness/vs-harness-engineering-corpus.md` (NEW)
- `wiki/adaptive-engineering-beyond-harness/claims-scorecard.md` (NEW)
- `wiki/adaptive-engineering-beyond-harness/caveats-and-corrections.md` (NEW)
- `wiki/adaptive-engineering-beyond-harness/hireui-and-vault-pilot.md` (NEW)
- `wiki/adaptive-engineering-beyond-harness/source-provenance.md` (NEW)
- `wiki/_master-index.md` (UPDATED — added topic at top, newest-first)
- `wiki/harness-engineering/_index.md` (UPDATED — added 1 additive counter-thesis cross-link line)
- `raw/_inventory.md` (UPDATED — added 2026-07-15 row, status compiled)
- `output/(C) 2026-07-15-adaptive-engineering-beyond-harness-pilot-methods.md` (NEW — "watch, don't build" pilot menu A–D)

## Final metric

- `gaps_closed_ratio` = **1.0**
- **Scorecard (11 checkable claims): 10 CONFIRMED / 1 MISLEADING / 0 FALSE / 0 FABRICATED** (+ 2 correct-but-unattributed frameworks). High-integrity philosophy talk.
- Stop reason: single-cycle cold-start compile complete; target ratio (0.5) exceeded.

## Corpus-firsts / notable

- **Corpus' FIRST source that argues AGAINST the fixed-harness paradigm** — a genuine counter-thesis to the 32-article `harness-engineering` flagship (same harness definition, opposite prescription). Wired in as a bidirectional cross-link.
- **First "watch, don't build" pilot posture in the corpus** — the topic's honest verdict is *do not adopt* (no working implementation; legibility-collapse risk in regulated domains). The pilot value is a *guard-rail* (keep hireui candidate paths legible) + a *lens* (Cynefin complicated-vs-complex pre-flight).
- **Event correction caught by verification:** ingest's initial "World's Fair 2026" assumption (from the July upload date) was wrong → **AI Engineer Europe 2026 (London, Apr 8–10)**, re-verified independently. Adds to the recurring "verify the venue separately from the content" pattern (cf. pocock-software-fundamentals).
- **Two unattributed frameworks flagged:** Cynefin (Snowden) and boids (Reynolds) — used accurately but never named.
- **Currency correction:** Pi repo moved `badlogic/pi-mono` → `earendil-works/pi` (Earendil Inc./Armin Ronacher, Apr–May 2026) — the corpus' pi-mono (Storm Bear v36) predates this; flag for update.

## Top-3 unclosed gaps

1. One secondary source (BigGo) lists a "recorded 21 May 2026" date that post-dates the April Europe event — likely an outlet error; venue = Europe 2026 is multi-source solid, but the exact recording date is not nailed. Minor.
2. Storm Bear **pi-mono** (v36) entry is now stale re: the `earendil-works/pi` move — noted here, not edited (out of autopilot scope; write is Storm-Bear-side).
3. The "horizontal-intelligence beats vertical" bet is the talk's one falsifiable claim but has no evidence either way in-corpus yet — flagged as a watch-item for `multi-agent-orchestration/research-roadmap`.

## Suggested next action

This is a **frontier-watch** topic — no pilot to run. The one immediately usable output is **A1**: add the Cynefin "complicated vs complex?" pre-flight question to the harness-design checklist (it *validates* your current fixed-harness approach for hireui's complicated work), and **B1**: turn the critic's legibility objection into an ADR that hireui's candidate-facing LLM paths (Match-Explain/ranking) stay fixed + legible + audited. Files are on the `autopilot-research` branch working tree, awaiting your `git commit`.
