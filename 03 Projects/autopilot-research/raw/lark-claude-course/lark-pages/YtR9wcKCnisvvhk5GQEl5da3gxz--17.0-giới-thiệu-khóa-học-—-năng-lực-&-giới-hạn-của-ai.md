# 17.0 - Giới thiệu khóa học — Năng lực & Giới hạn của AI

**Source:** https://transform.sg.larksuite.com/wiki/YtR9wcKCnisvvhk5GQEl5da3gxz
**Wiki ID:** YtR9wcKCnisvvhk5GQEl5da3gxz
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

17.0 - Giới thiệu khóa học — Năng lực & Giới hạn của AI

Last updated: Apr 20

Log In or Sign Up
17.0 - Giới thiệu khóa học — Năng lực & Giới hạn của AI
Bài 17.0: Giới thiệu khóa học — Năng lực & Giới hạn của AI
Tại sao bạn cần khóa học này?
Mục tiêu học tập
Mô hình tư duy về cỗ máy
Lộ trình khóa học (14 bài)
Capabilities & Limitations Framework
Hai nửa của một hệ thống: 4D + 4 thuộc tính
Tại sao khóa này "durable" (không lỗi thời)
Ba điều cần mang theo vào mỗi bài
1. "Calibrated trust" (Niềm tin được hiệu chỉnh)
2. "Hand the real task" (Mang task thật vào khóa học)
3. "Properties don't operate alone" (Thuộc tính không hoạt động độc lập)
Áp dụng ngay
Bài tập nền móng: Mapping Your Current AI Use (15-20 phút)
Suy ngẫm bài học
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
17.0 - Giới thiệu khóa học — Năng lực & Giới hạn của AI​
Modified April 20
Bài 17.0: Giới thiệu khóa học — Năng lực & Giới hạn của AI​
Module: Tổng quan khóa học​
Thời gian ước tính: 15 phút​
Mức độ: Cơ bản​
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
Tại sao bạn cần khóa học này?​
Hãy thành thật một chút. Trong vài tuần gần đây, bạn đã dùng AI (Claude, ChatGPT, hoặc bất kỳ trợ lý AI nào) bao nhiêu lần?​
Và trong số đó, bao nhiêu lần bạn rơi vào một trong các tình huống dưới đây:​
•
AI đưa ra câu trả lời nghe rất thuyết phục, nhưng sau khi bạn kiểm tra lại thì hóa ra hoàn toàn sai (một bài báo không tồn tại, một con số bịa ra, một trích dẫn không có thật).​
•
Bạn dán một tài liệu dài 20 trang vào, hỏi một câu hỏi ở trang 11, và AI... bỏ qua điều quan trọng nhất.​
•
Bạn hướng dẫn AI 20 phút đầu cuộc hội thoại, rồi đến tin nhắn thứ 40 thì nó quên sạch hướng dẫn ban đầu.​
•
Bạn nói "làm ngắn lại đi", AI làm ngắn — nhưng lại cắt mất cái ý quan trọng nhất trong bản nháp của bạn.​
•
Bạn phản biện một chút, AI lập tức rút lại ý kiến và đồng ý với bạn, dù bạn biết rằng ý kiến ban đầu của nó đúng hơn.​
Nếu bạn từng gặp ít nhất 2 trong 5 tình huống trên, bạn đang ở đúng chỗ. Khóa học này không dạy bạn "prompt tricks" hay "10 cách xài AI thần thánh". Nó dạy bạn một thứ bền hơn nhiều: một mô hình tư duy về cách AI thực sự hoạt động — để bạn không còn bị bất ngờ, và biết chính xác khi nào nên tin, khi nào nên kiểm tra, khi nào nên đổi cách làm.​
Mục tiêu học tập​
Sau khi hoàn thành khóa học này, bạn sẽ có thể:​
•
✅ Giải thích khóa học bao quát điều gì và được cấu trúc như thế nào​
•
✅ Hiểu tại sao kiến thức này không lỗi thời khi model và sản phẩm liên tục thay đổi​
•
✅ Nhận ra cách Capabilities & Limitations Framework kết hợp với 4D Framework thành một hệ thống hoàn chỉnh​
•
✅ Bắt đầu bài tập "Mapping Your Current AI Use" — nền móng cho mọi bài sau​
Mô hình tư duy về cỗ máy​
Comments (0)
Help Center
Keyboard Shortcuts
