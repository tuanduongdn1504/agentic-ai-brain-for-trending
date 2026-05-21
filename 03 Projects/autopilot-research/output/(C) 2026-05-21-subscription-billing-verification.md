# Subscription-billing verification — Hermes orchestrator pattern (Nemanja video 2026-05-20)

> **Question:** Is the video's central claim true — that routing Claude through a Hermes Profile burns "extra balance" while shelling out to Claude Code CLI as a subprocess preserves the subscription?
> **Trigger:** [wiki/harness-engineering/personal-repo-hermes-orchestrator.md](../wiki/harness-engineering/personal-repo-hermes-orchestrator.md) gap item #1
> **Method:** WebSearch (3 queries) + WebFetch (6 authoritative sources) on 2026-05-21
> **Verdict:** **DIRECTIONALLY CORRECT, BUT THE CLI-SUBPROCESS PATH HAS A KNOWN FOOTGUN THAT CAN SILENTLY FLIP TO API BILLING.** The video's framing is binary; reality is conditional. The architectural cost advantage is real ONLY when 3 environmental conditions hold simultaneously.

---

## Verified claim 1 — Hermes Profile DOES route to a separate billing pool

**Confirmed by 3 independent sources.**

### Source A — Anthropic Help Center (first-party)

> "If you have an ANTHROPIC_API_KEY environment variable set on your system, Claude Code will use this API key for authentication instead of your Claude subscription (Pro, Max, Team, or Enterprise plans), resulting in API usage charges rather than using your subscription's included usage."

Source: [support.claude.com/en/articles/11145838](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)

### Source B — Hermes-agent GitHub issue #12905

> "Anthropic appears to route third-party OAuth client requests to a separate `extra_usage` billing pool, which is effectively empty for most users."

The reporter is a Max subscriber whose subscription quota showed only 20% consumed, yet received "out of extra usage" errors when invoking Claude through Hermes' Anthropic OAuth provider.

