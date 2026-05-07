# 1.4 - Claude Desktop — Chat, Cowork, Code

**Source:** https://transform.sg.larksuite.com/wiki/RRIYwngqdimrUKkto9qlUoIXgce
**Wiki ID:** RRIYwngqdimrUKkto9qlUoIXgce
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

1.4 - Claude Desktop — Chat, Cowork, Code

Last updated: Apr 20

Log In or Sign Up
1.4 - Claude Desktop — Chat, Cowork, Code
Bài 04: Claude Desktop — Chat, Cowork, Code
Mục tiêu học tập
Mở đầu: Khi browser tab không còn đủ
Tổng quan kiến trúc: 3 chế độ, 1 intelligence
Chat mode — Claude quen thuộc, nhưng nhanh hơn
Khi nào dùng Chat mode?
4 tính năng đặc thù của Desktop Chat (không có trên web)
1. Quick Entry (Mac: double-tap Option key)
2. Screenshots & window sharing (Mac)
3. Dictation (Mac)
4. Desktop connectors
Khi nào thử Chat Desktop?
Cowork mode — Claude làm việc dài hơi
Cowork khác Chat ở đâu?
Cowork workflow điển hình
8 tính năng Cowork cần biết
1. Folder access
2. Scheduled tasks (killer feature)
3. Subagents
4. Dispatch — Cowork trên mobile
5. Projects trong Cowork
6. Browser use (qua Claude in Chrome)
7. Computer use (Pro/Max, macOS only, research preview)
8. Plugins
Protected environment — ranh giới an toàn
Khi nào thử Cowork?
Code mode — Full development environment
Chi tiết kỹ thuật
Cowork vs. Code — Khác biệt chính
Local vs. Remote
3 interaction modes
Multiple sessions
Chi tiết Claude Code ở Bài 12.
So sánh 3 chế độ
Ví dụ thực chiến: Một ngày với 3 mode
8:00 AM — Chat mode (quick check)
9:00 AM — Chat mode (Quick Entry)
10:00 AM — Cowork (delegate)
11:00 AM — Meeting (Claude tiếp tục work background)
12:00 PM — Quay về, review Cowork output
2:00 PM — Code mode (dev task)
4:30 PM — Chat (reflection)
7:00 AM sáng mai — Scheduled task tự chạy
Ví dụ theo ngành
💼 Sales Rep
💰 Finance Analyst
⚖️ Legal Counsel
🎓 Teacher
🏥 Medical Writer
📊 Data Analyst
Anti-patterns khi chọn mode
1.4 - Claude Desktop — Chat, Cowork, Code​
Modified April 20
Bài 04: Claude Desktop — Chat, Cowork, Code​
Module: Môi trường làm việc​
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
✅ Nhận diện 3 chế độ của Claude Desktop app — Chat, Cowork, Code — và việc gì mỗi chế độ được thiết kế cho​
•
✅ Giải thích các feature đặc thù của mỗi chế độ: quick entry, scheduled tasks, local vs. remote development​
•
✅ Chọn đúng chế độ dựa trên loại công việc​
•
✅ Setup Cowork với folder access và scheduled tasks​
•
✅ Hiểu ranh giới an toàn (contained environment) giữa 3 chế độ​
Mở đầu: Khi browser tab không còn đủ​
Bạn đã quen Claude qua web (claude.ai). Đủ tốt cho hầu hết câu hỏi. Nhưng có những lúc:​
•
Bạn đang viết report trong Word, muốn hỏi nhanh Claude mà không muốn chuyển tab​
•
Có 1 folder 50 file PDF client vừa gửi, muốn Claude đọc + summarize mà không phải upload từng cái​
•
Bạn muốn Claude tự chạy một daily morning brief lúc 7am, pull từ Slack + calendar + Gmail — ngay cả khi bạn chưa mở app​
•
Bạn đang code, muốn Claude read codebase, run tests, commit — không phải copy-paste qua lại​
Đây là lúc web app trở thành cái cổ chai. Browser tab không access được local files. Không có scheduled tasks. Không có quick entry overlay. Không chạy code trên máy bạn.​
Claude Desktop app giải quyết những giới hạn này. Và đặc biệt, desktop app mở ra 2 chế độ mới mà web không có: Cowork (cho agentic work dài hơi) và Code (cho development workflows).​
Bài này sẽ dạy bạn khi nào dùng mode nào, và cách chúng bổ sung (chứ không thay thế) web experience.​
Tổng quan kiến trúc: 3 chế độ, 1 intelligence​
Claude Desktop cho bạn 3 cách làm việc với cùng một Claude intelligence:​
Comments (0)
Help Center
Keyboard Shortcuts
