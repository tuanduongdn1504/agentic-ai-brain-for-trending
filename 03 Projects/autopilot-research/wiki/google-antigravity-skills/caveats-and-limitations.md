# Caveats & limitations (the critic layer)

> Antigravity is a **free public-preview** product moving fast. The video is a sunny beginner tutorial; this article is the counterweight. **Sourcing note:** the platform *facts* below are from official Google sources; the *operational pain points* are **community/support-forum reports as of mid-2026** and are labeled as such — treat them as directional, not certified.

## Source

Verification workflow `wf_1e5cf2f6-5ec` (usage-caveats dimension) + community/support threads. Distilled in [[google-antigravity-skills/source-provenance]].

---

## Confirmed / structural

- **Public preview, no production SLA.** Antigravity 2.0 shipped as a preview (May 2026). Not positioned for production-critical daily use in the launch window.
- **Chrome dependency.** The built-in `/browser` command requires **Google Chrome as the default browser** to work.
- **Linux is partial.** Supported on "specific Linux distributions", not universally; delivered as a `.tar.gz` bundle.
- **Data retention.** Enterprise offers **Zero Data Retention**; standard Gemini has an ~18-month retention window (configurable). If you point it at sensitive data, know which tier you're on. (Enterprise compliance certs — SOC2/ISO/HIPAA — not clearly documented for the preview.)

## Community-reported (mid-2026) — verify against your own usage

- **Heavy token overhead on the CLI.** Reports of **~23–25k tokens** consumed by system prompt + tools *per request* before your input. Documented anecdote: 24.3k of a 1M window used with ~2 tokens of user text. A "Flash (Low)" variant reportedly cuts overhead materially. → cost implications overlap with [[../claude-api-cost-optimization/_index]].
- **Quota that bites.** Marketing implied a short (~5-hour) refresh; users report **weekly quota cycles with multi-day lockouts** after a spring-2026 build. A **Reason-Act-Verify infinite loop with no failure threshold** was reported to drain an entire weekly quota in minutes. No official fix acknowledged in the window.
- **Account suspensions.** Multiple reports of automated **403 / ToS suspensions** with an unclear appeals path.
- **Stability on long jobs.** Context-memory errors and premature agent termination on long-running operations.

## Claims to NOT repeat as fact

These circulate online but are **single-source / unconfirmed** — I flag rather than assert them (per this vault's no-fabrication rule):

- Exact version strings + dates (e.g. "v1.20.3 on Mar 5 2026", "v1.20.5 regression").
- "**AGENTS.md used by 60,000+ repos**" — directional at best.
- The **6 persona names** (Sentinel/Explorer/Worker/Reviewer/Critic/Auditor) and hard limits ("max 10 nesting levels", "12,000-char workflows").
- "Gemini 3.5 Flash outperforms almost everything" — Google's benchmark wins are on **specific** agentic/coding benchmarks, not universal.
- A "catastrophic bait-and-switch" narrative — real quota/loop bugs exist, but no single official "catastrophe" event; the framing is user interpretation.

## What this means for a pilot

- **Don't put the preview on the critical path.** Great for a **sandbox / second-opinion** surface; not (yet) a Claude Code replacement for production work.
- **Watch the meter.** If you pilot the CLI, budget for the overhead and cap loops; treat quota as weekly, not hourly.
- **Keep secrets out.** Don't feed production candidate/PII data (e.g. hireui) into a preview tool with unclear retention/appeals — see the pilot menu's M0 gate.
- The **portable-skills thesis survives all of this**: even if you never adopt Antigravity as a daily driver, the `SKILL.md` + `AGENTS.md` standards work (see [[google-antigravity-skills/anthropic-agent-skills-portability]]).

## Key Takeaways

- **Public preview, no SLA**, Chrome-dependent, partial Linux, retention depends on tier — the *structural* caveats.
- **Community reports (mid-2026):** ~23–25k token overhead, weekly-quota lockouts, an infinite-loop quota drain, and automated 403 bans — real signal, not yet officially resolved.
- Several viral specifics (version dates, "60k repos", persona names, "beats everything") are **unverified** — don't restate them as fact.
- **Pilot it as a sandbox/second surface**, meter it, keep sensitive data out — the portable-standards payoff doesn't require betting production on the preview.
