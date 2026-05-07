# 6.50 - Quiz — Features of Claude

**Source:** https://transform.sg.larksuite.com/wiki/DFiDwJQBViaDV3kYcxZlNWYCg9e
**Wiki ID:** DFiDwJQBViaDV3kYcxZlNWYCg9e
**Archived:** 2026-05-07

---

Lark Docs
C
Claude Course 2026
Public access
Table of contents
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
6.82 - Final Assessment — Quiz tổng hợp
07 - Introduction to Model Context Protocol
08 - AI Fluency for Educators
09 - AI Fluency for Students
10 - Model Context Protocol: Advanced Topics
Transform Group

6.50 - Quiz — Features of Claude

Last updated: Apr 20

Log In or Sign Up
6.50 - Quiz — Features of Claude
Bài 6.50: Quiz — Features of Claude
12 câu hỏi
1. Extended thinking dùng khi nào tốt nhất?
2. thinking_budget minimum?
3. Image limit per request?
4. Image block type là gì?
5. PDF block type?
6. Web search tool — cần gì trước khi dùng?
7. Citations — thêm gì vào document block?
8. Code execution — môi trường như thế nào?
9. Files API dùng để?
10. Prompt caching tiết kiệm bao nhiêu cho cache read?
11. Cache TTL?
12. Minimum content để cache?
Đáp án
Bài tiếp theo
6.50 - Quiz — Features of Claude​
Modified April 20
Bài 6.50: Quiz — Features of Claude​
Module: 6 — Tính năng nâng cao​
Thời gian ước tính: 15 phút​
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
12 câu hỏi​
1. Extended thinking dùng khi nào tốt nhất?​
A) Mọi requestB) Task đơn giảnC) Complex reasoning sau khi prompt engineering không đủD) Khi budget thấp​
2. thinking_budget minimum?​
A) 100B) 1024C) 10000D) Không có minimum​
3. Image limit per request?​
A) 10B) 50C) 100D) Unlimited​
4. Image block type là gì?​
A) "picture"B) "image"C) "visual"D) "photo"​
5. PDF block type?​
A) "image"B) "file"C) "document"D) "pdf"​
6. Web search tool — cần gì trước khi dùng?​
A) Custom implementationB) Bật trong Console privacy settingsC) Pay extra subscriptionD) Nothing​
7. Citations — thêm gì vào document block?​
A) "cite": trueB) "citations": {"enabled": True}C) "include_sources": trueD) "show_refs": true​
8. Code execution — môi trường như thế nào?​
A) Full system accessB) Network accessC) Docker isolated, no networkD) Your local machine​
9. Files API dùng để?​
A) Delete filesB) Upload files once, reference by ID for future requestsC) Run codeD) Đồng nghĩa với prompt caching​
Comments (0)
Help Center
Keyboard Shortcuts
