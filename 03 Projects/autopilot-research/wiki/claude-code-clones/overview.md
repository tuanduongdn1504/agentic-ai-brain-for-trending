# Claude Code Clones — Overview

> **Topic:** [[_index|claude-code-clones]]
> **Source:** `../../raw/2026-05-13-open-source-claude-design-clones-alternative-agent.md`

---

## What "Claude Code clone" means in this bundle

The term is used loosely across the 6 videos. Three distinct things get called "clones":

- **Forks of leaked Claude Code source** — most notably **OpenClaw**, described as a project built from the accidental source-code leak that Fireship covered [Source 2]
- **Independent third-party agents replicating the UX** — **OpenCode** (also called "Open Code"), **Hermes**, and older terminal AI **Aider** [Source 2, Source 3, Source 6]
- **Agent-SDK bridges** that use the official Anthropic Agent SDK to run Claude in a custom interface (Telegram, Discord, Slack). Not strictly clones but solve a similar "run Claude my way" problem [Source 1, Source 4]

The bundle does NOT cover (or names only in passing): Codex, Aider's specific feature set, Cursor / Windsurf (IDE forks, explicitly distinguished from terminal clones) [Source 3], or any of the Storm Bear vault's tracked T4-archetype clones beyond OpenClaw.

---

## The four named clones

| Clone | First mentioned in | What it is (per bundle) | Verdict |
|---|---|---|---|
| **OpenClaw** | [Source 2, Source 4] | Fork built on the leaked Claude Code source map | Fireship: makes Open Code "completely obsolete" [Source 2]. Mark Kashef: **abandoned it** as "derivative of a derivative" [Source 4] |
| **Hermes** | [Source 1, Source 6] | Third-party Claude-style agent | Alex Finn: "great vibe coder for prototypes" but not for deep coding [Source 6] |
| **OpenCode / Open Code** | [Source 2, Source 3] | Competing open-source terminal AI agent | Fireship: rendered obsolete by OpenClaw [Source 2]. Caleb: precursor to the terminal-agent wave [Source 3] |
| **Aider** | [Source 3] | Earlier terminal AI predating Claude Code | Caleb: one of the first to move work "one layer up in the stack" with terminal as IDE [Source 3] |

The bundle has **no benchmark numbers, no feature-comparison matrix, no install / usage walkthroughs** for the clones themselves. Discussion stays at the verdict level.

---

## The May 2026 landscape per the bundle

What the sources collectively imply about the state of clones:

- **The leak changed the math.** Fireship's coverage of Anthropic's accidental source-code leak [Source 2] suggests Claude Code is "basic programming concepts... combined with prompt spaghetti" — not magic. Once the prompts and the bash-tool primitive were public, forks became tractable.
- **The "barely legal" forks proliferated post-leak.** The bundle calls the leak a catalyst for clones [Source 2]. OpenClaw is the headline example.
- **The first-mover practitioner (Mark Kashef) has reversed.** He used to promote OpenClaw [Source 4]; in [Source 1] he explicitly states he has replaced both OpenClaw and Hermes with the official Agent SDK bridge. This is the single strongest signal in the bundle.
- **Anthropic has cracked down on subscription abuse.** Caleb notes Anthropic banned third-party apps from tapping subsidised subscription pricing [Source 3]. This pressures clones that relied on smuggling subscription tokens. The Agent SDK is the sanctioned alternative.
- **The Desktop release competes from the other direction.** Alex Finn argues the new Claude Code Desktop app makes the terminal CLI itself less central [Source 6] — which weakens the appeal of terminal-only clones.

Net effect: the clone landscape is **active but contracting** — leak catalyst pushed it up, Anthropic countermoves (Agent SDK legitimisation + Desktop release + subscription crackdown) are pushing it down.

---

## What Claude Code clones replicate (design surface)

Across the bundle, "Claude Code's design" decomposes into:

- **Terminal-first UX** — `claude` CLI in the repo root, project-scoped context [Source 3]
- **`claude.md` / `code.md` / `skills.md` tribal-knowledge files** — text files at repo root telling the agent project-specific rules [Source 3, Source 5]
- **Dynamic prompt sandwich** — the runtime composes prompts from many hard-coded instruction strings glued together with TypeScript [Source 2]
- **Bash tool** — a ~1,000-line primitive that lets the LLM reliably parse and execute terminal commands [Source 2]
- **Safety scaffolding** — hard-coded "be a good boy" instruction strings + a regex-based frustration detector + Undercover Mode (don't self-attribute in commits) [Source 2]
- **MCP / tool ecosystem hooks** — only briefly referenced; bundle doesn't go deep on which clones replicate MCP

Of these, the **bash tool** is the single most-cited "Aha, that's the trick" primitive [Source 2]. Clones that replicate this primitive reliably are the ones that work.

---

## Key Takeaways

- The bundle names **only four clones** by name: OpenClaw, Hermes, OpenCode/Open Code, and Aider [Source 1, Source 2, Source 3, Source 6]
- **OpenClaw is the most-discussed**; it was catalysed by Anthropic's accidental source leak [Source 2, Source 4]
- The most-influential practitioner in the bundle (Mark Kashef) has **abandoned clones** for the Agent SDK bridge [Source 1, Source 4]
- The clone landscape is **active but contracting** — Anthropic's Agent SDK + Desktop release + subscription crackdown are pushing it down
- The bundle treats clones at the **verdict level only**; no benchmarks, no feature matrices, no install walkthroughs — see [[gaps-and-followups]]
- "Claude design" decomposes into terminal UX + `claude.md` files + dynamic prompt sandwich + bash tool + safety scaffolding; the **bash tool** is the load-bearing primitive [Source 2]
