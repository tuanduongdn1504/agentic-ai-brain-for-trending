# agentmemory — Wiki index

> **Subject:** [`rohitg00/agentmemory`](https://github.com/rohitg00/agentmemory)
> **Tagline (repo):** *"Your coding agent remembers everything. No more re-explaining."* / *"Persistent memory for AI coding agents, powered by iii-engine's three primitives."*
> **Wiki version:** v66 — built 2026-05-14 by Storm Bear vault
> **Routine:** `llm-wiki-routine-v2.2` (first wiki built under v2.2)

## At a glance

| Field | Value |
|---|---|
| **Tier** | **T2 Service** — persistent memory engine running as a server (ports 3111 REST / 3113 viewer); first dedicated agent-memory-system in the 65-wiki corpus |
| **Author** | **Rohit Ghumare** — solo individual engineer (`ghumare64@gmail.com`) |
| **Scale** | 7,900 stars / 675 forks / 23 subscribers / 28 open issues / 34 releases / ~35 days old = **~226 stars/day** (HIGH velocity, just below the 300/day EXTREME-VIRAL flag; **drive-by-stars-dominant** engagement profile) |
| **License** | Apache-2.0 |
| **Stack** | TypeScript 82.4% — `@agentmemory/agentmemory` v0.9.12 on npm; built entirely on **iii-engine** |
| **Architecture** | **4-tier memory consolidation** (Working → Episodic → Semantic → Procedural) + **triple-stream RRF search** (BM25 + Vector + Graph) + **12 auto-capture hooks** + 51 MCP tools + 107 REST endpoints |
| **Benchmark** | **95.2% R@5 on LongMemEval-S** (ICLR 2025) — first memory-retrieval-domain benchmark in corpus; vs mem0 68.5% / Letta-MemGPT 83.2% |
| **Platforms** | 15+ named ("32+" claimed) — Claude Code (deepest) / Cursor / Cline / Windsurf / Gemini CLI / Codex CLI / Hermes / OpenClaw / Goose / Aider / ... via one shared backend |
| **Primary novelty** | **Platform-Primitive Foundation** — built *entirely* on iii-engine's primitives; self-identifies as *"a running iii instance"* |

## Cluster map

| Cluster | Sources | Theme |
|---|---|---|
| [Cluster 1 — README + product positioning](./cluster-1-readme-and-positioning.md) | README.md | What agentmemory IS: the problem (agents forget), 4-tier memory + triple-stream search, 51 MCP tools + 12 hooks, the competitive-comparison table, the 95.2% benchmark claim |
| [Cluster 2 — Contributor docs + governance](./cluster-2-contributor-docs-and-governance.md) | AGENTS.md + CONTRIBUTING + CHANGELOG + ROADMAP + the 11-file governance set | How it's built + maintained: multi-file-sync discipline, Keep-a-Changelog rigor, ROADMAP to V1.0, the v0.8.2 6-vuln security batch, AND the DESIGN.md contamination + doc-skew findings |
| [Cluster 3 — iii-engine foundation + distribution + integrations](./cluster-3-iii-foundation-and-distribution.md) | README iii-engine section + package.json + repo tree + integrations/ + platform table | The iii-primitive foundation, npm distribution, REST/MCP surfaces, 15+ platform integration mechanism (shared-backend) |

## Entity pages

| Entity | Topic | Why |
|---|---|---|
| [Entity 1 — agentmemory core artifact](./entity-1-agentmemory-core.md) | What it IS — 4-tier memory engine / triple-stream RRF search / 12 auto-capture hooks / 51 MCP tools / privacy-by-design | Foundation reference |
| [Entity 2 — Platform-Primitive Foundation](./entity-2-platform-primitive-foundation.md) | Built *entirely* on iii-engine's primitives; self-identifies as "a running iii instance"; rolls none of its own infrastructure | **PRIMARY Pattern Library deliverable** — NEW candidate registration, corpus-first, N=1 stale-flagged |
| [Entity 3 — Distribution, ecosystem & the quality-maturity tension](./entity-3-distribution-and-quality-tension.md) | 15+ platform shared-backend integration + npm + iii-engine relationship — AND viral-velocity-outpacing-quality (DESIGN.md contamination, 6 early vulns, doc skew, README/ROADMAP tension) | Pattern #18 sub-archetype + NEW observational candidate |
| [Entity 4 — Storm Bear meta-entity](./entity-4-storm-bear-meta.md) | Highest-relevance **pilot candidate** in recent corpus — persistent memory for the vault's own Claude Code substrate; vault memory-architecture relevance; Phase 0.9 4/4 STRICT PASS | Phase 0.9 STRONG INCLUDE evidence + pilot-evaluation framing |

> **Storm Bear meta-entity INCLUDED at v66** per Phase 0.9 STRICT **4-of-4 PASS** (criterion (a) author-peer PASS + (b) operational-tool STRONG PASS + (c) methodology-influence PASS + (d) in-corpus-reference PASS). Strongest *breadth* of criteria-coverage in the post-amendment window (v65 was 3/4). Categorized **STRONG INCLUDE**. Streak advances to 2 post-v64-RESET. See [Entity 4](./entity-4-storm-bear-meta.md).

## Beginner guide

Bilingual VN+EN beginner walkthrough: [`(C) agentmemory - Huong dan cho nguoi moi.md`](../03%20Published/(C)%20agentmemory%20-%20Huong%20dan%20cho%20nguoi%20moi.md)

## Phase 4b primary deliverable

NEW Pattern candidate registration proposal: [`(C) Pattern Platform-Primitive Foundation N=1 registration proposal.md`](../01%20Analysis/(C)%20Pattern%20Platform-Primitive%20Foundation%20N=1%20registration%20proposal.md)

## Cross-wiki siblings (mandatory cross-references)

**Knowledge-graph / memory-primitive sibling:**
- [graphify](../../graphify%20-%20Beginner%20Analysis/02%20Wiki/) — knowledge-graph builder; agentmemory's triple-stream search includes a knowledge-graph traversal stream (shared primitive family)

**Claude-Code-host integration peers:**
- [claude-code-system-prompts v65](../../claude-code-system-prompts%20-%20Beginner%20Analysis/02%20Wiki/) — Claude Code internals reference; agentmemory ships `.claude-plugin/` + 12 Claude Code hooks
- [codex-plugin-cc v62](../../codex-plugin-cc%20-%20Beginner%20Analysis/02%20Wiki/) — also ships a `.codex-plugin/`; cross-vendor plugin packaging sibling
- [free-claude-code v60](../../free-claude-code%20-%20Beginner%20Analysis/02%20Wiki/) — T2-adjacent infrastructure sibling

**T2 service / multi-platform peers:**
- [n8n v56](../../n8n%20-%20Beginner%20Analysis/02%20Wiki/) — T2 service (workflow automation)
- [cc-sdd v61](../../cc-sdd%20-%20Beginner%20Analysis/02%20Wiki/) — multi-platform support sibling (8 platforms via install-time translation vs agentmemory's shared-backend mechanism)
