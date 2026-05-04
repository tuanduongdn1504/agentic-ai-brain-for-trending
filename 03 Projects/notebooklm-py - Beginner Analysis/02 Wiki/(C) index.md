# (C) Index — notebooklm-py Wiki

> Catalog wiki cho `teng-lin/notebooklm-py`.

## 🎯 Project status (2026-04-18)

- ✅ Phase 0: Pre-flight — PASSED (API probe, 26MB manageable, Tier 4 "bridge" classification)
- ✅ Phase 1: Setup — COMPLETE
- ✅ Phase 2: Source ingestion — COMPLETE (3 summaries)
- ✅ Phase 3: Entity pages — COMPLETE (4 entity pages)
- ✅ Phase 4a: Beginner published guide — COMPLETE
- ✅ Phase 4b: **Tier 4 proposal + cross-tier positioning** — COMPLETE (4-tier taxonomy v7)
- ✅ Phase 5: Iteration log v7 — COMPLETE
- ✅ Phase 6: Vault file updates — COMPLETE

**🎉 v7 SHIPPED.** 7th auto-execution. First Tier 4 "Agent-as-bridge" established. 4-tier taxonomy defensible.

**Repo:** teng-lin/notebooklm-py
- **Description:** "Unofficial Python API and agentic skill for Google NotebookLM. Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents like Claude Code, Codex, and OpenClaw."
- **Stats:** 11,043 stars, 1,466 forks, MIT license, 26MB size, Python, pushed 2026-04-17
- **Version:** v0.3.4 (Mar 12, 2026), 1-2 week release cadence
- **Author:** `teng-lin` (solo, not a fork)
- **Routine:** `05 Skills/llm-wiki-routine.md` v1 — 7th auto-execution, second different-domain
- **Domain:** **Tier 4 candidate (agent-as-bridge)** — NEW tier proposed by v7, different from Tier 1/2/3

## Sources (planned)

| Page | Summary | Status |
|------|---------|--------|
| [[(C) README summary]] | Main repo README — positioning, installation, 3 integration approaches (Python/CLI/Skill), web-UI-exclusive features, auth/config | ✅ |
| [[(C) SKILL summary]] | SKILL.md — invocation patterns, core operations matrix, workflow patterns, Claude Code integration examples, autonomy rules, output formats, error handling | ✅ |
| [[(C) Architecture + Release cluster summary]] | CLAUDE.md (4-layer architecture) + CHANGELOG (release cadence + v0.3.x maturity) + AGENTS.md (agent guidance rules) | ✅ |

## Concepts (planned từ Phase 0 probe)

- **Unofficial API** — wraps Google NotebookLM undocumented RPC endpoints
- **3 integration approaches** — Python API (async), CLI, agent Skill
- **4-layer architecture** — CLI → Client → Core → RPC
- **Namespaced Python API** — `client.notebooks.*`, `client.sources.*`, `client.artifacts.*`, `client.chat.*`, `client.sharing.*`
- **Web-UI-exclusive features** — batch downloads, PPTX export, mind-map JSON, individual slide revision
- **Artifact types** — podcast/audio, video, quiz, flashcards, slide-deck, mind-map, infographic, data-table, report
- **Content generation** — 4 audio formats, 7 video styles, 4 report formats
- **Language support** — 80+ languages via `language list/set/get`
- **Profile management** — multi-account, multi-agent isolation
- **Autonomy rules** — automatic vs confirmation-required operations
- **Agent skill bundle** — `notebooklm skill install` populates `~/.claude/skills/notebooklm`

## Entities (planned)

| Page | Type | Sources | Status |
|------|------|---------|--------|
| [[(C) CLI Surface]] | Building block | README CLI section + SKILL.md core operations | ✅ |
| [[(C) Python API Architecture]] | Architecture concept | README Python API + CLAUDE.md 4-layer design | ✅ |
| [[(C) Skill Integration (Claude Code + Codex + OpenClaw)]] | Integration concept | SKILL.md invocation + agent integration | ✅ |
| [[(C) Web-UI-Exclusive Capabilities]] | Value prop concept | README + SKILL key capabilities section | ✅ |

## Roadmaps / Published

- ✅ [[../03 Published/(C) notebooklm-py - Huong dan cho nguoi moi]] — beginner guide bilingual
- ✅ [[../03 Published/(C) Agent framework taxonomy v3 - 4 tier with bridge]] — Tier 4 bridge proposal + cross-tier positioning

## Cross-project siblings

- `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) index.md` (Tier 1)
- `../../Superpowers - Beginner Analysis/02 Wiki/(C) index.md` (Tier 1)
- `../../gstack - Beginner Analysis/02 Wiki/(C) index.md` (Tier 1)
- `../../get-shit-done - Beginner Analysis/02 Wiki/(C) index.md` (Tier 1)
- `../../goclaw - Beginner Analysis/02 Wiki/(C) index.md` (Tier 2)
- `../../ai-agents-for-beginners - Beginner Analysis/02 Wiki/(C) index.md` (Tier 3)

## Logs

- [[(C) log]]
