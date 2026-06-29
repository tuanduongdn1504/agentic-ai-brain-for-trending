# Original: Anthropic Prompt-Engineering Best Practices

*Anthropic's canonical prompt-engineering techniques that form the foundation for Claude skill development and the official Prompt Improver tool.*

## Source

**Primary:**
- Anthropic Official Docs: [Prompt Engineering Best Practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Anthropic Official Docs: [Prompting Tools](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-tools)
- Ben AI YouTube: [8 Claude Skills I Can't Live Without](https://www.youtube.com/watch?v=bXnRA3pJavE) (2026-04-18)

**Secondary:**
- Anthropic Official Docs: [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- Anthropic Official Docs: [Agent Skills Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

## Key Takeaways

### The 7 Canonical Techniques (Official, in Order)

1. **Be clear & direct** — Specify output format, constraints, and expectations. Use the "colleague test": would a peer be confused by this prompt?

2. **Add context & motivation** — Explain WHY behavior matters, not just WHAT to do. Enables Claude to generalize beyond examples and reason about intent.

3. **Use examples (multishot prompting)** — Provide 3–5 well-structured, diverse examples in `<example>` or `<examples>` XML tags. Cover edge cases. Critical for accuracy on complex tasks.

4. **Structure prompts with XML tags** — Use `<instructions>`, `<context>`, `<input>`, `<documents>`, `<document_content>`, `<source>` tags. Especially powerful for multi-document and long-context tasks.

5. **Give Claude a role** — Single sentence in system prompt (e.g., "You are a coding assistant specializing in Python"). Anchors behavior without overhead.

6. **Long-context prompting** — Place longform data ABOVE queries (~30% quality uplift). Ground responses in direct quotes from documents, not paraphrases.

7. **Model self-knowledge** — Explicitly state Claude version in system prompt ("The assistant is Claude 3.5 Sonnet, created by Anthropic"). Enables version-specific reasoning.

### First-Party Prompting Tools (Claude Console)

- **Prompt Generator** — Creates high-quality prompt templates from blank-page scenarios. Zero setup.

- **Prompt Improver** — Anthropic's official 4-step enhancement tool: example-identification → structured-template-creation → chain-of-thought-refinement → example-enhancement. Best for complex, accuracy-critical tasks. ⚠️ Ben AI's "Prompt Master" skill (if it exists) is likely a rebranding or independent third-party variant; Anthropic's official tool is "Prompt Improver."

- **Prompt Templates & Variables** — Use `{{placeholder}}` notation for reusable prompt structure. Enables consistency, efficiency, testability, and version control.

### Beyond the Core 7: Advanced Techniques

- **Thinking & Adaptive Thinking** — Leverage Claude's extended-thinking capability for complex reasoning (Opus 4.6+).
- **Tool use & parallel tool calling** — Optimize for deterministic operations and concurrent execution.
- **Agentic systems** — Multi-window workflows, state-management (JSON/git-based), research-gathering, subagent-orchestration.
- **Prompt chaining** — Break multi-step tasks into sequential prompts with state-passing between steps.
- **Structured Outputs** — JSON schema enforcement; modern replacement for deprecated prefilled responses (Claude 4.6+).

### Agent Skills Integration

- **Progressive disclosure** — [[claude-skills/overview|Agent Skills]] use three-level loading: metadata preloaded (~100 tokens), full SKILL.md on trigger (<5K tokens), bundled files/scripts on-demand (zero context cost until accessed).

- **Anthropic first-party skills** — Official pre-built skills: PowerPoint, Excel, Word, PDF creation/editing. Invoked contextually without explicit user invocation.

- **MCP Builder is a real Anthropic skill** — Ben's #8 maps to the official `mcp-builder` skill in [anthropics/skills](https://github.com/anthropics/skills) (verified 2026-06-20). See [[claude-skills/original-mcp-builder-and-mcp]].

## Cross-References

- [[claude-skills/overview]]
- [[claude-skills/the-eight-meta-skills]]
- [[claude-skills/original-anthropic-agent-skills]]
- [[claude-skills/original-matt-pocock-grill-me]]
- [[prompt-evaluation/_index]]
- [[harness-engineering/_index]]
- [[multi-agent-orchestration/_index]]
- [[ai-operating-system/_index]]

## Verification Status

**Anthropic Official (verified from platform.claude.com/docs, 2026-06-20):**
- All 7 canonical techniques documented and in canonical order.
- Prompt Improver, Generator, Templates & Variables confirmed as first-party tools.
- Agent Skills progressive-disclosure model verified.

**Third-Party Claims (flagged):**
- ⚠️ "Prompt Master" — Anthropic's official tool is "Prompt Improver," not "Prompt Master." Ben AI may have rebranded or built independent third-party skill.
- ✅ "MCP Builder" is a real built-in Anthropic skill — confirmed as `mcp-builder` in github.com/anthropics/skills (verified 2026-06-20).
- ⚠️ "91,000 skills" in skills.sh ecosystem — Outdated. Current: ~788K+ installs (2026-06-20); actual unique-skill count unclear but significantly higher than 91K.

---

**Operator note:** For [[ai-operating-system/_index]] and hireui Goal #2 deployment, master the 7 canonical techniques + Prompt Improver before attempting evaluation-harness or multi-agent-orchestration pilots. Foundational layer.
