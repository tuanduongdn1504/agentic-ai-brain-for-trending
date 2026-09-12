# The rubric-reject audit — what the selection formula threw away, and what we found instead

> **Drain:** 2026-09-12, autopilot `/loop`. **Not a new topic and not an ordinary revisit** — an audit *of the selection rubric itself*. Corpus stays at **80**.
> **Raw:** `raw/2026-09-12-hermes-agent-rubric-reject-audit/` · **Manifest:** `.../\_sources.md`
> **Workflows:** `wf_660869eb-780` (5 rejected sources, 24 agents) + `wf_93eb57c0-9b3` (6 selected sources as a **control**, 24 agents). 48 agents, 3.70M tokens, **0 errors, 0 empty results**.

## Why this exists

The operator asked whether a video could be ingested. The video — `DYdvJCxWd6M`, Metics Media, *"Hermes Agent — Full Tutorial & Setup Guide (For Beginners)"* — turned out to be **already named in this corpus**, in the 2026-09-03 manifest's list of *"High-reach candidates the rubric dropped."* It had been surfaced, scored, and rejected nine days earlier.

In those nine days it went **140,334 → 294,324 views (+109.7%)** while its two sibling videos on the same channel moved +1.5% and +2.3%. Video-specific velocity, not channel growth.

So instead of a third ordinary pass on a saturated topic, the operator elected to **grade the five sources the rubric rejected and compare them against the six it selected.**

## Part 1 — The rubric, reproduced exactly

`bin/autopilot-drain.py:select_videos()` scores:

```
score = log10(views) + (views / channel_subscribers) * 3 + max(0, 1 - days_old/365) * 2
```
with hard filters `views >= 1000`, `duration >= 300s`, `upload within 180 days`, and a cap of 2 videos per channel.

Recomputed at the 2026-09-03 selection date, this returns **exactly the six sources that were actually selected** — which is strong evidence the reproduction is faithful.

| # | score | source | views | subs | log10 | **eng×3** | rec×2 | outcome |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 1 | **676.22** | weeb3dev | 3,803 | **17** | 3.58 | **671.12** | 1.52 | SELECTED |
| 2 | 14.01 | Tonbi ep.1 | 80,849 | 31,200 | 4.91 | 7.77 | 1.33 | SELECTED |
| 3 | 13.53 | CodeHead 5-min | 224,435 | 99,900 | 5.35 | 6.74 | 1.44 | **REJECTED — 293s vs a 300s floor** |
| 4 | 9.56 | Wanderloots | 98,250 | 101,000 | 4.99 | 2.92 | 1.65 | SELECTED |
| 5 | 8.27 | Tina Huang | 398,873 | 1,310,000 | 5.60 | 0.91 | 1.75 | SELECTED |
| 6 | 8.05 | CodeHead t6 | 62,346 | 99,900 | 4.79 | 1.87 | 1.39 | SELECTED |
| 7 | **7.74** | **Metics full tutorial** | 140,334 | 696,000 | 5.15 | 0.60 | 1.98 | **REJECTED by 0.31** |
| 8 | 7.43 | Tina Huang HermesOS | 141,888 | 1,310,000 | 5.15 | 0.32 | 1.95 | REJECTED |
| 9 | 7.13 | Metics step-by-step | 129,686 | 696,000 | 5.11 | 0.56 | 1.46 | REJECTED |
| 10 | 6.85 | Metics ultimate | 117,001 | 696,000 | 5.07 | 0.50 | 1.28 | REJECTED |

Three mechanical facts fall out:

1. **`eng_ratio * 3` is unbounded.** A channel with **17 subscribers** and 3,803 views produced an engagement ratio of 223.71, contributing **671 of its 676 points — 99.2% of its score**, and beating the field by **48×**.
2. **`log10(views)` spans 3.58 → 5.60 across the entire pool — 2.02 points.** Reach is very nearly a constant in this formula. It cannot outvote anything.
3. **`MIN_DURATION_SEC = 300` excluded a 253,592-view source by 7 seconds**, and that source scored #3 of 11 — above three of the six actually selected. This is a structural exclusion, not a ranking judgement.

