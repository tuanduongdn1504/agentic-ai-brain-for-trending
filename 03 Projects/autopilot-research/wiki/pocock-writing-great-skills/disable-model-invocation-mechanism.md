# The `disable-model-invocation` mechanism vs Anthropic's docs

The talk's whole Trigger axis rests on one frontmatter field. We verified it against **first-party Anthropic Claude Code docs** and the **agentskills.io open standard**. Result: **the talk is verbatim-correct**, with one nuance the talk doesn't mention.

## Confirmed: it's a real, official Claude Code field

From `code.claude.com/docs/en/skills` (Anthropic's own docs), the frontmatter reference lists `disable-model-invocation` with this behaviour table:

| Frontmatter | You can invoke | Claude can invoke | When loaded into context |
|---|---|---|---|
| *(default)* | Yes | Yes | Name + description in context; full skill loads when invoked |
| **`disable-model-invocation: true`** | **Yes** | **No** | **Description NOT in context; full skill loads when you invoke** |

- The docs: *"Set to `true` to prevent Claude from automatically loading this skill. Use for workflows you want to trigger manually with `/name`."* And: *"Hide individual skills by adding `disable-model-invocation: true`… This removes the skill from Claude's context entirely."*
- This is **exactly** the talk's mechanism: user-invoked = *"strips the description from the agent's reach… zero context load"*; model-invoked = *"the description sits in the window every turn."*
- The docs also confirm the context-load claim generally: *"Claude loads this metadata at startup and includes it in the system prompt… Until a Skill is triggered, only its name and description occupy context."* → i.e. **descriptions are always in context; bodies are lazy-loaded** — so Matt's "100 model-invoked skills = 100 descriptions in context every turn" is **correct** (a verify agent wrongly claimed descriptions were lazy-loaded — see [[pocock-writing-great-skills/caveats-and-corrections]]).

## The nuance: it's a Claude Code *extension*, not part of the portable standard

- Claude Code's docs state plainly: *"Claude Code skills follow the [Agent Skills] open standard (agentskills.io)… Claude Code **extends the standard** with additional features like **invocation control**, subagent execution, and dynamic context injection."*
- The **agentskills.io open standard itself** documents only **6 frontmatter fields**: `name` (required), `description` (required), `license`, `compatibility`, `metadata`, `allowed-tools`. **`disable-model-invocation` is not in the portable spec.**
- So the precise truth:
  - ✅ `disable-model-invocation` is **real and officially documented** — *within Claude Code*.
  - ⚠️ It is a **Claude-Code-specific extension**, **not** cross-tool-portable. A skill relying on it is not guaranteed to behave the same under another `agentskills.io`-compliant runtime (GitHub Copilot CLI, Codex CLI, etc.).
- Matt's talk presents user/model-invocation as a general property of "skills" without flagging that the *field* is Claude-Code-only. Not misleading (his repo targets Claude Code), but worth knowing for portability.

## Corpus tie-in: the agentskills.io thread

This is the sharpest data point yet in the corpus' running `agentskills.io` investigation:

- [[github-copilot-cli-agents/agent-skills-shared-standard]] — GitHub "Agent Skills" and Claude Agent Skills = the *same* open spec (agentskills.io).
- [[teach-skill-ai-tutor/codex-skills-feature-verified]] — OpenAI Codex CLI = a *third vendor* on the same spec.
- [[pydantic-ai-2/progressive-disclosure-and-skills-lineage]] — Pydantic AI converged on the same *UX* without implementing the spec.
- **This topic adds the layer picture:** the open standard is a **6-field core**, and each vendor adds **extensions** on top (Claude Code: invocation-control + subagent-execution + dynamic-context). The portable contract is smaller than any single vendor's skill surface.

## Related field: `user-invocable`

- The docs mention a separate `user-invocable` field that "only controls menu visibility, not Skill-tool access." Matt uses `disable-model-invocation` (the one that actually removes the description from context), not `user-invocable`. The two are distinct; `disable-model-invocation` is the load-bearing one for the talk's argument.
