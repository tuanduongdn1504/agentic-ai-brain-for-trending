# Level 1 — Native: what ships with Claude Code

> **Source:** [[claude-code-memory-systems/_index]] · video [01:37–06:31]. **Cost:** free, already on your machine. **Setup:** mostly done for you.

Two built-ins, and "very few people use both together properly."

## 1a. `CLAUDE.md` — the always-loaded rules file

- A plain markdown file in your project that stores rules, brand facts, how you work with clients, coding style — **loaded into every single session**. Think of it as a system-prompt prefix.
- **Hierarchy (inheritance, local-wins):**
  - *Claude project / home level* (`~/.claude/CLAUDE.md`) → applies to all instances.
  - *Root folder level* → applies to several projects under one folder.
  - *Individual project level* → project-specific instructions.
  - Lower files **inherit** the parent, but on any conflict the **local `CLAUDE.md` wins**.
- **The #1 mistake: stuffing too much in.** Full brand guide + tone-of-voice doc + complete client list → Claude burns the context window reading all of it *every session*. That's **context rot** ([[claude-code-memory-systems/overview]]).
- **The rule of thumb: keep `CLAUDE.md` under ~200 lines.** Heavier context (e.g. a brand-voice doc) goes in a **separate external file referenced from** `CLAUDE.md`, so it's pulled in **only when needed**.

## 1b. Auto-memory — the `memory.md` file

- A second native system already running on your machine. Inspect it with the **`/memory`** slash command.
- `/memory` shows: **imported memory** (if you run a separate memory system), **project + user memory** (your `CLAUDE.md` files at different levels), and the **auto memory folder**.
- The auto-memory folder holds, **per project**, a `memory.md` that is an **index of memories** pointing to *other* files — it does **not** dump everything into one file. Example: a `feedback-project-structure.md` that's only loaded when Claude realizes you're working on project structure.
- This is the **same discipline as the 200-line rule**: treat `memory.md` (and `CLAUDE.md`) as an **index**, point to separate topic files.
- It's **silent + automatic** — Claude quietly takes notes on tasks + feedback in the background and builds the index. In an empty folder there's no `memory.md` until there's something to record; you don't have to create it yourself.

> **This is exactly what *you* already run.** Your `~/.claude/projects/-Users-Cvtot-KJ-OS-Template/memory/MEMORY.md` is this native auto-memory index, and you maintain per-fact topic files under it. See [[claude-code-memory-systems/your-current-setup-mapping]].

## ⚠️ "Kairos" — a leaked, unreleased daemon (UNVERIFIED)

The video reports that when **Claude Code source "accidentally leaked a couple of weeks back,"** people found references to a system/framework called **Kairos** — described as *an always-on daemon that watches your project continuously, decides what's worth remembering, and consolidates old notes while you sleep.* Said to be **not in any public build**.

**Treat this as an unverified rumor.** It is a single-source, leak-derived claim with no first-party Anthropic confirmation. The *directional* point — Anthropic is clearly investing in native memory, so Level 1 will improve — is reasonable; the **specific name + behavior are not confirmed**. Flagged in [[claude-code-memory-systems/source-provenance]]. (Independently plausible given LangChain's productization of agent memory in [[agent-development-lifecycle/_index]] and the broader trend — but plausibility ≠ confirmation.)

## Key Takeaways

- Level 1 is **free, native, and already on**: `CLAUDE.md` (always-loaded rules) + auto-memory (`memory.md` index + per-topic files).
- `CLAUDE.md` inherits down the folder tree; **local file wins** on conflicts.
- **Keep `CLAUDE.md` < ~200 lines**; push heavy context into referenced external files that load on demand — the core anti-context-rot move.
- `memory.md` is an **index that points to files**, never a dumping ground — the same pattern Levels 2–3 formalize.
- **Kairos** (always-on memory daemon) is a leak-rumor — directionally telling, specifically unverified.
- "The setup is already done for you. You just need to actually use them properly."
