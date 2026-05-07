# 2.4 - Workflow Explore → Plan → Code → Commit

**Source:** https://transform.sg.larksuite.com/wiki/ZYC8wt1h3iJOcZk1CoWlZHcrgKe
**Wiki ID:** ZYC8wt1h3iJOcZk1CoWlZHcrgKe
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

2.4 - Workflow Explore → Plan → Code → Commit

Last updated: Apr 20

Log In or Sign Up
2.4 - Workflow Explore → Plan → Code → Commit
Bài 2.4: Workflow Explore → Plan → Code → Commit
Mục tiêu học tập
Mở đầu: Hai dev, cùng task, kết quả ngược nhau
EPCC: Bức tranh toàn cảnh
Phase 1: EXPLORE — Đừng để Claude đoán
Tại sao phase này tồn tại
Hai cách Explore
Explore nên tìm ra điều gì
Anti-pattern: Skip Explore
Phase 2: PLAN — Nơi rẻ nhất để course-correct
Tại sao Plan quan trọng hơn Code
Cách vào Plan Mode
Cách viết prompt tốt cho Plan phase
Claude trả plan — bạn làm gì?
Bảng: Plan tốt vs Plan kém
Lặp lại Plan nếu cần
Phase 3: CODE — Execute có kiểm soát
Sau khi approve plan
3 yếu tố làm Code phase mượt
Xử lý khi Claude bị kẹt lặp lại
Multi-Claude: Chạy song song cho task lớn
Async Accept mode
Phase 4: COMMIT — Gate trước khi push
Tại sao cần phase riêng cho Commit
Subagent code reviewer
Claude generate commit message
GitHub Actions integration
Khi nào skip phase nào?
Ví dụ thực chiến đầy đủ: "Add WebP conversion to image pipeline"
Setup
Phase 1: EXPLORE (5-7 phút)
Phase 2: PLAN (8-10 phút)
Phase 3: CODE (15-20 phút)
Phase 4: COMMIT (3-5 phút)
Case studies theo role
Backend Engineer: Refactor service architecture
Frontend Engineer: Ship UI feature mới
Open source maintainer: Review và merge contributor PRs
Anthropic team: 22.000-line RL code change
Solo founder (vibe-coding): Ship nhanh, iterate
Anti-patterns: Những cái bẫy phổ biến
Anti-pattern 1: Skip Plan để "save time"
Anti-pattern 2: Analysis paralysis — Plan mãi, không Code
Anti-pattern 3: Code không có test suite
Anti-pattern 4: Commit không review
Anti-pattern 5: Full EPCC cho tiny task
Mẹo nâng cao
Mẹo 1: /rewind — rollback khi đi sai hướng
Mẹo 2: /compact giữa các phases
Mẹo 3: Plan-as-document
Mẹo 4: Test-driven prompt
2.4 - Workflow Explore → Plan → Code → Commit​
Modified April 20
Bài 2.4: Workflow Explore → Plan → Code → Commit​
Module: Workflow chuyên nghiệp​
Thời gian ước tính: 35 phút​
Mức độ: Trung cấp​
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
✅ Nắm vững 4 phases của workflow EPCC (Explore, Plan, Code, Commit) và mục đích riêng của từng phase​
•
✅ Biết khi nào nên skip phase nào và khi nào cần lặp lại nhiều vòng​
•
✅ Dùng Plan Mode đúng cách để align với Claude trước khi code, tránh course-correct tốn kém​
•
✅ Setup test suite và tools phù hợp để Code phase chạy mượt, ít back-and-forth​
•
✅ Tạo subagent code reviewer cho Commit phase để có "fresh pair of eyes" trước khi push​
​
​
Mở đầu: Hai dev, cùng task, kết quả ngược nhau​
Hãy tưởng tượng hai backend engineer — Minh và An — nhận cùng một ticket vào sáng thứ Hai:​
"Add WebP conversion to the image upload pipeline."​
Minh (làm việc theo cách cũ): Mở Claude Code, prompt thẳng:​
"Add WebP conversion to our image upload pipeline."​
Claude bắt đầu viết code. Nó tìm một file tên upload.ts, thêm thư viện sharp, viết converter. Trông có vẻ ổn. Minh approve, Claude tiếp tục. 20 phút sau, build error vì project thực ra dùng jimp không phải sharp. Fix xong, lại có lỗi khác — hoá ra pipeline upload không phải ở upload.ts mà ở một middleware chain phức tạp hơn nhiều. Claude đã đoán sai entry point. Sửa tiếp. Test fail. Debug. 2 tiếng sau, Minh vẫn đang loay hoay với một đống code chắp vá.​
An (dùng EPCC workflow): Shift+Tab vào Plan Mode, prompt:​
"I need to add WebP conversion to our image upload pipeline. Figure out where in the pipeline it should happen, whether we need new dependencies, and how to approach it."​
Claude đọc file, khám phá codebase, tìm ra: pipeline upload nằm ở middleware/storage.ts và project đã có jimp rồi — không cần thêm dependency. 5 phút sau, Claude trả ra plan chi tiết. An đọc, thấy hợp lý, comment thêm một yêu cầu về xử lý animated GIF, Claude revise plan. An approve. Claude execute từng bước theo plan, chạy test suite, commit gọn. Tổng thời gian: 25 phút.​
Comments (0)
Help Center
Keyboard Shortcuts
