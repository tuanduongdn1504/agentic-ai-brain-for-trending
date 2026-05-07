# 4.7 - Thực hiện thay đổi — Screenshots, Planning Mode, Thinking Mode

**Source:** https://transform.sg.larksuite.com/wiki/JaFZwysM0i8L3LkPWnll9eVagWe
**Wiki ID:** JaFZwysM0i8L3LkPWnll9eVagWe
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

4.7 - Thực hiện thay đổi — Screenshots, Planning Mode, Thinking Mode

Last updated: Apr 20

Log In or Sign Up
4.7 - Thực hiện thay đổi — Screenshots, Planning Mode, Thinking Mode
Bài 4.7: Thực hiện thay đổi — Screenshots, Planning Mode, Thinking Mode
Mục tiêu học tập
Mở đầu: Câu chuyện 2 lần fail của dev
Lần 1: "Fix cái button kia cho đẹp hơn"
Lần 2: "Migrate toàn bộ fetch calls sang TanStack Query"
Bài học
1. Screenshots — Giao tiếp bằng hình
Cách dán screenshot
Flow thực tế
Khi nào nên dùng screenshot?
Ví dụ prompt dùng screenshot
Mẹo dùng screenshot tốt
2. Planning Mode — "Show me the plan first"
Planning Mode là gì?
Cách bật
Trong Planning Mode, Claude sẽ:
Khi nào BẮT BUỘC dùng Planning Mode?
Khi nào KHÔNG cần?
Ví dụ output Planning Mode
Chi phí
3. Thinking Mode — "Think longer before you speak"
Thinking Mode là gì?
5 cấp độ thinking
Cách dùng
Khi nào dùng?
Dấu hiệu Claude đang "thinking"
Thinking giữa tool call (Claude 4+)
Planning Mode vs Thinking Mode — Khác biệt cốt lõi
Combine cả hai
Ví dụ thực chiến: Dùng 3 kỹ thuật cùng task
Task
Bước 1: Screenshot + mô tả (visual context)
Bước 2: Planning Mode (vì đụng nhiều file)
Bước 3: Thinking Mode (decision: move pricing data?)
Kết quả
Case studies theo ngành
💼 Product Designer (code-friendly) — Screenshot-driven design
🛠️ Backend engineer — Planning Mode cho migration
🎮 Game dev — Thinking Mode cho optimization
🏥 Health tech — Thinking cho compliance logic
📣 Marketing engineer — Combine Screenshots + Planning
Anti-patterns
❌ Dùng Planning Mode cho task siêu nhỏ
❌ Dùng ultrathink cho task trivial
❌ Paste screenshot nhưng không mô tả
❌ Approve Planning Mode plan mà không đọc kỹ
❌ Thinking Mode mà prompt không đủ context
Mẹo nâng cao
Mẹo 1: Shortcut kết hợp
Mẹo 2: Prompt "show plan only"
Mẹo 3: Combine visual + verbal cho precision
4.7 - Thực hiện thay đổi — Screenshots, Planning Mode, Thinking Mode​
Modified April 20
Bài 4.7: Thực hiện thay đổi — Screenshots, Planning Mode, Thinking Mode​
Module: 3 — Quy trình cơ bản​
Thời gian ước tính: 30 phút (đọc) + 20 phút (thực hành)​
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
✅ Dùng screenshot (Ctrl+V) để chỉ rõ phần UI cần thay đổi​
•
✅ Bật Planning Mode cho task phức tạp và đọc/verify plan trước khi execute​
•
✅ Dùng Thinking Mode với 5 cấp độ (think → ultrathink) cho task logic khó​
•
✅ Phân biệt khi nào Planning, khi nào Thinking, khi nào cả hai​
•
✅ Ước tính chi phí token và tốc độ cho mỗi mode​
Mở đầu: Câu chuyện 2 lần fail của dev​
Lần 1: "Fix cái button kia cho đẹp hơn"​
Dev gõ:​
​
Code block​
Plain Text
Copy
Làm button 'Subscribe' ở dashboard đẹp hơn. ​
Hiện tại nhìn rời rạc quá.​
​
​
Claude đoán "button đẹp hơn" = đổi màu gradient tím-xanh (generic AI taste). Thay đổi 3 file. Dev xem → "không, mình muốn flat design, màu xanh flat như screenshot Stripe."​
Rollback 3 file. Gõ lại prompt. Claude đoán khác. Rollback tiếp. Lần thứ 4 mới đúng.​
Mất: 15 phút + 3x tiền token.​
Lần 2: "Migrate toàn bộ fetch calls sang TanStack Query"​
Comments (0)
Help Center
Keyboard Shortcuts
