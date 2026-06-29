# Claude meta-skills (Ben AI's 8) — overview

*Eight cross-task "meta-skills" for Claude that get sharply more useful once you run a second brain — exactly the operator's situation.*

## What Claude Skills are

- **Agent Skills** = reusable capabilities packaged as a `SKILL.md` file: YAML frontmatter (`name` + `description`) + a Markdown body + optional bundled scripts/resources. See [[claude-skills/original-anthropic-agent-skills]] for the format.
- **Progressive disclosure** is the load-bearing trick: only `name`+`description` (~100 tokens/skill) preload; the full `SKILL.md` loads when Claude judges the task relevant; bundled files load on demand. Unbounded skill complexity, minimal context cost.
- **Cross-surface:** skills run in Claude.ai, **Claude Cowork**, Claude Code, the Agent SDK / Developer Platform, and 40+ third-party agents (Cursor, Copilot, Gemini CLI, Kiro, OpenHands…) via the open `agentskills.io` standard.

## What Ben AI means by "meta-skills"

- Not workflow-specific (sales, HR, a given report). **Cross-task upgrades** that improve Claude's output on *anything*.
- His recurring thesis: these skills *"get MUCH more powerful when you have a second brain / OS set up"* — they auto-pull context from your workspace so they don't re-ask what you've already documented.
- **Why this matters for the operator:** you run two Karpathy-style LLM-Wiki vaults plus a disciplined `~/.claude` memory. Ben's "second-brain multiplier" isn't aspirational for you — it's your baseline. These skills compound with what you already have; they don't rescue a missing foundation. Full applications: see the pilot menu in `output/`.

## The 8 meta-skills at a glance

| # | Skill | One-line | Original it derives from |
|---|---|---|---|
| 1 | **Process Interviewer** | Grills you with 10–15+ Qs to pin down a *fuzzy* process before building a skill; outputs a confirmed summary → PRD | Matt Pocock "grill me" + Anthropic skill best-practices ([[claude-skills/original-matt-pocock-grill-me]]) |
| 2 | **Prompt Master** | Turns a messy brain-dump into a structured, best-practice prompt; can auto-run | Anthropic prompt-engineering ([[claude-skills/original-prompt-engineering-best-practices]]) |
| 3 | **Humanizer** | Strips AI-writing tells from anything going public | Wikipedia "Signs of AI writing" ([[claude-skills/original-wikipedia-signs-of-ai-writing]]) |
| 4 | **Fact Checker** | Evidence-based claim verification + web cross-reference | verification methodology (no single source) |
| 5 | **Find Skills** | Discovers skills from the skills.sh marketplace | skills.sh / Vercel ([[claude-skills/original-skills-sh-marketplace]]) |
| 6 | **Front-end Slides** | Animated HTML decks from scratch or from PPT; brand-tokenized | slide-design best practices (methodology) |
| 7 | **Decision Toolkit** | First-principles decision framework ("guide, don't decide") + HTML wizard | decision science / first-principles (methodology) |
| 8 | **MCP Builder** | Scaffolds a custom MCP server from a target API's docs | ✅ the real official `mcp-builder` skill ([[claude-skills/original-mcp-builder-and-mcp]]) |

**Bonus skills Ben mentions** (less load-bearing, ⚠️ implementations not independently verified): **agent-browser** (claims to beat native browser use), **audio-transcriber** (any audio/video on any site), **OpenRouter** (test the same prompt across Gemini/GPT/etc.).

## Provenance summary (read [[claude-skills/source-provenance]] for the full ledger)

- **Verified real:** Agent Skills + progressive disclosure; Matt Pocock grill-me; Wikipedia "Signs of AI writing"; skills.sh (Vercel; its #1 skill literally *is* "find-skills", #2 "frontend-design"); Anthropic prompt-engineering + Prompt Improver; **`mcp-builder` as a genuine Anthropic skill** (confirmed in `github.com/anthropics/skills`, 2026-06-20).
- **Corrected from the video:** Ben's "**91,000 skills**" is just the count at video time — skills.sh now reports **788,224** (a growth/metric figure, not a contradiction).
- **Naming nuance:** Ben's "**Prompt Master**" is a community skill, not Anthropic's official "**Prompt Improver**" — same idea, different thing.
- **Flagged ⚠️:** the exact internals of Ben's own skills (Humanizer/Fact-Checker output formats, the free plugin's contents), the bonus skills, and his marketing claims are not independently verified.

## What this topic does NOT do

This is a **fast-cadence research note**, not operational memory and not the Storm Bear curated wiki. It captures the video + its originals + a pilot menu. It deliberately does not import the Storm Bear Pattern-Library taxonomy.

## Navigation

- [[claude-skills/the-eight-meta-skills]] — the full per-skill catalog (problem / what / demo / install / chain)
- [[claude-skills/original-anthropic-agent-skills]] — SKILL.md format, progressive disclosure, cross-platform
- [[claude-skills/original-matt-pocock-grill-me]] — Process Interviewer's lineage
- [[claude-skills/original-wikipedia-signs-of-ai-writing]] — the Humanizer's reference catalogue
- [[claude-skills/original-skills-sh-marketplace]] — the Find-Skills ecosystem + supply-chain risk
- [[claude-skills/original-mcp-builder-and-mcp]] — the real `mcp-builder` skill + MCP primer
- [[claude-skills/original-prompt-engineering-best-practices]] — Prompt Master's basis + the official Prompt Improver
- [[claude-skills/video-to-original-crosswalk]] — every skill → its source, what's added, what's omitted
- [[claude-skills/source-provenance]] — verification ledger

**Cross-topic:** [[ai-operating-system/_index]] (Ben AI's sister video; the second-brain thesis) · [[claude-cowork/_index]] (the surface Ben demos on) · [[claude-code-memory-systems/_index]] (progressive disclosure ≈ memory layering) · [[prompt-evaluation/_index]] (Fact Checker vs eval rigor) · [[claude-api-cost-optimization/_index]] (progressive disclosure = token discipline) · [[harness-engineering/_index]].

## Source

- **Video:** Ben AI — "8 Claude Skills I Can't Live Without" (YouTube `bXnRA3pJavE`, 2026-04-18, ~20 min, 147K views). Free plugin: `c.benai.co/8csiu-free` ⚠️ (URL not independently re-verified).
- **Raw:** `raw/(C) 2026-06-20-ben-ai-8-claude-skills.md` (full transcript via yt-dlp).
- **Standards:** `github.com/anthropics/skills`, `platform.claude.com/docs/.../agent-skills`, `skills.sh`, `agentskills.io`.

## Key Takeaways

- **Skills are cross-task upgrades, not one-off macros** — and progressive disclosure is what makes a big library cheap to keep loaded.
- **The second brain is the multiplier** — and the operator already has two. The value here is *formalize + chain + auto-run*, not "discover."
- **7 of 8 trace cleanly to real originals; 1 (MCP Builder) is genuinely first-party Anthropic.** The only soft spots are Ben's own skill internals and his marketing.
- **Discovery (Find Skills) carries real supply-chain risk** — see the Snyk data in [[claude-skills/original-skills-sh-marketplace]]; vet before installing.
