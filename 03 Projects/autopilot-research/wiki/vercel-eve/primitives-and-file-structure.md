# Eve primitives & file structure (the 10 directories)

## Source
- Bundle `raw/2026-07-18-vercel-eve/` (esp. Cole Medin `t1`, Syntax `t2`, openclaw `t7`). Primary grounding: [Vercel blog](https://vercel.com/blog/introducing-eve) + [github.com/vercel/eve](https://github.com/vercel/eve) README.

## The directory-as-agent layout

An Eve agent folder is a set of **conventional files/directories**, auto-discovered at compile time. Ten primitives (primary-source verified):

| Primitive | Required? | Purpose |
|---|---|---|
| `instructions.md` | **Required** | Always-on system prompt (agent personality/rules). Editable by non-devs. |
| `agent.ts` | Optional | Model + runtime config; provider fallbacks via AI Gateway. A minimal agent = just this + `instructions.md`. |
| `tools/` | Optional | One TS file = one tool; `defineTool` + **Zod** schemas; **auto-registered** with the agent loop (no imports/wiring). |
| `skills/` | Optional | Procedures/markdown **loaded on demand** (contextually) to save tokens. |
| `connections/` | Optional | **MCP servers OR OpenAPI APIs.** Framework brokers OAuth + token refresh; **credentials never reach the model.** Slack/GitHub/Snowflake/Salesforce/Notion/Linear at launch. |
| `channels/` | Optional | Adapters exposing one agent on many surfaces: HTTP, Slack, Discord, Teams, Telegram, Twilio, GitHub, Linear. Channels can hand off to each other. |
| `sandbox/` | Optional | Isolated execution for agent-generated code. Vercel Sandbox (prod) / Docker / microsandbox / just-bash (local); adapter-based. |
| `subagents/` | Optional | Child agents with **isolated context windows + restricted tool access**. |
| `schedules/` | Optional | Cron definitions → deploy as Vercel Cron Jobs. |
| `evals/` | Optional | Scored TS test suites; **deploy gate** — catch regressions before prod. |

> ⚠️ **Note on scope of `npx eve@latest init`:** the init wizard scaffolds a **core** subset (instructions.md, agent.ts, tools/, skills/, channels/, schedules/). The optional `connections/`, `sandbox/`, `subagents/`, `evals/` dirs are **added as needed**, not all scaffolded up front. A minimal working agent needs only `instructions.md` + a tool + model config.

## The compilation step (the actual magic)

- Running or deploying **traverses the single folder**, finds all skills/tools/MCP servers/etc., and builds **one manifest that wires everything together**.
- Consequence: the "entry point" (`agent.ts`) stays tiny; you never `import` a skill or tool by hand. Cole Medin: this is *"way different than what you see in other AI agent frameworks."* (Confirmed as the core auto-discovery behavior.)
- Directly analogous to how Claude Code auto-discovers a `skill.md` dropped into a skills folder (see [[claude-skills/_index]]).

## Claims that are weaker than they sound (verified)

- **Subagent independence is under-documented.** Primary sources confirm "isolated context windows + restricted tool access" — but do **not** confirm per-subagent *independent model selection*, per-subagent *sandboxes*, or the exact delegation trigger. Treat richer subagent claims as inference, not fact.
- **Sandbox auto-selection chain** ("Docker → lighter VM → pure JS") is **not documented** by Vercel — only that adapters exist. See [[vercel-eve/caveats-and-corrections]].

## Key Takeaways

- **10 primitives**, all optional except `instructions.md`; capability = file/dir placement.
- `tools/` (Zod-typed TS), `skills/` (on-demand markdown), `connections/` (MCP **or** OpenAPI, creds brokered) are the workhorses.
- The **compilation/auto-discovery** step is the real differentiator — zero manual wiring.
- `init` scaffolds a **core subset**, not all 10 dirs.
- Subagent + sandbox-selection details are **thinner than creators imply** — flagged.

## See also
- [[vercel-eve/production-features]] · [[vercel-eve/deployment-and-claude-code-plugin]] · [[vercel-eve/what-is-eve-directory-is-an-agent]]
- [[claude-skills/_index]] · [[claude-code-skills-stack/_index]]
