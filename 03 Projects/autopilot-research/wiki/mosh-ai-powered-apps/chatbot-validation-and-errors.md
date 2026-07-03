# Chatbot API, Zod Validation & Error Handling

## Source

Video PtETUYa3i2Q, chapters "Project: Building a ChatBot" (1:37:53) → "Error Handling" (1:59:33). Transcript read directly (lines ~2440–2870 + reader extraction).

## The chat endpoint (v1, pre-refactor)

- `POST /api/chat` with `express.json()` middleware; body `{ prompt, conversationId }`.
- Model choice for the bot: **GPT-4o mini** (cost-efficiency), **temperature 0.2** (factual), **max_tokens ~100** — the [[choosing-models-and-settings]] framework applied, not just defaults.
- Tested with the **Postman VS Code extension** (raw JSON body; UUID Generator extension for conversation IDs; known pretty-tab refresh glitch — use raw tab).
- Conversation memory via the `Map<conversationId, lastResponseId>` pattern from [[calling-models-responses-api]].

## Input validation (Zod)

```ts
const chatSchema = z.object({
  prompt: z.string().trim()
    .min(1, 'Prompt is required.')
    .max(1000, 'Prompt is too long (max 1000 characters).'),
  conversationId: z.string().uuid(),
});
const parseResult = chatSchema.safeParse(req.body);
if (!parseResult.success) {
  return res.status(400).json(parseResult.error.format());
}
```

- The **max(1000) is a cost/DoS guard**, not just UX — unbounded prompts = unbounded token spend (the input-side twin of max_tokens).
- `.trim()` before min/max so whitespace-only strings fail validation.
- `safeParse` + `error.format()` → structured field-level 400s instead of throws.

## Error handling

- Whole handler wrapped in try/catch; catch → `res.status(500).json({ error: 'Failed to generate a response' })`.
- Demonstrated failure: invalid model name (`gpt-4o!`) — without the catch, Express returns an HTML stack trace to an API client; with it, clean JSON.
- Rationale list: network down, quota exceeded, model doesn't exist — LLM calls are **network calls** and fail like any other.

## Key Takeaways

- Boundary validation (Zod at the controller) + bounded prompt length + generic 500s = the minimum production posture for any LLM endpoint — directly portable to a Claude/Express route.
- Claude-side addition: also branch on typed SDK errors (`RateLimitError`, `APIStatusError`) and `stop_reason` (`max_tokens`, `refusal`) — richer failure taxonomy than the video's single catch. See [[openai-to-claude-mapping]].
- Zod here validates the **request**; the same library validates **LLM output** in structured-outputs workflows (`zodOutputFormat` in the Claude TS SDK) — one skill, both directions.
- Prompt-length caps are the first "cost discipline enforcement primitive" in a Storm Bear sense — cheap, boring, effective.
- Cross-links: [[layered-architecture-refactor]] (where the schema moves into the controller), [[external|Storm Bear: prompt-evaluation]] (testing what comes back).
