# (C) awesome-llm-apps — Deep Dive (LLM Wiki v201)

> Source: `github.com/Shubhamsaboo/awesome-llm-apps` · fetched 2026-07-15 · §37.4 note: the GitHub API is mocked in this environment, so all star/fork/date figures are **PAGE-STATED / SEARCH-STATED, NOT API-verified** → **NOT a Pattern #52 (viral-velocity) claim.**
> Built via a read-only research workflow (`wf_353b105a-664`, 8 agents on Haiku, ~1.56M subagent-tokens; 7 done / 1 failed "prompt too long" [`src:frameworks-models`, hand-covered]). **Verdict + every corpus/collision/identity/mint claim produced BY HAND** per `feedback_wiki_verify_independently_check_collisions`; Haiku over-claims caught + corrected are logged at the end.

## One-line

A **third-party, multi-framework, multi-model gallery of 100+ full runnable LLM / AI-agent / RAG / MCP applications**, hand-built and organized by capability category — *"Clone it, ship it, sell it."* The largest and most canonical instance of the "runnable AI-app gallery" genre; Apache-2.0; ~121k★ (page-stated). Author **Shubham Saboo** (AI DevRel / educator, Unwind AI, 3× AI author — **NOT Anthropic**).

## What it actually is (the classification that matters)

It calls itself "awesome-" and is a curated collection — but it is **NOT a links list** (Python 54.6% / TS 21.6% / JS 16.4% = it is mostly **code**). Each entry is a **self-contained, runnable end-to-end application** with its own `README.md` + `requirements.txt` + source (typically a Streamlit UI + 3–4 files), demonstrating one pattern. So it sits in a specific genre:

| Genre | Members | awesome-llm-apps? |
|---|---|---|
| **Vendor cookbooks** (single-vendor notebooks) | OpenAI Cookbook · **anthropics/claude-cookbooks (= corpus v102)** | ✗ (multi-vendor, full apps not notebooks) |
| **Framework templates** (one framework) | LangChain Templates · CrewAI Examples | ✗ (framework-agnostic) |
| **Educational guides / links lists** (Pattern #68 awesome-genre) | dair-ai Prompt-Engineering-Guide · Hannibal046/Awesome-LLM · **corpus: build-your-own-x v8 / awesome-design-md v25 / awesome-mcp-servers v31 / awesome-claude-skills v50 / awesome-artificial-intelligence v170** | ~ (borrows the "awesome-" name + curated-collection spirit, but carries runnable code, not links) |
| **Application galleries** (runnable apps) | **awesome-llm-apps** · Together demos · E2B cookbook | ✓ — and, per landscape research, the **largest / most canonical multi-framework, multi-model, capability-organized** one |

**Landscape verdict (WebSearch, `web:landscape` agent + hand-read):** awesome-llm-apps is the corpus-first *and world-canonical/largest* "multi-framework, multi-model, full-runnable-application gallery organized by capability category." It is **NOT world-first** — the genre is populated (Together demos = provider-centric; CrewAI examples = framework-specific; E2B cookbook = infra-centric) — but no direct peer matches its breadth (7+ models × ~9 frameworks × 15 capability categories × ~129 full apps).

## Provenance (§37.4 — page/search-stated, NOT API-verified)

| Field | Value (source) |
|---|---|
| Stars | **~121,000** (page-stated; ⚠️ a stale search cache said "55k+" — the live repo page governs) |
| Forks | ~17,900 (page-stated) |
| Watchers | ~1,200 (page-stated) |
| Open issues / PRs | 4 / 15 (page-stated) |
| Commits | ~1,080 on `main` (page-stated) |
| Releases | **0** (collection-first, no versioning) |
| License | **Apache-2.0** ("Fork it, ship it, sell it") |
| Languages | Python 54.6% / TS 21.6% / JS 16.4% / HTML 4.5% / CSS 2.5% (page-stated) |
| Growth | 15k★ (Feb 2025) → 60k★ (Aug 2025) → ~121k★ (Jul 2026); "#1 trending / ~1,300★ in 24h" — SEARCH-stated milestones, **not a verified velocity → NOT #52** |
| Repo description | *"100+ AI Agent & RAG apps you can actually run — clone, customize, ship"* |
| README intro line | *"100+ open-source AI agents, agent skills, and RAG apps. Hand-built, tested end-to-end, Apache-2.0."* |
| Opening pitch | *"Clone it, ship it, sell it - 100% free and open-source. Works with Claude, Gemini, GPT, DeepSeek, Llama, Qwen and other open-source models."* |

## Author — Shubham Saboo (NOT Anthropic)

- AI **developer advocate / educator / product manager**; co-founder of **Unwind AI** (theunwindai.com — a daily AI newsletter + media brand, 200K+ subscribers, "community of 1M+ AI developers").
- **3× AI author** — co-authored *"GPT-3: Building Innovative NLP Products Using Large Language Models"* (O'Reilly, 2022, w/ Sandra Kublik) + *"Neural Search — From Prototype to Production with Jina"* (Packt); a third book is claimed on LinkedIn but unconfirmed in retail databases.
- **Employer:** AI DevRel / AI Product Manager — associated with **Tenstorrent** (Head of Developer Relations) *and* **Google** (Senior AI Product Manager). ⚠️ **Sources conflict on which is current vs prior** (both org-charts list him; my own WebSearch said Tenstorrent-current, the workflow agent said Google-current). **Immaterial to the verdict: he is not, and has never been, at Anthropic** — his engagement with Claude/MCP is public DevRel commentary, not employment.
- **Reputation:** clean — a well-known, prolific AI educator/builder; no hype red flags. The repo has a companion **Unwind AI newsletter funnel** ("New templates drop weekly — get them in your inbox").

## Structure — 15 capability categories (+ 2 nav sections), ~129 apps

README top-level headings in order: `🚀 Run one now` · `📂 Browse all templates` (nav) · then the 15 capability categories:

1. **🧩 Agent Skills** (~3) — Project Graveyard · Advisor Orchestrator Worker · Self-Improving Agent Skills
2. **🌱 Starter AI Agents** (~12) — Blog-to-Podcast, Data Analysis, Medical Imaging, Meme/Music Generator, Travel Agent, Reasoning Agent, xAI Finance, OpenAI Research, Web Scraping, …
3. **🚀 Advanced AI Agents** (~22) — Deep Research, VC Due Diligence, System Architect, Financial Coach, Movie Production, Earnings-Call Analyst, Fraud Investigation, **AI Recruitment**, Self-Evolving, Sales Intelligence, Trust-Gated Multi-Agent Research Team, …
4. **🛰️ Always-on Agents** (~1) — Always-on Hacker News Briefing
5. **🤝 Multi-agent Teams** (~13) — Competitor Intelligence, Finance Team, **AI Legal Agent Team**, **AI Recruitment**, Real Estate, Services Agency, Teaching, Multimodal Coding/Design/UX-Feedback, Travel Planner, AG2 Adaptive Research
6. **🗣️ Voice AI Agents** (~5) — Audio Tour, Customer Support Voice, Insurance Claim Live Team, Voice RAG, OpenSource Voice Dictation
7. **🖼️ Generative UI & Agentic Frontends** (~7) — Generative UI Starter, Dashboard Canvas, MCP App Builder, Shadcn Component Generator, Deep Research Agent
8. **🎮 Autonomous Game-Playing Agents** (~3) — 3D Pygame, Chess, Tic-Tac-Toe
9. **♾️ MCP AI Agents** (~5) — Browser MCP, GitHub MCP, Notion MCP, Travel Planner MCP, **Multi-MCP Agent Router**
10. **📀 RAG** (~20) — Agentic RAG (reasoning / EmbeddingGemma), Corrective RAG, Hybrid Search, Local RAG (DeepSeek/Llama-3.1), Vision RAG, RAG-as-a-Service, RAG with DB Routing, Knowledge-Graph RAG with Citations, RAG Failure-Diagnostics Clinic, …
11. **💾 LLM Apps with Memory** (~6) — ArXiv Agent, Travel Agent (memory), Stateful Chat, Personalized-Memory App, Local ChatGPT Clone, Multi-LLM App
12. **💬 Chat with X** (~6) — GitHub, Gmail, PDF, Research Papers, Substack, YouTube
13. **🎯 LLM Optimization Tools** (~2) — Toonify Token Optimization · **Headroom Context Optimization (= corpus subject v144 `chopratejas/headroom`)**
14. **🔧 LLM Fine-tuning** (~2) — Gemma 3 · Llama 3.2
15. **🧑‍🏫 AI Agent Framework Crash Courses** (~2) — Google ADK · OpenAI Agents SDK

## Frameworks & models (hand-inventoried; `src:frameworks-models` agent failed, covered from README + sample apps)

- **Agent/LLM frameworks:** LangChain / LangGraph (heavily), CrewAI, Agno, AG2 (AutoGen), OpenAI Agents SDK, Google ADK, browser-use (= corpus v41), Firecrawl, EvoAgentX, Mem0 (memory), Streamlit (UI), Chroma / Qdrant (vector DBs), Ollama (local).
- **LLM providers:** Claude (Anthropic), GPT (OpenAI), Gemini (Google), DeepSeek, Llama, Qwen, Grok (xAI).
- **Claude's prominence — the load-bearing (b) calibration:** the README says *"Works with Claude…"* and **the Agent Skills sub-section is explicitly Claude-Code-first** (verbatim: *"Works with Claude Code, Codex, Cursor, and other coding agents… Every skill ships real code and passes a security + eval CI gate"*). **BUT the broader gallery skews OpenAI/Gemini:** in a 4-app hand-sample by the workflow (RAG `rag_chain`/PharmaQuery → Gemini; multi-agent `multi_agent_researcher` → GPT-4o/Llama-3; memory `ai_travel_agent_memory` → GPT-4o+Mem0+Qdrant; starter `ai_reasoning_agent` → Ollama) **none defaulted to Claude**; of the 6 MCP agents, **only 2 support Claude** (`multi_mcp_agent_router` uses Claude primary; `browser_mcp_agent` supports it as a fallback), the other 4 are OpenAI-only. **Honest reading: Claude is a supported option, not the default; the repo is model-agnostic-leaning-OpenAI, not Claude-centric** (the Agent-Skills sub-section being the Claude-first exception).

## The Agent Skills section (the corpus-relevant core)

Verbatim: *"Give your coding agent new abilities. One command to install, plain English to use. Every skill ships real code and passes a security + eval CI gate. Works with Claude Code, Codex, Cursor, and other coding agents."* Install verb:

```
npx skills add https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/project-graveyard
```

- This is the **`npx skills add` verb — the agentskills.io ecosystem** the corpus first noted at **vercel-labs v51** (and tracks via agent-skills-standard v76 / anthropics-skills v93 / agent-skills v184), here pointed at a **GitHub sub-folder URL**. *(⚠️ The `src:agent-skills-mcp` Haiku agent called this "non-standard, not agentskills.io" — over-interpretation, corrected: the `skills` CLI accepts URLs and this is the same ecosystem verb.)*
- 3 skills: **Project Graveyard** (analyzes abandoned side projects via git history → failure patterns → revival suggestions) · **Advisor-Orchestrator-Worker** (three-tier: stateless workers + an expensive advisor at decision points + verification gates to prevent API-cost runaway — a maker/checker + cost-guardrail pattern) · **Self-Improving Agent Skills** (auto-refines capabilities via Gemini + ADK).

## Corpus subjects it demonstrates (cross-reference data-point)

awesome-llm-apps, like awesome-claude-skills v50 (Pattern #57 57b "aggregator-mediated"), **includes/demonstrates corpus subjects as example content**: **`headroom` (corpus v144)** as its "Headroom Context Optimization" app + **`browser-use` (corpus v41)** as a demonstrated framework. A #57 57b-style aggregator-mediated data-point (NOT a promotion; the subject demonstrates, it does not cite-as-influence).

## Supply-chain / install safety (`web:security` + hand)

- **Clean at the repo level** — no root `curl|bash` installer, no postinstall hooks, no telemetry; Apache-2.0. Standard flow = `git clone → cd <app> → pip install -r requirements.txt → set API key → streamlit run`.
- **Risk migrates to the per-app tail:** each app pins its own `requirements.txt` (no monorepo lockfile) → scratch venv + pin discipline is on you; many apps take the **API key in a Streamlit UI text box** (`type="password"` is UI-mask-only → prefer `.env` + `os.getenv`); the `npx skills add` community-skill registry governance is **opaque** (the claimed "security + eval CI gate" has no visible audit trail) → treat as a third-party trust boundary + `npm-security-check` before adding a skill; watch for **typosquatted forks** (`awesome-llm-apps-v2` etc.) — clone only from the author's URL.
