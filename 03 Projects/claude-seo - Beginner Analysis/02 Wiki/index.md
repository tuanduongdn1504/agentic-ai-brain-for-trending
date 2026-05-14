# claude-seo — Wiki index

> **Subject:** [`AgriciDaniel/claude-seo`](https://github.com/AgriciDaniel/claude-seo)
> **Tagline (repo):** *"Universal SEO skill for Claude Code. 25 sub-skills + 18 sub-agents (43 primitives total)"*
> **Wiki version:** v64 — built 2026-05-13 by Storm Bear vault
> **Routine:** `llm-wiki-routine-v2.1`

## At a glance

| Field | Value |
|---|---|
| **Tier** | T1 Augmentation — **NEW sub-archetype: domain-vertical-skill-collection** |
| **Author** | Solo individual + 5 named community contributors (Pro Hub Challenge v1.9.0) |
| **Scale** | 6,494 stars / 993 forks / 66 watchers / ~95 days = **~68 stars/day** (medium-high engagement; below Pattern #52 EXTREME-VIRAL threshold; **15.3% fork ratio** signals high active-deployment intent) |
| **License** | MIT (with CC BY 4.0 carve-out for bundled FLOW 41 prompts) |
| **Stack** | Python 3.10+ execution + Markdown SKILL.md skills + JSON manifests |
| **Versioning** | Semantic v1.9.9 (final 1.x patch 2026-05-11) — **5-source atomic-bump CI discipline (13 assertions)** |
| **Platforms** | 5 + 1 sister-port = **6-platform-reach** (Claude Code primary / Cursor / Cursor Cloud / Antigravity / Gemini CLI / Codex CLI port `codex-seo`) — **HIGHEST in corpus T1 history** |
| **Primitives** | **43 total** (25 sub-skills + 18 sub-agents) — **LARGEST T1 collection in corpus** |
| **Ecosystem** | **5-product portfolio**: claude-seo + claude-blog + banana-claude + codex-seo + FLOW framework |

## Cluster map

| Cluster | Sources | Theme |
|---|---|---|
| [Cluster 1 — README + 26 commands + features](./cluster-1-readme-and-commands.md) | README.md (398 lines) + plugin.json + marketplace.json | What the plugin does + how to invoke each of the 26 commands + 4-tier credential model + Quality Gates + Limitations (SPA/CSR transparent) |
| [Cluster 2 — Architecture + skill system](./cluster-2-architecture-and-skill-system.md) | CLAUDE.md (210 lines) + AGENTS.md (126 lines) + skills/ tree | 3-layer architecture (directive / orchestration / execution) + 25 sub-skills + 18 sub-agents + 30 Python scripts + multi-platform discipline (CLAUDE.md vs AGENTS.md split) + Security/Report-generation rules |
| [Cluster 3 — Ecosystem + CHANGELOG history](./cluster-3-ecosystem-and-changelog.md) | CHANGELOG.md (607 lines) + Ecosystem section + extensions/ | 5-product ecosystem-portfolio + v1.0→v1.9.9 release history with version-drift incidents + CI manifest-guard evolution (9→13 assertions) + Pro Hub Challenge community contributors + extension architecture |

## Entity pages

| Entity | Topic | Why |
|---|---|---|
| [Entity 1 — claude-seo core artifact + 3-layer architecture](./entity-1-claude-seo-core.md) | What the plugin IS — architecture, install paths, skill discovery, security/report rules, key principles | Foundation reference for understanding the rest |
| [Entity 2 — 5-product ecosystem-portfolio (Pattern #19 N=3)](./entity-2-ecosystem-portfolio-n3.md) | claude-seo + claude-blog + banana-claude + codex-seo + FLOW — sister-product mechanism + cross-skill workflow | **Pattern #19 ecosystem-portfolio-builder sub-type N=3 strengthening — PROMOTION-ELIGIBLE at v66** (gotalab v61 + forrestchang v63 + AgriciDaniel v64) |
| [Entity 3 — T1 domain-vertical sub-archetype + Living-Domain-Standards Tracking](./entity-3-domain-vertical-and-living-standards.md) | First SEO-vertical T1 collection in corpus + explicit deprecation-aware schema discipline (HowTo Sept 2023 / FAQ Aug 2023 / INP-replaced-FID 2024-03-12 / Quality Rater Sept 2025) | 2 NEW top-level Pattern Library candidates at v64 |
| [Entity 4 — 5-platform reach + Pattern Library implications](./entity-4-multi-platform-and-patterns.md) | Multi-platform via CLAUDE.md vs AGENTS.md split at 5-platform scale + Codex sister-port + full v64 Pattern Library implications | Pattern #18 strengthening + 6 strengthenings + 2 NEW candidates packaged for Phase 5 |

> **Storm Bear meta-entity SKIPPED at v64** per Phase 0.9 STRICT 1-of-4 check (0 strong PASS + 2 WEAK). See project [CLAUDE.md §Phase 0.9](../CLAUDE.md) for evidence. Streak resets 4 → 0 post-v64 SKIP. 9-instance post-amendment window now 77.8% INCLUDE rate (7 PASS / 2 SKIP).

## Beginner guide

Bilingual VN+EN beginner walkthrough: [`(C) claude-seo - Huong dan cho nguoi moi.md`](../03%20Published/(C)%20claude-seo%20-%20Huong%20dan%20cho%20nguoi%20moi.md)

## Cross-wiki siblings (mandatory cross-references)

**Pattern #19 ecosystem-portfolio-builder N=3 peers:**
- [cc-sdd v61](../../cc-sdd%20-%20Beginner%20Analysis/02%20Wiki/) — gotalab N=1 baseline (4-product Japanese SDD/skills ecosystem)
- [andrej-karpathy-skills v63](../../andrej-karpathy-skills%20-%20Beginner%20Analysis/02%20Wiki/) — forrestchang N=2 (2-product viral + commercial)

**T1 Augmentation peers (skills collections at different sub-archetypes):**
- [mattpocock-skills v57](../../mattpocock-skills%20-%20Beginner%20Analysis/02%20Wiki/) — 19-skill general-purpose collection
- [awesome-claude-skills v50](../../awesome-claude-skills%20-%20Beginner%20Analysis/02%20Wiki/) — curated-meta aggregator
- [agent-skills-of-vercel v51](../../agent-skills-of-vercel%20-%20Beginner%20Analysis/02%20Wiki/) — corporate-curated collection
- [andrej-karpathy-skills v63](../../andrej-karpathy-skills%20-%20Beginner%20Analysis/02%20Wiki/) — single-artifact behavioral collection

**Multi-platform peers:**
- [cc-sdd v61](../../cc-sdd%20-%20Beginner%20Analysis/02%20Wiki/) — 8 platforms framework-scale
- [andrej-karpathy-skills v63](../../andrej-karpathy-skills%20-%20Beginner%20Analysis/02%20Wiki/) — 2 platforms single-skill manual-sync

**Plugin marketplace peers:**
- [codex-plugin-cc v62](../../codex-plugin-cc%20-%20Beginner%20Analysis/02%20Wiki/) — corporate-scale OpenAI marketplace
- [oh-my-claudecode v27](../../oh-my-claudecode%20-%20Beginner%20Analysis/02%20Wiki/) — N=1 Pattern #59 solo marketplace
- [claude-hud v35](../../claude-hud%20-%20Beginner%20Analysis/02%20Wiki/) — N=2 Pattern #59 solo marketplace

**MCP extension peers:**
- [shannon v45](../../shannon%20-%20Beginner%20Analysis/02%20Wiki/) — AI-pentester with MCP
- [aidevops v47](../../aidevops%20-%20Beginner%20Analysis/02%20Wiki/) — DevOps with MCP
