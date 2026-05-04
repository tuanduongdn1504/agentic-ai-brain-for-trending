# (C) Index — deer-flow Wiki

## 🎯 Project status (2026-04-18)

- ✅ Phase 0: Pre-flight — PASSED (API probe, 32MB moderate, **Tier 5 "Agent-as-application" proposal**)
- ✅ Phase 1: Setup — COMPLETE
- ✅ Phase 2: Source ingestion — COMPLETE (3 summaries)
- ✅ Phase 3: Entity pages — COMPLETE (4 entity pages)
- ✅ Phase 4a: Beginner published guide — COMPLETE
- ✅ Phase 4b: **Tier 5 proposal (5-tier taxonomy extension)** — COMPLETE
- ✅ Phase 5: Iteration log v9 — COMPLETE
- ✅ Phase 6: Vault file updates — COMPLETE

**🎉 v9 SHIPPED.** 9th auto-execution. Tier 5 "Agent-as-application" established. 5-tier taxonomy v4 documented.

**Repo:** bytedance/deer-flow
- **Description:** "open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours."
- **Stats:** 62,505 stars, 8,079 forks, MIT license, 32 MB, Python + Next.js, pushed 2026-04-18 (TODAY)
- **Version:** v2.0 (rebuilt from scratch, Feb 2026 launch, reached #1 GitHub Trending)
- **Author:** ByteDance (TikTok parent)
- **Routine:** `05 Skills/llm-wiki-routine.md` v1 — 9th auto-execution, third different-domain
- **Domain:** **Tier 5 candidate (Agent-as-application)** — NEW tier, extends v7 4-tier → 5-tier

## Sources (planned)

| Page | Summary | Status |
|------|---------|--------|
| [[(C) README summary]] | Positioning ("SuperAgent harness"), architecture components, capabilities, model support, comparisons (Devin/AutoGPT/CrewAI/Claude Code), target users | ✅ |
| [[(C) Install + Setup summary]] | Docker + local setup paths, make commands, prerequisites, config.yaml requirements | ✅ |
| [[(C) Architecture + Contributing cluster summary]] | Nginx → Frontend/Gateway/LangGraph layered, code structure (backend/ frontend/ skills/), development workflow | ✅ |

## Concepts (planned từ Phase 0)

- **SuperAgent harness** — positioning framing (unique)
- **Long-horizon tasks** — minutes to hours (vs interactive Claude Code)
- **Sandbox** — Docker or filesystem isolation
- **Memory** — persistent cross-session
- **Skills** — Markdown-based, progressive loading
- **Sub-agents** — parallel fan-out với isolated context
- **Message Gateway** — Telegram/Slack/Feishu/WeChat/WeCom
- **LangGraph orchestration** — graph-based flow
- **Model-agnostic** — OpenAI-compatible APIs (GPT/Gemini/Qwen/Doubao/DeepSeek/Kimi)
- **Nginx reverse proxy** — port 2026 unified entry
- **Complementary Claude Code** — can invoke via OAuth; Claude Code can invoke via `claude-to-deerflow` skill

## Entities (planned)

| Page | Type | Sources | Status |
|------|------|---------|--------|
| [[(C) SuperAgent Harness Architecture]] | Architecture concept | README + CONTRIBUTING layered diagram | ✅ |
| [[(C) Skill System (Progressive Loading)]] | Building block | README skills framework + CONTRIBUTING skills folder | ✅ |
| [[(C) Sub-Agent System (Parallel Fan-out)]] | Workflow concept | README sub-agent section | ✅ |
| [[(C) Message Gateway (Multi-Channel)]] | Integration concept | README multi-channel list | ✅ |

## Roadmaps / Published

- ✅ [[../03 Published/(C) deer-flow - Huong dan cho nguoi moi]] — beginner guide bilingual
- ✅ [[../03 Published/(C) Agent framework taxonomy v4 - 5 tier with application]] — Tier 5 extension proposal

## Cross-project siblings (8 total)

- `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) index.md` (T1)
- `../../Superpowers - Beginner Analysis/02 Wiki/(C) index.md` (T1)
- `../../gstack - Beginner Analysis/02 Wiki/(C) index.md` (T1)
- `../../get-shit-done - Beginner Analysis/02 Wiki/(C) index.md` (T1)
- `../../goclaw - Beginner Analysis/02 Wiki/(C) index.md` (T2)
- `../../ai-agents-for-beginners - Beginner Analysis/02 Wiki/(C) index.md` (T3)
- `../../notebooklm-py - Beginner Analysis/02 Wiki/(C) index.md` (T4)
- `../../build-your-own-x - Beginner Analysis/02 Wiki/(C) index.md` (outside scope)

## Logs

- [[(C) log]]
