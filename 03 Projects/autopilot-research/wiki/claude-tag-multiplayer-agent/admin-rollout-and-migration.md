# Admin Rollout & the 2026-08-03 Migration

## Setup surface

- Provisioned org-wide by a Slack **Primary Owner/Owner** (Admin role cannot) at `claude.ai/admin-settings/claude-tag`; requires Claude **Enterprise or Team (≥10 seats)** ([setup docs](https://claude.com/docs/claude-tag/admins/setup-overview), support 15594475).
- **Permission hierarchy:** org-wide credentials → workspace-level access for public channels → private-channel-specific credentials layered on top.
- **Connectors must use service accounts** (not personal credentials); write-only credential entry screens; credentials travel only to named hosts (Agent Proxy — see [[architecture-and-execution-model]]).
- Member access restrictable via admin toggles (Claude-account-holders-only on Team; role-based on Enterprise); **defaults to workspace-wide availability** — a default worth noticing before rollout.
- Ambient (proactive) mode **can be disabled per channel** for high-sensitivity spaces.

## Spend controls

- Org-level **hard cap** + per-channel limits (inheritance defaults) + alerts at 75%/95%.
- Enforcement is **decline-work** at the cap (not silent degradation).
- **Launch credits:** $25,000 Enterprise / $2,500 Team, auto-applied, **expire 2026-09-01** (support 15575654) — i.e., the first ~10 weeks of usage data most orgs collect will be credit-subsidized; budget the GA number from September data, not July's.
- Channel work bills the org; **DMs bill the individual's personal account**.

## The migration cliff (legacy Claude in Slack → Tag)

Per [migrate-from-earlier docs](https://claude.com/docs/claude-tag/admins/migrate-from-earlier) + support 11506255:

- **2026-08-03: automatic switchover**, ~30-day opt-in window beforehand. Non-responding admins inherit the default configuration.
- Channels pinnable **Legacy / New / Inherit** during the window; after 08-03 **Legacy-pinned channels simply stop responding** — no rollback path.
- **No data migrates.** GitHub repos/connections made from individual accounts do **not** carry over; all connections must be reconfigured by admins under the service-account model. Allowed-users / verified-domain settings do carry forward.
- Retirement is stated on Anthropic surfaces only (Slack newsroom silent) — an Anthropic-driven sunset.

## Suggested rollout shape (synthesized from BERI's IT-guide framing + docs)

1. **Week 0:** inventory legacy Claude-in-Slack usage (channels, connectors, owners) — anything not reconfigured dies 08-03.
2. **Week 1:** sandbox workspace or 1-2 low-sensitivity public channels; ambient OFF; tight per-channel spend caps; service accounts with minimum scopes.
3. **Week 2-3:** widen to the 3 archetype channels the launch video showcases (feedback→PR, data-questions, docs-Q&A); ambient ON where members consent; measure spend against credits.
4. **Before 09-01:** compute the real GA run-rate from metered weeks; decide before credits mask costs disappear.

## Key Takeaways

- The two dates that matter: **08-03** (forced migration, connections must be rebuilt) and **09-01** (credits expire, true cost visibility).
- Defaults are adoption-biased (workspace-wide availability, ambient on, inheritance spend limits) — a governance-first rollout must flip several defaults on day one.
- The service-account requirement is the hidden migration cost: every legacy personal-credential connection needs an owner, a scope review, and a rebuild.

Cross-links: [[overview]] · [[slack-salesforce-context]] · [[security-and-governance]] · [[reception-and-risks]]
