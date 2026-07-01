# Portability: Antigravity Skills = Anthropic Agent Skills + AGENTS.md

> **This is the headline finding for a Claude-Code-centric workflow.** Antigravity did not invent its own skill format — it **adopted Anthropic's open "Agent Skills" `SKILL.md` standard**, and it reads the **cross-tool `AGENTS.md`** rules standard. Your existing harness is more portable than you thought.

## Source

Anthropic's Agent Skills publication + `agentskills.io/specification` + Google's Antigravity skills codelab (which explicitly credits Anthropic) + the Linux Foundation Agentic AI Foundation. Verified in [[google-antigravity-skills/source-provenance]].

---

## Two open standards, two vendors, one format

| Layer | Standard | Origin | Who reads it |
|---|---|---|---|
| **Reusable skill** | **`SKILL.md`** (Agent Skills) | **Anthropic**, published as an open format **Dec 18 2025**; spec at `agentskills.io/specification` | Claude Code, **Antigravity**, Cursor, Windsurf, … |
| **Project rules** | **`AGENTS.md`** | Multi-vendor (OpenAI/Amp/Google/Cursor/Factory, Aug 2025) → **Linux Foundation** Agentic AI Foundation (Dec 2025) | **Antigravity**, Claude Code, Cursor, Kiro, 28+ tools |

So the two files this vault already lives on — `SKILL.md` skills and `CLAUDE.md`-style rules — both have **open, cross-vendor successors** that Antigravity speaks natively. Google **adopting Anthropic's published standard** (not convergent design — it's explicit adoption, announced at Google I/O 2026) is itself a notable cross-vendor cooperation signal.

## What's identical across Antigravity and Claude Code

- **The skill file:** `SKILL.md` = YAML frontmatter (`description` required, `name` optional) + Markdown body. Same in both.
- **Optional subfolders:** `scripts/` (Python/Bash/Node), `resources/`, `assets/`. Same.
- **Progressive disclosure:** the agent sees name+description first, loads the full skill only when your request matches the description. Same model in both.

## What differs (the portability caveats)

Moving a skill/rule between tools is **high-compatibility but not zero-effort**:

| Thing | Antigravity | Claude Code |
|---|---|---|
| **Project skills dir** | `.agents/skills/` | `.claude/skills/` |
| **Global skills dir** | `~/.gemini/config/skills/` | `~/.claude/skills/` |
| **Project rules** | `GEMINI.md` (+ `AGENTS.md`) | `CLAUDE.md` (+ `AGENTS.md`) |
| **Invocation** | semantic match **or** `/skill-name` | semantic match; supports `disable-model-invocation:true` to make a skill user-only |

**To port a skill:** copy the folder and change the **directory** (`.claude/skills/` ↔ `.agents/skills/`). The `SKILL.md` itself usually needs no change. **To port rules:** put the tool-agnostic content in **`AGENTS.md`** (both tools read it) and keep only tool-specific bits in `CLAUDE.md` / `GEMINI.md`.

Cursor is a step further away: it uses `.cursor/rules/*.mdc` (a different file type), so a `SKILL.md` would need conversion — but Cursor **does** read `AGENTS.md`. See [[google-antigravity-skills/vs-claude-code-and-cursor]].

## The recommended multi-tool layout

```
your-repo/
├── AGENTS.md            # universal, cross-tool rules  (Antigravity + Claude Code + Cursor + Kiro)
├── CLAUDE.md            # Claude-Code-specific bits only
├── GEMINI.md            # Antigravity-specific bits only (if you use Antigravity)
├── .claude/skills/      # skills for Claude Code
└── .agents/skills/      # same SKILL.md skills, Antigravity path (copy or symlink)
```

Put ~everything portable in `AGENTS.md`; keep the native files thin. One skill authored once runs in every SKILL.md-aware tool.

## Why this matters for *this* vault

- The vault's **project-local skills** (`(C) yt-pipeline.md`, `(C) autopilot-research-routine.md`, etc.) and the root **`CLAUDE.md`** rules are conceptually the same primitives Antigravity uses. Re-expressing the reusable ones as **`SKILL.md`** + a portable **`AGENTS.md`** would make them **tool-agnostic** — runnable in Claude Code *and* Antigravity's free, multi-model surfaces.
- It de-risks tool lock-in: "harness > model" (see [[../harness-engineering/_index]], [[../pocock-agentic-workflow/_index]]) extends to "harness > *tool*" — your skills/rules outlive any single IDE.
- It connects directly to the pilot menu's headline move (adopt `AGENTS.md`; recognize your skills are already portable).

## Key Takeaways

- **Antigravity Skills ARE Anthropic's open `SKILL.md` format** (adopted, not reinvented; Anthropic published it Dec 18 2025, spec at `agentskills.io`).
- **`AGENTS.md`** is a **Linux-Foundation cross-tool rules standard** read by Antigravity, Claude Code, Cursor, and Kiro — the portable superset of `CLAUDE.md`.
- Porting is **copy-the-folder + swap the directory** (`.claude/skills/` ↔ `.agents/skills/`); `SKILL.md` content is unchanged. Invocation semantics differ slightly.
- Best practice: **universal rules in `AGENTS.md`**, tool-specific bits in `CLAUDE.md` / `GEMINI.md`, one shared set of `SKILL.md` skills.
- Net: your Claude Code harness is **portable to Antigravity for free** — the basis of the pilot.
