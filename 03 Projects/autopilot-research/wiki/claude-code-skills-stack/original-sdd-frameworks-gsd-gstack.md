# Original Deep-Dive: GSD + G-Stack (the two SDD frameworks Eric merges)

## Source

- **GSD:** [github.com/gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) (original, author **TACHES**) + [github.com/open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) (community continuation).
- **G-Stack:** [github.com/garrytan/gstack](https://github.com/garrytan/gstack) (owner login `garrytan` — claimed to be **Garry Tan, YC President/CEO**; see flag below) + gstacks.org.
- Verified (`gh api`, 2026-06-29) — see table.

| Repo | Stars | License | Lang | Created | State |
|---|---|---|---|---|---|
| `gsd-build/get-shit-done` | **64,570★** | MIT | JavaScript | 2025-12-14 | **ARCHIVED** |
| `open-gsd/gsd-core` | 5,346★ | MIT | JavaScript | 2026-05-22 | active |
| `garrytan/gstack` | **117,834★** | MIT | TypeScript | 2026-03-11 | active |

These are two of the three frameworks Eric merges (with Superpowers) via Skill Creator.

---

## GSD ("Get Shit Done")

- **What:** a lightweight meta-prompting / context-engineering / spec-driven-development system for Claude Code + 12 other runtimes (OpenCode, Gemini CLI, Copilot, Cursor, Windsurf, Codex, Kimi, etc.).
- **Differentiator (the video's framing — CONFIRMED):** **per-agent context protection**. It fights "context rot" by breaking work into **5 isolated phases — Discuss → Plan → Execute → Verify → Ship** — where each executor runs in a **fresh ~200K-token subagent context** while the main session stays lean. Persistent artifacts (`STATE.md`, `CONTEXT.md`) survive session boundaries without context bloat.
- **Eric's named skills** ("explore / discuss / create-new-project") map to the Discuss/Plan phases (exact slash-command names not independently confirmed — open question).
- **⚠️ Governance flag:** the original `gsd-build/get-shit-done` is **ARCHIVED** (the agents report a "meme-coin / trust" incident in spring 2026 prompting a governance move to the `open-gsd` org). **Adopt the active `open-gsd/gsd-core` fork**, not the archived original. (The incident detail is single-source — treat as a reason to prefer the maintained fork, not as a verified fact.)

## G-Stack

- **What:** turns Claude Code into a "virtual engineering team" — **~23 core "specialist" slash commands** (of ~43 total commands), each a persona-prompt for a role: CEO, Eng Manager, Designer, QA Lead, Release Engineer, Security Officer, Doc Engineer.
- **Differentiator (the video's framing — PARTIAL→CONFIRMED):** **persona-based multi-perspective review**. Confirmed commands: `/plan-ceo-review` (strategy/scope-challenge), `/plan-design-review` + `/design-review` (design audit, 0–10 ratings), `/review` (staff-eng bug hunt), **`/qa`** (opens **real Playwright Chromium**, walks flows, files+fixes bugs, writes regression tests), `/qa-only`, **`/cso`** (OWASP Top-10 + STRIDE security audit), `/ship` + `/land-and-deploy` + `/canary`.
- **⚠️ Correction:** no skill literally named **"devil's advocate"** — `/plan-ceo-review` does assumption-challenging/scope-reduction, and a `/codex` mode does "adversarial challenge". The video's "CEO / design engineer / devil's advocate" is a *paraphrase* of the persona set.
- **⚠️ Identity flag:** the repo owner is `garrytan`; sources attribute it to **Garry Tan (YC)**. The star trajectory (10K in 48h) is consistent with a high-profile author, but treat "the YC CEO personally authored this" as **plausible-but-not-hard-verified**.

## How Eric composes them (with Superpowers)

`build-feature` skill routing: **brainstorm** = Superpowers · **persona plan-review** = G-Stack · **plan/isolate/execute (TDD + parallel agents)** = Superpowers · **AI-integration phase** = GSD · **browser QA** = G-Stack `/qa` · **ship/PR** = G-Stack `/ship`. A ticket-classifier skips stages by work type.

## Operator relevance

- These are the **operational reference implementations** for patterns the vault tracks: G-Stack ≈ Pattern #76 (adversarial/persona review) + persona-SDD; GSD ≈ context-isolation discipline (sibling to [[claude-code-memory-systems/_index]] context-rot framing).
- For **hireui Goal #2**, G-Stack's `/cso` (security) + `/qa` (browser) are directly useful; GSD's phase-isolation suits long multi-step agent work.
- Cross-link the operator's existing **cc-sdd** pilot: cc-sdd = architectural role-separation; G-Stack = prompt-persona variant; Superpowers = skill-routing. Three distinct SDD strata to compare.

## Install safety

Both MIT, persona/config files (Markdown/TS), no postinstall. **Use `open-gsd/gsd-core`** (the archived original gets no updates). G-Stack co-author line shows "Claude Opus 4.6" (a known hardcoded attribution quirk, not meaningful).

## Key Takeaways

- Three frameworks, three real differentiators: Superpowers=execution/TDD, GSD=context-isolation, G-Stack=persona-review+QA+security.
- Prefer the maintained **open-gsd** fork; the original is archived.
- "Devil's advocate" and "Garry Tan authored it" are soft/paraphrase claims — flagged, not load-bearing.

## Related

[[claude-code-skills-stack/original-superpowers]] · [[claude-code-skills-stack/original-skill-creator]] · [[harness-engineering/_index]] · [[workflow-ai-coding/_index]] · [[claude-code-memory-systems/_index]]
