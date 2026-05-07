# 6.78 - Quiz — Workflows & Agents

**Source:** https://transform.sg.larksuite.com/wiki/Q1mGwFwFciBMcekX2KvlPvMHg0b
**Wiki ID:** Q1mGwFwFciBMcekX2KvlPvMHg0b
**Archived:** 2026-05-07

---

Lark Docs
C
Claude Course 2026
Public access
Table of contents
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

6.78 - Quiz — Workflows & Agents

Last updated: Apr 20

Log In or Sign Up
6.78 - Quiz — Workflows & Agents
Bài 6.78: Quiz — Workflows & Agents
12 câu hỏi
1. Workflow và agent khác nhau cơ bản?
2. Anthropic khuyến nghị mặc định dùng cái nào?
3. Abstract tools hay specialized tools cho agents?
4. Environment inspection critical vì?
5. Pattern "read before write" tồn tại vì?
6. Chaining workflow giải quyết:
7. Parallelization workflow ideal cho?
8. Routing workflow cơ chế?
9. Classifier trong router workflow thường dùng model?
10. Số categories ideal cho routing?
11. MCP servers extend Claude Code via?
12. Khi nào build MCP server cho team tools?
Đáp án
Bài tiếp theo
6.78 - Quiz — Workflows & Agents​
Modified April 20
Bài 6.78: Quiz — Workflows & Agents​
Module: 9 — Workflows & Agents​
Thời gian ước tính: 10 phút​
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
12 câu hỏi​
1. Workflow và agent khác nhau cơ bản?​
A) Workflow dùng Haiku, agent dùng OpusB) Workflow = pre-defined sequence, agent = Claude plans dynamicallyC) Workflow slow, agent fastD) Không khác​
2. Anthropic khuyến nghị mặc định dùng cái nào?​
A) Always agentB) Workflow when possible, agent when flexibility requiredC) Always parallelD) Depends on mood​
3. Abstract tools hay specialized tools cho agents?​
A) Specialized tốt hơnB) Abstract (như Claude Code's bash, read, edit)C) Mix 50/50D) Không quan trọng​
4. Environment inspection critical vì?​
A) Claude nhớ contextB) Claude bị bịt mắt nếu không see result of actionsC) SpeedD) Cost​
5. Pattern "read before write" tồn tại vì?​
A) Best practice ruleB) Claude cần context trước khi modify để không break existingC) Anthropic bắt buộcD) Không​
6. Chaining workflow giải quyết:​
A) Long prompt với nhiều constraints Claude missB) SpeedC) CostD) Security​
7. Parallelization workflow ideal cho?​
A) Dependent sequential stepsB) Independent subtasks có thể execute simultaneouslyC) Single API callD) Never​
8. Routing workflow cơ chế?​
A) Classify input → dispatch specialized pipelineB) Route traffic between serversC) Random selectionD) Always runs all pipelines​
9. Classifier trong router workflow thường dùng model?​
Comments (0)
Help Center
Keyboard Shortcuts
