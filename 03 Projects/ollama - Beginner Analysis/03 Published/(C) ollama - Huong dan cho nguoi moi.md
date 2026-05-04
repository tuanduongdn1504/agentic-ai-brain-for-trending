# (C) Ollama — Hướng dẫn cho người mới / Beginner's Guide

> **Song ngữ VN + EN.** ~480 dòng, 12 phần. Dành cho Storm Bear operator (Scrum Coach, VN-based) muốn hiểu + đánh giá Ollama như một option cho workflow coaching.

---

## Phần 1 — Ollama là gì? / What is Ollama?

**VN:** Ollama là một **LLM inference runtime** — tức là một phần mềm chạy trên máy của bạn (Mac / Windows / Linux / Docker) và làm nhiệm vụ *phục vụ* các mô hình ngôn ngữ open-weight như Llama 3, Qwen, DeepSeek, Gemma, Kimi qua một REST API cục bộ tại `http://localhost:11434`. Nói ngắn gọn: nếu OpenAI/Anthropic là "cloud LLM", thì Ollama là cách đơn giản nhất để chạy LLM trên *máy của bạn*.

**EN:** Ollama is an **LLM inference runtime** — software that installs on your machine (Mac / Windows / Linux / Docker) and *serves* open-weight language models like Llama 3, Qwen, DeepSeek, Gemma, Kimi via a local REST API at `http://localhost:11434`. TL;DR: if OpenAI/Anthropic are "cloud LLM", Ollama is the simplest way to run LLM on *your own machine*.

**Một câu khẩu hiệu verbatim:**
> "Start building with open models." — README dòng 9

---

## Phần 2 — Tại sao Storm Bear operator nên biết về Ollama? / Why should Storm Bear operator care?

**3 use cases thực tế cho Scrum Coach context:**

1. **Privacy pilot (có tiềm năng MEDIUM):**
   - Khi làm việc với khách VN mà dữ liệu nhạy cảm (retro transcripts, personal-KPI, compensation data), chạy Llama 3 / Qwen3 locally tránh gửi data sang API của Anthropic/OpenAI.
   - Hạn chế: cần Mac có 64GB+ RAM cho model 30B; 8GB+ RAM cho model 7B.

2. **Cost-optimization pilot (LOW-MEDIUM):**
   - Workload Scrum coaching nhiều token: Claude API cost $$
   - Ollama local = free sau khi đã mua hardware
   - Hoặc Ollama Cloud Pro $20/mo (tương đương Claude Code subscription cho light usage), Max $100/mo (nếu hardware local không đủ)

3. **Claude Code integration pilot (LOW):**
   - `ollama launch claude --model qwen3.5` — Claude Code binary dùng Ollama-served model qua Anthropic-compat API → không cần Anthropic API key.
   - Trade-off: open-weight models kém Claude Sonnet/Opus về reasoning, nhưng context window có thể lớn hơn (Qwen / Kimi support tới 200K+).

**Kết luận:** Ollama **KHÔNG phải top-priority pilot** cho Storm Bear (không lọt top-11 pilot ranking). Nhưng đáng biết nếu:
- Có engagement với khách yêu cầu on-premise / data sovereignty (VN enterprise)
- Muốn thử nghiệm Claude Code với open models (tiết kiệm chi phí test)
- Quan tâm pattern "local-first infrastructure" như reference architecture

---

## Phần 3 — Cài đặt / Installation

**macOS + Linux (curl một dòng):**
```shell
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows (PowerShell):**
```powershell
irm https://ollama.com/install.ps1 | iex
```

**Docker:**
```shell
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

**Homebrew (macOS alternative):**
```shell
brew install ollama
```

**Kiểm tra:**
```shell
ollama --version
# → ollama version is 0.21.2 (hoặc version mới hơn)
```

---

## Phần 4 — Chạy model đầu tiên / Run your first model

```shell
# Chạy model Gemma 3 (từ Google) — ~4 GB download
ollama run gemma3
```

Ollama sẽ:
1. Download model weights từ `ollama.com/library` (lần đầu)
2. Load model vào memory
3. Mở REPL chat để bạn nói chuyện với model

**Ví dụ conversation:**
```
>>> Scrum team 5 người, velocity 20 points/sprint, có 100 points backlog. Khi nào xong?
[Gemma 3 response...]

>>> /bye
```

