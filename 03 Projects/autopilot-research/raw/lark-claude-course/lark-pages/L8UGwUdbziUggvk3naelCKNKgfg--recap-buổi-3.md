# Recap buổi 3

**Source:** https://transform.sg.larksuite.com/wiki/L8UGwUdbziUggvk3naelCKNKgfg
**Wiki ID:** L8UGwUdbziUggvk3naelCKNKgfg
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
Recap buổi 3
Example
skill_creator_project.zip
bitis-offer-onboarding.zip
bitis-interview-kit.zip
bitis-cv-screening.zip
bitis-job-posting.zip
tiktok-content-producer.zip
✅
Buổi 4, Ngày 24/4 @7.30 PM
✅
Buổi 5, Ngày 28/4 @7.30 PM
Anthropic courses
📣
Bổ sung course
Transform Group

Recap buổi 3

Last updated: Apr 23

Log In or Sign Up
Recap buổi 3
1. Tổng quan buổi
2. Phần Tuấn: Pattern "Skill Creator Assistant"
2.1. Vấn đề với cách tạo skill thủ công
2.2. Pattern: Build một Project-as-Assistant thay vì dùng skill-creator default
2.3. Install skill đã sinh vào Claude
2.4. Vì sao Pattern này tốt hơn dùng skill-creator default
2.5. Demo 2: HRV MCP + Skill bundle (build trong 60 giây)
3. Phần Hải: Codymaster + Enterprise Vibe Coding
3.1. Giới thiệu Codymaster
3.2. Triết lý của Hải về Skills vs MCP
3.3. Lời khuyên Vibe Coding cho Enterprise (Q&A #2 — được upvote nhiều)
3.4. Vấn đề cài quá nhiều skills
3.5. Live demo: Landing page với Pencil.dev
3.6. Skill setup workflow của Hải
3.7. Xcel (Extension mới của Claude)
3.8. Coze.com để embed chatbot vào website (Q&A #11, #12)
3.9. NotebookLM cho company knowledge base (Q&A #13)
4. 22 Q&A từ Zoom (full list)
4.1. Skills & Creation
4.2. Enterprise Vibe Coding
4.3. API & Integration
4.4. Chatbot & NotebookLM
4.5. Design & UI
4.6. Khác
5. Insights từ Chat (ngoài Q&A chính thức)
5.1. Skills được học viên đề xuất cho các buổi sau
5.2. Phản ứng của học viên
5.3. Vấn đề kỹ thuật
5.4. Lark MCP + Claude (Q&A #25 trong chat — Hoai Nam hỏi)
5.5. Offline location (Q&A #30 — Q.Tran)
6. Resources được share
Core trong buổi
Platform references
8. Lịch các buổi tiếp theo
9. Key Takeaways
Recap buổi 3​
Modified April 23
1.
Tổng quan buổi​
Đây là buổi deep-dive về Skills — chức năng được hỏi nhiều nhất qua 2 buổi đầu. Cấu trúc buổi chia 2 nửa rõ rệt:​
•
Nửa đầu (Tuấn): Pattern "Skill Creator Assistant" — cách biến Claude thành trợ lý tự build skill thay vì user phải viết SKILL.md tay.​
•
Nửa sau (Hải): Codymaster — bộ ~60+ skills do Hải tự bill cho công ty phần mềm, live demo vibe coding landing page với Pencil.dev + kinh nghiệm enterprise (CRM/POS/ERP).​
Thông điệp xuyên suốt:​
​
"Không ai đi tạo skill bằng cách tự ngồi gõ file SKILL.md cả. Cách đúng là biến Claude thành người đồng sáng tạo giúp mình tạo skill." — Tuấn​
"Bản chất skill nó giống như mô tả công việc thôi, không phải gì cao siêu. Đọc xong thấy không giống nhu cầu thì sửa lại, chat với Claude nó cũng sửa lại cho." — Hải​
​
​
​
2.
Phần Tuấn: Pattern "Skill Creator Assistant"​
2.1. Vấn đề với cách tạo skill thủ công​
Tuấn mở đầu bằng cách chỉ ra 3 tầng tài liệu đã có sẵn cho Skills:​
1.
Bài số 4 trong 18 khóa Anthropic — chi tiết về cách build skill.​
2.
File PDF chính thức 3 trang của Anthropic — best-practices viết SKILL.md.​
3.
Slide 26 trang Tuấn tự tổng hợp — bản tiếng Việt rút gọn.​
4.
Podcast ~5 phút — Tuấn đã generate từ NotebookLM để nghe nhanh.​
Nhưng: "Tài liệu nhiều mà anh em cũng không đọc. Đọc xong cũng không nhớ. Đọc xong cũng không biết làm thế nào. Đặc biệt là chủ doanh nghiệp và quản lý — mọi người đang khát nước quá, cần giải quyết vấn đề ngay thay vì đọc cơ bản từng bước."​
→ Không ai sẽ ngồi viết SKILL.md thủ công cả.​
2.2. Pattern: Build một Project-as-Assistant thay vì dùng skill-creator default​
Thay vì dùng skill-creator default của Anthropic (có sẵn trong Skills library), Tuấn đề xuất:​
Bước 1: Dùng Claude Chat → prompt:​
​
"Tôi muốn tạo một Project trong Claude để giúp tôi xây dựng các skill theo nhu cầu của tôi. Hãy giúp tôi tạo các file .md để upload vào Project (Instructions + Knowledge files). Tôi đã đính kèm file best-practices 3 trang của Anthropic và 5 file từ khóa 18 — hãy tham khảo."​
​
Bước 2: Claude tự sinh 5 file:​
•
instructions.md — persona "Skill Architect Assistant"​
•
skill_template.md — template chuẩn Anthropic​
•
prompt_patterns.md — các pattern prompt cho từng loại skill​
•
checklist.md — checklist review skill​
•
examples.md — ví dụ skill đã pass​
Bước 3: Download 5 file → tạo Project mới tên "Skill Creator Assistant" → upload vào Knowledge → paste instructions.md vào Project Instructions.​
Bước 4: Từ đây trở đi, mọi lần cần skill mới → vào Project này, gõ ngắn:​
Comments (0)
Help Center
Keyboard Shortcuts
Loading...
