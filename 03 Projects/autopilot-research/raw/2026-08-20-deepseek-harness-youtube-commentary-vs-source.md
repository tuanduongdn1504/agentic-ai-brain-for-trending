# Raw analysis — DeepSeek Harness: YouTube commentary layer vs source-verified corpus

> **Date:** 2026-08-20 · **Path:** 1 `/loop`, main-loop direct-write · **Ingest:** yt-dlp auto-captions read in full, **NO NotebookLM** (deliberate — see below)
> **Queue entry:** "DeepSeek Harness — YouTube commentary layer vs source-verified corpus"
> **Wiki output:** `wiki/deepseek-harness/` — 15 files

## Why NotebookLM was skipped

The deliverable is a **claims scorecard**. Grading a claim requires the claim's own words; a summarization layer destroys the thing being graded. Precedent: `engineer-of-the-future` (2026-07-22) — *"NotebookLM: none (yt-dlp captions read in full)"*. All 6 transcripts (22,853 words) read in full in the main loop.

## Bundle (anchor validation PASS 1/1, overlap 100%)

Selected by `bin/autopilot-drain.py --dry-run --max 1` from query `DeepSeek Harness` + 1 declared anchor.

| # | ID | Channel | Date | Len | Views | Words |
|---|---|---|---|---|---|---|
| 1 | `f51ICIoHcjY` | **Chase AI** [ANCHOR] | 2026-08-20 | 11:16 | 5,021 | 2,531 |
| 2 | `sHtbzK8PBcE` | The Cef Experience | 2026-08-17 | 9:15 | 6,118 | 1,648 |
| 3 | `jtyV7O4Pt0s` | Turing Post TV | 2026-08-17 | 14:49 | 39,685 | 2,304 |
| 4 | `EM_ObHWvd94` | Code Bug (VN) | 2026-08-18 | 76:48 | 3,922 | 13,375 |
| 5 | `DTu4yvmc0Fc` | Better Stack | 2026-08-19 | 5:56 | 31,079 | 1,157 |
| 6 | `aaMM2HQqKKs` | Firecrawl | 2026-08-18 | 9:10 | 11,817 | 1,838 |

Fetch notes: `en-orig` for all EN; **`vi-orig`** for #4 (its `en` translation track failed HTTP 429 and was NOT retried — reading the original is better for grading). #4's first fetch hit 429; resolved with `--retries 5 --retry-sleep 10 --sleep-subtitles 5`.

## Collision check

