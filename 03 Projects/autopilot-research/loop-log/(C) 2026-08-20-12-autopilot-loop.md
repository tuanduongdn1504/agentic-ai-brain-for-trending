# (C) Autopilot Loop — 2026-08-20-12 · NEW topic deepseek-harness (75 → 76)

> **Mode:** Path 1 `/loop`, main-loop direct-write · **Trigger:** operator ("can I start build knowledge from this video with loop or anything in queue now?")
> **Constraint honoured:** no subagents, no Workflow (operator instruction). All reading, verification and authorship in the main loop.

---

## Phase 0 — queue + collision check

**Question asked was two questions.** "Can I start now?" → yes, nothing blocked it:

| Check | State |
|---|---|
| `raw/topics-queue.md` pending | **0** |
| Last drain (2026-08-19 23:35) | `Nothing to drain. Exiting.` rc=0 |
| Running autopilot processes | none |
| Next unattended run | 23:35 (launchd `com.cvtot.autopilot-research.plist`) |

**Collision check — the answer that shaped the whole ship:**
- **This vault:** zero hits for "deepseek harness" across 75 topics → genuinely NEW (#76).
- **Other vault** (`/Users/Cvtot/KJ OS Template/03 Projects/`): **NINE** shipped source-level DSH analyses (v235–v242, incl. a 201MB source clone).

So a naive explainer would have re-derived, from an 11-minute hype video, what eight source-level ships already settled. **Reframed as a cross-vault method experiment.** Operator was offered four scopes and elected the **full 6-video bundle**.

## Phase 1–2 — selection

`bin/autopilot-drain.py --dry-run --max 1`, query `DeepSeek Harness` + 1 declared anchor. **Anchor validation PASS (1/1, overlap 100%).**

Picked: `f51ICIoHcjY` Chase AI [ANCHOR] · `sHtbzK8PBcE` The Cef Experience · `jtyV7O4Pt0s` Turing Post TV · `EM_ObHWvd94` Code Bug (VN, 76:48) · `DTu4yvmc0Fc` Better Stack · `aaMM2HQqKKs` Firecrawl.

**Composition flagged BEFORE ingest, not after:** 5 of 6 superlative-framed titles, **zero skeptical/testing sources**. The only sceptic in the pool (CloudYeti, *"Is the Hype Real? LIVE Testing"*) sits at **891 views, below `MIN_VIEWS=1000`** — the rubric structurally cannot pick it. Two high-value videos were absent from this query's pool: Cloud Codes architecture deep-dive (49,192) and NeuralNine (196,090, largest reach). Recorded as deepen candidates; the bundle's counter-pole is the source corpus.

## Phase 3 — ingest

**NotebookLM deliberately skipped.** A claims scorecard cannot grade a paraphrase. Precedent: `engineer-of-the-future`. `yt-dlp --write-auto-subs` → `bin/vtt-to-md.py`; **22,853 words, all six transcripts read in full.**

One failure recorded: the VN video's caption fetch hit **HTTP 429**; retry with `--retries 5 --retry-sleep 10 --sleep-subtitles 5` recovered `vi-orig`. Its `en` translation track failed again and was **not** retried — reading the Vietnamese original is strictly better for grading.

## Phase 4–5 — independent verification

Per the standing rule that lens agents *and* web summaries confabulate, every load-bearing claim was fetched or grepped. Direct: `deepseek-ai/deepseek-harness` (169.1k★ / 18.1k forks / MIT / *"THERE WILL BE COMPATIBILITY-BREAKING CHANGES"* / Cordis credit / paper link) · `cordiverse/paper` (title, abstract verbatim, 2.4k★, *"Draft of August 13, 2026"*, *"preprint under active revision"*) · `github.com/topics/dsh-plugin` (**8,874 repos**). Plus web search for paper authorship, Cordis→Koishi→shigma lineage, star-velocity records, and DSH's own sandbox language.

**Two claims changed grade because of this:** the *"fastest ever"* superlative dropped to PLAUSIBLE-NOT-PRIMARY (no GitHub leaderboard, no primary source), and the ecosystem scale was reframed once the topic proved 6.3× the catalogue.

## Phase 6 — findings

1. ⭐⭐ **The videos caught a paper nine source-level ships missed — linked from the README they quoted.** → *A source read that stops at the repository boundary misses the literature the repository cites.*
2. ⭐⭐ **`dsh-plugin` topic = 8,874 repos vs the catalogue's ~1,400 (~16%).** N=2 instance of v240's own inventory rule, applied to v240.
3. ⭐ **Security primary-sourced:** DSH's docs — sandbox is *"containment for honest code, not a security boundary."*
4. ⭐ **RC6→RC7 extends v242's D24**, doesn't refute it. → *A zero-code-delta version bump is not a zero-impact version bump when third-party plugins pin your kernel's version.*
5. ⭐ **v242's star PIN refined**: it conflated *mocked-API* (v239, DSH's own surfaces) with *page-stated* (github.com). Seven consistent readings across four days, incl. the vault's own 159.0k.
6. **What the source read still owns alone:** governance (`CONTRIBUTING.md` refuses external PRs) — **not one of six videos mentions it**; provenance; D23 counts; and **zero mentions of evaluation in ~127 minutes**.

**Scorecard: 47 claims — 24 CONFIRMED / 10 CBI / 4 PLAUSIBLE-NOT-PRIMARY / 4 MISLEADING / 1 FALSE / 3 UNRESOLVED / 1 UNVERIFIABLE / 0 FABRICATED.**

## Phase 7–8 — librarian discipline

- **15 wiki files** at `wiki/deepseek-harness/`
- **32 unique wikilinks filesystem-validated → 0 broken**
- `raw/_inventory.md`: +1 table row, +1 bullet, Status `compiled`
- `wiki/_master-index.md`: topic prepended → **76 topics / 76 wiki dirs, reconciled**
- `raw/topics-queue.md`: entry moved to `## Completed`; **pending back to 0** (re-verified with `--list-only`)
- Raw analysis: `raw/2026-08-20-deepseek-harness-youtube-commentary-vs-source.md`

## Failures and corrections (Rule 12)

- **My scorecard totals were wrong on first write.** Hand-count 18/14/3/4/1/5/2; machine tally **24/10/4/4/1/3/1**. Both summed to 47, which is why it was invisible. → *A totals line you hand-count from a table you wrote is a second guess, not a check.*
- **Nearly misapplied a PIN.** v242's "the GitHub API is mocked" is v239's finding about **DSH's own UI**, not about github.com readings. Caught before it shipped.
- **Shell flakiness:** a `python3 - <<'PY'` heredoc was SIGKILLed (exit 137) mid-write. Verified the target file was **byte-identical to its backup** before retrying via a script file. No partial write.
- **One deliberate non-resolution:** the VN source's RC7-sandbox hypothesis, which he half-retracted himself. Left **UNRESOLVED** rather than resolved toward the more interesting reading.

## Metric

`gaps_closed_ratio`: DSH coverage in this corpus **0/1 → 1/1**. Cross-vault: **5 corrections owed to the other vault, recorded NOT executed** (editing another vault's ships is an operator decision).

## Next action

**Deepen pass** anchoring the three videos the rubric could not reach — Cloud Codes (49,192), NeuralNine (196,090), CloudYeti (891, below `MIN_VIEWS`, needs an explicit anchor). Then the ~2h zero-install hireui action: `docs/adr/llm-trajectory-record.md`.
