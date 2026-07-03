# OpenAI → Claude Mapping (the course, translated to the operator's stack)

> Every OpenAI pattern the course teaches, mapped to its Claude Messages API equivalent (verified against Anthropic's current SDK reference, 2026-07-03). This is the file that turns the course into a hireui-ready spec.

## Call-level mapping

| Course (OpenAI, Aug-2025) | Claude equivalent (2026) | Notes |
|---|---|---|
| `client.responses.create({model, input})` | `client.messages.create({model, max_tokens, messages:[{role:'user',content}]})` | `max_tokens` is **required** on Claude |
| `instructions` param | top-level `system` param | Same role; cache it (`cache_control`) |
| `response.output_text` | `response.content` blocks — filter `type === 'text'` | Guard by block type |
| `temperature` 0–2, 0.7 default | 0–1 on legacy models; **removed** on Fable 5 / Opus 4.8/4.7 / Sonnet 5 (400 if sent) | Steer with prompts + `output_config.effort` |
| `max_output_tokens` | `max_tokens` | Same truncation caveat; check `stop_reason === 'max_tokens'` |
| `stream: true` + `response.output_text.delta` events | `client.messages.stream()` + `text_stream` / `content_block_delta`; `finalMessage()` helper | Same async-iterable shape |
| JSON schema text format (Structured Outputs) | `output_config: {format: {type:'json_schema', schema}}` or `messages.parse()` + `zodOutputFormat` (TS) | The course already uses Zod — same schemas reuse |
| `store: true` + dashboard logs | No server-side transcript store; org-level retention config; Console usage | Privacy criterion flips in Claude's favor for sensitive data |
| js-tiktoken token counting | `POST /v1/messages/count_tokens` | **Never tiktoken for Claude** (undercounts 15–20%) |
| GPT-4o mini / GPT-4.1 / o3 tiers | Haiku 4.5 ($1/$5) / Sonnet ($3/$15) / Opus 4.8 ($5/$25 per 1M) | Same 6-criteria framework applies |

## Conversation state — the one structural difference

- **OpenAI (course):** server-side state; store only `Map<conversationId, lastResponseId>`; pass `previous_response_id`. OpenAI holds the transcript (30-day default).
- **Claude:** **stateless** — resend full history each turn (`messages` array). The repository stores the *transcript*, not a pointer:
  - `conversation.repository.ts` becomes `getMessages(conversationId)` / `appendMessage(conversationId, msg)` — same layer, different payload.
  - Cost is equivalent, not worse: OpenAI's chaining **also bills all previous input tokens** (verified from OpenAI's own guide). On Claude you claw most of it back with **prompt caching** — breakpoint on the last turn ⇒ prior history reads at ~0.1×.
  - Upside: your DB owns the transcript (audit, GDPR deletion, analytics); no 30-day vendor TTL semantics.

## The port, concretely

The course's own architecture confines the work to one seam ([[layered-architecture-refactor]]):

```ts
// packages/server/llm/client.ts — Claude provider
import Anthropic from '@anthropic-ai/sdk';
const client = new Anthropic(); // ANTHROPIC_API_KEY from env

export async function sendMessage(history: MessageParam[], system: string) {
  const response = await client.messages.create({
    model: 'claude-opus-4-8',
    max_tokens: 1024,
    system: [{ type: 'text', text: system, cache_control: { type: 'ephemeral' } }],
    messages: history,            // full history — cached prefix makes this cheap
  });
  const text = response.content.find(b => b.type === 'text')?.text ?? '';
  return { id: response.id, message: text };   // same ChatResponse shape
}
```

Controller, routes, Zod schemas, frontend: unchanged. Error handling gains Claude's typed exceptions (`RateLimitError` → 429 path, `APIStatusError`) and `stop_reason` branches (`max_tokens`, `refusal`).

## Key Takeaways

- The course is ~90% vendor-neutral by construction; the OpenAI-specific 10% (state chaining + sampling params + output shape) all lives behind the service seam.
- The Zod skills transfer twice: request validation (unchanged) and structured outputs (`zodOutputFormat`).
- Claude's missing "logs dashboard" is a feature under the course's own privacy criterion; observability instead via usage fields + [[external|Storm Bear: claude-code-observability]] patterns.
- For hireui's first LLM feature, this file + [[chatbot-validation-and-errors]] + the cost-optimization spec (`claude-api-cost-optimization`) compose into a complete build recipe.
- Cross-links: [[calling-models-responses-api]], [[the-originals]], [[external|Storm Bear: claude-api-cost-optimization]], [[external|Storm Bear: cowork-third-party-inference]].
