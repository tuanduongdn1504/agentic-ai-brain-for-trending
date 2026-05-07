# 6.1 - Chào mừng bạn đến với khóa học

**Source:** https://transform.sg.larksuite.com/wiki/PTYswnmUgiSyAck11SelF3nAgrd
**Wiki ID:** PTYswnmUgiSyAck11SelF3nAgrd
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
Transform Group

6.1 - Chào mừng bạn đến với khóa học

Last updated: Apr 20

Log In or Sign Up
6.1 - Chào mừng bạn đến với khóa học
Bài 6.1: Chào mừng bạn đến với khóa học
Mục tiêu học tập
Mở đầu: Khoảng cách giữa "biết Claude" và "xây app với Claude"
Khóa học này dạy gì?
Foundation (Module 1-4)
Build (Module 5-7)
Scale (Module 8-11)
Khóa học này KHÔNG dạy gì?
❌ Không dạy Machine Learning lý thuyết
❌ Không dạy fine-tuning
❌ Không dạy frontend / UX chatbot
❌ Không dạy deployment / DevOps
So sánh với các nguồn học khác
Ví dụ thực chiến: Lộ trình 6 tuần của một học viên điển hình
Tình huống
Tuần 1: Foundation
Tuần 2: Prompt engineering
Tuần 3: Eval
Tuần 4: RAG
Tuần 5: Tool use + caching
Tuần 6: Deploy + ship
Những gì chúng ta sẽ làm trong khóa này
Project 1: Chatbot cơ bản (sau Module 2-3)
Project 2: Eval suite (sau Module 4)
Project 3: Tool-using assistant (sau Module 5-6)
Project 4: RAG + MCP + Agent (sau Module 7-9)
Ứng dụng thực tế: Claude Code và Computer Use
💻 Claude Code
🖥️ Computer Use
Chuẩn bị môi trường (cài luôn bây giờ)
Bước 1: Cài Python 3.9+
Bước 2: Cài JupyterLab
Bước 3: Tạo project folder
Bước 4: Tạo notebook đầu tiên
Anti-patterns — Sai lầm người mới hay mắc
❌ Lướt nhanh qua bài early để tới "phần hay"
❌ Cố làm 2 module cùng lúc
❌ Bỏ exercise để tiết kiệm thời gian
Áp dụng ngay
Bài tập 1: Viết mục tiêu cá nhân (10 phút)
Bài tập 2: Cài môi trường & chạy Hello World (15 phút)
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
6.1 - Chào mừng bạn đến với khóa học​
Modified April 20
Bài 6.1: Chào mừng bạn đến với khóa học​
Module: 1 — Mở đầu​
Thời gian ước tính: 15 phút​
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
​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Giải thích vị trí của khóa học này trong hành trình học Claude của bạn​
•
✅ Xác định kỳ vọng thực tế về những gì khóa học dạy và không dạy​
•
✅ Thiết lập Python environment và Jupyter Notebook sẵn sàng cho bài đầu tiên​
•
✅ Biết nơi cần đến khi gặp lỗi hoặc cần cộng đồng hỗ trợ​
​
​
Mở đầu: Khoảng cách giữa "biết Claude" và "xây app với Claude"​
Hãy tưởng tượng bạn là một developer có 5 năm kinh nghiệm. Bạn đã dùng ChatGPT hàng ngày, thậm chí viết vài script nhỏ gọi OpenAI API. Một hôm, sếp đặt trên bàn bạn task:​
"Tuần sau ship cho tôi một nội bộ chatbot trả lời câu hỏi của 200 nhân viên về policy HR, tích hợp vào Slack, có log lại câu hỏi cho team legal review, và không được tốn quá $500/tháng."​
Bạn ngồi xuống, mở IDE, và... dừng lại. Vì bạn nhận ra:​
•
Prompt nào đủ tin cậy để không trả lời nhầm chính sách lương?​
•
Làm sao đo được "tin cậy" bằng con số cụ thể?​
•
Tool use hay RAG cho trường hợp này?​
•
Khi 200 người hỏi trùng câu, làm sao không trả tiền 200 lần?​
•
Log thế nào cho legal đọc được nhưng không leak PII?​
•
Nếu Claude ra bản mới, app của tôi có tự migrate được không?​
Đây chính xác là khoảng cách giữa biết Claude và xây app production với Claude. Khóa học này lấp đầy khoảng cách đó.​
Trong 82 bài sắp tới, bạn sẽ không học thêm tính năng mới của Claude — bạn sẽ học cách dùng những tính năng đã có để xây một hệ thống có thể ship, có thể đo, có thể scale, và có thể maintain.​
​
​
Comments (0)
Help Center
Keyboard Shortcuts
