# Unsloth - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`unslothai/unsloth`](https://github.com/unslothai/unsloth) — **"Run and train AI models with a unified local interface"** / **"Train 500+ models up to 2× faster with up to 70% less VRAM, no accuracy loss"**.

**62,218 stars (#8 in corpus), 5,422 forks (8.7% ratio), DUAL-LICENSE (Apache-2.0 core + AGPL-3.0 Studio UI), Python, main-branch, 1,153 open issues, 349 watchers, created 2023-11-29, pushed 2026-04-20**. Author: **Daniel Han + Michael Han + Unsloth team** (duo-founder + team; Han brothers likely; **10th organizational archetype candidate**).

**Scope status: OUTSIDE STORM BEAR CORE SCOPE** — training-infrastructure sub-type (2nd entrant after LlamaFactory v22). **Validates Pattern #41 at N=2.**

**Positioning:** *"Run and train AI models with a unified local interface"* — Unsloth Studio WebUI + consumer-GPU-optimization focus + custom Triton kernels for 2× speed / 70% less VRAM.

**Core product:** Training-infrastructure + Unsloth Studio WebUI
- **500+ models supported** — Gemma 4, Qwen3.5, gpt-oss, DeepSeek, Llama 3.1/3.2, Mistral, Phi-4, embedding models, VLMs, TTS models
- **Fine-tuning methods:** Full + LoRA + 4-bit + 16-bit + FP8 + GRPO (RL) + DPO + pretraining
- **Performance claims:** 1.5-2× faster training, 50-70% less VRAM (varies by model/method)
- **GRPO RL:** 80% less VRAM
- **MoE training:** 12× faster, 35% less VRAM
- **Custom Triton kernels** — RoPE + MLP + padding-free packing (3× faster + 30% less VRAM)
- **Long-context RL:** 7× longer context vs comparable setups
- **Unsloth Studio WebUI** — AGPL-3.0 licensed (distinct from Apache core)
- **Hardware focus:** NVIDIA RTX 30/40/50 + Blackwell + DGX + macOS (MLX coming) + AMD + Intel
- **Deployment:** pip + Docker (unsloth/unsloth) + Colab notebooks + local (macOS/Linux/WSL/Windows)

**v2 Routine 12-axis classification:**

| Axis | Value |
|------|-------|
| **Tier** | **OUTSIDE-SCOPE — training-infrastructure sub-type (2nd entrant)** |
| **Archetype** | **Duo-founder + team** (Daniel Han + Michael Han + Unsloth team) — potential 10th organizational archetype |
| **Scale tier** | Large (62.2K stars — #8 in corpus) |
| **Primary lang** | Python |
| **Packaging** | pip + Docker + Colab notebooks |
| **Origin story** | Unsloth AI (company/organization) founded 2023-11; Han brothers + team |
| **Methodology** | NONE (framework, not methodology) |
| **Governance files** | README + LICENSE (dual Apache + AGPL) + docs site (unsloth.ai/docs) |
| **Agent/skill count** | N/A (training framework) |
| **i18n** | None apparent (English-only) |
| **Intellectual influence** | Acknowledges llama.cpp, HuggingFace (transformers, TRL), PyTorch, Torch AO, NVIDIA NeMo DataDesigner. **Pattern #32 data point #3** (research-paper-chain) — shorter list than LlamaFactory. |
| **Agent platforms** | N/A (training infrastructure); but models trained here could power agents |

**Tier placement rationale:** OUTSIDE-SCOPE — training-infrastructure (same sub-type as LlamaFactory v22):
- Not an agent framework (T1-T5)
- Training-infrastructure: produces fine-tuned models
- **Validates Pattern #41 at N=2**

**Pattern validation analysis at v23 (primary Phase 4b focus):**

### Patterns that VALIDATE at N=2 (PROMOTE to confirmed)

- **Pattern #41 Training-Infrastructure Framework** — N=2 (LlamaFactory v22 + Unsloth v23)
  - Both are training-infrastructure sub-type
  - Both support 100-500+ models
  - Both replace fragmented fine-tuning tooling
  - Both consumer-GPU-optimization enabled
  - → **PROMOTE to CONFIRMED**

- **Pattern #43 Optimizer-Research Integration Velocity** — N=2 (LlamaFactory v22 + Unsloth v23)
  - LlamaFactory: 5 novel 2024 optimizers + 5 RL methods integrated
  - Unsloth: custom Triton kernels + GRPO + padding-free packing + FP8 + MLX (coming)
  - Both research-to-production velocity as competitive edge
  - → **PROMOTE to CONFIRMED**

### Patterns that STAY CANDIDATE at N=1 (scope refinement)

- **Pattern #42 Academic-Published Peer-Reviewed Framework** — Unsloth has NO academic publication
  - LlamaFactory: ACL 2024 peer-reviewed
  - Unsloth: no academic publications in README
  - **Scope refinement:** #42 correlates with academic-lab affiliation, not universal in training-infra space
  - Stays candidate N=1; may validate at v24+ with academic-lab framework

- **Pattern #44 Academic-Lab Affiliation Archetype** — Unsloth is company/duo, not academic
  - LlamaFactory: hiyouga + Lab4AI academic
  - Unsloth: Daniel Han + Michael Han + Unsloth team (company/duo)
  - **Scope refinement:** #44 is genuine academic-lab archetype, not all research-heavy frameworks
  - Stays candidate N=1; confirms hypothesis #42 + #44 correlate

### Additional pattern data points (strengthen confirmed)

- **Pattern #29 License-Category Diversity (confirmed v21)** — adds AGPL-3.0 data point (Unsloth Studio UI). Corpus non-permissive now at N=4: 2 GPL-3.0 + 1 AGPL-3.0 + 1 custom non-OSI.
- **Pattern #32 Research-Paper-Chain Lineage (promoted v22)** — adds 3rd data point (Unsloth acknowledges llama.cpp + HF + PyTorch + Torch AO + NVIDIA NeMo). Narrower lineage than fish-speech/LlamaFactory but same archetype. N=3.
- **Pattern #19 4th archetype (research-paper-chain)** — adds data point; archetype now N=3.
- **Pattern #20 archetype-dictionary** — add row? "Duo-founder + company + consumer-GPU-optimization: ~62K stars" — consider.

**NEW Pattern candidates at v23:**

- **#45 candidate: Dual-Licensing Strategy** — Apache-2.0 (core package) + AGPL-3.0 (UI/Studio). Deliberate license split to protect derivative UIs while enabling community code reuse. First in corpus.
- **#46 candidate: Duo-Founder + Team Archetype** — Daniel Han + Michael Han (likely brothers) + Unsloth team. Distinct from pure-solo (1 person) + LLC (formalized) + academic-lab (university-affiliated) + corporate (pre-existing). 10th organizational archetype in corpus.

**Novel elements at v23:**
1. **Dual-licensing** (Apache + AGPL) — first in corpus
2. **AGPL-3.0** — first in corpus (adds to #29)
3. **Han brothers duo-founder** — 10th organizational archetype
4. **Consumer-GPU-focus positioning** — RTX 30/40/50 + Blackwell explicit target
5. **Custom Triton kernels** (RoPE + MLP) — performance competitive moat
6. **Padding-free packing** — 3× faster + 30% less VRAM
7. **500+ models** — larger than LlamaFactory's 100+
8. **Unsloth Studio WebUI (AGPL)** — UI/backend license split
9. **MLX training support (coming)** — first Apple Silicon training mention
10. **gpt-oss + embedding + TTS + VLM** — cross-modality training breadth
11. **7× longer context RL** — unique long-context RL claim
12. **Reddit r/unsloth** — first subreddit community in corpus

**Phase 4b routing = validation analysis deliverable** — primary focus on which v22 candidates validate vs stay candidate; continues outside-scope training-infra sub-type at N=2.

## Claude's Role

Claude là wiki maintainer, chạy bằng routine `llm-wiki-routine-v2.md` (**23rd auto-execution, 5th v2 routine execution, 5th outside-scope wiki**):

- **Ingest sources via WebFetch** — README + docs.unsloth.ai
- **Cross-reference với 22 sibling wikis** — primarily LlamaFactory v22 (training-infra peer for Pattern #41 + #43 validation) + fish-speech v20 (research-paper-chain peer)
- **Phase 4b = validation analysis** — document which #41-44 validate vs stay candidate
- **Beginner roadmap** — angle: developers wanting faster fine-tuning on consumer hardware

**Prime directive:** Outcome = wiki + Pattern #41 + #43 PROMOTION to confirmed + Pattern #42 + #44 scope refinement + Pattern #29 + #32 evidence strengthening + 2 new candidates (#45 dual-licensing + #46 duo-founder archetype).

## Process — routine `llm-wiki-routine-v2.md`

7 phases. 5th v2 routine execution. Phase 4b = **validation analysis deliverable**.

## Key People / Organization

- **Daniel Han** — co-founder (likely)
- **Michael Han** — co-founder (likely brother)
- **Unsloth team** — unnamed team members
- **Unsloth AI** — organization name (incorporation unclear)
- **Community:** Discord + Reddit r/unsloth + X @unslothai
- **Cross-project:** 22 sibling wikis. This is 23rd = 5th outside-scope + 2nd training-infra + validation-density execution.

## Folder Structure

```
Unsloth - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md
├── 00-04 folders
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ VN + 13-section format
- **Cross-reference 22 siblings MANDATORY** — especially LlamaFactory v22 for Pattern #41/#43 validation
- **Pattern Library direct update** (v2 routine Phase 5) — promote #41 + #43; scope-refine #42 + #44; strengthen #29 + #32; register #45 + #46
- **Validation-density focus** — wiki primarily serves pattern-library validation, not novel-discovery

## Current Status

> **Last updated:** 2026-04-20
> **Status:** 🟡 Routine v2 auto-execute IN PROGRESS — 23rd LLM Wiki, 5th outside-scope, 5th v2 execution, validation-density focus

### Expected milestones

- [x] Phase 0 Pre-flight with v2 12-axis classification + validation analysis preview
- [ ] Phase 1 Scaffold
- [ ] Phase 2 Source ingestion (3 clusters — may be leaner given similarity to LlamaFactory)
- [ ] Phase 3 Entity pages (4 — focused on differentiators vs LlamaFactory)
- [ ] Phase 4a Beginner published guide (bilingual VN/EN)
- [ ] Phase 4b **Validation analysis deliverable** — Pattern #41 + #43 promotion + #42/#44 refinement
- [ ] Phase 5 Iteration log v23 + PATTERN_LIBRARY.md update (2 promotions + 2 new candidates)
- [ ] Phase 6 Vault file updates
