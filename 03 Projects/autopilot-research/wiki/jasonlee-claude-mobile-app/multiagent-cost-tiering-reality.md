# Multi-Agent Cost-Tiering — Documented Mechanism vs Chat-Prompt Theater

## Verdict on the video's claim
"Use a multi-agent workflow — Sonnet 5 for grunt work, Opus 4.8 for review — to maximize token efficiency" → **MISLEADING** (high confidence): the *capability* is real and documented; the *demonstration* (a natural-language prompt in a Desktop Code chat) does not establish that models were actually pinned per subagent.

## What IS documented (Claude Code subagents)
Per code.claude.com/docs/en/sub-agents, per-subagent model assignment exists with this resolution order:
1. `CLAUDE_CODE_SUBAGENT_MODEL` env var
2. per-invocation `model` parameter on the Agent tool call
3. the subagent definition's `model:` frontmatter field
4. fallback: **the main conversation's model** (inherit)

Claude Code markets "10s to 100s of parallel subagents" (claude.com/product/claude-code); the Desktop app exposes Code sessions, connectors, and a preview Browser pane.

## Why the on-screen demo is theater
- Jason types a *request* ("use smaller cheaper models like Sonnet 5 for grunt work..."); no agent files, no frontmatter, no CLI flags, no Agent-tool model params are shown. With none of steps 1–3 configured, subagents **inherit the parent model** (step 4).
- The "agent workflow table" with a per-agent model column and a "why" column is model-generated *prose* — a plan, not a binding configuration. Claude may honor it by passing `model` per Agent call, but nothing on screen verifies that.
- **Verified real bugs** (both independently ground-checked via GitHub API on 2026-07-11):
  - **anthropics/claude-code#44385** (filed 2026-04-06, now **closed**; resolution not verified): "agent definition frontmatter `model:` field is ignored — subagents always inherit parent model."
  - **anthropics/claude-code#47488** (filed 2026-04-13, still **open**): "Cowork: Agent tool `model` parameter silently ignored — all sub-agents routed to Haiku."
  - Net: even users who configure tiering correctly have had it silently not apply. "Trust but verify" — check per-request model usage, don't assume.
- The token-efficiency claim is asserted, never measured (no cost readout appears in the video).

## What Anthropic actually recommends
- First-party cost-tiering guidance ("Building Effective Agents"): **route by task complexity** — simple/common → Haiku-class, hard/unusual → Sonnet/Opus-class. The orchestrator-workers and evaluator-optimizer patterns are documented, but "Opus reviews, Sonnet executes" as a specific pairing is the video's (reasonable) synthesis, not a quoted recommendation.
- "Success isn't about building the most sophisticated system. It's about building the right system for your needs."

## The model lineup the video references (ground truth, 2026-07-11)
| Model | Released | API price (in/out per MTok) | Note |
|---|---|---|---|
| Fable 5 | GA 2026-07-01 (global) | $10 / $50 | Included in paid plans (≤50% weekly limit) **through 2026-07-12** (extended from 07-07 after backlash); usage credits from 07-13. Video's claim ✓ |
| Opus 4.8 | 2026-05-28 | $5 / $25 | Upgrade from Opus 4.7 (Opus line) |
| Sonnet 5 | 2026-06-30 | $3 / $15 (intro $2/$10 through 2026-08-31) | Direct upgrade from Sonnet 4.6 — Anthropic: "strict improvement" |
| Sonnet 4.6 | 2026-02-17 | $3 / $15 | Real model — the video's reference checks out |
| Haiku 4.5 | 2025 | $1 / $5 | The cheap tier the video never mentions |

"Opus 4.8 and Sonnet 5 are a big upgrade from Sonnet 4.6" → **OVERSIMPLIFIED** (main-loop grade; the verifier graded MISLEADING for the crossed product lines — Opus 4.8 upgrades Opus 4.7, not Sonnet 4.6; Sonnet 5 genuinely is the Sonnet 4.6 successor).

## How to do the video's intent properly
1. Define subagents as files with `model:` frontmatter (e.g. reviewer=opus, builder=sonnet, mechanical tasks=haiku) — and verify the routing actually applied (bug history above).
2. Or invoke the Agent tool with an explicit per-call `model` parameter.
3. Measure: `/cost`-class local telemetry or OTEL ([[external|Storm Bear: claude-code-observability]]) before believing any "token efficient" claim.
4. Haiku 4.5 at $1/$5 is the real grunt-work tier — the video's "cheap model" (Sonnet 5) is 2–3× its price.

## Key Takeaways
- Per-subagent model tiering: **real capability, buggy history, undemonstrated in this video**.
- Asking nicely in chat is not configuration. Configuration is files, params, or env vars — and verification is telemetry.
- The video's model *choices* (skip Fable 5, Opus-plans/Sonnet-builds) are economically sensible even where the mechanism is hand-waved.

## Sources
- https://code.claude.com/docs/en/sub-agents · https://github.com/anthropics/claude-code/issues/44385 · https://github.com/anthropics/claude-code/issues/47488 · https://www.anthropic.com/research/building-effective-agents · https://www.anthropic.com/news/claude-sonnet-5 · https://www.anthropic.com/news/claude-sonnet-4-6 · https://www.anthropic.com/news/claude-opus-4-8 · https://anthropic.com/news/redeploying-fable-5 · claude-api skill model table (cached 2026-06-24)
