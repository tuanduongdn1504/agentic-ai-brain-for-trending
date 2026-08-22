# (C) Verdict — v262 `hoquanghai/Auto-Create-Video`

**2026-08-21** · **GOAL-ALIGNED INCLUDE 3/4** · **NO MINT** · counts **46 / 12 UNCHANGED** · §C-1 **12** · §C-2 **38**

⚠️ **Attribution:** the operator supplied `mranex/Auto-Create-Video`, which the rendered page confirms is a **fork with zero commits by the forker**. All 34 commits are by **Ho Quang Hai**. The subject is the upstream and the credit is his.

---

## Phase 0.9 gate

| Criterion | Call | Basis |
|---|---|---|
| **(a) cultural-peer / Anthropic signal** | **FAIL** | Ho Quang Hai — a disclosed individual, not Anthropic, not a registered (a)-7 vendor source. §41: a disclosed individual answers NO. |
| **(b) goal-relevance** | **STRONG** | A **Claude Code skill is the primary, recommended entry point**; Claude *is* the content engine; and the project's stated thesis — *"AI for content, deterministic code for production"* — is precisely the design question hireui's first LLM feature has to answer. |
| **(c) substance** | **STRONG** | 1,569 lines of TypeScript + 645 of tests; 9 test files / 44 `it()` / **116 assertions**; 2 CI workflows; a 378-line Claude Code skill; a 697-line bilingual README; a live YouTube Shorts demo. Complete and shipped in ~3.5 days. |
| **(d) legibility** | **STRONG** | Small, layered, typed, tested. `src/{config,utils,tts,assets,render}` with a thin `cli.ts` orchestrator. |

**Cleanly GOAL-ALIGNED. No §40 invoked, no override consumed.**

---

## Why this ship matters more than a sixth same-author data point would have

The five-repository control (v256→v261) found exactly one habit that replicated **without a single exception** — across four domains, three GUI toolkits, two languages, durations from 87 minutes to 31 days, and 8k to 55k lines of code: **zero tests, zero CI, zero agent surface.** At v261 I recorded that engineering quality improved measurably project over project while verification did not improve at all, and called the latter a property of the author.

**This repository is the control that isolates the variable**, and I did not select it — the operator handed me the URL believing, as I did, that it was a sixth `mranex` project:

- same namespace (it sits in his account), same language and country context, same *"automate a media pipeline"* domain, same weeks;
- **9 test files, 116 assertions, 3 deliberately-invalid fixtures, 2 GitHub Actions workflows, a 378-line Claude Code skill, `.env.example` committed with `.env` gitignored, and an MIT `LICENSE` file.**

⚠️ **CORRECTED AT v263 — read this instead of what stood here.** I originally wrote that *"he forked this on or after 2026-04-29 and then created four more projects over the following twenty-eight days … the example was in his own account the whole time."* **The fork date is not establishable.** A fork's clone contains the upstream's history up to the fork moment, so its HEAD date (`8c2e043`, **2026-05-02**) is a **lower bound only** — the fork could have been made at any time after that, and GitHub does not expose fork dates in a clone (the API is mocked here per §37.4). ⭐ **D50: a fork's clone gives you a LOWER BOUND on the fork date, never the fork date. Do not build a timeline argument on when someone forked something.** **What survives, and it is still worth the ship:** this repository is in his account, it has 9 test files / 116 assertions / 2 CI workflows / 3 negative fixtures, and his own five projects have none of that. **The contrast is real and needs no dates.** What does not survive is the claim that the example demonstrably *preceded* his later projects. ⚠️ And v263 supplies the counter-case: a second fork in the same account whose HEAD is **2026-06-24**, i.e. necessarily *after* all five — so at least one of these forks postdates his own work in the same domain, which is ordinary, healthy behaviour and not evidence of anything.

⇒ ⭐⭐⭐ **v258 established that code moves forward in time and never backward. v262 extends it sideways: it does not even move forward from a repository you own. FORKING IS NOT ADOPTING.**

