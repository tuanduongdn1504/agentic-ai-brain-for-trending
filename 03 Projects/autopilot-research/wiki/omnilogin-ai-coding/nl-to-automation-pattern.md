# Original #5 — The "NL → script + self-config UI + output" pattern

## Source

Workflow `wf_1ac2a814-456` facet 5 + verifications. References: CopilotKit generative-UI, Google **A2UI**, **AG-UI** protocol, AutoAgent/UI-Genie papers, Playwright codegen docs, Skyvern/Browser-Use/Stagehand comparisons (WebVoyager), UiPath/RPA analyses, Anthropic MCP.

## What's actually novel here

The video's feature is **not** "AI writes code" (old) and **not** "AI clicks the browser for you" (browser agents). The keeper idea is narrower and 2026-current:

> **The agent generates the automation script *and* a parameterized config UI for it *and* an output view — so the artifact is a re-runnable mini-tool a non-coder can operate.**

That middle piece — **agent-generated UI** — is the 2026 development the field calls **generative UI** (CopilotKit) / **A2UI** (Google) / **AG-UI**: agents emit a **declarative JSON blueprint of UI components** with data bindings, which the client renders as native widgets. The win the research found quantified: two-way client-side binding eliminates ~80% of manual form-wiring code, and a single agent backend can render the same form to web/mobile/desktop.

## Where it sits vs the tools you already know

| Approach | What it does | How the video's feature differs |
|---|---|---|
| **Playwright codegen** (`playwright codegen`) | Record clicks → emit a script (record-playback) | Brittle, no NL intent, **no config UI**; video generates from a *description* + emits a runnable UI |
| **Classic RPA** (UiPath, Automa, n8n) | Static, predetermined visual workflows | Non-learning; video uses **semantic intent** + LLM generation |
| **Browser agents** (Skyvern, Browser-Use, Stagehand) | *Execute* a task live (WebVoyager: Browser-Use 89%, Skyvern 86%) | They **run** tasks; they don't hand you a **re-runnable artifact + config UI** for non-coders |
| **Claude Code / MCP** | Agent writes + runs code with tool access | Closest cousin; the video adds the **packaged config-UI deliverable** for non-technical re-use |
| **Omnilogin AI Coding** (this video) | NL → **script + config UI + output**, BYO-model, verify-fix loop | = generative UI applied to browser automation, vendor-packaged |

## The honest caveats (verification corrected the hype)

- **"AI generates a *complete* automation from NL"** → **overstated.** Real agentic task success is ~62% at best; production failure rates 70–95% on hard flows; ~68% of practitioners require human review within ≤10 autonomous steps. The video's **iterate-fix loop is not optional** — it's how you get from a 62%-correct draft to a working script.
- **"Agents generate their own config UI"** → **true with a nuance:** they compose forms from **pre-approved component catalogs** (A2UI/AG-UI widget sets), not arbitrary free-form interfaces. Bounded, but real.
- **Non-coders can re-run** → confirmed for the *config-form-driven* artifact (Skyvern, Replit Agent prove the shape); the re-run surface is the UI, not the code.

## Why this matters for the operator (Goal #2)

This pattern is **the shape of a hireui recruitment-automation feature**: a recruiter describes a screening step in plain language → the system generates a **parameterized, re-runnable automation + its config form** (candidate source, criteria, output format). It's the same architecture as [[multi-agent-orchestration/_index]]'s job-application-screener, with the generative-UI layer added so non-engineers operate it. The transferable engineering is: **decouple agent reasoning from UI presentation** (testable, portable) + **client-side binding** (fewer round-trips) + **semantic intent replaces hard-coded rules** (adapts to new job specs without redeploy).

## Key takeaways

- The novel unit is **code + generated config UI + output**, not code alone — that's "generative UI" (A2UI/AG-UI), a real 2026 standard.
- It is **distinct** from Playwright codegen (record-playback), RPA (static), and browser agents (execute-don't-package).
- **Generation is ~62%-correct, not magic** — the verify-fix loop is load-bearing; keep the human gate.
- For hireui, this is a **feature blueprint**, not a tool to buy.

## Cross-links

- [ai-coding-feature](ai-coding-feature.md) — the concrete three-pane implementation
- [[multi-agent-orchestration/_index]] — the job-screener that this could front-end
- [[harness-engineering/_index]] — verify-loops as the quality mechanism
- [[claude-skills/_index]] — package this as a reusable skill
