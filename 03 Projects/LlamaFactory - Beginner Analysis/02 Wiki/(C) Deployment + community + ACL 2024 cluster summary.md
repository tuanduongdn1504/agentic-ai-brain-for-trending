# (C) Deployment + community + ACL 2024 cluster summary

> **Cluster:** Multi-interface deployment + Docker variants + academic ACL 2024 context + community
> **Parent:** [[(C) index]]
> **Sources:** README deployment section + docs.llamafactory.readthedocs.io + Discord/WeChat references + arXiv 2403.13372 (ACL 2024)
> **Status:** ✅ Phase 2 cluster summary

---

## 1. Cluster scope

3 related signals:
1. **3 interfaces** — CLI + Gradio WebUI + OpenAI-style API
2. **Multi-variant Docker** — CUDA + NPU + ROCm
3. **ACL 2024 peer-reviewed publication** — academic context + community

## 2. Three interfaces

### Interface options for different users

| Interface | Audience | Use case |
|-----------|----------|----------|
| **`llamafactory-cli`** (CLI) | CLI-savvy researchers | Scriptable, reproducible pipelines |
| **Gradio WebUI** (LLaMA Board) | Non-programmer users | Point-and-click experimentation |
| **OpenAI-style API** | Developers integrating | Serve trained models |

### Why triple-interface matters

- **CLI** = reproducibility + version control + scripting
- **WebUI** = democratization (non-ML-engineer accessibility)
- **API** = production serving + agent integration

### Cross-framework comparison

| Framework | Interfaces |
|-----------|-----------|
| TRL | CLI only |
| PEFT | API only (library) |
| Axolotl | CLI (config-driven) |
| Unsloth | CLI + notebook examples |
| **LlamaFactory** | **CLI + WebUI + API (triple)** |

**LlamaFactory most accessible** of comparable frameworks.

## 3. LLaMA Board WebUI

### Gradio-powered interface

Visual interface for:
- Model selection from 100+ support list
- Training hyperparameter configuration
- Dataset selection + curation
- Training launch + monitoring
- Evaluation dashboard
- Export to HuggingFace / ModelScope

### Democratization signal

WebUI lowers barrier-to-entry for fine-tuning. Non-ML-engineer users can fine-tune via point-and-click.

## 4. Multi-variant Docker deployment (corpus-first)

### 3 Docker variants

| Variant | Target hardware |
|---------|-----------------|
| **CUDA** (default) | NVIDIA GPUs |
| **NPU** | Huawei Ascend NPUs (CN enterprise) |
| **ROCm** | AMD Instinct GPUs |

### First NPU + ROCm in corpus

- **NPU (Huawei Ascend)** = first CN-hardware support in corpus. Signals CN enterprise market focus.
- **ROCm (AMD)** = first AMD GPU support in corpus. Signals hardware-diversity awareness.

### Cross-corpus comparison

| Wiki | Hardware diversity |
|------|---------------------|
| Most corpus | Implicit (NVIDIA assumed) |
| gws v13 | Cloud-agnostic |
| fish-speech v20 | H200 flagship |
| **LlamaFactory v22** | **CUDA + NPU + ROCm (first explicit triple-support)** |

## 5. Deployment channels

### Install options

```bash
# pip (simplest)
pip install llamafactory

# Docker (managed)
docker pull llamafactory:cuda
docker pull llamafactory:npu
docker pull llamafactory:rocm

# Conda (research workflows)
conda install -c conda-forge llamafactory

# From source
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e ".[torch,metrics]"
```

### Cloud integrations

- **Google Colab** (free tier OK for small models)
- **Alibaba PAI-DSW** (CN cloud)
- **LLaMA Factory Online** (free tier)

### No commercial SaaS

Unlike fish-speech v20 (paid commercial API), LlamaFactory is pure-OSS. No paid tier.

## 6. Dataset ecosystem

### Dataset hubs

| Hub | Scope |
|-----|-------|
| **HuggingFace Hub** | Global standard |
| **ModelScope** | Alibaba CN hub |
| **Modelers** | Alibaba/HuggingFace partnership |
| **S3 / GCS** | Cloud storage |
| **Built-in curated** | LlamaFactory's own dataset library |

### Pattern #18 regional coverage

ModelScope + Modelers support = CN ecosystem parallel infrastructure. Strengthens Pattern #18 regional-ecosystem hypothesis (CN has own hubs alongside HuggingFace).

### Built-in datasets

LlamaFactory ships curated datasets for common fine-tuning tasks:
- Instruction tuning datasets (Alpaca, ShareGPT-like)
- RLHF preference datasets
- Multi-language datasets (EN + CN)
- Tool-use (function-calling) datasets

## 7. ACL 2024 — academic publication

### Publication details

- **Conference:** ACL 2024 (Association for Computational Linguistics)
- **Paper type:** System demonstration (likely) or short paper
- **arXiv preprint:** 2403.13372
- **Venue rigor:** Peer-reviewed (top-tier NLP venue)

### Significance for Storm Bear corpus

**ACL 2024 = first peer-reviewed publication in corpus.** Prior Pattern #8 evidence:

