# Hermes Agent — License, Pricing & the Skill Hub

## Source
Official README + [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com) + `/docs/`; t8 AI LABS (Skill Hub). Verified via `wf_06a79485-687` (C7, C16 = CONFIRMED).

## License (C7 — CONFIRMED)
- **MIT** — confirmed by GitHub API, README, and the site. No dual-license or relicensing nuance found. The **software is free and open source**; you self-host it.
- Built by **Nous Research** (confirmed org). No CLA/commercial-restriction traps surfaced (unlike [[herdr|herdr]]'s AGPL+commercial dual license).

## Cost model (C16 — CONFIRMED)
- **You pay for two things regardless of tier:** (1) **model tokens** (your provider) and (2) **hosting** (VPS/cloud) — *unless* you run a free local model on your own hardware.
- **Freemium Nous Portal tiers: Free / Plus / Super / Ultra.** Paid tiers bundle **monthly credits** + access to **"300+ models" with built-in tool use** via Nous Portal. The Portal is an *optional convenience* — you can bring your own OpenRouter/OpenAI/custom keys instead and skip Portal entirely.
- Practical cost lever (t1): **route by task** — expensive models for planning/reasoning, cheap models (e.g. DeepSeek) for crawl/gather. Costs are trackable in-app.

## The Skill Hub (t8)
- **Official skill marketplace** ("skill hub") with skills for many use-cases; **agentskills.io-compatible** so skills are portable.
- **~90 skills pre-installed by default** (version-dependent count) — these are **maintained by Nous** and therefore trusted.
- **Security posture:** the Skill Hub **runs a security scan on each skill** and watches for dangerous prompts/scripts (e.g. data-exfiltration). This is the explicit contrast the sources draw against OpenClaw's community skills, "a huge number of which weren't safe." *(Nous-maintained-and-scanned is a real, sensible security stance — but "scanned" ≠ "guaranteed safe"; treat third-party Skill Hub skills with normal supply-chain caution.)*

## Key Takeaways
- **Clean MIT + BYO-keys means no license or lock-in blocker** for evaluation — a favorable contrast with the AGPL/commercial and NOASSERTION traps seen elsewhere in the corpus.
- **Total cost = tokens + hosting**, not a Hermes license fee. Nous Portal tiers are optional; the operator can run it entirely on their own keys/hardware for data-residency control.
- The **security-scanned, Nous-maintained default skills** are a genuine differentiator vs unvetted community skill libraries — but apply normal supply-chain scrutiny to community Skill Hub entries.
- Cross-links: [[claude-api-cost-optimization|claude-api-cost-optimization]] (token economics), [[claude-code-skills-stack|claude-code-skills-stack]] + [[claude-skills|claude-skills]] (agentskills.io skill standard).
