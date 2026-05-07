# 5.4 - Cơ bản về Generative AI — Hiểu cái máy bạn đang dùng

**Source:** https://transform.sg.larksuite.com/wiki/AeqgwxFOLiOXZHkKHyflKgXag2f
**Wiki ID:** AeqgwxFOLiOXZHkKHyflKgXag2f
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
Slide: AI Fluency: Framework & Foundations.pdf
5.0 - Khóa 5: AI Fluency — Khung & Nền tảng (Bản tiếng Việt)
5.1 - Giới thiệu AI Fluency — Khóa học và bạn
5.2 - Tại sao cần AI Fluency — Và tại sao là bây giờ
5.3 - Khung 4D — Toàn cảnh Delegation, Description, Discernment, Diligence
5.4 - Cơ bản về Generative AI — Hiểu cái máy bạn đang dùng
5.5 - Năng lực và giới hạn của AI hôm nay
5.6 - Cận cảnh Delegation — Quyết định "ai làm gì"
5.7 - Lập kế hoạch dự án + Delegation — Thực hành
5.8 - Cận cảnh Description — Truyền đạt rõ ràng với AI
5.9 - Kỹ thuật prompting hiệu quả — 6 vũ khí cốt lõi
5.10 - Cận cảnh Discernment — Đánh giá phê phán AI
5.11 - Vòng lặp Description-Discernment — Thực hành dự án
5.12 - Cận cảnh Diligence — Trách nhiệm, minh bạch, an toàn
5.13 - Kết luận — Khung 4D như la bàn cho hành trình tiếp theo
5.14 - Bài kiểm tra & Chứng nhận hoàn thành
5.15 - Hoạt động bổ sung — Đào sâu hơn
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

5.4 - Cơ bản về Generative AI — Hiểu cái máy bạn đang dùng

Last updated: Apr 20

Log In or Sign Up
5.4 - Cơ bản về Generative AI — Hiểu cái máy bạn đang dùng
Bài 5.4: Cơ bản về Generative AI — Hiểu cái máy bạn đang dùng
Mục tiêu học tập
Mở đầu: Vì sao bạn cần biết "máy chạy thế nào"?
Generative AI là gì?
Định nghĩa ngắn
Phân biệt với các loại AI khác
Vì sao Generative AI khả thi NGAY BÂY GIỜ (không phải 10 năm trước)?
Trụ cột 1: Kiến trúc Transformer (2017)
Trụ cột 2: Dữ liệu khổng lồ
Trụ cột 3: Compute power
LLM học thế nào? — 2 giai đoạn
Pre-training: "Đọc cả Internet"
Fine-tuning: "Học cách làm helpful"
Khái niệm cốt lõi cần nắm
1. Token — đơn vị "từ" của LLM
2. Context window — "bộ nhớ ngắn hạn"
3. Knowledge cutoff — "đi tu trên núi"
4. Hallucination — "nói chắc nhưng sai"
5. Non-determinism — "mỗi lần khác nhau"
6. Emergent capabilities — "biết những thứ chưa được dạy thẳng"
7. Tools / Function calling — "tay chân"
So sánh các loại model — minh họa metric
Vì sao kiến thức này quan trọng cho 4D?
→ Cải thiện Delegation
→ Cải thiện Description
→ Cải thiện Discernment
→ Cải thiện Diligence
Ví dụ theo ngành — Kiến thức kỹ thuật giúp gì
💼 Marketing Analyst
🔍 Research Analyst (Pharma)
💰 Finance Analyst
⚖️ Legal
Anti-patterns
❌ "Model X tốt hơn Model Y, dùng X mọi lúc"
❌ "Tăng temperature lên cho creative hơn"
❌ "Context window 1M nên upload mọi thứ"
❌ "Model bịa = model hỏng"
Mẹo nâng cao
💡 Mẹo 1: Test "knowledge cutoff" của model
💡 Mẹo 2: Theo dõi anthropic.com/news + openai.com/blog
💡 Mẹo 3: Hiểu pricing tier
Áp dụng ngay
Bài tập 1: Tự test capability của AI bạn dùng (15 phút)
Bài tập 2: Reflection (10 phút)
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
5.4 - Cơ bản về Generative AI — Hiểu cái máy bạn đang dùng​
Modified April 20
Bài 5.4: Cơ bản về Generative AI — Hiểu cái máy bạn đang dùng​
Module: Nền tảng kỹ thuật​
Thời gian ước tính: 25 phút​
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
Slide: AI Fluency: Framework & Foundations.pdf​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Định nghĩa Generative AI và phân biệt với các loại AI khác​
•
✅ Giải thích 3 trụ cột công nghệ làm Gen AI khả thi: kiến trúc, dữ liệu, compute​
•
✅ Mô tả cơ chế học của LLM qua 2 giai đoạn: pre-training và fine-tuning​
•
✅ Hiểu khái niệm context window, knowledge cutoff, emergent capability​
•
✅ Sử dụng kiến thức kỹ thuật này để strengthen Delegation và Diligence​
Mở đầu: Vì sao bạn cần biết "máy chạy thế nào"?​
Bạn lái xe nhiều năm có thể không biết động cơ vận hành ra sao. Vẫn lái tốt.​
Nhưng nếu xe bạn bắt đầu phát ra tiếng lạ, đèn báo nháy, hoặc bạn cần quyết định mua xe mới — kiến thức "máy chạy thế nào" đột nhiên có giá. Bạn sẽ:​
•
Hỏi đúng câu hỏi với thợ​
•
Không bị lừa khi sửa​
•
Chọn xe phù hợp nhu cầu thay vì chạy theo quảng cáo​
Với AI cũng vậy. Khóa này có thể dạy bạn AI Fluency mà không cần kỹ thuật. Nhưng có hiểu kỹ thuật căn bản, bạn:​
•
Hiểu vì sao AI đôi khi bịa (hallucination) — không phải nó "lười"​
•
Biết vì sao câu hỏi tương tự có response khác nhau (non-determinism)​
•
Quyết định khi nào model nhỏ đủ vs. cần model lớn (cost vs. quality)​
•
Đánh giá claim của vendor: "context window 1 triệu token!" — quan trọng thế nào?​
Bài này không biến bạn thành ML engineer. Nó là 25 phút "tour động cơ" để bạn lái thông minh hơn.​
Comments (0)
Help Center
Keyboard Shortcuts
