# 1.2 Prompt Library & Demo Scripts

**Source:** https://transform.sg.larksuite.com/wiki/II1Dw3ap8i5IsikC9K2lxl0WgXf
**Wiki ID:** II1Dw3ap8i5IsikC9K2lxl0WgXf
**Archived:** 2026-05-07

---

Lark Docs
C
Claude Course 2026
Public access
Table of contents
Khoá học Claude toàn diện tiếng Việt
Lộ trình học tập.pdf
25 tập khám phá Claude AI
Lộ trình tự học 5 buổi × 2 tiếng
Buổi 1. Hiểu cỗ máy và khung tư duy 4D
Slide: Hiểu cỗ máy và khung tư duy 4D .pdf
1.1 Giáo án giảng viên
1.2 Prompt Library & Demo Scripts
1.3 Handouts học viên
1.4 Workbook học viên
1.5 Lịch sử Công ty TechViet Corporation
1.6 Checklist chuẩn bị đầy đủ cho giảng viên
Buổi 2. Prompting Mastery — Vòng lặp Description ↔ Discernment
Buổi 3. Projects & Artifacts — Không gian làm việc chuyên dụng
Buổi 4. Skills & Research — Đóng gói quy trình + Đào sâu đa nguồn
Buổi 5. Cowork & Automation
🔥
Recap 5 buổi học Claude AI online
Anthropic courses
📣
Bổ sung course
Transform Group

1.2 Prompt Library & Demo Scripts

Last updated: Apr 20

Log In or Sign Up
1.2 Prompt Library & Demo Scripts
Demo 1: Hallucination (NTP)
🎯 Mục tiêu demo
⏱ Thời gian
🛠 Setup
📝 Prompt chính
🎬 Kịch bản diễn đạt
🔄 Fallback prompts
📚 Tài liệu tham khảo khi học viên hỏi
Demo 2: Knowledge cutoff
🎯 Mục tiêu demo
⏱ Thời gian
🛠 Setup
📝 Prompts
🎬 Kịch bản diễn đạt
🔄 Fallback
Demo 3: Working Memory — Lost in middle
🎯 Mục tiêu demo
⏱ Thời gian
🛠 Setup
📝 File content template
📝 Prompts
🎬 Kịch bản diễn đạt
🔄 Fallback
Demo 4: Steerability — Letter vs Spirit
🎯 Mục tiêu demo
⏱ Thời gian
🛠 Setup
📝 3 Prompts chạy liên tiếp
🎬 Kịch bản diễn đạt
🔄 Fallback
File cần chuẩn bị trước
✅ File 1: long-document-demo.md
✅ File 2: Slide deck Buổi 1
✅ File 3: Backup videos
Backup prompts nếu demo fail
Trường hợp Claude rate limit / API error
Trường hợp học viên hỏi câu quá sâu
Checklist trước demo
Script đóng mỗi demo
1.2 Prompt Library & Demo Scripts​
Modified April 20
​
Mục đích: Tất cả prompt, demo file, và copy-paste material cần dùng trong Buổi 1. ​
Cách dùng: Giảng viên mở file này song song với slide deck. Mỗi demo có: setup, prompt, expected output, fallback script.​
​
Demo 1: Hallucination (NTP)​
🎯 Mục tiêu demo​
Cho học viên thấy AI bịa citation/specifics với tone tự tin 100%, không thể phân biệt từ output.​
⏱ Thời gian​
4 phút​
🛠 Setup​
•
Trình duyệt: Mở tab mới Claude.ai​
•
Chat mode: New chat​
•
Web search: TẮT (quan trọng — nếu bật, Claude có thể search và không bịa)​
•
Model: Claude Opus (hoặc bất kỳ, miễn là web search tắt)​
•
Chuẩn bị: Tab phụ Google/Google Scholar để verify citation​
📝 Prompt chính​
​
Code block​
Plain Text
Copy
Cite 3 academic papers từ 2023-2024 về "AI literacy training ​
programs in Vietnamese healthcare sector". ​
​
For each paper, include:​
- Full author names​
- Year​
- Journal name​
- DOI or URL​
- 2-sentence abstract​
​
Format as a numbered list.​
​
🎬 Kịch bản diễn đạt​
Trước khi submit:​
​
"Tôi sắp ask Claude cite 3 paper về chủ đề rất niche — AI literacy training trong ngành y tế Việt Nam 2023-2024. Topic đủ niche để Knowledge mỏng, và đủ cụ thể (tên tác giả, DOI, journal) để trigger NTP hallucination. Watch carefully."​
​
Sau khi có output:​
​
"OK các bạn nhìn output này. Format rất chuyên nghiệp. Tác giả Việt Nam (Nguyễn, Trần...). Journal có format chuẩn (Vietnam Journal of..., International Journal of...). DOI đầy đủ. Nếu tôi paste cái này vào báo cáo, các bạn sẽ tin không?​
[Chờ 3 giây]​
Chúng ta cùng verify LIVE. Copy DOI paper 1 — paste Google."​
​
Comments (0)
Help Center
Keyboard Shortcuts
