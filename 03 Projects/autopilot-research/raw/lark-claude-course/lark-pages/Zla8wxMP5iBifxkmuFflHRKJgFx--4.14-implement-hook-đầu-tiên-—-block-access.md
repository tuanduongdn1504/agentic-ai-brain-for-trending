# 4.14 - Implement hook đầu tiên — Block  access

**Source:** https://transform.sg.larksuite.com/wiki/Zla8wxMP5iBifxkmuFflHRKJgFx
**Wiki ID:** Zla8wxMP5iBifxkmuFflHRKJgFx
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

4.14 - Implement hook đầu tiên — Block access

Last updated: Apr 20

Log In or Sign Up
4.14 - Implement hook đầu tiên — Block access
Bài 4.14: Implement hook đầu tiên — Block .env access
Mục tiêu học tập
Mở đầu: Tại sao .env là priority #1 để protect?
Thiết kế (nhắc lại từ Bài 4.13)
Bước 1: Cài structure
Directory layout sau khi xong
Bước 2: Viết script read_hook.js
Phân tích script
Bước 3: Config settings.local.json
Tại sao settings.local.json?
Bước 4: Restart Claude Code
Bước 5: Test với 4 scenario
Scenario 1: Đọc .env trực tiếp
Scenario 2: Grep trong .env
Scenario 3: Đọc file khác (không phải .env)
Scenario 4: File có tên gần giống (false positive test)
Scenario 5: Đọc .env.local, .env.production
Debug khi hook không hoạt động
Triệu chứng 1: Hook không trigger
Triệu chứng 2: Hook error, không block
Triệu chứng 3: Hook chạy nhưng không block
Tactic: Log debug temporary
Mở rộng: Block thêm folder secrets/
Ví dụ thực chiến: Team rollout
Tuần 1: Pilot 1 dev
Tuần 2: Rollout team
Tuần 3: Monitor + iterate
Kết quả
Case studies theo ngành
💰 Bank — Block prod DB read
🏥 Health — Block PHI folder
🎓 University — Block student data
🏭 Enterprise — Block IP protect
🔐 Defense — Air-gap verify
Anti-patterns
❌ Dùng path tương đối
❌ Pattern block quá rộng
❌ Không handle exception
❌ Hook depend vào env variable không set trong session
❌ Dùng settings.json (shared) cho absolute path cá nhân
Mẹo nâng cao
Mẹo 1: Config bằng ENV var
Mẹo 2: Hook viết bằng shell cho đơn giản
Mẹo 3: Multiple hook chain
Mẹo 4: Hook conditional bằng file glob
Áp dụng ngay
Bài tập 1: Cài hook .env (20 phút)
Bài tập 2 (optional, 15 phút): Extend block list
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
4.14 - Implement hook đầu tiên — Block  access​
Modified April 20
Bài 4.14: Implement hook đầu tiên — Block .env access​
Module: 5 — Hooks​
Thời gian ước tính: 30 phút​
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
✅ Cài đặt end-to-end một hook PreToolUse block Claude đọc file .env​
•
✅ Viết Node.js script hook đầy đủ với error handling​
•
✅ Config hook trong .claude/settings.local.json​
•
✅ Test hook với 4 scenario khác nhau (Read direct, Grep, gián tiếp, false positive)​
•
✅ Debug khi hook không trigger​
Mở đầu: Tại sao .env là priority #1 để protect?​
Trong dev, .env chứa:​
•
API key (Anthropic, Stripe, AWS)​
•
DB password​
•
JWT secret​
•
Third-party credential​
Nếu Claude đọc .env:​
•
Token sensitive có thể lọt vào transcript → shared inadvertently​
•
Claude có thể quote secret trong response → tiếp tục lan truyền​
•
Compromise security khi transcript được lưu hoặc share​
Quy tắc vàng: .env tuyệt đối không xuất hiện trong prompt/response của LLM. Hook là cách enforce tuyệt đối.​
Thiết kế (nhắc lại từ Bài 4.13)​
Bước 1: Pre? → Yes, cần block trước khi tool đọc.​
Bước 2: Matcher? → Read|Grep (2 tool có thể truy cập file content).​
Comments (0)
Help Center
Keyboard Shortcuts
