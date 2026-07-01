# Workspace vs Global scope (the "two houses" analogy)

## Source

The [[google-antigravity-skills/video-summary|video]] (the "two houses / vacuum cleaner / street lamp" analogy) + Antigravity docs on skill & rule scopes. Verified paths in [[google-antigravity-skills/skills-system]] and [[google-antigravity-skills/rules-and-customization]].

---

## The video's analogy

The creator explains scope with two neighboring houses:

- **Workspace (project) skill** = *"a vacuum cleaner bought with your own money."* Agent A in House A uses it freely; Agent B in House B **can't touch it**. → per-project, private to that workspace.
- **Global skill** = *"a street lamp in the shared public area between the two houses."* **Both** agents A and B use it. → available across all projects.

This is a genuinely good mental model, and it's accurate.

## What that means on disk

| | **Workspace / project scope** | **Global scope (all projects)** |
|---|---|---|
| **Skills** | `<project-root>/.agents/skills/` | `~/.gemini/config/skills/` |
| **Rules (Antigravity)** | `<project-root>/GEMINI.md` (+ `.agent/rules/`) | `~/.gemini/GEMINI.md` |
| **Rules (cross-tool)** | `<project-root>/AGENTS.md` | `~/.gemini/AGENTS.md` |
| **Best for** | Project-specific scripts, proprietary framework boilerplate, one client's brand rules | Personal preferences that follow you everywhere (coding style, language, "never do X") |

The two scopes use **identical file/folder structures** — a skill is portable between them by moving the folder. Global entries are managed via the **"+ Global"** control in the Customizations panel (see [[google-antigravity-skills/rules-and-customization]]).

## How to choose

- **Workspace** when the knowledge is *only* meaningful inside one repo/project — e.g. "how we deploy *this* app", "*this* client's report template", the video's per-project sales-report skill.
- **Global** when it should apply to *everything you do* — e.g. "always write commit messages this way", "never touch raw data without asking", a personal writing-voice skill.
- **Precedence:** a workspace rule/skill is the local authority for that project; `GEMINI.md` wins over `AGENTS.md` on conflict (Antigravity-specific > cross-tool).

## Where the video is imprecise

The video says a skill "created in this folder can be used in other folders too — yes, because you can also put it in Global Skill." That's slightly muddled: a **workspace** skill is **not** shared across projects (that's the whole point of the vacuum-cleaner analogy). To share it, you **promote it to Global** (or copy it into the other workspace). The two-scope model is right; the "workspace skills leak across projects" phrasing is not.

## Key Takeaways

- **Workspace = private to one project** (`.agents/skills/`, `GEMINI.md`/`AGENTS.md` at root); **Global = everywhere** (`~/.gemini/config/skills/`, `~/.gemini/GEMINI.md`/`AGENTS.md`).
- The **vacuum-cleaner (workspace) vs street-lamp (global)** analogy is accurate — use workspace for project-specific knowledge, global for personal defaults.
- Same structure in both scopes → promote a skill from workspace to global just by moving the folder.
- Don't believe the "workspace skills auto-apply to other projects" phrasing — you must promote or copy them.
