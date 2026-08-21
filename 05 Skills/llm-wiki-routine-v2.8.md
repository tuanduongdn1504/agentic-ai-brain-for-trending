# LLM Wiki Routine — v2.8 delta (2026-08-21)

**Status:** CURRENT (delta extending v2.7). Codifies the three amendments signed off at the **v259 audit** (2026-08-21, `04 Reviews/(C) 2026-08-21 — v259 audit (v213–v258)`). No change to the Phase-0.9 STRICT criteria, to §31's 2-tier INCLUDE, or to §35's off-goal ceiling — v2.8 adds a method section, consolidates the accumulated method rules, and fixes a governance defect in §C.

Prior deltas: v2.3 base → v2.3.1 (§25–§26) → v2.4 (§27–§30) → v2.5 (§31–§34) → v2.6 (§35–§36, §39) → v2.7 (§40–§41) → **v2.8 (§42–§44)**.

---

## §42 — The same-author control (method)

**Sign-off:** operator-directed at the v259 audit; the method contribution of ships v256–v258.

**When it applies.** The operator requests two or more consecutive subjects by the same author.

**Rule.** Treat the **comparison** as a first-class deliverable, not a by-product of the individual ships.

1. **Hold a habit table across the set**, and use it to separate two different things:
   - **Dispositions** — what replicates across every repository regardless of project, domain or age. These are properties of the developer.
   - **Attention** — what varies between repositories. These are properties of what the developer happened to be working on.
   A habit that replicates is a far stronger finding than anything either repository can support alone, and the distinction is the whole value of the control.
2. **Verify every row with commands in every clone.** Do not assume symmetry. **Both parent ships of this rule were corrected on exactly that error** — v257 asserted an ignore-rule mechanism by analogy with v256 and was wrong by twenty-six days; v258 assumed a tree-level check sufficed and missed a deleted application sitting in the pack.
3. **An outcome that replicates through *different mechanisms* is stronger than one that repeats identically.** v258's three routes to the same ignored-yet-tracked files is the exemplar: one simultaneous slip, one rule written after the violation, one rule actively deleted. Same outcome, three causes ⇒ a disposition.
4. **State the sample size and refuse to generalise past it.** N=2 supports "these habits recur"; N=3 supports a hypothesis with a legible mechanism. Neither supports a law. Say which you have.
5. **Do not mint a §C standalone for the comparison.** A method is not a capability class. Record it in the audit's method section (this section), and in the ship as a recorded observation.

**Why.** Three repositories by one hand, shipped consecutively, produced findings none of them could individually: a six-habit replication at N=3, a measurable correlation between written-down reasoning and build quality, and the *code moves forward, never backward* generalisation with its mechanism (copy-forward is a one-way ratchet; only a shared library makes a fix travel backwards). That last one applies to this vault.

---

## §43 — Consolidated method rules D31–D47

**Sign-off:** v259 audit. These accumulated across v245–v258 and were previously scattered through per-ship entries. They are now routine, not folklore.

| Rule | Statement |
|---|---|
| **D31** | A scope verdict is a claim about a **date**, not a property of a subject. OUTSIDE-SCOPE is the one verdict that closes the file, so it rots unobserved — re-check outside-scope anchors. |
| **D32** | When two documents must carry the same fact and mechanisation is impractical, **declare which copy wins, inside the copy that loses.** |
| **D34** | Test a committed gate's own predicate against the history it governs. **A committed CI rule is not an enforced one.** |
| **D39** | To establish a structural git fact, use the command whose semantics **are** the definition (`rev-list --max-parents=0`, `rev-list --count`) — never `log \| head` or `log \| wc`. |
| **D40** | A stale label is safe when **declared** and dangerous when merely **compensated** — and check the declaration's own number too. |
| **D41** | A pipeline's exit status is the **last** command's. Run what matters alone and read its own status. *(This sandbox: `python3`/`pip` exist at `/usr/local/bin/` and are SIGKILLed on invocation — silently, inside a pipe.)* |
| **D42** | **A negative from a truncated search is not a negative.** State the extent of the search that produced it. |
| **D43** | `.filter(Boolean)` every `pipeline()`/`parallel()` result before dereferencing an element. **A crashed workflow is not a lost workflow** — read `journal.jsonl` and recover before re-running. |
| **D44** | An artifact is safe when it **carries its own context**, and dangerous when its context lived somewhere else and has since gone. A deleted rationale is worse than a stale one: staleness is detectable, absence is not. |
| **D45** | **Read the tree, then the file the documentation names.** Documentation that misattributes a real feature produces a false negative in exactly the reader who checks it. |
| **D46** | **A clean tree is not a clean history.** Enumerate the pack (`rev-list --objects --all \| cat-file --batch-check`) before concluding a repository has no dead generations. |
| **D47** | **Anchor the basename in filename greps**, or the test confirms whatever it is looking for. |

