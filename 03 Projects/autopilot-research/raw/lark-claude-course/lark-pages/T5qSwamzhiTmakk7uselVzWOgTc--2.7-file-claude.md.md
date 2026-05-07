# 2.7 - File CLAUDE.md

**Source:** https://transform.sg.larksuite.com/wiki/T5qSwamzhiTmakk7uselVzWOgTc
**Wiki ID:** T5qSwamzhiTmakk7uselVzWOgTc
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

2.7 - File CLAUDE.md

Last updated: Apr 20

Log In or Sign Up
2.7 - File CLAUDE.md
Bài 2.7: File CLAUDE.md
Mục tiêu học tập
Mở đầu: 2 giờ onboard, rồi 30 giây
CLAUDE.md là gì?
Lifecycle của CLAUDE.md trong một session
Bảng "4 Variants của CLAUDE.md"
Lưu ý quan trọng về Local variant
Anatomy của một CLAUDE.md tốt
Tại sao từng section tồn tại
Hierarchy và Composition
Ví dụ step-by-step: Setup CLAUDE.md cho project mới
Bước 1: Bắt đầu không có CLAUDE.md (observe pain points trước)
Bước 2: Identify 5-10 things bạn phải repeat
Bước 3: Run /init để generate draft
Bước 4: Edit draft, thêm observations từ Bước 2
Bước 5: Test với session mới
Bước 6: Commit và tạo user-level CLAUDE.md
Case studies theo industry
Backend team — Node.js microservices
Mobile team — React Native
Data team — Python ML/analytics
COBOL modernization — legacy system
Open source library maintainer
Anti-patterns
Anti-pattern 1: CLAUDE.md quá dài (200+ dòng)
Anti-pattern 2: Hardcode personal preferences vào project CLAUDE.md
Anti-pattern 3: Không update CLAUDE.md khi tech stack thay đổi
Anti-pattern 4: Generate /init rồi không bao giờ edit
Anti-pattern 5: Chỉ dùng project CLAUDE.md, bỏ qua user-level
Anti-pattern 6: Đẩy "PR review checklist" vào CLAUDE.md
Mẹo nâng cao
Memory mode với # shortcut
@filename syntax để reference docs
Nested CLAUDE.md cho monorepo
Ask Claude save rule sau correction
Trim CLAUDE.md định kỳ
Áp dụng ngay
Bài tập 1: Generate, edit, và test (20 phút)
Bài tập 2: Tạo user-level CLAUDE.md (10 phút)
Tóm tắt
Bài tiếp theo
Tài liệu tham khảo
2.7 - File CLAUDE.md​
Modified April 20
Bài 2.7: File CLAUDE.md​
Module: Persistent context — bộ nhớ xuyên session​
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
Slide: Claude Code 101.pdf​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Giải thích CLAUDE.md là gì, khi nào file được load, và tại sao nó là "bộ nhớ dài hạn" của Claude​
•
✅ Viết một CLAUDE.md tốt phù hợp với project thực tế của mình​
•
✅ Dùng đúng 4 variants: project-level, user-level, local, và nested theo từng tình huống​
•
✅ Reference file khác trong CLAUDE.md bằng @ syntax để tránh duplicate​
•
✅ Biết khi nào nên dùng /init để generate draft và khi nào nên viết tay từ đầu​
Mở đầu: 2 giờ onboard, rồi 30 giây​
Hãy tưởng tượng bạn quay lại một project Next.js sau 6 tháng nghỉ. Project của người khác handoff cho bạn từ trước Tết. Bạn mở Claude Code và gõ: "Implement feature dark mode."​
Claude hỏi lại: "Project này dùng framework CSS gì? Tailwind hay styled-components? Bạn có một design system chưa? Test command là gì?"​
Bạn phải tìm lại. Scroll qua package.json, đọc README.md (nếu có — và nó thường outdated), mở next.config.js, tìm hiểu cấu trúc thư mục. Phải mất gần 2 giờ để trả lời được những câu hỏi đó cho Claude, và câu trả lời thì bị rải rác trong prompt, trong file Claude đọc, trong context mà session sau sẽ không còn nhớ.​
Rồi bạn tạo CLAUDE.md. Bạn ghi vào đó: stack là Next.js 15 App Router + Tailwind + Drizzle ORM. Test command là pnpm test --run. Migration phải chạy qua pnpm db:migrate, không được gọi drizzle-kit migrate trực tiếp. Named exports only. Server Actions ưu tiên hơn API routes.​
Ngày hôm sau, bạn mở Claude Code. Bạn gõ: "Implement feature dark mode."​
Claude bắt đầu viết code ngay. Đúng Tailwind. Đúng App Router pattern. Đúng named export. Không hỏi gì thêm.​
30 giây thay vì 2 giờ.​
"CLAUDE.md is Claude's memory across sessions and across team."— Boris Cherny, Anthropic​
Đó là điểm mấu chốt. Claude Code không có memory tự nhiên giữa các session — mỗi khi bạn mở terminal mới, Claude bắt đầu từ zero. CLAUDE.md là cách bạn cho Claude "nhớ" project của mình trước khi bạn gõ prompt đầu tiên.​
Comments (0)
Help Center
Keyboard Shortcuts
