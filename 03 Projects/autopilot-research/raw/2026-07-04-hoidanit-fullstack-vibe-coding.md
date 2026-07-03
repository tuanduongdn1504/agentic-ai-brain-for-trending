# Raw source — Hỏi Dân IT "Fullstack Vibe Coding với AI" series, video #4 (backend NestJS + database)

> **Ingested:** 2026-07-04 (path 5 yt-dlp, operator-submitted URL)
> **Video:** https://www.youtube.com/watch?v=tD0Uve-0Ltk
> **Title:** #4. Dự Án Backend Nestjs & Database | Series Fullstack Vibe Coding với AI Dành Cho Beginner
> **Channel:** Hỏi Dân IT (@hoidanit, UCVkBcokjObNZiXavfAE1-fA) — 74,600 subs per yt-dlp at fetch (⚠️ reported; see provenance)
> **Uploaded:** 2026-07-01 · 1:33:39 · 1,425 views / 32 likes at fetch (edited livestream; live schedule = Monday 19:30)
> **Captions:** Vietnamese auto-subs (1.2MB VTT → deduped ~110K-char transcript, read in full by digest agent; EN track HTTP 429)
> **Transcript working copy:** scratchpad `transcript-vi.txt` (session-local; not committed — 110K chars)

## Series (playlist PLPTXD_6Mbmh4, all fetched via yt-dlp 2026-07-04)

| # | ID | Title | Date | Length | Views |
|---|----|-------|------|--------|-------|
| 1 | YBGwecf3NOw | Tôi Vibe Coding Để Tự Động Hóa Công Việc? Trả Lời Những Câu Hỏi Thường Gặp Của Beginners | 2026-06-10 | 1:16:32 | 1,373 |
| 2 | FQ1a4np7blk | Ý Tưởng Dự Án Thực Hành & Lựa Chọn Công Cụ Coding với AI | 2026-06-17 | 1:39:02 | 1,669 |
| 3 | osISSsyTJJ8 | MVP & Setup Môi Trường & Dự Án Frontend | 2026-06-24 | 1:27:32 | 1,337 |
| 4 | tD0Uve-0Ltk | Dự Án Backend Nestjs & Database | 2026-07-01 | 1:33:39 | 1,425 |

(Playlist item 5 = nOm04GgBLfI "OpenAI Codex Practical Coding Course… Results Demo" 10:30 — course promo, not a series episode. Flat-playlist fetch showed video 1 with an auto-translated English title; direct fetch shows the Vietnamese original.)

## Original resources (deep-dive layer)

1. **Course Google Doc** (in every video description): `docs.google.com/document/d/13sSoDBvFItcvH5BPwkeh8IQ8basnd7UgymQZx8maM9U` — fetched via `/mobilebasic` (export?format=txt 401s). Structure: About Author + Video 1–5 sections. Verbatim pins: "Chọn AI (chi phí sử dụng): Github Copilot (15$) và Gemini" · "Cài chính xác Node.js version 24" + nodejs.org/download/release/v24.14.0/ · "npm i -g @nestjs/cli@11.0.23" · MySQL Workbench username/password · "Lịch livestream trên kênh youtube Hỏi Dân IT: tối thứ 2 hàng tuần, từ 19h30". Starter repos distributed via **Google Drive** (frontend + backend), not GitHub. Video 5 (planned): React fundamentals & thinking (react.dev/learn/thinking-in-react linked).
2. **NestJS docs** (docs.nestjs.com; SPA — fetched via migration-guide + search): NestJS 11 requires Node ≥ 20, Express 5 default adapter.
3. **React docs** (react.dev/learn/creating-a-react-app): frameworks Next.js / React Router / Expo (+ TanStack Start beta, RedwoodSDK); from-scratch via Vite / Parcel / RSbuild; CRA absent from the page.
4. **hoidanit.vn** (direct fetch 403; identity via hoidanit.vn/about search snippets): Eric = founder, ex-HUST software engineer, 5+ yrs stock/banking/finance, freelancer; skills React/Angular/Vue, Express/NestJS/Spring/Laravel, React Native, SQL/NoSQL. Catalog includes ChatGPT+Codex, Claude Code ("thực chiến"), Claude AI zero, Antigravity coding courses.
5. **Node.js release** v24.14.0 — release dir HTTP 200 (real release).

## Digest (agent-read full transcript; EN structured extraction)

