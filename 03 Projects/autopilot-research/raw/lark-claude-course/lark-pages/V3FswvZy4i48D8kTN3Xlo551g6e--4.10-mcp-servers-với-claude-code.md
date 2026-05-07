# 4.10 - MCP servers với Claude Code

**Source:** https://transform.sg.larksuite.com/wiki/V3FswvZy4i48D8kTN3Xlo551g6e
**Wiki ID:** V3FswvZy4i48D8kTN3Xlo551g6e
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

4.10 - MCP servers với Claude Code

Last updated: Apr 20

Log In or Sign Up
4.10 - MCP servers với Claude Code
Bài 4.10: MCP servers với Claude Code
Mục tiêu học tập
Mở đầu: Vấn đề "tool use cứng"
MCP là gì?
Analogy "USB-C cho AI"
3 thứ MCP server có thể cung cấp
Hệ sinh thái MCP hiện có
Một số MCP server phổ biến
Cài đặt MCP server: Ví dụ Playwright
Playwright MCP làm gì?
Bước 1: Cài server
Bước 2: Verify
Bước 3: Hỏi Claude list tool
Bước 4: Cấu hình permission
Bước 5: Restart Claude Code
Ví dụ thực chiến: UI self-improving với Playwright MCP
Tình huống
Flow
Claude execute
Kết quả
CLI tool vs MCP server — Khi nào chọn gì?
Nguyên tắc từ Claude Code team
Lý do
Ví dụ cụ thể
Khám phá MCP ecosystem
Các category thường thấy
Ví dụ thực chiến: Dev stack MCP cho fullstack dev
Setup điển hình
Use case 1: Debug production issue từ Sentry alert
Use case 2: E2E test từ user report
Kết quả
Case studies theo ngành
🏥 Health tech — MCP EHR
💰 Finance — MCP Bloomberg terminal
🏭 Manufacturing — MCP MES
🎓 EdTech — MCP LMS
🛡️ Security — MCP Panther SIEM
Anti-patterns
❌ Cài MCP server random chưa verify
❌ Allow * MCP tool
❌ Dùng MCP cho task CLI tool làm được
❌ MCP server dev-only mà dùng production
❌ Không restart sau khi cài/config MCP
Mẹo nâng cao
Mẹo 1: Scope MCP theo project
Mẹo 2: MCP custom cho team
Mẹo 3: Monitor MCP usage
Mẹo 4: MCP với headless Claude Code (SDK)
Áp dụng ngay
Bài tập 1: Cài Playwright MCP (15 phút)
Bài tập 2 (optional, 20 phút): UI self-review
4.10 - MCP servers với Claude Code​
Modified April 20
Bài 4.10: MCP servers với Claude Code​
Module: 4 — Mở rộng & Tự động hóa​
Thời gian ước tính: 30 phút (đọc) + 20 phút (thực hành)​
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
✅ Giải thích MCP là gì, vì sao Anthropic gọi nó là "USB-C cho AI"​
•
✅ Cài đặt MCP server (ví dụ Playwright) bằng claude mcp add​
•
✅ Cấu hình permission trong settings.local.json để tránh prompt mỗi lần​
•
✅ Sử dụng MCP server để Claude điều khiển browser, query DB, tương tác với tool ngoài​
•
✅ Chọn giữa CLI tool và MCP server cho task cụ thể​
​
​
Mở đầu: Vấn đề "tool use cứng"​
Bài 4.2 đã giải thích tool use. Nhưng thực tế, tool built-in của Claude Code không cover được mọi trường hợp:​
•
Muốn Claude click button trong browser? Không có Click tool built-in.​
•
Muốn Claude query Postgres production (read-only)? Không có PostgreSQL tool.​
•
Muốn Claude reply Slack DM? Không có.​
•
Muốn Claude tạo Jira ticket? Không có.​
Cách cũ để giải quyết:​
1.
Anthropic thêm tool mới vào core (chậm, không scale cho mọi use case)​
2.
Mỗi vendor (Linear, Slack, Postgres) viết integration riêng cho từng LLM tool (nhân đôi công sức)​
MCP giải quyết cái này.​
​
​
MCP là gì?​
MCP = Model Context Protocol. Một giao thức mở (open protocol) do Anthropic công bố tháng 11/2024, cho phép:​
•
Bên thứ 3 tạo "MCP server" (cung cấp tool/resource/prompt)​
Comments (0)
Help Center
Keyboard Shortcuts
