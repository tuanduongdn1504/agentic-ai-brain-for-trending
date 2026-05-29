# (C) Phase 4b PRIMARY — NEW T1 sub-archetype "Autonomous Plan→Work→Review Operating-Loop Harness (Enforced-Gate)" PROVISIONAL N=1

**Vehicle:** routine v2.3 §3 Phase 4b vehicle #2 (sub-archetype proposal-document).
**Confidence:** HIGH (structural distinction is clean and verifiable).
**Subject:** v107 `Chachamaru127/claude-code-harness`.

## Proposed sub-archetype

> **T1 sub-archetype "Autonomous Plan→Work→Review Operating-Loop Harness (Enforced-Gate)"** — a Claude-Code/multi-harness skill-bundle that implements a *closed, gated operating loop* over agent work (Plan→Work→Review→Release), where the gates are **enforced by code** (compiled guardrail engine + git hooks + CLI gating logic), not merely described in prose, and where unseen data is held as `unknown` rather than invented.

## 5-criterion structural distinction

1. **Closed operating loop** — Plan→Work→Review→Release→Sync as named, sequenced verb-skills (`/harness-plan` / `/harness-work` / `/harness-review` / `/harness-release` / `/harness-sync`), not a grab-bag of independent skills.
2. **Enforced gates** — plan-approval **blocks** work; major review findings **block** release. Enforcement is mechanical (CLI gating + git hooks), not advisory.
3. **Compiled guardrail engine** — Go-native (no Node.js); the loop's invariants are enforced by compiled code + `monitors/` + `.githooks/`, distinguishing it from prose-only frameworks.
4. **Spec-as-source-of-truth with anti-invention** — `spec.md`/`Plans.md` are authoritative; *"data the agent has not seen stays `unknown` instead of being silently invented."*
5. **Evidence-pack release contract** — `/harness-release` packages a "Work All Evidence Pack" of *verified* outputs only; release artifacts are not rebuilt from memory.

## Why distinct from existing T1 instances

| Comparison | Distinction |
|---|---|
| **v71 agents-best-practices** | v71 = *descriptive* reference framework (Markdown-only, 15 reference files, L0–L4 autonomy taxonomy, principles). v107 = *executable, gated* realization — it **enforces** v71's "model proposes, harness disposes" with compiled gates. Description → enforcement. |
| **v61 cc-sdd** | cc-sdd = spec-driven-development scaffolding (Pattern #21). v107 wraps spec-discipline inside a *full enforced loop with review/release gates + guardrail engine*, not just spec generation. |
| **Design-skill cluster (v75/v81/v82/v83/v85/v91/v105)** | Those produce design artifacts. v107 governs the *development process itself*. Orthogonal. |
| **Domain-vertical-skill-collections (v64/v90/v98)** | Those are skill *libraries* for a domain. v107 is a *process-control loop*, not a domain library. |

## Promotion ladder
- **N=1 PROVISIONAL** at v107.
- First-cycle stale-check at next audit (~v110).
- N=2 watch: any future subject implementing an *enforced-gate* agentic operating loop (not a descriptive framework).
- 15-wiki forced-retire (~v122) if N=1-only.

## SECONDARY observations (held at OC layer — NOT registered at ship)

1. **Pattern #83 NEW sub-variant candidate "Unknown-Stays-Unknown anti-invention guardrail at spec-layer"** PROVISIONAL N=1 — honest-deficiency discipline (Pattern #83 family) made *structural*: unseen data stays `unknown`. Strong corpus-resonance with Storm Bear's CLAUDE.md anti-fabrication rules.
2. **Pattern #84 84c Provider-Agnostic-By-Design multi-harness N+1** — Claude Code (supported) + Codex + OpenCode (internal-compatible) + Cursor/Copilot/Codex-app (candidate tiers); explicit supported-vs-candidate **tier gradation** = honest distribution-maturity disclosure.
3. **Japan-LOCATED first-instance** — FIRST Japan-LOCATED subject in v60+ window; Pattern #19 NEW sub-mechanism candidate "Japanese-Located Solo-Dev with Vibe-Coder Identity (@vibecoder_japan)"; (a)-6 Asian-cluster new sub-locale (Vietnam + China-Mainland + Taiwan + **Japan**). *Note Pattern #19 graveyard pressure — register at OC layer only, do not worsen graveyard.*
4. **High-development-cadence-relative-to-star-velocity** Library-vocab N=2 (v89 VibeCodingTracker micro-scale + v107 mid-scale): ~1 release/day + 1,241 commits at modest 2.1K★ / ~12.6 stars/day.
5. **Memory-system adjacency** — `harness-mem` companion → Pattern #85 Platform-Primitive Foundation (v66 + v103); adjacent (companion, not subject).
6. **Pattern #57 57c-product** citation density — 4 corpus-subject harnesses (Claude Code v65 + Codex v62 + OpenCode v67 + Cursor v75/v76).
7. **Bilingual LICENSE** (`LICENSE.md` + `LICENSE.ja.md`) — corpus-notable license-translation artifact.
8. **Pattern #28 Editorial-Build-Validator adjacency** — scorecard.yml + evidence-packs + quality gates (validator-family discipline at process layer).

## Honest non-claims
- **agentskills.io conformance NOT claimed** — verb-skill model *aligns with* the paradigm but no spec-conformance declared; v107 is **NOT** added to the Pattern #57 57k standards-conformance chain.
- **NOT a Pattern #52 instance** — sustained-low ~12.6 stars/day.
- **Release count** — README 173 vs API page-1 30 (pagination); VERSION 4.12.11 cited as ground truth.