⚠️ **Stated fairly, because this is not a character finding.** Forking is not a commitment to adopt; people fork to read, to bookmark, to try. The honest claim is structural: **a practice does not transfer by proximity. Having the example in your account, in your language, in your domain, in the same month, is not having the habit. Practices transfer by doing, not by possessing.**

⭐ **And it closes the six-ship arc.** v261: a protocol with no gate is decorative — nine excellent sections, not one a precondition, zero evidence records written. v262: an example without practice is inert. **Declaration is not enforcement; possession is not practice.** Those two sentences are the whole failure mode of the preceding five repositories.

---

## NO MINT — and the §C-2 catalogue earned its keep

The candidate was an **N=2 of §C row C37** — *"Agent-First End-to-End Generative-Media (Video) Production System"*, anchored on **OpenMontage v188**. A routine collision grep surfaced it; reading its definition killed it.

C37 requires *"an agent-**FIRST** system (the coding agent IS the runtime; **NO** Python orchestrator)"* plus YAML pipelines, a multi-provider **generative-media** abstraction and a **$0 free/local path**. This project has a **deterministic TypeScript orchestrator as its defining feature** — the opposite architectural commitment, stated as its thesis — plus `script.json` behind a Zod schema rather than YAML, multi-provider **TTS** only, and no $0 path (TTS needs a key).

⇒ **Adjacency, not instance.** And the adjacency is informative *because* it is the opposite choice on the same substrate (HyperFrames + FFmpeg).

⭐⭐⭐ **This is the first live demonstration of the argument v259 used to keep §C-2.** That audit declined to retire 38 N=1 rows because *"retiring them would destroy the mechanism that makes collision-detection possible."* Here the mechanism worked exactly as claimed: the row surfaced, its definition was read, a false N=2 was prevented, and the boundary is now recorded so nobody re-derives it. **The catalogue paid for itself.**

