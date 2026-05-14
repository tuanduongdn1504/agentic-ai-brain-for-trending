# (C) v66 agentmemory — iteration log

> **Subject:** [`rohitg00/agentmemory`](https://github.com/rohitg00/agentmemory)
> **Wiki version:** v66 — built 2026-05-14, Storm Bear vault
> **Routine:** `llm-wiki-routine-v2.2` — **FIRST wiki built under v2.2** (v2.2 codified 2026-05-14; v66 EARLY-OPERATOR-ELECTED mini-audit was v2.2's first audit; this is v2.2's first wiki)

---

## 1. Phase-by-phase log

| Phase | Status | Notes |
|---|---|---|
| Phase 0 — probe | ✅ COMPLETE | 13-axis classification (v2.2). Multiple WebFetches (repo / README / package.json / repo tree / releases / AGENTS.md / CHANGELOG / ROADMAP / DESIGN.md). DESIGN.md anomaly caught + verified (Surprise #1). gh CLI absent + GitHub API rate-limited → repo age via CHANGELOG first-release-date proxy. |
| Phase 1 — scaffold | ✅ COMPLETE | CLAUDE.md (full probe summary) + 02 Wiki/index.md. Matched v65 project structure (4 dirs: 01 Analysis / 02 Wiki / 03 Published / 04 Reviews). |
| Phase 2 — sources | ✅ COMPLETE | 3 cluster summaries: Cluster 1 (README + positioning) / Cluster 2 (contributor docs + governance — holds Findings #1-#6) / Cluster 3 (iii-foundation + distribution — feeds PRIMARY). |
| Phase 3 — entities | ✅ COMPLETE | 4 entity pages: Entity 1 (core) / Entity 2 (Platform-Primitive Foundation — PRIMARY) / Entity 3 (distribution + quality-maturity tension) / Entity 4 (Storm Bear meta — Phase 0.9 4/4 STRICT PASS). |
| Phase 4a — beginner guide | ✅ COMPLETE | Bilingual VN/EN, 10 sections, ~400 lines. Ethical/safety framing included (memory-tool-ingests-everything + recent RCE + privacy-filter-trust). |
| Phase 4b — PRIMARY deliverable | ✅ COMPLETE | `(C) Pattern Platform-Primitive Foundation N=1 registration proposal.md` — NEW candidate registration proposal, Pattern #85, 12 sections per v2.2 proposal-document discipline. |
| Phase 5 — iteration log + Pattern Library | ✅ in progress (this file) | + `_patterns/03-active-candidates.md` + `_patterns/05-recent-additions.md` updates. |
| Phase 6 — vault sync | pending | Root CLAUDE.md + PATTERN_LIBRARY.md state-block updates. |

## 2. Key decisions made

1. **Wiki numbered v66.** v66 EARLY-OPERATOR-ELECTED mini-audit happened post-v65; this is the v66 *wiki*. Audits and wikis share numbering per corpus precedent (v50 / v53 / v63 all had both a wiki and an audit at the same number). v66 audit + v66 wiki is consistent.
2. **Routine v2.2 used** (not v2.1 as v65 used). v2.2 was codified 2026-05-14; this is its first wiki. 13-axis classification applied (Living-Domain-Standards axis = NO).
3. **Tier = T2 Service.** Long-lived server process delivering memory-as-a-service. T4-bridge-adjacent (cross-agent reach) but bridging is a consequence, not the core function. T1 rejected (the Claude Code plugin is a thin client over a backend, not the substance).
4. **Phase 4b PRIMARY = NEW candidate registration (Platform-Primitive Foundation).** Chosen over Pattern #83 Honest-Deficiency-Disclosure N=3 (rejected as PRIMARY because agentmemory's evidence is MIXED — README over-claims while CHANGELOG/ROADMAP are honest) and over Pattern #18 strengthening (already-confirmed, heavily-refined). The iii-foundation observation is corpus-first and clean.
5. **Storm Bear meta-entity INCLUDED — Phase 0.9 4/4 STRICT PASS.** Widest criteria-coverage in the post-amendment window. Categorized STRONG INCLUDE (not STRONGEST — criterion (d) is structural-sibling depth, not "documents THE most-cited product's internals" depth).
6. **AI-Generated-Repo Artifact Contamination registered as OBSERVATIONAL candidate, not formal top-level.** N=1, consolidation-forward discipline — register-and-wait. Bundled with viral-velocity-outpacing-quality-maturity observation.
7. **Pattern #83 evidence logged as MIXED partial / counter-nuance, NOT a clean N=3 strengthening.** Honest disclosure: the README over-claim breaks the clean-disclosure story.
8. **DESIGN.md excluded as a source.** Verified-contaminated (Lamborghini boilerplate); used only as a *finding*, never as agentmemory architecture data.

## 3. Surprises + corrections

- **Surprise #1 — DESIGN.md is contaminated.** The single biggest surprise. `DESIGN.md` contains 288 lines of an unrelated "Lamborghini design system." Caught when the first WebFetch returned obviously-wrong content; *not* dismissed as a fetch bug — verified with a 2nd WebFetch (blob URL) and a raw `curl` of the bytes. All three agreed. This became Finding #1 and the seed of the NEW observational candidate. **Correction discipline applied:** flagged to the operator immediately, excluded from sources, did not fabricate architecture content to fill the gap (Storm Bear rule: NEVER fabricate).
- **Surprise #2 — the repo is only ~35 days old.** CHANGELOG's first entry `[0.8.0] 2026-04-09` revealed the repo is ~35 days old at 7,900 stars = ~226 stars/day. Reframed the whole wiki around the viral-velocity-outpacing-quality-maturity angle.
- **Surprise #3 — README over-claims vs ROADMAP.** "Memories shared across all agents" (README, present tense) vs "cross-agent memory sharing" (ROADMAP, Q3 2026 candidate). Caught by reading both clusters side-by-side. Became Finding #2.
- **Correction — tooling limits.** `gh` CLI is not installed; GitHub API curl was rate-limited; a `python3 -c` parse was permission-denied. Worked around all three; repo age via CHANGELOG proxy. Honest disclosure carried into CLAUDE.md ("exact creation date not retrievable").
- **No fabrication events.** Where data was missing (exact repo creation date, DESIGN.md content), the gap was disclosed, not filled.

## 4. Pattern Library implications snapshot

| Item | Type | Disposition |
|---|---|---|
| **Pattern #85 Platform-Primitive Foundation** | NEW top-level candidate | REGISTER — N=1, stale-flagged (v68/v71 stale-check). PRIMARY deliverable. Proposal: `(C) Pattern Platform-Primitive Foundation N=1 registration proposal.md` |
| **Pattern #18 shared-backend-service** | NEW sub-archetype within CONFIRMED #18 | REGISTER as sub-archetype — 3rd multi-platform mechanism (Layer 1 coexistence / Layer 2 translation / shared-backend-service). N=1 stale-flagged. Does NOT add to candidate count (within-pattern). |
| **AI-Generated-Repo Artifact Contamination** | NEW observational candidate | REGISTER as observational (not formal top-level) — N=1, consolidation-forward. Bundled with viral-velocity-outpacing-quality-maturity. v68/v69 stale-check. |
| **Pattern #8 Research-Benchmark Integration** | Strengthening (CONFIRMED) | First memory-retrieval-domain benchmark in corpus (LongMemEval-S ICLR 2025). Within-pattern strengthening. |
| **Pattern #28 Multi-Provider AI Support** | Strengthening (CONFIRMED) | STRONG dual-axis instance (LLM + embeddings independently multi-provider). Within-pattern strengthening. |
| **Pattern #12 Governance-Depth** | Counter-evidence nuance | 11 governance files but DESIGN.md contaminated + AGENTS.md skewed → file-count proxy is gameable. Counter-evidence note. |
| **Pattern #81 Manifest-Drift-As-CI-Concern** | Strengthening (CANDIDATE) | "Names-the-drift-and-drifts-anyway" — AGENTS.md codifies the multi-file-sync surface then itself drifts. Within-candidate observation. |
| **Pattern #83 Honest-Deficiency-Disclosure** | MIXED partial evidence | NOT a clean N=3 strengthening — README over-claims while CHANGELOG/ROADMAP are honest. Logged as counter-nuance. |
| **Pattern #52 EXTREME-VIRAL-VELOCITY** | OBSERVATIONAL watch | ~226 stars/day below the 300/day flag, but quality-maturity-lag profile fits. v69 sustained-velocity re-check flag. |
| **Pattern #19 Intellectual Lineage** | Strengthening (CONFIRMED) | Research-paper-chain archetype (Ebbinghaus + sleep consolidation). Within-pattern. |
| **Pattern #57 Recursive Corpus Reference** | Strengthening (CONFIRMED) | Competitive table names the vault's own "Built-in CLAUDE.md" method; graph-stream sibling to graphify. Within-pattern. |
| **Pattern #66 Supply Chain Awareness** | OT extension | privacy-by-design + v0.8.2 as visible learning event. Observation-track note. |

**State change:** confirmed 43 (unchanged) / active candidates **26 → 27** (+1 Pattern #85) / ratio **0.605 → 0.628:1** (27:43; buffer 0.322 below 0.95:1 mini-trigger — still healthy). ZERO-NEW-ACTIVE-CANDIDATES streak remains BROKEN (was already broken at v66 audit).

## 5. v67/v68 audit agenda accumulated

- **v68 stale-check — Pattern #85 Platform-Primitive Foundation** — check v67-v68 subjects for all-4-criteria match; un-stale to N=2 if found; re-check coupling-risk diagnostic
- **v68 stale-check — Pattern #18 shared-backend-service sub-archetype** — check for 2nd shared-backend multi-platform subject
- **v68/v69 stale-check — AI-Generated-Repo Artifact Contamination observational** — check for 2nd provably-contaminated governance file; consider formal registration if N=2
- **v69 — Pattern #52 sustained-velocity re-check for agentmemory** — is ~226 stars/day sustained, accelerating past 300/day, or decaying? (joins the v69 Pattern #52 sustained-velocity batch with mattpocock + codex-plugin-cc + karpathy-skills)
- **Carry-forward (unchanged from v66 audit):** v67 (Pattern #77 + #78 78a/78b) / v68 (Pattern #74 + #75 + #76 v63 carry + #79 + #80 + #83 + #84) / v69 (Pattern #81 + #82 + Tier-Taxonomy T6)
- **Note for next audit:** v66 wiki added +1 candidate (#85) — active count now 27, runway to the ≥30 mini-audit trigger narrowed to 3.

## 6. Cross-wiki sibling decisions

- **graphify** — DIRECT sibling confirmed: agentmemory's knowledge-graph search stream is the same primitive family graphify is built around. Cross-referenced in index + Entity 1 + Entity 4.
- **claude-code-system-prompts v65** — sibling via Claude Code integration (agentmemory ships `.claude-plugin/` + 12 CC hooks; v65 documents CC internals).
- **codex-plugin-cc v62** — sibling via `.codex-plugin/` packaging (both ship a Codex CLI plugin directory).
- **free-claude-code v60** — T2-adjacent infrastructure sibling.
- **n8n v56** — T2 service sibling (workflow automation).
- **cc-sdd v61** — multi-platform sibling (contrast: cc-sdd uses install-time translation, agentmemory uses shared-backend).
- **mem0 / Letta / MemGPT** — NOT corpus subjects; named as agentmemory's competitors but cannot be cross-referenced. agentmemory is the first memory-system wiki.

## 7. Files written at v66

```
03 Projects/agentmemory - Beginner Analysis/
├── CLAUDE.md                                              (Phase 0 probe summary)
├── 01 Analysis/
│   ├── (C) Pattern Platform-Primitive Foundation N=1 registration proposal.md   (Phase 4b PRIMARY)
│   └── (C) iteration-log.md                               (this file)
├── 02 Wiki/
│   ├── index.md
│   ├── cluster-1-readme-and-positioning.md
│   ├── cluster-2-contributor-docs-and-governance.md
│   ├── cluster-3-iii-foundation-and-distribution.md
│   ├── entity-1-agentmemory-core.md
│   ├── entity-2-platform-primitive-foundation.md          (PRIMARY entity)
│   ├── entity-3-distribution-and-quality-tension.md
│   └── entity-4-storm-bear-meta.md
└── 03 Published/
    └── (C) agentmemory - Huong dan cho nguoi moi.md       (bilingual beginner guide)
```

11 files. Plus Phase 5/6 vault-state updates: `_patterns/03-active-candidates.md`, `_patterns/05-recent-additions.md`, root `CLAUDE.md`, `PATTERN_LIBRARY.md`.

## 8. Velocity comment

Direct-write build mode throughout — no agent-thrash (v56 lesson held; the subject's primitive count is high but the source docs are well-structured). Phase 0 was source-heavy (9 WebFetches + curls) because of the DESIGN.md anomaly investigation and the rate-limited API workarounds — appropriate spend, the anomaly became a Finding. Phases 1-5 direct-write. Estimated ~110-130 min main-loop equivalent — mid-range, consistent with a Pattern-Library-contributing wiki (a NEW candidate registration + a NEW sub-archetype + a NEW observational candidate is substantive Phase 4b/5 work).

## 9. What's notable about v66 — corpus-firsts + corpus-records

**Corpus-firsts:**
1. **First dedicated agent-memory-system** in the 65-wiki corpus (prior memory-adjacent: graphify knowledge-graph, claude-code-system-prompts CC memory-fragments — neither is a memory *system*)
2. **First Platform-Primitive Foundation observation** — built entirely on another platform's primitives, self-as-instance framing (NEW Pattern #85)
3. **First memory-retrieval-domain benchmark** in corpus (LongMemEval-S ICLR 2025) — extends Pattern #8's benchmark-domain coverage
4. **First Pattern #18 shared-backend-service mechanism** — 3rd multi-platform mechanism after coexistence + translation
5. **First provably-contaminated governance file** in corpus (DESIGN.md Lamborghini boilerplate) — seeds the AI-Generated-Repo Artifact Contamination observational candidate
6. **First wiki built under routine v2.2** (v2.2 codified 2026-05-14; v66 audit was v2.2's first audit, v66 wiki is v2.2's first wiki)
7. **First Phase 0.9 4/4 STRICT PASS** in the post-amendment window (v65 was the prior max at 3/4)

**Corpus-records:**
- **Youngest high-velocity subject relative to star count** observed at probe — ~35 days / 7,900 stars / ~226 stars/day. (Not the highest absolute velocity — that remains karpathy-skills v63 at ~1,186/day — but the youngest-repo + high-velocity + quality-maturity-lag *combination* is corpus-distinctive.)
- **Lowest watcher/stars ratio noted as a structural signal** — 0.0029 (23/7,900); drive-by-stars-dominant engagement profile made an explicit Finding.

**Storm Bear meta-streak:** v64 SKIP (RESET) → v65 STRONG PASS (1) → **v66 STRONG PASS (2)**. 10-instance window v57-v66 = 8 PASS / 2 SKIP = 80% INCLUDE rate (held).
