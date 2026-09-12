# Topics Queue

> Topics waiting for autopilot research routine to process.
> One topic per `## ` heading. Topics are processed top-to-bottom.
> When a topic is completed, move it to the "Completed" section at bottom.
>
> Format per topic:
> - **Query:** the search string handed to yt-search
> - **Anchors:** (optional) YouTube URLs to FORCE-INCLUDE in the bundle before yt-search picks the rest.
>   Format: nested bullet list under `**Anchors:**`. Up to `SOURCES_PER_TOPIC` (6) URLs.
>   Added 2026-05-14 after 4 of 6 user-named anchors got dropped by the search-rank rubric on 2026-05-13.
>   Example:
>     - **Anchors:**
>       - https://www.youtube.com/watch?v=ABC123
>       - https://www.youtube.com/watch?v=DEF456
> - **Notes:** optional hints (specific creators, deliverable type, follow-ups)
> - **Queued:** date queued
> - **Status:** pending / in-progress / completed
>
> Tools:
> - `python bin/autopilot-drain.py --list-only` — parse + show queue (no network, no log)
> - `python bin/autopilot-drain.py --dry-run`   — show selection plan (yt-search runs, no NotebookLM)
> - `python bin/autopilot-drain.py`             — full drain

---


## Completed

### Hermes Agent RUBRIC-REJECT AUDIT — grading the 5 sources the selection formula threw away ✅
- **Drained:** 2026-09-12 by `/loop`. **An audit OF THE SELECTION RUBRIC, not a new topic and not an ordinary revisit.** Corpus stays at **80**. Operator asked the usual opening question — *"Can I start build knowledge from this video with loop or anything in queue now?"* (**5th time** that exact question has opened a ship) — and the answer was unusual: **the video was already in this corpus, by name, on the 2026-09-03 manifest's list of "High-reach candidates the rubric dropped."** It had been surfaced, scored and rejected nine days earlier, and had since **more than doubled: 140,334 → 294,324 views (+109.7%)** while its two sibling videos on the same channel moved +1.5% and +2.3%. Operator elected **"audit the rubric's rejects"** over anchor-only, over a third full re-drain, and over skipping. Queue was empty (0 pending, confirmed two ways); launchd armed for 23:35.
- **Raw analysis:** `raw/2026-09-12-hermes-agent-rubric-reject-audit/` (`_sources.md` + 5 EN transcripts, 25,035 words). Fetch guard **PASS 5/5, 0 recoveries**.
- **Wiki output:** [[../wiki/hermes-agent/rubric-reject-audit-2026-09-12]] — **1 NEW article** + `_index.md` updated in place (header banner, scorecard table, a ⚠️ qualification on the 2026-09-03 per-source ranking, articles table, and a new 🔴 operator-relevance item). **348 claims graded across two bundles.**
- **Verification:** `wf_660869eb-780` (5 rejects, 24 agents) **+ matched control** `wf_93eb57c0-9b3` (the 6 SELECTED sources re-graded through the identical pipeline against the identical ground truth, 24 agents). 48 agents, 3.70M tokens, **0 errors, 0 empty**. Ground truth was **one pre-fetched local snapshot** shared by every verifier — which closed the silent GitHub-rate-limit failure and the grounder-fabrication failure from the two prior ships in one design decision.
- **NotebookLM:** none (25K words is direct-read range; a claims scorecard cannot grade a paraphrase).
- **Result:** ⭐⭐⭐ **A THIRD TO A HALF OF WHAT THIS CORPUS GRADES AS "CREATOR ERROR" IS SPEECH-RECOGNITION FAILURE.** Across 11 transcripts the vendor's name is rendered **"Nous Research" 6×, "News Research" 5×, "new research" 5×, "Nouse Research" 1× — 11 of 17 mentions garbled**, and every garble became a CORRECTED or FALSE verdict *against the creator*. Two proofs it is the machine, not the speaker: **`t4-wanderloots` contains both spellings in one transcript** (a human does not alternate), and **Metics Media says "OpenClaw" correctly in one video and "Open Cloud" twice in another**. Worst case: the operator's own 2026-09-03 anchor was graded **FABRICATED** — the harshest verdict in the taxonomy — for *"around August 2016"* in the **English auto-translation of a Vietnamese video**, after the extractor had itself written *"LIKELY GARBLED"* into the claim. ⭐⭐⭐ **The rubric is accuracy-NEUTRAL.** Matched control, same instrument: rejects **9 errors / 61 settleable = 14.8% raw → 9.8% corrected**; selected **19 / 96 = 19.8% raw → 10.4% corrected**. **Indistinguishable.** The case for changing the rubric rests on mechanics, not quality. ⭐⭐ **The mechanics are still broken:** `eng_ratio * 3` is **unbounded**, so a **17-subscriber** channel scored **676.22** against a field of 6.85–14.01 — **the engagement term alone contributed 671 of its 676 points (99.2%)** — while `log10(views)` spans just 2.02 points across the whole pool, making reach nearly a constant. A **253,592-view** source was excluded by `MIN_DURATION_SEC=300` **at 293 seconds — by 7 seconds** — having scored #3 of 11. The operator's video missed the last slot **by 0.31 points**. The score model **reproduces the real 2026-09-03 selection exactly**, which validates it. ⭐⭐ **4 of the 5 rejects demonstrably RAN the product on screen** (r1's live OpenRouter billing page: **13 cents / 105 requests / ~4M tokens**, three-quarters cache-served); **the one that did not is the one the duration floor excluded** — right outcome, wrong reason. ⭐⭐ **"HermesOS" is settled at its origin**: Tina Huang says *"my Hermes setup, my Hermes OS"* — a possessive for her own rig, never a product claim; the term appears **0×** in all ground truth. 🔴 **The vendor documents no prompt-injection risk at all** — "inject"/"untrusted"/"malicious" appear **0×** in README and desktop README, while a 294K-view third-party tutorial warns about it explicitly. ⚠️ **The 2026-09-03 "anchor is most accurate / reach ≠ reliability" headline can no longer bear its weight** — all four of the largest-reach source's errors and the anchor's only error are transcription artifacts (this does NOT clear either of genuine defects outside a README's reach, e.g. the Ollama Cloud trap). ⚠️ **The corpus's "no-code is MISLEADING" verdict is now TIME-BOUND** — `apps/desktop/README.md` says verbatim **"no terminal required"**. ⚠️ **All 5 rejects route through Hostinger** (correlated incentive; caveated because YouTube disclosure lives outside caption tracks). ⚠️ **6 verification-process failures recorded, including one caught before ship:** the first run's cross-bundle comparison was **invalid** (different ground truth than the 2026-09-03 scorecard) and was nearly written up — fixed by running the control; the three "perspective-diverse" lenses were **not diverse** (**110/140 unanimous, 0 no-consensus panels out of 140**); all 48 agents ran **Haiku**; and **my own extractor prompt caused the ASR misgrading**.
- **Infra fixed this session:** committed the `parse_queue()` silent-skip fix, and **diagnosed `--list-only`'s `rc=137`** — `/usr/local/bin/python3` is a symlink to a Python **3.7** framework carrying **only i386 + x86_64 slices, no arm64**, so it is SIGKILLed on this machine before executing a byte, and it sits **first on PATH**. Not a script bug. The launchd path is unaffected because `autopilot-drain.sh` sources the venv. **This also retroactively explains the grok-bot ship's "`vtt-to-md.py` killed exit 137"** — the exact file that failed converts cleanly via the venv interpreter (rc=0, 621 cue lines, 4,531 words), **proven not inferred**.
- **Deepen candidates:** ⭐⭐⭐ **add an ASR-artifact guard to the grading pipeline** — before any CORRECTED/FALSE on a proper noun, check whether the correct spelling appears elsewhere in the same transcript or the same creator's other transcripts; this would have caught **12 of 28 errors mechanically** and it touches **every scorecard already written** · ⭐⭐⭐ **re-grade the 2026-09-03 scorecard's 30 errors for ASR artifacts** — the per-source ranking rests on them · ⭐⭐ **bound the engagement term** (`min(eng_ratio, 2.0)`) and **lower/remove `MIN_DURATION_SEC`** · ⭐⭐ **grade "did they actually run it?" as a first-class signal** — it separated the bundles more cleanly than any verdict count · ⭐ **widen the ground-truth snapshot** (docs site, release bodies, skills hub) — **191 of 348 claims (54.9%) landed UNVERIFIED** · ⭐ **Portal pricing from a first-party page** · ⭐ **fix `autopilot-drain.sh`'s dead `EXIT_CODE=$?`** — under `set -e` the script aborts at the failing command, so the "drain exited rc=N" line can only ever record success



