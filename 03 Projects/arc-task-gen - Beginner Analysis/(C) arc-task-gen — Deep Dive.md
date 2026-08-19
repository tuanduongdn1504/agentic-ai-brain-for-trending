# (C) arc-task-gen — Deep Dive

**Subject:** `pathwaycom/arc-task-gen` — *"ARC-AGI-1 Task Generator: Distribution-Matched Tasks for Model Evaluation"*
**Wiki:** v249 · **Date:** 2026-08-19 · **Author of this doc:** Claude (`(C)` prefix per CLAUDE.md)
**Verdict:** GOAL-ALIGNED INCLUDE 3/4 · **NO MINT** · counts 46/11 UNCHANGED

---

## 0. Clone facts (source-cloned TWICE, byte-identical)

| Fact | Value |
|---|---|
| HEAD | `20b2203064b09f60f7925a191d75c11d72277f35` (2026-08-11 11:52:10 +0200) |
| Second clone | byte-identical (`diff -r --exclude=.git` → 0 differences) |
| Tracked files | **13** |
| Total lines | **2,139** (`generate_tasks.py` 905 · `generate_tasks_stratified.py` 508 · `label_eval_tasks.py` 238 · `describe_eval_tasks.py` 131 · `visualize_tasks.py` 108 · `instructions.md` 177 · `README.md` 58 · `pixi.toml` 14) |
| Commits | **12** on `HEAD` and on `--all` (identical) |
| Git roots | **TWO** — `1a90ea7` and `841753d`, both 2026-08-04 (D19 EXTENDED: count the roots) |
| Authors | one person: Ludovic Arnould / `ludovicPathway` `<ludovic@pathway.com>` (9 + 2 + 1) |
| Licence | MIT, "Copyright (c) 2026 Pathway" |
| Deps | `pixi` / conda-forge: python ≥3.12, numpy, httpx, openai, matplotlib. Lockfile 79.7 KB. |
| Page-stated (§37.4, **NOT** API-verified) | 3.6k★ · 21 forks · **1 watcher** · 1 open issue · 0 PRs |

**Timeline.** Code landed 2026-08-04. On **2026-08-10** commit `29dcd16` **renamed the technical `README.md` to `instructions.md`** and `68bb4e3` created a **new paper-promotion `README.md`** in front of it. On 2026-08-11 the paper link, the chart and the final wording landed. The accompanying paper (arXiv:2608.09888) was submitted **2026-08-10**. This is a launch artifact for a paper and a press release.

---

## 1. What it does

It asks a frontier chat model (default `gpt-5.6`, any OpenAI-compatible endpoint) to **invent** ARC-AGI-1-style puzzles, one per API call, so you can score a model on tasks it cannot have memorised.

Each call receives a **slot** — `{rows, cols, colors, n_train, n_test, anchor}` — copied **wholesale off one randomly chosen real ARC-AGI-1 evaluation task** rather than sampled per-axis, because (`generate_tasks.py:145-152`) *"Sampling these marginally and independently would produce incoherent combinations — e.g. a 2x2 grid asked to carry 9 distinct colours."* Then a convergence loop runs three filters and regenerates what they remove:

1. **intra-set dedup** — the model writes a one-sentence rule description per task; descriptions are embedded and any pair at cosine ≥ `DEDUP_THRESHOLD` 0.80 is collapsed (`:214`);
2. **eval-similarity** — generated descriptions compared against descriptions of the *real* eval tasks; anything ≥ `EVAL_SIMILARITY_THRESHOLD` 0.92 is removed (`:250`);
3. **structural validation** — rectangular grids, cells 0–9, ≥2 train pairs (`:293`).

Removed tasks are regenerated with their **slot recycled** and an **avoid list** of every rule description generated so far, kept or discarded.

`generate_tasks_stratified.py` monkey-patches two seams of that loop (`base.sample_joint_slots`, `base.generate_one`) to condition each task on one anchor's full shape sequence + an LLM-assigned category, optionally **allocating tasks evenly across 16 transformation mechanics** rather than following the eval set's own skewed distribution.

---

## 2. ⭐⭐⭐ THE HEADLINE — the contamination it exists to defeat is worse than it says, and I measured it

The repo's premise (`instructions.md:5-9`) is that *"The public ARC-AGI-1 evaluation set appears in web-scraped training corpora, so a model's score on it is an upper bound on genuine few-shot rule induction."* That is a diffuse claim about the open web. **There is a far more concrete channel, and neither the repo nor the paper mentions it.**

