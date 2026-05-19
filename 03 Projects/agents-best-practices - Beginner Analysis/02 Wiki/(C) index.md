# agents-best-practices Wiki — Phase Index

## Wiki Build Status (v71)

| Phase | Status | Completion | Key Deliverables |
|-------|--------|------------|------------------|
| **Phase 0** | ✓ Complete | 2026-05-19 | 13-axis classification, Pattern Library pre-check, Storm Bear meta-entity, corpus-firsts identification |
| **Phase 1** | ✓ Complete | 2026-05-19 | CLAUDE.md, COMMANDS.md, index.md, log.md |
| **Phase 2** | ✓ Complete | 2026-05-19 | open questions.md, iteration-log.md |
| **Phase 3** | ✓ Complete | 2026-05-19 | user-facing cluster summary, contributor-facing cluster summary, technical-distribution cluster summary |
| **Phase 4** | ✓ Complete | 2026-05-19 | entity-1 (core skill), entity-2 (distribution), entity-3 (pattern library), entity-4 (storm bear) |
| **Phase 5** | ✓ Complete | 2026-05-19 | Beginner guide (VN/EN, 400-700 lines) |
| **Phase 4b PRIMARY** | ✓ Complete | 2026-05-19 | Pattern #84 N=3 promotion evaluation + OC-O candidacy assessment |
| **Phase 6** | → Deferred | Separate session | Vault state sync (CLAUDE.md chapter updates, Pattern Library state updates) |

---

## Core Sources

**GitHub repository:** https://github.com/DenisSergeevitch/agents-best-practices

**Content analyzed:**
- README.md (project description, installation, usage)
- SKILL.md (core skill definition + YAML frontmatter)
- 15 reference files:
  - agentic_loop.md
  - 8_principles.md
  - autonomy_levels.md
  - context_architecture.md
  - tool_design.md
  - planning_mode.md
  - security_threats.md
  - implementation_pathway.md
  - draft_commit_pattern.md
  - error_handling.md
  - observability.md
  - prompt_caching.md
  - mcp_integration.md
  - skills_connectors.md
  - guardrails.md

---

## Entities (13-Section Canonical Format)

**Entity 1:** agents-best-practices Core Skill
- **Type:** T1 Assistant Skill
- **File:** `02 Wiki/(C) entity-1-core-skill.md`
- **Coverage:** 8 principles, agentic loop (7 invariants), autonomy levels, tool design framework, planning mode, draft-commit pattern

**Entity 2:** Distribution + Multi-Platform Ecosystem
- **Type:** Deployment & Packaging
- **File:** `02 Wiki/(C) entity-2-distribution-ecosystem.md`
- **Coverage:** Skills CLI, npm install, multi-platform support, 15-reference architecture, progressive skill disclosure, MCP integration

**Entity 3:** Pattern Library Primary Entity
- **Type:** Pattern Analysis
- **File:** `02 Wiki/(C) entity-3-pattern-library.md`
- **Coverage:** Pattern #84 N=3 (primary), Pattern #78 N=3 (secondary), Pattern #83 within-pattern, Pattern #21 within-pattern, NEW OC-O candidate

**Entity 4:** Storm Bear Meta-Entity
- **Type:** Corpus-Recursive
- **File:** `02 Wiki/(C) entity-4-storm-bear.md`
- **Coverage:** MODERATE 2/4 INCLUDE (b+c), operational skill deployment for Claude Code, methodology influence on routine v2.2-v2.3

---

## Cluster Summaries (3 User-Facing Perspectives)

**Cluster 1 — User-Facing (What is it? How do I use it?)**
- **File:** `02 Wiki/(C) user-facing cluster summary.md`
- **Scope:** README content, SKILL.md usage, installation, core concepts for beginners
- **Sections:** ~15 sections covering skill overview, quick-start, 8 principles, agentic loop, autonomy levels, trust model

