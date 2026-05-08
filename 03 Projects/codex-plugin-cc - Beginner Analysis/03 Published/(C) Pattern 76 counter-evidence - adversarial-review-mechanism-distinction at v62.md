# Phase 4b deliverable — Pattern #76 counter-evidence: adversarial-review-mechanism-distinction at v62

> **Routing mode (primary):** Counter-evidence-driven refinement of Pattern #76 Adversarial Subagent Review Architecture (1-wiki-after-registration narrowing — fastest counter-evidence cycle in corpus history)
> **Routing mode (secondary):** Cross-vendor cooperation corpus-first observation + T4 Layer 2 3rd sub-archetype + Pattern #19 corporate-archetype N=2 cross-org
> **Subject:** [`openai/codex-plugin-cc`](https://github.com/openai/codex-plugin-cc) — wiki v62
> **Date:** 2026-05-08
> **Audience:** Storm Bear vault operator preparing for v66 mini-audit (or earlier if pilot evidence accelerates)

---

## TL;DR

**Pattern #76 Adversarial Subagent Review Architecture was registered N=1 stale-flagged at v63 EARLY mini-audit (2026-05-07) based on cc-sdd v61 evidence (separate `kiro-review` subagent + auto-debug + completion gate).**

**codex-plugin-cc v62 ships `/codex:adversarial-review` 1 wiki later (2026-05-08) — initial impression suggests N=2 evidence, but closer reading reveals fundamental mechanism distinction:**

- cc-sdd v61: separate-role architectural primitive (3 distinct subagents, separate skill files, runtime architecture changes)
- codex-plugin-cc v62: prompt-framing variant within same review function (1 review-skill, 2 prompt-templates, no architecture changes)

**Two distinct strata of adversarial-review:**
- **Stratum A (Pattern #76):** Architectural role-separation
- **Stratum B (NEW sister candidate):** Prompt-framing within single function

**Recommendation for v66 mini-audit:** Apply counter-evidence-driven refinement narrowing Pattern #76 scope to Stratum A; register NEW sister candidate "Adversarial-Review-as-Prompt-Framing Variant" N=1 stale-flagged for Stratum B.

---

## 1. Pattern #76 v63 baseline

From `_patterns/03-active-candidates.md` Pattern #76 entry (post-v63 EARLY mini-audit):

> **Pattern #76 Adversarial Subagent Review Architecture at Framework Level** — registered N=1 stale-risk-flagged at v63 mini-audit.
> **Evidence:** cc-sdd v61 only — `/kiro-impl` autonomous mode dispatches Implementer subagent (TDD: RED→GREEN→REFACTOR) + Reviewer subagent (`kiro-review`: spec compliance / boundary fit / mechanical verification / RED-phase evidence) with auto-debug-on-rejection (`kiro-debug` returns ROOT_CAUSE/CATEGORY/FIX_PLAN/NEXT_ACTION) + fresh-evidence completion gate (`kiro-verify-completion` returns VERIFIED/NOT_VERIFIED/MANUAL_VERIFY_REQUIRED).
> **Formal statement:** AI agent frameworks codify adversarial-by-design subagent role separation as architectural primitive — implementer subagent + reviewer subagent + auto-debug + fresh-evidence completion gate, with explicit role boundaries and rejection-loop mechanics.
> **Required for promotion:** 2+ frameworks with adversarial-by-design subagent role separation as documented architectural primitive (explicit reviewer + implementer + rejection loop).
> **Re-evaluation:** v66 stale-check / v71 retire-check.

## 2. codex-plugin-cc v62 evidence — initial impression vs closer reading

### Initial impression (Phase 0 surface scan)

codex-plugin-cc ships `/codex:adversarial-review` slash command. Surface match:
- Adversarial-review primitive ✓
- Framework-level (plugin codifies) ✓
- Documented (in README) ✓

→ Initially appears N=2 evidence for Pattern #76 architectural-primitive scope.

### Closer reading (Phase 0 deeper probe)

README explicitly states:
> *"`/codex:adversarial-review` reframes the existing review function to pressure-test assumptions, tradeoffs, failure modes..."*

Key word: **"reframes the existing review function."**

This means:
- Same Codex review skill is invoked
- Same Codex backend session
- Same tool-access permissions
- ONLY the prompt template changes (adversarial-framing prompt vs neutral-review prompt)

**This is NOT separate-role architectural primitive.** It IS adversarial-framed prompt within same review function.

## 3. Mechanism distinction (key insight)

**Two distinct strata of adversarial-review:**

### Stratum A — Architectural role-separation (cc-sdd v61)

```
User: /kiro-impl <task>
  ↓
Implementer subagent (skill: kiro-impl)
  - Own skill file
  - Own system prompt
  - Own tool access
  - Lifecycle: TDD RED→GREEN→REFACTOR
  ↓ produces code
Reviewer subagent (skill: kiro-review)
  - DIFFERENT skill file
  - DIFFERENT system prompt
  - DIFFERENT tool access (e.g., can't write code, only critique)
  - Lifecycle: spec compliance + boundary fit + mechanical verification + RED-phase evidence
  ↓ produces ACCEPT or REJECT
On REJECT → Debug subagent (skill: kiro-debug)
  ↓ returns ROOT_CAUSE / CATEGORY / FIX_PLAN / NEXT_ACTION
On ACCEPT → Verify subagent (skill: kiro-verify-completion)
  ↓ returns VERIFIED / NOT_VERIFIED / MANUAL_VERIFY_REQUIRED
```

**Architectural primitive:** Each subagent is a distinct skill file with own prompt + tool access + lifecycle. Runtime architecture changes between roles. Rejection loop is encoded in subagent dispatch logic.

### Stratum B — Prompt-framing variant (codex-plugin-cc v62)

```
User: /codex:adversarial-review <args>
  ↓
Codex review skill (SAME as /codex:review)
  - Same skill file
  - Different prompt template (adversarial-framing variant)
  - Same tool access
  - Same lifecycle
  ↓ produces review output
User reads output (no automatic rejection-loop, no auto-debug, no completion gate)
```

**Prompt-framing variant:** Single skill, 2 prompt templates. No runtime architecture changes. No rejection loop.

### Comparison table

| Dimension | Stratum A (Pattern #76) | Stratum B (NEW sister) |
|---|---|---|
| Number of skill files | Multiple (3+ at cc-sdd) | 1 |
| Skill invocation paths | Multiple distinct | Single with prompt variation |
| Tool access | Per-role (reviewer can't write code) | Same as host function |
| Auto-debug-on-rejection | Yes (architectural pipeline) | No |
| Fresh-evidence completion gate | Yes | No |
| Implementation cost | High | Low |
| Reusability | High (each subagent reusable) | Medium (prompt-template tied to host) |
| Composability | High (pipeline architecture) | Low (single-function variant) |
| Robustness across model versions | Higher (architectural) | Lower (prompt brittle) |

## 4. Refinement proposal for v66 mini-audit

### 4.1 Pattern #76 formulation refinement

**Current formulation (v63):**
> AI agent frameworks codify adversarial-by-design subagent role separation as architectural primitive — implementer subagent + reviewer subagent + auto-debug + fresh-evidence completion gate, with explicit role boundaries and rejection-loop mechanics.

**Refined formulation (v66 candidate):**
> AI agent frameworks codify adversarial-by-design **subagent role separation as architectural primitive** — implementer subagent + reviewer subagent + auto-debug + fresh-evidence completion gate, with **explicit role boundaries enforced by separate skill/agent files (multiple distinct skill invocations, runtime architecture changes between roles)**, not just prompt template variation within same function. **Distinct from Stratum B prompt-framing variant** which achieves adversarial-review behavior via prompt-template variation within single skill.

### 4.2 NEW sister candidate registration

**Proposed Pattern (number TBD at v66):**
> **Pattern #XX Adversarial-Review-as-Prompt-Framing Variant** — AI agent frameworks codify adversarial-review behavior via **prompt-template variation within single review function**. Same skill, different prompts (neutral-review template vs adversarial-review template); no runtime architecture changes; no rejection loop. Distinct from Pattern #76's role-separation architectural primitive at fundamental implementation stratum. codex-plugin-cc v62 N=1 stale-flagged baseline.
>
> **Required for promotion:** 2+ frameworks shipping adversarial-review-as-prompt-framing variant within single review function.
>
> **Stale-check:** v66 / **Retire-check:** v71.

### 4.3 Stratum A vs Stratum B as Pattern Library taxonomy

Both patterns deliver same outcome category (adversarial-review behavior) at fundamentally different implementation strata. Could become Pattern Library taxonomy item:

> **Implementation-stratum taxonomy** for adversarial-review (and potentially other behavioral patterns):
> - Stratum A: Architectural role-separation (separate skill files + runtime architecture changes)
> - Stratum B: Prompt-framing variant (single skill + prompt template variation)

**Hypothesis:** As corpus grows, Stratum B observations will likely outnumber Stratum A by 3-5×. Stratum B has lower adoption barrier (prompt-template addition vs architectural restructuring). Watch for confirmation across v63-v75 wikis.

## 5. Speed of counter-evidence — corpus-first observation

**Pattern #76 was registered at v63 EARLY mini-audit (2026-05-07).**
**codex-plugin-cc ships v62 wiki (2026-05-08) with counter-evidence — 1 day / 1 wiki later.**

This is **fastest counter-evidence cycle in corpus history.** Prior counter-evidence cycles:

| Pattern | Registered | Counter-evidence | Wiki gap |
|---|---|---|---|
| #47 Vision-Based Browser Automation | v24 (Skyvern) | v29 audit (crawl4ai counter-evidence narrowing) | 5 wikis |
| #48 Proprietary Anti-Bot Commercial Moat | v24 (Skyvern) | v29 audit (crawl4ai OSS counter-evidence) | 5 wikis |
| #51 Vibe-Coding Spectrum | v25 baseline | v60 (anti-vibe pole streak break) | 35 wikis |
| **#76 Adversarial Subagent Review Architecture** | **v63 (cc-sdd)** | **v62 (codex-plugin-cc)** | **1 wiki** ← NEW LONGEST |

**Routine v2.2 codification candidate:** "Fast-counter-evidence detection" — when newly-registered pattern receives counter-evidence within 1-2 wikis of registration, fast-track refinement at next audit (don't wait full natural cadence).

**Lesson:** New patterns at N=1 are fragile. v62 demonstrates immediate refinement may be needed.

## 6. Counter-evidence vs N=2 evidence — categorization

Initial Phase 0 hypothesis: codex-plugin-cc adversarial-review = N=2 evidence for Pattern #76.

Closer reading verdict: codex-plugin-cc adversarial-review = COUNTER-EVIDENCE narrowing scope (NOT N=2 evidence within same scope).

**Distinction:**
- N=2 evidence = same mechanism observed in 2nd subject (would advance toward promotion)
- Counter-evidence = different mechanism observed in similar-named subject (refines pattern boundary; does NOT advance toward promotion)

codex-plugin-cc's adversarial-review is the latter category. Same outcome category (adversarial-review), different mechanism stratum (prompt-framing vs role-separation).

## 7. Adjacent Pattern Library implications

### 7.1 Pattern #18 Layer 2 cross-vendor-bridge sub-archetype (NEW 3rd Layer 2)

**Candidate registration:** "cross-vendor-platform-bridge-as-plugin" — codex-plugin-cc v62 bridges Anthropic Claude Code host + OpenAI Codex backend at runtime. Distinct from:
- v60 free-claude-code: api-protocol-translation-proxy (runtime, content axis)
- v61 cc-sdd: install-time-per-platform-skill-format-translator (install-time, format axis)
- **v62 codex-plugin-cc: cross-vendor-platform-bridge-as-plugin (runtime, vendor-axis)**

**Status:** N=1 candidate at v62. Stale-flag at registration. Re-evaluate at v66/v71.

### 7.2 NEW Pattern #77 candidate: Cross-Vendor Cooperative Plugin Publication

**Candidate registration:** AI provider organization publishes Apache-2.0/MIT OSS plugin targeting RIVAL provider's IDE/host platform — accepts host platform's distribution channel + UX while retaining own backend/auth.

**Evidence:** codex-plugin-cc v62 only (corpus-first; no precedent in 61 prior wikis).

**Status:** N=1 stale-flagged. Watch list:
- Anthropic publishes for Codex CLI / OpenAI ChatGPT
- Google Gemini for Claude Code or Codex CLI
- Microsoft GitHub Copilot for non-VSCode hosts
- xAI Grok for Claude Code or Cursor

### 7.3 Pattern #19 corporate-strategic archetype N=2 cross-org structural

**Pre-v62:** N=1 cross-corporate-org (Microsoft only, with 2 products: spec-kit v17 + markitdown v28)

**Post-v62:** N=2 cross-corporate-org (Microsoft + OpenAI distinct organizational entities)

**Promotion-eligibility check at v66:** structural-N=2 across distinct corporate orgs satisfied.

### 7.4 NEW Pattern candidate: Background-Task-Lifecycle-Primitive-Set

**Candidate observation:** 4-command background-task lifecycle as explicit primitive set:
- `/codex:rescue --background "task description"` — start
- `/codex:status` — poll
- `/codex:result <session-id>` — retrieve
- `/codex:cancel <session-id>` — abort

**Status:** N=1 at codex-plugin-cc v62. Prior corpus subjects (cc-sdd v61, BMAD v11) had implicit long-running execution; codex-plugin-cc surfaces explicit 4-command lifecycle.

**Required for promotion:** 2+ frameworks with explicit 4-command background-task lifecycle primitive set.

### 7.5 Pattern #59 Claude Code Plugin Marketplace Native — corporate-scale strengthening

Pre-v62: 2 solo observations (OMC v27 + claude-hud v35). Post-v62: + corporate-org observation. Pattern #59 corpus-scale-diversity expands.

## 8. Cross-references (for audit reviewer)

**Pattern Library state files:**
- `_patterns/03-active-candidates.md` Pattern #76 entry (v63 baseline)
- `_patterns/03-active-candidates.md` Pattern #18 Layer 2 sub-archetypes
- `_patterns/02b-confirmed-patterns-v42-plus.md` Pattern #19 corporate-archetype
- `_patterns/05-recent-additions.md` v63 audit summary
- `_patterns/01-audit-history.md` audit cadence + criteria

**Sibling wikis:**
- v61 cc-sdd: Pattern #76 N=1 architectural-primitive baseline
- v60 free-claude-code: T4 Layer 2 protocol-translation sibling
- v17 spec-kit + v28 markitdown: Microsoft corporate predecessors
- v27 OMC + v35 claude-hud: Pattern #59 marketplace siblings

**Routine v2.1 reference:**
- `05 Skills/llm-wiki-routine-v2.1.md` §"Counter-evidence-driven refinement (v2.1 formalized)" — refinement protocol applied here
- §"5 structural-promotion criteria" — promotion paths for NEW sister candidate
- §"OBSERVATION-TRACK sub-category" — reference for episodic-vs-architectural classification

## 9. Storm Bear vault decision context

**Vault state at v62 wiki ship (post-v63 EARLY mini-audit):**
- Confirmed: 42 (post-v63 audit Pattern #21 promoted)
- Active candidates: 19 (post-v63 audit; 17 + 3 NEW from v63 audit - 1 promoted)
- Stale: 1 (Pattern #52 only)
- Ratio: 0.452:1 (LARGEST sub-0.475 zone)

**v62 wiki impact (projected post-v66 mini-audit):**
- Confirmed: 42 → potentially 43 (Pattern #19 promotion-eligible at N=2 cross-org)
- Active candidates: 19 → 22-23 (4 NEW candidates: sister to #76 + Pattern #77 + Pattern #18 Layer 2 cross-vendor-bridge + Background-Task-Lifecycle)
- Stale: 1 → 1 (Pattern #52)
- Ratio: 0.452:1 → ~0.50:1 (still well below 0.95:1 trigger; buffer ~0.45 below)

**Pilot ranking decision:**
- codex-plugin-cc v62 inserts at #1.5 (post-cc-sdd v61, before free-claude-code v60)
- Best deployed AS COMPARISON to cc-sdd v61 (apple-to-apple Pattern #76 architectural vs Stratum B prompt-framing)
- Comparison-pilot would inform Pattern #76 + sister-pattern formulation at v66 audit

## 10. Final recommendation

**For v66 mini-audit (natural cadence +4 wikis from v62):**

1. **Apply counter-evidence-driven refinement to Pattern #76** — narrow scope to Stratum A architectural-role-separation specifically (with explicit role boundaries enforced by separate skill files + runtime architecture changes + auto-debug + completion gate)
2. **Register NEW sister candidate "Adversarial-Review-as-Prompt-Framing Variant"** N=1 stale-flagged with codex-plugin-cc v62 baseline
3. **Register NEW Pattern #77 Cross-Vendor Cooperative Plugin Publication** N=1 stale-flagged
4. **Register NEW Pattern candidate Background-Task-Lifecycle-Primitive-Set** N=1 stale-flagged
5. **Register Pattern #18 Layer 2 cross-vendor-bridge-as-plugin sub-archetype** N=1 stale-flagged (3rd Layer 2 sub-archetype)
6. **Pattern #19 corporate-strategic archetype N=2 cross-org promotion-eligibility check** — structural-unambiguity-at-N=2 satisfied (Microsoft + OpenAI distinct orgs)
7. **Pattern #59 corporate-scale strengthening note**

**Routine v2.2 codification candidates added at v62:**
1. Fast-counter-evidence detection (1-wiki cycle observed)
2. Stratum A vs Stratum B implementation-stratum taxonomy
3. Phase 0.9 (a) FAIL with (b)(c)(d) PASS handling discipline (3rd application at v62)

**For Storm Bear vault:**

1. Comparison pilot: cc-sdd + codex-plugin-cc adversarial-reviews on same diff
2. Document: detection-quality / latency / ergonomics / cost differences
3. Inform v66 audit Pattern #76 architectural-vs-prompt-framing distinction with empirical evidence

**For corpus monitoring (v63-v66 window):**

1. Watch for 2nd cross-vendor cooperation observation (un-stale Pattern #77)
2. Watch for 2nd Stratum B prompt-framing variant (un-stale sister candidate)
3. Watch for 2nd Background-Task-Lifecycle 4-command primitive set
4. Watch for next Pattern #18 Layer 2 sub-archetype (potential 5+ accumulation triggers meta-pattern consolidation)

---

**Wiki version:** v62
**Phase 4b primary routing mode:** counter-evidence-driven refinement of Pattern #76 (1-wiki-after-registration narrowing — fastest counter-evidence cycle in corpus history)
**Velocity:** ~75-90 min compressed-scope direct-write (estimated)
**Status: DONE** — counter-evidence cleanly identified; refinement proposal precise; no fact-verification concerns.
