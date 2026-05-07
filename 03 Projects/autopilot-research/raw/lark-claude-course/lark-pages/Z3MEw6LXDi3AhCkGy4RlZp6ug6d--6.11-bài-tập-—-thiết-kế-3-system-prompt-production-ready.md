# 6.11 - Bài tập — Thiết kế 3 system prompt production-ready

**Source:** https://transform.sg.larksuite.com/wiki/Z3MEw6LXDi3AhCkGy4RlZp6ug6d
**Wiki ID:** Z3MEw6LXDi3AhCkGy4RlZp6ug6d
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
Transform Group

6.11 - Bài tập — Thiết kế 3 system prompt production-ready

Last updated: Apr 20

Log In or Sign Up
6.11 - Bài tập — Thiết kế 3 system prompt production-ready
Bài 6.11: Bài tập — Thiết kế 3 system prompt production-ready
Mục tiêu học tập
Mở đầu: Viết system prompt là kỹ năng, không phải tài năng
Đề bài
Scenario 1: Email summarizer
Context
Input format
Output yêu cầu
Test cases (dùng để validate system prompt)
Gợi ý v1
Chạy thử
Điểm cần kiểm tra
Iteration v2
Self-review
Scenario 2: Interview question generator
Context
Input
Output
Test cases
Gợi ý approach
Scenario 3: Product description writer
Context
Input
Output
Test cases
Tự làm từ đầu
Pattern chung: Iteration workflow
Thư viện system prompt tái sử dụng
Checklist submit bài tập
Scenario X
Tips để prompt work tốt hơn
Tip 1: Start simple, add constraints
Tip 2: Put examples đúng format
Tip 3: Đặt constraint dương > phủ định
Tip 4: Cho "escape hatch"
Tip 5: Test same input 3 lần
Mẹo nâng cao
Mẹo 1: Chain-of-thought trong system prompt
Mẹo 2: Negative examples
Mẹo 3: XML section delimiter
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
6.11 - Bài tập — Thiết kế 3 system prompt production-ready​
Modified April 20
Bài 6.11: Bài tập — Thiết kế 3 system prompt production-ready​
Module: 2 — Gọi Claude qua API​
Thời gian ước tính: 60 phút​
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
✅ Áp dụng template 5-block để viết system prompt cho use case thật​
•
✅ So sánh output giữa các biến thể system prompt để chọn tối ưu​
•
✅ Nhận diện khi nào system prompt cần iteration thêm​
•
✅ Tạo thư viện system prompt tái sử dụng​
Mở đầu: Viết system prompt là kỹ năng, không phải tài năng​
Sai lầm của dev mới học: viết system prompt 1 lần, test 1 case, ship. Kết quả: 20% use case lỗi.​
Dev có kinh nghiệm: viết v1 → test 10 case → thấy fail 3 → v2 fix 3 đó → test thêm → v3... đến khi đạt >90% accuracy.​
Bài này là cơ hội luyện đúng quy trình đó trên 3 use case cụ thể.​
Đề bài​
Viết 3 system prompt cho 3 scenario sau. Với mỗi cái:​
1.
Draft v1 theo template 5-block (Role, Objective, Constraints, Output, Examples)​
2.
Test với 5-10 câu hỏi mẫu (bao gồm edge case)​
3.
Iterate v2 dựa trên output sai​
4.
Báo cáo kết quả (bao nhiêu pass/fail)​
Scenario 1: Email summarizer​
Comments (0)
Help Center
Keyboard Shortcuts
