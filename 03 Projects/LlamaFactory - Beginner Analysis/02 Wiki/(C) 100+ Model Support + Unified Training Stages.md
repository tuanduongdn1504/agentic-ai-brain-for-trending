# (C) 100+ Model Support + Unified Training Stages

> **Type:** Entity — core capability
> **Parent:** [[(C) index]]
> **Sources:** README model support + training stages section
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

LlamaFactory supports **100+ LLM and VLM families** for fine-tuning (broadest model-support in any Storm Bear corpus wiki). Unified framework consolidates **9 training stages** — pre-training, SFT, reward modeling, and 5 RL alignment methods (PPO, DPO, KTO, ORPO, SimPO). Enables full training lifecycle in single framework previously requiring PEFT + TRL + QLoRA + FastChat combined.

## 2. Key claims

1. 100+ models supported = broadest in corpus (1st training-side breadth)
2. Unified 9-stage training pipeline (pre-train → SFT → reward → 5 RL methods)
3. VLM (vision-language) support alongside text LLM
4. CN + Western model families equally supported
5. Replaces fragmented PEFT + TRL + QLoRA + FastChat tool chain

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 100+ models | README supported model list | High |
| 9 training stages | README training stages section | High |
| VLM support | README + docs | High |
| PEFT/TRL/QLoRA/FastChat lineage | Official acknowledgements | High |

## 4. Supported model families

### LLM families (core supported)

**English-primary:**
- **LLaMA 1/2/3/3.1/3.2/3.3** (Meta) — foundation model of framework name
- **Mistral 7B / Mixtral 8×7B / Mixtral 8×22B / Mistral Large** (Mistral AI)
- **Gemma 2 / Gemma 3** (Google)
- **Phi-3 / Phi-3.5** (Microsoft)
- **Falcon 7B / 40B / 180B** (TII)

**CN-primary:**
- **Qwen 1.5 / 2 / 2.5 / 3** (Alibaba) — broadest CN-family support
- **DeepSeek V2 / V3 / R1** (DeepSeek AI)
- **GLM 4 / GLM 5** (ZhipuAI)
- **InternLM 2 / 2.5 / 3** (InternLM)
- **MiniCPM 1 / 2 / 3** (ModelBest)

**Other:**
- **Gemma, Phi, Mixtral-MoE, Falcon, Command R, StableLM, Orion, Yi, XVERSE, Baichuan 2, ...**

**90+ additional model families** via community contributions.

### VLM families (vision-language)

- **LLaVA 1.5 / 1.6 / NeXT** (multi-modal)
- **Qwen-VL / Qwen2-VL / Qwen2.5-VL**
- **InternVL 2 / 3**
- **MiniCPM-V 2 / 2.5**
- **Phi-3.5-vision**
- **Gemma 3 (multi-modal)**

### Why 100+ matters

**Community contribution model:** As new LLM families release, community adds fine-tuning config. LlamaFactory becomes de-facto standard for fine-tuning support on day-of-release.

**Cross-corpus comparison:**

| Wiki | Model breadth |
|------|---------------|
| ECC v1 | 1 (Claude Code) |
| fish-speech v20 | 1 foundation model |
| TrendRadar v19 | 100+ inference providers (via LiteLLM) |
| **LlamaFactory v22** | **100+ training targets (first in corpus)** |

## 5. 9 training stages unified

### Stage 1: Pre-training

- **Purpose:** Train from random initialization
- **Use case:** Rare (resource-intensive)
- **Support:** Yes, but requires massive compute + data

### Stage 2: Supervised Fine-Tuning (SFT)

- **Purpose:** Adapt pretrained model to task/instruction-following
- **Use case:** Most common starting point
- **Dataset format:** Instruction-response pairs

### Stage 3: Reward Modeling

- **Purpose:** Train reward model on human preferences
- **Use case:** Precursor to PPO RLHF
- **Dataset:** Preference pairs (chosen vs rejected responses)

### Stage 4: PPO (Proximal Policy Optimization, 2017)

