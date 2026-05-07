# 5.8 - Cận cảnh Description — Truyền đạt rõ ràng với AI

**Source:** https://transform.sg.larksuite.com/wiki/QcVJw1IY0iEkUSkjo1OluePWgDh
**Wiki ID:** QcVJw1IY0iEkUSkjo1OluePWgDh
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

5.8 - Cận cảnh Description — Truyền đạt rõ ràng với AI

Last updated: Apr 20

Log In or Sign Up
5.8 - Cận cảnh Description — Truyền đạt rõ ràng với AI
Bài 5.8: Cận cảnh Description — Truyền đạt rõ ràng với AI
Mục tiêu học tập
Mở đầu: Sự khác biệt giữa "ăn tối" và "công thức"
Description là gì?
"AI không đọc được tâm trí"
3 loại Description
Loại 1 — Product Description
Loại 2 — Process Description
Loại 3 — Performance Description
Cách 3 loại tương tác trong 1 prompt
Trước/sau: Bad Prompt → Good Prompt
Ví dụ 1 — Email khách hàng
Ví dụ 2 — Code review
Ví dụ 3 — Research synthesis
Ví dụ theo ngành
💼 Sales — Account research
📣 Marketing — Campaign brief
💰 Finance — Quarterly variance analysis
🏥 Clinical — Document drafting (Gaia-style)
Anti-patterns
❌ "AI sẽ figure out"
❌ Wall of text Description
❌ Chỉ Product, bỏ Process + Performance
❌ Conflicting instructions
❌ Assume "model mới sẽ tự handle"
Mẹo nâng cao
💡 Mẹo 1: Build "prompt template" cho task lặp lại
💡 Mẹo 2: Ask AI improve prompt của bạn
💡 Mẹo 3: Reference example > describe abstractly
💡 Mẹo 4: Performance Description thay đổi với conversation length
💡 Mẹo 5: Test "describe to a new colleague"
Áp dụng ngay
Bài tập 1: Bad Prompt Makeover (15 phút)
Bài tập 2: Refine 1 prompt từ project cá nhân (10 phút)
Bài tập 3: Reflection (5 phút)
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
5.8 - Cận cảnh Description — Truyền đạt rõ ràng với AI​
Modified April 20
Bài 5.8: Cận cảnh Description — Truyền đạt rõ ràng với AI​
Module: 4 năng lực cốt lõi (D2)​
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
Slide: AI Fluency: Framework & Foundations.pdf​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Giải thích Description không chỉ là "viết prompt tốt"​
•
✅ Phân biệt 3 loại Description: Product, Process, Performance​
•
✅ Áp dụng cả 3 loại vào prompt của mình một cách có hệ thống​
•
✅ Nhận diện vì sao "AI không đọc được tâm trí" và làm sao bù đắp​
•
✅ Làm bài tập "Bad Prompt Makeover" nâng skill thực tiễn​
Mở đầu: Sự khác biệt giữa "ăn tối" và "công thức"​
Bạn nhờ một người bạn nấu cho bạn ăn tối. Bạn có 2 cách:​
Cách 1: "Nấu cho mình ăn tối nhé!"​
Bạn nhận: có thể là gì? Bún bò? Pizza? Salad? Có thể bạn dị ứng món họ chọn. Có thể bạn không thích vị họ nấu. Có thể họ nấu món cầu kỳ trong khi bạn đang vội ăn nhanh.​
Cách 2: "Mình muốn bữa tối nhẹ — phải có protein, không gluten, ăn trước 7h vì có meeting. Có 30 phút nấu thôi. Mình thích vị Việt — phở chay hoặc gà luộc với rau luộc okay. Còn nguyên liệu trong tủ lạnh đây."​
Bạn nhận: bữa tối đúng ý.​
Cả hai trường hợp, "người bạn" có cùng năng lực. Sự khác biệt là bạn đã mô tả hay chưa.​
AI cũng thế. Nó không đọc tâm trí. Nó pattern-match dựa trên những gì bạn nói. Nói ít → AI fill blank bằng generic. Nói rõ → AI đáp ứng đúng.​
Đây là Description.​
Description là gì?​
Description là năng lực truyền đạt rõ ràng và có chủ đích với AI — không chỉ "viết prompt", mà xây dựng môi trường cộng tác nơi cả bạn và AI đều có thể làm việc tốt nhất.​
Comments (0)
Help Center
Keyboard Shortcuts
