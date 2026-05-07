# 6.4 - Vòng đời một request — Từ client đến Claude và ngược lại

**Source:** https://transform.sg.larksuite.com/wiki/JJQcwnU7Vi31uqkABYbl8GWrgad
**Wiki ID:** JJQcwnU7Vi31uqkABYbl8GWrgad
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
Transform Group

6.4 - Vòng đời một request — Từ client đến Claude và ngược lại

Last updated: Apr 20

Log In or Sign Up
6.4 - Vòng đời một request — Từ client đến Claude và ngược lại
Bài 6.4: Vòng đời một request — Từ client đến Claude và ngược lại
Mục tiêu học tập
Mở đầu: Điều gì thực sự xảy ra trong 3 giây ấy?
5 bước của một request
Bước 1-2: Vì sao LUÔN phải có server trung gian?
3 lý do
Architecture điển hình
Các tham số bắt buộc trong mỗi request
Giải thích từng trường
Bước 3: Bên trong Claude — 4 giai đoạn
1. Tokenization
2. Embedding
3. Contextualization
4. Generation
Bước 4-5: Response trở về
Trường quan trọng
Ví dụ thực chiến: Debug một issue kỳ lạ
Tình huống
Phân tích theo vòng đời
Ví dụ code handle stop_reason
Case studies theo ngành
💻 Developer — API cost blowup
📊 Data Engineer — Batch processing chậm
🎧 Customer Support — Response kỳ quặc
Anti-patterns — Lỗi vòng đời phổ biến
❌ Gọi API từ client
❌ Không handle stop_reason
❌ Gửi history vô tận
❌ Không log usage
❌ Hardcode max_tokens=4096 universally
Áp dụng ngay
Bài tập 1: Vẽ lại flow cho app của bạn (10 phút)
Bài tập 2: Đọc 1 response thật (5 phút)
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
6.4 - Vòng đời một request — Từ client đến Claude và ngược lại​
Modified April 20
Bài 6.4: Vòng đời một request — Từ client đến Claude và ngược lại​
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
✅ Mô tả 5 bước trong vòng đời của một request đến Claude API​
•
✅ Giải thích vì sao không bao giờ gọi API trực tiếp từ client-side​
•
✅ Hiểu điều gì xảy ra bên trong Claude (tokenization → embedding → contextualization → generation)​
•
✅ Nhận diện các tham số bắt buộc trong mỗi request​
•
✅ Đọc và interpret được object response, đặc biệt trường stop_reason​
Mở đầu: Điều gì thực sự xảy ra trong 3 giây ấy?​
Bạn gõ vào app chat: "Giải thích quantum computing trong 1 câu." — nhấn Enter. 3 giây sau, câu trả lời hiện ra.​
Giữa khoảng thời gian đó, ít nhất 5 server khác nhau đã liên lạc với nhau, hàng tỷ phép tính đã được thực hiện, và một sequence token đã được chọn từ hàng triệu khả năng. Nếu bạn coi toàn bộ quá trình này là hộp đen, bạn sẽ:​
•
Không biết debug khi app chậm bất thường​
•
Không biết tại sao thỉnh thoảng câu trả lời bị cắt giữa chừng​
•
Không hiểu vì sao cost tính như vậy​
•
Không biết cần optimize ở đâu​
Bài này mở hộp đen đó. Xong bài, bạn sẽ có mô hình mental model rõ ràng về mỗi request — nền tảng cho mọi bài sau.​
5 bước của một request​
​
Code block​
Plain Text
Copy
​
Comments (0)
Help Center
Keyboard Shortcuts
