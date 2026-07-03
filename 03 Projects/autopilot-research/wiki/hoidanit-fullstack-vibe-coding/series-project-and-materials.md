# Series project & materials (e-commerce + AI consultation agent)

## Source
- Course Google Doc `13sSoDBvFItcvH5BPwkeh8IQ8basnd7UgymQZx8maM9U` (mobilebasic fetch, 2×) + video descriptions

## The project (doc verbatim)
> "Hệ thống web thương mại điện tử kết hợp AI Agent hỗ trợ tư vấn sản phẩm"
- An **e-commerce platform with an AI product-consultation agent**: buyer-facing product listing / detail / cart / checkout + admin panels (users, products, orders).
- Stack: React (pure) + TypeScript · NestJS 11 · MySQL — see [[tech-stack-rationale]].
- **The AI-agent feature is the series' end-boss** — episodes so far build the conventional substrate; the consult-agent build is still upcoming (the high-value future ingest for this topic).

## How the project was chosen (ep 2) and scoped (ep 3)
- **Community survey** picked e-commerce (most-voted); alternatives considered and deferred: stock-exchange dashboard (Socket.IO complexity), banking mini-games, EV-charging management, e-learning LMS — and the **AI product-consultation chatbot, noted as requiring MCP integration against a real backend** (it survives as the series' later-phase feature rather than the starting point).
- **MVP scope (ep 3):** frontend = 4 pages (listing / detail / cart / checkout); backend = 2 modules (inventory / orders). Explicitly deferred: **auth (optional!)**, online payment (COD first), reviews, discount codes, campaign mechanics, deployment. *"Không full topping từ ngày 1"* — cost-driven, phase-based versioning ("Shopee is a version-N product").

## Materials & distribution
- **One evolving Google Doc** per series: author bio, per-video sections, exact version pins ([[version-pinning-discipline]]), prerequisite links (W3Schools HTML/CSS, his own JS video, Git playlist, SQL crash course, MySQL setup guide), livestream schedule (Monday 19:30).
- **Starter projects via Google Drive** (frontend + backend zips) — not GitHub. Zero-GitHub, zero-LMS cohort infrastructure; the doc is the syllabus, the Drive is the registry.
- **Student AI stack (doc verbatim):** "Chọn AI (chi phí sử dụng): Github Copilot (15$) và Gemini" — a budget tier for students (but see [[caveats-and-corrections]]: Copilot Pro's published price is $10/mo). The instructor's other paid courses cover Claude Code, Antigravity, ChatGPT+Codex — and on-screen in #4 the error-fixing driver appears to be **Claude Code** (caption-derived).
- Backend test URL `http://localhost:3000/`; MySQL Workbench credentials required before backend episodes.

## Why this maps to hireui Goal #2
- Same shape as the operator's target: a conventional domain app (recruitment SaaS ↔ e-commerce) growing **one scoped LLM feature** (candidate consultation ↔ product consultation). The series will effectively publish a beginner-grade reference implementation of "add an AI consult agent to a CRUD app" on the exact stack family (React+TS+Node) hireui uses — worth tracking to completion; cf. [[mosh-ai-powered-apps/_index]] (the professional-grade version of the same arc) and [[ai-engineering/_index]] (the book-grade version).

## Key Takeaways
- The series project is declared up front in the doc — the AI agent is scoped as a *feature of a boring app*, not the app itself (the sanest beginner AI framing in the corpus).
- Doc + Drive + livestream = a complete cohort harness with zero developer-tooling overhead; portable to internal team training.
- Budget AI stack for students, premium stack for the instructor — cost-tiered tooling as explicit pedagogy (cf. [[claude-api-cost-optimization/_index]] tiering logic).
- Track episodes #5+ for the consult-agent build; that's when this topic earns a second compile cycle.
