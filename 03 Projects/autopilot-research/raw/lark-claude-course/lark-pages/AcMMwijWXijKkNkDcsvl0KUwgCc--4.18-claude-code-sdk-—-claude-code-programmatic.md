# 4.18 - Claude Code SDK — Claude Code programmatic

**Source:** https://transform.sg.larksuite.com/wiki/AcMMwijWXijKkNkDcsvl0KUwgCc
**Wiki ID:** AcMMwijWXijKkNkDcsvl0KUwgCc
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
Slide: Claude Code in Action.pdf
4.0 - Claude Code in Action — Tổng quan khóa học
4.1 - Giới thiệu khóa học "Claude Code in Action"
4.2 - Coding assistant là gì?
4.3 - Claude Code trong thực tế
4.4 - Cài đặt Claude Code
4.5 - Chuẩn bị project thực hành
4.6 - Thêm context với CLAUDE.md
4.7 - Thực hiện thay đổi — Screenshots, Planning Mode, Thinking Mode
4.8 - Điều khiển context — Escape, /compact, /clear
4.9 - Custom commands — Biến workflow lặp thành 1 lệnh
4.10 - MCP servers với Claude Code
4.11 - Tích hợp GitHub — Claude trong pull request và issue
4.12 - Giới thiệu hooks
4.13 - Định nghĩa hook — 4 bước thiết kế
4.14 - Implement hook đầu tiên — Block access
4.15 - Gotchas quanh hooks — Path, chia sẻ, bảo mật
4.16 - Hooks hữu ích cho production — Type check + Duplicate prevention
4.17 - Các hook event khác & Debug hook
4.18 - Claude Code SDK — Claude Code programmatic
4.19 - Quiz tổng hợp & Chứng nhận
4.20 - Tổng kết & bước tiếp theo
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

4.18 - Claude Code SDK — Claude Code programmatic

Last updated: Apr 20

Log In or Sign Up
4.18 - Claude Code SDK — Claude Code programmatic
Bài 4.18: Claude Code SDK — Claude Code programmatic
Mục tiêu học tập
Mở đầu: Khi CLI không đủ
SDK là gì?
Key insight
Ví dụ đơn giản: TypeScript
Setup
Code
Run
Output
Permissions — SDK default là read-only
Grant permission qua allowedTools
Grant qua settings
MCP tools
Python SDK
CLI headless mode
Shell script ví dụ
Ví dụ thực chiến 1: Git hook review
Setup
Ví dụ thực chiến 2: Cron job audit dependency
Setup
Cron
Ví dụ thực chiến 3: Slack bot với SDK
Setup
Ví dụ thực chiến 4: Documentation generator
Setup
Ví dụ thực chiến 5: CI/CD gate
Setup
Use case
Case studies theo ngành
💼 Fintech — Compliance scanner SDK
🏥 Healthcare — Data flow mapper
🛠️ Platform engineering — API breaking change detector
📣 Content platform — Content moderation pipeline
🎮 Game dev — Asset metadata extractor
SDK vs CLI — Decision tree
Anti-patterns
❌ Grant allowedTools: ["*"] cho SDK
❌ Ignore maxTurns
❌ Không handle error của SDK
❌ Run SDK trong loop không rate limit
❌ Hardcode API key trong code
Mẹo nâng cao
Mẹo 1: Structured output với JSON mode
Mẹo 2: Session resumption
Mẹo 3: Stream để UX responsive
Mẹo 4: Budget & monitoring
Áp dụng ngay
Bài tập 1: Script SDK đầu tiên (20 phút)
Bài tập 2 (optional, 25 phút): Automation script
Tóm tắt bài học
4.18 - Claude Code SDK — Claude Code programmatic​
Modified April 20
Bài 4.18: Claude Code SDK — Claude Code programmatic​
Module: 6 — Automation & Wrap-up​
Thời gian ước tính: 30 phút (đọc) + 25 phút (thực hành)​
Mức độ: Nâng cao​
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
Slide: Claude Code in Action.pdf​
​
​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Giải thích SDK là gì, khác gì với CLI, và khi nào dùng mỗi cái​
•
✅ Viết code TypeScript/Python gọi Claude Code programmatic​
•
✅ Cấu hình allowedTools và permission cho SDK​
•
✅ Embed SDK vào script, CI/CD pipeline, hook (đã dùng ở Bài 4.16)​
•
✅ Thiết kế 5 automation scenario dùng SDK hiệu quả​
​
​
Mở đầu: Khi CLI không đủ​
Bạn đã dùng Claude Code qua CLI:​
​
Code block​
Bash
Copy
claude​
> Fix bug trong userService.ts​
​
​
Interactive, thuận tiện — cho dev cá nhân.​
Nhưng khi muốn:​
•
Chạy Claude Code trong GitHub Action để auto-review PR (Bài 4.11 đã giới thiệu)​
•
Cron job mỗi đêm scan codebase, generate report​
•
Script tùy chỉnh analyze codebase khi merge​
•
Hook gọi Claude trong Claude (Bài 4.16)​
•
Chatbot internal với power của Claude Code​
CLI interactive không fit. Bạn cần programmatic access.​
Đó là Claude Code SDK.​
Comments (0)
Help Center
Keyboard Shortcuts
