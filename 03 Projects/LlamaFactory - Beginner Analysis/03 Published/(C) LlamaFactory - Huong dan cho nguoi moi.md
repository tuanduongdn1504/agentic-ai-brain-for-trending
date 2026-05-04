# (C) LlamaFactory — Hướng dẫn cho người mới / Beginner's Guide

> **Repo:** [hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) — 70.3K ⭐, 8.6K forks, Apache-2.0
> **Tagline:** *"Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)"*
> **Philosophy:** Consolidate fragmented fine-tuning tooling into unified framework
> **Wiki:** `(C) index` — 22nd LLM Wiki in Storm Bear corpus (**4th outside-scope** — training-infrastructure sub-type)
> **Audience:** VN developers + AI engineers + Scrum coaches wanting custom fine-tuned models

---

## Part 1 — LlamaFactory là gì? / What is LlamaFactory?

### 🇻🇳 Tiếng Việt

**LlamaFactory** là **unified fine-tuning framework** cho 100+ LLM/VLM — từ LLaMA, Qwen, Mistral, DeepSeek đến Gemma, Phi, GLM. Consolidate 5+ tools (PEFT, TRL, QLoRA, FastChat) vào 1 framework với 3 interfaces (CLI + WebUI + API).

**Điểm nổi bật:**
- **70.3K stars** (#6 trong Storm Bear corpus; largest fine-tuning framework by star count)
- **Apache-2.0** — 2nd permissive OSI license in corpus after gws v13
- **ACL 2024 peer-reviewed** (arXiv 2403.13372) — first peer-reviewed venue in corpus
- **100+ models supported** — broadest model-support in any corpus wiki
- **9 training stages:** Pre-train + SFT + Reward Model + PPO + DPO + KTO + ORPO + SimPO
- **6 fine-tuning methods:** Full + Freeze + LoRA + QLoRA + OFT + QOFT
- **5 novel optimizers:** GaLore + BAdam + APOLLO + Adam-mini + Muon (all 2024 research)
- **4 performance libraries:** FlashAttention-2 + Unsloth + Liger Kernel + contamination-free packing
- **FSDP + QLoRA:** 70B fine-tune on 2×24GB consumer GPUs
- **3 Docker variants:** CUDA + NPU + ROCm (first NPU/ROCm in corpus)
- **Research-paper-chain lineage** — PEFT + TRL + QLoRA + FastChat + 100+ research projects
- **Author:** hiyouga + Lab4AI academic affiliation (first academic-lab archetype in corpus)
- **Bilingual EN + 简体中文** README
- **No commercial tier** — pure OSS

### 🇬🇧 English

LlamaFactory is a unified fine-tuning framework consolidating PEFT + TRL + QLoRA + FastChat into single tool supporting 100+ LLM/VLM families. Triple interface (CLI + Gradio WebUI + OpenAI-style API) across consumer hardware (2×24GB GPUs for 70B) and enterprise (Megatron-core). ACL 2024 peer-reviewed publication from hiyouga + Lab4AI academic affiliation.

---

## Part 2 — Corpus firsts at v22

| Signal | LlamaFactory | Corpus context |
|--------|--------------|----------------|
| **First ACL 2024 peer-reviewed publication** | ✅ | Prior: arXiv-only preprints (fish-speech v20) |
| **First academic-lab affiliation archetype** | ✅ | 9th organizational archetype |
| **First NPU + ROCm Docker variants** | ✅ | Prior: CUDA-only |
| **First Megatron-core backend mention** | ✅ | NVIDIA enterprise distributed training |
| **Broadest model support (100+)** | ✅ | Prior: 1-31 tools/models |
| **4th outside-scope sub-type (training-infra)** | ✅ | After v8 aggregator + v20 foundation + v21 leak-archive |
| **Pattern #19 4th archetype validated at N=2** | ✅ | research-paper-chain validates via LlamaFactory + fish-speech |
| **Pattern #32 promotion-ready** | ✅ | structurally-unambiguous-N=2 |
| **2nd Apache-2.0 license** | ✅ | after gws v13 |
| **First ModelScope + Modelers hub support** | ✅ | CN ecosystem parallel hubs |
| **Pattern #8 6th data point — peer-reviewed rigor** | ✅ | New highest rigor tier |

---

## Part 3 — Outside-scope placement (4th sub-type)

### 🇻🇳 4 outside-scope sub-types at v22

| # | Wiki | Sub-type |
|---|------|----------|
| 1 | build-your-own-x v8 | Education aggregator |
| 2 | fish-speech v20 | Foundation model as product |
| 3 | system-prompts-leaks v21 | Prompt-leak archive |
| 4 | **LlamaFactory v22** | **Training infrastructure (NEW)** |

### 🇬🇧 Why training-infrastructure is distinct

- **Not an agent** (not T1-T5)
- **Not a model** (not fish-speech genre)
- **Not an archive** (not system-prompts-leaks genre)
- **Not education** (not build-your-own-x genre)
- **Training framework** — produces fine-tuned models; enables downstream agent development

---

## Part 4 — Cài đặt / Installation

### 🇻🇳 4 deployment options

#### Option A: pip (simplest)

```bash
# Install latest from PyPI
pip install llamafactory

# Or with extras for specific backends
pip install "llamafactory[torch,metrics,liger-kernel]"
```

#### Option B: Docker (managed, 3 variants)

```bash
# NVIDIA CUDA (standard)
docker pull llamafactory:cuda
docker run --gpus all -p 7860:7860 llamafactory:cuda

# Huawei NPU (CN enterprise)
docker pull llamafactory:npu

# AMD ROCm
docker pull llamafactory:rocm
```

#### Option C: Conda (research workflows)

```bash
conda create -n llamafactory python=3.10
conda activate llamafactory
pip install llamafactory
```

#### Option D: From source (development)

```bash
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e ".[torch,metrics]"
```

### 🇬🇧 Cloud integrations

- **Google Colab** — free GPU for small models (7B with QLoRA)
- **Alibaba PAI-DSW** — CN cloud
- **LLaMA Factory Online** — free tier

### Hardware requirements

| Use case | GPU |
|----------|-----|
| 7B LoRA | 1× RTX 3090/4090 (24GB) or Colab T4 (16GB with QLoRA) |
| 13B LoRA | 1× RTX 3090/4090 (24GB) or A100 40GB |
| 70B QLoRA + FSDP | 2× RTX 3090/4090 (2×24GB = 48GB total) |
| 70B full | 8× A100 80GB (enterprise) |

---

## Part 5 — Sử dụng / Usage — 3 interfaces

### 🇻🇳 Interface A: Gradio WebUI (LLaMA Board)

**Launch:**
```bash
llamafactory-cli webui
# Open browser: http://localhost:7860
```

**Workflow:**
1. Chọn base model (e.g., Qwen2.5-7B-Instruct)
2. Chọn dataset (built-in hoặc custom)
3. Configure hyperparameters (rank, alpha, learning rate)
4. Click "Start" → training begins
5. Monitor progress → evaluate → export

### 🇬🇧 Interface B: CLI

**Direct fine-tuning:**
```bash
llamafactory-cli train \
  --model_name_or_path Qwen/Qwen2.5-7B-Instruct \
  --dataset alpaca_gpt4_en \
  --template qwen \
  --finetuning_type lora \
  --lora_target all \
  --lora_rank 8 \
  --lora_alpha 16 \
  --num_train_epochs 3 \
  --learning_rate 2e-4 \
  --output_dir ./qwen-finetuned \
  --fp16 True
```

**Config-driven (recommended):**
```bash
# qwen_lora.yaml
llamafactory-cli train qwen_lora.yaml
```

### Interface C: OpenAI-style API

**Serve fine-tuned model:**
```bash
llamafactory-cli api \
  --model_name_or_path ./qwen-finetuned \
  --adapter_name_or_path ./qwen-finetuned/lora \
  --port 8000
```

**Use from client:**
```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
response = client.chat.completions.create(
    model="qwen-finetuned",
    messages=[{"role": "user", "content": "Xin chào"}]
)
```

---

## Part 6 — Fine-tuning methods

### 🇻🇳 6 methods explained

| Method | Memory | Quality | Use case |
|--------|--------|---------|----------|
| **Full-tuning** | Highest | 100% | Research with ample compute |
| **Freeze-tuning** | High | ~95% | Limited GPU, need quality |
| **LoRA** | Low | ~90-95% | Consumer GPU, most common |
| **QLoRA** | Lowest | ~90-95% | Minimum memory |
| **OFT** | Low | ~90-95% | Prevent catastrophic forgetting |
| **QOFT** | Lowest | ~90-95% | Memory-constrained OFT |

### Default recommendation cho beginners

Start với **QLoRA** trên 7B model:
- Memory: 16GB sufficient
- Training time: 30-60 min for 10K examples
- Quality: competitive with full-tuning

### 🇬🇧 When to use each

- **Full:** research projects, adequate compute, need ceiling quality
- **LoRA/QLoRA:** production fine-tuning, consumer hardware
- **OFT/QOFT:** domain adaptation where pretrained knowledge critical
- **Freeze:** simpler than LoRA, faster iteration

---

## Part 7 — 9 training stages

### Full pipeline

1. **Pre-training** — from-scratch (rare, resource-intensive)
2. **SFT** — supervised fine-tuning on instruction data
3. **Reward Modeling** — train preference model
4. **PPO** — classical RLHF
5. **DPO** — preference optimization without reward model
6. **KTO** — Kahneman-Tversky optimization
7. **ORPO** — combined SFT + preference
8. **SimPO** — simple preference optimization

### Typical pipeline

Most practitioners: **SFT → DPO** (skip pre-training, skip reward modeling, use DPO instead of PPO).

Simpler + competitive quality with classical PPO RLHF.

---

## Part 8 — Research-paper-chain lineage (Pattern #19 4th archetype)

### 🇻🇳 LlamaFactory builds on 4 foundational research

- **PEFT** (HuggingFace) — LoRA + other parameter-efficient methods
- **TRL** (HuggingFace) — RLHF pipeline
- **QLoRA** (Tim Dettmers et al., 2023) — quantized LoRA
- **FastChat** (LMSYS) — SFT conventions

### Pattern #19 4th archetype validation

Prior v20: fish-speech cited 7 research projects (Pattern #19 4th archetype hypothesis).
**v22 LlamaFactory validates at N=2** — research-paper-chain lineage structurally confirmed.

### 🇬🇧 Implication

Foundation-model-space + training-infrastructure-space frameworks have distinct intellectual-lineage archetype (research-paper-chain) from:
- Individual-author (Karpathy, John Lam)
- Methodology (SDD, BMAD)
- Community-viral (agency-agents, TrendRadar)

---

## Part 9 — Storm Bear relevance (VN operator)

### 🇻🇳 Đánh giá cho Scrum coach

**Relevance level:** 🟡 **LOW-MEDIUM** — capability-awareness + fine-tuning potential.

**Positive signals (vs v21 system-prompts-leaks):**
- ✅ **Real author identity** — hiyouga, not pseudonym
- ✅ **Academic backing** — Lab4AI affiliation
- ✅ **Peer-reviewed publication** — ACL 2024
- ✅ **Apache-2.0 permissive license** — commercial OK
- ✅ **No ethical gray zones**
- ✅ **No perverse-incentive monetization**

**Limitations:**
- ⚠️ **Outside-scope** — training infra, not agent framework
- ⚠️ **GPU required** — consumer GPUs work, but need setup
- ⚠️ **Not directly Scrum-relevant** — tool building, not coaching use
- ⚠️ **Time-intensive** — fine-tuning takes hours-days + dataset curation

### Potential Storm Bear applications

#### Use case A: Custom VN Scrum coaching agent

1. **Base model:** Qwen2.5-7B-Instruct (strong CN + VN support via multilingual training)
2. **Dataset:** VN Scrum coaching conversations (curate from practice)
3. **Method:** QLoRA SFT on 1-5K examples
4. **Training:** ~2-4 hours on RTX 4090
5. **Deploy:** OpenAI-compatible API for team access
6. **Iterate:** Add DPO on team feedback preferences

#### Use case B: Skill-development for Storm Bear operator

- Learn modern fine-tuning stack
- Understand PEFT/TRL/QLoRA research lineage
- Build expertise for future AI-first client engagements

#### Use case C: Benchmarking vendors

- Fine-tune open model on Scrum scenarios
- Compare vs Claude/GPT-4 on coaching tasks
- Inform vendor-selection decisions for clients

### When LlamaFactory NOT relevant

- Pure coaching consulting (tool use, not tool building)
- Short-timeline engagements (fine-tuning takes time + data)
- Zero-GPU environments
- Clients with compliance requirements for model outputs

### Scrum ceremony mapping

| Ceremony | Use case |
|----------|----------|
| Sprint planning | N/A (infrastructure, not direct Scrum use) |
| Daily standup | Fine-tuned Scrum assistant could summarize |
| Sprint review | Fine-tuned model could generate reports |
| Retrospective | Fine-tuned model could analyze retro notes |

---

## Part 10 — 4-week learning roadmap

### Week 1: Setup + first LoRA fine-tune

- Day 1-2: Install via pip / Docker; verify GPU support
- Day 3-4: Launch LLaMA Board WebUI; configure first Qwen2.5-7B + alpaca_gpt4_en LoRA fine-tune
- Day 5-7: Evaluate output quality; iterate on hyperparameters

### Week 2: Custom dataset + VN fine-tune

- Day 8-10: Prepare VN instruction dataset (even 100-500 examples)
- Day 11-12: Fine-tune Qwen2.5-7B on VN dataset
- Day 13-14: Evaluate VN output quality; compare with base model

### Week 3: DPO alignment + API serving

- Day 15-17: Generate preference data (chosen/rejected pairs)
- Day 18-19: DPO training on top of SFT
- Day 20-21: Serve via API; test with client applications

### Week 4: Evaluation + decision

- Day 22-24: Run MMLU / C-Eval / CMMLU evaluation
- Day 25-26: Compare fine-tuned vs base vs Claude/GPT-4 on Scrum tasks
- Day 27-28: Decide — deploy / iterate further / revert to commercial API

---

## Part 11 — Tradeoffs + limitations

### Strengths

- ✅ **Unified framework** — replaces 5+ tools
- ✅ **100+ models supported** — broadest in any framework
- ✅ **Triple interface** — CLI/WebUI/API (democratized)
- ✅ **Consumer hardware** — 70B on 2×24GB via QLoRA+FSDP
- ✅ **Research velocity** — newest methods integrated fast
- ✅ **Apache-2.0** — commercial OK
- ✅ **ACL 2024 peer-reviewed** — academic credibility
- ✅ **Active community** — Discord + WeChat + GitHub
- ✅ **Free** — no commercial tier

### Limitations

- ❌ **Outside agent-scope** — infrastructure not agent
- ❌ **GPU required** — not zero-install
- ❌ **Hyperparameter complexity** — framework simplifies but training still hard
- ❌ **Dataset quality dependency** — garbage in, garbage out
- ❌ **Maintenance overhead** — 978 open issues signal volume
- ❌ **Consumer GPU compromises** — 70B fine-tuning on 2×24GB is theoretically possible but fragile (OOM risks)
- ❌ **Cutting-edge methods instability** — Muon, OFT may have edge cases
- ❌ **Not beginner-friendly for ML novices** — requires ML fundamentals

---

## Part 12 — Comparison with alternatives

### Fine-tuning framework landscape

| Framework | Scope | Stars | Strength |
|-----------|-------|-------|----------|
| **LlamaFactory** | Unified everything | 70K | Breadth + unified |
| Unsloth | LoRA speed-optimized | 30K | 2× speed |
| Axolotl | Config-driven | 10K | YAML-simple |
| TRL (HuggingFace) | RLHF pipeline | 15K | Official HF |
| PEFT (HuggingFace) | Adapter methods | 20K | Official HF |
| Hugging Face accelerate | Training loops | Many | Low-level |

### When to choose LlamaFactory

- Want unified framework (don't want to stitch tools)
- Need breadth of model support (100+)
- Want WebUI for non-coding team members
- Like research-velocity approach
- Value peer-reviewed research backing

### When to choose alternatives

- **Unsloth:** speed-optimization priority (2× faster LoRA)
- **Axolotl:** want simpler YAML-config workflow
- **TRL alone:** need only RLHF, don't need broad model support
- **PEFT alone:** want lower-level adapter control

---

## Part 13 — References + next action

### Wiki pages

- [[(C) index]]
- [[(C) README + 100+ models + positioning cluster summary]]
- [[(C) Training methods + optimizers + research-lineage cluster summary]]
- [[(C) Deployment + community + ACL 2024 cluster summary]]
- [[(C) 100+ Model Support + Unified Training Stages]]
- [[(C) Fine-Tuning Methods + Optimizer Research Integration]]
- [[(C) Academic-Lab Archetype + Pattern 19 4th Archetype N=2 Validation]]
- [[(C) Outside-Scope 4th Sub-Type + Training-Infrastructure + Storm Bear]]

### Cross-wiki siblings

- Outside-scope precedents: build-your-own-x v8, fish-speech v20, system-prompts-leaks v21
- Pattern #19 4th archetype peer: fish-speech v20 (research-paper-chain at N=2 via LlamaFactory v22)
- Research-first peer: autoresearch v10 (Karpathy ML training framework T5)
- Apache-2.0 peer: gws v13
- CN-ecosystem adjacent: TrendRadar v19, deer-flow v9

### Official resources

- Repo: https://github.com/hiyouga/LLaMA-Factory
- Docs: https://llamafactory.readthedocs.io
- ACL 2024 paper: https://arxiv.org/abs/2403.13372
- Discord: (from README)
- WeChat: (CN community)

### 🎯 Suggested next action (Storm Bear)

**Primary:** Still strongly recommend **running graphify on vault** (NOW 6 sessions overdue since v16, user explicit decision needed).

**Secondary (if LlamaFactory exploration desired):** Start with 4-week roadmap above. Week 1-2 suffices for capability awareness. Week 3-4 only if serious deployment path.

**For custom VN Scrum agent:** If committed to building, use roadmap. Budget: 1-2 weeks of operator time + RTX 4090 access (~$2K or cloud).

**For pattern observation only:** This wiki serves that purpose. No further engagement needed.

---

**Wiki 22/22 — 4th outside-scope wiki (training-infrastructure sub-type) + Pattern #19 4th archetype VALIDATES at N=2 + Pattern #32 PROMOTION-READY + 4 new pattern candidates (#41-44) + Pattern #8 6th data point (peer-reviewed rigor) + first academic-lab archetype + first ACL 2024 venue + first NPU/ROCm support. Routine `llm-wiki-routine-v2.md` 4th execution. Apache-2.0 clean-license, academic-backed, commercially-viable.**
