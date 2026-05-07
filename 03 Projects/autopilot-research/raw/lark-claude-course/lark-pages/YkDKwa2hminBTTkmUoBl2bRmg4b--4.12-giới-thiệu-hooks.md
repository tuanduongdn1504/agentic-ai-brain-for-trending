# 4.12 - Giới thiệu hooks

**Source:** https://transform.sg.larksuite.com/wiki/YkDKwa2hminBTTkmUoBl2bRmg4b
**Wiki ID:** YkDKwa2hminBTTkmUoBl2bRmg4b
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

4.12 - Giới thiệu hooks

Last updated: Apr 20

Log In or Sign Up
4.12 - Giới thiệu hooks
Bài 4.12: Giới thiệu hooks
Mục tiêu học tập
Mở đầu: "Claude tôi không chịu format file!"
Hook là gì?
Luồng bình thường (không hook)
Luồng có hook
Hai loại hook căn bản
PreToolUse — Chặn trước
PostToolUse — Phản ứng sau
Vị trí cấu hình hook
Khi nào dùng từng vị trí?
Structure của hook config
Shape tổng quát
Giải thích từng field
Ví dụ cấu hình 1: PreToolUse
Ví dụ cấu hình 2: PostToolUse
Dữ liệu hook nhận (stdin)
Ví dụ JSON cho PreToolUse trên Read tool
6 ứng dụng thực tế của hooks
1. Code formatting tự động
2. Type checking + feedback
3. Access control
4. Running tests on file changes
5. Linting / convention enforcement
6. Logging / audit
Ví dụ thực chiến: Team setup hook đầu tiên
Tình huống
Setup
Kết quả
Case studies theo ngành
🏥 Health tech — Enforce HIPAA boundary
💰 Fintech — Audit log bắt buộc
🎓 EdTech — Student code safety
📣 Content team — Style guide enforce
🛠️ Platform — Cost control
Anti-patterns
❌ Hook làm task chậm (>30s)
❌ Hook lỗi silent
❌ Hook cần network call mỗi lần
❌ Hook chặn false positive
❌ Không test hook
Mẹo nâng cao
Mẹo 1: Debug hook bằng log-only hook
Mẹo 2: Chia hook theo loại tool
Mẹo 3: Hook trong Docker (isolation)
Mẹo 4: Giới hạn hook bằng /hooks
Áp dụng ngay
Bài tập 1: Tạo hook log-only (15 phút)
Bài tập 2 (optional, 15 phút): Lên danh sách hook team cần
Tóm tắt bài học
Bài tiếp theo
4.12 - Giới thiệu hooks​
Modified April 20
Bài 4.12: Giới thiệu hooks​
Module: 5 — Hooks: biến Claude thành teammate​
Thời gian ước tính: 25 phút​
Mức độ: Trung cấp → Nâng cao​
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
✅ Giải thích hook là gì và nó chèn vào luồng Claude Code ở đâu​
•
✅ Phân biệt PreToolUse và PostToolUse hook, và khi nào dùng mỗi loại​
•
✅ Nhận ra 3 vị trí lưu cấu hình hook (global / project shared / project local)​
•
✅ Đọc hiểu structure JSON của một hook configuration​
•
✅ Nhận diện 6 ứng dụng thực tế của hooks cho team​
Mở đầu: "Claude tôi không chịu format file!"​
Bạn và team thống nhất: mọi TS file phải format Prettier trước commit. Bạn viết trong CLAUDE.md:​
​
Code block​
Markdown
Copy
Always run Prettier after editing TypeScript files.​
​
​
Claude tuân... đôi khi. Quên 30% số lần. Bạn phải remind sau từng PR.​
Vấn đề gốc: Claude là LLM, không deterministic. Dù viết rule rõ, vẫn skip.​
Giải pháp: đừng dựa vào Claude tự nhớ. Làm action đó thành cấu hình máy bắt buộc — mỗi lần Claude Edit xong TS file, hệ thống tự chạy Prettier. Không hỏi Claude, không cần nhắc.​
Đó là hooks.​
Hook là gì?​
Hook = command shell bạn định nghĩa, chạy tự động trước hoặc sau khi Claude gọi tool.​
Không phải code Claude viết. Không phải prompt. Là hệ thống chạy.​
Comments (0)
Help Center
Keyboard Shortcuts
