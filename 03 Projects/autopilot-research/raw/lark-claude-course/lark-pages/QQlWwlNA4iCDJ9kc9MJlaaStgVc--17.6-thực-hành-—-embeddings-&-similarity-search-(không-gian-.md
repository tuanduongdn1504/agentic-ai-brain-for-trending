# 17.6 - Thực hành — Embeddings & Similarity Search (Không gian ngữ nghĩa 1024 chiều)

**Source:** https://transform.sg.larksuite.com/wiki/QQlWwlNA4iCDJ9kc9MJlaaStgVc
**Wiki ID:** QQlWwlNA4iCDJ9kc9MJlaaStgVc
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

17.6 - Thực hành — Embeddings & Similarity Search (Không gian ngữ nghĩa 1024 chiều)

Last updated: Apr 20

Log In or Sign Up
17.6 - Thực hành — Embeddings & Similarity Search (Không gian ngữ nghĩa 1024 chiều)
Bài 17.6: Thực hành — Embeddings & Similarity Search (Không gian ngữ nghĩa 1024 chiều)
Mục tiêu học tập
Mở đầu: Vấn đề kinh điển của tìm kiếm
Phần 1: 2D encoding — bắt đầu đơn giản
Retrieval — Tìm kiếm trong không gian
Phần 2: Thêm trục — nhưng 2 không đủ
Thí nghiệm: thêm trục 4
Real embeddings: hàng trăm đến vài nghìn dimensions
Phần 3: Unlabeled axes (trục không tên)
Hệ quả:
Nhưng Practice vẫn work
Phần 4: Cosine similarity
Cosine similarity là gì?
Tại sao cosine thay vì Euclidean distance?
Ví dụ cụ thể
Phần 5: Putting it all together — RAG
Tại sao RAG quan trọng?
Giới hạn của RAG
Ví dụ theo ngành
💰 Finance Analyst — RAG trên 10-K library
⚖️ Legal Counsel — Case law search
🔍 Research Analyst — Literature database
🎧 Customer Support — Knowledge base search
🛠️ Product Manager — User research synthesis
Anti-patterns khi dùng embeddings
❌ "Embedding tốt = RAG tốt"
❌ "Cosine similarity cao = nội dung trả lời đúng"
❌ "Embed tất cả, retrieve tất cả"
❌ "Embedding model nào cũng như nào"
Mẹo nâng cao
Mẹo 1: Chunking strategy per domain
Mẹo 2: Hybrid search pattern
Mẹo 3: Grounding prompt pattern
Mẹo 4: Embed your metadata, not just content
Áp dụng ngay
Bài tập 1: Mental embedding exercise (~10 phút)
Bài tập 2: Dùng embedding tool thực tế (~15 phút)
Bài tập 3: Setup RAG cho domain của bạn (stretch)
Suy ngẫm bài học
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
17.6 - Thực hành — Embeddings & Similarity Search (Không gian ngữ nghĩa 1024 chiều)​
Modified April 20
Bài 17.6: Thực hành — Embeddings & Similarity Search (Không gian ngữ nghĩa 1024 chiều)​
Module: Bốn thuộc tính cốt lõi (2/4 — thực hành)​
Thời gian ước tính: 25 phút​
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
✅ Giải thích vấn đề của string-matching search và tại sao meaning-as-a-place thay đổi mọi thứ​
•
✅ Visualize cách một đoạn text biến thành vector trong không gian 1024 chiều​
•
✅ Áp dụng similarity search để tìm thông tin liên quan ngữ nghĩa (không phải từ khóa)​
•
✅ Hiểu tại sao RAG (Retrieval-Augmented Generation) hoạt động — và giới hạn của nó​
•
✅ Thực hành đặt câu hỏi và dự đoán kết quả similarity trong không gian 2D/3D​
Mở đầu: Vấn đề kinh điển của tìm kiếm​
Bạn search "xe ô tô" trong tài liệu công ty. Kết quả:​
•
✅ "Chính sách sử dụng xe ô tô công ty" ← có chứa "xe ô tô"​
•
✅ "Báo cáo chi phí xe ô tô Q3" ← có chứa "xe ô tô"​
•
❌ "Tiêu chuẩn phương tiện giao thông" ← không chứa "xe ô tô", bị bỏ qua​
•
❌ "Quy định về sử dụng xe 4 bánh" ← không chứa "xe ô tô", bị bỏ qua​
•
❌ "My Civic needs new brakes" ← "Civic" là xe ô tô, nhưng string không match​
Trong hàng chục năm, đây là search — return results dựa trên string similarity, không phải meaning.​
Google đã improve dần với kỹ thuật:​
•
Synonym dictionaries: map "xe ô tô" ↔ "ô tô" ↔ "automobile"​
•
Stemming: "running" → "run", "cars" → "car"​
•
Click-pattern mining: "NYC apartments" và "Manhattan rentals" → same results​
Nhưng mỗi liên kết phải được map thủ công. Không thể scale cho mọi concept.​
Comments (0)
Help Center
Keyboard Shortcuts
