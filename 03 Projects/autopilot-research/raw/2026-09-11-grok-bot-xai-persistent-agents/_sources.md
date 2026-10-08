# Source bundle — Grok Bot (xAI persistent cloud-VM agents)

> **Drained:** 2026-09-11 by `/loop` · path 1 anchored bundle · **yt-dlp captions only, NO NotebookLM**
> **Query:** `Grok Bot xAI` · **Anchor validation:** PASS 1/1, overlap 100% · **Fetch guard:** PASS 6/6
> **Selection:** `bin/autopilot-drain.py --dry-run` (1 anchor force-included + 5 yt-search picks of 15 candidates)
> **Total:** 24,506 words across 6 transcripts, all read in full.

## Why no NotebookLM

The drain script's step 3/5 is a mandatory NotebookLM bundle, but the last six ships in this project all record *"NotebookLM: none (yt-dlp captions read in full — a claims scorecard cannot grade a paraphrase)."* That is a conflict between the tool and current practice; resolved per Rule 7 in favour of the **more recent and better-tested** practice. Captions were fetched directly and the NotebookLM step was skipped deliberately, not by failure. `notebooklm auth check` passes, so this was a choice, not a blocker.

## The six sources

| # | ID | Title | Channel | Views | Published | Lang | Words | Role |
|---|---|---|---|---|---|---|---|---|
| t1 | [`CqhE6qPoEAs`](https://www.youtube.com/watch?v=CqhE6qPoEAs) | Grokbot \| Elon knows how to build product | **Quân IT** | 237 | 2026-09-11 | VN | 4,830 | **OPERATOR ANCHOR** — same-day submission; hands-on install→demo |
| t2 | [`rTMVTkJrals`](https://www.youtube.com/watch?v=rTMVTkJrals) | Grok Bot Just Launched: Features, Uses and First Review | HistoryAI | 23,240 | 2026-09-03 | EN | 3,148 | first review |
| t3 | [`QBmgF1kJSK4`](https://www.youtube.com/watch?v=QBmgF1kJSK4) | 7 Grok Bot agents I use every day | How I AI | 312,210 | 2026-09-02 | EN | 6,534 | **largest reach**; daily-use practitioner |
| t4 | [`01jxZN2ZNsc`](https://www.youtube.com/watch?v=01jxZN2ZNsc) | Grok Bot Just Changed Businesses Forever! (Tutorial) | Eric Nowoslawski | 29,067 | 2026-08-18 | EN | 4,345 | tutorial |
| t5 | [`LM7Ft7g8qJw`](https://www.youtube.com/watch?v=LM7Ft7g8qJw) | Grok Bot Is The First AI Agent You Just Install. Is It Worth $200? | Nate B Jones | 160,996 | 2026-08-14 | EN | 3,841 | **skeptical value analysis**; earliest in bundle |
| t6 | [`bq16MwIAyCE`](https://www.youtube.com/watch?v=bq16MwIAyCE) | Why Grok Bot Is The Most Powerful AI Trading Agent You Can Have Right Now | Alex Carter | 55,381 | 2026-08-23 | EN | 1,808 | ⚠️ **CRYPTO-TRADING FRAME** — see handling note below |

## Anchor notes

**Quân IT is the 3rd topic from this creator** in the corpus, after [[../../wiki/local-llm-coding-hardware-ladder/_index]] and [[../../wiki/quanit-becoming-ai-engineer-2026/_index]].

**The anchor cannot be selected by the rubric.** `MIN_VIEWS = 1000`; the video had **0 views** when the operator submitted it, 192 at pre-flight, 237 at drain time — all far below the floor. It enters only because anchors bypass search ranking. This is the **third** time the corpus has hit this wall (DeepSeek's CloudYeti at 891 views; the hardware ladder's Asad Tinkers at 951) and the clearest case yet: a 0-view video is not a low-quality video, it is a *new* one.

**An `en` caption fetch for the anchor returned HTTP 429.** Not retried, per the block-handling discipline — the `vi-orig` original track is the preferred source anyway, and it downloaded cleanly (239,711 bytes / 20,745 raw words → 4,830 de-duplicated).

## ⚠️ Handling note on t6 (Alex Carter)

The selection guard written into the queue entry fired on this pick — the title says *"AI **Trading** Agent"*, and the channel's other uploads are *"How I Built a **Profitable** Kalshi AI Trading Bot"* and *"**Profitable** Trading Strategy Using OpenClaw AI"*. It was checked before the drain rather than judged by title.

**It is not an impersonation.** It describes the genuine product accurately: *"Grokbot, produced by xAI and Elon Musk, and it's essentially an agent harness. Meaning, it's not just a chatbot, it's a team of always-on agents that have their own computer, tap into any tool or app just like you do, and work 24/7 even when your laptop is closed."*

**But its entire purpose is crypto trading**: *"how you can actually plug it into your crypto trading and investing step-by-step."* Term frequency: crypto ×8, portfolio ×3, invest ×3, token ×1, sponsor ×1.

**Rule for compiling it:** its **product-mechanism** statements are usable evidence. Its **trading, profit and returns claims are not to be relayed, graded as findings, or repeated** — not because they are necessarily false but because this wiki does not carry investment claims. It is kept in the bundle for two reasons: it corroborates the architecture independently, and it is the best available evidence for *why* the operator's anchor reached for the word "blockchain."

## Fetch method

```
yt-dlp --skip-download --write-auto-subs --sub-langs "en-orig,en" --sub-format vtt   # t2-t6
yt-dlp --skip-download --write-auto-subs --sub-langs "vi-orig,vi,en" --sub-format vtt # t1
```

VTT → text by tag-strip + rolling-caption de-duplication (`sed 's/<[^>]*>//g'` → `grep -v` cue lines → `awk '!seen[$0]++'`).

**`bin/vtt-to-md.py` was killed (exit 137) on the 240 KB anchor VTT** and could not be used. Shell fallback produced the transcripts above. That converter does not scale to a ~1-hour auto-caption track — worth a fix, logged as a deepen candidate.

**Per-file guard asserted after fetch** (one transcript per selected video, checked explicitly) — the silent-`--sub-langs`-failure class first logged on the 2026-08-21 Homebrew ship and recurring on the 2026-09-03 Hermes revisit. **PASS 6/6, no recoveries needed.**
