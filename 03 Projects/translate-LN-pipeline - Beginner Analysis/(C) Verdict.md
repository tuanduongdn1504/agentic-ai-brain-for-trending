# (C) Verdict — v257 `mranex/translate-LN-pipeline`

**Date:** 2026-08-21 · **Branch:** `wiki/v257-translate-ln-pipeline` off the v256 tip (`66c0cec`) · **Not auto-merged.**

---

## 1. Phase 0.9 gate

| Criterion | Verdict | Evidence |
|---|---|---|
| **(a)** Anthropic / registered vendor-direct | **FAIL** | `mranex` is pseudonymous — no bio, no location, no company; three git names over one email (`elsgman1999@gmail.com`), commits at UTC+0700. **§41** is explicit: (a) passes only on a declared Anthropic affiliation or a registered (a)-7 vendor-direct source. A Vietnamese README and an operator-locale match are exactly the inference §41 forbids, and the corpus already holds Vietnam-located solo developers (**v76**, **v231**), so no corpus-first is available there either. |
| **(b)** goal relevance | **STRONG** ⚠️ *MODERATE recorded as the reviewable alternative* | Argued at §2. |
| **(c)** novelty / interest | **STRONG** | Three complete generations coexisting in one tree; committed bytecode of source that was never published; a confidence policy declared three times at two different values with the enforced one matching neither; a README whose primary launch command starts a different program; and — the reason this ship is worth more than its subject — the corpus's first genuine **same-author control**. |
| **(d)** analysability | **STRONG** | 88 files, 12,561 lines of Python, cloned twice and byte-identical, an 11-commit history read end to end, and the product's own two screenshots shipped in-repo and readable as images. |

**⇒ GOAL-ALIGNED INCLUDE 3/4.** **§40 applies:** operator-requested, goal-adjacent, (b) MODERATE+ ⇒ **no override consumed, no §35 pressure**, OFF-GOAL recorded as reviewable.

---

## 2. Why (b) is STRONG here and was MODERATE for the sibling

This is the one judgement in the ship that a later audit is most likely to revisit, so the reasoning is set out rather than asserted.

**v256 was rated MODERATE** because the LLM was **one stage of ten**: detection, OCR preparation, masking, inpainting, render preparation, typesetting and export are computer-vision and layout work, and the translation call sat in the middle of them. The architectural analogy to the operator's goals was real but indirect.

**This subject has no computer vision at all.** Strip the domain away and what remains is:

- **13 versioned prompt templates** on disk, numbered as a pipeline (`00_json_output_policy` → `12_quick_fix`), of which 12 consume a shared output contract by placeholder.
- **A render engine** with variable injection (`{{JSON_OUTPUT_POLICY}}`, `{{INPUT_JSON}}`, `{{genre}}`) and a **three-level override chain** — project, then shared, then repository default.
- **A response parser** that strips model markdown and recovers JSON from chatty prose with a correct quote-and-escape-aware scanner.
- **A step registry** distinguishing AI steps from deterministic local steps, with the local ones justified explicitly on cost.
- **A persistent entity/terminology canon** across a multi-volume series, with per-entry provenance, a confirmed/tentative status semantics that tells the model how a *downstream* model will use the field, and a conflict-marking protocol instead of silent overwrite.
- **A confidence field requested from the model** and a review-flag service that routes low-confidence output to a human.
- **An "Active Volume Canon" filter** whose entire purpose is to keep the prompt small by including only entities actually present in the current unit.

⭐ **That is an LLM-workflow substrate wearing a light-novel costume.** Four of those seven bullets map directly onto live operator threads: prompt-template versioning is what `05 Skills/` already does by hand; the canon filter is the same problem as the vault's own ~54K tool-catalog context budget; the confidence-to-human routing is the shape the **ratified candidate-LLM legibility ADR** demands; and the extraction-validate-correct loop is hireui's CV-parse problem.

**The honest case for MODERATE, recorded:** zero agent surface — no `CLAUDE.md`, no `AGENTS.md`, no MCP server, no skill, nothing an agent can call; 7 page-stated stars; a hobbyist domain; and the tool deliberately does not integrate with any model programmatically, which is the opposite of agent-nativity. A reader who weights "is this agent infrastructure?" above "is this LLM-workflow engineering?" should land on MODERATE, and the ship would still be GOAL-ALIGNED under §40 either way.

