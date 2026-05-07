# 6.52 - Text chunking strategies

**Source:** https://transform.sg.larksuite.com/wiki/HsOUwiun2i5PpqkyiVWl2jRwgic
**Wiki ID:** HsOUwiun2i5PpqkyiVWl2jRwgic
**Archived:** 2026-05-07

---

Lark Docs
C
Claude Course 2026
Public access
Table of contents
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
13 - Teaching AI Fluency
14 - AI Fluency for nonprofits
Transform Group

6.52 - Text chunking strategies

Last updated: Apr 20

Log In or Sign Up
6.52 - Text chunking strategies
Bài 6.52: Text chunking strategies
Mục tiêu học tập
Mở đầu: "Bug" nghĩa là gì?
4 chiến lược
1. Size-based
2. Structure-based (Markdown, HTML)
3. Sentence-based
4. Semantic chunking
So sánh
Practical recommendations
Starting fresh
Production case studies
Chunk size sweet spot
Eval chunks
Metadata với chunks
Anti-patterns
❌ No overlap
❌ Chunk quá nhỏ (< 200 tokens)
❌ Chunk quá lớn (> 4000)
❌ Không re-chunk khi doc update
❌ Chunk code size-based mid-function
Áp dụng ngay
Bài tập 1: Chunk sample doc (20 phút)
Bài tập 2: Test with query (20 phút)
Tóm tắt
Bài tiếp theo
6.52 - Text chunking strategies​
Modified April 20
Bài 6.52: Text chunking strategies​
Module: 7 — RAG​
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
Mục tiêu học tập​
•
✅ So sánh 4 chiến lược chunking: size, structure, sentence, semantic​
•
✅ Implement size-based chunking với overlap​
•
✅ Implement structure-based chunking cho Markdown​
•
✅ Chọn strategy phù hợp theo document type​
Mở đầu: "Bug" nghĩa là gì?​
Doc có 2 section: Medical Research và Software Engineering.​
User hỏi: "How many bugs did engineers fix this year?"​
Bad chunking: chunk chứa "bug" trong medical section (sinh vật) → Claude trả lời về bệnh tật.​
Good chunking: medical section và software section trong chunks tách biệt → retrieval lấy đúng software section.​
Chunking quyết định chất lượng toàn RAG.​
4 chiến lược​
1. Size-based​
Cắt text thành chunks ~N ký tự/tokens equal.​
Pros: Simple, universal (code, text, any format).Cons: Words cut mid-sentence, context lost.​
​
Code block​
Python
Copy
def chunk_by_char(text, chunk_size=1500, chunk_overlap=200):​
    chunks = []​
    start = 0​
    while start < len(text):​
        end = min(start + chunk_size, len(text))​
​
Comments (0)
Help Center
Keyboard Shortcuts
