# hermes-agent — the self-improving personal AI agent (Nous Research)

> **Topic created:** 2026-07-18 (autopilot `/loop`, operator anchor `y96gIckJJ2Q` Phan Dong Giang + 8-video bundle, operator-elected full bundle + verify)
> **Subject:** [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — MIT, Python, self-hosted "self-improving" personal AI agent. Org **Nous Research**.
> **Verification:** refute-first workflow `wf_06a79485-687` (44 agents; 8 gatherers → 22 claims with 3-skeptic panels on 6 hype claims → 2 critics; ~1.83M tokens, 0 errors). Grounded on GitHub API ×2 endpoints + official README + site + docs.

## One-line

**Hermes Agent is a single-user, always-on personal agent that remembers you and writes its own reusable skills** — reachable across 20+ chat channels (Telegram/Discord/Slack/…), provider-agnostic, with built-in memory (FTS5 + LLM summarization + Honcho), cron, isolated subagents, MCP, and 6 deployment backends. It is Nous Research's **OpenClaw successor** (ships `hermes claw migrate`).

## ⭐ Corpus-firsts

- **Largest single repo by stars in the entire 69-topic corpus — 216,731★** (verified 2× GitHub API), overtaking the prior record AutoGPT (184,043★, v59).
- **First dedicated *personal-agent-runtime* topic** — distinct from sibling agent-*framework* [[vercel-eve]] (t67) and agent-*multiplexer* [[herdr]] (t68).

## Claims scorecard (22 load-bearing claims)

**13 CONFIRMED · 4 MISLEADING · 4 FALSE · 1 UNVERIFIABLE · 0 fabricated**

The **capabilities are accurate; the framing is inflated.** Confirmed core: MIT, memory, channels, providers, subagents, cron, `hermes claw migrate`, MCP. Failed superlatives: "22K stars" (FALSE — it's 216K), "only agent with a learning loop" (FALSE), "launched Feb 2026" (FALSE — first release Mar-12-2026), "runs under Claude Code" (FALSE — it's MCP interop), "no-code/easier than OpenClaw" (MISLEADING), "224B tokens overtook OpenClaw" (UNVERIFIABLE). Biggest substantive caveat: the credible reviewer says "self-improving skills" is **memory-learning, not proven autonomous skill-quality evolution**. See [[claims-scorecard]] + [[caveats-and-corrections]].

## Articles

| Article | What's in it |
|---|---|
| [[overview]] | What Hermes is, the verified numbers, corpus positioning |
| [[learning-loop-and-self-improving-skills]] | The core differentiator + the skill-maturity contradiction (memory-learning vs autonomous improvement) |
| [[memory-system]] | FTS5 + `user.md`/`memory.md` token-capped summarization + Honcho (Plastic Labs) |
| [[channels-providers-deployment]] | 20+ channels, provider-agnostic, 6 backends, cron, subagents, install |
| [[hermes-vs-openclaw]] | The spine: replacement-vs-complementary debate, `hermes claw migrate`, security/skills contrasts |
| [[claude-code-interop]] | Correcting "runs under Claude Code" → real MCP interop both ways (Goal-relevant) |
| [[pricing-license-and-skill-hub]] | MIT + BYO-keys, freemium Nous Portal tiers, security-scanned Skill Hub |
| [[claims-scorecard]] | All 22 verdicts with evidence + corrections |
| [[caveats-and-corrections]] | Corrections, the maturity contradiction, unverified claims, deployment gaps |
| [[source-provenance]] | The 8 sources, stances, fetch + verification method |

## Operator relevance (hireui / Goal #2)

- **AVOID candidate-facing** — **data-residency + subagent-isolation are undocumented** (same hard blocker as [[vercel-eve]]); routing candidate PII through Honcho/Portal violates the candidate-LLM legibility ADR (EU AI Act Annex III).
- **BORROW now (patterns, MIT, no lock-in):** token-capped pruning memory (`user.md`/`memory.md`), security-scanned skill registry, model-by-task cost routing, and especially the **Hermes-as-MCP-server pattern** (an always-on memory/skills/channel layer *around* Claude Code — see [[claude-code-interop]]).
- **PILOT candidate (operator-side, non-candidate):** an always-on ops/automation agent (channel-monitoring, PRD-sync, health-checks) — orthogonal to the v189 loop; clean MIT license makes eval cheap.

## Cross-links
[[vercel-eve]] · [[herdr]] · [[agent-memory-architecture]] · [[harness-engineering]] · [[multi-agent-orchestration]] · [[claude-code-memory-systems]] · [[claude-code-clones]] · [[claude-api-cost-optimization]] · [[local-ai-coding-agents]]
