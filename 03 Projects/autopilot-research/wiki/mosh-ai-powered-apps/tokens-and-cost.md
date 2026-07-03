# Tokens & Cost

## Source

Video PtETUYa3i2Q, chapters "Understanding Tokens" (18:37) → "Counting Tokens" (21:40). Verified against openai/tiktoken, dqbd/tiktoken, OpenAI token-counting guide.

## Tokens

- Tokens are subword units — whole words, word fragments, punctuation, spaces, emojis. Models process tokens, not text.
- Video demo: OpenAI's interactive tokenizer (platform.openai.com/tokenizer); example text of 252 characters → 53 tokens (~4.75 chars/token — verifier reproduced the ratio with cl100k_base; plausibility-confirmed, not the exact demo text).
- Folk rules (~1 token ≈ 4 chars ≈ 0.75 English words) are **explicitly discouraged by OpenAI today** — the docs recommend real token counting; ~4 bytes/token is the empirical average.

## Counting tokens in code (as taught)

- Library: **js-tiktoken** (`npm install js-tiktoken`) — `import { getEncoding } from 'js-tiktoken'`, `getEncoding("cl100k_base").encode(text)` → array of token IDs.
- **Correction (verified):** encoding name is lowercase `cl100k_base`; and js-tiktoken is the **community port by dqbd** (dqbd/tiktoken, ~1.1K★) — OpenAI's official tiktoken is Python/Rust only.
- Needs `"type": "module"` in package.json for ESM imports.
- ⚠️ **Claude-side rule:** never use tiktoken for Claude — it undercounts by ~15–20%. Use `POST /v1/messages/count_tokens`. See [[openai-to-claude-mapping]].

## Cost & context windows (as taught, Aug-2025 numbers)

- Pricing is per-token, input and output priced separately; long documents (contracts etc.) make cost add up fast.
- The 13× spread: **GPT-4o mini $0.60 vs GPT-4.1 $8.00 per 1M output tokens** — confirmed against Aug-2025 OpenAI pricing (operator knowledge; the verifier for this claim died mid-run). **Historical** — neither model is in OpenAI's 2026 lineup ([[caveats-and-corrections]]).
- Context window = prompt + response + conversation history, all inclusive. Examples taught: GPT-4o mini ~128K (verified), GPT-4.1 ~1M (verified real at video time — see the misfire note in [[caveats-and-corrections]]), Mistral ~32K (verified — Mistral-7B v0.2 model card).
- Decision rule: don't default to the largest context/most powerful model — "Mistral is sufficient for summarizing blog posts or classifying tickets."

## Key Takeaways

- Token economics is a first-class engineering input, not an afterthought — the same thesis as [[external|Storm Bear: claude-api-cost-optimization]], taught here at beginner level.
- The 13×-by-model-choice lever is the cheapest optimization in existence (choose the model before optimizing anything else). Claude-side equivalent spread today: Haiku 4.5 $5 vs Opus 4.8 $25 per 1M output = 5×; plus prompt caching (~0.1× reads) and Batches (50%) stack on top.
- Exceeding the context window stops output mid-sentence — the failure mode Mosh demonstrates with max_tokens, and one Claude reports explicitly via `stop_reason` values.
- Cross-links: [[choosing-models-and-settings]] (the other 5 selection criteria), [[calling-models-responses-api]] (the hidden cost of conversation chaining).
