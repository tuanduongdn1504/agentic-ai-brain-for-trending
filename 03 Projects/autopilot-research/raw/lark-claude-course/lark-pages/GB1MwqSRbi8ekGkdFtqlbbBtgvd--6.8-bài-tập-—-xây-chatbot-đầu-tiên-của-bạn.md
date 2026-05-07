# 6.8 - Bài tập — Xây chatbot đầu tiên của bạn

**Source:** https://transform.sg.larksuite.com/wiki/GB1MwqSRbi8ekGkdFtqlbbBtgvd
**Wiki ID:** GB1MwqSRbi8ekGkdFtqlbbBtgvd
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
Transform Group

6.8 - Bài tập — Xây chatbot đầu tiên của bạn

Last updated: Apr 20

Log In or Sign Up
6.8 - Bài tập — Xây chatbot đầu tiên của bạn
Bài 6.8: Bài tập — Xây chatbot đầu tiên của bạn
Mục tiêu học tập
Mở đầu: Học bằng làm, không học bằng đọc
Đề bài
Tính năng bắt buộc
Tính năng optional (điểm cộng)
Hướng dẫn step-by-step
Bước 1: Setup boilerplate
Bước 2: Viết hàm chat với logging
Bước 3: Viết hàm main loop
Bước 4: Chạy
Bước 5: Test flow
Phiên bản nâng cao (optional)
Sliding window
Validation
Retry logic
Case studies tương tự bạn có thể thử sau
📚 Education — Study buddy
💼 Sales — Discovery prep
🍳 Cooking assistant
💪 Fitness coach
Debug guide — Khi gặp lỗi
Lỗi 1: BadRequestError: messages: first message must use "user" role
Lỗi 2: BadRequestError: messages: all messages must have non-empty content
Lỗi 3: AuthenticationError
Lỗi 4: Claude "quên" mặc dù có history
Lỗi 5: Response bị cắt
Self-review checklist
Functional
Code quality
Edge cases
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
6.8 - Bài tập — Xây chatbot đầu tiên của bạn​
Modified April 20
Bài 6.8: Bài tập — Xây chatbot đầu tiên của bạn​
Module: 2 — Gọi Claude qua API​
Thời gian ước tính: 45-60 phút​
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
​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Ship một chatbot hoàn chỉnh có thể chạy end-to-end​
•
✅ Áp dụng pattern multi-turn từ bài 6.7 vào use case thật​
•
✅ Debug các lỗi phổ biến khi chạy chatbot (role alternating, token limit)​
•
✅ Đo performance của chatbot: latency, token usage, cost​
​
​
Mở đầu: Học bằng làm, không học bằng đọc​
Bạn đã học 7 bài đầu tiên. Kiến thức chắc về:​
•
Cách gọi API (bài 6.6)​
•
Multi-turn conversation (bài 6.7)​
•
Helper functions chuẩn​
Bài này là milestone. Bạn không đọc thêm lý thuyết — bạn ship 1 thứ chạy được. Đây là lần đầu tiên trong khóa bạn tạo ra một sản phẩm nhỏ từ kiến thức đã học.​
​
​
Đề bài​
Xây một chatbot "Travel Assistant" trong Jupyter notebook. Yêu cầu:​
Tính năng bắt buộc​
1.
Multi-turn: nhớ context xuyên suốt phiên chat​
2.
Interactive: user gõ input, Claude trả lời, lặp lại đến khi user gõ "quit"​
3.
Giới hạn scope: Chatbot chỉ trả lời về du lịch (xin gợi ý địa điểm, lịch trình, ẩm thực). Nếu user hỏi off-topic, Claude phải từ chối lịch sự.​
4.
Log: In token usage mỗi turn để theo dõi cost​
Comments (0)
Help Center
Keyboard Shortcuts
