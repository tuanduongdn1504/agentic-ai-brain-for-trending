# LangChain 1.0 Agent Stack (create_agent / ProviderStrategy / streaming)

## Source

`hr_agent.py`, `hr_agent_be.py` + official docs (docs.langchain.com) verified by dive `langchain-api` + refute-first pass (wf_dd724957-cac).

## Verified API surface

- `from langchain.agents import create_agent` — **LangChain 1.0's** standard agent factory (docs call it "a highly configurable harness"). It builds on **LangGraph** internally (state + checkpoints) but abstracts the graph away. (PARTIAL nuance: you don't construct a state machine yourself.)
- `response_format=ProviderStrategy(PydanticModel)` — uses the **provider's native structured outputs** (OpenAI json_schema). Docs: "utilizes native implementations… the most reliable method when available"; `ToolStrategy` is the fallback for models without native support. (The often-repeated "FSM constrained decoding" mechanism is NOT in LangChain's official docs — don't cite it from there.)
- `result["structured_response"]` — CONFIRMED: the validated Pydantic object lands in the `structured_response` key of the agent's **final state** (via `invoke`/`ainvoke`).
- `agent.astream(..., stream_mode="values")` — CONFIRMED: emits the **full state after each step**. Critically: the streamed values chunks expose `messages`, **not** `structured_response` — see the mismatch below.
- Multimodal file input: `{"type": "file", "base64": …, "mime_type": "application/pdf", "filename": …}` is LangChain v1's cross-provider **FileContentBlock**; `langchain-openai` converts it to OpenAI's file-input format. (Exact conversion internals not documented officially.)
- gpt-4o-mini PDF input: vision-capable, **50MB per file / 50MB per request** confirmed; pages billed as text + image tokens (85 base + 170 per 512px tile at high detail). A commonly-cited "100 pages per document" limit was **not confirmed** in current OpenAI docs.

## The structured-output/streaming mismatch (load-bearing finding)

- The repo configures `ProviderStrategy(MatchResponse)` **and** serves via `astream(stream_mode="values")`.
- `stream_mode="values"` does not surface `structured_response` — so the backend ships the **raw AI message content** (a JSON string, sometimes fenced) to the client, and the Pydantic validation layer is **never executed on the serving path**.
- Consequence: the frontend re-implements parsing by hand — strips ```json fences, `json.loads`, and its own alias fallbacks (`reasoning`/`reason`/`explanation`). Two validation layers exist; the one that runs is the weaker, hand-rolled one.
- Fixes (either): (a) use `ainvoke` and return `structured_response` once analysis is done, keeping SSE only for progress events; or (b) read the final state's `structured_response` after the stream completes and emit it as the `result` event.

## Key Takeaways

- LangChain 1.0's `create_agent` + `ProviderStrategy` + `structured_response` is a clean, current pattern — the repo uses the modern API correctly at the *configuration* level.
- Configuration ≠ serving: streaming mode choices can silently bypass your validation layer. Check which object actually reaches the wire.
- Provider-native structured outputs make happy-path alias-mismatch largely impossible — the defensive validators pay off on fallback paths and provider swaps ([[defensive-output-schema]]).
- The FileContentBlock is vendor-portable in shape; on Claude the equivalent is the `document` content block ([[claude-stack-port]]).
- Cross-link: [[external|Storm Bear: multi-agent-orchestration]] covers the Anthropic-native agent-loop equivalents of this harness layer.
