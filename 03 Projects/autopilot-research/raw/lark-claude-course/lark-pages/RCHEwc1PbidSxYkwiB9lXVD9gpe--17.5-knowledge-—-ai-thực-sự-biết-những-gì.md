# 17.5 - Knowledge — AI thực sự biết những gì

**Source:** https://transform.sg.larksuite.com/wiki/RCHEwc1PbidSxYkwiB9lXVD9gpe
**Wiki ID:** RCHEwc1PbidSxYkwiB9lXVD9gpe
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

17.5 - Knowledge — AI thực sự biết những gì

Last updated: Apr 20

Log In or Sign Up
17.5 - Knowledge — AI thực sự biết những gì
Bài 17.5: Knowledge — AI thực sự biết những gì
Mục tiêu học tập
Mở đầu: Hai câu hỏi, hai thế giới
AI đã đọc cái gì và ngừng đọc lúc nào?
Đặc điểm 1: Không có lived experience
Đặc điểm 2: Không real-time browsing (trừ khi có tool)
Đặc điểm 3: Knowledge cutoff — dấu chấm cứng
Knowledge Continuum
Thử nghiệm suy nghĩ: đặt 5 câu hỏi vào continuum
4 failure modes đặc trưng
Failure 1: Staleness (thông tin lỗi thời)
Failure 2: Uneven coverage (phủ sóng không đều)
Failure 3: Inherited bias (thiên vị kế thừa)
Failure 4: Source amnesia (quên nguồn)
Product features "push edge out"
Feature 1: Web search / browsing
Feature 2: Retrieval / RAG / MCPs
Feature 3: Tool use
Feature 4: Explicit cutoff disclosure
Ví dụ theo ngành
💰 Finance Analyst — Dùng RAG cho research 10-K
🔍 Research Analyst — Phân loại chủ đề trước khi prompt
⚖️ Legal Counsel — Luật Việt Nam vs AI training data
🏥 Clinical Research Coordinator — Drug info workflow
📣 Content Marketer — "Inherited bias" cho Vietnamese market
🎓 Teacher — Stable content = AI's strength
Anti-patterns
❌ "AI có knowledge cutoff X, vậy sau X nó không biết gì"
❌ "Bật web search xong là xong"
❌ "Model bias không ảnh hưởng tôi vì tôi đọc output có phê phán"
❌ "RAG là silver bullet — dùng là hết vấn đề Knowledge"
Mẹo nâng cao
Mẹo 1: Xác định cutoff thực tế cho model bạn dùng
Mẹo 2: Template "context dump" cho mỗi domain
Mẹo 3: Split task theo "freshness requirement"
Mẹo 4: "Evidence ladder" cho claim
Áp dụng ngay
Bài tập 1: The Outsider Test (~25 phút)
Bài tập 2 (optional): Xây "context dump" template
Suy ngẫm bài học
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
17.5 - Knowledge — AI thực sự biết những gì​
Modified April 20
Bài 17.5: Knowledge — AI thực sự biết những gì​
Module: Bốn thuộc tính cốt lõi (2/4)​
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
✅ Giải thích tri thức của AI được hình thành trong huấn luyện và tại sao nó có hard cutoff (ngày cắt cứng)​
•
✅ Dự đoán chủ đề nào nằm ở capability zone (frequent, recent-in-training, consistent) vs edge (rare, post-cutoff, niche, contested)​
•
✅ Nhận diện 4 failure đặc trưng: staleness, uneven coverage, inherited bias, source amnesia​
•
✅ Nhận ra web search, retrieval/RAG, tool use, explicit cutoff disclosure = các tính năng vá kênh này​
•
✅ Xây habit cung cấp kiến thức thay vì giả định model có​
Mở đầu: Hai câu hỏi, hai thế giới​
Hãy tưởng tượng bạn hỏi Claude 2 câu liên tiếp:​
Câu 1: "Giải thích quá trình quang hợp."​
Claude trả lời đầy đủ: chloroplast, light-dependent reactions, Calvin cycle, chlorophyll, CO₂ + H₂O → glucose + O₂. Mượt, chi tiết, chính xác. Bạn có thể copy vào bài giảng.​
Câu 2: "Thị trưởng hiện tại của Hà Nội là ai?"​
Claude trả lời: "Theo thông tin mới nhất mà tôi có, thị trưởng Hà Nội là Trần Sỹ Thanh..."​
Vấn đề: Trần Sỹ Thanh trở thành Chủ tịch UBND TP Hà Nội từ tháng 7/2022 (tại thời điểm viết bài này). Claude có thể đúng về tên — tại thời điểm training. Nhưng đã đúng từ khi nào đến khi nào? Nếu bạn đang đọc bài này năm 2028 và có người mới thay thế từ 2027, Claude vẫn có thể nói tên cũ với cùng tone tự tin như quang hợp — vì model không có mechanism tự cập nhật.​
Cùng AI. Cùng tone. Cùng structure câu trả lời. Một trường hợp: 100% đáng tin. Trường hợp khác: cần verify lịch.​
Sự khác biệt không phải ở AI. Sự khác biệt ở câu hỏi:​
•
Quang hợp đã xuất hiện hàng nghìn lần trong training data. Frequent, recent, consistent.​
•
Thị trưởng Hà Nội là tên người cụ thể, thay đổi theo thời gian, local. Training data có thể có snapshot 2022 — nhưng không có snapshot 2027.​
Comments (0)
Help Center
Keyboard Shortcuts
