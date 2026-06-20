# (C) PRIMARY — SkillSpector (v169) — 1 NEW §C standalone + secondary observations + 2 corrections

**Subject:** `NVIDIA/SkillSpector` — defensive-security scanner for AI-agent skill packages.
**Pattern outcome shape:** the v158/v165 shape — **1 corpus-first §C standalone (N=1) + clean secondary observations, NO mint, NO confirmed-count change.**

---

## PRIMARY — 1 NEW Library-vocab §C standalone (N=1, CORPUS-FIRST)

### "Defensive-Security Scanner for the Agent-Skills Ecosystem (two-stage static + optional-LLM, risk-scored, multi-format/SARIF)"

A dedicated tool whose **entire purpose** is to detect vulnerabilities and malicious patterns in agent-skill *packages* **before installation**:

- static pattern-match + Python **AST** + **taint-tracking** + **YARA** signatures (16 categories, 64 patterns) →
- **optional LLM semantic** judgement (provider-pluggable) to reason about intent and cut false positives →
- a **0–100 risk score** + per-finding severity + recommendations →
- **multi-format output** (terminal / JSON / markdown / **SARIF** for CI & IDE security panels),
- with **live OSV.dev CVE lookups** (SC4) and **MCP-specific** checks (tool-poisoning, least-privilege).

**Why CORPUS-FIRST.** No prior subject is a *defensive security scanner for agent skills*. The two nearest security neighbours are honestly distinct:

- **shannon (v45)** — an **offensive** autonomous AI **web/API pentester** (T5 agent-as-application; *attacks running applications*, "POC or it didn't happen"). Opposite posture (offensive vs defensive), different target (running web apps vs skill artifacts), different tier (T5 autonomous agent vs T1 scanner tool).
- **magika (v44)** — Google-Research **ML file-type classification** (security-adjacent: routes files to scanners). A classifier, not a vulnerability scanner; not agent-skills-specific.

SkillSpector is neither offensive nor a classifier — it is **defensive vetting of agent-skill artifacts**, a new functional domain for the corpus.

**Distinct from adjacent vault concepts:**
- vs **Pattern #66 (supply-chain awareness)** — #66 is *passive awareness/attribution* (a subject screens `curl|bash`, is *aware* of supply-chain risk, often as a secondary trait). SkillSpector is an *active dedicated scanner*; supply-chain is just **1 of its 16 categories**. SkillSpector is the **active-scanner complement** to #66 — cross-referenced, not an instance of it.
- vs the agent-skills *authoring* chain (v76 agent-skills-standard, the agentskills.io #57 chain, v168 ponytail) — those **produce/define** skills; SkillSpector **vets** them. Same ecosystem, opposite end of the lifecycle.

**§28 compliance:** 1 new standalone (≤2 cap honored). **PROMOTION-ELIGIBLE at a genuine 2nd defensive scanner for agent skills.** Time-aware stale-watch: ≥15 wikis AND ≥30 days (§39).

**Forming meta-theme (WATCH, do not pre-merge):** *"agent-skills quality & safety tooling"* — v168 ponytail (write less code) + v169 SkillSpector (verify a skill is safe) sit on the same lifecycle axis but on **different dimensions** (code-quantity-minimalism vs security-vetting). They are NOT N=2 of one class — recording them as one would be the "generalize-the-definition-to-fit-the-2nd-instance" error the corpus explicitly guards against.

---

## SECONDARY observations (NOT minted)

### Pattern #17 variant-2 (big-tech-curator) — first NVIDIA-org author, a clean data-point

SkillSpector is the **first NVIDIA-authored subject in the 169-wiki corpus** (v72 referenced *NVIDIA NIM* only as an LLM provider). Pattern #17 variant-2 = big-tech-org-authored OSS (magika v44 = the Google-Research 2b instance). Recorded as a **data-point strengthening** of an already-CONFIRMED pattern, no new sub-mechanism.

**REJECTED (§28):** the build workflow proposed a new "**2c security-research-lab**" sub-distinction. NVIDIA's internal org-unit (official product vs research lab) is **not disclosed** on the repo, so even 2a-vs-2b is undetermined — minting a 2c is over-reach. No new sub-distinction.

### Pattern #84 84c "Provider-Agnostic-By-Design" — a scoped, distinct OBSERVATION (not a sub-mechanism mint)

SkillSpector's **semantic stage runs equally on OpenAI / Anthropic / NVIDIA** (`SKILLSPECTOR_PROVIDER`) — provider-agnostic *by design* on the **LLM-backend axis**. This is a genuine but **distinct flavor** of 84c, recorded as an observation only.

⚠️ **It is NOT ponytail's 84c.1/84c.2 mechanism** (distributing native rule files across 14 harnesses). See the correction below — the "14-platform / multi-format-output 84c, N=4→N=5" framing in the build candidate is a contamination from v168 and is rejected.

### Pattern #66 supply-chain — cross-reference (covered under PRIMARY, above)

---

## NON-claims

- **NOT a new top-level pattern** (confirmed max is #85; the scanner shape lives at the §C-standalone tier per §28 — the same discipline that rejected #86/#88 at v168).
- **NOT Pattern #52** (8.3k★/632 forks/0 releases page-stated, no creation date, §37.4 → velocity unestablishable).
- **NOT Pattern #57** (scans skills; not an agentskills.io authoring implementer; cites no corpus subjects).
- **NOT Pattern #18** (exportable LangGraph workflow = a library API, not a shared-backend service / runtime standard).
- **NOT a re-classification of #66** (active scanning ≠ passive supply-chain-awareness; different axis).

**Counts UNCHANGED: 46 patterns / 10 CONFIRMED Library-vocab.** Tracked PROVISIONAL surface ≈27 → **≈28** (+1 §C standalone).

---

## ⚠️ Two build-workflow corrections recorded (transparency, per the v168 precedent of logging over-reaches)

The v169 analysis workflow (6 recon agents → synthesis → 5 adversarial verifiers → completeness critic) produced sound *recon* (facts, (a)-precedent, model-id correction, study provenance) but its *synthesis layer* carried two cascade errors that propagated through every downstream agent. Both overridden at synthesis:

1. **TIER ERROR (critical) — "(a) FAIL → OFF-GOAL CAPTURE."** Wrong. Routine v2.5 §31 keys the tier on **(b) only**; v168 ponytail (`(a) FAIL · (b) STRONG`) shipped GOAL-ALIGNED. The agents reasoned from a shared false premise and cross-verified it. → Corrected to **GOAL-ALIGNED INCLUDE 3/4**; streak **GA:31** (not OG:12); §35 window 0 OG.
2. **PONYTAIL CONTAMINATION — "#84 84c via 14-platform cross-harness rule distribution / multi-format output, N=4→N=5."** That is v168 ponytail's distribution profile, not SkillSpector's. SkillSpector is a *scanner* with **4 output formats** and **3 LLM providers** — it does not distribute native rule files to 14 harnesses. → 84c kept only as a *scoped LLM-backend observation*; the "14-platform" corpus-first and the N-bump are rejected.

These are logged here the way v168 logged its two over-reaching verifiers (the non-existent #86/#88) — the adversarial layer is only as good as its premises, and a shared wrong premise defeats independent verification. The fix was a human-gated re-read of §31's actual text + the v168 tier precedent.
