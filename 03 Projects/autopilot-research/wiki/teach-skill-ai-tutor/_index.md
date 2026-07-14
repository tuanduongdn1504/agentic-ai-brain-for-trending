# Topic: teach-skill-ai-tutor

> **A Vietnamese community channel demos installing a "teach" AI-tutor Skill into OpenAI Codex CLI — verification finds the Skill itself is (near-certainly) Matt Pocock's public GitHub skill, unattributed, while the underlying Codex CLI Skills feature is real and independently confirmed as a third vendor on the shared `agentskills.io` spec.**
> **Compiled:** 2026-07-14 (path 5 yt-dlp-only, single video, full VN transcript read in main loop; adversarial verification via Workflow `wf_5eb1dd9c-596`).
> **Source video:** Tự Học Cùng AI — "Hướng dẫn cài Skill 'teach' và tạo lộ trình học theo năng lực" ([K3UXUOJ3ac0](https://www.youtube.com/watch?v=K3UXUOJ3ac0), 2026-06-28, 18:35). Skill distributed only via the creator's private Facebook group (`facebook.com/groups/tuhoccungai`) — not a public repo.

---

## The premise

The video demos a 6-concept, 3-layer "teach" AI-tutor Skill: give it a **Mission** (why you want to learn something), and it generates **Lessons** tailored to your stated goal, drawing on your **Resources** (books/links you provide), tracking a **Learning Record** (your mistakes/difficulty level) to tune future lessons, distilling **References** (quick-review cheat sheets), and honoring your **Note** preferences (tone, length, language). Philosophically: **Knowledge** (credible sources) → **Skill** (practice that feeds back into future lessons) → **Wisdom** (real-world community practice, which the AI explicitly cannot substitute for). Demoed on OpenAI's **Codex CLI**, installed by copying a folder into a hidden `.codex` directory and invoked with `$teach`. See [[overview]].

## Headline finding

**This is (near-certainly) Matt Pocock's public "teach" Agent Skill**, not an original creation of the VN community channel. A direct fetch of [`mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md`](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md) shows the **exact same six concepts** (Mission, Lesson, Reference, Learning Record, Resource, Note) and the **exact same three-layer Knowledge → Skills → Wisdom language**, down to matching phrasing. The video never mentions Matt Pocock or GitHub — it presents the Skill as something the channel "made and shared" with its private Facebook group. See [[matt-pocock-provenance]]. This is the **third time Matt Pocock's work has surfaced in this corpus** (previously: Process Interviewer in [[../claude-skills/_index|claude-skills]], the `/grill-with-docs` cross-port already tracked in the vault's own Pattern Library).

## What's actually confirmed about the tooling

- **Codex CLI's Skills feature is real** — shipped 2025-12-19, follows the same open `agentskills.io` spec already confirmed for Anthropic Claude Code + GitHub Copilot CLI. This makes OpenAI a **third vendor on the literal spec** (distinct from Pydantic AI's independent-convergence case). See [[codex-skills-feature-verified]].
- **The video's exact install path (`~/.codex/skill/`) is outdated/non-canonical** — OpenAI's current official docs specify `$HOME/.agents/skills` (a shared cross-vendor location), not `~/.codex/skills`. The feature works either way in the demo, but the canonical path has moved.
- **The `$skillname` invocation is a real, documented, first-class Codex CLI feature** (`type $ to mention a skill`) — not a prompt-engineering convention, confirmed via OpenAI's own docs.
- **The presenter's "works on a free ChatGPT account" claim does NOT match current official pricing** — OpenAI's pricing page states Codex CLI requires at minimum the Go plan ($8/month); Free explicitly excludes it. See [[codex-free-tier-fact-check]].
- **Donella Meadows / "Thinking in Systems" / "Leverage Points" attribution is correct** — the auto-captions garbled her name and the leverage-points concept, but the underlying citation is accurate. See [[donella-meadows-source]].

## Articles

- [[overview]] — what the video demos, full 6-concept + 3-layer breakdown, the persistent-files-as-memory mechanic
- [[codex-skills-feature-verified]] — ground-truth on Codex CLI's real Skills feature: spec, path, invocation, release date
- [[matt-pocock-provenance]] — the unattributed-match finding, why it matters, what remains unverifiable
- [[codex-free-tier-fact-check]] — the free-tier claim vs. current official pricing
- [[donella-meadows-source]] — confirming the systems-thinking source material + garble corrections
- [[claims-scorecard]] — full verdict table
- [[source-provenance]] — verification ledger (workflow + main-loop follow-up fetches)

## Cross-links

- [[../codex/_index]] — the general Codex-as-agentic-harness topic; this adds the Skills-feature dimension that topic didn't cover
- [[../github-copilot-cli-agents/agent-skills-shared-standard]] — updated with Codex CLI as a confirmed third vendor on the `agentskills.io` spec
- [[../claude-skills/_index]] — Matt Pocock's second corpus appearance (Process Interviewer / grill-me was the first)
- [[../agent-memory-architecture/_index]] · [[../claude-code-memory-systems/_index]] — the "persist everything as files so a new chat thread doesn't lose context" mechanic is the same files-as-memory pattern documented in both topics

## Source provenance (headline)

Verified via Workflow `wf_5eb1dd9c-596` (11 agents: 5 dives + 5 refute-first verifiers + 1 completeness critic; ~441K tokens, 138 tool calls, 0 errors) **plus main-loop direct-fetch follow-up** resolving the critic's flagged uncertainty about source-domain authority and the free-tier contradiction. **Scorecard: 2 CONFIRMED / 1 CORRECT-BUT-INCOMPLETE / 0 MISLEADING / 2 FALSE / 0 FABRICATED.** Full log: [[source-provenance]].
