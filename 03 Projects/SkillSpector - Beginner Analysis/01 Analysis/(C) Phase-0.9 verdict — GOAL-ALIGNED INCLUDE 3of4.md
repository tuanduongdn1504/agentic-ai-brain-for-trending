# (C) Phase-0.9 verdict — SkillSpector (v169) — GOAL-ALIGNED INCLUDE 3/4

**Subject:** `NVIDIA/SkillSpector` — "Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, and security risks."
**Date:** 2026-06-20 · **Routine:** LLM Wiki Routine v2.6
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG

---

## The four criteria

### (a) FAIL — author identity (cultural-peer / disclosed-identity axis)

NVIDIA is a fully-disclosed major US corporate vendor. The vault's criterion-(a) is **not** a generic "is the author a known entity?" test — it is a **cultural-peer axis** (the 6-axis taxonomy: VN/Asian solo-dev, Tiếng Việt, first-class vi-VN i18n, VN/Asian community-org, VN/Asian founder-anchor, recognized-cultural-cluster extension), plus one major-vendor carve-out **(a)-7 "Foundational-Vendor-Direct-Source," which is Anthropic-specific** (codified v92, reconfirmed v141).

NVIDIA satisfies none of the 6 cultural-peer axes and is not Anthropic. **Corporate-org status alone does not PASS (a).** The precedent is airtight and consistent:

| Subject | Author | (a) |
|---|---|---|
| v141 claude-for-financial-services | Anthropic (`anthropics`) | **PASS** via (a)-7 (Anthropic-only) |
| v140 google_workspace_mcp | Google APIs / individual | **FAIL** ("US-individual, not cultural-peer / not (a)-7") |
| v143 larksuite-cli | ByteDance (`larksuite`) | **FAIL** ("corporate official org / not (a)-7") |
| **v169 SkillSpector** | **NVIDIA** | **FAIL** (major US vendor, not Anthropic, no cultural-peer axis) |

→ **(a) FAILS cleanly.** No (a)-rescue is taken and no axis is minted (the v151-rec-(ii) / v160 / v164–v168 "no cultural-peer inferred, no door-opening for off-goal" discipline). SkillSpector does not need a rescue — it is goal-aligned through (b).

### (b) STRONG — goal-#1 relevance

Goal #1 = *"master Claude and autonomous agents for software development."* SkillSpector is a defensive-security scanner for the **agent-skills ecosystem** (Claude Code / Codex / Gemini CLI / MCP), i.e. the exact artifact class this vault both **authors** (`05 Skills/`) and **installs** (it evaluated the ponytail Claude-Code plugin at v168). It is **directly pilotable** — run it over the vault's own skills.

Held **STRONG, not STRONGEST:** it is a third-party tool *about* skills (passive validation of an artifact), not the substrate (Claude/Anthropic) and not a behavior layer that changes how the agent itself works. STRONGEST / near-STRONGEST is reserved for substrate-coupled subjects (the v161/v168 calibration). STRONG is the calibrated, non-inflated call.

→ **(b) PASSES at STRONG.**

### (c) STRONG — engineering maturity / rigor

Apache-2.0; a mature LangGraph two-stage pipeline; a 16-category YARA rule library + Python AST + taint-tracking; live OSV.dev CVE integration with offline fallback; MCP-aware checks (tool-poisoning, least-privilege); four output formats incl. **SARIF** for CI; Docker + pre-commit + `model_registry.yaml`; research-grounded design rationale (page-stated, §3 of the wiki). **Caveat:** 0 published releases / continuous-`main` development (36 commits) → pre-release maturity; flagged in the pilot fence. → **(c) PASSES at STRONG.**

### (d) STRONG — pattern-library connection

1 NEW corpus-first §C standalone (defensive-security scanner for agent skills) + a scoped Pattern #84 84c observation (multi-LLM-provider backend) + a Pattern #17 variant-2 data-point (first NVIDIA-org author) + a Pattern #66 cross-reference (active-scanner complement to passive supply-chain-awareness). Detail in the PRIMARY analysis doc. → **(d) PASSES at STRONG.**

---

## Tier determination (routine v2.5 §31 — keyed on (b))

> **§31 decision rule (verbatim):** *"INCLUDE with (b) MODERATE+ → GOAL-ALIGNED; INCLUDE with (b) FAIL (whether carried by (a)-rescue or by override) → OFF-GOAL CAPTURE."*

(b) is **STRONG** (MODERATE+) → **GOAL-ALIGNED INCLUDE.** The tier is keyed on **(b) only**; (a)'s outcome is irrelevant to it. **OFF-GOAL CAPTURE applies only when (b) FAILs** — which is not the case here.

**Precedent (the controlling one):** the immediately-prior ship **v168 ponytail** = `(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG` → shipped as **GOAL-ALIGNED INCLUDE 3/4.** SkillSpector is the identical shape and gets the identical tier.

### ⚠️ Correction of a build-workflow cascade error

The v169 build workflow's synthesis agent, **all five** adversarial verifiers, and the completeness critic **all** concluded "OFF-GOAL CAPTURE" on the reasoning "(a) FAIL → off-goal per §31." This is a **correlated error**: every agent reasoned from the same false premise (that (a) gates the tier) and "verified" each other rather than re-reading §31's decision rule or checking v168's tier. **Overridden at synthesis.** The correct verdict is **GOAL-ALIGNED INCLUDE 3/4** — this is *not* an off-goal capture, does *not* consume an OG slot, and **advances the goal-aligned streak to GA:31.**

---

## Streak / §35

- **Streak:** `GA:30 · OG:11 [7 ov]` → **`GA:31 · OG:11 [7 ov]`** (31st GOAL-ALIGNED PASS; NOT an override; "49+3\*" frozen @v125).
- **§35 ceiling:** rolling-3-ship window {v166 GA, v168 GA, **v169 GA**} = **0 OG → CLEAR** (v167 was an audit, not a ship). No ceiling-override needed or taken.
- **16 consecutive goal-aligned ships v153→v169.**

## Honest non-claims

- (a) genuinely FAILS (NVIDIA ≠ Anthropic; corporate-org ≠ (a)-7; matches v140/v143). No rescue, no axis.
- (b) STRONG, **not** near-STRONGEST (third-party tool *about* skills, not substrate/behavior-layer).
- GOAL-ALIGNED, **not** OFF-GOAL (overriding the workflow's shared error).
- No new top-level pattern; no confirmed-count change (46 / 10). 1 new §C standalone (≤2 cap).
