# Eve production features — durability, sandbox, HITL, evals

## Source
- Bundle `raw/2026-07-18-vercel-eve/` (Cole Medin `t1`, Infisical `t6`, openclaw `t7`). Primary grounding: [Vercel blog](https://vercel.com/blog/introducing-eve) + [github.com/vercel/eve](https://github.com/vercel/eve).

This is what distinguishes Eve from a "personal agent in a folder": production-grade reliability primitives, all framework-managed.

## Durable sessions (confirmed)

- Every session is a **checkpointed durable workflow**, built on Vercel's **open-source Workflow SDK / Workflow Development Kit (WDK)** — *not* proprietary tech.
- *"Each step checkpointed, so a session can pause, survive a crash or a deploy, and resume exactly where it stopped."* No manual durability code.

## Human-in-the-loop (confirmed)

- Any tool/action can carry a **`needsApproval: true`** field. The agent **pauses indefinitely, consuming zero compute**, until a human approves.
- Demoed live in Slack (approve/deny buttons on a risky SQL query). This is the safety/cost gate that maps cleanly onto governance requirements — see [[vercel-eve/hireui-translation]].

## Evals as a deploy gate (confirmed)

- `evals/` holds **scored TS test suites**; they run on deploy and **gate regressions before production** (green-checks-before-ship). Integrates into CI/CD.

## Credential brokering (confirmed)

- `connections/` **brokers OAuth + token refresh at the framework level**; real credentials are injected on-the-wire at request time; **the agent/model never holds or sees real keys** (dummy `.env` locally). Infisical's angle emphasizes this as the security story.

## Sandbox (confirmed; details partial)

- Agent-generated code runs **isolated**: **Vercel Sandbox** (hardware-isolated) in prod; **Docker / microsandbox / just-bash** locally; adapter-based (other providers possible).
- ⚠️ Isolation *strength varies by adapter* — local bash is weakest; the exact auto-selection/fallback order is **not documented**. No published escape-vector/resource-limit guarantees. See [[vercel-eve/caveats-and-corrections]].

## Observability (confirmed)

- **OpenTelemetry** spans exported to Braintrust / Raindrop / Arize / Honeycomb / Datadog / Jaeger; an **"Agent Runs"** tab on the Vercel dashboard shows a step-by-step execution timeline.

## Multi-channel + schedules (confirmed)

- One agent definition serves **HTTP + web chat + Slack + Discord + Teams + Telegram + Twilio + GitHub + Linear**. `schedules/` (cron) deploy as Vercel Cron Jobs for autonomous runs.

## Claims to treat with caution (verified)

- **"Scales to thousands/millions of concurrent users"** — UNVERIFIABLE from primary sources; no published capacity/throughput/concurrency numbers, and it's beta. Marketing-adjacent.
- **Billing model** for durable-session state storage, cron at scale, and sandbox resource use is **not published** — cannot forecast cost. (Gap.)

## Key Takeaways

- Durable checkpointed sessions (open-source **WDK**), **`needsApproval` HITL**, **evals-as-deploy-gate**, **credential brokering** (keys never reach the model), OTel observability — a genuinely strong reliability stack **on paper**.
- Sandbox isolation is real but **adapter-dependent** and under-documented on guarantees.
- **Scaling + pricing claims are unverified** — treat as aspirational until GA docs land.
- The HITL + evals + creds-never-on-agent triad is the part most relevant to governance-heavy use — see [[vercel-eve/hireui-translation]].

## See also
- [[vercel-eve/primitives-and-file-structure]] · [[vercel-eve/claims-scorecard]] · [[vercel-eve/caveats-and-corrections]]
- [[agent-development-lifecycle/_index]]
