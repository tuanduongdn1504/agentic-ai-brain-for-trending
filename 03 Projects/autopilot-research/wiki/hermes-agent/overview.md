# Hermes Agent — Overview

## Source
8-video YouTube bundle (`raw/2026-07-18-hermes-agent/`) anchored on Phan Dong Giang's VN tutorial ([y96gIckJJ2Q](https://www.youtube.com/watch?v=y96gIckJJ2Q)), grounded on primary sources: GitHub API (`NousResearch/hermes-agent`, verified 2× endpoints 2026-07-18), official README, [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com) + `/docs/`. Verified via refute-first workflow `wf_06a79485-687` (44 agents).

## What it is
- **Hermes Agent** = Nous Research's open-source, **self-hosted, single-user "self-improving" personal AI agent** — a headless/desktop process you talk to across chat channels that remembers you and writes its own reusable skills over time.
- Tagline: **"The Agent That Grows With You"** / README: *"the self-improving AI agent built by Nous Research… the only agent with a built-in learning loop"* (the **"only"** is FALSE — see [[claims-scorecard]]).
- Repo `NousResearch/hermes-agent` — **MIT** license, **Python 3.11** (+ Node.js), created **2025-07-22**.

## The numbers (re-verified 2026-09-03 — see [[revisit-2026-09-03]])

| | 2026-07-18 | **2026-09-03** | Δ |
|---|---|---|---|
| stars | 216,731 | **240,313** | +23,582 (+10.9%) |
| forks | 40,656 | **49,189** | +8,533 |
| open issues | 23,647 | **38,680** | +15,033 (+63.6%) |
| latest release | v0.18.2 (`v2026.7.7.2`, 07-08) | **v0.21.0** (`v2026.8.31`, 08-31) | 10 releases |
| tags | 27 | **37** | +10 |

Both 2026-09-03 star figures agree across two independent GitHub API endpoints. Watchers 939; `created_at` 2025-07-22; `pushed_at` 2026-09-03; language Python; MIT; not archived.

- **⭐ Corpus-first: the largest single repo by stars in the entire corpus** — ahead of the prior record-holder AutoGPT (184,043★, topic v59); the lead widened from ~17% to **~31%** over the 47-day gap.
- First public release **v0.2.0 on 2026-03-12**. CalVer tags (`v2026.8.31`) map to themed SemVer names — "The Pantheon Release" v0.21.0, "The Quicksilver Release" v0.19.0, "The Judgment Release" v0.18.0.
- **Release velocity is extreme and is itself a finding:** 10 releases in the 54 days from v0.18.2 to v0.21.0. v0.19.0 self-reports ~2,245 commits / ~1,065 merged PRs / 450+ contributors; v0.20.0 ~3,650 commits / ~1,400 PRs / **650+ contributors**; v0.21.0 5,800 commits / 2,475 PRs / 2,100 issues closed. Contributors grew 450→650 in the two weeks between v0.19.0 and v0.20.0.
- ⚠️ **Any version-pinned statement in this topic decays in days, not months.** Every source in both bundles is now behind `main`.
- Org **Nous Research** — real GitHub org (est. 2023-05-20, 88 public repos, [nousresearch.com](https://nousresearch.com)); best known for the **Hermes** open-weight model family.

## What it does (all primary-confirmed)
- **Learning loop** — agent-curated memory + autonomous skill creation + skill self-improvement → see [[learning-loop-and-self-improving-skills]].
- **Persistent memory** — FTS5 cross-session search + LLM summarization + Honcho dialectic user modeling → see [[memory-system]].
- **Multi-channel gateway** — one process reachable on Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI (docs claim 20+ incl. Teams/Matrix).
- **Cron scheduler**, **isolated parallel subagents + Python RPC**, **MCP** support, **agentskills.io** skills, web/vision/TTS tools.
- **Provider-agnostic** (Nous Portal / OpenRouter / OpenAI / any endpoint) across **6 backends** (local / Docker / SSH / Singularity / Modal / Daytona) → see [[channels-providers-deployment]].
- **OpenClaw successor** — ships `hermes claw migrate` to import an OpenClaw setup → see [[hermes-vs-openclaw]].

## Corpus positioning
- **Distinct niche vs its siblings:** Hermes is a **single-user, always-on personal agent runtime**, not an agent *framework* like [[vercel-eve|vercel-eve]] (topic 67, tools to *build* durable agents) nor an agent *multiplexer* like [[herdr|herdr]] (topic 68, orchestrating a *fleet* of coding agents). It sits closest to **OpenClaw** (its explicit migration target/rival).
- Cross-links: [[agent-memory-architecture|agent-memory-architecture]] (memory + Honcho; shared creator Sean's AI Stories), [[harness-engineering|harness-engineering]] (self-improving loop), [[multi-agent-orchestration|multi-agent-orchestration]] (subagents), [[claude-code-clones|claude-code-clones]] + [[local-ai-coding-agents|local-ai-coding-agents]] (self-hosted agent peers).

## Key Takeaways
- Hermes is a **personal, self-improving, self-hosted agent** from a credible lab (Nous Research), MIT-licensed, genuinely feature-rich — the confirmed core is strong.
- **The star count is real and record-setting for this corpus (240,313 ⭐ on 2026-09-03 > AutoGPT).** The SEO "22K stars" figure was a ~10× undercount ([[claims-scorecard]] H2 = FALSE) — and the 2026-09-03 revisit found that **no two sources in either bundle agree on this number**: ~7,000 (2026-05-04) · 140,000 (2026-05-14) · 200,000+ (2026-08-26). It is the single most-misreported fact about this project ([[revisit-2026-09-03]]).
- The marketing superlatives do **not** survive fact-check: "only agent with a learning loop" (FALSE), "launched Feb 2026" (FALSE — first release Mar 2026), "no-code / easier than OpenClaw" (MISLEADING), "224B tokens overtook OpenClaw" (UNVERIFIABLE). See [[caveats-and-corrections]].
- The most credible reviewer (Sean's AI Stories) says the "self-improving skills" are currently **memory-updates, not autonomous skill-quality evolution** — a material maturity caveat.
