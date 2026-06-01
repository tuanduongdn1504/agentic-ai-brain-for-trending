# Echo Loop — Wiki (v128)

> `echo-loop/Echo-Loop` · **"Echo Loop 是一款科学、高效的 AI 英语听说训练 App"** ("a scientific, efficient AI English listening-&-speaking training app") · A cross-platform **consumer language-learning app** (Flutter/Dart; iOS/Android/macOS) that drives learners through 盲听 (blind listening) → 精听 (intensive listening) → 跟读 (shadowing) → 复述 (retelling) → 间隔复习 (spaced repetition), with AI for translation, sentence/word analysis, auto-transcription, and ASR-based speaking evaluation.

**(C) Claude-generated wiki page.** Fetched 2026-06-01 (GitHub API + README). Routine v2.5, wiki #128. **⚠️ WEAK INCLUDE 1/4 — included on criterion (a) alone (China-Mainland cultural-peer); under routine v2.5 §31 this is an OFF-GOAL CAPTURE via the (a)-rescue channel, NOT a goal-aligned subject. It is a consumer English-learning app, off goal #1. See the verdict doc in `01 Analysis/`.**

---

## Identity

| Field | Value |
|---|---|
| Repo | [`echo-loop/Echo-Loop`](https://github.com/echo-loop/Echo-Loop) |
| What | **Consumer AI English listening/speaking training app** (Flutter cross-platform iOS/Android/macOS). Not a dev tool, not an agent, not a library. |
| Tier / archetype | **T5 Application** (consumer end-user app). Off the agent-*for-coding* corpus domain; an off-goal capture. |
| Stars / forks | **705★ / 40 forks** (fork_ratio ~0.057) |
| Watchers / open issues | 2 subscribers / 2 open |
| Created / pushed | 2026-05-07 / 2026-05-30 (**~25 days** old at fetch) |
| Velocity | **~28 stars/day** — short window (~25d); in the 25-150/d rate band but too young to confirm; **NOT a confirmed Pattern #52 instance** (nascent, not yet sustained) |
| License | **AGPL-3.0** (GitHub API agrees) |
| Language | **Dart** (Flutter) ~27MB; Riverpod (state) + Drift/SQLite (persistence) + Material 3 + just_audio + sherpa_onnx (on-device ASR) |
| Distribution | Consumer app builds (iOS/Android/macOS); homepage **echo-loop.top** |
| Default branch / homepage | `main` / https://www.echo-loop.top |
| Author | **`echo-loop`** (`owner.type: User`) — a **China-based developer**; the project is academically guided by **Prof. Yang Yan (杨彦), Minzu University of China, School of Foreign Languages**, with a Beijing PhD credential cited. Bilingual README (简体中文 primary + `README.en.md`). Personal developer name not clearly stated; China-Mainland origin is well-supported. |
| Topics | english-learning, language-learning, listening, speaking, spaced-repetition, flutter, ASR, AI-tutoring |

## What it is

A polished, pedagogy-driven **consumer language-learning app**. The learning loop is the product: blind-listen a clip, intensively listen (sentence-by-sentence with AI translation + word/grammar analysis), shadow (repeat aloud, scored by ASR), retell, and review on a spaced-repetition schedule. AI features (translation, sentence/word explanation, auto-caption transcription, speaking evaluation) are wired in as *components* of the tutoring experience; the README does not name a specific LLM provider, and ASR runs via native iOS/macOS recognizers plus on-device `sherpa_onnx`.

It is **not** a coding agent, a Claude-Code tool, an agentskills.io product, an MCP server, or a developer library. It is an end-user app for individual English learners. It lands in the corpus only as a cultural-peer capture (below).

## The one corpus-relevant thread (and why it doesn't flip the verdict)

The repo ships **`.claude/` + `AGENTS.md` + `CLAUDE.md`** — i.e. the developer uses **Claude Code as internal engineering discipline** to build the app. This is exactly the dograh-v122 "engineering exhaust" thread: genuinely interesting as a real-world adoption signal, but it is *how the app is built*, not *what the app is*. A large and growing fraction of repos now ship a `CLAUDE.md` + `AGENTS.md`; counting that as corpus-relevance would blow scope open. So it's recorded as an observation, not as grounds for inclusion.

This makes Echo Loop the **2nd off-goal subject whose only corpus thread is internal Claude-Code discipline** (dograh v122 + Echo Loop v128) — noted, not minted.

## Why it's in the corpus (and the honest caveat)

It clears the STRICT gate at **1/4**, on criterion (a) alone:

- **(a) PASS** — China-based developer with a declared academic anchor (Minzu University of China) + Chinese-first README = inferred/declared China-Mainland cultural-peer (the v82/v94/v100/v117/v123 cluster). This is the *only* criterion carrying the include.
- **(b) FAIL** — an English-listening/speaking app is off goal #1 ("master Claude and autonomous agents for software development"). No vault/Scrum/dev-workflow/agent utility. AI is one component of a consumer app, not a dev tool (contrast v112 freellmapi).
- **(c) WEAK** — a competent Flutter app, but off the corpus's agent/skill methodology domain; the only transferable thread is the incidental internal Claude-Code tooling above.
- **(d) WEAK** — incidental Claude-Code artifacts only; no agentskills.io chain, no MCP product, no Karpathy lineage.

→ **1/4 → WEAK INCLUDE on (a) alone** = the v80 SmartMacroAI / v123 MoneyPrinterTurbo pattern. Under **routine v2.5 §31 this is an OFF-GOAL CAPTURE via the (a)-rescue channel** — captured honestly as corpus-knowledge of a cultural-peer subject, NOT counted toward the goal-aligned streak.

**Good news vs. v127:** because it clears at 1/4, it is **NOT an operator override** — no 5th override, **no frequency-trigger trip.**

**⚠️ But it is the 3rd (a)-rescue off-goal capture** (v80 SmartMacroAI + v123 MoneyPrinterTurbo + v128 Echo Loop = **N=3**) — the channel the v125 audit flagged. v2.5 handles it correctly by tagging it OFF-GOAL CAPTURE (OG tally) rather than letting it silently pad the streak. **Soft off-goal-capture-rate watch (new in v2.5) is firing:** 2 of the last 3 ships (v127 override + v128 (a)-rescue) are off-goal; only v126 was goal-aligned.

## Honest non-claims

- **NOT** an agent-for-software-development tool; **NOT** a Claude-Code skill/plugin; **NOT** an agentskills.io implementer; **NOT** an MCP server; **NOT** a dev library.
- **NOT** a 2nd instance of v123's T5 "AI Media-Generation Pipeline App" sub-archetype (different vertical — language tutoring, not media generation); v123's N=1 stays N=1.
- **NO** new T5 sub-archetype minted here — per the v125 anti-inflation discipline, an off-goal capture should be corpus-knowledge, not pattern-fuel. (The informal "off-goal consumer AI app" grouping v123+v128 is noted, not registered.)
- **NOT** a confirmed Pattern #52 instance (~28/d, ~25-day window — nascent, not yet sustained).
- **NO** new top-level Pattern; **NO** Library-vocab promotion; **NO** Pattern Library state change. **ZERO new Library-vocab minted (§28).**

---

*See `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` for the full gate decision, and `01 Analysis/(C) Pattern-Library-Phase-4b-off-goal-capture-observation.md` for the (deliberately thin) Pattern Library contribution + the (a)-rescue N=3 finding.*
