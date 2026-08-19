# Agent Forgetfulness and Vendor Memory Strategy

> **Source:** [`MshYeoy8g2o`](https://www.youtube.com/watch?v=MshYeoy8g2o) (2026-04-22, 33:11) — the oldest video in the bundle, and the one that most directly overlaps existing corpus knowledge.

## The argument

1. **Why agents forget** ([01:29]–[02:23]): ChatGPT, Gemini and Claude lose long-conversation context because the **Transformer architecture has no memory component** — it maps input to output with no storage layer between calls. He anchors this on *"Attention Is All You Need"* (2017).
2. **Why it now matters** ([03:45]): the GenAI era (chat, generate text) is giving way to the **agentic era**, where agents take actions over multi-hour tasks. Without memory, agents don't just forget — they **fail silently**.
3. **Memory as a capital asset** ([29:36]): an agent that accumulates your company's procedures and its own right/wrong decisions becomes **like an employee**, and that memory is a *transferable asset* that compounds in value.
4. **The skill shift** ([30:57]): stop being a tool consumer, become an **agentic-system designer** — decide what to remember vs forget, which model to use, how agents coordinate.

## The canon he teaches — and it is the right canon

Notably, he teaches the actual research literature rather than vendor marketing. Everything below cross-checks against [[agent-memory-architecture/_index]], which the corpus compiled independently from an English-language source:

| His teaching | The underlying work | Check |
|---|---|---|
| Two foundational 2023 papers modelling **four human memory types** — working, procedural, semantic, episodic ([06:05], [08:23]) | **CoALA** (arXiv:2309.02427), whose taxonomy is exactly this | ✅ correct |
| **Stanford village simulation — 25 agents** with distinct roles, remembering conversations, forming relationships, generating autonomous events ([13:01]) | **Generative Agents** (arXiv:2304.03442) — 25 agents is the right number | ✅ correct |
| **Context window as a fixed bucket**; expanding it doesn't solve it because of **lost-in-the-middle** ([17:12], [17:40]) | Real, well-replicated positional-attention finding | ✅ correct |
| **Virtual-memory analogy**: main context = RAM, external store = disk, with functions that page memory in and out ([18:09], [20:00]) | **MemGPT** (arXiv:2310.08560) — this is precisely its framing | ✅ correct |

His explanation of *why* lost-in-the-middle happens — models trained on human documents that front-load and back-load importance — is a **plausible but contested** account rather than settled mechanism. Directionally fine, stated with more confidence than the evidence supports.

## The vendor survey — where it has aged

| Vendor, as he describes it | Assessment |
|---|---|
| **OpenAI** ([21:21]): ChatGPT auto-saves history and retrieves it so you needn't repeat context. **Weakness: no timestamp metadata** | ⏰ **Correct at publication, now stale.** OpenAI's memory gained per-item timestamps with the Dreaming V3 rollout (2026-06-04) — **six weeks after this video**. An automated verifier flagged this as MISLEADING without checking the upload date; corrected here. Judge the claim against 2026-04-22, not today |
| **Google** ([22:15]): Gemini leans on ecosystem reach — Gmail, Calendar, Drive, YouTube via a connected-apps toggle, querying live user data as external memory | ✅ Fair characterisation |
| **Anthropic** ([24:35]): Projects — upload files, all chats in the project share that file context; you organise the files manually | ⚠️ **Substantially incomplete.** This is one surface of four. The corpus documents claude.ai session synthesis, the **GA file-based memory tool** (`memory_20250818`), Managed-Agents memory stores + Dreams, and Claude Code's `MEMORY.md` ([[agent-memory-architecture/how-claude-memory-works]]). The file-based memory tool already existed when he filmed. Describing Anthropic's memory as "Projects" understates it the most of the three vendors |
| **Hermes Agent** ([25:59]): auto-saves user preferences, distils repetitive workflows into reusable skills | ⚠️ Treat with care — the corpus' [[hermes-agent/_index]] already **refuted** several circulating Hermes claims (star count, "only learning loop", "runs under Claude Code"). His narrower description is plausible but unverified here |
| **OpenClaw** ([28:42]): memory as **daily markdown files** (`YYYY-MM-DD.md`) the agent reads back; lightweight and version-control friendly | ✅ Interesting and architecturally notable — the plainest possible memory substrate, and the one closest to how this very vault works |

## ⚠️ The 100× pricing claim

At [31:25] he says model pricing varies by **100×** — "cents per 1M output tokens" versus "$100+". Within the Claude lineup the spread is **10×** on input ($1 Haiku → $10 Fable 5, see [[claude-pricing-ladder]]). A 100× spread requires reaching across to very cheap hosted open models. Directionally true across the whole market, loose as stated, and inconsistent with his own much more precise table in the anchor video.

## Why this article matters despite the overlap

This is the bundle's weakest claim to novelty — [[agent-memory-architecture/_index]] covers the same canon in more depth and with primary sources. Its value is different: it is **the same canon taught in Vietnamese to a 189K-subscriber non-specialist audience**, plus the OpenClaw markdown-memory pattern, plus the "memory as transferable capital asset" framing which the corpus does not otherwise state as crisply.

## Cross-links

- [[agent-memory-architecture/_index]] — the deeper, primary-source treatment of this exact canon
- [[agent-memory-architecture/how-claude-memory-works]] — the four Anthropic surfaces he reduces to one
- [[hermes-agent/_index]] — the corpus' refutations of circulating Hermes claims
- [[claude-code-memory-systems/_index]] — the 6-level memory taxonomy
- [[statelessness-and-context-cost]] — the same weakness, from the cost side
- [[claims-scorecard]]
