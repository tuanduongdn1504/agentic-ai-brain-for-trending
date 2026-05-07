# 6.10 - System prompts — Định hình hành vi của Claude

**Source:** https://transform.sg.larksuite.com/wiki/JlNtw9O3BiNjZbkyXcAl1YEng3c
**Wiki ID:** JlNtw9O3BiNjZbkyXcAl1YEng3c
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
Transform Group

6.10 - System prompts — Định hình hành vi của Claude

Last updated: Apr 20

Log In or Sign Up
6.10 - System prompts — Định hình hành vi của Claude
Bài 6.10: System prompts — Định hình hành vi của Claude
Mục tiêu học tập
Mở đầu: Huấn luyện vs ra lệnh
System prompt là gì?
Cấu trúc request có system prompt
Cách dùng
Basic
Output khác biệt rõ rệt
Tại sao không đặt mọi thứ vào user message?
Vấn đề 1: Claude ít "nghiêm chỉnh" với user message
Vấn đề 2: Khó tách chỉ dẫn khỏi user input thật
Vấn đề 3: Prompt injection dễ hơn
Cấu trúc system prompt hiệu quả
Template 5-block
Ví dụ đầy đủ — HR Chatbot
Dài bao nhiêu là đủ?
Flexible chat function
Cách dùng
Ví dụ thực chiến: 4 system prompt cho cùng 1 câu hỏi
System A — Business consultant
System B — Empathic therapist
System C — Practical friend
System D — Skeptical investor
Case studies theo ngành
🎧 Customer Support
⚖️ Legal
📊 Data Analysis
🏥 Healthcare (với disclaimers)
Anti-patterns
❌ System prompt quá vague
❌ System prompt conflict với user messages
❌ Đưa PII / secrets vào system
❌ System quá dài (bloat)
❌ Update system giữa conversation
Áp dụng ngay
Bài tập 1: 4 personality cho 1 chatbot (20 phút)
Bài tập 2: System prompt cho app của bạn (15 phút)
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
6.10 - System prompts — Định hình hành vi của Claude​
Modified April 20
Bài 6.10: System prompts — Định hình hành vi của Claude​
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
✅ Phân biệt system prompt và user message — vai trò khác nhau​
•
✅ Viết system prompt định hình tone, role, constraints cho Claude​
•
✅ Thiết kế chat function linh hoạt accept system prompt như parameter​
•
✅ Nhận diện khi nào system prompt là đủ, khi nào cần prompt engineering sâu hơn​
•
✅ Tránh 5 anti-patterns phổ biến với system prompt​
Mở đầu: Huấn luyện vs ra lệnh​
Hãy tưởng tượng bạn thuê một người trợ lý mới. Có 2 cách hướng dẫn:​
Cách A — Mỗi lần dặn lại:​
"Hôm nay khi khách đến, nhớ chào lễ phép. Dùng tiếng Anh chuẩn. Đừng nói tiếu lâm..."​
Bạn lặp lại lời dặn mỗi buổi sáng.​
Cách B — Brief 1 lần cho cả nhiệm kỳ:​
Job description viết sẵn: "Bạn là lễ tân công ty. Tone lễ phép. Tiếng Anh chuẩn. Không tiếu lâm. Xử lý khách VIP theo SOP A..."​
Trợ lý đọc 1 lần, giữ mãi, luôn áp dụng.​
Cách B = system prompt. Cách A = user message. Hai cơ chế này khác nhau về vai trò, ảnh hưởng tới cách Claude xử lý.​
Hiểu system prompt là bước ngoặt — từ "gõ câu hỏi rồi hy vọng" sang "thiết kế behavior chính xác".​
System prompt là gì?​
System prompt = chỉ dẫn cấp cao gửi cho Claude ngoài user messages. Claude "nhớ" nó xuyên suốt conversation và thiên về tuân theo hơn so với chỉ dẫn trong user message.​
Comments (0)
Help Center
Keyboard Shortcuts
