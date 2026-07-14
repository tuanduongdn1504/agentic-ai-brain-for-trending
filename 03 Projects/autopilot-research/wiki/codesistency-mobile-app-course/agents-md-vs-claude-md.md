# ⚠️ AGENTS.md vs CLAUDE.md — headline correction

This is the course's one genuine technical error. It matters because it's a claim many beginners will copy verbatim, and it ties directly to a standing corpus finding.

## What the presenter says

Paraphrasing the video (~01:11–01:17):

> "Both are plain markdown instruction files auto-loaded into the AI's context at the start of a session… `claude.md` is built specifically for Claude Code, but `agents.md` is **agent-agnostic** — all other AI coding tools can read it: Cursor, GitHub Copilot, Codex, Gemini CLI, **and even Claude Code itself**. So we can just go with `agents.md`, and in `claude.md` we make one reference to that file."

## What's actually true (verified July 2026)

- **Claude Code does NOT natively read `AGENTS.md`.** GitHub issue [anthropics/claude-code#6235](https://github.com/anthropics/claude-code/issues/6235) requesting it has been **open since 2025-08-21** with 5,200+ reactions and no shipped support; six-plus duplicate issues track the same request. Official Claude Code docs reference only `CLAUDE.md`.
- **GitHub Copilot added `AGENTS.md` support on 2025-08-28**; Cursor and Codex support it too. So "agent-agnostic for *other* tools" is fair — but the *"and even Claude Code itself"* part is **false**.
- The standard workarounds are a **symlink** (`ln -s AGENTS.md CLAUDE.md`) or an **import reference** inside `CLAUDE.md`.

This confirms, from a fresh source, the corpus pin established in [[github-copilot-cli-agents]] (Claude Code AGENTS.md non-support).

## The saving grace: his *setup* is correct

Crucially, the presenter does **not** rely on native AGENTS.md support. What he actually builds:

- An `AGENTS.md` containing the tech stack, conventions, and rules.
- A `CLAUDE.md` that **references AGENTS.md** so Claude Code reads it.

That reference is exactly the correct workaround. So the **mechanism he ships works**; only his **verbal explanation** ("Claude Code itself can read agents.md") is wrong. Verdict: **MISLEADING**, not FALSE — the tutorial's output is fine, the justification isn't.

## Why the distinction is worth flagging loudly

A viewer who *drops the CLAUDE.md reference* believing Claude Code reads AGENTS.md natively would silently get an ignored instructions file — the classic failure this vault's [[claude-md-12-rules]] Rule 12 ("fail loud") exists to prevent. The rule of thumb:

> For Claude Code, the file that is guaranteed to be read is **CLAUDE.md**. If you want a portable `AGENTS.md`, you must symlink it to `CLAUDE.md` or `@import` it from CLAUDE.md — do not assume native pickup.

## Rules he puts in AGENTS.md (good practice, regardless)

- Tech-stack declaration (Neon/Drizzle/Clerk/Inngest/ImageKit/Sentry).
- Styling convention: `className` (NativeWind), not inline styles.
- **"Always use native tabs"** (a project-wide UI rule).
- **"Never run the application yourself — I'm already running it in a separate terminal"** (prevents the agent spawning duplicate dev servers; directly supports the [[screenshot-verify-loop]]).

These are solid `AGENTS.md`/`CLAUDE.md` contents — the kind of durable rules [[jsm-practical-vibe-coding]] and this vault's own harness advocate.
