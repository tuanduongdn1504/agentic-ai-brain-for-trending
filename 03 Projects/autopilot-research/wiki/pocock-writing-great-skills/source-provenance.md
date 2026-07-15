# Source & provenance

## Video

- **Title:** *Building Great Agent Skills: The Missing Manual* (on-screen: "The Missing Manual — How to Write Great Skills")
- **ID / URL:** [`UNzCG3lw6O0`](https://www.youtube.com/watch?v=UNzCG3lw6O0)
- **Channel:** **AI Engineer** (`@aiDotEngineer`) — the official channel of the ai.engineer conference series (same channel as [[pocock-software-fundamentals/_index]] and [[github-copilot-cli-agents/_index]])
- **Uploaded:** 2026-06-29 · **Duration:** 20:43 · **Language:** English · **Views at ingest:** ~102,847 · **Likes:** ~3,556
- **Captions:** English auto-captions (`en`) → VTT dedupe → timestamped plain text (full transcript read in the main loop)

## Speaker

- **Matt Pocock** — TypeScript educator (creator of **Total TypeScript**), ex-XState core team, ex-Vercel developer advocate; runs **AI Hero** ([aihero.dev](https://aihero.dev), 70K+ subscribers). Author of the [`mattpocock/skills`](https://github.com/mattpocock/skills) repo.
- The corpus' **most-recurring individual**: 4 dedicated topics ([[pocock-writing-great-skills/_index]], [[pocock-software-fundamentals/_index]], [[pocock-agentic-workflow/_index]], [[pocock-real-feature-build/_index]]) + his `teach` skill in [[teach-skill-ai-tutor/_index]] + the grill-me lineage in [[claude-skills/_index]] + the vault's Pattern #52.

## Event

- **AI Engineer World's Fair 2026** — **June 29 – July 2, 2026**, Moscone West, 747 Howard St, San Francisco (6,000+ attendees, 29 tracks). The video was uploaded on the **opening day**.
- **Pre-recorded / remote:** Pocock says he "was dearly hoping to come… but family matters have intruded," so he recorded "the talk I would have given in San Francisco." Not found in the public in-person speaker schedule (consistent with a remote contribution).
- Distinct from [[pocock-software-fundamentals/_index]], which was **AI Engineer Europe 2026** (London, April) — a different event on the same conference series.

## The artifact

- **Repo:** [`github.com/mattpocock/skills`](https://github.com/mattpocock/skills) — "Skills for Real Engineers. Straight from my .claude directory." · MIT · Shell · created **2026-02-03** · **170,613★** at ingest (up from 169,558 the day before — the vault's tracked Pattern #52 extreme-viral curve).
- **The encoded skill:** [`skills/productivity/writing-great-skills/SKILL.md`](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md) (+ its `GLOSSARY.md`) — `disable-model-invocation: true`, "all reference."
- **Skills referenced on-screen:** `grill-me`, `grill-with-docs`, `to-spec` (the talk's `2PRD`), `domain-modeling`, `codebase-design` — all verified present in the repo.
- **Comparison repo:** [`github.com/obra/superpowers`](https://github.com/obra/superpowers) (Jesse Vincent / "obra") · MIT · created 2025-10-09 · 254,795★.

## Methodology (this ingest)

- **Path 5** (yt-dlp; operator-submitted single video). No NotebookLM.
- **Verification:** Workflow `wf_d267ed85-320` — 20 agents (5 dives + 14 refute-first verifiers + 1 completeness critic), all **Haiku 4.5**; ~833K tokens, 245 tool calls, **0 errors, 0 empty**, ~7.9 min.
- **Opus main-loop anchors (~12):** `gh api` on both repos + repo tree + individual `SKILL.md`/`GLOSSARY.md` fetches + a definitive user/model-invoked count across all 40 `SKILL.md`; `WebFetch` of Anthropic's `code.claude.com/docs/en/skills` + agentskills.io; `WebSearch` for World's Fair 2026 dates + aihero.dev.
- **5 Rule-12 overrides** of over-strict Haiku verdicts (CL2, CL3, CL6, CL7, CL14) + 1 dive token-mechanic reversal — all logged in [[pocock-writing-great-skills/caveats-and-corrections]].

## Key source URLs

- Talk: https://www.youtube.com/watch?v=UNzCG3lw6O0
- Skill: https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md
- Repo: https://github.com/mattpocock/skills · https://github.com/obra/superpowers
- Anthropic skills docs: https://code.claude.com/docs/en/skills
- Agent Skills open standard: https://agentskills.io/specification
- Event: https://www.ai.engineer/worldsfair/2026
- AI Hero: https://aihero.dev
