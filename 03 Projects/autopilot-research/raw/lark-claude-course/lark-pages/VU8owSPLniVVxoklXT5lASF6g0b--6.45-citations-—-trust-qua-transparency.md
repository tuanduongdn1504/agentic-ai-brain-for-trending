# 6.45 - Citations — Trust qua transparency

**Source:** https://transform.sg.larksuite.com/wiki/VU8owSPLniVVxoklXT5lASF6g0b
**Wiki ID:** VU8owSPLniVVxoklXT5lASF6g0b
**Archived:** 2026-05-07

---

Lark Docs
C
Claude Course 2026
Public access
Table of contents
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
6.78 - Quiz — Workflows & Agents
6.79 - Claude Code setup
6.80 - Claude Code in action — Workflows thực tế
6.81 - Course wrap-up — Bạn đã học được gì
Transform Group

6.45 - Citations — Trust qua transparency

Last updated: Apr 20

Log In or Sign Up
6.45 - Citations — Trust qua transparency
Bài 6.45: Citations — Trust qua transparency
Mục tiêu học tập
Mở đầu: "Trust but verify"
Enable citations
Response structure
For PDF (pages)
Extract citations
Plain text document
UI pattern: Interactive citations
Implementation
Ví dụ: Contract Q&A
Multi-document citations
Document vs Web search citations
When to use citations
✅ Use when
⚠️ Skip when
Anti-patterns
❌ Enable but không render citations
❌ Chỉ dùng với 1 doc nhỏ
❌ Assume Claude cite mọi statement
Áp dụng ngay
Bài tập 1: Cited Q&A (15 phút)
Bài tập 2: Multi-doc cited compare (20 phút)
Tóm tắt
Bài tiếp theo
6.45 - Citations — Trust qua transparency​
Modified April 20
Bài 6.45: Citations — Trust qua transparency​
Module: 6 — Tính năng nâng cao​
Thời gian ước tính: 15 phút​
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
Mục tiêu học tập​
•
✅ Enable citations cho PDF / text documents​
•
✅ Handle citation metadata trong response​
•
✅ Build UI với interactive citations​
•
✅ Hiểu khác biệt giữa citations (docs) vs web_search citations​
Mở đầu: "Trust but verify"​
User hỏi về document bạn provide, Claude trả lời. Nhưng:​
•
Claude tưởng tượng (hallucinate)?​
•
Có từ training data?​
•
Hay thực sự từ document?​
Citations giải quyết — Claude quote exact text từ document với page number. User verify được.​
Đặc biệt critical cho:​
•
Legal (contract terms)​
•
Medical (research)​
•
Compliance (policies)​
•
Academic (source material)​
Enable citations​
Modify document block:​
​
Code block​
Python
Copy
{​
    "type": "document",​
​
Comments (0)
Help Center
Keyboard Shortcuts
