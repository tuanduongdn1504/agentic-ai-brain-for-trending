# 17.10 - Thực hành — Letter vs Spirit (Theo chữ vs theo ý)

**Source:** https://transform.sg.larksuite.com/wiki/GBWHwDbihin6JnkJEq5lGgCXgNf
**Wiki ID:** GBWHwDbihin6JnkJEq5lGgCXgNf
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

17.10 - Thực hành — Letter vs Spirit (Theo chữ vs theo ý)

Last updated: Apr 20

Log In or Sign Up
17.10 - Thực hành — Letter vs Spirit (Theo chữ vs theo ý)
Bài 17.10: Thực hành — Letter vs Spirit (Theo chữ vs theo ý)
Mục tiêu học tập
Bối cảnh: Đồng nghiệp chuyển bạn một email
Phần 1: Xác định cấu trúc email
Các ý trong email
Priority
Phần 2: Chạy 3 prompts khác nhau
Prompt A: "Make it shorter" (letter)
Prompt B: "Make it shorter, keep the core" (slightly better)
Prompt C: State the goal (spirit)
Phần 3: So sánh 3 output
Nguyên lý: Prompt từ intent, không chỉ từ instruction
Patterns khi nào letter-vs-spirit gap lớn
Framework: IPO prompt — Intent-Purpose-Output
Ví dụ với email ở trên
Real-world tests
Mẹo nâng cao
Mẹo 1: "5 Whys" cho instruction của bạn
Mẹo 2: "Test audience" framing
Mẹo 3: "Before/after success state"
Anti-patterns
❌ "Just say 'make it better' — AI figure it out"
❌ "Long prompt = more control"
❌ "If AI missed intent, just say it louder"
Áp dụng ngay
Bài tập 1: The Jordan-Marcus rewrite (10 phút)
Bài tập 2: Audit 3 instruction-level prompts
Suy ngẫm bài học
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
17.10 - Thực hành — Letter vs Spirit (Theo chữ vs theo ý)​
Modified April 20
Bài 17.10: Thực hành — Letter vs Spirit (Theo chữ vs theo ý)​
Module: Bốn thuộc tính cốt lõi (4/4 — thực hành)​
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
Slide: AI Capabilities and Limitations.pdf​
​
​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Trải nghiệm trực tiếp hiện tượng letter-over-spirit qua một ví dụ thực tế ngắn​
•
✅ Nhận diện dấu hiệu khi instruction đã được honored literally nhưng intent bị miss​
•
✅ Viết lại prompt từ intent, không chỉ từ instruction​
•
✅ So sánh 3 cách phrase cùng một request — và thấy chất lượng output khác nhau ra sao​
​
​
Bối cảnh: Đồng nghiệp chuyển bạn một email​
Đồng nghiệp của bạn vừa chuyển cho bạn email dưới đây và nhờ "làm ngắn lại giùm":​
​
​
From: Jordan ReyesTo: Marcus ChenSubject: Following up on Q2 roadmap​
Hope your week is going well! I wanted to circle back on the Q2 roadmap discussion from last Tuesday. The team has been digging into the three proposed directions and we've landed on a recommendation, though there are some tradeoffs worth flagging. We think the platform consolidation path makes the most sense given the resourcing constraints, but it does mean pushing the mobile redesign to Q3. Would love to get your sign-off before we finalize with the broader team on Friday. Happy to hop on a call if that's easier.​
​
​
Email dài ~130 từ. "Làm ngắn" có thể nghĩa là nhiều thứ. Đó là điểm bài học.​
​
​
Phần 1: Xác định cấu trúc email​
Trước khi đưa cho AI, bạn hãy phân tích:​
Các ý trong email​
Comments (0)
Help Center
Keyboard Shortcuts
