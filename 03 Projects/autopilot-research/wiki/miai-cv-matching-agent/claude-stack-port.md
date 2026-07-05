# Claude-Stack Port (the hireui-relevant translation)

## Source

Main-loop synthesis using the claude-api skill reference (2026-07-05) + platform.claude.com/docs embeddings page (fetched 2026-07-05). The workflow's claude-stack dive agent died ("Prompt is too long"); this article closes that gap with first-party sources. Cited prices/limits verified against the skill's cached tables (2026-06-24).

## Component-by-component translation

| Demo (OpenAI stack) | Claude-stack equivalent | Notes |
|---|---|---|
| gpt-4o-mini agent LLM | **claude-haiku-4-5** ($1/$5 per MTok, 200K ctx) — or Sonnet tier for premium analysis | Haiku 4.5 supports structured outputs |
| `ProviderStrategy(MatchResponse)` | **Structured outputs, GA**: `output_config={"format": {"type": "json_schema", "schema": …}}` or `client.messages.parse(output_format=PydanticModel)`; `strict: true` tool use | No beta header. Same caveat as Pydantic: numeric bounds (ge/le) aren't API-enforceable — SDK strips + validates client-side; keep the defensive schema ([[defensive-output-schema]]) |
| PDF via base64 file block | **`document` content block** (base64, no beta): 32MB request; 600-page cap (100 pages on 200K-context models incl. Haiku) — CVs are 1–3 pages, fine. Files API (beta) to upload-once/reuse | Pages billed as text + image tokens, like OpenAI |
| text-embedding-3-small | **Anthropic has NO first-party embeddings API** — official docs recommend **Voyage AI**: `voyage-4` family (32K ctx, Matryoshka dims 256–2048), `voyage-4-lite` for cost, **`voyage-4-nano` open-weight Apache-2.0** (self-hostable legitimately), `voyage-context-4` for chunk-context, `input_type="query"/"document"` matters | Voyage is a MongoDB company; also on AWS Marketplace |
| (absent) reranker | **Voyage `rerank-2.5` / `rerank-2.5-lite`** — the Tier-1 upgrade from [[matching-quality-vs-production]] lives in the same vendor account | |
| LangChain `create_agent` | Direct **Anthropic SDK tool-use loop** (or tool runner helper); langchain-anthropic also works — ProviderStrategy supports Anthropic natively per LangChain docs | For one tool + one schema, the raw SDK loop is ~50 lines and removes a framework dependency |
| SSE via FastAPI | Same pattern; Claude SDK streaming events map cleanly onto status/result/done | |
| Chroma local | For hireui: **skip the vector DB in v1** (see below); else pgvector next to existing Postgres | |

## Cost math (Haiku 4.5, per CV analysis)

- Raw: ~5,700 in × $1/1M + ~800 out × $5/1M ≈ **$0.0097**.
- With prompt caching on the shared JD/system context (~4K tokens at 0.1× reads): ≈ **$0.006**. Note Haiku's min cacheable prefix = 4,096 tokens — structure the cached block above that.
- Batched (50%, nightly re-match): ≈ **$0.005**. At 10K CVs/month ≈ $50–100/month — 4–7× the OpenAI demo but still trivial vs product value ([[cost-economics]]).

## The v1 simplification hireui should notice

- A recruitment SaaS **owns both sides of the match** — no crawling ([[crawl-reality-and-robots]] is moot), and per-tenant open-job counts are small (tens, not thousands).
- Therefore v1 needs **no vector database at all**: SQL-filter the tenant's open JDs → put them in a **prompt-cached context block** → Claude judges + explains with structured outputs. Add Voyage embeddings + rerank only when JD counts outgrow the context/cache budget.
- This composes directly with the Mosh-thread **A2 vendor seam** (repository/service/controller split): the matching service is one more consumer behind the same LLM client seam.

## Key Takeaways

- Vendor split by layer: **reasoning/structured output = Claude; embeddings/rerank = Voyage** (Anthropic's own recommendation) — the demo's single-vendor assumption doesn't carry over.
- Structured outputs are GA on the Claude API — the demo's most modern pattern ports 1:1.
- Claude reads CV PDFs natively (document block) — no parser subsystem, same as the demo.
- Start without a vector DB; earn the retrieval infrastructure with scale.
- PII caveat: CVs to any third-party API need consent/DPA analysis first — [[recruitment-ai-regulatory-context]]; also note Anthropic ZDR constraints if data-residency requirements apply (cf. the agent-memory thread's data-residency ADR).