`arc-task-gen`'s only open issue — **#1, filed 2026-08-15 by `maurathat`, still open, no maintainer reply** — claims *375 of ARC-AGI-1's 400 eval tasks are in the ARC-AGI-2 public training set, undetectable by content hashing*, attributing the undetectability to demonstration-pair reordering combined with D₄ symmetry and colour permutation, and warning that task-ID matching cannot be relied on.

**I cloned both datasets and tested it at six cumulative levels** (`leak.js`, `spot.js`, reproducible):

| Level | Match rule | A1-eval tasks found in ARC-AGI-2 `data/training/` |
|---|---|---|
| L0 | same filename / task id | **376 / 400** |
| L1 | byte hash of the file | **0 / 400** |
| L2 | JSON-canonical hash | **0 / 400** |
| L3 | + demonstration pairs as an unordered set | **375 / 400** |
| L4 | + D₄ symmetry (8 dihedral transforms) | **375 / 400** — adds nothing |
| L5 | + colour permutation | 371 (4 fewer; a false-negative artifact of my own tie-group cap, so **L4's 375 is the sound figure**) |

**Controls.** ARC-AGI-1 *training* → ARC-AGI-2 training: **386/400**. ARC-AGI-1 eval → ARC-AGI-2 *eval*: **6/400**. ARC-AGI-2 eval → ARC-AGI-2 training: **0/120** — a clean negative control proving the matcher is not matching everything.

**The mechanism, exactly.** Of the 376 shared ids, **375 have an identical demonstration-pair multiset** — same grids, same colours, no rotation, no recolouring — and **not one of the 375 is byte-order identical**: in every single case the train pairs are simply in a different order. Worked example, task **`00576224`**: ARC-AGI-1 `data/evaluation/00576224.json` holds pairs [A, B]; ARC-AGI-2 `data/training/00576224.json` holds [B, A]. One shared id (`ac0c5833`) genuinely differs.

**So the issue is right about the number and wrong about the reason.** It is not D₄ and it is not colour permutation — those contribute **zero** additional matches. It is **pure pair reordering**. And **all 375 matches land on the same task id**, so this is detectable by `ls`: the issue's own closing caveat that ID matching cannot be relied on is false for this dataset pair.

**Is ARC Prize concealing it?** No, and this must be said plainly. `arcprize/ARC-AGI-2`'s `readme.md:31` states the training set *"combines tasks from ARC-AGI-1 as well as new tasks."* What it does **not** say — anywhere, including `changelog.md` — is that this includes **375 of ARC-AGI-1's 400 *evaluation* tasks**, in a sentence whose neighbouring line describes an evaluation split as *"intended for testing AI models that have never seen these tasks."* A reader's natural inference is training-set-from-training-set. **Disclosed, with the load-bearing half omitted.**

### 2b. And the paper's own training mixture reaches the eval set too

BDH-CQ §4.2, verbatim: *"The dataset combines privately curated examples with publicly available data from the ARC-AGI-1 training set, RE-ARC, ConceptARC, ARC-Heavy, and **ARC-GEN100K**. We apply additional augmentations."* There is **no overlap analysis anywhere in the paper.**

- **RE-ARC** (Hodel, arXiv:2404.07353) — verified: generators for ARC-AGI-1's **400 training tasks only**. Clean.
- **ARC-GEN** (Google, Apache-2.0) — I cloned it. `task_list.py` enumerates **900 distinct task ids: all 400 ARC-AGI-1 training ids, plus 328 of the 400 ARC-AGI-1 *evaluation* ids, plus 172 others.** Its README says the pre-generated **ARC-GEN-100K** set covers *"all four-hundred tasks"* without saying **which** 400.

⚠️ **Precisely what I claim and do not claim.** VERIFIED: the generator suite named in the paper's training mixture publishes generators covering **328 of the 400 evaluation tasks the paper reports 29.5% on**. NOT ESTABLISHED: whether the specific ARC-GEN100K artifact Pathway ingested draws from the eval-covering subset. This is **not an accusation and not a finding of contamination** — it is the observation that **the paper's headline number sits on a set that two of its own named public sources demonstrably reach, and no document performs the check.** Which is *exactly* the question issue #1 closes with, four days after publication, unanswered.

---

## 3. ⭐⭐⭐ THE INVERSION — the honest number exists, it is HIGHER, and it is in an appendix

I expected to find that the tool shipped and the trustworthy number did not. **That was wrong, and I corrected it by reading the paper.** Appendix A, **Table 6** (verified twice, independently prompted):

| Evaluation cohort | Tasks | Solved | Solve rate |
|---|---|---|---|
| Public ARC-AGI-1 evaluation | 400 | 118 | **29.5%** |
| Calibrated generated | 400 | 149 | **37.2%** |
| Mechanic-stratified generated | 1,131 | 337 | **29.8%** |

The 400-task "calibrated generated" cohort is `generate_tasks.py --n 400`. The 1,131-task cohort is `generate_tasks_stratified.py --mechanics all`; §A.2 says *"Every stratified task was authored by GPT-5.6 from a prompt naming the target mechanic."* **Table 7 breaks that cohort across the tool's exact 16 mechanics with Wilson confidence intervals, from Flood fill 68.6% down to Gravity and stacking 2.9%.**

**The model scores 7.7 points HIGHER on the set built to be uncontaminated.** That is the direction *inconsistent* with memorisation inflating the public score — the single strongest piece of evidence in the whole package for their own headline. It appears in **Appendix A.1**. It is not in the abstract, not in the README, not in the blog post, not in the press release.

⚠️ **It does not prove absence of contamination, and the authors correctly decline to say it does** (§A.1: *"The generated cohorts serve different experimental purposes and are not directly comparable."*). The gap is equally consistent with the generated set being **easier** — and **nothing in this tool measures difficulty.** It matches six surface statistics; grid area, colour count and pair count are not cognitive load. There is no published human solve rate for generated output, and `instructions.md:153-157` discloses that solvability is unverified with **19 of 20 hand-checked**. Note the direction: an ill-posed generated task is one the solver *loses*, so a ~5% ill-posed rate means 37.2% **understates** ability on that cohort and **widens** the gap. (A fleet agent inverted this and built a "calibrated ~24–26%" on a fabricated citation — see §10.)

**The most interesting number in the package is 29.8%.** The mechanic-stratified cohort — deliberately harder and broader, evenly allocated across 16 mechanics instead of following the eval set's skew — lands **0.3 points from the public figure**. Uninterpretable without a difficulty control, and still the most striking thing here.

**And this is the tool's real contribution, which its own README never states:** the point of a distribution-matched private set is not to restate the aggregate. It is to **buy statistical power in cells the real benchmark cannot fill.** 400 public tasks cannot support a per-mechanic estimate; 1,131 evenly-allocated ones can, and the answer — 68.6% on flood fill, 2.9% on gravity, a **24× spread** — is the actual scientific yield. The docstring's `--mechanics all --per-mechanic 94  # full powered design` is a power calculation.

---

## 4. ⭐⭐⭐ "Independent Reproduction" — a section header that does not hold for any of the three

`README.md:54` heads a section **`## Independent Reproduction`**:

- **`:56`** — *"BDH-CQ's ARC-AGI-1 results were evaluated and reproduced by Łukasz Kaiser, a co-author of the Transformer architecture and TensorFlow."* — Pathway's own blog names Kaiser among the company's **"investors and advisors"** and quotes him endorsing the work. The README omits the affiliation.
- **`:58`** — *"The results were also **independently** reproduced by Remigiusz Kinas, a contributor to Bielik, and Richard Zhong, an NYU researcher."* — **both are authors of the paper**, positions 8 and 9 of 9: *Björn Engdahl, Adrian Kosowski, Jan Chorowski, Zuzanna Stamirowska, Przemysław Uznański, Junlin Jiang, Rohan Phadke, **Remigiusz Kinas**, **Richard Zhong***.

**The direction of travel is documented in git.** Commit `b1ff64c` (2026-08-11) rewrote *"The results were also reproduced by Richard Zhong"* into *"The results were also **independently** reproduced by Remigiusz Kinas … and Richard Zhong"* — the word "independently" was **added**, in the same edit that added a second co-author.

**And Pathway's own blog post does not use the word "independent" or "independently" about any reproduction, and does not mention Kinas at all.** So the independence claim is **stronger in the developer-facing repository than in the company's own press release** — the opposite of the usual direction.

⚠️ **What I am not claiming:** that the reproductions did not happen, that Kaiser's statement is untrue (he said publicly he *"replicated their ARC-AGI-1 results myself"*), or that the result is wrong. The finding is narrow and verified: **a section headed "Independent Reproduction" names one investor/advisor and two co-authors, and calls two of them independent.**

---

## 5. ⭐⭐ The chart discloses a cross-set comparison with a legend glyph

`assets/Pathway_ARC-AGI_result_chart.png` (verified by cropping and reading the regions):

- **Legend:** hollow circle = **Public Eval Set**; filled circle = **Semi-Private Eval Set**.
- **All three BDH-CQ markers (Low / Medium / High) are hollow** → public set.
- **GPT-5.6 Luna (Low) is filled** → semi-private set, at **34.2% @ $0.008**.

So the headline comparison is **BDH-CQ 29.5% on the public set vs Luna 34.2% on the semi-private set** — and by the repository's own argument the public number is the inflated one and the semi-private one is not. The README states neither the set difference nor that **Luna (Low) scores higher**; "11× cheaper" is arithmetically right ($0.008 / $0.0007 ≈ 11.4×) and is a cost claim, not a capability claim.

**The footnotes are better than the prose, and two of them work against Pathway** — credit where due:
1. *"BDH-CQ cost is estimated from measured inference compute, assuming USD 3 per H200 GPU-hour."* — so `$0.0007` is a **self-hosted compute estimate at an assumed GPU rate**, compared against competitors' **public API pricing** (footnote 2). Not like-for-like; the README's word for this is "computed".
2. Leaderboard figures dated: *"accessed 4 August 2026."*
3. *"GPT-5.6 Luna costs are adjusted to 20% of ARC Prize's reported figures … 80% public API price reduction effective 30 July 2026"* — they adjusted the **competitor cheaper**, against their own interest.
4. TRM/HRM are compute estimates, not API prices.

---

## 6. ⭐⭐ Genuinely excellent: a contamination firewall enforced in code, not prose

`generate_tasks.py:641-643`:

> *"Eval descriptions are NEVER placed in the regeneration prompt — showing the generator real eval rules would leak the very set we are trying to stay independent of. **Eval similarity only ever removes; it never instructs.**"*

I traced it. `_build_avoid()` draws from `all_descriptions` + `seen_removed_descs` and **never** from `eval_descriptions`; `eval_descriptions` reaches only `find_eval_similar()`, which returns ids to delete. `generate_tasks_stratified.py:13` states the same rule for the other path: *"…descriptions and task ids never enter the prompt; only shape/colour statistics and labels do."* **The firewall is a property of the data flow, not a request to a model.** One sentence of policy, four lines of enforcement.

⭐ **And `.gitignore` is a load-bearing scientific instrument that explains itself** — its first entry, lines 1-3:

> *"Generated task sets are deliberately not published. The value of the benchmark is that no model has seen the tasks; committing them to a public repo puts them into web-scraped corpora and burns them."*

⭐ **The best single borrowable artifact is a pre-registered instrument-invalidity guard.** `label_eval_tasks.py:211-216`:

> *"'other' is the escape hatch; a large share means the closed list is wrong for this task set and the mechanic axis should not be analysed as-is"* → a runtime `WARNING` when `other` exceeds **15%**.

A stated falsification condition for your own measuring instrument, declared before the data exists, emitted as a warning by the thing that collects it. Paired with `:4` calling category *"the confirmatory analysis axis, comparable across task sets"* and mechanic an *"exploratory sub-bucket"* — textbook pre-registration vocabulary, in a 238-line script.

⭐ **The threshold calibration is real.** `generate_tasks.py:64-70`: 0.92 was chosen because nearest-neighbour similarity between *genuinely distinct* eval tasks has *"median 0.760, p95 0.879 and max 0.912 (38/400 pairs exceed 0.85)"* — so 0.85 *"would delete legitimate novel work."* A threshold derived from the reference set's own internal structure, with the rejected alternative and its failure mode recorded.

### The other half of the same tool is prose addressed to a language model

| Guarantee | Where | Enforced? |
|---|---|---|
| grids rectangular, cells 0–9, ≥2 train pairs | `:293-325` | ✅ **code** — and offenders are deleted and regenerated |
| eval content never in a generation prompt | `:641-643` + `_build_avoid()` | ✅ **code** |
| slot distribution pinned across rounds | `:634-639` | ✅ **code** |
| *"a genuinely new transformation rule you invent — do NOT copy, lightly edit, rotate/reflect, recolor, crop, or otherwise derive"* | `:74-79` | ❌ **prose** |
| *"The transformation rule must be unambiguously inferable from the training pairs alone"* | `:87` | ❌ **prose** |
| *"Before returning the result, verify the task yourself"* | `:90` | ❌ **prose** |
| generated grid sizes actually match the slot | — | ❌ **nothing checks it** |

**Both halves of the v247/v248 axis in one 905-line file.** The guarantee that protects the *experiment* is enforced in code. The guarantee that makes each task a *valid puzzle* is a request to `gpt-5.6`, and the only evidence for it is 19 of 20 hand-checked. To their credit, `instructions.md:151-169` says so in a **Caveats** section — Strix v248's code gate refuses to write a report without a working proof-of-concept; here the tool writes the task and tells you to sample it yourself.

---

## 7. ⭐⭐ The comments are a changelog of the author's own measurement errors — and every number in them checks out

Nine substantive comments record a defect, a rejected alternative, or a measurement that set a constant:

| Kind | Where | What it records |
|---|---|---|
| postmortem | `:161-165` | pooling input+output grids (*"the pre-2026-07-27 behaviour"*) under-sized inputs by *"~8%"*: *"189.7 vs 226.9 mean area"* |
| postmortem | `:332` | *"Two ragged grids reached a scoring run before this was enforced."* |
| postmortem | `:629-632` | running the two filters as sequential single passes *"let each undo the other's guarantee"* |
| rejected alt | `:634-639` | slots are **recycled** not redrawn, because removal correlates with slot properties |
| measurement | `:64-70` | the 0.92 calibration above |
| measurement | `:523-527` | *"Observed rounds-to-converge: 0/1/1/2/7 at N=16/32/64/100/400, with removal rates 0%/9.4%/7.8%/22%/46%. The rate has risen at every scale measured"* |
| measurement | `:761-762` | *"Removals normally decay geometrically (185/88/41/16/8/1/1 at N=400)"* |
| optimisation | `:193-199` | the previous implementation recomputed norms per pair, O(N²) norms for O(N²) comparisons |
| dead-flag disclosure | `:553`, `:564` | *"threshold needs recalibration"*, *"pending slot-recycling fix"* — messages that only print if the flags are set False, which they are not |

⭐ **I recomputed the ones that are checkable, from the public dataset, and they reproduce exactly:**

| Their figure | My recomputation |
|---|---|
| input grids mean area **226.9** (`:163`) | **226.9** (n=1,782) |
| output grids mean area **189.7** (`:163`) | **189.7** (n=1,782) |
| pooled under-sizes inputs by **~8%** | **8.2%** |
| `instructions.md` reference column: 226.92 / 144.00 / 13.23 / 13.70 / 5.35 | **226.92 / 144.00 / 13.23 / 13.70 / 5.35** — every one, exact |
| ≥4 demonstration pairs **34.2%** · 2 test pairs **4.8%** | 34.3% (137/400) · 4.8% (19/400) |
| sanity check's displayed reference *">=95%"* single-test-pair | **95.3%** (381/400) — accurate |

**That matters, and it is the counterweight to everything in §8.** Every number this repository states about the reference dataset — in its docs *and* in its code comments — is a real measurement that survives independent recomputation to the stated precision. On the one table a reader can check, it checks out.

⭐ **Also verified as a non-issue:** `validate_tasks` rejects any task with <2 train pairs, and **zero** of the 400 eval tasks have fewer than 2 (min 2, max 7), so the validator never conflicts with a faithfully-copied anchor.

⚠️ **The catch: 185+88+41+16+8+1+1 = 340.** Producing 400 novel tasks took **740 generations — 340 tasks were thrown away for every 400 kept**, and the first-round collision rate at N=400 is **46%** and *"has risen at every scale measured."* **That scaling wall is the most important operational fact about the tool and it exists only in a comment on a backstop constant.** Neither document mentions it. (`instructions.md:31` gives *"27 parse failures across 758 calls"*; 740 + retries ≈ 767 vs 758 — close, not reconcilable; I do **not** assert they are the same run.)

---

## 8. The doc-integrity ledger

**Undocumented in both README and `instructions.md`:**

- **`TOLERANCE = 0.40`** (`:402`) — the distribution sanity check reports **PASS** at up to a 40% deviation of mean/median from the eval set. On mean input area that permits anywhere in **[136.2, 317.7] cells** and still says PASS. ⚠️ In fairness: the reported run came in at **224.70 vs 226.92 — a 1.0% deviation, beating its own gate by ~40×.** The gate is loose; the result did not need it.
- **`single_test_pair_fraction`** (`:451-458`) — PASSes at `>= 0.80` while printing `"eval_value": ">=95%"`. The ">=95%" is **accurate about the eval set** (I measured 95.3%); the finding is only that the gate sits **15 points below the reference it displays**.
- **`ENABLE_DEDUP` / `ENABLE_EVAL_SIMILARITY`** — both filters have kill switches absent from the Configuration table.
- **The 46% / rising-collision finding and the 185/88/41/… decay series** — §7 above.
- **`MAX_TRAIN_PAIRS = 3`** (`label_eval_tasks.py:38`, `describe_eval_tasks.py:32`) — every eval-task rule description *and* every category label is derived from **at most the first 3 training pairs**, on the unverified assertion *"3 is enough to infer the rule."* Both downstream filters and the paper's stratification rest on it. Not mentioned in either document.

**🔴 A real bug, confirmed by my own grep.** `eval_similar_replaced` appears exactly three times in `generate_tasks.py`: initialised at **`:651`**, written into `sanity_check.json` at **`:862`**, printed at **`:882`**. **It is never incremented.** So the run report's `eval_similarity_summary.replacements_generated` is **structurally always 0**, and every run prints `Replacements generated: 0` for the contamination filter. Removals *are* recorded (`:698`). The audit trail of the tool's headline guarantee has a dead counter in it.

**The two-document split.** `instructions.md` is a genuinely excellent engineering document: a Configuration table, a "How it works" section that explains *why* one task per call (asking for 32 at once collapsed mean grid area to **14 cells against 208**), and a **Caveats** section with three named limitations. `README.md` has **zero** caveat subsections and **one** high-level epistemic note (`:37`). A reader who stops at the README learns 29.5%, $0.0007, 11×, three "independent" reproducers, and **no limitation at all** — not that solvability is unverified, not that ~1 in 20 sampled tasks was not solvable, not that 46% of first-round tasks collide. It does link to `instructions.md` — at line 52, after everything.

**On the two-document split I make one narrow claim and decline a broader one.** `README.md` still carries **two `<!-- TODO -->` comments at HEAD**; commit `3bf471e` replaced a **live `http://google.com`** placeholder in the paper citation; commit `c046ab7` deleted a blockquote reading *"**Note:** For the chart to render directly in this README, add the image to the repository—for example, at `assets/pathway-arc-agi-chart.png`—and replace the link above with:"* — a note instructing its own reader what to do next, committed publicly. Against that: **zero `Co-Authored-By` trailers on any of the 12 commits**, `.claude/` in `.gitignore`, and a codebase whose calibration commentary no model would invent. **Defensible: the README was assembled in haste with drafting scaffolding left in it.** Not defensible from this evidence, and I do not claim it: who or what wrote it.

⚠️ **The README also mis-cites the paper it promotes.** `:25` gives the title as *"BDH-CQ: **Introducing** In-Context Learning with Recurrent Latent Reasoning"*; the actual arXiv title is *"BDH-CQ: In-Context Learning with Recurrent Latent Reasoning"*. Harmless, and explained by the TODO on the next line — the citation was written from a draft.

⚠️ **v246's detector replicates — 4th repo.** `grep -rni "silent" .` returns exactly 2 hits: `:523` (*"an under-set one silently ships a set with residual clusters"* — a documented trade-off, immediately followed by the real termination condition) and `generate_tasks_stratified.py:232` (unlabelled anchors *"are silently excluded"* — **and the function then prints how many**). **Refinement: both hits are places where the author noticed a silence and removed it.** Contrast v246, where the grep found *loud failures* the author had engineered, and v248, where it found an evidence ladder. Here it finds a candid docstring. The detector keeps earning its keep.

⚠️ **v240's inventory rule, one instance.** `load_anchor_profiles()` (`generate_tasks_stratified.py:225-241`) drops eval tasks with no category label from the anchor pool. It reports **how many** were dropped, never **which** — so a partially-labelled run silently shrinks the anchor population, and the paper's stratified cohort of **1,131** tasks matches no clean multiple of 16 (the docstring's "full powered design" is `--per-mechanic 94` = 1,504). The tool has three documented ways to under-deliver — dropped id collisions (`:602`, `:738`), the stall detector, the round ceiling. **I name the mechanisms; I do not assert which produced 1,131**, and the paper does not say.

---

## 9. Prior art, mint decision, security

**Collision check CLEAN.** Zero prior vault mentions of `pathwaycom`, `arc-task-gen`, ARC-AGI, Chollet, Dragon Hatchling, BDH, Arnould, RE-ARC or BARC, against richly-hitting anchor controls.

**🔴 The Chollet attribution does not hold.** `label_eval_tasks.py:80` calls its six categories *"the six Chollet ARC-AGI categories"* and `:1`/`:4` call them *"a Chollet cognitive primitive category"* / *"the confirmatory analysis axis."* Chollet's *On the Measure of Intelligence* (arXiv:1911.01547) defines **four Core Knowledge priors** — objectness and elementary physics; agentness and goal-directedness; numbers and counting; elementary geometry and topology — the vocabulary `arcprize/ARC-AGI-2`'s own readme uses. Of the six: `numerical` maps cleanly, `object_centric` and `geometric` map loosely, `spatial_relational` is subsumed, and **`pattern_completion` and `compositional` have no counterpart at all.** The six are a reasonable taxonomy; they are not Chollet's. "Chollet" appears **7 times across 4 files**, including `instructions.md:46`/`:74` and — worst — `label_eval_tasks.py:220`, which writes *"Chollet category and transformation mechanic"* into the output JSON's own self-description, so **every downstream consumer of `arc_agi_eval_categories.json` inherits the misattribution.** And this is the axis the paper's Appendix-A analysis calls confirmatory.

**NOT world-first, on decisive external prior art:**

- **ARC-GEN** (Google, Apache-2.0, arXiv:2511.00162) — a generator explicitly **"mimetic"**, preserving grid size, colour distribution and pair counts; 900 tasks; **ARC-GEN-100K** pre-generated. This is *distribution-matched ARC task generation*, published by Google, **and it is in BDH-CQ's own training mixture.**
- **BARC / ARC-Heavy** (Li, Ellis et al., 2024) — LLM-generated ARC-like tasks at ~400k scale from seed solutions.
- **RE-ARC** (Hodel, 2024) — 400 procedural generators.
- **ARC-TGI** — *"461 generators covering 180 ARC-Mini tasks, 215 ARC-AGI-1 tasks (200 train, 15 test), and 66 ARC-AGI-2 tasks."*
- Contamination-resistant evaluation as a practice: LiveBench, Dynabench, GSM1k, canary strings, private/semi-private splits — ARC Prize itself runs semi-private and private sets.

**NO MINT, on five grounds:** (1) decisive external prior art above — the **v240** (awesome-selfhosted/HACS) / **v242** (Eclipse RCP/OSGi) discipline; (2) **technique-not-capability** — "synthetic benchmark-twin generation" is a method, and the **v211 PixelRAG** rule is that corpus-first-for-a-technique is not mintable; (3) **research artifact, not a capability layer** — a 2,139-line paper appendix, not a tool an agent reaches through (the v211 research-system-not-tool line); (4) **§28** anti-inflation at ~51 live standalones; (5) **not the exemplar** — ARC-GEN is Google's and larger.

**NOT an N=2 of the v233 ClawWork row.** That row is an *economic-survival benchmark harness* — agents solve, get paid, go bankrupt. This is a *dataset generator* producing `tasks.json`. Different object; no N-bump. ⚠️ **NO-MINT ALTERNATIVE RECORDED, operator/audit-reviewable, NOT self-executed:** *"LLM-Generated Distribution-Matched Private Benchmark Twin for Contamination Control (N=1)"* — defensible only on the narrow conjunction of joint-slot covariance sampling + a code-enforced eval-content firewall; loses on all five grounds and would be drawing the circle to fit (**camofox v179**).

**Pattern checks:** #57 **NO** (cites no corpus subject; none cites it). #18 B1-MCP **NO** (no MCP; the tool ships no agent-facing surface at all). #12 **NO** (no `AGENTS.md`/`CLAUDE.md`/`llms.txt`). #83 **YES, STRONG** — a Caveats section that names its own unverified guarantee with a hand-check figure, plus the pre-registered >15% invalidity guard, plus two flag messages naming the defects that once disabled them. #52 **CANNOT CLAIM** (§37.4 — the GitHub API is mocked; 3.6k★ is page-stated). #84 84c **YES, no N-bump** (any OpenAI-compatible endpoint; vLLM/Ollama/LM Studio named). #19 19a **FAIL** per §41 (Ludovic Arnould / Pathway; not Anthropic, not a registered vendor-direct source). #66 **LOW** — see below. Max pattern #85; no N-bumps taken.

**Security / supply chain — LOW risk, the cleanest in recent memory.** No port is bound. No CORS. No `eval`/`exec` on model output; the only dynamic import is `importlib` loading `generate_tasks.py` from the same repo. Network egress is exactly two destinations: `codeload.github.com` for the Apache-2.0 dataset tarball, and the configured OpenAI-compatible endpoint. The API key comes from `OPENAI_API_KEY` only, is never written anywhere, and `.gitignore` fences `.env` and `api_key.txt`. Writes are confined to `data/`. **No broken-auth triad — structurally, because there is no server.** `pixi.lock` (79.7 KB) pins the conda-forge resolution; `pixi.toml` uses floors, not exact pins. **Zero tests.** ⚠️ The real cost is money, not risk: a 400-task run is ~760 frontier-model calls plus embeddings. ⚠️ Licence: the tool consumes Apache-2.0 data and is MIT; it redistributes nothing (`instructions.md:171-176` says so).

---

## 10. Error ledger

**Mine — 1, self-caught before publication.** I framed the headline as *"the tool that would produce the honest number shipped; the honest number did not."* **Wrong.** Fetching the paper's HTML found Table 6 in Appendix A.1: the generated-set numbers exist and the calibrated one is **higher**. The finding inverted into something better, and the error was the vault's signature shape — **inferring that a mechanism was not used from its absence in the promotional surface.**

**The fleet's — 5, all rejected or corrected:**

1. 🔴 **A fabricated paper.** The situating agent built its whole difficulty analysis on *"Tong et al. arXiv:2405.18742, 'Synthetic Data for Evaluation of Language Models',"* quantified as *"34% human solvability vs 58% real ARC-AGI-1; models score ~8pp higher,"* and derived a *"calibrated score ~24–26%."* **arXiv:2405.18742 is "Musical Phrase Segmentation via Grammatical Induction" by Perkins & Ventura.** The paper, its findings and every derived number are invented. **All discarded.** The underlying objection is real and needs no citation: the code matches six surface statistics and measures difficulty nowhere.
2. **Inverted arithmetic** in the same report — unsolvable generated tasks treated as *"freebie passes"* inflating the score. An ill-posed task is one the solver **fails**; a ~5% rate means the measured figure **understates** ability. Direction reversed.
3. **The critic's #2 headline: *"THE PAPER NEVER MENTIONS ARC-TASK-GEN OR USES SYNTHETIC TASKS … a post-hoc narrative."*** **False** — Tables 6 and 7 are generated-set results. The agents could not load the full text and converted that into a confident negative. **Absence of evidence rendered as evidence.**
4. **Fabricated line citations**, caught by the contradiction stage in three separate reports: the firewall comment placed at 470 and at 400 (actually **641-643**), `TOLERANCE` at 860 (actually **402**), the threshold mismatch at 701 (actually **451-458**), and *"27 parse failures"* attributed to a code comment at line 758 (actually **`instructions.md:31`**).
5. **The critic invented an error in my grounding**, claiming I had cited the firewall at "~line 400". I gave no line number for it.

⭐ **The method finding replicates for a third consecutive ship, and sharpens.** The **contradiction stage** — hand a mapper's report over as a suspect document, demand six citations opened individually and a read receipt — caught every fabricated line number, including in the report that was otherwise strongest. It did **not** catch the fabricated *paper*, because no agent was asked to treat the *situating* reports as suspect. **The stage only protects the stages it is pointed at.** The v249 refinement: **pipeline the contradiction pass over the situating reports too, not just the mapping reports.** And the fabrication that mattered most was caught the same way every load-bearing thing in this ship was caught — by running the check myself.

---

## 11. What to take

1. ⭐⭐⭐ **The pre-registered instrument-invalidity guard.** State, before you collect data, the condition under which your own measuring axis is not analysable — and make the collector emit it. `label_eval_tasks.py:211-216`.
2. ⭐⭐⭐ **"Only ever removes; it never instructs."** When a filter must consult ground truth, let it delete but never inform. Enforce it in the data flow, not in a comment. `generate_tasks.py:641-643`.
3. ⭐⭐ **Generate a private set to buy statistical power in cells the real set cannot fill** — not to restate the aggregate. Table 7's 24× spread is the yield.
4. ⭐⭐ **Comment the measurement that set the constant, and the alternative you rejected.** Nine of them here, and the checkable ones reproduce exactly.
5. ⭐ **A `.gitignore` entry can be a scientific instrument.** Say why in the file.
6. ⭐ **Take a third party's quantified claim and test it yourself.** Issue #1 was right about 375 and wrong about the mechanism, and one afternoon of Node settled both.
