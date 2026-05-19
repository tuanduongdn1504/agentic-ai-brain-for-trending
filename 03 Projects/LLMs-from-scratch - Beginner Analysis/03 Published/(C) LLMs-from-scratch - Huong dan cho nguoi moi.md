# LLMs-from-scratch — Hướng dẫn cho người mới / Beginner's Guide

> **VN + EN** beginner-friendly guide for `rasbt/LLMs-from-scratch` by Sebastian Raschka (Manning 2024 book companion).
> AI-generated wiki page for the Storm Bear vault corpus at v74 (2026-05-19).

---

## 1. LLMs-from-scratch là gì? / What is LLMs-from-scratch?

**🇻🇳 Tiếng Việt:**

`rasbt/LLMs-from-scratch` là **kho code chính thức** đi kèm với cuốn sách *"Build a Large Language Model (From Scratch)"* của tác giả Sebastian Raschka, xuất bản bởi Manning năm 2024.

Repo này dạy bạn cách **xây dựng một mô hình ngôn ngữ lớn (LLM) giống ChatGPT từ đầu** bằng PyTorch — từng bước một, qua 7 chương Jupyter notebook + 5 phụ lục. Mục tiêu: hiểu LLM hoạt động *từ bên trong* bằng cách tự code lại từ đầu.

**🇬🇧 English:**

`rasbt/LLMs-from-scratch` is the **official code repository** companion to Sebastian Raschka's Manning-published book *"Build a Large Language Model (From Scratch)"* (2024).

The repo teaches you how to **build a ChatGPT-like Large Language Model (LLM) from scratch** in PyTorch — step by step, through 7 Jupyter notebook chapters + 5 appendices. The goal: understand LLMs *from the inside out* by coding them up from the ground.

---

## 2. Ai là tác giả? / Who is the author?

**🇻🇳 Tiếng Việt:**

**Sebastian Raschka** (GitHub: `rasbt`) là một học giả ML người Mỹ với background mạnh:
- Tiến sĩ Thống kê (Michigan State University)
- Cựu Trợ lý Giáo sư tại UW-Madison
- Hiện là AI Research Engineer chuyên về LLMs
- Tác giả của nhiều sách kinh điển: *Python Machine Learning* (Packt 2015-2019, 3 editions), *Machine Learning with PyTorch and Scikit-Learn* (Packt 2022), và *Build a Large Language Model From Scratch* (Manning 2024)
- 38,000 followers trên GitHub; blog "Ahead of AI" (magazine.sebastianraschka.com); YouTube channel @SebastianRaschka

Raschka là một trong những **giáo viên ML có ảnh hưởng nhất hiện nay** — sánh ngang với Andrej Karpathy về phong cách "dạy LLM bằng cách code lại từ đầu."

**🇬🇧 English:**

**Sebastian Raschka** (GitHub: `rasbt`) is an American ML academic-educator with strong credentials:
- PhD in Statistics (Michigan State University)
- Former Assistant Professor at UW-Madison
- Currently AI Research Engineer specializing in LLMs
- Author of multiple foundational books: *Python Machine Learning* (Packt 2015-2019, 3 editions), *Machine Learning with PyTorch and Scikit-Learn* (Packt 2022), and *Build a Large Language Model From Scratch* (Manning 2024)
- 38,000 GitHub followers; "Ahead of AI" Substack-style blog (magazine.sebastianraschka.com); YouTube @SebastianRaschka

Raschka is one of the **most-influential ML educators today** — alongside Andrej Karpathy in the "teach LLMs by coding them from scratch" pedagogical lineage.

---

## 3. Ai nên đọc / Who should learn from this

**🇻🇳 Tiếng Việt:**

Cuốn sách + repo này phù hợp nhất cho:

- ✅ **Lập trình viên Python với kinh nghiệm vững** muốn hiểu LLM thực sự hoạt động ra sao
- ✅ **Sinh viên CS/Data Science** đang học về deep learning và muốn hiểu transformer architecture từ A đến Z
- ✅ **AI engineer hoặc ML researcher** muốn có nền tảng vững về LLM internals trước khi làm việc với frontier models
- ✅ **Người tự học ML** không muốn chỉ "dùng" LLM mà muốn hiểu chúng

Không phù hợp với:
- ❌ Người chỉ muốn DÙNG ChatGPT / Claude / Copilot (đây là sách dạy XÂY chứ không phải dạy DÙNG)
- ❌ Người không có nền Python — bạn cần Python mạnh trước
- ❌ Người tìm "công cụ production-grade" — code trong sách được thiết kế chạy trên laptop để học, không phải để deploy

