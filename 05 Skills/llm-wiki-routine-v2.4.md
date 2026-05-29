# Skill: LLM Wiki Routine v2.4 (delta)

**Status:** CURRENT (supersedes v2.3.1 as of 2026-05-29). v2.3 base remains authoritative at `05 Skills/llm-wiki-routine-v2.3.md`; v2.4 documents the delta only.
**Trigger:** dedicated Library-vocab consolidation session, executed 2026-05-29 immediately after the v115 mini-audit, which §12-committed it as non-deferrable (deferred at v101+v106+v110). This is the "#1 v2.4 codification debt" the last four audits flagged.
**Scope:** the Library-vocab PROVISIONAL layer ("~108 items") + the standing anti-re-accumulation discipline + one fact reconciliation (Pattern #57 57k implementer count).

---

## §27. Library-vocab consolidation — the "~108" was a phantom count

### Finding

Through v114 the Library-vocab PROVISIONAL layer was reported as "~108 items." The consolidation session established (via exhaustive read-only extraction of `_patterns/05-recent-additions.md` + `_patterns/03-active-candidates.md` + the v2.3 §1 list) that **~108 was a phantom count**: the running *sum of per-wiki "NEW candidate X" mentions*, the large majority never tracked again, many near-duplicate or one-off. **There was never a maintained list.** This non-maintenance — not the items' content — is why three prior audits could only defer it: there was nothing clean to consolidate, only narrative to reconstruct.

### Resolution — a maintained registry

A single authoritative registry now exists: **`_patterns/06-library-vocab-registry.md`**. It replaces the phantom count with:
- **8 CONFIRMED** items (#12, #14, #15, #16, #17, #18, #19, #20) — unchanged at consolidation.
- **7 themed clusters** (LV-C1 Vendor-Direct Skill-Authoring · LV-C2 Cost/Capacity-Economics-of-Free-Cheap-Inference · LV-C3 Doc-Coherence Anti-Drift-vs-Drift-Exhibited · LV-C4 Cadence/Velocity micro-signals · LV-C5 Design-Skill Composition Vocabulary · LV-C6 Session/Prompt-Persistence & Autonomy · LV-C7 Packaging/Runtime-Substrate one-offs) absorbing ~25 named live observations.
- **~4 live standalone candidates** (section C of the registry).
- **A forced-retired long-tail** (section D) collapsing the phantom count.

**Net tracked PROVISIONAL surface ≈ 11 entries** (7 clusters + 4 standalones), down from the reported "~108."

### Forced-retire rule applied

Per existing routine §2 ("15-wiki forced retire if still N=1-only"): every N=1 standalone first-registered at or before **v99** (15 wikis before v114) and never strengthened to N=2 was FORCED-RETIRED (the v79–v89 long-tail; non-exhaustive enumeration, because these were never discrete entries). Retired items are re-registerable if a genuine 2nd instance later appears. No content was lost that was ever actually tracked.

### Promotions this session

**None.** One PROMOTION-ELIGIBLE sub-claim identified — LV-C2 "Cost-Attribution-via-External-Service" N=2 (LiteLLM v89 + external-pricing-service v109) → N=3 watch. The 8 CONFIRMED set is unchanged. The value of this session was **structural** (registry + clustering + retire + rule), not new vocabulary — and saying so plainly is the honest outcome, not a disappointing one.

---

## §28. Standing anti-re-accumulation discipline (load-bearing)

To prevent the layer from silently re-ballooning:

1. **Single registry.** `_patterns/06-library-vocab-registry.md` is the ONLY tracked location for Library-vocab items. Wiki narratives may NOTE an observation but must FILE it into the registry (a cluster or a tracked standalone) — or omit it. No more loose narrative minting.
2. **Registration cap.** A wiki may register at most **2 genuinely-NEW standalone** Library-vocab candidates. Further observations join an existing cluster or are omitted. (Formalizes the v115 freeze.)
3. **Auto-retire.** Any standalone N=1 not strengthened within 15 wikis is auto-retired at the next audit, checked mechanically against the registry.
4. **Count discipline.** Always report the **tracked-registry count** (8 CONFIRMED + 7 clusters + N live standalones), NEVER the cumulative-mention sum. The "~108" figure is **deprecated**.
5. **Clustering-first.** When a new observation resembles an existing cluster's theme, file it into the cluster (strengthening it toward a promotable sub-claim) rather than minting a near-duplicate standalone.

---

## §29. Pattern #57 57k implementer-count reconciliation (v115-flagged)

The v115 audit flagged a discrepancy: the v113/v114 wiki docs labeled their agentskills.io implementers "#6/#7-candidate," but v110 referenced a "9th-implementer watch." Reconciled against the chain history in `_state/03c-projects-v61-v114.md`:

- **5-implementer** chain v76→v93→v98→v99→v100 = **CONFIRMED N=3 at v101 audit**.
- **6th / 7th / 8th** implementers added in the v102–v105 era (N=4 STRONGER → N=5 STRONGEST → N=6 post-promotion strengthening).
- **Arc paused** v107–v109 (no agentskills.io conformance declared).
- **v113 = 9th implementer** (resumes the arc; satisfies v110's "9th-implementer watch"); **v114 = 10th implementer.**

**CORRECTION:** the v113/v114 wiki-doc "#6/#7-candidate" labels were WRONG and are corrected to **9th / 10th implementer**. CONFIRMED status is unchanged (N=3 since v101; the chain is now a 10-implementer post-promotion-strengthening arc). This is a count-labeling correction in the wiki docs, not a fact about the subjects; v115 correctly *flagged* rather than asserted it, so the audit's integrity holds. Implementer-kinds at v113/v114 (education-curriculum, product-vendor-for-own-product) remain correct and novel.

---

## §30. State after v2.4 consolidation

| Field | Value |
|---|---|
| Confirmed Patterns | **46** (unchanged) |
| Active candidates | ~25 (unchanged) |
| Library-vocab CONFIRMED | **8** (unchanged) |
| Library-vocab PROVISIONAL | **"~108" phantom → ~11 tracked** (7 clusters + ~4 standalones) in `_patterns/06-library-vocab-registry.md` |
| Routine version | **v2.4 CURRENT** (supersedes v2.3.1) |
| Streak | "44+1*" UNCHANGED (consolidation ≠ wiki ship) |
| Audit clean streak | 10 (v115); consolidation is not a fact-verification audit |

**Version log:** v2.4 = v2.3.1 + §27 (Library-vocab consolidation / phantom-count finding / maintained registry) + §28 (anti-re-accumulation discipline) + §29 (57k 10-implementer reconciliation) + §30 (state). v2.3.1 §25–§26 + v2.3 §1–§24 remain authoritative. Registry: `_patterns/06-library-vocab-registry.md`.

---

## Storm Bear's blunt-and-direct note

The headline isn't a pile of promotions — it's that **the "~108-item debt" was mostly a measurement artifact.** For ~50 wikis the routine kept *summing* every "NEW Library-vocab candidate" a wiki coughed up without ever maintaining a list, so the number grew monotonically and looked like a mountain. The real content was 8 CONFIRMED items + a couple dozen genuine-but-loose observations + a long tail of one-offs that lapsed their retire-window ages ago. The fix that matters is the **maintained registry + the cap + the count-discipline rule** — without those, this exact debt regrows in 20 wikis. The one honest correction shaken loose along the way: the 57k chain is at **10 implementers**, not the "#6/#7" my own v113/v114 docs claimed. No new CONFIRMED vocabulary, and that's the correct, non-inflated result.
