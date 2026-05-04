# (C) Validation Analysis + Pattern 41 + 43 Promotions (v23 Phase 4b)

> **Type:** Phase 4b deliverable — primary focus of v23 wiki
> **Purpose:** Document Pattern Library state transitions driven by Unsloth v23 observations
> **Sources:** PATTERN_LIBRARY.md post-v22 mini-audit + Unsloth wiki entities
> **Status:** ✅ Phase 4b published

---

## 1. Summary

v23 Unsloth wiki was selected via v22 mini-audit specifically for **validation density** — potential to promote 4 v22 candidates (#41-44) in single execution. Post-execution results:

| Pattern | Pre-v23 | Post-v23 | Action |
|---------|---------|----------|--------|
| **#41 Training-Infrastructure Framework** | Candidate N=1 | N=2 structurally unambiguous | **→ PROMOTE CONFIRMED** |
| **#43 Optimizer-Research Velocity** | Candidate N=1 | N=2 | **→ PROMOTE CONFIRMED** |
| **#42 Academic-Published Peer-Reviewed** | Candidate N=1 | Stays N=1 | Scope-refine |
| **#44 Academic-Lab Affiliation** | Candidate N=1 | Stays N=1 | Scope-refine |

Plus evidence strengthening (#29, #32) + 2 new candidates (#45, #46).

**Net outcome:** 2 promotions + 2 scope refinements + 2 strengthenings + 2 new candidates = **high validation density**, confirming mini-audit's operator-time-ROI framing.

## 2. Pattern #41 Training-Infrastructure Framework → CONFIRMED

### State trajectory

| Version | Count | Evidence |
|---------|-------|----------|
| v22 (LlamaFactory) | N=1 | Academic-lab archetype, 100+ models, ACL 2024, Apache-2.0 |
| **v23 (Unsloth)** | **N=2** | **Duo-founder archetype, 500+ models, no publication, dual-license Apache+AGPL** |

### Structural criteria — met at N=2

Both frameworks share:
- Produce fine-tuned models (not models themselves)
- Unified training pipeline
- Multi-model support (100-500+ families/variants)
- Method breadth (LoRA / QLoRA / full / RL / FP8)
- Consumer-GPU optimization
- Research-paper-chain lineage
- CLI + WebUI + Docker deployment
- Active community + maintenance

**Distinct organizational archetypes** (academic-lab + duo-founder) confirm pattern is **structural sub-type**, not archetype-specific.

### Confirmed formal statement

> **Pattern #41 Training-Infrastructure Framework (CONFIRMED v23):** 4th outside-scope sub-type (after education-aggregator, foundation-model-as-product, prompt-leak-archive). Produces fine-tuned models rather than being models or agent-orchestrators. Characterized by: (a) unified training pipeline, (b) multi-model support (100-500+ model families/variants), (c) fine-tuning method breadth (LoRA/QLoRA/full/RL/FP8), (d) consumer-GPU optimization common, (e) research-paper-chain lineage common, (f) CLI + WebUI + Docker multi-surface deployment. Organizational archetypes vary (academic-lab + duo-founder observed at N=2). Ecosystem stratification: upstream performance providers (Unsloth) + downstream unified platforms (LlamaFactory).

### Sub-pattern candidate for future

Potential v24+ differentiation:
- **T-IF-A: Academic-platform** (LlamaFactory-style: publication + Lab4AI + unified breadth)
- **T-IF-B: Performance-provider** (Unsloth-style: no publication + duo-founder + consumer-GPU-first)

Register as candidate after N=3 observation to test differentiation.

## 3. Pattern #43 Optimizer-Research Integration Velocity → CONFIRMED

### State trajectory

| Version | Count | Evidence |
|---------|-------|----------|
| v22 (LlamaFactory) | N=1 | 5 novel 2024 optimizers (GaLore, BAdam, APOLLO, Muon) + 5 RL methods (PPO, DPO, KTO, ORPO, SimPO) |
| **v23 (Unsloth)** | **N=2** | **Custom Triton kernels (RoPE + MLP) + GRPO + padding-free packing + FP8 + MLX (coming)** |

### Structural criteria — met at N=2

Both demonstrate:
- Integration of cutting-edge research methods within months of publication
- Open-source competition on cutting-edge capability as differentiation
- Performance/capability as competitive positioning
- Active research-to-production pipeline

### Confirmed formal statement

> **Pattern #43 Optimizer-Research Integration Velocity (CONFIRMED v23):** Training-infrastructure frameworks integrate cutting-edge research methods (novel optimizers, RL alignment methods, quantization precision, platform support, custom kernels) within months of publication. Distinguishes training-infrastructure sub-type from slower-moving infrastructure layers. Observed at N=2 across academic-lab + duo-founder archetypes; mechanism is open-source competition on cutting-edge capability. Specific evidence catalog: 2024 optimizers (GaLore/BAdam/APOLLO/Muon), RL methods (GRPO/DPO/KTO/ORPO/SimPO), precision (FP8), platforms (MLX Apple Silicon), custom kernels (Triton RoPE/MLP/padding-free). Likely persists across training-infra sub-type; may not generalize to agent frameworks (different velocity regime).

### Cross-tier generalization check

Pattern #43 currently observed only in training-infrastructure sub-type. Does research-to-production velocity appear in T1-T5?

- **T1 (agent-as-assistant):** Methodology iteration (SDD / BMM / TDD) on months-years cycle, not research-paper-tracking
- **T2 (agent-as-service):** Platform iteration, not research-tracking
- **T4 (agent-as-bridge):** API-tracking, not research-tracking
- **T5 (agent-as-application):** Mixed (autoresearch tracks research, deer-flow tracks platform capabilities)

**Verdict:** Pattern #43 is training-infra-specific. Scope locked to sub-type.

## 4. Pattern #42 Academic-Published → STAYS CANDIDATE (scope-refined)

### Evidence

- LlamaFactory v22: ACL 2024 peer-reviewed ✓
- Unsloth v23: No academic publication ✗

### Scope refinement

Pattern does NOT universally apply to training-infrastructure frameworks. Stays candidate N=1. Reformulated:

> **Pattern #42 Academic-Published Peer-Reviewed (CANDIDATE N=1, scope-refined):** Subset of training-infrastructure frameworks (those with academic-lab affiliation) publish peer-reviewed research alongside framework release. Not universal — performance-first frameworks (duo-founder / commercial) may skip publication. Correlates with Pattern #44 (Academic-Lab Affiliation).

### Validation path

Requires 2nd academic-lab training-infra framework to test. Candidates to watch:
- Megatron-LM (NVIDIA — corporate, not academic-lab)
- DeepSpeed (Microsoft — corporate)
- FSDP (Meta PyTorch — corporate)
- Flax/Axlearn (Google — corporate)

**Most major training-infra frameworks are corporate, not academic-lab.** Pattern #42 may stay rare.

## 5. Pattern #44 Academic-Lab Affiliation → STAYS CANDIDATE (scope-refined)

### Evidence

- LlamaFactory v22: hiyouga + Lab4AI ✓
- Unsloth v23: Han brothers + team (company, not academic) ✗

### Scope refinement

> **Pattern #44 Academic-Lab Affiliation Archetype (CANDIDATE N=1, scope-refined):** Distinct organizational archetype for training-infrastructure frameworks affiliated with academic research labs. Contrasts with duo-founder / LLC / corporate archetypes. Correlates with Pattern #42 (peer-reviewed publication) and Pattern #32 (extensive research-paper-chain lineage).

### #42 + #44 correlation

Both patterns drawn from single observation (LlamaFactory). Both absent from Unsloth. **Strong hypothesis:** #42 + #44 correlate as sub-archetype "academic-lab-published-training-infra." Test requires 2nd academic-lab data point.

## 6. Pattern #29 License-Category Diversity — evidence strengthening

### Pre-v23 state

Confirmed v21 at N=3 non-permissive: 2 GPL-3.0 + 1 custom non-OSI

### Post-v23 state

**4 non-permissive licenses** (17% of 23 wikis):

| License | Count | Wikis |
|---------|-------|-------|
| GPL-3.0 | 2 | TrendRadar v19 + system-prompts-leaks v21 |
| **AGPL-3.0** | **1** | **Unsloth Studio v23** ← NEW |
| Custom non-OSI | 1 | fish-speech v20 |

### Observation

Non-permissive licensing spans 3 distinct categories now (GPL + AGPL + custom). License diversity is structural corpus feature.

## 7. Pattern #32 Research-Paper-Chain Lineage — N=3

### State trajectory

| # | Wiki | Evidence |
|---|------|----------|
| 1 | fish-speech v20 | TTS research papers + academic lineage |
| 2 | LlamaFactory v22 | Extensive (PEFT + TRL + QLoRA + FastChat + 100+ papers) |
| 3 | **Unsloth v23** | **llama.cpp + HF + PyTorch + Torch AO + NVIDIA NeMo DataDesigner** |

### Observation

- Unsloth's lineage list is **narrower** than LlamaFactory's — may reflect duo-founder vs academic-lab archetype difference
- All 3 data points within outside-scope sub-types (foundation-model + training-infra ×2)
- Pattern confirmed structurally; depth varies by archetype

## 8. New candidate #45 Dual-Licensing Strategy

### Registration

> **Pattern #45 Dual-Licensing Strategy (CANDIDATE N=1):** Some projects use different licenses for different components within single product family — typically permissive (Apache/MIT) for core library enabling commercial reuse, combined with copyleft (AGPL/GPL) for UI/SaaS layer protecting against cloud-vendor appropriation. Strategic license engineering as competitive positioning.

### Evidence

- Unsloth v23: Apache-2.0 (core) + AGPL-3.0 (Studio UI)

### Validation path

Watch for:
- Frameworks with UI + library split
- Projects facing cloud-vendor appropriation concerns
- Enterprise-leaning OSS with dual revenue model

Likely candidates: TimescaleDB, Elastic, Redis, various emerging frameworks.

## 9. New candidate #46 Duo-Founder + Team Archetype

### Registration

> **Pattern #46 Duo-Founder + Team Archetype (CANDIDATE N=1):** Organizational archetype for frameworks authored by founding pair (often family/co-founder relationship) plus small unnamed team. Distinct from solo (1 person), LLC (formal legal entity), academic-lab (university affiliation), and corporate (pre-existing company). 10th archetype in corpus.

### Evidence

- Unsloth v23: Daniel Han + Michael Han (likely brothers) + Unsloth team

### Validation path

Watch for framework pairs with 2 named principals + small team + no formal incorporation disclosed.

## 10. Pattern Library state post-v23

### Counts

| Category | Count | Delta |
|----------|-------|-------|
| Confirmed | **25** | +2 (#41, #43) |
| Active candidates | 19 | -2 promoted + 2 new (#45, #46) = net 0 |
| Stale candidates | 2 | unchanged |
| **Total** | **46** | +2 |

### Health metrics

- Candidates-to-confirmed ratio: **19:25 = 0.76:1** (healthy; well below 2:1 blocker)
- Stale-to-active ratio: 2:19 = 0.11 (low)
- Promotion rate: 2 per wiki (healthy velocity)

### Next audit triggers

- +5 new candidates → 24 candidates
- +5 wikis → v28
- Stale count > 5
- Ratio > 2:1

**No trigger hit at v23.**

## 11. Candidate staleness watch (from v22 mini-audit)

Pre-v23 aging candidates:
- #21 SDD methodology emergence — still aging
- #23 AI-disclosure policy — still aging
- #25 Personality-driven agent design — still aging

Post-v23: all 3 untouched (Unsloth training-infra ≠ these candidate domains). Flag stale at v25+ if not revisited.

## 12. Corpus cross-reference map

### Training-infra sub-type (N=2)

- LlamaFactory v22 (academic-lab, ACL 2024, 100+ models, Apache)
- **Unsloth v23** (duo-founder, no paper, 500+ models, dual Apache+AGPL)

### Outside-scope sub-types (4)

- **Education-aggregator:** build-your-own-x v8
- **Foundation-model-as-product:** fish-speech v20
- **Prompt-leak-archive:** system-prompts-leaks v21
- **Training-infrastructure:** LlamaFactory v22 + **Unsloth v23**

### Pattern ecosystem

Training-infra sub-type patterns:
- #41 Framework (CONFIRMED v23)
- #43 Optimizer-Research Velocity (CONFIRMED v23)
- #42 Academic-Published (candidate, correlates w/ #44)
- #44 Academic-Lab Affiliation (candidate, correlates w/ #42)

Cross-sub-type patterns touched at v23:
- #29 License-Category Diversity (confirmed; +AGPL data point)
- #32 Research-Paper-Chain Lineage (confirmed; N=3 now)

## 13. Validation-density framing retrospective

### Hypothesis (from v22 mini-audit)

> "unslothai/unsloth ... highest validation density per operator-time. Potentially promotes 4 candidates (#41/#42/#43/#44) in single ~2h wiki."

### Actual outcome

- **2 promotions** (#41 + #43) — target met
- **2 scope refinements** (#42 + #44) — valid alternative outcome (pattern doesn't universally apply; correlation discovered)
- **2 strengthenings** (#29 + #32) — bonus
- **2 new candidates** (#45 + #46) — bonus

### Verdict

Mini-audit framework validated. Validation-density wiki selection is **operationally useful pattern**:
1. After each wiki: mini-audit updates candidate watch-list
2. Identify wikis that would promote 2+ candidates in single execution
3. Execute in validation-density mode
4. Document promotions + scope refinements + new candidates

### Routine v2.1 upgrade candidate

Formalize validation-density mode:
- Phase 4b template: validation-analysis deliverable
- Pattern-library direct update (already part of v2)
- Explicit test-expectation documentation (what we expect vs what happened)

## 14. Operator notes

### For Storm Bear operator

- v23 exit state: Pattern Library healthy, no consolidation action required
- graphify-on-vault still deferred (8 sessions now; not flagged per v22 commitment)
- Audit trigger at v28 or +5 candidates — whichever first

### For future wiki selection

Validation-density targets to consider (post-v23):
- Academic-lab training-infra framework (would test #42 + #44)
- Duo-founder framework other than Unsloth (would test #46)
- Framework with dual-licensing (would test #45)

## 15. References

- PATTERN_LIBRARY.md (pre-v23 state)
- v22 LlamaFactory wiki + iteration log
- v22 mini-audit document: `04 Reviews/(C) 2026-04-20 Pattern Library mini-audit post-v22.md`
- v23 Unsloth wiki entities (4 entity pages)

---

**Pattern #41 Training-Infrastructure Framework + Pattern #43 Optimizer-Research Integration Velocity PROMOTE to CONFIRMED at v23 (N=2 each, LlamaFactory + Unsloth). Pattern #42 + #44 stay candidate with scope refinement (correlate as academic-lab sub-archetype). Pattern #29 + #32 evidence strengthened. 2 new candidates registered (#45 dual-licensing + #46 duo-founder). Validation-density wiki selection pattern operationally validated.**
