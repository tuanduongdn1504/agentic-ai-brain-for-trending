# 2.2 Prompt Library & Demo Scripts

**Source:** https://transform.sg.larksuite.com/wiki/EO1twbprTiFmZGk9KdBlmsqMglh
**Wiki ID:** EO1twbprTiFmZGk9KdBlmsqMglh
**Archived:** 2026-05-07

---

Lark Docs
C
Claude Course 2026
Public access
Table of contents
Khoá học Claude toàn diện tiếng Việt
Lộ trình học tập.pdf
25 tập khám phá Claude AI
Lộ trình tự học 5 buổi × 2 tiếng
Buổi 1. Hiểu cỗ máy và khung tư duy 4D
Buổi 2. Prompting Mastery — Vòng lặp Description ↔ Discernment
Slide: Prompting Mastery.pdf
2.1 Giáo án giảng viên
2.2 Prompt Library & Demo Scripts
2.3 Handouts học viên
2.4 Workbook học viên
2.5 Demo Assets
2.6 Checklist chuẩn bị đầy đủ cho giảng viên
Buổi 3. Projects & Artifacts — Không gian làm việc chuyên dụng
Buổi 4. Skills & Research — Đóng gói quy trình + Đào sâu đa nguồn
Buổi 5. Cowork & Automation
🔥
Recap 5 buổi học Claude AI online
Anthropic courses
📣
Bổ sung course
Transform Group

2.2 Prompt Library & Demo Scripts

Last updated: Apr 20

Log In or Sign Up
2.2 Prompt Library & Demo Scripts
Demo 1: Email Makeover
🎯 Mục tiêu demo
⏱ Thời gian
🛠 Setup
📝 Prompt yếu (chạy trước)
📝 Prompt mạnh (chạy sau)
🎬 Kịch bản diễn đạt
Demo 2: Data Analysis Makeover
🎯 Mục tiêu demo
⏱ Thời gian
🛠 Setup
📝 Prompt yếu
📝 Prompt mạnh
🎬 Kịch bản diễn đạt
Demo 3: Creative Brief với Few-shot
🎯 Mục tiêu demo
⏱ Thời gian
🛠 Setup
📝 Prompt yếu
📝 Prompt mạnh (Few-shot)
🎬 Kịch bản diễn đạt
Meta-prompt Template
🎯 Mục tiêu
📝 Template chính
🎯 Variations cho tình huống khác nhau
D↔D Loop Example (cho giảng viên tham khảo)
Scenario
Round 1
Round 2
Round 3
Lesson
Fallback prompts cho học viên không có BTVN
Fallback 1: Weekly Report
Fallback 2: Meeting Recap
Fallback 3: Customer Reply
Fallback 4: Research Brief
Fallback 5: Content Repurpose
Fallback 6: Code Review
Fallback 7: Interview Question Prep
Backup plan nếu Claude lag / hit rate limit
Nếu chạy quá 3 prompts liên tiếp trong demo
Nếu cả 2 account hit limit
Prompt library dành riêng cho Vietnamese context
Template 1: Email formal Vietnamese
Template 2: Báo cáo tiếng Việt
Template 3: Content Vietnamese cho social
2.2 Prompt Library & Demo Scripts​
Modified April 20
​
Mục đích: Tất cả prompt + scripts demo cho Buổi 2. ​
Cách dùng: Giảng viên mở song song với slide deck, copy-paste ready.​
​
Demo 1: Email Makeover​
🎯 Mục tiêu demo​
Show 5/6 kỹ thuật áp dụng trên email task. Weak → Strong có weight khác biệt rõ.​
⏱ Thời gian​
5 phút​
🛠 Setup​
•
Claude.ai, new chat​
•
Web search có/không không quan trọng​
📝 Prompt yếu (chạy trước)​
​
Code block​
Plain Text
Copy
Viết email cho sếp báo project Phoenix chậm.​
​
Output dự đoán:​
•
180-220 từ​
•
Nhiều "I apologize", "I'm sorry to inform you"​
•
Generic, không có mitigation specific​
•
Không có subject line rõ​
•
Không có concrete ask​
📝 Prompt mạnh (chạy sau)​
​
Code block​
Plain Text
Copy
# ROLE​
Bạn là senior PM tại công ty SaaS 200 người.​
​
# CONTEXT​
- Project Phoenix (launch 15/5) chậm 2 tuần​
- Root cause: vendor Stripe migration API trễ deliver​
- Tôi đã có mitigation: (a) parallel workstream, ​
  (b) descope v1 từ 12 features → 9 features​
- Budget vẫn trong limit​
​
# AUDIENCE​
Sếp tôi là CTO — direct, thích numbers, ghét hình thức.​
Bạn ấy quan tâm: impact customer, cost, alternatives.​
​
# TASK​
Viết email 120-150 từ. ​
Subject: "Project Phoenix — 2-week delay + mitigation plan"​
​
Comments (0)
Help Center
Keyboard Shortcuts
