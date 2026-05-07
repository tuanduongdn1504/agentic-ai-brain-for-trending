# 2.10 - MCP — Kết nối Claude Code với thế giới bên ngoài

**Source:** https://transform.sg.larksuite.com/wiki/VnVwwB9wViGL5BkOJh5lqp6SgXf
**Wiki ID:** VnVwwB9wViGL5BkOJh5lqp6SgXf
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

2.10 - MCP — Kết nối Claude Code với thế giới bên ngoài

Last updated: Apr 20

Log In or Sign Up
2.10 - MCP — Kết nối Claude Code với thế giới bên ngoài
Bài 2.10: MCP — Kết nối Claude Code với thế giới bên ngoài
Mục tiêu học tập
Mở đầu: Từ copy-paste đến fetch tự động
MCP là gì?
Khái niệm cốt lõi: Tools
ASCII diagram: Kiến trúc MCP
2 loại MCP server
HTTP servers — Remote, hosted by service provider
Stdio servers — Local processes trên máy bạn
Bảng so sánh HTTP vs Stdio
Add MCP Server
Cú pháp cơ bản
Quản lý servers với /mcp
3 Scope của MCP server
Typical use case
.mcp.json example (project scope)
CRITICAL: Context Cost của MCP
MCP servers add tool definitions — kể cả khi bạn không dùng
Tính toán thực tế
Audit và clean up với /mcp
Auto tool search mode (unstable)
CRITICAL: MCP vs CLI vs Skill — Decision tree
Decision tree
Bảng so sánh CLI vs MCP vs Skill
Anthropic internal example: cu tool
Ví dụ thực chiến: Setup Linear + Context7 + Slack cho dev team
Bối cảnh
Bước 1: Add Linear MCP (HTTP, OAuth)
Bước 2: Add Context7 MCP (HTTP)
Bước 3: Add Slack MCP (HTTP)
Bước 4: Save vào .mcp.json project, commit
Bước 5: Team clone repo → auto get MCP servers
Bước 6: /mcp audit context cost — disable khi không cần
Case studies theo role
Backend Engineer: Postgres MCP + Plan Mode
DevOps/SRE: Incident Response với Datadog + PagerDuty
Frontend Engineer: Figma MCP fetch design specs
Product Manager: Sprint Summary
Marketing: weekly metrics digest
Anti-patterns
Anti-pattern 1: Bật mọi MCP server "phòng khi cần"
Anti-pattern 2: Dùng MCP khi CLI đã đủ tốt
Anti-pattern 3: Hardcode API key trong .mcp.json
Anti-pattern 4: Không refresh OAuth token định kỳ
Anti-pattern 5: Skip /mcp audit — MCP zombie
Anti-pattern 6: Dùng MCP cho one-off task
Mẹo nâng cao
Mẹo 1: Local MCP server cho internal tools
Mẹo 2: .mcp.json template cho organization
Mẹo 3: Multiple environment — dev vs prod MCP
Mẹo 4: Combine MCP + Skill cho workflows phức tạp
2.10 - MCP — Kết nối Claude Code với thế giới bên ngoài​
Modified April 20
Bài 2.10: MCP — Kết nối Claude Code với thế giới bên ngoài​
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
✅ Giải thích MCP là gì và tại sao nó là open standard quan trọng với hệ sinh thái agentic AI​
•
✅ Add MCP server (HTTP và stdio) bằng claude mcp add và cấu hình auth đúng cách​
•
✅ Chọn đúng scope (local / user / project) cho từng MCP server trong từng tình huống​
•
✅ Dùng /mcp để audit context cost và disable server không cần thiết​
•
✅ Quyết định khi nào dùng MCP, khi nào dùng CLI, khi nào dùng Skill​
Mở đầu: Từ copy-paste đến fetch tự động​
Đỗ Minh Khoa là backend engineer tại một startup fintech. Hôm nay anh cần review pull request cho ticket Linear MEN-12 — một thay đổi trong payment reconciliation flow.​
Trước khi có MCP:​
Khoa mở Linear trong browser, đọc ticket. Copy requirements. Mở terminal, mở Claude Code. Paste toàn bộ nội dung ticket vào prompt: "Đây là yêu cầu: [dán 400 từ]. Review PR này theo yêu cầu đó." Claude đọc, review. Mất khoảng 5 phút cho việc copy-paste, chưa kể khi ticket thay đổi (PM vừa update acceptance criteria) thì bản copy đã outdated và Claude đưa ra nhận xét không còn chính xác.​
Sau khi add Linear MCP:​
​
Code block​
Plain Text
Copy
> review PR #238 theo requirements của ticket MEN-12​
​
​
Claude tự fetch ticket MEN-12 từ Linear — description, acceptance criteria, comments mới nhất của PM — rồi cross-check với diff của PR. Toàn bộ diễn ra trong 30 giây. Không copy-paste. Không outdated. Claude có đúng context thực tế.​
Comments (0)
Help Center
Keyboard Shortcuts
