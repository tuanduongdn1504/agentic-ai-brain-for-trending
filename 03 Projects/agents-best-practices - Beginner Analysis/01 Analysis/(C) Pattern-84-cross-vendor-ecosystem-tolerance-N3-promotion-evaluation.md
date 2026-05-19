# Pattern #84 (Cross-Vendor Ecosystem-Tolerance) — N=3 Promotion Evaluation

**Type:** Pattern Library promotion evaluation | **Phase:** Phase 4b PRIMARY | **Scope:** Pattern #84 CANDIDATE → CONFIRMED transition assessment | **v71 Contribution:** N=2 → N=3 with NEW sub-typology 84c "Provider-Agnostic-By-Design" registration proposal

---

## Executive Summary

**Verdict: RECOMMEND PROMOTION of Pattern #84 from CANDIDATE to CONFIRMED status.**

agents-best-practices (v71) provides the **third N=3 evidence** for Pattern #84 (Cross-Vendor Ecosystem-Tolerance), meeting promotion criteria with high confidence. v71 introduces a **NEW sub-typology 84c "Provider-Agnostic-By-Design"** that enriches the pattern hierarchy and distinguishes **author design choice** (v71) from **ecosystem norm** (v62 + v65).

**v72 audit batch action:** Formal promotion decision + 84c sub-typology registration.

---

## Current Pattern #84 Status

### Definition

**Pattern #84 (Cross-Vendor Ecosystem-Tolerance):** "Agentic-AI ecosystem operates under emerging norm of cross-vendor tolerance for competitor-published or third-party artifacts."

### Current Evidence (N=2)

**v62: codex-plugin-cc**
- **Type:** T4 Bridge (OpenAI plugin ↔ Claude Code)
- **Evidence:** OpenAI publishes plugin **explicitly targeting Claude Code**, demonstrating tool-level cross-vendor tolerance
- **Sub-archetype:** 84a "Tool-Tolerance" (vendor-neutral tool publishing norm)
- **Mechanism:** Ecosystem norm driving cross-vendor cooperation

**v65: claude-code-system-prompts**
- **Type:** T1 Reference-archive (Anthropic product documentation)
- **Evidence:** Anthropic **documents Claude Code internals** for cross-vendor ecosystem awareness (helping OpenAI/third-party developers understand Claude Code patterns)
- **Sub-archetype:** 84b "Usage-Enforcement" (vendor-native documentation enabling cross-vendor usage)
- **Mechanism:** Ecosystem norm driving documentation transparency

### Pattern Status

**Current:** CANDIDATE at N=2
- **Criterion 1 (≥3 cross-corpus):** FAIL at N=2 (requires N=3 minimum)
- **Criterion 2 (≥2 sub-variants):** PASS at 84a + 84b (2 variants present)
- **Criterion 3 (consistent mechanism):** PASS (both reduce friction in cross-vendor agentic ecosystem)
- **Criterion 4 (corpus integration):** PASS (positioned for multi-vendor agent-skill discovery)
- **Criterion 5 (actionability):** PASS (informs cross-vendor architecture design)

**Promotion barrier:** Criterion 1 requires N=3; N=2 insufficient.

---

## v71 Evidence: agents-best-practices

### Repository Overview

**Repository:** https://github.com/DenisSergeevitch/agents-best-practices
**Author:** DenisSergeevitch (solo developer)
**Created:** 2026-05-15 (4 days old at wiki-build)
**Stats:** 821 stars, 72 forks, fork_ratio 0.088 (healthy)
**Type:** T1 Assistant Skill (markdown-only governance framework)
**Platforms:** 3 (Claude Code + Codex + OpenAI Agents)

### Provider-Agnostic Architecture

**Key Finding:** agents-best-practices is **explicitly provider-neutral** with **equal coverage of BOTH OpenAI and Anthropic patterns**.

#### OpenAI Coverage
- References OpenAI agents guide, function-calling, guardrails-approvals, tools-connectors-mcp, harness-engineering
- Examples use OpenAI Codex terminology alongside Claude Code
- Tool taxonomy applicable to OpenAI function-calling + MCP connectors

