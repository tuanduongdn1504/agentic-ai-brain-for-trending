# Source provenance and method

## The six sources

| # | Video | Channel | Date | Length | Views | Role |
|---|---|---|---|---|---|---|
| 1 | **[ANCHOR]** *Homebrew - package manager vô đối trên MacOS* [`A_nvIGTNfuw`](https://www.youtube.com/watch?v=A_nvIGTNfuw) | **Kunkka** (VN, 7,240 subs) | 2026-08-10 | 14:05 | 15,621 | The argument. Not a tutorial — says so explicitly |
| 2 | *Homebrew: macOS Package Manager* [`1uvr9-zUB3w`](https://www.youtube.com/watch?v=1uvr9-zUB3w) | **Hands-On Apple** — *Hands-On Mac*, TWiT, **Leo Laporte** | **2020-05-08** | 12:00 | 78,800 | The 2020 baseline. Pre-Apple-silicon |
| 3 | *The Ultimate Mac Terminal Setup* [`d4bTkiftBOk`](https://www.youtube.com/watch?v=d4bTkiftBOk) | **Warp** | 2023-07-07 | 8:20 | 452,340 | Weakest on-topic. Homebrew is one segment at 05:34 |
| 4 | *Getting Started with Homebrew* [`OPGxO1fdrT8`](https://www.youtube.com/watch?v=OPGxO1fdrT8) | **Dev Neil A** | 2025-12-06 | 10:22 | 4,382 | **Best operational coverage.** Lowest views in the bundle |
| 5 | *Homebrew on macOS: How to Install & Use (Full Guide 2026)* [`ODVaw70G0ko`](https://www.youtube.com/watch?v=ODVaw70G0ko) | **Easy Tech Steps** | 2026-03-26 | 7:21 | 6,681 | Consumer install walkthrough |
| 6 | *Homebrew 6.0 Just Changed How Your Mac Installs Software* [`IwzVzvDw68w`](https://www.youtube.com/watch?v=IwzVzvDw68w) | **Better Stack** | 2026-07-29 | 5:13 | 52,132 | **Most consequential.** The only source that knows 6.0 exists |

**Total transcript: 63,531 bytes across six files, all read in full.** No NotebookLM — a claims scorecard cannot grade a paraphrase, per the `engineer-of-the-future` and `deepseek-harness` precedents.

Two provenance notes:

- **Better Stack is a repeat channel**, having appeared in the `deepseek-harness` bundle three weeks earlier. Its value here is the same as there: fast, accurate coverage of a release, with dates worth double-checking.
- **Kunkka is new to this corpus** — grepped, zero prior mentions. So is Homebrew as a subject: it appeared in only two prior wiki files (`herdr/supported-agents-and-install.md`, `graphify-codebase-graph/opencode-integration.md`), both incidentally, as install instructions.

## Method

1. **Trigger.** Operator submitted one URL and asked whether anything in the queue blocked shipping it. **Queue was empty — 0 pending**; the previous overnight drain (2026-08-20 23:35) had logged `Nothing to drain. Exiting.`; no `brew`/`yt-dlp`/drain processes were running; the launchd job `com.cvtot.autopilot-research` fires at 23:35 daily. Nothing blocked it.
2. **Operator chose** an anchored 6-video bundle, run immediately, over three alternatives (single-source capture, a vault-hygiene framing, or skipping the topic as off-goal).
3. **Query selection.** Three candidate queries were probed by **importing `yt_search()` and `select_videos()` from `bin/autopilot-drain.py`** and running them directly, so the prediction used the real rubric rather than an approximation. Query `Homebrew macOS package manager terminal setup` produced the most topically coherent pool and was committed to the queue.
4. **Queue entry** written to `raw/topics-queue.md` with one declared anchor, then verified with `--list-only`.
5. **Selection** via `bin/autopilot-drain.py --dry-run` — no NotebookLM calls, no queue mutation. **Anchor validation PASS 1/1, overlap 100%.**
6. **Captions** via `yt-dlp --write-auto-subs`, `en-orig` ×5 and **`vi-orig`** ×1, converted with `bin/vtt-to-md.py`. ⚠️ The anchor's fetch **failed silently on the first attempt** — see [[caveats-and-corrections]] §7.
7. **Verification** in the main loop against `brew.sh`, `docs.brew.sh` (Versions, Support-Tiers, Tap-Trust), the `Homebrew/brew` issue tracker, Wikipedia and `x.com/mxcl`, plus **direct measurement of this machine**, which produced the topic's most important article.
8. **Scorecard tallied mechanically** from the table, after a hand-tally got it wrong.

## The rubric shaped this bundle, and it should be recorded

Two defects in `select_videos()` were visible during selection. Neither was fixed — Rule 3, surgical changes; a rubric change mid-ingest would invalidate the bundle it produced.

### Defect 1 — the recency filter cannot be satisfied on a mature topic

Every candidate query returned only **1–2 of 15** results inside the 6-month window, so the rubric hit its relaxation branch every time:

```
[11:19:23]   only 2 pass recency filter; relaxing
```

Homebrew is 17 years old and its YouTube corpus is evergreen tutorials. The relaxation is doing the right thing — an empty bundle would be worse — but it logs at the same level as everything else, so **a bundle silently mixing 2020 and 2026 material looks identical to a fresh one.** On this topic that produced a source predating Apple silicon by six months.

*It also produced the bundle's best result.* The 2020/2026 pairing is what surfaced the six-year trust arc in [[homebrew-6-security-release]] — `curl | bash` waved through on brand reputation in 2020, versus Homebrew itself refusing to trust third-party code by default in 2026. **Neither source knows about the other, and the contrast only exists because the filter relaxed.** The defect is that this was luck, not design.

### Defect 2 — an unbounded term in the score

```python
eng_ratio = v["view_count"] / v["channel_followers"] if v["channel_followers"] > 0 else 0.5
v["score"] = math.log10(max(1, v["view_count"])) + eng_ratio * 3 + recency_bonus * 2
```

`log10(views)` maxes near 6–7; `recency_bonus * 2` maxes at 2; `eng_ratio * 3` is **unbounded**. Measured on the discarded query `macOS developer environment setup 2026 terminal brew`:

| Video | Views | Score |
|---|---|---|
| Chasang Bhutia, *MacBook Air M2 Programming Setup* | 15,099 | **334.29** |
| Learn AWS with Me | 1,492 | **198.52** |
| Josean Martinez | **1,091,944** | 52.84 |
| Warp | 452,340 | 17.66 |

**The rubric ranks channel smallness above reach, authority and recency combined.** This is the mechanism behind the note already in the `local-llm-coding-hardware-ladder` log that the rubric "ranks engagement, not authority" — the reason Apple's own WWDC session had to be added by hand there. Filed as a background task with a request to report which past picks would have changed.

## Deepen candidates

1. ⭐⭐ **Run the [[this-machine-audit]] migration and write it up.** The audit is diagnosis only. A migration from `/usr/local` (x86_64, Rosetta, 105 formulae) to `/opt/homebrew` (native, 27 formulae), including rebuilding the project venv from a native Python, is a bounded piece of real work with a measurable before/after and a **September 2026 Tier 3 deadline**. It would also finally close the undiagnosed `python3` shim note in the project `CLAUDE.md`.
2. ⭐⭐ **Fail loudly on empty caption fetches.** Assert one transcript file per selected video before compiling. The near-miss in [[caveats-and-corrections]] §7 would have produced a wiki claiming six sources with five.
3. ⭐ **Homebrew's own documentation as a source.** The strongest results in this ingest came from `docs.brew.sh`, not from any video — three of the anchor's critiques are confirmed *verbatim* by it. A docs-first ingest on `Tap-Trust` and `Support-Tiers` would likely beat any video bundle on this subject.
4. ⭐ **Nix on macOS, on its own terms.** Two independent sources here place the Homebrew/Nix boundary at the same line (laptop vs build server) and neither examines Nix. The corpus has no Nix topic.
5. **Rosetta 2's deprecation timeline** — deliberately unverified here ([[caveats-and-corrections]] §9) and directly load-bearing for candidate 1.
6. **`brew bundle` versus real reproducibility.** C1–C2 establish that a `Brewfile` is a shopping list. What teams actually do about that on macOS fleets is an open question this bundle cannot answer.
7. **Kunkka's back catalogue.** One 14-minute video produced a design-history essay whose three central critiques survived verification against vendor documentation. That hit rate warrants checking what else the channel has.

## Cross-links

[[_index]] · [[this-machine-audit]] · [[caveats-and-corrections]] · [[claims-scorecard]] · [[../local-llm-coding-hardware-ladder/_index|local-llm-coding-hardware-ladder]] · [[../deepseek-harness/_index|deepseek-harness]]
