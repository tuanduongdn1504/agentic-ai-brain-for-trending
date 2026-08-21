# (C) Verdict — v258 `mranex/VOCra`

**Date:** 2026-08-21 · **Branch:** `wiki/v258-vocra` off the v257 tip (`df1398c`) · **Not auto-merged.**

---

## 1. Phase 0.9 gate

| Criterion | Verdict | Evidence |
|---|---|---|
| **(a)** Anthropic / registered vendor-direct | **FAIL** | `mranex` is pseudonymous; two git identities over one email, commits at UTC+0700. **§41**: (a) passes only on a declared Anthropic affiliation or a registered (a)-7 vendor-direct source. Locale and heritage inference are exactly what §41 forbids, and the corpus already holds Vietnam-located solo developers (**v76**, **v231**). |
| **(b)** goal relevance | **MODERATE** ⚠️ *OFF-GOAL recorded as reviewable* | Argued at §2. |
| **(c)** novelty / interest | **STRONG** | One commit that deleted a three-layer application, its CLI, its GUI, its `.gitignore` and 252KB of its own planning documentation while adding 80 `.pyc`; 262KB of reasoning written in 2.4 days with 98.7% deleted; and the **N=3 same-author control**, which is the ship's actual contribution and which corrected me twice. |
| **(d)** analysability | **STRONG** | 93 files, 9,641 lines, cloned twice and byte-identical, a 6-commit history read end to end, and the deleted generations recovered from the pack. |

**⇒ GOAL-ALIGNED INCLUDE 3/4.** **§40 applies:** operator-requested, goal-adjacent, (b) MODERATE+ ⇒ **no override consumed, no §35 pressure**, OFF-GOAL recorded as reviewable.

---

## 2. Why (b) moves *down* to MODERATE from v257's STRONG

Stating this because the tier moves in the opposite direction from the previous ship, and a later audit should see the reasoning rather than infer it.

**v257 rated STRONG** because the LLM *was* the subject: thirteen versioned prompt templates, a render engine with an override chain, a response parser, a step registry, a canon layer whose purpose was prompt-size control. Strip the light novels away and an LLM-workflow system remained.

**Strip the video away here and what remains is computer vision.** Frame extraction, interactive region cropping, SSIM deduplication, OCR provider plumbing, segmentation and frame-to-timestamp arithmetic, text cleaning, ffmpeg burning — that is the bulk of the 9,641 lines. The translator package is **~490 lines of 9,641**, and the LLM is one stage bolted to the end of a CV pipeline. **That is v256's shape, and v256 was MODERATE.**

**What is genuinely on-goal, ranked honestly:**

1. ⭐⭐⭐ **The N=3 same-author control itself** — a method contribution, not a property of the subject. Three repositories by one author in three consecutive ships is a natural experiment the corpus has never had, and §4 of the Deep Dive is the result.
2. ⭐⭐ **The cheap-deterministic-filter-before-the-expensive-model pattern** (SSIM dedupe in front of OCR) — the one *new* transferable idea, and the Pilot Menu's Rung 1.
3. ⭐ **The provider Protocol + factory** (19 + 17 lines) — a tidier version of a pattern the corpus already has.
4. — **The alignment guard** is already banked at v256; its value here is evidential (§5), not new.

**The OFF-GOAL reading, recorded:** this is a hobbyist tool for ripping subtitles off pirated video, with zero agent surface, 3 page-stated stars, and no dependency manifest. A reader who weights "is this agent or LLM infrastructure?" above "does it teach me something measurable" should land on OFF-GOAL CAPTURE. Under §40 the ship is GOAL-ALIGNED either way, and I record MODERATE because items 1 and 2 above are real and were not available from the siblings.

⚠️⚠️ **Precedent note, fourth consecutive ship.** **NO MINT** (pattern-library) and **OFF-GOAL** (Phase-0.9 intake) are **orthogonal.** `llm-wiki-routine-v2.7.md` §40 names **AI-For-Beginners v191** and **mlsysbook v197** — both NO MINT — and calls them *"simply GOAL-ALIGNED."* At v255 a critic conflated them and an anti-critic upheld it; at v256 and v257 the adversary caught it both times.

---

## 3. Mint decision — **NO MINT**

**Counts UNCHANGED: 46 confirmed patterns / 11 CONFIRMED Library-vocab. §C live standalones 51 unchanged. Tracked surface ≈58 unchanged. Max pattern #85. No N-bumps taken.**

