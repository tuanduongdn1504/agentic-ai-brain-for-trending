# Recap buổi 5

**Source:** https://transform.sg.larksuite.com/wiki/PUAlwUXCriovsmkMkjklFVi5gEd
**Wiki ID:** PUAlwUXCriovsmkMkjklFVi5gEd
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
✅
Buổi 1, Ngày 18/4
✅
Buổi 2, Ngày 20/4
✅
Buổi 3, Ngày 22/4 @7.30 PM
✅
Buổi 4, Ngày 24/4 @7.30 PM
✅
Buổi 5, Ngày 28/4 @7.30 PM
Recap buổi 5
guide.md
Mastering_Agentic_AI.pdf
Anthropic courses
📣
Bổ sung course
Transform Group

Recap buổi 5

Last updated: Apr 29

Log In or Sign Up
Recap buổi 5
1. Tổng quan buổi
2. Phần Tuấn: Chat → Agent + Build Agent từ Claude Code
2.1. Tâm thế và Mindset khi dùng Claude (mở đầu)
2.2. Tận dụng Image Generation mới của Claude
2.3. 4 Lớp khi sử dụng Claude
2.4. An toàn thông tin (Security mindset)
2.5. Demo: Build Agent từ Claude Code (deep dive)
2.6. Tại sao file .md?
2.7. Demo nhỏ: "Làm sao để AI gọi mình là 'Sếp'?" (Q&A #4)
2.8. Pricing reality talk
3. Phần Tony: Best Practices Claude Code (CLAUDE.md + Workflow)
3.1. CLAUDE.md là gì
3.2. Hai loại CLAUDE.md
3.3. CLAUDE.md độ dài tối ưu (Q&A #13 từ TruongCX)
3.4. Cái gì nên đưa vào CLAUDE.md (Q&A #19 từ TruongCX)
3.5. Plan Mode trước khi Code (best practice từ Anthropic)
3.6. Verify everything với examples
3.7. Git là life-saver (Trap thứ 3)
3.8. Course Correction (Trap thứ 7)
3.9. Skills (mục số 6) + MCP (mục số 7) + Sub-agent (mục số 8)
3.10. Security Boundaries (mục số 8)
3.11. Voice Mode (mục số 9 — New Project)
3.12. Tiếng Anh hay Tiếng Việt? (Tranh luận giữa Tony và Hải)
3.13. Specificity (mục số 11)
3.14. Đưa data cho AI (Q&A discussion)
3.15. Aesopian Slide Show (mục cuối Tony)
4. Phần Hải: QA/QC + Codymaster Deep Dive
4.1. Test-First Mindset (Q&A #10)
4.2. Codymaster QA reference (Q&A #12)
4.3. Coder + Reviewer trong cùng Agent? (Q&A #22 + #29 — Hung Le)
4.4. Tránh ảo giác (Q&A #21 — Thuy Nguyen)
4.5. Tâm Hoàng's Token Limit Error (Q&A #27, #28)
4.6. Live demo: Cô Gout (Codex / Codey?) cũng làm code OK
4.7. Schedule task automation
4.8. Auto-test course (free)
4.9. Notebook LM workflow ngược (Q&A #23, #24)
4.10. cc-connect (link Tuấn share)
4.11. Cẩn trọng với Browser Mode
5. 30 Q&A từ Zoom (organized)
5.1. NotebookLM & Knowledge Management (8 câu)
5.2. CLAUDE.md & Project Structure (4 câu)
5.3. Skills & Browser Mode (4 câu)
5.4. Models & Tools (4 câu)
5.5. Agents & Architecture (5 câu)
5.6. Quality & Testing (1 câu)
5.7. Reflective questions
6. Insights từ Chat (ngoài Q&A)
6.1. Pricing pain & switching
6.2. Hải's stack ranking
6.4. Học viên xác nhận giá trị
6.5. Requests cho buổi sau lễ
Recap buổi 5​
Modified April 29
1.
Tổng quan buổi​
Đây là buổi cuối của chuỗi 5 buổi "Học Claude AI" — diễn ra trước kỳ nghỉ lễ 30/04. Cấu trúc buổi chia 3 phần với 3 diễn giả, focus vào chuyển dịch tâm thế từ Chat → Agent + best practices Claude Code:​
•
Phần 1 (Tuấn): Mindset shift Chat→Agent, kiến trúc 4 lớp Skill, demo build agent bằng Claude Code trên 1 folder.​
•
Phần 2 (Tony): Best practices CLAUDE.md theo Claude in Action (course 117.1), plan mode workflow, voice mode, security boundaries.​
•
Phần 3 (Hải): QA/QC framework, test trước khi code, NotebookLM workflow ngược (knowledge → video courses), Codymaster QA.​
Đây cũng là buổi mở đầu cho hậu chuỗi — nhiều câu hỏi cuối buổi xin thêm session về NotebookLM, Vibe Coding sau lễ.​
​
"Cái mindset cốt lõi: Claude không phải là chatbot trả lời câu hỏi. Nó là cộng sự — mình giao việc, ủy quyền, và phải xây kỹ năng kiểm chứng." — Tuấn​
"Đầu tư $100/tháng đi các bạn. Nhân viên của năm đấy." — Tony (chốt buổi)​
​
2.
Phần Tuấn: Chat → Agent + Build Agent từ Claude Code​
2.1. Tâm thế và Mindset khi dùng Claude (mở đầu)​
Tuấn mở đầu bằng việc kể lại buổi 4 offline tại văn phòng Transform Group: anh thấy nhiều học viên còn bỡ ngỡ — quen ChatGPT/Gemini chỉ dùng để chat, chưa quen với Claude khi nó vừa chat vừa giao việc.​
Tuấn đã prompt Claude (Opus) viết một bài về "Tâm thế và Mindset khi sử dụng AI từ Chat sang Work" — nội dung được dùng làm khung cho phần này.​
Sự khác biệt cốt lõi giữa AI 2025 và 2026:​
​
​
Mindset shift quan trọng: Từ coi AI là công cụ → coi AI là cộng sự. Cộng sự thì phải define rõ:​
•
Vai trò là gì​
•
Profile (chân dung) ra sao​
•
Skills + permissions có gì​
•
Memory (ngắn hạn / dài hạn) thế nào​
2.2. Tận dụng Image Generation mới của Claude​
Tuấn note nhanh: Claude image generation mới ra "ăn đứt Gemini" (theo chat của Tuan Nguyen). Demo: Tuấn ném slide content + style reference vào Claude → 30 giây ra ảnh hero đẹp, đồng nhất style với các slide khác.​
Workflow Tuấn đang dùng để tạo slides:​
1.
Prompt Claude generate nội dung structured → output bullet text.​
Comments (0)
Help Center
Keyboard Shortcuts
Loading...
