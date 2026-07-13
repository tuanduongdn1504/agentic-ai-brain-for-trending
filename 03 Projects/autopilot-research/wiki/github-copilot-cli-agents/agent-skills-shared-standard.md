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

## See also
[[_index]] · [[agents-md-guardrail]] · [[custom-agents-vs-subagents]] · [[claims-scorecard]]
