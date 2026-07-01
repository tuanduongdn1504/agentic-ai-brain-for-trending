# Antigravity Rules & Customization (AGENTS.md, GEMINI.md, the Customizations panel)

## Source

antigravity.google/docs + agentpedia/community rule guides + the Linux Foundation Agentic AI Foundation announcement + the [[google-antigravity-skills/video-summary|video]]. Verified — see [[google-antigravity-skills/source-provenance]].

---

## The video's "Rule" concept

The video's most valuable teaching is the **Skill vs Rule split**:

- **Skill** = a **capability** ("analyze this Excel file, segment customers, chart it"). On-demand.
- **Rule** = a **cross-cutting constraint** the agent must always obey ("**never delete, edit, or overwrite raw data**; only create a new report sheet"). Always-on.

The creator's point: don't paste the same constraint into every skill. A project might have **3–5 skills but one rule** that all of them read. He also notes a rule is **scoped** — his "never overwrite raw data" rule applies to every skill in the *sales* workspace, but not to a different workspace. And for a constraint you want everywhere, use the **global** scope.

That maps precisely onto Antigravity's real rules architecture below.

## Antigravity's rules architecture

Antigravity layers instructions from most-authoritative down:

1. **System Rules (immutable)** — baked-in directives from Google DeepMind defining the agent's identity. You can't change these.
2. **`GEMINI.md`** — **Antigravity-specific** project rules. Takes **precedence** when it conflicts with `AGENTS.md`.
3. **`AGENTS.md`** — the **cross-tool** rules file (see below). Applied *after* `GEMINI.md`.
4. **`.agent/rules/`** — optional workspace **supplement** files, to split rules into separate concerns.

**Scopes** (matching the video's workspace-vs-global point):

| Scope | Antigravity-only | Cross-tool |
|---|---|---|
| **Project / workspace** | `<root>/GEMINI.md` (+ `.agent/rules/`) | `<root>/AGENTS.md` |
| **Global (all projects)** | `~/.gemini/GEMINI.md` | `~/.gemini/AGENTS.md` |

The video's Settings screen showing a **rule with "user global" and "agent" entries** maps to: **"user global"** = the global-scope rule (`~/.gemini/…`), and the **"agent"** entry = the project rules file (the video's "agent.mdown" ≈ **`AGENTS.md`**). See [[google-antigravity-skills/source-provenance]] for the naming reconciliation.

## AGENTS.md — the cross-tool standard (this is the big one)

`AGENTS.md` is **not** a Google or Cursor invention. It's an **open standard**:

- Started collaboratively (**OpenAI, Amp, Google, Cursor, Factory**, ~Aug 2025) and contributed to the **Linux Foundation "Agentic AI Foundation"** (Dec 2025), which now stewards it.
- **Plain Markdown, no required schema** — project-level context/guidance for agents.
- Read by **28+ tools**, including **Antigravity, Claude Code, Cursor, and Kiro** — so one `AGENTS.md` gives your project portable instructions across all of them. (This is the rules counterpart to skill portability — see [[google-antigravity-skills/anthropic-agent-skills-portability]].)
- It's the ecosystem's answer to "everyone had their own `CLAUDE.md` / `.cursorrules` / `GEMINI.md`."

> ⚠️ Some *specific* adoption figures floated online ("60,000+ repos", exact version numbers/dates for Antigravity's AGENTS.md support) are community-reported and **not independently confirmed** — treat as directional, not precise. The *standard's existence and multi-vendor governance* are confirmed.

## Rules vs Skills — the clean distinction

| Aspect | **Rules** (`AGENTS.md` / `GEMINI.md`) | **Skills** (`SKILL.md`) |
|---|---|---|
| Purpose | Always-active, project-wide **constraints/context** | On-demand, specialized **capabilities** |
| Activation | Loaded for **every** conversation | Loaded **only when semantically relevant** |
| Format | Plain Markdown (no required structure) | YAML frontmatter + Markdown |
| Discovery | File-based (static) | Semantic matching (dynamic / progressive disclosure) |
| Scope | Project (`AGENTS.md`/`GEMINI.md`) or global (`~/.gemini/…`) | Project (`.agents/skills/`) or global (`~/.gemini/config/skills/`) |

## Settings → Customization (the video's "vào setting → customization")

The video's UI path is **correct**: Antigravity has a **Customizations panel** where Rules and Skills are listed/managed. Notes:

- You can add a **global** rule via a **"+ Global"** button in the Customizations panel (or by editing `~/.gemini/GEMINI.md` / `~/.gemini/AGENTS.md` directly).
- Broader settings open via the **`/config`** (alias `/settings`) command as a full-screen overlay.
- **MCP** servers are configured centrally at `~/.gemini/config/mcp_config.json` (Antigravity ships pre-built MCP integrations for Google Cloud, Workspace, Firebase, and design-to-code/Stitch).

## Multi-agent orchestration (context, not the video's focus)

Antigravity 2.0 adds parallel **subagents** with **workspace isolation** and a **state-handoff** system for long jobs. It reportedly ships a multi-persona team model too. ⚠️ The specific **persona names** and hard limits (e.g. "6 personas Sentinel/Explorer/Worker/Reviewer/Critic/Auditor", "max 10 nesting levels", "12,000-char workflows") are **single-source / unverified** — recorded as reported-not-confirmed in [[google-antigravity-skills/source-provenance]]. The video does **not** cover personas; it's a solo-user Skills+Rules tutorial. For multi-agent patterns generally, see [[../multi-agent-orchestration/_index]].

## Key Takeaways

- **Rules = always-on constraints; Skills = on-demand capabilities.** One rule can govern many skills — the video's core lesson, and it matches Antigravity's real design.
- Antigravity's rule layers: **System (immutable) → `GEMINI.md` (Antigravity, wins) → `AGENTS.md` (cross-tool) → `.agent/rules/`**; project vs global (`~/.gemini/…`).
- **`AGENTS.md` is a Linux-Foundation cross-tool standard** (OpenAI/Amp/Google/Cursor/Factory → LF) read by Antigravity, Claude Code, Cursor, Kiro — a portable superset of `CLAUDE.md`.
- The video's **Settings → Customization** path, **global vs workspace** rules, and **"user global" + "agent"** entries all check out (with "agent" ≈ `AGENTS.md`).
- Treat specific persona names / version numbers / adoption counts as **reported, not verified**.