### Teaching thesis
- Sequential phases: copy knowledge (foundations) → iterative practice loop. AI = helper, **not** substitute for official docs.
- Two stated reasons NOT to let AI init a project: (1) AI depends on training data (may be stale); (2) official docs are tested cross-platform (Win/Mac/Linux), AI scaffolds are not guaranteed to be.
- "Run it first, understand internals later" (motorcycle analogy: ride before disassembling the engine).
- Frontend first (visible rewards motivate beginners) → backend → integration.

### Video 4 workflow (as demonstrated)
1. `npm i -g @nestjs/cli@11.0.23` (pinned) → verify `npm list --global --depth=0`
2. `nest new backend-nestjs-hoi-it` (npm; ESLint+Prettier yes)
3. Adjust package.json script naming to match frontend convention (`npm run dev` for watch mode)
4. `npm install` → 22-package vulnerability warning — explicitly triaged as ignorable in learning context
5. `npm run dev` → **TypeScript compilation error** (43:00 chapter "Fix lỗi typescript") → error pasted into AI (captions: "Clot Code" ≈ Claude Code, 95% confidence) → multiple suggestion iterations, partial fixes (baseUrl/dist issues) → resolved via version pin (5.9.3); exact garbled sequence in captions mixes TS and ESLint version numbers (see corrections)
6. Hello World verified at localhost:3000 (`src/app.service.ts`)
7. VS Code tsconfig warning explained: VS Code-bundled TS 6.0.3 vs project TS 5.9.3 = UI-level mismatch, not a code error ("not the machine broken; software version mismatch")
8. Database section: SQL-vs-NoSQL (claim: SQL covers ~90% of problems), MySQL + Workbench, port 3306 (Postgres 5432 alt), Docker deferred to a deploy series
9. React docs tour: react.dev, React 19 (19.0→19.2 "over ~2 years"), .jsx/.tsx, framework-vs-library, React-before-Next.js ("bicycle before big bike")

