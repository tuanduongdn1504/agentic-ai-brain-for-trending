# Source provenance

## The bundle

Selected by `bin/autopilot-drain.py --dry-run` from query `DeepSeek Harness`, with the operator's video force-included as a declared anchor. **Anchor validation: PASS (1/1 declared, overlap 100%).**

| # | Video | Channel | Date | Len | Views at selection | Role |
|---|---|---|---|---|---|---|
| 1 | Why DeepSeek Harness Just Became The Fastest Growing Github Repo EVER | **Chase AI** | 2026-08-20 | 11:16 | 5,021 | **[ANCHOR]** operator-named |
| 2 | DeepSeek Harness: Claude and Codex at Risk? | The Cef Experience | 2026-08-17 | 9:15 | 6,118 | best primitive explanation of "what a harness is"; reads the paper abstract |
| 3 | Why DeepSeek Harness Is The End Of Coding Agents as We Know Them | Turing Post TV | 2026-08-17 | 14:49 | 39,685 | **strongest source**; the paper, the lineage, the stated limits |
| 4 | Học AI — Phần 003: DeepSeek Harness — Tương Lai Của AI Agent | Code Bug (VN) | 2026-08-18 | 76:48 | 3,922 | **only source that shows it failing**; ecosystem + install reality |
| 5 | DeepSeek Harness Just Changed AI Forever | Better Stack | 2026-08-19 | 5:56 | 31,079 | concise architecture tour; desktop app |
| 6 | This Free Harness Just Broke GitHub (+150K Stars) | Firecrawl | 2026-08-18 | 9:10 | 11,817 | **the bundle's dissent**; hot-reload correction; security framing |

Total ~127 minutes / **22,853 transcript words**.

## Ingest method

**yt-dlp auto-captions, read in full. NotebookLM deliberately not used.**

The routine's Path A (`bin/autopilot-drain.py`) pipes bundles through NotebookLM for summary + 4 asks. For a claims scorecard that is the wrong instrument — grading a claim requires the claim's own words, and a summary layer destroys them. Precedent: the `engineer-of-the-future` ship (*"NotebookLM: none — yt-dlp captions read in full"*).

- English sources: `en-orig` VTT → `bin/vtt-to-md.py` → timestamped markdown.
- Vietnamese source: **`vi-orig`** — read in Vietnamese. Its `en` translation track failed with HTTP 429 and was not retried; reading the original avoids a translation layer between claim and grade.
- One transient failure worth recording: the VN video's first caption fetch hit **HTTP 429**, resolved by a retry with `--retries 5 --retry-sleep 10 --sleep-subtitles 5`.

## Independent verification performed

Every load-bearing claim was checked against a primary or external source on **2026-08-20**. Direct fetches:

- `github.com/deepseek-ai/deepseek-harness` — stars/forks (169.1k / 18.1k), MIT, About string, developer-preview warning, Cordis credit, paper link
- `github.com/cordiverse/paper` — title, abstract verbatim, 2.4k stars, *"Draft of August 13, 2026"*, *"preprint under active revision"*
- `github.com/topics/dsh-plugin` — **8,874 repositories**, top entries by stars
- Web search — paper authorship/affiliations, Cordis→Koishi→shigma lineage, the 4-year/4,000-plugin production history, star-velocity records, and DSH's own *"containment for honest code, not a security boundary"* sandbox language

This follows the standing vault rule that lens/critic agents **and** web summaries confabulate: every collision, identity, and prior-instance claim gets grepped or fetched. Two claims changed grade as a result — the *"fastest ever"* superlative (down to PLAUSIBLE-NOT-PRIMARY once it emerged that no primary source and no GitHub leaderboard supports it) and the ecosystem scale (the ~1,400 figure was reframed once the topic proved 6.3× larger).

## Cross-vault sources consulted

Nine prior source-level DSH analyses in `/Users/Cvtot/KJ OS Template/03 Projects/`: `deepseek-harness`, `deepseek-harness-desktop`, `deepseek-harness-v242-recursive-revisit`, `dsh-TUI`, `dsh-anchored-standard`, `dsh-web-ui`, `awesome-dsh-plugin`, plus their memory threads. Used as the grading baseline in [[deepseek-harness/hype-vs-source-scorecard]]. **Read-only — no files in that vault were modified.** Corrections owed to it are recorded, not executed.

## Selection caveat

The rubric returned a hype-saturated bundle: five of six titles are superlative-framed, and **zero skeptical/testing sources survived selection**. The only sceptic in the pool (CloudYeti, *"Is the Hype Real? LIVE Testing"*) sits at 891 views, below `MIN_VIEWS=1000`. Two high-value videos were absent from this query's pool entirely — Cloud Codes' architecture deep-dive (49,192 views) and NeuralNine's (196,090 views, the largest on the subject). **Flagged pre-ingest, not discovered post-hoc.** A deepen pass should anchor all three. See [[deepseek-harness/caveats-and-corrections]].

## Queue record

- Queue entry: `raw/topics-queue.md` → **DeepSeek Harness — YouTube commentary layer vs source-verified corpus**
- Raw analysis: `raw/2026-08-20-deepseek-harness-youtube-commentary-vs-source.md`
- Loop log: `loop-log/(C) 2026-08-20-11-autopilot-overnight.md` (dry-run selection record)
- Path: **`/loop`, main-loop direct-write** (no subagents; operator instruction)

## Cross-links

[[deepseek-harness/_index]] · [[deepseek-harness/claims-scorecard]] · [[deepseek-harness/caveats-and-corrections]] · [[deepseek-harness/hype-vs-source-scorecard]]
