# 1.8 - Connectors — Kết nối tools qua MCP

**Source:** https://transform.sg.larksuite.com/wiki/PdXDwHxDqiGCxekmmQelQj9TgSh
**Wiki ID:** PdXDwHxDqiGCxekmmQelQj9TgSh
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

1.8 - Connectors — Kết nối tools qua MCP

Last updated: Apr 20

Log In or Sign Up
1.8 - Connectors — Kết nối tools qua MCP
Bài 08: Connectors — Kết nối tools qua MCP
Mục tiêu học tập
Mở đầu: Khi bạn là "middleware" giữa Claude và tools
Connectors là gì?
Model Context Protocol (MCP) — "USB-C cho AI"
MCP là gì?
Tại sao điều này matter với bạn?
MCP là open standard
2 loại Connectors
1. Web Connectors
2. Desktop Extensions
Tìm và setup Connector
Connector Directory
Setup Web Connector — 5 bước
Bước 1: Find connector
Bước 2: Click Connect
Bước 3: Authenticate
Bước 4: Grant permissions
Bước 5: Test connection
Setup Desktop Extension — 4 bước
Bước 1: Download + install Claude Desktop app
Bước 2: Open app → Settings → Extensions
Bước 3: Browse available extensions → Install
Bước 4: Follow setup steps specific to extension
Dùng Connectors trong công việc
Practical use cases
Project Management (Asana, Linear, Jira)
Communication (Slack, Gmail)
Documentation (Notion, Google Drive, Confluence)
Business tools (Stripe, PayPal, Salesforce)
Ví dụ workflow: Release notes automation
Scenario
With Connectors (Linear + Google Drive)
Cross-tool workflows — Where connectors shine
Example 1: Meeting → Action items
Example 2: Customer ticket → Resolution
Example 3: Weekly intelligence brief
Ví dụ theo ngành
💼 Sales Manager
📣 Marketing Manager
💰 Finance Analyst
⚖️ Legal Counsel
🏥 Medical Writer
🎓 Curriculum Developer
📊 Data Analyst
🎧 Customer Support
Security và permissions — Important
1. Scoped access
2. Claude sees what you see
3. Revocable at any time
4. Custom connectors — Review code nếu untrusted
1.8 - Connectors — Kết nối tools qua MCP​
Modified April 20
Bài 08: Connectors — Kết nối tools qua MCP​
Module: Mở rộng phạm vi Claude​
Thời gian ước tính: 20 phút​
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
✅ Giải thích Connectors là gì và tại sao chúng matter cho công việc của bạn​
•
✅ Hiểu Model Context Protocol (MCP) — "USB-C cho AI"​
•
✅ Phân biệt Web connectors và Desktop extensions​
•
✅ Navigate connector directory và setup connection đầu tiên​
•
✅ Dùng connected tools hiệu quả trong chat​
•
✅ Hiểu security và permissions model​
Mở đầu: Khi bạn là "middleware" giữa Claude và tools​
Hãy điểm lại 24 giờ vừa qua. Bao nhiêu lần bạn làm điều này?​
•
Mở Slack, copy 1 message từ team, paste sang Claude để hỏi "tóm lại ý gì"​
•
Mở Gmail, copy email dài, paste sang Claude để reply​
•
Export CSV từ CRM, save local, upload vào Claude để analyze​
•
Take screenshot của Jira ticket, upload Claude để hỏi about context​
•
Download PDF từ Google Drive, upload Claude, rồi xóa local copy​
Mỗi hành động: 5-30 giây. Làm 20-30 lần/ngày = 10-15 phút "chuyển nhiên liệu" giữa tools và AI.​
Bạn đang làm middleware — người mang data qua lại. Cái giá: thời gian trực tiếp. Cái giá ẩn: cognitive load — bạn phải nhớ pull data gì, lúc nào, từ đâu.​
Và không chỉ data vào Claude. Khi Claude generate output — bạn cũng phải mang ra: copy response → paste vào Word, save Excel download → upload Google Drive, copy meeting notes → paste Slack.​
Connectors cắt đứt middleware layer này. Bạn connect Claude với tools bạn đã dùng → Claude access trực tiếp. Đọc mà không cần bạn paste. Write mà không cần bạn copy. Performance actions — update CRM, send Slack message, create Jira ticket — trực tiếp.​
Comments (0)
Help Center
Keyboard Shortcuts
