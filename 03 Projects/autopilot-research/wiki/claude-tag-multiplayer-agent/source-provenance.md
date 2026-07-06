# Source Provenance — claude-tag-multiplayer-agent

## Source chain (operator-submitted → first-party original)

1. **Operator-submitted entry point:** [`6kU_TpceoJ4`](https://www.youtube.com/watch?v=6kU_TpceoJ4) — **BizMate AI Official** (VN, ~7,390 subs, `@BizMateAI`), "(New Update) Anthropic ra mắt Claude Tag: Giải pháp AI đa người dùng cho doanh nghiệp", published 2026-07-05, 11:26, ~292 views at ingest (2026-07-06).
   - **Full Vietnamese dub** (lồng tiếng + Vietsub) of the Anthropic original — same 11:26 runtime, no added analysis, no edits found in a full VN-vs-EN transcript comparison.
   - Description credits the original explicitly and funnels to BizMate's Skool community (`bizmate-ai-community-9131`) + `anthropic.skilljar.com` cert program.
   - Same channel previously supplied the operator's entry into [[external|Storm Bear: elicit-verifiable-agent-dsl]] (BizMate dub of a Code with Claude London talk) — this is now a **recurring VN-localization funnel channel** for Anthropic first-party content.
2. **First-party original (the actual subject):** [`MhfnicQVkgY`](https://www.youtube.com/watch?v=MhfnicQVkgY) — official **Claude** channel, **"The future of work with @Claude"**, published 2026-07-02, 11:26, ~87,069 views at ingest.
   - Speakers (per official description; identity-verified in dive): **Boris Cherny — Head of Claude Code** and **Cat Wu — Head of Product, Claude Code**. No third interviewer identified in any official source; the off-camera-style questions ("Walk me back…", "What's next for Claude Tag?") appear to be the two interviewing each other.
   - Official EN captions pulled via yt-dlp and **read in full in the main loop** (raw file: [`raw/2026-07-06-claude-tag-future-of-work.md`](../../raw/2026-07-06-claude-tag-future-of-work.md)).
3. **First-party product surfaces (double-dive):** [claude.com/tag](https://claude.com/tag) · [claude.com/docs/claude-tag/overview](https://claude.com/docs/claude-tag/overview) (+ security-and-data, setup-overview, migrate-from-earlier sub-pages) · [anthropic.com/news/introducing-claude-tag](https://www.anthropic.com/news/introducing-claude-tag) · support.claude.com articles 15594475 / 15575654 / 11506255 · [Slack Marketplace listing A08SF47R6P4](https://slack.com/marketplace/A08SF47R6P4-claude) · claude.com/blog/agent-identity-access-model.

## Name note ("Claude Tag" vs "@Claude")

- The **product name is "Claude Tag"**; the YouTube title uses the interaction form "@Claude". The mechanic: you tag `@Claude` in a Slack channel (or it jumps in proactively once added).
- The VN dub's audio renders the name variously as *Clawd Tag / Quad Tag / QuadTag / Cotag / CodTag / ClawTag / Quattro* — caption-garble of one name, not different products. Initial operator-side hypothesis that "Claude Tag" was a dub artifact was **wrong in the opposite direction**: the dub name was accurate; the doubt was resolved by the official description + product page.

## Ingest method

- yt-dlp caption pulls for both videos (VN dub subs + EN official captions), both read in full in the main loop — no NotebookLM.
- Double-dive + verification: Workflow `wf_36db963e-d86` (dive agents on announcement / docs / security-admin / press / METR / speakers / 65%-claim / Slack-Salesforce / competitive / reaction + corpus positioning, then REFUTE-first verification + completeness critic). Run was **split by an account session-limit outage** mid-run (10 dives completed pre-outage; docs+corpus dives, 18 verifiers and critic resumed post-reset via workflow resume) — see [[caveats-and-corrections]] for anything the outage degraded.

## Dub-provenance caveats

- BizMate is a **third-party re-publisher**: no evidence of Anthropic authorization for the re-dub; monetization = community funnel. Treat BizMate framing ("Giải pháp AI đa người dùng cho doanh nghiệp") as marketing gloss; all wiki facts here are sourced from the EN original + first-party pages, not the dub.
- The dub's description accurately restates the video's claims (16h autonomy, 65% PR share, memory, Teams roadmap) — no fabrication found, one framing addition ("65% các Pull Request… được viết bởi Claude Tag" matches Cat Wu's spoken claim, not the description's "code" wording — see [[the-65-percent-claim]]).
