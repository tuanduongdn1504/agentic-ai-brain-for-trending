# (C) Autopilot Loop — 2026-06-29-00

> **Trigger:** /loop autopilot research (manual, operator-submitted video URL)
> **Topic:** claude-code-skills-stack — Eric Tech "8 Claude Code Skills Every Developer Needs in 2026" (Va-U1dqhwzk)
> **Started:** 2026-06-29
> **Ended:** 2026-06-29
> **Duration:** ~1 session (single continuous arc)
> **Operator ask:** "build knowledge from this video + double deep-dive into the original resource + pilot methods for my apply"

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 video + 10 originals | 1 (cold-start topic) | 0 (12 articles + index; all 10 originals deep-dived + verified) | ~1.0 |

Cold-start topic. Scope coverage: **10/10 originals** deep-dived + adversarially verified + independently `gh api`-ground-checked.

## Sources ingested

- `raw/2026-06-29-claude-code-skills-stack-eric-tech.md` (path 5 yt-dlp, en auto-subs, 8K-word transcript; ffmpeg absent → VTT parsed via `bin/vtt-to-md.py`)
- 10 originals fetched live (WebSearch/WebFetch + `gh api`): obra/superpowers · anthropics/skills · gsd-build/get-shit-done + open-gsd/gsd-core · garrytan/gstack · nextlevelbuilder/ui-ux-pro-max-skill · voltagent/awesome-design-md + google-labs-code/design.md · microsoft/playwright-mcp + microsoft/playwright-cli · kepano/obsidian-skills · EricTechPro/startup-claude-skills + ericosiu/ai-marketing-skills + anthropics/claude-plugins-official

## Method

- **Deep-dive + adversarial verify:** Workflow `wf_04da379d-ca9` (21 agents = 9 deep-dive [Haiku] + 9 verify + 3 cross-cutting refuters; 514 tool calls; ~898K subagent tokens; ~6.8 min).
- **Independent ground-check (main loop):** `gh api repos/<owner>/<repo>` for all 15 cited repos — confirmed every star count / license / created-date / archived-state against the live GitHub API (2026-06-29). The Haiku agents' suspiciously-high star counts (Superpowers 241K etc.) turned out **accurate**; the grounding also confirmed the structural corrections (kepano = personal repo; `obsidianmd/obsidian-skills` = 404; Eric's skills public; marketing = Eric Osiu).

## Wiki articles created (12 files, NEW topic)

- `wiki/claude-code-skills-stack/_index.md` (NEW)
- `wiki/claude-code-skills-stack/overview.md` (NEW)
- `wiki/claude-code-skills-stack/the-eight-skills.md` (NEW)
- `wiki/claude-code-skills-stack/original-superpowers.md` (NEW)
- `wiki/claude-code-skills-stack/original-skill-creator.md` (NEW)
- `wiki/claude-code-skills-stack/original-sdd-frameworks-gsd-gstack.md` (NEW)
- `wiki/claude-code-skills-stack/original-design-skills.md` (NEW)
- `wiki/claude-code-skills-stack/original-playwright-cli-vs-mcp.md` (NEW)
- `wiki/claude-code-skills-stack/original-obsidian-kepano.md` (NEW)
- `wiki/claude-code-skills-stack/original-fix-ticket-marketing-telegram.md` (NEW)
- `wiki/claude-code-skills-stack/video-to-original-crosswalk.md` (NEW)
- `wiki/claude-code-skills-stack/source-provenance.md` (NEW)
- `wiki/_master-index.md` (UPDATED — added topic #28)
- `raw/_inventory.md` (UPDATED — added compiled row)
- `output/(C) 2026-06-29-claude-code-skills-stack-pilot-methods.md` (NEW — 22 ranked methods across 4 flows + skip-list + critic reframe)

## Final metric

- `gaps_closed_ratio` ≈ **1.0** (cold-start; topic fully populated, 10/10 originals covered)
- Stop reason: scope complete (single cycle; all originals deep-dived + verified + ground-checked + pilot deliverable shipped)

## Key corrections (Rule 12 — fail loud)

1. **Superpowers** is **Shell/JS, not Markdown**; video's "tests-before-execute" order is wrong (TDD runs *during* execution).
2. **UI UX Pro Max** is a **deterministic CSV reasoning engine**, NOT "trained on hundreds of datasets".
3. **Obsidian skill** = Steph Ango's **personal** repo (`obsidianmd/obsidian-skills` = 404), and is a **format-handling skill, not a RAG** (the RAG is the Karpathy LLM-Wiki pattern this vault runs).
4. **Eric's /fix-ticket + Playwright skills are PUBLIC** (`EricTechPro/startup-claude-skills`, MIT), not gated.
5. **"43 marketing skills" are Eric Osiu's** (`ericosiu/ai-marketing-skills`), cited not authored.
6. **GSD original is archived** → use `open-gsd/gsd-core`.
7. **"/fix-ticket replaces 90% of junior jobs"** + **"0→1000 users from these skills"** = hyperbole/unverifiable.
8. **design.md** genuinely originated in **Google Stitch** (May 2025; open-sourced ~April 2026) — not a prior community convention.

## Top-3 unclosed gaps

1. **Pilot not yet deployed** — the headline methods (A1 compose-+-eval merged skill vs cc-sdd; C1 hireui TDD ticket) are *recommended*, not executed. Goal #2 still resolves only via actual deployment.
2. **"Garry Tan authored G-Stack"** + **GSD "meme-coin/governance incident"** are soft/single-source — repo facts verified, the celebrity-author + incident narrative flagged.
3. **Eric's specific in-video demos** (16-phase QA, exact merged-skill internals) are gated/unverifiable beyond the transcript.

## Suggested next action

Per the pilot file's Start-Here: **Week 1** install `kepano/obsidian-skills` in both vaults (zero-risk format upgrade) + sandbox Superpowers; **Week 2** run one real hireui ticket through a TDD harness + Playwright CLI QA (hireui-rooted, I-2/I-8); **Week 3** build the merged `build-feature` skill and EVAL it against cc-sdd via Skill Creator — that benchmark is the Goal #2 evidence currently missing. Consider Pattern Library evidence (Superpowers/GSD/G-Stack → #21/#76) at the next Storm Bear mini-audit.
