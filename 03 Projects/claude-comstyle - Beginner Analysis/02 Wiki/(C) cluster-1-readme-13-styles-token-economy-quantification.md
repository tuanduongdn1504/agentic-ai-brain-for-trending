# (C) Cluster 1 — README 13-styles + Token-Economy-Quantification methodology

**Source**: [`README.md`](https://github.com/bsquang/claude-comstyle/blob/main/README.md) primary English version (full content fetched 2026-05-22).

## What the product is

`claude-comstyle` is a **prompt-style library** — 13 named communication styles each implemented as a short reusable prompt that you paste at the start of a Claude chat (or persist to `~/.claude/CLAUDE.md` for every session). Same answer, different presentation; you choose how Claude talks to you.

Tagline: *"Same answer. You pick the style."* Pitch: *"You control how Claude talks to you. Same answer, different style — pick the one that fits how you think."* Disclaimer: *"Tested on Claude. May work with other AI assistants — results not guaranteed."*

This is **NOT a full Claude-Code-skill bundle** (1 skill = `style-switcher`); it's primarily a **prompt collection** with a thin auto-switching skill wrapper. Distinct corpus sub-archetype from prior T1 entries.

## The 13 styles — 3-category taxonomy

### Productivity (5 styles — token-reducing)

| Style | Token impact | Prompt (verbatim) |
|---|---|---|
| 🪖 **Military** | 🟢 65-75% fewer | `Military style. Direct. No preamble. No filler. Facts only. Format: [problem] → [cause] → [fix]. Code unchanged. Technical terms intact.` |
| 🪨 **Caveman** | 🟢 65-75% fewer | `Talk like caveman. Short words. No filler. Technical substance exact. Drop: articles, pleasantries, hedging. Fragments OK. Code unchanged.` |
| 🔍 **Reality Check** | 🟢 60-70% fewer | `Reality Check mode. Honest, direct, balanced. Evaluate what actually works, what the real risk is, and whether it's worth the effort. Format: [what works] → [real risk] → [verdict: ship / rethink / scrap]. Not here to criticize. Here to give the honest take nobody else will say.` |
| 📋 **git log** | 🟢 50-65% fewer | `Respond using git commit style. Imperative verbs. No prose. Bullet points only. Max 72 chars per line. No preamble. No conclusion.` |
| 📌 **BLUF** | 🟡 20-35% fewer | `Always lead with BLUF: one sentence conclusion first, then details. Format: BLUF: <answer in one sentence> --- <details if needed>` |

### Quirky / Fun (4 styles — token-neutral-to-increasing)

| Style | Token impact | Prompt (verbatim) |
|---|---|---|
| 🧙 **Yoda** | 🔴 ~0% neutral | `Speak like Yoda. Inverted syntax always. Technical accuracy, compromise you must not. Code unchanged. Jargon intact.` |
| 🏴‍☠️ **Pirate** | 🔴 +5-15% more | `Speak like a pirate. Nautical metaphors welcome. Technical accuracy required. Code unchanged. Keep it fun but never sacrifice correctness.` |
| 💾 **80s Hacker** | 🔴 +5-15% more | `Respond like a terminal in an 80s hacker movie. All caps where dramatic. Use > prompts, ellipses, and STATUS: labels. Be theatrical but technically correct.` |
| 👨 **Dad Joke** | 🔴 +10-20% more | `Explain technically, then end every response with a related dad joke. The joke must be terrible. The explanation must be accurate.` |

### Mental Model (4 styles — token-varying, learning-oriented)

| Style | Token impact | Prompt (verbatim) |
|---|---|---|
| 🦆 **Rubber Duck** | 🔴 0 to +20% | `Explain like I'm a rubber duck. No jargon. Break every step down. Assume zero context. One concept at a time.` |
| 🔬 **Feynman** | 🔴 +20-40% more | `Use the Feynman technique. Explain to a curious 12-year-old with no CS background. No jargon without immediate plain-English definition. Build intuition before detail.` |
| ❓ **Socratic** | 🟢 50-70% per response* | `Use the Socratic method. Never give answers directly. Ask questions that lead me to discover the answer myself. Only confirm when I've reached the correct conclusion.` |
| 🧱 **First Principles** | 🔴 +20-30% more | `Use first principles thinking. Break every problem to its fundamentals. Do not accept conventional solutions without examining why they work. Build reasoning from the ground up.` |

*Socratic asterisk = saves per-response but multi-turn cost can rise.

## The Token-Economy-Quantification design axis (PRIMARY observation)

Each of the 13 styles carries an **explicit % output-token-impact rating** in the README:

- **🟢 fewer**: Military 65-75%, Caveman 65-75%, Reality Check 60-70%, git log 50-65%, Socratic 50-70%* per response
- **🟡 slightly fewer**: BLUF 20-35%
- **🔴 neutral or more**: Yoda ~0%, Pirate +5-15%, 80s Hacker +5-15%, Dad Joke +10-20%, Rubber Duck 0 to +20%, First Principles +20-30%, Feynman +20-40%

This is **CORPUS-FIRST explicit-per-style %-token-impact quantification with 3-tier badge taxonomy** at the prompt-engineering layer. No prior corpus subject quantified token-economy as a design axis at the per-style granularity. Prior subjects (v85 ui-ux-pro-max + v76 agent-skills-standard) quantified **aggregate** token economy ("85% fewer tokens" / "540 tokens/skill avg") at LDS or routing-architecture layer, but not per-style.

The 3-tier badge taxonomy (🟢🟡🔴) provides at-a-glance categorical signaling distinct from raw % range. This is **Library-vocab item PRIMARY for v87**.

## The 7-attribute-per-style schema

Each style entry in the README follows an identical schema:

1. **Title** (emoji + name)
2. **One-line tagline** describing style flavor
3. **Token savings rating** (% range + 🟢🟡🔴 badge)
4. **Prompt** (verbatim, ready to copy)
5. **Before / After table** showing default Claude vs styled output for the SAME question (with native-VN second example in 4 of 13 styles)
6. **`+ terminal CLI style` variant** showing how the universal modifier strips markdown for additional 20-30% savings
7. **Pros / Cons** + "Best for / Not suitable for" axis

This schema is consistently applied across all 13 styles = micro-LDS density (13 styles × 7 attributes ≈ 91 attribute-instances). Far below v85's 669+ codified elements, but the **schema consistency at the per-style level** is a Library-vocab candidate "Multi-Attribute Style Schema".

## The `terminal CLI style` universal modifier

A meta-prompt appendable to **any** of the 13 base styles:

> *"Want even fewer tokens? Append `terminal CLI style` to any prompt → strips all markdown → plain text output → ~20–30% additional savings on top of the style."*

Each of the 13 style sections includes a `+ terminal CLI style` example showing the further-compressed plain-text variant. This is **CORPUS-FIRST plain-text-output universal modifier appendable to any communication style** in v60+ window. Library-vocab candidate "Universal-Modifier Composable With Base Styles".

## Mix & Match — Compositional Style Mixing framework

The README dedicates a section to **explicit prompt composition**:

```
Military brevity + BLUF format. Direct. No filler.
Lead with one-sentence answer. Details only if needed.
```

```
Feynman explanation style + git log action items at the end.
```

```
Reality Check + Military. Honest verdict, no words wasted.
```

This is **CORPUS-FIRST formal Mix & Match prompt-style composition framework** in v60+ window. No prior corpus subject framed prompt composition as a first-class product feature. Library-vocab candidate "Compositional Prompt Style Mixing".

The composition supports both:
- **Within-category mixing** (Military + BLUF = both Productivity)
- **Cross-category mixing** (Feynman + git log = Mental Model + Productivity)
- **Universal modifier overlay** (any style + `terminal CLI style`)

## Persistence options stated in README

Three install-modes for any of the 13 styles:

1. **Per-chat**: Copy prompt → paste at start of chat → applies to that conversation
2. **Permanent globally**: Add prompt to `~/.claude/CLAUDE.md` → active for every Claude session on the machine
3. **Per-workspace via skill**: Use `/style` command from style-switcher SKILL.md (see Cluster 2)

The 3-tier persistence is **CORPUS-FIRST tri-layer prompt-persistence at communication-style sub-product** in v60+ window (per-chat / global-user / per-workspace skill).

## What is NOT in the README

- No author name, location, or affiliation in README (must infer from VN-language fluency + GH profile)
- No metrics/screenshots of actual token-impact measurement methodology (% ranges are stated, not measured-and-published)
- No corpus-subject ecosystem citations beyond "Claude Code and Cowork"
- No formal `skill.json` manifest (only single `SKILL.md` for style-switcher; see Cluster 2)
- No multi-platform install matrix (Claude Code + Cowork mentioned; no Cursor / Codex / etc. instructions)
- No CLI tool, no `npx`, no `npm` package
- No automated testing or eval framework for the styles
- No version number on the project (no release tags visible)

## Storm Bear direct-applicability (synthesis)

Storm Bear root [`CLAUDE.md`](../../CLAUDE.md) defines two communication rules:

1. *"Blunt and direct — challenge me, don't sugarcoat, call me out when I'm wrong"*
2. *"Always end with a suggested next action — every response should close with what to do next"*

**4 of the 13 styles directly map to these rules**:

- **Reality Check** `[what works] → [real risk] → [verdict: ship / rethink / scrap]` = rule #1 (blunt verdict) + rule #2 (verdict-as-next-action implicit)
- **git log** imperative-verb bullets + max 72 chars + no preamble = rule #2 (every bullet is an action item)
- **Military** `[problem] → [cause] → [fix]` = rule #1 (no filler) + rule #2 (fix = next action)
- **BLUF** one-sentence conclusion first = rule #1 (no burying the lede)

**Compositional candidate for Storm Bear vault sessions**:

```
Reality Check + Military + git log action items. Honest verdict, no filler, bullet next-actions.
```

This composition maps to **both** Storm Bear CLAUDE.md communication rules at once. Tier-1 actionable pilot candidate at lowest-cost-of-trial in corpus (1-min single-file copy install).
