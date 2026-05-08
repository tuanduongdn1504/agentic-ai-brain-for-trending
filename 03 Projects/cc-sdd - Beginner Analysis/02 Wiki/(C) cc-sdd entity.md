# Entity: cc-sdd (core product) — SDD harness with Skills mode primary install target

> **Wiki:** cc-sdd v61 / 2026-05-07
> **Format:** 13-section canonical entity page (per `llm-wiki-ingest.md`)

---

## 1. Identity / one-line definition

**cc-sdd** is a **multi-platform SDD harness with Agent Skills mode as primary install target** that turns approved specifications into long-running autonomous implementation across 8 AI coding agents (Claude Code, Codex, Cursor, Copilot, Windsurf, OpenCode, Gemini CLI, Antigravity).

## 2. Source

- Repo: [`gotalab/cc-sdd`](https://github.com/gotalab/cc-sdd)
- License: MIT
- Stars: 3,300 / Forks: 241 / Commits: 429 / Open issues: 16
- Primary language: TypeScript 99.6%
- Latest release: v3.0.2 (2026-04-13/14)
- Author: gotalab (solo-Japanese / "Agentic AI Engineer / Data Analyst")

## 3. Tier placement

**T1 (Assistant — SDD harness for AI coding agents).**

Sibling to spec-kit v17, OpenSpec v58, GSD v5, gsd-2 v54. Multi-platform deployment (8 agents) is distribution; methodology (SDD) is substance.

Not T4 (the bridge framing) because: bridge translates protocols/data between systems; cc-sdd translates a methodology (SDD) into per-platform skill formats. Methodology is the product, translation is the deployment.

## 4. Core mechanism

Skills mode workflow:
1. `npx cc-sdd@latest --<platform>-skills` installs SDD harness as platform-native skills
2. `/kiro-discovery` routes new work into one of 5 outcomes
3. Spec phases (requirements / design / tasks) with human-approval gates
4. `/kiro-impl` executes autonomously with TDD + adversarial review + auto-debug

**Architectural primitives (corpus-firsts marked):**

| Primitive | Purpose | Note |
|---|---|---|
| `.kiro/steering/` | Project-wide rules (product.md / tech.md / structure.md + custom) | Steering directory |
| `.kiro/specs/<feature>/` | Per-feature spec contract | Specs directory |
| `brief.md` | Discovery routing artifact | **CORPUS-FIRST** explicit pre-spec routing artifact |
| `roadmap.md` | Multi-feature project map | Discovery output for batch workflow |
| `requirements.md` | EARS-formatted acceptance criteria | **CORPUS-FIRST** explicit EARS reference |
| `research.md` | Investigation notes | Generated when discovery needs investigation |
| `design.md` + File Structure Plan | Architecture + Mermaid + FSP | **CORPUS-FIRST** explicit FSP sub-section |
| `tasks.md` | P-wave + Boundary + dependencies | **CORPUS-FIRST** P-wave priority + Boundary marker primitives |
| `spec.json` | Phase status metadata | Per-spec configuration (incl. language) |

**Skill set (6 primary):**
- 3 workflow skills: `/kiro-discovery`, `/kiro-spec-batch`, `/kiro-impl`
- 3 supporting skills: `kiro-review`, `kiro-debug`, `kiro-verify-completion`

**Adversarial review architecture:**
- Implementer subagent (does the work)
- Reviewer subagent (separate role, checks spec compliance + boundary fit + mechanical verification + RED-phase evidence)
- Auto-debug-on-rejection loop (kiro-debug returns ROOT_CAUSE / CATEGORY / FIX_PLAN / NEXT_ACTION)
- Fresh-evidence completion gate (kiro-verify-completion returns VERIFIED / NOT_VERIFIED / MANUAL_VERIFY_REQUIRED)

## 5. Workflow

```
User idea
  │
  ▼
/kiro-discovery → brief.md + (optional roadmap.md)
  │ Routes into 5 outcomes:
  │   1. Extend existing spec
  │   2. Direct implementation
  │   3. Single spec creation
  │   4. Multi-spec decomposition
  │   5. No spec needed
  ▼
/kiro-spec-init → spec.json + spec directory
  ▼
/kiro-spec-requirements → requirements.md (EARS-format)
  │ [HUMAN APPROVAL GATE]
  ▼
[optional: /kiro-validate-gap (brownfield)]
  ▼
/kiro-spec-design → design.md (architecture + Mermaid + File Structure Plan) + research.md (if needed)
  │ [HUMAN APPROVAL GATE]
  ▼
[optional: /kiro-validate-design (GO/NO-GO)]
  ▼
/kiro-spec-tasks → tasks.md (P-waves + Boundaries + dependencies)
  │ [HUMAN APPROVAL GATE]
  ▼
/kiro-impl
  │ Autonomous mode: fresh-roles per iteration
  │   ↓
  │   Implementer subagent (TDD: RED → GREEN → REFACTOR)
  │   ↓
  │   Reviewer subagent (kiro-review: spec compliance / boundary / mechanical / RED-evidence)
  │   ↓
  │   On rejection: kiro-debug → fix → retry
  │   ↓
  │   On pass: kiro-verify-completion → VERIFIED → mark complete
  ▼
[optional: /kiro-validate-impl (test coverage + traceability)]
```

## 6. Differentiators (vs other corpus T1 SDD frameworks)

| Dimension | spec-kit v17 | OpenSpec v58 | GSD v5 / gsd-2 v54 | **cc-sdd** |
|---|---|---|---|---|
| **Org archetype** | Corporate (Microsoft) | Pseudonymous-org (Fission-AI) | Solo-product-line (gsd-build) | **Solo-Japanese (gotalab)** |
| **Methodology granularity** | Whole methodology (9-article constitution) | Per-tool format translation | Feature-level shape | **Multi-platform Skills harness with Kiro lineage** |
| **Multi-platform** | None | 30+ tools | None | **8 agents (2 stable / 5 beta / 1 experimental)** |
| **Workflow steps** | 3 (specify/plan/tasks) | varies per tool | feature-level | **6 (discovery → spec init → req → design → tasks → impl)** |
| **Approval gates** | constitution-gates | varies | implicit | **3 explicit human-approval gates** |
| **Skills format** | command-based | per-tool format | command-based | **Skills mode primary (v3.0)** |
| **Adversarial review** | absent | absent | absent | **Reviewer subagent + auto-debug** |
| **Vibe-coding stance** | Anti-vibe pure (9-article constitution explicit) | Anti-vibe (per-tool) | Anti-vibe-light | **Anti-vibe-with-pragmatic-acknowledgment** |
| **Marketplace** | 80+ ecosystem | None | None | None |
| **Stars** | ~unknown spec-kit | ~45.8K | varies | **3.3K** |

**Key differentiator:** cc-sdd combines:
1. Multi-platform Skills format translation (like OpenSpec but at 8 vs 30+)
2. Adversarial subagent review architecture (corpus-first at framework level)
3. Anti-vibe-with-pragmatic-acknowledgment positioning (counter-evidence to spec-kit v17 pure anti-vibe)
4. Solo-Japanese authorship with ecosystem-portfolio (4 pinned products in Claude Code / Agent Skills space)

## 7. Origin / lineage

- Methodology lineage: **Kiro IDE → multi-agent harness** (`.kiro/` directory convention; `kiro-*` skill naming; v3.0.2 CHANGELOG removed Amazon book reference suggesting potential original Kiro IDE methodology citation)
- Author lineage: gotalab solo-Japanese with ecosystem portfolio (cc-sdd + skillport + uxaudit + claude-code-marimo all in Claude Code / Agent Skills space)
- No academic-paper lineage cited
- No corpus-subject direct citation (does not cite spec-kit / OpenSpec / GSD by name)
- Ralph Loop dependency removed at v3.0.0 — Ralph Loop is unverified external project (community-tool? research artifact?). Worth investigating for potential Pattern #27 community-viral corpus-historical-foundational reference.

## 8. Adoption signals

- 3.3K stars / 241 forks / 16 open issues / 429 commits — small-to-medium adoption, healthy issue rate
- 13-language i18n (Greek added v2.0.5) — international adoption
- v3.0.0 architectural shift in April 2026 (recent) — may indicate growing momentum
- Ecosystem-portfolio author (gotalab) suggests committed maintenance + roadmap
- "v3.0 introduces autonomous Skills mode" matches industry trend toward agent-native workflows

## 9. Limitations / failure modes

- **No marketplace** — extension model is per-team customization of templates, not third-party plugin ecosystem (vs spec-kit v17 80+ marketplace)
- **No persona library** — does not provide pre-built persona definitions (vs BMAD v11)
- **Single-author scaling risk** — gotalab solo-author; bus factor concerns for production-critical adoption
- **Skills mode primary may exclude command-only workflows** — v3.0.0 deprecated command-based installs (still available but not primary)
- **5-of-8 platforms in beta** — production-stable only on Claude Code + Codex
- **Auto-approval flag (`-y`) skips human review** — operator footgun if used carelessly
- **`/kiro-impl` autonomous mode == long-running** — may consume significant agent time/tokens; cost discipline required

## 10. Storm Bear vault applicability

**Pilot relevance ranking: HIGH (top-tier).**

Why:
- Direct deployable for Storm Bear vault Claude Code workflows via `npx cc-sdd@latest --claude-skills`
- SDD methodology with explicit human-approval gates fits vault Scrum-coaching software-build patterns
- Boundary-first design with File Structure Plan ports well to solo-vault-author scenarios IF specs sized appropriately
- Anti-vibe-with-pragmatic-acknowledgment fits vault philosophy (LLM Wiki routine v2.1 itself respects when ad-hoc work is more efficient)
- 13-language coverage including Japanese suggests potential VN i18n contribution opportunity

Caveats:
- 6-step workflow may be over-engineered for solo-vault scenarios
- "/kiro-discovery legitimately concludes no spec needed" in many vault tasks
- Storm Bear vault projects often single-feature → may not exercise multi-spec batch capabilities

**Recommended pilot scope:**
1. Install `npx cc-sdd@latest --claude-skills` in 1 vault project (small-feature scenario)
2. Run /kiro-discovery + /kiro-spec-init for a single feature
3. Measure: (a) discipline-overhead, (b) value-add over ad-hoc Claude Code, (c) anti-vibe-pragmatism in practice
4. Compare against free-claude-code v60 pilot (also HIGH-OPERATIONAL ranking)

## 11. Open questions

See `01 Analysis/(C) open questions.md` — 20 questions covering project / author / Pattern Library / vault.

Highlights:
- Q3: What was Ralph Loop providing that v3.0 deprecated?
- Q11: Pattern #21 un-stale criterion interpretation (cross-tier vs cross-archetype)
- Q15: Is cc-sdd a viable pilot replacement for ad-hoc Claude Code workflows?
- Q18: Should "un-stale candidates that fail lineage-test re-evaluate on independence-test" be codified routine improvement?

## 12. Cross-references

**Direct SDD methodology peers:**
- [spec-kit v17](../../spec-kit%20-%20Beginner%20Analysis/) — Microsoft official, 9-article constitution, 80+ marketplace
- [OpenSpec v58](../../OpenSpec%20-%20Beginner%20Analysis/) — Fission-AI pseudonymous-org, 30+ tools per-tool format translation
- [get-shit-done (GSD) v5](../../get-shit-done%20-%20Beginner%20Analysis/) — feature-shaped SDD predecessor
- [gsd-2 v54](../../gsd-2%20-%20Beginner%20Analysis/) — GSD v5 successor (same lineage)

**Multi-platform deployment peers:**
- [free-claude-code v60](../../free-claude-code%20-%20Beginner%20Analysis/) — T4 6-provider API protocol translation
- [n8n v56](../../n8n%20-%20Beginner%20Analysis/) — 16-LLM platform routing

**Agent Skills ecosystem peers:**
- [mattpocock-skills v57](../../mattpocock-skills%20-%20Beginner%20Analysis/) — Agent Skills builder for Claude Code
- [awesome-claude-skills](../../awesome-claude-skills%20-%20Beginner%20Analysis/)
- [agent-skills-of-vercel](../../agent-skills-of-vercel%20-%20Beginner%20Analysis/)

**Solo-regional T1 archetype peers:**
- [codymaster v12](../../codymaster%20-%20Beginner%20Analysis/) — solo-VN
- [TrendRadar v19](../../TrendRadar%20-%20Beginner%20Analysis/) — solo-CN multi-tier
- [oh-my-claudecode v27](../../oh-my-claudecode%20-%20Beginner%20Analysis/) — solo-Korean

**Pattern Library entries referenced:**
- Pattern #21 SDD Methodology Emergence (UN-STALE candidate at v61)
- Pattern #18 protocol-translation (Layer 2 sub-archetype candidate: agent-platform-format-translation-installer)
- Pattern #51 Vibe-Coding spectrum (NUANCE / counter-evidence-driven refinement)
- Pattern #55 solo-regional T1 archetype (Japan added)
- Pattern #19 first-mover-authority-without-lineage (gotalab ecosystem-portfolio strengthens)
- Pattern #22c AGENTS.md ↔ CLAUDE.md duplication (cc-sdd has duplication, no explicit-sync-comment-header)

## 13. Next action

For Storm Bear vault: install `npx cc-sdd@latest --claude-skills` in a sandbox vault-project to evaluate pilot fit (HIGH-OPERATIONAL ranking; ~1h setup + 1-week measurement).

For Pattern Library: register Pattern #21 un-stale candidate at next mini-audit with promotion-recommendation under criterion #2 structural-unambiguity-at-N=2 (or criterion #5 meta-pattern-at-N=3-consolidation).

For corpus: monitor for next SDD-centered framework (v62-v65 window) — if T2-T5 SDD framework appears, Pattern #21 satisfies criterion #1 default ≥3-cross-tier and promotes unambiguously.
