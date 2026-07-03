# The Layered-Architecture Refactor

## Source

Video PtETUYa3i2Q, chapters "Refactoring the Chat API" (2:01:52) → "Extracting Routes" (2:20:03). Repo ground truth: `packages/server/repositories/conversation.repository.ts`, `services/chat.service.ts`, `controllers/chat.controller.ts` (all confirmed via gh api).

## The four layers (extracted live from one index.ts)

| Layer | File | Responsibility | Knows about |
|---|---|---|---|
| **Repository** | `repositories/conversation.repository.ts` | Data access — `getLastResponseId(conversationId)` / `setLastResponseId(conversationId, responseId)`; the `Map` stays private | Storage only |
| **Service** | `services/chat.service.ts` | Application/LLM logic — `sendMessage(prompt, conversationId): Promise<ChatResponse>`; calls OpenAI, updates repository | Repository + LLM SDK |
| **Controller** | `controllers/chat.controller.ts` | HTTP gateway — Zod-validate, extract, call service, shape response, try/catch | Service + HTTP |
| **Routes** | `routes.ts` | Endpoint registration — `express.Router()`, `router.post('/chat', chatController.sendMessage)`, `app.use(router)` in index.ts | Controller |

Dependency direction: Controller → Service → Repository — never reversed.

## The two load-bearing rules

1. **Encapsulation ("remote-control" metaphor):** expose buttons, hide the circuit board. The Map is invisible outside the repository — swap memory → database (the paid course's Prisma section) and only one file changes.
2. **No leaky abstractions:** the service returns a **platform-agnostic** `interface ChatResponse { id: string; message: string }`, mapping the OpenAI response into it — *"makes the service switchable to Gemini or other LLMs without controller changes."* The raw vendor response never crosses the service boundary.

## Why this is the payload of the whole course

- The refactor makes **vendor-independence a structural property**: the OpenAI-specific surface area is confined to the service (and in the full repo, further isolated into `llm/client.ts` — the repo supports OpenAI + Ollama + Hugging Face behind that one seam).
- Consequence for this vault: **porting the course's app to Claude is a one-file change** — reimplement the LLM client with `@anthropic-ai/sdk` and keep controller, routes, validation, and frontend untouched. [[openai-to-claude-mapping]] specifies exactly that file.
- This is the same "own the seam, not the vendor" thesis as BYOA/BYOM elsewhere in the corpus ([[external|Storm Bear: open-design]] bring-your-own-agent; [[external|Storm Bear: omnilogin-ai-coding]] bring-your-own-model) — here taught as classic backend architecture.

## Key Takeaways

- Repository/service/controller/routes with strict dependency direction, extracted stepwise on camera — the clearest beginner walkthrough of the pattern in the corpus.
- The platform-agnostic ChatResponse interface is the single highest-leverage line for a Claude shop reading an OpenAI course.
- In-memory Map is explicitly a placeholder; persistence is a repository-only change (Prisma+MySQL in the paid half).
- VS Code mechanics taught alongside (multi-cursor rename `Shift+Cmd+L`) — Mosh's signature tooling-fluency thread.
- Cross-links: [[chatbot-validation-and-errors]] (pre-refactor state), [[the-originals]] (post-refactor repo), [[external|Storm Bear: ai-engineering]] (Ch.9-10 production architecture as this pattern's grown-up form).
