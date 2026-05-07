# 2.1 - Cách Claude Code hoạt động

**Source:** https://transform.sg.larksuite.com/wiki/YvYkwSpxxiCetvkTR46lxY0pgrf
**Wiki ID:** YvYkwSpxxiCetvkTR46lxY0pgrf
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

2.1 - Cách Claude Code hoạt động

Last updated: Apr 20

Log In or Sign Up
2.1 - Cách Claude Code hoạt động
Bài 2.1: Cách Claude Code hoạt động
Mục tiêu học tập
Lần đầu mở Claude Code
Agentic Loop — Trái tim của Claude Code
Giải thích từng phase
Vai trò của bạn trong loop
Context Window — Bộ nhớ làm việc của Claude
Tools — Xương sống của mọi agent
Permission Modes — Bạn kiểm soát mức độ tự chủ
So sánh: Claude Code vs Chat AI thông thường
Ví dụ thực chiến: Thêm WebP conversion vào image upload pipeline
Case studies theo role
Backend Engineer: Refactor authentication module
DevOps Engineer: Debug production incident lúc 2 giờ sáng
Designer ship code: Megan's case study
Open source contributor: Khám phá codebase lạ
Data Engineer: ETL pipeline với built-in verification
Anti-patterns — Những cách dùng sai phổ biến
Anti-pattern 1: Dùng Claude Code như chat thông thường
Anti-pattern 2: Auto-accept mọi thứ mà không đọc plan
Anti-pattern 3: Bỏ qua permission review vì "phiền quá"
Anti-pattern 4: Bị "ám" bởi tư duy autocomplete
Anti-pattern 5: Tin kết quả mù quáng, bỏ qua verify step
Áp dụng ngay
Bài tập 1 (10 phút): Quan sát agentic loop trong thực tế
Bài tập 2 (15 phút): Task multi-step với verify tự động
Tóm tắt
Bài tiếp theo
Tài liệu tham khảo
2.1 - Cách Claude Code hoạt động​
Modified April 20
Bài 2.1: Cách Claude Code hoạt động​
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
✅ Giải thích agentic loop là gì và tại sao nó khác hoàn toàn với chat AI thông thường​
•
✅ Hiểu context window là gì ở mức tổng quan (overview) — để không bị bất ngờ khi Claude "quên"​
•
✅ Nắm 3 permission modes và khi nào nên dùng cái nào​
•
✅ Phân biệt Claude Code với Cursor, Copilot và các AI autocomplete tools khác​
•
✅ Nhận ra agentic loop đang diễn ra trong thực tế khi quan sát Claude làm việc​
​
​
Lần đầu mở Claude Code​
Hãy nhớ lại lần đầu bạn dùng GitHub Copilot hay Cursor.​
Bạn gõ một vài ký tự. Editor gợi ý tiếp theo. Bạn nhấn Tab để accept. Nó gợi ý thêm. Bạn tiếp tục gõ. Vòng lặp đó — bạn gõ, AI phản ứng, bạn gõ tiếp — diễn ra trong vài giây, liên tục, reactive.​
Giờ nhớ lại lần đầu bạn mở Claude Code.​
Terminal xuất hiện. Bạn gõ một yêu cầu: "Thêm tính năng export CSV vào admin dashboard." Bạn nhấn Enter. Và Claude Code... bắt đầu tự làm việc.​
Nó đọc file này. Grep cái kia. Đọc thêm 3 file nữa. Sửa code. Chạy test. Test fail — nó quay lại sửa. Chạy test lần nữa. Test pass. Nó hỏi bạn: "Tôi đã implement xong. Bạn có muốn commit không?"​
Bạn ngồi đó, không gõ gì, mà feature đã xong.​
Đó là khoảnh khắc mà nhiều developer mô tả là "jaw drop" — cú sốc nhận thức rằng đây không phải autocomplete. Không phải AI gợi ý code cho bạn gõ. Đây là một agent tự chạy, tự nghĩ, tự kiểm tra, và chỉ quay lại hỏi bạn khi thực sự cần.​
Đội ngũ Anthropic đã nói thẳng: "Gone from punch cards to prompts" — chúng ta đã đi từ thẻ đục lỗ đến prompt. Giao diện lập trình đang thay đổi căn bản, không phải chỉ nhanh hơn hay thông minh hơn, mà thay đổi về bản chất.​
Và khi ai đó hỏi tại sao Claude Code lại tốt đến vậy, câu trả lời thường là: "Đây là công cụ mà mọi người ở Anthropic dùng hàng ngày." Không phải demo. Không phải showcase. Đây là tool mà team đã build cho chính mình — và giờ chia sẻ với thế giới.​
Comments (0)
Help Center
Keyboard Shortcuts
