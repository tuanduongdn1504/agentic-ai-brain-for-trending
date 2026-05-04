# Unsloth — Hướng dẫn cho người mới / Beginner Guide

> **Dành cho:** Developer muốn fine-tune LLM nhanh hơn trên GPU consumer (RTX 3090/4090) — không đủ ngân sách thuê A100/H100.
> **Scope note:** Unsloth là **training infrastructure** (không phải agent framework). Storm Bear operator Scrum coach có thể không dùng trực tiếp — đọc phần "Khi nào bạn cần Unsloth" trước.

---

## 0. ⚠️ Đọc trước khi đi tiếp / Read this first

**VN:** Unsloth giải quyết vấn đề rất cụ thể: **fine-tuning LLM trên consumer GPU**. Nếu bạn:
- Chỉ dùng Claude API / ChatGPT / Gemini → **bạn KHÔNG cần Unsloth**
- Chỉ prompt-engineer agent workflows → **bạn KHÔNG cần Unsloth**
- Muốn tùy chỉnh model (LoRA / QLoRA / full fine-tune) với RTX 3090/4090 → **Unsloth là công cụ phù hợp**
- Đang thuê A100/H100 cluster → dùng LlamaFactory hoặc Megatron-LM, Unsloth vẫn OK nhưng không phải thế mạnh chính

**EN:** Unsloth solves a very specific problem: **fine-tuning LLMs on consumer GPUs**. Skip if you only use closed APIs or only do prompt engineering. Use if you want to customize models on RTX 3090/4090-class hardware.

---

## 1. Unsloth là gì? / What is Unsloth?

**VN:** Unsloth là framework fine-tuning mã nguồn mở do Daniel Han + Michael Han + đội Unsloth xây dựng (2023-11). Slogan: *"Train 500+ models up to 2× faster with up to 70% less VRAM, with no accuracy loss."*

Điểm nổi bật:
- **2× nhanh hơn** so với HuggingFace baseline
- **70% ít VRAM hơn** — nghĩa là model to hơn chạy trên GPU nhỏ hơn
- **500+ models hỗ trợ** — Gemma, Qwen, Llama, Mistral, Phi, DeepSeek, gpt-oss, v.v.
- **Không mất accuracy** — tối ưu ở tầng kernel (Triton), không phải thuật toán cắt xén
- **Unsloth Studio** — WebUI để fine-tune không cần code

**EN:** Unsloth is an open-source fine-tuning framework by Daniel + Michael Han (likely brothers) + team. Headline: 2× faster + 70% less VRAM via custom Triton kernels, 500+ models supported, no accuracy loss. Studio WebUI for non-coders (AGPL-3.0 separate from Apache core).

## 2. So với LlamaFactory / vs LlamaFactory

