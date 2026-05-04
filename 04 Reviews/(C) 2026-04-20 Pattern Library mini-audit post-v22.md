# (C) Pattern Library mini-audit — post-v22 (2026-04-20)

> **Trigger:** Proactive mini-audit before v23 (candidate count 19, approaching 15+ threshold recurrence)
> **Scope:** Fresh candidates (#41-44) + overlap analysis + watch-list prioritization + aging-candidate re-evaluation
> **Last full audit:** 2026-04-19 post-v21
> **Outcome:** 0 promotions, 0 retirements, 1 scope clarification (#35↔#41 distinction), 3 aging candidates flagged for v25 re-evaluation, validation watch-list published for v23+

---

## 1. Mini-audit scope (lighter than full audit)

### What this mini-audit covers

1. Fresh candidate (#41-44) quality review — formal statement clarity + overlap check
2. Overlap analysis — do any new candidates redundantly cover confirmed patterns?
3. Watch-list — which candidates should v23+ Phase 0 actively probe for?
4. Aging candidates — any approaching 5-wiki STALE-CANDIDATE threshold?

### What this mini-audit does NOT cover

- Full formal criteria re-application (done at v21 full audit)
- Retirement decisions (defer to next full audit)
- Refinement of confirmed patterns (no evidence warranting)
- Pattern #20 revision discussion (reformulated at v21, stable)

### Rationale for proactive

Post-v21 full audit reset triggers. Post-v22 added 4 candidates (#41-44). Candidate count at 19 — hitting v15+ trigger threshold with 1 more wiki. Mini-audit now prevents another multi-trigger hit at v23.

---

## 2. Fresh candidate (#41-44) quality review

### #41 Training-Infrastructure Framework

**Current status:** N=1 (LlamaFactory v22).

**Formal statement review:**
> Training-infrastructure frameworks produce fine-tuned models rather than being models or agent-orchestrators. 4th outside-scope sub-type.

**Quality:** Clear. Structurally distinct from agent-framework / foundation-model / content-archive / education-aggregator.

**Action:** No changes. Retain as-is.

### #42 Academic-Published Peer-Reviewed Framework

**Current status:** N=1 (LlamaFactory ACL 2024).

**Formal statement review:**
> Peer-reviewed publication at academic venue distinct from arXiv-only preprint.

**Quality:** Clear. Binary distinction (peer-reviewed vs preprint) with observable venue metadata.

**Overlap check:**
- vs Pattern #8 (Empirical Research Emergence, confirmed) — #8 is about research-benchmark emergence generally; #42 is specifically about peer-review tier. Different axes. **Keep distinct.**
- vs #32 (Research-Paper-Chain, promoted v22) — #32 is about lineage citation networks; #42 is about publication venue. Different. **Keep distinct.**

**Action:** No changes.

### #43 Optimizer-Research Integration Velocity

**Current status:** N=1 (LlamaFactory — 5 novel 2024 optimizers + 5 RL methods).

**Formal statement review:**
> Framework integrates cutting-edge research within 1-6 months of publication as competitive edge.

**Quality:** Clear but metric-fuzzy. "1-6 months" arbitrary. Observable via commit history or version releases cross-referenced with research papers.

**Sharpening consideration:** Could tighten to "integrates methods from papers published within 12 months of framework release at rate >3 per release cycle." But N=1 makes sharpening speculative.

**Action:** Defer sharpening to N=2. If Unsloth or Axolotl validates, refine then.

### #44 Academic-Lab Affiliation Archetype

**Current status:** N=1 (hiyouga + Lab4AI).

**Formal statement review:**
> 9th organizational archetype: author has university/research-lab affiliation providing research backing + paper co-authors + academic venue pathway + institutional continuity.

**Quality:** Clear. Well-differentiated from 8 prior archetypes.

**Overlap check:**
- vs #42 Academic-Published — #42 is publication-venue axis; #44 is organizational-backing axis. Co-occurrent but orthogonal (can have paper without lab; can have lab without paper). **Keep distinct.**

**Action:** No changes.

---

## 3. Overlap analysis across candidate library

### Light overlap flagged for monitoring

**#33 Non-OSI Custom License vs Pattern #29 (confirmed) License-Category Diversity**

- Pattern #29 (confirmed) covers both copyleft (GPL) + custom non-OSI as 2 non-permissive paths
- Pattern #33 is narrower sub-hypothesis specific to foundation-model space (fish-speech example)

**Decision:** Keep #33 as narrower sub-pattern. If validates at N≥2, may reveal foundation-model-specific license pattern distinct from general #29.

**Alternative if stale at v25:** Absorb #33 into #29 as sub-case; retire.

---

**#39 Controversial-License-Use vs Pattern #29**

- Pattern #29 addresses license diversity (which license chosen)
- Pattern #39 addresses license validity (applying to content you may not own)

**Orthogonal.** Keep both. Unambiguous distinction.

---

**#35 Foundation-Model-as-Product vs #41 Training-Infrastructure**

- #35 (fish-speech v20 evidence) — foundation-model IS the product
- #41 (LlamaFactory v22 evidence) — framework produces fine-tuned models

Both are outside-scope sub-types. #35 = foundation-model-space sub-type; #41 = training-infra sub-type. **Different sub-types.** Keep distinct.

**Scope clarification:** A v23+ wiki involving a foundation model that ALSO ships fine-tuning infrastructure (e.g., Llama-3 with training code) would test both patterns.

---

**#42 Academic-Published vs #32 (confirmed) Research-Paper-Chain**

- #32 (confirmed v22) — framework cites extensive prior-research network
- #42 (candidate) — framework publishes to peer-reviewed venue

**Co-occurrent but distinct.** LlamaFactory exemplifies both; fish-speech exemplifies #32 but not #42 (arXiv-only, not peer-reviewed).

**Keep both.** Productive overlap — predicts different corpus phenomena.

### Conclusion of overlap analysis

**No merges warranted at v22.** All light overlaps are productive (different predictive axes). Revisit at v25 if aging patterns show redundancy.

---

## 4. Validation watch-list for v23+

### HIGH likelihood validation (probe aggressively in v23+ Phase 0)

| Candidate | Reason | v23 candidates |
|-----------|--------|----------------|
| #41 Training-Infrastructure | 4 major competitors exist | Unsloth, Axolotl, TRL-standalone, Megatron-LM |
| #42 Academic-Published | NLP frameworks often have conference papers | Most research-lab-affiliated frameworks |
| #43 Optimizer-Research Velocity | Similar-velocity frameworks observable | Unsloth (high-velocity), Axolotl |
| #44 Academic-Lab Affiliation | Common pattern in research-heavy frameworks | Most fine-tuning + foundation-model frameworks |

**Priority v23 probe:** `unslothai/unsloth` would validate **#41 + #43 + #42 (if published)** simultaneously — highest validation density per wiki.

### MEDIUM likelihood (watch passively)

| Candidate | Reason |
|-----------|--------|
| #28 LiteLLM multi-provider abstraction | Common outside corpus; needs corpus-target framework |
| #30 3-Layer Ecosystem Stratification | Needs framework with MCP + LiteLLM + runtime-ID mix |
| #31 Open-Core Commercial | Mistral/Stable Diffusion/Black Forest candidates |
| #33 Non-OSI Custom License | Meta Llama-3, Mistral-non-commercial comparable |
| #34 Anti-Distillation Clause | Foundation-model licenses trending this direction |
| #38 Prompt-Leak-Archive Genre | May remain rare (legal barriers) |

### LOW likelihood / stale risk (approaching 5-wiki threshold)

| Candidate | Last data point | Wikis since | STALE threshold |
|-----------|------------------|-------------|-----------------|
| #14 Alignment-Theory Visibility | paperclip v14 | 8 | Already STALE |
| #16 Skill Dependency Locking | multica v15 | 7 | Already STALE |
| **#21 SDD Methodology Emergence** | **spec-kit v17** | **5** | **At threshold — flag for v24-v25 re-eval** |
| **#23 AI-Disclosure Policy** | **spec-kit v17** | **5** | **At threshold — flag for v24-v25 re-eval** |
| **#25 Personality-Driven Agent Design** | **agency-agents v18** | **4** | **Approaching — flag for v25 re-eval** |
| #26 Shell-first T1 | agency-agents v18 | 4 | Approaching (stable N=2 same-tier) |
| #36 Pseudonymous Researcher | system-prompts-leaks v21 | 1 | Fresh |
| #37 Crypto-Donation-Funded | system-prompts-leaks v21 | 1 | Fresh |
| #39 Controversial-License-Use | system-prompts-leaks v21 | 1 | Fresh |
| #40 Derivative-Security-Service | system-prompts-leaks v21 | 1 | Fresh |

---

## 5. Aging-candidate decisions

### #21 SDD Methodology Emergence — flag for v24 re-evaluation

- Current: N=2, both T1 (GSD v5 + spec-kit v17)
- Wikis since last data point: 5 (approaching 5-wiki STALE threshold)
- **v22 action:** NOT flagged stale yet (still 2 data points; single-tier prevents promotion criterion ≥2 tiers)
- **v24 re-evaluation trigger:** if no 3rd SDD-methodology framework appears by v24, consider STALE status or re-formulation

### #23 AI-Disclosure Policy Emergence — flag for v24 re-evaluation

- Current: N=1 (spec-kit v17)
- Wikis since: 5
- **v22 action:** approaching STALE
- **v24 re-evaluation trigger:** if no corporate-backed framework adds AI-disclosure policy by v24, promote to STALE-CANDIDATE

### #25 Personality-Driven Agent Design — flag for v25 re-evaluation

- Current: N=1 (agency-agents v18)
- Wikis since: 4
- **v22 action:** not yet STALE
- **v25 re-evaluation trigger:** if no 2nd framework with first-class personality design by v25, STALE consideration

### Other aging candidates (no action needed)

- #26 Shell-first T1: N=2 same-tier stable; unlikely to validate beyond T1; keep as niche-confirmed-hypothesis
- #28/#30/#31/#33/#34: N=1 fresh (1-2 wikis), too early

---

## 6. No promotions, no retirements at v22 mini-audit

**Rationale:** All new candidates (#41-44) are N=1 — need 2nd data point before promotion. No existing candidates hit promotion criteria at v22. No candidates clear retirement threshold (no explicit invalidation evidence).

**Promotion pipeline for v23:**
- If Unsloth or Axolotl validates: **#41 + possibly #43** promote to confirmed
- If academic-venue second framework: **#42 + possibly #44** promote

---

## 7. Audit trigger status post-mini-audit

### Reset triggers via mini-audit

This mini-audit serves as formal audit touchpoint, resetting trigger counter:
- Candidate count: 19 (still approaching 15+ but reviewed + watch-listed)
- Wikis since formal audit: 1 (v22, now mini-audited)
- Ratio: 0.83:1 (healthy)

**Triggers RESET.** Next trigger:
- Candidate count: > 15 AFTER adding more candidates (effectively >20)
- Wikis since: > 5 (at v28 if no new mini-audit)
- Ratio: > 1:1

### When next audit warranted

- **Proactive mini-audit:** if v23-v24 add >3 candidates or promote >2 → mini-audit
- **Full audit:** if ratio >1:1 OR candidate count >22 OR after 5 more wikis (v27)

---

## 8. Library state post-mini-audit

### Counts unchanged

| Status | Count |
|--------|-------|
| Confirmed | 23 |
| Refined (subset) | 6 |
| Active Candidate | 19 |
| Stale-candidate | 2 |
| Retired | 0 |
| **Total** | **44** |

**Ratio:** 19 : 23 = 0.83:1 (unchanged, healthy).

### Watch-list metadata added

- 4 HIGH-likelihood candidates flagged for v23 aggressive probing
- 6 MEDIUM-likelihood candidates flagged for passive watch
- 3 aging candidates flagged (#21, #23, #25) for v24-v25 re-evaluation

---

## 9. v23 recommendation from mini-audit

### Optimal v23 framework for validation density

**`unslothai/unsloth`** would potentially validate:
- #41 Training-Infrastructure (N=2 → PROMOTE)
- #42 Academic-Published (N=2 if peer-reviewed → PROMOTE)
- #43 Optimizer-Research Velocity (N=2 → PROMOTE)
- #44 Academic-Lab Affiliation (N=2 if lab-affiliated → PROMOTE)

**4 potential promotions from single wiki.** Highest pattern-validation density per operator-time.

Alternative: `axolotl-ai-cloud/axolotl` — similar space, YAML-config approach, likely validates #41 + #43.

### Non-v23 priorities

- T3 second entrant (only remaining single-entrant tier — closes 5/5 corpus)
- Pattern #18 CN test (3rd CN-origin agent framework)
- v2.1 routine consolidation (9 cumulative refinement items)

---

## 10. Key mini-audit insights

1. **Outside-scope wikis continue to dominate pattern discovery** — v20 + v21 + v22 = 14 candidates (fish-speech 5 + system-prompts-leaks 5 + LlamaFactory 4). Predictable pattern: outside-scope genres have rich novel structure.

2. **Fresh candidates cluster in training-research space** — #41-44 all related to research-first frameworks. Ecosystem specialization emerging as corpus dimension.

3. **Aging candidates form pattern:** agent-framework-space candidates (T1/T2 patterns #21/#23/#25/#26) age without validation. Corpus may be sampling-saturated on agent-framework structural patterns.

4. **Validation-density as v23 selection criterion:** Unsloth candidate would validate 4 patterns simultaneously vs T3-entrant would primarily fill tier without pattern validation.

5. **Stale-threshold mechanism working:** #14 + #16 flagged at v21 audit held up (still stale at v22). 3 more approaching threshold for v24-v25.

---

## 11. References

- v21 full audit: `(C) 2026-04-19 Pattern Library audit post-v21.md`
- v22 iteration log: `03 Projects/LlamaFactory - Beginner Analysis/04 Reviews/(C) 2026-04-19 v22 build learnings.md`
- Pattern Library: `PATTERN_LIBRARY.md` (vault root)

---

**v22 mini-audit complete. 0 promotions / 0 retirements / 0 major refinements. Watch-list published (HIGH/MEDIUM/LOW validation likelihood). 3 aging candidates flagged for v24-v25 re-evaluation (#21, #23, #25). Unsloth identified as v23 validation-density-optimal target. Triggers reset.**
