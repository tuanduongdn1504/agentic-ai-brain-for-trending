# 4.11 - Tích hợp GitHub — Claude trong pull request và issue

**Source:** https://transform.sg.larksuite.com/wiki/RaUWwa16NiRuAqkxGaalbg11gof
**Wiki ID:** RaUWwa16NiRuAqkxGaalbg11gof
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

4.11 - Tích hợp GitHub — Claude trong pull request và issue

Last updated: Apr 20

Log In or Sign Up
4.11 - Tích hợp GitHub — Claude trong pull request và issue
Bài 4.11: Tích hợp GitHub — Claude trong pull request và issue
Mục tiêu học tập
Mở đầu: Khi CI là đồng nghiệp
Hai workflow chính
Setup: /install-github-app
Bước 1: Chạy command trong Claude Code
Bước 2: Test
Test @claude mention
Test auto-review
Hiểu workflow YAML
Default claude.yml (@claude mention)
Default claude-review.yml (auto-review PR)
Customization — Nơi sức mạnh thực sự
Tùy chỉnh 1: Project Setup
Tùy chỉnh 2: MCP Server trong Actions
Tùy chỉnh 3: Allowed tools — BẮT BUỘC cho MCP
Tùy chỉnh 4: Scope custom instructions
Ví dụ thực chiến: Auto-triage workflow
Tình huống
Workflow custom
Kết quả
Case studies theo ngành
💼 Open source maintainer — 500 issue/tháng
🏢 Enterprise — Compliance review tự động
🏥 HealthTech — HIPAA audit trong CI
🛠️ Platform team — Bot cho infra queries
🎓 EdTech — Auto-answer student issue
Anti-patterns
❌ Quên tắt workflow khi experiment
❌ API key rò rỉ qua logs
❌ Permission quá rộng
❌ Allowed tools quá lỏng
❌ Không có human-in-loop cho destructive action
Mẹo nâng cao
Mẹo 1: Cost control với path filter
Mẹo 2: Multiple workflow cho multiple persona
Mẹo 3: Matrix strategy cho multi-language repo
Mẹo 4: Rate limit Claude response
Áp dụng ngay
Bài tập 1: Setup GitHub integration (20 phút)
Bài tập 2 (optional, 30 phút): Customize review workflow
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
4.11 - Tích hợp GitHub — Claude trong pull request và issue​
Modified April 20
Bài 4.11: Tích hợp GitHub — Claude trong pull request và issue​
Module: 4 — Mở rộng & Tự động hóa​
Thời gian ước tính: 30 phút (đọc) + 30 phút (setup)​
Mức độ: Trung cấp → Nâng cao​
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
✅ Cài đặt GitHub integration chính thức của Claude Code (/install-github-app)​
•
✅ Kích hoạt Claude bằng @claude trong issue/PR comment​
•
✅ Cấu hình auto-review mỗi PR mới​
•
✅ Customize workflow YAML với custom_instructions, mcp_config, allowed_tools​
•
✅ Bảo mật workflow với permission explicit + secret management​
​
​
Mở đầu: Khi CI là đồng nghiệp​
Bạn mở PR. Hệ thống CI chạy: lint pass, test pass, build pass. Rồi Claude comment:​
@claude:Reviewed this PR. Found 3 potential issues:​
​
Suggest addressing #1 before merge (security). #2 and #3 can be follow-up.​
Đây không phải human reviewer. Đây là Claude trong GitHub Actions.​
Kết quả: bạn có reviewer 24/7 nhìn mọi PR. Human reviewer chỉ cần focus vào high-level decisions. PR "chín muồi" nhanh hơn.​
Bài này dạy bạn setup.​
​
​
Hai workflow chính​
GitHub integration cung cấp hai GitHub Actions workflow mặc định:​
​
Code block​
Plain Text
Copy
​
Comments (0)
Help Center
Keyboard Shortcuts
