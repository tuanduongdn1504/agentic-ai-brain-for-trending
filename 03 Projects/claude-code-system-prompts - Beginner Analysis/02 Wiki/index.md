# claude-code-system-prompts — Wiki index

> **Subject:** [`Piebald-AI/claude-code-system-prompts`](https://github.com/Piebald-AI/claude-code-system-prompts)
> **Tagline (repo):** *"All parts of Claude Code's system prompt, 24 builtin tool descriptions, sub agent prompts (Plan/Explore/Task), utility prompts... Updated for each Claude Code version."*
> **Wiki version:** v65 — built 2026-05-13 → 2026-05-14 by Storm Bear vault
> **Routine:** `llm-wiki-routine-v2.1`

## At a glance

| Field | Value |
|---|---|
| **Tier** | T1 Augmentation — **NEW sub-archetype: reverse-engineering-reference-archive** |
| **Author** | **Piebald-AI** corporate-org (commercial agentic IDE company at piebald.ai) |
| **Scale** | 10,176 stars / 1,811 forks / 118 subscribers / ~176 days = **~57.8 stars/day** (medium-high engagement; **17.8% fork ratio = CORPUS-RECORD active-deployment intent**) |
| **License** | MIT |
| **Stack** | JavaScript (`tools/updatePrompts.js` extraction) + Markdown (293 system-prompt files) |
| **Versioning** | **176 versions tracked since v2.0.14** (current Claude Code v2.1.140 May 12 2026); 127 full + 49 no-change placeholder; updated **within minutes of each Claude Code release** |
| **Coverage** | **293 system-prompt files** spanning 6 categories: ~30 Agent Prompts / ~50 Data templates / ~50 System Prompts / ~40 System Reminders / ~50 Tool Descriptions / ~25 Skills |
| **Primary methodology** | **Reverse-engineering reference-archive** — automated extraction from compiled `@anthropic-ai/claude-code` npm package |
| **Sister products** | **Piebald** commercial agentic IDE (piebald.ai) + **tweakcc** local-patching tool |

## Cluster map

| Cluster | Sources | Theme |
|---|---|---|
| [Cluster 1 — README + 293-file prompt inventory](./cluster-1-readme-and-prompt-inventory.md) | README.md (69 KB, 405 lines) | What the archive contains: 6-category 293-file inventory + per-file token counts + descriptions + how to use the files |
| [Cluster 2 — Extraction methodology + CLAUDE.md](./cluster-2-extraction-methodology.md) | CLAUDE.md (1.6 KB) + tools/updatePrompts.js (19.5 KB) + README "Extraction" section | How extraction works: compiled-binary parsing via `updatePrompts.js` + "For AI agents" guidance + tweakcc sister-tool patching mechanism + Piebald-AI commercial context |
| [Cluster 3 — CHANGELOG 176-version evolution + Piebald-AI ecosystem](./cluster-3-changelog-and-ecosystem.md) | CHANGELOG.md (211 KB, 1896 lines) + Piebald-AI org context | 176-version absorption ledger discipline + per-version commit links + token-deltas + Piebald-AI ecosystem (Piebald commercial + tweakcc + open-source archive) |

## Entity pages

| Entity | Topic | Why |
|---|---|---|
| [Entity 1 — claude-code-system-prompts core artifact](./entity-1-archive-core.md) | What the archive IS — 293 prompt files / 6 categories / extraction methodology / minimal governance | Foundation reference |
| [Entity 2 — Pattern #78 N=2 strengthening + 1-wiki un-stale cycle](./entity-2-pattern-78-n2-strengthening.md) | claude-seo v64 (78a multi-vendor) + claude-code-system-prompts v65 (78b single-vendor-product-internals) = N=2 cross-archetype | **PRIMARY Pattern Library deliverable**: Pattern #78 PROMOTION-ELIGIBLE at v67 (or accelerated v66); FASTEST un-stale cycle in 64-wiki corpus history (1-wiki turnaround) |
| [Entity 3 — Piebald-AI corporate-org + Pattern #19 N=4 + Pattern #57 STRONGEST instance](./entity-3-piebald-ai-and-ecosystem.md) | Piebald commercial agentic IDE + claude-code-system-prompts + tweakcc = 3-product portfolio at CORPORATE-org archetype; corpus-recursive at maximum depth | Pattern #19 N=4 strengthening + Pattern #57 57c-strongest-instance |
| [Entity 4 — Storm Bear meta-entity: corpus-recursive maximum-depth reference](./entity-4-storm-bear-meta.md) | Why this subject = STRONGEST 3-of-4 STRICT PASS in Phase 0.9 history; vault uses Claude Code as primary substrate; 80% INCLUDE rate post-v65 | Phase 0.9 STRONG INCLUDE evidence + corpus-recursive observation |

> **Storm Bear meta-entity INCLUDED at v65** per Phase 0.9 STRICT 3-of-4 STRONG PASS (criterion (b) operational-tool STRONG + (c) methodology-influence STRONG + (d) in-corpus-reference STRONGEST-IN-CORPUS-HISTORY; only (a) author-archetype-peer FAIL). See [Entity 4](./entity-4-storm-bear-meta.md) for full Phase 0.9 evidence. Streak RESTARTS at 1 post-v64-RESET. 10-instance post-amendment window now 80% INCLUDE rate (8 PASS / 2 SKIP).

## Beginner guide

Bilingual VN+EN beginner walkthrough: [`(C) claude-code-system-prompts - Huong dan cho nguoi moi.md`](../03%20Published/(C)%20claude-code-system-prompts%20-%20Huong%20dan%20cho%20nguoi%20moi.md)

## Cross-wiki siblings (mandatory cross-references)

**Pattern #78 Living-Domain-Standards Tracking N=2 peer:**
- [claude-seo v64](../../claude-seo%20-%20Beginner%20Analysis/02%20Wiki/) — 78a multi-vendor industry domain standards baseline

**Pattern #21 System Prompts Leaks lineage (v21 system-prompts-leaks):**
- system-prompts-leaks v21 — Pattern #21 N=1 baseline (in `_state/05-projects-v1-v29.md`); one-time leak archive predecessor to v65 continuous-extraction discipline

**Pattern #19 ecosystem-portfolio-builder N=4 peers:**
- [cc-sdd v61](../../cc-sdd%20-%20Beginner%20Analysis/02%20Wiki/) — gotalab solo-Japanese N=1
- [andrej-karpathy-skills v63](../../andrej-karpathy-skills%20-%20Beginner%20Analysis/02%20Wiki/) — forrestchang solo-engineer-commercial N=2
- [claude-seo v64](../../claude-seo%20-%20Beginner%20Analysis/02%20Wiki/) — AgriciDaniel solo-individual-SEO-vertical N=3

**T1 Augmentation peers (skills collections at different sub-archetypes):**
- [mattpocock-skills v57](../../mattpocock-skills%20-%20Beginner%20Analysis/02%20Wiki/) — 19-skill general-purpose
- [awesome-claude-skills v50](../../awesome-claude-skills%20-%20Beginner%20Analysis/02%20Wiki/) — curated-meta aggregator
- [agent-skills-of-vercel v51](../../agent-skills-of-vercel%20-%20Beginner%20Analysis/02%20Wiki/) — corporate-curated
- [andrej-karpathy-skills v63](../../andrej-karpathy-skills%20-%20Beginner%20Analysis/02%20Wiki/) — single-artifact behavioral
- [claude-seo v64](../../claude-seo%20-%20Beginner%20Analysis/02%20Wiki/) — domain-vertical-skill-collection

**Claude-Code-host observational stance peers:**
- [free-claude-code v60](../../free-claude-code%20-%20Beginner%20Analysis/02%20Wiki/) — translates TO Claude Code's API (consumes Claude Code's surface from backend)
- [codex-plugin-cc v62](../../codex-plugin-cc%20-%20Beginner%20Analysis/02%20Wiki/) — OpenAI publishes FOR Claude Code (cross-vendor cooperation observation)
- (v65 = third observational stance: extracts FROM Claude Code's compiled binary)
