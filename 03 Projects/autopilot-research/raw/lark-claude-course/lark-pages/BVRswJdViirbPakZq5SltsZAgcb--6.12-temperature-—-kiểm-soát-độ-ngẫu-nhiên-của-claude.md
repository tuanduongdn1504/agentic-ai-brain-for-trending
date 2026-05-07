# 6.12 - Temperature — Kiểm soát độ ngẫu nhiên của Claude

**Source:** https://transform.sg.larksuite.com/wiki/BVRswJdViirbPakZq5SltsZAgcb
**Wiki ID:** BVRswJdViirbPakZq5SltsZAgcb
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
6.47 - Prompt caching — Khái niệm & ROI
6.48 - Rules of prompt caching — Breakpoints + invalidation
Transform Group

6.12 - Temperature — Kiểm soát độ ngẫu nhiên của Claude

Last updated: Apr 20

Log In or Sign Up
6.12 - Temperature — Kiểm soát độ ngẫu nhiên của Claude
Bài 6.12: Temperature — Kiểm soát độ ngẫu nhiên của Claude
Mục tiêu học tập
Mở đầu: "Núm điều chỉnh sáng tạo"
Tái cập lại quá trình generation
Temperature làm gì?
Temperature = 0 (deterministic)
Temperature = 0.5 (balanced)
Temperature = 1.0 (max creative)
So sánh 3 setting cụ thể
Temperature = 0
Temperature = 0.5
Temperature = 1.0
Khi nào dùng temperature nào?
Low (0.0 - 0.3): Factual, deterministic
Medium (0.4 - 0.7): Balanced
High (0.8 - 1.0): Creative
Above 1.0?
Thêm vào chat function
Dùng
Ví dụ thực chiến: Cùng prompt, 2 temperature
Prompt
Temperature = 0.0
Temperature = 1.0
Case studies theo ngành
💻 Developer Tools — Code generation
📝 Copywriting — Ad variants
📊 Data Analysis — Insights
⚖️ Legal — Contract analysis
🎓 Education — Tutoring
Interaction với system prompt
Ví dụ kết hợp
Anti-patterns
❌ Set temperature=0 cho chatbot general
❌ Set temperature=1 cho data extraction
❌ Tune temperature thay vì fix prompt
❌ Hardcode temp không document
❌ Test temp=0 rồi deploy temp=1
Áp dụng ngay
Bài tập 1: Temperature ladder (20 phút)
Bài tập 2: Pick temp cho use case (15 phút)
Mẹo nâng cao
Mẹo 1: Seed cho reproducibility (không có trên Anthropic)
Mẹo 2: Ensemble với temp=1
Mẹo 3: Adaptive temperature
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
6.12 - Temperature — Kiểm soát độ ngẫu nhiên của Claude​
Modified April 20
Bài 6.12: Temperature — Kiểm soát độ ngẫu nhiên của Claude​
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
✅ Giải thích cách temperature ảnh hưởng đến sampling của Claude​
•
✅ Chọn temperature phù hợp cho từng loại tác vụ (factual, creative, brainstorm)​
•
✅ Hiểu sự khác biệt giữa temperature=0, 0.5, 1.0​
•
✅ Update chat function accept temperature parameter​
•
✅ Tránh sai lầm thường gặp khi tune temperature​
Mở đầu: "Núm điều chỉnh sáng tạo"​
Hãy tưởng tượng bạn đang điều khiển mixer trong studio âm nhạc. Có 1 núm vặn:​
•
Xoay sang trái → âm thanh dự đoán được, theo format classical​
•
Xoay sang phải → âm thanh bất ngờ, jazzy, improvisational​
Cả 2 đều "đúng" — tùy thể loại nhạc bạn muốn.​
Temperature của Claude y hệt núm đó. Không có "temperature tốt". Chỉ có temperature phù hợp cho task.​
Hiểu temperature = control được Claude. Không hiểu = random behavior không giải thích được.​
Tái cập lại quá trình generation​
Ở bài 6.4 bạn đã học Claude generate text qua 4 bước:Tokenize → Embed → Contextualize → Generation.​
Bước generation cụ thể:​
​
Code block​
Plain Text
Copy
┌───────────────────────────────────────────────┐​
​
Comments (0)
Help Center
Keyboard Shortcuts