#### Anthropic Coverage
- References Anthropic: building-effective-agents, context-engineering, writing-tools-for-agents, long-running-agents, equipping-agents-for-the-real-world-with-agent-skills
- Examples use Claude Code skill semantics alongside OpenAI patterns
- Autonomy levels (L0-L4) integrate Claude Code practice

#### Vendor Preference Assessment
- **No vendor preference in documentation:** Code examples do not favor one vendor
- **No asymmetric coverage:** OpenAI + Anthropic sections are balanced in depth
- **No vendor-specific lock-in:** 15 reference files are platform-neutral; installable on 3 platforms without vendor-specific code

### Evidence Classification: Sub-Typology 84c

**v71 introduces NEW phenomenon not observed in v62 or v65:**

| Dimension | v62 (84a Tool-Tolerance) | v65 (84b Usage-Enforcement) | v71 (84c Provider-Agnostic-By-Design) |
|---|---|---|---|
| **Locus of Initiative** | OpenAI initiative (publishes cross-vendor) | Anthropic initiative (publishes cross-vendor) | Individual-author initiative (designs cross-vendor) |
| **Mechanism** | Ecosystem norm (cooperation norm) | Ecosystem norm (transparency norm) | Author design choice (intentional provision) |
| **Directedness** | Passive (OpenAI + Claude tolerance implicit) | Passive (Anthropic + OpenAI tolerance implicit) | Active (DenisSergeevitch explicitly unifies both) |
| **Evidence Type** | Artifact (plugin targeting Claude Code) | Documentation (system-prompt internals exposed) | Framework (unified governance framework) |
| **Archetype Shift** | Norm-driven | Norm-driven | Choice-driven |

### Promotion Criteria Application

**Criterion 1: ≥3 cross-corpus evidence**
- **v62:** ✓ codex-plugin-cc (T4 Bridge)
- **v65:** ✓ claude-code-system-prompts (T1 Reference)
- **v71:** ✓ agents-best-practices (T1 Skill)
- **Result:** PASS at N=3 across 3 distinct Tier-Archetype combinations

**Criterion 2: ≥2 sub-variants with consistent mechanism**
- **84a (Tool-Tolerance):** v62 evidence present
- **84b (Usage-Enforcement):** v65 evidence present
- **84c (Provider-Agnostic-By-Design):** v71 evidence present (NEW)
- **Result:** PASS at 3 sub-variants; consistent mechanism (all reduce cross-vendor friction)

**Criterion 3: Consistent mechanism across evidence**
- **v62 mechanism:** Vendor A publishes for Vendor B → reduces tool-availability friction
- **v65 mechanism:** Vendor publishes docs for ecosystem → reduces knowledge friction
- **v71 mechanism:** Individual author targets all vendors equally → reduces adoption friction
- **Result:** PASS — all 3 share common mechanism (friction reduction) despite different loci

**Criterion 4: Corpus integration positioning**
- **v62 + v65:** v71 evidence is **not redundant** with prior 2 (author-choice distinct from norm-choice)
- **Future positioning:** Sub-typology 84c uniquely positions corpus for monitoring **individual-author provider-agnostic designs** (signals independent author trend toward multi-vendor thinking)
- **Actionability:** Sub-typology 84c informs agent-skill design discipline (authors should ask: "Am I designing for 1 vendor or all?")
- **Result:** PASS — corpus integration is strengthened

**Criterion 5: Actionability for practitioners**
- **Signal to developers:** Cross-vendor support is a viable design choice, not accident
- **Signal to ecosystems:** Convergence toward provider-agnostic agent infrastructure
- **Signal to corpus:** Sub-typology 84c models author-level ecosystem tolerance (enriches pattern understanding)
- **Result:** PASS — actionable across 3 stakeholder groups

### Overall Criterion Assessment

| Criterion | Result | Confidence |
|---|---|---|
| **1. ≥3 cross-corpus** | PASS | HIGH (N=3 clearly achieved) |
| **2. ≥2 sub-variants** | PASS | HIGH (3 variants identified + consistent) |
| **3. Consistent mechanism** | PASS | HIGH (friction reduction mechanism spans all 3) |
| **4. Corpus integration** | PASS | HIGH (84c uniquely positions for future monitoring) |
| **5. Actionability** | PASS | HIGH (informs author design discipline) |

---

## Sub-Typology 84c Proposal: "Provider-Agnostic-By-Design"

