# 17.11 - When Properties Collide — Chẩn đoán khi 2 thuộc tính giao thoa

**Source:** https://transform.sg.larksuite.com/wiki/EQKUwcatviLZCYkgpfil1nhRgzh
**Wiki ID:** EQKUwcatviLZCYkgpfil1nhRgzh
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
Slide: AI Capabilities and Limitations.pdf
17.0 - Giới thiệu khóa học — Năng lực & Giới hạn của AI
17.1 - AI ở đây là gì — Vẽ ranh giới của "generative AI"
17.2 - AI hình thành tính cách như thế nào — Pretraining, Fine-tuning & những dấu vân tay
17.3 - Next Token Prediction — Autocomplete ở quy mô khổng lồ
17.4 - Thực hành — Text Your Friend Markov
17.5 - Knowledge — AI thực sự biết những gì
17.6 - Thực hành — Embeddings & Similarity Search (Không gian ngữ nghĩa 1024 chiều)
17.7 - Working Memory — Context window & vách đá cứng
17.8 - Thực hành — Context Degradation (Khi "thêm context" làm tệ hơn)
17.9 - Steerability — Bạn kiểm soát được AI đến đâu?
17.10 - Thực hành — Letter vs Spirit (Theo chữ vs theo ý)
17.11 - When Properties Collide — Chẩn đoán khi 2 thuộc tính giao thoa
17.12 - Next Steps — Tổng hợp, cam kết hành động, và đi sâu hơn
17.13 - Quiz tổng kết — Kiểm tra mental model của bạn
📣
Bổ sung course
Transform Group

17.11 - When Properties Collide — Chẩn đoán khi 2 thuộc tính giao thoa

Last updated: Apr 20

Log In or Sign Up
17.11 - When Properties Collide — Chẩn đoán khi 2 thuộc tính giao thoa
Bài 17.11: When Properties Collide — Chẩn đoán khi 2 thuộc tính giao thoa
Mục tiêu học tập
Mở đầu: Một trải nghiệm quen thuộc
Four properties — nhắc lại nhanh
5 collision patterns phổ biến
Collision 1: Next Token Prediction × Knowledge = Hallucinated specifics
Collision 2: Working Memory × Steerability = Long-conversation drift
Collision 3: Next Token Prediction × Steerability = Letter-over-spirit at scale
Collision 4: Knowledge × Steerability = Confidently wrong on niche instructions
Collision 5: All 4 — Long multi-step task with specific domain
Diagnostic framework: "Which 2 collided?"
Diagnostic table: Common symptoms → properties → fixes
Ví dụ theo ngành
💼 Sales Manager — "AI biến một deal thành 2 deals"
🔍 Research Analyst — "Lit review bịa 3 paper"
⚖️ Legal Counsel — "50-page contract review — AI missed 3 critical clauses"
💰 Finance Analyst — "Wrong IRR in memo"
🎧 Customer Success Manager — "Chat got worse over 30 messages"
🏥 Clinical Research Coordinator — "AI gave wrong drug protocol"
Anti-patterns
❌ "It's just hallucination" — single-property diagnosis
❌ "Re-prompt until it works"
❌ "Model got better, same prompt works now"
❌ "Single fix = solves all my problems"
❌ "AI will eventually ask me if confused"
Mẹo nâng cao
Mẹo 1: "Failure log" với property tagging
Mẹo 2: Task complexity matrix before starting
Mẹo 3: "Stress test" bằng cách introduce property issues
Mẹo 4: "Property-aware review" habit
Mẹo 5: Cross-property failure cascades
Áp dụng ngay
Bài tập 1: Failure Diagnosis (~25 phút)
Bài tập 2: Preemptive collision mapping (optional)
Suy ngẫm bài học
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
17.11 - When Properties Collide — Chẩn đoán khi 2 thuộc tính giao thoa​
Modified April 20
Bài 17.11: When Properties Collide — Chẩn đoán khi 2 thuộc tính giao thoa​
Module: Tích hợp & áp dụng​
Thời gian ước tính: 25 phút​
Mức độ: Nâng cao​
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
Slide: AI Capabilities and Limitations.pdf​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Nhận ra hầu hết AI failures liên quan 2 hoặc nhiều thuộc tính tương tác, không phải 1​
•
✅ Chẩn đoán các failure pattern phổ biến (hallucinated citations, long-conversation drift, confidently wrong math, agreeable bad premises) bằng cách đặt tên properties liên quan​
•
✅ Áp dụng targeted fix dựa vào thuộc tính limiting (nút cổ chai)​
•
✅ Xây diagnostic habit: trước khi reach for prompt fix, hỏi "which properties am I looking at?"​
Mở đầu: Một trải nghiệm quen thuộc​
Tuần trước, đây là task thực tế:​
Bạn đang nghiên cứu thị trường fintech Việt Nam cho một pitch đầu tư. Dùng Claude với web search enabled. Prompt:​
"Tìm 5 fintech startups Vietnam lớn nhất, founded 2020-2024.Cho tôi: tên, founder, tổng funding raised, HQ location,và 1 câu về product."​
Claude trả về table đẹp:​
​
Company​
Founder​
Funding​
HQ​
Product​
VNPay​
	
Lê Thanh Long​
	
$300M​
	
Hanoi​
	
Payment gateway​


Momo​
	
Phạm Thành Đức​
	
$500M​
	
HCMC​
	
E-wallet​


Tiki (Finova)​
	
Trần Ngọc Thái Sơn​
	
$250M​
	
HCMC​
	
Lending platform​


...​
	
​
	
​
	
​
	
​
​
Comments (0)
Help Center
Keyboard Shortcuts
