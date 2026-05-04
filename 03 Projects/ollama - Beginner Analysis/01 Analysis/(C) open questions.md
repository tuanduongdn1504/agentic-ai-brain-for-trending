# ollama v46 — Open Questions

## Corporate + commercial structure

1. Who are the Ollama, Inc. founders? (no individual-author lineage cited in README; not surfaced at ollama.com landing)
2. What is Ollama, Inc. funding state? (YC batch? VC? Self-funded? Revenue from Pro/Max tiers?)
3. Ollama Cloud infrastructure — Ollama-owned GPUs or hyperscaler resale?
4. Ollama Cloud Pro $20/mo + Max $100/mo — conversion rate from 170K-star OSS base?
5. Enterprise / team tiers beyond Max? (not surfaced on public pricing page)

## Architecture

6. Why separate `openai/` + `anthropic/` API-compat subdirs rather than unified adapter pattern?
7. `harmony/` + `thinking/` + `tools/` — what's the decomposition rationale across these 3 subdirs for chain-of-thought + tool-use handling?
8. `kvcache/` — Ollama's own KV cache implementation or thin wrapper over llama.cpp?
9. `ml/` vs `llm/` vs `runner/` — boundary between these 3 inference-pipeline subdirs?
10. MLX_VERSION + MLX_C_VERSION vendored pins — how frequently updated? Coupling cost?

## Model registry

11. ollama.com/library curation gate — who approves new model submissions?
12. Modelfile format versioning strategy?
13. Cloud models (`:cloud` suffix) — server-side inference billing model?

## Integration protocol

14. `ollama launch <runtime>` — how is integration onboarding handled? (PRs to cmd/launch/?)
15. Why is Claude Code first-class via `ollama launch claude` but not the other way around?
16. Runtime version pinning — does `ollama launch claude` pin to specific Claude Code version?
17. OpenClaw integration depth — why dedicated 27.4KB `cmd/launch/openclaw.go` (largest launcher file)?

## Pattern-library follow-ups

18. Pattern #47 conditional-retirement OBSERVATION-TRACK replacement formulation — "Browser-Agent Architectural-Approach 3-point spectrum"; what does the OT tracking look like vs confirmed-pattern tracking?
19. Pattern #28 inversion observation — should "provider-being-consumed" become standalone sub-observation or stay within-#28?
20. Pattern #18 Layer 0 (runtime-bundled-launcher) — new layer added to 3-layer taxonomy? (Layer 0 ollama / Layer 1 MCP universal / Layer 2 community-platform-scoped / Layer 3 per-runtime)

## Storm Bear pilot

21. Privacy pilot — Ollama on Storm Bear operator's Mac for Scrum-coaching LLM invocations with VN client data?
22. Cost calculation — Ollama local (free after hardware) vs Claude API for Scrum workloads?
23. Ollama Cloud Pro $20/mo vs Claude Code subscription — which maps better to Storm Bear usage pattern?
24. Does Ollama local serve well enough for Scrum coaching at 64GB Mac RAM?

## Corpus observations

25. Pattern #57 Recursive Corpus Reference — Ollama Pi integration cites BOTH Pi (v36) AND Karpathy autoresearch (v10). Is this a new sub-variant "compound-cross-corpus-citation" (2 prior wikis cited in one integration doc)?

26. Pattern #18 governance discipline — Ollama's CONTRIBUTING discourages new features explicitly. Does this correlate with commercial-runtime-infrastructure archetype vs feature-rich aggregator archetype?
