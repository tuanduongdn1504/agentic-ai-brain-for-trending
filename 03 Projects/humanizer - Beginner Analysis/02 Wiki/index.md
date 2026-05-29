# humanizer — Wiki (v108)

> *"Claude Code skill that removes signs of AI-generated writing from text."*

## 1. Identity & metadata

| Field | Value |
|---|---|
| Repo | `blader/humanizer` |
| Author | **Siqi Chen (@blader)** — San Francisco; co-founder/CEO **Runway** (FP&A platform); 4-time founder (ex-CEO Sandbox VR · ex-VP Postmates · ex-Zynga); NASA JPL alum (Congressional Space Act award); angel investor (~100 cos incl. ElevenLabs, Amplitude, Mercury); prominent AI/startup commentator. 16-year GitHub account, 870 followers. |
| Tier / archetype | **T1 Assistant Skill** / single-purpose text-transformation skill (pure-Markdown; anti-slop at the prose layer) |
| License | MIT |
| Languages | none (pure Markdown — 4 files, 94 KB) |
| Stars / forks | **21,421 ★ / 2,032 forks** (MEGA-viral; fork ratio 0.095 — very high absolute forks → "fork-and-customize-my-voice" usage) |
| Subscribers / open issues | 151 / 42 (healthy MEGA-scale engagement, NOT engagement-deficit) |
| Created / pushed | 2026-01-18 / 2026-05-27 (~131 days) |
| Velocity | **~163.5 stars/day = Pattern #52 HIGH-NOT-EXTREME** (150–300/d band) N+1 (CONFIRMED v75; cf. v73 cc-switch 195/d, v99 cmux 166.8/d) |
| Versioning | in-doc **1.0.0 → 2.7.0** with **0 GitHub releases** (versioning lives in SKILL.md/README, not GitHub releases) |
| Default branch | `main` · no topics · no homepage |

## 2. What it does

A single Claude Code skill that **detects and rewrites AI-generated writing patterns** so text reads as human-written. It analyzes against **30 documented patterns** (with before/after examples) and rewrites passages to eliminate them. Pattern categories:

- **Content:** significance inflation · notability name-dropping · vague attributions
- **Language:** AI vocabulary ("Additionally," "testament") · copula avoidance ("serves as") · synonym cycling
- **Style:** em-dash overuse · excessive boldface · title-case headings · emojis · curly quotes
- **Communication:** chatbot artifacts ("I hope this helps!") · sycophantic tone
- **Filler/hedging:** "in order to" → "to" · excessive qualification

**Voice calibration:** users supply writing samples so output matches *their* style rather than producing a generic "de-slopped" voice.

## 3. Architecture & distribution

```
humanizer/
├── SKILL.md     ← skill manifest (the 30-pattern ruleset + rewrite workflow)
├── AGENTS.md    ← agent configuration (Library-vocab #12 LLM-routing artifact)
├── README.md
└── LICENSE (MIT)
```

- **Pure-Markdown, 4-file, 94 KB** — extreme minimal footprint at MEGA-viral scale (21K★). Contrast with prior pure-Markdown T1 [[v87 claude-comstyle]] (micro-scale): same form, opposite scale.
- **Install:** clone or copy `SKILL.md` to `~/.claude/skills/humanizer/` (Claude Code) or `~/.config/opencode/skills/` (OpenCode). Multi-harness (Claude Code + OpenCode) = Pattern #84 84c light (2-harness).
- **agentskills.io conformance NOT claimed** — `SKILL.md` + `AGENTS.md` present but no spec-conformance declared → NOT counted in the Pattern #57 57k chain.

## 4. Corpus position (cross-references)

- **Pattern #88 Anti-Slop — FIRST text/prose-layer instance (PRIMARY).** Pattern #88 "Anti-Slop-Design-Curation" was CONFIRMED at v86 (N=3, sub-typology 88a framing / 88b named-rules / 88c machinery) with **design-layer** instances: [[v81 taste-skill]] ("Anti-Slop Frontend Framework") + [[v82 huashu-design]] ("Anti-AI-slop Rules") + [[v83 open-design]] ("Anti-AI-slop machinery") + [[v85 ui-ux-pro-max]] + [[v105 guizang]] (op7418 "去 AI 味/Stop Slop"). humanizer is the **first TEXT/PROSE instance** — same mechanism (named-rules + enumeration + detect/rewrite machinery = 88b+88c), new domain. → proposal to generalize #88 to domain-general "Anti-Slop-Curation."
- **Pattern #52 HIGH-NOT-EXTREME N+1** (~163.5/d; [[v73 cc-switch]], [[v99 cmux]] band-mates).
- **Pure-Markdown T1 N=2** at opposite scale — [[v87 claude-comstyle]] (micro) + v108 (MEGA). Library-vocab candidate "Minimal-Footprint MEGA-Viral Single-Purpose Skill" (4 files / 94 KB / 21K★).
- **Voice-calibration personalization** — Library-vocab candidate (provide-samples-to-match-style; explains the unusually high fork count).
- **Pattern #51 vibe-coding-spectrum** — anti-slop is the discipline pole; humanizer is its canonical text-layer artifact.
- **Pattern #19 candidate (OC layer only):** SF-founder-CEO-investor-influencer-with-viral-single-skill (Siqi Chen). Held at OC layer — graveyard-pressure caveat; not registered.
- Minor: NASA JPL lineage coincidence with [[v99 cmux]] founders (not load-bearing).

## 5. Functional fit / pilot relevance

**HIGH — Tier-1 actionable for the publishing layer.** The whole vault is LLM-generated; humanizer's targets (em-dash overuse, "Additionally," title-case headings, sycophantic "I hope this helps!", emoji) are exactly what to strip from *published* content (`03 Published/`, README, external comms). It also resonates with Storm Bear's CLAUDE.md "blunt and direct, no sugarcoat" — humanizer explicitly removes sycophantic tone + chatbot artifacts. Caveat: the vault's *internal state-blocks* are intentionally dense/jargon (not human-prose targets), so this applies to **outward-facing** content, not the state machinery. Cost-of-trial MINIMUM (single-file copy, reversible). Complementary to claude-mem v103 (memory) + claude-code-harness v107 (operating-loop).

## 6. Honest caveats

- **(a) FAILS** — Siqi Chen is SF-located (not the Asian-LOCATED cluster); Chinese-American ethnicity is non-(a)-qualifying per the v106 audit (a)-6 = strictly geographic. English-only, no locale-inclusion.
- **0 GitHub releases** despite in-doc v2.7.0 — versioning is documentary, not tagged.
- **Pattern #88 is already CONFIRMED** — this ship *generalizes its domain scope*; it does not create a new top-level pattern. Administrative-tier promotion.
- **Not a primary-language codebase** — pure Markdown; "language: null" on the API.

## Sources
- [blader/humanizer · GitHub](https://github.com/blader/humanizer)
- [Siqi Chen (@blader) · X](https://x.com/blader)
- [Siqi Chen — Co-Founder/CEO, Runway · Crunchbase](https://www.crunchbase.com/person/siqi-chen)
