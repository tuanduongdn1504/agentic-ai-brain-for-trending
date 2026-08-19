# (C) watermarks-remover — Verdict

**Subject:** [`guillaumemeyer/watermarks-remover`](https://github.com/guillaumemeyer/watermarks-remover) · **Wiki v251** · 2026-08-19
**Licence:** MIT · **HEAD:** `1cc2783` · **Source verified:** two independent clones, `diff -rq` clean both ways

---

## Rating

**GOAL-ALIGNED INCLUDE — 3/4**

| Axis | Call | Reason |
|---|---|---|
| (a) Anthropic affiliation | **FAIL** | §41: Guillaume Meyer is not Anthropic; no registered vendor-direct axis. No inference from name, email or locale. |
| (b) Goal relevance | **STRONG** | An agent skill for Claude Code (the operator's primary tool), and its subject matter — AI-output provenance under EU AI Act Art. 50 — bears directly on any LLM feature hireui ships. |
| (c) Quality/rigour | **STRONG** | 23,605 lines of Python, 465 test functions, clean CI, exemplary licence hygiene, unusually honest documentation. |
| (d) Corpus value | **STRONG** | The corpus's first subject whose object is AI provenance itself. |

**No override needed; no §40 invoked.** (b) is cleanly STRONG.

**NO MINT. Counts 46/11 UNCHANGED. §C live standalones 51 unchanged.**

---

## The one-sentence finding

**They built a rigorous instrument to measure whether watermark removal works, and that instrument is structurally incapable of measuring the one watermark the tool exists to remove — and rather than hide this, they wrote it into the README four times and compiled it into two of their own Python files, so it reaches the user at runtime.**

---

## Why it matters

The **EU AI Act Transparency Code took effect 2026-08-02**; Anthropic's marking applies to models released on or after that date, under an Article 50(2) Code of Practice it has signed. **The announcement reached press on 2026-08-11 at 05:13 PDT** (TechCrunch). **This repository's first commit is timestamped 2026-08-11 09:32 −0700** — *"Initial skill: remove Claude text marks and C2PA metadata."*

⭐ **Four hours and nineteen minutes.** Eight days later it stands at 128 commits, 8 releases, 26 contributor identities and (page-stated) **15.1k stars**.

⚠️ Stated precisely: same morning, ~4h after publication, same timezone. That the author saw *that* story is inference; the timing is the evidence.

The delivery vehicle is the sharp part: **an agent skill you install into Claude Code.** You use Claude to strip Claude's own compliance marks.

And then the project does the thing almost nobody does. Its `removal-matrix.md` carries a column headed **"Verifiable today?"** which answers **"No"** for statistical text watermarks and **"No"** for pixel image watermarks — its two headline capabilities. Its README contains a section arguing that its own Layer B is probably pointless: *"If the plan is to rewrite the text with a cheaper model anyway, why pay for a premium model in the first place?"* Its detection harness states that detection is *"only valid against the SAME scheme config + keys used at generation."*

**15.1k people starred a watermark remover whose own documentation dismantles the reason they starred it.**

---

## Decisions

### NO MINT — four grounds

1. **Not world-first.** Metadata scrubbing is `exiftool`'s decades-old core function; the commercial "AI humanizer" industry predates this substantially; C2PA's own threat model acknowledges hard-bound manifests are strippable.
2. **The differentiating machinery is external** (v242 **D25** / v246). MarkLLM, MarkDiffusion, CtrlRegen and reverse-SynthID are all upstream projects loaded at runtime from user-supplied checkouts. This repo is the wiring and the honesty layer, not the removal engine.
3. **Technique/domain, not a capability class** (the v211 PixelRAG and v196 meetily discipline).
4. **§28** anti-inflation at 51 live standalones.

⚠️ **Strongest NO-MINT alternative — RECORDED, reviewable, NOT self-executed:** a §C standalone at N=1, *"Agent-Skill Capability Layer for Defeating AI Content Provenance."* It is genuinely corpus-first for the surface — nothing in 250 prior ships targets provenance removal. Declined on grounds 1–4. **Flagged to the overdue audit.**

### New DEFERRED watch axis (N=1)

*"AI content provenance as a contested surface — marking, detection and removal as an adversarial pair."* The corpus's first subject whose object is **the provenance of AI output itself** rather than a capability an agent gains.

### Closest corpus relative

**v209 `gpt-5.6-instruct`** — an offensive/dual-use artifact catalogued as **defensive threat-intel**. Same handling, with one material difference: v209's payload had no legitimate use, while this has a real one (metadata hygiene on your own files) and an ethics document that explicitly forbids the abusive cases.

---

## Where it sits in the v246→v250 code-vs-prose set

⭐⭐⭐ **This is the first member of the set to face a genuinely UNDECIDABLE constraint, and it handles it correctly on both clauses.**

The ledger is exact. Every constraint protecting **the file** is code: XXE refusal (`audit_website.py:76`), SSRF refusal (`:211`), zip-bomb caps (`container_meta.py:771`), unknown-format refusal, binary-input refusal, body/batch caps, redirect refusal. Every constraint protecting **the world** is prose: `references/ethics.md` and the SKILL.md Ethics section, addressed to a language model. A grep of all Python for `consent|authoriz|you own|ethic|fraud|academic` returns **only HTTP `Authorization` headers**.

By v250's rule — *you can only compile the part of your aesthetic that becomes a lie when violated* — this is **correct**. "Do you own this content?" is not decidable from the bytes. And v250's second clause — *when you leave one in prose, do not call it non-negotiable* — is also satisfied: `ethics.md:32` explicitly disclaims liability *"for potential misuse by users"*, which is an admission of non-enforcement, and the file's own H1 is *"Intended use"*, not "policy".

**v250 articulated the boundary. This one stands on the far side of it and says so.**

---

## Other confirmed corpus tests

| Test | Result |
|---|---|
| **v247 D34** (are the gates wired?) | ✅ **CLEAN PASS — 2nd consecutive.** 3 workflows, `continue-on-error` = 0, `\|\| true` = 0, `pytest -q` runs the full suite, plus `pip-audit`, ruff lint+format, OpenAPI validation, Windows smoke, CodeQL. |
| **v246 `grep -rni "silent"`** | ✅ **6th consecutive replication, NEW SPECIES** — the silence hunted is a **false success**: exiftool exits `0`, viewers show no metadata, *"but the original metadata bytes stay in the file verbatim"*. Fixed with `qpdf --linearize`, **with a test** (`tests/test_pdf_structural_rewrite.py`), and a loud warning when qpdf is absent. |
| **v231/v232 broken-auth triad** | ✅ **NO TRIAD.** Loopback default (`server.py:951`), **no CORS at all**, auth fails open but only behind a loopback bind and with an explicit stderr warning (`:970`). |
| **v244/v245/v246 licence set** | ✅ **THE COUNTER-EXAMPLE THAT CLOSES IT.** A Docker image table whose **"Published?" column is derived from each upstream's licence** (`README.md:218-224`), including one upstream that *"ships no LICENSE"* — correctly treated as all-rights-reserved. Repeated in `compose.yaml` ×3, a README section, the changelog, and the sidecar docstring. |
| **v240 inventory rule** | ⚠️ Partial. 7 of 27 service scripts are never named in the 65KB README; most are internal modules, so the finding is weak. |
| **v243 duplicate-file drift** | ⭐ A **byte-equality test** (`tests/test_lightweight_skill.py:79-85`) — weaker than ToolJet's symlink, but it carries the incident that caused it (`:89`). |
| **v250 filename-inventory trap** | 🔴 **CAUGHT ME AGAIN.** I flagged `synthid_score_server.py` as an undocumented second server because the *filename* appears zero times in the README. It is documented by **role** (`wr-synthid-score`). Self-caught in two steps. Fix, both times: read the parent document, don't diff filenames. |

---

## Defects found in the subject

1. 🔴 **"Google confirmed" over-states its source.** `references/vendor-notes.md:35` claims Google confirmed the API no longer watermarks text *"and `DETECT_TEXT_WATERMARK` is rejected on current (3.x) models."* I fetched the cited developer-forum thread: it supports *"Generated text from the API is NOT SynthID-watermarked"* and *"Native text watermarking is not planned at the moment"*, but **says nothing about `DETECT_TEXT_WATERMARK`**, and the responder's Google affiliation is not established on the page. A forum answer of unverified affiliation was upgraded to a vendor confirmation. Ironically the same file warns at `:47`: *"Do not invent algorithm claims."*
2. ⚠️ **No committed benchmark results.** `benchmarks/` holds only scripts and 8 seed texts; no `results.json`/`report.md` is tracked. The instrument ships; no reading from it does.
3. ⚠️ **`bench_synthid_text.py` is named for a scheme it no longer benchmarks** — its own docstring line 1 says *"Benchmark for **MarkLLM** text-watermark removal."* A fossil of the pivot.

---

## Provenance (D26/D27 applied)

- **106 of 128 HEAD commits** are Guillaume Meyer across **two** author identities (87 + 19) — summing is mandatory; the `noreply` address alone understates him by 18%. A **third** identity appears in trailers.
- **By volume:** 24,200 additions of ~32k total ≈ **75%**. Poorvith M P (3,235) is a genuinely substantive second; Zhaohan Wang (1,398) a real third; then a drive-by tail. "26 contributors" overstates distributed authorship without being false.
- **AI attribution: 61 trailer LINES across 36 COMMITS** (both counts reported, per D26) — Claude Opus 5 ×10, Claude Fable 5 ×2, Cursor ×4, `pi` ×1. **`CONTRIBUTING.md` asks for none of them** ⇒ a left-on default, the 4th instance after v243/v246/v247.
- 73 PR-numbered commits vs 10 merge commits ⇒ squash-merge workflow.
- ⚠️ The `pi <pi@m2.local>` trailer is *suggestive* of a #57 link to corpus subject Pi (v36/v228) but is **NOT ESTABLISHED** — `pi` may be a handle.

---

## Verdicts

**Security: LOW.** Loopback default, no CORS, genuine SSRF hardening (unwraps IPv4-mapped IPv6, strips zone identifiers, rejects on `is_global`), XXE and zip-bomb guards, non-root read-only containers with tmpfs, env-only API keys, redirect refusal, a staged installer with rollback and no network, SHA-pinned CI with `pip-audit` and CodeQL.

**Pilot: READ-AND-BORROW. Do NOT install.**

Not on security grounds — the engineering is better than several tools this corpus has piloted. **On purpose grounds.** hireui handles candidate data under a RATIFIED ADR demanding legible, audited, human-in-loop LLM paths; EU AI Act Art. 50 transparency is live in the operator's market; and hiring is exactly the context the subject's **own** `ethics.md:14-16` places out of bounds. There is no configuration in which this belongs near hireui.

🔴 **NEVER:** point it at candidate CVs or submitted documents · use it to present AI-assisted output as human-written in hiring · cite its removal as verified (**its own matrix says "No"**) · repeat the `DETECT_TEXT_WATERMARK` claim · cite the star count as verified.

---

## Error ledger — 12 caught, 3 MINE

**MINE (all corrected before ship):**

1. 🔴 **The date framing — the most consequential error of the run.** I wrote *"nine days later,"* measuring 2026-08-02 → 2026-08-11. Wrong interval: **Aug 2 is the EU AI Act effective date, not an announcement.** The announcement broke 2026-08-11 05:13 PDT and the first commit is 09:32 −0700 — **the same morning, ~4h19m later.** Caught by the contradiction-over-situate stage, then verified by me at TechCrunch and Anthropic's own news post. **The correction makes the finding stronger, not weaker.**
2. 🔴 **Contributor count 27 → 26.** I read a `shortlog` and counted rows by eye instead of piping to `wc -l`. All three counting methods agree on **26**. The exact error shape this vault warns about: *settle a count with a command, not by looking at it.*
3. ⚠️ **"An undocumented second HTTP server."** I grepped for the *filename* `synthid_score_server.py` (0 hits in README) and missed that it is documented by **role** as `wr-synthid-score`, with its non-commercial licence disclosed in four places. Self-caught in two steps. **The v250 filename-inventory trap, repeating.**

**THE FLEET'S (9):**

4. **Seven fabricated line citations** in the what-it-does report — `SKILL.md:343-344` in a 321-line file; `rewrite_text.py:285-298` for a function actually at `206-222`; `container_meta.py:80-85`; `server.py:68-70`; `server.py:67-92`. All caught by the contradiction stage.
5. **A grep count inflated from 114 to 185** (+62%) in the ethics report.
6. **Undocumented env vars claimed "32+", actual ~18.**
7. **Coverage ratio 0.65 claimed, 0.694 actual** — from dividing by a source-line figure that was itself wrong.
8. **MarkDiffusion dated October 2025; arXiv 2509.10569 is September 2025.**
9. **Forbes/Register coverage asserted HARD-VERIFIED with no URLs in the read receipt** — the fabrication pattern the situating-contradiction stage exists to catch. Unverifiable; discarded.
10. **The ethics report missed `SECURITY.md`** marking fraud out-of-scope, and missed the second skill's own ethics docs — a 3-document count where 6+ exist.
11. **The critic mis-framed the thin-client rule** as unenforced prose. It is **structurally enforced by absence**: `skills/remove-ai-marks/` contains only `SKILL.md` and `references/` — there is no script in the skill to run. That is enforcement-by-construction, the same class as v243's symlink.
12. **The contradiction-over-situate stage did not flag the Forbes/Register missing URLs** even while catching the date error — an oversight in the checker, logged by the critic.

⭐ **METHOD NOTE — the v249 fix worked a second time.** Pointing a contradiction stage at the *situating* reports (not just the code reports) is what caught the date error, which was the single most consequential mistake in this ship and was **mine**, not an agent's. ⚠️ But the pattern from v250 holds too: **I still had to verify the correction myself** — the critic asserted the announcement was Aug 11 without distinguishing it from the Aug 2 effective date, and only fetching TechCrunch and Anthropic's own post produced the precise, defensible version.

⚠️ **One agent failed:** a contradiction stage hit the StructuredOutput retry cap (5) and returned nothing, leaving one code surface with a map report but no contradiction pass. Its claims were hand-checked by me instead. 17/18 agents completed; ~2.33M tokens, 563 tool uses, 893 s.

---

## The three borrowable ideas — zero install

1. ⭐⭐⭐ **A "Verifiable today?" column.** Put per-capability verifiability *in the capability table*, and answer "No" where you must. Port to hireui's feature matrix (discharging the ADR's unimplemented eval-gating clause) and to `PATTERN_LIBRARY.md`.
2. ⭐⭐⭐ **Propagate the hedge into the runtime output, not just the docs** (`rewrite_text.py:495`). For hireui Match-Explain, the confidence caveat belongs in the **API response body**, so every consumer inherits it.
3. ⭐⭐ **Byte-equality assertion for duplicated content, with the incident in the comment** — fold into the v250 Rung-1 `bin/verify-vault-inventory.sh` as a fourth clause.

### ⭐ And the direction inversion, which is the operator-relevant point

This tool removes marks from **output you generated**. A recruitment product's live question is the opposite: **detecting AI authorship in candidate input** — CVs, cover letters, take-home submissions. The two problems share a map but point in opposite directions.

What this repository is genuinely good for, read that way:
- `image_meta.py` + `container_meta.py` (**153,786 bytes**) are a per-format inventory of where provenance lives in ~20 formats — i.e. **what an upload pipeline must preserve** rather than silently destroy on re-encode.
- `score_stylometry.py` is **zero-LLM** cadence/burstiness scoring — detection with no model call and no data leaving the box.
- The `/inspect` and `/detect` endpoints are read-only.

🔴 **But the hard limit must be stated in the same breath:** the project's own matrix answers **"No"** to *"Verifiable today?"* for statistical text marks, and `ethics.md:18` says *"A removed mark does not mean the content was never AI-assisted"* — whose converse is equally binding: **an absent mark is not evidence of human authorship.** Any hiring use of AI-detection signal would need the full candidate-LLM ADR treatment, and stylometric "AI-detector" scores are a documented source of false accusations against non-native English writers. **Do not build a candidate-facing AI detector off this.** Read it to understand the terrain; do not deploy it against applicants.

---

## Streak

**`GA:109 · OG:13 [7 ov]` — 32 consecutive goal-aligned ships (v220→v251).** §35 CLEAR (window {v249 GA, v250 GA, v251 GA} = 0 OG).

⚠️ **The ~v221 audit is now 39 ships overdue** (last v212). This ship adds: the recorded §C alternative, the new watch axis, the 6th `silent`-detector datapoint with a new species, the second consecutive D34 pass, and the counter-example that closes the v244/v245/v246 licence set.

---

## Blunt

Anthropic switched on machine-readable marking of Claude output on August 2nd under a code of practice it had signed, and nine days later a man built the remover — as a Claude Code skill, so you use Claude to strip Claude's marks. In eight days it went to 23,605 lines of Python, 465 tests, eight releases and fifteen thousand stars.

The interesting part is not that it exists. It is that the author kept writing after the stars arrived, and what he wrote is the case against his own tool. There is a column in his capability matrix headed "Verifiable today?" and it says "No" on both features anyone came for. There is a section in the README explaining that removing a text watermark means rewriting the text with a weaker model, and asking why you paid for the good model in the first place. There is a sentence — "no tool can honestly certify this fails the official check" — that appears in the README four times and inside two of the Python files, so it reaches the user at runtime and not just the reader.

He built a proper benchmark, too: 52,787 bytes that measure clear rate, score suppression, quality drift and dollar cost. It cannot be pointed at Anthropic's watermark, because detection only works against a key you already hold, and Anthropic has not published one. So the instrument is real and the one number everybody wants is unobtainable, and he says so instead of publishing a number he could not defend. No results are committed at all — which is either the discipline or the gap, and honestly it reads as both.

The ethics are entirely prose, with not one line of code behind them, and that is the right call: no program can check whether you own the file you just handed it. He does not pretend otherwise — he disclaims liability, which is an admission, and titles the file "Intended use". That is exactly the line v250 drew, and this is the first project in the set to stand on the undecidable side of it honestly.

Take three things and install nothing. Put a "how would we know it worked" column in hireui's feature matrix, because the candidate-LLM ADR has demanded eval gating for months and still has no implementation. Put your confidence caveats in the API response instead of the docs, the way he put his in the Python. And when two copies of a file must stay identical, assert it in a test and write the incident in the comment — the vault has a chapter file whose name has been wrong for sixty-eight versions, and nothing has ever noticed.
