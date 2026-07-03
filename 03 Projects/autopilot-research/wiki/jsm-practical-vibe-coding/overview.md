# Overview — JSM "Practical Vibe Coding" (mobile)

## Source

- Video: https://www.youtube.com/watch?v=Q7AYc2kECDI — "How to Actually Build Mobile Apps with AI in 2026 | A Complete Beginner's Tutorial"
- Channel: JavaScript Mastery (Adrian Hajdin), 1M+ subs — **first-party** (his own methodology, his own build)
- Uploaded 2026-05-15 · 3:40:48 · ~330K views / ~4.3K likes at ingest (2026-07-03)
- Raw transcript: `raw/2026-07-03-jsm-practical-vibe-coding.md` (~209K chars, read in full across main-loop + 2 lens agents)
- Build repo: [adrianhajdin/react-native-lingua](https://github.com/adrianhajdin/react-native-lingua) — created 2026-05-11, TypeScript, 94★, **NO LICENSE** (same as ghost-ai)

## Thesis

- Pure vibe coding (Karpathy, Feb 2025) "doesn't survive contact with anything serious" — breaks around feature 5; over-engineering (days of docs, zero screens) never ships. **"Practical Vibe Coding" is the middle**: keep AI speed, add just enough structure.
- The whole method runs through **one file — `AGENTS.md`** — plus a fixed **four-part prompt structure** for every prompt.
- Explicit framing: **"The app isn't the point; the workflow is."** The Duolingo clone is the demo vehicle.

## What gets built

Duolingo clone ("Lingua"): onboarding → email+social auth (Clerk) → language selection → hardcoded lesson content (TS data files) → Zustand+AsyncStorage state → bottom tabs → home UI → lesson + audio-lesson UI → **real-time AI voice teacher** (Stream transport + Vision Agents Python service + OpenAI Realtime) → live captions → PostHog analytics → CodeRabbit PR review. Editor: VS Code + Claude extension; he claims the workflow works identically for Copilot, Claude Code, Codex, Cursor, Windsurf, Warp, OpenCode, Gemini CLI.

## The two originals deep-dived

1. **[[vision-agents-deep-dive|GetStream Vision Agents]]** — open-source (Apache-2.0) Python framework for real-time voice/video AI agents; the AI-teacher engine. See deep-dive.
2. **The AGENTS.md standard** — Linux Foundation (Agentic AI Foundation) stewarded, 60K+ projects; see [[agents-md-anatomy]] for what the video gets right and wrong about it.

## Corpus placement

- Sister to [[jsm-six-file-context/_index|jsm-six-file-context]] (same channel, 2 weeks earlier): that video teaches a **six-file context system + 29 feature specs** for a web app; this one compresses to **one AGENTS.md + per-prompt discipline** for mobile. Same author, two tiers of ceremony — JSM implicitly scales ceremony to project size. Both ship the vendor-skills lockfile supply chain ([[skills-supply-chain-second-observation]]).
- The four-part prompt structure is a mass-market cousin of [[pocock-agentic-workflow|Pocock's]] scoped-prompt discipline and the [[claude-md-12-rules|12-rules]] Surgical-Changes/Think-Before-Coding contract.
- The AI-teacher is a production sibling of the [[multi-agent-orchestration|voice/agent orchestration]] thread.

## Key Takeaways

- The methodology is genuinely stack-agnostic and cheap to adopt: one context file + four-part prompts + one-feature-per-prompt + verify-before-next.
- The video's discipline for **what to protect** (behavioral constraints) is its sharpest idea — most prompt advice covers what to build, not what to keep intact.
- The load-bearing tech original (Vision Agents) is real, active, and open-source at the framework layer — but rides Stream's commercial edge network in every shipped example.
- The repo is the evidence trove: committed AGENTS.md, skills-lock.json (21 skills), `.well-known`-installed vendor skill, PostHog-wizard-installed skill, and committed Claude Code auto-memory.
- Sponsor-integrated curriculum (~half the runtime touches the 5 sponsors) — workflow knowledge credible; service superlatives need discounting ([[stack-and-sponsors]]).