### Grok Bot — SpaceXAI persistent cloud-VM agents (VN same-day hands-on anchor) ✅
- **Drained:** 2026-09-11 by `/loop` (operator anchor `CqhE6qPoEAs` **Quân IT** VN "Grokbot | Elon knows how to build product" + yt-search ×5 on query `Grok Bot xAI`, selected via `bin/autopilot-drain.py --dry-run`; **two-word query chosen over the probe's higher-scoring `Grokbot`** to keep third-party "grokbot" projects out of the picks; anchor validation **PASS 1/1, overlap 100%**; **fetch guard PASS 6/6, no recoveries**). **NEW topic — corpus 79→80.** Operator asked whether anything in the queue blocked building from the video and elected **full 6-source bundle** + **fix the queue bug now** (both recommended options). **The queue was genuinely empty — and checking that found a silent-skip bug, fixed in the same session.**
- **Raw analysis:** `raw/2026-09-11-grok-bot-xai-persistent-agents/` (`_sources.md` + 6 transcripts, 24,506 words + 1 VN `vi-orig` VTT)
- **Wiki output:** [[../wiki/grok-bot/_index]] — **NEW topic**, 8 files; **93 wikilinks validated 0 broken**; **160 claims / 0 FABRICATED** (anchor: 7 CONFIRMED / 8 CBI / 3 CORRECTED / 1 MISLEADING / 16 UNVERIFIED / 1 UNFALSIFIABLE); 3 main-loop overrides logged
- **NotebookLM:** none (yt-dlp captions read in full — the drain's mandatory step 3/5 **deliberately skipped** per Rule 7 in favour of the last six ships' practice; `notebooklm auth check` passes, so a choice not a failure)
- **Result:** 🔴 **THE LOAD-BEARING FACT, AND THE BUNDLE GOT IT BACKWARDS 4-TO-2** — the launch page says *"Bots have their own computer"*; `docs.x.ai/grok-bot/faq` says *"Every Bot on your account uses one persistent cloud computer… assigned **per user, not per Bot**. **Do not use separate Bots as a security boundary.**"* One **Firecracker microVM per user**, sharing files/browser sessions/logins. The four wrong sources **all recite the same headline — one vendor simplification propagated four times**, so majority count is worthless and a prompt-injected bot **inherits every credential on the machine**; the bundle's own demos put a plaintext-credential `.env` and a card-on-file session inside that blast radius on camera. The two that got it right: a $200-skeptic and a crypto-promo channel; the two wrong include the **paid sponsored** walkthrough and the **312K-view flagship** — **neither reach, sponsorship nor independence predicted accuracy where being wrong is expensive.** ⭐⭐ **THE VENDOR RENAMED ITSELF AND ALL 6 SOURCES MISSED IT** — SpaceX acquired xAI **2026-02-02**, entity is **SpaceXAI LLC** (x.ai's own copyright line), rebranded July 2026, two months *before* Grok Bot shipped; **a pre-flight lens scoped to first-party surfaces fetched the right page and read past the notice** because it was checking *whether* the product was official, not *who owns it*. **Garble self-corrects across sources; a stale-but-live brand name fails all six together** — 3rd instance of correlated upstream error after the Hermes vendor-seeded claim. ⭐⭐ **THE PRICING "CONTRADICTION" WAS A TIMELINE** — the pre-flight critic returned **do-not-ship** over it; there is **no Grok Bot price at all** (no SKU, launch page names no figure), the floor fell **$200→$60→$20** Aug 11/21/26 by *expanding eligibility*, Nate's *"Is It Worth $200?"* was right when asked and expired 12 days later, and averaging $200 and $20 gives $110 — **true on no day**; underneath sit an **unpublished** weekly quota and **uncapped** overage in arrears. **Cursor is a co-vendor gating access and billing**, which the anchor's "xAI/Elon built this" frame misses. ⭐⭐ **THE ANCHOR'S "BLOCKCHAIN PRODUCT" ERROR HAS A DOCUMENTED INTERNAL ORIGIN, ON CAMERA** — he'd tried to build a **DePIN-style idle-compute marketplace** (*"distributed system để cho những cái con AI nó có thể access được vô những cái VM á mà mình bỏ trống"*), a category that genuinely is blockchain-settled and whose own 2026 pitch is verbatim **"always-on AI agents"**; not a scam-token confusion, and **the explanation sat 20 seconds into a transcript the main loop had already read** — missed because the interesting hypothesis crowded out the cheap one, so a **15-agent scam investigation ran against the wrong question.** ⭐⭐⭐ **THE METHODOLOGICAL FINDING, which indicts this corpus's own metric: the scorecard rewards reciting and punishes doing** — best score (5.9% error / 64.7% CONFIRMED) = the **paid sponsored** source with **zero security reservations in 3,148 words**; worst CONFIRMED (19.4%) + highest UNVERIFIED (44.4%) = the **only source that installed it from zero**, unauditable **by construction**; a source with **no evidence of installing it** posts the 2nd-highest CONFIRMED *and* the highest error rate. **Report the error SIGNATURE, not the rate.** **The Hermes "operator's anchor was most accurate" finding does NOT replicate** — ~11% hard error **again** (11% → 11.1%, strikingly stable) but **rank 3rd of 6, because rank is a property of the companion set**; *"reach ≠ reliability"* **inverts** at the extremes here. Anchor has **0 FALSE / 0 CONTRADICTED** — only source besides the paid one — while 3 of 5 companions assert things their own artifact never showed them. **CBI dominates: the defect is omission, not invention.** ⚠️ **8 of this ingest's own errors recorded**, incl. quoting the launch page's marketing sentence to the operator as verified fact **and passing it to 14 agents as ground truth** (two graders overturned it — *a launch announcement is marketing, not documentation*), misnaming the vendor 3× off the page that names it, and **writing a guessed explanation into two committed files**. ⚠️ Pre-flight `wf_8c75e04e-3e8` ran **all-Haiku** and **lost 3 of 4 lenses to schema failures**, then reported the survivor as a `1/1` tally fed to 3 refuters as consensus; compile `wf_c3cb4b9e-bbe` **pinned to Opus: 14/14, 0 errors, 0 empty**, 1.35M tokens. ⚠️ **`bin/vtt-to-md.py` killed exit 137** on the 1-hour caption track; **`--dry-run` still emits no video IDs**; `en` fetch hit **429**, not retried. ⚠️ **Same-author corroboration is not corroboration** (How I AI's own companion page). 🔴 **hireui: DO NOT pilot against candidate data** — shared sessions + shared filesystem + *"training opt-out follows the applicable Cursor account and privacy settings"*; same **BOLA**-shaped class flagged as this operator's #1 unmitigated risk.
- **Deepen candidates:** ⭐⭐⭐ **install it and test the shared-machine boundary directly** — every unresolved security question collapses on one hands-on hour and no further video will settle any · ⭐⭐⭐ **docs-first ingest of `docs.x.ai/grok-bot/*`** — the docs outperformed all six videos on every contested fact, same result as the Homebrew ship; *on any topic with a first-party owner, read the owner's docs before the commentary* · ⭐⭐ **pin publication dates into the grader prompt** — a dated claim measured against a live page manufactures false errors (happened here: Alex Carter graded "stale by five tiers" against today's page, corrected to three) · ⭐⭐ **fix `vtt-to-md.py`** for hour-long tracks + **make `--dry-run` emit video IDs** so bundles are replayable · ⭐⭐ **report error signature, not error rate** · ⭐ **third anchor-audit datapoint** — two bundles at ~11% makes a third a trend · ⭐ **the Cursor relationship** — a co-vendor gating access to a SpaceXAI product is odd and unexplained by any source here


