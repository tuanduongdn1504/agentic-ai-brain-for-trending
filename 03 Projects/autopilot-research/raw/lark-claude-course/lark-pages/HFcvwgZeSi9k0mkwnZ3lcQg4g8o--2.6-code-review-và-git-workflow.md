# 2.6 - Code Review và Git Workflow

**Source:** https://transform.sg.larksuite.com/wiki/HFcvwgZeSi9k0mkwnZ3lcQg4g8o
**Wiki ID:** HFcvwgZeSi9k0mkwnZ3lcQg4g8o
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

2.6 - Code Review và Git Workflow

Last updated: Apr 20

Log In or Sign Up
2.6 - Code Review và Git Workflow
Bài 2.6: Code Review và Git Workflow
Mục tiêu học tập
Mở đầu: Khi bottleneck review làm chậm cả team
Subagent Code Reviewer
Tại sao cần subagent riêng cho review?
Tạo subagent reviewer qua /agents
Check subagent vào repo
Gọi reviewer trước khi push
Bảng so sánh: Subagent Reviewer vs Human Reviewer vs Lint/CI
Skill /commit-push-pr
Vấn đề với workflow thủ công
/commit-push-pr làm gì
Tích hợp Slack tự động
So sánh thực tế
Session linking với --from-pr
Vấn đề: Mất context khi quay lại PR cũ
--from-pr giải quyết thế nào
Use cases thực tế
GitHub Actions Integration
Setup với /install github-action
Cách @Claude hoạt động trong PR comments
Scope capability của GitHub Actions Claude
Live demo: Quiz App từ GitHub Issues
Ví dụ thực chiến: Full code review workflow trên team 5 engineers
Setup ban đầu (một lần)
Workflow hàng ngày
Case studies theo role
Indie hacker (1 người)
Engineering team (5+ người)
Open source maintainer
Designer ship code
DevOps / Platform team
Anti-patterns
Anti-pattern 1: Subagent reviewer có write tools
Anti-pattern 2: Skip human review hoàn toàn
Anti-pattern 3: Không check .claude/agents/ vào repo
Anti-pattern 4: Auto-merge PR sau Claude review
Anti-pattern 5: Tag @claude cho task không phải code
Mẹo nâng cao
Mẹo 1: Custom reviewer prompt theo team priorities
Mẹo 2: Hook PostToolUse chạy ESLint trước commit
Mẹo 3: Multiple specialized reviewers chạy parallel
Mẹo 4: --from-pr resume khi CI fail sau vài ngày
Mẹo 5: Combine /commit-push-pr với reviewer
Áp dụng ngay
Bài tập 1: Tạo subagent code reviewer (15 phút)
Bài tập 2: Setup GitHub Actions (20 phút)
Tóm tắt
Bài tiếp theo
Tài liệu tham khảo
2.6 - Code Review và Git Workflow​
Modified April 20
Bài 2.6: Code Review và Git Workflow​
Module: Workflow chuyên nghiệp​
Thời gian ước tính: 25 phút​
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
✅ Tạo subagent code reviewer dùng chung toàn team, check vào repo để nhất quán​
•
✅ Dùng skill /commit-push-pr để commit, push và tạo PR trong một bước duy nhất​
•
✅ Link các session với --from-pr để tiếp tục công việc đúng điểm đã dừng​
•
✅ Setup GitHub Actions integration và dùng tag @Claude trong PR comments để Claude tự fix​
•
✅ Biết khi nào nên — và không nên — dùng @Claude để tránh over-delegation​
​
​
Mở đầu: Khi bottleneck review làm chậm cả team​
Hãy tưởng tượng một team 5 engineers ở một AI startup. Họ build nhanh — mỗi ngày đẩy 3-5 PR. Nhưng có một vấn đề: chỉ có hai engineer senior có thể review code đúng nghĩa. Và cả hai đều đang bận với feature của mình.​
Kết quả? Mỗi PR trung bình chờ 2-3 ngày trước khi được review lần đầu. Sau khi nhận feedback, engineer phải fix rồi chờ thêm 1-2 ngày review lần hai. Tổng thời gian từ push branch đến merge: 5-7 ngày cho một feature không phức tạp.​
Team bắt đầu chọn cách dễ hơn: merge PR mà không review kỹ. Kỹ thuật nợ tích lũy. Bug lọt vào production.​
Sau khi adopt subagent code reviewer cùng với GitHub Actions integration, bức tranh thay đổi hoàn toàn. Engineer push branch → subagent reviewer chạy ngay trên CI, comment lên PR trong vòng 3 phút — kiểm tra logic, security, style consistency. Engineer fix ngay trong cùng session. Human reviewer chỉ cần approve architectural decisions.​
Time-to-merge giảm từ 5-7 ngày xuống còn 4-6 giờ.​
Và khi cần fix PR theo comment của reviewer? Không còn phải "nhớ lại" mình đang làm đến đâu. Chỉ cần:​
​
Code block​
Plain Text
Copy
claude --from-pr 247​
​
​
Comments (0)
Help Center
Keyboard Shortcuts
