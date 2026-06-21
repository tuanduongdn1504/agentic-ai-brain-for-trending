# (C) v178 SkillOpt — Verdict & Collision-Check Record

> Internal decision record for the v178 ship. The reader-facing wiki is `../(C) SkillOpt — LLM Wiki.md`.
> Built **inline** (Ultracode off) with hand verification — per `feedback_wiki_verify_independently_check_collisions`, the 3-lens+critic workflow confabulates corpus facts, so collision/identity claims were grep-verified before incorporation.

## Verdict (one line)
**GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG. Tier T2 Service. 1 NEW §C standalone (CORPUS-FIRST, N=1). Counts UNCHANGED 46/10.**

## Verification log

**1× WebFetch — repo page** (`github.com/microsoft/SkillOpt`): tagline, languages (Py 86.6 / HTML 12.2 / Shell 1.2), MIT, v0.1.0, 8.6k★/828 forks, target models (incl. Claude), harnesses (incl. Claude Code CLI), 52-cell benchmark claim.
**1× WebFetch — raw README** (`raw.githubusercontent.com/.../main/README.md`): training-loop mechanism (rollout→reflect→edit→validate), optimizer-vs-target split, textual learning-rate budget, rejected-edit buffer, epoch-wise meta-update, held-out validation gate, `best_skill.md` (300–2,000 tok), zero inference-time overhead, `pip install skillopt`, BibTeX (Yang et al., arXiv 2605.23904), related projects (gbrain / gbrain-evals / darwin-skill). README does **not** position against DSPy/TextGrad/GEPA.
**1× WebSearch — lineage/novelty:** confirmed Microsoft *Research* project; paper "SkillOpt: Executive Strategy for Self-Evolving Agent Skills"; Microsoft Research publication page + HuggingFace papers page (2605.23904); "released May 2026"; lifts +23.5/+24.8/+19.1.

**Collision grep over `_state/*.md` + `_patterns/*.md` + `03 Projects/`:**
- ❌ **"corpus-first Microsoft" — REFUTED.** `markitdown` v28 = `microsoft/markitdown` (T4 corporate-narrow-utility); `spec-kit` v17 = `github/spec-kit` (GitHub = Microsoft-owned, "corporate-official"). Microsoft is a **returning** author. Claim corrected → #19 19a data-point. (This is exactly the identity-claim class the memory note flags; caught pre-incorporation.)
- ✅ **"text-space skill optimizer is corpus-first" — CONFIRMED.** No prior §C standalone or pattern for prompt-optimization / DSPy / TextGrad / text-space / skill-optimization / validation-gated edits / trainable-skill. The only "optimizer" hits are **Pattern #43 Optimizer-Research Integration Velocity** (weight-space optimizers — GaLore/RL/quantization — in training-INFRA like LlamaFactory v22 / Unsloth) = **opposite space**, and **Odysseus v136** "self-evolving SKILL.md" (loosely-controlled self-revision) = the exact foil SkillOpt's motivation contrasts against.
- The earlier `skill-opt`/`skill-optimizer` grep hits were all gh-aw's internal `.skill-optimizer` directory in `03 Projects/gh-aw .../00 Source/` — **not** a SkillOpt subject.

## INCLUDE rubric (routine v2.6 §31 — 2-tier, keyed on (b))

- **(a) FAIL, clean, no axis.** Microsoft = declared-non-Anthropic-institution ((a)-7 Anthropic-only). No heritage rescue (v159→v177 discipline + rec (ii)). RETURNING author (markitdown v28 / spec-kit v17). #19 19a only.
- **(b) STRONG — keys the tier.** Optimizes **agent skills** = the exact `05 Skills/` SKILL.md artifact the vault produces; runs on Claude + Claude Code CLI; a methodology+tool directly pilotable into the vault's own skills. STRONG-not-STRONGEST: MS Research third-party, multi-model (GPT-5.5 headline; Claude one of 7), Goal #1 centers Claude. **A clear tier above GLM-5 v176's (b) MODERATE** (raw model). → GOAL-ALIGNED unambiguous.
- **(c) STRONG.** Real optimizer engine (validation gates / LR budget / rejected-edit buffer / meta-update / bounded edits), 6 benchmarks × 7 models × 3 harnesses, WebUI, PyPI, arXiv paper. Caveat: v0.1.0 / 1 release / ~3 weeks old.
- **(d) STRONG.** Agent-skills cluster (SkillSpector v169 / ponytail v168 / agent-skills-standard v76 / book-to-skill v137 / Odysseus v136 / nature-skills v119) + #84 84c + #43 contrast + LV #20.

## Pattern decision
**MINT 1 §C standalone (CORPUS-FIRST, N=1): "Text-Space Skill Optimizer."** Defining conjunction = (text-space, no weights) × (training loop w/ epochs/LR/batches) × (held-out validation gate accepting edits only on measured improvement) × (deployable zero-overhead `best_skill.md`). PROMOTION-ELIGIBLE at N=2. §28 ≤2-cap honored.

DISTINCT-from table → see wiki §6. NON-claims → wiki §8. SECONDARY (NOT minted): #19 19a · #84 84c (no N-bump) · LV #20 QUALIFIED-ADJACENT (N stays 4) · #18 adjacency · author/standardize/scan/**optimize** quadrant cross-ref.

## State deltas
- Counts UNCHANGED **46 / 10**; §C surface ≈34 → **≈35** (+1 standalone, N=1).
- max top-level pattern UNCHANGED **#85**.
- streak `GA:39 · OG:11 [7 ov]` → **`GA:40 · OG:11 [7 ov]`** (GA reading; OFF-GOAL-v176 reading → GA:39·OG:12). **§35 CLEAR** — window {v176 GA/OG, v177 GA, **v178 GA**} = 0 OG (GA reading) / ≤1 OG (OFF-GOAL-v176) → clear under both. **25 consecutive goal-aligned ships v153→v178** (GA reading).
- `inflation_check`: discipline HELD — 1 mint ≤2 cap, N=1 correct, max #85, counts 46/10 unchanged, no double-count.

## Ship mechanics
- Branch **`wiki/v178-skillopt`** off **`wiki/v177-kilocode`** (based at 8c2327c = v177, itself unmerged — branching off main would orphan the v168→v177 cumulative state). **NOT auto-merged** — operator reviews + merges (`feedback_branch_wiki_ships_not_main`).
- Chapter file `_state/03c-projects-v61-v177.md` → renamed `v61-v178.md` + v178 entry appended.
- Registry `_patterns/06-library-vocab-registry.md` — new §C standalone filed.
- Root `CLAUDE.md` shim — state head + Weekly Update head + chapter index + counts/streak updated.
