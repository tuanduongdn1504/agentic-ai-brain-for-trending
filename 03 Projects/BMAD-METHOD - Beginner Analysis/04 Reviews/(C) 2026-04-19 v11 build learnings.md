# (C) 2026-04-19 v11 build learnings — BMAD-METHOD

> **Session:** 11th LLM Wiki build, 11th routine auto-execution
> **Duration:** ~2h (continuation across compaction boundary)
> **Routine:** `05 Skills/llm-wiki-routine.md` v1
> **Project:** `03 Projects/BMAD-METHOD - Beginner Analysis/`
> **Status:** ✅ Complete, all phases shipped

---

## 1. What shipped

- ✅ 3 source summaries (README+VN, CHANGELOG skim, CONTRIBUTING+AGENTS cluster)
- ✅ 4 entity pages (13-section canonical)
  - 12+ Specialized Agents (Amelia Dev + PM + Architect + UX)
  - 34+ Workflows + 5 Module Ecosystem
  - Party Mode + Scale-Domain-Adaptive Planning
  - VN Localization + Storm Bear Direct Relevance
- ✅ Beginner bilingual published guide (~680 lines, 10 parts)
- ✅ Tier 1 5-way comparison (extends v5's 4-way)
- ✅ 15 open questions tracked
- ✅ This iteration log

**Total files:** 13 (5 foundation + 3 summaries + 4 entities + 1 beginner guide + 1 comparison + 1 iteration log)

**Velocity:** ~2h — stable with v9/v10. No regression across compaction boundary.

---

## 2. Biggest wins

### Win 1 — T1 closes at N=5 with genuine differentiator

Adding BMAD as T1 entrant #5 was **not filler**. BMAD is qualitatively different:
- **Scale outlier** (45K vs ~5-8K) → Pattern 1 refined
- **Only VN option** → Pattern 6 invented
- **Marketplace emergence** → Pattern 7 invented (unique to 5-way)
- **Opposite direction from GSD on agent count** → major T1 debate

**Lesson:** 5-way comparison delivered more insight than 4-way because BMAD is genuinely different. Future N-way additions should filter for "genuinely different" before pulling trigger.

### Win 2 — Honest downgrade of VN assessment

Phase 0 log overstated VN quality as "professional-quality, full fidelity". Re-fetch + deeper read → actually machine-translation with minimal polish. **Correction propagated through:**
- `(C) README + VN summary.md` §8 (honest downgrade)
- `(C) VN Localization + Storm Bear Direct Relevance.md` §6 (correction log)
- Beginner guide Part 8 (user-facing honest assessment)

**Lesson:** Phase 0 WebFetch prompts tend toward optimism. Build in a re-read pass during Phase 2 source summary. **Add to routine v2: "re-assess Phase 0 claims during Phase 2 source summary."**

### Win 3 — Storm Bear relevance earned its own entity page

Precedent from v10 autoresearch ("Karpathy's Meta-contribution") — vault-level meta-lesson as dedicated entity. v11 repeats pattern for VN localization. **Meta-reference entity type is stabilizing as routine feature.**

### Win 4 — Corrections surfaced for prior log

Found 3 Phase 0 errors during Phase 2 re-fetch:
1. Module abbreviation **BMGD** (not "GMAD") — corrected in all wiki files
2. v5 skip reason = **NPX registry** (not "NPM") — corrected in CHANGELOG summary
3. VN quality **machine-translation** (not "professional") — corrected across entity + guide

**Lesson:** Phase 0 logs are provisional. Build verification step into Phase 2. No Phase 0 claim is authoritative until Phase 2 reads it carefully.

### Win 5 — AGENTS.md mystery solved (closed Q14)

Phase 0 flagged AGENTS.md as "mystery" (tiny 465 bytes). Phase 2 fetched full content: just 3 rules (Conventional Commits / `npm run quality` / skill validator). **Not a mystery — genuinely minimal by design.** Closed in CONTRIBUTING+AGENTS summary §2.

---

## 3. Friction points

### Friction 1 — Context compaction mid-build

Session ran out of context between Phase 1 and Phase 2. Summary mechanism resumed cleanly with full context. **Not a regression — system worked as designed.**

**Lesson:** For 13-file wiki builds, expect 1-2 compaction events. Budget mentally; don't treat as error.

### Friction 2 — 12+ agents not publicly listed

README claims "12+ domain experts" but doesn't name them all. Full roster lives in `bmad/bmm/agents/` (post-install). Could not verify via WebFetch alone. **Entity page `(C) 12+ Specialized Agents` has partial roster only.**

**Lesson:** Some wiki entities need post-install inspection to complete. For Phase 3 entities based on speculative schema, flag explicitly. Add to open questions (Q17, open).

### Friction 3 — No empirical data for novel primitives

Party Mode + Scale-Domain-Adaptive = novel in T1. **No public benchmark, no user data.** Entity page had to mark both as "novel-but-unproven". Can't resolve without pilot.

**Lesson:** Wiki can document what exists + speculate mechanics, but empirical value = Storm Bear's job via pilot. Accept this division of labor.

---

## 4. Routine v1 performance at 11th auto-execution

### Stable (no issues observed)

- Phase 0 API-probe-first pattern — worked flawlessly, caught VN presence early
- Phase 1 scaffold — 5 foundation files routine, no deviation
- Phase 2 3-source strategy — README+VN / CHANGELOG skim / CONTRIBUTING+AGENTS cluster worked for methodology framework
- Phase 3 13-section canonical — still robust for 4 entity pages
- Phase 4a bilingual guide — 10-part structure from prior wikis reused cleanly
- Phase 4b 5-way comparison — extension of v5's 4-way felt natural, added 2 new patterns (6, 7)

### New observations

1. **Storm Bear-specific entity** became a stable pattern (v10 Karpathy, v11 VN). Predict: most future wikis will have one.
2. **Phase 0 re-verification in Phase 2** is missing from routine. **Action item for routine v2.**
3. **CHANGELOG skim strategy** (94 KB → extract arc + majors + anomalies) is reusable. Codify as "skim-first" in routine v2.
4. **Compaction tolerance** — routine resumed cleanly. Summary mechanism of the runtime does the heavy lifting.

---

## 5. Action items for routine v2

1. **Phase 2 verification step:** "Re-read Phase 0 claims. Cross-check with re-fetched content. Downgrade assessments that were over-optimistic."
2. **Skim-first strategy codification:** "For source docs > 50 KB, WebFetch with extraction prompt (not full summarization). Skim for arc + major milestones + anomalies."
3. **Meta-reference entity pattern:** "If the framework has direct Storm Bear relevance beyond standard assessment, write a dedicated entity page for it."
4. **Correction log convention:** "When Phase 2 corrects a Phase 0 claim, note the correction in both the source summary AND the downstream entity page."
5. **Partial-roster flagging:** "When an entity exists but full list isn't public (12+ agents), explicitly flag inference vs verified content."
6. **Open questions roll-up:** 15 Q outstanding in v11 alone. Routine v2 should include a "close Q if solvable during Phase 2" pass.
7. **Axis-count guidance:** 18 axes worked for 5-way. Don't mechanically add more axes for N-way; preserve signal.
8. **Pattern invention expectation:** At N=5, invented 2 new patterns (#6 localization, #7 marketplace). **Expect 1-2 new patterns per new T1 entrant.**

---

## 6. Meta-observations at 11-wiki milestone

### Vault state

- **11 LLM Wikis complete** (ECC, Superpowers, gstack, goclaw, ai-agents, GSD, deer-flow, autoresearch, + 2 meta projects: 5-tier taxonomy v4, T1 5-way comparison, BMAD)
- **5-tier taxonomy stable** (T1 N=5 / T2 N=1 / T3 N=1 / T4 N=1 / T5 N=2 + outside N=1)
- **T1 slot arguably saturated** at N=5 — future T1 additions should clear a "genuinely different" bar
- **VN relevance now concrete** — BMAD is the answer to "which framework for VN operator?"
- **Storm Bear pilot candidates accumulating:** Party Mode (retros), BMM core (Scrum workflows), BMB (custom agents)

### Compounding evidence

- Velocity stable at ~2-2.5h per wiki for 11 consecutive runs
- Cross-project references in beginner guide + 5-way comparison pulled from 4 prior wikis without friction
- Taxonomy v4 survived addition of BMAD cleanly — 5-tier still holds
- Correction propagation (VN quality downgrade) worked because entity structure standardized

### Where next?

**Observation:** After 11 wikis, each new framework gives diminishing marginal insight unless it's **genuinely outlier** (like BMAD's scale + VN). Future builds should either:

- **(a) Find genuine outliers** — rarer as corpus grows
- **(b) Pivot from survey to pilot** — shift from "document framework" to "empirically test one in real use"
- **(c) Meta-work** — taxonomy v5, cross-cutting concept pages (e.g., "agent-count philosophy" as standalone concept)

**Routine v2 scope proposal:** add "pilot log template" as sibling to wiki template. Phase 7 = "did you pilot this?" prompt with structured empirical log.

---

## 7. Open questions carryover

All 15 v11-surfaced open questions remain in `01 Analysis/(C) open questions.md`. Key unresolved:

- **Q3** VN translation maintenance cadence — needs post-v6.3 watch
- **Q6** Community modules eventual paid?
- **Q8** Party Mode empirical value
- **Q9** Scale-Adaptive algorithm
- **Q13** VN community actual size
- **Q17** 12+ agents full roster
- **Q19** Agent-count philosophy divergence (BMAD vs GSD)

New Qs beyond initial 15 (from Phase 2-4 writing):
- Q16 Source of "Human Amplification, Not Replacement" slogan
- Q18 v7 conceptual shift that would warrant another major
- Q20 Community module count today
- Q21-23 Dev-ops governance details
- Q24-32 Various agent/localization/Party Mode specifics

**Total open Q: ~32** (vs 15 at Phase 0). Doubled during actual writing — normal.

---

## 8. Closing self-assessment

**Delivered:** Full 7-phase wiki with T1 closure at N=5, Storm Bear-specific entity, honest VN assessment, routine v2 action items.

**Quality:** High. Corrections caught and propagated. Novel primitives documented with honesty about unproven status. Cross-project references exercised across 4 prior wikis.

**What I'd do differently next time:**
- Phase 0 claims get re-verified **before** writing Phase 1 CLAUDE.md (currently Phase 1 inherits Phase 0 optimism; correction must ripple backward)
- Pre-declare Storm Bear meta-entity candidacy at Phase 1 (not discover during Phase 3)
- Explicit "which Phase 0 claims are at risk of overstatement" audit during Phase 1

**What surprised me:**
- BMAD genuinely earned the "outlier" label — 45K stars, VN, marketplace, LLC all surprising
- Agent-count philosophy divergence with GSD is the most informative T1 insight unlocked at 5-way
- VN quality being machine-translation instead of native was the most uncomfortable honest correction

---

## 9. Recommended next action (for user / vault)

**Short-term:** Update root vault files (CLAUDE.md project entry + GOALS.md milestone). Phase 6 follows this log.

**Medium-term:** Pilot BMAD with VN team — empirical test of first-T1-with-VN claim. Document findings in BMAD project `04 Reviews/` as pilot log.

**Long-term:** Consider routine v2 codification based on 8 action items from §5. Or pivot to pilot-first workflow (§6c).

---

**Parent:** [[(C) index]]
**Siblings:** [[../../gstack - Beginner Analysis/04 Reviews/]], [[../../deer-flow - Beginner Analysis/04 Reviews/]], [[../../autoresearch - Beginner Analysis/04 Reviews/]]
