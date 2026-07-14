# Source provenance — verification ledger

## Primary source

- Video `K3UXUOJ3ac0` — Tự Học Cùng AI, "Hướng dẫn cài Skill 'teach' và tạo lộ trình học theo năng lực" (2026-06-28, 18:35, VN community channel). `vi-orig` auto-captions fetched via `yt-dlp`, cleaned with `sed`/`grep`/`awk` (python3 denied under this session's sandbox — see raw file header), read IN FULL in the main loop. `--write-info-json` pulled the VN description (which independently confirms the 6-concept/3-layer terminology in the presenter's own words, including the English terms Knowledge/Skill/Wisdom).

## Verification workflow

**Workflow `wf_5eb1dd9c-596`** — 11 agents (5 first-party dives + 5 refute-first verifiers, paired per-claim + 1 completeness critic). ~441K tokens, 138 tool calls, ~3.5 min wall-clock, all agents on Haiku 4.5. **0 errors, 0 empty results.**

## Main-loop follow-up (Rule 12 — fail loud)

The completeness critic flagged two concerns that the main loop resolved independently rather than trusting the workflow's own verdicts at face value:

1. **"Is `learn.chatgpt.com` actually OpenAI's own docs domain, or a lookalike?"** — Resolved by a direct `WebFetch` of `developers.openai.com/codex/pricing` and `developers.openai.com/codex/skills`: both return a **308 permanent redirect to `learn.chatgpt.com`**, confirming it as OpenAI's own docs domain (rebranded under "ChatGPT Learn"), not a third-party site.
2. **The free-tier contradiction** — The workflow's own verify pass had already landed on FALSE (citing `help.openai.com`), but the *dive* agent's initial finding, several general-web search summaries, and a first main-loop `WebSearch` pass all suggested Free-tier CLI access was real. A direct `WebFetch` of the actual pricing page (via the confirmed-authoritative redirect) settled it: **the Free plan explicitly excludes Codex CLI**; the minimum tier with CLI access is Go ($8/month). The third-party aggregator blogs surfaced by search were conflating general ChatGPT-app Codex access with CLI-specific access.
3. **Matt Pocock provenance** — rather than trusting the dive agent's summary of the `mattpocock/skills` repo, the main loop directly `WebFetch`ed the actual `teach/SKILL.md` file and confirmed the near-verbatim concept and language match itself (quoted in [[matt-pocock-provenance]]).
4. **Codex CLI's canonical skills path** — the main loop directly fetched `learn.chatgpt.com/docs/build-skills` (following the confirmed-authoritative redirect) rather than relying on third-party paraphrase, establishing `$HOME/.agents/skills` as the documented canonical path (not `~/.codex/skills`).

No verifier misfires or agent deaths in this run — the main-loop follow-up was precautionary (per the critic's explicit request for a sanity check on domain authority), not a correction of a broken agent.

## Scorecard

See [[claims-scorecard]] — 2 CONFIRMED / 1 CORRECT-BUT-INCOMPLETE / 0 MISLEADING / 2 FALSE / 0 FABRICATED.

## See also

[[_index]] · [[claims-scorecard]]
