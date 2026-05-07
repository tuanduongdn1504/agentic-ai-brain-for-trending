# OpenSpec - Beginner Analysis

> **Project type:** LLM Wiki v58 — Storm Bear corpus 58th wiki
> **Subject:** `Fission-AI/OpenSpec` — "Spec-driven development (SDD) for AI coding assistants"
> **Date:** 2026-05-07 (session 70)
> **Tier:** T1 Assistant (SDD framework targeting 30+ AI coding assistants — extends T1 N count)
> **Build mode:** Main-loop direct-write compressed scope (per v56 + v57 lessons)
> **Storm Bear meta-entity:** ✅ INCLUDE (Phase 0.9 STRICT criteria PASS — 3-of-4; see decision below)

---

## 12-axis classification

| Axis | Value |
|---|---|
| **Tier** | **T1 Assistant** (Spec-Driven Development framework — generates per-tool skill files / slash commands / prompt files for 30+ AI assistants; itself NOT an assistant but assistant-augmenter) |
| **Archetype** | **Pseudonymous-org + small-team** — Fission-AI org "no public members" (members hidden); 2 public repos (OpenSpec + PR-QUEST); tagline "From Idea to Action, Instantly" / package author "OpenSpec Contributors" / no individual founder visible |
| **Scale tier** | **X-Large 45,800 stars** (3,200 forks; 225 watchers; 225 open issues; high-velocity TS/MIT npm-distributed) |
| **Primary lang** | TypeScript 98.9% |
| **Packaging** | `npm install -g @fission-ai/openspec@latest` + `openspec init` CLI scaffolder + per-tool skill/command file generation |
| **Origin story** | Pseudonymous-org methodology-lineage SDD ("Spec-driven development") — explicit positioning vs spec-kit (corpus v17) + AWS Kiro as anti-pattern foils |
| **Methodology** | **SDD (Spec-Driven Development)** — proposal → specs → design → tasks → implementation; 5 explicit principles ("fluid not rigid / iterative not waterfall / easy not complex / brownfield not greenfield / scalable personal-to-enterprise") |
| **Governance** | Medium (AGENTS.md + MAINTAINERS.md + CHANGELOG + LICENSE + README + README_OLD + WORKSPACE_REIMPLEMENTATION_*.md notes + .changeset + flake.nix Nix config + vitest test infra) |
| **Agent/skill count** | **11 generated skills/commands per tool** (`openspec-propose / -explore / -new-change / -continue-change / -apply-change / -ff-change / -sync-specs / -archive-change / -bulk-archive-change / -verify-change / -onboard`) × **30+ supported tools** = ~330+ generated artifacts |
| **i18n** | EN-only README; multi-language support listed in docs TOC |
| **Intellectual influence** | **SDD methodology lineage** (sibling to spec-kit v17 SDD); explicitly cites spec-kit + Kiro as anti-pattern foils; no academic citations / no individual founder lineage (Fission-AI org pseudonymous) |
| **Agent platforms** | **30+ supported tools** (corpus-broadest multi-platform-by-design — surpasses mattpocock v57 ~8, n8n v56 ~16-LLM-providers): Amazon Q Developer / Antigravity / Auggie / IBM Bob Shell / **Claude Code** / Cline / CodeBuddy / Codex / ForgeCode / Continue / CoStrict / Crush / Cursor / Factory Droid / Gemini CLI / GitHub Copilot / iFlow / Junie / Kilo Code / Kimi CLI / **Kiro** / Lingma / OpenCode / Pi / Qoder / Qwen Code / RooCode / Trae / Windsurf |

---

## Phase 0.5 overlap pre-check (10 candidate observations)

All 10 routed to within-pattern strengthening per consolidation-forward discipline; **0 new standalone candidates** anticipated.

