# 17.12 - Next Steps — Tổng hợp, cam kết hành động, và đi sâu hơn

**Source:** https://transform.sg.larksuite.com/wiki/YJKzwUQvPiR1ASkCDeKlROUEgZd
**Wiki ID:** YJKzwUQvPiR1ASkCDeKlROUEgZd
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

17.12 - Next Steps — Tổng hợp, cam kết hành động, và đi sâu hơn

Last updated: Apr 20

Log In or Sign Up
17.12 - Next Steps — Tổng hợp, cam kết hành động, và đi sâu hơn
Bài 17.12: Next Steps — Tổng hợp, cam kết hành động, và đi sâu hơn
Mục tiêu học tập
Mở đầu: Bạn đến với một câu hỏi, rời với một cấu trúc
Cái bạn mang theo
Hai giai đoạn training → mọi hành vi truy ngược được
Bốn thuộc tính, mỗi cái là một continuum
Lỗi thường là 2 thuộc tính giao thoa
Two halves of one system: 4D + 4 Properties
Mapping cụ thể:
Calibrated Trust là một habit, không phải một attitude
Hình dạng của framework stays useful
Cái sẽ thay đổi — và cái sẽ không
Một vài ghi chú về điều khóa học không nói
1. Agentic systems
2. Multi-modal
3. Fine-tuning custom models
4. AI safety & alignment research
Commitment: Một thay đổi cụ thể tuần này
4 categories of change
Choose ONE. Write it down.
Áp dụng ngay
Bài tập: Your Commitment (15 phút)
Suy ngẫm bài học (cuối cùng)
Tóm tắt khóa học
Đi sâu hơn
Nếu bạn chưa học AI Fluency: Framework & Foundations
Advanced reading
Keep testing edges
Bài tiếp theo
Feedback
Lời kết
Tài liệu tham khảo
17.12 - Next Steps — Tổng hợp, cam kết hành động, và đi sâu hơn​
Modified April 20
Bài 17.12: Next Steps — Tổng hợp, cam kết hành động, và đi sâu hơn​
Module: Tích hợp & áp dụng​
Thời gian ước tính: 20 phút​
Mức độ: Tổng hợp​
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
✅ Tổng hợp 4 thuộc tính + training fingerprints thành một working mental model duy nhất​
•
✅ Kết nối Capabilities & Limitations Framework với 4D Framework — hai nửa của một hệ thống​
•
✅ Xác định một thay đổi cụ thể bạn sẽ áp dụng trong AI practice tuần này​
•
✅ Biết đi đâu tiếp theo để đi sâu hơn​
​
​
Mở đầu: Bạn đến với một câu hỏi, rời với một cấu trúc​
Bạn đã vào khóa học này với một phiên bản nào đó của câu hỏi:​
"Tại sao AI làm như thế?"​
Bạn đang rời khóa học với một cấu trúc để tự trả lời câu hỏi kế tiếp.​
Đó là khác biệt mọi người cần. Không phải 1 danh sách failure modes để thuộc lòng. Không phải 5 prompt tricks cho 5 tình huống. Mà là một mental model giúp bạn đứng trước bất kỳ task AI nào mới và hỏi đúng câu hỏi.​
​
​
Cái bạn mang theo​
Hai giai đoạn training → mọi hành vi truy ngược được​
​
Code block​
Plain Text
Copy
┌──────────────────────────────────────────────────────────┐​
│                                                          │​
│   Stage 1: PRETRAINING                                   │​
│   → Document completer (predict next token)              │​
│                                                          │​
│              ↓                                           │​
​
Comments (0)
Help Center
Keyboard Shortcuts