**The rejected bundle out-reached the selected bundle**: 753,344 views against 664,343 at selection time.

### The honest version of that finding

An adversarial critic was tasked with refuting the headline, and it **partially succeeded**. The arithmetic is not in dispute. What the arithmetic does *not* establish is that the bias is *harmful*:

- `views/subscribers` is a resonance measure, not a smallness measure. Rewarding it may be a deliberate preference for scrappy over polished.
- weeb3dev, the source it elevated, was graded mid-pack on 2026-09-03 — not worst.
- Capping the engagement term at 2.0 reshuffles the top (CodeHead-5min 12.78 · Tonbi 12.24 · weeb3dev 11.09) but **changing an outcome is not evidence of improving it.**

**Adopted claim:** *the engagement term is unbounded and creates a 48× score gap favouring small-channel, high-engagement content over large-channel content. Whether that is a bug or a feature depends on whether views-per-subscriber predicts quality — which the next section tests.*

## Part 2 — The control, and the result nobody predicted

To make "did the rubric pick better sources?" answerable, the **six selected sources were re-graded through the identical pipeline against the identical ground truth**. Same extractor prompt, same three lenses, same code-based adjudication, same three local files. Only then are the numbers comparable.

Both bundles were graded against a deliberately narrow snapshot (README + apps/desktop/README + repo metadata + 30 releases), so a large share of claims land as UNVERIFIED in **both**. The meaningful denominator is therefore **settleable claims** — those the ground truth can actually decide.

| Bundle | sources | claims | UNVERIFIED | settleable | errors | **err / settleable** |
|---|---:|---:|---:|---:|---:|---:|
| **REJECTED** | 5 | 140 | 79 | 61 | 9 | **14.8%** |
| **SELECTED** | 6 | 208 | 112 | 96 | 19 | **19.8%** |

On raw numbers the rejects look better. **But the raw numbers are wrong**, and the reason is the real finding of this ship.

## ⭐⭐⭐ A third to a half of what this corpus grades as "creator error" is speech-recognition failure

Reading all 28 graded errors by hand, a pattern dominates: the defect is not in what the creator said, it is in **what YouTube's automatic captioning heard**.

How the vendor's name is rendered across the 11 transcripts:

| rendering | count | where |
|---|---:|---|
| **Nous Research** ✅ | 6 | r1, r2, t1, t4 ×2, t6 |
| **News Research** ❌ | 5 | t2 ×2, t4 ×1, t5 ×2 |
| **new research** ❌ | 5 | t3 ×5 |
| **Nouse Research** ❌ | 1 | r4 |

**11 of 17 mentions are garbled, and every one became a CORRECTED or FALSE verdict against the creator.**

Two proofs that this is the machine and not the speaker:

- **`t4-wanderloots` contains both spellings — "Nous Research" twice and "News Research" once, in one transcript.** A human does not alternate mid-video.
- **Metics Media says "OpenClaw" correctly in `r1`, and "Open Cloud" twice in `r4`** — same creator, same product, different caption track. *"If you've used a tool called **Open Cloud** before…"* is `OpenClaw`, and it cost that video two CORRECTED verdicts.

The most severe case: the operator's own 2026-09-03 anchor was graded **FABRICATED** — the harshest verdict in the taxonomy — for the phrase *"around August 2016"* in the **English auto-translation of a Vietnamese video**. The extractor itself wrote *"LIKELY GARBLED"* into the claim text. All three lenses graded it FABRICATED anyway.

### Reclassified, conservatively

Counting as an artifact only those errors whose *sole* defect is a garbled proper noun:

| Bundle | errors | **ASR artifacts** | genuine | settleable | **corrected error rate** |
|---|---:|---:|---:|---:|---:|
| **REJECTED** | 9 | 3 (33%) | 6 | 61 | **9.8%** |
| **SELECTED** | 19 | 9 (47%) | 10 | 96 | **10.4%** |

**9.8% versus 10.4%. The rubric's rejects and its picks are indistinguishable.**

