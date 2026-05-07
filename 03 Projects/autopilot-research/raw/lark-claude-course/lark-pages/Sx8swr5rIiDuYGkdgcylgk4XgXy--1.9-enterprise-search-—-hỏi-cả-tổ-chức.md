# 1.9 - Enterprise Search — Hỏi cả tổ chức

**Source:** https://transform.sg.larksuite.com/wiki/Sx8swr5rIiDuYGkdgcylgk4XgXy
**Wiki ID:** Sx8swr5rIiDuYGkdgcylgk4XgXy
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
Slide: Claude 101.pdf
1.0 - Claude 101 — Tổng quan khóa học
1.1 - Claude là gì?
1.2 - Cuộc trò chuyện đầu tiên với Claude
1.3 - Tối ưu kết quả — AI Fluency & Iteration
1.4 - Claude Desktop — Chat, Cowork, Code
1.5 - Projects — Không gian làm việc chuyên dụng
1.6 - Artifacts — Sáng tạo tương tác
1.7 - Skills — Đóng gói quy trình
1.8 - Connectors — Kết nối tools qua MCP
1.9 - Enterprise Search — Hỏi cả tổ chức
1.10 - Research mode — Đào sâu đa nguồn
1.11 - Claude theo vai trò — Use cases by role
1.12 - Các cách khác làm việc với Claude
1.13 - Tổng kết và bước tiếp theo
1.14 - Quiz tổng hợp & Chứng nhận
02 - Claude Code 101
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

1.9 - Enterprise Search — Hỏi cả tổ chức

Last updated: Apr 20

Log In or Sign Up
1.9 - Enterprise Search — Hỏi cả tổ chức
Bài 09: Enterprise Search — Hỏi cả tổ chức
Mục tiêu học tập
Mở đầu: Khi bạn cần trí nhớ của cả tổ chức
Enterprise Search là gì?
Khác gì so với regular chat + connectors?
Loại câu hỏi nào Enterprise Search shine?
5 use case categories
1. Catching up (ramping after time away)
2. Policy & process questions
3. Research & analysis
4. Onboarding new team members
5. Performance & project tracking
Cách Enterprise Search work
Setup — 2-step process
Bước 1: Admin setup (Owners)
Admin process:
Bước 2: User authentication
User process:
Các câu hỏi hiệu quả — 4 patterns
Pattern 1: Time-bounded queries
Pattern 2: Source hints
Pattern 3: Specific entities
Pattern 4: Synthesis requests
Ví dụ workflow
Scenario: New PM joining team
Query 1: Team landscape
Query 2: Ongoing initiatives
Query 3: Recent decisions
Query 4: Stakeholders
Query 5: Current blockers
Ví dụ theo ngành
💼 Sales leadership
📣 Marketing leadership
💰 Finance / Ops
⚖️ Legal / Compliance
🛠️ Product / Engineering
🎧 Customer Success
👥 People Ops / HR
Security và privacy — "An toàn không?"
Principles
1. You see only what you can already see
2. Conversations remain private
3. Data không indexed or stored separately
4. Org-level controls
Compliance posture
Anti-patterns với Enterprise Search
❌ Treat nó như Google-for-org
❌ Không cite check
❌ Over-share sensitive queries
❌ Expect outdated info to be current
❌ Không iterate
1.9 - Enterprise Search — Hỏi cả tổ chức​
Modified April 20
Bài 09: Enterprise Search — Hỏi cả tổ chức​
Module: Mở rộng phạm vi Claude​
Thời gian ước tính: 15 phút​
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
Slide: Claude 101.pdf​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Giải thích Enterprise Search là gì và các loại câu hỏi nó trả lời​
•
✅ Hiểu quy trình setup 2 bước — admin trước, users sau​
•
✅ Nhận diện khi nào dùng Enterprise Search vs. regular chat với connectors​
•
✅ Setup Enterprise Search từ user's perspective​
•
✅ Hiểu security & permissions model bảo vệ organizational data​
Mở đầu: Khi bạn cần trí nhớ của cả tổ chức​
Tình huống quen thuộc: Thứ 2 đi làm lại sau 3 ngày nghỉ.​
Bạn mở laptop, 200 emails, 15 Slack unread channels, 4 Notion notifications, 8 Jira tickets cần review. Nhìn vào cái đống đó 30 giây, bạn đã muốn rút lui trở lại nhà.​
Câu hỏi thật trong đầu bạn:​
•
"Gì đã xảy ra khi tôi đi vắng?"​
•
"Có quyết định nào được chốt mà tôi cần cập nhật?"​
•
"Có blocker nào trên Platform project không?"​
•
"Có ai ping tôi cần response không?"​
Mỗi câu cần lục ít nhất 3 tools để trả lời. Slack (messages), Gmail (decisions/announces), Jira (tickets), Notion (docs), Google Drive (shared files).​
Gửi ai trong team hỏi? "Hey, có gì mới không?" — họ bận hoặc chỉ biết góc của họ.​
Bạn dành 1.5 tiếng chỉ để "ramp up" trước khi có thể làm việc thật.​
Tuần sau lặp lại. Nhân viên mới vào team: cũng lặp lại. Nhân viên chuyển department: 2-3 tháng trước khi "biết tổ chức work how".​
Knowledge của tổ chức nằm khắp nơi — không ai own toàn bộ. Và không một ai đủ kiên nhẫn đi lục hết mỗi lần cần.​
Comments (0)
Help Center
Keyboard Shortcuts
