# AGENTS.md — the bare-minimum guardrail

## The claim (as made)

"Guardrail number one. This is the absolute bare minimum, right? Agents.md. Should have this in all your GitHub repos or whatever kind of repo structure you have. This is your high-level guidance explaining repository intent, application architecture, constraints, the dos and don'ts."

## Verified

- **AGENTS.md is a real, cross-vendor open convention**, stewarded by the Agentic AI Foundation (Linux Foundation), used across 25+ tools (OpenAI Codex, Google Jules, Cursor, Windsurf, Factory, Aider, Devin, Zed, VS Code, JetBrains, Warp, and others). It is plain Markdown with **no required fields** — "the closest thing today to a vendor-neutral baseline."
- **GitHub Copilot genuinely reads it.** Support was added **2025-08-28** (`github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/`). It works *alongside*, not instead of, GitHub's own `.github/copilot-instructions.md`:
  - **AGENTS.md** — cross-tool, works in Copilot, Cursor, Codex, etc.
  - **`.github/copilot-instructions.md`** — GitHub/Copilot-specific instructions
  - **`.github/instructions/*.instructions.md`** — path-scoped instructions
  - Copilot's coding agent reads AGENTS.md, CLAUDE.md, *and* GEMINI.md if present, plus its own file — it's genuinely omnivorous about repo-level instruction files.
- Framing it as "the bare-minimum guardrail" is accurate — GitHub's own 2,500-repository analysis of AGENTS.md files independently converged on the same "bare minimum" framing (a three-tier Always/Ask-First/Never guardrail structure).

## The important caveat: Claude Code does not read AGENTS.md

This is the sharpest, most actionable finding in this whole topic. Chris's talk doesn't make a false claim about Claude here — he doesn't actually say "Anthropic supports AGENTS.md" (that "vendor agreement" line, checked carefully against the transcript, is about **Skills**, not AGENTS.md — see [[agent-skills-shared-standard]]). But it's worth stating plainly for anyone drawing the parallel themselves:

- **Claude Code reads `CLAUDE.md`, not `AGENTS.md`, natively.** There is no fallback or auto-import.
- This is a large, long-standing, unresolved community request. **GitHub issue #6235** ("Feature Request: Support AGENTS.md," opened 2025-08-21) has accumulated thousands of reactions and is described by third-party trackers as the single largest unmet feature request in the `anthropics/claude-code` issue tracker — with at least three duplicate/related open issues (#31005, #34235, #36153) as of mid-2026. Anthropic has not shipped native support and has not publicly committed to a timeline as of this writing. *(Exact reaction/comment counts are omitted here deliberately — two independent checks returned different numbers; treat "thousands, growing" as the safe fact, not any specific figure.)*
- **This does not affect hireui.** hireui already uses CLAUDE.md as its source of truth per its own constitution — there's no gap to close, just a fact worth knowing if hireui ever needs to interoperate with a Copilot-based teammate or tool on the same repo.

## See also
[[_index]] · [[agent-skills-shared-standard]] · [[claude-code-parity-and-gaps]] · [[claims-scorecard]]
