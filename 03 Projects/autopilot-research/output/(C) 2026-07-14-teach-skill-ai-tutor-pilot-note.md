# Pilot note — teach-skill-ai-tutor (2026-07-14)

> Full research: [wiki/teach-skill-ai-tutor/_index.md](../wiki/teach-skill-ai-tutor/_index.md)

## Is this a code-level pilot candidate for hireui?

**No — this is a pattern-recognition + provenance-discipline note, not an adoption candidate.** hireui has no tutoring/onboarding feature planned, and the Skill itself runs on Codex CLI, not any tooling hireui uses.

## What's worth taking, conceptually

- **The files-as-memory mechanic** (mission/note/resource/learning-record persisted as plain files, re-read at the start of each session instead of relying on chat history) is the same pattern already banked in [[../agent-memory-architecture/_index]] and [[../claude-code-memory-systems/_index]] — a reminder that this "structured markdown files as durable agent state" approach keeps reappearing across genuinely different use cases (coding agents, tutoring agents), not just a coding-agent trick.
- **Provenance discipline reminder:** an unattributed "community-made" skill package should be checked against known public skill repositories (starting with `mattpocock/skills`, now confirmed as a recurring source in this corpus — 3 appearances) before treating it as novel. Worth keeping in mind for any future video that presents a generically-named skill/prompt-pack as original.

## Why not build on this directly

Nothing here is hireui-adjacent: no LLM feature of hireui's needs an AI-tutor Skill, and the Codex CLI Skills-feature finding (real, `agentskills.io`-compliant) only matters if a teammate were ever using Codex CLI rather than Claude Code.

## Bottom line

File this as a **provenance-and-pattern reference** only. No new entry needed in the vault's pilot-ranking backlog.
