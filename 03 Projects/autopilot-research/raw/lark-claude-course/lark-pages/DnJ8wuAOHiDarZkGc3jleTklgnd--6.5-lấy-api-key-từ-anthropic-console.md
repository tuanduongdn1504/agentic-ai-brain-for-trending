# 6.5 - Lấy API key từ Anthropic Console

**Source:** https://transform.sg.larksuite.com/wiki/DnJ8wuAOHiDarZkGc3jleTklgnd
**Wiki ID:** DnJ8wuAOHiDarZkGc3jleTklgnd
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
Transform Group

6.5 - Lấy API key từ Anthropic Console

Last updated: Apr 20

Log In or Sign Up
6.5 - Lấy API key từ Anthropic Console
Bài 6.5: Lấy API key từ Anthropic Console
Mục tiêu học tập
Mở đầu: API key là "thẻ tín dụng" của bạn
Quy trình 5 bước lấy API key
Bước 1: Vào Anthropic Console
Bước 2: Nạp credit (nếu chưa có)
Bước 3: Navigate đến API Keys page
Bước 4: Create Key
Bước 5: Copy key và lưu an toàn
Lưu trữ API key an toàn
Setup chuẩn với .env
Tạo file .env.example (best practice)
Nhiều environment — nhiều key
Naming convention
Quản lý key qua thời gian
Rotate định kỳ (khuyến nghị 3-6 tháng)
Check usage định kỳ
Khi nào cần revoke ngay
Ví dụ thực chiến: Setup hoàn chỉnh cho course
Bước 1: Tạo project
Bước 2: Tạo .gitignore
Bước 3: Tạo .env
Bước 4: Tạo .env.example
Bước 5: Setup venv + install
Bước 6: Test
Bước 7: Init git
Case studies theo ngành
💻 Startup Tech — Multi-tenant SaaS
📊 Data Team — Shared notebook
⚖️ Legal / Enterprise — Compliance
Anti-patterns — Sai lầm bảo mật
❌ Commit .env vào Git
❌ Share key qua Slack / email
❌ Để key trong Docker image
❌ Log key vào log file
❌ 1 key cho tất cả
Áp dụng ngay
Bài tập 1: Lấy API key và test (15 phút)
Bài tập 2: Tự audit security (10 phút)
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
6.5 - Lấy API key từ Anthropic Console​
Modified April 20
Bài 6.5: Lấy API key từ Anthropic Console​
Module: 2 — Gọi Claude qua API​
Thời gian ước tính: 10 phút​
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
✅ Tạo tài khoản Anthropic và lấy API key đầu tiên​
•
✅ Lưu trữ API key an toàn (không leak vào Git)​
•
✅ Thiết lập workspace và quản lý nhiều key cho dự án khác nhau​
•
✅ Nhận diện cảnh báo bảo mật quan trọng khi xử lý API key​
Mở đầu: API key là "thẻ tín dụng" của bạn​
Mỗi API key của Anthropic giống như một thẻ tín dụng không giới hạn hạn mức nối vào credit của bạn. Ai có key đó đều có thể:​
•
Gọi Claude không giới hạn request​
•
Tiêu đến hạn mức tín dụng bạn đã nạp​
•
Trong trường hợp xấu: để lại log với thông tin nhạy cảm trên server của kẻ xấu​
Đã có rất nhiều case developer push API key lên GitHub public → 5 phút sau bot quét key → key bị dùng làm proxy miễn phí → bill vài ngàn $.​
Bài này mất 10 phút — nhưng nếu làm sai có thể tốn vài triệu. Đọc kỹ.​
Quy trình 5 bước lấy API key​
Bước 1: Vào Anthropic Console​
Mở trình duyệt, vào: console.anthropic.com​
Nếu chưa có tài khoản:​
•
Click "Sign up"​
•
Đăng nhập bằng Google / GitHub / email​
Comments (0)
Help Center
Keyboard Shortcuts