| # | Wiki | Evidence type | Rigor tier |
|---|------|---------------|------------|
| 1 | codymaster v12 | SkillsBench internal | Framework-internal |
| 2 | autoresearch v10 | val_bpb metric | Personal metric |
| 3 | graphify v16 | 71.5× token reduction | Documentation claim |
| 4 | spec-kit v17 | 48× productivity | Documentation claim |
| 5 | fish-speech v20 | 2 arXiv preprints | Preprint (not peer-reviewed) |
| **6** | **LlamaFactory v22** | **ACL 2024 peer-reviewed** | **Peer-reviewed venue (NEW highest rigor)** |

**Pattern #8 6th data point with new highest rigor tier.**

### Pattern #42 candidate — Academic-Published Peer-Reviewed Framework

**Formal statement (candidate):**
> Academic-published peer-reviewed frameworks distinct from arXiv-only preprint. ACL / NeurIPS / ICLR / ICML venue implies methodology documentation at peer-review depth + community validation. Stronger research signal than preprint.

**Evidence at v22:** 1 (LlamaFactory ACL 2024).

**Prediction:** More academic-community frameworks may appear with peer-reviewed publications. Pattern distinguishes research-lab rigor levels.

## 8. Community channels

### Global + regional community

- **Discord** — global English community
- **WeChat user groups** — CN community (primary)
- **GitHub Issues** (978 open) — technical feedback
- **Blog platform** — research updates + tutorials

### Lab4AI academic affiliation

hiyouga is affiliated with Lab4AI (academic research lab). Signals:
- Academic backing (vs pure-OSS-solo)
- Research continuity
- Paper co-authors collaboration

### Pattern #44 candidate — Academic-Lab Affiliation Archetype

**Formal statement (candidate):**
> Academic-lab affiliated solo framework archetype: author has university or research-lab affiliation providing research backing + paper co-authors + academic community. Distinct from pure-solo + corporate + LLC + pseudonymous + open-core archetypes.

**Evidence at v22:** 1 (hiyouga + Lab4AI).

**Prediction:** More academic-affiliated frameworks may emerge (ACL / ICLR / NeurIPS paper-adjacent repos).

## 9. Pattern #44 distinction from other archetypes

### Organizational archetype map post-v22

| # | Archetype | Example |
|---|-----------|---------|
| 1 | Pure-solo known | Karpathy (autoresearch), Jesse Vincent (Superpowers), sansan0 (TrendRadar) |
| 2 | Solo formalized LLC | BMad Code (BMAD) |
| 3 | Solo VN-context | Tody Le (codymaster) |
| 4 | Corporate official | Google (gws), GitHub (spec-kit), ByteDance (deer-flow) |
| 5 | Community-ambiguous | paperclip, GSD |
| 6 | Education corporate | Microsoft (course) |
| 7 | Open-core commercial entity | 39 AI INC (fish-speech) |
| 8 | Pseudonymous | x1xhlol (system-prompts-leaks) |
| 9 | **Academic-lab affiliation** | **hiyouga + Lab4AI (LlamaFactory — NEW v22)** |

**9 organizational archetypes now documented in corpus.**

## 10. Comparison with v20 fish-speech (closest peer)

Both research-first, both outside-scope:

| Dimension | fish-speech v20 | LlamaFactory v22 |
|-----------|-----------------|-------------------|
| Outside-scope sub-type | Foundation-model-as-product | Training-infrastructure |
| Paper | 2 arXiv preprints | ACL 2024 peer-reviewed |
| Organization | 39 AI INC (commercial) | Academic lab affiliation |
| License | Custom non-OSI | Apache-2.0 |
| Scale | 29.8K | 70.3K |
| Deployment | Docker + HF + SGLang | Docker 3-variant + pip + conda |
| Commercial tier | Yes (paid API) | No |
| Research lineage | 7 citations | PEFT+TRL+QLoRA+FastChat + 100+ |
| Community | Discord | Discord + WeChat + blog |

**Key distinction:** fish-speech = commercial-research-lab; LlamaFactory = academic-research-lab.

## 11. Key observations

### Cluster-level

- **3 interfaces** (CLI + WebUI + API) — democratization signal
- **Multi-variant Docker** (CUDA + NPU + ROCm) — hardware diversity
- **ACL 2024 peer-reviewed** — first peer-reviewed in corpus
- **Academic-lab affiliation** (Lab4AI) — new organizational archetype
- **Pure-OSS no-paid-tier** — distinct from open-core fish-speech

### Cross-corpus

- **Pattern #8 6th data point** with new peer-reviewed rigor tier
- **Pattern #42 candidate** (Academic-Published Peer-Reviewed)
- **Pattern #44 candidate** (Academic-Lab Affiliation Archetype)
- **Pattern #18 regional** — NPU hardware + ModelScope/Modelers hubs strengthen CN-ecosystem evidence

## 12. References

- Parent: [[(C) index]]
- Source: README deployment section + llamafactory.readthedocs.io + arXiv 2403.13372
- Sibling clusters: [[(C) README + 100+ models + positioning cluster summary]] + [[(C) Training methods + optimizers + research-lineage cluster summary]]

---

**Cluster summary: 3 interfaces (CLI/WebUI/API) + multi-variant Docker (CUDA/NPU/ROCm first in corpus) + ACL 2024 peer-reviewed publication (first in corpus) + Lab4AI academic affiliation (9th organizational archetype). Pattern #8 6th data point with highest-rigor tier (peer-reviewed). Patterns #42 (Academic-Published Peer-Reviewed) + #44 (Academic-Lab Affiliation Archetype) formalized. Pure-OSS Apache-2.0 no-commercial-tier distinct from fish-speech v20 open-core.**
