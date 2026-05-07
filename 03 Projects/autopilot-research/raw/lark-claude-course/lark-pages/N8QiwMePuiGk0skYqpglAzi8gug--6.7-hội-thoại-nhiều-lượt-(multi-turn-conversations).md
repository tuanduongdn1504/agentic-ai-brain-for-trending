# 6.7 - Hội thoại nhiều lượt (Multi-Turn Conversations)

**Source:** https://transform.sg.larksuite.com/wiki/N8QiwMePuiGk0skYqpglAzi8gug
**Wiki ID:** N8QiwMePuiGk0skYqpglAzi8gug
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
Transform Group

6.7 - Hội thoại nhiều lượt (Multi-Turn Conversations)

Last updated: Apr 20

Log In or Sign Up
6.7 - Hội thoại nhiều lượt (Multi-Turn Conversations)
Bài 6.7: Hội thoại nhiều lượt (Multi-Turn Conversations)
Mục tiêu học tập
Mở đầu: Cuộc trò chuyện với người mất trí nhớ mỗi giây
Tại sao Claude lại stateless?
3 lý do thiết kế
Trade-off
Cách multi-turn hoạt động
3 helper function chuẩn
Cách dùng
Pattern nâng cao: Interactive loop
Vấn đề: History dài vô tận
3 chiến lược quản lý history
Ví dụ thực chiến: Tutor AI toán
Tình huống
Code
Output dự kiến
Case studies theo ngành
💼 Sales — Discovery call assistant
🎧 Customer Support — Contextual resolution
📝 Content — Iterative writing
Anti-patterns với multi-turn
❌ Quên append assistant message
❌ Thêm role khác ngoài user/assistant
❌ Gửi empty string làm content
❌ Không trim history, bill blowup
❌ Append response mà chưa check stop_reason
Áp dụng ngay
Bài tập 1: Xây chatbot 5-turn (20 phút)
Bài tập 2: Implement sliding window (15 phút)
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
6.7 - Hội thoại nhiều lượt (Multi-Turn Conversations)​
Modified April 20
Bài 6.7: Hội thoại nhiều lượt (Multi-Turn Conversations)​
Module: 2 — Gọi Claude qua API​
Thời gian ước tính: 20 phút​
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
✅ Giải thích tại sao Claude API stateless — không tự nhớ conversation​
•
✅ Tự quản lý message history trong code Python​
•
✅ Viết 3 helper function tái sử dụng: add_user_message, add_assistant_message, chat​
•
✅ Nhận diện và tránh các lỗi phổ biến với multi-turn (role alternating, history bloat)​
Mở đầu: Cuộc trò chuyện với người mất trí nhớ mỗi giây​
Hãy tưởng tượng bạn đang trò chuyện với một người bạn có chứng mất trí nhớ từng giây — mỗi khi bạn dứt lời, họ reset hoàn toàn. Bạn hỏi:​
Bạn: "Giải thích quantum computing."Họ: "Quantum computing là..."Bạn: "Viết 1 câu nữa đi."Họ: "Về cái gì?"​
Đó chính xác là tình trạng mặc định của Claude API — stateless hoàn toàn. Mỗi request là một cuộc gặp mới, Claude không nhớ đã nói gì trước đó.​
Bài này dạy bạn cách "ghi nhớ giùm Claude" — tự duy trì history trong code, gửi lại mỗi lần request. Đây là nền tảng cho mọi app chat, RAG, agent bạn xây sau này.​
Tại sao Claude lại stateless?​
3 lý do thiết kế​
1. Scalability​
Stateful system cần lưu state cho từng user — scale ra triệu user = khó khăn ngàn lần. Stateless = mỗi request độc lập, có thể phân phối đến bất kỳ server nào.​
2. Privacy​
Nếu Anthropic tự lưu history, họ phải lưu data của bạn. Stateless = data về user ở server của bạn, Anthropic chỉ thấy trong 1 request rồi xóa.​
Comments (0)
Help Center
Keyboard Shortcuts
