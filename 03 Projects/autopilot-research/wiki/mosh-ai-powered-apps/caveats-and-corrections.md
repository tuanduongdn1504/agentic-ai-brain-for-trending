# Caveats & Corrections

## API drift since the video (Aug-2025 → Jul-2026)

- **Model lineup:** GPT-4.1, GPT-4o, o3, o4-mini are **gone from OpenAI's current models page** — the 2026 lineup is GPT-5.5 / 5.4 / 5.4-mini / 5.4-nano (verified against developers.openai.com). Every concrete model name, price, and context-window number in the video is **historical**; the decision *framework* survives.
- **Conversation state:** `previous_response_id` chaining **still works and is still documented**, but the **Conversations API** (durable conversation objects, exempt from the 30-day response TTL) is now the recommended durable-state primitive. The video's Map pattern remains valid for lightweight cases.
- **Pricing:** the 13× example ($0.60 vs $8.00/1M output) was correct for Aug-2025; both models are now retired. The *lever* (model choice = order-of-magnitude cost swing) still holds on every vendor.

## Video-level caveats

- **Chained conversations are NOT free:** OpenAI bills all previous input tokens on every chained turn — the video presents `previous_response_id` purely as a convenience and never mentions its cost profile.
- **Dev-only scope:** no tests, no deployment, no production CORS/auth — the free half ends before any of that; the Postman checks are the only verification shown. (Same "discipline without test-verification" gap flagged across the JSM topics.)
- **In-memory state** is explicitly a placeholder (paid course adds Prisma).
- **Repo has NO LICENSE** — read for patterns, don't copy files.
- **store:true default** means prompts persist server-side at OpenAI unless disabled — relevant under the course's own privacy criterion.

## Verifier misfires overridden (main-loop ground checks — the recurring pattern)

1. **"GPT-4.1 never existed" (verify REFUTED → OVERRIDDEN):** a verifier read OpenAI's *current* 2026 docs and declared GPT-4.1 fictional. Ground truth: GPT-4.1 launched April 2025 with a 1M-token context window and was on the featured-models page (with o4-mini and o3 — exactly as the transcript describes) at video time. Correct verdict: CONFIRMED-at-video-time, retired since.
2. **"Temperature range is 0–1, claim refuted" (→ OVERRIDDEN):** the verifier cited *Anthropic's* docs against an *OpenAI* course. OpenAI's temperature range is 0–2 as taught. The vendor difference itself became a wiki fact ([[openai-to-claude-mapping]]).
3. **"previous_response_id no longer documented / deprecated" (dive agent → OVERRIDDEN):** direct fetch of OpenAI's conversation-state guide (2026-07-03) shows it fully documented alongside the Conversations API. Same misfire class as the "instructions param removed" claim — treat both as doc-navigation failures, not API facts.
4. **Critic's garble-table error:** the completeness critic listed "GPT-4.1" as a caption garble of GPT-4o. It isn't — GPT-4.1 was real ((1) above). Critics confabulate too.
5. **"Amazon review summaries UNVERIFIABLE" (→ CLOSED CONFIRMED):** verifier hit 403/503 walls; a plain web search finds Amazon's own Aug-2023 announcement (aboutamazon.com).

## Closed by operator knowledge (verifiers died mid-run, "Prompt is too long")

- GPT-4o mini $0.60 & GPT-4.1 $8.00 per 1M output (Aug-2025) — matches operator-known pricing tables exactly; flagged **historical-confirmed**.
- JSON-schema structured outputs exist — trivially real (OpenAI Structured Outputs, Aug-2024; Claude `output_config.format`).

## Reported-but-unverified (flag, don't quote as fact)

- "Claude Code for Professional Developers (9h)" in Mosh's catalog — single course-page fetch, not independently confirmed.
- Node 22.17 "latest" in-video — actually 22.18.0 was latest on upload day (v22.17.0 was ~2 months old); trivial, corrected.
- Video's tokenizer demo numbers (252 chars = 53 tokens) — ratio reproduced with cl100k_base, exact demo text not re-run.
- Reader paraphrases rendered some SDK calls as `client.chat.completions.create` / `client.messages.create` — repo ground truth is `client.responses.create`; wiki uses the repo's shape throughout.

## Key Takeaways

- Treat every dated fact (models, prices, windows) as a snapshot; treat the frameworks (6 criteria, layering, validation posture) as durable.
- The misfire pattern held again: **verifiers refute post-cutoff or retired-but-real things by reading only current docs** — always ground-check REFUTED verdicts on time-sensitive claims against primary sources or period knowledge before accepting.
- Cross-links: [[source-provenance]] (full verdict table), [[tokens-and-cost]], [[calling-models-responses-api]].