- **This vault:** zero hits for "deepseek harness" across all 78 wiki topics. Genuinely NEW topic (#79).
- **Other vault** (`/Users/Cvtot/KJ OS Template/03 Projects/`): **NINE** shipped source-level DSH analyses — v235 `deepseek-harness`, v236 `dsh-TUI`, v237 `dsh-better-sidebar`, v238 `dsh-anchored-standard`, v239 `dsh-web-ui`, v240 `awesome-dsh-plugin`, v241 `dsh-desktop`, v242 recursive revisit (201MB source clone). Used as the grading baseline. **Read-only; nothing in that vault was modified.**

## Independent verification (2026-08-20)

Direct fetches: `github.com/deepseek-ai/deepseek-harness` (169.1k★ / 18.1k forks / MIT / developer-preview warning / Cordis credit / paper link) · `github.com/cordiverse/paper` (title, abstract verbatim, 2.4k★, "Draft of August 13, 2026", "preprint under active revision") · `github.com/topics/dsh-plugin` (**8,874 repositories**). Web search: paper authorship + affiliations, Cordis→Koishi→shigma lineage, 4-year/4,000-plugin history, star-velocity records, DSH's own sandbox language.

## Headline findings

**1. The videos caught a formal paper that nine source-level ships missed — and it is linked from the README they quoted.**
`cordiverse/paper`, *"A Programming Paradigm for Spatiotemporal Composability"*, ~80pp, Yifan Shi (PKU+DeepSeek) / Wei Zhang (PKU) / Tianyi Cui (DeepSeek), built on **effects and coeffects** from type theory, with a **confluence** result. v242 quoted `README.md:7` for the Cordis credit and did not follow the outbound paper link on the same page.
→ **Rule: a source read that stops at the repository boundary misses the literature the repository cites.**

**2. Ecosystem is 6.3× larger than the vault had measured.** `dsh-plugin` topic = **8,874 repos**; the `awesome-dsh-plugin` catalogue v240 audited = **~1,400 entries (~16%)**. A clean N=2 instance of **v240's own inventory rule**, applied to v240. Also: `open-design` (89.4k★, already a vault topic) and `reactive-resume` (41.2k★) carry the tag — an unknown share of the 8,874 is retrofitted tags on pre-existing repos, making the topic count a weak proxy for plugin development.

**3. Security: primary-source confirmation.** DSH's own docs: *"The sandbox is containment for honest code, not a security boundary — host-realm helpers on the sandbox global are reachable, so package code can reach Node."* Four videos independently report full shell + filesystem access for every plugin. v240 (metadata) + v241 (identity, *"do not review the plugin or its dependency tree"*) + v242 (effect unmeasured) built this inferentially across three ships; the videos found the sentence where DeepSeek concedes it.

**4. RC6→RC7 extends v242's D24 rather than refuting it.** The VN source broke on the bump v242 measured as "version strings only." His failures were Node-version and plugin-pinned-Cordis resolution errors — ecosystem, not core. → **New rule: a zero-code-delta version bump is not a zero-impact version bump when third-party plugins pin your kernel's version.**

**5. "Fastest growing repo EVER" = PLAUSIBLE, NOT PRIMARY.** ~20k★ in ~1h, ~100k in <48h, prior reference Grok-1 ~1.2 days, OpenClaw named as prior holder (independently reached by the VN source). **But GitHub publishes no star-velocity record and no primary source makes the claim.** Chase AI's *numeric* claim (167,000 on 08-20) is CONFIRMED — 169.1k measured same day.

**6. Star-count PIN refined, not overturned.** v242's "do not cite any star figure" conflated two caveats: *mocked GitHub API* applies to figures rendered by **DSH's own surfaces** (v239); *page-stated* applies to github.com readings. Seven mutually-consistent readings across four days (incl. the vault's own 159.0k on 08-18) is stronger than one. → Cite only date-stamped + marked page-stated; never from DSH's UI; never a velocity record.

**7. What the source read still owns exclusively:** governance (`CONTRIBUTING.md` refuses external PRs → publish a `dsh-plugin`-tagged plugin instead; 1,008 internal PR merges; the `deepseek-harness` org has zero public repos) — **not one of six videos mentions it**; provenance (12,404 commits, one root commit, exemplary Shigma vendoring, deny-by-default install scripts, zero npmmirror/cnpm in 1,203 lockfile resolutions); D23 language-basis counts; and **the total absence of an eval harness** — six videos, ~127 minutes, zero mentions of evaluation or benchmarks.

## Scorecard

**47 claims: 24 CONFIRMED · 10 CBI · 4 PLAUSIBLE-NOT-PRIMARY · 4 MISLEADING · 1 FALSE · 3 UNRESOLVED · 1 UNVERIFIABLE · 0 FABRICATED.**
Totals tallied programmatically from the table — my hand-count was wrong on first write (see `caveats-and-corrections`).

The single **FALSE**: Cef's unqualified *"when you modify a plugin, it gets updated without having to rebuild or relaunch"* — true of dynamic (creator-minted) plugins, false of installed presets, which Firecrawl demonstrates are frozen at session start.

## Selection caveat (flagged pre-ingest)

Rubric returned a **hype-saturated bundle**: 5 of 6 titles superlative-framed, **zero skeptical/testing sources**. The only sceptic in the pool (CloudYeti *"Is the Hype Real? LIVE Testing"*) sits at 891 views, below `MIN_VIEWS=1000`. Two high-value videos absent from this query's pool: **Cloud Codes** architecture deep-dive (49,192 views — most gradeable-against-source) and **NeuralNine** (196,090 — largest reach on the subject). **A deepen pass should anchor all three.** The bundle's counter-pole is therefore the source corpus, not another video; Firecrawl's dissent (*"solving a problem I'd say never existed"*) and Chase AI's *"probably not"* partially compensate.

## Standing position unchanged

**Read-and-borrow. Install nothing.** Developer preview + *"THERE WILL BE COMPATIBILITY-BREAKING CHANGES"* + vendor-disclaimed sandbox + no eval harness + closed to external PRs (no upstream recourse). Nothing was installed during this ship. **The one thing worth taking is the trajectory** — see `wiki/deepseek-harness/hireui-relevance.md`.

## Corrections owed to the other vault (recorded, NOT executed)

1. Add `cordiverse/paper` + the spatiotemporal-composability formalism to the DSH chain (absent from all nine ships).
2. Restate v240's count as "1,390 curated entries out of 8,874 topic repositories (~16%)."
3. `dsh-market` (in-harness runtime marketplace, v1.13.1) is a third ecosystem surface neither v240 nor v241 covers.
4. Extend v242's D24 with the plugin-pinning corollary.
5. Refine v242's star-figure PIN per finding #6.