1. **Cites spec-kit v17 + Kiro as anti-pattern foils in README** → **Pattern #57 57c forward-citation-then-wiki STRENGTHENING** — adds N=1 (OpenSpec v58 cites spec-kit v17; T1→T1 same methodology lineage; gap 41 wikis); 57c grows from N=7 (post-v57) → **N=8 conservative-attribution**. NEW: also cites Kiro (NOT in corpus — out-of-corpus citation; does NOT advance 57c which requires in-corpus citation, but observational signal of "framework-comparison-positioning" pattern).
2. **2nd corpus SDD-methodology framework at T1** (after spec-kit v17 SDD) → **Pattern #17 / Pattern #19 methodology convergence — 2nd SDD instance at T1 strengthens SDD-as-named-methodology lineage**; both pseudonymous-org-or-corporate (spec-kit = Microsoft GitHub corporate-official; OpenSpec = Fission-AI pseudonymous-org)
3. **30+ AI tools supported = corpus-broadest multi-platform-by-design** → **Pattern #18 Layer 1 universal-protocol consumer STRONGEST evidence to date** (surpasses prior n8n v56 16-LLM-providers + mattpocock v57 ~8 platforms); structural extension of existing pattern, no new candidate
4. **Pseudonymous-org "no public members"** → **Pattern #19 archetype + Pattern #21 system-prompts-leaks-style pseudonymity** observational; recalls v21 system-prompts-leaks pseudonymous author archetype but at org-level not individual-level — **NEW sub-variant candidate org-level-pseudonymity-with-active-commercial-product?** (vs v21 individual-pseudonymity-with-leaked-content). N=1 stale-flagged v63/v68.
5. **MIT license** → Pattern #29 strengthening at standard-OSI sub-context (does NOT advance non-commercial-restriction-custom-license N=4)
6. **npm-package-as-installer + `openspec init` scaffolder** → Pattern #2 distribution-evolution data point (CLI-installer-as-primary surface; sister to mattpocock `npx skills add` pattern)
7. **AGENTS.md present** → Pattern #22 cross-wiki standard validation (AGENTS.md adoption strengthens at N+1 instance)
8. **Anti-vibe positioning** ("vague prompts and unpredictable results" without specs) → **Pattern #51 Vibe-Coding Spectrum anti-vibe pole strengthening** at 2nd-most-explicit position (after mattpocock v57 "real engineering not vibe coding"); both v57 and v58 strengthen anti-vibe pole consecutively
9. **Per-tool skill-file generation = corpus-first explicit "skill-file-as-deployment-target multi-tool"** → **Pattern #18 Layer 0 sub-axis: skill-file-as-universal-deployment-format STRENGTHENING** (after mattpocock v57 plugin-manifest declaration); does NOT promote (single-tier T1)
10. **Posthog-node analytics dependency** → observational supply-chain note (telemetry-by-default in dev tool); flag for COMMANDS.md / safety section in beginner guide (Pattern #66 supply-chain OBSERVATION-TRACK relevance)

**0 NEW STANDALONE CANDIDATES likely** (1 borderline at #4 org-level-pseudonymity stale-flagged). **STREAK PENDING:** if zero new candidates → **22-CONSECUTIVE-WIKI ZERO-NEW-ACTIVE-CANDIDATES** (extending v57 21-streak — NEW LONGEST in corpus history maintained).

## Un-stale check

- **#45 Dual-Licensing** — OpenSpec single MIT; does NOT un-stale. STAY STALE.
- **#52 Extreme-Viral-Velocity** — 45.8K stars / TS-codebase / v1.3.1 mature; needs commit-count probe. Does NOT trivially un-stale at v58. STAY STALE / OBSERVATIONAL.
- **#72 PolyForm-Noncommercial** — MIT not PolyForm. STAY STALE.

3 of 3 un-stale checks NEGATIVE.

## Phase 0.9 STRICT 4-criteria gate (session-66 amendment)

| Criterion | Verdict | Evidence |
|---|---|---|
| (a) Author archetype peer | ❌ FAIL | Fission-AI = pseudonymous-org + hidden-members + 2-repo small-org. Storm Bear = solo-VN-Scrum-coach individual. Org-vs-individual archetype mismatch + transparency mismatch (vault is public + identifiable; OpenSpec org members hidden). |
| (b) Operational tool for Scrum-coaching workflows | ✅ **PASS** | OpenSpec is directly deployable in Storm Bear's daily Claude Code workflows: SDD framework for client-spec-discovery → proposal artifact / Scrum-sprint-planning → tasks artifact / requirements-clarification → specs artifact / technical-design-discussion → design artifact. MIT license = no commercial-use barrier. `openspec init` integrates with existing project. **Concrete vault use cases:** (1) client-discovery-session output as proposal.md → specs/ → tasks; (2) Scrum sprint-planning artifact pipeline; (3) team retrospective decisions captured as design.md. |
| (c) Methodology-influence-node | ✅ **PASS** | OpenSpec embodies **SDD (Spec-Driven Development)** named methodology — same lineage as corpus v17 spec-kit. SDD methodology directly relevant to vault routine v2.1 design discipline (proposal/specs/design/tasks pipeline parallels Pattern Library candidate-registration / refinement / promotion / archive lifecycle). Vault routine v2.1 phase-discipline ↔ OpenSpec phase-artifact discipline structurally analogous. |
| (d) In-corpus reference | ✅ **PASS** | README explicitly cites spec-kit (v17 corpus) as anti-pattern foil ("Thorough but heavyweight. Rigid phase gates"). Pattern #57 57c forward-citation-then-wiki: corpus subject (spec-kit v17) cited by later corpus subject (OpenSpec v58). T1→T1 same-methodology citation; gap 41 wikis. **Observation:** 2 consecutive wikis (v57 + v58) provide 57c forward-citation evidence — 57c is increasingly dominant evidence-stream. |

**DECISION:** Criteria (b) + (c) + (d) **STRONGLY PASS** (3 of 4). **INCLUDE Storm Bear meta-entity legitimately under STRICT amendment.**

**41st consecutive Storm Bear meta-entity** (40 prior including v56 STRICT-1st 2-of-4 + v57 STRICT-2nd 3-of-4 + v58 STRICT-3rd 3-of-4). **3 consecutive STRICT-instances satisfied** validates Phase 0.9 amendment is regularly satisfiable; STRICT-pattern emergent: corpus subjects with named-methodology + in-corpus-citation reliably pass STRICT criteria.

## Counter-evidence audit

- Pattern #57 57c forward-citation-then-wiki: STRENGTHENS strongly (8th conservative-attribution data point post-v58)
- Pattern #18 Layer 1 universal-protocol consumer: STRENGTHENS strongly (30+ tools = corpus-broadest)
- Pattern #51 Vibe-Coding Spectrum anti-vibe pole: STRENGTHENS (2 consecutive wikis at anti-vibe pole)
- Pattern #19 archetype: NEW org-level-pseudonymity sub-variant N=1 observational
- Pattern #29 MIT license: NEUTRAL-BASELINE (standard OSI; no narrowing)

## Velocity + scope notes

- 58th wiki built main-loop direct-write compressed-scope (post-v56 + v57 lessons applied)
- Probe → write velocity ~30-45 min target
- Compressed-scope: 1 cluster summary + 4 entities + 1 beginner guide + 1 Phase 4b deliverable + 1 iteration log

## File index

- `00 INDEX.md` / `00 LOG.md` / `00 OPEN-QUESTIONS.md`
- `01 Sources/(C) Cluster — Combined source summary.md`
- `02 Entities/` — 4 entity pages (Core product / SDD methodology + spec-kit citation / Multi-platform breadth / Storm Bear meta)
- `(C) 03 Beginner Guide.md` — bilingual VN+EN
- `(C) 04 Phase 4b — 2nd SDD framework + Pattern 57 57c N=8 + corpus-broadest multi-platform.md`
- `(C) 05 Iteration log v58.md`

## Pattern Library impact (post-v58)

- **Pattern #57 57c grows N=7 → N=8 conservative-attribution** (OpenSpec v58 cites spec-kit v17; T1→T1; gap 41 wikis). 8 data points cement 57c as one of best-evidenced sub-variants in library.
- **Pattern #18 Layer 1 STRONGEST multi-platform evidence** at 30+ tools (corpus-broadest)
- **Pattern #51 anti-vibe pole strengthening 2 consecutive wikis** (v57 + v58)
- **41st consecutive Storm Bear meta-entity** (3-of-4 STRICT criteria pass — 3rd consecutive STRICT-instance satisfied; pattern emergent: named-methodology + in-corpus-citation reliably triggers STRICT criteria)
- **22-consecutive-wiki ZERO-NEW-ACTIVE-CANDIDATES streak** (NEW LONGEST extends v57 21-streak) — pending verification org-level-pseudonymity at #4 not promoted to standalone candidate
- Pattern Library state post-v58: **39 confirmed + 17 active + 3 stale + 9 retired + 6 OT = 74 full / 56 active. Ratio 17:39 = 0.436:1 PRESERVED 8TH CONSECUTIVE CYCLE** (largest buffer 0.514 below 0.95:1 mini-audit trigger preserved 8 cycles — NEW LARGEST in corpus history maintained 8 cycles)

## v27 diagnostic HIGH bundle status

- Pre-v58: v27 HIGH bundle 100% COMPLETE session 68; vault public-released; routine v2.1 STRICT Phase 0.9 amendment continues
- Post-v58: no new HIGH-bundle blockers; v60 mini-audit natural cadence approaches (2-wiki runway)

## References

- Routine: `05 Skills/llm-wiki-routine-v2.1.md`
- Style reference: `_state/03a-projects-v48-v55.md` (v57 mattpocock-skills entry)
- Sibling SDD framework (anti-pattern foil cited): `03 Projects/spec-kit - Beginner Analysis/` (v17 corpus)
- Sibling skills-collections T1: `03 Projects/awesome-claude-skills - Beginner Analysis/` (v50) + `03 Projects/agent-skills-of-vercel - Beginner Analysis/` (v51) + `03 Projects/mattpocock-skills - Beginner Analysis/` (v57)
- Pattern #57 57c precedents: post-v53 mini-audit promotion (multica v15→vercel-labs v51 + OMC v27→omo v52); strengthened post-v56 mini-audit (Skyvern v24→n8n v56); STRONGEST at v57 (mattpocock cites BMAD+GSD+spec-kit); v58 adds spec-kit citation (T1→T1)
