# 6.13 - Nhập môn prompt engineering — Prompt là code

**Source:** https://transform.sg.larksuite.com/wiki/WpyJw61EAi2udKkNr3ml78VMgue
**Wiki ID:** WpyJw61EAi2udKkNr3ml78VMgue
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
Transform Group

6.13 - Nhập môn prompt engineering — Prompt là code

Last updated: Apr 20

Log In or Sign Up
6.13 - Nhập môn prompt engineering — Prompt là code
Bài 6.13: Nhập môn prompt engineering — Prompt là code
Mục tiêu học tập
Mở đầu: "Prompt là code" — từ mindset đến workflow
Prompt engineering là gì?
Phân biệt với các khái niệm khác
Vòng lặp 5 bước (core loop)
Bước 1: Set goal
Bước 2: Write v1 (baseline)
Bước 3: Evaluate
Bước 4: Apply technique
Bước 5: Re-evaluate
Framework setup
1. Test dataset
2. Grader
3. Runner
Ví dụ thực chiến: Meal planner
Bước 1: Goal
Bước 2: v1 baseline
Bước 3: Test 3 athlete
Bước 4: Apply technique — Clear & direct (bài 6.16)
Bước 5: Re-eval v2
Iterate: v3 — Add specific guidelines (bài 6.17)
Iterate: v4 — Add examples (bài 6.18)
Ship v4
Techniques bạn sẽ học trong Module 3
Tại sao eval là "must-have"?
Without eval
With eval
Anti-patterns
❌ Iterate nhiều thứ cùng lúc
❌ Overfit test dataset
❌ Không version control prompt
❌ Không regression test
❌ Skip baseline
Áp dụng ngay
Bài tập 1: Framework mental model (15 phút)
Bài tập 2: Viết baseline (15 phút)
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
6.13 - Nhập môn prompt engineering — Prompt là code​
Modified April 20
Bài 6.13: Nhập môn prompt engineering — Prompt là code​
Module: 3 — Prompt Engineering​
Thời gian ước tính: 25 phút​
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
​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Định nghĩa prompt engineering và phân biệt với "tip trick ChatGPT"​
•
✅ Mô tả vòng lặp 5 bước của quy trình iterate prompt​
•
✅ Hiểu vì sao eval là không thể thiếu cho prompt engineering thật sự​
•
✅ Xác định baseline score cho prompt đầu tiên​
•
✅ Setup framework để track improvement qua các version prompt​
​
​
Mở đầu: "Prompt là code" — từ mindset đến workflow​
Nếu bạn đã dùng ChatGPT nhiều, chắc bạn đã thấy các bài viết blog kiểu:​
"10 prompt magic khiến ChatGPT siêu thông minh!""Từ khóa bí mật giúp AI trả lời hay hơn!"​
Đó không phải prompt engineering. Đó là tips, tricks, hacks — thú vị nhưng không dùng được cho production.​
Prompt engineering thật sự là kỹ thuật. Nó có:​
•
Mục tiêu đo lường được (score, accuracy)​
•
Quy trình lặp lại (baseline → iterate → verify)​
•
Version control (v1, v2, v3 của prompt)​
•
Regression testing (prompt mới không làm tệ case cũ)​
Nói cách khác: prompt là code. Và bạn viết code cho production thế nào, thì viết prompt production thế ấy.​
Bài này đặt nền tảng cho cả Module 3 và Module 4 (Prompt Evaluation). Đọc kỹ.​
​
​
Prompt engineering là gì?​
Định nghĩa chính thức:​
Prompt engineering là quy trình iteratively improve một prompt để đạt reliability và chất lượng cao hơn cho output từ LLM.​
Comments (0)
Help Center
Keyboard Shortcuts
