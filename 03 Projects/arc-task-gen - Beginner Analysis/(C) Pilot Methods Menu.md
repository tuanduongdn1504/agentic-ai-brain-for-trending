# (C) Pilot Methods Menu — v249 `pathwaycom/arc-task-gen`

**Verdict:** 🔴 **READ-AND-BORROW.** Do not run the tool. Port the method.

**Why the method matters to you specifically.** Your RATIFIED ADR (`project_hireui_candidate_llm_legibility_adr`) says any hireui LLM path touching a candidate must be **fixed + legible + audited + human-in-the-loop + eval-gated**. hireui has **no LLM integration yet** (`project_hireui_no_llm_yet`) and therefore no eval set — and you cannot freely use real candidate data to build one (GDPR / EU AI Act). `arc-task-gen` is a 2,139-line worked example of the exact manoeuvre that unblocks this: **build a synthetic evaluation set whose measured distribution matches your real one, and guarantee in code that the generator never saw the answers.**

---

## The equivalence map

| arc-task-gen | hireui Match-Explain equivalent |
|---|---|
| **Slot** — `{rows, cols, colors, n_train, n_test}` copied **wholesale from one real eval task** so covariance survives (`generate_tasks.py:145-152`: sampling axes independently gives *"a 2x2 grid asked to carry 9 distinct colours"*) | **Profile slot** — `{seniority band, sector, years-bucket, education type, job-level, location type, JD length band, CV length band}` copied **wholesale from one real recruiter-labelled pair**. Never per-axis. This is the whole trick: a "senior backend, 12 years, 300-word CV" is a coherent case; a marginal-sampled "intern, 20 years, 40-word CV" is not. **Metadata axes only — never CV text, never skills, never employers, never names.** |
| **Eval-similarity filter** — generated rule descriptions compared against real eval descriptions; anything ≥0.92 deleted. Threshold set from the reference set's own internal structure (median 0.760, p95 0.879, max 0.912 between *genuinely distinct* tasks) | Generated explanations compared against real recruiter explanations; delete the near-duplicates. **Calibrate the threshold the same way**: measure similarity *between distinct real recruiter explanations first*, and put the threshold just above that observed maximum. Do not pick 0.9 because it looks like a number. |
| ⭐ **"Only ever removes; it never instructs"** (`:641-643`) — `_build_avoid()` draws only from prior generations and prior rejections; eval content reaches the filter and nothing else | **The single most important line to port.** The real recruiter explanations may inform *what gets deleted* and must never appear in *the prompt that generates*. Enforce it as a data-flow property with one function that builds the prompt and cannot see the ground-truth set — not as a comment. |
| ⭐ **`.gitignore` as an instrument** (lines 1-3, with the reason in the file) — *"the value of the benchmark is that no model has seen the tasks; committing them puts them into web-scraped corpora and burns them"* | `evals/synthetic/` gitignored **with the reason written in the gitignore**, plus a pre-commit check that no path under it is referenced from any training / fine-tune / system-prompt file. Publishing burns the set; so does feeding it back. |
| ⭐ **Pre-registered invalidity guard** (`label_eval_tasks.py:211-216`) — *"'other' is the escape hatch; a large share means the closed list is wrong … and should not be analysed as-is"*, emitted as a runtime WARNING above 15% | Your rubric's escape category ("insufficient evidence" / "other"). **Before you collect anything**, write down the share above which your rubric axis is not analysable, and make the scorer print it. This is the cheapest scientific discipline in the repo. |
| **Sanity check** on 6 surface statistics with `TOLERANCE = 0.40` (`:402`) | Compare synthetic vs real on word count (mean/median), reason count, score distribution, seniority/sector balance. **Set the tolerance tighter than 0.40 and put it in the docs** — theirs is undocumented and 40× looser than the run needed (224.70 vs 226.92 = 1.0%). |
| **Caveats: "Solvability is not verified programmatically … 19 of 20 hand-checked"** (`instructions.md:151-157`) | *"Explanation validity is not verified programmatically."* Blind hand-check **20** synthetic pairs with a recruiter: would you agree with this explanation for this candidate-job pair? Record the pass rate. Below 19/20, the generation prompt is wrong — fix it before scoring anything. |
| **One task per call** — asking for 32 at once collapsed mean grid area to **14 cells against 208** (`instructions.md:99-107`) | One synthetic case per call. A model given a batch spends a fixed effort budget across it and every item gets thinner. Expect the same and budget for it. |
| ⭐ **Stratify to buy power, don't restate the aggregate** — Table 7's 16 evenly-allocated mechanics gave a **24× spread** (flood fill 68.6%, gravity 2.9%) that 400 naturally-distributed tasks could never reveal | **Do not build a synthetic set to re-measure your overall accuracy.** Build it to fill the cells your real data cannot: career-changers, employment gaps, non-linear progressions, under-represented sectors. Allocate evenly across those cells and you learn *where* Match-Explain fails. That is the deliverable. |
| **The 46% wall** (`:523-527`, in a comment only) — first-round collision rate rose at every scale, 0%→46% at N=400; 400 kept cost 740 generations | **Budget for it and measure it.** Expect to throw away roughly as many synthetic cases as you keep at a few hundred, and log the removal rate per round. If it rises with N, your diversity pressure is the binding constraint, not your model. |

