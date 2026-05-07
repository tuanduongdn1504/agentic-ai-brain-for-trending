# 2.8 - Subagents

**Source:** https://transform.sg.larksuite.com/wiki/JaB2wZveuiBAZukHJ8rlvaoYgSf
**Wiki ID:** JaB2wZveuiBAZukHJ8rlvaoYgSf
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

2.8 - Subagents

Last updated: Apr 20

Log In or Sign Up
2.8 - Subagents
Bài 2.8: Subagents
Mục tiêu học tập
Mở đầu: "You get the answer without the journey"
Subagent là gì?
Cơ chế hoạt động
3 thành phần cốt lõi
Built-in Subagents
Tạo custom subagent
Cách tạo qua /agents
Output: file markdown với YAML frontmatter
Scope: project-level vs user-level
Subagent vs Main Agent: Khi nào dùng cái nào?
Ví dụ thực chiến: COBOL Modernization Case Study
Tình huống
Phase 1: Documentation từ subagent
Phase 2: Migration COBOL → Java
Case studies theo role
Backend Engineer — tìm deprecated function usage
DevOps — phân tích log incident
Architect — parallel review 5 modules
Frontend Engineer — WCAG accessibility audit
Open Source Maintainer — triage incoming issues
Customization nâng cao
Persistent memory
Preload skills
Tool restrictions — subagent read-only
Custom system prompt — focus chuyên môn
Anti-patterns
Spawn subagent cho task cần interactive back-and-forth
Custom subagent có ALL tools — mất đi ý nghĩa tách biệt
Không check .claude/agents/ vào repo
Spawn subagent cho task tiny dưới 5 phút
Forget rằng main agent không "thấy" journey của subagent → khó debug
Mẹo nâng cao
Parallel subagents: 4 cái cùng lúc = 4x throughput
Subagent chain: A research → B implement
Chọn đúng built-in cho task
Subagent + skill combo cho specialized workflow
Verify subagent output khi critical
Áp dụng ngay
Bài tập 1 (15 phút): Spawn Explore subagent trên project của bạn
Bài tập 2 (25 phút): Tạo custom subagent cho project
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
2.8 - Subagents​
Modified April 20
Bài 2.8: Subagents​
Module: Hệ sinh thái mở rộng​
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
✅ Giải thích subagent là gì và cơ chế forked context hoạt động như thế nào​
•
✅ Sử dụng thành thạo 3 built-in subagents: general-purpose, Explore, Plan​
•
✅ Tạo custom subagent qua lệnh /agents với tools, scope, và system prompt riêng​
•
✅ Phân biệt khi nào nên dùng subagent thay vì để main agent xử lý trực tiếp​
•
✅ Customize subagent nâng cao: persistent memory, preloaded skills, tool restrictions​
Mở đầu: "You get the answer without the journey"​
Hãy tưởng tượng bạn vừa được assign vào một codebase mới — một hệ thống e-commerce mà team vừa mua lại. Sếp cần biết ngay: "Authentication endpoint nằm ở đâu?"​
Bạn mở Claude Code và hỏi thẳng.​
Không có subagent, Claude bắt đầu một cuộc hành trình khám phá:​
•
Đọc package.json để hiểu dependencies — 1.200 token​
•
Scan src/ với glob pattern để tìm file liên quan — 2.400 token​
•
Đọc src/app.ts, src/server.ts, src/routes/index.ts — 4.100 token​
•
Grep "auth" toàn project — 3.800 kết quả, mỗi hit load vào context — 6.200 token​
•
Đọc thêm 8 file middleware để trace request flow — 7.300 token​
•
Cuối cùng: "Endpoint nằm ở src/api/auth/login.ts dòng 42"​
Tổng thiệt hại: 25.000 token cho context window của bạn. Và Claude vẫn đang "nhớ" tất cả 15 file đó trong suốt phần còn lại của session, dù bạn không cần nữa.​
Có subagent, bạn chỉ thấy:​
​
Code block​
Plain Text
Copy
> Spawn Explore subagent để tìm authentication endpoint.​
​
Comments (0)
Help Center
Keyboard Shortcuts
