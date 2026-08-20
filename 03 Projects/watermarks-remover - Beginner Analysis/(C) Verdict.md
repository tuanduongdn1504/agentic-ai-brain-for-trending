# (C) watermarks-remover — Verdict (REBUILT)

> Rebuilt from scratch 2026-08-20 at operator request, replacing the original v251 verdict.
> Original recoverable at `74c1b2a`. Subject re-pinned at HEAD `d5563d2` (the original pinned `1cc2783`, 12 commits earlier).

---

## Rating — GOAL-ALIGNED INCLUDE 3/4 (unchanged)

| Criterion | Call | Basis |
|---|---|---|
| **(a) Anthropic affiliation / registered vendor-direct source** | **FAIL** | Guillaume Meyer is a disclosed individual — entrepreneur, Microsoft MVP, founder of Memo, Paris/LA. No declared Anthropic affiliation. Per §41, a disclosed individual is not a registered (a) axis; no name, locale or notability inference. |
| **(b) Goal relevance** | **STRONG** | Ships as a Claude Code / Cursor agent skill; the subject is AI content provenance, which bears directly on any candidate-facing LLM feature and on EU AI Act Article 50 exposure in the operator's market. No §40 needed. |
| **(c) Technical quality** | **STRONG** | 25,873 lines of stdlib Python, 549 tests at 0.749:1, three CI workflows with zero soft-fail, pip-audit + CodeQL, loopback-first design, genuine SSRF and zip-bomb hardening. |
| **(d) Corpus value** | **STRONG** | The strongest structured limitation disclosure in the corpus; a seventh replication of the `silent` detector with a live prospective validation; and — new — a controlled measurement of the vault's own error profile. |

**Streak: unchanged.** This is a rebuild of an existing ship, not a new one. No streak increment, no §35 movement, no override.

---

## Mint decision — **NO MINT**. Counts **46 / 11 UNCHANGED**. §C live standalones **51 unchanged**. Surface ≈58 unchanged.

Four independent grounds, any one sufficient:

1. **Not world-first.** ExifTool has stripped metadata since **2003** (verified: Phil Harvey, 2003-11-19). The "AI humanizer" product category is commercially mature. C2PA's own specification names manifest stripping in its threat model. At least two other open-source AI-watermark-removal repositories exist.
2. **The differentiating machinery is external** (v242 **D25**). MarkLLM, MarkDiffusion, CtrlRegen and reverse-SynthID are all upstream projects loaded from user-supplied checkouts. This repository is the wiring, the format coverage, and the honesty layer — not the watermarking science.
3. **Technique / domain, not a capability class** (the v211 and v196 discipline).
4. **§28 anti-re-accumulation** at 51 standalones.

**Strongest alternative, recorded and NOT self-executed:** a §C standalone at N=1, *"Agent-Skill Capability Layer for Defeating AI Content Provenance"* — genuinely corpus-first for the surface. Declined on grounds 1–4 above and flagged to the overdue audit for review.

**Closest relative:** v209 `gpt-5.6-instruct` — an offensive artifact catalogued as defensive threat intelligence. One difference: v209's payload had no legitimate use. This one has several (privacy, engineering hygiene, watermark-robustness research), plus an ethics file that names the abusive cases and places them out of bounds.

**Deferred watch axis (N=1), carried forward:** *"AI content provenance as a contested surface — marking, detection and removal as an adversarial pair."*

---

## What changed versus the original v251 verdict

The verdict itself does not move. The **evidence under it** does, in four places:

