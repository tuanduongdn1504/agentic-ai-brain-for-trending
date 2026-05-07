# 6.80 - Claude Code in action — Workflows thực tế

**Source:** https://transform.sg.larksuite.com/wiki/NPvDwfR9DikSPlkW6qkl7b8Kgcb
**Wiki ID:** NPvDwfR9DikSPlkW6qkl7b8Kgcb
**Archived:** 2026-05-07

---

Lark Docs
C
Claude Course 2026
Public access
Table of contents
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

6.80 - Claude Code in action — Workflows thực tế

Last updated: Apr 20

Log In or Sign Up
6.80 - Claude Code in action — Workflows thực tế
Bài 6.80: Claude Code in action — Workflows thực tế
Mục tiêu học tập
Mở đầu: Không phải code generator, là teammate
/init — first thing mỗi project
CLAUDE.md example
Future sessions
Workflow 1: Context → Plan → Implement
Step 1: Context
Step 2: Plan (NO CODE YET)
Step 3: Implement
Workflow 2: Test-Driven (TDD)
Workflow 3: Bug fixing
Workflow 4: Refactor
Workflow 5: Learning codebase
# command — enforce rules
Multi-step with TodoWrite
Handling large changes
Best practices
1. One task per session
2. Commit frequently
3. Review generated code
4. Use extended thinking for hard problems
5. Cost monitor
Common sessions
Daily — morning standup
Weekly — tech debt
Code review
Documentation
Headless usage (automation)
Anti-patterns
❌ "Just build it"
❌ No CLAUDE.md
❌ Skip plan step
❌ Ignore Claude's plan feedback
❌ Full codebase write access in prod
Áp dụng ngay
Bài tập 1: 3-step workflow (30 phút)
Bài tập 2: TDD workflow (30 phút)
Tóm tắt
Bài tiếp theo
6.80 - Claude Code in action — Workflows thực tế​
Modified April 20
Bài 6.80: Claude Code in action — Workflows thực tế​
Module: 10 — Claude Code​
Thời gian ước tính: 25 phút​
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
Mục tiêu học tập​
•
✅ Use /init để setup CLAUDE.md​
•
✅ Apply 3-step workflow: context → plan → implement​
•
✅ TDD workflow với Claude Code​
•
✅ Best practices for productive usage​
Mở đầu: Không phải code generator, là teammate​
Claude Code không phải "gõ prompt → nhận code". Nó là engineer đồng đội — needs context, needs direction, có thể iterate.​
Pattern Anthropic recommend: feed context → plan → implement. Adherence này cải thiện quality đáng kể.​
/init — first thing mỗi project​
​
Code block​
Bash
Copy
cd my-project​
claude​
> /init​
​
​
Claude:​
1.
Scan codebase structure​
2.
Read README, package.json, main files​
3.
Identify: languages, frameworks, patterns, commands​
4.
Generate CLAUDE.md​
CLAUDE.md example​
Comments (0)
Help Center
Keyboard Shortcuts
