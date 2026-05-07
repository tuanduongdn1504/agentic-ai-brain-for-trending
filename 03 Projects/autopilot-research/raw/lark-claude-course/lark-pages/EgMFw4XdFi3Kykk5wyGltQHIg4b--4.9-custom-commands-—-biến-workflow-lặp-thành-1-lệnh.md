# 4.9 - Custom commands — Biến workflow lặp thành 1 lệnh

**Source:** https://transform.sg.larksuite.com/wiki/EgMFw4XdFi3Kykk5wyGltQHIg4b
**Wiki ID:** EgMFw4XdFi3Kykk5wyGltQHIg4b
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

4.9 - Custom commands — Biến workflow lặp thành 1 lệnh

Last updated: Apr 20

Log In or Sign Up
4.9 - Custom commands — Biến workflow lặp thành 1 lệnh
Bài 4.9: Custom commands — Biến workflow lặp thành 1 lệnh
Mục tiêu học tập
Mở đầu: "Công thức" lặp lại mỗi tuần
Custom command là gì?
Anatomy
Ví dụ đơn giản
Cách tạo command
Bước 1: Tạo folder
Bước 2: Viết command file
Bước 3: Restart Claude Code
Bước 4: Dùng
$ARGUMENTS — Làm command linh hoạt
Cơ chế
Nhiều cách dùng $ARGUMENTS
Tổ chức command cho team
Structure khuyến nghị
Commit hay không?
Quy tắc đặt tên
Command templates nâng cao
Template 1: Multi-step với verification
Template 2: Context-aware feature
Template 3: Delegate to subagent
Template 4: Onboard newcomer
Ví dụ thực chiến: Command set cho team fintech
Tình huống
Command suite
Workflow cá nhân/dev với commands
Kết quả sau 3 tháng
Case studies theo ngành
💼 Sales engineering — /prep_demo
⚖️ Legal tech — /check_contract_template
🏥 Health tech — /validate_fhir
🎮 Game dev — /balance_check
📣 Marketing — /repurpose_post
Anti-patterns
❌ Command quá generic
❌ Hardcode đường dẫn cá nhân trong command
❌ Command không có verification
❌ Nhồi 5 task vào 1 command
❌ Không update command khi convention đổi
Mẹo nâng cao
Mẹo 1: Command gọi command khác
Mẹo 2: Conditional logic
Mẹo 3: Nạp template bằng @
Mẹo 4: Meta-command /list_commands
Áp dụng ngay
Bài tập 1: Tạo command đầu tiên (15 phút)
Bài tập 2 (optional, 20 phút): Build bộ command cho team
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
4.9 - Custom commands — Biến workflow lặp thành 1 lệnh​
Modified April 20
Bài 4.9: Custom commands — Biến workflow lặp thành 1 lệnh​
Module: 4 — Mở rộng & Tự động hóa​
Thời gian ước tính: 25 phút (đọc) + 20 phút (thực hành)​
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
✅ Tạo custom slash command (/audit, /write_tests, /review...) cho project​
•
✅ Dùng $ARGUMENTS placeholder để command nhận input động​
•
✅ Tổ chức folder .claude/commands/ theo cách team có thể share qua Git​
•
✅ Nhận ra 3 dấu hiệu "đáng tự động hóa thành command"​
•
✅ Tránh 5 anti-patterns khi thiết kế command​
Mở đầu: "Công thức" lặp lại mỗi tuần​
Quan sát developer bạn: họ gõ cùng một prompt cho Claude mỗi tuần:​
•
Monday audit security: "Chạy npm audit, list CVE critical, suggest fix."​
•
Mỗi PR review: "Check coverage, điểm yếu, suggest edge case thiếu."​
•
Trước deploy: "Scan secret leak, check migration pending, run typecheck."​
•
Mỗi feature mới: "Write test theo Vitest + RTL, coverage happy path + edge + error."​
Mỗi prompt lần nào cũng gõ lại 10-15 dòng. Tốn 2-3 phút gõ, chưa kể Claude đọc + execute. Làm 10 lần/tuần × 8 dev = 160 phút chỉ để gõ prompt lặp lại.​
Custom commands xử lý chính xác vấn đề này. Bạn viết prompt chuẩn một lần trong file markdown → gọi bằng /tên-command → Claude nhận prompt đầy đủ ngay.​
Kết quả: 10 dòng prompt → 1 slash.​
Custom command là gì?​
Một custom command là file markdown nằm trong thư mục .claude/commands/ của project. Khi bạn gõ /tên-file trong Claude Code, nội dung file được gửi như prompt của bạn.​
Comments (0)
Help Center
Keyboard Shortcuts
