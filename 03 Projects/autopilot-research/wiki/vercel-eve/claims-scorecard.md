# Eve claims scorecard (30 claims verified)

## Source
- Refute-first verification workflow `wf_e215817b-a5d` (7 digests → consolidate → per-claim refute-first verify against primary sources → synthesis + completeness critic). Bundle `raw/2026-07-18-vercel-eve/`.

## Tally

**30 load-bearing claims:** **14 CONFIRMED · 10 CORRECT-BUT-INCOMPLETE · 4 UNVERIFIABLE · 1 FALSE · 1 MISLEADING** (0 fabricated).

Profile: the framework's headline mechanics are **real**; the failures are (a) one timeframe error, (b) one security-posture overstatement, and (c) a cluster of *under-documented specifics* creators asserted with more confidence than Vercel's own docs support.

## CONFIRMED (14)

- Open-source (Apache-2.0) agent framework by Vercel.
- Durable, checkpointed workflows survive crashes/restarts (open-source **Workflow SDK**), no manual code.
- Human-in-the-loop / approval gate on any tool (`needsApproval`).
- Cron scheduling via `schedules/`.
- **Evals as a deploy gate** (scored suites, catch regressions pre-prod).
- Tools + skills **auto-discovered/auto-loaded** — no manual imports.
- **MCP** server connections supported (first-class, alongside OpenAPI).
- Multi-channel from one definition: Slack/Discord/Teams/Telegram/Twilio/web(+GitHub/Linear).
- Model-agnostic; model set in `agent.ts`, routed via AI Gateway.
- Local dev via `eve dev` / `npm run dev`.
- Deploys via `vercel deploy` (durable workflows + sandboxes + cron built in).
- **Credential brokering** — real keys in a vault, injected on-the-wire; agent never holds keys.
- "The Next.js of agent frameworks" (file-location-as-architecture, convention-over-config).
- Vercel ships a **Claude Code plugin** (auto-discovery of skills + deploy MCP).

## CORRECT-BUT-INCOMPLETE (10) — true, but missing a caveat

- **Directory-as-agent / primitive lists (c2, c3):** creators list 6–7 primitives; there are **10** (they omit `sandbox/`, `subagents/`, `evals/`). Channels = 8 (not 5); connections = MCP **or** OpenAPI.
- **`npx eve init` (c14):** scaffolds a **core subset**, not all dirs; minimal agent = instructions + a tool + model.
- **Sandbox isolation (c5):** real, but **strength varies by adapter** (local bash weakest); "throwaway" not explicitly guaranteed.
- **Subagents (c10):** "isolated context + restricted tools" confirmed; **independent models / per-subagent sandboxes / delegation trigger NOT confirmed**.
- **Sandbox auto-select chain (c20):** adapters confirmed; the **Docker→VM→JS fallback order is not documented**.
- **Lock-in (c17):** true-ish but the wording "runs on Vercel proprietary infra" **overstates** it — WDK is open-source, adapters exist → *pragmatic* lock-in.
- **Cron/durable billing (c28):** features confirmed; **billing model unpublished**.
- **Slack streaming/threading (c29):** Slack is a channel; **thinking-state streaming + threading impl not in docs**.
- **Component non-novelty (c30):** correct — the novelty is the **pattern/packaging**, not the components.

## UNVERIFIABLE (4) — not in primary sources, don't quote as fact

- **"Vercel Connect costs $3 / 10K token requests"** (Elie Steinbock) — no such pricing/term in Vercel docs.
- **Repo-caching internals** (~5GB template image, copy-on-write) — undocumented.
- **"Scales to thousands/millions of concurrent users"** — no capacity/throughput numbers; it's beta.
- **`eve build` → Nitro self-host** (Sonny Sangha) — not a documented flow.

## FALSE (1)

- **"<3%→29% of Vercel deployments in 6 months"** (openclaw) → Vercel's blog says **"a year ago"** → the move took **≈1 year**, not 6 months.

## MISLEADING (1)

- **"Deployed Eve agents are 'completely open' / need manual security config"** (Rob Shocks) → credential brokering + code sandboxing are **framework-managed by default**; "openness" refers to deployment/data-residency setup, not an insecure-by-default posture.

## Key Takeaways

- **14/30 clean-confirmed; 0 fabricated** — the core is solid.
- Every non-confirmed item is documented in [[vercel-eve/caveats-and-corrections]] with the corrected statement.
- **Do not quote** the $3/10K pricing, the sandbox fallback order, the scaling numbers, or `eve build` self-host as facts.

## See also
- [[vercel-eve/caveats-and-corrections]] · [[vercel-eve/sources-and-stances]] · [[vercel-eve/_index]]