Source: [github.com/NousResearch/hermes-agent/issues/12905](https://github.com/NousResearch/hermes-agent/issues/12905)

### Source C — MindStudio analysis of the Hermes.md billing bug

Anthropic's reportedly stated reasoning per the analysis:

> "subscriptions weren't built for the usage patterns of these third-party tools."

Source: [mindstudio.ai blog](https://www.mindstudio.ai/blog/hermes-md-bug-claude-max-billing-subscription-pricing)

**Conclusion:** Nemanja's claim that Hermes Profile billing **does not consume subscription quota** is correct. Whichever path Anthropic uses for 3rd-party OAuth clients — either `ANTHROPIC_API_KEY` (= standard API billing) or a separate `extra_usage` pool — neither path consumes the Pro/Max subscription quota.

---

## Verified-with-caveats claim 2 — CLI subprocess CAN use subscription, BUT only under 3 conditions

**The video presents this as automatic. It is not.**

### Source D — Hermes' own bundled Claude Code skill (SKILL.md)

The Hermes skill the video relies on documents two invocation modes:

```
# Print mode (non-interactive, used by orchestrator)
claude -p 'task description' --allowedTools 'Read,Edit' --max-turns 10

# Bare mode (for CI/scripting — explicitly REQUIRES API key)
claude --bare  # "skips hooks, plugins, MCP discovery, and CLAUDE.md loading... Requires ANTHROPIC_API_KEY"
```

The skill itself states: *"run `claude` once to log in (browser OAuth for Pro/Max, or set `ANTHROPIC_API_KEY`)"*.

Source: [raw.githubusercontent.com/NousResearch/hermes-agent/main/skills/autonomous-ai-agents/claude-code/SKILL.md](https://raw.githubusercontent.com/NousResearch/hermes-agent/main/skills/autonomous-ai-agents/claude-code/SKILL.md)

### Source E — Real-world failure: $1,800 in 2 days

GitHub issue #37686 (titled *"claude -p suggested to Max subscriber — caused unintended API billing ($1,800+ in two days)"*):

> "`claude -p` bypasses OAuth and requires `ANTHROPIC_API_KEY` — meaning it **always bills to the API account**, never to a Max subscription."

The user was a $200/month Max subscriber. They set `ANTHROPIC_API_KEY` (for unrelated work) and used `claude -p` for scheduled tasks. The CLI silently preferred the API key over the OAuth login, billing $1,800 in 2 days. The issue's recommended correct alternative: *"Use Claude Desktop built-in scheduled tasks (runs under subscription) / Use `/loop` skill / **Never** set up `ANTHROPIC_API_KEY` + `claude -p`."*

Source: [github.com/anthropics/claude-code/issues/37686](https://github.com/anthropics/claude-code/issues/37686)

### Source F — Confirming evidence on subscription auth working when conditions hold

GitHub issue #20976 (a UI display bug where Max subscribers see "API Usage Billing" label even though they're actually on subscription):

```json
{"claudeAiOauth": {"subscriptionType": "max", "rateLimitTier": "default_claude_max_20x"}}
```

This confirms that **when `claude` is OAuth-logged-in and no API key is in the environment**, the CLI does correctly use subscription billing. The "API Usage Billing" label is just a UI bug.

Source: [github.com/anthropics/claude-code/issues/20976](https://github.com/anthropics/claude-code/issues/20976)

### The 3 conditions that must hold simultaneously

For the video's "CLI subprocess uses subscription" claim to actually deliver on a given task invocation, ALL THREE must be true:

1. **`ANTHROPIC_API_KEY` is NOT set** in the environment Hermes inherits when it shells out. If any prior tool, `.envrc`, shell profile, or systemd unit exported this variable — even with an unrelated key — Claude Code will silently prefer it and bill API.
2. **The skill does not invoke `claude --bare`**. Bare mode is explicitly documented as API-key-only. Hermes' skill exposes bare mode; the user's prompt determines whether it gets used.
3. **The `claude` CLI was previously OAuth-logged-in** with the same Pro/Max account that owns the relevant billing context.

If any one of the three fails, the orchestrator silently bills against API credits at standard rates — and the operator may not notice until the credit-card invoice arrives.

---

## Operational implications for any pilot

If you pilot the Hermes + Codex + Claude orchestrator pattern with subscription preservation as the goal:

| Mitigation | Action |
|---|---|
| **Audit env before each pilot run** | `env \| grep -i anthropic` — should be empty. If anything is set, `unset ANTHROPIC_API_KEY` in the Hermes-launching shell. |
| **Lock down Hermes profile prompts** | Inspect the `coder` and `reviewer` profile contents (Nemanja offered to share in comments — request them). Ensure neither invokes `--bare` mode unless API billing is intentional. |
| **Verify post-run** | Check Claude Console → API Usage dashboard the day after each pilot. If any API calls appear, an env-leak occurred. |
| **Set a `max-budget-usd` cap** | Hermes' skill supports `--max-budget-usd` (minimum ~$0.05) as a kill switch. Use a small cap during pilot to bound blast radius. |
| **Alternative if footgun risk is unacceptable** | Use Claude Desktop's built-in scheduled tasks OR vault-level `/loop` skill, both of which run under subscription. Tradeoff: lose Hermes' cross-vendor orchestration. |

---

## Bottom-line verdict for the wiki article

The video's central architectural claim — that orchestrator-mediated cross-vendor via CLI subprocess preserves subscription billing — is **technically achievable but operationally fragile**. The fragility was not mentioned in the video and is the difference between the pattern being a free-lunch cost optimization and a $1,800/2-day footgun.

Recommended wiki-article amendment: change "load-bearing innovation is subscription-arbitrage" to "**conditional** subscription-arbitrage" and link this report.

---

## Followup research surface (deferred)

1. **Direct test in a sandbox account.** Spin up a fresh Pro account with no extra credits, install Hermes + Codex + Claude CLIs, run one `/goal` cycle, check both Anthropic and OpenAI invoice the next day. N=1 empirical resolution.
2. **Verify Codex CLI subscription-billing behavior.** This report covers only Claude. ChatGPT Plus / Pro subscription billing semantics for Codex CLI invoked as subprocess are not yet researched. The video assumes parity; worth checking.
3. ~~**Audit Hermes' `coder.md` and `reviewer.md` profile contents.**~~ **RESOLVED 2026-05-21:** profiles are in companion repo [github.com/nemanjadotcom/goal-video-resources](https://github.com/nemanjadotcom/goal-video-resources) under filenames `SOUL-codexbuilder.md` and `SOUL-claudereviewer.md`. **Reviewer profile prescribes `claude -p` with `--allowedTools "Read,Bash"` and `--max-turns 10`** — confirms the API-billing dependency would be triggered if the pilot adopts the published profile. See `raw/2026-05-21-nemanja-goal-video-resources-repo.md`.
4. **Track Hermes-agent issue #12905** for Anthropic's response on whether 3rd-party-OAuth-via-extra-usage-pool is the documented intent or an unintended artifact.

## Post-audit corroboration (2026-05-21 YouTube comments evidence)

Comments on the source video O-PEeD7fymo independently corroborate the audit findings:

**Technical corroboration (commenter @kikserthg233, 1♥):**
> "claude -p will be billed same as if api is used. Maybe computer use can be a workaround?"

**Host's response (Nemanja, OP):**
> "I had extra usage turned off in my account during this test. Hermes initiates it just like you would."

**Interpretation:** Nemanja did NOT rebut the technical claim that `claude -p` bills against API. His defense is an operational hard-cap: he set Anthropic billing "extra usage" to $0 so the API path could not consume real money. **This is the actual safeguard the architecture relies on — not subscription preservation by construction.** A pilot must apply the same cap.

**Pattern-class evidence (commenter @aichess.online, 1♥):**
> "I'm kind of doing the same workflow, but instead of using Claude Code for reviewing I'm using Droid CLI"

Independent practitioner running the same orchestrator-mediated cross-vendor pattern with a different reviewer CLI — strengthens the case that this is a pattern-class with multiple independent instances, not a Hermes+Codex+Claude-specific trick.

## Recommended pilot guardrails (final)

1. **Set Anthropic billing extra-usage cap to $0** before any pilot run. This is the safety net Nemanja relies on.
2. **`unset ANTHROPIC_API_KEY`** in the shell that launches Hermes. Audit with `env | grep -i anthropic` → empty.
3. **Start with the demo's no-profile architecture** (per the PROMPT.md in the companion repo: "Do NOT use Hermes agent profiles for this test. Use Codex CLI directly... Use Claude Code CLI directly..."). The full SOUL-profile architecture is aspirational and triggers the `claude -p` API-billing path.
4. **Verify post-run:** check Anthropic Console → API Usage AND check that "extra usage" cap was not hit. Either signal indicates the architecture leaked to API billing.
5. **N=1 empirical test answers the architecture question.** With both safeguards active, run one `/goal` cycle. If the reviewer succeeds → OAuth fallback is working in the current Claude Code version. If reviewer fails → confirmed API-billing dependency; either accept the cost or use the no-profile demo path only.
