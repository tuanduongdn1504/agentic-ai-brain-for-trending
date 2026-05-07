# 4.2 - Coding assistant là gì?

**Source:** https://transform.sg.larksuite.com/wiki/UCMlwntKFi7dJHkm4RflH1WmgZf
**Wiki ID:** UCMlwntKFi7dJHkm4RflH1WmgZf
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

4.2 - Coding assistant là gì?

Last updated: Apr 20

Log In or Sign Up
4.2 - Coding assistant là gì?
Bài 4.2: Coding assistant là gì?
Mục tiêu học tập
Mở đầu: Câu hỏi đơn giản mà phần lớn người trả lời sai
Coding assistant hoạt động thế nào?
1. Gather context — Thu thập ngữ cảnh
2. Formulate a plan — Lập kế hoạch
3. Take action — Thực hiện
Vấn đề: LM chỉ sinh text
Thí nghiệm nhỏ
Tool use — Mắt, tai, tay cho LM
Luồng hoạt động chi tiết
5 bước của một tool use loop
So sánh với developer người
Tool use challenge — Không phải LM nào cũng giỏi
Các cách LM có thể "dở" về tool use
Tại sao Claude (Opus, Sonnet, Haiku) mạnh ở tool use?
Lợi ích của tool use mạnh đối với Claude Code
1. Giải quyết task khó hơn
2. Platform có thể mở rộng
3. Bảo mật tốt hơn
Ví dụ thực chiến: Chứng kiến tool use loop
Tình huống
Bước 1: Bạn gõ
Bước 2: Claude gather context (tool use — Grep)
Bước 3: Claude đọc các file (tool use — Read)
Bước 4: Claude lập kế hoạch (text only, không tool)
Bước 5: Claude thực thi (tool use — Edit + Bash)
Bước 6: Claude loop back (context mới = error)
Kết quả
Case studies: tool use power theo ngành
💼 Developer Productivity — Team frontend
🏭 Platform Engineering — Database migration
🔍 Code Archaeology — Onboard codebase 1M dòng
🛡️ Security Review — Audit dependency
Anti-patterns khi tin vào tool use
❌ Giả sử Claude "biết" những gì không cung cấp
❌ Confused khi Claude "lơ" tool có sẵn
❌ Không biết tool nào có sẵn
❌ Dùng chat web (claude.ai) cho task cần tool file system
Mẹo nâng cao
Mẹo 1: Hỏi Claude list tool khi nghi ngờ
Mẹo 2: Verify tool call bằng cách quan sát
Mẹo 3: Khi debug, xem transcript
Áp dụng ngay
Bài tập 1: Quan sát tool use loop (10 phút)
Bài tập 2 (optional, 15 phút): Phân biệt chat vs Claude Code
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
4.2 - Coding assistant là gì?​
Modified April 20
Bài 4.2: Coding assistant là gì?​
Module: 1 — Nền tảng​
Thời gian ước tính: 25 phút (đọc) + 10 phút (thử demo)​
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
✅ Mô tả quy trình 3 bước mà một coding assistant thực hiện khi nhận task​
•
✅ Giải thích vì sao language model một mình không đọc được file hay chạy được command​
•
✅ Mô tả cơ chế tool use — cách LM "gọi" action ra thế giới thực​
•
✅ So sánh khả năng tool use của Claude với các model khác, và hiểu vì sao điều đó quan trọng​
•
✅ Dự đoán khi nào Claude Code "bí" và cần bạn can thiệp​
Mở đầu: Câu hỏi đơn giản mà phần lớn người trả lời sai​
Hỏi 10 developer dùng AI coding tool: "Khi bạn ra lệnh 'đọc file X', ai thực sự đọc file đó?"​
Phần lớn trả lời: "Model đọc."​
Câu trả lời đúng: Không. Model không bao giờ tự đọc file.​
Hiểu nhầm này là lý do tại sao:​
•
Bạn confused khi Claude trả lời "tôi không có truy cập internet" đôi lúc nhưng lại search được lúc khác​
•
Bạn không biết tại sao "câu lệnh" trong Claude Code đôi khi tương tác với file system, đôi khi không​
•
Bạn không biết khi nào Claude có thể đi sai, khi nào không​
Bài này vá lỗ hổng đó. Hiểu rồi, bạn sẽ dùng Claude Code như senior — không phải như user tin mù.​
Coding assistant hoạt động thế nào?​
Một coding assistant nhận task — ví dụ "sửa bug dựa trên error message này" — và làm ba việc, giống hệt cách một developer người làm:​
​
Code block​
Plain Text
Copy
┌──────────────────────────────────────────────────────────┐​
​
Comments (0)
Help Center
Keyboard Shortcuts
