# 1.1 - Claude là gì?

**Source:** https://transform.sg.larksuite.com/wiki/LuirwmJsuiphkgkDJxulscVOgxh
**Wiki ID:** LuirwmJsuiphkgkDJxulscVOgxh
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

1.1 - Claude là gì?

Last updated: Apr 20

Log In or Sign Up
1.1 - Claude là gì?
Bài 01: Claude là gì?
Mục tiêu học tập
Mở đầu: Ý tưởng của bạn cần một đối tác
Claude — Định nghĩa kỹ thuật
Constitutional AI — Nền tảng đạo đức của Claude
Steerable — Có thể điều hướng
Claude khác gì một chatbot thông thường?
Năng lực cốt lõi của Claude
1. Writing & content creation
2. Research & analysis
3. Coding assistance
4. Reasoning & problem-solving
5. Learning
Các cách truy cập Claude
Claude.ai (và desktop / mobile app) — trọng tâm của khóa này
Claude Code
Claude và Slack
Claude for Excel
Claude for Chrome
Lesson reflection — Claude có thể giúp gì cho bạn?
Ví dụ theo ngành
💼 Sales Rep
📣 Marketing Manager
💰 Finance Analyst
⚖️ Legal Counsel
🎓 Educator / L&D
Anti-patterns — Sai lầm thường gặp khi mới dùng Claude
❌ Coi Claude như Google
❌ Không dùng file upload
❌ Dùng sai model cho task
❌ Không trust, không verify
Áp dụng ngay
Bài tập 1: Claude audit công việc tuần này (10 phút)
Bài tập 2 (optional): Prompt đầu tiên với Claude (5 phút)
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
1.1 - Claude là gì?​
Modified April 20
Bài 01: Claude là gì?​
Module: Làm quen với Claude​
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
Slide: Claude 101.pdf​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Giải thích Claude là gì và các nguyên tắc thiết kế đằng sau (Constitutional AI)​
•
✅ Mô tả năng lực cốt lõi của Claude và phân biệt với một chatbot thông thường​
•
✅ Nhận diện các cách khác nhau để truy cập Claude (web, desktop, mobile, và các biến thể chuyên biệt)​
•
✅ Kể ra ít nhất 3 loại công việc bạn có thể bắt đầu giao cho Claude ngay tuần này​
Mở đầu: Ý tưởng của bạn cần một đối tác​
Hãy thử mường tượng cảnh này.​
Hôm qua, ngồi trong quán cà phê, bạn có một ý tưởng — một startup? một chiến dịch marketing? một dự án nội bộ? Một cái gì đó đủ lớn để bạn không ngủ được. Tối đó, bạn note vội 3 dòng vào iPhone rồi đi ngủ.​
Sáng nay, mở laptop, bạn định triển khai. Nhưng ngay lập tức, cái tường chắn quen thuộc dựng lên:​
•
"Để ý tưởng này thành form, cần một deck. Deck cần data thị trường. Data thị trường cần research 5-10 đối thủ."​
•
"Nhưng để research cho nghiêm túc, cần ít nhất nửa ngày. Ai có nửa ngày giữa 4 cuộc họp hôm nay?"​
•
"Thôi để cuối tuần."​
Cuối tuần, có những việc khác. Tuần sau, ý tưởng đã nguội. Tháng sau, bạn không còn nhớ 3 dòng trên iPhone nói gì.​
Đây là cái chết thầm lặng của 90% ý tưởng tốt. Không phải vì chúng tệ. Mà vì giữa "ý tưởng" và "bản đầu tiên có thể show cho ai đó" là một khoảng cách làm việc tay chân khổng lồ — research, take notes, cross-reference, organize, viết draft, làm slide, gửi email setup meeting…​
Bây giờ thử mường tượng lại. Nhưng lần này, bên cạnh bạn có một thinking partner — một cộng sự:​
•
Nhớ 3 dòng note bạn gõ tối qua (Memory)​
•
Đọc cùng bạn 20 báo cáo thị trường, trả về 2 trang summary có citation (Research)​
•
Đã có sẵn brand guide của team, biết tông giọng bạn hay viết (Projects)​
Comments (0)
Help Center
Keyboard Shortcuts
