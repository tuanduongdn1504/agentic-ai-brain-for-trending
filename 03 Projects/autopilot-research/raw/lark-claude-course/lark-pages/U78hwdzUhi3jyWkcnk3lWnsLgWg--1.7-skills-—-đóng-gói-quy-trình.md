# 1.7 - Skills — Đóng gói quy trình

**Source:** https://transform.sg.larksuite.com/wiki/U78hwdzUhi3jyWkcnk3lWnsLgWg
**Wiki ID:** U78hwdzUhi3jyWkcnk3lWnsLgWg
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

1.7 - Skills — Đóng gói quy trình

Last updated: Apr 20

Log In or Sign Up
1.7 - Skills — Đóng gói quy trình
Bài 07: Skills — Đóng gói quy trình
Mục tiêu học tập
Mở đầu: Từ "biết" đến "làm đúng mỗi lần"
Skills là gì?
Cách Skills hoạt động — progressive disclosure
2 loại Skills
1. Anthropic Skills (built-in)
2. Custom Skills
Enable Skills
Cho Pro / Max users
Cho Enterprise plans
Cho Team plans
Sau khi enable
Dùng Skills trong practice
Examples prompts invoke Skills
Khi Claude dùng Skill
File execution — working với files thực tế
Supported file operations
Requirement: network access toggle
Security considerations
✅ Safe practices
⚠️ Red flags khi install custom Skill
Recommendation
Tạo Custom Skill đầu tiên
Process — 4 bước
Bước 1: Start new chat, declare intent
Bước 2: Answer Claude's questions
Bước 3: Upload reference materials
Bước 4: Save skill
See your skills
Iteration
Case study: Custom Skill "quarterly-variance-analysis"
Setup conversation
Skill structure generated
Sau khi save
Skills vs. Projects — Khi nào dùng cái nào?
Projects = knowledge hubs
Skills = procedural machines
Chúng complement nhau
Bảng so sánh
Use case kết hợp
Ví dụ theo ngành
💼 Sales Rep
📣 Marketing Manager
💰 Finance Analyst
⚖️ Legal Counsel
🏥 Medical Writer
🎓 Curriculum Developer
📊 Data Analyst
👥 HR Manager
Anti-patterns với Skills
1.7 - Skills — Đóng gói quy trình​
Modified April 20
Bài 07: Skills — Đóng gói quy trình​
Module: Tổ chức công việc​
Thời gian ước tính: 15 phút​
Mức độ: Trung cấp​
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
✅ Giải thích Skills là gì và cách Claude load Skills động​
•
✅ Nhận diện Anthropic's built-in Skills cho document creation​
•
✅ Enable và manage Skills trong settings​
•
✅ Tạo Custom Skill đầu tiên qua một cuộc trò chuyện với Claude​
•
✅ Phân biệt Skills vs. Projects và khi nào dùng cái nào​
•
✅ Hiểu về security considerations khi dùng Skills từ external sources​
Mở đầu: Từ "biết" đến "làm đúng mỗi lần"​
Bạn đã làm quarterly variance analysis ở công ty được 3 năm. Quy trình:​
1.
Pull số P&L từ ERP​
2.
So với budget sheet​
3.
Flag variance > 15% của revenue, > 10% của expenses​
4.
Categorize nguyên nhân (volume / price / mix / timing)​
5.
Viết summary memo cho CFO theo template specific​
Mỗi quý lặp. Bạn có SOP 15 trang, bạn nhớ rõ. Nhưng đồng nghiệp mới vào team → mất 3 quý để họ làm ra memo "giống bạn". Hỏi vài lần: "format đúng chưa?", "variance 8% có cần flag không?", "category 'mix' định nghĩa sao?".​
Bạn cũng thử Claude giúp. Prompt quí 1: work tốt. Prompt quí 2: Claude quên template cũ, format khác chút. Quí 3: lại phải paste lại 15 trang SOP.​
Knowledge là một chuyện. Nhưng "làm đúng theo methodology mỗi lần" là chuyện khác.​
Đây là chỗ Skills bước vào. Skill đóng gói cả quy trình — steps, templates, reference files, style rules — thành một package Claude tự động invoke mỗi khi task tương tự xuất hiện.​
Comments (0)
Help Center
Keyboard Shortcuts
