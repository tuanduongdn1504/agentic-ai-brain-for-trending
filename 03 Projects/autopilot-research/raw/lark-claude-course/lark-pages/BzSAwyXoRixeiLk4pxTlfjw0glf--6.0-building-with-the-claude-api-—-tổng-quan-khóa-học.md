# 6.0 - Building with the Claude API — Tổng quan khóa học

**Source:** https://transform.sg.larksuite.com/wiki/BzSAwyXoRixeiLk4pxTlfjw0glf
**Wiki ID:** BzSAwyXoRixeiLk4pxTlfjw0glf
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
Transform Group

6.0 - Building with the Claude API — Tổng quan khóa học

Last updated: Apr 20

Log In or Sign Up
6.0 - Building with the Claude API — Tổng quan khóa học
Building with the Claude API — Tổng quan khóa học
Tại sao bạn nên học khóa này?
Bạn sẽ học được gì?
Về tư duy
Về kỹ năng
Về thực hành
Lộ trình 82 bài học
Cách học hiệu quả nhất
Quy tắc 60/30/10 cho khóa này
3 nhóm người đọc — 3 cách tiếp cận
Những gì bạn cần chuẩn bị
Bắt buộc
Nên có
Không cần
Triết lý xuyên suốt khóa học
1. "Prompt là code" (Prompts are code)
2. "Eval-driven development" (EDD)
3. "Delegate, don't converse" (Ủy thác, không trò chuyện)
4. "Tool use là cửa ngõ vào agents"
5. "MCP là standard, không phải tùy chọn"
Một lời khuyên từ kinh nghiệm thực tế
Bạn sẵn sàng chưa?
Bắt đầu nào
Phản hồi và hỗ trợ
6.0 - Building with the Claude API — Tổng quan khóa học​
Modified April 20
Building with the Claude API — Tổng quan khóa học​
Khóa học: Xây dựng ứng dụng với Claude API​
Phiên bản: 2.0 — Bản tiếng Việt chuyên sâu cho developer và kỹ sư AI​
Dựa trên: Anthropic Academy — Claude with the Anthropic API + Introduction to Model Context Protocol​
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
Tại sao bạn nên học khóa này?​
Hãy thành thật một chút. Mỗi tuần bạn dành bao nhiêu giờ để làm những việc sau?​
•
Đọc lại tài liệu API, copy-paste code snippet, hy vọng nó chạy​
•
Prompt model xong thấy output "gần đúng" nhưng không đủ tin cậy để đưa vào sản phẩm​
•
Không biết vì sao cùng một prompt mà lần này ra tốt, lần sau ra dở​
•
Xây demo đẹp trong 2 giờ nhưng mất 2 tuần để ra production​
•
Nghe nói về RAG, tool use, MCP, agents... nhưng chưa bao giờ tự tin viết được từ đầu​
•
Chi phí API tăng vùn vụt mỗi khi có nhiều user, không biết cách tối ưu​
Nếu bạn dành hơn 5 giờ mỗi tuần cho những việc trên, bạn đang ở đúng chỗ.​
Khóa học này không dạy bạn "prompt một cái gì đó với Claude". Nó dạy bạn xây ứng dụng production-grade với Claude — từ request HTTP đầu tiên, qua prompt engineering, evaluation, tool use, RAG, MCP, agents, cho đến Claude Code. Nền tảng bạn xây xong sẽ dùng được cho bất kỳ use case nào của AI trong 5 năm tới.​
Bạn sẽ học được gì?​
Sau khi hoàn thành 82 bài học, bạn sẽ có thể:​
Về tư duy​
•
Hiểu kiến trúc đầy đủ của một ứng dụng AI — từ client, qua server, đến API và ngược lại​
•
Phân biệt được 3 lớp trừu tượng: prompt → workflow → agent — biết lúc nào dùng cái nào​
•
Suy nghĩ như một AI engineer: eval-driven development thay vì "prompt rồi hy vọng"​
•
Biết khi nào dùng MCP, khi nào viết tool từ đầu — và tại sao điều đó quan trọng cho scale​
Về kỹ năng​
•
Gọi Claude API từ Python một cách chuẩn, an toàn (không leak API key)​
Comments (0)
Help Center
Keyboard Shortcuts
