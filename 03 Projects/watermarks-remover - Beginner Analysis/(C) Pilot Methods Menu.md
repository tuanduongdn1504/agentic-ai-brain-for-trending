# (C) watermarks-remover — Pilot Methods Menu (REBUILT)

> Rebuilt 2026-08-20. **Verdict: READ-AND-BORROW. Do not install.**
> The block is *purpose*, not security — recruitment is the context the subject's own `ethics.md:14-16` places out of bounds.

---

## Rung 0 — 15 minutes, zero risk, zero install

Read three files in the browser. Nothing else in this repository is as portable as these.

1. `skills/remove-ai-marks/references/removal-matrix.md` — the **"Verifiable today?"** column.
2. `service/scripts/detect_gumbel.py`, lines 21-25 — the "Honesty caveat" block.
3. `README.md:798-800` — the section that argues against the product, and then argues fairly for it.

**The question Rung 0 answers:** what does a capability table look like when it is allowed to say *no* about the feature everyone came for?

---

## Rung 1 — 2 hours, zero install. **This is the rung that pays.**

### ⭐⭐⭐ 1. A "Verifiable today?" column in hireui's feature matrix

Their matrix has five columns and the fifth is the honest one. Every hireui feature that touches an LLM gets the same column, answered before the feature ships:

| Feature | Method | Verifiable today? |
|---|---|---|
| Match-Explain | Claude, structured rubric | *(answer honestly)* |
| CV parse | vision → confidence-scored JSON | *(answer honestly)* |

**Why this matters more than it looks:** the RATIFIED candidate-LLM legibility ADR requires eval gating, and that clause **still has no implementation**. A column that forces "how would we know this worked?" to be answered in writing, per feature, is the smallest artifact that discharges it. If the honest answer for a feature is "No", that is not a blocker — it is the disclosure that has to ship next to the feature.

### ⭐⭐⭐ 2. Put the caveat in the API response, not the docs

`rewrite_text.py:509-510` compiles the hedge into a `note` field that travels with the result:

> "Layer B is best-effort against statistical token-sampling watermarks; cannot certify removal against a vendor detector."

Documentation is read once, by the person who integrates. A response field is read every time, by every consumer, including the next service down the chain. For Match-Explain, the confidence caveat belongs in the **response body**, not the README — and it composes with the v217 wardrobe CV-parse template already recorded.

### ⭐⭐ 3. A byte-equality assertion with the incident in the comment

`tests/test_lightweight_skill.py` (`:79-85` at the original pin, `:129-135` today):

```python
def test_vendored_text_unicode_is_identical_to_service_engine():
    # The Layer A engine is vendored byte-for-byte; only the CLI wrappers
    # (clean_text.py, inspect_text.py, common.py) may differ. Any engine
    # change must be applied to both copies in the same commit.
    assert service == vendored
```

The comment records *why the test exists* — and the very next test in the file records the drift that already happened. Fold this into the still-unwritten `bin/verify-vault-inventory.sh` as a fourth clause.

### ⭐⭐ 4. **New this rebuild — make the inventory check bidirectional, and prove it**

This ship produced a controlled measurement of the vault's own failure mode. Across the original v251 write-up: **sixteen quotation-and-line-number checks, sixteen passes. Four count-and-inventory claims, four failures.**

The lesson is not "be more careful." It is structural: **reading a file and quoting it is reliable; enumerating a directory and generalising from one member is not.** Both v250 and v251 flagged the filename-inventory trap; v251 then fell into it in its own headline.

So `bin/verify-vault-inventory.sh` — still unwritten after two ships recommended it — should carry, in `node`/`awk` (**never `python3`; it is SIGKILLed in this sandbox**):

1. `_state/` files on disk ↔ chapter index in `CLAUDE.md`, **both directions**
2. memory files on disk ↔ `MEMORY.md` index, **both directions**
3. the chapter **filename label** vs the newest entry it contains — the clause that would finally detect the `-v183` drift, now wrong for sixty-eight versions
4. byte-equality for any content the vault stores twice

**And a fifth clause this ship earned:** for every hardcoded count in `CLAUDE.md`, the command that regenerates it, so a stale number is a failing check rather than a sentence nobody re-reads.

---

## Rung 2 — NOT RECOMMENDED

Installing the service would mean running a provenance-stripping tool on a machine that also holds candidate data, under an ADR that requires every candidate-facing LLM path to be legible and audited. The tool is well built. The context is wrong. **Skip this rung.**

If a legitimate need ever arises for the operator's **own** content — stripping invisible Unicode from published documentation, for instance — the Layer A path is the deterministic, testable, low-risk part, and `skills/clean-user-facing-text/` runs it locally with no service at all. Fence it to a scratch directory, pin the commit, and never point it at anything a candidate sent you.

---

## 🔴 Never

- Point it at candidate CVs, cover letters, or portfolios.
- Present AI-assisted output as human-written in a hiring context.
- Cite its removal as verified. Its own matrix answers **"No"** for both headline features, and the repository publishes **zero** benchmark results.
- Repeat the `DETECT_TEXT_WATERMARK` claim at `vendor-notes.md:35` — the cited forum thread does not support it.
- Cite the star or fork figures as verified. They are page-stated; the GitHub API is mocked in this environment. **No viral-velocity claim.**
- **Build a candidate-facing AI-authorship detector on `score_stylometry.py`.** The forensic-readiness study (arXiv:2607.16010, verified at source) measures baseline false-negative rates of **70% / 83% / 80%** for KGW / Unigram / SynthID **before any attack at all**. An absent mark is not evidence of human authorship — that is the converse of the subject's own `ethics.md:18` — and stylometric detection is a documented source of false accusations against non-native English writers. On a hiring decision that error is not recoverable.
