# 6.16 - Clear & Direct — Dòng đầu tiên quyết định tất cả

**Source:** https://transform.sg.larksuite.com/wiki/FaO3wnc6YiiHxZkYlgnll9pTg4d
**Wiki ID:** FaO3wnc6YiiHxZkYlgnll9pTg4d
**Archived:** 2026-05-07

---

Lark Docs
C
Claude Course 2026
Public access
Table of contents
Khoá học Claude toàn diện tiếng Việt
🔥
Recap 5 buổi học Claude AI online
Anthropic courses
01 - Claude 101
02 - Claude Code 101
03 - Claude Cowork
04 - Claude Code in Action
05 - AI Fluency: Framework & Foundations
06 - Building with the Claude API
Slide: Building with the Claude API.pdf
6.0 - Building with the Claude API — Tổng quan khóa học
6.1 - Chào mừng bạn đến với khóa học
6.2 - Tổng quan các model của Claude
6.3 - Các ứng dụng của Anthropic — Claude Code và Computer Use
6.4 - Vòng đời một request — Từ client đến Claude và ngược lại
6.5 - Lấy API key từ Anthropic Console
6.6 - Gọi request đầu tiên đến Claude
6.7 - Hội thoại nhiều lượt (Multi-Turn Conversations)
6.8 - Bài tập — Xây chatbot đầu tiên của bạn
6.9 - Streaming response — Hiển thị text khi Claude đang sinh
6.10 - System prompts — Định hình hành vi của Claude
6.11 - Bài tập — Thiết kế 3 system prompt production-ready
6.12 - Temperature — Kiểm soát độ ngẫu nhiên của Claude
6.13 - Nhập môn prompt engineering — Prompt là code
6.14 - Structured data — Ép Claude trả JSON/code sạch
6.15 - Bài tập — Structured data cho 3 use case
6.16 - Clear & Direct — Dòng đầu tiên quyết định tất cả
6.17 - Being specific — Guidelines và Process Steps
6.18 - Providing examples — Few-shot prompting
6.19 - Structure với XML tags
6.20 - Bài tập tổng hợp — Viết prompt production-grade
6.21 - Quiz — Prompt Engineering
6.22 - Prompt evaluation là gì?
6.23 - Workflow eval 5 bước
6.24 - Generating test datasets
6.25 - Running the eval — Build pipeline cốt lõi
6.26 - Model-based grading — Claude chấm Claude
6.27 - Code-based grading — Validation bằng Python
6.28 - Bài tập — End-to-end eval cho app của bạn
6.29 - Quiz — Prompt Evaluation
6.30 - Nhập môn Tool Use — Cho Claude "bàn tay"
6.31 - Tool schemas — JSON mô tả tool cho Claude
6.32 - Tool functions — Python code Claude sẽ gọi
6.33 - Handling message blocks — Multi-block responses
6.34 - Sending tool results — Gửi kết quả về Claude
6.35 - Multi-turn với tools — Sequential tool calls
6.36 - Triển khai multi-turn loop — Full code
6.37 - Dùng nhiều tools cùng lúc — Adding tools to your system
6.38 - Fine-grained tool calling — Stream tool inputs
6.39 - The text editor tool — Built-in tool cho file operations
6.40 - Quiz — Tool Use
6.41 - Extended thinking — Giấy nháp cho Claude
6.42 - Image support — Claude đọc ảnh (Vision)
6.43 - PDF support — Đọc tài liệu thẳng từ PDF
6.44 - The web search tool — Claude tra cứu internet
6.45 - Citations — Trust qua transparency
6.46 - Code execution & Files API — Claude chạy Python
6.47 - Prompt caching — Khái niệm & ROI
6.48 - Rules of prompt caching — Breakpoints + invalidation
6.49 - Prompt caching in action — Production code
6.50 - Quiz — Features of Claude
6.51 - Nhập môn RAG — Retrieval Augmented Generation
6.52 - Text chunking strategies
Transform Group

6.16 - Clear & Direct — Dòng đầu tiên quyết định tất cả

