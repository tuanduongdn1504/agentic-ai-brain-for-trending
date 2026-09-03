# hermes-agent — the self-improving personal AI agent (Nous Research)

> **Topic created:** 2026-07-18 (autopilot `/loop`, operator anchor `y96gIckJJ2Q` Phan Dong Giang + 8-video bundle, operator-elected full bundle + verify)
> **🔄 REVISITED 2026-09-03** (autopilot `/loop`, operator anchor `k8lz9P3MrlM` holetex + operator-elected **full 6-source re-drain**; 0 of 6 videos overlap the prior bundle). **Every figure below the "Topic created" line was re-verified; the ones that moved are corrected in place.** New: [[revisit-2026-09-03]] · [[the-vendor-seeded-false-claim]] · [[hermes-desktop]].
> **Subject:** [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — MIT, Python, self-hosted "self-improving" personal AI agent. Org **Nous Research**.
> **Verification:** refute-first workflow `wf_06a79485-687` (44 agents; 8 gatherers → 22 claims with 3-skeptic panels on 6 hype claims → 2 critics; ~1.83M tokens, 0 errors). Grounded on GitHub API ×2 endpoints + official README + site + docs.

## One-line

**Hermes Agent is a single-user, always-on personal agent that remembers you and writes its own reusable skills** — reachable across 20+ chat channels (Telegram/Discord/Slack/…), provider-agnostic, with built-in memory (FTS5 + LLM summarization + Honcho), cron, isolated subagents, MCP, and 6 deployment backends. It is Nous Research's **OpenClaw successor** (ships `hermes claw migrate`).

## ⭐ Corpus-firsts

- **Largest single repo by stars in the entire corpus — 240,313★** on 2026-09-03 (verified 2× GitHub API; was 216,731★ on 2026-07-18), against the prior record AutoGPT (184,043★, v59) — lead widened ~17% → **~31%**.
- **CORPUS-FIRST: a FALSE claim traced to live vendor copy rather than to a creator.** The exclusivity claim this corpus graded FALSE on 2026-07-18 is still in the README's first paragraph 47 days later; the 2026-08-26 anchor reads it off the screen and attributes it correctly. **Origin predicts recurrence** — [[the-vendor-seeded-false-claim]].
- **First dedicated *personal-agent-runtime* topic** — distinct from sibling agent-*framework* [[vercel-eve]] (t67) and agent-*multiplexer* [[herdr]] (t68).

## Claims scorecards — two drains

| Drain | Claims | Verdicts |
|---|---|---|
| 2026-07-18 (8 sources) | 22 | **13 CONFIRMED · 4 MISLEADING · 4 FALSE · 1 UNVERIFIABLE · 0 fabricated** |
| **2026-09-03 (6 sources)** | **78** | **34 CONFIRMED · 15 MISLEADING · 14 UNVERIFIED · 9 FALSE · 6 CORRECTED · 0 fabricated** |

**The 2026-09-03 drain confirms the 2026-07-18 thesis and inverts one of its lessons.** Confirmed: *accurate capabilities, inflated framing* — it holds at 4× the claim count. Inverted: the operator's own **anchor was the most accurate source in the bundle (11% error rate vs 50% for the largest-reach source)**, and the two sources an early sampling defect had excluded turned out to be the least accurate. Full tables: [[revisit-2026-09-03]].

### 2026-07-18 detail (22 load-bearing claims)

**13 CONFIRMED · 4 MISLEADING · 4 FALSE · 1 UNVERIFIABLE · 0 fabricated**

The **capabilities are accurate; the framing is inflated.** Confirmed core: MIT, memory, channels, providers, subagents, cron, `hermes claw migrate`, MCP. Failed superlatives: "22K stars" (FALSE — it's 216K), "only agent with a learning loop" (FALSE), "launched Feb 2026" (FALSE — first release Mar-12-2026), "runs under Claude Code" (FALSE — it's MCP interop), "no-code/easier than OpenClaw" (MISLEADING), "224B tokens overtook OpenClaw" (UNVERIFIABLE). Biggest substantive caveat: the credible reviewer says "self-improving skills" is **memory-learning, not proven autonomous skill-quality evolution**. See [[claims-scorecard]] + [[caveats-and-corrections]].

## Articles

| Article | What's in it |
|---|---|
| 🔄 [[revisit-2026-09-03]] | **The 2026-09-03 re-drain: the 6×4 replication matrix, the full 78-claim scorecard, per-source accuracy, v0.18→v0.21 drift, and 10 recorded verification failures** |
| ⭐ [[the-vendor-seeded-false-claim]] | Why F4 keeps coming back — the falsehood is the vendor's, not the creators', and origin predicts recurrence |
| 🆕 [[hermes-desktop]] | Hermes Desktop + Bot Mode — first-party, in-tree, and absent from the prior build; HermesOS does not exist |
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
- 🔴 **NEW 2026-09-03 — the Ollama Cloud trap sharpens that blocker.** Two sources present Ollama as the route to *local, private* inference. The documented integration is **"Ollama Cloud" — a cloud service on an API key, default endpoint `https://ollama.com/v1`**; pointing it at a local Ollama is an *undocumented* config override. The most-recommended "keep it private" path in the bundle ships data to a third party by default. Verify the endpoint by inspection, never by tutorial ([[revisit-2026-09-03]]).
- **BORROW now (patterns, MIT, no lock-in):** token-capped pruning memory (`user.md`/`memory.md`), security-scanned skill registry, model-by-task cost routing, and especially the **Hermes-as-MCP-server pattern** (an always-on memory/skills/channel layer *around* Claude Code — see [[claude-code-interop]]).
- **PILOT candidate (operator-side, non-candidate):** an always-on ops/automation agent (channel-monitoring, PRD-sync, health-checks) — orthogonal to the v189 loop; clean MIT license makes eval cheap.

## Cross-links
[[vercel-eve]] · [[herdr]] · [[agent-memory-architecture]] · [[harness-engineering]] · [[multi-agent-orchestration]] · [[claude-code-memory-systems]] · [[claude-code-clones]] · [[claude-api-cost-optimization]] · [[local-ai-coding-agents]]
