# (C) oh-my-openagent — Open Questions

> 20+ questions for follow-up; observational baseline + meta-discipline tracking.

## License + commercial structure

1. Is SUL-1.0 the n8n.io license family or distinct? (Sustainable Use License — same name as n8n.io's; verify text equivalence.)
2. Sionic AI vs Sisyphus Labs: parent-subsidiary, sibling-companies, or parallel ventures? (sisyphuslabs.ai claims "fully productized version of Sisyphus" — separate-product positioning observed but legal-relationship unclear.)
3. Will commercial-tier pricing/structure for "fully productized Sisyphus" be revealed? (Currently only waitlist on sisyphuslabs.ai.)
4. SUL-1.0 + Sisyphus Labs commercial-tier model = open-core? Or pure license-restriction (no separate paid SaaS)? (omo OSS already non-commercial-restricted; commercial waitlist suggests separate paid tier coming.)
5. Does YeonGyu hold IP rights individually or via Sionic AI / Sisyphus Labs? (LICENSE.md doesn't disclose; "licensor" is undefined entity.)

## Adversarial-Anthropic positioning

6. What was the specific incident behind "Anthropic blocked OpenCode because of us"? (X.com @thdxr post link asserts but doesn't elaborate; verify per third-party reporting.)
7. Has Anthropic responded publicly to the README claim? (Brand-association implications for any Storm Bear adoption.)
8. Will adversarial-positioning intensify or moderate over time? (omo's commercial-incubation via Sisyphus Labs may pressure tone shift.)
9. Does adversarial framing drive subscription-rotation or actually compromise feature compatibility with Claude API? (Claim: "Claude Code's a nice prison" but README also says "Your hooks, commands, skills, MCPs, and plugins? All work here." — apparent compatibility suggests pricing/strategy tension, not product break.)

## Korean ecosystem peer relationships

10. Are YeonGyu-Kim and Yeachan Heo (OMC v27) collaborators or independent? (Both Korean Seoul; both build agent harnesses; both reference Sisyphus mythology; both fork OpenClaw; geographic + naming + lineage convergence is high. OMC v27 cited "oh-my-opencode" as inspirational source.)
11. What's the broader Korean Claude/agent-tooling community size? (Discord channels, conferences, Naver/Kakao engineers, etc.)
12. Why Sisyphus mythology specifically (vs Hercules / Apollo / etc.)? (Sisyphus = "endless toil" — fits "agent that never stops" framing; Albert Camus reference?)
13. Will 3rd Korean T1 entrant emerge to validate 73a Korean N=3 default-criterion? (Current N=2 = OMC + omo.)

## Architecture + technical depth

14. How does omo's `OpenClaw` fork differ from upstream OpenClaw mainline? (`src/openclaw/` subdir handles bidirectional integration — Discord/Telegram/webhook/command — but core fork modifications opaque without diff.)
15. Hashline `LINE#ID` edit tool — is `oh-my-pi` (can1357) implementation precedent or independently invented? (README cites oh-my-pi as inspiration; verify implementation similarity.)
16. 1,766 TS files / 377K LOC at 4.7-month age = sustainable maintenance load? (Solo author + contributor PRs via CLA; `bus factor = 1` concern even at this scale.)
17. 11-platform binary build pipeline maintenance cost — automated via GitHub Actions per `publish-platform.yml`; failure rate at 200+ releases?
18. 3-tier MCP system (built-in + Claude Code .mcp.json + skill-embedded) — is skill-embedded tier corpus-first? Or precedent in another framework?
19. `IntentGate` classifier (research/implementation/investigation/evaluation/fix) — any published documentation on classifier design or only inferable from src/?

## Storm Bear pilot relevance + license blocking

20. Can Storm Bear use omo for personal/internal Scrum coaching workflows (not commercial)? (SUL-1.0 says "internal business purposes" allowed — but Storm Bear's Scrum coaching IS commercial business. Pilot-eval-only or internal-process-tooling acceptable?)
21. Does omo's `docs/superpowers/` integration mean omo IS a strict superset of Superpowers v2 functionality? Or just cites/references it?
22. SKILL.md format compatibility with Vercel v51 / awesome-claude-skills v50 / aidevops v47 / Anthropic skills registry?
23. Multi-runtime category-routing (visual-engineering / deep / quick / ultrabrain) — is category schema fixed or extensible? (`src/tools/delegate-task/constants.ts` per AGENTS.md; verify customization API.)
24. "Skip This README — paste link to your agent" workflow assumes operator already has Claude Code or other AI agent runtime. What's onboarding path for fresh users without prior runtime?

## Pattern Library + corpus discipline

25. Pattern #57 57c N=2 structural promotion-candidate at v52 mini-audit — would promotion under structural-N=2 criterion be appropriate, or wait for default-criterion N=3?
26. Pattern #18 OpenCode-primary N=2 (registered v47 N=1 stale-risk-flagged with v52 stale-check; un-stales at v52 omo evidence) — promotion-candidate at next mini-audit under structural-N=2?
27. Pattern #58 58c sub-variant at N=1 — wait for v57 stale-check or promote to formalized within-pattern variant immediately?
28. Pattern #50 50d sub-variant at N=1 — same question (incubation-waitlist-as-funnel-terminus).
29. Pattern #29 SUL-1.0 sub-context formalization — is "custom-non-OSI-non-commercial-restriction" sufficiently distinct from PolyForm Noncommercial (Pattern #72) to warrant separate sub-context vs Pattern #72 generalization?
30. Will 16-streak zero-registration extend further or break at v53? (Trend forecast: depends on next wiki source novelty + consolidation-forward discipline.)
