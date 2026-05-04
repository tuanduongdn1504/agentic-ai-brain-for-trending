# pi-ai + pi-agent-core — Foundation libraries

**Entity type:** Foundation libraries (underneath pi-coding-agent)
**npm:** `@mariozechner/pi-ai` + `@mariozechner/pi-agent-core`
**Location:** `packages/ai/` + `packages/agent/` in `badlogic/pi-mono` monorepo
**Wiki version:** v1 (2026-04-23 — pi-mono wiki v1, 36th LLM Wiki)

---

## What these packages are

`pi-ai` and `pi-agent-core` are the **foundation layers** underneath pi-coding-agent. Together they provide:

- **pi-ai:** 20+-provider unified LLM API with type-safe tool definitions, streaming with partial JSON tool arguments, cross-provider context handoffs mid-conversation, cost tracking built-in
- **pi-agent-core:** Stateful agent runtime built on pi-ai — tool execution (parallel or sequential), event streaming, message queues for steering/follow-up, hook system for before/after tool calls

Other packages in the monorepo (`pi-coding-agent`, `pi-mom`, `pi-web-ui`) all depend on pi-agent-core, which itself depends on pi-ai. This creates a **3-level foundation stack**: pi-ai → pi-agent-core → {pi-coding-agent | pi-mom | pi-web-ui}. pi-pods, pi-tui do not depend on this stack (pi-pods is a standalone CLI; pi-tui is a general-purpose TUI library usable by pi-coding-agent for rendering).

---

## pi-ai: 20+ provider unified LLM API

**Tagline:** *"Unified LLM API with automatic model discovery, provider configuration, token and cost tracking."*

### Providers (20+)

From pi-ai README + provider-extension checklist in AGENTS.md:

1. Anthropic
2. OpenAI
3. Google (Gemini)
4. Google Vertex
5. Amazon Bedrock
6. Mistral
7. Groq
8. Cerebras
9. xAI
10. OpenRouter
11. Vercel AI Gateway
12. Azure OpenAI
13. GitHub Copilot
14. ZAI
15. OpenCode Zen
16. OpenCode Go
17. Hugging Face
18. Fireworks
19. Kimi For Coding
20. MiniMax
21. OpenAI-compatible (Ollama, vLLM, LM Studio, custom endpoints)

### Key architectural features

**Type-safe tool definitions via TypeBox:**
Tool schemas double as validation (runtime) and serialization (across distributed systems). Contrast OpenAI SDK's `zod`-based approach or Anthropic SDK's direct JSON schema.

**Thinking-as-text transformation:**
Cross-provider compatibility by converting reasoning blocks (Claude's `thinking` / OpenAI's `reasoning`) to tagged text, allowing mid-session provider handoffs without losing reasoning context. `streamSimple()` / `completeSimple()` offer provider-agnostic thinking interface.

**Cross-provider context handoffs:**
Single conversation can switch from Claude → GPT-5 → Gemini mid-session. Thinking blocks preserved. This is a **differentiator vs LiteLLM** (which handles provider abstraction but not context handoff) and vs Claude Code (single-provider-locked).

**Context serialization:**
Database persistence + transfer between services. Enables distributed agent workflows.

**Granular event types:**
Streaming events: `text` / `thinking` / `tool_call` (with partial JSON parsing) / `usage` / `stop` / `error`. Extensions can subscribe to any of these.

**Registry pattern with lazy loading:**
Providers registered via `register-builtins.ts` lazy-loader wrappers (per AGENTS.md §Adding a New LLM Provider). No static imports of provider implementations from the registry — prevents bloat when only 1 provider is used.

**Cost tracking built-in:**
Every response includes token-usage + cost, not bolted-on. Contrast with manual cost-calculation in most OpenAI-SDK apps.

### Basic usage pattern

```ts
import { getModel, stream } from '@mariozechner/pi-ai';

const model = await getModel('anthropic', 'claude-3.5-sonnet');
const context = { messages: [...] };
for await (const event of stream({ model, context, tools: [...] })) {
  // handle text, thinking, tool_call, usage, stop events
}
```

---

## pi-agent-core: stateful agent runtime

**Tagline:** *"Stateful agent with tool execution and event streaming built on the pi-ai library."*

### Architecture

Three-layer message transformation:
```
AgentMessage[] → transformContext() → convertToLlm() → pi-ai messages
```

Events flow through subscribers for UI updates. **Synchronous barrier** ensures message processing completes before tool execution begins — avoiding race conditions between message finalization and tool validation.

