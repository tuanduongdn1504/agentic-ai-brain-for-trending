# (C) Phase 0 + Phase 0.9 INCLUDE verdict — MoneyPrinterTurbo (v123)

**Routine:** v2.4. **Fetched:** 2026-05-30 (GitHub API + README + README-en + owner profile + root-contents listing). **Verdict:** **WEAK INCLUDE 1/4** ((a) PASS inferred-China-Mainland; (b) FAIL; (c) WEAK; (d) WEAK). 1st clean PASS after the v122 dograh OVERRIDE.

> ✅ **Cadence:** v120 mini-audit (2026-05-30) cleared the cadence — "v121+ = wikis OK; next natural audit ~v124–v125." v123 is the 3rd wiki of the post-v120 window (v121 CodexKit + v122 dograh + v123). ⚠️ The ~v124 audit is already **MANDATED** to review Phase 0.9 STRICT (v122 dograh tripped 2-in-20); v123 adds an "(a)-rescue N=2" input to that review (below).

---

## Phase 0 — scope gate

| Gate | Result |
|---|---|
| Repo reachable + readable | ✅ `harry0703/MoneyPrinterTurbo` |
| License present | ✅ **MIT** (GitHub API `mit`) |
| Active / recently pushed | ✅ pushed 2026-05-30; created 2024-03-11 (~810 days) |
| Scale floor (≥1★) | ✅ **70,294★** / 10,136 forks (fork_ratio 0.144) — mega-scale |
| Tier classification | **T5 Application** — a deployable, self-hostable app (Streamlit WebUI + FastAPI). **NEW sub-archetype candidate: "AI Media-Generation Pipeline App (faceless short-video)."** |

**Phase 0 = PASS on the mechanical gates, but FLAGGED off-goal-domain.** This is a faceless short-video generator (TikTok/Shorts content). It is an *application that uses LLMs* (13 providers, for the script-generation step), not a coding agent, not a Claude-Code tool, not an agent-skill. The corpus's prior faceless-content subject (v5x `cporter202/automate-faceless-content`) was classified **OUTSIDE-SCOPE** — so the domain has precedent for being out.

---

## Phase 0.9 — STRICT 4-criterion INCLUDE filter

### (a) Author cultural-peer to Storm Bear — **PASS (inferred)**

Owner = **harry0703** (`owner.type: User`), a solo indie developer. Profile location/bio undeclared, but the signals point to **China-Mainland / Chinese-heritage** with high confidence: (1) **Chinese-primary README** (`README.md` is Simplified Chinese; `README-en.md` is the English secondary); (2) Chinese-language project descriptions across his repos ("利用AI大模型…", and his other repo AudioNotes "快速提取音视频内容…"); (3) targeting a Chinese-speaking developer audience. This is inference-tolerant evidence comparable to **v117 CodexPlusPlus** (inferred-PASS China-Mainland on community signals) and **v100 Easydict** (inferred/declared Chinese-Mainland). Per §8 PROBABLE-PASS discipline, recorded as **PASS-equivalent, flagged inferred** (re-anchor at next audit if a profile field later declares otherwise).

Extends the China-Mainland sub-cluster (v82 huashu / v94 Lum1104 / v100 Easydict / v117 CodexPlusPlus / v119 nature-skills + **v123**). Storm Bear is Vietnamese → Asian-cluster cultural peer. No new (a) sub-axis (China-Mainland is well established). **(a) PASS (inferred).**

### (b) Goal-relevance / vault-utility — **FAIL**

Documented #1 goal: *"Master Claude and autonomous agents for software development."* MoneyPrinterTurbo generates **faceless short videos** for TikTok/YouTube Shorts — a content/marketing tool.
- Not a vault tool, not a Scrum tool, not a coding assistant, not an agent.
- Storm Bear (software dev + Scrum coach) has no indicated faceless-video use case.
- It orchestrates 13 LLM providers, but **only for the script-generation step** — it is not an LLM dev-utility the way v112 freellmapi (a multi-provider *proxy*) was. The LLM is one component of a video pipeline.
- The single conceivable use (personal content/marketing) is not goal #1.

**(b) FAIL.** (Same domain as the OUTSIDE-SCOPE v5x faceless subject; the difference here is (a), not (b).)

### (c) Instructive / exemplary — **WEAK**

Genuinely competent software: a clean **MVC** split (Streamlit WebUI + FastAPI API + MoviePy pipeline), a **pluggable 13-provider LLM abstraction** (provider selected via `config.toml`), and an end-to-end automated media pipeline (script → footage → TTS → Whisper/edge subtitles → BGM → composite). **But that instruction lives in a different domain** (media generation), and the corpus's Pattern Library tracks agent/skill/distribution/governance methodology. The one mildly-transferable nugget is the multi-provider LLM config layer (see (d)). Calling (c) a PASS would launder "well-built video app" into "instructive for our agent corpus." It isn't.

