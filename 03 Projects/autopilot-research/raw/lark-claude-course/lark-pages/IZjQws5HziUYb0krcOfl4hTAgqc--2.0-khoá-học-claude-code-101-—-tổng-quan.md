# 2.0 - Khoá học Claude Code 101 — Tổng quan

**Source:** https://transform.sg.larksuite.com/wiki/IZjQws5HziUYb0krcOfl4hTAgqc
**Wiki ID:** IZjQws5HziUYb0krcOfl4hTAgqc
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

2.0 - Khoá học Claude Code 101 — Tổng quan

Last updated: Apr 20

Log In or Sign Up
2.0 - Khoá học Claude Code 101 — Tổng quan
Khoá học Claude Code 101 — Tổng quan
Tại sao học khoá này?
Bạn sẽ học được gì?
Về tư duy
Về kỹ năng
Về mở rộng
Lộ trình 11 bài học
Cách học hiệu quả
Quy tắc 70/20/10 áp dụng cho khoá này
3 nhóm reader — 3 path tiếp cận
Những gì bạn cần chuẩn bị
Bắt buộc
Nên có
Không cần
Triết lý xuyên suốt khoá học
1. "Don't write code yet"
2. "Be Claude's PM"
3. "If it should always happen, hook it"
Sai lầm người mới thường gặp
Bạn sẵn sàng chưa?
Bắt đầu nào
2.0 - Khoá học Claude Code 101 — Tổng quan​
Modified April 20
Khoá học Claude Code 101 — Tổng quan​
Khoá học: Claude Code 101​
Phiên bản: v1.0 — Bản tiếng Việt dành cho developer và builder​
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
Tại sao học khoá này?​
Hãy thành thật một chút.​
Bạn đang làm việc với một AI assistant — có thể là ChatGPT, GitHub Copilot, hay Claude trên web — và mỗi ngày bạn lặp lại một quy trình quen thuộc đến mức nhàm chán:​
•
Mở chat tab mới, copy một đoạn code vào, giải thích context từ đầu​
•
Nhận câu trả lời, copy ngược lại vào IDE, sửa tay những chỗ không khớp​
•
Hỏi thêm câu tiếp theo, lại phải nhắc lại "project này dùng pnpm nhé, không phải npm"​
•
Đóng tab, mở session mới hôm sau — và mọi thứ biến mất, bắt đầu từ đầu​
Đây không phải vấn đề của riêng bạn. Đây là cách phần lớn developer đang dùng AI: như một search engine thông minh hơn, không phải như một công cụ lập trình thực sự.​
Vấn đề là gì? Bạn đang thiếu persistent context — khả năng để AI thực sự hiểu project của bạn, nhớ các quyết định đã thống nhất, và làm việc trực tiếp trên codebase thay vì qua copy-paste. Bạn cũng thiếu agentic loop — thay vì AI chỉ trả lời câu hỏi, nó có thể tự chạy lệnh, đọc file, test code, sửa lỗi, và commit — tất cả mà không cần bạn ngồi canh từng bước.​
Claude Code ra đời để giải quyết đúng hai vấn đề này. Nó không phải là một chat interface. Nó là một agentic coding tool chạy trong terminal, có thể đọc toàn bộ codebase, chạy bash, gọi tool, và làm việc liên tục trên nhiều file. Anthropic đã dùng nó nội bộ và khi cho nhân viên dùng thử lần đầu, "daily actives went straight up for three days."​
Khoá học này sẽ đưa bạn từ "copy-paste qua chat tab" đến "làm việc cùng Claude như một senior dev luôn hiểu project của bạn." Từ "punch cards" đến "prompts" — theo nghĩa thực sự của cụm từ đó.​
Bạn sẽ học được gì?​
Sau khi hoàn thành khoá học, bạn sẽ có thể:​
Về tư duy​
•
Giải thích agentic loop hoạt động thế nào — tại sao Claude Code có thể "tự làm" thay vì chỉ "tự trả lời"​
•
Áp dụng EPCC mindset (Explore → Plan → Code → Commit) thay vì nhảy thẳng vào code như phản xạ tự nhiên​
Comments (0)
Help Center
Keyboard Shortcuts
