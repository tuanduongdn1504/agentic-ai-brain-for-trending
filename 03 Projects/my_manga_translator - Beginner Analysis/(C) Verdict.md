# (C) Verdict — v256 `mranex/my_manga_translator`

**Date:** 2026-08-20 · **Branch:** `wiki/v256-my-manga-translator` off the v255 tip (`742f45f`) · **Not auto-merged.**

---

## 1. Phase 0.9 gate

| Criterion | Verdict | Evidence |
|---|---|---|
| **(a)** author is Anthropic / registered vendor-direct | **FAIL** | `mranex` is a pseudonymous individual — no bio, no location, no company, no website, 2 followers, 7 public repos; commits from `elsgman1999@gmail.com` at UTC+0700. **§41 is explicit:** (a) passes only on a declared Anthropic affiliation or a registered (a)-7 vendor-direct source. A handle, a heritage inference, a Vietnamese README and an operator-locale match are **all insufficient**, and §41 supersedes the v78 product-locale precedent by name. |
| **(b)** goal relevance | **MODERATE** ⚠️ *(OFF-GOAL recorded as the reviewable alternative)* | Argued in full at §2. |
| **(c)** novelty / interest | **STRONG** | An imported-then-deleted program still described by the dependency file; a deleted AI agent's memory whose prescribed fix still runs; a staleness mark that is declared, persisted, displayed and deliberately unenforced; a five-layer segment-alignment guard; a flagship README feature unreachable because a dataclass lacks a field; AGPL-3.0 asserted over Monotype's Arial and a MyFonts webfont kit; a hallucination-filter taxonomy committed under an obscenity. |
| **(d)** analysability | **STRONG** | 186 files, 54,977 lines, source-cloned twice, `diff -rq` clean both ways, complete 62-commit history with one root and one merge. Everything in this ship was read or measured. |

**⇒ GOAL-ALIGNED INCLUDE 3/4.** **§40 applies:** operator-requested, goal-adjacent, (b) MODERATE+ ⇒ **no override consumed, no §35 pressure**, OFF-GOAL recorded as the reviewable alternative.

---

## 2. The (b) argument, honestly

**The case against (the OFF-GOAL reading, at its strongest).** This is a manga-translation desktop application for hobbyist scanlators. It has **zero agent surface** — no `CLAUDE.md`, no `AGENTS.md`, no MCP server, no agent skill, no tool schema, nothing an agent can call (`git ls-files | grep -Ei 'claude|AGENTS\.md|\.cursor|copilot|llms\.txt|SKILL'` → nothing). It is not an agent, not agent infrastructure, and not a coding tool. Goal #1 is mastering Claude and autonomous agents **for software development**; a PyQt6 comic-lettering workbench is not that. Under this reading the subject is OFF-GOAL CAPTURE, admitted on (c) and (d) alone.

**The case for MODERATE, which I record as the verdict.** Four threads, weighed:

1. ⭐⭐ **It is a production multi-provider LLM-client application with a real prompt system.** Five translation backends behind one seam, a nine-style prompt library, a batch orchestrator, and per-provider response validation. This is the same architectural question as the `xsAI` seam the vault took from **v210** and the provider-agnostic seams from **v222 / v224** — read for architecture, not product.
2. ⭐⭐⭐ **Its architecture *is* the shape the operator's ratified candidate-LLM legibility ADR demands** — human-in-the-loop, per-stage inspectable artifacts, every intermediate correctable before the next step consumes it, staleness surfaced rather than hidden. The ADR requires *fixed + legible + audited + human-in-loop + eval-gated*; this subject implements four of those five as its product thesis, and the README argues for them explicitly.
3. ⭐⭐⭐ **It is an image → structured-text extraction pipeline, which is hireui's CV-parse problem**, and §5 of the Deep Dive extracts a directly-usable guard for the hardest failure mode in that problem. This is the strongest single thread and it is Goal #2, not Goal #1.
4. ⚠️ **Vietnamese-authored, operator-locale.** Recorded as context, and explicitly **not** counted toward (a) or (b) — §41 forbids exactly that inference.