**(c) WEAK** — instructive-but-off-domain.

### (d) Corpus connectivity — **WEAK**

- **13 LLM providers** (OpenAI / Moonshot / Azure / gpt4free / one-api / Qwen / Gemini / Ollama / DeepSeek / MiniMax / ERNIE / Pollinations / ModelScope) → **Pattern #84 cross-vendor-tolerance** N+1. Honest non-claim: this is **NOT a Pattern #18 #8 "Multi-Source LLM Aggregator"** instance — #8's confirmed members (cc-switch / freellmapi / CodexPlusPlus) are *dedicated aggregators/proxies/switchers*; MoneyPrinterTurbo is a consumer *app* with multi-provider config. Counting it would dilute #8's just-CONFIRMED-N=3 status (v120 flagged exactly this watch).
- **China-Mainland cluster** N+1 (v82/v94/v100/v117/v119).
- **Faceless-content domain-sibling** — but the sibling (v5x automate-faceless-content) was itself OUTSIDE-SCOPE, so this is a *negative*-leaning connection, not a strengthening one.
- **No** agentskills.io chain, **no** SKILL.md/AGENTS.md/.claude/MCP, **no** Karpathy lineage, **no** Claude-Code adjacency (root-contents listing confirms zero agent artifacts).

**(d) WEAK.**

---

## Verdict

| Criterion | Result |
|---|---|
| (a) cultural-peer | **PASS (inferred)** — harry0703, inferred China-Mainland solo indie (Chinese-primary README); China-cluster +1 |
| (b) goal-relevance / vault-utility | **FAIL** — faceless short-video generator; no software-dev / agent / vault utility |
| (c) instructive | **WEAK** — competent MVC + multi-LLM layer, but off the corpus's agent/skill methodology domain |
| (d) corpus connectivity | **WEAK** — #84 cross-vendor + China-cluster; zero agent/skill/Claude/MCP surface; faceless-sibling was outside-scope |

**WEAK INCLUDE 1/4** — the include rests **entirely on (a)**. This is the **v80 SmartMacroAI pattern**: a single (a)-cultural-peer PASS rescues an otherwise off-goal-domain subject into a WEAK INCLUDE (≥1 clear PASS = INCLUDE, not the 0-PASS SKIP threshold). Not an override; streak advances.

**Finding-2 calibration note:** (b) deliberately held at **FAIL**, not laundered to WEAK-PASS on "it uses LLMs" grounds — a faceless-video app does not serve the documented #1 goal, and the prior faceless subject was outside-scope. (c)/(d) deliberately held at WEAK, not inflated to MODERATE on multi-provider grounds. The honest shape of this subject is *one strong axis (a) + three weak/failed axes*, and saying so plainly is the rubric working. Healthy discrimination: notably weaker than v121 CodexKit's 3/4 and v122-was-an-override.

**Streak:** "47+3\*" → **"48+3\*"** (48 PASS + 3 OVERRIDE; v123 = 1st clean PASS after the v122 dograh override). v123 is a clean PASS and does **not** add to the override count.

**⚠️ Audit input for the mandated ~v124 Phase 0.9 review:** v122 dograh tripped 2-in-20, mandating a Phase 0.9 STRICT systematic-miss review. v123 adds a related data point: **"(a)-cultural-peer rescue of an off-goal-domain subject" is now N=2** (v80 SmartMacroAI Windows-RPA + v123 MoneyPrinterTurbo faceless-video) — both 1/4 WEAK INCLUDEs carried by (a) alone, both off goal #1. Combined with the 3 overrides (v84/v116/v122, all (a)+(b) FAILs), the audit's real question is sharpening: **the corpus is absorbing notable-but-off-goal subjects through two channels — override (when (a) fails) and (a)-rescue (when (a) passes).** Candidate fix remains a lightweight **corpus-knowledge-outlier track** distinct from goal-aligned INCLUDEs. Surfaced here as an audit input; deliberately **not** minted as Library-vocab (§28).

## Pilot

**NOT a pilot — corpus-knowledge only.** A faceless short-video generator serves no part of Storm Bear's software-dev / Scrum / LLM-wiki work. It does not join the operational Claude-Code-adjacent stack (claude-mem / harness / humanizer / cclog-cli). Like v80 SmartMacroAI, it is a WEAK-INCLUDE corpus entry, not an actionable pilot.
