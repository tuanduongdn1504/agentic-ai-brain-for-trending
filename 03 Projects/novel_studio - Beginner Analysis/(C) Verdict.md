# (C) Verdict — v261 `mranex/novel_studio`

**2026-08-21** · **GOAL-ALIGNED INCLUDE 3/4** · **NO MINT** · counts **46 / 12 UNCHANGED** · §C-1 **12** · §C-2 **38**

---

## Phase 0.9 gate

| Criterion | Call | Basis |
|---|---|---|
| **(a) cultural-peer / Anthropic signal** | **FAIL** | `mranex` — pseudonymous individual, one email, no disclosed identity, no Anthropic affiliation, no registered (a)-7 source. §41: no inference from name, heritage or locale. |
| **(b) goal-relevance** | **STRONG** | The strongest (b) of the five siblings by a wide margin, and the first that needs no §40. |
| **(c) substance** | **STRONG** | 6,638 lines of Python + 3,004 TSX + 888 TS; 62 endpoints; 12 backend service packages; a 785-line schema module; a Tkinter sub-app; **plus 3,594 lines of recovered specification**. Source-verified by two clones. |
| **(d) legibility** | **STRONG** | Cleanly layered; 0 `TODO`/`FIXME` in 6,638 lines; the recovered `master_plan.md` is professional-grade architecture writing. |

### Why (b) is STRONG — the contrast with v260

v260 had **zero** LLM surface and **zero** agent surface; its single AI-grep hit was `ScrollMode` matching `llm`, and it needed §40 to clear the bar at MODERATE. This subject is the opposite on every axis:

- It is **an LLM application**: an OpenAI-compatible provider abstraction with per-task provider routing (`backend/app/llm/`), a prompt subsystem with six seeded, user-editable templates and a shared JSON-output contract, batch translation jobs with retry, and structured-output validation via Pydantic `TypeAdapter`.
- It is **an agent-built application**, and it committed the machinery: a 676-line master plan, 14 numbered phase specifications, and `Agent.md` — a **149-line, nine-section multi-agent operating protocol** with a mandatory per-phase evidence record, a concurrent-agent filename convention, and an explicit pre-completion verification rule.
- ⭐ It is therefore **directly on Goal #1** — this is what running AI coding agents against a phased specification actually looks like in the wild, including how it fails.

**Cleanly GOAL-ALIGNED. No §40 invoked, no override consumed, no OFF-GOAL alternative worth recording.**

---

## NO MINT — five grounds

The declinable candidate is a §C-2 standalone at N=1: *"Specification-First, Agent-Built Application Shipping Its Own Committed Multi-Agent Handoff Protocol."*

1. 🔴 **Not world-first, and not corpus-first — decisive.** Specification-driven agent development is one of the most heavily represented threads in this corpus: **OpenSpec v49**, **cc-sdd v61**, **gsd-2 v54**, **agent-skills v184** (source-driven / doubt-driven development), **loop-engineering v189** (L0–L3 autonomy, a REJECT-first verifier), and Pocock's grill→PRD→AFK→QA pipeline. `AGENTS.md`-style protocol files are first-party-documented convention. This subject is a competent *instance*, not a new class.
2. 🔴 **The differentiating machinery does not ship — and here that is literal.** The distinguishing artifact is the plan-plus-protocol, and the final commit **deleted all 19 planning files**. A class cannot be anchored on an artifact absent from the delivered repository. (v242 **D25**; the v252 closed-CLI precedent.)
3. 🔴 **Form-factor within a genre.** An offline single-user FastAPI + React desktop-ish tool is the shape already ruled on at **v236 / v227 / v222**.
4. 🔴 **§28 — supporting ground only**, per routine **v2.8 §44 clause 5**, measured against **§C-1 = 12**, and explicitly not load-bearing alone. It is not: grounds 1–3 each suffice.
5. 🔴 **Bus-factor-one anchor with zero verification surface** — one author, four commits, zero tests, zero CI, and a foundation phase whose written acceptance criterion was not met (v180 / v234).

