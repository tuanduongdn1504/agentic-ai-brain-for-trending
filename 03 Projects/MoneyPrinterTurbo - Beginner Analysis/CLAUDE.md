# MoneyPrinterTurbo — Project Context

**Subject:** [`harry0703/MoneyPrinterTurbo`](https://github.com/harry0703/MoneyPrinterTurbo) — "利用AI大模型，一键生成高清短视频 / Generate short videos with one click using AI LLM."
**Wiki version:** v123 (Routine v2.4).
**Status:** SHIPPED 2026-05-30. **WEAK INCLUDE 1/4** ((a) PASS inferred-China-Mainland; (b) FAIL; (c) WEAK; (d) WEAK). 1st clean PASS after the v122 dograh OVERRIDE.

## One-line

A faceless **short-video generator**: give it a topic/keyword and it auto-produces the script (via one of 13 LLM providers), pulls stock footage, generates voiceover + subtitles + background music, and composites a 1080p TikTok/Shorts video. Python 97.9% (Streamlit WebUI + FastAPI + MoviePy), MIT, **70,294★ / 10,136 forks**, created 2024-03-11 (~810 days), ~86.8★/day SUSTAINED-MODERATE-HIGH (mega-cumulative). Author **harry0703** = inferred China-Mainland solo indie dev.

## Why this is a (legitimate but WEAK) INCLUDE

Phase 0.9 STRICT = **1/4**. The include rests **entirely on (a)** — harry0703 is an inferred China-Mainland solo indie developer (Chinese-primary README, solo account), an Asian-cluster cultural-peer (cf. v100 Easydict / v117 CodexPlusPlus inferred-PASS). **(b) FAILs** (faceless-video tool, not software-dev/agents — no goal-#1 utility), **(c)/(d) WEAK** (off the corpus's agent/skill methodology domain; **zero** agent/skill/Claude/MCP surface). 

**Honest kicker:** the corpus's prior faceless-content subject (v5x `automate-faceless-content`) was OUTSIDE-SCOPE; the faceless domain has precedent for being out. (a)-cultural-peer is the *only* thing rescuing this into a WEAK INCLUDE — the exact v80 SmartMacroAI pattern (1/4, (a)-only). It's **corpus-knowledge of a hugely-popular cultural-peer subject, NOT goal-#1 progress**, and the 2nd off-goal-domain subject in a row (after v122 dograh).

## Pattern Library impact

**PRIMARY (NEW T5 sub-archetype, PROVISIONAL N=1):** "AI Media-Generation Pipeline App (faceless short-video)" — a standalone deployable app whose pipeline is *LLM-script → stock-footage retrieval → TTS voiceover → Whisper/edge subtitles → BGM → composite render*. Corpus-first **in-scope** standalone AI-video-generation app (distinct from v84 image-blaster's Claude-skill-bundle form, and from the OUTSIDE-SCOPE v5x faceless *course*). **SECONDARY (administrative / within-pattern, NO new standalones):** Pattern #52 SUSTAINED-MODERATE-HIGH N+1 (very-long 810d sustenance + 70K★ mega-cumulative — near the LONG-SUSTAINED-MEDIUM boundary); Pattern #84 cross-vendor-tolerance N+1 (13 LLM providers via `config.toml`); China-Mainland cluster N+1 (v82/v94/v100/v117/v119 + v123); Pattern #82 quantitative-marketing (thin, "一键生成"). 

**§28: ZERO new Library-vocab minted** — a WEAK off-domain subject should not expand the vocabulary; registry `06` NOT moved. The one meta-observation worth tracking — **"(a)-cultural-peer rescue of an off-goal-domain subject into WEAK-INCLUDE-on-(a)-alone" N=2 (v80 SmartMacroAI + v123)** — is **surfaced to the mandated v124 Phase 0.9 audit** (which is already reviewing how off-goal subjects enter the corpus, post the v122 2-in-20 override trip), not minted as vocabulary.

**Honest non-claims:** NOT a Pattern #18 #8 "Multi-Source LLM Aggregator" instance (it's a consumer *app* with multi-provider config, not a dedicated aggregator/proxy/switcher like cc-switch/freellmapi/CodexPlusPlus — claiming it would dilute #8's just-CONFIRMED-N=3 status); NOT an agent/skill/Claude-Code/agentskills.io subject; NOT a pilot. State UNCHANGED (46 confirmed / ~25 active / 8 Library-vocab CONFIRMED). Streak "47+3\*" → "48+3\*".

## Files

- `02 Wiki/index.md` — the wiki page.
- `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` — the WEAK INCLUDE 1/4 gate + the "(a)-rescue N=2" audit input.
- `01 Analysis/(C) Pattern-Library-Phase-4b-T5-AI-Media-Generation-Pipeline-N1.md` — the PRIMARY sub-archetype + secondaries + honest non-claims.

## Pilot note

**NOT a pilot — corpus-knowledge only.** A faceless short-video generator serves no part of Storm Bear's software-dev / Scrum / LLM-wiki work; it does not join the operational Claude-Code-adjacent stack. The only conceivable use is personal content/marketing, which is not goal #1.
