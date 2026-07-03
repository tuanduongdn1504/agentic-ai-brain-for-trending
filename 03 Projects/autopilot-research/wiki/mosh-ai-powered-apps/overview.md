# Overview — Mosh's "Build AI-Powered Apps"

## Source

- Video: https://www.youtube.com/watch?v=PtETUYa3i2Q — "AI Course for Developers – Build AI-Powered Apps with React", uploaded 2025-08-25, 2:25:39, ~161.9K views / 4.2K likes as of 2026-07-03
- Channel: **Programming with Mosh** (Mosh Hamedani), **5.09M subscribers** — the largest-channel FIRST-PARTY source ingested into this wiki so far (JSM was 1.25M)
- Full course: https://codewithmosh.com/p/build-ai-powered-apps (via mosh.link/build-ai-powered-apps)
- Course code (public, unpaywalled): https://github.com/mosh-hamedani/ai-powered-apps-course

## What it is

- The **free first ~2h25m of a 7-hour paid course** (120 lessons, 8 sections). The YouTube cut ends exactly where the chatbot frontend build begins.
- Positioning: *"every software engineer will be expected to know how to work with AI models just like we're expected to work with databases today"* — AI-features-as-baseline-skill, not AI research.
- Structure of the free half: foundations (LLMs, tokens, context windows, model selection, settings) → full-stack scaffold (Bun monorepo + Express + React/Vite + Tailwind + shadcn/ui + Prettier/Husky) → theme-park chatbot ("WonderWorld") with conversation state, Zod validation, error handling → **clean-architecture refactor** (repository/service/controller/routes).
- Author: Mosh Hamedani — 20+ years software engineering (verified: Microsoft certifications 2004–2008, official "I've spent 20+ years in the industry"), codewithmosh.com school (launched 2016, ~52 courses, subscription $29/mo or $149/yr). **This is his first AI/LLM course**; a separate "Claude Code for Professional Developers" course (9h) now appears in his catalog (reported from course-page fetch).

## Why it matters for this vault

- **Goal #2 bullseye, implementation-grade:** [[external|Storm Bear: hireui]] is a React SaaS with **zero LLM integration** ([[openai-to-claude-mapping]] maps every pattern to the Claude stack). Where [[external|Storm Bear: ai-engineering]] (Chip Huyen) is the conceptual assembly diagram, Mosh's course is the *typed-out Express/React implementation* of its first third — and the paid half's **review summarizer** is exactly the "AI insight over user-generated text" archetype a recruitment SaaS needs (candidate-feedback summarization).
- **The refactor IS the payload.** The course's layered architecture exists explicitly so the LLM call is swappable (*"switchable to Gemini/other LLMs without controller changes"*). That makes the course's pattern directly reusable Claude-side: swap one service file. See [[layered-architecture-refactor]].
- **Corpus contrast:** the JSM build-alongs ([[external|Storm Bear: jsm-six-file-context]]) teach *AI-assisted coding* (agent writes the app); Mosh teaches *AI-powered apps* (you write an app that calls models). Same mega-educator tier, opposite direction of the AI relationship. Mosh appeared once before in the corpus (codex topic, "Mosh implicitly says Claude wins" in a Codex-vs-Claude comparison bundle).

## Key Takeaways

- Free video = first 2h25m of a 7h/120-lesson course; the **complete course code is public on GitHub despite the course being paid** (freemium-code model).
- Teaches the OpenAI **Responses API** (not Chat Completions): `client.responses.create`, `output_text`, `previous_response_id` conversation chaining.
- Model guidance is decision-framework-first: "there is no best model" — 6 criteria (intelligence, speed, modality, cost, context window, privacy).
- Engineering discipline is half the course: env vars, .env.example, Zod validation, try/catch JSON errors, Prettier, Husky pre-commit, layered refactor.
- The architecture lesson ("repository = data access, service = LLM logic, controller = HTTP, never leak the OpenAI response shape") is vendor-independence by construction.
- Paid-only sections: prompt engineering (32m), review summarizer project (2h, with Prisma + MySQL), open-source models via Ollama + Hugging Face (28m).
