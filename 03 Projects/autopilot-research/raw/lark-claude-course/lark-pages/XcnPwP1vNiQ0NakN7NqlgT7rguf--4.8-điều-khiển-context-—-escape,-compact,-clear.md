# 4.8 - Điều khiển context — Escape, /compact, /clear

**Source:** https://transform.sg.larksuite.com/wiki/XcnPwP1vNiQ0NakN7NqlgT7rguf
**Wiki ID:** XcnPwP1vNiQ0NakN7NqlgT7rguf
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

4.8 - Điều khiển context — Escape, /compact, /clear

Last updated: Apr 20

Log In or Sign Up
4.8 - Điều khiển context — Escape, /compact, /clear
Bài 4.8: Điều khiển context — Escape, /compact, /clear
Mục tiêu học tập
Mở đầu: Tại sao conversation dài lại tệ?
1. Escape — "Dừng lại, tôi muốn redirect"
Khi nào cần Escape?
Cách dùng
Ví dụ thực tế
2. Escape + Memory Mode — Vá lỗi lặp lại vĩnh viễn
Tình huống
Flow vá vĩnh viễn
Ví dụ
3. Double Escape — Rewind conversation
Khi nào cần?
Cách dùng
Ví dụ
Khi nào Esc Esc hữu ích nhất?
Lưu ý
4. /compact — Tóm tắt, giữ knowledge
Khi nào dùng?
Cách dùng
Ví dụ trước/sau
Khi nào là lúc chạy /compact?
Output compact mẫu
5. /clear — Xóa hết, khởi động lại
Khi nào dùng?
Cách dùng
Ví dụ khi nên clear
/compact vs /clear — So sánh
Decision tree
Ví dụ thực chiến: Full-day session với 4 task khác nhau
Tình huống
Flow với Claude Code
Kết quả
Case studies theo ngành
💼 Consultant multi-client — Context switching sạch
🏥 Health tech — /clear bắt buộc cho PHI
🛠️ Platform team — /compact để save cost
📣 Content marketer — Escape cho iterate nhanh
🔐 Security engineer — Esc Esc cho rollback thử nghiệm
Anti-patterns
❌ Không bao giờ /clear cả ngày
❌ /clear khi vẫn cần context
❌ Escape rồi quên redirect
❌ Spam Escape mỗi khi Claude đọc file
❌ Dùng Esc Esc như "undo file edit"
Mẹo nâng cao
Mẹo 1: Shortcut reference card
Mẹo 2: /compact custom instruction
Mẹo 3: Đặt "checkpoint" bằng commit
Mẹo 4: Context dashboard
Áp dụng ngay
4.8 - Điều khiển context — Escape, /compact, /clear​
Modified April 20
Bài 4.8: Điều khiển context — Escape, /compact, /clear​
Module: 3 — Quy trình cơ bản​
Thời gian ước tính: 25 phút (đọc) + 10 phút (thực hành)​
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
​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Dùng Escape để dừng Claude khi đi sai hướng, redirect cho đúng​
•
✅ Dùng Esc Esc (double escape) để rewind conversation về message trước​
•
✅ Phân biệt /compact (giữ context, tóm tắt) và /clear (xóa hết, bắt đầu mới)​
•
✅ Kết hợp Escape với memory mode (#) để vá lỗi lặp lại​
•
✅ Biết khi nào keep conversation, khi nào compact, khi nào clear​
​
​
Mở đầu: Tại sao conversation dài lại tệ?​
Hầu hết user mới nghĩ "càng nói chuyện nhiều với Claude càng thông minh hơn." Sai.​
Claude có context window 200,000 token — nghe nhiều, nhưng mỗi session dài nghĩa là:​
•
Chậm hơn — mỗi request Claude phải đọc lại toàn bộ history​
•
Đắt hơn — 50,000 token input × $3/1M × mỗi request = tăng dần​
•
Dễ lạc hơn — Claude "nhớ" cả lỗi cũ, quyết định đã rollback, context không liên quan​
•
Dễ hallucinate — khi prompt quá dài, model đôi khi miss instruction ở giữa​
Giải pháp: quản lý context trong session — biết khi nào giữ, khi nào compact, khi nào clear.​
Bài này dạy bạn 4 "reset tool": Escape, Esc Esc, /compact, /clear. Dùng tốt = khác biệt giữa Claude hoạt động mượt cả ngày vs Claude "nặng" dần mỗi giờ.​
​
​
1. Escape — "Dừng lại, tôi muốn redirect"​
Khi nào cần Escape?​
Đang trong một conversation, Claude đang chạy — bạn thấy:​
•
Claude đang Read đúng thứ sai (ví dụ: hỏi sửa file A, Claude đọc file B, C, D không liên quan)​
Comments (0)
Help Center
Keyboard Shortcuts
