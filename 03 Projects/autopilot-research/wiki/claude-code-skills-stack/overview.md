# Overview — Eric Tech's 8-Skill Claude Code Stack

## Source

- Video: Eric Tech — "8 Claude Code Skills Every Developer Needs in 2026" ([Va-U1dqhwzk](https://www.youtube.com/watch?v=Va-U1dqhwzk), 2026-04-24, 32:52, 10.3K views).
- Raw transcript: `raw/2026-06-29-claude-code-skills-stack-eric-tech.md` (path 5 yt-dlp en auto-subs).
- Presenter: "Eric Tech" (GitHub `EricTechPro`) — ex-Amazon SDE L6 (6 yrs), ex-Microsoft; founder of **BookZero.ai** (live AI-bookkeeping SaaS); runs skool.com/erictech.

## The thesis

Out-of-the-box Claude Code is powerful but "chaotic" — it starts writing code with no planning, no tests, no methodology ("vibe coding"). Eric's stack is a **layered set of skills** that impose discipline and extend reach, ordered from foundation to advanced workflow:

1. **Discipline layer** — Superpowers (TDD/spec-first methodology) + Skill Creator (build your *own* methodology)
2. **Design layer** — UI UX Pro Max (design-system generation) + Awesome Design MD (copy a brand's `design.md`)
3. **Eyes-and-hands layer** — Playwright CLI (browser QA: screenshots + console logs → QA report)
4. **Memory layer** — Obsidian (a markdown folder as zero-overhead knowledge system)
5. **Growth layer** — "43 marketing skills" (SEO/copy/email/CRO)
6. **Automation layer** — /fix-ticket (Sentry/Jira → reproduce → fix → deploy → handoff)

## The load-bearing meta-move (skill #2 in action)

The most transferable idea in the video isn't any single skill — it's the **composition pattern**: use the first-party **Skill Creator** to *merge the best stage of each rival SDD framework into one custom skill*. Eric builds a `build-feature` skill that routes:

- **brainstorm** → Superpowers (spec-first clarification)
- **plan / persona review** → G-Stack (CEO / design / devil's-advocate perspectives)
- **plan write + env isolation + execute (TDD + parallel agents)** → Superpowers
- **AI-integration phase** → GSD
- **QA in browser** → G-Stack `/qa`
- **ship / PR** → G-Stack `/ship`

…with a **classify-the-ticket-first** front door (small/medium/large; UI/API/full/infra) that *skips* stages by work type (e.g., skip browser QA on an API-only change; skip brainstorm on a high-complexity-but-well-understood task). This is the operator's own [[harness-engineering/_index]] "harness-is-the-box" thesis applied at the skill-composition level.

## What's genuinely useful vs marketing

- **Keepers (real, free, high-leverage):** Superpowers (TDD harness), Skill Creator (first-party; the eval-driven build loop), the Playwright **CLI** approach (token-efficient QA), the Obsidian skill (you already run this pattern), the *composition* meta-move.
- **Design layer:** real and useful, but the operator already has a stronger, already-surfaced option — the **Taste Skill** ([[ai-web-design-workflow/_index]]) — plus Anthropic's first-party `frontend-design`. UI UX Pro Max and Awesome Design MD are alternatives/complements, not requirements.
- **Marketing layer:** the "43 skills" are **Eric Osiu's** `ai-marketing-skills`, *cited* by Eric, not his. Lower relevance to the operator (no consumer-SaaS marketing motion right now).
- **Hype to discount:** "/fix-ticket replaces ~90% of junior engineer jobs" (hyperbole; real signal = managers freezing junior hiring), "43 skills took BookZero 0→1000 users" (unverifiable single-channel attribution).

## Provenance headline

Every original was deep-dived + adversarially verified (`wf_04da379d-ca9`, 21 agents) and then **independently ground-checked against the live GitHub API** (`gh api`, 2026-06-29). All 10 originals are confirmed-real with accurate star counts. The corrections are about *framing*, not existence — see [[claude-code-skills-stack/source-provenance]].

## Key Takeaways

- The real product is a **layered, composable skill stack**, not 8 isolated tools — and the spine is Skill-Creator-driven composition.
- Three rival SDD frameworks exist and each has a genuine differentiator: **Superpowers** = TDD/subagent execution; **GSD** = per-agent context isolation; **G-Stack** = persona-based multi-perspective review + browser QA + security.
- The Obsidian skill is the operator's *own* pattern made first-party-adjacent (by Obsidian's CEO, personally) — high relevance, low novelty.
- The video's value for the operator is **discipline + composition**, not discovery — most of these map onto patterns the vault already tracks.

## Related

[[claude-code-skills-stack/the-eight-skills]] · [[claude-code-skills-stack/original-superpowers]] · [[claude-code-skills-stack/original-skill-creator]] · [[claude-code-skills-stack/video-to-original-crosswalk]] · [[claude-skills/_index]] · [[harness-engineering/_index]] · [[ai-web-design-workflow/_index]]
