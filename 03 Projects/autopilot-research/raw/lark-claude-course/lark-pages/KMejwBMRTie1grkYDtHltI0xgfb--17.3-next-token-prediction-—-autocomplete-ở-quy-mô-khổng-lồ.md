# 17.3 - Next Token Prediction — Autocomplete ở quy mô khổng lồ

**Source:** https://transform.sg.larksuite.com/wiki/KMejwBMRTie1grkYDtHltI0xgfb
**Wiki ID:** KMejwBMRTie1grkYDtHltI0xgfb
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

17.3 - Next Token Prediction — Autocomplete ở quy mô khổng lồ

Last updated: Apr 20

Log In or Sign Up
17.3 - Next Token Prediction — Autocomplete ở quy mô khổng lồ
Bài 17.3: Next Token Prediction — Autocomplete ở quy mô khổng lồ
Mục tiêu học tập
Mở đầu: Một câu chuyện hallucination đã đi vào lịch sử
Next Token Prediction là gì?
Tại sao phân biệt này quan trọng?
Next Token Prediction Continuum
Ví dụ cụ thể: Cùng model, 3 vị trí khác nhau
Tính năng nào đang "push edge out"?
1. Citations & source grounding
2. Uncertainty signaling
3. Constrained generation / Skills
4. Generator-verifier pattern
Các thói quen bạn tự xây (4 quy tắc vàng)
Quy tắc 1: Confident tone ≠ accuracy signal
Quy tắc 2: Specificity là nơi fabrication tập trung
Quy tắc 3: Treat outputs as drafts to verify
Quy tắc 4: Model không thể tự distinguish grounded vs invented
Ví dụ theo ngành
⚖️ Legal Counsel — Bài học Schwartz, áp dụng hàng ngày
🔍 Research Analyst — Xây generator-verifier cho literature review
💰 Finance Analyst — Xây habit cho numerical specifics
📝 Content Marketer — Well-worn vs novel trong content creation
🏥 Clinical Research Coordinator — Confidence calibration trong drug info
Anti-patterns
❌ "Tone tự tin = chắc chắn đúng"
❌ "Hỏi AI 'bạn có chắc không?' làm verification"
❌ "AI đã nâng cấp, chắc bớt hallucination rồi"
❌ "Citation có format đẹp = citation thật"
❌ "Probe 1 lần thấy OK → dùng cho mọi task tương tự"
Mẹo nâng cao
Mẹo 1: "Specificity threshold" cá nhân
Mẹo 2: Dùng "likelihood of fabrication" trước khi prompt
Mẹo 3: "Placeholder pattern" cho draft
Mẹo 4: "Inversion test" cho claims
Áp dụng ngay
Bài tập 1: The Verification Test (~25 phút)
Bài tập 2: Specificity Threshold Worksheet
Suy ngẫm bài học
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
17.3 - Next Token Prediction — Autocomplete ở quy mô khổng lồ​
Modified April 20
Bài 17.3: Next Token Prediction — Autocomplete ở quy mô khổng lồ​
Module: Bốn thuộc tính cốt lõi (1/4)​
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
✅ Giải thích Next Token Prediction là cơ chế cốt lõi của generative AI và tại sao nó tạo ra cả fluency lẫn hallucination​
•
✅ Định vị task trên Next Token Prediction continuum — well-worn path vs novel territory​
•
✅ Nhận diện specificity (tên, ngày, citation, thống kê) là vùng bịa đặt tập trung nhiều nhất​
•
✅ Nhận ra các tính năng sản phẩm (citations, uncertainty signaling, constrained generation, generator-verifier pattern) là biện pháp khắc phục giới hạn này​
•
✅ Xây habit verify dựa trên vị trí task trên continuum, không dựa trên tone tự tin của AI​
Mở đầu: Một câu chuyện hallucination đã đi vào lịch sử​
Đầu năm 2023. Steven Schwartz, một luật sư ở New York với hơn 30 năm kinh nghiệm, nộp một brief pháp lý lên tòa án liên bang (vụ Mata v. Avianca). Trong brief, ông trích dẫn nhiều vụ án tiền lệ để ủng hộ lập luận của mình. Tất cả nghe rất chuyên nghiệp:​
•
"Varghese v. China Southern Airlines Co., Ltd." (11th Cir. 2019)​
•
"Shaboon v. EgyptAir" (11th Cir. 2013)​
•
"Petersen v. Iran Air" (D.D.C. 2013)​
•
"Martinez v. Delta Airlines" (11th Cir. 2019)​
•
... và vài vụ nữa.​
Đối phương kiểm tra. Phần lớn các vụ án được cite đều không tồn tại.​
Tên tác giả, trích đoạn, số trang — tất cả đều do ChatGPT sinh ra. Luật sư không biết. Ông đã dùng ChatGPT làm "công cụ nghiên cứu" và tin rằng đó là cơ sở dữ liệu pháp lý. Ông không verify.​
Tháng 6/2023, tòa phạt ông và luật sư cộng sự + firm tổng $5,000. Ngành luật toàn cầu shock. Bài báo New York Times viết: "The ChatGPT Lawyer Explains Himself".​
Comments (0)
Help Center
Keyboard Shortcuts
