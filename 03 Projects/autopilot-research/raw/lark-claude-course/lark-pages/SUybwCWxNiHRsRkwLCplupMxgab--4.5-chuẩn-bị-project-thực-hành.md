# 4.5 - Chuẩn bị project thực hành

**Source:** https://transform.sg.larksuite.com/wiki/SUybwCWxNiHRsRkwLCplupMxgab
**Wiki ID:** SUybwCWxNiHRsRkwLCplupMxgab
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

4.5 - Chuẩn bị project thực hành

Last updated: Apr 20

Log In or Sign Up
4.5 - Chuẩn bị project thực hành
Bài 4.5: Chuẩn bị project thực hành
Mục tiêu học tập
Mở đầu: Tại sao không học trên project giả?
Uigen là gì?
Giới thiệu
Tech stack
Tại sao chọn project này?
Yêu cầu trước khi setup
Bắt buộc
Optional (khuyến khích cho trải nghiệm đầy đủ)
Kiểm tra prerequisite
Setup bước-bằng-bước
Bước 1: Tải source
Bước 2: Setup
Bước 3 (optional): Cấu hình API key
Bước 4: Chạy dev server
Bước 5: Test end-to-end
Cấu trúc project cần hiểu
Nếu bạn muốn dùng project riêng
Ví dụ thực chiến: Setup + first task
Tình huống
Prompt
Kết quả
Case studies setup tương tự
💼 Startup founder — Học Claude Code trên MVP thực
🏫 University CS professor — Setup cho 60 sinh viên
🛠️ Tech team lead — Uigen cho team workshop
Anti-patterns khi setup
❌ Bỏ qua npm run setup vì "tôi biết npm install rồi"
❌ Dùng Node.js 16 hoặc cũ hơn
❌ Chạy project trong folder path có space hoặc tiếng Việt
❌ Commit .env với API key
❌ Không verify app chạy được trước khi qua Bài 4.6
Áp dụng ngay
Bài tập 1: Setup + verify uigen (15 phút)
Bài tập 2 (optional, 10 phút): Explore với Claude Code
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
4.5 - Chuẩn bị project thực hành​
Modified April 20
Bài 4.5: Chuẩn bị project thực hành​
Module: 2 — Khởi động​
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
Slide: Claude Code in Action.pdf​
​
​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Setup project uigen để thực hành xuyên suốt các bài sau​
•
✅ Biết cách sử dụng project của bạn như một lựa chọn thay thế​
•
✅ Chạy app local, test Claude API integration (optional)​
•
✅ Verify môi trường dev sẵn sàng cho Bài 4.6 trở đi​
•
✅ Troubleshoot lỗi phổ biến khi setup Next.js + SQLite​
​
​
Mở đầu: Tại sao không học trên project giả?​
Khóa học này có thể đưa bạn vào một "sandbox giả lập" — kiểu chỉ có 3 file toy, làm quick demo rồi next bài. Chúng tôi không làm vậy. Lý do:​
Claude Code chỉ phát huy khi ở codebase thực sự. Với 3 file, Grep không cần thiết, Planning Mode cũng vô dụng, Hooks không có gì để hook vào. Bạn sẽ không cảm nhận được giá trị.​
Giải pháp: chúng tôi cung cấp uigen — một Next.js app thật, nhỏ nhưng có cấu trúc đầy đủ (API route, DB, React component, test, prompt template). Bạn có thể:​
•
Follow example chính xác như khóa học​
•
Hoặc dùng project thật của bạn (khuyên dùng nếu có) — chỉ cần đọc kỹ để map concept​
💡 Quan điểm của chúng tôi: Học tốt nhất là trên project bạn đang thật sự care. Nếu có side project, work project thoải mái mang vào khóa — uigen là backup.​
​
​
Uigen là gì?​
Giới thiệu​
Uigen = "UI generator". Một Next.js 14 web app dùng Claude API để generate React component từ prompt người dùng.​
Comments (0)
Help Center
Keyboard Shortcuts
