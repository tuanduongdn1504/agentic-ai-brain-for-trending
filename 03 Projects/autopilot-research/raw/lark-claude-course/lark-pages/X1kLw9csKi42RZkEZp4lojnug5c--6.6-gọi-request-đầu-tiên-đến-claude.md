# 6.6 - Gọi request đầu tiên đến Claude

**Source:** https://transform.sg.larksuite.com/wiki/X1kLw9csKi42RZkEZp4lojnug5c
**Wiki ID:** X1kLw9csKi42RZkEZp4lojnug5c
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
Transform Group

6.6 - Gọi request đầu tiên đến Claude

Last updated: Apr 20

Log In or Sign Up
6.6 - Gọi request đầu tiên đến Claude
Bài 6.6: Gọi request đầu tiên đến Claude
Mục tiêu học tập
Mở đầu: Từ "hiểu concept" đến "chạy code"
Cài đặt SDK
Cài package
Trong Jupyter notebook
Request đầu tiên — Full example
Cell 1: Setup
Cell 2: Tạo messages
Cell 3: Gọi API
Cell 4: Extract text
Đi sâu vào response object
Mỗi trường có ý nghĩa gì?
max_tokens — Cần lưu ý gì?
Ví dụ
Quy tắc chọn max_tokens
Messages — cấu trúc chi tiết
Single-turn (1 user message)
Multi-turn (conversation history)
Quy tắc cứng
Ví dụ thực chiến: Query về dữ liệu công ty
Tình huống
Bước 1: Setup
Bước 2: Câu hỏi đầu tiên
Bước 3: Đọc response
Bước 4: Xem usage
Kết quả
Case studies theo ngành
📊 Data Analyst
📝 Content Writer
🎧 Support Ops
Anti-patterns phổ biến
❌ Quên load_dotenv()
❌ messages không là list
❌ Access .content như string
❌ Không handle exceptions
❌ Set max_tokens quá cao "for safety"
Áp dụng ngay
Bài tập 1: "Hello World" với 3 câu hỏi khác nhau (15 phút)
Bài tập 2: Viết utility function (15 phút)
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
6.6 - Gọi request đầu tiên đến Claude​
Modified April 20
Bài 6.6: Gọi request đầu tiên đến Claude​
Module: 2 — Gọi Claude qua API​
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
✅ Cài đặt Anthropic Python SDK và cấu hình client​
•
✅ Thực hiện request đầu tiên với đầy đủ 4 tham số bắt buộc​
•
✅ Giải mã response object và extract text​
•
✅ Hiểu ý nghĩa của từng tham số trong messages.create()​
•
✅ Phân biệt user message và assistant message​
Mở đầu: Từ "hiểu concept" đến "chạy code"​
Sau 3 bài đầu, bạn đã biết:​
•
Claude có nhiều tier (Opus/Sonnet/Haiku)​
•
Request đi qua 5 bước từ client → server → API​
•
Cách lấy và bảo vệ API key​
Bây giờ, trong 20 phút, bạn sẽ chuyển từ biết sang làm. Chạy request thật. Nhìn response thật. Hiểu từng trường output.​
Đây là bài short but critical — mọi code sau trong khóa dựa trên pattern bạn học ở đây.​
Cài đặt SDK​
Anthropic có SDK chính thức cho Python, TypeScript, Go, Ruby, Java. Trong khóa này dùng Python.​
Cài package​
Trong virtual env của project (source .venv/bin/activate):​
​
Code block​
Bash
Copy
​
Comments (0)
Help Center
Keyboard Shortcuts
