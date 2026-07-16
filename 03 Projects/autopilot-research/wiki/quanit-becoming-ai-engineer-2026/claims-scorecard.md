# Claims scorecard

> Adversarial verification via Workflow `wf_0f3ff851-bd2` (refute-first fact-check clusters + independent re-check pass) + main-loop cross-checks. Every verdict carries a source URL. Discard-as-garble guard applied (VN auto-caption proper-noun garbles resolved by meaning).

## Tally

**10 checkable claims: 8 CONFIRMED · 1 MISLEADING · 0 FALSE · 0 FABRICATED · 1 UNVERIFIABLE.** A high-integrity talk — the speaker fabricates nothing; the two non-CONFIRMED items are one inflated magnitude and one unidentifiable brand name (the underlying phenomenon of which is real).

## Table

| ID | Claim | Verdict | Note |
|----|-------|---------|------|
| C1 | OpenAI tied its IPO to a ~$1 trillion valuation ("$1T or no IPO") | **CONFIRMED** | Altman called sub-$1T a "nonstarter"; confidential S-1 targeting ~$1T (mid-2026). The narrative he mocks is *real*. |
| C2a | DeepSeek is a real frontier LLM (garbled "Dipsic") | **CONFIRMED** | DeepSeek V4 (Apr 2026), MIT open-weight. |
| C2b | Kimi is a real frontier LLM (Moonshot AI) | **CONFIRMED** | Kimi K2.6 (Apr 2026), 1T params. |
| C2c | Top AI researchers earn "a few million $/yr" | **MISLEADING** | Median frontier-lab researcher ~$1–1.5M; only top 5–10% reach $2M+. Point holds, magnitude inflated. |
| C3 | HuggingFace = open-model hub; OpenAI/Anthropic flagships closed API-only | **CONFIRMED** | HF ~2.2M models; OpenAI/Anthropic flagship weights closed. |
| C4 | MCP = Anthropic's; OpenAI's equivalent = "function calling"; both call external functions | **CONFIRMED** | MCP created by Anthropic (Nov 2024, now vendor-neutral); function-calling = OpenAI term (2023). Nuance: both vendors support both by 2026. |
| C5 | LangChain is a real RAG framework; agentic RAG (classify→route→retrieve) is a real pattern | **CONFIRMED** | LangChain v1.0 (2025); agentic/adaptive RAG documented production pattern. |
| C6 | "Fable" and "GPT-5.6" are real current models | **CONFIRMED** | Claude Fable 5 (2026-06-09); GPT-5.6 Sol (2026-07-09). Caveat: GPT-5.6 Sol flagged by METR/Apollo for reward-hacking — see [[quanit-becoming-ai-engineer-2026/caveats-and-corrections\|caveats]]. |
| C7 | Oracle OPERA is a real, highly-configurable hotel PMS | **CONFIRMED** | OPERA 5 + OPERA Cloud; hundreds of integrations, thousands of REST APIs. |
| C8a | A chatbot "Dodas" was prompt-injected and leaked discount codes | **UNVERIFIABLE** | No incident under that name. But the *phenomenon* is real & documented (Chevrolet $1-Tahoe; an 80%-discount prompt-injection case). Ship as illustrative, not a named fact. |

## Sources (selected)

- **C1:** finance.yahoo.com (Altman "nonstarter"); fool.com; thestreet.com (OpenAI IPO / $1T).
- **C2a/b:** simonwillison.net (DeepSeek V4); siliconangle.com + miraflow.ai (Kimi K2.6).
- **C2c:** levels.fyi (OpenAI/Meta research comp bands).
- **C3:** huggingface.co state-of-open-source 2026; help.openai.com; platform.claude.com.
- **C4:** anthropic.com/news/model-context-protocol; anthropic.com (MCP → Agentic AI Foundation); descope.com (MCP vs function calling).
- **C5:** LangChain v1.0 + LangGraph agentic-RAG production writeups (2026).
- **C6:** claude5.ai + openai.com/index/gpt-5-6; techtimes.com (Sol reward-hacking); METR/Apollo.
- **C7:** oracle.com/hospitality; hoteltechreport.com; altexsoft.com (OPERA integrations).
- **C8a:** medium.com (80%-discount prompt injection); Chevrolet $1-Tahoe (Dec 2023); techcrunch.com (DoorDash "Ask DoorDash", no breach).

## Key Takeaways

- **Substance-reliable.** Everything about *what the technologies are* checks out; the map he draws is accurate.
- **Two soft spots, both minor:** an inflated pay figure (C2c) and an unidentifiable brand (C8a) whose underlying risk is nonetheless real.
- **The most interesting result is C1:** a claim delivered as hype-mockery turned out to be a verifiable fact — a reverse instance of the discard-as-garble guard.