**Why MODERATE and not STRONG:** threads 2 and 3 are genuinely valuable, but they are *architectural analogies and one borrowable guard*, not agent substrate. Calling it STRONG would put a comic-lettering tool on the same tier as MCP infrastructure. **Why MODERATE and not FAIL:** thread 3 is a direct, concrete, same-week contribution to a live product thread, and thread 2 answers a ratified ADR. That is a goal thread, not an absence of one.

**This is v255's shape exactly** — MODERATE keying the tier, OFF-GOAL defensible and recorded, §40 covering it without an override.

⚠️⚠️ **Precedent note, stated pre-emptively because the vault has got it backwards twice.** **NO MINT** (a pattern-library decision) and **OFF-GOAL** (a Phase-0.9 intake decision) are **orthogonal.** `llm-wiki-routine-v2.7.md` §40 names **AI-For-Beginners v191** (curriculum) and **mlsysbook v197** (textbook) among the precedents it covers and says of them: *"Under §40 these are simply GOAL-ALIGNED."* Both were **GOAL-ALIGNED and NO MINT simultaneously** — the same shape as this ship, and the same shape as v255. Declining a mint on domain-not-capability grounds is **not** an argument for OFF-GOAL, and at v255 a critic made that error and an anti-critic upheld it.

---

## 3. Mint decision — **NO MINT**

**Counts UNCHANGED: 46 confirmed patterns / 11 CONFIRMED Library-vocab. §C live standalones 51 unchanged. Tracked surface ≈58 unchanged. Max pattern #85. No N-bumps taken.**

**The strongest alternative, recorded and declined:** a §C standalone at N=1 — ***"Human-in-the-Loop Multi-Stage Media-Localization Workbench with Per-Stage Editable Cached Artifacts."*** It is genuinely distinctive on mechanism (the persisted `downstream_stale` mark plus a fully editable artifact at every one of ten stages), and I record it as reviewable. **Declined on five grounds:**

1. 🔴 **Domain-not-capability — decisive.** Manga/comic localization is a **domain**, and §C vocabulary is tool/capability-shaped. This is the settled line: **v197 mlsysbook** (*"a single-domain educational curriculum is not a recurring capability class"*), **v196 meetily** (corpus-first for a **domain** ≠ mintable), **v210 AIRI** (the AI-companion/VTuber domain), **v220 little-book-rl**, **v211 PixelRAG** (technique-not-capability). A desktop app for one media vertical is a domain slice.
2. 🔴 **Not world-first, and not even canonical.** The staged, GUI-driven, manually-correctable comic translator is an established product category with far larger incumbents. Under **v222** (*world-canonical is not world-first*) this subject cannot claim either: **32 page-stated stars, 62 commits, 14 days, one author.**
3. 🔴 **The differentiating machinery is not this repository's.** Every capability that makes the product work is a third-party model — PP-DocLayoutV3, Manga RT-DETR, DeepSeek-OCR, PaddleOCR-VL, LaMa-manga — and a meaningful slice of the code was **imported wholesale in commit #2** (§2 of the Deep Dive). This is an orchestrator over other people's models, which is **v242 D25** applied to the anchor itself.
4. 🔴 **Form-factor-within-a-genre.** A desktop GUI over an existing pipeline category is a form factor — the **v102** cookbook precedent and the **v236 / v227 / v222** front-end chain.
5. 🔴 **§28 anti-inflation** at **51 live standalones**, ≤2-per-ship cap, clustering-first — against a **bus-factor-one, 14-day-old, 32-star** anchor. The **v180 / v234** weak-anchor precedent.

**Any one of grounds 1–3 is sufficient. `inflation_check` HELD.**

**Recorded, not self-executed (audit business):**

