# 17.8 - Thực hành — Context Degradation (Khi "thêm context" làm tệ hơn)

**Source:** https://transform.sg.larksuite.com/wiki/GyZnwwKBKiUQNhk7ckblohISgbh
**Wiki ID:** GyZnwwKBKiUQNhk7ckblohISgbh
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

17.8 - Thực hành — Context Degradation (Khi "thêm context" làm tệ hơn)

Last updated: Apr 20

Log In or Sign Up
17.8 - Thực hành — Context Degradation (Khi "thêm context" làm tệ hơn)
Bài 17.8: Thực hành — Context Degradation (Khi "thêm context" làm tệ hơn)
Mục tiêu học tập
Mở đầu: Một bản năng gây hại
Phần 1: Memory Test trên chính bạn (5 phút)
Cách làm
Kết quả
Phần 2: U-Shaped Curve — Serial Position Effect
Primacy (đầu list)
Recency (cuối list)
Giữa
Phần 3: LLMs biểu hiện cùng pattern
Research Stanford 2023
Tại sao?
Phần 4: Điều này có ý nghĩa gì cho prompting?
Thực tế: nếu bạn paste 20-page document
Dangerous pattern (cần tránh)
Safer pattern
3 quy tắc vàng context engineering
Quy tắc 1: Place critical info at edges
Quy tắc 2: Repeat what matters
Quy tắc 3: Curate ruthlessly
Context engineering vs prompt engineering
Ví dụ theo ngành
⚖️ Legal — Redesign contract review prompt
💰 Finance — 10-K analysis prompt
📝 Content Marketing — Brief dài
🎧 Customer Support — Ticket analysis
Anti-patterns
❌ "Big context dump → AI tự figure out cái quan trọng"
❌ "Repeat critical info là redundant"
❌ "Chat dài vẫn OK vì model handle 200K tokens"
❌ "Copy-paste tất cả tin nhắn Slack hôm qua vào cho AI context"
Mẹo nâng cao
Mẹo 1: "XML tags" làm attention anchors
Mẹo 2: "Table of contents" cho long prompts
Mẹo 3: "Highlight" critical instruction
Mẹo 4: Adaptive chunking thresholds
Mẹo 5: Cross-chunk synthesis pattern
Áp dụng ngay
Bài tập 1: Lost-in-the-middle probe (~15 phút)
Bài tập 2: Audit 1 long prompt của bạn
Suy ngẫm bài học
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
17.8 - Thực hành — Context Degradation (Khi "thêm context" làm tệ hơn)​
Modified April 20
Bài 17.8: Thực hành — Context Degradation (Khi "thêm context" làm tệ hơn)​
Module: Bốn thuộc tính cốt lõi (3/4 — thực hành)​
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
Slide: AI Capabilities and Limitations.pdf​
​
​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Trải nghiệm trực tiếp hiệu ứng "lost in the middle" qua một memory test trên chính bạn​
•
✅ Giải thích serial position effect — primacy và recency — và tại sao LLM biểu hiện cùng pattern​
•
✅ Nhận ra context engineering không chỉ là "cái gì include" mà còn là "đặt ở đâu"​
•
✅ Áp dụng 3 quy tắc vàng: place critical instructions at edges, repeat what matters, curate ruthlessly​
​
​
Mở đầu: Một bản năng gây hại​
Khi dùng AI, bản năng tự nhiên là đưa cho nó mọi thứ. Paste nguyên document. Include mọi tin nhắn trước. Đưa tất cả context bạn có thể tìm.​
More information = better answers, đúng không?​
Không phải luôn luôn.​
Có một hiện tượng mà ai đã cram trước kỳ thi đều biết: có giới hạn bạn hold được trong đầu cùng lúc. Và cái giữa biến mất đầu tiên.​
Trước khi nói hiện tượng này ảnh hưởng AI thế nào, xem nó ảnh hưởng chính bạn ra sao.​
​
​
Phần 1: Memory Test trên chính bạn (5 phút)​
Cách làm​
Dưới đây là 15 từ. Đọc chúng một lần, theo thứ tự, mỗi từ dành 1.5 giây. Không quay lại.​
Sau khi đọc hết, che xuống và cố nhớ nhiều từ nhất có thể (theo thứ tự bất kỳ). Ghi chúng ra giấy trước khi scroll xuống.​
Comments (0)
Help Center
Keyboard Shortcuts
