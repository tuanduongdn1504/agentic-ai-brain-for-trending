# 17.7 - Working Memory — Context window & vách đá cứng

**Source:** https://transform.sg.larksuite.com/wiki/KgW6wLQuLiR594kZe0YlA5sPgve
**Wiki ID:** KgW6wLQuLiR594kZe0YlA5sPgve
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

17.7 - Working Memory — Context window & vách đá cứng

Last updated: Apr 20

Log In or Sign Up
17.7 - Working Memory — Context window & vách đá cứng
Bài 17.7: Working Memory — Context window & vách đá cứng
Mục tiêu học tập
Mở đầu: Khoảnh khắc "AI quên hết"
Context window — Bộ nhớ làm việc của AI
Điều gì xảy ra khi đầy?
Giữa sessions — Reset về 0
Đây là thuộc tính có CLIFF (vách đá)
Working Memory Continuum
Ví dụ task trên continuum
4 failure modes đặc trưng
Failure 1: Hard length limits — Silent truncation
Failure 2: Lost in the middle
Failure 3: No persistent memory by default
Failure 4: Model không learn từ correction
Product features "push cliff out"
Feature 1: Memory
Feature 2: Compaction / Summarization
Feature 3: Projects / Workspaces
Feature 4: Skills
Feature 5: Larger context windows
Context-as-leverage: Kỹ thuật của chính bạn
Kỹ thuật 1: Front-loading
Kỹ thuật 2: Chunking
Kỹ thuật 3: Re-supply critical context
Kỹ thuật 4: Structure over narrative
Kỹ thuật 5: Explicit context markers
Ví dụ theo ngành
⚖️ Legal Counsel — 50-page contract review
🔍 Research Analyst — Literature review 30+ papers
📝 Content Marketer — Multi-platform content repurposing
💻 Developer — Long code review
🎧 Customer Success Manager — QBR prep cho 20 accounts
Anti-patterns
❌ "More context = better results"
❌ "AI remember mọi thứ tôi đã nói"
❌ "Correct một lần là Claude 'biết'"
❌ "1 giant upload tốt hơn 5 chunks nhỏ"
❌ "Giữ mọi tin nhắn cũ — biết đâu cần"
Mẹo nâng cao
Mẹo 1: Token counter mental model
Mẹo 2: "Context budget" plan
Mẹo 3: "Structured handoff" pattern cho long session
Mẹo 4: "Standing context" file
Mẹo 5: "Attention anchors" trong long prompt
Áp dụng ngay
Bài tập 1: The Before-and-After (~25 phút)
Bài tập 2 (optional): Context budget
Suy ngẫm bài học
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
17.7 - Working Memory — Context window & vách đá cứng​
Modified April 20
Bài 17.7: Working Memory — Context window & vách đá cứng​
Module: Bốn thuộc tính cốt lõi (3/4)​
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
Slide: AI Capabilities and Limitations.pdf​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Giải thích context window là một fixed-size container và hệ quả của điều này cho long documents, long conversations, cross-session memory​
•
✅ Nhận ra tính chất cliff (vách đá) của Working Memory — khác với gradient của 3 thuộc tính còn lại​
•
✅ Áp dụng các chiến lược context-as-leverage: front-loading, chunking, re-supplying critical context​
•
✅ Nhận diện memory, compaction, projects/workspaces, larger windows = các tính năng sản phẩm giải quyết giới hạn này​
•
✅ Thiết kế workflow tận dụng context hiệu quả cho task của bạn​
Mở đầu: Khoảnh khắc "AI quên hết"​
Có một lần, tôi dành 2 giờ đầu cuộc hội thoại setup context rất kỹ với Claude:​
•
Dán 12 trang style guide công ty​
•
Paste 5 ví dụ email bạn đã duyệt​
•
Explain persona của khách hàng mục tiêu​
•
Demo 3 câu trả lời tốt vs 2 câu trả lời tệ​
Sau đó, tôi bắt đầu nhờ Claude draft emails thực tế. 20 email đầu — hoàn hảo, theo style guide từng chi tiết.​
Đến email số 25, tôi nhận ra một cái gì đó lệch. Style hơi khác. Có vài từ ngữ không đúng brand voice.​
Email 30: đi xa hoàn toàn. Tone formal kiểu luật sư, không phải casual-professional như đã dặn.​
Tôi scroll lên trên. Tôi vẫn thấy cái style guide trong hội thoại. Nhưng Claude không còn "chú ý" đến nó.​
Cái gì đã xảy ra?​
Context window đã đầy. Claude bắt đầu bỏ qua (hoặc attention yếu dần trên) những phần sớm nhất. Style guide 12 trang — đặt ở đầu — bây giờ ở "đáy biển" của cái mà model đang nhìn thấy.​
Comments (0)
Help Center
Keyboard Shortcuts