**I record STRONG** because the artifact under analysis is a prompt-engineering and response-governance system, and because the borrowable material (§Pilot) is larger and more directly applicable than v256's single guard.

⚠️⚠️ **Precedent note, stated pre-emptively for the third consecutive ship.** **NO MINT** (a pattern-library decision) and **OFF-GOAL** (a Phase-0.9 intake decision) are **orthogonal.** `llm-wiki-routine-v2.7.md` §40 names **AI-For-Beginners v191** and **mlsysbook v197** — both NO MINT — and says *"Under §40 these are simply GOAL-ALIGNED."* At **v255** a critic conflated the two and an anti-critic upheld it; at **v256** the adversary caught the same conflation and rejected it. Declining a mint on domain grounds is not an argument for OFF-GOAL.

---

## 3. Mint decision — **NO MINT**

**Counts UNCHANGED: 46 confirmed patterns / 11 CONFIRMED Library-vocab. §C live standalones 51 unchanged. Tracked surface ≈58 unchanged. Max pattern #85. No N-bumps taken.**

**The strongest alternative, recorded and declined:** a §C standalone at N=1 — ***"Prompt-Rendering Workbench That Deliberately Does Not Call the API — the Human Carries the Prompt to a Chat LLM and Pastes the Response Back."*** It is the most interesting mint candidate the last several ships have produced, because it is the **honest pole of an economic pressure the corpus has already minted the dishonest pole of**: v207/v208 re-expose CLI-tool OAuth subscriptions as APIs, and v231/v232 drive consumer chat UIs to harvest a free entitlement. All four automate the subscription. **This one refuses to automate it and puts a human in the transport instead.** Declined on five grounds:

1. 🔴 **Domain-not-capability.** Light-novel/web-novel translation is a domain; §C vocabulary is capability-shaped. **v197 mlsysbook** (*"a single-domain educational curriculum is not a recurring capability class"*), **v196 meetily** (corpus-first for a domain ≠ mintable), **v210 AIRI**, **v220 little-book-rl**.
2. 🔴 **The distinctive property is an ABSENCE.** The candidate class is defined by what the tool declines to do. A §C row that names a missing integration is not a capability; the positive description — *renders a prompt into a text box and parses what you paste back* — is a **form factor**, which is the **v102** cookbook precedent and the **v236/v227/v222** front-end chain.
3. 🔴 **Not world-first and not canonical.** Structured copy-paste LLM workflows and prompt-template tools long predate this. Under **v222** (*world-canonical is not world-first*) a **7★ / 11-commit / 88-file** repository claims neither.
4. 🔴 **§28 anti-inflation** at **51 live standalones**, ≤2 per ship, clustering-first, against a **bus-factor-one** anchor whose author has three git identities and no licence — the **v180 / v234** weak-anchor precedent.
5. 🔴 **The sibling was declined one day earlier on five grounds** (v256). Minting this while declining that requires a distinction stronger than "the LLM is a larger share of this one," which is a difference of degree.

**Any one of grounds 1–3 is sufficient. `inflation_check` HELD.**

⭐ **What I do record for the audit, because it is genuinely new:** a **DEFERRED WATCH AXIS — "manual/human-transport LLM workflow: a tool built so the operator's chat subscription substitutes for API billing, with no automation of the transport."** This is the counterpart to the **v207/v208/v231/v232 gateway cluster** and belongs on the audit agenda as a boundary question against those rows, **not** as a mint. Recorded, not executed — a promotion is an audit act.

**Recorded, not self-incremented:**

- **#83 — POSITIVE and NEGATIVE in the same document, for the second consecutive ship.** POSITIVE: the README's *"Tình Trạng Phát Triển Hiện Tại"* NOTE block openly discloses that the `review_*` steps are registered as local steps only to keep the flow continuous and are actually performed in the Editor tab — an unprompted admission that a documented step is a placeholder. NEGATIVE: the unmeasured 80% claim, the `.bak` misattribution, and a primary launch command that starts the wrong program.
- **#12 — a clean NEGATIVE, and a same-author N=2** with v256. Zero agent-surface files and zero `.yml`/`.yaml` on any ref in **either** repository.
- **#66 — a mixed exemplar.** Clean secrets posture (`api_key_env`, `.env.example`, `.gitignore`) against an unbounded `openai>=1.0.0` floor, no lockfile, and 18 committed `.pyc`. Useful beside **v256**, which was a strong negative, and **v228 pi**, the corpus's positive pole.
- **#19 — the author archetype gains its second data point.** `translate-LN-pipeline` (text) and `my_manga_translator` (image) are two halves of one Vietnamese content-localization toolchain, alongside `novel_studio`, `Anime_Vault` and `VOCra`.
- **NOT #52** (7 page-stated stars; §37.4 — the API is mocked here, so no velocity claim exists).

