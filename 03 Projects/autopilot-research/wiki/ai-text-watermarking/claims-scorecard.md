# Claims scorecard

> **Every load-bearing claim in the 6-source bundle, graded.** Totals are **tallied programmatically** from this table, never hand-counted (rule inherited from [[../deepseek-harness/_index]]: *tally the table, don't hand-count it*).
> **Verdict key:** CONFIRMED · CORRECTED (true core, wrong specifics) · CBI = confirmed-but-incomplete · MISLEADING (technically defensible, misleads as stated) · FALSE · TIME-BOUND (true at publication) · UNVERIFIED (could not settle) · UNFALSIFIABLE · FABRICATED
> **Sources:** S1 anchor/BizMate · S2 Squintist · S3 Ulku · S4 Code Bear · S5 BetterWay · S6 Balmer

## A. Anthropic's policy — scope, dates, coverage

| ID | Src | Claim | Verdict | Basis |
|---|---|---|---|---|
| A01 | S1 | **All** Anthropic models will insert a watermark into any text they generate | **CORRECTED** | Primary: models launched **on or after 2026-08-02**; earlier models in a transition period. Two verification lenses wrongly returned CONFIRMED |
| A02 | S6,S5 | Models launched on/after 2026-08-02 support marking at launch | **CONFIRMED** | `support.claude.com`, verbatim |
| A03 | S5 | Models already released have until December | **CONFIRMED** | AI Omnibus provisional agreement (May 2026): **2026-12-02** |
| A04 | S1,S2,S3 | Embedded watermarks apply to all generated text | **CONFIRMED** | *"Embedded watermarks will apply to all generated text."* |
| A05 | S6 | Supported files also get signed C2PA provenance metadata | **CONFIRMED** | `.svg`, `.png`, `.jpg` per primary |
| A06 | S3 | Applies across API, Claude Code and Cowork | **CONFIRMED** | Marking applies wherever Claude is offered |
| A07 | S6,S5 | Applies worldwide regardless of user location | **CONFIRMED** | *"wherever Claude is offered, worldwide"* |
| A08 | S5 | Worldwide scope is Anthropic's choice, not an EU requirement | **CONFIRMED** | No durable regional limiting; regulation is EU-scoped |
| A09 | S1 | The mark does not change meaning, quality or readability | **CBI** | Anthropic's claim + Nature satisfaction data support it; S6's cited practitioner disputes it for code. Unresolved |
| A10 | S3 | Anthropic is working on retrofitting older models | **CONFIRMED** | *"we're working to add marking support for those models as well"* |
| A11 | S1 | Users cannot opt out | **UNVERIFIED** | Anthropic's page is silent on opt-out in every tier. Silence ≠ confirmation |
| A12 | S6,S5 | Technical documentation and detection tooling not yet released | **CONFIRMED** | *"We'll share details on detection mechanisms in forthcoming technical documentation."* |
| A13 | S6 | Anthropic will ship a text detection API | **CONFIRMED** | Stated by Anthropic; no date, no access tier, no error rates |
| A14 | S2 | Anthropic has not published how its mark works | **TIME-BOUND** | True at S2's publication (2026-08-13); Anthropic's fuller explanation landed 2026-08-14. Two lenses wrongly graded this CONTRADICTED / MISLEADING by judging a dated source against later facts |
| A15 | S4 | Anthropic's method **is** Google's SynthID-Text | **CBI** | Anthropic says "based on"; whether it is unmodified is unresolved |

## B. What a mark proves

| ID | Src | Claim | Verdict | Basis |
|---|---|---|---|---|
| B01 | S1 | A scanner detects **whether Claude is the author** | **MISLEADING** | Anthropic: *"may have been **processed** by Claude"*. Authorship is precisely what it cannot establish |
| B02 | S2,S3,S6 | A mark means Claude touched the text; it says nothing about who wrote it | **CONFIRMED** | Primary, verbatim |
| B03 | S1,S3,S6 | The mark persists when Claude only translates, summarizes or proofreads | **CONFIRMED** | *"People often use Claude to proofread, translate, summarize, or convert files."* |
| B04 | S6 | A mark used as an automatic cheating verdict overstates Anthropic's claim | **CONFIRMED** | Follows from B02 + no published error rate |
| B05 | S6 | Absence of a mark does not prove human authorship | **CONFIRMED** | Pre-Aug-2 model, short passage, rewritten, stripped metadata, or another vendor |
| B06 | S6 | Anthropic's detector returns "not AI" for ChatGPT output | **CONFIRMED** | A vendor watermark detector is not a general AI detector |
| B07 | — | A detected watermark can prove a specific person's authorship | **FALSE** | All six sources and Anthropic agree it cannot |
| B08 | S1 | Risk of false-positive accusations against students | **CONFIRMED** | Risk is real; magnitude unquantified because no error rate is published |
| B09 | S1 | Firms could lose contracts when clients detect AI editing | **UNVERIFIED** | Plausible; no instance found |

## C. Mechanism

| ID | Src | Claim | Verdict | Basis |
|---|---|---|---|---|
| C01 | S2,S3,S5 | The mark **is** the word choices; nothing is inserted into the text | **CONFIRMED** | arXiv:2603.03410, arXiv:2402.19361; Anthropic primary |
| C02 | S3,S6 | Not metadata, not hidden characters, not a hidden file | **CONFIRMED** | Same |
| C03 | S2 | SynthID runs a knockout tournament among candidate tokens, decided by a hidden score | **CONFIRMED** | Matches the published algorithm exactly |
| C04 | S2,S5 | The score comes from a secret key mixed with the preceding tokens, and reshuffles every step | **CONFIRMED** | Same |
| C05 | S2 | Across many steps each word wins as often as it would unwatermarked; frequencies do not shift | **CONFIRMED** | Distortion-free property of tournament sampling |
| C06 | S2 | Detection re-runs the sampler's math with the key; human text scores ~50%, keyed text above | **CONFIRMED** | Same |
| C07 | S2 | Detection needs no database and no model — only the words plus the key | **CONFIRMED** | *"watermark detection is computationally efficient, without using the underlying LLM"* |
| C08 | S2 | Signal exists only in aggregate over hundreds of words, never one word | **CONFIRMED** | Same |
| C09 | S6 | Cruder green-list/red-list schemes work by hashing the prior token and boosting a word set | **CONFIRMED** | Kirchenbauer et al. family |
| C10 | S2 | Google ran SynthID live in Gemini and published in *Nature* | **CONFIRMED** | *Nature* 634:818, Oct 2024, `s41586-024-08025-4` |
| C11 | S2 | About 20 million Gemini responses were assessed | **CONFIRMED** | *"approximately 20 million watermarked and unwatermarked responses"* |
| C12 | S2 | Thumbs-up rate differed by ~1/100 of a percent | **CONFIRMED** | *"differed by 0.01% (with the watermarked model being higher)"*; thumbs-down 0.02% |
| C13 | S2 | Slowdown was about half a percent | **CONFIRMED** | 15.527 → 15.615 ms/token = **+0.57%** |
| C14 | S2 | The watermark needs linguistic freedom; one-answer questions and code have no room | **CONFIRMED** | Low-entropy contexts cannot carry signal |
| C15 | S2 | The more the model rephrases, the stronger the mark can be | **CONFIRMED** | Follows from entropy dependence |
| C16 | S6 | Rigging the sampler degrades output, materially so for code | **CBI** | Practitioner claim, mechanistically coherent, directly contradicts A09. No measurement for Anthropic's scheme |
| C17 | S1 | The pattern is unrecognizable to humans but detectable by a model | **CONFIRMED** | Detectable with the key; "by a model" is loose but not wrong |

## D. Attacks and robustness

| ID | Src | Claim | Verdict | Basis |
|---|---|---|---|---|
| D01 | S2,S3,S5 | Paraphrase or round-trip translation removes the mark | **CONFIRMED** | arXiv:2607.16010 |
| D02 | S2 | A team's test removed the mark in **58 of 59** cases | **CONFIRMED** | 98.3%; same paper. Earlier schemes (KGW, Unigram) 100% |
| D03 | S1,S3,S5 | Light editing usually will not remove it; a full rewrite will | **CONFIRMED** | Anthropic + literature |
| D04 | S2 | Google open-sourced SynthID-Text, which is why the attack is testable | **CONFIRMED** | Public release |
| D05 | S2 | A 9B open model on a home machine suffices to strip it | **CONFIRMED** | Reported attack setup |
| D06 | S2 | An open model cannot be compelled to mark, since the operator controls sampling | **CONFIRMED** | Structural |
| D07 | S5 | ETH Zurich: SynthID-Text is easier to strip than several competing designs | **CONFIRMED** | watermark-stealing.org |
| D08 | S5 | Secret rules can be approximated via public API queries for under $50 | **CONFIRMED** | arXiv:2402.19361, verbatim |
| D09 | S5 | Scrubbing success **above 90%** | **CORRECTED** | Paper states *"over 80%"*. Use over 80% |
| D10 | S5 | Piggyback spoofing: edit marked text to invert meaning, mark survives | **CONFIRMED** | arXiv:2604.11546 (62% with minimal supervision), arXiv:2502.18608 |
| D11 | S5 | One group forged a prominent scheme >80% of the time | **CONFIRMED** | Same |
| D12 | S5 | Removal-resistance and spoof-resistance trade off by construction | **CONFIRMED** | Stated as a fundamental trade-off in the literature |
| D13 | S5 | Watermarks are "radioactive" — models trained on marked text inherit the bias | **CONFIRMED** | arXiv:2402.14904, p < 10⁻⁵ at 5% contamination |
| D14 | S5 | Effect holds when only 6.5% of the training set is watermarked | **CONFIRMED** | Same |
| D15 | S5 | Contamination is detectable even against a closed model with no training-data access | **CONFIRMED** | Same |
| D16 | S5 | This turns a transparency measure into a distillation detector | **CONFIRMED** | The paper describes it as a side effect |
| D17 | S6 | Industry-wide marking helps labs exclude synthetic data from future training | **UNFALSIFIABLE** | Coherent motive attribution; no lab has stated it |
| D18 | S3 | Homoglyph swaps break entity resolution and trip a long-standing spam signal | **CONFIRMED** | Tokenization, not vision; mixed-script detection is well established |
| D19 | S5 | Humanizer AI passed 6 million users before the announcement | **UNVERIFIED** | Vendor-reported figure, not independently checked |
| D20 | S5 | Open-source projects to remove Claude's mark appeared within days | **CBI** | Attributed to Decrypt; the category plainly exists, the specific timing unchecked |

## E. Detectors (a different instrument)

| ID | Src | Claim | Verdict | Basis |
|---|---|---|---|---|
| E01 | S2 | Style detectors have no key and judge style, unlike watermark detectors | **CONFIRMED** | Definitional; five of six sources omit this distinction |
| E02 | S2 | OpenAI's 2023 detector caught ~¼ of AI text, false-flagged 9% of human writing, shut down in months | **CONFIRMED** | ~26% / ~9%, Jan–Jul 2023 |
| E03 | S2 | Stanford 2023: 61% of non-native-English essays flagged as AI across 7 detectors | **CONFIRMED** | 91 TOEFL essays; ~19.8% unanimous |
| E04 | S2 | Pangram now reports zero flags on that dataset | **UNVERIFIED** | Vendor-reported |
| E05 | S2 | A professor's hand-polished comedy story was flagged 100% AI | **UNVERIFIED** | Anecdote; not independently located |
| E06 | S2 | NeurIPS scanned 969 submissions and rejected 178 before peer review, ~18%, no appeal | **CONFIRMED** | ~969–971 scanned with Pangram v3.3.2; **178 = 18.4%**; +123 (12.7%) conditional; 273 initially at 100% |
| E07 | S2 | A rejected author ran the chairs' own papers and got 24–69% | **CONFIRMED** | 69, 45, 36, 24 |
| E08 | — | The same detector flagged 1% of accepted ICLR 2026 papers vs 28% at NeurIPS | **CONFIRMED** | Calibration finding; **absent from the entire bundle** |
| E09 | S5 | ICML July 2026 caught 506 reviewers violating a no-LLM policy via planted watermarks | **CONFIRMED** | 506 reviewers, 795 reviews, 497 papers desk-rejected |
| E10 | S2 | Post-ChatGPT, its favourite words appear up to 50% more often in human talks | **CBI** | Direction well documented; the exact 50% figure not traced to a primary study |
| E11 | S2 | Detector-vs-humanizer is a self-sustaining arms race | **CONFIRMED** | Both product categories exist and retrain against each other |

## F. The EU chain

| ID | Src | Claim | Verdict | Basis |
|---|---|---|---|---|
| F01 | S2,S5,S6 | The driver is the EU AI Act | **CONFIRMED** | Article 50(2) + Code of Practice |
| F02 | S6 | Article 50(2) obliges **providers** to mark synthetic output machine-readably | **CONFIRMED** | Verbatim from the Act |
| F03 | S6 | Provider vs deployer is the root of most confusion; 50(4) binds deployers | **CONFIRMED** | Only source in the bundle to name it |
| F04 | S2 | Obligations bite from August 2nd | **CONFIRMED** | 2026-08-02 |
| F05 | S2 | The law exempts standard editing — spelling, grammar, translation | **CONFIRMED** | Guidelines exempt *"assistive editing functions"*. Anthropic marks it anyway |
| F06 | S2 | The Code requires free public checking, but text checkers may initially be limited to verified experts | **CONFIRMED** | The regulator treats text marks as the least reliable modality |
| F07 | S2,S6 | Anthropic, OpenAI, Google, Meta, Microsoft, Mistral all signed | **CONFIRMED** | EC signatory material |
| F08 | S5 | ~190 organizations signed, in July 2026 | **CONFIRMED** | EC |
| F09 | S5 | Penalty reaches €15M or 3% of global turnover | **CONFIRMED** | Article 99 ceilings |
| F10 | S6 | The Act reaches non-EU providers when output is used in the EU | **CONFIRMED** | Extraterritorial scope |
| F11 | S6 | xAI is the only major holdout and refused to sign | **CONFIRMED** | Absent from the EC signatory list |
| F12 | S6 | Google has marked text with SynthID since early 2024 | **CONFIRMED** | Nature paper Oct 2024; deployment from 2024 |
| F13 | — | The Code requires **at least two independent layers** of machine-readable marking | **CONFIRMED** | Explains text watermark + C2PA. **Absent from the bundle** |
| F14 | — | Interoperable public detection tooling required by **2027-02-02** | **CONFIRMED** | **Absent from the bundle**; the date a builder would plan against |
| F15 | S1 | The measure is covert surveillance users cannot switch off | **MISLEADING** | Published law, named article, signed public code, ~190 signatories. The anchor never mentions any of it |

## G. SEO, and the anchor's other items

| ID | Src | Claim | Verdict | Basis |
|---|---|---|---|---|
| G01 | S3 | Google's documented position: producing content with AI is not itself a violation | **CONFIRMED** | 2023 guidance, still live |
| G02 | — | A search engine demotes watermarked text | **FALSE** | No public evidence; three years of counter-evidence for marked images |
| G03 | S3 | SynthID has marked Google images/video/audio since 2023 and is detectable in Search/Lens | **CONFIRMED** | Live product surface |
| G04 | S3 | An AI-generated image scored 99% AI on a free detector in seconds | **CBI** | Demonstrated on camera; single unnamed detector, single image |
| G05 | S3 | His clients' pages rank with AI text and AI images, no demotion, over 4 windows | **UNVERIFIED** | First-party agency screenshots for the product the video sells |
| G06 | S3 | You cannot use Claude/OpenAI/Gemini to strip the mark — all are signatories | **CONFIRMED** | Follows from F07 |
| G07 | S3 | The mark "survives editing" (opening claim) | **CONTRADICTED-IN-BUNDLE** | Contradicted at `[01:52]` **by the same video**: heavy rewriting kills it |
| G08 | S1 | NotebookLM added copy/duplicate notebooks with owner-controlled copy permission | **CONFIRMED** | Google Workspace Updates, Aug 2026; "Allow copies"; copies carry sources + Studio, not chat history |
| G09 | S1 | Gemini 3.7 Flash shipped in AI Studio, a slight improvement on 3.6 | **CONFIRMED** | Released 2026-08-13, 1M context; "slight" understates — FrontierCode 43.6% vs 34.4%, intro price half of 3.6 |
| G10 | S1 | A Claude-powered OpenClaw agent exploited a gym API to cancel a stranger's booking | **CONFIRMED** | Melbourne, 2026-08-10, ABC News + 7 outlets. Agent verbatim: *"zero authorization checks on cancelling other people's reservations"* |
| G11 | S1 | Manus users must back up data before "the end of this month" or lose it permanently | **CORRECTED** | Real, and **more urgent**: deadline **07:59 SGT 2026-08-23**; deletion 23–24 Aug SGT; restore from the 25th |
| G12 | S1 | Grok Bot requires a $200+/month plan and burns credits in a day | **UNVERIFIED** | Not checked; outside this topic's scope |
| G13 | S1 | Free ChatGPT Plus for university students from ~September | **UNVERIFIED** | Not checked |
| G14 | S1 | Marking may push users toward unmarked models | **UNFALSIFIABLE** | Prediction. Note the anchor promotes Grok — xAI being the one lab that refused to sign |

---

## Totals

**Tallied programmatically** by parsing the tables above (101 rows, 101 unique IDs, 0 duplicates):

| Verdict | Count |
|---|---|
| CONFIRMED | **76** |
| UNVERIFIED | 8 |
| CONFIRMED-BUT-INCOMPLETE | 6 |
| CORRECTED | 3 |
| MISLEADING | 2 |
| FALSE | 2 |
| UNFALSIFIABLE | 2 |
| TIME-BOUND | 1 |
| CONTRADICTED-IN-BUNDLE | 1 |
| **FABRICATED** | **0** |
| **Total** | **101** |

**75% CONFIRMED, zero fabricated.** The highest confirmation rate and the largest scorecard in this corpus to date
(cf. 46 claims / 63% for [[../homebrew-macos-package-manager/_index]], 47 / 51% for [[../deepseek-harness/_index]]).

**Why the rate is this high:** the subject is a *published policy with a published legal driver and a peer-reviewed
mechanism*. Unlike a product roundup, almost every claim here has a primary document behind it — Anthropic's support
page, the Act, the EC signatory list, a *Nature* paper with an open-access mirror. **A verifiable subject produces a
high score; it is not a sign the sources were unusually careful.** The two weakest source-classes are visible in the
distribution: vendor-reported figures (E04, D19) and first-party agency data (G05) account for most UNVERIFIED rows.

## The eight rows that carry the topic

- **A01 CORRECTED** — "all their models" is the anchor's one material error, and two verification lenses confirmed it anyway.
- **B01 MISLEADING** — "whether Claude is the author" is the inversion of Anthropic's actual claim.
- **F15 MISLEADING** — surveillance framing for a measure whose legal driver the video never names.
- **D09 CORRECTED** — ">90%" scrubbing should be "over 80%".
- **G11 CORRECTED** — the Manus deadline is 2026-08-23, not "end of month". Wrong in the direction that loses data.
- **G02 FALSE** — no search engine has been shown to demote watermarked text.
- **B07 FALSE** — a watermark cannot prove a person's authorship. Unanimous across all six sources and Anthropic.
- **G07 CONTRADICTED-IN-BUNDLE** — a video contradicting itself 84 seconds apart.

See [[caveats-and-corrections]] for the unresolved set and for the six verification-process failures.
