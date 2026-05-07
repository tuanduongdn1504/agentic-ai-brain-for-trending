# 6.2 - Tổng quan các model của Claude

**Source:** https://transform.sg.larksuite.com/wiki/Is5QwjUXPifWClkdnqpluxo2gEb
**Wiki ID:** Is5QwjUXPifWClkdnqpluxo2gEb
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
Transform Group

6.2 - Tổng quan các model của Claude

Last updated: Apr 20

Log In or Sign Up
6.2 - Tổng quan các model của Claude
Bài 6.2: Tổng quan các model của Claude
Mục tiêu học tập
Mở đầu: Ba người thợ cho ba công việc
Bộ ba model: Opus, Sonnet, Haiku
♠ Opus — Model lớn nhất, thông minh nhất
♣ Sonnet — Workhorse cân bằng
♦ Haiku — Nhanh, rẻ, cho volume lớn
Đọc tên model
Alias vs snapshot
So sánh 3 tier
Quy tắc 10x
Khi nào dùng model nào?
Ma trận quyết định
Flow chart chọn model
Ví dụ thực chiến: Ước tính chi phí cho chatbot HR
Tình huống
Bước 1: Tính traffic
Bước 2: Tính token/tháng
Bước 3: Tính chi phí (3 scenario)
Bước 4: Quyết định
Case studies theo ngành
💰 Finance — Investment Analyst
📝 Publishing — Content moderation
⚖️ Legal — Contract review
🎧 Customer Support — First response
🔍 Research — Literature review
Context window — Yếu tố ít được chú ý
Quy tắc ngón cái
Khi nào cần context lớn?
Roadmap upgrade
Quy trình migration khi có model mới
Anti-patterns — Sai lầm chọn model
❌ "Luôn dùng model tốt nhất cho an toàn"
❌ "Dùng alias claude-sonnet-4-0 cho production"
❌ "Không chạy eval khi switch model"
❌ "Dùng Haiku cho agentic multi-step"
❌ "Chọn model theo giá, không theo use case"
Áp dụng ngay
Bài tập 1: Lập mapping cho app của bạn (15 phút)
Bài tập 2: Ước tính chi phí (10 phút)
Mẹo nâng cao
Mẹo 1: Dùng Haiku để "tiền xử lý" cho Sonnet
Mẹo 2: Tier based on confidence
Mẹo 3: Batch API cho Haiku
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
6.2 - Tổng quan các model của Claude​
Modified April 20
Bài 6.2: Tổng quan các model của Claude​
Module: 1 — Mở đầu​
Thời gian ước tính: 20 phút​
Mức độ: Cơ bản​
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
✅ Phân biệt 3 dòng model chính của Claude: Opus, Sonnet, Haiku​
•
✅ Đọc và hiểu tên model ID (ví dụ claude-sonnet-4-6-20260205)​
•
✅ Chọn model phù hợp cho từng use case theo 3 trục: chất lượng, tốc độ, chi phí​
•
✅ Ước tính chi phí API cho một workload thực tế​
•
✅ Biết khi nào cần migrate sang model mới​
Mở đầu: Ba người thợ cho ba công việc​
Hãy tưởng tượng bạn đang xây một căn nhà.​
Bạn thuê 3 người thợ với kỹ năng khác nhau:​
•
Bác phó cả giàu kinh nghiệm — giải được bài toán kết cấu phức tạp, tư vấn kiến trúc sáng tạo, xử lý tình huống chưa từng gặp. Nhưng tính phí $150/giờ và đi chậm.​
•
Anh thợ lành nghề — làm đúng 85% tác vụ trong kinh doanh. Nhanh, giá phải chăng ($30/giờ), chất lượng ổn định.​
•
Em thợ phụ trẻ — chạy việc vặt, sơn tường, lắp ốc vít đơn giản. Nhanh như chớp ($8/giờ), làm được khối lượng lớn.​
Nếu bạn thuê bác phó cả để sơn tường, bạn đang đốt tiền.Nếu bạn thuê em thợ phụ để thiết kế kết cấu, nhà bạn sẽ sập.​
Đây chính xác là cách team Claude được thiết kế. 3 dòng model — Opus, Sonnet, Haiku — đóng vai trò 3 người thợ đó. Và công việc của AI engineer không phải là "luôn dùng model tốt nhất", mà là chọn đúng model cho đúng tác vụ.​
Trong bài này, bạn sẽ học cách đọc "resume" của từng model, và ra quyết định chọn model có cơ sở — không phải đoán.​
Comments (0)
Help Center
Keyboard Shortcuts
