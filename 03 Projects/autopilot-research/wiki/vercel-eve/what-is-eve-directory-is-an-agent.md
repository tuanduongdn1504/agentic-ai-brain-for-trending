# What is Vercel Eve — "an agent is a directory"

## Source
- Bundle `raw/2026-07-18-vercel-eve/` (7 transcripts). Primary grounding: [Vercel blog — Introducing eve](https://vercel.com/blog/introducing-eve), [github.com/vercel/eve](https://github.com/vercel/eve), [Vercel changelog](https://vercel.com/changelog/introducing-eve-an-open-source-agent-framework).
- Anchor video: Cole Medin, [`m8VC2SV2igM`](https://www.youtube.com/watch?v=m8VC2SV2igM) — **⚠️ creator disclosed on-camera "I worked with Vercel on this video."** Cross-checked against independent sources.

## The core idea

- **Eve** is Vercel's **open-source, filesystem-first framework for durable AI agents**. Tagline: *"A filesystem-first framework for durable AI agents. Core agent capabilities live in conventional locations, so projects are easier to inspect, extend, and operate."*
- **Central thesis: "an agent is a directory."** File placement + naming define capabilities — the same mental model Next.js applied to routing. As openclaw puts it: *"Next.js is folders-as-routes; Eve is directories-as-agents."*
- An Eve agent is **just a folder of markdown + TypeScript**. You drop a skill in `skills/`, a tool in `tools/`, an MCP server in `connections/` — and Eve's **compilation step** traverses the folder, discovers everything, and builds a single wired manifest. No manual imports/hookup in the main `agent.ts`. (Confirmed — this is the genuinely novel packaging.)
- What's novel is the **packaging/ergonomics, not the components.** Durable execution, sandboxing, model gateways already existed elsewhere in 2026; Eve's contribution is compressing scaffolding to ~1 minute and standardizing the layout (verified — see [[vercel-eve/vendor-lock-in-and-competitive-landscape]]).

## Facts (primary-source verified)

- **Vendor:** Vercel. **License:** Apache-2.0. Language: TypeScript (pnpm-workspaces monorepo).
- **Launched:** Vercel Ship London, **2026-06-17**. **Status: PUBLIC PREVIEW / BETA** (Vercel beta terms; APIs/behavior/docs may change before GA — no published GA date).
- **Model-agnostic:** model chosen in `agent.ts`, routed through Vercel **AI Gateway** with provider fallbacks; **Claude Opus 4.8** supported at launch.
- **Why Vercel built it:** on stage they reported agent-triggered deployments went **from <3% to ~29% over ≈1 year** (projected ~50% soon). ⚠️ One source (openclaw) said "6 months" — that is **FALSE**; Vercel's blog says *"a year ago."* See [[vercel-eve/caveats-and-corrections]].

## Positioning

- Framed by Vercel as **complementary to MCP / Claude Code, not competitive** — *"MCP is a standard, Eve is a carrier."* You can use Claude Code to *generate* an Eve agent, then `vercel deploy` it.
- Cole Medin frames Eve as a **standard-in-the-making** for filesystem-based agents (analogy to how a `skill.md` dropped in a folder "just works" in Claude Code) — but hedges it may not become *the* standard. (Opinion, flagged.)

## Key Takeaways

- Eve = **Apache-2.0, filesystem-first, durable** agent framework by Vercel; an agent is a **directory of markdown + TypeScript**, auto-compiled into a wired manifest.
- The innovation is **ergonomics/packaging** (Next.js-for-agents), not the underlying primitives.
- **Beta / public preview** — not production-stable yet; no GA date.
- The "why now" stat is real but the timeframe is **≈1 year, not 6 months**.
- Anchor source is **Vercel-collaborated** (Cole Medin) — every load-bearing claim here is cross-checked against Vercel's own docs + independent devs.

## See also
- [[vercel-eve/primitives-and-file-structure]] · [[vercel-eve/production-features]] · [[vercel-eve/claims-scorecard]] · [[vercel-eve/hireui-translation]]
- [[claude-skills/_index]] (the `skill.md`-in-a-folder analogy) · [[agent-development-lifecycle/_index]]
