# Original Deep-Dive: Eric's /fix-ticket + the marketing skills + Telegram/Sentry/Jira/Vercel

## Source

- **Eric's skills (public):** [github.com/EricTechPro/startup-claude-skills](https://github.com/EricTechPro/startup-claude-skills) — 51★, MIT (skills: `fix-ticket`, `develop-team`, `review-team`, `review-fix`, `playwright-qa-cli`).
- **Marketing skills:** [github.com/ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) — **Eric Osiu** (Single Grain), 2,738★, MIT.
- **Telegram:** `anthropics/claude-plugins-official` (31.3K★, Apache-2.0) → `external_plugins/telegram/`.
- BookZero.ai (real product, ~1.2K users). Verified via `gh api` + web (2026-06-29).

---

## Skill #8 — /fix-ticket (Eric's own, PUBLIC)

The capstone "workflow skill": **bug → done**, fully automated.

1. **Read** the Jira ticket (often auto-created from a **Sentry** log); understand the problem.
2. **Reproduce** via **Playwright CLI** (locally/prod).
3. **Research** with subagents → root-cause.
4. **Plan** → ask for **approval** (HITL gate).
5. **Fix** via TDD + multiple agents following best practices; review.
6. **Verify** via Playwright CLI again.
7. **Ship:** commit, push, merge worktree, **deploy to Vercel**, update the Jira ticket + summarize; hand off to a human QA engineer.
   It reports phase count, agents spawned, and a **token estimate** per run.

- **Public/gated (corrected):** the skill is **public MIT** in `startup-claude-skills` — not behind the Skool paywall. (Only the broader community/templates are paid: Skool $19→$99/mo.)
- **⚠️ Hype:** "replaces ~90% of junior software engineer jobs". **PARTIAL/hyperbole** — the real, documented signal is managers *freezing junior hiring* (~62% in one 2024 survey) and junior postings down ~30% since 2022; the honest read is "automates a large slice of *routine bug-fix toil*", not "90% of the role".

## Skill #7 — "43 Marketing Skills" (MISATTRIBUTED)

- The pack Eric demos is **Eric Osiu's** `ericosiu/ai-marketing-skills` (Single Grain) — **not Eric Tech's**. He *cites/uses* it.
- Real shape: ~15 primary categories (Growth, Sales Pipeline, Content Ops, SEO, Finance Ops, Revenue Intelligence, Conversion Ops, …) + utilities; "43" is a loose sub-skill count.
- **⚠️ "Took BookZero 0→1000 users" — UNVERIFIABLE:** BookZero is real (~1,247 users, plausibly hit 1K ~March 2026), but attributing growth to *these skills* specifically is a single-channel claim with no evidence. Some categories overlap [[claude-skills/_index]] (humanizer, SEO).

## The integrations (all official — these are the reusable parts)

- **Telegram + Claude Code:** the official **Anthropic Telegram plugin** (`anthropics/claude-plugins-official`) — single-user DM pairing via security code, message forwarding, reactions, attachments. Eric adds a `claude.sh` **reset hook** (a `/reset` slash command ends the session and starts a fresh one for a clean context window). This is the operator's already-piloted [[telegram-remote-control-stack/_index]] Recipe A.
- **Sentry** → official Sentry MCP (free). **Jira** → official Atlassian MCP. **Vercel** → official Vercel MCP/plugin. **GA4** for marketing analytics.

## Operator relevance (hireui Goal #2)

- **/fix-ticket is the single most hireui-shaped skill in the video** — a recruitment SaaS will have a Sentry→Jira→fix→deploy loop. Adopt the *architecture* (reproduce→research→approve→fix→verify→ship→handoff) using **official MCPs** (Sentry/Jira/Vercel) under hireui's **BMAD + I-2 agent-branch + I-8** governance — don't copy Eric's repo wholesale.
- The HITL **approval gate** + token-budget reporting align with the operator's cost-discipline + [[autonomous-loops-human-in-the-loop/_index]] thin-slice HITL.
- Telegram reset-hook = a clean recipe for the operator's existing remote-control stack.

## Install safety

`startup-claude-skills` + `ai-marketing-skills`: MIT, public, no postinstall (Markdown/Python skill files) — but **audit before adopting** (they're individual-author repos; treat as templates, run code-review, and install per hireui I-8). All the *integrations* are official first-party MCPs/plugins — safe.

## Key Takeaways

- /fix-ticket is **public** (not gated) and is the most directly hireui-relevant pattern — adopt the architecture via official MCPs.
- The marketing skills are **Eric Osiu's**, not Eric Tech's; growth attribution is unverifiable; low operator priority.
- The integration layer (Telegram/Sentry/Jira/Vercel) is all official first-party — the safe, reusable substrate.

## Related

[[claude-code-skills-stack/original-playwright-cli-vs-mcp]] · [[telegram-remote-control-stack/_index]] · [[autonomous-loops-human-in-the-loop/_index]] · [[claude-code-observability/_index]] · [[multi-agent-orchestration/_index]]