**Cluster 2 — Contributor-Facing (How is it built? What are the design principles?)**
- **File:** `02 Wiki/(C) contributor-facing cluster summary.md`
- **Scope:** System design philosophy, threat taxonomy, security discipline, guardrails architecture, error handling
- **Sections:** ~15 sections covering design philosophy, trust labels, threat model (15 categories), guardrails, observability, evaluation

**Cluster 3 — Technical/Distribution (How does it deploy? What are the technical components?)**
- **File:** `02 Wiki/(C) technical-distribution cluster summary.md`
- **Scope:** MCP integration, skills CLI, npm packaging, multi-platform support, prompt caching, reference architecture
- **Sections:** ~15 sections covering distribution model, reference library (15 files), MCP integration, prompt caching strategy, reference architecture

---

## Published Artifacts

**Beginner Guide (VN/EN):**
- **File:** `03 Published/(C) agents-best-practices - Huong dan cho nguoi moi.md`
- **Language:** Vietnamese primary, English technical terms
- **Length:** 400-700 lines
- **Structure:** 12-13 part standard beginner guide format
- **Target audience:** Storm Bear + future vault operators exploring agent-skill integration

---

## Analysis & Planning

**Open Questions:**
- **File:** `01 Analysis/(C) open questions.md`
- **Count:** ~25-30 questions
- **Coverage:** Skill design, deployment implications, Pattern Library integration, Storm Bear usage, future roadmap

**Iteration Log:**
- **File:** `01 Analysis/(C) iteration-log.md`
- **Coverage:** Phase-by-phase log, key decisions, surprises, Pattern Library implications, v72 audit agenda, cross-wiki decisions, velocity comment

**Phase 4b PRIMARY:**
- **File:** `01 Analysis/(C) Pattern-84-cross-vendor-ecosystem-tolerance-N3-promotion-evaluation.md`
- **Length:** 200-400 lines
- **Content:** Pattern #84 current status, N=3 evidence evaluation, 84c sub-typology proposal, promotion criteria, verdict, OC-O candidacy brief, audit checklist

---

## Cross-Links (All Entity Pages + Cluster Summaries Include)

