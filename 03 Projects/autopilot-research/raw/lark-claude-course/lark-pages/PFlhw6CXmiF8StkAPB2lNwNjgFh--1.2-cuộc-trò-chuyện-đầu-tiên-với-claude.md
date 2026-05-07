# 1.2 - Cuộc trò chuyện đầu tiên với Claude

**Source:** https://transform.sg.larksuite.com/wiki/PFlhw6CXmiF8StkAPB2lNwNjgFh
**Wiki ID:** PFlhw6CXmiF8StkAPB2lNwNjgFh
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
Slide: Claude 101.pdf
1.0 - Claude 101 — Tổng quan khóa học
1.1 - Claude là gì?
1.2 - Cuộc trò chuyện đầu tiên với Claude
1.3 - Tối ưu kết quả — AI Fluency & Iteration
1.4 - Claude Desktop — Chat, Cowork, Code
1.5 - Projects — Không gian làm việc chuyên dụng
1.6 - Artifacts — Sáng tạo tương tác
1.7 - Skills — Đóng gói quy trình
1.8 - Connectors — Kết nối tools qua MCP
1.9 - Enterprise Search — Hỏi cả tổ chức
1.10 - Research mode — Đào sâu đa nguồn
1.11 - Claude theo vai trò — Use cases by role
1.12 - Các cách khác làm việc với Claude
1.13 - Tổng kết và bước tiếp theo
1.14 - Quiz tổng hợp & Chứng nhận
02 - Claude Code 101
03 - Claude Cowork
04 - Claude Code in Action
05 - AI Fluency: Framework & Foundations
06 - Building with the Claude API
07 - Introduction to Model Context Protocol
08 - AI Fluency for Educators
09 - AI Fluency for Students
10 - Model Context Protocol: Advanced Topics
13 - Teaching AI Fluency
14 - AI Fluency for nonprofits
15 - Introduction to agent skills
16 - Introduction to subagents
17 - AI Capabilities and Limitations
📣
Bổ sung course
Transform Group

1.2 - Cuộc trò chuyện đầu tiên với Claude

Last updated: Apr 20

Log In or Sign Up
1.2 - Cuộc trò chuyện đầu tiên với Claude
Bài 02: Cuộc trò chuyện đầu tiên với Claude
Mục tiêu học tập
Mở đầu: Trang giấy trắng và một cộng sự
Tổng quan interface claude.ai
Sidebar — trung tâm điều hướng
Chat area — nơi làm việc
Viết prompt hiệu quả — Công thức 3 phần
1. CONTEXT — Set the stage
2. TASK — Define clearly
3. RULES — Specify constraints
Ví dụ thực chiến: Từ 1 dòng → prompt đầy đủ
Tình huống
Prompt cấp 1 — Yếu (khởi đầu)
Prompt cấp 2 — Better (có task rõ)
Prompt cấp 3 — Strong (đủ 3 phần)
4D Framework for AI Fluency — nền tảng cho prompt framework
Thêm context qua file upload
Các loại file Claude đọc được
Cách upload
Ví dụ use cases với file upload
Pro tip: Đặt tên file descriptive
Search & Tools — mở rộng khả năng của Claude
Web search
Connectors
Pro tip
Chọn model phù hợp với task
Model selector
Extended thinking mode
Iterate — Power move thực sự
4 cách iterate
Khi nào restart chat mới?
Personalize Claude — Memory, Styles, Preferences
Memory
Styles
Preferences
Ví dụ theo ngành
💼 Sales Rep — prompt prep meeting
📣 Marketing Manager — repurpose content
💰 Finance Analyst — analyze file
⚖️ Legal Counsel — review contract
🎓 Teacher — personalize lesson plan
Anti-patterns — Sai lầm prompt thường gặp
❌ Prompt 1 dòng kỳ vọng "magic"
❌ Nhồi quá nhiều task vào 1 prompt
❌ Quá vague về độ dài / format
❌ Không dùng follow-up, restart chat liên tục
❌ Không upload file, paste text dài
Áp dụng ngay
Bài tập 1: Viết 3 prompts theo công thức C-T-R (15 phút)
Bài tập 2 (optional): Setup Styles + Memory (10 phút)
Tóm tắt bài học
1.2 - Cuộc trò chuyện đầu tiên với Claude​
Modified April 20
Bài 02: Cuộc trò chuyện đầu tiên với Claude​
Module: Làm quen với Claude​
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
Slide: Claude 101.pdf​
​
​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Bắt đầu một cuộc trò chuyện mới với Claude và navigate interface thành thạo​
•
✅ Viết prompt hiệu quả theo công thức Context + Task + Rules​
•
✅ Upload files và images để cung cấp context cho Claude​
•
✅ Iterate thông qua follow-up messages để refine response​
•
✅ Cấu hình Styles, Memory, Preferences để personalize trải nghiệm​
​
​
Mở đầu: Trang giấy trắng và một cộng sự​
Hình dung: bạn đang nhìn một trang giấy trắng. Một project lớn, phức tạp — bạn không biết bắt đầu từ đâu.​
Cảm giác đó, bạn đã có bao nhiêu lần trong tuần?​
•
Ngồi trước Word để viết báo cáo cho sếp lúc 5pm​
•
Mở Excel với 8 sheet người khác để lại​
•
Bắt đầu một research về ngành bạn chưa từng làm​
•
Viết email "delicate" — phải xin lỗi khách hàng nhưng không thừa nhận lỗi​
•
Làm slide deck cho buổi present với board chiều nay​
Trang giấy trắng là điểm ma sát lớn nhất của knowledge work. Không phải vì bạn không có ý tưởng — mà vì bạn đang làm một mình.​
Giờ mường tượng lại. Nhưng lần này, cạnh bạn là một cộng sự thông minh, kiên nhẫn, sẵn sàng break down vấn đề cùng bạn. Bạn nói ra suy nghĩ lộn xộn; cộng sự helps organize. Bạn draft; cộng sự helps refine. Bạn stuck; cộng sự helps unlock.​
Đây là khoảnh khắc "aha" với Claude. Nhưng để đến được khoảnh khắc đó, bạn cần học cách nói chuyện — không phải theo nghĩa "ra lệnh cho máy", mà theo nghĩa "brief một cộng sự giỏi".​
​
​
Comments (0)
Help Center
Keyboard Shortcuts
