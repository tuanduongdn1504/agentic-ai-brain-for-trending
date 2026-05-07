# 6.41 - Extended thinking — Giấy nháp cho Claude

**Source:** https://transform.sg.larksuite.com/wiki/PlZiw9I47ikZNhkavPalhPegglh
**Wiki ID:** PlZiw9I47ikZNhkavPalhPegglh
**Archived:** 2026-05-07

---

Lark Docs
C
Claude Course 2026
Public access
Table of contents
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
6.58 - Giới thiệu MCP — Model Context Protocol
6.59 - MCP clients — Communication bridge
6.60 - Project setup — CLI chatbot với MCP
6.61 - Triển khai MCP client
6.62 - Server inspector — Debug UI cho MCP
6.63 - Định nghĩa tools qua MCP
6.64 - Định nghĩa prompts qua MCP
6.65 - Prompts trong client — UX cho slash commands
6.66 - Định nghĩa resources qua MCP
6.67 - Truy cập resources từ client
6.68 - MCP review — Tổng kết pattern
6.69 - Quiz — MCP
6.70 - Workflows vs Agents — Pattern nào khi nào?
6.71 - Agents và tools — Abstract vs specialized
6.72 - Project overview — Reminder agent
6.73 - Environment inspection — Agent phải "nhìn" được
6.74 - Chaining workflows — Sequential breakdown
6.75 - Parallelization workflows — Concurrent subtasks
6.76 - Routing workflows — Dispatch by category
6.77 - Enhancements với MCP servers — Extending Claude Code
Transform Group

6.41 - Extended thinking — Giấy nháp cho Claude

Last updated: Apr 20

Log In or Sign Up
6.41 - Extended thinking — Giấy nháp cho Claude
Bài 6.41: Extended thinking — Giấy nháp cho Claude
Mục tiêu học tập
Mở đầu: "Scratchpad" của Claude
Khi nào dùng?
Enable trong API
Rules
Response structure
Extract
Signature — Security
Redacted thinking
Multi-turn với thinking
Interaction với tools
Ví dụ thực chiến: Code debug
Cost & latency
Anti-patterns
❌ Thinking for easy tasks
❌ thinking_budget quá nhỏ
❌ max_tokens <= thinking_budget
❌ Modify thinking text
Áp dụng ngay
Bài tập 1: Compare with/without thinking (20 phút)
Bài tập 2: Eval-driven decision (20 phút)
Tóm tắt
Bài tiếp theo
6.41 - Extended thinking — Giấy nháp cho Claude​
Modified April 20
Bài 6.41: Extended thinking — Giấy nháp cho Claude​
Module: 6 — Tính năng nâng cao​
Thời gian ước tính: 20 phút​
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
Slide: Building with the Claude API.pdf​
​
​
​
Mục tiêu học tập​
•
✅ Giải thích extended thinking và khi nào dùng​
•
✅ Enable thinking trong API call​
•
✅ Handle thinking blocks trong response​
•
✅ Hiểu redacted thinking và signature security​
•
✅ Đánh giá trade-off cost/latency/quality​
​
​
Mở đầu: "Scratchpad" của Claude​
Hỏi Claude 1 bài toán phức tạp:​
Không thinking:​
User: "12345 × 6789 = ?"Claude: "83,810,205" (có thể sai)​
Có extended thinking:​
​
Code block​
Plain Text
Copy
User: "12345 × 6789 = ?"​
Claude [thinking]: Let me break this down step by step.​
  12345 × 6789 = 12345 × 6000 + 12345 × 700 + 12345 × 80 + 12345 × 9​
              = 74,070,000 + 8,641,500 + 987,600 + 111,105​
              = 83,810,205​
Claude: "83,810,205"​
​
​
Claude có giấy nháp để reason qua problem trước khi trả lời.​
​
​
Khi nào dùng?​
✅ Use cases:​
Comments (0)
Help Center
Keyboard Shortcuts
