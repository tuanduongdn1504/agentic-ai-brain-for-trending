# 6.21 - Quiz — Prompt Engineering

**Source:** https://transform.sg.larksuite.com/wiki/I4VFwvbRKiV3qBkZD9DlL59xgIc
**Wiki ID:** I4VFwvbRKiV3qBkZD9DlL59xgIc
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
Slide: Building with the Claude API.pdf
6.0 - Building with the Claude API — Tổng quan khóa học
6.1 - Chào mừng bạn đến với khóa học
6.2 - Tổng quan các model của Claude
6.3 - Các ứng dụng của Anthropic — Claude Code và Computer Use
6.4 - Vòng đời một request — Từ client đến Claude và ngược lại
6.5 - Lấy API key từ Anthropic Console
6.6 - Gọi request đầu tiên đến Claude
6.7 - Hội thoại nhiều lượt (Multi-Turn Conversations)
6.8 - Bài tập — Xây chatbot đầu tiên của bạn
6.9 - Streaming response — Hiển thị text khi Claude đang sinh
6.10 - System prompts — Định hình hành vi của Claude
6.11 - Bài tập — Thiết kế 3 system prompt production-ready
6.12 - Temperature — Kiểm soát độ ngẫu nhiên của Claude
6.13 - Nhập môn prompt engineering — Prompt là code
6.14 - Structured data — Ép Claude trả JSON/code sạch
6.15 - Bài tập — Structured data cho 3 use case
6.16 - Clear & Direct — Dòng đầu tiên quyết định tất cả
6.17 - Being specific — Guidelines và Process Steps
6.18 - Providing examples — Few-shot prompting
6.19 - Structure với XML tags
6.20 - Bài tập tổng hợp — Viết prompt production-grade
6.21 - Quiz — Prompt Engineering
6.22 - Prompt evaluation là gì?
6.23 - Workflow eval 5 bước
6.24 - Generating test datasets
6.25 - Running the eval — Build pipeline cốt lõi
6.26 - Model-based grading — Claude chấm Claude
6.27 - Code-based grading — Validation bằng Python
6.28 - Bài tập — End-to-end eval cho app của bạn
6.29 - Quiz — Prompt Evaluation
6.30 - Nhập môn Tool Use — Cho Claude "bàn tay"
6.31 - Tool schemas — JSON mô tả tool cho Claude
6.32 - Tool functions — Python code Claude sẽ gọi
6.33 - Handling message blocks — Multi-block responses
6.34 - Sending tool results — Gửi kết quả về Claude
6.35 - Multi-turn với tools — Sequential tool calls
6.36 - Triển khai multi-turn loop — Full code
6.37 - Dùng nhiều tools cùng lúc — Adding tools to your system
6.38 - Fine-grained tool calling — Stream tool inputs
6.39 - The text editor tool — Built-in tool cho file operations
6.40 - Quiz — Tool Use
6.41 - Extended thinking — Giấy nháp cho Claude
6.42 - Image support — Claude đọc ảnh (Vision)
6.43 - PDF support — Đọc tài liệu thẳng từ PDF
6.44 - The web search tool — Claude tra cứu internet
6.45 - Citations — Trust qua transparency
6.46 - Code execution & Files API — Claude chạy Python
6.47 - Prompt caching — Khái niệm & ROI
6.48 - Rules of prompt caching — Breakpoints + invalidation
6.49 - Prompt caching in action — Production code
6.50 - Quiz — Features of Claude
6.51 - Nhập môn RAG — Retrieval Augmented Generation
6.52 - Text chunking strategies
6.53 - Text embeddings — Biến text thành số
6.54 - The full RAG flow — End-to-end example
6.55 - Triển khai RAG pipeline — Production code
6.56 - BM25 lexical search — Hybrid với keyword
6.57 - Multi-Index RAG pipeline — Extensible architecture
Transform Group

6.21 - Quiz — Prompt Engineering

Last updated: Apr 20

Log In or Sign Up
6.21 - Quiz — Prompt Engineering
Bài 6.21: Quiz — Prompt Engineering
Giới thiệu
Phần 1: Khái niệm (Câu 1-4)
Câu 1
Câu 2
Câu 3
Câu 4
Phần 2: Clear & Direct (Câu 5-7)
Câu 5
Câu 6
Câu 7
Phần 3: Being Specific (Câu 8-9)
Câu 8
Câu 9
Phần 4: Examples (Câu 10-12)
Câu 10
Câu 11
Câu 12
Phần 5: XML Tags (Câu 13-14)
Câu 13
Câu 14
Phần 6: Integration (Câu 15)
Câu 15
Đáp án & Giải thích
Phần 1
Phần 2
Phần 3
Phần 4
Phần 5
Phần 6
Tính điểm
Bản đồ câu sai → Bài cần ôn
Practical self-assessment
Bài tiếp theo
6.21 - Quiz — Prompt Engineering​
Modified April 20
Bài 6.21: Quiz — Prompt Engineering​
Module: 3 — Prompt Engineering​
Thời gian ước tính: 20 phút​
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
Slide: Building with the Claude API.pdf​
​
Giới thiệu​
Quiz này gồm 15 câu bao phủ Module 3 (bài 6.13 → 6.20). Mục tiêu kiểm tra bạn đã nắm vững:​
•
Khái niệm prompt engineering và eval loop​
•
4 kỹ thuật cốt lõi​
•
Anti-patterns và best practices​
Điểm chuẩn:​
•
13-15/15 : Thành thạo — sẵn sàng Module 4​
•
10-12/15 : Tốt — review 2-3 bài chưa chắc​
•
7-9/15 : Cần ôn Module 3​
•
< 7 : Nên đọc lại từ 6.13​
Phần 1: Khái niệm (Câu 1-4)​
Câu 1​
Đâu là đặc điểm phân biệt prompt engineering với prompting tip/trick?​
A) Prompt engineering dùng từ chuyên ngành, tips khôngB) Prompt engineering có iteration loop đo lường được, tips là "magic phrase"C) Prompt engineering chỉ dùng cho Claude, tips dùng cho ChatGPTD) Tips nhanh hơn, không có khác biệt nghiêm trọng​
Câu 2​
Vòng lặp core của prompt engineering gồm những bước nào?​
A) Write prompt → Test → ShipB) Set goal → v1 → Evaluate → Apply technique → Re-evaluate → iterateC) Research → Brainstorm → Write → DeployD) Copy from docs → Adapt → Run​
Comments (0)
Help Center
Keyboard Shortcuts
