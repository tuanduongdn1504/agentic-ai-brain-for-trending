# 4.0 - Claude Code in Action — Tổng quan khóa học

**Source:** https://transform.sg.larksuite.com/wiki/KyT3wQtdBiG9kJkwZ0Xl7So7gUb
**Wiki ID:** KyT3wQtdBiG9kJkwZ0Xl7So7gUb
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

4.0 - Claude Code in Action — Tổng quan khóa học

Last updated: Apr 20

Log In or Sign Up
4.0 - Claude Code in Action — Tổng quan khóa học
Claude Code in Action — Tổng quan khóa học
Tại sao bạn nên học khóa này?
Bạn sẽ học được gì?
Về tư duy
Về kỹ năng
Về thực hành
Lộ trình 20 bài
Cách học tập hiệu quả nhất
Quy tắc 70/20/10 áp dụng cho khóa này
3 nhóm học viên — 3 cách tiếp cận
Những gì bạn cần chuẩn bị
Bắt buộc
Nên có
Không cần
Triết lý xuyên suốt khóa học
1. "Context là vua — quản lý context là kỹ năng cao nhất"
2. "Verify, don't trust"
3. "Prompt là code, CLAUDE.md là config"
4. "Tự động hóa điểm đau, không phải toàn bộ"
Một lời khuyên từ kinh nghiệm thực tế
Sai lầm 1: Học lý thuyết xong mới thực hành
Sai lầm 2: Copy prompt mà không hiểu
Sai lầm 3: Chỉ dùng Claude Code cho task nhỏ
Sai lầm 4: Bỏ qua /init
Sai lầm 5: Không share với team
Bạn sẵn sàng chưa?
Các tài liệu chính thức
Bắt đầu nào
Phản hồi và hỗ trợ
4.0 - Claude Code in Action — Tổng quan khóa học​
Modified April 20
Claude Code in Action — Tổng quan khóa học​
Khóa học: Claude Code in Action — bản tiếng Việt chuyên sâu​
Phiên bản: 2.0 (tinh chế từ original Anthropic Academy + transcripts + best practices)​
Đối tượng: Developer, tech lead, engineering manager đang muốn làm chủ agentic coding workflow​
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
Tại sao bạn nên học khóa này?​
Hãy thành thật một chút. Mỗi tuần bạn dành bao nhiêu giờ cho những việc sau?​
•
Viết boilerplate code (CRUD, validator, test scaffolding) cho feature mới​
•
Tìm file trong codebase 50k+ dòng mà bạn chưa thuộc lòng​
•
Migrate 40+ call site khi đổi function signature​
•
Review PR với 80% là nitpicks (naming, format, convention)​
•
Fix CI fail vì quên update docs / changelog / typecheck​
•
Onboard dev mới trong 1-2 tuần chỉ để họ "biết file nào ở đâu"​
Nếu bạn dành hơn 10 giờ mỗi tuần cho những việc trên, bạn đang ở đúng chỗ.​
Khóa học này dạy bạn dùng Claude Code — agentic coding assistant của Anthropic — để dịch chuyển workflow:​
•
Từ "bạn làm + AI gợi ý" (Copilot style) → "AI làm + bạn duyệt" (agent style)​
•
Từ "rule dựa vào hy vọng dev nhớ" → "rule enforce deterministic qua hooks"​
•
Từ "mỗi dev dùng AI kiểu riêng" → "team workflow đồng nhất qua CLAUDE.md + commands share"​
Kết quả điển hình sau 90 ngày apply: 10-15 giờ/tuần/dev được giải phóng, PR quality đồng nhất, onboarding 2-5x nhanh.​
Bạn sẽ học được gì?​
Sau khi hoàn thành khóa học này, bạn sẽ có thể:​
Về tư duy​
•
Giải thích vì sao LM cần tool use, và agentic search vs indexing khác nhau thế nào​
•
Phân biệt task Claude làm tốt (có clear context) vs task dễ fail (ambiguous, huge scope)​
•
Design workflow với mindset "AI teammate" thay vì "AI autocomplete"​
Comments (0)
Help Center
Keyboard Shortcuts
