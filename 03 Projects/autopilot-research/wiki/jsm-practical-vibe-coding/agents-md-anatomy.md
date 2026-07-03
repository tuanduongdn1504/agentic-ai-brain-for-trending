# AGENTS.md — the taught anatomy vs the committed reality vs the standard

## Source

- Transcript 00:04:16–00:07:28 (theory) + 00:28:37 (setup); the REAL committed file fetched via `gh api repos/adrianhajdin/react-native-lingua/contents/AGENTS.md` (2026-07-03); https://agents.md fetched live.

## The taught anatomy (six parts)

1. **Role** — "You're an expert React Native + Expo engineer. You write clean, simple code…" ("That paragraph alone changes the quality of everything that follows.")
2. **Overview** — what the app is, one paragraph.
3. **Stack** — every library/service, one line each ("stops the AI from suggesting alternatives mid-build").
4. **Folder structure** — where screens/components/state live.
5. **Styling rules** — approach, tokens, quirks (e.g. "NativeWind doesn't work with SafeAreaView — write that down").
6. **Patterns to follow** — anything you'd otherwise repeat across sessions.

Not written perfectly up front: **"write what you know, update it when something keeps coming up."**

## What the committed file actually contains (primary source)

The real `AGENTS.md` in react-native-lingua matches the anatomy and adds four sections the crash course doesn't teach:

- **Development Philosophy** — 8 numbered rules ("Build the smallest useful version first", "Refactor only when repetition or complexity appears").
- **Decision Making & Clarifications** — the agent must **ask permission before adding libraries**, with a worked example ("…using react-native-reanimated would make animations smoother. Do you want me to add it?"). This is the ask-before-acting contract, cf. [[claude-md-12-rules]] Rule 1.
- **UI Implementation Rules** — "replicate the provided design exactly … pixel-perfectly", an 8-item match list (layout/spacing/fonts/colors/radius/shadows/alignment/proportions), "Do not approximate. Do not simplify unless explicitly asked." This is the file-side half of the [[four-part-prompt-structure|design-reference]] prompt part.
- **NativeWind Rule** — *"Check the current NativeWind version in package.json … Do not use APIs, config patterns, or examples from a different NativeWind version."* — a **version-drift countermeasure baked into the context file** (see [[when-ai-knowledge-ends]]).

## Reality check against the standard (verified 2026-07-03)

- agents.md is real and stewarded by the **Agentic AI Foundation under the Linux Foundation**; "over 60,000 open-source projects use AGENTS.md"; supported by Codex, Jules, Gemini CLI, GitHub Copilot, Cursor, Aider, VS Code, Devin, Windsurf, Zed, Warp, UiPath and others (agents.md, fetched live).
- **The video's blanket claim is wrong for Claude Code**: "Tools like Cursor, Claude Code, and Windsurf read project files … agents.md is the first file they read." Claude Code's own docs (code.claude.com/docs/en/memory): **"Claude Code reads CLAUDE.md, not AGENTS.md"** — the documented bridge is a CLAUDE.md that `@AGENTS.md`-imports it. (Cross-corpus: same portability seam as [[google-antigravity-skills/anthropic-agent-skills-portability|the Antigravity thread]].)
- **Coherence save:** his own four-part prompt begins "Read the agents.md first and follow it strictly" **every time** — an explicit pointer that works even in tools that never auto-read the file. The prompt discipline compensates for the wrong claim; viewers who skip part 1 in Claude Code get silent context loss.
- The standard has **no required fields** — the six-part anatomy is prescriptive JSM guidance, not spec.
- Next.js 16.2's create-next-app generates AGENTS.md (and CLAUDE.md) by default — confirms the [[jsm-six-file-context/agents-md-claude-md-portability|prior topic's finding]]. ⚠️ The prior topic's "Vercel eval: AGENTS.md beats skills 100% vs 79%" did NOT reproduce on the current published evals page (shows with/without-AGENTS.md deltas like 75%→100%); flagged in [[caveats-and-corrections]].

## Key Takeaways

- Anatomy = role + overview + stack + folders + styling + patterns; the committed file adds philosophy, ask-permission, pixel-perfect UI rules, and a version-pin rule.
- AGENTS.md is a real LF standard with wide adoption — but Claude Code natively reads CLAUDE.md; bridge with an import, or do what Adrian does and point at the file in every prompt.
- The most transferable single rule in the file is the NativeWind version-pin: **pin the version the project actually uses and forbid other-version APIs** — cheap insurance against training-data drift.
- One evolving context file beats re-typing context per prompt; across 20 prompts unmanaged context yields "five different people, ten architectures".
