# 2.2 - Cài đặt Claude Code

**Source:** https://transform.sg.larksuite.com/wiki/FUxrwBZ5OizNDekPyiFl4WvigQb
**Wiki ID:** FUxrwBZ5OizNDekPyiFl4WvigQb
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

2.2 - Cài đặt Claude Code

Last updated: Apr 20

Log In or Sign Up
2.2 - Cài đặt Claude Code
Bài 2.2: Cài đặt Claude Code
Mục tiêu học tập
Mở đầu: 30 giây vs 30 phút
5 cách cài đặt Claude Code
Surface 1: Terminal (Recommended)
macOS và Linux (hoặc WSL trên Windows)
Windows (không dùng WSL)
Surface 2: VS Code Extension
Surface 3: JetBrains Plugin
Surface 4: Claude Desktop
Surface 5: Web (claude.ai/code)
So sánh 5 surfaces
Ví dụ step-by-step: Cài Claude Code lần đầu trên macOS
Bước 1: Cài Claude Code bằng curl
Bước 2: Mở project và khởi động Claude Code
Bước 3: Chọn theme và đăng nhập
Bước 4: Prompt đầu tiên để test
Case studies theo role
Indie hacker — laptop cá nhân, solo project
Engineering lead — team 8 người, startup fintech
Designer (non-technical) — ship code lần đầu
Mobile developer — Android Studio, IntelliJ
Remote / distributed team — làm việc trên nhiều máy, nhiều timezone
Anti-patterns
Anti-pattern 1: Cài Homebrew/winget mà không biết không có auto-update
Anti-pattern 2: Chạy claude từ home directory ($HOME)
Anti-pattern 3: Login bằng Pro account khi org có Enterprise
Anti-pattern 4: Cài VS Code extension từ author không phải Anthropic
Anti-pattern 5: Mix terminal + IDE đồng thời cùng một project
Áp dụng ngay
Bài tập 1 (10 phút): Cài Claude Code và prompt đầu tiên
Bài tập 2 (5 phút): Khám phá các mode với Shift+Tab
Tóm tắt
Bài tiếp theo
Tài liệu tham khảo
2.2 - Cài đặt Claude Code​
Modified April 20
Bài 2.2: Cài đặt Claude Code​
Module: Nền tảng​
Thời gian ước tính: 20 phút​
Mức độ: Cơ bản​
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
​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Cài Claude Code thành công trên hệ điều hành của mình (macOS, Linux, WSL, hoặc Windows)​
•
✅ Chọn surface phù hợp với workflow của bạn (terminal, IDE, desktop, hoặc web)​
•
✅ Hiểu pricing và các authentication options (Pro, Max, API key, Enterprise)​
•
✅ Biết cách update Claude Code đúng cách và tránh bị kẹt ở version cũ​
​
​
Mở đầu: 30 giây vs 30 phút​
Nhớ lại lần đầu bạn cài một IDE plugin "AI assistant" nào đó. Bạn vào trang docs, thấy một danh sách bước dài 14 bước. Bước 1: cài extension. Bước 2: tạo account trên platform của vendor. Bước 3: generate API key. Bước 4: vào settings, tìm tab "Integrations", nhập endpoint URL. Bước 5: cấu hình JWT expiry. Bước 6: đặt port. Bước 7: restart IDE. Bước 8: nếu IDE không nhận, clear cache và thử lại...​
30 phút sau, bạn vẫn đang đọc StackOverflow, không rõ tại sao plugin báo "Connection refused".​
Claude Code khác hoàn toàn.​
Toàn bộ quá trình cài đặt trên macOS hoặc Linux là một dòng lệnh:​
​
Code block​
Bash
Copy
curl -fsSL https://claude.ai/install.sh | sh​
​
​
Chạy xong, gõ claude, và Claude Code tự walk-through phần còn lại — chọn theme, đăng nhập, xong. Tổng cộng khoảng 30 giây nếu bạn đã có tài khoản Anthropic.​
Điều đáng nói hơn là sự đơn giản này không phải là do Claude Code thiếu tính năng. Ngược lại — đây là tool mà toàn bộ team engineering tại Anthropic dùng mỗi ngày. Như một kỹ sư trong team chia sẻ: "This is the same tool everyone at Anthropic uses every day. We debated: is this secret sauce? Are we sure we want to give it to people?"​
Comments (0)
Help Center
Keyboard Shortcuts
