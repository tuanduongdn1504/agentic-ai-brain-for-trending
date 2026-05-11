# Entity: Multi-platform breadth — 30+ AI tools (corpus-broadest)

> Pattern relevance: **Pattern #18 Layer 1 universal-protocol consumer STRONGEST evidence to date** / Pattern #2 distribution-evolution

## 1. Headline observation

OpenSpec generates skill/command files for **30+ AI coding assistants** — corpus-broadest multi-platform-by-design surface.

## 2. Tool enumeration (30 listed in docs/supported-tools.md)

| # | Tool | Type |
|---|---|---|
| 1 | Amazon Q Developer | IDE/CLI assistant |
| 2 | Antigravity | Coding assistant |
| 3 | Auggie | Coding assistant |
| 4 | IBM Bob Shell | Shell assistant |
| 5 | **Claude Code** | Anthropic CLI |
| 6 | Cline | VS Code agent |
| 7 | CodeBuddy | Coding assistant |
| 8 | Codex | OpenAI assistant |
| 9 | ForgeCode | Coding assistant |
| 10 | Continue | VS Code/JetBrains agent |
| 11 | CoStrict | Coding assistant |
| 12 | Crush | Coding assistant |
| 13 | Cursor | Standalone IDE |
| 14 | Factory Droid | Coding assistant |
| 15 | Gemini CLI | Google CLI |
| 16 | GitHub Copilot | Microsoft IDE assistant |
| 17 | iFlow | Coding assistant |
| 18 | Junie | JetBrains AI |
| 19 | Kilo Code | Coding assistant |
| 20 | Kimi CLI | Moonshot CLI |
| 21 | **Kiro** | AWS IDE (cited as anti-pattern foil) |
| 22 | Lingma | Alibaba assistant |
| 23 | OpenCode | Open-source agent |
| 24 | Pi | Coding assistant |
| 25 | Qoder | Coding assistant |
| 26 | Qwen Code | Alibaba CLI |
| 27 | RooCode | Coding assistant |
| 28 | Trae | Bytedance IDE |
| 29 | Windsurf | Codeium IDE |

(README claims "20+" / "25+"; docs list 30+. Q9 in OPEN-QUESTIONS.)

## 3. Comparison vs prior corpus multi-platform holders

| Wiki | Subject | Multi-platform breadth | OpenSpec advance |
|---|---|---|---|
| v56 n8n | n8n.io workflow automation | 16 native LLM providers (no LiteLLM) | OpenSpec ~2× more tools |
| v57 mattpocock/skills | Matt Pocock skill bundle | ~8 platforms ("any model" claim) | OpenSpec ~4× more tools |
| v51 agent-skills-of-vercel | Vercel AI Vibrant skills | 24 vendor skills | OpenSpec slightly more, different mechanism |
| v50 awesome-claude-skills | Aggregator skill collection | Claude-only (single-tool) | OpenSpec ~30× more tools |

**Verdict:** OpenSpec sets corpus-record for multi-platform-by-design at T1.

## 4. Integration mechanism (corpus-first cross-tool-skill-format-translator)

OpenSpec generates skill/command files in 2 deployment modes per tool:

**Mode 1: Skills installation**
- File pattern: `openspec-*/SKILL.md`
- Tool-specific directories: `.claude/skills/`, `.cursor/skills/`, etc.

**Mode 2: Commands installation**
- File formats vary per tool: markdown / TOML / prompt format
- Tool-specific command/workflow directories

**Per-tool format translation** = corpus-first observable. Most prior multi-platform corpus subjects (n8n, mattpocock) use single deployment-format for all targets; OpenSpec translates per target.

## 5. Pattern #18 Layer 1 universal-protocol consumer evidence

OpenSpec is the corpus-first explicit demonstration of:
- **N tools = 30+** (corpus-broadest at single subject)
- **Per-tool format translation** (not single-format-for-all)
- **2 deployment modes** (skills installation + commands installation)

Prior Pattern #18 Layer 1 evidence: MCP universal-protocol (n8n v56 bidirectional; mattpocock v57 plugin-manifest) + AGENTS.md cross-tool standard.

OpenSpec extends Layer 1 evidence: explicit N tools breadth + per-tool format translation. **Strengthens Pattern #18 at strongest-data-point level to date.**

## 6. Counter-evidence

OpenSpec's 30+ tool count creates risk of:
- Tool-format-drift breakage (any of 30 tool format changes break OpenSpec generator)
- Maintenance burden disproportionate to user-facing surface

Pattern #66 OBSERVATION-TRACK supply-chain awareness: 30+ tool dependency = 30+ format-spec maintenance commitments. Fission-AI org "no public members" + 2-repo small-org → maintenance scaling concern observational only.

## 7. Storm Bear relevance

- **Direct deployment:** Storm Bear vault uses Claude Code primarily (Tool #5); OpenSpec generates `.claude/skills/openspec-*/SKILL.md` automatically on `openspec init`
- **Multi-tool team scenario:** if Storm Bear's team uses Cursor + Claude Code + Gemini CLI (3 tools), OpenSpec single install generates 3-tool-coverage; manual setup would require 3 separate skill-collection installs
- **Tool-format-translator pattern adoption:** vault could pilot per-tool format translation for `brain-setup-v2.md` skill at v60+ if cross-team adoption emerges

## 8. Cross-references

- **Pattern #18** in `_patterns/02b-confirmed-patterns-v42-plus.md` — Layer 1 universal-protocol consumer
- **v56 n8n** — prior multi-platform record holder; OpenSpec surpasses
- **v57 mattpocock/skills** — plugin-manifest aggregation precedent
- **v50 awesome-claude-skills + v51 agent-skills-of-vercel** — T1 skills-collection precedents (different mechanism)
