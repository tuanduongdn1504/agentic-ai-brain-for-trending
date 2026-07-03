# AGENTS.md + CLAUDE.md in ghost-ai — the portability layer

> Ground truth: both root files fetched and read in full; provenance of the injected block verified against the official Next.js 16.2 blog.

## AGENTS.md (1.2KB — the real harness)

Two blocks:

1. **Injected Next.js block** between `<!-- BEGIN:nextjs-agent-rules -->` … `<!-- END:nextjs-agent-rules -->`:
   *"# This is NOT the Next.js you know — This version has breaking changes… Read the relevant guide in `node_modules/next/dist/docs/` before writing any code."*
2. **"Application Building Context"** — the six-file reading order (1→6) + update-tracker rule + docs-as-master rule ([[six-file-context-system]]).

### Provenance of the injected block (dead-panel claim, closed with primary source)

- The **marker mechanism is official Next.js 16.2** ("Next.js 16.2: AI Improvements", nextjs.org/blog/next-16-2-ai, 2026-03-18): `create-next-app` now ships an `AGENTS.md` by default; existing projects add it manually or via `npx @next/codemod@latest agents-md`. The markers delimit the "Next.js-managed section"; future updates only replace inside them.
- The **current official wording** is *"# Next.js: ALWAYS read docs before coding — …Your training data is outdated — the docs are the source of truth."* Ghost-ai's *"This is NOT the Next.js you know"* is a **variant** (earlier template revision or edited) — same mechanism, different words. Do not cite ghost-ai's phrasing as the official template.
- Load-bearing context from the same blog: the Next.js package now **bundles its full docs as Markdown** (`node_modules/next/dist/docs/`) — version-matched local context for agents; plus browser-log forwarding to terminal, dev-server lock file with PID, and `next-browser` agent devtools (installable *as a skill*: `npx skills add vercel-labs/next-browser`).

## CLAUDE.md (35KB — NOT what you'd expect)

- Line 1: `@AGENTS.md` — the official Claude Code include directive (also documented in the Next.js blog as the recommended pattern). So Claude Code reads AGENTS.md via CLAUDE.md.
- The remaining ~35KB is **vendored Trigger.dev v4 SDK documentation** (sections delimited `<!-- TRIGGER.DEV basic START/END -->` etc.), injected by Trigger.dev's init tooling. Zero project-specific content.
- **Pattern reversal vs our vault:** here AGENTS.md holds the project harness and CLAUDE.md is a vendored-docs dump + include shim — the opposite of Storm Bear's CLAUDE.md-as-brain convention. Same standards, inverted roles: more evidence that the *content architecture* (six files) matters and the entry-file name is interchangeable.

## The portability picture (three standards stacked)

| Layer | Standard | In ghost-ai |
|---|---|---|
| Entry/rules file | **AGENTS.md** (Linux Foundation cross-tool standard; read by Claude Code via `@`, Codex, Cursor, Antigravity, Next.js tooling) | six-file reading order + Next.js managed block |
| Skills | **SKILL.md** (Anthropic open Agent Skills format) in `.agents/skills/` + per-agent symlinks | 19 vendor skills ([[skills-supply-chain]]) |
| Framework docs | Bundled Markdown docs in the npm package | `node_modules/next/dist/docs/` |

Demonstrated payoff: **Feature 08 implemented by Codex instead of Claude Code** with the identical spec + context files — agent swap ≈ zero migration. This is the same conclusion as [[../google-antigravity-skills/_index]] (invest in open standards, not one IDE), now observed in a 1.25M-subscriber mainstream tutorial — evidence the portability stack is going mass-market.

## Vercel's AGENTS.md-vs-skills eval (tension worth tracking)

Vercel: AGENTS.md-injected bundled docs scored **100%** on Next.js evals vs **≤79%** for skills-based retrieval — "always-available context works better than on-demand retrieval, because agents often fail to recognize when they should search." Consistent with the video's reactive-skill-rescue moment. Rule of thumb this suggests: **framework-core knowledge → always-on context; tool-specific patterns/debugging → skills, explicitly invoked.**

## Key Takeaways

- Framework vendors are now *injecting managed blocks into your agent files* — AGENTS.md has infrastructure semantics (managed regions), not just prose.
- `@AGENTS.md` as the whole of CLAUDE.md is a legitimate minimal pattern; harness content lives once.
- The stack (AGENTS.md + SKILL.md + bundled docs) is the same portable harness this vault already bet on — this topic adds first-party Next.js/Vercel weight behind it.
- When citing the injected block, cite the **markers** as official and the **wording** as variant.
