# (C) Index — goclaw Wiki

> Catalog wiki cho `nextlevelbuilder/goclaw`. Cập nhật sau mỗi ingest.

## 🎯 Project status (2026-04-18)

- ✅ Phase 0: Pre-flight — PASSED (42MB, 117 .md, **adjacent domain** → Phase 4b reframed)
- ✅ Phase 1: Setup — COMPLETE
- ✅ Phase 2: Source ingestion — COMPLETE (3 source summaries)
- ✅ Phase 3: Entity pages — COMPLETE (4 entity pages)
- ✅ Phase 4a: Beginner published guide — COMPLETE
- ✅ Phase 4b: **Agent framework taxonomy** (reframed from 4-way comparison) — COMPLETE
- ✅ Phase 5: Iteration log v4 — COMPLETE
- ✅ Phase 6: Vault file updates — COMPLETE

**🎉 v4 SHIPPED.** 4th auto-execution của routine. First adjacent-domain project. Taxonomy abstraction unlocked.

**Repo:** 117 .md files, 42MB, Go-based
**Author:** nextlevelbuilder (nlb_io)
**Routine:** `05 Skills/llm-wiki-routine.md` — 4th auto-execution
**Domain:** Multi-Tenant AI Agent Platform (agent-as-service tier)

## Positioning vs siblings

**goclaw = different architectural layer:**
- **Agent-as-assistant** (ECC/Superpowers/gstack): enhance Claude Code cho dev workflow
- **Agent-as-service** (goclaw): multi-tenant platform cho end users

→ Not competitor. Complementary.

## Sources

| Page | Summary | Ingested |
|------|---------|----------|
| [[(C) README summary]] | Overview, 8 core features, 20+ providers, 7 channels, Karpathy LLM Wiki connection | 2026-04-18 |
| [[(C) CLAUDE.md + Architecture summary]] | Dev conventions, 17 Plan Verification Rules, 13 mobile UI rules, V3 pipeline, 11 distinctive patterns | 2026-04-18 |
| [[(C) Key Docs deep dive]] | Skills Runtime (5-tier hierarchy), Agent Teams model, 5-layer defense security, CHANGELOG skim | 2026-04-18 |

## Concepts (planned từ Phase 0 survey)

- 8-Stage Agent Pipeline (context → history → prompt → think → act → observe → memory → summarize)
- 4-Mode Prompt System (Full/Task/Minimal/None)
- 3-Tier Memory (Working/Episodic/Semantic + progressive loading L0/L1/L2)
- Knowledge Vault (wikilinks + FTS + pgvector) — **meta-relevant to Storm Bear vault**
- Multi-Tenant architecture (per-user workspaces, AES-256-GCM, RBAC)
- Agent Teams & Orchestration (3 modes: auto/explicit/manual)
- Self-Evolution (metrics → suggestions → auto-adapt)
- Skills Runtime (Anthropic-compatible)
- 20+ LLM providers + 7 messaging channels
- Desktop Edition "GoClaw Lite" (Wails v2 + React + SQLite)

## Entities

| Page | Type | Sources | Status |
|------|------|---------|--------|
| [[(C) 8-Stage Agent Pipeline]] | Workflow concept | 01-agent-loop + CLAUDE.md | ✅ |
| [[(C) 3-Tier Memory + Knowledge Vault]] | Storage concept | README + CLAUDE.md + vault/consolidation modules | ✅ |
| [[(C) Multi-Tenant Architecture]] | Distribution/deployment concept | README + CLAUDE.md + 09-security | ✅ |
| [[(C) Agent Teams and Orchestration]] | Orchestration concept | README + 11-agent-teams | ✅ |

## Roadmaps / Published

- ✅ [[../03 Published/(C) goclaw - Huong dan cho nguoi moi]] — beginner guide bilingual
- ✅ [[../03 Published/(C) Agent framework taxonomy]] — **tier-based taxonomy** (4-framework positioning, không phải 4-way comparison)

## Cross-project siblings

- `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) index.md`
- `../../Superpowers - Beginner Analysis/02 Wiki/(C) index.md`
- `../../gstack - Beginner Analysis/02 Wiki/(C) index.md`

## Logs

- [[(C) log]]
