# DeepSeek-TUI Wiki — Phase Index

## Wiki Build Status (v72)

| Phase | Status | Completion | Key Deliverables |
|-------|--------|------------|------------------|
| **Phase 0** | ✓ Complete | 2026-05-19 | 13-axis classification, Pattern Library pre-check, Storm Bear meta-entity, 12 corpus-firsts |
| **Phase 1** | ✓ Complete | 2026-05-19 | CLAUDE.md, COMMANDS.md, index.md, log.md |
| **Phase 2** | ✓ Complete | 2026-05-19 | open questions.md, iteration-log.md |
| **Phase 3** | ✓ Complete | 2026-05-19 | user-facing cluster, contributor-facing cluster, technical-distribution cluster |
| **Phase 4** | ✓ Complete | 2026-05-19 | entity-1 (coding agent), entity-2 (distribution + multi-provider), entity-3 (pattern library), entity-4 (storm bear) |
| **Phase 5** | ✓ Complete | 2026-05-19 | Beginner guide (VN/EN, 400-700 lines) |
| **Phase 4b PRIMARY** | ✓ Complete | 2026-05-19 | Pattern #52 HIGH-NOT-EXTREME sub-class N=2 evaluation (FIRST POST-v72-AUDIT POLICY SATISFACTION) |
| **Phase 6** | → Deferred | Separate session | Vault state sync |

## Core Sources

**GitHub repository:** https://github.com/Hmbown/DeepSeek-TUI
**Homepage:** https://deepseek-tui.com/
**Crates.io:** deepseek-tui-cli (`deepseek` entry point) + deepseek-tui (TUI binary)
**npm:** deepseek-tui (wrapper around release binaries)

**Content analyzed:**
- README.md (588 lines; install paths + features + multi-provider)
- README.zh-CN.md (zh-Hans translation)
- README.ja-JP.md (Japanese translation)
- AGENTS.md (132 lines; project instructions for AI assistants; corpus-rich governance content)
- docs/ARCHITECTURE.md (305 lines)
- docs/MODES.md (93 lines; Plan/Agent/YOLO + approval modes)
- docs/SUBAGENTS.md (178 lines; concurrent sub-agent pool)
- docs/MCP.md (226 lines; MCP server integration)
- 20+ additional docs/ files (INSTALL / CONFIGURATION / KEYBINDINGS / etc.)
- CHANGELOG.md (272 KB; extreme release activity)

## Entities (13-Section Canonical Format)

**Entity 1:** DeepSeek-TUI Coding Agent
- **Type:** T1 Coding Agent / Framework
- **File:** `02 Wiki/(C) entity-1-coding-agent.md`
- **Coverage:** 3 modes (Plan/Agent/YOLO), reasoning-effort tiers, sub-agent pool, RLM batch sessions, MCP integration, OS-level sandbox, durable task queue

