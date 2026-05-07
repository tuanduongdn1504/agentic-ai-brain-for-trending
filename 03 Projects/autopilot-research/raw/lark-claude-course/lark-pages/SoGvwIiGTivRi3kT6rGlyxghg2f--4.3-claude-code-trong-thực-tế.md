# 4.3 - Claude Code trong thực tế

**Source:** https://transform.sg.larksuite.com/wiki/SoGvwIiGTivRi3kT6rGlyxghg2f
**Wiki ID:** SoGvwIiGTivRi3kT6rGlyxghg2f
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

4.3 - Claude Code trong thực tế

Last updated: Apr 20

Log In or Sign Up
4.3 - Claude Code trong thực tế
Bài 4.3: Claude Code trong thực tế
Mục tiêu học tập
Mở đầu: Xem con người vs Claude làm cùng một việc
Dev người làm thế nào (flow thực tế, có timer)
Claude Code làm thế nào
Claude Code có những tool gì sẵn?
Phân loại theo cách dùng
Điều thực sự mạnh: Orchestration
Ví dụ: Refactor rename function
Bài học: Orchestration quan trọng hơn từng tool
Ví dụ thực chiến: Một session 5 phút với Claude Code
Tình huống
Session
Case studies theo ngành
💼 Sales Engineering — Custom demo nhanh
🏭 DevOps — Audit Kubernetes manifest
🎮 Game Development — Bug triage từ Steam review
🏥 Health Tech — Generate FHIR schema từ sample
Anti-patterns: Khi Claude orchestrate sai
❌ Claude skip gather context, đi thẳng vào code
❌ Claude đọc QUÁ nhiều file trước khi action
❌ Claude stuck trong loop Grep → Read → Grep → Read
❌ Bạn tin Claude "đã làm" mà không verify
Mẹo nâng cao
Mẹo 1: Prompt để Claude "suy nghĩ trước hành động"
Mẹo 2: Giới hạn scope rõ ràng
Mẹo 3: Hỏi Claude list tool cho task
Áp dụng ngay
Bài tập 1: Dự đoán tool use (10 phút)
Bài tập 2 (optional, 20 phút): Quan sát orchestration
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
4.3 - Claude Code trong thực tế​
Modified April 20
Bài 4.3: Claude Code trong thực tế​
Module: 2 — Khởi động​
Thời gian ước tính: 20 phút (đọc) + 15 phút (theo dõi demo)​
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
​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Liệt kê các built-in tool của Claude Code và mục đích của mỗi cái​
•
✅ Mô tả cách Claude Code orchestrate nhiều tool để giải task phức tạp​
•
✅ Đoán trước được tool Claude sẽ dùng cho một prompt cụ thể​
•
✅ Phân biệt "task đơn giản 1-tool" với "task phức hợp cần orchestration"​
•
✅ Nhận ra dấu hiệu Claude đang đi sai tool strategy​
​
​
Mở đầu: Xem con người vs Claude làm cùng một việc​
Bài tập thực tế: thêm dark mode cho một Next.js dashboard.​
Dev người làm thế nào (flow thực tế, có timer)​
Minute 0–5: Mở project, tìm file layout. Vì không nhớ Tailwind config ở đâu, find . -name "tailwind.config*". Thấy, mở.​
Minute 5–12: Đọc docs Tailwind về darkMode: 'class'. Thêm vào config.​
Minute 12–20: Tìm toggle component — không có. Tạo mới. Cần sate management → dùng next-themes? Chọn next-themes. npm install.​
Minute 20–35: Code component, import vào layout, test.​
Minute 35–45: Dark mode hoạt động ở page chính. Nhưng nhiều component child vẫn bg-white cứng → phải grep tìm, thay bg-white bằng bg-white dark:bg-slate-900. Làm thủ công cho 20 file.​
Minute 45–55: Chạy dev server, test. Có button primary vẫn sáng quá → vào primary.tsx sửa.​
Minute 55–60: Commit, viết message.​
Tổng: 60 phút.​
Claude Code làm thế nào​
Comments (0)
Help Center
Keyboard Shortcuts
