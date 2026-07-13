# Source provenance & verification record

## The source

- **Video:** [GdvKNwMcfd0](https://www.youtube.com/watch?v=GdvKNwMcfd0) — *"From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft"*
- **Channel:** AI Engineer (`@aiDotEngineer`), 539K subscribers — the official YouTube channel of the **AI Engineer World's Fair / ai.engineer** conference series. Confirmed via the conference's own website (states it publishes "free talk & workshop videos" via this channel, citing 1.2M uniques / 10M views on 2025 conference-talk videos) and YouTube's own metadata.
- **Uploaded:** 2026-07-11 · 23:05 · ~8,487 views at ingest · Science & Technology category. Metadata (title, channel, date, view count) independently confirmed via this project's own `yt-dlp --print` pull at ingest time, not solely from the verification workflow's provenance agent.
- **Speaker:** Chris Noring — GitHub handle `softchris`, self-described in the video as "Cloud Developer Advocate at Microsoft... work[ing] a lot with AI engineering." Independently verified: real Microsoft employee, 276 public GitHub repos, published books (React, RxJS), co-author of Microsoft's "Web Dev For Beginners" curriculum, Google Developer Expert. His public bio/GitHub profile skews toward general cloud/JS/web-framework advocacy historically; "AI engineering" as a current focus is plausible (people's beats shift, especially into 2026) but not independently corroborated beyond his own self-introduction — flagged as a minor imprecision, not a red flag, in [[claims-scorecard]] (C7).
- **Ingest:** path 5 (yt-dlp-only). EN auto-captions → `sed`/`uniq` dedupe (stripped rolling-caption redundancy + word-level karaoke timestamp tags) → 656-line / 4,272-word clean transcript, **read in full in the main loop** across two reads. No NotebookLM used.
- **Raw:** [../../raw/2026-07-13-github-copilot-cli-agents.md](../../raw/2026-07-13-github-copilot-cli-agents.md)

## First-party originals double-dived

| Original | First-party source(s) | Article |
|---|---|---|
| GitHub Copilot CLI + `/delegate` | docs.github.com/copilot, github.blog/changelog | [[copilot-cli-and-delegate]] |
| Custom agents (`.github/agents/*.agent.md`) | docs.github.com/copilot/reference, /copilot-sdk | [[custom-agents-vs-subagents]] |
| Agent Skills (Copilot side) | docs.github.com/copilot/concepts/agents/about-agent-skills | [[agent-skills-shared-standard]] |
| Agent Skills (Claude side) | code.claude.com/docs/en/skills, platform.claude.com/docs | [[agent-skills-shared-standard]] |
| Copilot coding agent (issue → PR) | github.blog/changelog (2025-09-25 GA entry, found by main-loop takeover) | [[coding-agent-issue-to-pr]] |
| AGENTS.md adoption | github.blog/changelog (2025-08-28), agents.md, devblogs.microsoft.com | [[agents-md-guardrail]] |
| Claude Code AGENTS.md status | github.com/anthropics/claude-code issue #6235 + duplicates (verified independently) | [[agents-md-guardrail]] |
| GitHub MCP server | github.com/github/github-mcp-server | [[mcp-servers-in-copilot]] |
| Playwright MCP | github.com/microsoft/playwright-mcp | [[mcp-servers-in-copilot]] |
| Claude Code subagents / Routines / Claude Tag | code.claude.com/docs/en/sub-agents, /routines; anthropic.com/news/introducing-claude-tag | [[claude-code-parity-and-gaps]] |

## Verification workflow

- **Workflow `wf_a1693ef8-4dc`** — 17 agents: 8 first-party dives + 8 refute-first skeptics + 1 completeness critic. ~688K tokens, 232 tool calls, ~5.3 minutes, **0 errors, 0 empty results**.
- **Agents ran on Haiku 4.5.** The completeness critic (also Haiku 4.5) caught one likely-confabulated verifier quote/date on its own — a good outcome for the adversarial-pass design, but the confabulation still needed a **main-loop independent check** to actually resolve (see [[caveats-and-corrections]]).
- **No agent deaths, no empty results** — a clean run by this corpus's usual standards (contrast with `jsm-six-file-context`'s 13-panel-verifier outage or `local-ai-coding-agents`' 2 "prompt too long" deaths).

## Corrections logged (Rule 12 — fail loud)

1. **Coding-agent GA date + press-release quote** — corrected from a likely-fabricated "July 2026" / press-release citation to the real, independently-found **2025-09-25** changelog entry. See [[caveats-and-corrections]] for the full account.
2. **AGENTS.md "vendor agreement" claim-mapping** — the verification workflow's own claim C6 attributed a "vendors including Anthropic agree to support this" framing to the AGENTS.md guardrail. Re-checking the transcript directly: Chris's "all the big vendors, whether you are Anthropic or Microsoft" line is actually about **Skills**, not AGENTS.md. The Skills version of that claim is true (see [[agent-skills-shared-standard]]); the AGENTS.md article states GitHub's real adoption and Claude Code's real non-adoption as two independent facts, without implying Chris made a claim he didn't make.
3. **Unverified specifics quarantined** — exact GitHub issue #6235 reaction counts and the exact `argument-hint` regression citation are held as *plausible-but-unverified* rather than stated as settled fact (see [[caveats-and-corrections]]).

## See also
[[_index]] · [[claims-scorecard]] · [[caveats-and-corrections]] · [[overview]]
