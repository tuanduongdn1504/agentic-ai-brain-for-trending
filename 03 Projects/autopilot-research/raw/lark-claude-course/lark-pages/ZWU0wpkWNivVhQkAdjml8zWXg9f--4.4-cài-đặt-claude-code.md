# 4.4 - Cài đặt Claude Code

**Source:** https://transform.sg.larksuite.com/wiki/ZWU0wpkWNivVhQkAdjml8zWXg9f
**Wiki ID:** ZWU0wpkWNivVhQkAdjml8zWXg9f
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

4.4 - Cài đặt Claude Code

Last updated: Apr 20

Log In or Sign Up
4.4 - Cài đặt Claude Code
Bài 4.4: Cài đặt Claude Code
Mục tiêu học tập
Mở đầu: Tại sao cài Claude Code không giống cài một CLI bình thường?
Các option cài đặt
Chọn option nào?
Cài đặt bước-bằng-bước
macOS với Homebrew
macOS / Linux / WSL với install script
Windows (CMD)
Authenticate lần đầu
Chọn option nào?
Option 1: Login với Pro/Max
Option 2: API key
Option 3: AWS Bedrock (enterprise)
Option 4: GCP Vertex AI
Verify cài đặt đầy đủ
Test 1: Version check
Test 2: Simple conversation
Test 3: File operation
Ví dụ thực chiến: Onboard dev mới trong team
Tình huống
Script onboard (tech lead viết, dùng cho mọi dev mới)
Kết quả
Case studies theo ngành
🏭 Enterprise SaaS — Bedrock cho compliance
🎓 EdTech — Classroom license
🛠️ Devtool startup — Dogfooding
Anti-patterns khi cài đặt
❌ Cài xong không update PATH
❌ API key commit vào git
❌ Dùng chung API key cho cả team
❌ Cài Claude Code nhưng chưa cài Node.js
❌ Cài bản cũ, không update
Troubleshooting 5 lỗi phổ biến
Lỗi 1: "SSL certificate verify failed"
Lỗi 2: "Command not found: claude" sau khi cài
Lỗi 3: "Rate limit exceeded"
Lỗi 4: "Authentication failed" ngẫu nhiên
Lỗi 5: Windows — "Cannot execute binary"
Áp dụng ngay
Bài tập 1: Cài đặt + verify (15 phút)
Bài tập 2 (optional, 10 phút): Setup global CLAUDE.md
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
4.4 - Cài đặt Claude Code​
Modified April 20
Bài 4.4: Cài đặt Claude Code​
Module: 2 — Khởi động​
Thời gian ước tính: 15 phút (cài) + 5 phút (verify)​
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
Slide: Claude Code in Action.pdf​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Cài đặt Claude Code trên macOS, Linux hoặc Windows​
•
✅ Authenticate lần đầu và lựa chọn đúng mode (Pro/Max subscription hoặc API key)​
•
✅ Biết chạy Claude Code với AWS Bedrock hoặc Google Cloud Vertex (enterprise)​
•
✅ Verify cài đặt bằng một test prompt end-to-end​
•
✅ Fix 5 lỗi cài đặt phổ biến nhất​
Mở đầu: Tại sao cài Claude Code không giống cài một CLI bình thường?​
Nghĩ thử: cài curl hay git = tải binary → chạy. Xong.​
Claude Code thì khác. Nó là CLI, nhưng mỗi lần bạn gõ prompt, LM Claude ở server Anthropic là thứ thực sự "nghĩ". Tức là:​
•
Máy bạn cần binary Claude Code​
•
Máy bạn cần network đến Anthropic API (hoặc AWS Bedrock / GCP Vertex)​
•
Authentication đúng = bạn có quota gọi model​
•
Permission đúng = Claude Code không bị chặn write file​
Bỏ qua một bước = gặp lỗi khó hiểu sau này. Bài này đi qua từng bước với mindset "ít phút bây giờ = tiết kiệm hàng giờ debug sau".​
Các option cài đặt​
​
Code block​
Plain Text
Copy
┌────────────────────────────────────────────────────────────┐​
│                                                            │​
│  Option 1: Homebrew (macOS)                                │​
​
Comments (0)
Help Center
Keyboard Shortcuts
