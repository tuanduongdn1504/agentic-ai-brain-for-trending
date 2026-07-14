# Claims scorecard

| # | Claim | Verdict | Article |
|---|---|---|---|
| 1 | Codex CLI has an official Skills-folder feature you install by dropping a folder into `.codex` | **CORRECT_BUT_INCOMPLETE** — feature is real (`agentskills.io` spec, shipped 2025-12-19); the video's exact path (`~/.codex/skill/`) is outdated vs. current canonical `~/.agents/skills` | [[codex-skills-feature-verified]] |
| 2 | `$skillname` is a real Codex CLI invocation mechanism (not a prompt-engineering convention) | **CONFIRMED** — directly quoted in OpenAI's own docs: "type `$` to mention a skill" | [[codex-skills-feature-verified]] |
| 3 | Codex CLI works with a free ($0/month) ChatGPT account | **FALSE** — current official pricing excludes Free from Codex CLI; minimum is Go ($8/month) | [[codex-free-tier-fact-check]] |
| 4 | The "teach" skill's 6-concept + 3-layer structure is genuinely original to the VN community creator, with no public precedent | **FALSE** — near-verbatim match to Matt Pocock's public `mattpocock/skills` "teach" Agent Skill, unattributed in the video | [[matt-pocock-provenance]] |
| 5 | "Donella Meadows" / "Thinking in Systems" / "Leverage Points" is the correct resolution of the video's garbled captions | **CONFIRMED** — real author, real book, real essay | [[donella-meadows-source]] |

**Totals: 2 CONFIRMED / 1 CORRECT-BUT-INCOMPLETE / 0 MISLEADING / 2 FALSE / 0 FABRICATED.**

Note: none of the FALSE verdicts indicate deliberate fabrication by the video's presenter — claim 3 is plausibly a pricing-policy or API-key-vs-plan mismatch (see [[codex-free-tier-fact-check]]), and claim 4 is an attribution gap rather than a technical falsehood (the skill genuinely works as shown; it's the "we made this" framing that doesn't hold up).

## See also

[[_index]] · [[source-provenance]]
