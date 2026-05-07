# 4.16 - Hooks hữu ích cho production — Type check + Duplicate prevention

**Source:** https://transform.sg.larksuite.com/wiki/VLmUwIuiBiIqpwkEJPllBCXWg0f
**Wiki ID:** VLmUwIuiBiIqpwkEJPllBCXWg0f
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

4.16 - Hooks hữu ích cho production — Type check + Duplicate prevention

Last updated: Apr 20

Log In or Sign Up
4.16 - Hooks hữu ích cho production — Type check + Duplicate prevention
Bài 4.16: Hooks hữu ích cho production — Type check + Duplicate prevention
Mục tiêu học tập
Mở đầu: Khi codebase lớn, Claude có "trí nhớ kém"
Vấn đề 1: Sửa function, quên call site
Vấn đề 2: Tạo duplicate query
Giải pháp: Hook thông minh
Hook 1: TypeScript typecheck feedback
Flow
Implement
Config
Cách hoạt động với Claude
Tương đương cho untyped languages
Hook 2: Query duplication prevention
Vấn đề chi tiết
Giải pháp: "Claude review Claude" pattern
Implement
Config
Trade-offs — Quan trọng đọc
Chi phí
Mở rộng pattern
Khuyến nghị scope
Ví dụ thực chiến: Fintech team rollout 2 hook
Setup
Tuần 1 — Pilot senior engineer
Tuần 2 — Rollout team
Tháng 1 — Metrics
Tối ưu
Case studies hook production
💰 Fintech — Compliance check hook
🏥 Health tech — PHI leak prevention
🛠️ Platform eng — API consistency
🎮 Game dev — Balance data validation
📣 Marketing — Brand voice check
Anti-patterns hook production
❌ Sub-Claude permission leak
❌ Hook recursive
❌ Feedback hook quá mơ hồ
❌ Hook chạy trên file khổng lồ
❌ Không log metrics
Mẹo nâng cao
Mẹo 1: Hook "expensive" opt-in
Mẹo 2: Cache sub-Claude response
Mẹo 3: Parallel hook chain
Mẹo 4: Hook dev vs prod
Áp dụng ngay
Bài tập 1: Typecheck hook (20 phút)
Bài tập 2 (optional, 30 phút): Build custom review hook
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
4.16 - Hooks hữu ích cho production — Type check + Duplicate prevention​
Modified April 20
Bài 4.16: Hooks hữu ích cho production — Type check + Duplicate prevention​
Module: 5 — Hooks​
Thời gian ước tính: 35 phút (đọc) + 30 phút (implement)​
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
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Build hook TypeScript typecheck feedback — bắt Claude quên update callsite​
•
✅ Build hook query duplication prevention — Claude không tạo duplicate DB query​
•
✅ Hiểu pattern "Claude review Claude" bằng Claude Code SDK​
•
✅ Đánh giá trade-off của expensive hook (latency, cost)​
•
✅ Áp dụng 2 hook này vào codebase thật của bạn​
Mở đầu: Khi codebase lớn, Claude có "trí nhớ kém"​
Với project 50,000 dòng, Claude đôi khi:​
Vấn đề 1: Sửa function, quên call site​
Task: "Thêm parameter verbose: boolean vào formatReport() trong lib/report.ts"​
Claude:​
​
Code block​
Plain Text
Copy
[Edit] lib/report.ts — thêm parameter, sửa signature​
​
​
Xong, exit.​
Nhưng formatReport() được gọi ở 8 file khác. Claude không update những call site đó. Type error lan ra khắp project — bạn phát hiện sau khi chạy tsc tay.​
Comments (0)
Help Center
Keyboard Shortcuts
