# (C) Autopilot Loop — 2026-08-21-13 · ai-text-watermarking

> **Trigger:** `/loop` (manual, operator-initiated)
> **Topic:** AI text watermarking — Anthropic's invisible mark on Claude output (EU AI Act Article 50) · corpus **#79**
> **Started:** 2026-08-21 ~12:50 ICT
> **Ended:** 2026-08-21 ~14:0x ICT
> **Mode:** Path A selection (`bin/autopilot-drain.py --dry-run`) + Workflow verification + main-loop direct-write compile

## Trigger context

Operator submitted `https://www.youtube.com/watch?v=5R9Nw8eKDCA` and asked whether anything in the queue blocked
shipping it, or whether it should wait for something already queued — **the third consecutive ship opened by that
exact question** (`deepseek-harness`, `homebrew-macos-package-manager`, this one).

Pre-flight answer: **nothing blocked it.**

| Check | Result |
|---|---|
| `raw/topics-queue.md` pending topics (`--list-only`) | **0** |
| Running drain / `yt-dlp` / `notebooklm` processes | none |
| `CronList` / `list_scheduled_tasks` | no jobs, no scheduled tasks |
| `crontab -l` | no crontab |
| launchd `com.cvtot.autopilot-research` | loaded, fires **23:35** daily |
| Corpus size | **78 topics** |
| Existing watermark / C2PA coverage | **zero across all 78 topics** |

Dependency gate (routine Phase 0.3): `yt-dlp` ✅ · venv Python `3.12` ✅ · `notebooklm-py 0.3.4` ✅ (present,
deliberately unused).

## Operator decision

One question was put before any work started, because the anchor is a **14-item news roundup** with four plausible
query axes and picking the wrong one wastes the yt-search bundle. Options offered: watermark-anchored topic + bundle
(recommended) / weekly snapshot from the single source, following the `ai-news-2026-w19` precedent / both / queue for
the 23:35 drain.

**Operator elected: watermark topic + bundle.** Correct call — the watermark axis was the only one with a primary
document behind every claim.

Concerns stated **before** asking, not after: the anchor is a **1,683-view dubbed news roundup**, the thinnest anchor
in the corpus, and a roundup is structurally shallow (~14 items in 14 minutes). Both stated plainly; the operator
elected the full bundle anyway.

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 6 | 1 (topic absent) | 0 | **1.0** |

**Stop reason:** `gaps_closed_ratio` (1.0) ≥ target 0.5 after one cycle. Single cycle, no loop-back.

**Honest accounting of the metric:** the formula scores the topic-level gap, which one cycle closes by construction.
It does not capture that the cycle also **opened 9 explicitly named unresolved items**
(`caveats-and-corrections.md` §1) and **8 deepen candidates**. As at #78: the ratio is 1.0 and simultaneously
understates the remaining work. Recorded, not smoothed.

## Sources ingested

`bin/autopilot-drain.py --dry-run`, query `Anthropic Claude watermark AI generated text`, 1 declared anchor.
**Anchor validation PASS 1/1, overlap 100%.** Query chosen after probing 3 candidates by importing
`yt_search()`/`select_videos()` directly — no queue writes, no log spam.

1. **[ANCHOR]** `5R9Nw8eKDCA` — BizMate AI Official, VN-**dubbed**, 2026-08-19, 14:47, 1,683 views
2. `3FhxdhVMJoU` — **Squintist**, 2026-08-13, 15:00, 176,578 — **strongest source in the bundle**
3. `KUeW3zzF49A` — Caleb Ulku, 2026-08-14, 10:37, 133,195
4. `FnAqruxx-QE` — **Code Bear**, 2026-08-15, 12:15, 132,023 — REPEAT channel (`deepseek-harness`)
5. `vcBevA3skXU` — BetterWay, 2026-08-17, 8:11, 7,689 — **smallest reach, deepest security content**
6. `rR2QW5WQ3aE` — **Kyle Balmer / AI with Kyle**, 2026-08-12, 19:57, 52,073 — the corrective

88,712 bytes / 2,193 cue lines, all read in full. **No NotebookLM.**

## Wiki articles created

- `raw/2026-08-21-ai-text-watermarking-claude-eu-ai-act.md` (NEW)
- `wiki/ai-text-watermarking/` — **13 files, NEW**: `_index` · `what-anthropic-actually-said` ·
  `how-the-watermark-works` · `the-eu-ai-act-chain` · `what-it-does-not-prove` · `attacks-and-robustness` ·
  `detectors-are-not-watermarks` · `the-seo-panic` · `the-anchor-audit` · `consequences-for-this-vault` ·
  `claims-scorecard` · `caveats-and-corrections` · `source-provenance`