### Definition

**Sub-typology 84c (Provider-Agnostic-By-Design):** Individual authors intentionally create agent frameworks, tools, or skills that serve **multiple AI providers equally** without vendor preference or lock-in.

### Distinguishing Features

1. **Intentional Design:** Author explicitly targets multiple vendors in design phase (not retrofitted)
2. **Equal Coverage:** Documentation, examples, and reference implementations are balanced across vendors
3. **No Lock-In:** Skill/tool is portable across platforms; no vendor-specific code or assumptions
4. **Author Autonomy:** Design choice driven by individual author, not ecosystem norm or vendor incentive
5. **Synthesis:** Author integrates competing vendor patterns into unified framework

### Evidence (v71)

**agents-best-practices demonstrates all 5 features:**
1. ✓ Designed to integrate OpenAI + Anthropic patterns from inception
2. ✓ 15 reference files cover Codex, Claude Code, OpenAI Agents equally
3. ✓ Markdown-only, no vendor-specific binaries; works on all 3 platforms
4. ✓ DenisSergeevitch's solo design decision (no corporate mandate)
5. ✓ Synthesizes OWASP + NIST + MCP + Anthropic + OpenAI into unified framework

### Distinction from 84a/84b

| Aspect | 84a Tool-Tolerance | 84b Usage-Enforcement | 84c Provider-Agnostic-By-Design |
|---|---|---|---|
| **Who decides** | Vendor (OpenAI) | Vendor (Anthropic) | Individual author |
| **Scope** | Tool integration | Documentation/knowledge | Framework synthesis |
| **Motivation** | Business cooperation | Transparency strategy | Design philosophy |
| **Effort** | Plugin development | Doc writing | Comprehensive framework design |
| **Evidence type** | Binary artifact | Documentation | Skill package + philosophy |

### Promotion Readiness

**84c is promotion-ready as formal sub-typology because:**
- Clear definition (individual-author multi-vendor framework design)
- Single clear evidence (v71 agents-best-practices)
- Distinct from parent (84a/84b driven by ecosystem norms; 84c driven by author choice)
- Actionable (informs future corpus monitoring for similar author-choice patterns)

**Recommended action:** Register 84c as formal sub-typology at v71+ audit; evaluate promotion of Pattern #84 to CONFIRMED.

---

## NEW Candidate OC-O Brief

**v71 introduces separate architectural pattern that deserves observation candidate status:**

**Candidate: Agentic-Harness-Execution-Separation**

**Definition:** Formal separation of inference-layer (model proposes) from execution-layer (harness executes or rejects) via 7 explicit invariants:
1. Each tool call gets exactly one result
2. Arguments validated before execution
3. Permission decisions precede side effects
4. Results bounded, structured, traceable
5. Hard budgets enforced
6. Final answers derive from observations
7. Errors become structured observations

**Why distinct from Pattern #84:** Pattern #84 is ecosystem-level (cross-vendor tolerance). OC-O is architectural-governance-level (how to separate inference from execution safely). Not sub-pattern of #84; separate observational candidate.

**v71 Evidence:** 7-invariant loop formalization in agents-best-practices core discipline.

**Recommended action:** Register OC-O at v71+ audit pending v72+ corroboration.

---

## Pattern #84 Promotion Verdict

### Formal Recommendation

**RECOMMEND PROMOTION of Pattern #84 from CANDIDATE to CONFIRMED at v72 audit.**

### Justification

1. **Criterion 1 PASS:** N=3 clearly achieved (v62 + v65 + v71 across 3 Tier-Archetype combinations)
2. **Criterion 2 PASS:** 3 sub-variants identified (84a + 84b + 84c); consistent mechanism
3. **Criterion 3 PASS:** Cross-vendor friction reduction theme consistent across all 3 evidence
4. **Criterion 4 PASS:** Sub-typology 84c uniquely enriches corpus positioning and future monitoring
5. **Criterion 5 PASS:** Actionable across developer, ecosystem, and corpus stakeholder groups

### Strength Assessment

**Confidence: HIGH** — All 5 promotion criteria PASS with clear evidence. Sub-typology 84c proposal is well-defined and distinct. No internal contradictions.

### Acceleration Note

