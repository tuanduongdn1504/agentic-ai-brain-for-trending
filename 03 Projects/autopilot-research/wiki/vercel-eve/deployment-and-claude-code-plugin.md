# Deploying Eve + the Vercel Claude Code plugin

## Source
- Bundle `raw/2026-07-18-vercel-eve/` (Cole Medin `t1`, Sonny Sangha `t3`, openclaw `t7`). Primary grounding: [Vercel blog](https://vercel.com/blog/introducing-eve) + README.

## The developer loop (confirmed)

1. **Scaffold:** `npx eve@latest init my-agent` (or `npx eve@latest init .` into an existing project) → core directory structure in <1 minute.
2. **Edit:** `instructions.md` (who the agent is) + `agent.ts` (model) + drop a TS file in `tools/`.
3. **Run locally:** an interactive **TUI** via `eve dev` / `npm run dev` — chat with the agent in the terminal, switch models with slash commands.
4. **Deploy:** `vercel deploy` → production with built-in durable workflows, sandboxes, cron.

## The Vercel plugin for coding agents (confirmed)

- Vercel ships a **plugin for Claude Code / Cursor**, installed with a single command. It bundles:
  - **Vercel Eve skills** — so your coding agent already knows Eve's structure (how to build channels, skills, schedules, sandbox) and can scaffold/extend agents for you.
  - the **Vercel MCP** server for deploying.
- Net effect (Cole Medin demo): you can tell Claude Code **"Scaffold a new Eve agent called X"** or **"Deploy this Eve agent"** and it does the whole thing — including a smoke test. This is the **plugin-as-delivery-mechanism** pattern (cf. [[claude-code-plugins-stack/_index]]).
- Vercel's framing: Eve is **complementary to Claude Code** — use the coding agent to *generate* the Eve agent, deploy via Vercel.

## Friction points the sources flagged (verified)

- **Slack setup is genuinely manual** — Cole Medin: *"a good number of steps… good number of manual things you have to do"* to create/wire the Slack app, even with Claude Code guiding it. Framework convenience stops at the third-party OAuth boundary.
- **Manual credential/env scaffolding** — dummy `.env` values + separately-brokered real keys adds operational steps vs. seamless injection.

## Self-hosting: NOT a documented path (verified — UNVERIFIABLE claim)

- Sonny Sangha suggested **`eve build` compiles to a standard Nitro output** for self-hosting. This is **NOT in Vercel's official docs.** Vercel's documented deploy path is **`vercel deploy`.**
- Eve is Apache-2.0 with local/Docker adapters, so off-Vercel deployment is *plausible* — but there is **no tested flow, doc, or roadmap** for standalone Eve. Treat self-hosting as unproven. See [[vercel-eve/vendor-lock-in-and-competitive-landscape]].

## Key Takeaways

- `init → edit → eve dev → vercel deploy` — scaffolding in ~1 min; the intended prod target is Vercel.
- The **Claude Code / Cursor plugin** (Eve skills + Vercel MCP) makes "scaffold/deploy an agent" a one-instruction coding-agent task.
- Real-world friction lives at **third-party OAuth (Slack)** and **credential scaffolding**, not in Eve itself.
- **Self-hosting (`eve build` → Nitro) is unverified** — do not assume a supported exit route from Vercel.

## See also
- [[vercel-eve/vendor-lock-in-and-competitive-landscape]] · [[vercel-eve/production-features]]
- [[claude-code-plugins-stack/_index]] · [[claude-code-skills-stack/_index]]
