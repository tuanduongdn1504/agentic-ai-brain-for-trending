# (C) Verdict — v249 `pathwaycom/arc-task-gen`

**Date:** 2026-08-19 · **Routine:** LLM Wiki Routine **v2.7** (§31 tiering · §40 operator-direction GA · §41 (a)-solid-signal)

---

## Phase 0.9 — STRICT criteria

| Criterion | Call | Reasoning |
|---|---|---|
| **(a)** author is Anthropic / a registered (a)-7 vendor-direct source | **FAIL** | Ludovic Arnould, Pathway (`ludovic@pathway.com`), sole author of all 12 commits. Not Anthropic, not a registered vendor-direct axis. Per **§41** no name / notability / locale inference rescues it. Pathway is an independent company; Łukasz Kaiser is among its investors/advisors, which is not an (a) signal either. |
| **(b)** goal-relevance | **MODERATE — keys the tier** ⚠️ *STRONG arguable, flagged reviewable* | **FOR:** the operator holds a **RATIFIED ADR** requiring every hireui LLM path touching a candidate to be **eval-gated**, and hireui has no eval set and cannot freely use real candidate data. This repo is a worked, readable example of *build a synthetic evaluation set whose measured distribution matches your real one, and guarantee in code that the generator never saw the answers* — the exact problem the ADR creates. **AGAINST:** it is eval-**data-generation** for a rival lab's reasoning model, produces ARC puzzles, and ships no agent-facing surface at all (no MCP, no skill, no `AGENTS.md`). It is not Claude/coding-agent substrate. **MODERATE is the honest call**; STRONG is defensible on the ADR link alone. |
| **(c)** technical solidity | **STRONG** ⚠️ *tempered* | 2,139 lines of clean, well-reasoned Python; a code-enforced contamination firewall; thresholds calibrated against the reference set's own internal structure; nine comments recording defects and rejected alternatives; every checkable number reproduces exactly on independent recomputation. **Tempered by:** zero tests, one dead counter in the audit trail (`eval_similar_replaced`), a misattributed confirmatory taxonomy, and the tool's central quality guarantee being prose addressed to a language model. |
| **(d)** pattern coupling / ecosystem | **STRONG** | Strong **#83** (a named Caveats section + a pre-registered invalidity guard + two flag messages naming their own defects). **#84 84c** provider-agnostic. Sits on the corpus's live eval/benchmark axis opened by **v233 ClawWork**, and on the code-gate-vs-prose axis of **v247/v248** — carrying **both** sides of it in one file. Replicates **v246**'s `silent` detector (4th repo) with a refinement, and supplies one **v240** inventory-rule instance. |

### Tier

> ## GOAL-ALIGNED INCLUDE 3/4 — [(a) FAIL · (b) MODERATE keys the tier · (c) STRONG · (d) STRONG]

Per **v2.7 §40** (operator-requested, touches a live goal thread, (b) MODERATE+): GOAL-ALIGNED per operator direction, **no override consumed, no §35 pressure.**

⚠️ **OFF-GOAL CAPTURE recorded as the reviewable alternative** — the defensible reading is that a benchmark-dataset generator for another lab's model is off both goals and belongs in the corpus-knowledge-outlier track. It loses because the eval-gating requirement is *ratified vault policy*, not a passing interest.

---

## Mint decision

> ## NO MINT — counts **46 / 11 UNCHANGED**; §C live standalones **51 unchanged**; surface ≈58 unchanged; max pattern **#85**; **no N-bumps taken**

**Five independent grounds:**

1. **Decisive external prior art.** **ARC-GEN** (Google, Apache-2.0, arXiv:2511.00162) is an explicitly **"mimetic"** ARC generator preserving grid size, colour distribution and pair counts — distribution-matched ARC task generation, published by Google, and **named in BDH-CQ's own training mixture**. Plus **BARC/ARC-Heavy** (LLM-generated, ~400k), **RE-ARC** (400 procedural generators), **ARC-TGI** (461 generators, incl. 15 ARC-AGI-1 test tasks). The **v240** / **v242** decisive-prior-art discipline.
2. **Technique-not-capability.** "Synthetic benchmark-twin generation" is a method. The **v211 PixelRAG** rule: corpus-first-for-a-technique is not a mintable §C class.
3. **Research artifact, not a capability layer.** A 2,139-line appendix to a paper, with no agent-facing surface. The **v211** research-system-not-tool line; contrast the mint-at-N=1 capability precedents (v183 / v194 / v206 / v215 / v244), every one of which an agent reaches *through*.
4. **§28** anti-inflation at ~51 live standalones.
5. **Not the exemplar.** ARC-GEN is Google's, larger, and Apache-2.0.

**NOT an N=2 of the v233 ClawWork row.** That row is an economic-survival **benchmark harness** (agents solve, are paid, go bankrupt). This is a **dataset generator** emitting `tasks.json`. Different object, no N-bump.

⚠️ **NO-MINT ALTERNATIVE RECORDED — operator/audit-reviewable, NOT self-executed:** *"LLM-Generated Distribution-Matched Private Benchmark Twin for Contamination Control"* (N=1), defensible only on the narrow conjunction of joint-slot covariance sampling + a **code-enforced** eval-content firewall. Loses on all five grounds; minting it would be drawing the circle to fit the subject inside (**camofox v179**).