- **#83 honest-deficiency-disclosure — POSITIVE, two instances**, and unusually sharp: the README discloses the Google Lens rate-limit/IP-ban risk, and the Developer Notes name the repo's own dead root scripts and tell you not to edit them. ⚠️ Set against the same document advertising an OCR provider that does not exist (§6) — **the same README is a #83 positive and a #83 negative, on different features.** That tension is worth an audit note.
- **#12 agent surface — a clean NEGATIVE, and richer than v255's.** Not merely absent: **inherited and deleted.** `.jules/bolt.md` was imported in commit #2 and removed on 2026-05-18.
- **#66 supply chain — a strong NEGATIVE exemplar** (two unsatisfiable pins, 10 of 24 requirements with zero importers, 20+ advisories against pinned versions, no lockfile or hashes). Useful as the counter-pole to **v228 pi**, the corpus's positive exemplar.
- **#19 author archetype** — `mranex` runs a small Vietnamese content-localization portfolio: `my_manga_translator`, **`translate-LN-pipeline`** (light novels — the text sibling to this image tool), `novel_studio`, `Anime_Vault`, `VOCra`. An ecosystem-portfolio-builder shape at small scale; recorded, not registered.
- **NOT #52.** 32 page-stated stars; and §37.4 — this environment mocks the GitHub API, so no velocity claim is available in any case.
- ⚠️ **The free-tier-harvester boundary, and I decline to stretch it.** The §C standalone minted at **v232** (crediting **v231**) is scoped to a *self-hosted **gateway** that re-exposes* a free consumer entitlement *as an API*. This subject is an **end-user application that consumes** Google Lens directly and **re-exposes nothing** — no local server, no OpenAI-compatible endpoint, no entitlement laundering. **It is an adjacency, not an instance**, and generalising that row to cover "any application that calls a free consumer endpoint" would silently fire its own promotion arithmetic. Recorded for the audit as a **boundary question**, not taken.

**Tier:** application/client tier (a desktop end-user product), ⚠️ tier assignment reviewable.

---

## 4. Streak and ceilings

- **Streak: v255 `GA:113` → `GA:114 · OG:13 [7 ov]`** — **37 consecutive GOAL-ALIGNED ships, v220 → v256.**
- **§35 CLEAR** — rolling window {**v254 GA**, **v255 GA**, **v256 GA**} = **0 OFF-GOAL**.
- **No override consumed** (§40). Lifetime operator overrides remain **10**; v153 → v256 = **zero**.
- ⚠️ **The audit is now 44 ships overdue** (last audit v212; v213–v256 all shipped).

**This ship adds to the audit agenda:** the §C alternative above; the **v232-row boundary question** (application-consumes vs gateway-re-exposes); the **fourth instance of the licence-vs-artifact class** and the first where the artifact is not code; the **`silent`-detector vocabulary finding** (§10 of the Deep Dive — its fourth consecutive null, on a codebase that *does* practise the doctrine, in Vietnamese); the **#83 positive-and-negative-in-one-document** tension; the **#12 inherited-then-deleted** refinement; and **D41/D42** below.

---

## 4½. The critic earned its keep — one real miss, one straw-man rejected

The 20-agent fleet crashed before its critic stages ran (D43), so I relaunched a two-agent **critic → adversary-over-critic** pass over the finished deliverables. It paid for itself twice, in opposite directions.

**🔴 It found a real defect I had missed, and I verified it myself before accepting it.** `detectors/comic_text_detector.py:9` is `from .matching import assign_text_regions_to_bubbles`, and `detectors/matching.py` defines six functions, none of them that one. It existed at `617d044` (`matching.py:143`) and was removed by **`2aebd41 "Remove CTD"` (2026-05-17)**; the import survived. **The module raises `ImportError` on load** — latently, because nothing imports it. ⭐ **It is the fourth and sharpest row of the ship's synthesis** (an artifact whose context was deleted), and **the concrete price of "no CI, ever": one `python -c "import detectors.comic_text_detector"` would have caught it the day it was made.** Added to the Deep Dive §11½ and to the defect list. ⚠️ Both the critic and the original fleet report cited it at line **10**; it is line **9**.

**✅ And the adversary-over-critic refused to rubber-stamp the critic's other main allegation** — that the OFF-GOAL reading is so much stronger that (b) MODERATE understates it. It read `llm-wiki-routine-v2.7.md` itself, quoted §40 and the v191/v197 precedents, noted that this Verdict already states NO MINT and OFF-GOAL are orthogonal and already records the OFF-GOAL alternative as reviewable, and called the allegation a straw-man. **The critic itself conceded "I would not have rated it differently."**

⭐⭐ **That is the v255 refinement working as designed.** v255's lesson was that pointing an adversary at the critic overturned nothing and *failed by upholding the one allegation that was checkable and false*, with the recommendation: **hand the adversary the routine text, not only the drafts.** I did — and this time the adversary upheld the true allegation and rejected the false one. **No change to (b); the miss is real and is now in the ship.**

