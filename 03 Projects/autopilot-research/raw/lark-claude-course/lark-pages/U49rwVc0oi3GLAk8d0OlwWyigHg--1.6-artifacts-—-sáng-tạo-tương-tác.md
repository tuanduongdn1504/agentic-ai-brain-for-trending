# 1.6 - Artifacts — Sáng tạo tương tác

**Source:** https://transform.sg.larksuite.com/wiki/U49rwVc0oi3GLAk8d0OlwWyigHg
**Wiki ID:** U49rwVc0oi3GLAk8d0OlwWyigHg
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
Slide: Claude 101.pdf
1.0 - Claude 101 — Tổng quan khóa học
1.1 - Claude là gì?
1.2 - Cuộc trò chuyện đầu tiên với Claude
1.3 - Tối ưu kết quả — AI Fluency & Iteration
1.4 - Claude Desktop — Chat, Cowork, Code
1.5 - Projects — Không gian làm việc chuyên dụng
1.6 - Artifacts — Sáng tạo tương tác
1.7 - Skills — Đóng gói quy trình
1.8 - Connectors — Kết nối tools qua MCP
1.9 - Enterprise Search — Hỏi cả tổ chức
1.10 - Research mode — Đào sâu đa nguồn
1.11 - Claude theo vai trò — Use cases by role
1.12 - Các cách khác làm việc với Claude
1.13 - Tổng kết và bước tiếp theo
1.14 - Quiz tổng hợp & Chứng nhận
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
📣
Bổ sung course
Transform Group

1.6 - Artifacts — Sáng tạo tương tác

Last updated: Apr 20

Log In or Sign Up
1.6 - Artifacts — Sáng tạo tương tác
Bài 06: Artifacts — Sáng tạo tương tác
Mục tiêu học tập
Mở đầu: Output không chỉ là text
Artifacts là gì?
Claude tự động tạo Artifact khi content đạt các tiêu chí
6 loại Artifacts phổ biến
1. Documents — file text bạn sẽ export/edit
2. Code snippets — working code bạn view, copy, download
3. HTML pages — complete web pages
4. SVG images — scalable vector graphics
5. Mermaid diagrams — flowcharts, sequences, Gantt, org charts
6. React components — interactive UI với real logic
Tạo Artifact đầu tiên
4 ví dụ prompts
Flowchart
Interactive dashboard
Landing page
Reusable template
Khi Artifact xuất hiện, bạn có thể
Iterate trên Artifacts
Pattern iterate hiệu quả
1. One change at a time
2. Specific feedback
3. Build incrementally
Khi cần request artifact explicit
Share & Publish
1. Copy / Download (personal use)
2. Share trong organization (Claude for Work)
3. Publish publicly (Free, Pro, Max users)
Bảng so sánh 3 options
5 Tips để tăng ROI Artifacts
1. Be specific về cái bạn muốn
2. Describe end user
3. Iterate incrementally
4. Request artifacts khi cần
5. Think "reusable template"
Ví dụ theo ngành
💼 Sales Manager
📣 Content Marketer
💰 Finance Analyst
⚖️ Legal Counsel
🎓 Teacher
📊 Data Analyst
👥 HR Manager
🏢 Real Estate Agent
Anti-patterns với Artifacts
❌ Không dùng Artifacts cho reusable content
❌ Quá nhồi nhét trong 1 artifact
❌ Publish nhạy cảm content public
❌ Không test interactive artifacts
❌ Hard-code values thay vì inputs
1.6 - Artifacts — Sáng tạo tương tác​
Modified April 20
Bài 06: Artifacts — Sáng tạo tương tác​
Module: Tổ chức công việc​
Thời gian ước tính: 20 phút​
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
Slide: Claude 101.pdf​
​
​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Giải thích Artifacts là gì và khi nào Claude tạo Artifacts​
•
✅ Nhận diện các loại Artifacts phổ biến (documents, code, HTML, SVG, diagrams, React components)​
•
✅ Create, iterate, share, và publish Artifacts​
•
✅ Troubleshoot common artifact issues​
•
✅ Biết 5 use cases làm tăng ROI đáng kể​
​
​
Mở đầu: Output không chỉ là text​
Hình dung bạn nói với đồng nghiệp: "Làm cho tôi một dashboard theo dõi monthly expense theo category, có pie chart, có warning khi vượt budget."​
Nếu đồng nghiệp là designer → họ gửi Figma mockup. Nếu là developer → họ gửi 300 dòng code React bạn không đọc được. Nếu là data analyst → họ gửi Excel template.​
Rồi bạn phải:​
•
Mở Figma / code editor / Excel​
•
Preview / compile / test​
•
Feedback — "ô này làm nhỏ hơn", "đổi màu chỗ kia"​
•
Lặp lại 5 lần​
Nửa ngày trôi qua.​
Giờ thử với Claude + Artifacts. Bạn nói:​
"Build me a monthly budget tracker: input expenses by category, pie chart breakdown, warning khi over budget."​
Và ngay trong chat, Claude mở một cửa sổ riêng → tạo working dashboard có thể dùng ngay. Bạn input số thật → thấy chart update → click "over budget" scenario → thấy warning. Không cần setup, không cần download, không cần compile.​
Comments (0)
Help Center
Keyboard Shortcuts
