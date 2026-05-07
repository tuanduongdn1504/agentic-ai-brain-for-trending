# 4.13 - Định nghĩa hook — 4 bước thiết kế

**Source:** https://transform.sg.larksuite.com/wiki/DTlhw0p6Ui6QxNkkD3Ql7a55gIe
**Wiki ID:** DTlhw0p6Ui6QxNkkD3Ql7a55gIe
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

4.13 - Định nghĩa hook — 4 bước thiết kế

Last updated: Apr 20

Log In or Sign Up
4.13 - Định nghĩa hook — 4 bước thiết kế
Bài 4.13: Định nghĩa hook — 4 bước thiết kế
Mục tiêu học tập
Mở đầu: Tại sao viết hook lần đầu khó?
Quy trình 4 bước thiết kế hook
Bước 1: Pre hay Post?
Bước 2: Matcher — Tool nào trigger?
Bước 3: Command nhận stdin JSON
Bước 4: Exit code
JSON input — Cấu trúc chi tiết
Fields chung cho mọi hook event
PreToolUse — thêm tool_name + tool_input
PostToolUse — thêm tool_response
Code defensive khi đọc field
Ví dụ: Thiết kế 3 hook từng bước
Hook A: Block .env access
Hook B: Auto-format TS
Hook C: Block dangerous bash
Ví dụ thực chiến: Team setup 3 hook foundational
Context
settings.json
Kết quả
Case studies theo ngành
💰 Fintech — PreToolUse block prod DB destructive
🏥 Health tech — PreToolUse enforce audit
🛠️ Platform — PostToolUse Kubernetes manifest validation
🔐 Security — PreToolUse block public repo push
🎨 Design system — PostToolUse enforce token usage
Anti-patterns
❌ Không check tool_name, apply logic cho mọi tool
❌ Hook làm heavy work trong hot path
❌ Exit code sai
❌ Swallow error silent
❌ Regex quá lỏng
Mẹo nâng cao
Mẹo 1: Test hook độc lập
Mẹo 2: Share hook qua npm package
Mẹo 3: Conditional hook based trên branch
Mẹo 4: Timeout cho hook
Áp dụng ngay
Bài tập 1: Design hook trên giấy (10 phút)
Bài tập 2: Đọc JSON thực tế (15 phút)
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
4.13 - Định nghĩa hook — 4 bước thiết kế​
Modified April 20
Bài 4.13: Định nghĩa hook — 4 bước thiết kế​
Module: 5 — Hooks​
Thời gian ước tính: 25 phút​
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
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Áp dụng quy trình 4 bước thiết kế một hook từ đầu​
•
✅ Đọc hiểu JSON mà Claude Code push vào stdin của hook​
•
✅ Dùng đúng exit code để communicate với Claude (0 vs 2)​
•
✅ List được các built-in tool (Read, Edit, Bash...) và schema input của chúng​
•
✅ Nhận diện khi nào hook cần nhìn tool_input.file_path vs field khác​
Mở đầu: Tại sao viết hook lần đầu khó?​
Câu chuyện thật:​
Dev: "Tôi muốn hook block nếu Claude định rm -rf. Nhưng tôi không biết JSON Claude push vào stdin có field gì, hay exit code nào để block..."​
Vấn đề không phải khái niệm, mà là thiếu chỉ dẫn về data shape và control flow.​
Bài này filled that gap. Bạn sẽ biết:​
1.
Quy trình 4-bước để thiết kế hook trước khi code​
2.
JSON shape cho mỗi loại tool​
3.
Exit code rules​
4.
Cách inspect JSON nếu không nhớ​
Quy trình 4 bước thiết kế hook​
​
Code block​
Plain Text
Copy
┌──────────────────────────────────────────────────────────┐​
│                                                          │​
​
Comments (0)
Help Center
Keyboard Shortcuts