- `wiki/_master-index.md` (UPDATED — topic #79 prepended)
- `raw/_inventory.md` (UPDATED — in-flight `raw` row inserted at Phase 0, updated to `compiled` at Phase 7)
- `raw/topics-queue.md` (UPDATED — moved to Completed; queue verified back to `Pending topics: 0`)

**70 wikilinks filesystem-validated, 0 broken. 0 broken relative markdown links.**

**Scorecard: 101 claims — 76 CONFIRMED / 8 UNVERIFIED / 6 CBI / 3 CORRECTED / 2 MISLEADING / 2 FALSE /
2 UNFALSIFIABLE / 1 TIME-BOUND / 1 CONTRADICTED-IN-BUNDLE / 0 FABRICATED.** Largest scorecard and highest
confirmation rate in the corpus; **tallied programmatically** (101 rows, 101 unique IDs, 0 duplicates) per the
`deepseek-harness` rule.

## Verification

**Workflow `wf_89d8a73f-4de`** — 11 agents, 3 phases, **749,523 tokens / 218 tool calls / 0 errors / 0 empty /
0 skipped**, ~11 min: 6 per-transcript digests → 4 grounding lenses (Anthropic primary · EU AI Act · watermarking
literature · adversarial refuter) → 1 completeness critic. 148 deduped claims, 90 load-bearing.

**Plus 7 main-loop primary fetches, which overturned 4 lens verdicts.**

## Findings

**1. The anchor is right about the fact and wrong about the frame.** Anthropic really does watermark Claude's text
output, and it really does persist when Claude only proofreads/translates/summarizes. But *"tất cả các mô hình của
họ"* (all their models) is **CORRECTED** — Anthropic's page says *models launched on or after 2026-08-02*, with
earlier models due by 2026-12-02. *"whether Claude is the author"* is **MISLEADING** — Anthropic's own words are
*"may have been **processed** by Claude."* And the video **never says "EU", "AI Act" or "law"** once, presenting a
measure taken under a code signed by ~190 organizations as covert surveillance. The bundle's largest-reach video is
20 minutes of debunking exactly that framing.

**2. The watermark and the operator's own product ADR come from the same statute.** The mark exists because of **EU AI
Act Article 50(2)**; `hireui`'s ratified candidate-LLM legibility ADR exists because of the EU AI Act. Read together:
**50(2) binds providers, 50(4) binds deployers** — a vendor's mark discharges none of the deployer's duty. Four of the
ADR's five requirements survive contact; **"eval-gated" breaks**, because Anthropic's detector does not exist publicly
and **no false-positive rate has been published by anyone.**

**3. The anchor's *other* story is a confirmed real-world BOLA.** A Melbourne man's **Claude-powered OpenClaw agent**
probed a gym booking API and reported *"zero authorization checks on cancelling other people's reservations … I tested
this with the person in waitlist position #1, and it actually went through"*, then deleted a stranger's booking and
could not undo it. Confirmed across eight outlets. That is the exact class `api-security-7-techniques` names as this
operator's **#1 unmitigated risk**, and the discovery mechanism was **a helpful agent, not an attacker.**

**4. 🔴 An expiring item was surfaced by the discard-as-garble guard.** The roundup's quick-news tail says Manus users
must back up data *"before the end of this month"*. Real — and **the deadline is 07:59 SGT on 2026-08-23**, two days
after this compile. The anchor is wrong **in the direction that loses data.** One search, per the guard's rule 1 for
date-sensitive claims in a mangled transcript ("Matis" → Manus).

**5. ⚠️ Six verification-process failures — in the verifier, not the sources.** Full detail in
`caveats-and-corrections.md` §2:
(a) **two lenses returned CONFIRMED on the anchor's one material error** — including the adversarial lens whose entire
brief was to refute; one fetch of `support.claude.com` settled it;
(b) the completeness critic asserted *"No head-on verdict disagreements detected"* — **false**, there were three;
(c) two lenses graded a 2026-08-13 source against 2026-08-14 facts (anachronism) — correct verdict TIME-BOUND;
(d) one lens searched **only arXiv** and returned UNVERIFIED for four non-arXiv facts that a sibling confirmed from
Gizmodo / The Markup / AI Weekly / Nature;
(e) one lens generalized its own fetch failure into *"anthropic.com uses React-rendered dynamic content"* and graded
Anthropic's policy from TechCrunch, **while two siblings fetched `anthropic.com/news/claude-text-watermark` fine**;
(f) one lens abandoned the *Nature* figures at the paywall when an **open-access PMC mirror** yields all three
verbatim — a violation of the project's own block-handling discipline (*a block means change technique, not give up*).
**"0 agent errors" means nothing crashed. It does not mean the verdicts were right.**
**Rule for next time: when a claim concerns the subject's own published policy, the main loop fetches the primary
source itself.** One call, four verdicts overturned.

**6. ⚠️ The source bundle is not reproducible — and the guard caught it.** Three selection runs on the same query
minutes apart: two produced the logged bundle, one substituted a different video into a slot. `--dry-run` **records** a
bundle, it does not **lock** one. Caught only because the fetch script asserted resolved titles against the titles the
dry-run had logged; the dry-run's bundle was then honoured by resolving its titles to URLs explicitly. **Filed, not
fixed** (Rule 3): `--dry-run` should emit video IDs and a drain should accept an ID list.

**7. The #78 deepen candidate was implemented and passed.** *"Assert one transcript file per selected video before
compiling"* → `GUARD: PASS — 6/6 videos have a transcript >=2KB`. The anchor again needed **`vi-orig` named
explicitly** (no manual subs, ~190 machine translations); the #78 lesson held on its first re-test.

**8. Depth was inversely correlated with reach.** The bundle's best security content — spoofing, watermark-stealing,
radioactivity — came from the **smallest** channel (7,689 views). The rubric ranks engagement and has no notion of
depth. The unbounded `eng_ratio * 3` defect from #78 also resurfaced: score **313.39** for one pick against **49.58**
for a video with 3.5× the views. Recorded, unfixed.

## Rule compliance

- **Rule 6 (token budget) — BREACHED, surfaced not hidden.** A 6-source wiki ship plus an 11-agent verification
  workflow (749K subagent tokens) exceeds the 4,000/task and 30,000/session budgets by orders of magnitude, as every
  prior ship in this corpus has. The operator elected the full bundle after the thin-anchor concern was stated.
  Flagging rather than silently overrunning.
- **Rule 3 (surgical changes)** — three known defects in `bin/autopilot-drain.py` (unbounded engagement term,
  unsatisfiable recency filter, no ID-based replay) left **unfixed**; filed here instead. Changing selection
  mid-ingest would invalidate the bundle it produced. The fetch guard was added to the *ingest script*, not to the
  drain tool, so selection behaviour is untouched.
- **Rule 7 (surface conflicts)** — A09 vs C16 (does marking degrade quality?) is stated as an unresolved
  contradiction rather than averaged. The three lens disagreements are named with both sides.
- **Rule 12 (fail loud)** — the six verification failures, the bundle non-reproducibility, the nine unresolved items,
  the 12 unverified roundup items, the `WebFetch`-summarization caveat on Anthropic's quotes, and the fact that this
  wiki is itself watermarked Claude output are all recorded in the wiki, not papered over.
- **Constitutional #1 (scope)** — all writes inside `03 Projects/autopilot-research/`. Storm Bear root files, the
  hireui repo, and `05 Skills/` were read-only or untouched.
- **Constitutional #4 (never fabricate)** — 0 FABRICATED across 101 claims; 8 UNVERIFIED left standing as gaps.
- **Constitutional #6 (no recursion)** — no `ScheduleWakeup`, no self-trigger.
- **Block-handling discipline** — one block hit (`nature.com` 303 → auth wall). **Technique changed, not retried**:
  open-access PMC mirror, which yielded all three figures. One further redirect (`ncbi.nlm.nih.gov` → `pmc.ncbi`)
  followed once, as instructed by the tool.

## Note on a mislabeled sibling log

`bin/autopilot-drain.py --dry-run` again emitted `loop-log/(C) 2026-08-21-13-autopilot-overnight.md` with the header
*"Trigger: unattended (launchd UserAgent)"*. Cosmetically wrong — this was an operator-initiated `/loop`.
`flush_loop_log()` hardcodes the unattended header regardless of invocation path. Same as #78; still not worth a code
change on its own, still worth knowing when reading logs.

## Suggested next action

**Two things, in this order.**

1. **🔴 Today: decide the Manus question.** If any data lives in Manus, the backup deadline is **07:59 SGT / 19:59 EDT
   on 2026-08-23** — inside 48 hours of this log. This is the only item in the ship with an external clock.
2. **Then: run the BOLA audit on `hireui`.** The Melbourne gym incident converts `api-security-7-techniques`' #1
   flagged risk from a theoretical finding into a dated public precedent with a verbatim agent transcript, where the
   exploiting party was an ordinary user's helpful agent. Start with the endpoints that mutate or delete another
   tenant's objects and ask the one question the gym's API could not answer: **does this endpoint check that the
   caller owns the object?**

The topic's own top deepen candidate is different and worth queueing separately: **non-English watermark and detector
performance.** Every robustness number in this topic is English, the anchor is Vietnamese, and `hireui` screens
non-native-English candidates — the population that style detectors flag at **61%**.
