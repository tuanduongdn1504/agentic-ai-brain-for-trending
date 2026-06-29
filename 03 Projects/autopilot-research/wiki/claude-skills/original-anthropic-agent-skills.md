# Original Anthropic Agent Skills (the foundation)

*Deep dive into the architecture, format, and best practices underlying all agentic extensibility in Claude.*

## Overview

Agent Skills are Anthropic's official framework for extending Claude's capabilities through modular, reusable, filesystem-based procedures. Unlike Projects (static always-loaded context) or MCP (external service connectors), Skills follow a simple two-part structure: SKILL.md metadata (YAML frontmatter + instructions) plus optional bundled scripts, references, and assets. The framework uses **progressive disclosure**—load only what's needed—to keep context overhead minimal while supporting unbounded complexity. Skills run identically across Claude.ai, Claude Code, Claude API, Agent SDK, AWS Claude Platform, and 40+ third-party agents (Cursor, GitHub Copilot, Gemini CLI, OpenHands, Letta, Kiro, Databricks Genie, and others), making them a de facto open standard.

## Source

- Anthropic engineering blog: [Equipping Agents for the Real World with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- Anthropic official documentation: [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), [best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- GitHub: [anthropics/skills](https://github.com/anthropics/skills) — open-source reference implementations
- Registry: [agentskills.io](https://agentskills.io) client showcase (40+ platforms); [skills.sh](https://skills.sh) ecosystem (788K+ installs, 1000+ listed skills as of June 2026)
- Support documentation: [What are skills](https://support.claude.com/en/articles/12512176-what-are-skills), [Creating custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills), [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)

## Key Takeaways

- **Two-part structure**: SKILL.md (required YAML frontmatter `name` + `description` + Markdown body) + optional bundled files (scripts/, references/, assets/). Requires code execution enabled; available on Free, Pro, Max, Team, Enterprise plans.

- **Progressive disclosure by design**: Level 1 loads only name+description in system prompts at startup (~100 tokens/skill); Level 2 loads full SKILL.md when Claude determines task-relevance (<5K tokens); Level 3+ loads bundled files on-demand (zero context cost until accessed). Prevents context explosion while supporting complex skills.

- **Cross-platform standard**: Adopted by 40+ agents (Anthropic's own platforms + Cursor, GitHub Copilot, Gemini CLI, OpenHands, Letta, Databricks Genie, Snowflake Cortex, Kiro, VS Code Copilot, OpenCode, Goose, Mux, Workshop, and others). Single skill authored once, runs everywhere; no per-platform reimplementation.

- **Triggering mechanism**: Claude reads SKILL.md description and decides relevance based on task match. Descriptions must be specific and outcome-focused for reliable triggering. Keep focused on single workflow; include examples and expected outputs for context.

- **Optional bundled scripts**: Python/JavaScript supported for deterministic operations (calculations, transformations, deterministic workflows). All dependencies must be pre-installed in the container for API Skills; scripts referenced from SKILL.md are executed via bash tools when needed.

- **Anthropic's built-in skills**: Official skills for Excel (xlsx), Word (docx), PowerPoint (pptx), PDF creation; Claude invokes contextually without explicit user activation. The same repo also publishes `mcp-builder`, `skill-creator`, `frontend-design`, and `claude-api` (verified 2026-06-20) — so Ben's #8 MCP Builder and the "skill creator" he mentions are both genuine Anthropic skills.

- **Distinguishing Skills from related patterns**: Skills ≠ Projects (static, always-loaded context); ≠ MCP (external service connectors); ≠ Custom Instructions (broad personality vs task-specific workflows). Multiple skills can be used together automatically; however, skills cannot explicitly reference each other (no cross-skill imports).

## SKILL.md Format & Minimal Template

```yaml
---
name: your-skill-name
description: Clear description of what this does and when Claude should trigger it (max 1024 chars)
---

# Your Skill Name

## Quick Start
[Concise core instructions; 2-3 sentences on how Claude uses this skill]

## Examples
- **Input:** [Example task or query]
  **Output:** [What Claude produces]
- [2-3 more examples covering edge cases]

## Advanced Features
[Optional reference to bundled files: see FORMS.md for templates, API_REFERENCE.md for endpoint details, etc.]
```

Keep SKILL.md body <500 lines. For complex skills, split reference material into separate bundled files and reference them via relative links.

## Required Folder Structure

```
skill-name/
├── SKILL.md              (required: metadata + instructions)
├── scripts/              (optional: Python/JS deterministic operations)
│   └── process.py
├── references/           (optional: docs, templates, API specs)
│   ├── API_REFERENCE.md
│   └── FORMS.md
└── assets/               (optional: images, templates, style guides)
    └── brand-guide.json
```

Package as ZIP with skill folder as root. Upload via Claude.ai Settings > Skills, Claude Code, or API endpoints.

## Authoring Best Practices (Anthropic)

- **Stay focused**: One workflow per skill. Multi-purpose skills fail to trigger reliably.
- **Write specific descriptions**: Outcome-focused, not task-name-focused. ✓ "Turns messy brain-dumps into structured prompts per best practices" vs ✗ "prompt optimizer".
- **Include concrete examples**: 3-5 input/output pairs covering typical and edge-case usage.
- **Test incrementally**: Upload to sandbox project, try multiple prompts, review Claude's thinking, iterate description if needed.
- **Document expected outputs**: Include format examples (markdown, JSON, HTML, etc.) so Claude knows what structure to produce.
- **Avoid cross-skill dependencies**: Skills cannot import from each other; each must be self-contained.

## Cross-Platform Support & Distribution

Skills run identically across:
- **Anthropic-native**: Claude.ai, Claude Code, Claude API, Agent SDK, AWS Claude Platform, Microsoft Foundry
- **Third-party agents** (40+ verified at agentskills.io): Cursor, GitHub Copilot, VS Code Copilot, Gemini CLI, OpenHands, Letta, Databricks Genie, Snowflake Cortex, Kiro, OpenCode, Goose, Mux, Workshop, and others
- **Ecosystem distribution**: Upload to skills.sh (788K+ installs tracked; ~1000+ skills listed as of June 2026); install via `npx skills add <owner/repo>` or within Claude's Find Skills interface

## Skill Authoring vs Agent Skill Framework Extension

Skills are **end-user reusable capabilities**; they are distinct from:
- **Prompt templates** (static instruction sets; not discoverable, not shared)
- **Projects** (always-loaded context; static, not procedural)
- **MCP servers** (external service connectors; require network/auth setup)

Skills encode **procedural knowledge** (how-to methodologies, systematic workflows, decision frameworks) in a format Claude can discover, invoke, and chain automatically.

## Connection to [[claude-code-memory-systems/_index]]

Skills' progressive-disclosure model mirrors memory-system Level 2-3 layering (metadata preloaded, full content on-demand, bundled resources zero-cost until accessed). The framework assumes external knowledge (CLAUDE.md chapters, PATTERN_LIBRARY.md, second-brain workspace) auto-pulls into skill context. For [[ai-operating-system/_index]] / Karpathy LLM Wiki deployments, Skills are the **operator-defined workflow-automation layer** layered atop the knowledge base.

## Connection to [[multi-agent-orchestration/_index]]

Skills enable workflows authored in your vault (like those in `autopilot-research` topics) to become reusable first-class agent procedures. Workflows (structured interviewing, prompt optimization, fact-checking, decision analysis) chain together as **multi-step procedural agent workflows**. Skill chaining (one skill's output → next skill's input) builds agentic orchestration without explicit code.

## Operator-Facing Discipline

For hireui Goal #2 (deploy agents into recruitment SaaS):
- Skills package recruitment workflows (screening decision matrix, candidate-summary generation, interview note formatting per ATS templates) as reusable capabilities Claude agents invoke deterministically
- Custom skills wrap hireui's ATS/API (if no current connector exists) via MCP integration pattern (create MCP server from API docs → wrap as skill)
- Skills enforce [[claude-code-memory-systems/_index]] auto-pull: second-brain workspace (hireui's candidate database, ATS schema, compliance rules) auto-loads into skill context on trigger
- Decision frameworks skill directly applicable: candidate-screening matrix (alternative × evaluation-criteria) with structured analysis prevents rushed hiring decisions

Cross-platform + discipline notes:
- One SKILL.md runs identically across 40+ agent platforms — author once, no per-platform reimplementation.
- Skills encode concrete procedures (reference-based rigor), not vibe prompts.
- Third-party meta-skills collection exemplifies architectural role-separation between skill authoring harness and discovery/execution platforms

---

**Next action**: Audit the available meta-skills ecosystem against recruitment workflow needs. Prioritize decision-analysis frameworks (candidate screening) and content-quality tooling (compliance communications) as 2-week micro-pilots. Cross-reference [[claude-skills/original-matt-pocock-grill-me]] for structured-interviewing methodology foundations.
