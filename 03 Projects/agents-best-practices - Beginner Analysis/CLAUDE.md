# DenisSergeevitch/agents-best-practices — v71 Wiki

## Subject Overview

**Repository:** https://github.com/DenisSergeevitch/agents-best-practices
**Author:** DenisSergeevitch (solo developer, likely Eastern European)
**Created:** 2026-05-15 (4 days old as of wiki-build 2026-05-19)
**Stats:** 821 stars | 72 forks | 4 open issues | 4 subscribers
**Velocity:** 205.25 stars/day (high, though age too young for sustained classification)
**License:** MIT | **Language:** Markdown-only
**Fork ratio:** 0.088 (healthy engagement)

**Description:** Provider-neutral Agent Skill synthesizing production patterns from OpenAI, Anthropic, and agentic-harness design. Core philosophy: "The model proposes; the harness validates, authorizes, executes, records, and returns observations." Installable via `npm install -g skills && skills attach DenisSergeevitch/agents-best-practices` or direct git clone.

**Corpus position:** v71 (continuing 70-wiki series; 4th corpus T1 skill entry; Storm Bear meta-entity slot 4)

---

## 13-Axis Classification (Phase 0)

| Axis | Classification | Notes |
|------|---|---|
| **Tier** | T1 (assistant skill) | Installable SKILL.md + 15 reference files = 17-file governance package |
| **Archetype** | solo-community | Individual developer; synthesis of production patterns |
| **Scale** | Small (<5K stars) | 821 stars at v71 build |
| **Primary Language** | Markdown-only | No source code; 100% documentation + guidance |
| **Packaging** | npm/shell skills CLI | `skills attach` deployment model; also git-clone compatible |
| **Origin story** | individual-author synthesis | Curated from Anthropic + OpenAI production docs |
| **Methodology** | Feature-framework prescriptive | 8 foundational principles + 7 loop invariants + L0-L4 autonomy levels |
| **Governance file count** | Extensive (17 files) | SKILL.md + README + 15 reference files; most comprehensive reference library in corpus |
| **Agent/skill count** | 1 skill + 15 sub-references | Single unified skill with deep reference architecture |
| **i18n** | EN-only | No translation or i18n support |
| **Intellectual influence** | Multi-vendor synthesis | Anthropic (5 guides) + OpenAI (2 guides) + OWASP + NIST AI RMF |
| **Agent platforms** | 3-platform coverage | Claude Code + Codex + OpenAI Agents |
| **Living-Domain-Standards** | YES (Pattern #78) | MCP spec 2025-11-25 (version-pinned URL) + OWASP + NIST + Anthropic suite + OpenAI suite |

---

## Pattern Library Pre-Check (Phase 0)

### Pattern #78 (CONFIRMED) — Living-Domain-Standards Tracking
- **Current status:** N=2 (v64 claude-seo + v65 claude-code-system-prompts)
- **v71 evidence:** agents-best-practices = N=3 strengthening
  - Implements MCP spec 2025-11-25 (version-pinned reference)
  - Integrates OWASP AI Agent Security Cheat Sheet + Agentic Skills Top 10
  - Integrates NIST AI Risk Management Framework
  - Cites Anthropic: building-effective-agents, context-engineering, writing-tools-for-agents, long-running-agents, equipping-agents-for-the-real-world-with-agent-skills
  - Cites OpenAI: agents guide, function-calling, guardrails-approvals, tools-connectors-mcp, harness-engineering
  - **v71 sub-mechanism:** 78a multi-vendor (OWASP + NIST + MCP + Anthropic + OpenAI triple-vendor triple-standard integration)
- **Promotion status:** CONFIRMED (unchanged; within-pattern strengthening only)

### Pattern #84 (CANDIDATE) — Cross-Vendor Ecosystem-Tolerance
- **Current status:** N=2 (v62 codex-plugin-cc + v65 claude-code-system-prompts)
- **v71 evidence:** agents-best-practices = N=3 potential promotion
  - **v62 codex-plugin-cc (84a):** Tool-tolerance (OpenAI publishes plugin explicitly FOR Claude Code)
  - **v65 claude-code-system-prompts (84b):** Usage-enforcement (Anthropic documents Claude Code product internals for cross-vendor awareness)
  - **v71 agents-best-practices (84c):** Provider-Agnostic-By-Design (individual author creates unified framework explicitly targeting BOTH OpenAI Codex AND Anthropic Claude Code equally; neither vendor dominates)
- **Promotion criteria evaluation:** See `01 Analysis/(C) Pattern-84-cross-vendor-ecosystem-tolerance-N3-promotion-evaluation.md`
- **Note:** v71 evidence archetype differs from v62/v65 (author design choice vs ecosystem norm); recommend sub-typology 84c "Provider-Agnostic-By-Design" registration during evaluation

### Pattern #83 (CONFIRMED) — Honest-Deficiency-Disclosure Discipline
- **v71 within-pattern strengthening:** 83b (methodology deficiency disclosure)
  - "Prompt-only safety is insufficient"
  - "Most agent failures caused by weak harness boundaries, not insufficient autonomy"
  - Autonomy-level-gating discipline: "Move up levels only when evals show the simpler level is insufficient"

### Pattern #21 (CONFIRMED) — SDD Methodology Emergence
- **v71 within-pattern strengthening:** Prescriptive agentic system design methodology with explicit loop invariants, autonomy levels, planning mode formalization

### Pattern #66 (CONFIRMED) — Supply-Chain Isolation
- **v71 within-pattern strengthening:** 66d "Malicious skill packages" threat category (v71 explicitly treats connector tool descriptions as potentially unreliable unless from trusted sources)

### NEW Candidate — "Agentic-Harness-Execution-Separation"
- **Definition:** "The model never executes a tool directly. It emits a structured request. The harness executes or rejects it." Formal separation of inference-layer (model proposes) from execution-layer (harness disposes).
- **v71 evidence:** 7 loop invariants explicitly formalizing this separation:
  1. Each tool call gets exactly one result
  2. Arguments parsed and validated before execution
  3. Permission decisions occur before side effects
  4. Results bounded, structured, traceable
  5. Hard budgets for steps, time, tokens, cost, calls
  6. Final answers derive from observations, not assumed success
  7. Errors become structured observations
- **Rationale for candidacy:** Novel architectural governance principle not captured in existing patterns (closest: Pattern #80 Tool-Level Adversarial Review, which is about review discipline, not execution separation architecture)
- **Recommended action:** Register as NEW observational candidate OC-O "Agentic-Harness-Execution-Separation" pending v71+ evaluation

---

## Phase 4b PRIMARY Routing

**File:** `01 Analysis/(C) Pattern-84-cross-vendor-ecosystem-tolerance-N3-promotion-evaluation.md`

**Route:** Pattern #84 N=3 promotion evaluation with sub-typology 84c registration proposal

**Content:**
- Current N=2 status + v71 N=3 evidence framework
- 84c sub-typology definition: "Provider-Agnostic-By-Design"
- Promotion criteria evaluation (5 criteria + cross-archetype dimension)
- Verdict and acceleration timeline
- NEW candidate OC-O brief mention
- Audit checklist for v71+ incorporation

---

## Storm Bear (Phase 0.9)

**Meta-entity slot:** 4 (corpus-recursive analysis)
**Classification:** MODERATE INCLUDE (2/4 PASS)

| Criterion | Result | Evidence |
|---|---|---|
| (a) Author archetype peer | FAIL | Eastern European solo developer; not VN/Asian-diaspora demographic match |
| (b) Operational tool for vault | PASS | Directly installable as Claude Code skill; applicable to Storm Bear vault agentic-harness design work |
| (c) Methodology influence | PASS | 7-invariant loop architecture + context tiers + planning mode + autonomy levels directly inform LLM wiki routine v2.2 design and refinement |
| (d) In-corpus reference | FAIL | References Claude Code + Anthropic docs, but no explicit corpus-subject URL citation (Pattern #57 57d at most) |

**Recommendation:** MODERATE INCLUDE (meta-entity slot 4); deploy as operational skill-reference for Storm Bear's Claude Code agentic work; routine v2.2 methodology-influence recognized for future routine refinement phases.

---

## Cross-Wiki Siblings

- **v66 agentmemory** (T2 Service) — agent memory system; Pattern #85; operational sister-service
- **v65 claude-code-system-prompts** (T1 reference-archive) — Pattern #78 N=2 + Pattern #84 N=2; methodology-sister
- **v64 claude-seo** (T1 skill-collection) — Pattern #78 N=1; Living-Domain-Standards precedent
- **v62 codex-plugin-cc** (T4 Bridge) — Pattern #84 N=1 first cross-vendor evidence
- **v63 andrej-karpathy-skills** (T1 single-artifact) — high-velocity T1 precedent
- **v61 cc-sdd** (T1 framework) — SDD methodology precedent (Pattern #21)
- **agent-skills-of-vercel** (older T1) — similar skill distribution archetype
- **claude-code-best-practice** (older T1) — best-practices format precedent
- **awesome-mcp-servers** (older reference) — MCP ecosystem context

---

## Corpus-Firsts (v71)

1. **FIRST explicit "model proposes, harness disposes" execution-separation formalization** (7-invariant loop architecture as governance principle, not just architectural pattern)
2. **FIRST 15-reference-file structured reference library within single skill** (most comprehensive reference architecture in corpus; previous max ~5-8 references per subject)
3. **FIRST explicit autonomy-level taxonomy (L0-L4) as safety framework** (graduated deployment governance)
4. **FIRST provider-agnostic skill explicitly synthesizing BOTH OpenAI AND Anthropic agentic patterns equally** (Pattern #84 N=3; meta-archetype shift from v62/v65 ecosystem-tolerance to author-design-choice)
5. **FIRST 15-category security threat model in agent skill context** (comprehensive threat coverage: prompt injection, malicious retrieved content, tool misuse, permission bypass, secret leakage, data exfiltration, unsafe external communication, financial/destructive side effects, connector abuse, malicious skill packages, runaway loops, cost exhaustion, false success claims, compaction state loss, subagent miscoordination)
6. **FIRST "draft-commit" pattern formalization** (draft_email→send_email two-phase separation as explicit architectural principle; Pattern #21 strengthening)
7. **FIRST OWASP + NIST + MCP-spec triple-standard integration** (Pattern #78 N=3; v71 multi-vendor-standards convergence)
8. **FIRST 12-tier context architecture taxonomy** (context tiering governance: provider/organization/role/task/plan/scoped/retrieved/visible-skill/visible-tool/observations/history/reminders)

---

## v71 Build Metadata

**Build date:** 2026-05-19 (session 73++)
**Repository analysis date:** 2026-05-19
**Phase 0 completion date:** 2026-05-19
**Phases 1-6 build status:** In progress
**Storm Bear author:** DenisSergeevitch (noted as likely Eastern European; no Storm Bear demographic match)
**Velocity classification:** HIGH-velocity-NOT-EXTREME (205.25 stars/day; age 4 days; below Pattern #52 >300 threshold; too young for sustained classification)
**Engagement:** sub-threshold-control test case (age <4 days; not Pattern #52 candidate yet; will re-evaluate at v72+)

---

## Files Created at v71

- CLAUDE.md (this file)
- COMMANDS.md
- 00 Sources/ (placeholder)
- 01 Analysis/
  - (C) open questions.md
  - (C) iteration-log.md
  - (C) Pattern-84-cross-vendor-ecosystem-tolerance-N3-promotion-evaluation.md
- 02 Wiki/
  - (C) index.md
  - (C) log.md
  - (C) user-facing cluster summary.md
  - (C) contributor-facing cluster summary.md
  - (C) technical-distribution cluster summary.md
  - (C) entity-1-core-skill.md
  - (C) entity-2-distribution-ecosystem.md
  - (C) entity-3-pattern-library.md
  - (C) entity-4-storm-bear.md
- 03 Published/
  - (C) agents-best-practices - Huong dan cho nguoi moi.md
- 04 Reviews/ (placeholder)
- 05 Skills/ (placeholder)
- 06 Archive/ (placeholder)
- 07 Inbox/ (placeholder)

---

## Next Actions

1. Read repo README + SKILL.md + 15 reference files (detailed content analysis)
2. Complete Phases 1-6 files in order: COMMANDS.md → foundational → cluster summaries → entity pages → beginner guide → Phase 4b primary → iteration log
3. Cross-link all entity pages and cluster summaries
4. Validate Pattern Library integrations
5. Storm Bear meta-entity recommendations
6. Phase 6 vault sync (CLAUDE.md state updates) — deferred to separate session
