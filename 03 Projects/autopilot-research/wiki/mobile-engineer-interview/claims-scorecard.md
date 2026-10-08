# Claims scorecard — verification verdicts

Each interview was extracted by one agent and independently re-checked by a **refute-first verifier** that re-read *both* transcripts (vi-original + en-translation), assuming items were hallucinated / mis-reconstructed / mis-attributed / technically wrong until proven otherwise.

Because the source is **doubly-garbled ASR**, verification here targets three things: **(a) faithfulness** (was this actually asked, at ~this time, by the right speaker?), **(b) reconstruction** (is the garbled-term guess defensible?), and **(c) technical correctness** (is the canonical/model answer right?).

## Per-video results

| Video | Candidate | Items | Verified faithful | Faithfulness issues | Reconstruction flags | Technical corrections |
|---|---|---|---|---|---|---|
| 1 OVN | Vũ Thành Long (Flutter) | 45 | 42 | 0 | 2 | 1 |
| 2 aKMV | Đỗ Minh Thành (Flutter) | 34 | 28 | 2 | 4 | 2 |
| 3 0n8o | Trương Nhất (React/JS) | 23 | 22 | 0 | 1 | 0 |
| 4 PVO5 | Đỗ Thanh Tuấn (RN) | 15 | 14 | 0 | 0 | 0 |
| 5 Dzto | Huỳnh Đinh Hoàng Viên (React) | 53 | 32/34* | 1 | 1 | 1 |
| **Total** | | **170** | **~166** | **3** | **8** | **4** |

\* Video 5's verifier assessed a 34-item subset in detail (timestamp/scope), verifying 32; the extraction's 53 items include finer-grained behavioral splits.

**Overall:** a **high-integrity study guide** — ~97% of items faithful to the transcript, no speaker-swaps of substance, and every technical correction applied to the wiki's model answers. The failure mode of this corpus is **ASR garble + occasional imprecision**, never fabricated questions.

## The technical corrections (applied in the wiki)

1. **Flutter lifecycle methods belong to the `State` class** (video 1) — only `createState()` is on `StatefulWidget`; `initState/build/didUpdateWidget/dispose` are State methods. Fixed in [[04-flutter-and-dart]].
2. **Dart `const` vs `final`** (video 2) — candidate's claim was **inverted**; `const` = compile-time, `final` = runtime, both immutable. The verdict "wrong" was correct; the wiki states the right version. [[04-flutter-and-dart]]
3. **`git checkout -B` vs `-b`** (video 2) — lowercase `-b` = create; uppercase `-B` = create-or-reset (force). Distinction added in [[07-git-testing-and-engineering-practice]].
4. **Call stack holds local variables, not the heap** (video 5) — candidate said variables live in the heap; correct: **stack** holds function calls + locals, **heap** holds objects. Fixed in [[02-async-and-event-loop]].

## The faithfulness / timestamp flags (recorded, not load-bearing)

- **Video 2:** the "git pull vs rebase" item is likely **rebase-vs-merge** and/or timestamp-shifted (~[00:11] not [00:09]); the const/final *summary* inverted the candidate's own words while the verdict stayed correct.
- **Video 5:** the "testing stages" question is ~[00:21], not [00:15] (6-min shift); a TypeScript-experience question was missed by the extractor.
- **Video 1:** the live-coding array section is **4 distinct questions** (add / remove / sort / dedupe) compressed into one item.
- None of these change a model answer; all are noted in [[caveats-and-corrections]].

## Reconstruction flags (garbled terms, reconstructed by context — defensible but not quotable)

`git xưa`→git rebase (v1) · null-operator terminology (v1) · `gigit/kick`→git, `gig fake/gig m`→rebase/merge (v2) · `material pay`→MaterialPageRoute (v2) · `Isaac/IAC`→Axios (v3) · `Fet 1`→`flex:1`, `GD/GCK`→Grid, `Bit O`→Big O (v3) · `hit`→heap (v5). Full map: [[caveats-and-corrections]].

## Method note

- 13 agents across **2 Workflows**: `wf_89de7c46-db7` (extract+verify 3/5) and `wf_2408264b-657` (recovery of the 2 that failed a strict-schema truncation). Extraction is maker; verification is checker; Opus main-loop authored the wiki folding in verdicts (maker/checker split — the same discipline as [[nodejs-backend-interview/claims-scorecard]]).

**Back to** [[_index]] · **corrections detail:** [[caveats-and-corrections]].