**The alternative, recorded and declined:** a §C standalone at N=1 — *"Burned-In Subtitle Extraction Pipeline: region crop → SSIM frame deduplication → local VLM OCR → LLM translation, in one desktop workbench."*

**Five grounds:**

1. 🔴 **Domain-not-capability.** Subtitle extraction is a domain; §C vocabulary is capability-shaped (**v197**, **v196**, **v210**, **v220**).
2. 🔴 **Not world-first, and not remotely canonical.** Burned-in subtitle OCR is long-established territory — VideoSubFinder and `videocr` occupy exactly this space. Under **v222** (*world-canonical is not world-first*) a **3★ / 6-commit / 2.4-day** repository claims neither.
3. 🔴 **§28 anti-inflation** at **51 live standalones**, ≤2/ship, against **the weakest anchor of the three siblings** — bus factor one, no dependency manifest, no licence file (**v180 / v234** weak-anchor precedent).
4. 🔴 **Form-factor-within-a-genre** — a desktop GUI over an OCR pipeline (**v102**; the **v236 / v227 / v222** front-end chain).
5. 🔴 **Both siblings were declined on five grounds each, one and two days ago.** Minting the third of three would need a distinction that does not exist.

**Any of grounds 1–3 is sufficient. `inflation_check` HELD.**

**⭐ Recorded for the audit — not a mint, and deliberately not phrased as one:**

- ⭐⭐⭐ **A METHOD NOTE: the same-author control.** When the operator requests consecutive repositories by one author, the *comparison* is worth more than either subject. Three points let you separate a developer's **dispositions** (what replicates regardless of project) from their **attention** (what varies with what they were looking at). This ship is the corpus's first N=3 of that kind, and the shape is reusable — it belongs in the routine's method section, not in §C.
- ⭐⭐ **An observation, not a capability: "code moves forward, never backward."** In a solo multi-project toolchain an improvement invented in project N reaches N+1 by copy-forward and never reaches N−1, because nothing carries it back. Evidence at Deep Dive §5. This is an argument for extracting shared libraries; it is not §C vocabulary.
- ⭐⭐ **"A plan document is a fence around the surfaces it names."** Deep Dive §3 measures it: the one layer the surviving plan discusses is shared by import; every layer it omits was copy-pasted, one byte-for-byte, plus a 788KB icon committed twice.

**Recorded, not self-incremented:**

- **#12 — a clean NEGATIVE, now same-author N=3.** Zero agent-surface files and zero `.yml`/`.yaml` on any ref in all three repositories.
- **#66 — the strongest of the three on egress and secrets, the weakest on declaration.** Zero hardcoded URLs in 75 files; secrets in a separate file with an env override and an explicit pop-before-save. But **no dependency manifest at all** (§4) and ten committed `.pyc`.
- **#83 — POSITIVE and NEGATIVE in one document, third consecutive ship.** POSITIVE: `vocra_translator/plan.md` states its decisions plainly and the code honours the load-bearing one. NEGATIVE: two unmeasured headline percentages, a licence claimed in prose with no file, and a logo that 404s.
- **#19 — the author archetype's third data point.** manga (image) → light novels (text) → video (subtitles): three halves of a Vietnamese content-localization toolchain, alongside `novel_studio` and `Anime_Vault`.
- **NOT #52** (3 page-stated stars; §37.4 — the API is mocked).
- **Tier:** application/client, ⚠️ reviewable.

---

## 4. ⭐ The README is load-bearing for two things convention puts in files

Worth isolating because it unifies three separate defects.

- **The licence** is a sentence at `README.md:169` claiming MIT. There is **no licence file** among the 93 tracked files and none in any of the 6 commits.
- **The dependencies** are a bare `pip install PySide6 numpy opencv-python Pillow pillow_heif requests scikit-image` at `README.md:129` — **seven packages, zero version pins.** There is **no `requirements.txt`, no `pyproject.toml`, no manifest of any kind.**
- **And the top of that same README is broken:** its logo links to `https://github.com/your-username/vocra` and loads an image from the matching raw URL. Both return **HTTP 404**.

⇒ **The one file carrying the licence grant and the dependency set is also the file with an unfilled template placeholder in its first element.**

⭐ **And it completes a three-way divergence with the siblings on both axes**, which is the §4 pattern of the Deep Dive in miniature:

| | licence | dependencies |
|---|---|---|
| v256 | AGPL-3.0 **file**, added by the final commit | `requirements.txt`, 24 lines, **two unsatisfiable pins** |
| v257 | **none at all**, no claim | `requirements.txt`, 3 lines, clean |
| v258 | **MIT claimed in prose** | **no manifest**, 7 unpinned packages in prose |

For the operator this makes v258 the **most permissive** of the three: v257 grants nothing, v256 grants AGPL, and this one at least states MIT — while being the least reproducible, since nothing pins what it needs.

---

## 5. Streak and ceilings

- **Streak: v257 `GA:115` → `GA:116 · OG:13 [7 ov]`** — **39 consecutive GOAL-ALIGNED ships, v220 → v258.**
- **§35 CLEAR** — window {**v256 GA**, **v257 GA**, **v258 GA**} = **0 OFF-GOAL**.
- **No override consumed** (§40). Lifetime operator overrides remain **10**; v153 → v258 = **zero**.
- ⚠️ **The audit is now 46 ships overdue** (last audit v212; v213–v258 all shipped). ⭐ **Three consecutive same-author ships have produced a method contribution that belongs in the routine, which is an audit act — this is the strongest argument yet for making v259 the audit.**

---

## 6. Method rules this ship proposes

**D46 — a clean tree is not a clean history; enumerate the pack.** My tree-level import trace found zero dead modules in VOCra, and I sanity-tested the detector against a planted name before trusting it. It was still the wrong question: `git rev-list --objects --all | git cat-file --batch-check` exposed a deleted 93KB GUI, a deleted `app/` service layer, a deleted `cli/`, and **252KB of deleted documentation** — which became the ship's two best sections. **Before concluding a repository has no dead generations, list the largest blobs across all refs and check which are absent from `git ls-files`.**

**D47 — anchor the basename in filename greps.** I tested for a dependency manifest with a pattern including `setup\.py` and got a hit — on `vocra_gui/scene_setup.py`, because grep matches substrings. The honest answer was *no manifest exists*. **A filename test must anchor (`-x`, `$`, or a basename comparison), or it will confirm whatever it is looking for.**

⭐ **And the standing one, now on its third consecutive ship.** v256: a truncated font search. v257: three misattribution traps (**D45**). v258: the tree-versus-pack blind spot, plus a `|| echo` attached to `head` rather than `grep` (**D41**, in my own hands one ship after writing it). **The consistent shape: I am reliable when I read a file and quote it, and unreliable when I generalise from where I chose to look.** Every negative in this ship therefore states the extent of its search.

---

## 7. The three things worth remembering

1. ⭐⭐⭐ **He wrote 262,074 bytes of planning and progress documentation in 2.4 days and deleted 98.7% of it — and the 3,306-byte survivor is the only place in three repositories where a stated decision is honoured by the code.** The ladder is the detail: a 2,064-line agent-style progress log and a 1,178-line plan, both deleted the same day; replaced by 157 lines, deleted the next day; replaced by 75 lines, kept. **The smallest document is the only one that did any work.**
2. ⭐⭐⭐ **A plan document is a fence around exactly the surfaces it names.** The surviving plan discusses the translator core — which is genuinely shared by import (`provider_factory.py:3–5`). It says nothing about widgets, so `scene_nav_button.py` is a **byte-identical 117-line copy** in both apps, `log_panel.py` differs by two lines, and a **788,588-byte icon is committed twice.** The actionable form: **name the boring surfaces too.**
3. ⭐⭐⭐ **Code moves forward in time, never backward.** The alignment guard was invented in v256 on 2026-05-15, carried into v258 eleven days later with a near-identical error string, and never backported into v257 — which was committed to six times after that date, including on the last recorded day of all three repositories. Nothing in a copy-forward workflow ever runs in reverse, and that is the whole argument for a shared library: **it is the only mechanism that makes a fix travel backwards.**

**Suggested next action:** review and merge `wiki/v258-vocra` (the chain v204 → … → v257 → v258 merges in order), then **Rung 1 of the Pilot Menu** — ninety minutes, nothing installed: the cheap-deterministic-filter-before-the-expensive-model pattern, and the plan-as-fence rule applied to the vault's own copied-between-projects skills. Then ⭐ **make v259 the audit.** It is 46 ships overdue, and this three-ship run has generated a method contribution (the same-author control) that only an audit can actually adopt.