**NEW DEFERRED WATCH AXIS (recorded, not minted):** *"benchmark-contamination tooling — generate-a-private-twin as an evaluation-integrity practice."* N=1. The corpus's first subject whose object is *the trustworthiness of a number* rather than a capability.

---

## Streak / governance

| Field | Value |
|---|---|
| Streak | **v248 `GA:106` → `GA:107 · OG:13 [7 ov]`** |
| Consecutive GA | **30** (v220 → v249) |
| §35 off-goal ceiling | **CLEAR** — window {v247 GA, v248 GA, v249 GA} = 0 OG |
| Overrides | **0** consumed (v153 → v249 = zero); lifetime 10, 3 `[ceiling-override]` (v146/v148/v152) |
| Pattern counts | **46 confirmed / 11 CONFIRMED Library-vocab** — UNCHANGED |
| ⚠️ Audit debt | the **~v221 audit is now 37 SHIPS OVERDUE** (last v212). v249 adds: the new watch axis, the recorded NO-MINT alternative, and a fourth `silent`-detector datapoint. |

---

## The three findings, ranked

**⭐⭐⭐ 1. The contamination it exists to defeat is worse than it says, and it is one `ls` away.** ARC-AGI-2's public **training** set republishes **375 of ARC-AGI-1's 400 evaluation tasks** — same grids, same colours, **under their original task ids** — with the demonstration pairs shuffled, which defeats byte and JSON hashing while leaving filenames intact. I verified it at six levels with three controls: 376 shared ids, 375 identical pair multisets, **0 byte-identical**, **all 375 reordered-only**, all at the same id; ARC-AGI-2 eval → ARC-AGI-2 train = **0/120**. D₄ and colour permutation contribute **zero** additional matches, so the open issue that raised this is right about the number and wrong about the mechanism. And the paper's own training mixture names **ARC-GEN100K**, whose generator suite covers **328 of those same 400 eval tasks** — with **no overlap analysis anywhere in the paper**.

**⭐⭐⭐ 2. The honest number exists, it is HIGHER, and it is in Appendix A.** Table 6: public ARC-AGI-1 **29.5%** (118/400) · calibrated generated **37.2%** (149/400) · mechanic-stratified generated **29.8%** (337/1,131). The tool worked, it was run at scale, and the cohort with clean provenance scored **7.7 points better** — the direction *inconsistent* with memorisation inflating the public figure. That number is in an appendix; the contaminated one is in the abstract, the README, the chart and the press release. Defensible (only the public number is leaderboard-comparable) and costly (their own best evidence is invisible). ⚠️ It proves nothing on its own — **nothing in this tool measures difficulty** — and the authors correctly decline the inference.

**⭐⭐ 3. "Independent Reproduction" holds for none of the three named people.** `README.md:54` heads the section; `:56` credits **Łukasz Kaiser**, whom Pathway's own blog lists among its **investors and advisors**; `:58` says the results were *"also independently reproduced by"* **Remigiusz Kinas** and **Richard Zhong**, who are **authors 8 and 9 of the paper**. Commit `b1ff64c` **added the word "independently"** in the same edit that added a co-author — and **Pathway's own blog never uses the word at all.** The claim is stronger in the repository than in the press release.

**What a README-only reader misses:** all three.

---

## Pilot line

> ## 🔴 READ-AND-BORROW — do NOT run it

It costs real money (~760 frontier-model calls for a 400-task set), and its output is ARC puzzles, which hireui has no use for. **The method is the asset; the tool is not.** Risk of running it is genuinely low (no server, no port, no CORS, no `exec` on model output, egress to exactly two hosts, writes confined to `data/`) — the reason not to run it is that there is nothing to gain, not that it is dangerous.

⭐ **Rung 1 (2–3 h, zero install, zero spend) — do this one:** read `generate_tasks.py:641-643` + `_build_avoid()` and `label_eval_tasks.py:211-216`, then write `hireui/evals/METHOD.md` fixing three rules in hireui's own words: **(i)** the eval-similarity filter may delete a synthetic case but may never appear in the prompt that generates one; **(ii)** before collecting anything, state the condition under which the measurement axis is invalid, and make the collector print it; **(iii)** a synthetic eval case is never training, fine-tuning or prompt-engineering input, enforced by a gitignore + a pre-commit check, with the reason written in the file. Full ladder in `(C) Pilot Methods Menu.md`.

**Never:** point the profile sampler at real CV *content* (metadata axes only); use synthetic eval cases for SFT/DPO/prompt engineering; publish them; skip the blind hand-check of 20; or cite this repo's benchmark numbers as verified — **the 29.5% is self-reported, is on a set two of the paper's own named sources reach, and the $0.0007 is a self-hosted compute estimate at an assumed $3/H200-GPU-hour compared against competitors' retail API prices.**

---

## Suggested next action

Review + merge **`wiki/v249-arc-task-gen`** (the chain v204 → … → v248 → v249 merges in order), then **do Rung 1** — and make **v250 the badly overdue audit** rather than another wiki.
