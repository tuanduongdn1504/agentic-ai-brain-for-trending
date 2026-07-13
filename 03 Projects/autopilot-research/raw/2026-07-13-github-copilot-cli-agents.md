---
source: yt-dlp-only (path 5, manual main-loop ingest, NO NotebookLM)
topic: github-copilot-cli-agents
generated: 2026-07-13T00:00:00-00:00
video_id: GdvKNwMcfd0
channel: AI Engineer (@aiDotEngineer)
speaker: Chris Noring, Microsoft
uploaded: 2026-07-11
duration: 23:05
views_at_ingest: ~8487
---

# From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft

**Video:** https://www.youtube.com/watch?v=GdvKNwMcfd0
**Channel:** AI Engineer (539K subs at ingest) — the AI Engineer World's Fair / ai.engineer conference channel (@aiDotEngineer)
**Speaker:** Chris Noring (GitHub: `softchris`), Cloud Developer Advocate at Microsoft
**Uploaded:** 2026-07-11 · Duration 23:05 · ~8,487 views / Science & Technology at ingest

## Description (as published)

For decades, developers have been valued primarily for how much code they could write and how quickly they could write it. That model no longer scales. As AI becomes a first-class collaborator, the bottleneck is no longer syntax or implementation speed—it's clarity of intent, architectural thinking, and the ability to coordinate work across many autonomous contributors.

Today's challenge is not "How do I write this code?" but "How do I ensure this system is built correctly, consistently, and to company standards—across dozens of moving parts?" Without structure, AI-assisted development risks fragmentation: inconsistent patterns, duplicated logic, and solutions that technically work but fail architectural, security, or organizational expectations.

This talk introduces a new mental model for modern development: the developer as planner, system designer, and orchestrator of agents. Using GitHub Copilot, GitHub Copilot CLI, and custom Copilot agents driven by agents.md, we'll explore how developers can decompose large problems, delegate implementation to specialized AI agents, and encode standards, constraints, and intent directly into the workflow.

## Ingest method

Captions fetched via `yt-dlp --skip-download --write-auto-sub --sub-lang en --sub-format vtt` (EN auto-captions only). Rolling-caption redundancy + word-level `<c>` karaoke tags stripped via `sed` + `uniq` → 656-line / 4,272-word clean transcript, **read in full in the main loop**. No NotebookLM used.

## Transcript (cleaned, full)

> Full transcript archived at ingest time; see wiki articles in `../wiki/github-copilot-cli-agents/` for the compiled, verified, cross-linked treatment. Raw transcript available in the session scratchpad at ingest; key passages are quoted directly in the wiki articles with their surrounding context.

### Structural summary of the talk (3 acts, as the speaker frames it)

1. **CLI as new entry point** — instead of opening the editor first, start in GitHub Copilot CLI (or Claude Code); use it for issue/PR triage, first-draft generation, "build me an app" prompts.
2. **Editor as "control board"** — once agents are running across CLI/editor/GitHub, the editor becomes a dashboard for watching streams, not where code gets typed line-by-line. This is where three "guardrails" get introduced:
   - **Guardrail 1 — AGENTS.md**: bare-minimum, high-level repo intent/architecture/constraints doc.
   - **Guardrail 2 — Skills**: repeatable, folder-based, constrained "recipes" an agent invokes — explicitly compared to Claude's `.claude/skills/` + `SKILL.md`.
   - **Guardrail 3 — Custom agents**: persona + tool-allowlist + reasoning/orchestration, one level above skills, can use MCP servers, stored at `.github/agents/*.agent.md`.
3. **Scale/delegate** — GitHub Copilot CLI's `/delegate` command (sends session to GitHub, creates a background coding-agent job, opens a draft PR) and the GitHub issue "assign to agent" UI path (same underlying "Copilot coding agent," different entry point). Human-in-the-loop = the draft-PR review/merge gate. Framed as "10x/20x/100x developer," not developer replacement.

Closing line: "the guardrails I'm introducing today... is about scaling you now that we have AI, not replacing you."
