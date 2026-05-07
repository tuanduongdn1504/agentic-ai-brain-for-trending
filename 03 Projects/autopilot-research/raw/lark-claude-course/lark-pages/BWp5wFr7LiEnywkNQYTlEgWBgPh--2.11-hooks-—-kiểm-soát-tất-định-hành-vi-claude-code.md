# 2.11 - Hooks — Kiểm soát tất định hành vi Claude Code

**Source:** https://transform.sg.larksuite.com/wiki/BWp5wFr7LiEnywkNQYTlEgWBgPh
**Wiki ID:** BWp5wFr7LiEnywkNQYTlEgWBgPh
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
Slide: Claude Code 101.pdf
2.0 - Khoá học Claude Code 101 — Tổng quan
2.1 - Cách Claude Code hoạt động
2.2 - Cài đặt Claude Code
2.3 - Prompt Đầu Tiên
2.4 - Workflow Explore → Plan → Code → Commit
2.5 - Quản lý Context
2.6 - Code Review và Git Workflow
2.7 - File CLAUDE.md
2.8 - Subagents
2.9 - Skills — Dạy Claude một lần, dùng mãi mãi
2.10 - MCP — Kết nối Claude Code với thế giới bên ngoài
2.11 - Hooks — Kiểm soát tất định hành vi Claude Code
2.12 - Quiz tổng hợp — Claude Code 101
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

2.11 - Hooks — Kiểm soát tất định hành vi Claude Code

Last updated: Apr 20

Log In or Sign Up
2.11 - Hooks — Kiểm soát tất định hành vi Claude Code
Bài 2.11: Hooks — Kiểm soát tất định hành vi Claude Code
Mục tiêu học tập
Mở đầu: "Claude quên" không còn là lý do hợp lý nữa
Hook là gì?
Lifecycle của Claude Code — nơi hooks can thiệp
5 Hook Events
Anatomy của hook config
Cấu trúc JSON
Giải thích từng thành phần
Script nhận gì từ Claude Code?
Exit Codes và Behavior
Ví dụ thực chiến: Auto-format hook
Bước 1: Tạo script
Bước 2: Cấp quyền thực thi
Bước 3: Thêm vào settings.json
Bước 4: Commit vào repo
Bước 5: Test
Blocking với PreToolUse
Script nhận gì?
Ví dụ: Block lệnh Bash nguy hiểm
Hook vs Skill vs CLAUDE.md vs MCP
Case studies theo role
Backend Engineer: Lint guarantee
DevOps / Security Engineer: Prod file protection
Engineering Team: Async notification
Compliance team: Audit log bắt buộc
Open Source Maintainer: Test trước commit
Solo founder: macOS notification
Anti-patterns
Script chạy quá lâu (>10 giây)
PreToolUse không xử lý input rỗng
Hardcode absolute path trong command
Không commit settings.json và script vào repo
Hook chứa secret / API key
Dùng hook cho việc nên là Skill
Matcher quá rộng (no matcher)
Mẹo nâng cao
Dùng CLAUDE_PROJECT_DIR cho mọi path reference
Combine hooks: PreToolUse → PostToolUse → Stop pipeline
Idempotent scripts — chạy nhiều lần không có side effect
Test hook isolation trước khi enable
Conditional logic trong script (không chỉ dựa vào matcher)
Debug: comment tạm matcher để isolate hook behavior
Multiple matchers trong 1 entry
Áp dụng ngay
Bài tập 1: Auto-format hook (~25 phút)
Bài tập 2: PreToolUse blocking hook (~20 phút)
Tóm tắt
Bài tiếp theo
Tài liệu tham khảo
2.11 - Hooks — Kiểm soát tất định hành vi Claude Code​
Modified April 20
Bài 2.11: Hooks — Kiểm soát tất định hành vi Claude Code​
Module: Hệ sinh thái mở rộng​
Thời gian ước tính: 30 phút​
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
Slide: Claude Code 101.pdf​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Giải thích hook là gì và tại sao nó deterministic (tất định) trong khi CLAUDE.md và skill thì probabilistic (xác suất)​
•
✅ Nắm rõ 5 lifecycle events: PreToolUse, PostToolUse, UserPromptSubmit, Stop, Notification — và khi nào dùng cái nào​
•
✅ Cấu hình hooks đúng cách trong settings.json với matcher, command, và script​
•
✅ Dùng exit codes (0 / 2) để allow hoặc block tool call từ PreToolUse hook​
•
✅ Share hooks với cả team bằng cách commit settings.json và script vào repo​
Mở đầu: "Claude quên" không còn là lý do hợp lý nữa​
Một dev backend ở startup fintech đã viết vào CLAUDE.md:​
"Sau mỗi lần edit file TypeScript, hãy chạy Prettier để format code."​
Đơn giản, rõ ràng. Trong 2 tuần đầu, Claude làm đúng khoảng 80% thời gian. Đủ tốt để bỏ qua.​
Cho đến buổi chiều thứ Sáu trước ngày release. CI pipeline báo đỏ: 47 file lỗi format. Dev phải ngồi lại chạy Prettier tay toàn bộ thư mục src/. Mất 40 phút. Sprint bị trễ.​
Vấn đề không phải Claude "lười". Vấn đề là CLAUDE.md là probabilistic — model đọc rồi quyết định có thực hiện hay không, dựa trên ngữ cảnh hiện tại, độ dài cuộc hội thoại, và hàng chục yếu tố khác. 80% tốt là một con số tốt trong ML. Nhưng trong production workflow, 80% nghĩa là 1 trong 5 lần bạn sẽ bị bất ngờ.​
Hook giải quyết chính xác vấn đề này.​
Khi bạn đặt logic vào hook, Claude không còn là người quyết định nữa. Hệ thống Claude Code chạy script của bạn tại event được chỉ định — mà không cần model "nhớ" hay "quyết định". 100% mỗi lần, không ngoại lệ.​
"If something needs to happen every time without fail, don't put it in a prompt. Put it in a hook."— Hooks documentation, Anthropic​
Đây là bài học bạn sẽ nhớ mãi sau khi đọc xong bài này.​
Comments (0)
Help Center
Keyboard Shortcuts
