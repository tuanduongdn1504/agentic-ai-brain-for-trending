# 6.32 - Tool functions — Python code Claude sẽ gọi

**Source:** https://transform.sg.larksuite.com/wiki/SHfpw54DFiIebmk4auflEJ01gKc
**Wiki ID:** SHfpw54DFiIebmk4auflEJ01gKc
**Archived:** 2026-05-07

---

Lark Docs
C
Claude Course 2026
Public access
Table of contents
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
Transform Group

6.32 - Tool functions — Python code Claude sẽ gọi

Last updated: Apr 20

Log In or Sign Up
6.32 - Tool functions — Python code Claude sẽ gọi
Bài 6.32: Tool functions — Python code Claude sẽ gọi
Mục tiêu học tập
Mở đầu: Function đơn giản nhưng cần robust
Best practices
1. Descriptive names
2. Validate inputs
3. Meaningful error messages
4. Return strings (thường)
3 tool functions mẫu
1. get_current_datetime
2. add_duration_to_datetime
3. set_reminder
Pattern: Try-except với informative error
Pattern: Side effects + confirmation
Function + schema pairing
Security considerations
Tool có thể run code / modify data — nguy hiểm
Rate limiting
Whitelisting
Anti-patterns
❌ No validation
❌ Silent failure
❌ Return nothing
❌ Complex nested return
Áp dụng ngay
Bài tập 1: Viết 3 tool function (30 phút)
Bài tập 2: Pair với schema (15 phút)
Tóm tắt
Bài tiếp theo
6.32 - Tool functions — Python code Claude sẽ gọi​
Modified April 20
Bài 6.32: Tool functions — Python code Claude sẽ gọi​
Module: 5 — Tool Use​
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
✅ Viết tool function theo best practices: descriptive names, validation, error messages​
•
✅ Hiểu Claude "thấy" error → tự retry với corrected params​
•
✅ Viết 3 function mẫu: datetime, duration, reminders​
•
✅ Connect function với schema​
Mở đầu: Function đơn giản nhưng cần robust​
Tool function là Python function bình thường — nhưng có 2 khác biệt:​
1.
Caller là Claude, không phải dev — params có thể "kỳ quặc", need validation​
2.
Error visible to Claude — Claude có thể retry nếu error clear​
Best practices​
1. Descriptive names​
​
Code block​
Python
Copy
# ❌​
def f(x, y): ...​
​
# ✅​
def get_current_datetime(date_format): ...​
def calculate_shipping_cost(weight, destination): ...​
​
​
Tên function + param phải tự-documenting.​
2. Validate inputs​
Comments (0)
Help Center
Keyboard Shortcuts
