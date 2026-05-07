# 17.1 - AI ở đây là gì — Vẽ ranh giới của "generative AI"

**Source:** https://transform.sg.larksuite.com/wiki/IYacw26Zvi0udtkhmLulA1aigFf
**Wiki ID:** IYacw26Zvi0udtkhmLulA1aigFf
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

17.1 - AI ở đây là gì — Vẽ ranh giới của "generative AI"

Last updated: Apr 20

Log In or Sign Up
17.1 - AI ở đây là gì — Vẽ ranh giới của "generative AI"
Bài 17.1: AI ở đây là gì — Vẽ ranh giới của "generative AI"
Mục tiêu học tập
Mở đầu: Một ngày của bạn với "AI"
Phân loại AI: 2 họ lớn
Họ 1: Classification / Prediction AI (AI phân loại & dự đoán)
Họ 2: Generative AI (AI tạo sinh)
Bảng so sánh nhanh
Sinh ra từ đâu: Hai giai đoạn huấn luyện
Generative AI ở cốt lõi là một hệ thống dự đoán
4 thuộc tính: Xem trước
🔮 Next Token Prediction — Câu trả lời từ đâu ra?
🌐 Knowledge — AI thực sự biết gì?
🧠 Working Memory — AI đang chú ý gì?
🎚️ Steerability — Bạn kiểm soát được đến đâu?
Calibrated trust: Cái duy nhất bạn cần mang theo khóa này
Ví dụ theo ngành: 5 task ở 5 vị trí khác nhau trên continuum
💼 Sales Manager — Viết email "xin lỗi" theo template công ty
💰 Finance Analyst — Kiểm tra số liệu doanh thu Q3 2025 của một startup Việt Nam
🔍 Research Analyst — Tìm 3 paper gần đây về "cognitive bias in algorithmic trading"
⚖️ Legal Counsel — Review 50-page contract
🎓 Teacher — Giải thích khái niệm quang hợp cho học sinh lớp 6
Anti-patterns — Những hiểu lầm cần tránh
❌ Anti-pattern 1: "AI đã giỏi, mình không cần biết nó hoạt động thế nào"
❌ Anti-pattern 2: "AI luôn đúng" hoặc "AI luôn sai"
❌ Anti-pattern 3: "Coi chatbot và photo tagger là cùng một thứ"
❌ Anti-pattern 4: "Dùng AI = chỉ prompt giỏi"
Áp dụng ngay
Bài tập 1: Generative or Not? (~15 phút)
Bài tập 2 (optional): Tìm classification AI "đội lốt" generative
Suy ngẫm bài học
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
17.1 - AI ở đây là gì — Vẽ ranh giới của "generative AI"​
Modified April 20
Bài 17.1: AI ở đây là gì — Vẽ ranh giới của "generative AI"​
Module: Nền móng​
Thời gian ước tính: 20 phút​
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
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Phân biệt generative AI với các loại AI phân loại/dự đoán mà bạn gặp hàng ngày​
•
✅ Hiểu rằng các thuộc tính của generative AI tồn tại trên một continuum từ năng lực sang giới hạn​
•
✅ Xem trước 4 thuộc tính cốt lõi sẽ đào sâu trong các bài sau: Next Token Prediction, Knowledge, Working Memory, Steerability​
•
✅ Giải thích khái niệm "calibrated trust" (niềm tin được hiệu chỉnh) và tại sao nó khác với "trust / distrust wholesale"​
Mở đầu: Một ngày của bạn với "AI"​
Hãy dừng lại 30 giây và nghĩ về hôm nay — kể từ lúc bạn mở mắt đến giờ, bạn đã chạm vào bao nhiêu "AI"?​
•
Mở điện thoại: Face ID nhận khuôn mặt bạn (AI nhận dạng).​
•
Mở Gmail: spam filter đã lọc 23 email rác qua đêm (AI phân loại).​
•
Mở Maps: app gợi ý tuyến đường tránh kẹt xe (AI dự đoán).​
•
Mở YouTube trong lúc uống cà phê: thuật toán gợi ý đặt video gì vào feed bạn (AI xếp hạng).​
•
Lướt Instagram: photo tagging đã nhận mặt bạn bè trong ảnh (AI phân loại).​
•
Spotify morning playlist: recommendation engine biết bạn thích jazz vào sáng thứ Bảy (AI xếp hạng).​
•
Mở điện thoại gõ tin nhắn: autocomplete gợi ý từ tiếp theo (AI... kiểu này).​
•
Đến văn phòng, mở Claude, gõ "Giúp tôi draft email cho sếp về vụ trễ deadline": đây mới là cái khóa học này nói đến.​
6 trong 8 ví dụ trên là AI — nhưng không phải loại AI mà chúng ta sẽ học. Chúng sort, rank, classify, predict (sắp xếp, xếp hạng, phân loại, dự đoán). Chúng chạy ngầm 24/7 trong cuộc sống của bạn và cực kỳ hữu ích. Nhưng không cái nào trong số chúng sinh ra nội dung mới.​
Cái mới nổi lên vài năm qua — và là đối tượng của khóa học này — là generative AI: hệ thống sinh ra nội dung mới (văn bản, hình ảnh, code, audio) thay vì phân loại nội dung đã có.​
Comments (0)
Help Center
Keyboard Shortcuts
