# 2.5 - Quản lý Context

**Source:** https://transform.sg.larksuite.com/wiki/PiYwwuv0BitFPmkcqchlhKzNgZd
**Wiki ID:** PiYwwuv0BitFPmkcqchlhKzNgZd
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
Slide: Claude Code 101.pdf
2.0 - Khoá học Claude Code 101 — Tổng quan
2.1 - Cách Claude Code hoạt động
2.2 - Cài đặt Claude Code
2.3 - Prompt Đầu Tiên
2.4 - Workflow Explore → Plan → Code → Commit
2.5 - Quản lý Context
2.6 - Code Review và Git Workflow
2.7 - File CLAUDE.md
2.8 - Subagents
2.9 - Skills — Dạy Claude một lần, dùng mãi mãi
2.10 - MCP — Kết nối Claude Code với thế giới bên ngoài
2.11 - Hooks — Kiểm soát tất định hành vi Claude Code
2.12 - Quiz tổng hợp — Claude Code 101
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

2.5 - Quản lý Context

Last updated: Apr 20

Log In or Sign Up
2.5 - Quản lý Context
Bài 2.5: Quản lý Context
Mục tiêu học tập
Mở đầu: Khi Claude bắt đầu "quên" giữa chừng
Context window là gì?
Context window dưới góc nhìn dev
Phép so sánh dễ nhớ
Chuyện gì xảy ra khi context "đầy"?
3 lệnh cốt lõi
/context — chẩn đoán trước khi quyết định
/compact — nén thông minh, giữ ký ức
/clear — xóa sạch, bắt đầu lại
Bảng so sánh quyết định: /compact vs /clear vs Auto-compact
Ví dụ thực chiến: Một ngày làm dev với context-aware Claude Code
Tình huống
9:00 — Bắt đầu fix webhook bug
10:30 — Chuyển sang feature CSV export
11:30 — Review PR KYC của teammate
Kết quả
5 chiến thuật tiết kiệm context
Chiến thuật 1: Be specific (prompt cụ thể tiết kiệm context)
Chiến thuật 2: Đẩy ngữ cảnh thường dùng vào CLAUDE.md
Chiến thuật 3: Subagent — outsource exploration
Chiến thuật 4: Skills thay vì hardcode trong CLAUDE.md
Chiến thuật 5: Dọn dẹp MCP servers không dùng
Case studies — quản lý context theo role
🛠️ Backend Engineer — long feature development
📣 Product Designer ship code (designer-as-developer)
⚙️ DevOps Engineer — incident response
🎓 CS Student học một codebase mới
Anti-patterns — Những sai lầm hủy context
❌ Anti-pattern 1: "Just keep going" — không bao giờ compact/clear
❌ Anti-pattern 2: "Tải tất cả file để Claude hiểu"
❌ Anti-pattern 3: Mix nhiều task khác nhau trong cùng 1 session
❌ Anti-pattern 4: Bật mọi MCP server "phòng khi cần"
❌ Anti-pattern 5: Dùng /clear khi đang dở task quan trọng
Mẹo nâng cao
Mẹo 1: Pin quan trọng vào CLAUDE.md trước khi /compact
Mẹo 2: Dùng # shortcut cho memory
Mẹo 3: Multi-session cho task song song
Mẹo 4: Estimate context trước khi prompt
Áp dụng ngay
Bài tập 1: Audit context trong session hiện tại (~10 phút)
Bài tập 2: Workflow /compact vs /clear (~15 phút)
Bài tập 3 (nâng cao): Design context budget cho 1 task lớn
Tóm tắt bài học
Bài tiếp theo
Tài liệu tham khảo
2.5 - Quản lý Context​
Modified April 20
Bài 2.5: Quản lý Context​
Module: Vận hành Claude Code chuyên nghiệp​
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
Slide: Claude Code 101.pdf​
​
Mục tiêu học tập​
Sau bài này, bạn sẽ có thể:​
•
✅ Giải thích context window là gì và tại sao nó là tài nguyên quan trọng nhất khi dùng Claude Code​
•
✅ Phân biệt khi nào nên dùng /compact và khi nào nên dùng /clear​
•
✅ Đọc kết quả lệnh /context để biết phần nào đang chiếm chỗ trong bộ nhớ làm việc​
•
✅ Áp dụng 5 chiến thuật tiết kiệm context: prompt cụ thể, CLAUDE.md, subagent, skill, MCP cleanup​
•
✅ Tránh được 4 anti-patterns thường gặp khiến context "phình to vô tội vạ"​
Mở đầu: Khi Claude bắt đầu "quên" giữa chừng​
Hãy tưởng tượng bạn là một backend engineer đang debug một bug authentication phức tạp. Bạn mở Claude Code, kể bối cảnh, share file auth.ts, share log lỗi, share schema database. Claude đọc, tìm hiểu, đề xuất hướng fix. Bạn approve. Claude bắt đầu sửa.​
30 phút sau, sau khi đã đọc 18 file, chạy 12 lệnh test, gọi 4 lần web search để tra cứu library docs — Claude bỗng dừng lại và nói:​
"Tôi đang nén lại cuộc hội thoại để giải phóng context window..."​
Vài giây sau, Claude tiếp tục — nhưng bạn nhận ra nó "quên" mất chi tiết bạn nói lúc đầu rằng JWT secret được rotate mỗi 7 ngày. Claude lại đề xuất một fix mà bỏ qua chi tiết đó. Bạn phải nhắc lại. Mất 5 phút.​
Tệ hơn nữa: Bạn chuyển sang task khác — implement một feature notification mới — nhưng bug auth vẫn còn trong context. Claude bị "ám" bởi authentication patterns, đề xuất một solution overly defensive với try-catch khắp nơi như đang sợ JWT lại bị rotate.​
Cả hai vấn đề trên đều xuất phát từ một gốc rễ: bạn chưa quản lý context window đúng cách.​
Context không phải là vô hạn. Nó là tài nguyên quý nhất khi làm việc với Claude Code — và nếu bạn không chủ động quản lý, nó sẽ tự "hết" và Claude sẽ bắt đầu "quên" hoặc "lệch hướng" theo những cách khó dự đoán.​
Bài này sẽ dạy bạn 3 thứ: (1) hiểu context window dưới capot, (2) biết khi nào dùng /compact vs /clear vs /context, và (3) áp dụng 5 chiến thuật tiết kiệm context để session của bạn dài và mượt hơn.​
Comments (0)
Help Center
Keyboard Shortcuts