### Hermes Agent REVISIT — VN no-code replication test + v0.18→v0.21 refresh ✅
- **Drained:** 2026-09-03 by `/loop` (operator anchor `k8lz9P3MrlM` **holetex** VN "Cài Trợ Lý AI Cá Nhân Từ Số 0 (Không Cần Biết Code)" + yt-search ×5 on query `Hermes Agent Nous Research setup tutorial`, selected via `bin/autopilot-drain.py --dry-run`; anchor validation **PASS 1/1, overlap 100%**; **fetch guard PASS 6/6 after 1 recovery** — 2nd occurrence of the silent `--sub-langs` failure class first logged on the Homebrew ship, and the guard that ship recommended caught it on first use). **REVISIT of an existing topic — corpus stays at 79.** Operator elected **run now** + **FULL 6-source re-drain** (widest of 3 offered scopes) over the recommended anchor-only revisit; **the stated overlap risk did not materialise — 0 of 6 videos overlap the 2026-07-18 bundle** (1 creator overlap, different episode).
- **Raw analysis:** `raw/2026-09-03-hermes-agent-revisit/` (`_sources.md` + 6 EN transcripts 27,703 words + 1 VN original 12,536 words + 18 VTT tracks)
- **Wiki output:** [[../wiki/hermes-agent/_index]] — **3 NEW articles** ([[../wiki/hermes-agent/revisit-2026-09-03]] + [[../wiki/hermes-agent/the-vendor-seeded-false-claim]] + [[../wiki/hermes-agent/hermes-desktop]]) + **6 existing files corrected in place**; 14 files; **137 wikilinks validated 0 broken**; **78 claims: 34 CONFIRMED / 15 MISLEADING / 14 UNVERIFIED / 9 FALSE / 6 CORRECTED / 0 FABRICATED** (majority-with-severity-tiebreak; 14 no-consensus panels hand-adjudicated to the primary-source lens; 13 overrides logged)
- **NotebookLM:** none (yt-dlp captions read in full — a claims scorecard cannot grade a paraphrase)
- **Result:** the replication test asked whether the 4 prior FALSE claims were creator-specific or genre-wide, and **returned a third answer the design did not anticipate — VENDOR-SEEDED.** ⭐⭐⭐ The one claim that replicated is the one **Nous Research still publishes in its own README** (*"It's the only agent with a built-in learning loop"* — first paragraph, live 2026-09-03, 47 days after this corpus graded it FALSE), and the anchor reads it off the GitHub page **attributing it correctly** (VN [00:55] *"ở đây họ mô tả"* = "here **they** describe"). The 3 claims the vendor does **not** own drew **0 repeats and 5 contradictions** across 6 independent sources. **Origin predicts recurrence; fidelity is not accuracy** — a careful creator quoting the vendor reproduces the vendor's falsehoods more reliably than a careless one, so the only fix is upstream. ⭐⭐ **The operator's own anchor was the MOST accurate source in the bundle — 11% error rate (7/9 CONFIRMED, 0 MISLEADING) vs 50% for the largest-reach source (398,873 views)**; "reach ≠ reliability" holds at the extremes only, with no monotone trend at N=6. ⭐⭐ **`hermes-desktop` closes a real gap** the prior CLI-shaped query structurally could not see (first-party in-tree `apps/desktop/`, MIT, macOS/Windows/Linux; a true no-code installer exists but is the *un*-recommended path, while the "no coding needed" anchor demonstrates a VPS terminal session; **HermesOS does not exist** — 0 org results, creator coinage). 🔴 **Ollama Cloud trap** — two sources present Ollama as the local/private route; the documented integration is a **cloud service on an API key** (`https://ollama.com/v1`), which compounds the standing data-residency blocker for candidate PII. **The star count is this project's most-misreported fact**: ~7,000 → 140,000 → 200,000+ across three sources vs **240,313** verified, no two agreeing. **47-day drift:** v0.18.2→**v0.21.0**, 6→**7** backends (+Vercel Sandbox), 27→37 tags, open issues **+63.6%** against +10.9% stars, **10 releases in 54 days**. ⚠️ **10 verification-process failures recorded — 6 of them agents asserting untruths**, incl. a grounder that **fabricated a 20-platform enumeration absent from the README** (propagated into the wiki, then reverted on manual re-read), a critic that **"confirmed" figures by reading this wiki** (circular), 2 confabulated multi-source patterns disproved by `grep`, and **a skewed claim cap of my own** that excluded 100% of two sources and 8 of the operator's 9 anchor claims — caught by self-audit and fixed with a 2nd 133-agent run, which revealed **the excluded sources were the least accurate**. ⚠️ **GitHub API rate limit exhausted mid-run** (60/hr unauthenticated → 0 across 248 agents). ⚠️ **Token budget breached loudly: 248 agents / 16.42M tokens.**
- **Deepen candidates:** ⭐⭐⭐ **`git clone` the repo** — 6 UNVERIFIED verdicts are document-shaped and collapse on inspection (memory filenames · real built-in skill/tool counts · whether `apps/desktop` bundles Bot Mode · whether the Ollama endpoint can point at localhost); no further video will settle any of them · ⭐⭐⭐ **switch fan-out verification to `raw.githubusercontent.com` and/or an authenticated token** — the 60/hr unauthenticated API ceiling is a structural cap above ~20 agents and it fails *silently* into UNVERIFIED · ⭐⭐ **adopt majority-with-severity-tiebreak as the corpus default panel rule** (worst-wins overstated MISLEADING here by 46%; only 11 of 34 first-run panels were unanimous) · ⭐⭐ **never sort-then-cap on a boolean** — stratify by source so no source can reach zero coverage · ⭐⭐ **re-drain mature topics on a deliberately different query** to surface what the first query structurally could not see (this is exactly how Desktop appeared) · ⭐ a **browser-capable fetch path** for JS-rendered first-party sites (Nous Portal + docs) — 3 unresolved items are blocked on it and `curl` cannot fix it · ⭐ read the **v0.19/v0.20/v0.21 release notes in full** (only summaries were read; "Security & Reliability" sections spotted, not mined) · ⭐ **Tonbi's "Better than OpenClaw? Testing Hermes Agent w/ Qwen 3"** (18,072 views) — the pool's only **critical-comparison** stance, and **this bundle has zero critical sources**


