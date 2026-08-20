# (C) Autopilot Loop — 2026-08-20-13

> **Trigger:** `/loop` (interactive, operator-initiated)
> **Topic:** Local LLM coding on Apple Silicon — the 64 GB Mac mini M4 middle of the hardware ladder
> **Operator ask:** *"Can I start build knowledge from this video https://www.youtube.com/watch?v=GBf_mKxGqtk with loop or anything in queue now?"* → operator elected **anchored 6-video bundle** (deepseek-harness shape)
> **Result:** NEW topic #77 `local-llm-coding-hardware-ladder` — 11 files, 123 wikilinks, 0 broken

## Pre-flight

| Check | State |
|---|---|
| `raw/topics-queue.md` | 0 pending |
| `mcp__scheduled-tasks` | none |
| `CronList` / system crontab | none / no crontab |
| Running processes | no drain, no loop, no overnight orchestrator |

**Lane was clear.** Last activity: `deepseek-harness` ship earlier the same day.

## Sources

7 videos, **27,896 words / 329 timestamped paragraphs**, all read in full in the main loop. **No NotebookLM.**

1. **[ANCHOR]** `GBf_mKxGqtk` Quân IT — 64 GB Mac mini, VN, 48:34, 1,755 views
2. `HjA7_QUGQls` WEBdoze — 24 GB M4 Pro
3. `zPqcS5AvQvQ` ForrestKnight — real Excalidraw + Warp (AMD-sponsored)
4. `JpJaEPGzPF4` Samuel Gregory — 128 GB M5 Max, OMLX
5. `3zSANOIBHYw` Zen van Riel — RTX 5090
6. `hfba9dAT6xE` Tech With Tim — 64 GB M5 Max
7. **`wykPErJ8M-8` Apple WWDC26 session 232** — *main-loop addition, not a rubric pick*

## ⚠️ Tooling bug found and fixed — `bin/autopilot-drain.py`

The first `--dry-run` **failed anchor validation 0/1** and logged *"anchor unreachable"*. The URL was fine.

**Cause:** the `yt-dlp --print` template used `|` as its field delimiter. The anchor's title — *"…64GB ram **|** quanIT"* — split into 9 fields where `yt_meta()` required exactly 8, so it returned `None`. The same `len(parts) != 8: continue` in `yt_search()` was **silently discarding every pipe-titled video from the candidate pool**.

**Measured impact on this run:**

| | Before fix | After fix |
|---|---|---|
| Anchor | ✗ dropped | ✓ PASS 1/1, 100% |
| Recency filter | *"only 5 pass; relaxing"* | no relaxation |
| Bundle dates | **3 of 6 from 2025** | **all 6 from 2026** |

**Fix:** delimiter → `|@@|` in both functions; the silent `continue` now counts and emits a `WARN`; *"anchor unreachable"* → *"anchor probe returned no usable metadata"*. Backup: `/tmp/autopilot-drain.py.bak`. Live re-confirmation: source #7's title also contains a pipe and parsed correctly.

**This bug predates this ingest and has been narrowing source selection for the corpus's entire history.**

## Verification

**Workflow `wf_9dd08c75-e02`** — 24 agents (6 grouped verifiers → 17 refute-first adversarial passes → 1 completeness critic). **1,409,555 tokens · 387 tool calls · 336 s · 0 errors / 0 empty / 0 skipped.**

**Plus 7 main-loop Opus checks**, which produced 3 load-bearing facts the agents missed or got wrong:
- **Qwen3.6-27B exists** (agent asserted it didn't) — 2026-04-22, Apache-2.0
- **Warp open-sourced the client only** — AGPL-3.0, Oz proprietary
- **Base M4 caps at 32 GB** ⇒ the anchor's 64 GB mini is an **M4 Pro at 273 GB/s**

**Scorecard: 12 CONFIRMED · 5 CBI · 1 FALSE · 3 UNRESOLVED · 0 FABRICATED.**

### ⚠️ Two verification-agent errors caught

Both the same failure — **model-inventory knowledge lagging reality by ~a year, stated confidently**:
1. *"No Qwen3.6 model exists"* — false, and it would have contradicted this corpus's own `local-ai-coding-agents/qwen3.6-27b` article. Caught in the main loop.
2. *"Qwen3.5 does not exist"* — overturned by the workflow's **own refuter** against the official model card (*"262,144 natively and extensible up to 1,010,000 tokens"*). The refute-first stage paid for itself.

Model-existence claims from agents are now **low-trust by default** in this project.

## Findings

**Headline:** memory capacity is the wrong axis. Agentic coding is **prefill-dominated** — Apple, first-party: *"agentic sessions usually comprise hundreds of thousands of tokens, and most of those are not generated."* Binding constraints are **bandwidth** and **repository size**.

**The corpus claim is refuted.** `local-ai-coding-agents` published *"≥24 GB is a practical minimum"*; a 24 GB M4 Pro stalled and died on a small static site running a 4 B 4-bit model.

**The purchase-deciding fact:** every positive "good enough" verdict in the bundle sits on toy/greenfield work. **Both sources that tested real production repos returned negative verdicts.** Even Apple demos a blank Xcode project.

## Method lesson recorded

**An engagement-ranked rubric has no notion of authority.** Apple's own WWDC session on this exact subject (493 K views) never won a slot, yet became the best-sourced article in the topic. **On any topic with a first-party owner, check for the vendor's own material before compiling — the rubric will not.**

## Files written

- `raw/2026-08-20-local-llm-coding-apple-silicon-hardware-ladder.md`
- `wiki/local-llm-coding-hardware-ladder/` — 11 files (`_index`, `the-hardware-ladder`, `why-agentic-differs-from-chat`, `apple-mlx-stack`, `anchor-quanit-64gb`, `the-tooling-layer`, `quality-ceiling-and-failure-modes`, `corpus-correction`, `claims-scorecard`, `caveats-and-corrections`, `source-provenance`)
- `wiki/_master-index.md` — UPDATED (76 → **77** topics)
- `raw/_inventory.md` — row added, Status `compiled`
- `raw/topics-queue.md` — moved to Completed
- `bin/autopilot-drain.py` — **bug fix**

**No files in `wiki/local-ai-coding-agents/` were edited.** Recommended corrections are listed in `corpus-correction.md` for the operator to approve — per the vault rule *"ask before editing existing notes."*

## Metric

- `gaps_at_start` = 1 (topic did not exist) · `gaps_at_end` = 0 · **`gaps_closed_ratio` = 1.0**
- Stop reason: target ratio reached, single cycle
- Queue: 1 pending → **0 pending**

## Suggested next action

**Approve the four `local-ai-coding-agents` edits** listed in `wiki/local-llm-coding-hardware-ladder/corpus-correction.md` — the stale *"≥24 GB practical minimum"* line is the one a reader will act on.

Then, highest-value follow-up: **an M5-generation agentic test against a real repository.** Apple claims 4× matmul on M5 aimed squarely at the prefill bottleneck, and **nobody in this bundle has measured it on a large codebase** — it is the one question that would change the buying advice.
