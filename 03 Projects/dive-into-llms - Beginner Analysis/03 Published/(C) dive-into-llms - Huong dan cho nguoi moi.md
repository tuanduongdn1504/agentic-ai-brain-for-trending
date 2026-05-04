# (C) dive-into-llms — Hướng dẫn cho người mới / Beginner Guide

> **Repo:** `Lordog/dive-into-llms` — 《动手学大模型》系列编程实践教程
> **Scale:** 34,000⭐ / 4,200🍴 / Jupyter Notebook 100% / NO LICENSE / v0.1.0 / actively maintained (pushed 2026-04-15)
> **Author:** SJTU BCMI Lab (Zhang Zuosheng / 张倬胜) + 多国多机构 consortium (SJTU + NUS + Huawei Ascend)
> **Tier:** T3 Agent-as-education (3rd T3 entrant in Storm Bear corpus)
> **Bilingual:** VN primary + EN technical
> **Length:** ~500 lines, 12 parts

---

## ⚠️ Đọc phần này trước / Read this first

**Dive-into-llms là tài liệu học thuật CN-primary** (中文), **KHÔNG có file LICENSE** — nghĩa là bạn:

✅ **Được phép:** đọc, học, tham khảo cá nhân, trích dẫn (citation) cho học thuật

❌ **KHÔNG được phép:** fork + sửa + phân phối lại, dịch + xuất bản lại, dùng thương mại (kể cả có attribution), hoặc tạo tác phẩm phái sinh mà không xin phép tác giả

**Mặc định copyright áp dụng** (theo công ước Berne + luật IP Trung Quốc). Nếu muốn dùng content cho mục đích khác (ví dụ: Storm Bear muốn dịch VN + xuất bản), hãy **liên hệ Zhang Zuosheng** qua trang SJTU BCMI để xin phép trước.

**This tutorial is CN-primary academic material with NO LICENSE file** — which means you can read/study/cite personally BUT cannot legally fork/redistribute/adapt without author permission. Default copyright applies. Contact Zhang Zuosheng via SJTU BCMI if you want to adapt content.

---

## 1. Đây là gì? / What is it?

**VN:** *Dive into LLMs* là chuỗi tutorial học thuật thực hành về mô hình ngôn ngữ lớn (LLM), do **Đại học Giao Thông Thượng Hải (SJTU)** xuất phát từ 2 khóa học:
- **NIS8021** "Công nghệ tiên tiến Xử lý ngôn ngữ tự nhiên"
- **NIS3353** "Công nghệ bảo mật AI"

Giảng viên đầu ngành: **Zhang Zuosheng** (张倬胜) của BCMI Lab. Tutorial được mở rộng từ giáo trình lớp học thành tài liệu công cộng miễn phí (公益 / public-welfare).

Repo chứa **11 chương**, mỗi chương có **3 thành phần**: README (hướng dẫn) + slide PDF (2-11 MB) + Jupyter notebook (thực thi code).

**EN:** *Dive into LLMs* is an academic hands-on tutorial series on Large Language Models, originated at **Shanghai Jiao Tong University (SJTU)** from 2 courses (NIS8021 NLP Frontier + NIS3353 AI Security) taught by **Zhang Zuosheng** of BCMI Lab. It was expanded from classroom handouts into free public-welfare material. The repo has **11 chapters**, each with **3 deliverables**: README tutorial + PDF slides (2-11 MB) + Jupyter notebook.

## 2. Tín hiệu corpus-first / Corpus-first signals at v39

Trong Storm Bear corpus (39 wiki tổng cộng), dive-into-llms là:

1. **T3 entrant thứ 3** (sau Microsoft v6 + HF agents-course v26) — đóng T3 với N=3 + 100% archetype-diversity
2. **T3 CN-primary đầu tiên** trong corpus (2 T3 trước là EN-primary)
3. **T3 academic-course-lineage đầu tiên** (sub-archetype mới; khác big-tech-corporate Microsoft + commercial-ecosystem-platform HuggingFace)
4. **T3 multi-institutional-consortium đầu tiên** (SJTU + NUS + Huawei; khác 2 T3 trước đều single-institution)
5. **T3 với PDF-slides-per-chapter đầu tiên** (format phân phối mới ở tier này)
6. **Wiki corpus thứ 2 không có LICENSE** (sau v37 bizos) — củng cố Pattern #29 License-Category absent-LICENSE sub-category ở N=2
7. **Data point thứ 4 cho Pattern #44 Academic-Lab Affiliation** (Lab4AI + UIUC+CMU + HKU + **SJTU BCMI**); đồng thời là **sub-variant mới "multi-institutional-consortium-with-industry-partner"**
8. **Cross-corpus citation externally-originated đầu tiên** — chapter 9 GUI Agent verbatim cite `LLaMa-Factory` (chủ đề của v22 wiki!) cho việc fine-tune Qwen2-VL-7B trên OS-Kairos dataset
9. **Partnership corporate-community của Huawei Ascend đầu tiên** trong corpus (khác với Pattern #17 variant đã biết)
10. **Framing 公益 (public-welfare) + 国产化 (national-substitution)** — CN-tech-policy-context cụ thể, corpus-first

## 3. Vị trí trong 5-tier taxonomy / Tier placement

**Tier 3 Agent-as-education** — tutorial dạy con người về LLM + AI security + đôi chút agent-space. Khác với:
- **Tier 1** (Agent-as-assistant): Claude Code + spec-kit + codymaster v.v. — giúp bạn code với AI
- **Tier 4** (Agent-as-bridge): gws + notebooklm-py + crawl4ai — kết nối agents với thế giới
- **Tier 5** (Agent-as-application): OpenHands + DeepTutor — standalone agent app

Dive-into-llms focus vào **nền tảng lý thuyết + thực hành ML/DL/LLM**, không phải agent-framework hay runtime. Nếu bạn muốn hiểu "làm sao LLM được train, fine-tune, align, đánh giá, và bị tấn công" — T3 là tier đúng.

## 4. Cài đặt + chạy thử / Installation + quick start

### Prerequisites

- **Python 3.9+** (Python 3.8 đủ cho nhiều chương nhưng 3.9+ ổn định)
- **PyTorch** + **Transformers** + **Datasets** (các thư viện HF ecosystem)
- **Jupyter Notebook** hoặc JupyterLab
- **GPU** — tùy chương (xem bảng mục 5)
- **Nền tảng:** Linux preferred (một số chương như 4, 9 có requirements Linux-specific); macOS + Windows khả thi cho các chương nhẹ hơn

### Clone + điều hướng

```bash
git clone https://github.com/Lordog/dive-into-llms.git
cd dive-into-llms/documents/chapter1   # hoặc chapter-N bạn muốn bắt đầu

# Đọc slide trước (PDF)
open dive-into-llm.pdf                  # hoặc evince / mupdf trên Linux

# Đọc tutorial walkthrough
cat README.md | less

# Chạy notebook
jupyter notebook dive-tuning.ipynb
```

### Thiết lập môi trường Python (Chapter 1 ví dụ)

```bash
conda create -n llm python=3.9
conda activate llm

# Nếu network CN-optimal:
pip install transformers -i https://pypi.tuna.tsinghua.edu.cn/simple

# Nếu network Western:
pip install transformers torch datasets jupyter gradio

# Cho chapter 11 (RLHF):
pip install trl
```

### HuggingFace mirror cho VN / CN users

Nhiều chương download model + dataset từ HuggingFace. Nếu tốc độ chậm hoặc bị chặn:

```bash
export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download --resume-download <model-id>
```

## 5. Yêu cầu GPU theo từng chương / GPU requirements by chapter

| Ch | Chủ đề | GPU tối thiểu | Chi phí cloud ước lượng |
|----|--------|---------------|--------------------------|
| 1 | Fine-tuning + deployment | 8-16 GB (RTX 3090/4090 OK) | Miễn phí local |
| 2 | Prompting + CoT | N/A (API) | $5-20 cho API calls |
| 3 | Knowledge editing | 8-16 GB | Miễn phí local |
| 4 | Math reasoning + distillation | **≥40 GB** | $5-15 cho A100 1-hour rental |
| 5 | Watermark | 8-16 GB | Miễn phí local |
| 6 | Jailbreak | 8-16 GB | Miễn phí local |
| 7 | Steganography | 16-24 GB | Miễn phí local |
| 8 | Multimodal | 24-40 GB | $10-20 cloud rental |
| 9 | GUI Agent | **3× 80 GB A100** | $50-100 multi-GPU cloud |
| 10 | Agent safety | 16-24 GB | Miễn phí local |
| 11 | RLHF | 16-24 GB | Miễn phí local |

**Tổng chi phí để hoàn thành 11 chương:** ~$100-200 USD (nếu không có access GPU cụm). Tier A (8 chương) hoàn toàn local trên RTX 4090.

## 6. Curriculum structure — 11 chương / 4 clusters

### Cluster A — Nền tảng (Foundations): Chapters 1-2

- **Ch1 Fine-tuning + deployment:** BERT + Transformers + Gradio Spaces. Đây là entry point cho người mới. Fake-news classification task với Kaggle dataset.
- **Ch2 Prompting + CoT:** Multi-provider API (Qwen DashScope / Zhipu AI / Baidu Wenxin / OpenAI). Zero-shot + few-shot + Chain-of-Thought reasoning.

### Cluster B — Bảo mật + Alignment: Chapters 3, 5, 6, 10, 11 (5 chương — cluster lớn nhất)

- **Ch3 Knowledge editing:** Sửa "ký ức" của model (ROME, MEMIT style methods)
- **Ch5 Watermarking:** Nhúng watermark vào text LLM sinh ra
- **Ch6 Jailbreak attacks:** "Muốn bảo mật tốt hơn, hãy học tấn công trước" — security offense for safety research
- **Ch10 Agent safety:** Agent trong môi trường mở có nhận biết rủi ro không?
- **Ch11 RLHF + PPO:** Tutorial "rất nguy hiểm" — dùng TRL + GPT-2 + BERT reward trên IMDB sentiment data

Cluster này dominant vì **NIS3353 AI Security Technology** là 1 trong 2 course origin.

### Cluster C — Kiến trúc nâng cao: Chapters 4, 7, 8

- **Ch4 Math reasoning:** Distill DeepSeek-R1 → Qwen2.5-Math-1.5B qua SFT trên DeepMath-103K. Notebook **73.7 KB (lớn nhất)**; workflow end-to-end complete.
- **Ch7 Steganography:** "Mực tàng hình" — ẩn thông tin chỉ "người nhà" nhận ra trong output LLM
- **Ch8 Multimodal:** MLLM reasoning + generation; có giúp đạt AGI không?

### Cluster D — Agents: Chapters 9-10

- **Ch9 GUI Agent:** Qwen2-VL-7B + **LLaMa-Factory** (🔗 cross-corpus citation đến Storm Bear v22 wiki!) + OS-Kairos dataset → build adaptive human-AI-interaction GUI agent
- **Ch10 Agent safety:** paired với ch9

Cluster này thêm vào 2025/06 — reflect agent-era frontier.

## 7. Cross-corpus discovery cho độc giả Storm Bear

Khi đọc chapter 9 GUI Agent, bạn sẽ thấy:

> 本教程采用LLaMa-Factory对Qwen2-VL-7B进行有监督微调 (Tutorial này dùng LLaMa-Factory để SFT Qwen2-VL-7B)

**LLaMa-Factory = chủ đề của Storm Bear wiki v22!** (outside-scope training-infrastructure, ACL 2024, academic-lab Lab4AI).

**Ý nghĩa:**
- SJTU **không biết** về Storm Bear corpus — họ cite LLaMa-Factory vì nó là tool genuinely-upstream hữu ích
- Đây là **validation externally-originated** cho việc Storm Bear wiki-subject selection chuẩn
- Nếu bạn đã đọc v22 Storm Bear wiki về LLaMa-Factory, bạn hiểu tool này sâu hơn khi dùng trong ch9

## 8. So sánh với các T3 wiki khác / Compare to other T3 Storm Bear wikis

| Dimension | Microsoft v6 | HF agents-course v26 | **dive-into-llms v39** |
|-----------|--------------|-----------------------|-------------------------|
| Ngôn ngữ chính | EN | EN | **CN 🆕** |
| Tổ chức | Microsoft (big-tech-corporate) | HuggingFace (commercial-ecosystem-platform) | **SJTU BCMI + NUS + Huawei (multi-institutional-consortium) 🆕** |
| Origin | Azure ecosystem strategy | HF platform teaching + multi-framework BYO | **SJTU course handouts (NIS8021 + NIS3353) 🆕** |
| Cấu trúc | 10 + 4 + 4 bài học (horizontal) | 4 unit + bonus (vertical framework-scoped) | **11 chương (topic-scoped) 🆕** |
| Chứng chỉ | Không formal | Unit 4 leaderboard | Không (academic-only) |
| LICENSE | MIT | Apache-2.0 | **ABSENT 🆕** |
| Format | Markdown + notebook | MDX + Colab | **README + PDF + Jupyter triple 🆕** |
| Audience | Beginner dev | Agent-builder dev | **Graduate student + researcher 🆕** |
| Scale | ~26K⭐ | ~28K⭐ | **34K⭐ 🆕 (largest T3)** |
| Star velocity | ~26K/~2yr ≈ 30/day | ~28K/15mo ≈ 62/day | **~34K/12-18mo ≈ 60-90/day 🆕** |

**Storm Bear note:** Với scale 34K stars, dive-into-llms hiện là **T3 lớn nhất** trong corpus — demonstrate rằng academic-course-lineage archetype có reach đáng kể ở CN ecosystem.

## 9. Storm Bear VN operator relevance

### 9.1 Self-learning ranking refresh at v39

Cho bạn (Storm Bear operator: VN dev + Scrum coach):

1. **claude-howto v32** — VN-diaspora Claude-Code fluency (13h weekend; immediate ROI)
2. **dive-into-llms v39 🆕** — CN-academic foundational LLM depth (3-month commitment; complements #1)
3. **Microsoft v6** — EN entry-level agent-focused
4. **HF agents-course v26** — EN intermediate agent-focused multi-framework

### 9.2 CN-VN adjacency cho VN reader

Tin tốt: **VN và CN chia sẻ 60-80% technical vocabulary** trong LLM domain (qua Hán-Việt etymology: 模型 / mô hình, 提示 / gợi ý hoặc "prompt", 大模型 / LLM v.v.).

**Strategies để parse CN content:**
- Chrome Translate extension (chính xác ~90%+ cho technical text)
- Dùng Jupyter notebook (code + English ML vocab dominate; Chinese comments minority)
- Kết hợp với Microsoft v6 / HF v26 cho overlap topics; dive-into-llms cover unique (ch4 math reasoning + ch7 steganography less available Anglosphere)

### 9.3 Hardware feasibility cho VN operator

- **8 chương tier A** (1, 2, 3, 5, 6, 7, 10, 11) → chạy được trên RTX 4090 24GB local. Tổng ~30-50 giờ study + code.
- **2 chương tier B** (4, 8) → cloud A100 rental. Budget ~$20-50.
- **1 chương tier C** (9 GUI Agent) → multi-GPU cloud. Budget ~$50-100. Có thể skip nếu budget-constrained.

**Total budget realistic:** $80-180 USD cloud + 60-80 giờ over 3 tháng.

### 9.4 Ethical framing ⚠️

Vì absent-LICENSE:
- ✅ Học cá nhân hoàn toàn OK
- ✅ Cite trong Storm Bear vault (academic-standard)
- ✅ Discuss concepts + share learnings với team (fair use ở VN)
- ❌ KHÔNG dịch + xuất bản VN version mà không xin phép SJTU
- ❌ KHÔNG dùng content làm training material cho sản phẩm thương mại

Nếu muốn dịch / adapt: **email Zhang Zuosheng** qua trang BCMI https://bcmi.sjtu.edu.cn/home/zhangzs/. Academic authors thường grant liberal permission cho non-commercial educational use.

## 10. 3-month roadmap cho VN operator / 3-month study plan

**Month 1 — Foundations + API practice:**
- Tuần 1: Chapter 1 (BERT fine-tuning, RTX 4090)
- Tuần 2: Chapter 2 (multi-provider prompting + API practice; thử Qwen / DeepSeek rẻ)
- Tuần 3-4: Chapter 5 watermark + Chapter 6 jailbreak (security primer; useful cho own-VN-Scrum-bot mitigation)

**Month 2 — Advanced + reasoning:**
- Tuần 5: Chapter 4 math reasoning (**cloud rental A100** 1-day intensive; prepare budget)
- Tuần 6: Chapter 7 steganography + Chapter 8 multimodal
- Tuần 7-8: Chapter 10 agent safety + Chapter 11 RLHF (quan trọng cho alignment intuition)

**Month 3 — Agents + synthesis:**
- Tuần 9-10: Chapter 3 knowledge editing + Chapter 9 GUI agent (nếu cloud budget cho multi-GPU; optional)
- Tuần 11: Thử secondary curriculum Ascend initial-tier (optional; cần đăng ký hiascend.com)
- Tuần 12: **Viết Storm Bear tutorial synthesis** cho VN audience dựa trên learnings (own work; no license issue)

**Expected outcomes sau 3 tháng:**
- Foundational LLM fluency (hiểu fine-tuning + PPO + alignment sâu hơn dùng Claude API-only)
- Custom VN-language Scrum coach agent prototype (Qwen2.5-7B + VN Scrum knowledge corpus)
- Cross-wiki depth (đã đọc v22 LlamaFactory wiki AND dùng LLaMa-Factory thực tế qua ch9)
- Intellectual foundation cho future Storm Bear VN tutorial material

## 11. Tradeoffs + limitations / Đánh đổi và giới hạn

### Ưu điểm

- ✅ Academic-rigor (SJTU peer-review-vetted qua course curriculum committee)
- ✅ Hands-on Jupyter (executable; không chỉ lý thuyết)
- ✅ Coverage rộng (11 topics từ foundational đến agent-era)
- ✅ CN-academic register engaging (playful-serious-question-hook)
- ✅ Free + công khai accessible
- ✅ Cập nhật active (push 2026-04-15; 2025/06 expansion batch)
- ✅ Multi-institutional credibility (SJTU + NUS + Huawei)
- ✅ Cross-corpus citation validates upstream-utility

### Hạn chế

- ❌ **Absent-LICENSE** (legal friction cho adaptation/redistribution)
- ❌ **CN-primary** (friction cho non-CN-literate readers; mitigatable qua translate tools)
- ❌ **Hardware requirements** uneven (ch4 + ch9 cần 40-240GB GPU)
- ❌ **No formal paper** (khác các T5 academic-lab OpenHands ICLR 2025 / DeepTutor arXiv)
- ❌ **No certification** (khác HF v26 leaderboard Unit 4)
- ❌ **Governance minimal** (no CONTRIBUTING / CODE_OF_CONDUCT / SECURITY; khó contribute officially)
- ❌ **Secondary curriculum trên external platform** (Huawei Ascend) — extra registration friction
- ❌ **Không có English translation** (official hoặc community; rủi ro tầm ảnh hưởng quốc tế giới hạn)

### Who it's for

**Tốt cho:**
- Graduate students VN/CN/Asia-diaspora muốn foundational LLM rigor
- Researchers muốn reference tutorial hands-on cho specific topics (watermark / steganography / jailbreak / alignment ít cover ở tutorial Anglo-sphere)
- Self-learners comfortable với CN academic register + GPU cloud budget
- Storm Bear operator muốn complement claude-howto self-onboarding với foundational LLM depth

**Không phù hợp cho:**
- Beginners without Python + basic ML background (prerequisites implicit)
- People needing English-only materials
- Commercial content adapter (license blocker)
- People without GPU access (even cloud) — ch4 + ch9 required hardware

## 12. Resources + next actions / Tài nguyên + bước tiếp theo

### Official resources

- **Main repo:** https://github.com/Lordog/dive-into-llms
- **Primary curriculum:** 11 chapters at `documents/chapter1-11/`
- **Secondary curriculum:** https://www.hiascend.com/edu/growth/lm-development (Huawei Ascend community; registration likely required)
- **Lead author homepage:** https://bcmi.sjtu.edu.cn/home/zhangzs/
- **Star history chart:** https://star-history.com/#Lordog/dive-into-llms&Date

### Related Storm Bear wikis

- **v22 LlamaFactory** — chapter 9 cross-corpus citation target; outside-scope training-infra
- **v38 DeepTutor** — T5 academic-lab HK counterpart (agent-native tutoring vs static curriculum)
- **v6 Microsoft ai-agents-for-beginners** — T3 big-tech-corporate contrast
- **v26 HF agents-course** — T3 commercial-ecosystem-platform contrast
- **v32 claude-howto** — VN self-onboarding complement
- **v37 bizos** — absent-LICENSE precedent

### Next actions for Storm Bear operator

**Option A — Quick sampling (1-2 days):**
- Clone repo, browse 11 chapter READMEs (CN + Chrome translate)
- Read chapter 1 + 2 + 11 (workable on local RTX or laptop)
- Decide if 3-month commitment justified

**Option B — Focused study (1 week intensive):**
- Complete chapters 1 + 2 + 5 + 6 + 10 + 11 (all Tier A GPU; security-alignment focus for VN Scrum coach bot safety design)
- Skip advanced architecture + agents for later

**Option C — Full 3-month study (quarterly investment):**
- Follow roadmap from part 10
- Budget $100-200 cloud GPU + $50 cloud API
- 60-80h over 3 months

**Option D — Observational only (this wiki is enough):**
- No direct study; use Storm Bear wiki as reference
- Revisit specific chapters when tackling concrete problems (e.g., need RLHF intuition → read ch11; need agent safety → read ch10)

**Recommended for Storm Bear v39 post-build:** Option D or A. Reason: claude-howto v32 self-onboarding still has higher ROI (VN-specific Claude-Code fluency), and v27 diagnostic HIGH bundle (vault CLAUDE.md refactor + others) is still BLOCKING-RECOMMENDATION after 16 sessions deferred. **Don't start 3-month study until vault backlog clears.**

---

## Summary / Tóm tắt

**VN:** Dive-into-llms là tài liệu học thuật CN-primary, quy mô lớn (34K stars), rigor cao (SJTU BCMI Lab + NIS8021 + NIS3353 origin), nhưng có friction cho VN operator do (1) ngôn ngữ CN, (2) absent-LICENSE legal blocker cho adaptation, (3) GPU requirements ở vài chương. Giá trị observational cao (Pattern #44 academic-credibility template + dual-curriculum + corporate-community partnership) — direct self-study priority #2 sau claude-howto v32. ⚠️ Đọc Part 0 "Read this first" để hiểu legal posture trước.

**EN:** Dive-into-llms is large-scale (34K stars) CN-primary academic material with high rigor (SJTU BCMI origin), but has friction for VN operator from (1) CN language, (2) absent-LICENSE legal blocker for adaptation, (3) uneven GPU requirements. High observational value (Pattern #44 academic-credibility template + dual-curriculum + corporate-community partnership) — self-study priority #2 after claude-howto v32. ⚠️ Read Part 0 for legal posture.

*Generated as part of Storm Bear v39 LLM wiki build, 2026-04-24. Part of bilingual guide standard since v10 autoresearch.*
