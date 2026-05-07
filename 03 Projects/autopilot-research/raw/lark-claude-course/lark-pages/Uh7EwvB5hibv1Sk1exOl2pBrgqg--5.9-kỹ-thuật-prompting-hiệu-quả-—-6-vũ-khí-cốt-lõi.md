# 5.9 - Kỹ thuật prompting hiệu quả — 6 vũ khí cốt lõi

**Source:** https://transform.sg.larksuite.com/wiki/Uh7EwvB5hibv1Sk1exOl2pBrgqg
**Wiki ID:** Uh7EwvB5hibv1Sk1exOl2pBrgqg
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

5.9 - Kỹ thuật prompting hiệu quả — 6 vũ khí cốt lõi

Last updated: Apr 20

Log In or Sign Up
5.9 - Kỹ thuật prompting hiệu quả — 6 vũ khí cốt lõi
Bài 5.9: Kỹ thuật prompting hiệu quả — 6 vũ khí cốt lõi
Mục tiêu học tập
Mở đầu: Prompt engineering là chuyện nhỏ hay chuyện lớn?
6 kỹ thuật cốt lõi
Kỹ thuật 1 — Give Context
Nguyên tắc
Cách làm
Ví dụ
Khi nào kỹ thuật này crucial
Kỹ thuật 2 — Show Examples (Few-Shot)
Nguyên tắc
Cách làm
Ví dụ
Khi nào kỹ thuật này crucial
Kỹ thuật 3 — Specify Constraints
Nguyên tắc
Cách làm
Ví dụ
Khi nào kỹ thuật này crucial
Kỹ thuật 4 — Break Complex Tasks into Steps
Nguyên tắc
Cách làm
Khi nào kỹ thuật này crucial
Kỹ thuật 5 — Ask AI to Think First
Nguyên tắc
Cách làm
Ví dụ
Khi nào kỹ thuật này crucial
Kỹ thuật 6 — Define Role / Tone
Nguyên tắc
Cách làm
Ví dụ
Khi nào kỹ thuật này crucial
Tích hợp 6 kỹ thuật — Prompt mẫu hoàn chỉnh
"Vũ khí bí mật": Ask AI to improve YOUR prompt
Pattern thành công thường gặp
Troubleshooting — Khi prompt không work
Issue 1: Output generic
Issue 2: Output quá dài / quá ngắn
Issue 3: Wrong tone
Issue 4: Miss step
Issue 5: Reasoning sai
Issue 6: Output đúng format nhưng nội dung lệch
General troubleshooting workflow
Mối liên hệ với Description (Bài 5.8)
Áp dụng ngay
Bài tập 1: Prompt makeover marathon (15 phút)
Bài tập 2: Build template library (15 phút)
Bài tập 3: Meta-prompt (5 phút)
Anti-patterns
❌ Áp 6 kỹ thuật cho mọi prompt
5.9 - Kỹ thuật prompting hiệu quả — 6 vũ khí cốt lõi​
Modified April 20
Bài 5.9: Kỹ thuật prompting hiệu quả — 6 vũ khí cốt lõi​
Module: 4 năng lực cốt lõi (D2 — applied)​
Thời gian ước tính: 35 phút​
Mức độ: Trung cấp → Nâng cao​
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
✅ Hiểu prompt engineering là gì và tại sao nó là kỹ năng nền tảng​
•
✅ Áp dụng 6 kỹ thuật prompting cốt lõi: context, examples, constraints, steps, think-first, role/tone​
•
✅ Áp dụng "secret weapon": dùng AI để improve prompt của chính bạn​
•
✅ Troubleshoot khi prompt không cho output mong muốn​
•
✅ Có 1 thư viện prompt template cá nhân để áp dụng cho task lặp​
Mở đầu: Prompt engineering là chuyện nhỏ hay chuyện lớn?​
Có hai trường phái:​
Trường phái A — "Prompt engineering sẽ chết":"Model tương lai đủ thông minh để hiểu intent từ vài từ. Bạn không cần học prompt nữa."​
Trường phái B — "Prompt engineering quan trọng forever":"Cùng một model, người fluent vs. người mới có output khác hẳn. Đây là kỹ năng meta."​
Sự thật ở giữa, nghiêng về B.​
Đúng — model mới (Claude 4.x, GPT-5) đã tha thứ hơn cho prompt sơ sài. Nhưng gap giữa output baseline và output xuất sắc vẫn rất lớn — và gap đó được close bởi prompting kỹ thuật.​
Hơn nữa: ngay cả khi model tự suy được intent, biết mô tả rõ vẫn giúp bạn:​
•
Suy nghĩ rõ hơn về mình muốn gì (forcing function)​
•
Reproducible — prompt tốt có thể template, share team​
•
Production-ready — automation cần prompt deterministic​
Prompt engineering = kỹ năng giao tiếp, không phải mánh kỹ thuật. Nó không lỗi thời.​
6 kỹ thuật cốt lõi​
Comments (1)
Go to the first comment
Help Center
Keyboard Shortcuts