**`inflation_check` HELD** — 0 mints, 0 N-bumps, 0 promotions, 0 retires.

---

## ⭐⭐⭐ The N=5 result: the code improves, the record does not

v260 concluded that four of six same-author habits broke, and that the break was explained by **workflow** (a bulk import) rather than **character** — leaving open whether the author was actually improving. **v261 settles it, in both directions.**

**The code demonstrably improves.** Three defects I recorded against earlier siblings are *fixed here*, in the next project:

| Defect recorded at | v261 |
|---|---|
| **v257** — missing `00_json_output_policy.txt` set `json_policy = ""` and rendered anyway: *a prompt with no JSON contract, no warning* | `storage/files.py:98-104` **raises `FileNotFoundError`**; `read_prompt_file` passes no default. **Loud by default, quiet only on request.** Same concept name, same role, 34 days later. |
| **v260** — `allow_origins=["*"]` + credentials, no auth | `main.py:118` scoped to the two named dev-server origins |
| **v258** — the timeout was on a millisecond probe while the multi-hour encode had none | `llm/client.py:31` `timeout=120` on the call that actually blocks; retry at the job layer (`translation/service.py:177`) |

Add: **all five requirements pins bounded on both sides** (best of the five), atomic **schema-validated** writes with optional backups and a fail-closed `project_root` precondition, zero `shell=True`, zero bare `except:`, zero `TODO` in 6,638 lines.

**The record does not improve — it gets worse.** Both habits v260 identified as *properties of the author* replicate here in their most extreme form:

- **Run-instructions describe something other than the program.** The README's `## Main Documents` lists **eight items and all eight fail** — seven deleted, and `Dont_touch/` never existed on any ref. Its `Verification:` block runs `pytest backend\tests tests`; neither directory has ever existed. Its `## AI Coding Agent Workflow` tells the next agent to read six files, every one deleted, and closes *"See `Agent.md` for the full rules."*
- **No verification, at N=5.** Zero tests and zero CI in all five repositories.

⇒ ⭐⭐⭐ **THE N=5 STATEMENT: engineering quality improves measurably, project over project, on axes I can name and cite. Verification and documentary honesty do not improve at all. Those are two independent skills, and only one of them is learned by writing more code.**

⭐ **The v260 §42 amendment candidate is CONFIRMED and REFINED.** This repository was the **workspace for the specification** (commits 1–3) and a **destination for the code** (commit 4, one 95-file drop) — a third category the amendment did not anticipate, and precisely why the plan survives in the pack while no `.pyc` was ever committed. **Recommendation to the audit: record the workspace/destination status *per artifact class*, not per repository.** Recorded, not self-executed.

---

## Bookkeeping

- **Counts:** 46 top-level patterns · **12** CONFIRMED Library-vocab · §C-1 **12** · §C-2 **38** · max pattern #85. **All unchanged.**
- **Streak:** v260 `GA:117` → **`GA:118 · OG:13 [7 ov]`** — **41 consecutive goal-aligned ships, v220→v261**.
- **§35:** **CLEAR.** Window {v258 GA, v260 GA, v261 GA} = 0 OG (v259 was an audit).
- **Override:** none. §40 not invoked.
- **Tier:** T5 Application, with a genuine **method/process facet** — the recovered plan-and-protocol is the more valuable half of the subject.
- **Secondary, not minted:** #19 19a (fifth `mranex` data-point) · **#12 clean NEGATIVE, N=5** · **#66 MIXED but the best of the five** (bounded pins, scoped CORS, atomic validated writes, no `shell=True`, against plaintext API keys with no warning and 62 unauthenticated local endpoints) · **#83 — a new species: a genuine deficiency disclosure that was WRITTEN and then ERASED** (`master_plan.md` §17 *"Open Decisions"* recorded the plaintext-key risk and required a warning; the warning was never written and §17 was deleted).
- ⭐ **NEW RELATIONSHIP TYPE, recorded for the audit:** the corpus has five **REVISITS** (same repository, later pin — v78, v228, v242, v245, v248) but has never had a **SUCCESSOR**: a *different* repository, same author, same domain, rebuilt from scratch. v257 → v261 is the first. This is not #57 (no corpus subject is cited) and not a revisit. **Recorded, not minted.**

