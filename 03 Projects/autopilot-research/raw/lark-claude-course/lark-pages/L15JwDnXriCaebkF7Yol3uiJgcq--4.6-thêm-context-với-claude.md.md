# 4.6 - Thêm context với CLAUDE.md

**Source:** https://transform.sg.larksuite.com/wiki/L15JwDnXriCaebkF7Yol3uiJgcq
**Wiki ID:** L15JwDnXriCaebkF7Yol3uiJgcq
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

4.6 - Thêm context với CLAUDE.md

Last updated: Apr 20

Log In or Sign Up
4.6 - Thêm context với CLAUDE.md
Bài 4.6: Thêm context với CLAUDE.md
Mục tiêu học tập
Mở đầu: Cái giá của "quên việc"
CLAUDE.md là gì?
Luồng hoạt động
Hai vai trò chính
Lệnh /init — Sinh CLAUDE.md tự động
Khi Claude xin permission
Ví dụ output điển hình sau /init
Ba vị trí của CLAUDE.md
Quy tắc phân loại nội dung
Sai lầm phổ biến
CLAUDE.md không phải silver bullet — vẫn có giới hạn
Thêm hướng dẫn tùy chỉnh qua memory mode (#)
Khi nào nên dùng memory mode?
Ví dụ conversation thực tế
Cú pháp @ — Mention file cụ thể
Khác biệt với CLAUDE.md
Dùng @ bên trong CLAUDE.md
Ví dụ thực chiến: Onboard một team 8 engineer
Tình huống
Bước 1: Mở repo, chạy /init
Bước 2: Thêm team conventions (viết tay)
Bước 3: Commit & broadcast
Bước 4: Mỗi dev tự customize local
Kết quả sau 2 tuần
Case studies theo ngành
💰 Finance Engineer — Compliance-aware Claude
⚖️ Legal Tech — Dữ liệu nhạy cảm không leak
🏥 Healthcare SaaS — HIPAA boundary
📣 Marketing Agency — Brand voice consistency
🛠️ Product Engineer — Migration dần dần
Prompt templates cho CLAUDE.md
Anti-patterns — Những sai lầm cần tránh
❌ Viết CLAUDE.md như brochure giới thiệu sản phẩm
❌ Nhồi quá nhiều rule — không ưu tiên
❌ Rule "negative" không có alternative
❌ Commit secrets hoặc path cá nhân
❌ Không update khi codebase thay đổi
❌ Giả định model hiểu implicit
Mẹo nâng cao
Mẹo 1: Dùng section heading cho Claude scan nhanh
Mẹo 2: Versioning nhẹ
Mẹo 3: Test CLAUDE.md như test code
Mẹo 4: Phân tầng rule theo độ nghiêm ngặt
Áp dụng ngay
Bài tập 1: Bootstrap CLAUDE.md cho project thật của bạn (15 phút)
Bài tập 2 (optional, 30 phút): Audit CLAUDE.md cũ
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
4.6 - Thêm context với CLAUDE.md​
Modified April 20
Bài 4.6: Thêm context với CLAUDE.md​
Module: 3 — Quy trình cơ bản​
Thời gian ước tính: 30 phút (đọc) + 15 phút (thực hành)​
Mức độ: Cơ bản → Trung cấp​
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
✅ Giải thích vai trò của file CLAUDE.md như "bộ nhớ dự án" mà Claude đọc lại ở mỗi request​
•
✅ Dùng /init để Claude tự sinh CLAUDE.md đầu tiên từ codebase​
•
✅ Phân biệt ba vị trí đặt CLAUDE.md (project, local, global) và biết file nào chia sẻ với team​
•
✅ Thêm hướng dẫn cá nhân qua memory mode (#) mà không cần mở file thủ công​
•
✅ Tham chiếu file cụ thể bằng cú pháp @ — cả trong chat lẫn trong CLAUDE.md​
•
✅ Nhận diện 5 lỗi phổ biến khi viết CLAUDE.md và cách viết để Claude thực sự tuân theo​
Mở đầu: Cái giá của "quên việc"​
Hãy hình dung bạn là một senior engineer vừa onboard vào team mới. Sáng thứ Hai, bạn mở Claude Code trong repo 40,000 dòng chưa từng thấy, gõ:​
"Thêm một endpoint mới GET /users/:id/invoices trả về 20 hóa đơn gần nhất của user."​
Claude trả lời sau 45 giây. Code chạy. Test pass. Nhưng reviewer PR gắn 6 comment:​
•
"Dùng Drizzle ORM, sao lại import Prisma?"​
•
"Folder này phải có file .schema.ts kèm theo mỗi route — convention của team."​
•
"Bọn mình pascal-case cho DTO, không phải camelCase."​
•
"Response đã có helper paginated() rồi, sao viết lại pagination tay?"​
•
"Bạn chưa add vào openapi.yaml — CI sẽ fail."​
•
"Comment in-line dạng // get user id — thừa."​
Không phải Claude viết sai. Claude viết chính xác theo default — nhưng default không phải là convention của team bạn. Claude không có cách nào biết team dùng Drizzle, không biết bạn có helper paginated(), không biết quy tắc comment.​
Cách đắt nhất để giải quyết: mỗi lần gõ prompt, copy-paste lại toàn bộ convention → 200 dòng boilerplate mỗi request, tốn token, còn dễ quên.​
Comments (0)
Help Center
Keyboard Shortcuts
