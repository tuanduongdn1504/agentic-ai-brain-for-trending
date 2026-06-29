# Level 6 — A single brain for ALL your AI tools

> **Source:** [[claude-code-memory-systems/_index]] · video [35:13–end] + deep-dive of [OpenBrain / OB1](https://github.com/NateBJones-Projects/OB1) (Nate Jones) and [Mem0](https://mem0.ai/). **The only level where every AI tool shares the same memory — at the cost of leaving your laptop.**

**The problem L6 solves:** everything in L1–L5 lives **inside Claude Code on one machine**. But your research from ChatGPT three months ago, the brainstorm on your phone, your Cursor sessions — none of them know about each other. L6 is the **infrastructure layer for your thinking**: one DB, one channel, any AI plugs in.

## OpenBrain / OB1 (Nate Jones) — own your brain

- **Premise:** *"One database, one AI gateway, one chat channel. Any AI you use can plug in. No middleware, no SaaS chains."* Every tool (Claude Code, ChatGPT, Claude Desktop, Cursor) reads/writes the **same** persistent memory.
- **Architecture:**
  - **Data:** **PostgreSQL on Supabase**; core table **`thoughts`** = one row per memory = *text chunk + embedding vector + tags + timestamp*; **pgvector** for semantic search.
  - **Access:** an **MCP server** + **Supabase Edge Functions** as the gateway (JSON-RPC) — the "front door" every AI tool queries via vector similarity + metadata filtering.
  - **Extensibility:** Schemas (extra tables) + Skills (reusable prompt packs) + Recipes (standalone workflows).
- **You own it:** it's *your* Supabase project — **export the whole Postgres DB anytime**, control which tools get access. When the next big AI tool ships in 6 months, you just connect it — **no migration**.
- **Cost:** the *video* says **"less than a dollar a month"** / "10–30p on Supabase's free tier." **⚠️ The repo does not state pricing** — treat the figure as a **video claim**, flagged in [[claude-code-memory-systems/source-provenance]]. License: **FSL-1.1-MIT**.
- **Setup:** **~45 min** (Supabase provisioning → Edge Function deploy → capture integration → MCP config), or **AI-assisted setup** by pointing Claude Code/Cursor at the repo; a ~27-min video walkthrough + **companion prompts to migrate** existing Claude memory into OpenBrain. There's a live community on the GitHub.
- **The honest downsides (video):** **most complex setup** in the taxonomy; **external DB = network latency on every query** (you query a remote DB each time, vs a local file/index); data lives **off your laptop** (secure, but not local).

## Mem0 — the well-funded hosted alternative

- A **cross-tool memory layer** — well-funded, well-marketed, "used by 100,000 developers," **<1-min setup**, "universal self-improving AI memory layer for your LLM applications," cross-tool.
- **When to choose it:** if you're **shipping an AI product** and want production-ready strength rather than a DIY Supabase project.
- **Downside vs OpenBrain:** your data lives on **Mem0's servers permanently** — you don't own/export the store the way you own a Supabase Postgres DB.

## OpenBrain vs Mem0 — the axis

Same trade-off that runs through the whole taxonomy (readable/owned vs managed/opaque), now at the *cross-tool* layer:

| | OpenBrain / OB1 | Mem0 |
|---|---|---|
| **Ownership** | You own the Postgres DB; export anytime | Hosted; data on their servers |
| **Setup** | ~45 min (or AI-assisted) | < 1 min |
| **Best for** | Max control + portability, personal "brain" | Shipping an AI product, fast start |
| **Cost** | Video: pennies/mo on Supabase free tier *(repo unconfirmed)* | SaaS pricing |

## Should you go here?

The video's guidance: **skip L6 if you live mostly inside Claude Code on one machine.** Go here only if you genuinely **switch between AI tools constantly** (ChatGPT on phone + Claude Code at desk + Cursor) and want them to share memory in real time. It's *"the most future-proof + portable"* — and the **most complex + the only one with meaningful monthly cost + added latency.**

## Key Takeaways

- L6 = **one memory shared across every AI tool**, via a database + an MCP/gateway front door — the only level that escapes the single-tool, single-machine box.
- **OpenBrain/OB1**: your own **Postgres-on-Supabase** (`thoughts` table + pgvector) + MCP server + Edge Functions; **you own + export** it; ~45-min setup; **video-claimed** pennies/month (repo unconfirmed); FSL-1.1-MIT.
- **Mem0**: hosted, <1-min start, production-grade — but **data lives on their servers**. Choose it when shipping a product, not for a personal owned brain.
- **Costs of cross-tool reach:** most complex setup, real monthly cost, and **per-query network latency** (remote DB), and data off your laptop.
- Same **own-it-readable vs managed-opaque** axis as L3 (MemSearch vs claude-mem) and L4 — now at the portability layer.
