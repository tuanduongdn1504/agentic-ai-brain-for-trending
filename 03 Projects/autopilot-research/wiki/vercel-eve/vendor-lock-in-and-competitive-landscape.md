# Eve: vendor lock-in & competitive landscape

## Source
- Bundle `raw/2026-07-18-vercel-eve/` (Syntax `t2`, Elie Steinbock `t4`, openclaw `t7`). Primary grounding: [Vercel blog](https://vercel.com/blog/introducing-eve) + README.

## The lock-in question (the central criticism)

- Eve is **Apache-2.0** — but the community's real objection is that **production-grade features are optimized for Vercel infra**: Workflow durability, Sandbox, AI Gateway, Edge-network channels.
- **Nuance (verified — this is "pragmatic," not hard, lock-in):**
  - Durability runs on the **open-source Workflow SDK (WDK)** — not proprietary.
  - Sandbox is **adapter-based** (Docker / microsandbox / local; other providers possible).
  - AI Gateway has **provider fallbacks**; observability is standard **OpenTelemetry**.
  - Channels are TS adapters inside the Apache-2.0 codebase.
- Vercel's **own** framing (per primary sources): *"open source, runs anywhere"* is **directionally true but not fully realized in practice.** This is the honest center of gravity: you *can* run pieces elsewhere, but the smooth path — and the best performance — is Vercel. Same playbook as Next.js (runs anywhere; ISR/middleware/server-actions shine on Vercel).
- ⚠️ One overstatement corrected: the flat claim that core features *"run on Vercel proprietary infrastructure"* is **MISLEADING** — WDK is open-source and adapters exist. See [[vercel-eve/caveats-and-corrections]].

## Competitive landscape (verified where checkable)

| Framework | Position | Note |
|---|---|---|
| **Mastra** | **Closest direct rival** | TS-first; durable execution via open-source **Inngest**; **platform-agnostic** (AWS/GCP/self-host). The go-to if you want Eve's DX **without** Vercel binding. |
| **Flu(e)** (Fred Schott, Astro creator) | "The open agent framework" | "Write once, deploy anywhere" philosophy; lower maturity/adoption than Eve. (Elie Steinbock's Eve-vs-Flue comparison; Syntax also names it.) |
| **LangGraph** | Graph-based state control | Max flexibility for complex stateful workflows; less convention than Eve. |
| **OpenAI AgentKit** | Vendor-agnostic | Deployable AWS/GCP/self-host; less integrated tooling. |
| **Dawn** | Also "directory-as-agent" | Same emerging pattern → suggests directory-as-agent is becoming a de-facto convention, not Eve-specific. |
| **Manual composition** | DIY | Next.js + Claude Code + AI SDK + MCP from first principles; max flexibility, highest build cost (Elie Steinbock's pragmatic stance). |

- **Standard Agent spec** (agent.org) exists but is **not yet public** (Syntax: Scott has access). Sandboxing makes frameworks *safer but less useful out-of-the-gate* than more open agents (e.g., Hermes / OpenClaw) — the classic safety-vs-utility trade.

## Key Takeaways

- Lock-in is **pragmatic, not hard**: Apache-2.0 + WDK-open + adapters, but production leans Vercel — by Vercel's own admission.
- **Mastra is the strongest vendor-neutral alternative** (platform-agnostic durability via Inngest) — the natural comparison for anyone needing self-host/multi-cloud.
- "Directory-as-agent" is a **converging industry pattern** (Eve, Dawn, Flue), not a Vercel invention — the moat is DX + distribution, à la Next.js.

## See also
- [[vercel-eve/deployment-and-claude-code-plugin]] · [[vercel-eve/hireui-translation]] · [[vercel-eve/caveats-and-corrections]]
- Storm Bear pilot threads (prose ref, cross-vault): Mastra (competitor), Archon (harness *builder* — contrasting DIY/portable philosophy).
