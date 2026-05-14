# Claude Code Clones — Alternative Agent CLIs

> **Topic:** Open-source forks/clones replicating Claude Code's design (CLI UX, slash commands, hooks, MCP) — the May 2026 landscape as seen through one practitioner-video bundle
> **First compiled:** 2026-05-14 (autopilot overnight drain 2026-05-13)
> **Source bundle:** `../../raw/2026-05-13-open-source-claude-design-clones-alternative-agent.md` (6 YouTube videos via NotebookLM)
> **NotebookLM ID:** `5155a280-86ce-49ce-8328-d4b75c0119ce`
> **Maintained by:** Claude Code librarian per `../../CLAUDE.md`

---

## What this is

A landscape note on the small but growing class of **third-party agent CLIs that replicate Claude Code's design** — the terminal-based, project-rooted, slash-command-driven agent UX that Anthropic shipped — built atop either the Anthropic Agent SDK, a leaked Claude Code source map, or independent re-implementations of the same pattern.

The bundle is candid about the messy reality: only a handful of clones are named (**OpenClaw, Hermes, OpenCode, Aider**), the legitimacy debate is unresolved, and the most influential video (Mark Kashef) **abandons clones entirely** in favour of the Agent SDK bridge. This wiki preserves both the named clones and the practitioner verdict.

---

## Articles in this topic

| Article | What it covers |
|---|---|
| [[overview]] | The four named clones (OpenClaw, Hermes, OpenCode, Aider), what "Claude design" means in practice, why the landscape is small as of May 2026 |
| [[core-patterns]] | Recurring techniques across clones — terminal-first UX, dynamic prompt sandwich, bash-tool primitive, hive-mind memory, Agent-SDK-as-bridge |
| [[expert-disagreements]] | Whether clones are "obsolete" (Fireship), "great for vibe coding" (Alex Finn), or actively avoided (Mark Kashef who abandoned OpenClaw) |
| [[practical-takeaways]] | 7 actionable rules — when to pick a clone, when to stay on Claude Code, when to bridge via Agent SDK instead |
| [[gaps-and-followups]] | What the sources don't cover — license analysis, business-model risk, copyright / IP, multi-tenant scaling, model-routing implications |

---

## Source citations (within this topic)

| Source # | Channel | Title | URL |
|---|---|---|---|
| 1 | Mark Kashef | I Replaced OpenClaw and Hermes With This Claude Code Setup | https://www.youtube.com/watch?v=rVzGu5OYYS0 |
| 2 | Fireship | Tragic mistake... Anthropic leaks Claude's source code | https://www.youtube.com/watch?v=mBHRPeg8zPU |
| 3 | Caleb Writes Code | Claude Code Debacle: OpenCode, AI Coding | https://www.youtube.com/watch?v=LOjwfOf39mg |
| 4 | Mark Kashef | I Replaced OpenClaw With Claude Code in One Day | https://www.youtube.com/watch?v=9Svv-n11Ysk |
| 5 | Hasan Aboul Hasan | Claude Code Is Now 100% Free - Here's How | https://www.youtube.com/watch?v=t0Mesp118l4 |
| 6 | Alex Finn | Claude Code for Desktop is the BEST way to build apps with AI EVER (full tutorial) | https://www.youtube.com/watch?v=pHr1O_Af5NA |

> Source numbers above match the inline `[Source N]` citations within each article.

---

## Source-signal caveat

The bundle is **only partially on-topic**. Most of the videos focus on Claude Code workflow / personal automation rather than deep clone analysis. The richest clone-specific signal comes from [Source 1, Source 2, Source 4] — Mark Kashef's two videos plus Fireship's leak coverage. [Source 3, Source 5, Source 6] mention clones only in passing. See [[gaps-and-followups]] for what this implies.

---

## Related topics

- [[../claudekit/_index]] — ClaudeKit is a Claude Code **augmentation** framework (contrast: clones replicate Claude Code itself, claudekit extends it)
- [[../claude-code-hooks/_index]] — hooks are a Claude-Code-specific primitive that clones may or may not replicate
- [[../harness-engineering/_index]] — Lopopolo's harness-engineering discipline applies regardless of which CLI you pick
- [[../workflow-ai-coding/_index]] — practitioner workflow context; some of the same speakers
- [[../10x-claude-code/_index]] — tactical Claude Code tips; clones inherit much of this surface
- [[external|Storm Bear: Pattern Library T4 archetype]] — corpus entries v60 free-claude-code (api-protocol-translation-proxy) + v61 cc-sdd (SDD methodology framework) + v62 codex-plugin-cc (cross-vendor cooperation) map to this topic; see `../../../../CLAUDE.md` and `../../../../PATTERN_LIBRARY.md` in the vault root
