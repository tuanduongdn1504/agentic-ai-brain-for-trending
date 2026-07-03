# Source Provenance

## Pipeline

- **Trigger:** operator-submitted URL (path 5), 2026-07-03: "build knowledge from this video + double deep dive into the original resource + pilot methods."
- **Ingest:** yt-dlp metadata JSON + English auto-captions → deduped transcript (**~22.9K words / 3,428 lines**), key sections read directly in main loop (AI-engineering, model settings, calling models, conversation state) + 4 exhaustive chunk-readers.
- **Video:** PtETUYa3i2Q — "AI Course for Developers – Build AI-Powered Apps with React", Programming with Mosh, 2025-08-25, 8,739s, 161,914 views / 4,175 likes / 254 comments at fetch; channel 5.09M subs.
- **Workflow:** `wf_05723834-938` — **28 agents** (4 transcript readers + 5 original-resource dives + 16 adversarial verifiers [2 died: "Prompt is too long"] + 1 completeness critic + orchestration), **438 tool calls, ~1.15M subagent tokens**, ~6.5 min wall-clock.
- **Main-loop ground checks:** OpenAI conversation-state guide fetch (settled `previous_response_id` status + the input-token-billing caveat), Amazon review-highlights web search (aboutamazon.com Aug-2023), claude-api skill reference (the mapping article), Aug-2025 OpenAI pricing from operator knowledge.

## Verdict summary (16 verifiers returning)

- **CONFIRMED (8):** Mosh 20+yr background · ML-vs-AI-engineer distinction (Huyen-consistent) · GPT-4o mini 128K context · Mistral ~32K (v0.2) · 252-chars≈53-tokens ratio (plausibility) · low-temp-for-factual guidance · high-temp-for-creative guidance · image-model-outputs-images-only (verifier tested DALL-E; video's actual example was gpt-image-1 — claim-mutation noted, conclusion holds for both)
- **CORRECTED (5):** video = 2h25m preview of 7h course (not "2h") · Node latest was 22.18.0 not 22.17 · cl100k_base lowercase, dqbd community port · o3-most-powerful → GPT-5.5 as of 2026 · temperature-scale claim reconciled to 0–2 (OpenAI)
- **REFUTED (2) — both OVERRIDDEN by ground truth:** "GPT-4.1 has 1M context" (real at video time; verifier read 2026 docs only) · "temperature 0–2" (verifier cited wrong vendor's docs)
- **UNVERIFIABLE (1) — CLOSED CONFIRMED:** Amazon AI review highlights (aboutamazon.com, Aug-2023)
- **Died (2) — closed by operator knowledge:** the 13× pricing claim (historical-confirmed) · JSON-schema structured outputs (trivially real)
- **Dive-agent claim OVERRIDDEN:** "previous_response_id / instructions removed from docs" — direct fetch shows both still documented; Conversations API added as complement.

## Fail-loud log (Rule 12)

- 5 misfires/confabulations caught and overridden (see [[caveats-and-corrections]] for details) — the **stale-cutoff / current-docs-only verifier misfire pattern recurred**, this time in the inverse direction (refuting *retired-but-real* items rather than post-cutoff ones).
- Reader paraphrase-garbles (`client.messages.create`, `chat.completions.create`, `response.choices[0]`) rejected in favor of repo ground truth (`client.responses.create` / `output_text`).
- Critic coverage holes acknowledged: frontend build (not in the free video — it ends there), testing (none exists in the free half — recorded as a caveat, not a gap), refactor *process* (covered from direct transcript read).
- Caption garble map applied: Mash Hamadani→Mosh Hamedani · codewithmarsh→codewithmosh · Shatsen→shadcn/ui · Olama→Ollama · open AAI→OpenAI · GPT-40→GPT-4o · bonex→bunx · Chat JPT→ChatGPT · Freshesk→Freshdesk · Grock→Grok · "env oren"→dotenv · "2 to 4" (temp)→0.2–0.4.

## Sources of record

- https://www.youtube.com/watch?v=PtETUYa3i2Q (video)
- https://codewithmosh.com/p/build-ai-powered-apps (course page)
- https://codewithmosh.com/pricing ($29/mo, $149/yr)
- https://github.com/mosh-hamedani/ai-powered-apps-course (repo + file-level checks)
- https://developers.openai.com/api/docs/guides/conversation-state (2026 state semantics)
- https://github.com/dqbd/tiktoken · https://github.com/openai/tiktoken
- https://www.aboutamazon.com/news/amazon-ai/amazon-improves-customer-reviews-with-generative-ai
