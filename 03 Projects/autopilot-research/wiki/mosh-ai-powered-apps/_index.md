# mosh-ai-powered-apps — Topic Index

> **Topic:** Mosh Hamedani's "Build AI-Powered Apps" course — the free 2h25m YouTube half + double deep-dive into the paid course and its public GitHub repo
> **Source video:** [AI Course for Developers – Build AI-Powered Apps with React](https://www.youtube.com/watch?v=PtETUYa3i2Q) (PtETUYa3i2Q, Programming with Mosh, 2025-08-25, 2:25:39, ~162K views, 5.09M subs — **FIRST-PARTY**, biggest-channel first-party source in this wiki to date)
> **Compiled:** 2026-07-03 (path 5 yt-dlp + workflow `wf_05723834-938`, 28 agents)

## Articles

- [[overview]] — what the video/course is, who Mosh is, why it matters for this vault (hireui has no LLM yet)
- [[ai-engineering-foundations]] — AI engineer vs ML engineer, the database analogy, 6 real-world feature archetypes, LLM mental model
- [[tokens-and-cost]] — tokens, tokenizer, js-tiktoken, context windows, the 13× pricing spread, cost discipline
- [[choosing-models-and-settings]] — 6-criteria model decision framework + settings (temperature, top_p, max tokens, text formats)
- [[calling-models-responses-api]] — OpenAI SDK, Responses API, streaming, conversation state (`previous_response_id` → Map), 2026 status
- [[fullstack-scaffold-bun-monorepo]] — Bun workspaces, Express, Vite proxy, Tailwind, shadcn/ui, Prettier + Husky + lint-staged, dotenv
- [[chatbot-validation-and-errors]] — the chat API, Zod input validation, HTTP 400/500 error handling
- [[layered-architecture-refactor]] — repository → service → controller → routes; the leaky-abstraction rule; why the LLM swap becomes a one-file change
- [[the-originals]] — deep-dive: the paid course (7h/120 lessons/8 sections) + the PUBLIC repo `mosh-hamedani/ai-powered-apps-course`
- [[openai-to-claude-mapping]] — every OpenAI pattern in the course mapped to its Claude Messages API equivalent (the operator's stack)
- [[caveats-and-corrections]] — API drift since Aug-2025 (GPT-4.1/o3 gone, Conversations API), verifier misfires overridden, unverified items
- [[source-provenance]] — pipeline, workflow stats, verdicts, garble map, fail-loud log

## One-line thesis

A mega-educator (5.09M subs) teaching "AI features are the new database skills" — the free half builds an Express+React chatbot on the OpenAI Responses API with a clean repository/service/controller layering whose explicit purpose is **making the LLM vendor swappable**; the paid half (public code!) extends to prompt engineering, a review-summarizer (the exact Amazon-style feature), Prisma persistence, and Ollama/HF open-source models.
