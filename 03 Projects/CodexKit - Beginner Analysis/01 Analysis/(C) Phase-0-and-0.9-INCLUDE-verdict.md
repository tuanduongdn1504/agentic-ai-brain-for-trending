# (C) Phase 0 + Phase 0.9 INCLUDE verdict — CodexKit (v121)

**Routine:** v2.4. **Fetched:** 2026-05-30. **Verdict:** **STRONG INCLUDE 3/4** ((a) PASS inferred-VN + (b) **WEAK** + (c)(d) STRONG). 4th consecutive clean PASS after the v116 Sana OVERRIDE.

> ✅ **Cadence:** v120 mini-audit (2026-05-30) cleared the cadence — "v121+ = wikis OK; next natural audit ~v124–v125." CodexKit is the **first build of the post-v120 window**. No audit-deferral flag.

---

## Phase 0 — scope gate

| Gate | Result |
|---|---|
| Repo reachable + readable | ✅ `hoavdc/CodexKit` |
| License present | ✅ **MIT** (GitHub API `mit`) |
| Active / recently pushed | ✅ pushed 2026-05-15; created 2026-03-20 (~71 days); v0.10.0 / 8 releases |
| Scale floor (≥1★) | ✅ **19★** (micro-scale, but above floor) |
| Tier classification | **T1 Assistant Skill / Multi-Domain (Cross-Functional) Skill Collection** |

**Phase 0 = PASS.** In-scope: an installable agent-skill collection (90 skills) with a defined skill spec, install scripts, and MCP guidance. The twist vs the recent corpus: the harness is **OpenAI Codex / ChatGPT**, and the skill format is Codex-native (`SKILL.md` + `agents/openai.yaml` + `.agents/skills`), **not** agentskills.io / `.claude/`.

---

## Phase 0.9 — STRICT 4-criterion INCLUDE filter

### (a) Author cultural-peer to Storm Bear — **PASS (inferred)**

Author **Hoa Dang** (`hoavdc`). Profile **location and bio are null** — no declared country. But two strong signals make Vietnamese the high-confidence inference: (1) **"Hoa Dang"** is a Vietnamese name; (2) the repo ships a **`HUONG-DAN-NHANH.md`** — "Hướng dẫn nhanh" = Vietnamese for "Quick guide" — a first-class Vietnamese-language onboarding doc for non-technical office users. This is *stronger* evidence than v117's community-signal inference of China-Mainland (an actual VN-language artifact is shipped in-repo), but it remains **inferred, not declared** (cf. v119 nature-skills, which was a *declared* PASS). Storm Bear is Vietnamese → direct cultural peer.

Extends the VN sub-cluster (v76 Hanoi solo + v80 VN solo + v85 VN-org + v91 VN-solo + **v121**) and is another instance of Pattern #19's **CONFIRMED** "VN-Community Multi-Profile-Type" (N=5) — here a **VN-solo prolific-builder** (236 public repos). No new (a) sub-axis (VN-located is well established). **(a) PASS (inferred).**

### (b) Goal-relevance / vault-utility — **WEAK**

Two independent reasons this is honestly WEAK, not MODERATE:

1. **Harness:** CodexKit is **OpenAI Codex / ChatGPT-first with zero Claude support** — it routes *entirely* away from the vault's Claude substrate. This is more Codex-pure than v117 CodexPlusPlus (which at least managed a coding agent) and than v112 freellmapi (which could proxy *any* provider including Claude). Goal #1 is explicitly "master **Claude** and autonomous agents for software development."
2. **Domain:** the 90 skills are **business operations** (finance, legal, HR, marketing, sales, ops, strategy, CX) — not software development and not agent-mastery. Even setting the harness aside, the *content* is off-goal.

The only genuine value is as a **skill-authoring reference** (the 5-layer framework + tiering are studyable). That is real but study-only, not operational. Per §10 (cost × relevance), an off-substrate + off-domain subject whose value is reference-only = **WEAK**. Deliberately not inflated.