**🇬🇧 English:**

This book + repo is best suited for:

- ✅ **Python developers with strong fundamentals** who want to understand how LLMs actually work
- ✅ **CS/Data Science students** learning deep learning and transformer architecture in-depth
- ✅ **AI engineers or ML researchers** wanting solid LLM-internals foundation before working with frontier models
- ✅ **Self-taught ML learners** who don't just want to *use* LLMs but understand them

NOT a fit for:
- ❌ People who only want to USE ChatGPT / Claude / Copilot (this teaches how to BUILD, not how to USE)
- ❌ People without Python foundation — strong Python required
- ❌ People looking for "production-grade tools" — code is laptop-scaled for learning, not deployment

---

## 4. Bạn sẽ học được gì / What you'll learn

**🇻🇳 Tiếng Việt:**

Sau khi đọc hết cuốn sách + chạy hết code, bạn sẽ hiểu:

1. **Chương 1:** LLM là gì, hoạt động ra sao ở mức khái niệm (không code)
2. **Chương 2:** Xử lý dữ liệu văn bản — tokenization, BPE, embedding, dataloader
3. **Chương 3:** Cơ chế Attention từ đơn giản đến multi-head attention
4. **Chương 4:** Lắp ráp toàn bộ GPT model từ các thành phần đã học
5. **Chương 5:** Pretrain model trên dữ liệu không gán nhãn (Project Gutenberg / Custom data)
6. **Chương 6:** Finetune để phân loại văn bản (spam classifier)
7. **Chương 7:** Finetune để theo lệnh (instruction tuning) — gần với cách ChatGPT được train

**Phần thưởng (bonus folders):** Llama 3.2 / Qwen3 / Gemma 3 / OLMo 3 architectures, LoRA finetuning, Direct Preference Optimization (DPO), Mixture-of-Experts (MoE), KV Cache, Grouped-Query Attention, Sliding Window Attention, và nhiều biến thể attention khác.

**🇬🇧 English:**

After reading the book + running the code, you'll understand:

1. **Chapter 1:** What LLMs are and how they work conceptually (no code)
2. **Chapter 2:** Text data processing — tokenization, BPE, embedding, dataloaders
3. **Chapter 3:** Attention mechanisms from simple to multi-head attention
4. **Chapter 4:** Full GPT model assembly from earlier components
5. **Chapter 5:** Pretraining on unlabeled data (Project Gutenberg / custom data)
6. **Chapter 6:** Finetuning for text classification (spam classifier example)
7. **Chapter 7:** Finetuning to follow instructions — close to how ChatGPT is trained

**Bonus folders:** Llama 3.2 / Qwen3 / Gemma 3 / OLMo 3 architectures, LoRA finetuning, Direct Preference Optimization (DPO), Mixture-of-Experts (MoE), KV Cache, Grouped-Query Attention, Sliding Window Attention, and many other attention variants.

---

## 5. Cách cài đặt + chạy / Setup + run

**🇻🇳 Tiếng Việt:**

Repo này KHÔNG cần cài qua npm/pip vì code là Jupyter notebook + Python scripts. Cách dùng đơn giản:

```bash
# Clone repo (chỉ branch chính, tiết kiệm dung lượng)
git clone --depth 1 https://github.com/rasbt/LLMs-from-scratch.git

# Vào thư mục
cd LLMs-from-scratch

# Cài Python packages cần thiết (xem setup/ folder để có hướng dẫn đầy đủ)
pip install -r requirements.txt  # hoặc dùng uv (mới hơn)

# Mở Jupyter notebook và chạy ch02.ipynb, ch03.ipynb, ...
jupyter notebook
```

**Yêu cầu phần cứng:** *"thiết kế chạy trên laptop thông thường trong khoảng thời gian hợp lý"* — không bắt buộc GPU; nếu có GPU thì code tự dùng.

Repo có 3-OS CI testing (Linux + Windows + macOS) — bạn có thể tin tưởng nó chạy được trên hệ điều hành phổ biến.

**🇬🇧 English:**

This repo does NOT need npm/pip install since the code is Jupyter notebooks + Python scripts. Simple usage:

```bash
# Clone the repo (main branch only, save bandwidth)
git clone --depth 1 https://github.com/rasbt/LLMs-from-scratch.git

# Enter the directory
cd LLMs-from-scratch

# Install required Python packages (see setup/ folder for full instructions)
pip install -r requirements.txt  # or use uv (modern)

# Open Jupyter notebook and run ch02.ipynb, ch03.ipynb, ...
jupyter notebook
```

**Hardware requirements:** *"designed to run on conventional laptops within a reasonable timeframe"* — no GPU required; if you have one, code auto-uses it.