That is the answer to the question the operator actually asked. The rubric is not costing this corpus accuracy — and it is not buying any either. It is, on this evidence, **accuracy-neutral**, and the case for changing it rests on the mechanical grounds in Part 1, not on source quality.

### What this does to two earlier headlines

Both need qualifying, and this section states the limits carefully.

- **Tina Huang** (398,873 views) was the 2026-09-03 bundle's *worst* source at 50%. In this run **all four of her errors are the same "Nous"→"News" garble**, including a FALSE verdict on the URL *"hermesagent.newsresearch.com"* — where the real homepage, per `repo.json`, is `hermes-agent.nousresearch.com`.
- **The holetex anchor's** single error here is the "August 2016" translation artifact.

⚠️ **This does NOT mean either source has zero genuine errors.** This run's ground truth is deliberately narrower than the 2026-09-03 run's, which had live web access. Real defects that run found — the **Ollama Cloud trap**, the **Claude Code positioning** claim — sit outside what a README can settle and are **not** overturned here. The correct statement is narrower and still significant: *among the claims this ground truth can decide, the error signature of both the best- and worst-rated sources is dominated by transcription noise* — so **the 2026-09-03 per-source ranking, and the "reach ≠ reliability" reading built on it, cannot bear the weight placed on them.**

The prior ship half-saw this. It noted *"Speaker said 'Claw code'"* in a footnote for one claim, and never generalised it.

## ⭐⭐ Four of the five rejected sources demonstrably ran the product; the fifth did not

Independent of any verdict count, the extractors were asked whether each creator *actually ran the thing on screen*. This is the content difference the rubric could not see:

- **r1 Metics (294K)** — **YES**, and the strongest artifact in either bundle: a live OpenRouter billing page showing **13 cents across 105 requests and ~4M tokens**, with three-quarters served from cache. Real money, real numbers, on camera.
- **r4 Metics (133K)** — **YES**. Telegram round-trip; agent returns a real server path `/opt/data/email-marketing-top-5-youtube.md`.
- **r5 Metics (119K)** — **YES**. Setup wizard, live Telegram, memory recall, job creation with a returned job ID.
- **r3 Tina Huang (166K)** — **YES**. `npm start`, a running Pomodoro app, skin-switching demonstrated.
- **r2 CodeHead (254K)** — **NO.** The only on-screen evidence is narration over a screenshot of the skills hub. *"Hermes Agent itself is never instantiated or demonstrated working."*

**r2 is the source the duration floor excluded** — and it is the one that never ran the product. On that single case the filter was right, for entirely the wrong reason: it fires on length, and length is not the variable that mattered.

## ⭐⭐ What the rejected bundle carries that the wiki did not have

- **Prompt injection.** r1 explicitly warns that *"a web page it reads can contain malicious instructions called prompt injections."* **The README contains zero occurrences of "inject", "untrusted", or "malicious"** (grep-verified). The source is more safety-conscious than the vendor — the inverse of this corpus's usual finding, and directly relevant to the operator's standing security concerns.
- **"HermesOS" is settled, at its origin.** Tina Huang says *"my Hermes setup, **my Hermes OS**"* — a possessive describing her own rig. She never claims a product exists. The corpus had flagged the term as creator coinage without ever holding the source that coined it. "HermesOS" appears **0 times** in all ground-truth files.
- **A no-terminal path exists now.** `apps/desktop/README.md` says verbatim **"no terminal required"**, and r1 demonstrates a one-click managed VPS deploy where no shell is ever opened. The corpus graded *"no-code"* **MISLEADING** on 2026-07-18 against a `curl|bash` CLI. That verdict was right in July; it is now **TIME-BOUND** — see [[caveats-and-corrections]].
- **Portal pricing is still unverified.** r1 says *"from about $20 a month"*. The README documents Portal and "300+ models" but **names no price**. Same shape as the grok-bot pricing finding: the product is real, the number is unsourced.

## ⚠️ Correlated incentive across the whole rejected bundle

