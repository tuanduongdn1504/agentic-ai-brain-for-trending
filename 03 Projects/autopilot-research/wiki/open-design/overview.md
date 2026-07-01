# Overview — Open Design, the open-source Claude Design alternative

## Source

- **Primary:** [QOqWZzecjuY](https://www.youtube.com/watch?v=QOqWZzecjuY) — "Open Design in 20 Minutes (Full Setup + Demo)", **CodingMenace** (Dennis), 2026-05-05, 22:04, ~19.4K views. Transcript: `raw/2026-07-01-open-design.md`.
- **Authoritative:** [`nexu-io/open-design`](https://github.com/nexu-io/open-design) README + [open-design.ai](https://open-design.ai) (gh-api + WebFetch verified 2026-07-01).

## What it is

**Open Design** is a **local-first, open-source desktop app** (macOS/Windows, Linux AppImage) that turns your existing coding-agent CLI into a design engine. It is explicitly positioned as an **open-source alternative to [Claude Design](https://www.anthropic.com/news/claude-design-anthropic-labs)** (Anthropic's closed, cloud-only, subscription-gated design product — see [[open-design/open-design-vs-claude-design]]).

The tagline the README uses: *"the Figma alternative for the agent era — instead of pushing pixels on a canvas, it delivers single-page artifacts in real CSS, real fonts, real components."*

- **Repo facts (gh api, 2026-07-01):** `nexu-io/open-design` — **73,468★**, **8,348 forks**, **Apache-2.0**, **TypeScript**, created **2026-04-28**, latest release **v0.12.0** (2026-06-26). Org `nexu-io` created 2026-02-24 (18 repos, 1,233 followers).
- **What it generates:** web / desktop / mobile **prototypes**, live **dashboards / artifacts**, **decks** (PPTX/PDF), **images**, **video** + **HyperFrames** motion graphics. Exports **HTML / PDF / PPTX / MP4**, previewed in a sandboxed iframe.
- **What it ships in the box (README figures):** "100+ skills", "150 design systems", "261 plugins", "21 coding agents", "14 media providers" — *actual repo directory counts are higher and fast-growing* (≈159 skills, ≈152 design systems, ≈440+ items). Treat all counts as approximate; see [[open-design/caveats-and-safety]].

## The one thesis: "we don't ship an agent — yours is good enough"

This is the line to remember. Open Design does **not** bundle an LLM. On first run its local daemon **PATH-scans** your machine, finds the coding-agent CLIs you already have (Claude Code, Codex, Cursor, Copilot, Gemini, OpenCode, Qwen, Kimi, …), and **drives one of them** as the design engine. You pick the default; you can force a specific model (the video's demo detected **Claude Opus 4.7** as the default CLI). No CLI installed? A **BYOK proxy** lets you paste an OpenAI-/Anthropic-/Ollama-compatible endpoint instead.

This is **bring-your-own-agent (BYOA)** — the design-tool expression of the **harness-over-model** thesis in [[../pocock-agentic-workflow/_index]] and [[../harness-engineering/_index]]. Your leverage isn't the model; it's the skills + design systems (the harness) you compose around whatever model you already pay for.

## The six "load-bearing ideas" (from the app's own intro screen)

The video pauses on Open Design's own philosophy screen. Verbatim-ish from the transcript + README:

1. **We don't ship an agent. Yours is good enough.** (BYOA — drive the CLI on your PATH.)
2. **Skills are files, not plugins.** Each skill is a folder with a `SKILL.md` (the Claude Code convention) — drop it in, restart the daemon, it appears in the picker.
3. **Design systems are portable markdown** (`DESIGN.md`) **+ team JSON** (`open-design.json`). Brand logic decoupled from discovery/execution. → [[open-design/design-md-as-source-of-truth]]
4. **Local-first, BYOK at every layer.** Native desktop, `127.0.0.1` daemon, no cloud round-trip, bring your own key/credentials.
5. **Open source shoulders ("OD" = *open, on the shoulders of…*).** It sits on a stack of prior open-source projects rather than reinventing them → [[open-design/the-originals]].
6. **Agent-native, model-agnostic.** One-click swap between agents; the design system stays put.

## How it "sits on shoulders"

The README's *"References & lineage"* table names the projects Open Design composes (the video mangles the Chinese names badly — corrected here):

| Video's mangling | Real upstream | What Open Design takes |
|---|---|---|
| "Huashu design" | [`alchaincyf/huashu-design`](https://github.com/alchaincyf/huashu-design) | the **design philosophy** (anti-slop, brand-asset protocol) |
| "Wizeng / Guizhong PPT" | [`op7418/guizang-ppt-skill`](https://github.com/op7418/guizang-ppt-skill) | the **default deck skill** (bundled verbatim) |
| — (not in video) | [`lewislulu/html-ppt-skill`](https://github.com/lewislulu/html-ppt-skill) | the **HTML PPT Studio** deck family |
| "opencode design / Open Cowork AI" | [`OpenCoworkAI/open-codesign`](https://github.com/OpenCoworkAI/open-codesign) | the **UX North Star** (streaming-artifact loop, sandboxed iframe) |
| "Kami / daemon / path-scan" | [`multica-ai/multica`](https://github.com/multica-ai/multica) | the **daemon + adapter architecture** |
| — | [`VoltAgent/awesome-design-md`](https://github.com/VoltAgent/awesome-design-md) | the **`DESIGN.md` 9-section schema** |
| — | [`bergside/awesome-design-skills`](https://github.com/bergside/awesome-design-skills) | a batch of **design skills** |
| — | [`heygen-com/hyperframes`](https://github.com/heygen-com/hyperframes) | the **HTML→MP4** motion engine |

Full deep-dive: [[open-design/the-originals]] and [[open-design/huashu-design-deep-dive]].

## Why this matters to *you* (Storm Bear)

- It's the **tool-level counterpart** to your [[../ai-web-design-workflow/_index]] topic. That topic centers the **Taste Skill** (anti-slop gate); Open Design is a whole *design harness* that the Taste Skill (and huashu-design's anti-slop philosophy) can gate.
- Its **`DESIGN.md` pattern is the direct antidote** to hireui's drifted design tokens (the Candidate Detail refactor: navy `#1E2960`→`#002D79`, accent `#E8743C`→`#DC6803`, Inter→Roboto). You can adopt the *pattern* without adopting the *tool*.
- Because it runs on **your** Claude Code CLI, piloting it produces genuine **Goal #2** ("build software with these tools") deployment evidence. See `output/(C) 2026-07-01-open-design-pilot-methods.md`.

## Key Takeaways

- Open Design is a **local-first, Apache-2.0, bring-your-own-agent** open clone of Anthropic's closed **Claude Design**; it ships no model and drives the CLI already on your PATH.
- Its philosophy is small and sharp: **skills are files**, **design systems are portable markdown**, **local-first + BYOK**, and it **stands on open-source shoulders** rather than reinventing them.
- The video is a **7-days-post-launch first impression** by a third-party creator — good for *feel*, unreliable for numbers and names (all corrected against the repo here).
- Its relevance to you is concrete: it's the tool sibling of your Taste-Skill topic and a ready-made answer to hireui's token-drift problem via `DESIGN.md`.