**§43.1 — The standing self-diagnosis.** Three consecutive ships independently confirmed it: **the orchestrator is reliable when it reads a file and quotes it, and unreliable when it generalises from where it chose to look.** Therefore **every negative in a ship must state the extent of the search that produced it**, and every `path:line` citation must be one the orchestrator read in its own command output — not one a subagent reported.

**§43.2 — A ground-truth block handed to a fleet is an AMPLIFIER.** At v257 a single unchecked assertion propagated into sixteen agents and returned from the adversary as *"Established GT confirms…"*. **Every line of a fleet's ground-truth block must be the output of a command, never an inference from the previous ship.** Where a line is an inference, label it so.

**§43.3 — Fleet scope.** A wiki **documents** its subject; it does not repair it. Reject fleet output that proposes edits to the subject repository as blockers for shipping — the subject's author is not a party to the document. (Raised at v257 and again at v258.)

---

## §44 — §C bifurcation, and the end of the deferred retire pass

**Sign-off:** v259 audit.

**The defect.** §C was defined as *"live standalone candidates"* — a promotion queue — and §39 auto-retires an N=1 row past both floors (≥15 wikis **and** ≥30 days) without a second instance. In practice §C has been doing **two** jobs: holding genuine promotion candidates, and cataloguing one-off corpus-firsts with their evidence. §39's auto-retire is correct for the first and destructive for the second, so **four consecutive audits declined to apply it** — leaving the vault carrying a declared-but-unenforced rule of exactly the kind it documented in five subjects during the v213–v258 window.

**The amendment.** §C is split:

| Section | Contents | §39 auto-retire | Purpose |
|---|---|---|---|
| **§C-1** | live promotion candidates, **N ≥ 2** (12) | **applies** | a real queue — a second instance means the class may be recurring |
| **§C-2** | recorded corpus-firsts, **N = 1** (38) | **does not apply** | a collision-detection catalogue; retained for evidential value, explicitly **not** awaiting promotion |

**Rules.**

1. A new mint at N=1 is filed in **§C-2**. Nothing is retired for age.
2. When a §C-2 row gains a genuine second instance it is **promoted into §C-1**, and from that moment §39's floors apply to it.
3. **"§C live standalones" in a ship's counts means §C-1** — the real queue. §C-2 is reported separately as a catalogue size.
4. Every row in both sections carries a **stable `C##` marker** as its first field so the counts are derivable by `grep -c` and drift is machine-detectable. *(This closes the standing WARN in clause 7 of `bin/verify-vault-inventory.sh`, raised at v255 and carried by every ship since.)*
5. **§28 recalibration.** The anti-inflation argument must be made against **§C-1**, not against the catalogue. At the v259 audit that is **12 candidates, not 50** — a materially weaker inflation argument. ⚠️ **Ships must not lean on §28 alone to decline a mint.** The other grounds — domain-not-capability, technique-not-capability, form-factor-within-a-genre, not-world-first, machinery-does-not-ship — are unaffected and remain load-bearing. *(Reviewed at v259: no decline in the v213–v258 window rested on §28 alone.)*

**Why not simply retire the 23 eligible rows.** The prior deferrals were right on substance. Each row records a verified corpus-first with its evidence, and later ships have cited them as prior art — the v182 audit caught the #23 anchor error precisely because the catalogue existed. **Retiring them would destroy the mechanism that makes collision-detection possible.** The rule was wrong, not the practice.

---

## Net

- **§42** — the same-author control: when subjects share an author, the comparison is the deliverable; separate dispositions from attention; verify every row in every clone; state the sample size.
- **§43** — D31–D47 consolidated into the routine, plus the standing self-diagnosis (§43.1), the ground-truth-amplifier hazard (§43.2) and fleet scope (§43.3).
- **§44** — §C bifurcated into §C-1 (N≥2, a real queue, §39 applies) and §C-2 (N=1, a catalogue, §39 does not); `C##` row markers added; §28 recalibrated against §C-1 and explicitly demoted to a supporting ground.
- **Counts after v2.8 / the v259 audit:** 46 top-level patterns · **12** CONFIRMED Library-vocab (#24 promoted from the v192 §C standalone) · §C-1 **12** · §C-2 **38** · max pattern #85.
- Phase-0.9 STRICT criteria, §31, §35 and §40/§41 unchanged.

*Skill file — the v2.8 delta. Base routine = v2.3 (`_state/01-skill-references.md` + `05 Skills/llm-wiki-routine-v2.3.md`); deltas v2.3.1/v2.4/v2.5/v2.6/v2.7 in their dated files. Prefix `(C)`-equivalent: Claude-authored under operator sign-off.*
