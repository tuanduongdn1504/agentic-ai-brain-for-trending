# 6.75 - Parallelization workflows — Concurrent subtasks

**Source:** https://transform.sg.larksuite.com/wiki/GNdwwunMJieA0rkB6S3l68NngQf
**Wiki ID:** GNdwwunMJieA0rkB6S3l68NngQf
**Archived:** 2026-05-07

---

Lark Docs
C
Claude Course 2026
Public access
Table of contents
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
13 - Teaching AI Fluency
14 - AI Fluency for nonprofits
15 - Introduction to agent skills
16 - Introduction to subagents
17 - AI Capabilities and Limitations
📣
Bổ sung course
Transform Group

6.75 - Parallelization workflows — Concurrent subtasks

Last updated: Apr 20

Log In or Sign Up
6.75 - Parallelization workflows — Concurrent subtasks
Bài 6.75: Parallelization workflows — Concurrent subtasks
Mục tiêu học tập
Mở đầu: Material designer — 1 prompt fail
Single prompt approach
Parallel approach
Pattern
Implementation với asyncio
Performance
Pattern variants
Homogeneous
Heterogeneous
Both
Aggregation strategies
Voting
Weighted
Claude aggregate
When parallel worth
✅ Good fit
⚠️ Skip
Rate limits
Bounded concurrency
Cost aware
Real-world use cases
📊 Data analysis
📄 Document processing
🏢 Multi-dimensional evaluation
🎬 Content generation
🔍 Research
Anti-patterns
❌ Forget bounded concurrency
❌ Parallel sequential steps
❌ Ignore partial failures
Áp dụng ngay
Bài tập 1: Parallelize for your app (30 phút)
Bài tập 2: Material recommender (30 phút)
Tóm tắt
Bài tiếp theo
6.75 - Parallelization workflows — Concurrent subtasks​
Modified April 20
Bài 6.75: Parallelization workflows — Concurrent subtasks​
Module: 9 — Workflows & Agents​
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
✅ Understand parallelization pattern​
•
✅ Split single task → specialized parallel subtasks → aggregate​
•
✅ Implement với asyncio​
•
✅ Balance speed vs cost​
Mở đầu: Material designer — 1 prompt fail​
User upload part image → recommend material (metal, polymer, ceramic, composite, elastomer, wood).​
Single prompt approach​
​
Code block​
Plain Text
Copy
"Evaluate this part image and choose best material from: ​
metal, polymer, ceramic, composite, elastomer, wood.​
Consider: strength, weight, cost, manufacturability..."​
​
​
Claude juggle 6 material × 4 criteria = 24 considerations. Overwhelmed → suboptimal pick.​
Parallel approach​
Run 6 parallel evaluations, each specialized cho 1 material. Aggregate picks.​
Pattern​
​
Code block​
Plain Text
Copy
​
Comments (0)
Help Center
Keyboard Shortcuts
