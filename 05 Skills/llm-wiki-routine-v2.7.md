# LLM Wiki Routine — v2.7 delta (2026-07-16)

**Status:** CURRENT (delta extending v2.6). Codifies the two operator-signed-off amendments from the **v203 audit** (2026-07-16, `04 Reviews/(C) 2026-07-16 — v203 audit (v183–v202)`), resolving **standing recommendations (i) + (ii)** that had been held de-facto since v159 but never formally signed off. No other change: the Phase-0.9 STRICT criteria and the §31 2-tier INCLUDE / §35 off-goal-ceiling mechanics are otherwise unchanged — v2.7 only clarifies them.

Prior deltas: v2.3 base → v2.3.1 (§25–§26) → v2.4 (§27–§30) → v2.5 (§31–§34) → v2.6 (§35–§36, §39) → **v2.7 (§40–§41)**.

---

## §40 — Operator-Direction GOAL-ALIGNED default for goal-adjacent subjects (resolves standing rec (i))

**Sign-off:** operator elected "Formalize operator-direction GA" (v203 audit, 2026-07-16).

**Rule.** An **operator-requested** subject that **touches a live goal thread** — the agent substrate (agent skills / MCP / orchestration / memory / capability layers), Claude/Anthropic tooling, autonomous-agents-for-software (Goal #1), the hireui/TalentAxis product (Goal #2), or any live pilot thread — is classified **GOAL-ALIGNED per operator direction** whenever **(b) is MODERATE or better** ((a) may FAIL). In that case:

- **No override is consumed** (it does not count toward the 2-in-20 / 3-in-30 override-frequency triggers), and
- it does **not** stress the §35 off-goal-rate ceiling (goal-adjacent ≠ off-goal), and
- the **OFF-GOAL reading is recorded as the reviewable alternative** in the verdict (honesty preserved — the operator or a later audit can flip it).

**Boundary.** A subject with **no goal thread at all** — no connection to the agent substrate, Claude, software-agent goals, hireui, or a pilot — remains **OFF-GOAL CAPTURE** (the v2.5 §31 corpus-knowledge-outlier track) and/or an explicit `[ceiling-override]` if force-included. §40 does **not** open the door to arbitrary off-goal intake; it only stops classifying *goal-adjacent* subjects as off-goal.

**Effect / why.** This codifies the working status quo (0 operator overrides v153→v202; §35 clear under the GA reading) and ends the recurring audit flag "is this an override / does this stress §35?" for goal-adjacent subjects. **Precedents now covered by §40** (previously each labeled "GOAL-ALIGNED per operator direction, OFF-GOAL defensible"): GLM-5 v176 (frontier LLM), DeepSpec v186 (spec-decoding framework), AI-For-Beginners v191 (curriculum), TimesFM v193 (forecasting FM), meetily v196 (meeting app), mlsysbook v197 (textbook). Under §40 these are simply GOAL-ALIGNED (goal-adjacent, operator-requested, (b) MODERATE+), with the OFF-GOAL alternative on record.

**Streak notation.** The forward-only `GA:` count (v2.5 §32) continues to count these as GA. The standing "alt OFF-GOAL reading" annotations (`GA:xx · OG:yy`) may be **retired going forward** — under §40 they are GA, not a dual-reading — but historical alt-reading notes are left frozen, not recomputed (the §32 forward-only discipline).

## §41 — (a)-criterion requires a SOLID signal; no inference-rescue (resolves standing rec (ii))

**Sign-off:** operator elected "Yes — require a solid signal" (v203 audit, 2026-07-16).

**Rule.** Criterion **(a)** ("is the author Anthropic / a cultural peer of the operator?") **PASSES only on a solid signal**:
1. a **declared / verifiable Anthropic affiliation** (the author is Anthropic, or an Anthropic employee acting as such), **or**
2. a **registered (a)-7 Foundational-Vendor-Direct-Source** (the existing vendor-direct axis).

A **name / heritage / locale / notability inference is NOT an (a)-rescue.** Specifically: a name that suggests an ethnicity or nationality, a non-English or operator-locale README, a "famous framework/domain author," or a "notable individual" is **insufficient** for an (a) PASS. Such subjects **FAIL (a)** and are keyed on (b) per §31 (they still routinely ship GOAL-ALIGNED via (b)).

**Effect / why.** Closes the off-goal (a)-rescue door — the mechanism by which a subject could be admitted on a weak author-identity inference. This formalizes de-facto practice across **v159→v202** (~40+ ships all cleanly (a)-FAILed on this basis with no problems: e.g. NVIDIA v169 corporate-not-Anthropic, the v171/v174/v181 disclosed-indie builders, the v183/v184/v185/v189/v202 notable individuals, the v78-style product-locale case). (a) remains one of the four criteria; §41 only tightens what counts as a PASS. **Note:** the v78 "PASS via product-locale-inclusion" precedent is **superseded** by §41 (locale is no longer an (a)-rescue); v78's ship stands as recorded, but the criterion-(a) reasoning is not repeated.

**Disclosed-individual (a)-axis:** the repeatedly-flagged question of whether "notable/disclosed individual builder" should be a registered (a) cultural-peer axis is **answered NO by §41** — it is not a solid signal and registering it would reopen the rescue door. This retires the "disclosed-indie-builder (a)-axis, operator-reviewable, N=k" watch item.

---

## Net

- **§40** — operator-requested goal-adjacent subjects default GOAL-ALIGNED per direction on (b) MODERATE+; no override, no §35 pressure; OFF-GOAL recorded as the reviewable alternative. Truly off-everything subjects still use OFF-GOAL CAPTURE / override.
- **§41** — (a) PASSES only on a declared Anthropic affiliation or a registered (a)-7 vendor-direct source; no name/heritage/locale/notability inference; the disclosed-individual (a)-axis is answered NO.
- Standing recs (i) + (ii) → **RESOLVED / ADOPTED.** Rec (iii) (shim-rebuild) was executed at v167. No standing recs remain open.
- Counts / patterns unchanged; this is a routine-governance codification, not a corpus mint.

*Skill file — the v2.7 delta. Base routine = v2.3 (`_state/01-skill-references.md` + `05 Skills/llm-wiki-routine-v2.3.md`); deltas v2.3.1/v2.4/v2.5/v2.6 in their dated files. Prefix `(C)`-equivalent: Claude-authored under operator sign-off.*
