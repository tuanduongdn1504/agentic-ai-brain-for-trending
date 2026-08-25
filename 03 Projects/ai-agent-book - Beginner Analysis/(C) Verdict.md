# (C) Verdict — `bojieli/ai-agent-book` (v280)

**GOAL-ALIGNED INCLUDE 3/4 · NO MINT · counts 46/12 UNCHANGED · §C-1 13, §C-2 39 UNCHANGED**
Apache-2.0 · 1,670 commits · 11,713 files · 91 authors · 14 languages · 109 experiment dirs · **live** (pushed mid-clone)

---

## Phase 0.9 screening (STRICT)

| Criterion | Call | Ground |
|---|---|---|
| **(a)** Anthropic-affiliated / registered vendor-direct source | **FAIL** | Bojie Li is **Chief Scientist at Pine AI** (`19PINE-AI`), lecturer at 图灵 / 中国科学院大学. Not Anthropic. §41 forbids inference from notability, heritage or locale. Citing `anthropics/skills` is not affiliation. |
| **(b)** Goal-relevance | **STRONG** | A ten-chapter engineering book on *building AI agents* — the vault's goal #1 verbatim. `grep -oi` in `book/*.md`: **claude 82**, **anthropic 60**. Claude Code is a named reference architecture; ch5's thesis is coding-agent-plus-filesystem as the foundation of all general agents; ch7 is an evaluation methodology. No §40 needed. |
| **(c)** Depth / substance | **STRONG** | 1,670 commits over 11.5 months, 11,713 files, 109 experiment directories, **772** test functions, 8 evidence ledgers, 14 editions, 202 merges, PR #999. |
| **(d)** Corpus fit / novelty | **STRONG** | Extends the six-ship gate arc with a fifth, sharper instance; Pattern #57 at N=3; the corpus's strongest published-negative-results artifact. |

⇒ **GOAL-ALIGNED INCLUDE 3/4.** No override. **§35 CLEAR** — window {v278 GA, v279 GA, v280 GA} = 0 OG.

---

## The sentence

> **Every check in this repository compares one copy to another copy. Nothing compares a claim to the tree.**

Five independent sites, each verified by my own commands:

1. **The count.** CI computes the correct figure (**118**) and prints it on every run; the README publishes **108** and **103**; they are never compared. The claim was **exact twice** — 88 = 88 at birth, 92 = 92 the next day at a commit titled *"Fix stale project counts"* — and has not matched since 2026-07-30.
2. **The translations.** Thirteen editions replaced a 9-row error-taxonomy table with a paragraph. **Section counts stayed identical at 49 across all fourteen editions, before and after** — the structure was perfect and 11 rows had vanished from inside it. The gate fires on `book*/**` and `grep -n "book" scripts/check_i18n_consistency.py` returns **0 matches**.
3. **The 14th language.** `docs/` holds 13 locales, no `he`; Hebrew's README is at the root. `discover_locales()` cannot see it, so the full `book-he/` edition is exempt from all six checks — while `README.he.md` is an explicit *trigger* of the workflow whose script ignores it.
4. **The evidence.** Experiments **7-3 and 7-4** are marked `Complete` with links to `.json` files that `git log --all` proves were **never committed** — because `.gitignore` blanket-ignores `results/` and the hand-built allowlist names 7-11 and not them.
5. **The capstone.** `test_ledger_links_resolve_to_existing_files` — docstring: *"**Every** ledger link … must point to a real file"* — matches **7 of 53** links (13%), because its regex demands a bullet at line start ending in `.md`. The broken links are `.json`, inside table cells. It is permanently green.

**The corollary.** The discipline is genuine — this is a careful engineer, and the numbers were right while one person could hold them. It stopped being right exactly where his memory had to hold two files at once. **v274's rule was "a claim is safe when a gate covers it, or when a habit covers it." Here the habit covered it until the repository outgrew the habit, and every gate had been pointed at agreement instead of truth.**

---

## Mint decision — **NO MINT**

| Ground | Detail |
|---|---|
| **Domain-not-capability (decisive)** | It is a book. The corpus declines books and curricula consistently: **v197** mlsysbook · **v191** AI-For-Beginners · **v270** Foundations-of-LLMs · **v220** little-book-rl. T3 Education tier. |
| **Technique-not-capability** | The distinctive artifact — the evidence-gated experiment ledger — is a documentation *practice*, not a capability layer. |
| **Not world-first** | ACM artifact evaluation, ML reproducibility checklists and papers-with-code precede the reproducibility-ledger idea. |

⚠️ **Recorded as the audit-reviewable §C-2 candidate, not minted:** *"Evidence-Gated Companion-Experiment Ledger for a Technical Book"* — a book whose companion experiments carry a public per-experiment status distinguishing Complete / Incomplete / Reader-exercise, which publishes negative results and refuses to count a smoke test as completion. Genuinely corpus-first in shape; **bundled inside the education genre**, and the corpus mints conservatively there. This is the v279 handling of the auth gate, applied.

**Recorded, not self-executed:**
- **Pattern #57 at N=3 in a single subject** — `NousResearch/hermes-agent` (**v227**/**v268**), `unslothai/unsloth` (**v245**), `browser-use/browser-use` (**v41**), all pinned as experiment targets. Experiment 9-8 hands the whole book *plus Hermes's own source* to Hermes and has it modify itself through three reviewer rejections.
- **T3 Education tier** instance-strengthening (v197 / v191 / v270 / v220).
- **Method-rule candidate:** in zsh, `"$var:path"` triggers the `:c` history modifier and silently returns the wrong file — brace every variable preceding a colon in a git revspec. *(This produced wrong numbers in my own analysis before I caught it. D51 class.)*

**Streak:** `GA:136` → **`GA:137 · OG:13 [7 ov]`** — **60 consecutive goal-aligned ships v220→v280.** Override review **20th consecutive discharge**. Tier **T3 Education** (+ a T1 experiment-collection facet).

---

## Hazards — facts only

- 🔴 **Never cite an experiment count from this README.** It publishes 108 and 103 on one page; disk holds 109 directories; CI derives 118 rows. Say which basis you mean. **99 ✅ + 4 🚧 = 103** is a coincidence that lets a reader "confirm" the wrong number.
- ⚠️ **Do not treat `Complete` in `EXPERIMENT_STATUS.md` as "evidence is in the repo."** It is true for the ones I spot-checked with committed artifacts (7-11 at 14.96 MB) and false for **7-3 and 7-4**.
- ⚠️ **Translations may lag the Chinese in content while matching it in structure.** Chapter 7 was realigned on 2026-08-25; no gate prevents recurrence, and no other chapter has been audited this way.
- ⚠️ **Hebrew is outside every consistency check.**
- ⚠️ **Running experiments costs real money and, in places, real risk**: live computer-use, GPU training runs (RTX PRO 6000-class), robotics actuation tracks, and paid multi-provider campaigns. The evidence packages describe campaigns of 148,856 provider receipts (10-5) and 1,440 trajectories (7-11).
- ✅ **Cloning and reading is safe.** No `pull_request_target`; all actions version-pinned; explicit `permissions:`; the only key-shaped strings in the tree are fixtures in the repo's own redaction tests. Install-time execution exists only inside **vendored third-party** trees (e.g. AWorld), not in the book's own packaging.

---

## Suggested next action

Merge the chain and take **Rung 1** — the vault item is thirty minutes and it is the sixth ship in a row pointing at the same unfinished job. Details in `(C) Pilot Methods Menu.md`.

**Artifact:** https://claude.ai/code/artifact/d5eb5324-4ca3-4f51-84fe-e1699462655b
