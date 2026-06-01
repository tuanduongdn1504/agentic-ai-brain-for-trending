# (C) Pattern Library mini-audit — v125

**Date:** 2026-05-30. **Routine:** v2.4. **Trigger:** **MANDATED** — v122 dograh tripped the **first-ever 2-in-20 override-frequency trigger** (routine v2.3 §7), which mandates a Phase-0.9 STRICT systematic-miss review at the next audit. Also: NATURAL-CADENCE (4 wikis since the v120 audit: v121/v122/v123/v124, the projected ~v124–v125 window) + three N=2→N=3 promotion-eligible sub-claims + the "(a)-rescue N=2" observation queued at v123. **Type:** mini-audit; the **first trigger-MANDATED audit in corpus history** (every prior audit was operator-elected or natural-cadence).

**One-line:** The 2-in-20 trigger fired *truthfully* — there **is** a systematic pattern — but it is **NOT a Phase-0.9 STRICT criteria defect; it's an intake-channel pattern.** The corpus is absorbing notable-but-off-goal subjects through **two** channels: **override** when (a) fails (v84/v116/v122) and **(a)-rescue** when (a) passes (v80/v123). Resolution: **NO criteria redesign**; recommend a lightweight **corpus-knowledge-outlier track** (operator sign-off pending). Also: all **3 N=2 sub-claims HOLD** (no 3rd instance appeared); a **NEW Pattern #66 skill-security-scanning N=2**; **§28 rule-5 HELD across v121–v124** (the v120 filing-discipline fix worked — first clean §28 window); facts **clean** (v121–v124 verified, 0 errors). Streak **UNCHANGED "49+3\*"** (audit ≠ ship).

---

## A. The MANDATED override-frequency systematic-miss review (§7) — headline, DISCHARGED

The 2-in-20 trigger (v116 + v122 within the last 20 wiki-ships) mandated this review. §7 prescribes: identify whether there's a common cause; if a *criteria* common-cause → revise Phase-0.9 STRICT; if no criteria common-cause → tighten override-discipline.

**The 3 overrides, examined:**

| Override | Subject | (a) | (b) | Why overridden |
|---|---|---|---|---|
| v84 image-blaster | image→3D creative-tech Claude-skill bundle | PROBABLE-PASS-on-revision | WEAK | In the agentskills ecosystem, but creative-tech vertical — off goal #1 (Scrum/software-dev) |
| v116 Sana | NVIDIA generative-vision research model | FAIL (US mega-corp) | FAIL (GPU vision) | Fully out-of-corpus-scope; notable research, operator wanted it captured |
| v122 dograh | commercial voice-AI/telephony platform | FAIL (VC startup) | FAIL (voice agents) | Out-of-corpus-scope; incidental Claude-Code dev-tooling; operator wanted it captured |

**Common cause — YES, and it is clear:** all three **FAIL (b) goal-relevance** ("autonomous agents *for software development*"). They are *notable/interesting repos the operator chose to capture despite being off-goal.* This is **not** "Phase-0.9 STRICT is wrongly rejecting subjects that should be INCLUDEd" — the criteria worked correctly; they accurately flagged all three as off-goal. The override was the operator electing to capture corpus-knowledge anyway.

**Verdict (DISCHARGES the mandate):**
- **NO Phase-0.9 STRICT criteria redesign.** The criteria are calibrated correctly; they are not producing false-rejections. The 2-in-20 trigger surfaced a *real* pattern, but it is an **intake-channel** pattern, not a criteria defect.
- The pattern's true shape is broader than the override channel alone — see §B (the (a)-rescue channel does the same thing when (a) passes). The right response is the **outlier-track** (§C), not a STRICT change and not punitive override-tightening.
- Override-discipline itself **HOLDS**: all 3 were operator-elected + honestly documented (0/4 or honest-WEAK framing, B2 streak notation). No discipline failure to tighten.

The mandated review is **DISCHARGED**: examined, common-cause identified, criteria cleared, resolution routed to §C.

---

## B. The off-goal-intake 2-channel finding (the real systematic pattern)

The override review (§A) only sees half the pattern. The other half is the **(a)-rescue channel**:

