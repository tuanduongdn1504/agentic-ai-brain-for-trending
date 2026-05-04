# (C) Log — Unsloth Wiki Build

## 2026-04-20 Phase 0+1 — Pre-flight + Scaffold (v2 routine 5th execution)

- **API probe passed:** 62,218 stars (#8 in corpus), 5,422 forks (8.7%), **DUAL-LICENSE Apache-2.0 core + AGPL-3.0 UI**, Python, created 2023-11-29
- **Author:** Daniel Han + Michael Han + Unsloth team (duo-founder, likely brothers)
- **Organization:** Unsloth AI (company/team, not academic-lab)
- **Homepage:** unsloth.ai/docs
- **Docker:** unsloth/unsloth
- **Consolidation guard:** PASSED (post-v22 mini-audit 0.83:1 ratio)

### Scope decision: OUTSIDE-SCOPE — training-infrastructure sub-type (2nd entrant)

Pattern #41 Training-Infrastructure Framework validates at N=2:
- 1st entrant: LlamaFactory v22 (70.3K stars, academic-lab Lab4AI, ACL 2024, 100+ models)
- **2nd entrant: Unsloth v23 (62.2K stars, duo-founder Han brothers, no publication, 500+ models)**

### Critical validation analysis at v23

**Patterns that VALIDATE (PROMOTE to confirmed):**
- **#41 Training-Infrastructure Framework** — N=2 (LlamaFactory + Unsloth) → PROMOTE
- **#43 Optimizer-Research Integration Velocity** — N=2 (LlamaFactory 5 optimizers + Unsloth Triton kernels + GRPO + padding-free) → PROMOTE

**Patterns that STAY CANDIDATE at N=1 (scope refinement):**
- **#42 Academic-Published Peer-Reviewed** — Unsloth has no peer-reviewed publication; scope refines to academic-lab-correlated
- **#44 Academic-Lab Affiliation** — Unsloth is company/duo, not academic; scope refines to genuine academic-lab archetype

**Additional updates:**
- **Pattern #29 License-Category Diversity** (confirmed v21) — adds AGPL-3.0 data point (Unsloth Studio UI). Corpus non-permissive now at N=4.
- **Pattern #32 Research-Paper-Chain Lineage** (promoted v22) — adds 3rd data point (Unsloth acknowledges llama.cpp + HF + PyTorch + Torch AO + NVIDIA NeMo). N=3 now.
- **Pattern #19 4th archetype** — adds data point; N=3 now.

### NEW Pattern candidates at v23 (2)

- **#45 Dual-Licensing Strategy** — Apache-2.0 (core) + AGPL-3.0 (UI). First dual-license in corpus. Deliberate license split to protect derivative UIs while enabling community code reuse.
- **#46 Duo-Founder + Team Archetype** — Daniel Han + Michael Han + Unsloth team. 10th organizational archetype in corpus (distinct from solo-known, corporate, LLC, academic-lab, pseudonymous, etc.).

### Top findings from Phase 0

1. **62.2K stars / 5.4K forks** — #8 in corpus, close to LlamaFactory (70.3K)
2. **Dual-license** (Apache core + AGPL UI) — first in corpus
3. **500+ models** — broader than LlamaFactory's 100+ (marketing framing)
4. **2× faster / 70% less VRAM** — headline performance claims
5. **GRPO with 80% less VRAM** — MoE 12× faster + 35% less VRAM
6. **Custom Triton kernels** — RoPE + MLP + padding-free packing
7. **Consumer-GPU focus** — RTX 30/40/50 + Blackwell explicit target
8. **Unsloth Studio WebUI** — AGPL-3.0 separate from core
9. **MLX training coming** — first Apple Silicon training mention in corpus
10. **Han brothers duo-founder** — 10th org archetype candidate
11. **No academic publication** — distinct from LlamaFactory ACL 2024
12. **No academic-lab affiliation** — distinct from LlamaFactory Lab4AI
13. **Community:** Discord + Reddit r/unsloth + X @unslothai
14. **Active maintenance** — 1,153 open issues, pushed 2026-04-20
15. **Research-paper-chain lineage** — shorter than LlamaFactory (Pattern #32 data point #3)

### Source strategy (leaner than typical — validation-focused wiki):

1. README + performance claims + 500 models cluster — headline positioning
2. Custom Triton kernels + GRPO + consumer-GPU focus cluster — technical differentiation
3. Dual-license + duo-founder + Unsloth Studio cluster — organizational + licensing novelty

- **Phase 0+1 status:** ✅ COMPLETE
- **Next:** Phase 2 source summaries

---

## 2026-04-20 Phase 2-6 — v23 Unsloth wiki SHIPPED

### Phase 2: 3 cluster summaries ✅
- README + performance claims + 500 models
- Custom Triton kernels + GRPO + consumer-GPU focus
- Dual-license + duo-founder + Unsloth Studio

### Phase 3: 4 entity pages ✅
- (C) 500+ Models + Performance-Optimization Positioning
- (C) Custom Triton Kernels + Pattern 43 Validation
- (C) Han Brothers Duo-Founder + Dual-License Strategy
- (C) Training-Infra 2nd Entrant + Pattern 41 43 Validation + Storm Bear (13th Storm Bear meta)

### Phase 4a: Beginner bilingual guide ✅
`03 Published/(C) Unsloth - Huong dan cho nguoi moi.md` — consumer-GPU fine-tuning angle with honest "skip if API-only" warning

### Phase 4b: Validation analysis deliverable ✅
`03 Published/(C) Validation analysis + Pattern 41 43 promotions.md` — primary v23 focus; documents pattern library state transitions

### Phase 5: Iteration log + Pattern Library direct updates ✅
`04 Reviews/(C) 2026-04-20 v23 build learnings.md` created; PATTERN_LIBRARY.md updated inline:
- **Promoted: #41 Training-Infrastructure Framework + #43 Optimizer-Research Velocity** (both N=2, structurally unambiguous)
- **Scope-refined: #42 + #44** (academic-lab-correlated, stays candidate)
- **Strengthened: #29** (+AGPL-3.0, N=4 non-permissive) + **#32** (N=3 research-paper-chain)
- **New candidates: #45 Dual-Licensing Strategy + #46 Duo-Founder + Team Archetype**
- Post-v23 counts: **25 confirmed + 19 active + 2 stale = 46 total; ratio 0.76:1 (healthy)**

### Phase 6: Vault sync ✅
- project index/log marked complete
- root CLAUDE.md + GOALS.md appended

### Summary

- **Duration:** ~2h (velocity plateau maintained)
- **Validation density:** 2 promotions + 2 scope refinements + 2 strengthenings + 2 new candidates = 8 pattern-library actions in single wiki
- **Validation-density framing validated** as operationally useful routine pattern
- **8 new routine v2.1 action items** (~135+ cumulative)

---
