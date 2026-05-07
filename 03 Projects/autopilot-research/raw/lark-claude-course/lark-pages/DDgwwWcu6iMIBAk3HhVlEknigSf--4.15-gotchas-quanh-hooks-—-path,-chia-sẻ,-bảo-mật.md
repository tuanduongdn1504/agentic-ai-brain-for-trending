# 4.15 - Gotchas quanh hooks — Path, chia sẻ, bảo mật

**Source:** https://transform.sg.larksuite.com/wiki/DDgwwWcu6iMIBAk3HhVlEknigSf
**Wiki ID:** DDgwwWcu6iMIBAk3HhVlEknigSf
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

4.15 - Gotchas quanh hooks — Path, chia sẻ, bảo mật

Last updated: Apr 20

Log In or Sign Up
4.15 - Gotchas quanh hooks — Path, chia sẻ, bảo mật
Bài 4.15: Gotchas quanh hooks — Path, chia sẻ, bảo mật
Mục tiêu học tập
Mở đầu: Bạn để ý 2 file settings.json?
Gotcha 1: Absolute path là bắt buộc (vì bảo mật)
Quy tắc từ docs Anthropic
Minh họa attack
Fix: Absolute path
Trade-off: Không share được
Gotcha 2: Giải pháp $PWD + setup script
Pattern
Trong package.json:
Flow cho dev mới
.gitignore cần có
Gotcha 3: Hook path với space hoặc ký tự đặc biệt
Fix
Gotcha 4: Hook chạy chậm làm UX tệ
Tactic giảm chi phí
Gotcha 5: Hook im lặng khi crash
A. Hook crash, exit 1 nhưng Claude Code không log
B. Path binary sai
C. Hook chạy, return exit code, nhưng không có side effect
Gotcha 6: Hook và settings.local.json không được Auto-reload
Fix
Gotcha 7: Hook interaction giữa 3 settings level
Câu hỏi: Hook ở cả 3 level — chạy theo thứ tự nào?
Implication
Gotcha 8: Khi nào KHÔNG nên dùng hook
Dùng HOOK khi:
ĐỪNG dùng hook khi:
Ví dụ thực chiến: Rollout cho team 20 dev
Tuần 0: Pilot
Tuần 1: Chuẩn hóa
Tuần 2: Rollout
Tuần 3: Iterate
Kết quả
Case studies theo ngành
💼 Enterprise Java — Monorepo hook scale
🏥 Health — Hook chained với SCRD (Secure Code Review Daemon)
🎮 Game dev — Skip hook cho prototype
🛠️ Open source maintainer — Hook conditional trên fork
🔐 Security team — Hook chain approval
Anti-patterns
❌ Commit settings.local.json với absolute path cá nhân
❌ Hook silent crash không có log
❌ Over-engineer hook từ đầu
❌ Chia sẻ hook mà không audit
❌ Hook mặc định ON cho mọi project
Mẹo nâng cao
Mẹo 1: Script claude-doctor kiểm tra hook
Mẹo 2: Version hook
Mẹo 3: Feature flag trong hook
4.15 - Gotchas quanh hooks — Path, chia sẻ, bảo mật​
Modified April 20
Bài 4.15: Gotchas quanh hooks — Path, chia sẻ, bảo mật​
Module: 5 — Hooks​
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
Slide: Claude Code in Action.pdf​
​
​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Giải thích lý do bảo mật buộc dùng absolute path trong hook command​
•
✅ Dùng trick $PWD placeholder + setup script để share hook qua Git​
•
✅ Nhận diện 6 gotcha phổ biến khi rollout hook cho team​
•
✅ Verify hook không bị tamper bởi path interception​
•
✅ Biết khi nào KHÔNG nên dùng hook (ưu tiên pattern khác)​
​
​
Mở đầu: Bạn để ý 2 file settings.json?​
Sau khi chạy npm run dev của uigen (hoặc một project được setup với hook chuẩn), bạn thấy:​
​
Code block​
Plain Text
Copy
.claude/​
├── settings.example.json    ← commit Git, chia sẻ​
└── settings.local.json      ← gitignore, cá nhân​
​
​
Tại sao cần hai file? Tại sao project setup phải copy cái này thành cái kia?​
Câu trả lời nằm ở giao điểm giữa security requirement và team sharing. Hiểu được, bạn biết cách setup hook scale lên team 50 người.​
​
​
Gotcha 1: Absolute path là bắt buộc (vì bảo mật)​
Quy tắc từ docs Anthropic​
Hook script paths must be absolute to mitigate:​
Comments (0)
Help Center
Keyboard Shortcuts
