# (C) Pilot Methods Menu — `bojieli/ai-agent-book` (v280)

**Verdict: ⭐⭐ READ-AND-BORROW, with one genuinely low-cost RUN available.**
A fenced clone-and-read is safe (Apache-2.0, no `pull_request_target`, pinned actions, no committed secrets). The book is free, complete and in English. What it costs is disk (2.0 GB) and, if you run anything, API credit.

---

## Rung 0 — Read (60 min, zero risk, zero cost)

1. **`book/introduction.md`** — the whole framework in 107 lines: *Agent = LLM + Context + Tools* → *brain + eyes + hands* → *Policy / Observation Space / Action Space*, plus the **实践在前，命名在后** thesis. English: `book-en/introduction.md`.
2. **`docs/EXPERIMENT_STATUS.md`** — read it as a *specimen of an evidence regime*, which is what you are actually here for. Note how many rows read *"Complete; hypothesis not observed."*
3. **`.github/workflows/provider-adoption-tests.yml`** — the best-commented CI file of this run. Every exclusion is named with its blocker; API keys are set **empty rather than unset** so a resolver bug fails loudly.
4. **`tests/test_docs_experiment_status_links.py`** — 34 lines. Read it beside the two broken links it cannot see. This is the cheapest possible lesson in gate scoping.

---

## ⭐ Rung 1 — THE VAULT ITEM (30 min, zero install)

This is the sixth consecutive ship pointing at the same unfinished job, and this subject supplies the sharpest exemplar yet.

**(a) Add clause (h) to `(C) proposed-verify-vault-inventory.sh`** — *a check must compare a claim to the tree, not a copy to a copy.*

The vault has exactly this disease. `CLAUDE.md`'s chapter index says `_state/03c-projects-v61-v183.md` holds "v61–v279"; the filename says `-v183`; the file holds v280. Three copies, no comparator. Clause (g) (from v278/v279) asks whether a published count is anchored to a command. **Clause (h) asks the next question: is the comparison pointed at the source, or at another copy of the claim?**

Cite in the script's own comments:
- **exemplar of the failure** — `scripts/check_i18n_consistency.py` check 5: computes the correct total (118), prints it, compares only locale-to-locale.
- **exemplar of the scoping failure** — `test_ledger_links_resolve_to_existing_files`: 7 of 53 links, because the regex demands a bullet ending in `.md`.
- **exemplar of the invisible-entry failure** — Hebrew, absent from `docs/`, therefore absent from `discover_locales()`, therefore never checked.

**(b) RUN the script.** It is now **25 ships overdue** (`main` is at v226; v227→v280 are outstanding). Running it is the entire point of having written it.

**(c) One concrete vault check, borrowed directly:** the vault's own index↔disk comparison — every `_state/*.md` on disk must appear in the `CLAUDE.md` chapter table, *and* every path cited in that table must exist. That is the Hebrew failure and the 7-3/7-4 failure in one predicate, and the vault has already hit clause 1 of it once (v255→v256, five unindexed files).

---

## ⭐ Rung 2 — The one experiment worth running (45 min, ~$0)

**`chapter1/context/` (experiment 1-1)** — a systematic ablation showing what each component of an agent's context contributes. It is the book's cleanest empirical claim and it maps directly onto the hireui candidate-LLM legibility ADR.

Why this one:
- `.env.example` ships an uncommented **free** default (`OPENROUTER_MODEL=google/gemma-4-31b-it:free`), and the chapter README explicitly recommends starting at `context/`.
- It is one of the 9 experiments actually covered by `provider-adoption-tests.yml`'s sibling suite, so its offline tests are known-green in CI.
- ⚠️ **The honest part is the reason to read it:** `chapter1/README.md` states that in the formal five-arm run, *"去掉 reasoning 必然退化" 没有在该次运行中复现* — the expected degradation **did not reproduce**. That disclosure, printed in the chapter's own front matter, is worth more than the result.

**Fence:** clone into a scratch dir, `uv sync --extra ch1` or a venv, free OpenRouter key only, no vault or hireui data anywhere near it.

**Cheap alternatives if you'd rather not spend a key:** `chapter1/web-search-agent/` has offline unit tests that run with keys blanked (`python -m pytest` with `MOONSHOT_API_KEY=""`), which is a zero-cost way to see the provider-fallback design work.

---

## Rung 3 — Borrow into hireui (60 min, design only)

1. **`agentbook/providers/` (793 lines, 7 files)** — a small, clean multi-provider registry that chapters 1–5 route through instead of each carrying its own fallback logic. This is the **vendor-seam blueprint** the ADR wants, at a readable size. Compare with the v210 AIRI `xsAI` seam already recorded; this one is smaller and Python.
2. **The evidence-status vocabulary** — `Complete / Incomplete / Reader exercise`, plus the rule *"a smoke test does not establish completion."* Lift this verbatim into `hireui/evals/METHOD.md`. It composes with v249's *"only ever removes"* and v244's fail-closed gate.
3. **The refusal-to-pool rule** — *"this same-family configuration must not be silently pooled with upstream default-Gemini results."* That single sentence is the discipline hireui's Match-Explain evals will need the first time a model is swapped mid-campaign.
4. **Chapter 7 entire** — the evaluation methodology chapter is the most directly applicable content in the book to the hireui LLM work: evaluation environments, dataset design, LLM-as-a-Judge, evaluation-driven model selection.

---

## 🔴 NEVERs

- **Never cite an experiment count from this repo's README** — 108 and 103 are both published, 109 is on disk, **118** is what CI derives. State the basis.
- **Never treat a `Complete` status as proof the evidence is committed** — 7-3 and 7-4 are `Complete` and their evidence was never committable.
- **Never assume a translation matches the Chinese in content** because it matches in structure — that is precisely the failure this repo fixed at PR #999, and nothing prevents it recurring.
- **Never run the GPU-training, robotics-actuation or live computer-use tracks** as a casual pilot (chapters 8, 6, 9 — RTX PRO 6000-class hardware, physical actuation, real credentials).
- **Never wire any of this at candidate or production data.** It is a teaching repository full of live-API experiments.
- **Never quote the star count or Trending badge from this analysis** — no network access; those are unverified.
- **Never reuse `git show "$rev:path"` in zsh** — brace it (`"${rev}:path"`) or you will silently read the wrong file, as I did.
