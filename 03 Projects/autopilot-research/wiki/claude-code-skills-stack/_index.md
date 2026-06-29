# Topic: claude-code-skills-stack

> **Eric Tech's "8 Claude Code Skills Every Developer Needs in 2026"** + a double deep-dive into the original resource behind each skill. A *workflow/dev* skill stack (foundation → design → QA → memory → marketing → bug-fix), distinct from the *meta*-skills in [[claude-skills/_index]] (Ben AI).
> **Compiled:** 2026-06-29 (path 5 yt-dlp full transcript + direct primary-source fetch + adversarial workflow verification `wf_04da379d-ca9` + independent `gh api` ground-check of every repo).
> **Source video:** Eric Tech — "8 Claude Code Skills Every Developer Needs in 2026" ([Va-U1dqhwzk](https://www.youtube.com/watch?v=Va-U1dqhwzk), 2026-04-24, 32:52, 10.3K views). Paid community: skool.com/erictech ($19→$99/mo).

---

## The premise

A self-described ex-Amazon (L6, 6 yrs) / ex-Microsoft engineer building **BookZero.ai** (a real, live AI-bookkeeping SaaS, ~1.2K users) walks through the 8 Claude Code skills he uses daily — from a TDD-enforcing foundation, through design + browser-QA, to a memory layer and a full automated bug-fix workflow. The load-bearing meta-move: **use Anthropic's Skill Creator to merge the best of three rival SDD frameworks (Superpowers + GSD + G-Stack) into one custom "build-feature" skill.** See [[claude-code-skills-stack/overview]].

## The 8 skills → their originals (all GitHub stars `gh`-verified 2026-06-29)

| # | Skill | Original | Verified |
|---|---|---|---|
| 1 | Superpowers | `obra/superpowers` (Jesse Vincent) | 240.9K★ MIT, Shell/JS |
| 2 | Skill Creator | `anthropics/skills` skill-creator | first-party, 156.4K★ |
| 3 | UI UX Pro Max | `nextlevelbuilder/ui-ux-pro-max-skill` + `uipro-cli` | 97.6K★ MIT (CSV lookup, not "trained") |
| 4 | Awesome Design MD | `voltagent/awesome-design-md` + Google Stitch `design.md` | 94.1K★ / 23K★ |
| 5 | Playwright CLI | `microsoft/playwright-cli` vs `microsoft/playwright-mcp` | 11.7K★ / 34.5K★ |
| 6 | Obsidian | `kepano/obsidian-skills` (Steph Ango, **personal** repo) | 38.8K★ MIT |
| 7 | "43 Marketing Skills" | `ericosiu/ai-marketing-skills` (**Eric Osiu**, not Eric Tech) | 2.7K★ MIT |
| 8 | /fix-ticket | `EricTechPro/startup-claude-skills` (Eric's own) | 51★ MIT, **public** |
| + | GSD, G-Stack | `gsd-build/get-shit-done` (archived) / `garrytan/gstack` | 64.6K★ / 117.8K★ |

## Articles

- [[claude-code-skills-stack/overview]] — the stack thesis, the 8 skills, the merge-via-Skill-Creator meta-move, the operator-relevance headline, provenance summary
- [[claude-code-skills-stack/the-eight-skills]] — full per-skill catalog (problem / what / how / install / public-or-gated / corrections)
- [[claude-code-skills-stack/original-superpowers]] — **the foundation:** Jesse Vincent's 7-stage TDD pipeline, what the video gets wrong about the order, v6.0 token-cut, parallel agents
- [[claude-code-skills-stack/original-skill-creator]] — first-party Anthropic skill-creator: Create→Eval→Improve→Benchmark, the grader/comparator/analyzer agents, "2.0" (2026-03-03)
- [[claude-code-skills-stack/original-sdd-frameworks-gsd-gstack]] — the two frameworks Eric merges: GSD (context-isolation, archived→open-gsd) + G-Stack (persona review, /qa, /cso)
- [[claude-code-skills-stack/original-design-skills]] — UI UX Pro Max (CSV reasoning engine) + Awesome Design MD + the `design.md` / Google Stitch origin; vs the Taste Skill + Anthropic frontend-design
- [[claude-code-skills-stack/original-playwright-cli-vs-mcp]] — CLI (disk snapshots, ~68-token schema) vs MCP (state-into-context, ~4× tokens); the genuine tradeoff
- [[claude-code-skills-stack/original-obsidian-kepano]] — the Obsidian-CEO skill (real, but **personal** not official; and it is **not** itself a RAG — it composes with the Karpathy LLM-Wiki pattern this vault runs on)
- [[claude-code-skills-stack/original-fix-ticket-marketing-telegram]] — Eric's own /fix-ticket workflow (public), the misattributed marketing skills, the official Telegram/Sentry/Jira/Vercel integrations
- [[claude-code-skills-stack/video-to-original-crosswalk]] — every skill → source → what Eric adds → what the video gets wrong/omits
- [[claude-code-skills-stack/source-provenance]] — verification ledger: confirmed / corrected / flagged (incl. the independent `gh api` ground-check)

## Pilot

Ranked methods to apply the stack to the operator's flows: `output/(C) 2026-06-29-claude-code-skills-stack-pilot-methods.md` (methods across autopilot-vault / Storm-Bear-vault / hireui-Goal-#2 / Claude-Code-harness / Scrum-coaching, + skip list + critic's reframe).

## Cross-links

- [[claude-skills/_index]] — **sibling "8 skills" video** (Ben AI's 8 *meta*-skills); distinct list, same SKILL.md substrate. Eric's #2 Skill Creator ≈ Ben's #8 MCP Builder (both first-party `anthropics/skills`).
- [[harness-engineering/_index]] — the SDD frameworks (Superpowers/GSD/G-Stack) are individual-scale harness instances; Pattern #21 SDD-emergence + #76 adversarial-review evidence
- [[workflow-ai-coding/_index]] — SDD / plan-first methodology lineage
- [[ai-web-design-workflow/_index]] — the design skills vs the **Taste Skill** (the operator's already-surfaced design lever for hireui)
- [[claude-code-memory-systems/_index]] — Obsidian skill = the L1/L5 substrate; Karpathy LLM Wiki = this vault
- [[prompt-evaluation/_index]] — Skill Creator's eval loop = the operator's grading discipline
- [[telegram-remote-control-stack/_index]] — the Telegram skill (already piloted Recipe A)
- [[claude-api-cost-optimization/_index]] — CLI-vs-MCP token economics + Superpowers v6.0 cost-cut
- [[multi-agent-orchestration/_index]] — Superpowers parallel agents / subagent-driven dev
- [[10x-claude-code/_index]] — Eric Tech is already a cited creator there

## Source provenance (headline)

Primary-source-grounded + adversarially verified (`wf_04da379d-ca9`, 21 agents) + **independently `gh api`-ground-checked** (every repo's stars/license/created-date confirmed against the live API 2026-06-29). All 10 originals are confirmed-real. Key corrections: Superpowers is **Shell/JS not Markdown** + the video's pipeline order is wrong (TDD runs *during* execution, not before); UI UX Pro Max is a **bundled-CSV reasoning engine, not "trained on datasets"**; the Obsidian skill is Steph Ango's **personal** repo (not official Obsidian org — `obsidianmd/obsidian-skills` is a 404) and is **not itself a RAG**; Eric's skills are **public, not gated**; the "43 marketing skills" are **Eric Osiu's**, cited not authored; "/fix-ticket replaces 90% of junior jobs" is hyperbole. Full log: [[claude-code-skills-stack/source-provenance]].
