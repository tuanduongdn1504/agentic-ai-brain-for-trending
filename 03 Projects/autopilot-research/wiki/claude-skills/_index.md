# Topic: claude-skills

> **Ben AI's "8 Claude meta-skills"** + a double deep-dive into the original resource behind each. Demoed in Claude Cowork; usable in Claude Code / Codex / any skills-supporting surface.
> **Compiled:** 2026-06-20 (path 5 yt-dlp full transcript + direct primary-source fetch + adversarial workflow verification `wf_884737d0-afa`).
> **Source video:** Ben AI — "8 Claude Skills I Can't Live Without" ([bXnRA3pJavE](https://www.youtube.com/watch?v=bXnRA3pJavE), 2026-04-18, ~20 min, 147K views). Free plugin: `c.benai.co/8csiu-free`.

---

## The premise

Ben AI argues Skills are the most important Claude feature to learn, and that the 8 he uses daily are **meta-skills** — cross-task upgrades (not workflow-specific) that get sharply stronger **with a second brain set up**. The operator runs two LLM-Wiki vaults + a `~/.claude` memory, so the second-brain multiplier applies directly. See [[claude-skills/overview]].

## The 8 skills → their originals

1. **Process Interviewer** ← Matt Pocock "grill me" + Anthropic skill best-practices
2. **Prompt Master** ← Anthropic prompt-engineering (≠ official Prompt Improver)
3. **Humanizer** ← Wikipedia "Signs of AI writing"
4. **Fact Checker** ← evidence-based verification + web cross-ref
5. **Find Skills** ← skills.sh (Vercel) marketplace
6. **Front-end Slides** ← slide-design best practices
7. **Decision Toolkit** ← first-principles / decision science
8. **MCP Builder** ← the **real official `mcp-builder` Anthropic skill** + MCP protocol

## Articles

- [[claude-skills/overview]] — what skills are, the meta-skill concept, the 8 + bonus 3, provenance summary, the second-brain multiplier
- [[claude-skills/the-eight-meta-skills]] — full per-skill catalog (problem / what / demo / install / customize / chain) + auto-run & chaining patterns
- [[claude-skills/original-anthropic-agent-skills]] — **the foundation:** SKILL.md format, progressive disclosure, authoring best practices, cross-platform reach, skills vs MCP/Projects
- [[claude-skills/original-matt-pocock-grill-me]] — Process Interviewer's lineage; grill-me / grill-with-docs; the operator already cross-ported this into brain-setup v2
- [[claude-skills/original-wikipedia-signs-of-ai-writing]] — the Humanizer's reference catalogue (8+ categories of AI tells, era-specific vocab)
- [[claude-skills/original-skills-sh-marketplace]] — the Find-Skills ecosystem (788K+ installs), install model, **Snyk supply-chain audit + vetting framework**
- [[claude-skills/original-mcp-builder-and-mcp]] — the real `mcp-builder` skill + an MCP primer + the config flow
- [[claude-skills/original-prompt-engineering-best-practices]] — Prompt Master's basis: Anthropic's 7 canonical techniques + the official Prompt Improver
- [[claude-skills/video-to-original-crosswalk]] — every skill → source → what Ben adds → what it omits; methodology-derived vs original-backed vs first-party
- [[claude-skills/source-provenance]] — verification ledger: verified / corrected / flagged

## Pilot

Ranked methods to apply the 8 skills to the operator's flows: `output/(C) 2026-06-20-claude-skills-pilot-methods.md` (22 methods across personal-memory / autopilot-vault / Storm-Bear-vault / hireui-Goal-#2 / Scrum-coaching, + a skip list + a critic's reframe).

## Cross-links

- [[ai-operating-system/_index]] — Ben AI's sister video ("5 Skills to Build an AI Operating System"); the second-brain framing
- [[claude-cowork/_index]] — the product surface Ben demos on
- [[claude-code-memory-systems/_index]] — progressive disclosure ≈ memory-layering
- [[prompt-evaluation/_index]] — Fact Checker vs grading/eval rigor
- [[claude-api-cost-optimization/_index]] — progressive disclosure as token discipline
- [[harness-engineering/_index]] · [[multi-agent-orchestration/_index]] · [[cowork-third-party-inference/_index]]

## Source provenance (headline)

Primary-source-grounded + adversarially verified. **7 of 8 skills trace to real originals; #8 (`mcp-builder`) is genuinely first-party Anthropic.** Corrected from the raw drafts: the MCP-Builder "fake" error (it's real), Ben's "91,000 skills" (now 788K — a metric drift, not a contradiction), and the "Cowork unverified" flag (Cowork is real). Flagged ⚠️: Ben's own skill internals, the free plugin contents, the bonus skills, marketing claims. Full log: [[claude-skills/source-provenance]].