Repo has 3-OS CI testing (Linux + Windows + macOS) — you can trust it runs on common operating systems.

---

## 6. License notes / Lưu ý về giấy phép

**🇻🇳 Tiếng Việt:**

Repo này dùng **Apache-2.0 với một sửa đổi quan trọng**:
- **Code** trong repo: Apache-2.0 — bạn được dùng tự do
- **Nội dung sách + hình ảnh chương** trong cuốn sách Manning: **KHÔNG covered** bởi Apache — vẫn là copyright của Manning

Vì vậy:
- ✅ Bạn được copy / modify / dùng code trong các project khác (Apache-2.0)
- ❌ Bạn KHÔNG được copy nội dung từ sách giấy / ebook và phân phối lại (đó là vi phạm bản quyền Manning)
- ❌ Bạn KHÔNG được upload PDF lậu của sách (đó là vi phạm bản quyền)

**Đây là CORPUS-FIRST trong vault Storm Bear**: chưa subject nào trước v74 dùng kiểu sửa đổi Apache để loại trừ nội dung sách khỏi license. Storm Bear vault chính thức ghi nhận đây là Pattern #45 sub-typology 45d.

**🇬🇧 English:**

This repo uses **Apache-2.0 with an important modification**:
- **Code** in the repo: Apache-2.0 — free to use
- **Book content + chapter images** from the Manning book: **NOT covered** by Apache — remains Manning's copyright

So:
- ✅ You can copy / modify / use the code in other projects (Apache-2.0)
- ❌ You CANNOT copy book content from the printed/ebook version and redistribute it (Manning copyright violation)
- ❌ You CANNOT upload pirated PDFs of the book (copyright violation)

**This is CORPUS-FIRST in the Storm Bear vault**: no subject before v74 used this kind of Apache modification to exclude book content from license coverage. Storm Bear vault officially registers this as Pattern #45 sub-typology 45d.

---

## 7. Cuốn sách bao nhiêu tiền / Cost

**🇻🇳 Tiếng Việt:**

- **Code repo:** Miễn phí (Apache-modified)
- **Sách Manning (print + ebook):** Khoảng $40-60 USD (Manning có discount thường xuyên)
- **Khóa video Manning livevideo:** Khoảng $40-60 USD (companion video 17h15m do Raschka thực hiện)
- **PDF 170-trang "test yourself" guide:** Miễn phí từ Manning website

Mua sách qua **homepage URL của repo (Amazon affiliate link `amzn.to/4fqvn0D`)** sẽ ủng hộ tác giả qua chương trình Amazon Associates.

**🇬🇧 English:**

- **Code repo:** Free (Apache-modified)
- **Manning book (print + ebook):** ~$40-60 USD (Manning has frequent discounts)
- **Manning livevideo course:** ~$40-60 USD (companion 17h15m video by Raschka)
- **Free 170-page "test yourself" guide PDF:** Free from Manning website

Purchasing through the repo's **homepage URL (Amazon affiliate link `amzn.to/4fqvn0D`)** supports the author via Amazon Associates.

---

## 8. So sánh với các tài liệu khác / Comparison to similar resources

**🇻🇳 Tiếng Việt:**

| Tài liệu | Cách tiếp cận | Độ sâu | Phù hợp cho |
|----------|---------------|--------|-------------|
| **LLMs-from-scratch (Raschka)** | Sách + code + video, 7 chương từng bước | RẤT SÂU | Người muốn hiểu LLM từ A-Z |
| **nanoGPT (Karpathy)** | Single repo + YouTube series "Let's build GPT" | RẤT SÂU nhưng tập trung | Người thích phong cách Karpathy code-along |
| **HuggingFace Course** | Web tutorials + Colab notebooks | RỘNG nhưng không SÂU | Người muốn dùng transformers library |
| **fast.ai Deep Learning** | Top-down approach từ kết quả → lý thuyết | SÂU ở góc nhìn pragmatic | Người tự học muốn build apps nhanh |

Lựa chọn Raschka phù hợp khi:
- Bạn muốn cấu trúc chương sách hệ thống
- Bạn muốn hiểu từ math cơ bản đến full GPT
- Bạn không ngại đọc dài + chạy notebook

**🇬🇧 English:**

