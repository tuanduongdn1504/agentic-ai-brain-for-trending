# 1.3 - Tối ưu kết quả — AI Fluency & Iteration

**Source:** https://transform.sg.larksuite.com/wiki/Ikefw0RWdiZgYfkxO1ulBlQygqI
**Wiki ID:** Ikefw0RWdiZgYfkxO1ulBlQygqI
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

1.3 - Tối ưu kết quả — AI Fluency & Iteration

Last updated: Apr 20

Log In or Sign Up
1.3 - Tối ưu kết quả — AI Fluency & Iteration
Bài 03: Tối ưu kết quả — AI Fluency & Iteration
Mục tiêu học tập
Mở đầu: Tại sao response không đúng ý?
5 common challenges và cách fix
Ví dụ fix: từ generic → specific
Iteration Mindset — Shift quan trọng nhất
Tại sao khó?
3 nguyên tắc Iteration
1. First drafts as starting points
2. Specific feedback
3. Know when to start fresh
AI Fluency — và tại sao nó quan trọng
4D Framework — Đào sâu
1. Delegation — Giao gì cho AI?
2. Description — Giao thế nào?
3. Discernment — Đánh giá output thế nào?
4. Diligence — Trách nhiệm cuối cùng
Delegation-Diligence Loop — Build confidence có căn cứ
Case study: Rio — Program Director tại Valley Veterans Services
Rio's loop — 6 bước
Bước 1: Identify specific task
Bước 2: Find past data với ground truth
Bước 3: Prompt AI tái tạo kết quả
Bước 4: Check output vs. ground truth
Bước 5: Refine description
Bước 6: Test harder question
Kết quả loop
Điều quan trọng: 2 outcomes đều giá trị
Khi bạn không đủ kiến thức để spot gaps?
Evals — Test hệ thống cho workflows của bạn
Tại sao eval matter?
Lightweight eval approach — 4 bước
Bước 1: Gather examples
Bước 2: Create test prompts
Bước 3: Compare outputs
Bước 4: Refine approach
Eval ví dụ cụ thể: weekly status report
Golden examples (Bước 1)
Test prompt (Bước 2)
Compare (Bước 3)
Refine (Bước 4)
Ví dụ theo ngành — Eval template
📊 Data Analyst
📣 Content Marketer
💰 Finance Analyst
🎓 Teacher
Anti-patterns khi iterate và eval
❌ Fix symptom thay vì root cause
❌ Over-iterate trên một response
❌ Eval 1 lần rồi forget
❌ Confuse subjective feedback với accuracy issue
1.3 - Tối ưu kết quả — AI Fluency & Iteration​
Modified April 20
Bài 03: Tối ưu kết quả — AI Fluency & Iteration​
Module: Làm quen với Claude​
Thời gian ước tính: 20 phút​
Mức độ: Cơ bản → Trung cấp​
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
✅ Nhận diện 5 common challenges khi dùng Claude và áp dụng kỹ thuật fix nhanh​
•
✅ Giải thích AI Fluency và biết nơi học sâu hơn​
•
✅ Áp dụng 4D Framework vào công việc cụ thể của mình​
•
✅ Thiết lập delegation-diligence loop để test Claude trên task riêng​
•
✅ Chạy lightweight evals để build confidence có căn cứ vào AI​
Mở đầu: Tại sao response không đúng ý?​
Bạn đã dùng Claude được vài ngày. Có những lần response rất đúng ý — bạn cảm giác "wow, AI hiểu mình". Nhưng cũng có lần:​
•
Response quá generic, bạn đọc nửa chừng phải dừng vì nó viết như AI (oh, irony)​
•
Claude confident-sounding nhưng sai một con số quan trọng​
•
Tông quá formal, không match context Việt Nam / team của bạn​
•
Bạn yêu cầu 200 từ, nó viết 800 từ; bạn yêu cầu bullet, nó trả về prose​
Phản ứng đầu tiên là blame AI. "AI ngu quá." "Claude không hiểu tôi." "Đây rồi, AI overhyped."​
Phản ứng đúng: Đây là signal. Mỗi response "chưa ưng" là một cơ hội học thêm về cách brief Claude cho đúng. Người thạo AI sau 6 tháng không phải vì Claude đã cải thiện 10x — mà vì họ đã học cách giao tiếp với Claude theo cách có hệ thống hơn.​
Bài này dạy bạn:​
1.
Troubleshooting techniques — fix nhanh 5 loại problem phổ biến​
2.
4D Framework — cách suy nghĩ về AI collaboration​
3.
Evals — cách test Claude một cách hệ thống trên task của bạn​
Comments (1)
Go to the first comment
Help Center
Keyboard Shortcuts
