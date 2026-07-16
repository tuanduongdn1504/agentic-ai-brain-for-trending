# Pillar 2 — The stack around AI

## Source
Quân IT, [`RcF6ofU2nLs`](https://www.youtube.com/watch?v=RcF6ofU2nLs) [04:23–09:34].

## What he says

"AI is just a stack." At the center is the LLM; around it you must understand:

1. **Open vs closed models** [05:18] — go to **HuggingFace** to see open-weight models (what they're trained for, how they're used); vs **API-only** vendors like OpenAI and Claude/Anthropic that *don't* open-source their weights. Knowing this lets you decide: **use a third-party API, or self-host your own model.**
2. **RAG, fine-tuning, context window** [05:46–06:45] — you can't dump an entire corpus at a model. His example: *"what was 2016 revenue?"* — you can't throw 2000→2026 financial reports at the model and hope. **RAG** supplies the domain-specific data so the model answers precisely. **Fine-tuning** specializes a model to solve *one* core problem well — it is explicitly **not** a frontier model that answers everything.
3. **MCP / function calling** [06:45–07:42] — *"MCP is Claude's (Anthropic's) thing; OpenAI calls it function calling."* Both let the model **call external functions/APIs**: `1+1` → call a calculator; "today's weather on July 14?" → call a weather API. (The model shouldn't compute `1+1` from its own weights.)
4. **Embeddings + vector database** [07:42–08:37] — turn raw company data into embeddings for retrieval.
5. **Data cleanup + asking the right questions** [08:10–09:05] — *the part he stresses most.* When a company says "we want to deploy AI," you must interrogate their data: Is it clean? Is it on paper / PDF / Excel / a database? His killer example: an **HR policy with 10 different versions, each with different content** — *"even 10 Fable or GPT-5.6 can't answer that."* You must ask the precise questions that let you clean the data and deploy correctly.
6. **How you build RAG** [09:05–09:34] — use a framework like **LangChain**, or do **agentic RAG**: one model *classifies* the question, then routes to another agent that *retrieves* the right data for that class of question.

## Verified facts behind the pillar

All **CONFIRMED** (see [[quanit-becoming-ai-engineer-2026/claims-scorecard|claims-scorecard]]):
- **C3** open-vs-closed + HuggingFace-as-open-hub, OpenAI/Anthropic flagships closed API-only.
- **C4** MCP = Anthropic (open standard, Nov 2024; donated to a Linux-Foundation body Dec 2025); "function calling" = OpenAI's term (2023). **Nuance:** by 2026 both vendors support both — OpenAI added native MCP support — so it's "MCP is vendor-neutral, function-calling is OpenAI-native," not "two rival things." His historical attribution is correct.
- **C5** LangChain is a real, dominant RAG/LLM framework (v1.0, 2025); "agentic RAG" (classify→route→retrieve, a.k.a. adaptive RAG) is a real named production pattern.
- **C6** "Fable" (Claude Fable 5) and "GPT-5.6" are real 2026 models — used only as illustrative model names.

## The dated-stack caveat

This pillar is **2023–24 orthodoxy**, per the critical appraisal:
- **Long-context models** (100K+ tokens) now make RAG *optional* for many domains.
- **Prompt/response caching** patterns (e.g. the [[mosh-ai-powered-apps/_index]] Responses-API seam, provider prompt-caches) shift the tradeoffs he doesn't mention.
- He gives the **happy path only** — no discussion of RAG failure modes (retrieval gaps, embedding drift), vector-DB recall guarantees, or MCP as a prompt-injection vector (which his own Pillar 3 security section *should* connect to).
- For the newer patterns, cross-read [[agent-memory-architecture/_index]] and [[claude-code-memory-systems/_index]].

## Key Takeaways

- The **map is correct and useful** for a beginner: open-vs-closed → RAG/fine-tune/context → MCP/function-calling → embeddings/vector-DB.
- **The data-cleanup point is the gem** — "10 conflicting policy versions defeat any model" is a real failure mode that no amount of model scaling fixes. This is where AI projects actually die.
- **Fine-tuning ≠ frontier model** — a genuinely useful clarification for beginners who conflate the two.
- Treat the *specific* stack as a **2024 checklist**, then update it with long-context + caching (2026) and with failure-mode handling.
