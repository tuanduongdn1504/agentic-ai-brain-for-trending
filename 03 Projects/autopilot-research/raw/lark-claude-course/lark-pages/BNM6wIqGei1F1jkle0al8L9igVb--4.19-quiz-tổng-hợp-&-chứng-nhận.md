# 4.19 - Quiz tổng hợp & Chứng nhận

**Source:** https://transform.sg.larksuite.com/wiki/BNM6wIqGei1F1jkle0al8L9igVb
**Wiki ID:** BNM6wIqGei1F1jkle0al8L9igVb
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

4.19 - Quiz tổng hợp & Chứng nhận

Last updated: Apr 20

Log In or Sign Up
4.19 - Quiz tổng hợp & Chứng nhận
Bài 4.19: Quiz tổng hợp & Chứng nhận
Giới thiệu
Phần 1: Nền tảng & khái niệm (Câu 1–5)
Câu 1: Khi bạn gõ "đọc file X" trong Claude Code, ai THỰC SỰ đọc file đó?
Câu 2: Pattern nào sau đây mô tả đúng cách agentic coding assistant hoạt động?
Câu 3: Claude Code không indexing toàn bộ codebase. Thay vào đó, nó dùng approach gì?
Câu 4: Mệnh đề nào SAI về tool use?
Câu 5: Lý do kiến trúc agentic search + tool use tốt cho enterprise về bảo mật?
Phần 2: Context management (Câu 6–10)
Câu 6: File CLAUDE.md được include vào request Claude khi nào?
Câu 7: Bạn vừa nhận ra Claude thường xuyên mắc cùng một lỗi cụ thể. Cách tốt nhất để "sửa vĩnh viễn" là gì?
Câu 8: Khác biệt chính giữa /compact và /clear là gì?
Câu 9: Khi nhấn Escape hai lần (Esc Esc), điều gì xảy ra?
Câu 10: File CLAUDE.local.md nên chứa gì?
Phần 3: Commands, MCP, GitHub (Câu 11–14)
Câu 11: Bạn muốn tạo custom command /audit cho project. Nên đặt file ở đâu?
Câu 12: Trong custom command, $ARGUMENTS đại diện cho gì?
Câu 13: MCP server Playwright cho phép Claude làm gì?
Câu 14: Trong GitHub Actions workflow Claude, điều gì bắt buộc phải khai báo explicit (không auto-allow như local)?
Phần 4: Hooks (Câu 15–18)
Câu 15: Hai loại hook cơ bản là gì?
Câu 16: Exit code nào BLOCK tool call trong PreToolUse hook?
Câu 17: Tại sao hook path phải là absolute path thay vì relative?
Câu 18: Pattern $PWD trong settings.example.json được dùng để làm gì?
Phần 5: SDK & tổng hợp (Câu 19–20)
Câu 19: SDK Claude Code khác CLI Claude Code ở điểm chính nào?
Câu 20: Claim nào sau đây đúng về cost control khi dùng SDK?
Đáp án & giải thích
Phần 1
Phần 2
Phần 3
Phần 4
Phần 5
Bản đồ câu sai → Bài cần ôn
Tính điểm
Tự đánh giá — Kỹ năng thực hành
Practical skill checklist
Chứng nhận hoàn thành
Bước tiếp theo sau khóa học này
Khóa học nâng cao đề xuất
Self-directed learning
Feedback vào khóa học
Lời kết
Bài tiếp theo
4.19 - Quiz tổng hợp & Chứng nhận​
Modified April 20
Bài 4.19: Quiz tổng hợp & Chứng nhận​
Module: 6 — Automation & Wrap-up​
Thời gian ước tính: 30 phút​
Mức độ: Tổng hợp toàn khóa​
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
Giới thiệu​
Quiz này gồm 20 câu hỏi bao phủ 18 bài nội dung chính. Mục tiêu không phải pass/fail — mà để:​
•
✅ Kiểm tra bạn đã nắm vững phần nào​
•
✅ Phát hiện concept cần ôn lại​
•
✅ Củng cố kiến thức trước khi thực chiến​
Cách làm:​
•
Đọc câu hỏi, suy nghĩ (đừng lướt xuống đáp án ngay)​
•
Chọn 1 đáp án bạn tin nhất​
•
Sau khi hoàn thành toàn bộ, check với đáp án ở cuối​
•
Câu nào sai → quay lại bài tương ứng, đọc kỹ phần liên quan​
Điểm chuẩn đề xuất:​
•
18–20: 🏆 Thành thạo — sẵn sàng dùng Claude Code production​
•
15–17: 🥈 Tốt — ôn thêm vài chủ đề​
•
11–14: 🥉 Khá — cần review 2–3 bài​
•
< 11: 🔄 Nên review từ Bài 4.6 trở đi​
​
​
Phần 1: Nền tảng & khái niệm (Câu 1–5)​
Câu 1: Khi bạn gõ "đọc file X" trong Claude Code, ai THỰC SỰ đọc file đó?​
A) Language model Claude ở server AnthropicB) Claude Code CLI trên máy bạnC) Cả hai — LM đọc trước, CLI verifyD) Tùy version Claude​
​
​
Câu 2: Pattern nào sau đây mô tả đúng cách agentic coding assistant hoạt động?​
A) Generate code → Format → DoneB) Gather context → Plan → Act (vòng lặp có thể)C) Predict next token → Stop khi user hài lòngD) Index codebase → Embed → Retrieve → Answer​
Comments (0)
Help Center
Keyboard Shortcuts
