# Original: Higgsfield (the generation platform behind Scroll World)

## Source

Direct `WebFetch` of `higgsfield.ai/mcp` and `higgsfield.ai/pricing` (main loop, 2026-07-14) + Workflow `wf_885d81d7-1a2` dive/verify `higgsfield-platform`.

## What Higgsfield is

Higgsfield is a real, currently-operating AI media-generation platform that aggregates multiple third-party image/video models behind one account, one credits system, and (relevant here) one MCP server + CLI so coding agents can call it directly.

## MCP server — confirmed directly, one correction made

A direct `WebFetch` of `higgsfield.ai/mcp` confirms an official MCP server product. **The real setup flow, quoted from the page:**

1. Copy the Higgsfield MCP URL: `https://mcp.higgsfield.ai/mcp`
2. In your agent's settings, go to **Settings → Connectors**, add a custom connector, name it "Higgsfield," and paste the URL.
3. Click **Add → Connect**, then sign in with your Higgsfield account. No API key is required for this flow.

The page also states: *"If you are using Claude Code, Codex, OpenClaw, Hermes, it's better to use the CLI."* — i.e. there is a separate, CLI-specific install path for terminal-resident coding agents, distinct from the generic Settings→Connectors UI flow above.

**Correction (Rule 12 fail-loud):** one workflow dive agent asserted a specific setup command — `claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp` — as if it were lifted from Higgsfield's docs. It is not; it does not appear anywhere on the fetched page. This looks like a plausible-sounding but invented command (the general shape of a `claude mcp add` invocation is real Claude Code syntax, but Higgsfield's own documented flow is the Connectors UI, not this exact CLI line). **Excluded from this wiki's install instructions; use the Connectors flow above, or the CLI referenced by name only.**

## Models exposed — confirmed

The same `higgsfield.ai/mcp` page explicitly lists **"GPT Image 2"** and **Seedance 2.0** among its available models — directly confirming the video's claim that Higgsfield is what actually calls these two models on the user's behalf, for both Claude Code and Codex/OpenClaw/Hermes users. See [[scroll-world-animation-skill/original-gpt-5-6-and-fable-5]] for the model identities themselves.

## Pricing / credits — real system, unconfirmed exact numbers

Higgsfield uses a **credits**-based monthly-allowance pricing model — this is corroborated by multiple secondary sources (a workflow dive found tier names/amounts referenced around Starter/Plus/Ultra ≈ 200/1,000/3,000 monthly credits, and per-generation costs in the tens of credits for a single Seedance clip). **A direct `WebFetch` of `higgsfield.ai/pricing` by the main loop returned no usable pricing data** (the page is evidently client-side-rendered and the fetch only surfaced navigation chrome) — so the specific tier numbers above are **not independently confirmed by this wiki**, only by the workflow's own (Haiku-run) research pass.

The video's own claim — "~800 credits" for the six-scene reference example it describes (see [[scroll-world-animation-skill/overview]] for why "six scenes" and the actually-completed four-scene demo are two different things in the transcript) — could not be confirmed or refuted with confidence. Cheaper per-clip cost estimates from secondary sources would put a 6-scene run well under 800 credits, which suggests either higher-resolution/longer clips than a baseline estimate, multiple regeneration attempts, or simply an unverifiable creator-reported number. **Treat "~800 credits" as plausible but unverified, not confirmed.**

## The Higgsfield link is very likely a sponsor placement

The video description's **first link, above everything else** — including the presenter's own paid community — is `higgsfield.ai/s/cli-chase-h-ai-ejnlNI`. The `/s/` path structure plus the embedded `chase-h-ai` brand token is consistent with a referral/affiliate tracking link (Higgsfield is known to run creator-partnership programs), though the exact terms of that specific link were not independently confirmed. **Nothing in the 9:49 transcript discloses a sponsorship on camera** — the word "sponsor," "partner," or "ad" never appears in the spoken content; the only signal is the link's placement and structure. This matters for how to read the video's objectivity: the presenter has a plausible financial incentive to make Higgsfield look good, on top of his own incentive to promote his fork and his paid Skool community.

## Key takeaways

- Higgsfield's MCP server is real and directly confirmed; the exact install command in one workflow finding was invented and has been corrected here.
- GPT Image 2 and Seedance 2.0 are both genuinely available through Higgsfield, under those names.
- The credits pricing system is real; the specific "~800 credits for 6 scenes" figure is unverified, not confirmed.
- The video very likely has an undisclosed Higgsfield sponsorship (link placement/structure), which should temper how much weight to give the presenter's product opinions in this space.

## Cross-links

[[scroll-world-animation-skill/_index]] · [[scroll-world-animation-skill/original-scroll-world-and-fork]] · [[scroll-world-animation-skill/original-gpt-5-6-and-fable-5]] · [[ai-web-design-workflow/original-seedance-2-0]] (prior Seedance confirmation, same model family)
