# Managed Agents API + Interactions API (the teaser)

> The video defers this to a future video but frames it as "an agent orchestration framework, just arrived in the free tier, that can auto-write code / images / video." Here's the real shape.

## What's real

- **Managed Agents** (Gemini API) — a single call to the **Interactions API** (GA since ~June 2026) spins up a managed agent in an **isolated Linux sandbox** (Ubuntu, Python 3.12 + Node.js 22) that reasons, executes code (Bash/Python/Node), searches the web, fetches URLs, and manages files — **autonomously**. ([blog](https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/), [agents docs](https://ai.google.dev/gemini-api/docs/agents)).
- **The Antigravity agent** = Google's general-purpose managed agent (Gemini 3.5 Flash), invoked by model ID; it **shares the same harness** as the [[../google-antigravity-skills/_index|Google Antigravity]] development platform (desktop/CLI/SDK). API-first, so no IDE lock-in. ✅ CONFIRMED.
- **Declarative config** — custom managed agents are defined via **`AGENTS.md` (system instructions) + `SKILL.md` (skills)** in a `.agents/` directory, registered once, invoked by ID. Same format family as Anthropic Skills / [[../google-antigravity-skills/anthropic-agent-skills-portability|Antigravity Skills]].
- Supported orchestration frameworks (per docs): LangChain, LangGraph, CrewAI, **Vercel AI SDK**, Temporal, Google ADK, Antigravity SDK.

## ⚠️ The pin — "in the free tier" is MISLEADING

- Managed Agents are **paid, public preview**. Only the **sandbox compute** (CPU/memory/execution) is **not billed *during the preview period***; **all model inference is billed at standard Gemini token rates** (input + output + intermediate reasoning). There is **no free service tier** for Managed Agents. The video conflates *"free compute during preview"* with *"free tier."*
- **"Auto-write code" is native; "generate images/video" is NOT.** Native tools = code exec, web search, URL fetch, function calling. Image (Nano Banana) and video (Veo/Gemini Omni) are **separate Gemini APIs** the agent must call via function-calling — not built-in agent capabilities. ⚠️
- Other preview limits: environments **deleted after 7 days idle**; **no structured-output support**; input **text + images only**; `temperature`/`top_p`/`max_output_tokens` unsupported; schema may change.

## ⚠️ The blocker for hireui — preview forbids PII

Google's Service-Specific Terms: **"Customer should not use Pre-GA Offerings to process personal data or other data subject to legal/regulatory compliance requirements."** Managed Agents are preview ⇒ **excluded from the DPA/SLAs**, with **no documented data-residency**. So Managed Agents are **not deployable for candidate data** today.

## Why it matters for hireui — a WATCH item, not a build

- **Candidate provider behind the Match-Explain seam (later).** Managed Agents (AGENTS.md/SKILL.md, sandbox) is a plausible *alternative* to the planned Claude-Haiku Match-Explain implementation — but only once it hits **GA with a DPA + residency**. Because the [[../mosh-ai-powered-apps/_index|Mosh A2 vendor seam]] already abstracts the provider, adopting it later is a **config swap, not a rewrite**. That's pilot **C1** (watch/compare, don't build now).
- **AGENTS.md/SKILL.md convergence** (pilot **C2**): Claude Code, Antigravity, *and* Gemini Managed Agents now share the same declarative harness format → keep hireui's harness rules in that portable format and they travel across all three. Reinforces the [[../google-antigravity-skills/anthropic-agent-skills-portability|"author once, stay portable"]] thesis.

## See also
[[_index]] · [[../google-antigravity-skills/_index|google-antigravity-skills]] · [[../mosh-ai-powered-apps/_index|mosh-ai-powered-apps]] · [[pricing-privacy-data]]