*(Declined from the critic: a suggestion to add pseudocode for the alignment guard was taken — see the Pilot Menu. A complaint that "not held in memory" was imprecise was correct and the phrasing is fixed.)*

---

## 5. Method rules this ship proposes

**D41 — a pipeline's exit status is not your command's.** I recorded *"all 152 files byte-compile cleanly, exit 0"* and it was false: `python3 -m compileall` was **`Killed: 9`** and the `0` I read belonged to the `tail` at the end of the pipe. This is v255's `set -- $pair` failure in a new costume, and the general form is: **when a command's result matters, run it alone and read its own status.** Corollary, now pinned for this sandbox: **`python3` exists at `/usr/local/bin/python3` and is SIGKILLed on invocation** — it does not error, it dies, and inside a pipeline it dies *silently*. The vague "python3 is silently broken" note carried since v236 is now diagnosed.

**D43 — guard the return, and read the journal before you mourn.** The 20-agent fleet crashed **after 17 of 18 agents had finished** because four agents produced no schema-valid output, `pipeline()` dropped those items to `null`, and my final `return` did `mapResults.map(r => r.key)` with no null guard. Two rules follow. **(1)** Any `pipeline()`/`parallel()` result must be `.filter(Boolean)`-ed before its elements are dereferenced — the harness documents that a throwing stage yields `null`, and a schema-failing agent is a throwing stage. **(2)** A crashed workflow is not a lost workflow: **all 13 non-empty reports were recoverable from `journal.jsonl`**, which records each agent's actual return value. Recover first, re-run only what is genuinely missing — here, the critic and adversary-over-critic, relaunched as a two-agent follow-up.

**D42 — a negative from a truncated search is not a negative.** My first font pass (`strings -a | head -60`) returned almost nothing and I nearly recorded "the fonts are unremarkable." TTF name tables sit deep in the file and are frequently UTF-16BE; adding `strings -a -e b` and removing the `head` produced the entire §7 finding — Monotype, Blambot, a MyFonts `wfkit2` slug and a "DEMO" family name. **Before publishing a zero, state the extent of the search that produced it.**

---

## 6. The three things worth remembering

1. ⭐⭐⭐ **An unenforced check is a defect only when something claims it is enforced.** v250 called six rules non-negotiable and gated one; v252 headed a block *"Automated, Zero Tolerance"* and automated nothing; v247 committed a gate its own history violates 66 times in 82. **This subject persists a machine-readable staleness mark, shows it to the user, enforces nothing — and its README says exactly that.** The label matches the mechanism, and the human it defers to is in the loop by design. That is not a missing gate; it is a correctly-scoped one.
2. ⭐⭐⭐ **An artifact is safe when it carries its own context, and dangerous when its context lived somewhere else and has since gone.** Three artifacts in this repository outlived what made them correct, and all three still look authoritative: `requirements.txt` (its context was `app.py`, deleted 18 May); `_model_cache` and its two comments (their context was `.jules/bolt.md`, deleted in the same commit); and the committed `run_server.bat` (its context was one machine's config, and the generator that supersedes it is still in the tree). The counter-example is in the same repository — `downstream_stale` names the stages it invalidates, inside the artifact it invalidates, to the person who must act. **This generalises v255's D32/D40 by naming what "declared" buys you**, and it identifies the failure mode that is *worse* than staleness: a deleted rationale leaves an artifact that is currently correct and unmaintainable, because staleness can be detected by comparison and absence cannot be detected at all. ⚠️ **The vault's own instance is the CLAUSE-1 FAIL this ship closed** — five `_state/` files on disk, named nowhere, whose reason for existing lived only in the session that wrote them.
3. ⭐⭐ **Deleting a program does not delete its dependencies.** The purge commit removed 100% of the imported Flask application's source and 0% of its install cost, and four days earlier was the last time anyone edited `requirements.txt`. A dependency list is the last place anyone looks for dead code — and here it is the only surviving description of a program that no longer exists.

**Suggested next action:** review and merge `wiki/v256-my-manga-translator` (the chain v204 → … → v255 → v256 merges in order), then **do Rung 1 of the Pilot Menu** — ninety minutes, nothing installed, and it closes an open clause of the ratified candidate-LLM ADR with a test that needs no ground-truth corpus. Then **make v257 the audit**, now 44 ships overdue.