---

## Rung ladder

### ⭐ Rung 1 — 2–3 h · ZERO install · ZERO spend · **DO THIS ONE**
Read exactly three things: `generate_tasks.py:641-643` plus `_build_avoid()`, `label_eval_tasks.py:211-216`, and `.gitignore:1-3`. Then write **`hireui/evals/METHOD.md`** fixing three rules in your own words: **(i)** the ground-truth set may delete a synthetic case and may never appear in the prompt that generates one; **(ii)** state the invalidity condition for each measurement axis before collecting, and make the collector print it; **(iii)** synthetic eval cases are never training, fine-tuning or prompt-engineering input — gitignore + pre-commit, reason written in the file.
**Fence:** none. Nothing runs.
**Why you'll actually do it:** it is a reading task with a one-file deliverable, it discharges a ratified-policy obligation you currently cannot meet, and it needs no API key.

### Rung 2 — 3–4 h · ZERO install · ZERO spend
Write `hireui/evals/PROFILE_SLOTS.md`: enumerate the profile-slot axes, and compute their **real joint distribution** from whatever labelled pairs you have — the marginals are useless, you need the covariance. Add the `--dry-run-plan` idea from `generate_tasks_stratified.py:451`: a flag that prints the sampled plan and exits without calling any API. Then decide which **cells** you want power in.
**Fence:** read-only over your own data; no model calls; aggregate counts only, no CV text leaves the query.

### Rung 3 — 6–8 h · your own generator · metered spend
Write `hireui/evals/generate_cases.py` on this repo's shape: slot sampling → one case per call → dedup on generated explanations → ground-truth-similarity filter that **only removes** → distribution sanity check → write to gitignored `evals/synthetic/` with a run manifest (model, prompt version, rubric version, seed, removal-rate-per-round). Blind hand-check 20.
**Fence:** `--dry-run` first and inspect 5 samples by hand; profile slots from metadata only; a documented tolerance; the manifest is mandatory; the pre-commit check from Rung 1 must already be in place.

### Rung 4 — 8–12 h · the eval gate itself (depends on Rung 3)
Wire the synthetic set into a **fails-closed** gate on the Match-Explain path: no score is returned to any UI unless the eval run passed. This is the clause of the ADR that currently has no implementation. Log every call (input hash, model + prompt + rubric version, output, timestamp).
**Fence:** feature-flagged to a pilot recruiter set; human-in-the-loop on every candidate-facing output; weekly re-run of the synthetic set to detect drift.

### Rung 5 — LAST · run `arc-task-gen` itself
Only if you want to see the machine work. `pixi install`, `python generate_tasks.py --n 16` (the default 32 is 32 frontier calls; 16 converges in 0–1 rounds per `:524`), then `visualize_tasks.py` to eyeball the PNGs. Skip `describe_eval_tasks.py` (400 calls) unless you want the eval-similarity filter on.
**Fence:** throwaway venv via `/install-snapshot`; a spend-capped key; `ARCGEN_MODEL` pinned; leave `OPENAI_BASE_URL` unset or point it at a local model; **never** point it at candidate data — it does not take any, and it should stay that way.
**Value:** low. You will learn nothing Rung 1 didn't teach.

---

## What must NEVER happen

1. 🔴 **Profile slots never read CV or JD *content*.** Metadata axes only. If skills, employers, names or accomplishments enter the sampler, the synthetic set is derived from real candidates and the whole GDPR argument for building it collapses.
2. 🔴 **Synthetic eval cases never become training, fine-tuning, DPO or system-prompt input.** Enforced by pre-commit, not by intention. Their only value is independence from the model.
3. 🔴 **Never publish them**, for the reason `.gitignore:1-3` gives: they go into web-scraped corpora and burn.
4. 🔴 **Never skip the blind 20.** This repo's own caveat is that solvability is unverified with 19/20 hand-checked; yours will be *explanation validity*, and it is the only check that catches a generation prompt drifting away from your rubric.
5. 🔴 **Never quote this repo's headline numbers as verified.** 29.5% pass@2 is **self-reported**, measured on a set that ARC-AGI-2's public training split republishes 375/400 of and that ARC-GEN's generators cover 328/400 of; `$0.0007` is a **self-hosted compute estimate at an assumed $3/H200-GPU-hour** set against competitors' **retail API prices**; and the chart's own legend shows BDH-CQ on the **public** set against comparators on the **semi-private** set. The one number worth remembering is the buried one: **37.2% on the generated cohort** — and it is uninterpretable without a difficulty control nobody has run.
6. 🔴 **Never repeat the "six Chollet categories" attribution.** Chollet's ARC framework is **four Core Knowledge priors**; two of this repo's six have no counterpart. If you build a rubric taxonomy, attribute it to yourself.