**Corrected:**
1. 🔴 **"An agent skill that ships ZERO code" is wrong.** The repo ships **two** skills; `skills/clean-user-facing-text/` carries **four Python scripts, 1,038 lines**, including a vendored byte-identical copy of the 724-line Layer A engine. Present at the original pin. The claim was recorded as a *correction of the critic* — the critic was right.
2. 🔴 **"Guillaume Meyer 106 of 128" is a base mix.** At the pin, by name: **80 of 128**. All-refs gives 108/167; HEAD gives 81/140. Nothing gives 106/128.
3. ⚠️ **"Redirects refused" is the wrong verb.** They are followed with per-hop revalidation and origin pinning — cross-origin redirects are refused, same-origin ones are not.
4. ⚠️ **"Format matrix checks BOTH ways" is half true.** Docs→code is clean (no phantoms). Code→docs is not: 41 dispatched extensions, 21 named in the README table.

**Confirmed, at the original pin, every one:** all four README hedge citations, `rewrite_text.py:495`, `vendor-notes.md:47`, `how-claude-marks.md:21`, `test_lightweight_skill.py:79-85`, `detect_text_watermark.py:8-10`, the 52,787-byte benchmark, 23,605 lines / 465 tests / 0.69:1, 61 trailer lines across 36 commits with all four AI-tool tallies, `continue-on-error` = 0, the 128 MiB zip caps, the empty `benchmarks/`, the ethics grep, the licence-derived Docker column, and the `wr-synthid-score` self-correction.

**Sixteen citation checks, sixteen passes. Four count-and-inventory claims, four failures.** That is the finding: quoting a file you have opened is reliable; enumerating a directory and generalising from one member is not.

**Strengthened by new evidence:**
- The headline is now **stronger**. A **third** detector shipped (`detect_gumbel.py`, 308 lines) and it too is a same-key closed loop, saying so in its own docstring: *"A negative result establishes nothing… This detector is not a vendor oracle."*
- The benchmark's own header declares the ceiling: *"Google retired SynthID text watermarking on its API in Aug 2026, **so no vendor tier exists**."*
- Anthropic's own support page — not the repo — confirms detection is **"forthcoming."** The caveat is vendor-confirmed, not self-serving.
- The 24 hours after the original ship produced **nine commits of exactly the false-clean defect class** v251 named, **eleven of twelve authored by strangers**. A diagnosis validated prospectively, by the subject, in a day.

---

## Security — LOW

No broken-authentication triad: **zero CORS** anywhere in the repo, loopback-default binds on both HTTP servers, and auth that fails open only when unconfigured and only behind loopback, with an explicit warning. SSRF handling is better than most production code (IPv4-mapped IPv6 unwrapped, `is_global` enforced, per-hop redirect revalidation with origin pinning). Zip bombs capped at 128 MiB **per member and cumulatively**. Containers read-only, non-root, tmpfs. Installer touches no network and has no postinstall. Three CI workflows with **zero** `continue-on-error` and **zero** `|| true`.

**One unaddressed gap:** a fetched web page enters the agent's context and nothing treats it as untrusted text. Low severity — the worst realistic outcome is a bad clean — but the sentence is missing.

---

## Pilot — 🔴 READ-AND-BORROW. **DO NOT INSTALL.**

**Not on security grounds.** The engineering here is better than several tools this corpus has piloted. The block is **purpose**: hireui handles candidate data under the RATIFIED candidate-LLM legibility ADR, EU AI Act Article 50 is live in the operator's market, and recruitment is precisely the context the subject's **own** `ethics.md:14-16` places out of bounds.

**Take three things, install nothing** — detail in the Pilot Methods Menu.

🔴 **Never:** point it at candidate CVs · present AI-assisted output as human-written in hiring · cite its removal as verified (its own matrix says **"No"**, and it publishes **zero** results) · repeat the `DETECT_TEXT_WATERMARK` claim in `vendor-notes.md:35`, whose cited forum thread does not support it · cite the star figures as verified · build a candidate-facing AI-authorship detector on `score_stylometry.py`. On that last point the arithmetic is decisive: the forensic-readiness study (arXiv:2607.16010, verified) measures baseline false-negative rates of **70–83% with nobody attacking**. An absent mark is not evidence of human authorship, and a false accusation on a hiring decision is not a recoverable error.