- **Purpose:** RL alignment using reward model
- **Use case:** Classical RLHF (OpenAI's InstructGPT method)
- **Complexity:** High (requires reward model + policy + reference model)

### Stage 5: DPO (Direct Preference Optimization, 2023)

- **Purpose:** RL alignment without reward model
- **Use case:** Simpler + stabler than PPO
- **Innovation:** Derives optimal policy directly from preferences

### Stage 6: KTO (Kahneman-Tversky Optimization, 2024)

- **Purpose:** RL alignment with prospect-theory framing
- **Use case:** Loss-aversion aware alignment
- **Innovation:** Doesn't require paired preferences (can use single-sample feedback)

### Stage 7: ORPO (Odds Ratio Preference Optimization, 2024)

- **Purpose:** Combined SFT + preference learning
- **Use case:** Single-stage alternative to SFT→DPO
- **Innovation:** Adds preference loss term to SFT

### Stage 8: SimPO (Simple Preference Optimization, 2024)

- **Purpose:** Reference-free preference optimization
- **Use case:** Simpler than DPO (no reference model)
- **Innovation:** Length-normalized reward

### Stage flow

Typical pipeline: Pre-train (optional) → SFT → RL alignment (pick 1 of 5 methods)

### Method progression (18 months of research)

| Method | Year | Adoption |
|--------|------|----------|
| PPO | 2017 | Mature |
| DPO | 2023 | Widely adopted |
| KTO | 2024 | Emerging |
| ORPO | 2024 | Emerging |
| SimPO | 2024 | Latest |

LlamaFactory ships all 5 simultaneously. Research-to-integration velocity competitive edge.

## 6. Broadest model support + comprehensive stages = "unified" positioning

### Fragmented alternative

Without LlamaFactory, fine-tuning workflow requires:
- **PEFT** for LoRA/QLoRA
- **TRL** for SFT + reward + PPO
- **QLoRA codebase** for quantization
- **FastChat** for SFT conventions
- **Custom glue code** to integrate

### Unified replacement

LlamaFactory consolidates all above into single framework with consistent:
- Configuration format
- CLI
- WebUI
- Dataset loaders
- Model loaders
- Evaluation

### Competitive advantage

**Time-to-first-training:**
- Fragmented: days (setup + glue code + debugging)
- LlamaFactory: minutes (CLI one-liner or WebUI click)

**Learning curve:**
- Fragmented: learn 4-5 frameworks
- LlamaFactory: learn 1 framework

## 7. CN + Western equal support (Pattern #18 regional neutrality)

### Regional model families

| Region | Models |
|--------|--------|
| Western | LLaMA, Mistral, Gemma, Phi, Falcon |
| **CN** | **Qwen, DeepSeek, GLM, InternLM, MiniCPM** |
| Other | Yi, XVERSE, Baichuan, Orion, etc. |

### Training-infrastructure regional neutrality

**Pattern #18 refinement v22:** Training infrastructure is regional-neutral. Unlike agent runtime identifiers (OpenClaw/Hermes — Western community-platform), training frameworks serve all ecosystems equally.

Reason: Training math is universal. Regional differences are at:
- Agent runtime (Western adopts OpenClaw/Hermes; CN uses direct MCP)
- Push channels (Slack vs WeChat)
- Hubs (HuggingFace + ModelScope/Modelers)

But training itself = universal.

## 8. VLM (Vision-Language Model) support

### Why VLM matters

Recent model progression: LLM → VLM (multi-modal). Fine-tuning VLMs requires:
- Image encoder + text encoder + cross-attention
- Multi-modal dataset format
- Different hyperparameters

**LlamaFactory includes VLM support** — not most fine-tuning frameworks do.

### VLM use cases

- **Custom vision-language agents** (image-aware assistants)
- **Document understanding** (PDF + chart + table analysis)
- **Medical imaging** (fine-tune for radiology)
- **Product image analysis**

## 9. Agent-adjacent feature: function-calling dataset support

Although LlamaFactory is training-infrastructure (outside Storm Bear agent-scope), it supports:

### Function-calling fine-tuning

- **Dataset format:** tool-use demonstrations
- **Use case:** Fine-tune model for specific tool/agent context
- **Output:** Agent-ready model

### Storm Bear implication

Operator could use LlamaFactory to train custom VN-language Scrum-coaching agent:
- Fine-tune Qwen2.5-7B on VN Scrum coaching demonstrations
- Add tool-use training for Jira/Linear integration
- Deploy via API for Scrum team assistance

## 10. Edges + failure modes

### Known limitations

- **Model compatibility lag** — newest models may take days-weeks to support
- **Memory surprises** — QLoRA + FSDP claims don't always hold (depends on sequence length)
- **Dataset quality** — framework doesn't guarantee data quality
- **Reward hacking in RLHF** — PPO can exploit reward model
- **Overfitting in LoRA** — small adapter size doesn't prevent overfitting
- **Catastrophic forgetting** — full-tuning may erase pretrained capabilities

### Configuration complexity

Despite unified framework, hyperparameter space is vast:
- Learning rate (typically 1e-5 to 5e-4)
- LoRA rank (typically 8-64)
- Training epochs
- Batch size
- Sequence length
- Gradient accumulation
- Warmup ratio
- Scheduler
- etc.

Expertise still required for good results.

## 11. Related concepts

- [[(C) Fine-Tuning Methods + Optimizer Research Integration]] — deeper method detail
- [[(C) Academic-Lab Archetype + Pattern 19 4th Archetype N=2 Validation]] — lineage + org
- [[(C) Outside-Scope 4th Sub-Type + Training-Infrastructure + Storm Bear]] — outside-scope framework
- Pattern #19 4th archetype — validates at N=2 via LlamaFactory
- Pattern #43 Optimizer-Research Integration Velocity — candidate formalized
- Parent: [[(C) index]]

## References

- README supported model list
- README training stages section
- arXiv 2403.13372 (ACL 2024)
- llamafactory.readthedocs.io

---

**100+ LLM/VLM families supported (broadest in corpus). 9 unified training stages: pre-train + SFT + reward modeling + 5 RL alignment (PPO/DPO/KTO/ORPO/SimPO). Replaces fragmented PEFT + TRL + QLoRA + FastChat tool chain. CN (Qwen/DeepSeek/GLM/InternLM/MiniCPM) + Western (LLaMA/Mistral/Gemma/Phi/Falcon) equal support — Pattern #18 training-infrastructure regional-neutral. VLM support enables multi-modal fine-tuning. Function-calling dataset support enables agent fine-tuning.**
