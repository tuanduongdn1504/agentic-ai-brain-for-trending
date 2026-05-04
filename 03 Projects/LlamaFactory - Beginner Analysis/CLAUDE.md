# LlamaFactory - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`hiyouga/LLaMA-Factory`](https://github.com/hiyouga/LLaMA-Factory) — **"Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)"**.

**70,305 stars (#6 in corpus), 8,604 forks (12.2% ratio), Apache-2.0 (2nd in corpus after gws v13), Python, main-branch, 978 open issues, 332 watchers, created 2023-05-28, pushed 2026-04-12**. **Author: hiyouga** (solo maintainer at 70K scale, **5th solo-at-enterprise-scale in corpus** after agency-agents 82.9K, spec-kit 89.2K corporate, TrendRadar 52.1K, system-prompts-leaks 135K).

**Scope status: OUTSIDE STORM BEAR CORE SCOPE** — training-infrastructure / fine-tuning-framework. **4th outside-scope sub-type** (after v8 education-aggregator + v20 foundation-model + v21 prompt-leak-archive).

**Positioning:** *"Unified Efficient Fine-Tuning of 100+ LLMs & VLMs"* — consolidates fine-tuning methods + model support + training stages into single framework.

**Core product:** Fine-tuning training infrastructure
- **100+ models supported** — LLaMA, Qwen, Mistral, Mixtral-MoE, DeepSeek, Gemma, GLM, Phi, InternLM, MiniCPM, Falcon + 90 others
- **Fine-tuning methods:** Full-tuning + Freeze-tuning + LoRA + QLoRA + OFT + QOFT
- **Training stages:** Pre-training + SFT (supervised fine-tuning) + Reward Modeling + PPO + DPO + KTO + ORPO + SimPO
- **Optimizer research integration:** GaLore + BAdam + APOLLO + Adam-mini + Muon (cutting-edge optimizers)
- **Performance:** FlashAttention-2, Unsloth, Liger Kernel, contamination-free packing
- **Distributed:** FSDP+QLoRA (70B on 2×24GB GPUs), DeepSpeed, Megatron-core backend
- **Interfaces:** CLI (`llamafactory-cli`) + WebUI (Gradio LLaMA Board) + OpenAI-style API
- **Datasets:** HuggingFace + ModelScope + Modelers hub + S3/GCS + built-in curated
- **Evaluation:** MMLU + C-Eval + CMMLU benchmarks integrated; W&B + SwanLab tracking
- **Deployment:** pip + Docker (CUDA/NPU/ROCm variants) + conda

**v2 Routine 12-axis classification:**

| Axis | Value |
|------|-------|
| **Tier** | **OUTSIDE-SCOPE — training-infrastructure sub-type** (4th sub-type in corpus) |
| **Archetype** | Solo (hiyouga) with Lab4AI academic affiliation |
| **Scale tier** | Large (70.3K stars — 6th in corpus) |
| **Primary lang** | Python |
| **Packaging** | pip + Docker (3 variants: CUDA/NPU/ROCm) + conda |
| **Origin story** | Academic research → ACL 2024 paper → community adoption (research-first pattern) |
| **Methodology** | NONE (framework, not methodology) |
| **Governance files** | README (bilingual EN+CN) + LICENSE (Apache-2.0) + docs site (llamafactory.readthedocs.io) + changelog |
| **Agent/skill count** | N/A (training framework, not agent) |
| **i18n** | **Bilingual EN + 简体中文** (2 langs) |
| **Intellectual influence** | **Research-paper-chain** — PEFT + TRL + QLoRA + FastChat + 100+ research projects. **Validates Pattern #19 4th archetype at N=2** (fish-speech + LlamaFactory). |
| **Agent platforms** | N/A (training infrastructure); but models trained here could power agents |

**Tier placement rationale:** OUTSIDE-SCOPE — training-infrastructure sub-type:
- Not an agent framework (T1-T5)
- Not a foundation model (fish-speech genre)
- Not a content archive (system-prompts-leaks genre)
- Not an aggregator (build-your-own-x genre)
- **Training-infrastructure / fine-tuning framework** — novel outside-scope sub-type at v22

**Outside-scope sub-types post-v22:**
1. Education aggregator (build-your-own-x v8)
2. Foundation model as product (fish-speech v20)
3. Prompt-leak archive (system-prompts-leaks v21)
4. **Training-infrastructure / fine-tuning framework (LlamaFactory v22 — NEW)**

**Critical Pattern tests at v22:**

- **Pattern #19 4TH ARCHETYPE VALIDATES at N=2** — research-paper-chain lineage at 2 data points (fish-speech v20 + LlamaFactory v22). Both cite extensive prior-research networks. Archetype now structurally confirmed.
- **Pattern #32 Research-Paper-Chain Lineage** — **PROMOTION-READY at N=2** (fish-speech + LlamaFactory).
- **Pattern #8 Empirical Research Emergence — 6th data point** — LlamaFactory has **ACL 2024 peer-reviewed publication** (stronger than arXiv-only like fish-speech 2 arXiv preprints). New highest-rigor evidence level.
- **Pattern #20 archetype-dictionary (v21 audit reformulation)** — consider adding row: "Solo training-infrastructure academic-published: ~70K stars" if this becomes pattern.
- **Pattern #18 OpenClaw/Hermes:** N/A (training framework, not agent).
- **Pattern #27 Community-Viral:** doesn't apply cleanly — LlamaFactory's scale path is academic-publication + community adoption (distinct from Reddit/CN/crypto viral).
- **Pattern #29 License-Category Diversity:** Apache-2.0 (permissive); doesn't add non-permissive data point.

**NEW Pattern candidates at v22:**

- **#41 candidate: Training-Infrastructure Framework** — new outside-scope sub-type (4th). LlamaFactory first. May predict Unsloth / Axolotl / TRL adjacent wikis.
- **#42 candidate: Academic-Published Peer-Reviewed Framework** — ACL 2024 venue distinct from arXiv-only preprint (fish-speech). Peer-review stronger research signal. May predict ICLR / NeurIPS / ACL frameworks distinct from arXiv-only.
- **#43 candidate: Optimizer-Research Integration Velocity** — LlamaFactory integrates GaLore + BAdam + APOLLO + Adam-mini + Muon (cutting-edge optimizer research). Research-velocity as feature. May predict more research-first frameworks with rapid integration.
- **#44 candidate: Academic-Lab Affiliation Archetype** — hiyouga + Lab4AI affiliation = academic-community solo pattern. Distinct from pure-solo + corporate + LLC + pseudonymous + open-core. May predict more academic-affiliated frameworks.

**Pattern promotions imminent at v22:**

- **Pattern #32 Research-Paper-Chain Lineage** — N=2, promotion-ready. But single archetype (foundation-model-space). Multi-tier requirement: both v20 + v22 outside-scope sub-types. Could promote at "structurally unambiguous at N=2" clause.
- **Pattern #19 4th archetype itself** (research-paper-chain) — already in confirmed Pattern #19 structure; validation at N=2 strengthens confidence.

**Novel elements at v22:**
1. **4th outside-scope sub-type** — training-infrastructure
2. **ACL 2024 peer-reviewed publication** — first peer-reviewed venue in corpus (vs arXiv-only)
3. **100+ models supported** — broadest model-support in any corpus wiki
4. **Optimizer research integration** — GaLore + BAdam + APOLLO + Adam-mini + Muon
5. **Multi-training-stage unified** — pre-train + SFT + reward model + RL (PPO/DPO/KTO/ORPO/SimPO)
6. **Lab4AI academic affiliation** — first academic-community archetype
7. **Docker multi-variant** — CUDA + NPU + ROCm (first NPU/ROCm support documented)
8. **Megatron-core backend** — first distributed-training backbone mentioned
9. **FSDP+QLoRA 70B on 2×24GB** — aggressive memory optimization claim
10. **ModelScope + Modelers hub** — first CN-hub support in corpus (beyond HuggingFace)
11. **OFT/QOFT methods** — orthogonal fine-tuning; novel vs standard LoRA

**Phase 4b routing = outside-scope meta-reference + 4th sub-type establishment + Pattern #19 4th archetype N=2 validation + Pattern #32 promotion-ready.** 4th use of outside-scope mode; continues v2 routine generalization.

## Claude's Role

Claude là wiki maintainer, chạy bằng routine `llm-wiki-routine-v2.md` (**22nd auto-execution, 4th v2 routine execution, 4th outside-scope wiki**):

- **Ingest sources via WebFetch** — README bilingual + docs (readthedocs) + arXiv 2403.13372 abstract
- **Cross-reference với 21 sibling wikis** — primarily v20 fish-speech (research-paper-chain precedent + outside-scope); v21 system-prompts-leaks (outside-scope + sub-type framework); v10 autoresearch (Karpathy ML training framework T5 peer)
- **Phase 4b = outside-scope 4th sub-type + Pattern #19 validation + Pattern #32 promotion candidate**
- **Beginner roadmap** — angle: developers wanting to fine-tune LLMs for custom agents; Storm Bear operator potential: training custom VN-language agent via LlamaFactory

**Prime directive:** Outcome = wiki + outside-scope 4th sub-type (training-infrastructure) + Pattern #19 4th archetype N=2 validation + Pattern #32 promotion-ready evidence + 4 new pattern candidates (#41-44) + Pattern #8 6th data point.

## Process — routine `llm-wiki-routine-v2.md`

7 phases. 4th v2 routine execution. Phase 4b = **outside-scope training-infrastructure + Pattern #19 validation**.

## Key People / Organization

- **hiyouga** — solo maintainer (ACL 2024 author)
- **Lab4AI** — academic affiliation
- **Co-authors on ACL 2024 paper** — inferred (arXiv 2403.13372)
- **Community:** Discord + WeChat (CN) + blog platform
- **Cross-project:** 21 sibling wikis. This is 22nd = 4th outside-scope + training-infrastructure sub-type + Pattern #19 4th archetype validation at N=2.

## Folder Structure

```
LlamaFactory - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md
├── 00-04 folders
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ VN + 13-section format
- **Cross-reference 21 siblings MANDATORY** — especially v20 fish-speech (research-lineage precedent)
- **Pattern Library direct update** (v2 routine Phase 5)
- **Document Pattern #19 4th archetype N=2 validation**
- **Document Pattern #32 promotion-ready evidence**
- **Establish outside-scope 4th sub-type** (training-infrastructure)

## Current Status

> **Last updated:** 2026-04-19
> **Status:** 🟡 Routine v2 auto-execute IN PROGRESS — 22nd LLM Wiki, 4th outside-scope, 4th v2 execution

### Expected milestones

- [x] Phase 0 Pre-flight with v2 12-axis classification
- [ ] Phase 1 Scaffold
- [ ] Phase 2 Source ingestion (3 clusters)
- [ ] Phase 3 Entity pages (4)
- [ ] Phase 4a Beginner published guide (bilingual VN/EN)
- [ ] Phase 4b **Outside-scope 4th sub-type + Pattern #19 N=2 validation + Pattern #32 promotion-ready**
- [ ] Phase 5 Iteration log v22 + PATTERN_LIBRARY.md update
- [ ] Phase 6 Vault file updates
