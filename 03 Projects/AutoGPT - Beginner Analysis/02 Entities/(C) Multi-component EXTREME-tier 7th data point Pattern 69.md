# (C) Multi-component EXTREME-tier 7th data point — Pattern #69 strengthening

> **Entity 3 of 4** — AutoGPT v59
> **Type:** Novel-pattern entity (Pattern #69 EXTREME-primitive-count strengthening; multi-tier monorepo at T1+T5 = corpus-first explicit T1+T5 convergence)

---

## 1. What it is (one-line)

AutoGPT v59 is the **7th EXTREME-primitive-count subject in corpus** (Pattern #69 strengthening) AND the **first explicit multi-tier T1+T5 monorepo within single repo** — distinct from prior multi-tier observations (gh-aw v48 single-T-with-multi-component / n8n v56 single-T2 with multi-integrations).

## 2. Pattern #69 EXTREME-primitive-count history

| # | Wiki | Tier | Primitive count source |
|---|---|---|---|
| 1 | ruflo v42 | T2 | AI orchestration with 7+ primitive types |
| 2 | aidevops v47 | T1 | Multi-component DevOps agent platform |
| 3 | gh-aw v48 | Bridge | Multi-tier workflow-automation primitives |
| 4 | awesome-claude-skills v50 | T1 | 100s of skills + categories aggregator |
| 5 | oh-my-openagent v52 | T1 | Multi-runtime + multi-protocol primitives |
| 6 | n8n v56 | T2 | 400+ integrations + 16 LLM providers + 11 vector stores + 8 memory + 6 agent types |
| **7** | **AutoGPT v59** | **T1+T5** | **Platform + Classic + Forge + benchmark + frontend + docs + agents-config + .claude-config + workflows = ≥7 distinct primitive-types** |

**Formal-statement-extension at v60 mini-audit:** Pattern #69 with N=7 data points across 4 distinct tiers (T1 / T2 / T1+T5 / Bridge). Distribution: 4× T1 / 2× T2 / 1× T1+T5 / 1× Bridge.

## 3. AutoGPT-specific primitive list

**AutoGPT Platform primitives (`autogpt_platform/`):**
- Agent Builder (low-code interface)
- Workflow Management
- Ready-to-Use Agents library
- Monitoring/observability
- Backend services (Python)
- Frontend UI (TypeScript)

**AutoGPT Classic primitives (`classic/`):**
- Standalone agent loop
- Tool-use abstraction
- Memory store
- Configuration system
- CLI interface

**AutoGPT Forge primitives (`classic/forge/`):**
- Agent template/scaffold
- Forge SDK for custom agents
- Provider abstractions

**Benchmark primitives:**
- Agent performance evaluation harness
- Benchmark suite definitions

**Frontend primitives:**
- TypeScript UI components
- Visual agent-builder UI

**Governance primitives:**
- AGENTS.md (agent-other-than-Claude config)
- CLAUDE.md (Claude-specific config)
- CITATION.cff (citation metadata)
- LICENSE (dual-license declaration)
- SECURITY.md
- .pre-commit-config.yaml + codecov.yml + .deepsource.toml

**Total ≥9 distinct primitive types** — comfortably EXTREME-tier.

## 4. Multi-tier T1+T5 within single repo (corpus-first)

**T1 Platform** (`autogpt_platform/`) = agent-building-platform (corpus tier T1 = agent-builder/host substrate)

**T5 Classic** (`classic/`) = standalone-agent-application (corpus tier T5 = application-layer, end-user-facing)

**Bridge Forge** (`classic/forge/`) = developer-toolkit for building agents (T1↔T5 bridge — used by both platform-builders and application-builders)

**Why this is corpus-first:**
- gh-aw v48 = workflow-automation single-tier (T-bridge) with multiple components within
- n8n v56 = single-T2 platform with 400+ integrations (integrations are sub-components, not separate-tier products)
- oh-my-openagent v52 = T1 with multi-runtime/protocol (sub-components, single-tier)
- awesome-claude-skills v50 = T1 aggregator
- AutoGPT v59 = **explicitly different products at different tiers within single repo** — Platform (T1) AND Classic (T5) are distinct deployable products with distinct value-props served by single repo

**Pattern #2 distribution-evolution sub-observation: multi-tier-within-monorepo distribution strategy.**

## 5. Architectural implications

**Why dual-licensing maps to multi-tier-monorepo:**

The dual-licensing (MIT for Classic + Forge / PolyForm-Shield for Platform) reflects the architectural-tier divergence within the monorepo:
- **MIT** for the community-foundation ecosystem layer (Classic agent + Forge toolkit + benchmark)
- **PolyForm-Shield** for the commercializable platform layer (in-development cloud-tier)

This is a **license-as-tier-marker pattern** — license boundary cleanly maps to tier boundary within monorepo. **NEW Pattern #29 + Pattern #45 sub-observation.**

## 6. Cross-references to siblings

- **n8n v56** — 6th EXTREME-tier predecessor; 2nd-largest corpus pure-product (185K stars peer); single-T2 not multi-tier
- **gh-aw v48** — 3rd EXTREME-tier predecessor; multi-tier-but-single-product
- **oh-my-openagent v52** — 5th EXTREME-tier predecessor; T1-only multi-runtime
- **ruflo v42** — first EXTREME-tier observation (Pattern #69 origin)

## 7. Pattern #22 AGENTS.md + CLAUDE.md coexistence

**Both files present at root** = Pattern #22 strengthening sub-observation. Most corpus subjects have one or the other, not both.

**Hypothesis (open question Q7):** AGENTS.md serves agents-other-than-Claude (universal agent-instructions) while CLAUDE.md serves Claude-specific instructions. If verified, **role-divergence sub-observation** = Pattern #22 sub-axis worth flagging.

**Comparable cases:**
- gsd-2 v54 (similar 2-file presence)
- Verify other corpus subjects at v60 mini-audit grep for 2-file-coexistence frequency

## 8. Tier placement nuance

AutoGPT presents a **classification challenge** — multi-tier-within-single-repo doesn't fit Storm Bear corpus's 1-subject = 1-tier convention.

**Decision:** Primary T1 (autogpt_platform/ active development center-of-gravity); secondary T5 noted (classic/ legacy-but-still-distributed).

**Routine v2.1 future-version proposal:** Add multi-tier-subject support to Phase 0.4 classification probe. NEW v2.2 candidate at next routine refactor.

## 9. Cross-references summary

- **EXTREME-tier predecessors:** ruflo v42 / aidevops v47 / gh-aw v48 / awesome-claude-skills v50 / oh-my-openagent v52 / n8n v56
- **Multi-tier-monorepo precedent:** n8n v56 (single-T2 with sub-components — different from AutoGPT's multi-tier explicit divergence)
- **Pattern #22 2-file-coexistence:** gsd-2 v54

## 10. Pattern Library impact

| Pattern | Direction | Note |
|---|---|---|
| #69 EXTREME primitive-count | STRENGTHEN | 7th data point; formal-statement-extension at v60 |
| #2 distribution-evolution | STRENGTHEN | Multi-tier-within-monorepo NEW sub-observation |
| #22 AGENTS.md + CLAUDE.md coexistence | STRENGTHEN | 2-file-coexistence rare |
| **Multi-tier T1+T5 within single repo** | **NEW SUB-OBSERVATION** | corpus-first; consolidation-forward routes to within-pattern (Pattern #2 distribution-evolution sub) |

## 11. Tier placement confirmation

Primary **T1 Assistant** with secondary **T5 Application** noted; multi-tier subject classification for v59 entry in state-block.

## 12. Open questions

- Q8-10 (architectural questions): Python+TS hybrid disaggregation by sub-component; runtime substrate; Forge T1-vs-T5 placement nuance

## 13. Storm Bear pilot relevance

**LOW-MEDIUM for direct deployment** (multi-component complexity high; would require significant infrastructure investment for self-host).

**HIGH for architectural-vocabulary contribution** — multi-tier-within-monorepo + license-as-tier-marker observations enrich Pattern Library at v60 mini-audit.