**Tier:** application/client tier, ⚠️ reviewable.

---

## 4. Streak and ceilings

- **Streak: v256 `GA:114` → `GA:115 · OG:13 [7 ov]`** — **38 consecutive GOAL-ALIGNED ships, v220 → v257.**
- **§35 CLEAR** — window {**v255 GA**, **v256 GA**, **v257 GA**} = **0 OFF-GOAL**.
- **No override consumed** (§40). Lifetime operator overrides remain **10**; v153 → v257 = **zero**.
- ⚠️ **The audit is now 45 ships overdue** (last audit v212; v213–v257 all shipped).

**This ship adds to the audit agenda:** the manual-transport watch axis above and its boundary against the v207/v208/v231/v232 gateway cluster; the **same-author control method** itself (§9 of the Deep Dive) as a reusable ship shape; the second consecutive **#83 both-poles-in-one-document**; the **#12 same-author N=2**; and method rule **D45** below.

---

## 5. Method rule this ship proposes

**D45 — read the tree, then the file the documentation names.** Three times in this ship I grepped the single file the README pointed at, found nothing, and nearly published an absence: the `.bak` mechanism (real, in `jsonio.py`, not the named `workspace.py`), the three-level prompt lookup (real, in `workspace.py`, not the named engine), and the confidence policy (real, in `review_flags.py`, at a third threshold). **All three would have been false findings, and all three became better findings once found.** This is **D42** (*a negative from a truncated search is not a negative*) with the specific failure mode named: **documentation that misattributes a real feature produces a false negative in exactly the reader who checks it.** The procedure is to search the whole tree for the *mechanism* before concluding anything from the *location*. Third consecutive ship where this class of error appeared in my own work — v255 the `set --` word-split, v256 the truncated font search, v257 three misattribution traps — which is why it is being written down as a rule rather than a note.

---

## 6. The three things worth remembering

1. ⭐⭐⭐ **The habits are the constant; the quality is the variable.** Same author, same month, two repositories: this one's dependency file is three clean lines and the sibling's cannot resolve; the sibling's response validation is five layers deep and this one has none; this one has real screenshots and the sibling's README points at images that never existed — **and it added them the day before editing the other README without fixing it.** Yet the *bookkeeping* failures are identical in both: an ignore rule that arrives alongside the files it would exclude, one fact declared in three places, committed artifacts carrying the author's own machine paths, dead generations left in the tree, no CI, and an unmeasured headline number. **Discipline attaches to whatever surface the developer was thinking about; structure fails everywhere else.**
2. ⭐⭐⭐ **A gate can outlive its signal source.** The release gate skips any row not marked `"success"`, is consumed in two files, and is correctly written — and in the generation that actually ships, the only code that writes that field hardcodes `"success"`. The one place that can write `"failed"` belongs to a generation the README does not document. The gate cannot fire, and nothing about it looks broken.
3. ⭐⭐ **When one policy is written down three times, the copies disagree.** The model is told the thresholds are 0.72 and 0.82; the application enforces 0.8; the config file that declares the canonical pair is not read by the application at all. Each copy looks authoritative in isolation, and the four most valuable escalation conditions — the ones that say *always ask a human when you could not identify the speaker* — exist only in the copy nothing reads.

**Suggested next action:** review and merge `wiki/v257-translate-ln-pipeline` (the chain v204 → … → v256 → v257 merges in order), then **do Rung 1 of the Pilot Menu** — two hours, nothing installed, and it converts this subject's declared-but-unwired review policy into the one hireui actually needs. Then **make v258 the audit**, now 45 ships overdue; it has a genuinely new agenda item in the manual-transport axis and a reusable method in the same-author control.
