# Storm Bear — Agent Instructions

> **Authoritative source:** `CLAUDE.md` in this same directory.
>
> This file is a **22c authoritative-with-shim** template (corpus reference: aidevops v47). Agents reading this should redirect to `CLAUDE.md` for full project context.

## Quick redirect

For full operator context, vault rules, Pattern Library state, and project overviews:

→ Read `CLAUDE.md`

## Why this shim exists

Storm Bear vault uses Anthropic Claude Code as primary harness, but vault content is **runtime-agnostic** by design. This `AGENTS.md` shim makes vault discoverable to:

- OpenCode (consumes AGENTS.md)
- Aider (consumes AGENTS.md)
- Cursor (consumes AGENTS.md)
- Future agentic-AI runtimes

All of these find vault context by reading `AGENTS.md` first. This shim redirects them to `CLAUDE.md` (the authoritative source) without duplicating content.

## Vault state architecture

Refactored 2026-04-27 session 67 — bulk content moved to chapter files:

- `_state/` — CLAUDE.md chapter files (skill references / pattern library state history / project overviews)
- `_goals/` — GOALS.md chapter files (milestones / version log)
- `_patterns/` — PATTERN_LIBRARY.md chapter files (audit history / confirmed patterns / candidates / retired / recent additions)

**Reading discipline for agents:**
- Never read more than 1 chapter file in a single session — context-thrashing risk
- Use `awk` via Bash for surgical line-range extracts when full-chapter not needed
- For wiki builds: read routine v2.1 + 1 most-recent project chapter (`_state/03a-projects-v48-v55.md`) + WebFetch new subject

## License

MIT License. See `LICENSE.md` in this directory.

## Vault is operational, not service

This vault is operator's personal LLM Wiki knowledge base + skill ecosystem. It is published for transparency / pattern-sharing / community-learning. It is NOT:

- A managed service (operator does not host vault-as-a-service)
- A turnkey product (clone-and-run requires Claude Code + Obsidian setup)
- A drop-in agent framework (vault is content + methodology; runtime is your own choice)

## Pattern: LLM Wiki (Karpathy lineage)

Vault implements Karpathy's LLM Wiki pattern (March 2024 lineage) — agent maintains structured wiki per session, agent reads wiki next session for compounding context. Vault has 56 wikis as of 2026-04-29; 39 confirmed cross-wiki patterns; routine v2.1 autonomous orchestration codified in `05 Skills/llm-wiki-routine-v2.1.md`.

## Agent etiquette

When operating this vault:

1. **Blunt + direct** — challenge operator decisions, don't sugarcoat
2. **`(C)` prefix on AI-generated files** — preserve transparency
3. **Ask before editing existing files** — don't modify without permission
4. **Never fabricate** — if you don't know, say so
5. **End every response with suggested next action** — operator habit reinforcement

Full vault rules: `CLAUDE.md` "Claude's Rules & Boundaries" section.

---

For full project context, please read `CLAUDE.md` (authoritative source).