### AI text watermarking — Anthropic's invisible mark on Claude output (EU AI Act Article 50) ✅
- **Drained:** 2026-08-21 by `/loop` (operator anchor `5R9Nw8eKDCA` BizMate AI Official + yt-search ×5 on query `Anthropic Claude watermark AI generated text`, selected via `bin/autopilot-drain.py --dry-run` after probing 3 candidate queries; anchor validation **PASS 1/1, overlap 100%**; **fetch guard PASS 6/6** — the ⭐⭐ deepen candidate from topic #78, implemented)
- **Raw analysis:** `raw/2026-08-21-ai-text-watermarking-claude-eu-ai-act.md`
- **Wiki output:** [[../wiki/ai-text-watermarking/_index]] — 13 files; 70 wikilinks validated 0 broken; **101 claims: 76 CONFIRMED / 8 UNVERIFIED / 6 CBI / 3 CORRECTED / 2 MISLEADING / 2 FALSE / 2 UNFALSIFIABLE / 1 TIME-BOUND / 1 CONTRADICTED-IN-BUNDLE / 0 FABRICATED** (largest scorecard + highest confirmation rate in corpus; tallied programmatically)
- **NotebookLM:** none (yt-dlp captions read in full — a claims scorecard cannot grade a paraphrase)
- **Result:** the anchor is **right about the fact, wrong about the frame** — Anthropic really does watermark Claude's text output and it really does persist through proofread/translate/summarize, but "all their models" is **CORRECTED** (models launched on/after 2026-08-02; earlier ones by 2026-12-02), "detects whether Claude is the author" is **MISLEADING** (Anthropic: *"may have been **processed** by Claude"*), and the video **never names the EU AI Act** that caused it. **The mark comes from Article 50(2); the ratified hireui candidate-LLM ADR comes from the same Act** — 50(2) binds providers, 50(4) binds deployers, and the ADR's "eval-gated" clause is currently unimplementable (no public detector, no published false-positive rate). **The anchor's other story is a confirmed real-world BOLA**: a Claude-powered OpenClaw agent in Melbourne found *"zero authorization checks on cancelling other people's reservations"* and deleted a stranger's booking — the exact class `api-security-7-techniques` flags as this operator's #1 risk. ⚠️ **6 verification-process failures recorded** incl. 2 lenses CONFIRMING the anchor's one material error and a critic that falsely reported "no disagreements detected". ⚠️ **The source bundle is NOT reproducible** — 1 of 3 selection runs drifted.
- **Deepen candidates:** ⭐⭐ **non-English watermark/detector performance** (the topic's largest real gap — every number is English, the anchor is Vietnamese, and hireui screens non-native-English candidates) · ⭐⭐ **make `--dry-run` emit video IDs and let a drain accept an ID list**, so a selection can be replayed rather than re-rolled (the non-reproducibility finding) · ⭐⭐ **re-read `support.claude.com` verbatim** rather than through `WebFetch`'s summarizing layer, and pick up the detection API when it ships (release date, access tier, error rates) · ⭐ **does the mark degrade code?** the one unresolved contradiction (A09 vs C16), and the question that matters most for Claude Code · ⭐ the **2027-02-02 Code-of-Practice interoperability deadline**, absent from all 6 sources · ⭐ **C2PA as a topic in its own right** (the corpus has none) · ⭐ the **12 unverified items** in the anchor's roundup, listed in `the-anchor-audit` so a later ingest need not re-derive them · ⭐ **fix `eng_ratio * 3` unboundedness** — surfaced again here at score 313.39 vs 49.58 for a video with 3.5× the views

### Homebrew — the macOS package-manager layer (VN anchor + 6.0 release) ✅
- **Drained:** 2026-08-21 by `/loop` (operator anchor `A_nvIGTNfuw` Kunkka + yt-search ×5 on query `Homebrew macOS package manager terminal setup`, selected via `bin/autopilot-drain.py --dry-run`; anchor validation **PASS 1/1, overlap 100%**)
- **Raw analysis:** `raw/2026-08-21-homebrew-macos-package-manager-layer.md`
- **Wiki output:** [[../wiki/homebrew-macos-package-manager/_index]] — 11 files; 109 wikilinks validated 0 broken; **46 claims: 29 CONFIRMED / 5 CORRECTED / 4 CBI / 3 UNVERIFIED / 2 TIME-BOUND / 1 MISLEADING / 1 UNFALSIFIABLE / 1 CONTRADICTED-IN-BUNDLE / 0 FABRICATED**
- **NotebookLM:** none (yt-dlp captions read in full — a claims scorecard cannot grade a paraphrase)
- **Result:** the anchor is a design-history essay, not a tutorial, and its three central critiques of Homebrew are confirmed verbatim by `docs.brew.sh`. **The headline finding is original to the ingest**: this machine (Apple M4 Pro) runs its primary Homebrew as **x86_64 under Rosetta 2** at `/usr/local` while a native arm64 install sits unused at `/opt/homebrew` — which diagnoses the long-standing "broken `python3` shim" note in the project `CLAUDE.md`, and lands on Homebrew's **Intel → Tier 3 September 2026** deprecation path.
- **Deepen candidates:** ⭐⭐ run the prefix migration and write it up (bounded, measurable, Sept-2026 deadline) · ⭐⭐ assert one transcript file per selected video before compiling (silent-fetch-failure guard) · ⭐ a **docs-first** ingest of `docs.brew.sh` Tap-Trust + Support-Tiers (the docs outperformed every video here) · ⭐ **Nix on macOS** — two sources place the boundary there and the corpus has no Nix topic · Rosetta 2's own deprecation timeline (deliberately unverified) · `brew bundle` vs real fleet reproducibility · Kunkka's back catalogue
### Local LLM coding on Apple Silicon — the 64GB Mac mini M4 hardware ladder ✅
- **Drained:** 2026-08-20 by `/loop` (operator anchor `GBf_mKxGqtk` Quân IT + yt-search ×5: WEBdoze / ForrestKnight / Samuel Gregory / Zen van Riel / Tech With Tim; anchor validation **PASS 1/1** — *after* fixing a delimiter bug in `bin/autopilot-drain.py` that had silently dropped it as "unreachable")
- **+1 main-loop addition:** Apple WWDC26 session 232 `wykPErJ8M-8` (first-party; the rubric ranks engagement, not authority)
- **Raw analysis:** `raw/2026-08-20-local-llm-coding-apple-silicon-hardware-ladder.md`
- **Wiki output:** [[../wiki/local-llm-coding-hardware-ladder/_index]] — 11 files; 123 wikilinks validated 0 broken; **21 claims: 12 CONFIRMED / 5 CBI / 1 FALSE / 3 UNRESOLVED / 0 FABRICATED**
- **NotebookLM:** none (yt-dlp captions read in full)
- **Result:** TESTS AND CORRECTS `local-ai-coding-agents` — its "≥24 GB practical minimum" is **refuted** for agentic coding. Memory capacity is the wrong axis; prefill/bandwidth/repo-size are binding.
- **Deepen candidates:** ⭐ an **M5-generation** agentic test against a real repo (the biggest open question — Apple claims 4× matmul, nobody has measured it on a large codebase) · Apple WWDC26 session **233** (distributed inference) · **OMLX** hands-on (SSD-persistent prefix cache) · **Alex Ziskind** bandwidth/TCO bundle (appeared in all 3 test queries, never won a slot) · Asad Tinkers "Ultimate Local Mac Agentic AI Coding Workflow" (951 views — **below `MIN_VIEWS=1000`, rubric structurally cannot pick it, needs an anchor**)

### DeepSeek Harness — YouTube commentary layer vs source-verified corpus ✅
- **Drained:** 2026-08-20 by `/loop` (operator anchor `f51ICIoHcjY` Chase AI + yt-search ×5: The Cef Experience / Turing Post TV / Code Bug VN / Better Stack / Firecrawl; anchor validation **PASS 1/1**)
- **Raw analysis:** `raw/2026-08-20-deepseek-harness-youtube-commentary-vs-source.md`
- **Wiki output:** [[../wiki/deepseek-harness/_index]] — 15 files; 32 wikilinks validated 0 broken; **47 claims: 24 CONFIRMED / 10 CBI / 4 PLAUSIBLE-NOT-PRIMARY / 4 MISLEADING / 1 FALSE / 3 UNRESOLVED / 1 UNVERIFIABLE / 0 FABRICATED**
- **NotebookLM:** none (yt-dlp captions read in full — a claims scorecard cannot grade a paraphrase)
- **Deepen candidates:** Cloud Codes architecture deep-dive (49,192 views) + NeuralNine (196,090, largest reach) + CloudYeti "Is the Hype Real? LIVE Testing" (891 views, below `MIN_VIEWS` so the rubric cannot pick it — **needs an anchor**)

### Engineer of the future — Addy Osmani AIEWF-2026 keynote + role-under-AI-agents bundle ✅
- **Drained:** 2026-07-22 by `/loop` (operator anchor `n97BCfyFIvw` + yt-search ×5: Karpathy / Ng / Cursor-Truell / Gergely Orosz / Harrison Chase)
- **Raw analysis:** `raw/2026-07-22-engineer-of-the-future-osmani-aie-keynote-bundle.md`
- **Wiki output:** [[../wiki/engineer-of-the-future/_index]] — 15 files (0 FALSE / 0 FABRICATED; workflow `wf_dabc1f67-f9f`)
- **NotebookLM:** none (yt-dlp captions read in full)

### API types explained (REST, SOAP, GraphQL, gRPC, WebSocket, webhook) ✅
- **Drained:** 2026-07-21 by overnight orchestrator
- **Raw analysis:** `raw/2026-07-21-api-types-explained-rest-soap-graphql-grpc-websock.md`
- **NotebookLM:** `ed17cc3d-952c-4fe0-9572-27a418d0f390`
### Harness Engineering — getting started / beginner introduction (Vietnamese anchor) ✅
- **Drained:** 2026-05-30 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-30-harness-engineering-getting-started-beginner-intro.md`
- **NotebookLM:** `4c7d51e4-b450-4504-933b-3bb4be28b393`
### Anthropic Cowork first-party documentation + setup-cowork skill ✅
- **Drained:** 2026-05-30 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-30-anthropic-cowork-first-party-documentation-setup-c.md`
- **NotebookLM:** `b05d3444-6dbb-4955-a8fb-be9b021a0350`
### AI Operating System — 5-skills framework ✅
- **Drained:** 2026-05-29 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-29-ai-operating-system-5-skills-framework.md`
- **NotebookLM:** `1f5811fb-60c1-4857-a039-c784508b2ec4`
### Claude Cowork — Anthropic scheduled-agent feature ✅
- **Drained:** 2026-05-29 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md`
- **NotebookLM:** `f851b538-c0cb-405f-9a8b-c46837464930`
### Autonomous Loops with HITL — anchor-injection re-run ✅
- **Drained:** 2026-05-23 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-23-autonomous-loops-with-hitl-anchor-injection-re-run.md`
- **NotebookLM:** `94db9216-eb26-489d-8f06-fd65fbea3fd4`
### Open Source Claude Design clones — anchor-corrected re-run ✅
- **Drained:** 2026-05-14 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-14-open-source-claude-design-clones-anchor-corrected.md`
- **NotebookLM:** `de7bec64-846d-486b-8661-4784d3cf0a1f`
### Codex — anchor-corrected re-run (3 anchors) ✅
- **Drained:** 2026-05-14 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-14-codex-anchor-corrected-re-run-3-anchors.md`
- **NotebookLM:** `3561e31a-5cfa-4fe6-9d5f-bec48b84d029`
### Agent Dashboard / Agent OS — anchor-corrected re-run ✅
- **Drained:** 2026-05-14 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-14-agent-dashboard-agent-os-anchor-corrected-re-run.md`
- **NotebookLM:** `1cd445b9-d834-4686-9fd0-12f4d67ce9d6`
### AI daily news — May 2026 weekly snapshot ✅
- **Drained:** 2026-05-13 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-13-ai-daily-news-may-2026-weekly-snapshot.md`
- **NotebookLM:** `9f08f424-31bc-4fe9-8e8b-3a91862171a1`
### Open Source Claude Design clones — alternative agent CLIs ✅
- **Drained:** 2026-05-13 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-13-open-source-claude-design-clones-alternative-agent.md`
- **NotebookLM:** `5155a280-86ce-49ce-8328-d4b75c0119ce`
### Codex — long-running agentic harness alternative to Claude Code ✅
- **Drained:** 2026-05-13 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-13-codex-long-running-agentic-harness-alternative-to.md`
- **NotebookLM:** `01707594-d36a-4a2f-b3f8-7fa9044528ba`
### Harness Engineering — personal-repo continuation (Vietnamese practitioner take + more) ✅
- **Drained:** 2026-05-13 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-13-harness-engineering-personal-repo-continuation-vie.md`
- **NotebookLM:** `58c51d8e-ab36-4331-993f-8a61dfd0a2c4`
### Auto-Loop Goals with human-in-the-loop ✅
- **Drained:** 2026-05-13 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-13-auto-loop-goals-with-human-in-the-loop.md`
- **NotebookLM:** `abe1647e-c9c3-4ad1-8e63-5e93fac50865`
### Agent Dashboard / Agent OS — Claude Code observability + dashboards ✅
- **Drained:** 2026-05-13 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-13-agent-dashboard-agent-os-claude-code-observability.md`
- **NotebookLM:** `54d7812d-2305-4eac-b250-43ba577cb1dc`
### Remote agent control — tunneling, SSH, ngrok, tailscale ✅
- **Drained:** 2026-05-07 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-07-remote-agent-control-tunneling-ssh-ngrok-tailscale.md`
- **NotebookLM:** `46ee01f8-81e3-47d6-b617-4c322359b6b9`
### MCP servers for messaging platforms — Telegram, WhatsApp, Discord ✅
- **Drained:** 2026-05-07 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-07-mcp-servers-for-messaging-platforms-telegram-whats.md`
- **NotebookLM:** `183e3635-ea8c-4c52-9c16-11aa32e19c78`
### Claude Code SDK — headless / programmatic automation ✅
- **Drained:** 2026-05-07 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-07-claude-code-sdk-headless-programmatic-automation.md`
- **NotebookLM:** `dafc8c4f-840b-41a1-b125-bfe973c919f0`
### Telegram bot — remote control Claude Code/Desktop from phone ✅
- **Drained:** 2026-05-07 by overnight orchestrator
- **Raw analysis:** `raw/2026-05-07-telegram-bot-remote-control-claude-codedesktop-fro.md`
- **NotebookLM:** `5f514e9c-d8e4-42be-af1e-c456dfa1e4c7`
### Workflow for AI Coding — champions roundup ✅
- **Drained:** 2026-05-07 by autopilot loop `(C) 2026-05-07-15-autopilot-loop.md`
- **Wiki output:** [[../wiki/workflow-ai-coding/_index]] — 5 articles + index
- **NotebookLM:** `ec93ea09-b589-4103-95a9-3fb2c13d5a2e`

### How to 10x Claude Code — tips & tricks roundtable ✅
- **Drained:** 2026-05-07 by autopilot loop `(C) 2026-05-07-15-autopilot-loop.md`
- **Wiki output:** [[../wiki/10x-claude-code/_index]] — 5 articles + index
- **NotebookLM:** `d1d18b0b-ab85-4773-a999-98f36fb39cf5`

- TODO: hoidanit fullstack-vibe-coding series — re-drain playlist PLPTXD_6Mbmh4 when episode >=5 lands; **cadence now deterministic (ep-3 deepening 2026-07-04): live Mondays 19:30 ICT, VOD Wednesdays → ep-5 (React fundamentals) expected ~Wed 2026-07-08**; PRIORITY when the AI-consult-agent episode ships (wiki/hoidanit-fullstack-vibe-coding gap)
