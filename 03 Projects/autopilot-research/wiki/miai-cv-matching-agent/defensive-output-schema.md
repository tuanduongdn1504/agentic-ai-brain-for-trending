# Defensive Output Schema (Pydantic alias-normalization pattern)

## Source

`hr_agent_format.py` (read in full).

## The pattern

The response schema doesn't just declare fields — it **absorbs known LLM instabilities** before validation:

- `model_validator(mode="before")` maps alias field names the model has been observed to emit:
  - `reason` / `explanation` / `rationale` / `match_reasoning` / `fit_reason` → `reasoning`
  - `tips` / `improvement_tip` / `advice` / `suggestions` / `recommendation` → `improvement_tips`
- `field_validator(mode="before")` coerces type drift: list → `"; "`-joined string, `None` → `""` for both `reasoning` and `improvement_tips`.
- Bounds enforced declaratively: `match_score: int, ge=0, le=100`.
- The system prompt *also* shouts the contract ("CRITICAL: reasoning must be a non-empty string… improvement_tips must be a single string, NOT a list") — belt and suspenders with the schema.

## Where it's redundant vs load-bearing

- With `ProviderStrategy` + OpenAI native structured outputs, the schema is enforced server-side on the happy path — aliases *shouldn't* occur. The author's on-camera comments ("có lúc nó vẫn không đúng đâu" — sometimes it still doesn't comply) suggest the validators were born from real dev-time failures, likely pre-ProviderStrategy or under fallback.
- They stay load-bearing for: `ToolStrategy` fallback, provider swaps (a Claude port keeps them useful), refusal/partial outputs, and any path that parses raw text — which is exactly what this repo's serving path does ([[langchain-v1-agent-stack]]).
- Irony (verified): the FE duplicates the alias logic in raw dict lookups because the serving path bypasses this Pydantic layer entirely. The best-engineered file in the repo never runs in production flow.

## Key Takeaways

- "Schema + alias-map + coercion" is a cheap, reusable hardening recipe for any structured-output feature — port it to Zod for TypeScript services (hireui: Zod `.transform()` + `.catch()` equivalents).
- Put the tolerance in the schema, not in scattered `if` statements — one choke point, testable.
- Keep the defensive layer even when the provider guarantees the schema: it's your vendor-portability and fallback insurance.
- Make sure the validated object is what you actually serve — a defense layer that's bypassed is decoration ([[code-audit]]).
- Sister pattern in corpus: [[external|Storm Bear: mosh-ai-powered-apps]] uses Zod input guards (max-1000-char) for cost/DoS; this is the output-side counterpart.
