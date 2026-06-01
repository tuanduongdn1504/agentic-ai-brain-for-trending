# (C) Phase 0 + Phase 0.9 verdict — Echo Loop (v128) — **WEAK INCLUDE 1/4 → OFF-GOAL CAPTURE**

**Routine:** v2.5. **Fetched:** 2026-06-01 (GitHub API + README). **Verdict:** STRICT **1/4 → WEAK INCLUDE** on criterion (a) alone → routine v2.5 §31 **OFF-GOAL CAPTURE via the (a)-rescue channel** (NOT an operator override — it clears the gate; NOT a 0/4 SKIP).

---

## Phase 0 — scope gate

| Gate | Result |
|---|---|
| Repo reachable + readable | ✅ `echo-loop/Echo-Loop` |
| License present | ✅ **AGPL-3.0** (GitHub API agrees) |
| Active / recently pushed | ✅ created 2026-05-07 / pushed 2026-05-30 (~25 days) |
| Scale floor (≥1★) | ✅ **705★** / 40 forks (fork_ratio ~0.057) |
| Tier classification | **T5 Application** (consumer end-user app). Off the agent-for-coding corpus domain. |

**Phase 0 = clears the mechanical gates, FLAGGED off-domain.** Echo Loop is a consumer English listening/speaking training app, not an agent/Claude/skill/dev subject.

---

## Phase 0.9 — STRICT 4-criterion INCLUDE filter

### (a) Author cultural-peer to Storm Bear — **PASS (inferred/declared)**

Owner = `echo-loop` (`owner.type: User`), a **China-based developer**. Evidence: bilingual README with 简体中文 primary (+ `README.en.md`), Chinese product copy throughout, homepage `echo-loop.top`, and an explicit academic anchor — the project is guided by **Prof. Yang Yan (杨彦) of Minzu University of China, School of Foreign Languages**, with a Beijing PhD credential cited. This is a well-supported China-Mainland cultural-peer (the v82 / v94 / v100 / v117 / v123 China-cluster; inference-tolerant per §8). **(a) PASS.**

### (b) Goal-relevance / vault-utility — **FAIL**

Documented #1 goal: *"Master Claude and autonomous agents for software development."* Echo Loop is an **English listening/speaking training app** for individual learners. AI (translation, sentence/word analysis, auto-transcription, ASR speaking-evaluation) is wired in as *components of a consumer tutoring product*, not as a dev tool. No vault/Scrum/dev-workflow/coding-agent utility. (Contrast v112 freellmapi, whose LLM-proxy was a genuine dev-side utility scoring (b) STRONG.) **(b) FAIL** — the same off-goal shape as v123 MoneyPrinterTurbo.

### (c) Instructive / exemplary — **WEAK**

Two layers:
1. **The subject** (a Flutter language-learning app) is competently built (Riverpod + Drift + sherpa_onnx on-device ASR + a clear pedagogical loop) but teaches nothing transferable to the corpus's agent/skill/distribution/governance methodology.
2. **The engineering exhaust** is the only corpus-relevant thread: the repo ships `.claude/` + `AGENTS.md` + `CLAUDE.md`, i.e. the developer uses **Claude Code as internal engineering discipline**. This is the dograh-v122 thread — genuinely interesting as an adoption signal, but it is *how the app is built*, not the app, and PASSing (c) on it would launder "this dev uses Claude Code well" into "this language app is instructive for our agent corpus." Disciplined call: note it, don't PASS on it.

**(c) WEAK.**

### (d) Corpus connectivity — **WEAK**

- `.claude/` + `AGENTS.md` + `CLAUDE.md` = Library-vocab #12 LLM-routing-artifacts, a real N+1 but **incidental** (internal dev tooling at an off-goal subject).
- China-Mainland cluster N+1.
- No agentskills.io product chain, no SKILL.md product, no MCP product, no Karpathy lineage, no Claude-Code-tool-as-product adjacency.

**(d) WEAK.**

---

## Verdict

| Criterion | Result |
|---|---|
| (a) cultural-peer / (a)-7 | **PASS** (inferred/declared China-Mainland) |
| (b) goal-relevance / vault-utility | **FAIL** (off goal #1 — consumer language app) |
| (c) instructive | **WEAK** (off-domain subject; incidental Claude-Code thread) |
| (d) corpus connectivity | **WEAK** (incidental / cluster only) |

**STRICT = 1 clear PASS (a-only) → WEAK INCLUDE.** The include rests ENTIRELY on (a); the only thing separating Echo Loop from an outside-scope subject is the cultural-peer PASS. This is the **v80 SmartMacroAI / v123 MoneyPrinterTurbo pattern**.

**Routine v2.5 §31 tagging: OFF-GOAL CAPTURE via the (a)-rescue channel.** Because (b) FAILs but the subject is captured anyway (via an (a) PASS, not an override), v2.5 labels it an OFF-GOAL CAPTURE — corpus-knowledge of a cultural-peer subject — NOT a goal-aligned INCLUDE, and it does NOT pad the goal-aligned (GA) streak. This is the v2.5 machinery working as designed: the v125 audit's whole point was that (a)-rescue off-goal captures were silently padding the streak as "WEAK INCLUDEs"; v2.5 gives them an honest OG tag instead.

**Streak (v2.5 §32 forward-only):** historical **"49+3\*" FROZEN @v125**. Forward **GA:1 · OG:1 [1 ov] → GA:1 · OG:2 [1 ov]** — v128 increments the OFF-GOAL CAPTURE tally; the `[1 ov]` override subset is **unchanged** (Echo Loop is an (a)-rescue capture, NOT an override). **No override-frequency trigger trip** (not an override).

**⚠️ Findings for the next audit:**
1. **(a)-rescue off-goal capture is now N=3** (v80 SmartMacroAI + v123 MoneyPrinterTurbo + v128 Echo Loop) — past the threshold the v125 audit cared about. The channel is real and recurring.
2. **v2.5 soft off-goal-capture-rate watch is firing:** of the 3 ships under v2.5 (v126 GA, v127 OG-override, v128 OG-(a)-rescue), **2 of 3 are off-goal** and the most recent 2 ships are both off-goal. The corpus is, again, capturing faster than it advances goal #1 — exactly the drift v2.5's accounting was built to make visible.
3. **Internal-Claude-Code-discipline-at-an-off-goal-subject is now N=2** (dograh v122 + Echo Loop v128) — noted as an observation, not minted (off-goal captures should not drive the Pattern Library; §28 + v125 anti-inflation).

**Honest framing carried to every artifact:** Echo Loop is corpus-knowledge of a cultural-peer subject. It is NOT a pilot, NOT goal-aligned, and contributes NO change to Pattern Library state. NO new T5 sub-archetype minted (it is a different vertical from v123, and minting for off-goal apps is the inflation the v125 audit warned against).
