# 4.17 - Các hook event khác & Debug hook

**Source:** https://transform.sg.larksuite.com/wiki/YGdmwpgPsitSzAk9sENlmkp2gad
**Wiki ID:** YGdmwpgPsitSzAk9sENlmkp2gad
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

4.17 - Các hook event khác & Debug hook

Last updated: Apr 20

Log In or Sign Up
4.17 - Các hook event khác & Debug hook
Bài 4.17: Các hook event khác & Debug hook
Mục tiêu học tập
Mở đầu: Pre/Post chưa đủ
7 hook event của Claude Code
Mô tả từng event
JSON shape khác nhau theo event
Ví dụ 1: PostToolUse trên TodoWrite
Ví dụ 2: Stop event
Ví dụ 3: UserPromptSubmit
Ví dụ 4: Notification (permission request)
Pattern: Log-first, implement-later
Cách làm
Ví dụ hook sử dụng event khác
Hook A: Notification — Desktop alert khi Claude xin permission
Hook B: Stop — Auto-commit sau mỗi session
Hook C: UserPromptSubmit — Sanitize / rewrite prompt
Hook D: SessionStart — Auto-sync config
Hook E: PreCompact — Snapshot trước compact
Ví dụ thực chiến: Team dùng 5 hook event
Setup
Kết quả sau 3 tháng
Case studies theo ngành
💼 Customer success — Prompt analytics
🏥 Health tech — Session audit cho SOC2
🎮 Game dev — Auto-screenshot khi edit asset
🛠️ Platform team — Notification Slack
🎓 EdTech — Teacher mode
Anti-patterns
❌ Hook log-all chạy mãi không remove
❌ Notification hook spam
❌ SessionStart quá chậm
❌ Hook modify transcript
❌ Quên xử lý fail gracefully
Mẹo nâng cao
Mẹo 1: Hook orchestrator
Mẹo 2: Conditional hook bằng env
Mẹo 3: Hook với telemetry
Mẹo 4: Share hook qua npm
Áp dụng ngay
Bài tập 1: Log-first debugging (15 phút)
Bài tập 2 (optional, 20 phút): Chọn 1 event mới cho project
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
4.17 - Các hook event khác & Debug hook​
Modified April 20
Bài 4.17: Các hook event khác & Debug hook​
Module: 5 — Hooks​
Thời gian ước tính: 25 phút​
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
Slide: Claude Code in Action.pdf​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Liệt kê 7 hook event của Claude Code (không chỉ Pre/PostToolUse)​
•
✅ Chọn event phù hợp cho các use case: notification, stop detection, session lifecycle​
•
✅ Dùng log-only hook để inspect JSON structure mà không cần đoán​
•
✅ Viết hook cho Stop, Notification, SessionStart, UserPromptSubmit​
•
✅ Debug hook với pattern "log first, implement later"​
Mở đầu: Pre/Post chưa đủ​
Bài 4.12–4.16 tập trung PreToolUse và PostToolUse. Đây là 2 event phổ biến nhất.​
Nhưng Claude Code có nhiều event khác — mỗi cái mở use case riêng:​
•
Muốn alert khi Claude "stuck" chờ permission? → Notification event​
•
Muốn cleanup khi session kết thúc? → Stop event​
•
Muốn validate prompt trước khi gửi Claude? → UserPromptSubmit event​
•
Muốn init state mỗi khi session start? → SessionStart event​
Biết các event này = hook game bạn mở rộng nhiều.​
7 hook event của Claude Code​
​
Code block​
Plain Text
Copy
┌──────────────────────────────────────────────────────────┐​
│                                                          │​
│  LIFECYCLE                                               │​
│  ├── SessionStart     — khi Claude Code khởi động        │​
│  ├── SessionEnd       — khi Claude Code đóng             │​
​
Comments (0)
Help Center
Keyboard Shortcuts
