# 17.4 - Thực hành — Text Your Friend Markov

**Source:** https://transform.sg.larksuite.com/wiki/ILHWwcXv6iqhVyk9VhHlVmDRgVh
**Wiki ID:** ILHWwcXv6iqhVyk9VhHlVmDRgVh
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

17.4 - Thực hành — Text Your Friend Markov

Last updated: Apr 20

Log In or Sign Up
17.4 - Thực hành — Text Your Friend Markov
Bài 17.4: Thực hành — Text Your Friend Markov
Mục tiêu học tập
Mở đầu: Một trò chơi tuổi teen của tác giả Anthropic
Phần 1: Training bằng tay (7 phút)
Dataset của chúng ta: 5 tin nhắn
Bước 1: Đếm các "bigram" (cặp từ liền nhau)
Bước 2: Chuẩn hóa thành xác suất
Phần 2: Sampling bằng tay (7 phút)
Sampling step by step
Nhưng đôi khi nó sinh ra tin mới
Hai thuật ngữ quan trọng bạn vừa làm
Phần 3: Scale up (3 phút)
Thí nghiệm suy nghĩ
Phần 4: Các "knobs" — Sampling strategies (5 phút)
Phần 5: Từ Markov đến Claude
Phần 6: 100 năm lịch sử (3 phút)
Anti-patterns khi nghĩ về LLM
❌ "AI có hiểu thực sự"
❌ "AI tra cứu trong database"
❌ "Temperature = 0 làm AI chính xác"
Áp dụng ngay
Bài tập 1: Xây Markov chain của chính mình (~15 phút)
Bài tập 2 (stretch): Sampling strategies trong Claude API
Bài tập 3: Giải thích cho bạn
Suy ngẫm bài học
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
17.4 - Thực hành — Text Your Friend Markov​
Modified April 20
Bài 17.4: Thực hành — Text Your Friend Markov​
Module: Bốn thuộc tính cốt lõi (1/4 — thực hành)​
Thời gian ước tính: 25 phút​
Mức độ: Trung cấp (có thực hành bằng tay)​
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
✅ Xây bằng tay một mô hình dự đoán token đơn giản (Markov chain) từ 5 tin nhắn — hiểu "training" và "sampling" là gì​
•
✅ Giải thích transition matrix là gì và tại sao normalize row cho ra xác suất "next token"​
•
✅ Thực hiện sampling với các strategies khác nhau (greedy, random, temperature, top-k) — chính là các "knob" của Claude​
•
✅ Kết nối Markov chain (1906) với modern LLM (transformer 2017) — cùng một nguyên lý, khác ở cách compute distribution​
Mở đầu: Một trò chơi tuổi teen của tác giả Anthropic​
Nhiều năm trước, một nhóm bạn chơi một trò vớ vẩn: cầm điện thoại, chỉ dùng các từ gợi ý từ autocomplete để gõ một tin nhắn gửi bạn. Mở iMessage, gõ "I", để bàn phím đề xuất 3 từ, chọn 1 trong 3... và cứ thế.​
Kết quả luôn kỳ quặc. Câu văn grammatically ổn, nhưng ý nghĩa? Vô vọng.​
Họ gọi bàn phím đó là "Me-bot" — một phiên bản chatbot của chính mình. Nó gợi ý dựa trên cách mỗi người đã gõ trong quá khứ. Họ thấy "giọng" của mình trong các gợi ý.​
Lúc đó, mọi người coi đây là "tech magic". Không ai nghĩ thuật toán đằng sau đơn giản đến mức nào.​
Bài này chúng ta xây một Me-bot bằng tay. 5 tin nhắn. Giấy bút là đủ. Khi xây xong, bạn sẽ hiểu Claude ở một mức rất cụ thể — không còn là "phép màu".​
Phần 1: Training bằng tay (7 phút)​
Dataset của chúng ta: 5 tin nhắn​
​
Code block​
Plain Text
Copy
1. "i think we should probably ship it"​
​
Comments (0)
Help Center
Keyboard Shortcuts