**Các model phổ biến khác để thử:**
```shell
ollama run llama3.2             # Meta Llama 3.2 (nhẹ, ~2 GB)
ollama run qwen3-coder          # Alibaba Qwen3-Coder (coding specialized)
ollama run deepseek-r1          # DeepSeek R1 (reasoning)
ollama run mixtral              # Mistral Mixtral (MoE architecture)
```

Xem đầy đủ tại: https://ollama.com/library

---

## Phần 5 — REST API cơ bản / Basic REST API

Khi Ollama chạy (tự động khi bạn `ollama run`), nó serve REST API tại `http://localhost:11434`.

**Native API:**
```shell
curl http://localhost:11434/api/chat -d '{
  "model": "gemma3",
  "messages": [
    {"role": "user", "content": "Viết 3 user stories cho sprint planning meeting."}
  ],
  "stream": false
}'
```

**OpenAI-compatible API** (dùng với LangChain, LiteLLM, any-llm, vv.):
```shell
curl http://localhost:11434/v1/chat/completions -d '{
  "model": "gemma3",
  "messages": [{"role": "user", "content": "Hello"}]
}'
# base_url: http://localhost:11434/v1
# API key: ollama (hoặc bỏ trống)
```

**Anthropic-compatible API** (dùng với Claude Code):
```shell
# Trong terminal:
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434
claude --model qwen3.5
# → Claude Code binary giờ dùng Qwen3 model qua Ollama
```

**Python SDK:**
```shell
pip install ollama
```

```python
from ollama import chat
response = chat(model='gemma3', messages=[
    {'role': 'user', 'content': 'Giải thích Daily Scrum trong 1 câu.'}
])
print(response.message.content)
```

**JavaScript SDK:**
```shell
npm i ollama
```

```javascript
import ollama from "ollama";
const response = await ollama.chat({
  model: "gemma3",
  messages: [{role: "user", content: "Sprint velocity là gì?"}],
});
console.log(response.message.content);
```

---

## Phần 6 — Ollama Cloud (commercial tier)

Nếu hardware của bạn không đủ cho model lớn (30B+ parameters), Ollama Cloud cho phép chạy trên datacenter GPU của Ollama Inc.

**3 tiers:**
- **Free với account** — có sẵn cloud models cơ bản khi signup
- **Pro $20/mo** (hoặc $200/yr) — chạy 3 cloud models cùng lúc, 50× usage vs Free
- **Max $100/mo** — chạy 10 cloud models, 5× usage vs Pro

**Cách dùng:**
```shell
ollama signin        # tạo account ollama.com
ollama run kimi-k2.5:cloud    # note: :cloud suffix = chạy trên Ollama Cloud
```