### (c) Instructive / exemplary — **STRONG**

A genuinely well-architected skill-authoring model:
- **5-Layer Skill Framework** — Intent / Knowledge / Execution / **Verification (explicit 4C gates: Correctness, Completeness, Context-fit, Consequence)** / Evolution. The named verification-gate layer + an explicit Evolution layer are more disciplined than most corpus skill collections.
- **3-tier progressive structure** (T1 spec-only 90 → T2 +verification+examples 26 → T3 +templates+scripts 5) — a clean separation of "every skill" vs "deepened skills" vs "technical skills."
- **8-category taxonomy** + 90-skill breadth + playbooks + automation recipes + workspace kits.

This methodology is **cross-applicable to agentskills.io / Claude skill authoring** despite the Codex runtime — which is exactly why it earns STRONG even with (b) WEAK. **(c) STRONG.**

### (d) Corpus connectivity — **STRONG**

- **Codex-tool cluster** — siblings v62 codex-plugin-cc (bridge) + v117 CodexPlusPlus (management harness). CodexKit is the **skill-content** member of that cluster.
- **VN cultural-peer cluster** — v76 / v80 / v85 / v91 (+ Pattern #19 CONFIRMED N=5).
- **T1 skill-collection archetype** — a **multi-domain variant** contrasting the single-vertical Domain-Vertical-Skill-Collection (CONFIRMED N=4).
- **Codex-native skill standard as a *parallel* to agentskills.io** — corpus-novel: the agentskills.io 57k chain (v76→…→v119, 11 implementers) is the Claude/multi-harness standard; CodexKit implements the *competing* Codex standard. Evidence of ecosystem bifurcation. (Deliberately **not** counted as a 57k implementer.)
- **MCP guidance** (`mcp/`); high-fork-ratio micro-scale signal (LV-C4).

**(d) STRONG.**

---

## Verdict

| Criterion | Result |
|---|---|
| (a) cultural-peer | **PASS (inferred)** — Hoa Dang, inferred-Vietnamese (name + shipped VN quick-guide); VN cluster → +1; location undeclared |
| (b) goal-relevance / vault-utility | **WEAK** — Codex/ChatGPT-only (no Claude) + business-ops domain (not software-dev); reference-value only |
| (c) instructive | **STRONG** — 5-layer framework + 4C verification gates + 3-tier structure = exemplary skill-authoring reference |
| (d) corpus connectivity | **STRONG** — Codex-tool cluster + VN cluster + multi-domain skill-collection variant + Codex-vs-agentskills.io parallel-standard + MCP |

**STRONG INCLUDE 3/4** — INCLUDE rests on (a)(c)(d); (b) honestly WEAK. Precedent for a one-strong-axis VN-peer include is well established (v80 SmartMacroAI was WEAK INCLUDE 1/4); CodexKit is materially stronger at 3/4.

**Finding-2 calibration note:** (b) deliberately held at **WEAK**, not laundered to MODERATE on skill-authoring-reference grounds. A Codex-only, business-ops skill OS does not serve the documented #1 goal operationally, and saying so plainly is the point of the rubric. Healthy discrimination (one notch below v117's MODERATE, which at least managed a coding agent).

**Streak:** "46+2\*" → **"47+2\*"** (47 PASS + 2 OVERRIDE; v121 = 4th consecutive clean PASS after the v116 Sana override — v117 1st, v118 2nd, v119 3rd).

**Pilot:** **NOT a pilot — corpus-knowledge + skill-authoring reference only.** CodexKit runs on Codex/ChatGPT (Storm Bear uses Claude) and targets business-ops (not software-dev/Scrum). Like v80, it does **not** join the operational Claude-Code-adjacent stack (claude-mem / harness / humanizer / cclog-cli). The only actionable use is to *read* the 5-layer framework + 3-tier structure as a model for authoring the vault's own (Claude) skills.
