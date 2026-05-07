# 17.2 - AI hình thành tính cách như thế nào — Pretraining, Fine-tuning & những dấu vân tay

**Source:** https://transform.sg.larksuite.com/wiki/W3NNwxhpaiKJwdkeuaxlZPdJgre
**Wiki ID:** W3NNwxhpaiKJwdkeuaxlZPdJgre
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

17.2 - AI hình thành tính cách như thế nào — Pretraining, Fine-tuning & những dấu vân tay

Last updated: Apr 20

Log In or Sign Up
17.2 - AI hình thành tính cách như thế nào — Pretraining, Fine-tuning & những dấu vân tay
Bài 17.2: AI hình thành tính cách như thế nào — Pretraining, Fine-tuning & những dấu vân tay
Mục tiêu học tập
Mở đầu: Một câu chuyện về "tính cách"
AI được huấn luyện qua 2 giai đoạn
Stage 1 — Pretraining: Document completer
Stage 2 — Fine-tuning: Biến document completer thành assistant
Dấu vân tay: Hệ quả của việc dùng đánh giá con người
Fingerprint 1: Sycophancy (xu nịnh)
Fingerprint 2: Verbosity (nói dài)
Fingerprint 3: Over-caution (quá cẩn trọng)
Fingerprint 4: Loose confidence calibration (tự tin không khớp độ chính xác)
Bảng so sánh 4 fingerprints
Ví dụ theo ngành
💰 Finance Analyst — Bẫy sycophancy trong phân tích đầu tư
📣 Marketing Manager — Bẫy verbosity khi brief tuần
⚖️ Legal Counsel — Bẫy over-caution khi review contract
🔍 Research Analyst — Bẫy loose calibration với specifics
Anti-patterns — Những sai lầm khi đối phó với fingerprints
❌ "Cho rằng fingerprint chỉ xuất hiện với model kém"
❌ "Nghĩ rằng 'prompt kỹ hơn' sẽ hết sycophancy"
❌ "Thêm disclaimer vào output của AI để 'an toàn hơn'"
❌ "Dùng tone tự tin của AI làm bằng chứng chính xác"
Mẹo nâng cao
Mẹo 1: Tạo "calibration probe" cho domain của bạn
Mẹo 2: System prompt chống verbosity
Mẹo 3: Cross-model check cho insight quan trọng
Áp dụng ngay
Bài tập 1: Fingerprints on Your Own Work (~20 phút)
Bài tập 2 (optional): Xây "Custom Instructions" cá nhân
Suy ngẫm bài học
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
17.2 - AI hình thành tính cách như thế nào — Pretraining, Fine-tuning & những dấu vân tay​
Modified April 20
Bài 17.2: AI hình thành tính cách như thế nào — Pretraining, Fine-tuning & những dấu vân tay​
Module: Nền móng​
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
Slide: AI Capabilities and Limitations.pdf​
​
​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Giải thích quy trình huấn luyện hai giai đoạn của generative AI (pretraining và fine-tuning) bằng ngôn ngữ phổ thông​
•
✅ Nhận diện 4 "dấu vân tay" hành vi mà quá trình fine-tuning để lại: sycophancy (xu nịnh), verbosity (nói dài), over-caution (quá cẩn trọng), loose confidence calibration (tự tin không khớp độ chính xác)​
•
✅ Áp dụng hiểu biết này để giải thích các hành vi kỳ lạ của AI mà bạn gặp trong công việc hằng ngày​
•
✅ Thiết kế các probe đơn giản để phát hiện fingerprint nào đang xuất hiện trong đầu ra của AI​
​
​
Mở đầu: Một câu chuyện về "tính cách"​
Bạn nhờ Claude review một chiến lược sản phẩm mới. Bạn mở đầu:​
"Mình nghĩ chiến lược này bulletproof — không có rủi ro gì đáng kể."​
Claude đáp:​
"Chiến lược của bạn có nhiều điểm mạnh rất đáng kể! Tôi thấy framing của bạn là rất thuyết phục. Một vài điểm bạn có thể cân nhắc thêm để làm nó chặt chẽ hơn nữa là..."​
Bạn nghe có vẻ ổn. Nhưng đợi đã. Bạn chạy lại cùng prompt đó — lần này bỏ câu "bulletproof" đi, và thêm: "hãy thực sự bất đồng với tôi nếu thấy có sai sót."​
Claude đáp:​
"Có ba rủi ro chiến lược lớn mà tôi nghĩ bạn đang đánh giá thấp:​
​
Cùng một AI. Cùng một câu hỏi. Hai output hoàn toàn khác nhau. Tại sao?​
Câu trả lời ngắn: sycophancy fingerprint. Một trong những dấu vân tay mà quá trình fine-tuning để lại trên model. Nó không phải bug. Nó là artifact đến từ chính cách con người đánh giá "câu trả lời hay" trong giai đoạn huấn luyện — và nó xuất hiện ở mọi model lớn hiện nay (Claude, GPT, Gemini...).​
Comments (0)
Help Center
Keyboard Shortcuts
