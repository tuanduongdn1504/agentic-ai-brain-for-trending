# 2.9 - Skills — Dạy Claude một lần, dùng mãi mãi

**Source:** https://transform.sg.larksuite.com/wiki/DRDQwEUxciHQz8kw1aQlznp1gBc
**Wiki ID:** DRDQwEUxciHQz8kw1aQlznp1gBc
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

2.9 - Skills — Dạy Claude một lần, dùng mãi mãi

Last updated: Apr 20

Log In or Sign Up
2.9 - Skills — Dạy Claude một lần, dùng mãi mãi
Bài 2.9: Skills — Dạy Claude một lần, dùng mãi mãi
Mục tiêu học tập
Mở đầu: 50 lần nhắc cho 50 PR
Skill là gì?
Cơ chế auto-trigger
Anatomy của SKILL.md
Ví dụ thực tế: PR review skill
YAML frontmatter — phần quan trọng nhất
Body — instructions chi tiết
Bảng so sánh: Skill vs CLAUDE.md vs Slash Command vs Hook
Quy tắc quyết định nhanh
Storage locations — đặt skill ở đâu?
Personal skills: ~/.claude/skills/
Project skills: .claude/skills/
Bảng quyết định: personal vs project
Ví dụ thực chiến: Tạo skill code-explainer từ scratch
Bước 0: Identify pattern
Bước 1: Tạo folder
Bước 2: Viết frontmatter
Bước 3: Viết body — 5 sections thiết yếu
Bước 4: Test với 3 prompt variations
Bước 5: Iterate
Case studies theo role
Engineering team: skill release-notes
Designer ship code (Megan use case): skill design-handoff
DevOps: skill incident-postmortem
Mobile team: skill icon-export
Open source maintainer: skill triage-issue
Marketing/Content team: skill blog-seo-check
Khi nào tạo Skill? — Decision flowchart
Anti-patterns
Anti-pattern 1: Description quá generic
Anti-pattern 2: Description quá cứng nhắc
Anti-pattern 3: Nhồi mọi thứ vào 1 skill khổng lồ
Anti-pattern 4: Hardcode paths và usernames
Anti-pattern 5: Nhầm skill với hook
Anti-pattern 6: Personal skill trong project repo (hoặc ngược lại)
Anti-pattern 7: Không version skill khi tech stack thay đổi
Mẹo nâng cao
Mẹo 1: Test description với 5 variations trước khi deploy
Mẹo 2: Composable skills
Bước 2: Parse và format
Áp dụng ngay
Bài tập 1 (20 phút): Viết skill đầu tiên của bạn
Bài tập 2 (15 phút): Khám phá skills hiện có
Tóm tắt
Bài tiếp theo
Tài liệu tham khảo
2.9 - Skills — Dạy Claude một lần, dùng mãi mãi​
Modified April 20
Bài 2.9: Skills — Dạy Claude một lần, dùng mãi mãi​
Module: Hệ sinh thái mở rộng​
Thời gian ước tính: 30 phút​
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
✅ Giải thích Agent Skill là gì và cơ chế auto-trigger hoạt động như thế nào​
•
✅ Viết một SKILL.md đúng format với YAML frontmatter và body instructions​
•
✅ Quyết định đặt skill ở đâu: personal (~/.claude/skills/) hay project (.claude/skills/)​
•
✅ Phân biệt chính xác Skill vs CLAUDE.md vs slash command vs hook — cái nào dùng khi nào​
•
✅ Nhận ra pattern lặp lại trong workflow của mình và biến nó thành skill trong dưới 20 phút​
​
​
Mở đầu: 50 lần nhắc cho 50 PR​
Bạn là một senior backend engineer. Mỗi tháng bạn làm khoảng 50 PR — review, merge, hotfix, refactor, feature. Mỗi lần bạn mở Claude Code để chuẩn bị commit và push PR, bạn phải nhắc:​
"Format commit message theo Conventional Commits nhé — type(scope): subject. Nếu có breaking change thì thêm BREAKING CHANGE ở footer. Bao giờ cũng include ticket number từ Linear — format là [PROJ-XXX]. Và tag reviewer là @alice cho backend, @bob cho infra."​
Claude ghi nhớ — nhưng chỉ trong session đó. Session tiếp theo, bạn lại nhắc lại y chang. 50 PR/tháng = 50 lần copy-paste đoạn instructions đó. Tính ra một năm bạn đã mất gần 5 tiếng chỉ để nhắc Claude cùng một thứ.​
Tệ hơn: nếu có teammate mới join, bạn phải gửi đoạn instructions đó cho họ qua Slack, rồi họ lại phải nhớ copy-paste mỗi lần.​
Đây chính xác là vấn đề mà Agent Skills giải quyết.​
Bạn viết SKILL.md cho /commit-pr một lần. Claude tự đọc, tự hiểu, và mỗi khi bạn nói "chuẩn bị commit", "làm PR này", "viết commit message" — Claude tự apply toàn bộ quy tắc đó mà không cần bạn nhắc lại.​
"If you find yourself explaining the same thing to Claude repeatedly, that's a skill waiting to be written."​
50 PR/tháng → 0 lần nhắc. Skill viết một lần, dùng mãi mãi.​
​
​
Skill là gì?​
Comments (0)
Help Center
Keyboard Shortcuts
