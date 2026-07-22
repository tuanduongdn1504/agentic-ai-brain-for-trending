# LangChain — Agent Futures, Continual Learning & "Everyone Builds Agents"

> **Source:** Harrison Chase (LangChain co-founder/CEO), "The Future of AI Agents: What Will Interrupt 2027 Look Like?", **Interrupt 26** conference (`R9K2574YEAg`, May 2026). Co-presented with LangChain teammates demoing LangSmith Fleets.

## Two divergent agent types

Chase future-casts a split (already emerging):
- **Long-horizon agents** — run minutes → hours → days; code execution, planning, sub-agents, skills; driven by **outcomes/goals**; doing valuable knowledge work.
- **Low-latency customer-experience agents** — support/sales; **brand + voice** matter; latency is the constraint.
- There's a **shared stack** underneath — an open question is how much is common vs particular.

## Voice, sandboxes, open models

- **Voice:** today = STT → agent(text) → TTS "sandwich"; native **speech-to-speech** models emerging (OpenAI released a v2 — **GPT-Realtime-2, May 2026**); not steerable enough yet for high-control apps, expected to change.
- **Sandboxes:** every agent (esp. long-horizon) needs one — code isn't just software, it's data analysis, web browsing, image-gen, deep research. "Give the marketing team a software engineer — what would it build?"
- **Open models** rising: approaching frontier on some tasks; cheaper (coding agents burn tokens fast); **trainable for your domain** on your own traces.

## Agent identity / auth

Two patterns, both here to stay:
- **On behalf of a user** — uses *your* credentials; different users see different things.
- **Fixed credentials / service account** — everyone interacting sees the same. OpenClaw popularized the agent-as-its-own-entity with its own creds; some SaaS now let agents create their own accounts. Being *precise about which* is the skill.

## Continual learning across three layers

Chase's headline: improve the **agentic system** over time, across three layers — **all** improvable:

| Layer | What it is | Examples |
|---|---|---|
| **Model** | the LLM | fine-tune for a domain — **Ramp + Prime Intellect** fine-tuned an open model ("FastAsk", Qwen3.5-based) for *Ramp Sheets*: ~4% more accurate than Claude Opus 4.6, Haiku-level latency |
| **Harness** | code around the model connecting it to the environment | Deep Agents, Claude Code SDK — **"Meta-Harness" paper (Stanford-led, arXiv 2603.28052)**: an agent optimizes a coding harness on **Terminal-Bench 2** and beats human-written harnesses |
| **Context** | what guides the harness per task | `agent.md`, **skills** |

- **Evals + traces are the "training gradient"** for the harness/context layers (not literal gradient descent — the evals act as a forcing function). LangChain moved **top-30 → top-5 on Terminal-Bench 2 by changing only the harness** (GPT-5.2-Codex fixed; 52.8% → 66.5%).
- Announced **LangChain Labs** (research group) + LangSmith as the trace/feedback foundation.

## "Everyone builds agents"

- The best agent-builders are **the people who do the job** (domain experts), because "agents are just a collection of instructions, skills, and tools."
- **LangSmith Fleets** — a **no-code, natural-language agent builder**: **Arcade partnership (~7,500 tools) + MCP + Deep Agents harness** (the "~200 built-in tools" count is unverified); native in Slack/Gmail/Outlook; shareable like a Google Doc; credential/auth management; **cost tracking + spend limits**; **human-in-the-loop first-class**; model-agnostic; downloadable to code.
- Demo: a go-to-market agent (Salesforce/BigQuery/Slack/Gmail; sub-agents + skills; **HITL email approval**) — 84% of the GTM team uses it weekly; originally engineer-built, rebuilt in Fleet so the GTM team owns it end-to-end without code.

## Key Takeaways

- Agents diverge into **long-horizon** (goal-driven knowledge work) vs **low-latency customer-experience** types.
- **Continual learning** happens across **model / harness / context** — and **evals + traces are the training signal** (the harness layer alone took LangChain top-30 → top-5 on Terminal-Bench 2).
- **Domain experts will build their own agents** (no-code, e.g. LangSmith Fleets) with HITL + cost controls first-class.
- The systems-level restatement of the bundle: improving agents is **an evals/ownership discipline**, not just prompting.

## See also

- [[engineer-of-the-future/inner-loop-outer-loop]] — harness/context = the outer-loop levers
- [[engineer-of-the-future/convergent-thesis]] — evals-as-forcing-function ties to answerability
- [[prompt-evaluation/_index]] — the eval gate this depends on
- [[harness-engineering/_index]] · [[multi-agent-orchestration/_index]] · [[vercel-eve/_index]] (durable-agent framework sibling)