**Linked sibling subjects:**
- v66 agentmemory (T2 Service; Pattern #85; sister operational tool)
- v65 claude-code-system-prompts (T1 reference-archive; Pattern #78 N=2, Pattern #84 N=2)
- v64 claude-seo (T1 skill-collection; Pattern #78 N=1)
- v62 codex-plugin-cc (T4 Bridge; Pattern #84 N=1 first evidence)
- v63 andrej-karpathy-skills (T1 single-artifact; high-velocity precedent)
- v61 cc-sdd (T1 framework; Pattern #21 precedent)

**Linked vault resources:**
- `/Users/Cvtot/KJ OS Template/CLAUDE.md` (Storm Bear meta-entity entry point)
- `/Users/Cvtot/KJ OS Template/PATTERN_LIBRARY.md` (root shim)
- `/Users/Cvtot/KJ OS Template/_patterns/05-recent-additions.md` (recent Pattern Library narrative)
- `/Users/Cvtot/KJ OS Template/05 Skills/llm-wiki-routine-v2.2.md` (LLM Wiki Routine v2.2 reference)

---

## Pattern Library Integration Map

| Pattern | Type | Status | v71 Evidence | File Reference |
|---------|------|--------|------|-----------------|
| #21 (SDD Methodology) | CONFIRMED | within-pattern | Prescriptive agentic design + loop invariants + autonomy levels | entity-3, Pattern #84 doc |
| #66 (Supply-Chain Isolation) | CONFIRMED | within-pattern | 66d "Malicious skill packages" threat | entity-3, Cluster 2 (contributor) |
| #78 (Living-Domain-Standards) | CONFIRMED | N=3 strengthen | MCP 2025-11-25 + OWASP + NIST + multi-vendor | entity-3, Cluster 2 (contributor) |
| #83 (Honest-Deficiency-Disclosure) | CONFIRMED | within-pattern | 83b methodology ("prompt-only insufficient", autonomy-level gating) | entity-3, Cluster 1 (user) |
| #84 (Cross-Vendor Ecosystem) | CANDIDATE | N=3 promote? | 84c Provider-Agnostic-By-Design (NEW archetype) | **PRIMARY Phase 4b doc** |
| OC-O (Agentic-Harness-Execution-Separation) | NEW CANDIDATE | register | 7-invariant loop formalization | entity-3, **PRIMARY Phase 4b doc** |

---

## Corpus-Firsts Summary

1. ✓ First explicit "model proposes, harness disposes" execution-separation formalization (7-invariant loop)
2. ✓ First 15-reference-file structured reference library within single skill
3. ✓ First explicit autonomy-level taxonomy (L0-L4) as safety framework
4. ✓ First provider-agnostic skill synthesizing BOTH OpenAI AND Anthropic equally (Pattern #84 N=3)
5. ✓ First 15-category security threat model in agent skill context
6. ✓ First "draft-commit" pattern formalization as architectural principle
7. ✓ First OWASP + NIST + MCP-spec triple-standard integration (Pattern #78 N=3)
8. ✓ First 12-tier context architecture taxonomy

---

## Timeline (v71 Build)

| Date | Phase | Status | Notes |
|------|-------|--------|-------|
| 2026-05-15 | -- | -- | agents-best-practices repo created (baseline) |
| 2026-05-19 (09:00) | Phase 0 | ✓ Complete | 13-axis classification, Pattern Library pre-check |
| 2026-05-19 (10:00) | Phase 1 | ✓ Complete | CLAUDE.md, COMMANDS.md, foundational files |
| 2026-05-19 (11:00) | Phase 2 | ✓ Complete | open questions, iteration log |
| 2026-05-19 (12:00) | Phase 3 | ✓ Complete | 3 cluster summaries |
| 2026-05-19 (13:00) | Phase 4 | ✓ Complete | 4 entity pages |
| 2026-05-19 (14:00) | Phase 5 | ✓ Complete | Beginner guide (VN/EN) |
| 2026-05-19 (15:00) | Phase 4b PRIMARY | ✓ Complete | Pattern #84 N=3 evaluation + OC-O candidacy |
| → Deferred | Phase 6 | Pending | Vault state sync (separate session) |

---

## Next Actions

1. **Review entity pages + cluster summaries** for cross-link accuracy and Pattern Library integration
2. **Validate Pattern #84 promotion evaluation** — confirm sub-typology 84c definition and promotion criteria logic
3. **OC-O candidacy assessment** — determine if NEW candidate registration warrants OC slot at v71 or defers to v72
4. **Storm Bear MODERATE 2/4 rationale** — confirm (b) operational tool + (c) methodology influence are primary drivers
5. **Phase 6 deferral (separate session):** Rename `_state/03c-projects-v61-v70.md` → `03c-projects-v61-v71.md` and append v71 entry; update Pattern Library state block; update CLAUDE.md weekly update

---

## Files Created at v71

```
03 Projects/agents-best-practices - Beginner Analysis/
├── CLAUDE.md                                        ✓
├── COMMANDS.md                                      ✓
├── 00 Sources/
├── 01 Analysis/
│   ├── (C) open questions.md                        ✓
│   ├── (C) iteration-log.md                         ✓
│   └── (C) Pattern-84-cross-vendor-ecosystem-tolerance-N3-promotion-evaluation.md ✓
├── 02 Wiki/
│   ├── (C) index.md                                 ✓
│   ├── (C) log.md                                   ✓
│   ├── (C) user-facing cluster summary.md           ✓
│   ├── (C) contributor-facing cluster summary.md    ✓
│   ├── (C) technical-distribution cluster summary.md ✓
│   ├── (C) entity-1-core-skill.md                   ✓
│   ├── (C) entity-2-distribution-ecosystem.md       ✓
│   ├── (C) entity-3-pattern-library.md              ✓
│   └── (C) entity-4-storm-bear.md                   ✓
├── 03 Published/
│   └── (C) agents-best-practices - Huong dan cho nguoi moi.md ✓
├── 04 Reviews/
├── 05 Skills/
├── 06 Archive/
└── 07 Inbox/
```
