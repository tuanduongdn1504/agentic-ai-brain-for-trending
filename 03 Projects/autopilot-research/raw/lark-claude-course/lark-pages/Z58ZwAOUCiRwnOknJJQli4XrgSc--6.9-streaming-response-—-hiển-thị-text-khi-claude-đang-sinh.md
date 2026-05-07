# 6.9 - Streaming response — Hiển thị text khi Claude đang sinh

**Source:** https://transform.sg.larksuite.com/wiki/Z58ZwAOUCiRwnOknJJQli4XrgSc
**Wiki ID:** Z58ZwAOUCiRwnOknJJQli4XrgSc
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
Transform Group

6.9 - Streaming response — Hiển thị text khi Claude đang sinh

Last updated: Apr 20

Log In or Sign Up
6.9 - Streaming response — Hiển thị text khi Claude đang sinh
Bài 6.9: Streaming response — Hiển thị text khi Claude đang sinh
Mục tiêu học tập
Mở đầu: 10 giây cứng đơ đủ để mất user
Vấn đề: Response time có thể 10-30 giây
Cách streaming hoạt động
6 loại event trong stream
Cách 1: Low-level với stream=True
Filter chỉ lấy text
Cách 2: High-level với client.messages.stream()
Lấy complete message sau stream
Integration vào chatbot từ bài 6.8
Ví dụ thực chiến: Writer assistant với streaming
Tình huống
Code
UX khác biệt
Case studies theo ngành
🎧 Customer Support — Chatbot web
📝 Content — Marketing tool
💻 Developer Tools — Code assistant
Anti-patterns streaming
❌ Stream vào file log
❌ Stream khi không hiển thị UI
❌ Forget flush=True
❌ Không handle None từ text_stream
❌ Append chunks vào messages thay vì final text
Áp dụng ngay
Bài tập 1: Upgrade chatbot với streaming (20 phút)
Bài tập 2: Đo TTFT (Time To First Token) (15 phút)
Mẹo nâng cao
Mẹo 1: Stream vào WebSocket cho web app
Mẹo 2: Parse tool_use trong stream
Mẹo 3: Cancel stream giữa chừng
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
6.9 - Streaming response — Hiển thị text khi Claude đang sinh​
Modified April 20
Bài 6.9: Streaming response — Hiển thị text khi Claude đang sinh​
Module: 2 — Gọi Claude qua API​
Thời gian ước tính: 25 phút​
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
✅ Giải thích lý do streaming cải thiện UX chatbot một cách đột phá​
•
✅ Bật streaming với stream=True và xử lý event stream​
•
✅ Dùng simplified streaming API (client.messages.stream) để code gọn​
•
✅ Lấy cả streaming text và final complete message cho lưu trữ​
•
✅ Nhận diện 6 loại event trong stream​
Mở đầu: 10 giây cứng đơ đủ để mất user​
Hãy so sánh 2 trải nghiệm:​
Trải nghiệm A — Không stream:​
​
Code block​
Plain Text
Copy
User: "Giải thích quantum computing..."​
[Spinner quay ... 8 giây ...]​
[Toàn bộ 500 từ hiện ra cùng lúc]​
​
​
Trải nghiệm B — Có stream:​
​
Code block​
Plain Text
Copy
User: "Giải thích quantum computing..."​
"Quantum " (0.3s)​
"Quantum computing " (0.5s)​
"Quantum computing is a form of " (1s)​
...​
​
Comments (0)
Help Center
Keyboard Shortcuts
