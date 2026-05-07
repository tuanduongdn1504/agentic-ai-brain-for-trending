# 4.1 - Giới thiệu khóa học "Claude Code in Action"

**Source:** https://transform.sg.larksuite.com/wiki/VKetwBqv6irPVrkY6ijlyNXxgcf
**Wiki ID:** VKetwBqv6irPVrkY6ijlyNXxgcf
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

4.1 - Giới thiệu khóa học "Claude Code in Action"

Last updated: Apr 20

Log In or Sign Up
4.1 - Giới thiệu khóa học "Claude Code in Action"
Bài 4.1: Giới thiệu khóa học "Claude Code in Action"
Mục tiêu học tập
Mở đầu: Từ "AI gợi ý code" đến "AI làm việc"
Một ví dụ cụ thể
Khóa học này dành cho ai?
✅ Phù hợp nếu bạn:
❌ Chưa phù hợp nếu bạn:
Lộ trình 6 module, 20 bài
Cách học hiệu quả nhất
Quy tắc 70/20/10 áp dụng cho khóa này
3 nhóm học viên — 3 cách tiếp cận
Chuẩn bị trước khi bắt đầu
Bắt buộc
Nên có
Không cần
Triết lý xuyên suốt khóa học
1. "Context là vua — quản lý context là kỹ năng cao nhất"
2. "Verify, don't trust"
3. "Prompt là code, CLAUDE.md là config"
4. "Tự động hóa điểm đau, không phải toàn bộ"
Lời khuyên từ người đi trước
Bạn sẵn sàng chưa?
Bắt đầu nào
Tài liệu tham khảo
4.1 - Giới thiệu khóa học "Claude Code in Action"​
Modified April 20
Bài 4.1: Giới thiệu khóa học "Claude Code in Action"​
Module: 1 — Nền tảng​
Thời gian ước tính: 15 phút​
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
✅ Giải thích khóa học giải quyết vấn đề gì cho bạn với tư cách developer​
•
✅ Nhận diện đối tượng học viên phù hợp và đối tượng chưa sẵn sàng​
•
✅ Hình dung được lộ trình 20 bài + 6 module và cách các bài liên kết với nhau​
•
✅ Chuẩn bị đúng môi trường, mindset, kỳ vọng trước khi bắt đầu Bài 4.2​
​
​
Mở đầu: Từ "AI gợi ý code" đến "AI làm việc"​
Bạn đã dùng Copilot, Tabnine, hay thậm chí ChatGPT để copy code vào file. Có lúc tuyệt, có lúc bực. Vì sao?​
Vì tất cả những tool đó về bản chất đều là "autocomplete thông minh". Chúng gợi ý — bạn vẫn là người đọc file, edit code, chạy test, review diff. Khi task nhỏ (viết một hàm, sửa một bug), flow này OK. Nhưng khi task lớn — "refactor module auth", "migrate Prisma sang Drizzle", "thêm feature pagination cho 12 endpoint" — quy trình "copy-paste-chạy" vẫn tốn 80% thời gian của bạn.​
Claude Code khác ở đâu?​
Claude Code là một agentic coding assistant: nó không chỉ gợi ý, nó hành động. Nó đọc file của bạn, chạy command, sửa code, chạy test, xem kết quả, tự fix — trong một vòng lặp mà bạn chỉ review khi cần can thiệp.​
Kết quả: thay vì bạn làm + AI gợi ý, flow thành AI làm + bạn duyệt. Đây là dịch chuyển lớn nhất của lập trình trong thập kỷ qua.​
Một ví dụ cụ thể​
Task: "Thêm feature xuất invoice PDF cho user, có preview trong dashboard."​
Với autocomplete AI truyền thống:​
1.
Bạn search codebase tìm chỗ đặt route (5 phút)​
2.
Bạn gọi AI gợi ý tạo route stub, copy vào file (5 phút)​
3.
Bạn cài thư viện @react-pdf/renderer (5 phút)​
Comments (0)
Help Center
Keyboard Shortcuts
