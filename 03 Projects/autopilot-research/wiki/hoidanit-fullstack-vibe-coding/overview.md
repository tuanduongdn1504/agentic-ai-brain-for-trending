# Overview — Hỏi Dân IT Fullstack Vibe Coding với AI (beginner series)

## Source
- Video #4: https://www.youtube.com/watch?v=tD0Uve-0Ltk (2026-07-01, 1:33:39, edited Monday-19:30 livestream) — raw: `raw/2026-07-04-hoidanit-fullstack-vibe-coding.md`
- Course doc: Google Doc `13sSoDBvFItcvH5BPwkeh8IQ8basnd7UgymQZx8maM9U` (fetched via mobilebasic)

## Who
- **Hỏi Dân IT** ("Ask People in IT") — Vietnamese commercial educator brand run by **Eric**: former HUST (Bách Khoa Hà Nội) CS student, 5+ years software engineering in stock/banking/finance, now freelancer + full-time educator (verified via hoidanit.vn/about snippets + Facebook askITwithERIC).
- Channel @hoidanit ≈ **74K subs** (yt-dlp + search corroborated). Sells courses at hoidanit.vn — including a **Claude Code course** (`claude-code-thuc-chien-tu-beginner-den-pro.html`, URL verified), ChatGPT+Codex, Claude AI zero, Antigravity courses.
- Positioning ≈ **the Vietnamese analog of Mosh-style commercial beginner education** — cf. [[mosh-ai-powered-apps/_index]] (largest-channel first-party corpus source): same archetype, VN market, 1/68th the audience.

## What the series is
- **"Fullstack Vibe Coding với AI Dành Cho Beginner"** — free weekly livestream series (4 episodes so far, Jun 10 → Jul 1 2026, all 76–99 min, ~1.3–1.7K views each), building one project across the series:
- **The project:** "Hệ thống web thương mại điện tử kết hợp AI Agent hỗ trợ tư vấn sản phẩm" — an e-commerce site **with an AI product-consultation agent** (buyer pages + admin panel). Stack: React (pure, not Next.js) + TypeScript · NestJS 11 · MySQL.
- **Student AI stack:** GitHub Copilot + Gemini (budget tier — see [[caveats-and-corrections]] on the doc's "15$"); the instructor drives **Claude Code** on-screen when fixing errors (caption-derived, high confidence).
- Episodes (all four transcripts read — #4 in the anchor pass, #1–#3 in the deepening pass `wf_8bf5253d-aa2`): #1 beginner Q&A (product-first boundary; JS+TS recommendation; Fair-Play/Graph-API ethics) · #2 project idea + AI tool selection (community survey; **on-camera "Claude Code is currently the best" — but popular-and-safe Copilot+Gemini chosen for beginners**; Antigravity 2.0 called disappointing; Next.js rejected as "spaghetti") · #3 MVP + env setup + frontend init (React+Vite; 4-page/2-module MVP; auth optional, COD-first) · #4 backend init (NestJS) + database (MySQL) · #5 planned: React fundamentals ("Thinking in React").

## Why it's corpus-notable
- **First Vietnamese-language first-party structured beginner series** in this wiki (prior VN sources: licensed dub, small third-party tutorials, blogs).
- **Sharpest instance of the vibe-branding / discipline-content inversion:** the series is *named* "vibe coding" but *teaches* [[docs-first-ai-second]], [[version-pinning-discipline]] and [[error-triage-and-warning-literacy]] — i.e., anti-vibe engineering discipline wearing the vibe-coding label for reach. (Relevant to Storm Bear Pattern #51 anti-vibe spectrum; also a pedagogy-tier counterpart to [[jsm-practical-vibe-coding/_index]]'s "practical vibe coding".)
- **Beginner pole of the corpus:** JSM teaches seniors spec-systems; Mosh teaches devs to build AI apps; this teaches *absolute beginners* to code **with** AI without being lied to by it — the missing pedagogical tier.

## Key Takeaways
- A "vibe coding" series that spends 93 minutes on version pins, docs reading, and warning triage is discipline education in disguise — the brand is acquisition, the content is engineering.
- Every load-bearing technical claim in episode 4 survived refute-first verification (NestJS 11 / Node ≥20 / Express 5 / CLI pin = npm `latest` / React 19.2.x / TS 6.0.x real) — rare for a beginner-tier source; see [[source-provenance]].
- The series project (e-commerce + AI consult agent) is the same *shape* as hireui's Goal-#2 first-LLM-feature ambition — a consumer-facing domain app with one scoped AI agent feature.
- Weekly livestream + one evolving Google Doc + Drive-distributed starters = a low-ceremony cohort teaching harness (no GitHub, no LMS).