**VN:** Nếu bạn đã biết LlamaFactory (Pattern #41 peer của Unsloth):

| Khía cạnh | LlamaFactory | Unsloth |
|-----------|--------------|---------|
| Positioning | Nền tảng thống nhất mọi thứ | Performance-first (tốc độ + bộ nhớ) |
| Model count | 100+ families | 500+ variants |
| Hardware | Consumer + enterprise + CN (NPU) | Consumer-first (RTX primary) |
| Custom kernels | Dùng Liger | **Custom RoPE + MLP Triton** |
| Publication | ACL 2024 | Không có |
| License | Apache-2.0 | **Dual: Apache (core) + AGPL (Studio UI)** |
| Archetype | Academic lab (Lab4AI) | Duo-founder (Han brothers) |
| Relationship | **Dùng Unsloth như performance library** | **Provides performance upstream** |

**Quan hệ:** LlamaFactory dùng Unsloth như thư viện tăng tốc. Hai dự án **bổ sung** chứ không cạnh tranh trực tiếp — Unsloth là upstream, LlamaFactory là downstream platform.

**EN:** LlamaFactory is a unified platform that embeds Unsloth as a performance library. Complementary, not competing. Unsloth = upstream performance provider; LlamaFactory = downstream unified platform.

## 3. Khi nào bạn cần Unsloth / When you need Unsloth

**Bạn CẦN Unsloth khi:**
- ✅ Fine-tune Llama-3.1-8B QLoRA trên RTX 3090 (24GB) — với Unsloth: ~45 phút; với HF baseline: ~90 phút
- ✅ Fine-tune Qwen2.5-7B LoRA trên RTX 4090 — ~30 phút Unsloth vs ~60 phút HF
- ✅ Thử nghiệm GRPO RL alignment trên consumer GPU (80% less VRAM)
- ✅ Train MoE model (Mixtral, DeepSeek V2/V3) với 12× faster
- ✅ Long-context RL (7× longer context)
- ✅ Train trên M-series Mac (sắp có MLX)

**Bạn KHÔNG cần Unsloth khi:**
- ❌ Chỉ dùng API-only LLM
- ❌ Cần đào tạo from-scratch quy mô >70B (dùng Megatron-LM / NeMo)
- ❌ Cần support NPU (Ascend) — dùng LlamaFactory NPU variant
- ❌ Nghiên cứu academic với kernel PhD-level customization (dùng raw PyTorch)

## 4. Cài đặt / Installation

### 4.1 Google Colab (dễ nhất)

Unsloth có starter notebooks cho:
- Llama 3.1 / 3.2
- Qwen 2.5 / 3.5
- Gemma 4
- gpt-oss GRPO
- embedding models

Mở Colab notebook chính thức từ README → Run All → có model fine-tuned sau ~30 phút.

### 4.2 Local pip install

```bash
pip install unsloth
```

Yêu cầu:
- NVIDIA GPU (RTX 30/40/50 hoặc A100/H100)
- CUDA 12.x
- Python 3.10+
- PyTorch 2.x

### 4.3 Docker

```bash
docker pull unsloth/unsloth
docker run --gpus all -v $PWD:/workspace unsloth/unsloth
```

### 4.4 Unsloth Studio WebUI

```bash
pip install unsloth
unsloth studio
```

Mở `http://localhost:7860` → point-and-click fine-tuning.

**Lưu ý license:** Unsloth Studio là **AGPL-3.0** (khác với core Apache-2.0). Nếu bạn deploy Studio như SaaS, phải công bố mã nguồn cho users theo AGPL terms.

## 5. Quick start — Fine-tune Llama 3.1 8B với LoRA

```python
from unsloth import FastLanguageModel
import torch

# Load model (4-bit quantized)
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Meta-Llama-3.1-8B-bnb-4bit",
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=True,
)

# Add LoRA adapters
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj","k_proj","v_proj","o_proj",
                    "gate_proj","up_proj","down_proj"],
    lora_alpha=16,
    lora_dropout=0,
    bias="none",
    use_gradient_checkpointing="unsloth",  # 30% less VRAM
)

# Training (use TRL SFTTrainer)
from trl import SFTTrainer
from transformers import TrainingArguments

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=your_dataset,
    dataset_text_field="text",
    max_seq_length=2048,
    args=TrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        warmup_steps=5,
        max_steps=60,
        learning_rate=2e-4,
        fp16=not torch.cuda.is_bf16_supported(),
        bf16=torch.cuda.is_bf16_supported(),
        logging_steps=1,
        optim="adamw_8bit",
        output_dir="outputs",
    ),
)

trainer.train()
```

Trên RTX 4090: ~30 phút cho 60 steps với small dataset.

## 6. Kỹ thuật đằng sau / Under the hood

### 6.1 Custom Triton kernels

Unsloth viết lại 2 kernel quan trọng bằng OpenAI Triton:
- **RoPE (Rotary Position Embedding)** — xử lý attention position
- **MLP (Feedforward)** — fused operations

Kết quả: ~2× speedup so với PyTorch native.

### 6.2 Padding-free packing

3× nhanh hơn + 30% less VRAM. Pack nhiều sequence ngắn vào một batch mà không để attention "leak" giữa sequences.

### 6.3 GRPO RL alignment

Group Relative Policy Optimization — phương pháp RL alignment từ DeepSeek-R1. Unsloth tối ưu để 80% less VRAM, làm RL alignment khả thi trên consumer GPU.

### 6.4 FP8 training

8-bit floating point — cần H100/H200/RTX 50. Unsloth là framework đầu tiên trong corpus Storm Bear nhắc đến FP8.

### 6.5 MLX (sắp có)

Apple Silicon training qua MLX framework — lần đầu tiên trong corpus có framework nhắc Apple M-series training.

## 7. Hardware matrix / Ma trận phần cứng

| Hardware | Unsloth support |
|----------|-----------------|
| NVIDIA RTX 30 / 40 / 50 | ✅ Primary |
| NVIDIA Blackwell | ✅ |
| NVIDIA A100 / H100 / H200 | ✅ |
| NVIDIA DGX (multi-GPU) | ✅ |
| AMD Instinct | Chat/data only; training via Core |
| Intel GPU | Giới hạn |
| Apple Silicon (MLX) | Sắp có |
| macOS CPU | Chat only |

**Positioning:** Consumer-first. Nếu bạn chạy A100/H100 enterprise tier, cân nhắc LlamaFactory hoặc Megatron-LM.

## 8. Ecosystem / Hệ sinh thái

- **Discord** — primary technical community
- **Reddit r/unsloth** — first subreddit community trong corpus Storm Bear
- **X @unslothai** — announcements + performance updates
- **GitHub** — 62.2K stars, #8 trong corpus
- **Docs** — unsloth.ai/docs

## 9. Lộ trình 4 tuần / 4-week roadmap

### Tuần 1 — Orient

- [ ] Đọc README + cluster summary wiki ngày 1
- [ ] Mở Colab notebook Llama 3.1 8B → Run All → quan sát fine-tuning hoàn thành
- [ ] Hiểu LoRA rank, alpha, target_modules
- [ ] Kiểm tra GPU setup (RTX 3090/4090 khuyến nghị)

### Tuần 2 — First fine-tune

- [ ] Chuẩn bị dataset tự tạo (JSON/CSV với instruction + response)
- [ ] Fine-tune Qwen2.5-7B LoRA trên dataset nhỏ (100-1000 samples)
- [ ] Đánh giá output qualitative
- [ ] Lưu + load lại adapter

### Tuần 3 — Production considerations

- [ ] Scale dataset lên 10K+ samples
- [ ] Thử QLoRA (4-bit) — nếu GPU không đủ VRAM
- [ ] Experiment với hyperparameters (lr, batch size, rank)
- [ ] Quantization cho inference (GGUF export)

### Tuần 4 — Advanced

- [ ] Thử GRPO nếu có reward model / dataset
- [ ] Thử Unsloth Studio WebUI
- [ ] Đọc về custom Triton kernel (nếu cần optimization sâu)
- [ ] Evaluate vs LlamaFactory nếu cần full platform

## 10. Storm Bear operator relevance / Mức độ phù hợp cho Storm Bear

**VN:** Storm Bear operator là Scrum coach + software developer. Unsloth là **outside-scope** cho vault:
- Không fine-tune LLM (dùng Claude API)
- Không cần consumer-GPU training workflow
- Không build agent framework

**Giá trị quan sát (không phải adopt):**
1. **Dual-licensing strategy** (Apache core + AGPL UI) — reference nếu Storm Bear publish tooling sau này
2. **Duo-founder archetype** — khả năng tổ chức cho team OSS nhỏ (không solo, không LLC)
3. **Performance-first positioning** — ngược với Storm Bear's knowledge-architecture-first
4. **Pattern validation value** — v23 wiki validates Pattern #41 + #43 = pay off của 3 wiki trước

**Direct action: KHÔNG có.** Wiki này là asset tham chiếu cho pattern library, không phải roadmap implementation.

**EN:** Unsloth is outside-scope for Storm Bear (Scrum coach, no fine-tuning workflow). Value is observational (dual-licensing + duo-founder archetype + positioning spectrum) + pattern validation (promotes #41 + #43 to confirmed). No direct adoption.

## 11. Next actions

**Nếu bạn là developer muốn fine-tune:**
1. Mở Colab notebook Llama 3.1 8B ngay hôm nay → 30 phút để có fine-tuned model đầu tiên
2. Sau đó thử với dataset của bạn

**Nếu bạn là Storm Bear operator (Scrum coach):**
1. Wiki này = pattern library asset, đọc xong → quay lại vault governance
2. Track Pattern #45 (dual-licensing) + #46 (duo-founder) nếu gặp framework tương tự

**Nếu bạn quan tâm training infrastructure:**
1. Đọc wiki LlamaFactory v22 song song (peer framework, Pattern #41 co-validator)
2. So sánh positioning: performance-first (Unsloth) vs unified-platform (LlamaFactory)

## 12. References

- Unsloth GitHub: github.com/unslothai/unsloth
- Docs: unsloth.ai/docs
- Discord: (in README)
- Reddit: r/unsloth
- Sibling wiki: LlamaFactory - Beginner Analysis v22

---

**Unsloth = performance-first training infrastructure (2× faster / 70% less VRAM). 500+ models, consumer-GPU focus, dual-licensing (Apache core + AGPL Studio), duo-founder archetype (Han brothers). Use if fine-tuning on consumer GPU. Skip if API-only or enterprise-scale. Storm Bear: observational value only.**
