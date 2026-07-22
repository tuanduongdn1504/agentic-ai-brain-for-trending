# Claims Scorecard

> **Verification:** adversarial refute-first Workflow `wf_dabc1f67-f9f` — 15 claim-cluster verifiers + 1 corpus-collision agent (16 agents, 0 errors / 0 empty / 0 skipped; ~711K tokens; 253 web tool calls; all Haiku 4.5). Each verifier was instructed to **refute** and to default to UNVERIFIABLE if sources were thin. Corrections are detailed in [[engineer-of-the-future/caveats-and-corrections]].

## Tally (53 checkable claims)

| Verdict | Count |
|---|---|
| **CONFIRMED** | **29** |
| **CONFIRMED-BUT-IMPRECISE** | **21** |
| **MISLEADING** | **1** |
| **UNVERIFIABLE** | **2** |
| **FALSE** | **0** |
| **FABRICATED** | **0** |

**Profile: a high-integrity bundle.** These are conference keynotes by named senior practitioners; the ideas and headline numbers hold up. The failure mode is **imprecision** (exact figures, sole-vs-co attribution, product/venue specifics) — never fabrication. Zero FALSE claims across 53.

## Notable CONFIRMED

- Addy Osmani = Director of Engineering, Google Chrome; author. Evidence/understanding/verdict + answerability framing (his essay "Own the Outer Loop").
- **Boris Cherny** (spelling correct) = creator & head of Claude Code at Anthropic.
- **Sonar 2026 State of Code Developer Survey** (Oct 2025 fieldwork, Jan 2026 release): AI code "mainstream, not marginal" (~42% of committed code, →65% by 2027); **96% don't fully trust AI code; only 48% always verify**; clean vs messy repos = ~equal pass rate but **7.2% fewer input / 8.5% fewer output tokens + ~⅓ fewer file revisits** (540 agent runs, 6 matched pairs).
- **Paul Graham** taste quote (X, Feb 2026). Karpathy **Software 1.0/2.0/3.0** (YC, June 17 2025); **coined "vibe coding"** (Feb 2 2025 → Wikipedia → Collins WotY 2025); **Waymo 2013 → "decade of agents."**
- **llms.txt**, **MCP** (Anthropic, Nov 2024; donated to Linux Foundation Dec 2025), **GitIngest**, **DeepWiki** (Cognition/Devin).
- **Cursor** (speaker **Michael Truell**, CEO): agent requests **~15× YoY**; **~30%** internal PRs fully agent; enterprise **~15% → ~75%** AI-generated.
- **Zuckerberg** "replace mid-level engineers" (Jan 2025); **Wired** vibe-coding-jobs article (Jun 2025).
- **Dec-2025 breakthrough**: **Opus 4.5 (Nov 24 2025) + GPT-5.2 (Dec 11 2025)**. **Claude Cowork built ~10 days** largely by Claude. **Codex >90% self-generated**, 4–8 parallel agents (Tibo = Thibault Sottiaux). **Peter Steinberger** (OpenClaw) **joined OpenAI Feb 2026**.
- **DHH** = Rails; **Mitchell Hashimoto** = Ghostty + HashiCorp co-founder; **Simon Willison** = Django co-creator + coined "prompt injection".
- **Harrison Chase** two-agent-types; **Ramp + Prime Intellect** domain fine-tune; **LangChain top-30 → top-5 on Terminal-Bench 2** via harness only.

## The 1 MISLEADING

- **"Boris Cherny stopped opening his IDE; Opus 4.5 wrote all his PRs"** (Orosz talk) — that exact quote ("first month I didn't open an IDE at all… Opus 4.5 wrote ~200 PRs, every single line") is **Hamel Husain's**, not Cherny's. Cherny only replied *"I feel this way most weeks."* News outlets misattributed it to "the Claude Code creator." → see caveats.

## The 2 UNVERIFIABLE

- **Ng's "Federal Reserve Bank of Philadelphia study"** — couldn't confirm; Ng's documented citations are Jevons paradox + BLS growth projections + James Bessen's ATM research.
- **"Star Wars premiered at what is now Cursor's office"** — the premiere (Northpoint Theatre, SF, May 1977) and the Dykstraflex are real; **no evidence Cursor operates from that building** (verified HQ = 33 New Montgomery St).

## Representative CONFIRMED-BUT-IMPRECISE (full list in caveats)

- Keynote's **official title** = "Don't build agents you can't answer for"; conference = **AI Engineer World's Fair 2026** (not "AIE").
- Cherny archetypes = **Prototyper / Builder / Sweeper / Grower / Maintainer** (noun forms; his June 28 2026 post).
- Hashimoto taste def omits **"consistently."**
- Wharton study: **73% = "cognitive surrender"** (their term), 80% = broader "followed wrong answer"; confidence **+~12pp** (Shaw & Nave, Jan 2026).
- Ng quote = **"100% of my tasks run through AI agents"**; PM-ratio nuance (Cagan ~1:6–10; Ng ~2 PMs/eng).
- OpenAI Chat Completions = **older/not-recommended, NOT deprecated.**
- MenuGen domain = **menugen.app.** Cursor browser = **"FastRender"** (Planner/Worker/Judge hierarchy; maintainability 1.3/5).
- Cursor senior-eng research = **Suproteem Sarkar (UChicago)**, not "Eric."
- Meta-Harness = **Stanford-led** (arXiv 2603.28052), one MIT co-author.
- OpenAI speech-to-speech v2 = **GPT-Realtime-2, May 7 2026.**
- Kent Beck ~50 yrs (from 1979); Fowler = primary author of *Refactoring* (with co-authors); Armin Ronacher = early (not "founding") Sentry engineer; Adam Wathan = one of four Tailwind creators.

## Key Takeaways

- **53 claims: 29 CONFIRMED / 21 CBI / 1 MISLEADING / 2 UNVERIFIABLE / 0 FALSE / 0 FABRICATED.**
- Failure mode is **imprecision, not error** — expected for named-practitioner keynotes.
- The one misattribution worth flagging loudly: **"stopped opening my IDE" = Hamel Husain, not Boris Cherny.**

## See also

- [[engineer-of-the-future/caveats-and-corrections]] — every correction in full · [[engineer-of-the-future/source-provenance]]
