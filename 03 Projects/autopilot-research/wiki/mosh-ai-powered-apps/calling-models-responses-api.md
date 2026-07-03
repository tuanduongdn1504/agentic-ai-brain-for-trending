# Calling Models — the OpenAI Responses API

## Source

Video PtETUYa3i2Q, chapters "Calling Models" (39:32) + "Managing Conversation State" (1:47:22). Transcript read directly; repo ground truth `packages/server/llm/client.ts` (openai@5.8.2); OpenAI conversation-state guide fetched 2026-07-03.

## The basic call (as taught)

```ts
import OpenAI from 'openai';
const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const response = await client.responses.create({
  model: 'gpt-4.1',
  input: 'write a story about a robot',
  temperature: 0.7,
  max_output_tokens: 50,
});
console.log(response.output_text);
```

- `response.output_text` = the generated text; `response.usage` = token counts; `response.id` = the unique response identifier that later powers conversation state; `store` defaults true (logged server-side, 30-day retention).
- API keys: create per-project keys in the dashboard; **never in source code** — `.env` (gitignored) + `.env.example` (committed, names only); `require('dotenv').config()` before anything reads `process.env`.

## Streaming

- `stream: true` → returns an **async iterable** of events instead of a response object; `for await (const event of stream)`.
- Text chunks are `response.output_text.delta` events with a `delta` property (plus sequence numbers); not every event has a delta — guard before printing; use `process.stdout.write(event.delta)` (console.log adds newlines).

## Conversation state (the free half's core lesson)

1. **Problem:** the API has no memory — "what was my previous question?" fails.
2. **Step 1 (naive):** module-level `let lastResponseId: string | null`; pass `previous_response_id: lastResponseId` into `responses.create`; update after each response. Works for exactly one global conversation.
3. **Step 2 (real):** `const conversations = new Map<string, string>()` mapping **conversationId → lastResponseId**. Client generates a GUID per conversation (like ChatGPT's URL); server does `conversations.get/set`. Memory-only — "real applications store this in a database" (the paid course's Prisma section).
4. OpenAI stores the actual transcript server-side; your app only stores the pointer.

## 2026 status (ground-checked directly)

- `previous_response_id` **still documented** in OpenAI's conversation-state guide (a workflow dive-agent claimed it was removed — overridden; see [[source-provenance]]).
- The newer **Conversations API** (durable `conversation` objects, no 30-day TTL) is now the recommended durable-state approach, working *with* the Responses API — chaining is for lightweight cases.
- **The cost caveat the video never mentions:** *"Even when using previous_response_id, all previous input tokens for responses in the chain are billed as input tokens."* The pattern saves **code**, not **money** — cost grows with conversation length exactly as if you resent history yourself.

## Key Takeaways

- Responses API core loop: `responses.create({model, input, ...})` → `output_text` → chain by `previous_response_id`.
- The Map<conversationId, lastResponseId> pattern is a **server-side-state convenience unique to OpenAI**; Claude's Messages API is stateless — you resend history and make it cheap with prompt caching (see [[openai-to-claude-mapping]] for the full translation).
- Chained conversations bill full history as input tokens on both vendors — caching (OpenAI automatic; Claude `cache_control` ~0.1× reads) is where the actual savings live: [[external|Storm Bear: claude-api-cost-optimization]].
- Streaming = async-iterable deltas on both vendors; Claude's SDK adds `text_stream` / `finalMessage()` helpers.
- Cross-links: [[chatbot-validation-and-errors]] (where this call gets wrapped), [[layered-architecture-refactor]] (where it gets encapsulated).