**Timing Recommendation:** Promote at v72 audit (immediately next audit cycle) rather than deferring. Rationale:
- v71 evidence is strong (comprehensive framework, not marginal feature)
- Sub-typology 84c enriches pattern understanding (not a burden to register)
- Corpus positioned to monitor 84c trend (individual-author multi-vendor designs may increase)
- No dependencies on other pattern states; promotion is orthogonal to other changes

---

## v72 Audit Batch Actions (from v71)

### Pattern #84 Promotion Block

1. **Formal promotion decision:** CONFIRMED (if v71 evaluation endorses PASS verdict)
2. **Sub-typology 84c registration:** "Provider-Agnostic-By-Design" formal entry (update PATTERN_LIBRARY.md chapter files)
3. **Corpus-subject tagging:** v62, v65, v71 tagged with 84a/84b/84c respectively
4. **State update:** Pattern Library state = 44 confirmed (if Pattern #84 promoted from CANDIDATE)

### OC-O Candidacy Block

5. **OC-O registration:** "Agentic-Harness-Execution-Separation" observational candidate (pending v72+ evaluation)
6. **OC-O evidence:** v71 agents-best-practices 7-invariant formalization cited
7. **OC-O corroboration decision:** Accept v71 solo evidence or defer until v72+ second corpus subject?

### Related Stale Checks

8. **Pattern #78 (Living-Domain-Standards):** v71 within-pattern strengthening (N=3 sub-mechanism 78a multi-vendor); no promotion implied
9. **Pattern #83 (Honest-Deficiency-Disclosure):** v71 within-pattern strengthening (83b methodology); no promotion implied
10. **Pattern #21 (SDD Methodology):** v71 within-pattern strengthening (7-invariant formalization); no promotion implied
11. **Pattern #66 (Supply-Chain Isolation):** v71 within-pattern strengthening (66d malicious skill packages); no promotion implied

---

## Checklist for v72 Audit Incorporation

- [ ] Re-read v71 agents-best-practices evidence (confirm N=3 meets criteria)
- [ ] Validate 84c "Provider-Agnostic-By-Design" definition (distinct from 84a/84b)
- [ ] Assess OC-O "Agentic-Harness-Execution-Separation" candidacy (distinct from existing patterns)
- [ ] Update PATTERN_LIBRARY.md state block (Pattern #84 CONFIRMED + 84c sub-typology + OC-O NEW)
- [ ] Update CLAUDE.md weekly update § (v71 promotion decision + state changes)
- [ ] Update _patterns/05-recent-additions.md (v71 wiki-ship narrative + promotion verdict)
- [ ] Tag v62/v65/v71 corpus-subjects with 84a/84b/84c in project CLAUDE.md files
- [ ] Confirm no contradictions with other v72 audit items (Pattern #83 promotion, Pattern #19 enrichment, etc.)

---

## Appendix: Promotion Criteria Framework Reference

**CONFIRMED pattern requires all 5 criteria PASS:**

| Criterion | Definition | v71 Result |
|---|---|---|
| **1. ≥3 cross-corpus** | Evidence from ≥3 independent corpus subjects | PASS (v62 + v65 + v71) |
| **2. ≥2 sub-variants** | ≥2 distinct sub-archetypes or mechanisms | PASS (84a + 84b + 84c) |
| **3. Consistent mechanism** | All evidence demonstrates same underlying pattern | PASS (cross-vendor friction reduction) |
| **4. Corpus integration** | Evidence uniquely enriches corpus positioning | PASS (84c monitors author-choice trend) |
| **5. Actionability** | Pattern informs practitioner design discipline | PASS (3 stakeholder groups) |

**Promotion verdict criteria:**
- **All 5 PASS:** Recommend PROMOTION
- **4 PASS, 1 FAIL:** Hold for next audit
- **<4 PASS:** Remain CANDIDATE or RETIRE

---

## Summary

**agents-best-practices (v71) meets all criteria for Pattern #84 promotion to CONFIRMED status.** v71 introduces third N=3 evidence and NEW sub-typology 84c "Provider-Agnostic-By-Design" that enriches the pattern hierarchy. Recommend formal promotion decision at v72 audit. OC-O "Agentic-Harness-Execution-Separation" registered as NEW observational candidate pending v72+ evaluation.

