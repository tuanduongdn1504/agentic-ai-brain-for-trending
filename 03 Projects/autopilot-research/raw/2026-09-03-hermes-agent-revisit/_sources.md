# Source manifest — hermes-agent REVISIT bundle (2026-09-03)

> **This is a REVISIT, not a new topic.** `wiki/hermes-agent/` already exists (built 2026-07-18, 10 articles, 22 graded claims). Per `(C) autopilot-research-routine.md:288` — *"Topic already exists: Phase 3 adds new articles to existing topic folder; updates `_index.md`. No duplicate topic creation."* Corpus topic count stays at **79**.
>
> **Trigger:** operator asked *"Can I start build knowledge from this video with loop or anything in queue now?"* — the **third** time that exact question has opened a ship (`deepseek-harness` 2026-08-18, `homebrew-macos-package-manager` 2026-08-21). Queue was empty (0 pending; the 2026-09-02 23:41 overnight drain exited `Nothing to drain`), nothing running, launchd `com.cvtot.autopilot-research` armed for 23:35.
>
> **Operator elections:** (1) run **now** via `/loop` rather than queue for the 23:35 drain; (2) **FULL 6-source re-drain** — the widest of three offered scopes, chosen over the recommended anchor-only revisit, with the overlap risk stated and accepted.
>
> **Fetch method:** `yt-dlp --cookies-from-browser chrome --skip-download --write-subs --write-auto-subs --sub-langs "en-orig,en,en-US,vi,vi-orig" --sub-format vtt` → `bin/vtt-to-md.py`. Read in full. **NotebookLM: none** (27,703 words EN is direct-read range, matching the 2026-07-18 bundle's ~33.1K decision — a claims scorecard cannot grade a paraphrase).
>
> **Verification:** refute-first workflow `wf_519820ad-57c` — 6 transcript gatherers + 5 primary-source grounders (concurrent) → merge/dedupe in code → 3 perspective-diverse lenses per load-bearing claim (primary-source / framing / time-bound) → 2 completeness critics. Grounders instructed to use `curl` via Bash rather than a summarizing fetch layer, per the `ai-text-watermarking` ship's ⭐⭐ finding that a summarizing layer paraphrased a support page.

## Why this revisit has substance

The prior wiki's numbers have all gone stale. Verified against the GitHub API on 2026-09-03:

| | wiki snapshot 2026-07-18 | now 2026-09-03 | Δ |
|---|---|---|---|
| stars | 216,731 | **240,300** | +23,569 (+10.9%) |
| forks | 40,656 | **49,187** | +8,531 |
| open issues | 23,647 | **38,679** | +15,032 (+63.6%) |
| latest release | v0.18.2 (`v2026.7.7.2`, 2026-07-08) | **v0.21.0** (`v2026.8.31`, 2026-08-31) | 3 minor releases |

The anchor was uploaded **2026-08-26 — five days before v0.21.0** — so it documents roughly v0.20.x.

## YouTube sources (6 ingested)

| # | Slug | Video ID | Channel | Views | Len | Uploaded | Stance / why in bundle |
|---|------|----------|---------|-------|-----|----------|------------------------|
| 1 ⚓ | `t1-holetex-anchor` | [k8lz9P3MrlM](https://www.youtube.com/watch?v=k8lz9P3MrlM) | **holetex** (VN) | 20,222 | 47:34 | 2026-08-26 | **Operator anchor + replication-test subject.** VN no-code "from zero, no coding needed" tutorial — same language, genre and framing as the *prior* bundle's anchor (Phan Dong Giang, *"Dễ Hơn OpenClaw"*), different creator, six weeks later. **Longest source in the bundle.** |
| 2 | `t2-weeb3dev` | [UUcsxd99ER0](https://www.youtube.com/watch?v=UUcsxd99ER0) | weeb3dev | 3,803 | 8:27 | 2026-06-08 | Smallest source (784 words). **Only Linux/Ubuntu-specific source**; Nous Portal + **Hermes Desktop**. |
| 3 | `t3-tonbi-ep1` | [R3YOGfTBcQg](https://www.youtube.com/watch?v=R3YOGfTBcQg) | Tonbi's AI Garage | 80,849 | 28:31 | 2026-05-04 | **Only creator overlap with the prior bundle — different episode.** Prior used **ep.3** (`ZKZLko9kLm4`, memory/plugins/Honcho/Obsidian); this is **ep.1** (installation/setup/basic commands). Complementary; graded for ep.1↔ep.3 contradictions. |
| 4 | `t4-wanderloots` | [GL67DEf2nyI](https://www.youtube.com/watch?v=GL67DEf2nyI) | Wanderloots | 98,250 | 28:50 | 2026-07-01 | **Hermes Desktop**-focused, agentic-workflow lens. |
| 5 | `t5-tina-huang` | [5_N84t1rUU0](https://www.youtube.com/watch?v=5_N84t1rUU0) | **Tina Huang** | **398,873** | 29:40 | 2026-07-20 | **Largest-reach source in the bundle by ~4× and new to the corpus.** Mega-reach sources produced 2 of the 4 prior FALSE claims → superlatives graded hardest. |
| 6 | `t6-codehead` | [8GjyOQy19so](https://www.youtube.com/watch?v=8GjyOQy19so) | CodeHead | 62,346 | 7:47 | 2026-05-14 | Install + use-cases. **Needed a fetch retry** (see caption caveats). |

**Total runtime:** 2h 30m 49s. **Word counts (EN):** t1 7,334 · t2 784 · t3 4,370 · t4 6,968 · t5 6,646 · t6 1,601 = **27,703**. Plus `t1-holetex-anchor.vi.md` (VN original, **12,536 words**) retained for fidelity cross-check of the anchor.

> The VN original runs **1.71× the word count** of its EN auto-translation for identical content — Vietnamese space-separates syllables (*"Trợ Lý"* = 2 words for *"assistant"*). Consistent with the [[../../wiki/wecommit-tokens-and-context-window/_index]] finding on Vietnamese token inflation.

## Overlap audit vs the 2026-07-18 bundle (operator-requested)

The operator elected the full re-drain over a stated overlap risk. **Result: the risk did not materialise.**

Prior bundle IDs: `y96gIckJJ2Q` (Phan Dong Giang) · `QQEgIo4Juxg` (NetworkChuck) · `86Dfgazdu-0` (Tech With Tim) · `LqG1q5NpOBE` (Sean's AI Stories) · `ZKZLko9kLm4` (Tonbi ep.3) · `jIP0q7HEC0g` (Elestio) · `fiCNQyYwnRw` (Plastic Labs) · `Sb96po6S67k` (AI LABS).

- **Video-level overlap: 0 of 6.** No prior source was re-picked.
- **Creator-level overlap: 1 of 6** — Tonbi's AI Garage, ep.1 here vs ep.3 previously. Complementary, not duplicate.
- The specific re-picks predicted as likely (NetworkChuck, Tech With Tim) **did not occur**. Tech With Tim surfaced twice in the search pool (`mTYxpIRK7xA`, `1ve4Atbqmoo`) but neither is the prior bundle's `86Dfgazdu-0` and neither was selected. The query differed (`Hermes Agent Nous Research setup tutorial` vs the prior `Hermes Agent Nous Research`), which appears to be what moved the pool.
- **Three of six sources are Hermes Desktop-focused** (t2, t4, and partly t6) against **zero Desktop coverage in the prior wiki** — the largest apparent gap this revisit closes, pending the `ground:desktop` grounder establishing that Hermes Desktop and "HermesOS" are first-party before anything is written down.

## High-reach candidates the rubric dropped

Surfaced in the top-15 pool, **not** selected — recorded so a later ingest need not re-derive them:

- `9GpWELm3_XI` **CodeHead** "Hermes Agent Explained In 5 Minutes" — **224,435 views**
- `1CLc-VeEivk` **Tina Huang** "My FULL Hermes Agent Setup (**HermesOS**)" — **141,888 views** ⭐ the only source naming "HermesOS"
- `DYdvJCxWd6M` / `CwPUOVUdApE` / `LvWobwr0Neg` **Metics Media** ×3 — 140,334 / 117,001 / 129,686 views; three slots in the top-15, none selected
- `mTYxpIRK7xA` / `1ve4Atbqmoo` **Tech With Tim** ×2 — 126,266 / 93,632 views
- `4sAmpcSOVEw` **Adrian Twarog** — 42,210 views
- `8tpuky8HpXw` **Tonbi's AI Garage** "Better than OpenClaw? Testing Hermes Agent w/ Qwen 3" — 18,072 views; the pool's only **critical-comparison** stance
- `x89MvP6gLaA` **Tonbi's AI Garage** "Masterclass 1 … (**Updated**)" — 8,534 views; an updated cut of the selected t3

## Caption caveats

- **(t1)** The working file is the **EN auto-translation** of a Vietnamese video. Per the discard-as-garble guard, names and numbers are treated as unverified until confirmed against `t1-holetex-anchor.vi.md`; gatherer instructed to name the file each cited value was confirmed in and to mark disagreements garbled rather than picking a side.
- **(t6)** ⚠️ **Silent fetch failure, recovered.** The documented command wrote **0 caption files at rc=0**. Cause: `en-orig` was unavailable for this video (no PO token) and its absence **aborted the entire caption write** — `en` and `vi` both existed and were still lost, behind nothing but a `WARNING`. Recovered with `--sub-langs "en,en-US,vi"`; content is the `en` auto-caption track.
  **This is the 2nd occurrence of the silent `--sub-langs` failure class**, first logged on the 2026-08-21 Homebrew ship (`--sub-langs "en.*,vi.*"` → no file, rc=0). `validate_anchors()` validates *selection*, not *retrieval*. The ⭐⭐ deepen candidate that ship filed — *"assert one transcript file per selected video before compiling"* — was implemented here as a per-slug fetch guard and **caught the failure on its first use**. Guard result: **PASS 6/6 after 1 recovery**.

## Selection note

15 candidates surfaced from `yt-dlp ytsearch15` on `Hermes Agent Nous Research setup tutorial`; the operator anchor `k8lz9P3MrlM` was force-included via the queue `**Anchors:**` mechanism, and yt-search filled the remaining 5 of `SOURCES_PER_TOPIC=6`. Anchor validation **PASS 1/1, overlap 100%**.

⚠️ **`--dry-run` still does not emit video IDs**, so the overlap audit above required re-running the search by hand to resolve them. This is the ⭐⭐ deepen candidate filed by the `ai-text-watermarking` ship (*"make `--dry-run` emit video IDs and let a drain accept an ID list, so a selection can be replayed rather than re-rolled"*) — **still open, and it cost a round trip here.** Until it lands, no bundle in this corpus is replayable.

⚠️ **Queue format doc/code mismatch found.** The `topics-queue.md` header documents `**Query:** the search string handed to yt-search`, but `parse_queue()` at `bin/autopilot-drain.py:102` requires the query to be **inside backticks** (`\*\*Query:\*\*\s*` + backtick group) and the block regex at line 97 requires a **blank line after the `## ` heading**. A correctly-documented entry parses as `skip (no Query in block)` and the drain reports `Pending topics: 0` — i.e. **a silently ignored topic**. Cost one round trip; entry patched to satisfy the code, not the doc.
