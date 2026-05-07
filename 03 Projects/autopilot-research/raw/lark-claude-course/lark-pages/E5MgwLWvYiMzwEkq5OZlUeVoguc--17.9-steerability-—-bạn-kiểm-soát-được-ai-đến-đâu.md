# 17.9 - Steerability — Bạn kiểm soát được AI đến đâu?

**Source:** https://transform.sg.larksuite.com/wiki/E5MgwLWvYiMzwEkq5OZlUeVoguc
**Wiki ID:** E5MgwLWvYiMzwEkq5OZlUeVoguc
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

17.9 - Steerability — Bạn kiểm soát được AI đến đâu?

Last updated: Apr 20

Log In or Sign Up
17.9 - Steerability — Bạn kiểm soát được AI đến đâu?
Bài 17.9: Steerability — Bạn kiểm soát được AI đến đâu?
Mục tiêu học tập
Mở đầu: Khoảnh khắc "letter over spirit"
Steerability là gì — và tại sao nó hoạt động
Điều này không phải tự nhiên có
Nhưng steerability không là understanding
Steerability Continuum
Ví dụ cụ thể
3 failure modes đặc trưng
Failure 1: Reasoning drift
Failure 2: Letter over spirit
Failure 3: Prompt injection (security concern)
Product features "push edge out"
Feature 1: System prompts / Custom instructions
Feature 2: Code execution
Feature 3: Visible reasoning (Extended Thinking)
Feature 4: Structured output modes
Techniques của bạn: Thu hẹp gap intent-instruction
Technique 1: State goal alongside steps
Technique 2: Break long chains với checkpoints
Technique 3: Restate goal, not instruction
Technique 4: Verify-able output specs
Technique 5: Role + Purpose together
Ví dụ theo ngành
💰 Finance Analyst — Precision in calculations
⚖️ Legal Counsel — Letter-over-spirit in contract drafting
📝 Content Marketer — Structured output cho newsletter
🔍 Research Analyst — Checkpoint protocol cho lit review
🎧 Customer Support — Role + purpose prompt
Anti-patterns
❌ "Prompt kỹ hơn = AI control tốt hơn"
❌ "AI 'hiểu' rồi, no need to repeat goal"
❌ "Instruction ambiguous thì AI sẽ hỏi"
❌ "Chain of thought = AI now reasoning properly"
❌ "Structured output → output chắc chắn đúng"
Mẹo nâng cao
Mẹo 1: "Chain-of-verification" pattern
Mẹo 2: "Devil's advocate" internal debate
Mẹo 3: "Template + examples" — few-shot pattern
Mẹo 4: "Meta-prompt" — ask AI to structure your prompt
Mẹo 5: Log steerability failures
Áp dụng ngay
Bài tập 1: The Goal Rewrite (~25 phút)
Bài tập 2: Write a "standing role" prompt (optional)
Suy ngẫm bài học
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
17.9 - Steerability — Bạn kiểm soát được AI đến đâu?​
Modified April 20
Bài 17.9: Steerability — Bạn kiểm soát được AI đến đâu?​
Module: Bốn thuộc tính cốt lõi (4/4)​
Thời gian ước tính: 30 phút​
Mức độ: Trung cấp → Nâng cao​
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
✅ Giải thích tại sao steerability hoạt động (fine-tuning đã dạy model instruction-following) và tại sao nó có giới hạn (instructions được theo qua pattern-matching, không phải understanding)​
•
✅ Dự đoán nơi control chặt nhất (instruction ngắn, cụ thể, kiểm chứng được) vs lỏng nhất (long reasoning chains, abstract asks, precision tasks)​
•
✅ Nhận diện 3 failure đặc trưng: reasoning drift, letter over spirit, brittle arithmetic​
•
✅ Nhận ra system prompts, code execution, visible reasoning, structured outputs = tính năng sản phẩm​
•
✅ Thu hẹp gap giữa "điều bạn gõ" và "điều bạn muốn" qua kỹ thuật prompt từ intent​
Mở đầu: Khoảnh khắc "letter over spirit"​
Bạn gửi Claude một email 200 từ và nói:​
"Làm cho nó ngắn hơn."​
Claude trả về email 100 từ. Ngắn hơn thật — đúng 50%. Nhưng...​
Email gốc có 4 ý:​
1.
Cảm ơn khách hàng​
2.
Xin lỗi về chậm trễ​
3.
Đề xuất giải pháp cụ thể + ngày hoàn thành mới​
4.
Invite to follow-up call​
Email ngắn giữ 1, 2, 4 — cắt ý 3. Cái ý quan trọng nhất.​
Tại sao? Vì ý 3 là đoạn dài nhất (60 từ), cắt nó giảm được nhiều ký tự nhất. Từ góc nhìn letter of instruction: "làm ngắn hơn" — tuân thủ. Từ góc nhìn spirit of intent: "giữ được cái quan trọng và cắt cái filler" — thất bại.​
AI không cố tình hỏng. Nó không "hiểu" rằng ý 3 quan trọng hơn. Nó theo literal instruction qua pattern matching, không qua understanding intent.​
Comments (0)
Help Center
Keyboard Shortcuts