| Resource | Approach | Depth | Best for |
|----------|----------|-------|----------|
| **LLMs-from-scratch (Raschka)** | Book + code + video, 7 chapters step-by-step | VERY DEEP | Those wanting to understand LLMs A-to-Z |
| **nanoGPT (Karpathy)** | Single repo + YouTube "Let's build GPT" series | VERY DEEP but focused | Those who like Karpathy's code-along style |
| **HuggingFace Course** | Web tutorials + Colab notebooks | BROAD but not DEEP | Those wanting to use transformers library |
| **fast.ai Deep Learning** | Top-down approach from results → theory | DEEP in pragmatic angle | Self-learners wanting to build apps fast |

Choose Raschka when:
- You want systematic book-chapter structure
- You want to understand from basic math to full GPT
- You don't mind long reads + running notebooks

---

## 9. Lưu ý cho người dùng vault Storm Bear / Notes for Storm Bear vault users

**🇻🇳 Tiếng Việt:**

LLMs-from-scratch **KHÔNG phải là pilot candidate** cho vault Storm Bear vì:
- Đây là tài liệu giáo dục, không phải công cụ vận hành
- Vault Storm Bear dùng LLM (Claude Code) như sản phẩm "hộp đen" — không cần tự xây LLM
- Học LLM internals không trực tiếp giúp vault hoạt động tốt hơn (chỉ giúp hiểu sâu hơn về substrate)

**Tuy nhiên**, đây vẫn là một **methodology-influence-node mạnh**:
- Hiểu LLM hoạt động giúp prompt tốt hơn
- Hiểu context window giúp thiết kế routine v2.x tốt hơn
- Hiểu finetuning giúp đánh giá khi nào nên dùng custom models vs Claude

Storm Bear vault đăng ký Raschka là **corpus-second-foundation-individual** sau Karpathy (v63 corpus-foundation-individual).

**🇬🇧 English:**

LLMs-from-scratch is **NOT a pilot candidate** for the Storm Bear vault because:
- It's educational material, not an operational tool
- The Storm Bear vault uses LLM (Claude Code) as a "black-box" product — no need to build LLMs from scratch
- Learning LLM internals doesn't directly help the vault operate better (only helps understand the substrate more deeply)

**However**, this is still a **strong methodology-influence-node**:
- Understanding how LLMs work helps with better prompting
- Understanding context windows helps design routine v2.x better
- Understanding finetuning helps evaluate when to use custom models vs Claude

Storm Bear vault registers Raschka as **corpus-second-foundation-individual** after Karpathy (v63 corpus-foundation-individual).

---

## 10. Bottom line / Tóm lại

**🇻🇳 Tiếng Việt:**

`rasbt/LLMs-from-scratch` là **sách giáo khoa + code companion tốt nhất hiện tại** cho ai muốn hiểu LLM hoạt động ra sao. Tác giả Sebastian Raschka là một trong những giáo viên ML có ảnh hưởng nhất.

Đây là tài liệu giáo dục dài hơi (1,032 ngày tuổi vẫn duy trì 92.2 stars/ngày) — mua sách nếu bạn nghiêm túc muốn học LLM từ đầu. Repo miễn phí nếu chỉ muốn xem code.

**Verdict cho vault Storm Bear:** Không phải pilot. Là corpus-knowledge-only subject để học hỏi pattern thiết kế repo book-companion + Apache-modified license + multi-book-portfolio discipline.

**🇬🇧 English:**

`rasbt/LLMs-from-scratch` is **the best LLM textbook + code companion** currently available for anyone wanting to understand how LLMs work. Author Sebastian Raschka is one of the most-influential ML educators.

This is long-horizon educational material (1,032 days old still sustaining 92.2 stars/day) — buy the book if you're serious about learning LLMs from scratch. The repo is free if you just want to browse code.

**Verdict for Storm Bear vault:** Not a pilot. A corpus-knowledge-only subject for learning book-companion-repo design patterns + Apache-modified license + multi-book-portfolio discipline.

---

## 11. Tài liệu tham khảo / References

- **Repo:** https://github.com/rasbt/LLMs-from-scratch
- **Sách Manning:** https://www.manning.com/books/build-a-large-language-model-from-scratch
- **Amazon (affiliate):** https://amzn.to/4fqvn0D
- **Trang tác giả:** https://sebastianraschka.com
- **Blog Ahead of AI:** https://magazine.sebastianraschka.com
- **YouTube:** https://www.youtube.com/@SebastianRaschka
- **Twitter/X:** @rasbt
- **CITATION:** *"Build A Large Language Model (From Scratch), Published by Manning, ISBN 978-1633437166"* by Sebastian Raschka (2024)
- **Sequel repo:** https://github.com/rasbt/reasoning-from-scratch (Build a Reasoning Model From Scratch)

---

*Storm Bear vault wiki v74 · 2026-05-19 · routine v2.2 fifth-wiki-since-routine-validation*
