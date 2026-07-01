# Google Antigravity — Overview (platform, surfaces, and what the video teaches)

## Source

- **Video (entry point):** [UFmV7YsVqlM](https://www.youtube.com/watch?v=UFmV7YsVqlM) — "Google Antigravity 2.0: Cách tạo Skill AI, Rule Và Quản Lý Skill Từ A-Z" (Dũng - Chia Sẻ Công Nghệ, 2026-06-27, 22:39). Raw: `raw/2026-07-01-google-antigravity-skills-rules-dung-chiasecongnghe.md`.
- **Original resource (deep-dive target):** Google Antigravity itself — verified against official Google sources (see [[google-antigravity-skills/source-provenance]]).

---

## What Google Antigravity is

**Google Antigravity is Google's agent-first agentic development platform** — you operate at a task level and delegate planning, execution, and verification to autonomous agents rather than typing every edit yourself.

- **Launched:** public preview **November 2025** (18 Nov), alongside **Gemini 3**. Free.
- **"Antigravity 2.0":** a real, official milestone — a **standalone desktop application** for orchestrating multiple agents in parallel, announced around **Google I/O 2026 (May 2026)**. It is *distinct from* the original Antigravity IDE. (The video's title "Antigravity 2.0" is therefore accurate — see [[google-antigravity-skills/source-provenance]] for how this was verified after an initial mis-read.)
- **Who built it:** Google, with the ex-**Windsurf/Codeium** team. Precisely: in July 2025 Google struck a **~$2.4B non-exclusive licensing deal with Codeium** and hired CEO **Varun Mohan** + key staff (a "reverse acquihire") — **not** a company acquisition. Lineage is a VS Code-family editor (debated: fork of VS Code, or of Windsurf which is itself a VS Code fork).
- **Platforms:** macOS, Windows, and specific Linux distributions (desktop app; Linux via a `.tar.gz` bundle).

### The four surfaces (all share one "Antigravity Harness")

| Surface | What it is |
|---|---|
| **Antigravity 2.0** | Standalone desktop **orchestration hub** — run/manage many agents & tasks in parallel |
| **Antigravity IDE** | The original agentic IDE — in-editor agent + line-by-line code control |
| **Antigravity CLI** | Terminal interface, **built in Go** (not Python) — headless/high-velocity |
| **Antigravity SDK** | **Python** library for building custom agents programmatically |

All four **share the same authentication, context, skills, and rules** — so a `SKILL.md` or `AGENTS.md` written once applies across surfaces.

### Models (multi-model)

Antigravity is multi-model. As of **mid-2026** the model menu includes **Gemini 3.5 Flash** (the default agentic model), **Gemini 3.1 Pro**, **Claude Sonnet 4.5 / 4.6 (Thinking)**, **Claude Opus 4.6 (Thinking)**, and **GPT-OSS-120B**. (At the Nov-2025 launch the headline pairing was Gemini 3 Pro + Claude Sonnet 4.5 + GPT-OSS.) That Claude models run *inside Google's IDE* is why this topic matters to a Claude-Code-centric workflow — see [[google-antigravity-skills/anthropic-agent-skills-portability]].

---

## What the video actually teaches

The video is a **beginner-friendly, non-coder tutorial** (small Vietnamese channel) that uses one running example — **automating a monthly Excel sales report** — to teach two things: **Skills** and **Rules**.

Its framing metaphor: *stop re-explaining the same task to the AI every day. **Teach it once.*** The creator calls this **"cloning yourself"** — you spin up a copy that already knows your skills and procedures and works in your place. Concretely, it walks through:

1. **What a Skill is** (a folder + `SKILL.md`) and the **auto-discovery** mechanism → [[google-antigravity-skills/skills-system]]
2. **Workspace vs Global** scope (the "two houses" analogy) → [[google-antigravity-skills/workspace-vs-global]]
3. **Skill vs Rule** — the distinction people confuse most → [[google-antigravity-skills/rules-and-customization]]
4. **Two ways to build a skill** — by hand, or by working with the agent and asking it to capture the workflow → [[google-antigravity-skills/build-methods]]
5. A **live Excel demo** — analyze May revenue, save the workflow as a skill, add a **"never overwrite raw data"** rule, then one-shot the June report → [[google-antigravity-skills/video-summary]]

The single most useful *idea* in the video is the **Skill-vs-Rule split**: put reusable **capabilities** in skills, and cross-cutting **constraints** in one rule that every skill obeys. That maps cleanly onto Antigravity's real architecture (`SKILL.md` skills + `AGENTS.md`/`GEMINI.md` rules).

---

## Why this is relevant to a Claude-Code + LLM-Wiki workflow

- **Antigravity's Skills are literally the Anthropic "Agent Skills" open format** (`SKILL.md`) — the *same* format used in `.claude/skills/` and in this vault's project-local skills. Your existing skills are already Antigravity-compatible. → [[google-antigravity-skills/anthropic-agent-skills-portability]]
- **`AGENTS.md`** — Antigravity's cross-tool rules file — is a **Linux Foundation standard** read by Claude Code, Cursor, Kiro, and 28+ tools. It's a portable superset of your `CLAUDE.md`. → [[google-antigravity-skills/rules-and-customization]]
- So this topic isn't "learn a new tool" — it's "your harness (skills + rules) is more **portable** than you thought, and here's a **free, multi-model** second surface to run it on." The pilot menu builds on exactly that.

## Key Takeaways

- **Antigravity = Google's agent-first dev platform** (IDE + CLI + SDK + the 2.0 desktop hub), free public preview since Nov 2025, multi-model incl. Claude.
- **"Antigravity 2.0" is real** — a standalone multi-agent desktop app from Google I/O 2026, not just a creator's label.
- The video teaches **Skills (capabilities) + Rules (constraints)** via an Excel-report example — the "teach once, clone yourself" pattern.
- The load-bearing insight for *you*: Antigravity Skills = **Anthropic's open `SKILL.md` format**, and its rules file **`AGENTS.md`** is a **cross-tool standard** — your Claude Code harness is portable here.
