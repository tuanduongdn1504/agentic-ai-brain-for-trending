# The Originals — Paid Course + Public Repo

> Per the operator's "double deep-dive into the original resource" convention, the deep-dive targets behind the free video are (1) the paid course and (2) its public GitHub repo.

## Original 1 — the paid course

- **"Build AI-Powered Apps – An AI Course for Developers"** — https://codewithmosh.com/p/build-ai-powered-apps
- **7 hours, 120 lessons, 8 sections** (fetched 2026-07-03): Getting Started (7m) · Introduction to AI Models (40m) · Setting Up a Full-Stack Project (51m) · Building a Chatbot (2h) · **Prompt Engineering (32m)** · **Review Summarizer (2h)** · **Open Source Models (28m)** · Wrap Up (1m)
- The free YouTube video ≈ the first three sections + most of Building a Chatbot (ends as the frontend begins). Paid-only: prompt engineering, the second project, open-source models.
- **Pricing:** no per-course price displayed; codewithmosh.com is subscription all-access — **$29/month or $149/year**, 30-day money-back (verified via pricing page + author dive). Also sold per-course on Udemy.
- Prerequisites: modern JS/TS + basic React; backend/DB helpful, no AI experience needed.
- Catalog context: Mosh's **first AI/LLM course** among ~52 courses; a **"Claude Code for Professional Developers" (9h)** course now also appears in the catalog (reported from homepage fetch 2026-07-03) — the mega-educator tier is now teaching the operator's daily tool.

## Original 2 — the public repo (the paid course's code, free)

- **`mosh-hamedani/ai-powered-apps-course`** — created **2025-08-18** (one week before the video), **145★ / 80 forks**, TypeScript, **NO LICENSE file** (⚠️ default copyright — reference, don't redistribute).
- README names the course + links codewithmosh.com/p/build-ai-powered-apps — confirmed official.
- **Architecture (verified file-by-file):**
  - Bun monorepo: `packages/client` (React 19 + Vite + Tailwind + **React Query**) + `packages/server` (Express + TS)
  - `packages/server/llm/client.ts` — **openai@5.8.2**, Responses API: `model, input, instructions, temperature, max_output_tokens, previous_response_id`
  - `repositories/conversation.repository.ts` — in-memory Map, `getLastResponseId`/`setLastResponseId`
  - Controllers → services → repositories layering exactly as taught
  - **WonderWorld** theme-park chatbot (the imaginary park from the course intro)
  - **Review summarizer** with **Ollama (tinyllama)** + **Hugging Face Inference** support — multi-LLM behind the `llm/client.ts` seam
  - **Prisma ORM + MySQL** for persistence (the "repository → database" payoff)
- **The notable business observation:** the complete paid-course code is public and unpaywalled — the course sells the *walkthrough*, not the artifact. (Freemium-code pattern; sister observation to JSM's public repos for free videos, but here it's the PAID course's code.)

## Key Takeaways

- The repo is the fastest way to consume the paid half without buying it: prompt-engineering usage, the review-summarizer implementation, the Ollama/HF multi-provider client, and Prisma persistence are all readable today.
- `llm/client.ts` supporting OpenAI + Ollama + HF confirms the vendor-seam design is real, not aspirational — adding Claude is adding one more provider to an existing seam.
- No license = code is look-but-don't-lift; patterns are freely learnable, files are not copy-paste-able into hireui.
- The review summarizer (paid section 6) is the highest-value target for the operator: user-review analysis ≈ candidate-feedback analysis, and it ships with DB persistence.
- Cross-links: [[overview]], [[layered-architecture-refactor]], [[openai-to-claude-mapping]].
