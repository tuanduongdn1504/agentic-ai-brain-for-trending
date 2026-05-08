# Entity: /codex:adversarial-review prompt-framing mechanism (counter-evidence to Pattern #76)

> **Wiki:** codex-plugin-cc v62 / 2026-05-08
> **Format:** 13-section entity page (focus: counter-evidence-driven refinement of Pattern #76)

---

## 1. Identity

**`/codex:adversarial-review`** is codex-plugin-cc's adversarial-review slash command that **reframes the existing review function** with adversarial system/user prompts to pressure-test design decisions. Mechanism: prompt-engineering variant within same Codex review function — NOT separate-role architectural primitive.

## 2. Source

- README excerpt: *"a steerable challenge review"* that *"reframes the existing review function"* to *"pressure-test assumptions, tradeoffs, failure modes, and whether a different approach would have been safer or simpler"*
- Inferred implementation: prompt template at `plugins/codex/prompts/adversarial-review.md` (or similar) within plugin
- Invocation: `/codex:adversarial-review [--base <ref>] [custom focus text]`

## 3. Counter-evidence to Pattern #76

Pattern #76 was registered at v63 EARLY mini-audit (1 wiki ago) with cc-sdd v61 evidence:

> Pattern #76 Adversarial Subagent Review Architecture at Framework Level — registered N=1 stale-risk-flagged. Evidence: cc-sdd v61 — `/kiro-impl` autonomous mode dispatches Implementer subagent (TDD: RED→GREEN→REFACTOR) + Reviewer subagent (`kiro-review`: spec compliance / boundary fit / mechanical verification / RED-phase evidence) with auto-debug-on-rejection (`kiro-debug` returns ROOT_CAUSE/CATEGORY/FIX_PLAN/NEXT_ACTION) + fresh-evidence completion gate (`kiro-verify-completion`).

**Required for promotion:** 2+ frameworks with adversarial-by-design subagent role separation as documented architectural primitive (explicit reviewer + implementer + rejection loop).

**codex-plugin-cc's `/codex:adversarial-review` analysis against Pattern #76 criteria:**

| Pattern #76 criterion | cc-sdd v61 (N=1 baseline) | codex-plugin-cc v62 |
|---|---|---|
| Adversarial-by-design (yes/no) | YES | YES |
| Subagent role separation | YES (3 distinct subagents) | **NO (same review function)** |
| Documented architectural primitive | YES (skill files) | **NO (prompt template variation)** |
| Implementer + reviewer | YES | NO (review-only, no implementer pipeline) |
| Rejection loop | YES (auto-debug returns) | NO (review output to user) |
| **Verdict** | **N=1 architectural-primitive evidence** | **NOT N=2 architectural-primitive; counter-evidence narrowing scope** |

## 4. Mechanism distinction (key insight)

**Two distinct strata of adversarial-review:**

### Stratum A — Architectural role-separation (cc-sdd v61)
- Separate subagents with distinct lifecycle
- Each subagent has own skill file + invocation path
- Runtime architecture changes between roles (different system prompts, different tool access, different state)
- Pattern #76 baseline scope

### Stratum B — Prompt-framing variant (codex-plugin-cc v62)
- Same skill / function with prompt template variation
- Single subagent invokes different prompts based on user intent
- No runtime architecture changes; prompt-engineering only
- **Distinct sub-mechanism** — sister to Pattern #76, not within it

**Both deliver "adversarial-review behavior" outcome category but at fundamentally different implementation strata.**

## 5. Refinement proposed

**Pattern #76 formulation refinement (v66 mini-audit candidate):**

> Pattern #76 Adversarial Subagent Review Architecture at Framework Level — narrowed-scope: AI agent frameworks codify adversarial-by-design **subagent role separation as architectural primitive** — implementer subagent + reviewer subagent + auto-debug + fresh-evidence completion gate. **Explicit role boundaries enforced by separate skill/agent files**, not just prompt template variation within same function.

**NEW sister candidate (v66 mini-audit registration target):**

> Pattern #XX Adversarial-Review-as-Prompt-Framing Variant — AI agent frameworks codify adversarial-review behavior via **prompt-template variation within single review function**. Same skill, different prompt; no runtime architecture changes. Distinct from Pattern #76's role-separation architectural primitive. Codex-plugin-cc v62 N=1 stale-flagged baseline.

## 6. Differentiators

| Dimension | Stratum A (Pattern #76) | Stratum B (NEW sister) |
|---|---|---|
| Implementation cost | High (multiple subagents + skill files + lifecycle) | Low (1 prompt template addition) |
| Reusability | High (each subagent reusable independently) | Medium (prompt-template-shaped tied to host function) |
| Composability | High (role-separation enables pipelines) | Low (single function variant) |
| Outcome quality | Potentially-higher (separate tool-access per role) | Variable (depends on prompt-engineering quality) |
| Adoption barrier | Higher (architecture overhead) | Lower (prompt template addition) |

**Operator predictability:** Stratum B (prompt-framing) likely MORE common in corpus than Stratum A (architectural). Stratum A requires methodology investment; Stratum B requires only prompt-engineering skill.

**Hypothesis:** As corpus grows, Stratum B observations will likely outnumber Stratum A by 3-5×. Watch for confirmation.

## 7. Origin / lineage

- OpenAI prompt-engineering competence direct lineage (Codex CLI history of prompt variations)
- LLM-as-judge research influence (constitutional AI / red-teaming) — implicit
- Adversarial-review as concept predates AI-agent frameworks (code review with devil's advocate role is decades old)
- codex-plugin-cc adopts prompt-framing approach because architectural-role-separation would require restructuring Codex backend (out of scope for plugin)

## 8. Adoption signals

- `/codex:adversarial-review` is one of 2 review commands surfaced (alongside `/codex:review`); promoted as primary feature
- Custom focus text + `--base <ref>` flag = interface design suggesting common usage pattern
- Background-mode support (`/codex:adversarial-review --background`) suggests long-running adversarial reviews expected
- Workflow examples in README emphasize `/codex:adversarial-review` for design-decision review

## 9. Limitations / failure modes

- Same-function-same-tool-access: adversarial review cannot use different tool surface than standard review (cc-sdd's separate `kiro-review` could have different tool boundaries; codex-plugin-cc cannot)
- Prompt-engineering brittle: adversarial-prompt template may degrade across model versions; cc-sdd's role-separation more robust
- No auto-debug pipeline: review output goes to user, not back into rejection loop
- Cannot invoke implementer corrections: read-only review (Pattern #76's adversarial-architectural-primitive integrates implementer + reviewer + corrections)

## 10. Storm Bear vault applicability

Worth comparison-pilot vs cc-sdd v61 `kiro-review`:
- Run both on same diff
- Measure: detection-quality (catches what other misses?) / ergonomics / cost / latency
- Inform Pattern #76 vs sister-pattern formulation at v66 audit

**Pilot relevance: HIGH for COMPARISON purpose**, MEDIUM as standalone tool (since cc-sdd already provides review-augmentation).

## 11. Open questions

- Q1: Is `/codex:adversarial-review` purely prompt-template, or does it dispatch separate Codex session with adversarial system prompt?
- Q11: Pattern #76 counter-evidence handling — narrow scope OR register sister pattern? (Routine v2.1 §"Counter-evidence-driven refinement" suggests narrow-scope; but Stratum A vs B are mechanistically distinct enough to warrant separate pattern.)

## 12. Cross-references

- [cc-sdd v61](../../cc-sdd%20-%20Beginner%20Analysis/) — Pattern #76 N=1 architectural-primitive baseline
- Pattern #76 entry in `_patterns/03-active-candidates.md`
- Routine v2.1 §"Counter-evidence-driven refinement (v2.1 formalized)" — refinement protocol

## 13. Next action

For Pattern Library v66 mini-audit:
1. Apply counter-evidence-driven refinement to Pattern #76 (narrow scope to architectural-role-separation specifically)
2. Register NEW sister candidate "Adversarial-Review-as-Prompt-Framing Variant" N=1 stale-flagged
3. Document Stratum A / Stratum B distinction as Pattern Library taxonomy

For Storm Bear vault:
- Comparison pilot (cc-sdd v61 + codex-plugin-cc v62 on same diff) — would inform both Pattern #76 architectural-primitive evidence + sister-pattern prompt-framing-variant evidence
