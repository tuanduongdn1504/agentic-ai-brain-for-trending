# Agent Skills — the best-verified finding in this topic

## The claim (as made)

Skills are "a recipe, something that's repeatable... a skill is called by an agent, it has a strict contract, it's self-contained because it just lives in a folder... this is how it works within GitHub Copilot, but if you're on Claude... you usually have dot Claude slash skills... folders, one folder for each skill, and then you have a skill.md [with] front matter with name and description."

And separately, on why this convergence exists: "I think it's great that we are all in agreement, all the big vendors, whether you are Anthropic or Microsoft or anyone else, because ultimately as developers... we don't always decide what vendor that we use."

## Verified — and it's better than the talk implies

Both halves of the claim are true, and the second half is *more* true than a casual viewer would assume:

- **GitHub Copilot's feature is officially called "Agent Skills"** (`docs.github.com/en/copilot/concepts/agents/about-agent-skills`), not a generic "skills" — folders of instructions/scripts/resources Copilot loads when relevant.
- **GitHub's own docs state the spec is an open standard**: *"The Agent Skills specification is an open standard, used by a range of different AI systems."*
- **Copilot CLI has a real `/skills` command family**: `/skills list`, `/skills info`, `/skills add`, `/skills remove`, `/skills reload`, plus inline invocation (`/skill-name <prompt>`).
- **Claude's side matches almost exactly**, confirmed against Anthropic's own docs (`code.claude.com/docs/en/skills`, `platform.claude.com/docs/en/agents-and-tools/agent-skills/overview`): a folder per skill, `SKILL.md` as the entrypoint, YAML frontmatter with required `name` (lowercase+hyphens, max 64 chars, must match directory) and `description` (max 1024 chars), optional `allowed-tools`/`license`/`metadata`/etc. Storage locations explicitly include `.claude/skills/`, `.github/skills/`, **and** `.agents/skills/` — Anthropic's own docs list the GitHub-flavored path as an equally valid option.
- **Both vendors cite the same named spec: [agentskills.io](https://agentskills.io).** This is the real headline: it's not that Copilot copied Claude's convention or vice versa — **both independently adopted a shared, vendor-neutral open standard**, the same way both read (or in Copilot's case, also write) AGENTS.md-style files. This is a genuinely rare, clean cross-vendor-convergence data point for the corpus (compare [[../claude-code-skills-stack/_index|claude-code-skills-stack]] and [[../google-antigravity-skills/_index|google-antigravity-skills]] — three vendors, one spec).

## Verdict

**CONFIRMED**, and worth citing as the strongest evidence in this whole talk that "guardrails" have genuinely become an industry-wide, spec-level convention rather than vendor marketing. See [[claims-scorecard]] (claim C3).

## Why this matters for hireui

Every skills-based pattern already banked from this corpus (`.claude/skills/` folders, `SKILL.md` frontmatter) is portable to a shared open spec, not a Claude-only bet. If hireui or a teammate ever needs a Copilot-side agent to read the same skill definitions, the folder-and-frontmatter shape should transfer largely unchanged.

## Update (2026-07-14) — a fourth vendor that converged independently, not on the spec

[[../pydantic-ai-2/progressive-disclosure-and-skills-lineage|pydantic-ai-2]] adds a useful contrast point: Pydantic AI's v2.0 "capability" primitive supports the same progressive-disclosure UX (brief description loads first, full instructions load on demand) and its own docs even cite Anthropic's Agent Skills by name as the inspiration — but it does **not** implement the `agentskills.io` spec itself (a third-party adapter, `pydantic-ai-skills`, exists specifically to bridge the gap). So the fuller picture is: **GitHub + Claude share one literal spec; Pydantic AI independently converged on the same UX pattern without adopting the spec.** Same convergence signal, two different depths of convergence.

## Update (2026-07-14, session 3) — OpenAI Codex CLI confirmed as a third vendor on the literal spec

[[../teach-skill-ai-tutor/codex-skills-feature-verified|teach-skill-ai-tutor]] adds a genuine third data point, and unlike Pydantic AI (independent convergence on the *pattern*, not the spec — see the update above), **Codex CLI is confirmed on the literal `agentskills.io` spec itself**: same `SKILL.md` + YAML-frontmatter folder shape, shipped 2025-12-19, and OpenAI's own docs state plainly that "the same SKILL.md files that work in Claude Code and OpenClaw work in Codex CLI." One wrinkle: Codex's *canonical* discovery path is the shared cross-vendor `$HOME/.agents/skills` location, not a Codex-specific folder — reinforcing that `.agents/skills` is emerging as the common convergence point across vendors, alongside each vendor's own historical path (`.claude/skills/`, `.github/skills/`).

## See also

[[_index]] · [[agents-md-guardrail]] · [[custom-agents-vs-subagents]] · [[claims-scorecard]]
