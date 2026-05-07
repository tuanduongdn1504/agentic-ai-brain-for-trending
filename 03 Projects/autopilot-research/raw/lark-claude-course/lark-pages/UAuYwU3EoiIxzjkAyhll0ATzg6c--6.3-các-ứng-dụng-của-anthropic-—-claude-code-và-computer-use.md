# 6.3 - Các ứng dụng của Anthropic — Claude Code và Computer Use

**Source:** https://transform.sg.larksuite.com/wiki/UAuYwU3EoiIxzjkAyhll0ATzg6c
**Wiki ID:** UAuYwU3EoiIxzjkAyhll0ATzg6c
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
Transform Group

6.3 - Các ứng dụng của Anthropic — Claude Code và Computer Use

Last updated: Apr 20

Log In or Sign Up
6.3 - Các ứng dụng của Anthropic — Claude Code và Computer Use
Bài 6.3: Các ứng dụng của Anthropic — Claude Code và Computer Use
Mục tiêu học tập
Mở đầu: Hai "đứa con" tiêu biểu của Anthropic
Claude Code — Terminal-based coding agent
Tại sao Claude Code là landmark agent?
Những pattern bạn sẽ học lại từ Claude Code
Computer Use — Claude điều khiển desktop
Computer Use vs Claude Code
Tại sao Computer Use quan trọng?
Cả hai là agents — và agents có 4 tính chất
1. Tool integration
2. Multi-step execution
3. Environment interaction
4. Autonomous problem-solving
Ví dụ thực chiến: Một session Claude Code điển hình
Tình huống
Bước 1: Bạn prompt
Bước 2: Claude lập plan (tự hiển thị)
Bước 3: Claude thực thi (hiển thị từng bước)
Bước 4: Claude báo cáo
Kết quả
Case studies theo ngành: Ai dùng các app này?
💻 Software Engineering — Startup 20 người
🎧 Customer Support — Ops team
📊 Finance — Month-end close
🏭 Manufacturing — Inventory sync
Anti-patterns — Khi KHÔNG nên dùng agent
❌ Dùng agent cho task 1-shot đơn giản
❌ Dùng Computer Use khi có API
❌ Deploy agent không có observability
❌ Cho agent full access production không có sandbox
Áp dụng ngay
Bài tập 1: Cài Claude Code và chạy thử (15 phút)
Bài tập 2: Lập danh sách task cho app của bạn (10 phút)
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
6.3 - Các ứng dụng của Anthropic — Claude Code và Computer Use​
Modified April 20
Bài 6.3: Các ứng dụng của Anthropic — Claude Code và Computer Use​
Module: 1 — Mở đầu​
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
✅ Giải thích Claude Code và Computer Use là gì, khác nhau thế nào​
•
✅ Nhận diện chúng là "agent" — và tại sao đây là case study xuyên khóa​
•
✅ Mô tả các pattern kỹ thuật (tool use, multi-step, environment interaction) xuất hiện trong cả hai​
•
✅ Biết mình sẽ mổ xẻ hai ứng dụng này ở bài nào của khóa​
Mở đầu: Hai "đứa con" tiêu biểu của Anthropic​
Anthropic không chỉ là công ty làm model. Họ cũng xây app sản phẩm để:​
1.
Chứng minh model họ đủ tốt cho use case thực​
2.
Đẩy biên giới kỹ thuật về agent design​
3.
Làm reference cho cộng đồng dev​
Hai app đáng chú ý nhất — và cũng là hai case study xuyên khóa:​
•
Claude Code (công bố 02/2025) — Agent coding chạy trong terminal, đã thành "mặc định" của dev stack nhiều công ty lớn​
•
Computer Use (công bố 10/2024) — Bộ tool cho Claude điều khiển máy tính desktop, mở đầu cho làn sóng "browser agents" và "computer agents"​
Hai app này không phải để bạn dùng thay thế việc học, mà để bạn hiểu ngược — khi nào đã học hết kỹ thuật trong khóa này, nhìn lại hai app này, bạn sẽ thấy: "À, đây là tool use multi-turn. Đây là environment inspection. Đây là chaining workflow."​
Claude Code — Terminal-based coding agent​
Comments (0)
Help Center
Keyboard Shortcuts
