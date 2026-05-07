# 6.17 - Being specific — Guidelines và Process Steps

**Source:** https://transform.sg.larksuite.com/wiki/TBhYw8l0di7kAdk1tLHlycqtgbe
**Wiki ID:** TBhYw8l0di7kAdk1tLHlycqtgbe
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
6.53 - Text embeddings — Biến text thành số
Transform Group

6.17 - Being specific — Guidelines và Process Steps

Last updated: Apr 20

Log In or Sign Up
6.17 - Being specific — Guidelines và Process Steps
Bài 6.17: Being specific — Guidelines và Process Steps
Mục tiêu học tập
Mở đầu: "Viết 1 short story" — nhưng 1000 output khác nhau
2 loại specificity
Loại 1: Output Quality Guidelines
Loại 2: Process Steps
Case study: Meal planner tiếp tục (3.9 → 7.86)
v2 (từ bài 6.16) — Clear & direct
v3 — Add Quality Guidelines
v4 — Add Process Steps (optional)
Khi nào dùng loại nào?
Quality Guidelines — Luôn
Process Steps — Cho problem phức tạp
Ví dụ thực chiến: Sales drop analysis
Not specific enough
Specific with Process Steps
Ví dụ: Code review prompt
Generic
Specific — Guidelines + Steps
Template: Specific prompt
Case studies theo ngành
🎓 Education — Graded essay feedback
💼 Sales — Call prep brief
💰 Finance — Investment memo
Anti-patterns
❌ Guidelines contradict mỗi other
❌ Too many guidelines
❌ Process steps quá prescriptive
❌ Dùng Process Steps cho simple task
Áp dụng ngay
Bài tập 1: Add guidelines to your prompt (15 phút)
Bài tập 2: Decision-making prompt với Process Steps (15 phút)
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
6.17 - Being specific — Guidelines và Process Steps​
Modified April 20
Bài 6.17: Being specific — Guidelines và Process Steps​
Module: 3 — Prompt Engineering​
Thời gian ước tính: 20 phút​
Mức độ: Trung cấp​
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
✅ Phân biệt 2 loại specificity: Output Guidelines vs Process Steps​
•
✅ Viết quality guidelines kiểm soát length, format, elements​
•
✅ Viết process steps giúp Claude reason qua problem systematically​
•
✅ Biết khi nào cần cả 2, khi nào chỉ cần 1​
•
✅ Đo impact: case study 3.9 → 7.86 score​
Mở đầu: "Viết 1 short story" — nhưng 1000 output khác nhau​
Bạn prompt: "Viết short story về nhân vật phát hiện tài năng ẩn giấu."​
Claude có thể output:​
•
Story 200 từ hoặc 5000 từ​
•
1 nhân vật hoặc 10​
•
Chủ đề: music, sports, magic, science...​
•
Tone: heart-warming, dark, comedic​
•
Setting: fantasy, modern, sci-fi​
Cùng prompt → vô số output khác nhau. Nếu bạn ship prompt này cho app, mỗi user thấy 1 story khác nhau về style/length → inconsistent brand.​
Technique specificity giải quyết — đưa constraint cụ thể để output predictable.​
2 loại specificity​
Loại 1: Output Quality Guidelines​
Kiểm soát WHAT output trông như thế nào.​
Comments (0)
Help Center
Keyboard Shortcuts