**Entity 2:** Distribution + Multi-Provider Ecosystem
- **Type:** Deployment & Packaging
- **File:** `02 Wiki/(C) entity-2-distribution-multi-provider.md`
- **Coverage:** 5 packaging methods, 9-provider matrix (Pattern #84 84c), 4-locale i18n, 2-binary dispatcher-companion split, China-friendly install paths

**Entity 3:** Pattern Library Primary Entity
- **Type:** Pattern Analysis
- **File:** `02 Wiki/(C) entity-3-pattern-library.md`
- **Coverage:** Pattern #52 HIGH-NOT-EXTREME N=2 (PRIMARY), Pattern #84 84c FIRST POST-PROMOTION strengthening, Pattern #21 sub-variant (concurrent-sub-agent-pool), Pattern #83 83b/83d within-pattern, Pattern #66 GitHub-issue-as-attack-surface sub-mechanism candidate, NEW OC-P Community-Built-Canonical-Vendor-Client

**Entity 4:** Storm Bear Meta-Entity
- **Type:** Corpus-Recursive
- **File:** `02 Wiki/(C) entity-4-storm-bear.md`
- **Coverage:** MODERATE 2/4 INCLUDE (b+c), vendor-diversification pilot candidate, session-longevity discipline methodology influence on routine v2.3

## Cluster Summaries (3 User-Facing Perspectives)

- **Cluster 1 — User-Facing:** `(C) user-facing cluster summary.md` (install + first session + modes + key commands)
- **Cluster 2 — Contributor-Facing:** `(C) contributor-facing cluster summary.md` (Rust workspace + AGENTS.md governance + community-contribution discipline + session-longevity)
- **Cluster 3 — Technical/Distribution:** `(C) technical-distribution cluster summary.md` (architecture + 5 packaging methods + 9-provider matrix + OS-sandbox + MCP/LSP integration)

## Published Artifacts

- **Beginner Guide (VN/EN):** `03 Published/(C) DeepSeek-TUI - Huong dan cho nguoi moi.md`

## Analysis & Planning

- **Open Questions:** `01 Analysis/(C) open questions.md`
- **Iteration Log:** `01 Analysis/(C) iteration-log.md`
- **Phase 4b PRIMARY:** `01 Analysis/(C) Pattern-52-HIGH-NOT-EXTREME-velocity-N2-sub-class-strengthening-evaluation.md`

## Cross-Links

**Linked sibling subjects:**
- v71 agents-best-practices (T1 Assistant Skill; Pattern #84 84c sister + Pattern #21 + #78 sisters)
- v70 codegraph (T2 Service; Pattern #18 sub-mechanism B sister; 4-layer hierarchy precedent)
- v69 CloakBrowser (T2 Service; Pattern #52 HIGH-NOT-EXTREME sub-class N=1 sister — DIRECT Phase 4b PRIMARY sister)
- v68 vercel-labs/zero (T1 NEW sub-archetype; Pattern #52 EXTREME-VIRAL adjacent)
- v66 agentmemory (T2 Service; Pattern #18 B1 MCP variant sister)
- v65 claude-code-system-prompts (T1 reference-archive; Pattern #78 N=2 sister)
- v63 andrej-karpathy-skills (T1; Pattern #52 EXTREME-VIRAL N=1 corpus-record sister)
- v61 cc-sdd (T1 SDD framework; Pattern #21 sister)

**Linked vault resources:**
- `/Users/Cvtot/KJ OS Template/CLAUDE.md` (Storm Bear meta-entity entry point)
- `/Users/Cvtot/KJ OS Template/PATTERN_LIBRARY.md` (root shim)
- `/Users/Cvtot/KJ OS Template/_patterns/05-recent-additions.md` (v71/v72-audit narrative)
- v72 audit document at `/Users/Cvtot/KJ OS Template/04 Reviews/(C) 2026-05-19 Pattern Library mini-audit post-v70-v71 (PROMOTION-DRIVEN + 5TH-CONSECUTIVE-TRIGGER; Pattern #84 + Pattern #18 sub-mechanism B PROMOTIONS + 22 other items).md`

## Pattern Library Integration Map

| Pattern | Type | Status | v72 Evidence | File Reference |
|---------|------|--------|------|-----------------|
| #21 (SDD Methodology) | CONFIRMED | within-pattern + sub-variant candidate | 3-mode taxonomy + concurrent-sub-agent-pool with completion events + RLM batch sessions | entity-1, entity-3 |
| #52 (Sustained-Velocity) | CANDIDATE | **HIGH-NOT-EXTREME sub-class N=2** | 267.6/d × 120d satisfies v72-set criteria | **PRIMARY Phase 4b doc** |
| #66 (Supply-Chain Isolation) | CONFIRMED | sub-mechanism candidate 66e | GitHub-issue-as-attack-surface formal treatment | entity-3, Cluster 2 |
| #78 (Living-Domain-Standards) | CONFIRMED | within-pattern (6-layer strengthening) | DeepSeek API + OpenAI-spec + MCP + LSP + Rust-edition + OSC | entity-3, Cluster 3 |
| #83 (Honest-Deficiency-Disclosure) | CONFIRMED | 83b + 83d within-pattern | Multi-surface methodology + experimental-status disclosure | entity-3, Cluster 2 |
| #84 (Cross-Vendor Ecosystem) | CONFIRMED v72 | **84c FIRST POST-PROMOTION STRENGTHENING** | 9-provider-matrix (DeepSeek + 8 alternatives) | entity-2, entity-3 |
| #18 (Agent Runtime Std) | CONFIRMED | sub-mechanism candidate (dispatcher-companion-binary-split) | `deepseek` + `deepseek-tui` 2-binary architecture | entity-1, entity-3 |
| OC-P (Community-Built-Canonical-Vendor-Client) | NEW CANDIDATE | register N=1 | Solo dev builds vendor-product-quality client at 32K-star scale | entity-3 |

## Timeline (v72 Build)

| Date | Phase | Status | Notes |
|------|-------|--------|-------|
| 2026-01-19 | -- | -- | DeepSeek-TUI repo created (baseline) |
| 2026-05-19 (post-audit) | Phase 0 | ✓ Complete | 13-axis classification, Pattern Library pre-check |
| 2026-05-19 | Phase 1 | ✓ Complete | CLAUDE.md, COMMANDS.md, foundational files |
| 2026-05-19 | Phase 2 | ✓ Complete | Open questions, iteration log |
| 2026-05-19 | Phase 3 | ✓ Complete | 3 cluster summaries |
| 2026-05-19 | Phase 4 | ✓ Complete | 4 entity pages |
| 2026-05-19 | Phase 5 | ✓ Complete | Beginner guide (VN/EN) |
| 2026-05-19 | Phase 4b PRIMARY | ✓ Complete | Pattern #52 HIGH-NOT-EXTREME N=2 evaluation |
| → Deferred | Phase 6 | Pending | Vault state sync |

## Next Actions

1. Review entity pages + cluster summaries for cross-link accuracy
2. Validate Pattern #52 HIGH-NOT-EXTREME sub-class N=2 evidence + v75 audit path
3. Confirm OC-P registration as observational candidate (Community-Built-Canonical-Vendor-Client)
4. Pattern #84 84c FIRST POST-PROMOTION-STRENGTHENING validation
5. Storm Bear MODERATE 2/4 rationale confirm (b+c)
6. Phase 6 vault sync: rename `_state/03c-projects-v61-v71.md` → `03c-projects-v61-v72.md` + append v72 entry; update Pattern Library state; update CLAUDE.md weekly update