---

## The one-line verdict

**He wrote a better specification than most teams write, had agents build it substantially correctly, fixed three defects I had recorded against his earlier projects — and then deleted the plan, the protocol, the phase specs and the evidence directory in the same commit that declared it done, leaving a README whose central sections instruct the next agent to read files that no longer exist.**

---

## Appendix — the engineering positives, verified by hand

These are the claims I checked myself rather than inherited, because they are the reason this subject reads differently from its four siblings.

- ⭐⭐⭐ **`write_json_atomic` (`storage/files.py:56-96`) is a textbook durable write:** validate against the schema **first**, fail closed if a backup is requested without a `project_root`, create the temp file **in the target's own directory** via `mkstemp` (so the replace is same-filesystem), `json.dump(..., ensure_ascii=False, indent=2)`, `flush()`, **`os.fsync(file.fileno())`**, `os.replace()`, and on any exception unlink the temp file and re-raise. Nothing in the other four repositories is close to this.
- ⭐⭐ **Path traversal is properly guarded** (`storage/files.py:12-18`): resolve root and target, `os.path.commonpath`, and `raise ValueError(f"Path escapes project root: {target}")`. Fails loud.
- ⭐⭐ **`read_markdown` raises `FileNotFoundError`** when the file is absent and no `default` is supplied (`files.py:98-104`) — loud by default, quiet only on request. **This is v257's silent-`json_policy` defect closed.**
- ⭐ **CORS scoped** to `http://localhost:5173` and `http://127.0.0.1:5173` (`main.py:118`) — **v260's wildcard closed.**
- ⭐ **`timeout=120` on the blocking LLM call** (`llm/client.py:31`), with retry at the job layer (`translation/service.py:177`) — **v258's wrong-place-timeout closed.**
- ⭐ **All five dependency pins bounded on both sides** (`fastapi>=0.115,<1.0` … `pytest>=8.0,<9.0`) — the best manifest discipline of the five siblings, and the only one where every line has an upper bound.
- ✅ **`source_preparer` is real and correctly packaged** — 11 modules, a proper `__main__.py`, three tkinter imports. The README's `python -m source_preparer` works as written. *(The fleet's synthesis claimed the opposite on all three counts; see Deep Dive §11.)*
- ✅ 0 `TODO`/`FIXME`/`XXX` in 6,638 lines · 0 `NotImplementedError` · 0 bare `except:` · 0 `shell=True`.

⇒ ⭐⭐⭐ **And that is the tension the ship turns on: the most careful code in the five-repo set sits in the repository least able to demonstrate that any of it works.**

---

## Method note

Hand-verified throughout, with a 27-agent fleet used for one job — grading the 14 recovered specifications. **13 of 14 graded; phase 11 is genuinely UNGRADED** (its agent failed to return structured output). **13 claims overturned by the adversarial refuters, all in the author's favour.**

⭐⭐ **Method result, recorded for the audit:** every agent that read files produced checkable claims; **the one stage that read only other agents' claims — the synthesis — produced all five of the fleet's factual errors**, including calling a delivered, correctly-packaged feature nonexistent, and inventing a *"~85%"* and a *"29 of 34"* that no file contains. **Aggregation stages have no ground truth to be wrong against, and they are the stage a reader is most likely to quote.** ⇒ *point the adversary at the synthesis, not only at the findings; and never let an aggregation stage introduce a number that no file contains.* This extends v249's *"the contradiction stage only protects the stages it is pointed at"* with a structural mechanism.
