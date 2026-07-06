# The Slack/Salesforce Side

## The app itself

- Slack Marketplace listing: [App ID A08SF47R6P4](https://slack.com/marketplace/A08SF47R6P4-claude) — the **same "Claude" app identity** as the legacy integration, upgraded to Tag.
- OAuth scopes (synthesized from the listing + search results — **no single canonical first-party scope doc was found**): `chat:write`, `channels:history`, `groups:history`, `search:read.{public,private,mpim,im,files}`, `canvases:read/write`, `users:read`, `users:read.email`, `reactions:write`. The search scopes ride Slack's new **Real-Time Search API** ("respecting existing permissions" — [Slack blog](https://slack.com/blog/news/powering-agentic-collaboration)).
- Marketplace listing states Slack conversations are **not used for model training by default**; security posture: HackerOne program, SAML/SSO, token rotation.
- No public review counts / install counts on the Marketplace — adoption is unobservable from outside.

## The partnership economics

- Salesforce owns Slack; announced expectation of **~$300M spend on Anthropic tokens in 2026** ([Technology Magazine](https://technologymagazine.com/news/salesforce-plans-to-spend-us-300m-on-anthropic-ai-tokens)) and holds **~1% equity in Anthropic** (~$1B at current valuation, per [Crypto Briefing](https://cryptobriefing.com/salesforce-open-ai-ecosystem-slack-anthropic/)).
- Rob Seaman (Slack EVP/GM), on the launch: "Slack is the only layer in the AI stack where teams work together" ([Salesforce Ben](https://www.salesforceben.com/anthropic-and-salesforce-announce-new-claude-to-slack-integration/)).
- Internal awkwardness reported: Salesforce employees questioned promoting a product that overlaps **Agentforce** and **Slackbot** ([The Next Web](https://thenextweb.com/news/salesforce-employees-anthropic-claude-tag-slack-tension)); Salesforce's public reconciliation frames three layers — Agentforce (orchestration) / Slackbot (conversational) / Claude Tag (task delegation) ([Salesforce Ben analysis](https://www.salesforceben.com/claude-tag-raises-a-bigger-question-what-is-agentforce-for/)).

## The legacy retirement

- **2026-08-03**: legacy "Claude in Slack" auto-switches to Claude Tag. Stated by **Anthropic surfaces only** (support.claude.com 15594475 + the announcement); Slack's own newsroom is silent — an Anthropic-driven sunset.
- Migration mechanics (per [migrate-from-earlier docs](https://claude.com/docs/claude-tag/admins/migrate-from-earlier)): admins get a ~30-day opt-in window; channels pinnable to Legacy/New/Inherit; after 08-03 **Legacy-pinned channels stop responding**; **no data migrates** (GitHub connections from individual accounts don't carry over; admins reconfigure connections; allowed-users/verified-domain settings do carry).

## Reading

- The launch is a **two-sided bet**: Anthropic gets the enterprise collaboration surface it doesn't own; Salesforce gets marquee proof that Slack is "where agents work" (and a token-revenue stream) at the cost of muddying Agentforce. The tenancy risk cuts the other way too — Slack built Real-Time Search API *for* this class of agent, and OpenAI got write-access the day before (see [[competitive-landscape]]).
- For buyers, the forced 08-03 migration with no rollback is the sharpest operational date in the whole launch — see [[admin-rollout-and-migration]].

Cross-links: [[overview]] · [[admin-rollout-and-migration]] · [[competitive-landscape]]