### Key features

**Flexible message system:**
Supports custom app-specific types via TypeScript declaration merging. Apps can extend `AgentMessage` union with their own message variants.

**Streaming event architecture:**
20+ granular event types (`agent_start`, `message_update`, `tool_execution_start`, `tool_execution_end`, etc.). UI layers subscribe to specific events for targeted updates.

**Configurable tool execution modes:**
Parallel (all tools at once) or sequential (one at a time). Hooks `beforeToolCall` / `afterToolCall` for validation + post-processing.

**Message queues:**
- **Steering queue** — interrupt current turn; message delivered after this turn
- **Follow-up queue** — message delivered after ALL work (including queued tool calls) completes

Allows user to queue clarifications/corrections while agent is mid-work.

**Thinking level support:**
Customizable token budgets (off / minimal / low / medium / high / xhigh).

### Design trade-off

**Synchronous barrier sacrifices some performance for deterministic state guarantees.** This distinguishes pi-agent-core from raw async generators — the barrier enforces "all tool calls in an assistant message are validated before any tool executes." Claude Code takes a similar approach; OpenAI's raw streaming API does not enforce this barrier.

---

## Combined implications

The pi-ai + pi-agent-core pair is essentially **Claude Code's core engine, unbundled and made provider-agnostic**. If Mario ever stops pi-coding-agent development, a community fork or an entirely different coding-agent could be rebuilt on pi-ai + pi-agent-core with manageable effort — the foundation is OSS, type-safe, and provider-flexible.

This is structurally significant: pi-mono is NOT just a pi-coding-agent distribution — it's an **open-source coding-agent engine** that anyone can build on. The root README's ask — *"Share your OSS coding agent sessions"* — becomes a training-data flywheel for this engine.

---

## Corpus-relevance: Pattern #28 Multi-Provider AI Support

Pattern #28 (CONFIRMED v25 audit) has N=6+ prior data points. Existing sub-variants:
- **Abstraction-library adoption (LiteLLM):** TrendRadar v19 (100+ providers via LiteLLM), crawl4ai v29 (LiteLLM fork for supply-chain security)
- **Native framework-level routing:** multica v15 (native BYO across 8 models), Skyvern v24 (native BYO 8+ providers), OpenHands v30 (SDK-level routing), markitdown v28 (`llm_client` DI)

pi-ai is **a NEW sub-variant class: "native-built-in multi-provider AT T1 coding-agent scope"** (distinct from pure-abstraction libraries OR DI-pattern libraries OR framework-level routing for T5 apps). This is a **refinement candidate for Pattern #28 at next mini-audit.**

At v36 pi-ai is flagged for observation but NOT registered as a separate candidate (consolidation-forward discipline; Pattern #28 is already confirmed — refinement is appropriate mechanism).

---

## pi-skills interop bridge (corpus-relevant sibling)

Mario published `badlogic/pi-skills` (1.3K stars, MIT, JavaScript-primary, created 2025-12-12) as a separate repo: *"Skills for pi coding agent (compatible with Claude Code and Codex CLI)."*

**Interop implication:** pi-skills follows the emerging **Agent Skills standard** that works across multiple runtimes. This is Pattern #18 Agent Runtime Standardization's **skill-layer** variant — distinct from MCP's **tool-layer** standardization that pi rejects.

At v36 this is observational; Pattern #18 at N=9+ MCP-consumers + 2 skill-layer-interop examples (pi-skills + anthropics/skills referenced in graphify v16 earlier). If 3rd skill-standard-interop emerges explicitly, consider Pattern #18 refinement to "dual-layer standards: MCP at tool layer + Agent Skills at skill layer."

---

## Cross-references

- Cluster: `(C) Cluster — pi-coding-agent CLI + extensions + skills.md`; `(C) Cluster — AGENTS.md governance + lgtm gate + release cadence.md` (provider-integration checklist)
- Related entities: `(C) pi-coding-agent — Flagship terminal coding harness.md` (primary consumer); `(C) Mario Zechner — Austrian solo-flagship + ecosystem portfolio.md`
- Pattern observations:
  - Pattern #28 Multi-Provider AI Support — new sub-variant "native-built-in at T1-coding-agent scope" (refinement candidate)
  - Pattern #18 Agent Runtime Standardization — pi-skills extends skill-layer-interop hypothesis (observation)

---

*(C) Claude-generated 2026-04-23 per routine v2.1.*