Last updated: Apr 20

Log In or Sign Up
6.16 - Clear & Direct — Dòng đầu tiên quyết định tất cả
Bài 6.16: Clear & Direct — Dòng đầu tiên quyết định tất cả
Mục tiêu học tập
Mở đầu: Đồng nghiệp mới cần chỉ dẫn rõ, không úp mở
2 nguyên tắc
1. CLEAR — Dùng ngôn ngữ đơn giản, không ambiguous
2. DIRECT — Ra lệnh, không hỏi
Case study: Meal planner (từ bài 6.13)
v1 — Vague
v2 — Clear & Direct
Danh sách action verbs mạnh
Generate / Create
Analyze / Evaluate
Extract / Parse
Transform / Convert
Classify / Categorize
Before/After library
Ví dụ 1: Summary task
Ví dụ 2: Coding
Ví dụ 3: Email
Ví dụ 4: Analysis
Case studies theo ngành
📝 Content — SEO writer
💼 Sales — Email drafter
🎓 Education — Test generator
Anti-patterns
❌ Over-politeness
❌ Hypothetical phrasing
❌ Multiple actions in one
❌ Action verb yếu
❌ Apologize trước khi prompt
Áp dụng ngay
Bài tập 1: Rewrite 5 prompts (15 phút)
Bài tập 2: Refactor prompt của bạn (15 phút)
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
6.16 - Clear & Direct — Dòng đầu tiên quyết định tất cả​
Modified April 20
Bài 6.16: Clear & Direct — Dòng đầu tiên quyết định tất cả​
Module: 3 — Prompt Engineering​
Thời gian ước tính: 15 phút​
Mức độ: Cơ bản → Trung cấp​
​
💡
Cách học hiệu quả:​
•
NotebookLM đã được nạp toàn bộ khóa học, bạn có thể chat, hỏi với AI thay vì đọc hết toàn bộ​
https://notebooklm.google.com/notebook/2a42eeff-a797-44cd-86d5-f8b8a4ee491b​
•
Tổng hợp 25 video dành cho người mới bắt đầu, dễ nghe, dễ hiểu các khái niệm​
​
25 tập khám phá Claude AI​
•
Xem slide về khóa học này để tổng quát, trực quan​
​
Slide: Building with the Claude API.pdf​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Nhận diện prompt vague vs prompt clear & direct​
•
✅ Bắt đầu prompt với action verb mạnh (Generate, Write, Analyze)​
•
✅ Biết sự khác biệt giữa "hỏi" và "ra lệnh" — và vì sao ra lệnh hiệu quả hơn​
•
✅ Đo improvement cụ thể khi áp dụng technique (2.3 → 3.9 trong case study)​
Mở đầu: Đồng nghiệp mới cần chỉ dẫn rõ, không úp mở​
Hãy tưởng tượng bạn vừa tuyển trợ lý mới. Monday sáng bạn nói:​
Cách A:​
"Ừm, em biết không, kiểu như, anh đang nghĩ đến cái slide deck, về cái dự án mới, có lẽ làm sao đó cho thuyết phục khách hàng, em hiểu ý anh chứ?"​
Cách B:​
"Tạo slide deck 10 slide cho dự án Q2, audience là khách hàng enterprise, gửi draft cho anh trước 5pm thứ 4."​
Trợ lý cách A: confused, có thể làm sai hướng.Trợ lý cách B: biết chính xác task, có thể bắt đầu ngay.​
Claude y hệt. Prompt cách A → output vague. Prompt cách B → output clear, on-point.​
Technique "Clear & Direct" — đầu tiên và quan trọng nhất trong prompt engineering — chính là rèn cách B.​
2 nguyên tắc​
1. CLEAR — Dùng ngôn ngữ đơn giản, không ambiguous​
❌ Vague:​
"Tôi cần biết về những thứ mà người ta đặt trên mái nhà để dùng năng lượng mặt trời — cái gọi là solar panel ấy."​
Comments (0)
Help Center
Keyboard Shortcuts
