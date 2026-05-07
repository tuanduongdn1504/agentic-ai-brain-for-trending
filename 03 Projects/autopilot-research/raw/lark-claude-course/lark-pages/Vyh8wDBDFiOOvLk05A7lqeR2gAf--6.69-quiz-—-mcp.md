# 6.69 - Quiz — MCP

**Source:** https://transform.sg.larksuite.com/wiki/Vyh8wDBDFiOOvLk05A7lqeR2gAf
**Wiki ID:** Vyh8wDBDFiOOvLk05A7lqeR2gAf
**Archived:** 2026-05-07

---

Lark Docs
C
Claude Course 2026
Public access
Table of contents
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
15 - Introduction to agent skills
16 - Introduction to subagents
17 - AI Capabilities and Limitations
📣
Bổ sung course
Transform Group

6.69 - Quiz — MCP

Last updated: Apr 20

Log In or Sign Up
6.69 - Quiz — MCP
Bài 6.69: Quiz — MCP
12 câu hỏi
1. MCP giải quyết vấn đề gì?
2. 3 primitives của MCP:
3. MCP client là gì?
4. Transport options của MCP:
5. Tool của MCP khác tool use thông thường như thế nào?
6. Prompt trong MCP là:
7. Resources trong MCP:
8. @mcp.tool decorator làm gì?
9. MCP Inspector để làm gì?
10. Build MCP server vs client — thường chọn cái nào?
11. FastMCP là:
12. Ai maintain MCP tools (GitHub MCP server)?
Đáp án
Bài tiếp theo
6.69 - Quiz — MCP​
Modified April 20
Bài 6.69: Quiz — MCP​
Module: 8 — MCP​
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
1. MCP giải quyết vấn đề gì?​
A) Claude không có toolsB) Maintenance burden khi có nhiều integrationsC) Claude chậmD) API đắt​
2. 3 primitives của MCP:​
A) Input, output, processB) Tools, Prompts, ResourcesC) Client, Server, ProtocolD) Request, Response, Error​
3. MCP client là gì?​
A) UI cho end-userB) Library/code app dùng để talk to MCP serversC) Type of serverD) Database​
4. Transport options của MCP:​
A) Chỉ HTTPB) stdio, HTTP, WebSocketC) gRPC onlyD) TCP only​
5. Tool của MCP khác tool use thông thường như thế nào?​
A) Khác completelyB) MCP = where tool lives. Tool use = how Claude calls. Complementary.C) MCP thay thế tool useD) Không khác gì​
6. Prompt trong MCP là:​
A) System promptB) Template curated bởi server author, user trigger qua slash commandC) User inputD) Same as tool​
7. Resources trong MCP:​
A) Read-only data với URIB) Actions có side effectC) Images onlyD) Database tables​
8. @mcp.tool decorator làm gì?​
A) Protect toolB) Auto-generate JSON schema từ type hintsC) Add loggingD) Cache tool​
9. MCP Inspector để làm gì?​
A) Production monitoringB) Browser UI test server standaloneC) Claude debuggingD) Payment​
Comments (0)
Help Center
Keyboard Shortcuts
