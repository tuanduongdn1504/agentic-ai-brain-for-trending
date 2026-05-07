# 1.5 - Projects — Không gian làm việc chuyên dụng

**Source:** https://transform.sg.larksuite.com/wiki/Pmj0wrw9hi8GCBkdrPTlFxlggAr
**Wiki ID:** Pmj0wrw9hi8GCBkdrPTlFxlggAr
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

1.5 - Projects — Không gian làm việc chuyên dụng

Last updated: Apr 20

Log In or Sign Up
1.5 - Projects — Không gian làm việc chuyên dụng
Bài 05: Projects — Không gian làm việc chuyên dụng
Mục tiêu học tập
Mở đầu: Sự mệt mỏi của việc lặp context
Projects là gì?
Khi nào dùng Projects?
3 signals bạn cần Project
1. Reference materials bạn sẽ dùng lặp lại
2. Consistent requirements về cách Claude respond
3. Team collaboration
Test đơn giản: "Lần thứ 3"
Tạo Project đầu tiên — 3 bước
Bước 1: Setup project
Bước 2: Add project instructions
Cấu trúc instruction tốt — 4 phần
Pro tip: Instructions là programming language của bạn
Bước 3: Build knowledge base
Cách upload
Upload gì?
Pro tip: Tên file descriptive
Cơ chế retrieval — RAG khi knowledge base lớn
RAG hoạt động thế nào?
Thực tế với bạn
Pro tip: Reference documents by name
Khi nào knowledge vs. conversation context?
Collaboration features — Team & Enterprise
3 permission levels
Can view
Can edit
Owner
Cách share project
Use case điển hình: Brand team shared project
5 Example Projects để inspire
1. Q4 Product Launch
2. Research Support
3. Client Account Hub
4. Event Planning Workspace
5. Personal Finance Tracker
Ví dụ theo ngành
💼 Sales Team Lead
💰 Finance Analyst
⚖️ Legal Counsel
🎓 Curriculum Developer
📊 Data Analyst
Anti-patterns khi dùng Projects
❌ Project "kho rác"
❌ Instructions quá vague
❌ Never update knowledge base
❌ Không dùng descriptive filenames
❌ Share project với 50 người không cần
❌ Upload sensitive data vào personal project
Best practices — 5 rules
1.5 - Projects — Không gian làm việc chuyên dụng​
Modified April 20
Bài 05: Projects — Không gian làm việc chuyên dụng​
Module: Tổ chức công việc​
Thời gian ước tính: 20 phút​
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
✅ Giải thích Projects là gì và khi nào nên dùng​
•
✅ Tạo một Project mới với name, description, visibility settings​
•
✅ Upload documents vào knowledge base của Project​
•
✅ Viết project instructions hiệu quả để guide Claude's behavior​
•
✅ Share Projects với teammates (dành cho Team / Enterprise users)​
•
✅ Hiểu cơ chế Retrieval Augmented Generation (RAG) khi knowledge base lớn​
Mở đầu: Sự mệt mỏi của việc lặp context​
Hình dung một tuần của một Brand Manager ở công ty flower business.​
Thứ 2, 9:00 AM — Chat mới: "Tôi làm brand marketing cho 1 công ty hoa online. Brand voice của chúng tôi là friendly, warm, slightly poetic. Target audience là phụ nữ 28-45, trung cấp thành thị. Viết blog về care tips cho tulip…"​
Thứ 3, 2:00 PM — Chat mới: "Tôi làm brand marketing cho 1 công ty hoa online. Brand voice…" (paste lại đoạn 150 từ)​
Thứ 4, 11:00 AM — Chat mới: "Tôi làm brand marketing cho…" (paste lại)​
Thứ 6, 3:00 PM — Paste lại. Lần thứ 5 trong tuần.​
Mỗi lần mở chat mới, bạn phải paste lại 150 từ context. Lần nào quên là Claude output tông tùy hứng — quá formal, quá corporate, không match brand.​
Cuối tuần bạn tính: 5 lần × 2 phút = 10 phút "paste context" chỉ trong một tuần. Chưa kể 5 lần upload lại cùng brand guide PDF — mỗi lần 30 giây đợi upload.​
1 năm = 520 phút = hơn 8 giờ chỉ để copy-paste context lặp.​
Và đó là chưa tính đến cognitive load — bạn phải nhớ paste đúng context, nhớ upload đúng file. Mỗi lần quên là lần response chệch.​
Comments (0)
Help Center
Keyboard Shortcuts
