# Antigravity Skills — the mechanism (SKILL.md, paths, auto-discovery)

## Source

Google Codelabs "Authoring Antigravity Skills" (`codelabs.developers.google.com/getting-started-with-antigravity-skills`) + antigravity.google/docs + the [[google-antigravity-skills/video-summary|video demo]]. Adversarially verified — see [[google-antigravity-skills/source-provenance]].

---

## What a Skill is

A **Skill** is a directory-based knowledge package: a folder whose only required file is **`SKILL.md`**, plus optional supporting subfolders. It teaches the agent *how to do a specific task* — and it loads **only when relevant**. This is exactly Anthropic's open "Agent Skills" format (see [[google-antigravity-skills/anthropic-agent-skills-portability]]).

## On-disk paths (get these exact)

| Scope | Path |
|---|---|
| **Project / workspace** | `<project-root>/.agents/skills/` |
| **Global (all projects)** | `~/.gemini/config/skills/` |
| Legacy (still recognized) | `.agent/skills/` (singular) — `.agents/` (plural) is the current default |

> ⚠️ **The video's path is wrong.** The Vietnamese auto-caption rendered the path as "Asian triệt skill" / "giặt ngang skill", which I initially read as `.antigravity/skills`. The **official path is `.agents/skills/`** (project) / `~/.gemini/config/skills/` (global). Don't propagate `.antigravity/skills`. See [[google-antigravity-skills/source-provenance]].

## SKILL.md format

`SKILL.md` = **YAML frontmatter + Markdown body**:

```markdown
---
name: excel-sales-report          # OPTIONAL — defaults to the directory name (lowercase-hyphens)
description: Analyze a monthly sales Excel file — segment customers, compute revenue/AR, chart by province, and produce a director-ready report.   # REQUIRED
---

# Instructions
1. Read the input .xlsx …
2. Segment paid vs unpaid customers …
3. Draw comparison charts …
(the procedural knowledge the agent follows once this skill activates)
```

- **`description` is the single most important field** — it is the **semantic trigger** the model matches your request against. Vague descriptions ("Database tools") are explicitly discouraged by Google's codelab; write it as *what it does + when to use it*.
- `name` is **optional** (defaults to the folder name). The video implies you must name things carefully; in practice only `description` is mandatory.
- Optional frontmatter (from the shared Agent Skills spec at `agentskills.io/specification`): `license`, `compatibility`, `metadata`, and an experimental `allowed-tools`.

## Directory layout (flat — no nested `rules/`)

```
.agents/skills/excel-sales-report/
├── SKILL.md          # required
├── scripts/          # optional — executable code, referenced by relative path
│   ├── analyze.py
│   └── chart.sh
├── resources/        # optional — templates, reference docs
│   └── report_template.md
└── assets/           # optional — images/logos
```

- **`scripts/` is real and optional.** Supported languages per Google's codelab: **Python, Bash, Node.js**. The agent runs them by relative path (e.g. `python scripts/analyze.py`). The video's "Python / PowerShell" is fine (PowerShell works on the creator's Windows box) but Python/Bash/Node are the canonical examples.
- The video's claim that "a skill folder contains `SKILL.md` + a `scripts/` folder" is **correct** — with the nuance that `scripts/` (and `resources/`, `assets/`) are **optional**; only `SKILL.md` is required.

## Auto-discovery = Progressive Disclosure (the video's "cơ chế auto discovery")

The video's headline claim — *"you give a command and it scans your skill folders and auto-activates the one matching the description"* — is **CONFIRMED**, and has a name: **Progressive Disclosure**.

1. **Discovery:** at conversation start the agent sees only a lightweight *menu* of each skill's `name` + `description` — cheap, no token bloat.
2. **Activation:** when your request **semantically matches** a `description`, the agent loads that skill's **full `SKILL.md`** (and can run its scripts).
3. **Execution:** it follows the instructions.

So you usually **don't invoke skills manually** — the description does the routing. The video's reassurance ("AI is smart enough to pick the right skill from your description — don't worry") is accurate *because* activation is description-driven semantic matching.

## Invocation (manual, when you want it)

Skills also surface as **slash commands**: type **`/skill-name`** in the prompt panel to force a specific skill. (The video's "type `/` to see your skills" is correct.) You can also just ask *"what skills are available?"* to list them.

## Creating a skill

**There is no official one-click / `/create-skill` command.** Skills are created by **writing files**:

1. `mkdir .agents/skills/<name>/`
2. Write `SKILL.md` (frontmatter + body).
3. (Optional) add `scripts/`, `resources/`, `assets/`.
4. Restart/refresh so Antigravity indexes it; verify with `/skill-name` or "what skills are available?".

The video's **Method 2** ("work with the agent, then tell it to create a skill from what we just did") works — but as an **emergent use of the agent**, not a documented feature: the agent can *author the `SKILL.md` file for you* when asked. See [[google-antigravity-skills/build-methods]] for both methods and the nuance.

## Key Takeaways

- A Skill = a folder with a **required `SKILL.md`** at **`.agents/skills/`** (project) or **`~/.gemini/config/skills/`** (global). *Not* `.antigravity/skills`.
- `SKILL.md` = **YAML frontmatter (`description` required, `name` optional) + Markdown**; optional `scripts/` (Python/Bash/Node), `resources/`, `assets/`.
- Discovery is **Progressive Disclosure**: the agent sees names+descriptions, then loads the full skill only when your request matches the `description` — so **write great descriptions**.
- Invoke automatically (semantic) or manually via **`/skill-name`**.
- Skill creation is **manual file authoring** (no official generator command); the "ask the agent to make a skill" trick works because the agent writes the file.
