# 2.3 - Prompt Đầu Tiên

**Source:** https://transform.sg.larksuite.com/wiki/MTXhw3LgwiVHOgk0JzSld4TLgeg
**Wiki ID:** MTXhw3LgwiVHOgk0JzSld4TLgeg
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

2.3 - Prompt Đầu Tiên

Last updated: Apr 20

Log In or Sign Up
2.3 - Prompt Đầu Tiên
Bài 2.3: Prompt Đầu Tiên
Mục tiêu học tập
Mở đầu: Tại sao prompt đầu tiên quan trọng hơn bạn nghĩ
3 Permission Modes: Claude Code hoạt động ở chế độ nào?
Default (Approval Mode)
Auto Accept
Plan Mode
Bảng so sánh: Khi nào dùng mode nào
Boris's 3-Task Framework
Easy: One-shot task
Medium: Plan trước, execute sau
Hard: Bạn là người điều hướng
Ví dụ thực chiến: Add Dark Mode Toggle (Step-by-step)
Tình huống
Bước 1: Vào Plan Mode
Bước 2: Viết prompt có đủ context và constraint
Bước 3: Claude trả về plan 7 bước
Bước 4: Review plan và comment điều chỉnh
Bước 5: Approve plan
Bước 6: Claude execute với Auto Accept
Bước 7: Verify visual và run tests
Kết quả
Anatomy của prompt tốt
Bảng đối chiếu: Prompt yếu vs Prompt mạnh
Anti-patterns: 5 sai lầm phổ biến nhất
Anti-pattern 1: Prompt quá broad — "Build me an app"
Anti-pattern 2: Skip Plan Mode cho task > 30 phút
Anti-pattern 3: Auto Accept trên production branch
Anti-pattern 4: Không define "done" → Claude loop vô tận
Anti-pattern 5: "Hãy fix tất cả bugs"
Mẹo nâng cao
Mẹo 1: "Think hard" và extended thinking
Mẹo 2: Reference file cụ thể bằng @filename
Mẹo 3: Multi-line prompt — ngắn nhưng cụ thể
Mẹo 4: Interrupt khi Claude đi sai hướng
Áp dụng ngay
Bài tập 1: Reproduce Dark Mode Demo (15 phút)
Bài tập 2: Prompt yếu vs Prompt mạnh — so sánh kết quả (10 phút)
Tóm tắt bài học
Bài tiếp theo
Cross-references
Tài liệu tham khảo
2.3 - Prompt Đầu Tiên​
Modified April 20
Bài 2.3: Prompt Đầu Tiên​
Module: Nền tảng​
Thời gian ước tính: 25 phút​
Mức độ: Cơ bản → Trung cấp​
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
✅ Viết prompt hiệu quả — đủ context, đủ constraint, đủ success criteria​
•
✅ Phân biệt 3 permission modes: Default, Auto Accept, Plan Mode — và biết khi nào dùng cái nào​
•
✅ Kích hoạt Plan Mode đúng lúc để tránh Claude "lao đầu viết code" khi task còn mơ hồ​
•
✅ Hiểu Boris's 3-task framework — Easy/Medium/Hard — để chọn cách tiếp cận phù hợp​
•
✅ Tự tay chạy demo Dark Mode Toggle end-to-end theo Plan Mode workflow​
Mở đầu: Tại sao prompt đầu tiên quan trọng hơn bạn nghĩ​
Hãy hình dung bạn mới cài Claude Code xong. Terminal đang mở. Bạn hào hứng gõ vào:​
"Viết cho tôi một function login."​
Claude bắt đầu chạy. Sau 2 phút, bạn nhận được một file login.ts 80 dòng. Nhưng khi nhìn kỹ — nó dùng express-session, trong khi project của bạn đang dùng JWT. Nó tạo endpoint /login riêng, trong khi codebase đã có authRouter. Nó viết bcrypt theo kiểu cũ, trong khi team đã chuẩn hoá dùng argon2.​
Bạn mất 20 phút gỡ ra và viết lại. Lần này tốn nhiều thời gian hơn làm tay.​
Vấn đề không phải ở Claude. Vấn đề ở prompt.​
Boris Cherny — kỹ sư chủ chốt trong nhóm phát triển Claude Code tại Anthropic — có một lời khuyên ngược đời mà nhiều người bỏ qua:​
"Don't use Claude Code to write code first. Use it to ask questions about the codebase."​
Đây là sự khác biệt về mindset: prompt không phải là command — prompt là brief. Bạn không đang ra lệnh cho một cái máy. Bạn đang brief cho một kỹ sư mới vào team, người cực kỳ tài năng nhưng chưa biết gì về codebase của bạn.​
Một kỹ sư giỏi khi nhận brief sẽ làm gì? Họ sẽ hỏi lại. Họ sẽ đọc code hiện tại trước. Họ sẽ đề xuất plan trước khi gõ dòng code đầu tiên. Claude Code được thiết kế để làm đúng như vậy — nếu bạn biết cách prompt.​
Bài này sẽ dạy bạn cách làm điều đó.​
Comments (0)
Help Center
Keyboard Shortcuts