**All five rejected sources route through Hostinger.** Mention counts: r5 ×11, r4 ×9, r1 ×5, r3 ×3, r2 ×2. Only r3 discloses verbally (*"A portion of this video is sponsored by Hostinger"*); the three Metics videos use affiliate phrasing (*"link in the description"* ×4 and ×7, *"coupon"*) with no spoken sponsorship disclosure.

⚠️ **Caveat, stated because it would be easy to overclaim:** YouTube's paid-promotion disclosure lives in the description box and a UI badge, **neither of which appears in a caption track.** Transcript-absence is *not* evidence of non-disclosure. To r1's credit it volunteers the free alternative: *"If you'd rather run everything for free on your own hardware, the official docs cover that path."*

The structural point survives: a bundle in which every source recommends the same paid host carries a shared incentive, and a "you need a $6/month server" claim from such a bundle should not be read as a technical requirement. The README's own framing is *"Run it on a $5 VPS, a GPU cluster, or serverless infrastructure"* — one option among several.

## ⚠️ Verification-process failures in THIS audit

Recorded because the prime directive is not repeating a mistake twice.

1. **The first run's comparison was invalid and was nearly shipped.** It reported "rejected 6.4% vs selected 38.5%" by comparing this run's numbers against the 2026-09-03 scorecard — which used **different ground truth and live web access**. A narrower ground truth mechanically converts errors into UNVERIFIED. Caught before write-up; fixed by running the 6 selected sources as a control. **No cross-bundle error rate in this corpus is meaningful unless both bundles were graded by the same instrument.**
2. **The three "perspective-diverse" lenses were not diverse.** 110 of 140 panels (78.6%) in the reject run and 144 of 208 (69.2%) in the control were **unanimous**, and the reject run produced **0 no-consensus panels out of 140**. Same model, same three files — the diversity was prompt-deep only. This is the corpus's own *"same-instrument agreement is correlated error, not corroboration"* rule, violated by its own verification design.
3. **All 48 agents ran Haiku 4.5** — the configuration that lost 3 of 4 lenses to schema failures on the grok-bot ship one day earlier. It produced 0 errors here, but it also produced the ASR misgradings. The model was left unchanged for the control **deliberately**, because symmetry between bundles matters more than absolute grading quality for a comparison.
4. **My own extractor prompt caused the ASR misgrading.** It said *"preserve the speaker's own terms — a mis-said name is itself a finding."* Intended to prevent normalising away real mistakes; graders read it as licence to score caption artifacts as creator errors.
5. **`r3` is statistically empty and its 50% should never be quoted** — 20 claims, 18 UNVERIFIED, **2 settleable**. A rate on n=2 is not a rate.
6. **The completeness critic independently caught (1)** and named the missing ground-truth files. It also mis-derived per-source claim counts it had not been given, so its arithmetic is unreliable while its structural reasoning was correct.

## Deepen candidates

- ⭐⭐⭐ **Add an ASR-artifact guard to the grading pipeline.** Before any CORRECTED/FALSE verdict on a proper noun, check whether the correct spelling appears elsewhere in the same transcript or in the same creator's other transcripts. This would have caught 12 of 28 errors mechanically. It is the highest-value fix this corpus has surfaced in several ships, and it touches **every scorecard already written**.
- ⭐⭐⭐ **Re-grade the 2026-09-03 scorecard's 30 errors for ASR artifacts.** The per-source ranking and the "reach ≠ reliability" finding both rest on it.
- ⭐⭐ **Bound the engagement term** (`min(eng_ratio, 2.0)`) and **lower or remove `MIN_DURATION_SEC`**, which excluded a 253K-view source by 7 seconds. Bound first, measure after — Part 1's critic is right that reshuffling is not improvement.
- ⭐⭐ **Grade "did they run it?" as a first-class signal.** It separated these bundles more cleanly than any verdict count, and it is cheap to extract.
- ⭐ **Widen the ground-truth snapshot** to the docs site, release bodies, and the skills hub — 191 of 348 claims (54.9%) landed UNVERIFIED, and the critic named the exact files that would settle most of them.
- ⭐ **Portal pricing from a first-party page** — the one live number in r1 that nothing in-repo can confirm.