A fresh §C-2 mint for the hybrid architecture was also declined on five grounds: **not world-first** (LLM-for-judgement plus deterministic-pipeline-for-output is the standard shape — v217's vision→confidence-JSON→QA-gate, v188's ~90 deterministic tools, v249's *"only ever removes; it never instructs"*); **architectural principle, not capability class**; **domain-not-capability**; **§28 as a supporting ground only** per v2.8 §44 clause 5, measured against §C-1 = 12 and not load-bearing alone; and a small single-author anchor with a 3.5-day history.

**`inflation_check` HELD** — 0 mints, 0 N-bumps, 0 promotions, 0 retires.

---

## Bookkeeping

- **Counts:** 46 top-level patterns · **12** CONFIRMED Library-vocab · §C-1 **12** · §C-2 **38** · max pattern #85. **All unchanged.**
- **Streak:** v261 `GA:118` → **`GA:119 · OG:13 [7 ov]`** — **42 consecutive goal-aligned ships, v220→v262**.
- **§35:** **CLEAR.** Window {v260 GA, v261 GA, v262 GA} = 0 OG.
- **Override:** none.
- **Tier:** T5 Application with a genuine **agent-skill facet** (the skill is the recommended entry point, not an afterthought). Reviewable.
- **Secondary, not minted:**
  - ⭐ **#12 POSITIVE — and it is the first POSITIVE in this run of six.** #12 had five consecutive NEGATIVEs (v256–v261). Real tests, real CI, real negative-case fixtures.
  - **#19 19a** — first `hoquanghai` / Ho Quang Hai author in the corpus.
  - **#66 mostly POSITIVE** — `.env.example` committed with `.env`/`.env.local` gitignored, MIT with a licence file, `nock` for HTTP mocking so the TTS tests do not hit live APIs. ⚠️ Minor: `hyperframes ^0.4.34` is a pre-1.0 dependency behind a caret range, and the toolchain deps (`typescript ^6.0.3`, `vitest ^4.1.5`) are unpinned carets — fine for an app, worth naming.
  - **#83 POSITIVE (small)** — the optional Gemini thumbnail step is documented as *"gracefully skipped if absent,"* an accurate deficiency disclosure.
- **NON-claims:** NOT #52 (the fork shows 1 star; **the upstream's figures are unmeasured — I fetched the fork's page, not the upstream's**, and the API is mocked per §37.4) · NOT #57 (HyperFrames is `heygen-com/hyperframes`, a substrate the corpus *names* via C37, not a corpus subject) · NOT world-first · NOT a C37 instance · NOT executed (no node, no ffmpeg).

⭐ **RECORDED FOR THE AUDIT — new method rule candidate D49:** *a repository's namespace is not a claim about its authorship.* Before attributing a repository to the account hosting it, run `git log --format='%an <%ae>' | sort -u` and check the rendered page for a fork notice. Forks, transfers and org membership all place other people's work under a given name. **I stated N=6 in my own prior message before running that command; the check is one line and it inverted the ship.**

---

## The one-line verdict

**A small, complete, genuinely well-built agent-native pipeline whose one-sentence thesis — AI for content, deterministic code for production — I checked and found true; and, entirely by accident, the control that proves the preceding five repositories' missing tests were never a function of domain, stack or language.**

---

## ⚠️ Appendix — the correction that changed this verdict's shape

My first pass rated this README as the run's strongest claim-versus-code result. **The fleet's claims audit refuted that, and after verifying every item myself, it was right.** The verified split:

**Correct to the digit, and all of it gated or checkable:** *"44 unit tests"* (44 exactly — the fleet said 45 and was wrong) · 1080×1920 @ 30 fps (asserted inside a test) · the 3-tier SFX selector (implemented, 20 assertions) · every dependency version in the Tech Stack table · the determinism thesis (verified in the Deep Dive).

**Inflated or absent, and none of it gated:** *"12 Smart Templates"* — the Zod union has **six**, and `README:201` specifically claims *"discriminated unions (12 template variants)"* · *"6 theme palettes"* naming six themes that appear **only in `README.md` and `README.vi.md`, zero times in `src/`** · a **Gemini 2.5 Flash Image thumbnail stage** in the Tech Stack table and the pipeline diagram, with 0 hits in `.env.example` and 0 in `src/` · **`voiceChunks`** (5 README mentions, 0 in `src/`) · **hyperframes lint/validate/inspect quality gates** (drawn into the diagram, 0 in `src/`) · **`sns_post.txt`** (2 mentions, 0 in `src/`) · fonts (*"Manrope + Anton + Lora"* against `styles.css:5`'s **Inter + Anton + Bebas Neue**).

⭐⭐⭐ **And the repository's final commit is titled `docs: refresh README tech sections to match current codebase`.** The reconciliation was performed deliberately, as the project's last act, and did not converge.

⇒ ⭐⭐⭐ **THE CORRECTED FINDING, which is better than the one it replaces: he built real gates and aimed every one at the CODE. The prose has no gate, so the prose is where the drift lives.** A v250 specimen — *a gate's AIM, not its quality, decides what rots*.

⭐⭐⭐ **And it sharpens the six-ship conclusion rather than softening it.** The five `mranex` repositories had **no gates anywhere**, and both code and docs drifted. This one has **gates on the code** — and its claims are honest *precisely where something checks them*, inflated everywhere else. ⇒ **Tests do not make you honest. They make you honest about the things they test.**

**This does not change the verdict** — GOAL-ALIGNED 3/4, NO MINT, counts unchanged, and the engineering practice is still the first in six worth copying. It changes what the ship is *about*: not "finally, an honest README", but "here is exactly how far honesty extends when you point your gates at one surface and not the other."

⚠️ **My own error, recorded:** I first **refuted** the theme finding because `grep -rn 'tech-blue' .` returned four hits, which I read as existence. All four were in the two README files. **I counted matches without looking at the paths.** `grep -c` answers *how many*; only `grep -l` answers *where*. Same shape as every error in this run — a measurement whose extent I did not inspect, not a misreading of something I had opened.

⭐ **Method note, and it is the counterpart to v261's:** at v261 the fleet's aggregating stage produced all five of its errors while every file-reading agent was reliable. **Here a file-reading agent produced the single most valuable finding of the ship and overturned the orchestrator.** The fleet is worth running for exactly this — breadth across surfaces one reader will not systematically enumerate — and it must be verified item by item, which is what happened.
