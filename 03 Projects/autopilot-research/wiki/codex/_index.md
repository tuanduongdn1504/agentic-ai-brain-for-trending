# Codex — Long-Running Agentic Harness

> **Topic:** OpenAI Codex as a long-running, terminal-resident agentic harness — positioned in the May 2026 landscape as an alternative to and complement of Claude Code.
> **First compiled:** 2026-05-14 (autopilot overnight drain 2026-05-13)
> **Source bundle:** `../../raw/2026-05-13-codex-long-running-agentic-harness-alternative-to.md` (6 YouTube videos via NotebookLM)
> **NotebookLM ID:** `01707594-d36a-4a2f-b3f8-7fa9044528ba`
> **Maintained by:** Claude Code librarian per `../../CLAUDE.md`

---

## What this is

OpenAI **Codex** has, by May 2026, evolved into a long-running, terminal-resident coding agent that sits in the same category as Claude Code: an "agentic harness" that takes natural-language goals and turns them into multi-step shell, file-system, and git workflows [Source 1, Source 3]. The 6-video bundle here mixes deep dives on Codex itself (Keith AI, Riley Brown) with Claude-Code-centric material (Mosh, Teacher's Tech) and a hybrid "use both together" view (Jack Roberts, The AI Automators). The recurring framing: **don't pick one — compose them**, with Claude for building, Codex/GPT for adversarial review, and Gemini for long-context analysis [Source 6].

---

## Articles in this topic

| Article | What it covers |
|---|---|
| [[overview]] | What Codex is in May 2026, terminal/agentic-harness framing, how it compares to Claude Code, the long-running-agent positioning |
| [[core-patterns]] | Recurring techniques: project memory files (`agents.md`/`claude.md`), planning mode, git worktrees + parallelism, adversarial evaluation, sandbox/permission model |
| [[expert-disagreements]] | Codex-as-primary vs Claude-as-primary, multi-model vs single-model, vibe-coding vs real-engineering, context-window cynicism |
| [[practical-takeaways]] | 10 actionable rules for adopting Codex, composing it with Claude Code, and configuring memory, planning, voice, and adversarial review |
| [[gaps-and-followups]] | What the 6 sources don't cover — team-scale collaboration, enterprise IAM, observability, compliance, automated quality gates; 6 follow-up topics |

---

## Source citations (within this topic)

| Source # | Channel | Title | URL |
|---|---|---|---|
| 1 | Keith AI | Master OpenAI Codex in 26 minutes | https://www.youtube.com/watch?v=EwVs3O2Zm6I |
| 2 | The AI Automators | Anthropic Just Dropped the New Blueprint for Long-Running AI Agents | https://www.youtube.com/watch?v=9d5bzxVsocw |
| 3 | Riley Brown | Codex Full Course 2026: The NEW Best AI Coding Tool | https://www.youtube.com/watch?v=KXIdYEdOPys |
| 4 | Teacher's Tech | Claude Code: Build Your First AI Agent | https://www.youtube.com/watch?v=gHB4JFG9i3k |
| 5 | Programming with Mosh | Claude Code Tutorial - Build Apps 10x Faster with AI | https://www.youtube.com/watch?v=IuyVVtr1uhY |
| 6 | Jack Roberts | Claude Code just got 10X Better (Codex + Gemini) | https://www.youtube.com/watch?v=ETvz1qhQDXE |

> Source numbers above match the inline `[Source N]` citations within each article.

---

## Related topics

- [[../harness-engineering/_index]] — Lopopolo's harness-engineering discipline (Codex is OpenAI's flagship long-running harness; same category, different vendor)
- [[../claudekit/_index]] — Claude-Code-side framework comparison
- [[../workflow-ai-coding/_index]] — practitioner workflow context (Codex shares vocabulary: planning mode, memory files, parallelism)
- [[../claude-md-12-rules/_index]] — individual-scale behavioral contract (applies regardless of harness — Codex uses `agents.md` for the same role)
- [[../claude-code-hooks/_index]] — deterministic event-driven enforcement layer (Codex equivalent not covered in this bundle — see [[gaps-and-followups]])
- [[../autonomous-loops-human-in-the-loop/_index]] — long-running-agent oversight patterns (overlaps with Codex's "let it cook" workflow)
- [[external|Storm Bear: codex-plugin-cc v62 corpus entry]] — OpenAI publishing Apache-2.0 plugin FOR Claude Code (cross-vendor cooperation; complements this operator-side wiki — see `../../../codex-plugin-cc/` in vault if/when added)
