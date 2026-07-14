# Pilot note — pydantic-ai-2 (2026-07-14)

> Full research: [wiki/pydantic-ai-2/_index.md](../wiki/pydantic-ai-2/_index.md)

## Is this a code-level pilot candidate for hireui?

**No — this is a design-pattern reference, not an adoption candidate.** Pydantic AI is a Python framework; hireui is TypeScript/Next.js. There's no direct migration path.

## What's worth taking, conceptually

The **capability** primitive — bundle an agent's instructions, tools, lifecycle hooks, and model settings into one reusable, progressively-disclosed unit — is a clean way to think about structuring hireui's planned **Match-Explain** LLM feature (the recruitment CV↔job matching feature spec'd across [[../miai-cv-matching-agent/_index]] and [[../mosh-ai-powered-apps/_index]]):

- Instead of one monolithic system prompt + tool list, define **capability-shaped units** even in plain TypeScript: a `matchExplanation` capability (instructions + the scoring tool + a guardrail hook) separate from a `candidateQA` capability (different instructions + knowledge-base tool), each independently reusable if hireui ever needs a second agent surface (e.g. a candidate-facing chatbot reusing the same knowledge-base logic).
- **Progressive disclosure matters even without a framework enforcing it:** don't load every possible tool/instruction into every LLM call. Gate expensive or rarely-needed instructions (e.g. an escalation-to-recruiter path) behind an explicit "does this conversation need it" check, mirroring what Pydantic AI's `defer_loading=True` and Anthropic's own Agent Skills spec both do natively.
- This is the same underlying idea already banked from [[../github-copilot-cli-agents/agent-skills-shared-standard]] (Claude/GitHub Agent Skills) — Pydantic AI is now a third independent confirmation that "small catalog entry, full detail on demand" is the right shape for composable agent behavior, regardless of framework or language.

## Why not build on Pydantic AI directly

hireui has no Python service today and no LLM integration yet at all (verified 2026-06-15: zero Claude API usage in product code). Introducing a second-language backend just to get this pattern isn't justified — the pattern is portable as an architecture idea; the framework isn't.

## Bottom line

File this as a **design-review vocabulary item** (bring it up when scoping Match-Explain's prompt/tool architecture), not as a queued pilot. No new entry needed in the vault's pilot-ranking backlog.