### Teachings (transferable)
- **Docs-first-AI-second**: init/setup from official docs; AI for error fixing; verify each AI suggestion empirically ("AI is helper, not oracle").
- **Error triage**: INFO (white) / WARNING (yellow — ignorable while learning) / ERROR (red — app won't start, act now). Anti-panic training for beginners.
- **Version pinning**: exact pins (Node 24.14.0, CLI 11.0.23) so cohort + AI suggestions stay reproducible; copy exact version strings, don't run `@latest`.
- **Read-old-docs skill**: version dropdown in docs; real jobs maintain old versions, not greenfield latest.
- **File extensions as self-documentation**: .jsx vs .tsx.

### Notable quotes (VN + EN, from transcript)
- [00:13:06] "Bởi vì không phải cái gì AI nó cũng biết. AI thì nó phụ thuộc vào data, nó training." — "AI doesn't know everything. AI depends on its data, its training."
- [00:18:58] motorcycle/ride-first quote (pedagogy anchor)
- [00:40:50] open-source outdated-package warnings normalized in learning context
- [01:06:27] "Khoảng 90% … SQL nó đã giải quyết được … 10% … no SQL" — 90/10 SQL/NoSQL claim
- [00:57:08] "Không phải rằng là máy của chúng ta lỗi đâu mà do cái phần mềm nó bị vênh cái version thôi." — version-mismatch root-cause teaching

### Caption garbles noted by digest agent
"Nets/NJS"→NestJS · "máy SQL"→MySQL · "Clot Code"→Claude Code (95%) · "BGress"→PostgreSQL · "ESN"→ESLint · "React Dock/TikTok"→Tic-Tac-Toe · ESLint-vs-TypeScript version numbers cross-contaminated around 43:00–52:25 (5.9.3 is a real TypeScript version; treat ESLint specifics as UNRELIABLE) · Playwright "63M/wk downloads" reported-only.

### Series project (from Google Doc, authoritative)
"Hệ thống web thương mại điện tử kết hợp AI Agent hỗ trợ tư vấn sản phẩm" — e-commerce with an AI product-consultation agent; buyer pages (listing/details/cart/checkout) + admin (users/products/orders). Stack: React (pure) + TypeScript / NestJS / MySQL. Budget AI stack for students: GitHub Copilot ("15$" per doc — see corrections) + Gemini; instructor's other courses cover Claude Code / Antigravity / Codex.

<!-- compiled: 2026-07-04 -->

---

## Episodes 1–3 digests (deepening pass, workflow wf_8bf5253d-aa2, 2026-07-04 — VN auto-subs fetched + read in full by digest agents)

### Ep 1 (YBGwecf3NOw) — beginner Q&A
- Product-first stance: beginners say "I want to automate my work" (vague); Eric's diagnostic: "bây giờ các bạn muốn xây sản phẩm gì?" — WHAT product (desktop/web/mobile) must be decided by the human; scope cannot be delegated to AI.
- Delegate to AI: implementation of the tool once scoped. Do NOT delegate: scope/requirements, prompt copy-paste without understanding, language choice by trend.
- Ethics: "Fair Play" — use official Graph API not scraping; know platform-ban implications.
- Language recommendation: JavaScript + TypeScript pair (one language, both ends); PHP aging; Python = backend-only trap for beginners wanting UI.
- Pragmatic close: "Anyway thì cứ dùng thôi bạn. Nếu mà nó đáp ứng được cái nhu cầu bài toán của bạn thì ok. Còn không ok thì chúng ta move on."
- Series-scope claim [~3:26 in ep4 per first digest]: ~20–50 videos planned, ~1/week, vs a prior ~100-video series ("Booking Care") — CAPTION-DERIVED, treat as approximate.
- ⚠️ digest-agent confabulation caught: ep1 digest wrote "5M+ subscribers" — contradicts yt-dlp ground truth (74.6K); DISCARDED. Also ep1 digest said live "Tuesdays 7:30 PM" vs course-doc "Monday 19:30" vs ep4-digest "Tue+Thu" — caption-derived day conflicts; the doc's own claim (Monday 19:30) stands as the doc's claim; uploads land Wednesdays.

### Ep 2 (FQ1a4np7blk) — project idea + AI tool selection (HIGH VALUE)
- Project chosen by community survey (most-voted: e-commerce); alternatives considered: stock-exchange dashboard (Socket.IO complexity), banking mini-games, EV-charging mgmt, e-learning LMS, and an AI product-consultation chatbot ("agent hỗ trợ tư vấn sản phẩm" — noted as requiring MCP integration against a real backend). Phase-based delivery model declared.
- AI tools compared: GitHub Copilot, Google Gemini, Codex/ChatGPT, Claude Code. **On-camera statement: Claude Code is currently the best ("xịn sò con bò nhất") — "nhưng không biết tháng sau tuần sau có thay đổi không"** — yet the series picks **Copilot + Gemini**: "chọn cái phổ biến, an toàn" (popular + safe + findable docs/mentorship for beginners).
- Antigravity 2.0 reviewed as DISAPPOINTING ("thất vọng") — dismissed as a Cursor clone despite Google's resources. Cursor recommended over Antigravity. JetBrains = paid/legacy option.
- Anti-tool-mystification: "Các ông đừng có quan trọng hóa cái việc rằng là tôi phải dùng công cụ này công cụ kia."
- Framework comparisons with popularity numbers (caption-derived): React vs Vue vs Angular/Svelte/Alpine/HTMX/Solid — React wins on popularity + job market; NestJS vs Express/Fastify/Hono — NestJS balances learning curve vs config overhead; **Next.js explicitly rejected for this project: "spaghetti"** (mixing front/back logic).
- Balance principle: "simple frontend ⇒ we can afford a complex backend".

### Ep 3 (osISSsyTJJ8) — MVP scoping + frontend init
- MVP = proof-of-workflow, core features only; cost-driven ("tiền chính là yếu tố sống còn"); version-1→N iteration; "không full topping từ ngày 1"; Shopee = version-N product.
- MVP scope: frontend 4 pages (listing / detail / cart / checkout) + backend 2 modules (inventory / orders). Deferred: auth (OPTIONAL!), online payment (COD first), reviews, discounts, campaigns, deployment (skipped; existing tutorials).
- **THIRD docs-first reason stated here: token/cost efficiency — AI init generates many files = high token cost.** (Ep4 gave staleness + cross-platform; ep3 adds cost.)
- Frontend stack detail: Vite (Evan You; CRA unmaintained; ~81K stars caption-derived), vanilla CSS first (NO Tailwind for beginners; AntD/shadcn/Chakra later), React Context (no Redux/Zustand), Fetch API (no Axios/React-Query).
- Database: MySQL (his 7-month-old setup tutorial reused; Docker avoided for simplicity).
