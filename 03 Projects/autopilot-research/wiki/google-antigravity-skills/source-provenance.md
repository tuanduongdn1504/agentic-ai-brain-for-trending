# Source provenance — verification ledger & don't-re-fabricate list

> How this topic was verified, what got corrected, and the claims **not** to restate as fact. Antigravity is a brand-new platform (public preview since Nov 2025) with high confabulation risk — this article is the audit trail.

## How it was built

- **Entry point:** one Vietnamese YouTube tutorial ([UFmV7YsVqlM](https://www.youtube.com/watch?v=UFmV7YsVqlM), Dũng - Chia Sẻ Công Nghệ). Path 5 (yt-dlp). The Vietnamese `timedtext` endpoint returned **HTTP 429**; the caption was pulled with `--extractor-args "youtube:player_client=tv,web_safari,mweb"` + vtt fallback, then deduped. Raw: `raw/2026-07-01-google-antigravity-skills-rules-dung-chiasecongnghe.md`.
- **Original-resource deep-dive:** the platform itself (Google Antigravity), verified via **Workflow `wf_1e5cf2f6-5ec`** — **16 agents** (7 dimension gatherers → 7 adversarial verifiers → synthesis → completeness critic; **~816K subagent tokens, 355 tool calls, ~8 min**), each grounding claims against official Google sources, **plus operator WebFetch/WebSearch ground-checks** of the codelabs, the launch coverage, and the Cloud "choosing your surface" page.

## The two corrections the workflow made to the operator's own first read

1. **"Antigravity 2.0" is REAL and official.** The operator's quick search initially leaned "2.0 = informal creator label." **Wrong.** The workflow found the official **`cloud.google.com/blog/.../choosing-your-surface-antigravity-20-…`** page (independently WebFetched) describing **Antigravity 2.0 as a standalone desktop application** launched around **Google I/O 2026 (May 2026)**, alongside the IDE, CLI (Go), and SDK (Python). The video's title is accurate.
2. **Windsurf was a *licensing + reverse-acquihire*, not an acquisition.** Common phrasing says "Google acquired Windsurf for $2.4B." Precisely: a **~$2.4B non-exclusive licensing deal with Codeium** + hiring of Varun Mohan & key staff (July 2025). Windsurf the product remained separate (Cognition). Don't say "Google acquired Windsurf."

### Meta: a verifier misfired (the recurring pattern)

When the operator WebFetched the official Cloud "Antigravity 2.0 surfaces" page to double-check the workflow, the **WebFetch summarizer model slapped a "this appears fictional/speculative" disclaimer on it** — purely because its own knowledge cutoff predates 2026. **Its quoted page content confirmed the page is real** ("Antigravity 2.0 is a standalone desktop application…"), so the disclaimer was **overridden**. This is the same wiki-verify confabulation failure mode logged across this vault (a verifier with a stale cutoff declaring a real, post-cutoff thing "fabricated"). Trust the *quoted primary content*, not the summarizer's editorializing.

## Confabulation guard — the 11 video claims, ruled

| # | Video claim | Verdict | Correction |
|---|---|---|---|
| 1 | Skills live at `.antigravity/skills` | **REFUTED** | `.agents/skills/` (project) + `~/.gemini/config/skills/` (global); legacy `.agent/skills`. The VN caption garbled the spoken path. |
| 2 | `SKILL.md` + a `scripts/` folder (Python/PowerShell) | **CONFIRMED** (nuanced) | `SKILL.md` **required**; `scripts/`+`resources/`+`assets/` **optional**. Canonical script langs: **Python/Bash/Node** (PowerShell works, isn't the example). |
| 3 | Auto-discovery matches your request to a skill by description | **CONFIRMED** | It's **Progressive Disclosure**: agent sees name+description, loads full `SKILL.md` on semantic match. |
| 4 | Workspace vs Global scope | **CONFIRMED** | `.agents/skills/` vs `~/.gemini/config/skills/`. |
| 5 | Skill = capability, Rule = constraint; 1 rule for many skills | **CONFIRMED** | Maps to `SKILL.md` (on-demand) vs `AGENTS.md`/`GEMINI.md` (always-on). |
| 6 | Managed in Settings → Customization | **CONFIRMED** | Customizations panel (+ `/config`/`/settings` overlay). |
| 7 | Rule file = `agent.md`; entries "user global" + "agent" | **NEEDS-NUANCE** | Rules file is **`AGENTS.md`** (+ `GEMINI.md`); "user global" = global scope (`~/.gemini/…`), "agent" ≈ the project `AGENTS.md`. |
| 8 | Two build methods: manual, or ask the agent to make a skill | **CONFIRMED** (nuanced) | Manual = yes. "Auto" isn't a product feature — **the agent authors the `SKILL.md` when asked**; no `/create-skill` command. Verify the output. |
| 9 | Invoke skills by typing `/` | **CONFIRMED** | Skills surface as slash commands (`/skill-name`); also auto-load semantically. |
| 10 | Reads `.md`, not `.doc` | **CONFIRMED** | `SKILL.md`/`AGENTS.md` are Markdown. |
| 11 | "Antigravity 2.0" is a real new platform | **CONFIRMED** | Real standalone desktop app, Google I/O 2026. |

## Don't-re-fabricate list (claims to flag, not assert)

- Exact **version strings / dates** — "v1.20.3 (Mar 5 2026)", "v1.20.5 regression". Reported, unconfirmed.
- "**AGENTS.md used by 60,000+ repositories**" — directional marketing figure.
- The **6-persona names** (Sentinel/Explorer/Worker/Reviewer/Critic/Auditor) and hard limits ("max 10 nesting", "12,000-char workflows"). Single-source. The video doesn't cover personas at all.
- "**Gemini 3.5 Flash beats almost everything**" — Google's wins are on *specific* agentic/coding benchmarks.
- A "**catastrophic bait-and-switch**" event — real quota/loop bugs, but no official "catastrophe."
- A `.specify/memory/constitution.md`-style memory system — **that's this vault's / spec-kit's convention, not Antigravity's** (an agent nearly imported it; caught).
- Operational pain points (token overhead, weekly-quota lockouts, 403 bans) are **community reports as of mid-2026**, not official — label them.

## Best sources (for future ingests)

- `blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/`
- `developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/`
- `antigravity.google/docs` · `codelabs.developers.google.com/getting-started-with-antigravity-skills`
- `agentskills.io/specification` (the `SKILL.md` standard) · `anthropic.com/engineering` (Agent Skills, Dec 2025)
- `linuxfoundation.org` (Agentic AI Foundation / `AGENTS.md` governance)
- `cloud.google.com/blog/.../choosing-your-surface-antigravity-20-…`

## Open questions (carry forward)

- Exact precedence when `CLAUDE.md` + `AGENTS.md` + `GEMINI.md` all exist in one repo (for Antigravity).
- Whether skills can compose/call other skills; skill versioning & breaking-change story.
- Official failure-threshold limits for the Reason-Act-Verify loop; whether the quota/ban issues have an official fix post-mid-2026.
- Any undocumented `SKILL.md` frontmatter fields beyond `name`/`description`/`license`/`compatibility`/`metadata`/`allowed-tools`.

## Key Takeaways

- Verified by a **16-agent adversarial workflow + operator ground-checks**; two operator-first-read corrections (2.0 is real; Windsurf = licensing not acquisition).
- The **WebFetch "fictional" misfire** on a real Google page is logged as the recurring verifier-confabulation pattern — overridden by quoted primary content.
- **11/11 video claims ruled**: 8 confirmed (some nuanced), 1 refuted (the skills path), 1 needs-nuance (rule filename), plus "2.0 is real" confirmed.
- The **don't-re-fabricate list** guards the specific version/persona/adoption numbers that are unverified.
