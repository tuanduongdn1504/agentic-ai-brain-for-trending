# Level 2 — Reliable recall: structured memory + an injection hook

> **Source:** [[claude-code-memory-systems/_index]] · video [06:31–16:55] + **deep-dive of the originals**: [John Connolly, "How I finally sorted my Claude Code memory"](https://www.youngleaders.tech/p/how-i-finally-sorted-my-claude-code-memory) built on [Paweł Huryn](https://substack.com/@huryn/note/c-216337711) (the original concept, ~Feb 18, *before* Anthropic shipped auto-memory). **The video's verdict: "most of you should stop right there."**

**The problem L2 solves:** Level 1's auto-memory works, but Claude doesn't *reliably* read the index at the right moment, and the structure isn't enforced. L2 makes the loading **deterministic** (a hook) and the structure **disciplined**.

## The folder structure (Connolly / Huryn)

A structured memory tree rooted at **`~/.claude/memory/`** (global) plus **per-project** memory:

```
~/.claude/memory/
├── memory.md           # INDEX ONLY — read at session start; one-line description per topic
├── general.md          # cross-project facts, preferences, environment setups
├── tools/              # one file per tool: tool-specific config, workarounds, edge cases
│   ├── slack.md
│   ├── snowflake.md
│   └── atlassian.md
└── domain/             # one file per topic/product/project: domain-specific knowledge
    └── {topic}/{topic}.md

~/.claude/projects/{project}/memory/MEMORY.md   # per-project knowledge (200-line budget)
```

**The discipline (verbatim principles from the original):**
- **`memory.md` is an index, not a store** — it points to the right files; updated whenever files are created/modified.
- **Project `MEMORY.md` has a ~200-line budget** — *"use it for project knowledge, not boilerplate. Burn 20 lines on routing rules and you've given up 10% of your budget."*
- **Entry format: `date, what, why` — nothing more.**
- **Write immediately:** *"When you learn something worth remembering — architectural decisions, bug fixes, gotchas, environment quirks — write it to the right file immediately."*
- **Load lazily:** read `memory.md` at session start; **load specific topic files only when relevant**.

## Part 1 — set up the structure (run in plan mode)

Connolly ships a markdown block you **paste into a prompt** (not directly into `CLAUDE.md`). It instructs Claude to:
1. Create the global memory directory structure (`general` / `tools` / `domain`).
2. Update `CLAUDE.md` with the five memory sections (Memory Management / Global Memory / Global Memory Reference / Repo Memory Auto-Init / etc.).
3. Initialize project `MEMORY.md` files.

**How to run it (from the video):** open Claude Code in a project → **Shift+Tab twice → plan mode** → paste the whole block → review the plan → build it. The plan walks the parent tree to see what already exists and inherits downward.

**Critical safety rule baked into the prompt:** *"If any file already exists and would be modified or removed, use AskUserQuestion first. Show the current content and the proposed change. Do not modify without explicit confirmation."* (Mirrors your own vault rule: *ask before editing existing notes.*)

## The `reorganize memory` ritual

A **manual command** you run periodically (in **plan mode**, so you see changes first). Claude:
1. Reads all memory files
2. Removes duplicates + outdated entries
3. Merges entries that belong together (consolidation)
4. Splits files covering too many topics
5. Re-sorts entries by date
6. Updates the `memory.md` index
7. Runs a verification phase

*Real run from the video:* deleted 13 empty/template files, trimmed 6 sessions, finished 9 open threads, added 10 cross-references, added 3 patterns to `general.md`, kept 12 daily files with meaningful content. **This is the "dreaming"/consolidation idea, done on demand instead of by a daemon.**

## Part 2 — the auto-injection hook (the load-bearing upgrade)

The structure alone still relies on Claude *choosing* to read the index. Part 2 removes that dependency with a **hook** that injects the index automatically — including when you spin up **sub-agents**.

Connolly's implementation uses **two files** in `~/.claude/hooks/` plus a `settings.json` registration:

- **`pre-tool-memory.py`** — uses `os.getppid()` as the session id (not `CLAUDE_SESSION_ID`); maps the project dir (`/Users/you/Projects/foo` → `-Users-you-Projects-foo`); reads the **first 200 lines** of the project `MEMORY.md`; returns JSON with an **`additionalContext`** field; writes a `/tmp/claude-memory-loaded-{ppid}` flag to avoid double-loading.
- **`pre-tool-memory.sh`** — a bash wrapper that checks the flag *before* invoking Python (~5 ms vs ~80 ms Python startup), so the Python call only runs on the **first tool use** per process.
- **`settings.json`** registration:

```json
"PreToolUse": [
  { "matcher": "*",
    "hooks": [
      { "type": "command",
        "command": "bash ~/.claude/hooks/pre-tool-memory.sh",
        "timeout": 5 } ] }
]
```

> **Hook-event nuance:** the video frames this as a **SessionStart** injection ("when you open a new terminal or spin off sub-agents, it loads the memory index"). Connolly's actual implementation uses a **PreToolUse** hook with a first-call flag — same *effect* (index loaded before Claude does real work, once per process), different *event*. Either way it's an auto-injection hook; see [[claude-code-hooks/_index]]. The key word is **`additionalContext`** — the hook injects the *index*, not the full memory, keeping the window lean.

## Results after ~5 days (Connolly's own numbers)

- `~/.claude/CLAUDE.md`: **189 → 63 lines** (the bloated 155-line reference block now lives in files that load on demand).
- **7 new files** in `~/.claude/memory/` (tools + domain), **3 new** project-memory files.
- Memory *files* grew a lot (≈ +90% over John's usage), but `memory.md` / `general.md` barely grew — because they're **indexes**, not stores.

## Team-sharing + the domain lifecycle

- **Sharing:** because everything is plain markdown, teammates can **sync domain files** in a shared folder — granular detail Claude needs to be useful for a given domain/tool, shared across the team. (Huryn's original advantage: version-controlled in GitHub, shareable across Claude Code / Cowork / Web.)
- **Domain lifecycle (3 stages):** **Staging** (knowledge accumulates in `domain/{name}/`) → **Promotion** (enough to package as a plugin/skill) → **Pointer** (the memory file becomes a pointer to the plugin; the plugin holds the knowledge). This is the same maturation arc as [[claude-cowork/skills-vs-plugins-hierarchy]] and your own vault's promotion path.

## Key Takeaways

- L2 = **structured `.claude/memory/`** (index + general + domain + tools) + a **hook that auto-injects the index** so recall stops depending on Claude's discretion.
- **`memory.md` is an index; entries are `date/what/why`; the project file has a ~200-line budget.** Discipline beats volume.
- The hook injects via **`additionalContext`** (the *index*, not the bulk) — once per process, fast-path guarded by a flag file. Video says SessionStart; the original uses PreToolUse — same effect.
- **`reorganize memory`** is on-demand consolidation ("dreaming" without a daemon) — run it in plan mode.
- Plain markdown → **shareable across a team** + version-controllable; **domains graduate into plugins/skills** over time.
- **This is essentially your current setup, automated.** You already keep an index + per-fact files + date/why entries — L2's only addition for you is the injection hook + the `reorganize memory` ritual. See [[claude-code-memory-systems/your-current-setup-mapping]].