| (a)-rescue case | Subject | Verdict | Off-goal? |
|---|---|---|---|
| v80 SmartMacroAI | Windows RPA tool | WEAK INCLUDE 1/4 ((a) PASS VN-located; b/c/d FAIL) | Yes — RPA, not software-dev-agents |
| v123 MoneyPrinterTurbo | faceless short-video generator | WEAK INCLUDE 1/4 ((a) PASS inferred-China; (b) FAIL, c/d WEAK) | Yes — content tool, not software-dev-agents |

**The unified finding:** the corpus absorbs off-goal subjects through **two channels**:
1. **Override** — when (a) FAILS (commercial/mega-corp authors): v84/v116/v122. *Honestly flagged* (0/4 + override notation + asterisk in streak).
2. **(a)-rescue** — when (a) PASSES (cultural-peer authors with off-goal projects): v80/v123. **Silently absorbed** — a "WEAK INCLUDE 1/4" looks like a normal clean PASS, counts toward the streak/INCLUDE-rate, and carries no "off-goal" flag.

The asymmetry is the problem: the override channel is honest about being off-goal; the (a)-rescue channel is **not**. Both admit subjects that don't serve goal #1, but only one is labeled as such. So the corpus's "INCLUDE rate" and PASS-streak silently blend goal-central subjects (a Claude-Code tool, an agent-skill library) with cultural-peers' off-goal side-projects (an RPA tool, a faceless-video generator). The signal "this subject advances goal #1" is diluted.

**Root cause:** Phase-0.9 treats *any* single criterion PASS as INCLUDE-worthy, and conflates two orthogonal questions — **"is the author a cultural-peer?" (a)** and **"does the subject serve the goal?" (b)**. A cultural-peer's off-goal project PASSes (a) and thus "INCLUDEs," even though (b) — the goal-relevance question — failed.

---

## C. RECOMMENDATION — corpus-knowledge-outlier track (2-tier INCLUDE) — ✅ ADOPTED 2026-05-30

> **UPDATE 2026-05-30 — ADOPTED.** Operator signed off on this recommendation; codified as **routine v2.5** (`05 Skills/llm-wiki-routine-v2.5.md`, §31–§34) with the recommended defaults: **forward-only** (no retroactive re-tag; "49+3\*" frozen @v125) + **streak-split going forward** (GA goal-aligned / OG off-goal-capture from v126). No Phase-0.9 STRICT criteria change. The "operator's call" items in this section are now decided per the recommended defaults below.

Proposed resolution (a v2.5 codification candidate; **flagged for operator decision** because it changes verdict semantics + streak accounting):

**A 2-tier INCLUDE distinction, keyed on (b) goal-relevance:**
- **GOAL-ALIGNED INCLUDE** — (b) PASSes (MODERATE+). The subject genuinely serves goal #1 (Claude-Code tool / agent-skill / autonomous-coding / LLM-tooling). The corpus's core; counts toward the goal-aligned streak.
- **OFF-GOAL CAPTURE (corpus-knowledge-outlier)** — (b) FAILs, but the subject is captured anyway, via *either* channel: (a)-rescue ((a) passes) *or* operator override ((a) fails). Tagged distinctly + honestly labeled "off-goal corpus-knowledge"; does **not** inflate the goal-aligned-INCLUDE rate; reserves the override-budget/asterisk for genuine STRICT-misses rather than deliberate off-goal captures.

**What this fixes:** unifies the override + (a)-rescue channels under one honest label ("off-goal capture"), regardless of (a); stops the (a)-rescue channel from silently padding the streak; gives the operator a legitimate, non-punitive way to capture notable off-goal repos (which they clearly want to do — 5 instances now: v80/v84/v116/v122/v123) without it reading as either a discipline failure (override) or a goal-aligned win ((a)-rescue).

