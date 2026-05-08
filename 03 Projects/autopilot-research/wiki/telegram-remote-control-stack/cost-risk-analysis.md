# Cost & Risk Analysis — Recipe A

> **Compiled:** 2026-05-08 during pilot deployment
> **Operator context:** Claude Max subscription, Mac at home, single user
> **Purpose:** baseline numbers for future cost comparison across recipes (A/B/C) + risk inventory before going daily-use

## Direct cost — ~$1-3/month incremental

| Item | Cost | Notes |
|---|---|---|
| Anthropic Max subscription | **$0 incremental** | Already paid. Bot adds zero $/month |
| Telegram | $0 | Bot API is free for personal use, no rate caps that matter |
| Bun/Node/npm | $0 | Open source |
| Plugin v0.0.6 | $0 | MIT license inside `anthropics/claude-plugins-official` |
| Bot token | $0 | BotFather grants for free |
| **Hardware electricity** | ~$5-15/year | Mac M-series ~5-10W idle × 24/7. **Doubles to 2-3× if `caffeinate -i` keeps CPU non-sleep** |

**Total marginal $: ~$1-3/month** (mostly electricity from preventing system sleep).

## Real cost risk — rate-limit + time, not money

On Claude Max the cost vector is **daily message budget**, not $/token. Burn-through patterns:

### Risk #1 — Rate limit burn from phone use (HIGH)

| Pattern | Daily quota usage | Outcome |
|---|---|---|
| 5-10 simple DMs (`pwd`, `ls`, `git status`) | ~5-10% | Safe |
| 30-50 DMs incl. code review/refactor | ~30-50% | May hit cap during other work sessions |
| CI/CD reactive auto-fix | 50-200% | **Will throttle, blocks main productivity** |

**Mitigation:** console.anthropic.com → Usage → daily alert at 70%/85%.

### Risk #2 — Runaway loop (HIGH, non-obvious)

Dangerous pattern from bundle Drain 1 (Developers Digest):
- DM "fix all linter errors"
- Claude fixes error A
- New error B appears (caused by fix A)
- Stop hook triggers another fix
- ∞ loop

**Recognition signals:**
- Mac heat + fan noise
- Anthropic dashboard alert
- Telegram notification spam from bot

**Mitigation:**
- Set hard turn limit per conversation (max 20 turns)
- Stop hooks with explicit escape conditions
- DON'T auto-approve dangerous tools (`rm -rf`, `git push --force`)
- Disable Edit/Write for bot scope if read-only is enough

### Risk #3 — Adversarial prompt injection (MEDIUM)

If allowlist breaches (rare) OR you accidentally share access:
- Crafted prompts cause expensive tool calls
- Could exfiltrate data if Read tool enabled
- Quota burn

**Mitigation:**
- Allowlist already enabled (Recipe A step 7) ✅
- Don't share bot username publicly
- Don't add other users to allowlist unless trusted
- Token rotation monthly if paranoid (BotFather → Revoke API Token)

### Risk #4 — Hidden context cost (LOW-MEDIUM)

The Telegram MCP server registers tools (`reply`, `react`, `edit_message`) into Claude's context **every turn**. ~500-1000 tokens/turn just for plugin presence.

| Math | Numbers |
|---|---|
| Plugin overhead per turn | 500-1000 tokens |
| 50 messages/day | 25K-50K tokens/day overhead |
| Share of Claude Max daily quota | ~1-3% |

Bundle Drain 3 flagged this as the "MCP token cost warning" — not huge, but not zero.

### Risk #5 — Time cost (CERTAIN)

Most-realistic risk for newcomer to this stack:

| Event | Frequency estimate | Time cost |
|---|---|---|
| Plugin breaks on Claude Code update | 1-2x/month (still experimental) | 15-60 min debug |
| Mac sleeps → bot silent | 1-3x/week without persistence | 5-10 min recovery |
| Token expired / rotated | 1-2x/year | 5 min |
| Forgot to allowlist after pair | 1-2x lifetime | Risk-based |
| Restart machine → bot dies | 1-2x/week without launchd | 2-5 min |

**Est. total: ~2-4 hours/month** without persistence automation. Drops to ~30 min/month after launchd setup.

## Bottom line

| Question | Answer |
|---|---|
| Costs more $/month? | ~$1-3 (electricity only) |
| Risk hitting Anthropic cap? | **YES**, especially for code-review/auto-fix patterns. Productivity loss > $$ loss |
| Security cost risk? | LOW with allowlist + token security; MEDIUM if auto-approve dangerous tools enabled |
| Worst-case scenario? | Runaway loop eats 100% Max daily quota → no Claude on main laptop until next day. **No additional charges.** |
| When to upgrade to Recipe B (VPS)? | When Recipe A's "Mac must stay awake" causes >3 missed critical events/month. **Not a cost decision — friction decision.** |

## Recommended safeguards (priority order)

1. **Anthropic usage alerts** (5 min, free) — console.anthropic.com → Usage → alerts at 70%/85% daily quota
2. **Audit log hook** (already implemented in this project, see [[../../bin/audit-log-hook.py]] — fires PostToolUse, logs to `~/.claude/channels/telegram/audit.log`)
3. **Tool restrictions** in `.claude/settings.local.json` — explicit allow-list of tools the bot can call
4. **Turn cap per conversation** — TBD on syntax, but default ~20-30 turns prevents runaway
5. **Stop hooks with escape condition** — `[[../claude-code-hooks/_index|Claude Code hooks § Stop]]` covers this

## Cost comparison snapshot — Recipe A vs B (for future reference)

| Dimension | Recipe A (local Mac) | Recipe B (VPS, projected) |
|---|---|---|
| Monthly $ | ~$1-3 | ~$5-15 (VPS rental + electricity reduction) |
| Setup time | 10 min happy path / 45 min first time | A + ~30 min VPS hardening |
| Time cost/month (without persistence) | ~2-4h | ~30 min (VPS + systemd auto-restart) |
| Time cost/month (with persistence) | ~30 min | ~30 min |
| Daily quota burn | Same (subscription is per-account) | Same |
| Latency | ~1-3 sec | Same (Telegram polls outbound from VPS) |
| Hardware reliability | Mac sleep / lid close / power | VPS uptime ~99.95% |
| When does B become worth it? | Recipe A persistence keeps failing OR you need to react to events while Mac is off | — |

Update this table after running Recipe B to lock in real numbers.

## Cross-references

- [[setup-recipe-a]] — verified deployment ritual
- [[security-model]] — threat model details
- [[gaps-production]] — what's NOT covered (rate limiting, FinOps caps, IaC) for production-grade
- [[../claude-code-hooks/_index|Claude Code hooks]] — Stop hook pattern for runaway prevention