Same CLI / API như local — chỉ khác suffix model name. Đây là cách Ollama upsell commercial tier (Pattern #50 corpus).

**Models cloud phổ biến:**
- `kimi-k2.5:cloud` — Moonshot (multimodal reasoning)
- `glm-5:cloud`, `glm-5.1:cloud` — Zhipu (code + reasoning)
- `qwen3.5:cloud` — Alibaba (general + vision)
- `minimax-m2.7:cloud` — fast coding

---

## Phần 7 — Modelfile: tạo model tùy chỉnh / Create custom model

Ollama dùng **Modelfile** — một file declarative format giống Dockerfile — để bundle: base model + template + system prompt + parameters + optional LoRA adapter.

**Ví dụ Modelfile cho Storm Bear Scrum Coach agent:**

```modelfile
FROM qwen3-coder

PARAMETER temperature 0.3
PARAMETER num_ctx 65536

SYSTEM """
Bạn là một Scrum Coach chuyên nghiệp làm việc cho Storm Bear.

Nguyên tắc:
- Luôn hỏi về team context trước khi đề xuất solution
- Tôn trọng Scrum framework nhưng thực dụng khi adapt
- Song ngữ VN+EN — user VN-speaker, ghi chú technical EN

Không làm:
- Không đưa ra advice generic như "Agile coach tool"
- Không bỏ qua cultural context VN work environment
"""
```

Build:
```shell
ollama create storm-bear-scrum -f Modelfile
ollama run storm-bear-scrum
```

Xong — bây giờ bạn có một agent custom chạy local / cloud với personality Storm Bear.

---

## Phần 8 — `ollama launch <runtime>`: magic integration

Tính năng **corpus-first** của Ollama (trong Storm Bear corpus v46): `ollama launch <runtime>` tự động install + configure + start các agent runtimes phổ biến.

**10+ runtimes được bundle:**

```shell
ollama launch claude       # Claude Code (qua Anthropic-compat)
ollama launch codex        # OpenAI Codex CLI
ollama launch copilot      # GitHub Copilot CLI
ollama launch opencode     # OpenCode
ollama launch droid        # Factory.ai Droid
ollama launch goose        # Block Goose
ollama launch pi           # Pi (pi-mono, từ Mario Zechner — wiki v36)
ollama launch openclaw     # OpenClaw (WhatsApp/Telegram/Slack/Discord AI assistant)
ollama launch hermes       # Hermes Agent
```

Example workflow:
```shell
ollama launch claude --model qwen3.5:cloud
# → Auto: cài Claude Code nếu chưa có
# → Auto: set ANTHROPIC_BASE_URL=http://localhost:11434
# → Auto: pull qwen3.5:cloud model
# → Drop vào Claude Code session với Qwen3
```

Đây là **Pattern #18 Layer 0** trong Storm Bear corpus — Ollama introduces "runtime-bundled-agent-launcher" như primitive mới ở mức infrastructure-runtime. 10+ agent runtimes đều có launcher riêng trong `cmd/launch/` (33 files total).

---

## Phần 9 — So sánh với các corpus wikis khác / Comparison with other corpus wikis

| Project | Tier | Vai trò đối với LLM | So với Ollama |
|---------|------|----------------------|-----------------|
| **Ollama v46** | Outside-scope runtime (NEW 9th sub-type) | **Chạy inference** model đã train | — |
| fish-speech v20 | Outside-scope foundation-model | **Tạo model weights** (TTS) | Ollama consume weights do fish-speech tạo |
| LlamaFactory v22 | Outside-scope training-infra | **Train model weights** | Ollama run model do LlamaFactory train |
| Unsloth v23 | Outside-scope training-infra | Train + fine-tune | Same as LlamaFactory |
| magika v44 | Outside-scope ML-security-classifier | Classify file types | Khác domain hoàn toàn |
| browser-use v41 | T5 agent-as-application | Browser automation agent | browser-use CÓ THỂ dùng Ollama as LLM backend |
| pi-mono v36 | T1 agent-as-assistant | Coding agent CLI | Pi có thể dùng Ollama — `ollama launch pi` |

**Ollama là runtime layer mà 11+ frameworks trong corpus có thể consume:**
- LiteLLM (treats Ollama as provider)
- LangChain (7 ngôn ngữ - Python/JS/4j/Go/Rust/Dart/.NET)
- LlamaIndex
- Microsoft Semantic Kernel
- Google Firebase Genkit
- AWS Strands Agents
- Mozilla any-llm
- Portkey, Haystack, crewAI, AutoGPT, ...

Đây gọi là **Pattern #28 structural inversion** — Ollama đảo ngược pattern thông thường. Các framework khác support multi-provider; Ollama LÀ provider bị support.

---

## Phần 10 — Governance + commercial model

**License:** MIT (permissive)

**Commercial entity:** Ollama, Inc. (founders không public)

**Commercial tier:** Ollama Cloud Pro $20/mo + Max $100/mo. Đây là Pattern #31 Open-Core thứ 9 trong corpus (sau fish-speech / Skyvern / crawl4ai / OpenHands / GitNexus / browser-use / ruflo / shannon / ollama).

**Governance discipline mạnh:**

CONTRIBUTING.md nói thẳng:
> "Changes that break backwards compatibility in Ollama's API (including the OpenAI-compatible API) [may not be accepted]"

> "New features... add surface area to Ollama and make it harder to maintain in the long run as they cannot be removed without potentially breaking users"

→ Đây là **commercial-runtime-infrastructure-stability archetype** — khi product của bạn là "stable API cho 130+ downstream tools", bạn không dám break anything. Storm Bear operator có thể học cách discipline này khi thiết kế interface cho clients.

---

## Phần 11 — 2-tuần roadmap đánh giá / 2-week evaluation roadmap

Nếu muốn serious evaluate Ollama cho Storm Bear context:

**Tuần 1 — Setup + baseline:**
- Day 1: Install Ollama + test `ollama run gemma3` trên Mac của bạn
- Day 2: Thử 3-4 models khác nhau (qwen3, llama3.2, deepseek-r1, mixtral) — đánh giá reasoning quality với câu hỏi Scrum coach thật
- Day 3: Setup Python SDK + viết script test gen user stories
- Day 4: Viết Modelfile custom cho Storm Bear Scrum Coach agent
- Day 5: Integration với Claude Code — `ollama launch claude --model qwen3.5`

**Tuần 2 — Deeper evaluation:**
- Day 6-7: So sánh output quality Ollama-Qwen3 vs Claude Sonnet cho:
  - Retro facilitation
  - User story splitting
  - Sprint planning estimation
  - Team health diagnostic
- Day 8: Thử Ollama Cloud Pro ($20/mo) với Kimi-K2.5 cho tasks cần reasoning sâu hơn
- Day 9: Privacy test — chạy hoàn toàn offline + verify không có network call ra ngoài localhost
- Day 10: Decision point — Ollama có add giá trị gì cho current Storm Bear workflow không?

**Budget:** $0-20 (Ollama local free; $20 nếu thử 1 tháng Cloud Pro)

**Expected outcome:** Có thể integration marginal-value cho privacy-sensitive clients. Không thay thế Claude API primary. **Observational > adoption.**

---

## Phần 12 — Rủi ro + hạn chế / Risks + Limitations

**Kỹ thuật:**
- Hardware requirement: 64GB+ RAM cho 30B models; 8-16GB cho 7B models
- Apple Silicon Mac work tốt (MLX backend vendored); Windows/Linux có llama.cpp CUDA/ROCm
- Model quality: Qwen3/Llama3/DeepSeek-R1 < Claude Sonnet cho reasoning tasks phức tạp
- Context window limits vary per model (Qwen3 support 200K+, Gemma ~32K)

**Business:**
- Ollama, Inc. founders opaque — bus factor chưa rõ
- 170K stars scale nhưng commercial viability chưa prove — Pro/Max tier còn mới
- EN-only docs — không có VN localization
- Backwards-compat discipline mạnh nhưng cũng có nghĩa feature velocity chậm

**Pháp lý + Ethical:**
- MIT license: clean, commercial-usable
- Model weights downloadable có license riêng: Llama 3 có Meta Custom License (có usage restrictions); Qwen có Alibaba license; DeepSeek MIT. **Check model license trước khi commercial use.**
- Khi chạy locally, toàn bộ inference là local — không có data leak ra Ollama Inc.
- Khi chạy Ollama Cloud (`:cloud` suffix), data đi qua Ollama Inc. servers — check Ollama's privacy policy.

**Cho Storm Bear VN context:**
- Kimi-K2.5 / GLM-5 / Qwen3 có CN-focus — có thể có bias hoặc content-filter policy khác với Western models. Test careful nếu dùng cho VN clients.

---

## Phần 13 — References + Bước tiếp theo / Next actions

**Tài liệu chính thức:**
- GitHub repo: https://github.com/ollama/ollama
- Docs site: https://docs.ollama.com
- Model library: https://ollama.com/library
- Pricing: https://ollama.com/pricing

**Community:**
- Discord: https://discord.gg/ollama
- Reddit: https://reddit.com/r/ollama
- X: https://x.com/ollama

**Sibling wiki cross-references:**
- v36 pi-mono — Pi coding agent có thể dùng Ollama via `ollama launch pi`
- v10 autoresearch-Karpathy — được Ollama Pi integration docs cite verbatim
- v20 fish-speech — outside-scope precedent (foundation-model vs inference-runtime)
- v22 LlamaFactory + v23 Unsloth — outside-scope precedent (training vs inference)
- v44 magika — outside-scope precedent (ML-classifier vs runtime)
- v45 shannon — Pattern #31 Open-Core precedent (N=8 → N=9 at v46)

**Bước tiếp theo cho Storm Bear operator:**

1. **Nếu có hardware Apple Silicon 64GB+** — install Ollama, thử 1 tuần với qwen3-coder cho coding tasks local
2. **Nếu không có hardware đủ** — skip hoặc chỉ Cloud Pro $20/mo thử 1 tháng
3. **Nếu chưa có use case cụ thể** — observational, skip; revisit khi có VN-client privacy requirement
4. **Observational value HIGH cho pattern reference** — commercial-runtime-infrastructure-stability governance model có thể áp dụng cho Storm Bear vault discipline

**Verdict:** Ollama = powerful runtime layer, nhưng Storm Bear workflow (markdown-vault + Scrum coaching) không depend critically vào local LLM infrastructure. Theo dõi observational; pilot khi có concrete need.

---

**Ghi chú:** Đây là wiki v46 trong Storm Bear corpus. 46 wikis → 10-streak zero-new-candidates (v37-v46 — longest streak in corpus). Pattern #47 conditional retirement trigger FIRES tại v46 → chờ mini-audit kế tiếp để cleanup. Pattern Library ratio preserved at 0.54:1 (UNPRECEDENTED 10th consecutive wiki).
