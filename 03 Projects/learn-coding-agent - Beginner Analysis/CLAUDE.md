# Project: learn-coding-agent — Beginner Analysis

> **Subject:** `sanbuphy/learn-coding-agent` ("Claude Code Architecture Study")
> **Build session:** 53 (v53 LLM wiki)
> **Date:** 2026-04-26
> **Routine:** v2.1 (10th v2.1-era execution)
> **Storm Bear Wiki #:** 53rd

---

## Phase 0 — 12-axis classification

| Axis | Value |
|------|-------|
| **Tier** | **OUTSIDE-SCOPE — single-tool-internals-reverse-engineering-archive** (sub-variant of Pattern #38 prompt-leak-archive genre; sister-archive to system-prompts-leaks v21) |
| **Archetype** | Solo-Chinese-author + research-archive + abandoned-since-day-2 (zero commits since 2026-04-01) + zero-governance + research-only-non-commercial-restriction-without-formal-license |
| **Scale tier** | Medium (11.7K stars in 25 days = ~470 stars/day fast cold-start; **CORPUS-RECORD 168.2% fork-to-star inversion**: 19,741 forks > 11,735 stars by 68%; mechanism unclear — possibly CN-class-assignment-fork OR mass-fork-bot OR fork-as-bookmark CN-GitHub-culture) |
| **Primary lang** | **null** (markdown-only; zero code; 4 READMEs + 20 docs across en/ja/ko/zh) |
| **Packaging** | None (clone + read; no install surface) |
| **Origin story** | Solo Chinese researcher (Sanbu / sanbuphy / 散步 = "stroll") compiled from publicly-available online references and community discussions on Claude Code v2.1.88; 25 days old; **abandoned 24 days ago** (last push 2026-04-01) |
| **Methodology** | Reverse-engineering archive; no methodology-as-product |
| **Governance** | **MINIMUM (4 READMEs only)** — NO LICENSE / NO CONTRIBUTING / NO AGENTS.md / NO CLAUDE.md / NO SECURITY / NO CHANGELOG / NO `.github/`. Only governance: README §"Copyright & Disclaimer" with "Commercial use is strictly prohibited" + DMCA-style removal-on-request. **Informal research-only-non-commercial-restriction without formal license name** (NOT Apache/MIT/AGPL/SUL/PolyForm) |
| **Agent/skill count** | N/A — not agent framework. ~24 primitives total: 4 READMEs + 20 deep-analysis reports (5 reports × 4 languages) |
| **i18n** | **Quadrilingual EN+CN+JA+KO** at root README + all 5 deep-dive reports translated; CN-author so CN treated as authoritative; corpus-strong i18n at outside-scope (ties OMC v27 7-lang / fish-speech v20 7-lang / oh-my-openagent v52 5-lang at outside-scope) |
| **Intellectual influence** | **Archetype 4 no-explicit-individual-lineage** — README explicit: *"All materials are compiled entirely from publicly available online references and discussions"* (community-amalgam citation; consistent with archive-genre norms; same as system-prompts-leaks v21) |
| **Agent platforms** | N/A (not agent-targeted; subject IS Claude Code = Anthropic-runtime; this archive STUDIES Claude Code internals) |

---

## Phase 0.5 — Pattern pre-check (v2.1 mandatory)

**Default: consolidation-forward. Target: extend 16-consecutive-wiki zero-new-active-candidates streak to 17 (v37-v53).**

### Overlap pre-check (each candidate observation routed)

| # | Observation | Existing pattern? | Decision |
|---|-------------|-------------------|----------|
| 1 | Single-tool-internals-reverse-engineering-archive (Claude Code internals) | **Pattern #38 prompt-leak-archive genre** (CANDIDATE since v21 N=1) | **Strengthen #38 with NEW sub-variant 38b single-tool-internals-deep-dive** (joins 38a multi-tool-prompt-archive system-prompts-leaks v21); structural-N=2 promotion-candidate at next mini-audit. **DO NOT register standalone outside-scope sub-type.** |
| 2 | 168.2% fork-to-star inversion CORPUS-RECORD | **Pattern #75 Template-Use Fork-Star Anomaly OBSERVATION-TRACK** (NEW v37 bizos N=1 138% inversion) | **Strengthen #75 to N=2 — but mechanism caveat**: bizos = template-use; sanbuphy = mechanism-unclear (possibly different mechanism — CN-class-fork / mass-fork-bot / fork-as-bookmark CN-culture). Register as N=2 OBSERVATION-TRACK strengthening with explicit mechanism-divergence flag for mini-audit overlap-pre-check. **DO NOT auto-promote without operator overlap-resolution.** |
| 3 | Absent-LICENSE + research-only-non-commercial-restriction-without-formal-license + Copyright-disclaimer | **Pattern #29 absent-LICENSE 4 sub-contexts** (29-absent-1 commercial-cold-start bizos / 29-absent-2 academic-public-welfare dive-into-llms / 29-absent-3 README-OSI-claim awesome-claude-skills+vercel-labs / **NEW 29-absent-4**) | **Strengthen #29 with NEW 29-absent-4 sub-context** (research-only-non-commercial-restriction-without-LICENSE-file + Copyright-disclaimer). Sub-context formalization-candidate at next mini-audit. |
| 4 | Quadrilingual EN+CN+JA+KO at outside-scope | Pattern #29 license diversity orthogonal; i18n observational | Strengthen-only — no pattern action |
| 5 | Adversarial-Anthropic-positioning (telemetry-no-opt-out + undercover-mode + remote-killswitches disclosure) | v52 omo competitive-anti-lock-in framing N=1 observational; mechanism DIFFERS (omo = competitive-positioning; v53 = reverse-engineering-disclosure) | **Document N=2 observational; DO NOT register standalone candidate** (mechanisms differ; consolidation-forward) |
| 6 | CN-author at outside-scope | TrendRadar v19 + this v53 = N=2 CN-authors at outside-scope; cross-tier CN observational across corpus (dive-into-llms v39 academic / MiroFish v49 commercial / TrendRadar v19 outside-scope / this v53 outside-scope) | Cross-tier CN observational; insufficient mechanism distinction for new candidate. Strengthen-only. |
| 7 | Pattern #19 archetype 4 no-explicit-individual-lineage at outside-scope | Pattern #19 confirmed; archetype 4 strengthening | Strengthen-only |
| 8 | Pattern #22 AGENTS.md absence at archive-genre minimum-governance | Pattern #22 confirmed; absence-baseline observation | Strengthen-only (archive-genre minimum-governance baseline reinforced) |
| 9 | Pattern #12 Governance-Depth refined-formulation 8th counter-evidence-or-baseline-fits wiki | Pattern #12 v42 refined formulation (3-factor: maintainer-philosophy + maturity-ambition + scale-tier) — solo-Chinese + abandoned + minimum-governance + small-scale = baseline-fits not counter-evidence | Strengthen-only — supports refined formulation |
| 10 | Pattern #27 Community-Viral 22nd observation (~470 stars/day fast cold-start) but anomalous fork-amplified-not-star | Pattern #27 confirmed; cold-start sub-path observation | Strengthen with note: counter-evidence-narrowing observation (community-viral via fork-amplification distinct from star-amplification) |
| 11 | Pattern #57 Recursive Corpus Reference | Subject (Claude Code) is implicitly substrate of MANY corpus T1 wikis (spec-kit/aidevops/claude-howto/OMC/oh-my-openagent/etc.) but learn-coding-agent docs do NOT cite specific Storm Bear wikis | NOT 57a (no direct citation); NOT 57b (no compound 2-wiki cross-corpus); NOT 57c (no forward citation). **No Pattern #57 hit.** Subject-of-subject reverse-engineering is structurally distinct meta-pattern; insufficient evidence. |
| 12 | Pattern #18 Agent Runtime — Claude Code as subject of internals-research | Pattern #18 confirmed; Claude Code is well-established Layer 2/3 runtime per #18 v36 + v52 refinements | Strengthen-only — no formal action (subject-of-research observation orthogonal to runtime-standardization pattern) |

### Decisions summary

- **0 new active candidates** (extends zero-registration streak to **17 CONSECUTIVE WIKIS v37-v53 — NEW LONGEST in corpus history**)
- **0 new top-level OBSERVATION-TRACKs** (Pattern #75 strengthened in-place; no new OT registration)
- **3 sub-variant / sub-context strengthenings within existing patterns:**
  - Pattern #38 NEW sub-variant 38b single-tool-internals-deep-dive (structural-N=2 promotion-candidate)
  - Pattern #29 NEW sub-context 29-absent-4 research-only-non-commercial-restriction (sub-context formalization-candidate)
  - Pattern #75 strengthening to N=2 with mechanism-divergence caveat (mini-audit decides promotion vs OT-stay)
- **8+ patterns strengthened without status change** (#19 / #22 / #12 / #27 / #18 / #57 negative-confirmation / cross-tier CN observation / archive-genre i18n)
- **Adversarial-Anthropic-positioning** observation N=2 (omo v52 + v53) documented but NOT registered (mechanisms differ; consolidation-forward)
- **Un-stale checks:** All 3 stale candidates (#45 dual-licensing / #52 extreme-viral-velocity / 3rd) — NEGATIVE. Disciplined.

### Promotion candidates accumulated post-v53 (cumulative across v45-v53)

Adds to v52's 14 carry-forward: **17+ promotion candidates** at next mini-audit:
- v53 NEW: #38 38b structural-N=2 + #29 29-absent-4 sub-context + #75 N=2 mechanism-divergence-flagged
- v52 carry: #57 57c structural-N=2 + #18 OpenCode-primary structural-N=2 + #29 SUL-1.0 sub-context + #58 58c sub-variant + #50 50d sub-variant
- v51 carry: #22 22d identical-mirror + #57 57c + #29 29-absent-3 + #29 AGPL-at-project-scope + #50 50b + #66 OT sub-categorization + #18 4-layer + #22 22c scope-narrowing + #47 retirement (carry-forward)

**Mini-audit warranted at next operator-trigger** (~30-60 min for ~17 candidates).

---

## Phase 0.9 — Primitive-count flagging (v2.1 informal discipline)

**Outcome: GREEN** (well-bounded; ~24 primitives across 2 categories: 4 READMEs + 20 deep-dive reports = 5 topics × 4 languages)

- 4-entity allocation comfortably preserves standard format
- No lossy compression needed
- Velocity: targeting ~2h plateau preserved
- 5th GREEN-track post-v44 session (v44 magika + v50 awesome-claude-skills + v51 vercel-labs + v52 omo EXTREME exception + v53 GREEN return)

---

## Phase 4b mode

**Mode:** OUTSIDE-SCOPE STRENGTHENING + Pattern #38 sister-archive comparison (v21 prompt-leak-archive parent + v53 single-tool-internals-deep-dive sub-variant)

**Phase 4b deliverable focus:** Pattern #38 38b sub-variant promotion-candidate analysis + Pattern #75 N=2 mechanism-divergence + Pattern #29 4th sub-context + 5-doc deep analysis content summary + adversarial-Anthropic-positioning N=2 observational + sister-archive comparison with system-prompts-leaks v21 + Storm Bear operational caveats summary (telemetry / undercover / killswitches Storm Bear should know about Claude Code daily-use).

---

## Storm Bear meta-entity per-wiki applicability check (v2.1 Phase 0.9)

**APPLICABLE — 42nd consecutive Storm Bear meta-entity (v10-v53).**

Justification:
- Storm Bear vault uses Claude Code as primary harness
- Telemetry (no UI-exposed opt-out for 1P), undercover-mode, remote-killswitches, GrowthBook flags → **direct operational caveats** Storm Bear operator should know
- Sister-archive to v21 system-prompts-leaks (which had Storm Bear meta-entity at outside-scope tier)
- Frame: "Claude Code internals operational awareness for Storm Bear daily-use" — NOT pilot-candidate (research-only license blocks commercial Scrum coaching re-use)

---

## Caveats / fact-verification

- **All claims about Claude Code internals are per Sanbu's analysis based on publicly-available sources**; not Anthropic-confirmed. Beginner guide MUST flag this verbatim.
- **Studied Claude Code version: v2.1.88** (current Claude Code may have changed in 25+ days since archive frozen)
- **Repo abandoned 2026-04-01** — no follow-up analysis; specific version-bound claims may be stale
- **License**: research-only-non-commercial-restriction blocks commercial re-use of THIS archive's content; Storm Bear can READ but not REPACKAGE for client work
- **168.2% fork-to-star anomaly mechanism unclear** — flag for mini-audit; do NOT auto-promote Pattern #75 without overlap-resolution

---

## Build state

- Phase 0: ✅
- Phase 0.5: ✅ (this doc)
- Phase 0.9: ✅ GREEN
- Phase 1-3: source already cloned + 5 EN docs read in full
- Phase 4: 13 deliverables to build
- Phase 5: PATTERN_LIBRARY.md update mandatory
- Phase 6: vault-root sync mandatory (CLAUDE.md state block + project entry + GOALS.md session 63)