**What's deliberately NOT decided here (needs operator sign-off):**
- Whether to **retroactively re-tag** v80/v123 (currently "WEAK INCLUDE 1/4") and v84/v116/v122 (currently "OVERRIDE") as "off-goal capture." (Recommend: forward-only; note the lineage; don't rewrite committed history.)
- Whether/how to **split the streak** ("goal-aligned PASS" vs "off-goal capture"). (Recommend: track separately going forward; leave "49+3\*" as the historical figure.)
- Formal codification into the routine (v2.5).

**Audit position:** the finding (2-channel off-goal intake) is **DECIDED** (it's clear and evidence-backed at 5 instances). The *resolution* (the outlier track) is **RECOMMENDED**, adopted as the working framing for labeling going forward, but the formal policy/accounting change is **operator's call** — it's consequential enough not to lock unilaterally in a mini-audit.

---

## D. Promotion decisions — all 3 queued N=2 sub-claims HOLD; 1 new N=2 registered

Checked each N=2 sub-claim for a 3rd instance in the v120→v124 window. **None appeared. All HOLD at N=2 (PROMOTION-ELIGIBLE at N=3).** An audit must not manufacture promotions.

| Sub-claim | N | 3rd instance in v121–v124? | Decision |
|---|---|---|---|
| **LV-C2 Cost-Attribution-via-External-Service** (v89 LiteLLM + v109 pricing-service) | 2 | No | **HOLD N=2** |
| **LV-C7 Tauri-Desktop-Management-GUI-for-a-Coding-Agent** (v73 cc-switch + v117 CodexPlusPlus) | 2 | No (no 3rd *management-GUI*; v118–v124 added none) | **HOLD N=2** |
| **Brand-Named Third-Party Repo + Affiliation Disclaimer** (v98 + v119) | 2 | No (v124 K-Dense has no famous-brand-in-name + no disclaimer) | **HOLD N=2** |
| **Pattern #57 corpus-recursive-at-methodology-influence** (v94 + v118) | 2 | No | **HOLD N=2** |

**NEW N=2 registered (at the Pattern layer):**
- **Pattern #66 "published automated LLM-based skill-security-scanning" N=2** — v76 agent-skills-standard (injection-scanning + audit-logs) + v124 scientific-agent-skills (Cisco AI Defense weekly scans → 518 KB SECURITY.md). PROMOTION-ELIGIBLE at N=3. Honest: v76 was first; v124 is not corpus-first, it strengthens. Emerging skill-supply-chain hygiene worth watching.

**Administrative (already-CONFIRMED, recorded, no state change):**
- **T1 Domain-Vertical-Skill-Collection → N=5** (v64 SEO + v90 academic + v98 cyber + v119 nature + v124 scientific). CONFIRMED archetype since v101; +1 count, largest-scale instance (v124, 141 skills).
- **agentskills.io 57k chain → 12th implementer** (v124, after v119's 11th). CONFIRMED N=3 unchanged.

**No new top-level Pattern. No new CONFIRMED Library-vocab. Confirmed-pattern count UNCHANGED at 46.**

---

## E. §28 rule-5 discipline check (v121–v124) — HELD ✅ (the v120 fix worked)

The v120 audit found §28 rule-5 ("filing is an act, not a claim") had FAILED across v116–v119 (narratives claimed filings; the registry was never edited) and remediated + codified rule 5. v125 is the first test of whether the fix held:

| Wiki | New Library-vocab? | Registry actually edited? | Verdict |
|---|---|---|---|
| v121 CodexKit | 2 standalones + 2 cluster notes (at the ≤2 cap) | ✅ YES (committed in 62d98a8) | HELD |
| v122 dograh | ZERO (out-of-scope override) | ✅ N/A — correctly minted nothing | HELD |
| v123 MoneyPrinterTurbo | ZERO (WEAK off-domain) | ✅ N/A — correctly minted nothing | HELD |
| v124 scientific-agent-skills | 0 standalones + 2 cluster-filings (LV-C1 + LV-C3) | ✅ YES (committed in 0de8726) | HELD |

**§28 rule-5 HELD across all 4 ships** — the registry diffs in 62d98a8 + 0de8726 are the proof (vs v116–v119's prose-only claims). The cap (rule 2) and count-discipline (rule 4) also held (tracked surface ≈ 14, never re-inflated). **First clean §28 window since the rule existed.** Good signal: the honor-system gap §28 rule-5 closed at v120 stayed closed.

---

## F. Fact-verification — CLEAN (v125 is a fully-clean audit)

- v122 dograh / v123 MoneyPrinterTurbo / v124 scientific-agent-skills: metadata freshly fetched 2026-05-30 this session (stars/license/language/dates) — current, 0 errors.
- v121 CodexKit (shipped concurrently; not personally fetched at ship) **spot-checked this audit:** 19★ / 10 forks (fork_ratio 0.526) / MIT / TypeScript / hoavdc User / created 2026-03-20 — **all match the state-block.** 0 errors.
- **0 fact-errors in v121–v124.** Unlike v120 (subject-facts clean but carried a §28 *process* finding), v125 is clean on **both** facts and process. **Clean-audit count → 12** (v66+v69+v72+v86+v90+v96+v101+v106+v110+v115+v120+v125; v120 facts-clean-process-finding, v125 fully clean).

---

## G. State after v125 audit

| Field | Value |
|---|---|
| Confirmed Patterns (top-level) | **46** (UNCHANGED) |
| Active candidates | ~25 (UNCHANGED) |
| Library-vocab CONFIRMED | **8** (UNCHANGED) |
| Library-vocab PROVISIONAL tracked | **~14** (7 clusters + 7 standalones; UNCHANGED — v124 added 2 cluster members, 0 standalones) |
| NEW N=2 this audit | Pattern #66 published-skill-security-scanning (v76+v124) |
| Routine | v2.4 CURRENT (outlier-track = v2.5 codification candidate, operator-sign-off pending) |
| Streak | **"49+3\*"** UNCHANGED (audit ≠ ship; 49 PASS + 3 OVERRIDE) |
| Override count / frequency | 3 lifetime (v84/v116/v122); 2-in-20 trigger DISCHARGED (intake-channel finding, no criteria redesign) |
| Fact-verification audits clean | **12** (v125 fully clean — facts + §28 process) |

**Promotion-eligible (N=2 → N=3 watch):** LV-C2 Cost-Attribution-via-External-Service · LV-C7 Tauri-Management-GUI-for-a-Coding-Agent · Brand-Named-Repo+Disclaimer · Pattern #57 corpus-recursive-at-methodology-influence · **Pattern #66 skill-security-scanning (NEW)**.

---

## H. Next audit triggers

- **Mandated override-review: DISCHARGED** at v125 (no criteria redesign; intake-channel finding routed to the outlier-track recommendation).
- **Cadence: RESET.** v125 clears it; **v126+ = wikis OK**; next natural audit **~v129–v130** (or operator-elected, or trigger-forced).
- **Override-frequency monitoring continues:** still 3 lifetime overrides; if a 4th lands inside the next 20 ships → 2-in-20 re-trips (and if within 30 of v116/v122 → 3-in-30 fires, forcing a harder review).
- **⚠️ CARRY-FORWARD (CRITICAL): the corpus-knowledge-outlier track (§C) needs an operator decision** — it's the genuine resolution of the off-goal-intake finding, and until it's decided, the (a)-rescue channel keeps silently padding the streak. Recommend deciding it before (or as) the next codification (v2.5).
- 5 N=2 sub-claims on N=3 watch (above).

---

## I. Storm Bear's blunt take

The trigger earned its keep. The 2-in-20 fired for the first time, I was *required* to look, and the look found something real — just not the thing the trigger literally checks for. Phase-0.9 STRICT isn't miscalibrated; it correctly flagged dograh, Sana, and image-blaster as off-goal. The real finding is bigger and more uncomfortable: **off-goal subjects are getting into the corpus through two doors, and only one of them has a sign on it.** The override door is honest (0/4, asterisk). The (a)-rescue door — a cultural-peer's off-goal side-project sailing in as a "WEAK INCLUDE 1/4" — is silent, and it's been used twice (v80, v123) for an RPA tool and a faceless-video generator. Five off-goal captures total now. That's not a criteria bug to patch; it's a missing category. The fix I'm recommending — a 2-tier INCLUDE that labels off-goal capture honestly regardless of which door it came through — is yours to sign off on, because it changes how PASSes are counted, and I won't rewrite that semantics unilaterally in a mini-audit.

The rest is clean and non-inflated: all three N=2 sub-claims **held** (no 3rd instance — I didn't invent one), the only new N=2 is skill-security-scanning (and I said plainly it's N=2 with v76, not corpus-first), T1 N=5 and the 57k 12th are administrative counts, and **§28 rule-5 held across all four ships** — the registry actually got edited at v121 and v124, the diffs prove it, and v122/v123 correctly minted nothing. Facts are clean on all four. So: 1 mandated review discharged, 1 real structural finding (with a recommendation parked for your call), 0 manufactured promotions, 1 clean §28 window. The honest next move is the one I keep flagging — decide the outlier track, then **pilot** (OpenHuman fenced / v113 READ-pilot) — because the corpus just spent four ships proving it can catalogue faster than it can advance the goal.
