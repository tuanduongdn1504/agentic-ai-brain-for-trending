# (C) punkpeye — Author ecosystem + MCP advocate archetype

**Entity type:** Individual actor + author ecosystem (Pattern #17 data point)
**Real name:** Frank Fiegel
**GitHub:** [@punkpeye](https://github.com/punkpeye)
**Commercial entity:** Glama (https://glama.ai)
**Archetype:** Solo-ecosystem-layer-with-commercial-platform (proposed Pattern #17 variant 6 candidate at N=1; structurally parallels v25 VoltAgent org-level + v27 Yeachan individual-multi-runtime)

---

## 1. Profile summary

Frank Fiegel is a **Miami-based engineer-turned-founder** who has built a vertical ecosystem slice around the Model Context Protocol (MCP) starting 2024-11-30 (within days of Anthropic's MCP public launch). As of 2026-04-22 he maintains a 7-repo MCP portfolio + commercial platform Glama + ecosystem-state publications.

**Self-description (GitHub bio):** *"Engineer turned founder"*

**Short summary:**
- Rapid-sequence MCP ecosystem builder: directory → framework → utilities → sibling-directories → industry-state report in 12 months
- Solo author (no co-maintainers observed at scale)
- Commercial incentive aligned with ecosystem-growth incentive (glama.ai monetizes on MCP adoption)
- Positions as **neutral curator + active historian** of MCP ecosystem

## 2. 7-repo portfolio (GitHub API snapshot 2026-04-22)

| Repo | Stars | Role |
|------|-------|------|
| awesome-mcp-servers | 85,323 | Primary server directory |
| awesome-mcp-clients | 6,394 | Client directory (sister) |
| fastmcp | 3,054 | TypeScript framework for building MCP servers |
| pipenet | 484 | Localhost tunnel utility |
| awesome-mcp-devtools | 445 | Dev-tool directory |
| mcp-proxy | 251 | stdio↔HTTP/SSE transport proxy |
| mcp-ping | 7 | Host ping utility |

**Total:** ~95,958 stars across 7 repos. All MCP-focused.

**Distribution signal:** Directory layer dominates (~92K stars) while framework (~3K) and utilities (~742) serve as complements. Fiegel's **actual competitive moat = curation + directory authority**, not code.

## 3. Glama commercial platform surface

| Glama surface | URL | Role |
|---------------|-----|------|
| Glama Chat | glama.ai/chat | Multi-modal AI client with MCP support |
| MCP Servers directory | glama.ai/mcp/servers | Web UI synced with `awesome-mcp-servers` |
| MCP Clients directory | glama.ai/mcp/clients | Web UI synced with `awesome-mcp-clients` |
| Glama Blog | glama.ai/blog | Industry publications (State-of-MCP-2025) |

**Commercial stack characteristics:**
- All surfaces downstream of MCP ecosystem growth
- Curation revenue model: directory as lead-gen for Chat + hosted services
- No explicit paid tiers observed at probe-time; likely freemium OR enterprise-sales

## 4. Relationship to corpus patterns

### Pattern #17 Ecosystem-Layer Organizations (confirmed; refined v27 to 5-variant)

Pre-v31 5 variants:
1. Individual-led dev-ecosystem (Karpathy implicit; nextlevelbuilder explicit)
2. Big-tech curator (Anthropic/Vercel)
3. Commercial-startup ecosystem (VoltAgent)
4. Solo-brand ecosystem (safishamsi + penpax.ai)
5. Individual-multi-runtime-publisher (Yeachan + oh-my-claudecode + oh-my-codex)

**v31 Fiegel proposes variant 6 candidate:** *Solo-ecosystem-layer-with-commercial-platform*.

Distinguishing characteristics vs variant 4 (safishamsi):
- **Portfolio size:** Fiegel 7 repos vs safishamsi 1 primary + companion site
- **Commercial depth:** Glama multi-product platform vs penpax.ai single companion
- **Industry publications:** Fiegel produces State-of-MCP report; safishamsi does not

Distinguishing vs variant 5 (Yeachan):
- **Commercial companion:** Fiegel has Glama explicit; Yeachan has no commercial platform at v27 observation
- **Directory-role:** Fiegel curates multi-repo directory; Yeachan publishes frameworks only

**Audit recommendation at v31:** Document as Pattern #17 N=6 data point strengthening existing pattern; consider 6th variant tag at next formal audit. Do NOT register as new candidate (Pattern Library discipline).

### Pattern #50 Commercial-Funnel Companion Platform (candidate post-v25)

At v25: N=1 VoltAgent + getdesign.md.
At v31: **N=2 with Fiegel + Glama platform.**

Structurally-unambiguous promotion candidate: both are *commercial-funnel-via-companion-site-not-proprietary-tier* (distinct from Pattern #31 open-core proprietary-tier). Both wrap an OSS aggregator with a commercial platform. MIT/permissive licensing in both.

**Audit recommendation at v31:** Document as Pattern #50 strengthening to N=2 structurally-unambiguous. Consider promotion at next audit.

### Pattern #18 Agent Runtime Standardization (candidate)

Fiegel **IS the directory of the MCP runtime standard**. v31 strengthens Pattern #18 materially:
- MCP adoption is corpus-wide (6+ wikis reference MCP directly)
- awesome-mcp-servers 85K stars = community validation
- Fiegel's State-of-MCP-2025 report = ecosystem-historian framing confirms MCP as *the* standard

Recommendation: Pattern #18 approaches promotion criteria at v31. Audit should evaluate.

## 5. MCP-first advocate positioning

Fiegel's bio + company + all 7 repos = 100% MCP-aligned. **No hedging across protocols.** Contrast:
- Anthropic publishes MCP + competing APIs (Claude tool-use, Desktop integrations)
- LangChain bridges many protocols
- Fiegel = pure-play MCP bet

**Risk:** Protocol bifurcation. If MCP loses to alternative (Google A2A, OpenAI function-calling extensions, Apple-variant), Fiegel's stack unwinds. Current probability LOW — MCP has ~18 months of adoption momentum.

## 6. Timeline (Fiegel's MCP ecosystem build-out)

| Date | Milestone |
|------|-----------|
| 2022-06-28 | Fiegel creates GitHub account |
| 2024-Q4 | Anthropic releases MCP spec |
| **2024-11-30** | **awesome-mcp-servers created (Day-0/-1 concurrent with MCP spec)** |
| 2024-12-27 | fastmcp TypeScript framework |
| 2024-12-29 | mcp-proxy utility |
| 2025-01-11 | awesome-mcp-clients sibling directory |
| 2025-04-27 | awesome-mcp-devtools directory |
| 2025-06-09 | mcp-ping (minor) |
| 2025-12-07 | "The State of MCP in 2025" report published on Glama blog |
| 2026-01-19 | pipenet (localhost tunnel) |
| 2026-04-15 | Most recent push to awesome-mcp-servers |
| **2026-04-22** | **85,323 stars; #4 in Storm Bear corpus** |

## 7. Storm Bear relevance

**Direct actionable:** use `awesome-mcp-servers` as discovery input for Storm Bear Scrum-coach MCP tooling. Categories with highest utility:
- Product Management (Jira/Linear/Asana)
- Version Control (GitHub/GitLab)
- Communication (Slack/Discord/Teams)
- Workplace & Productivity (Google Workspace/Notion)
- Knowledge & Memory (vector stores for corpus search)

**Observational value:**
- Fiegel playbook (rapid-sequence + directory-first + commercial-companion) is **applicable model** if Storm Bear ever publishes awesome-vietnamese-scrum-resources or similar.
- Ecosystem-historian role (State-of-MCP) parallels Storm Bear's Pattern Library production methodology.

## 8. Risks / reservations

- **Bus factor 1:** Solo maintainer. If Fiegel is incapacitated, 85K-star community directory stalls. MIT + fork-cheap mitigates.
- **Commercial incentive drift:** Future Glama monetization pressures could bias curation (preferential Glama Chat listing, hidden fees for premium directory slots, etc.). Not observed currently.
- **Protocol-risk concentration:** 100% MCP bet. Hedge-free.
- **Supply-chain transitive risk:** Listing a server ≠ auditing it. Users must audit individually (Pattern #66).

## 9. Quotes (verbatim from README)

> "A curated list of awesome Model Context Protocol (MCP) servers."

> "MCP is an open protocol that enables AI models to securely interact with local and remote resources through standardized server implementations. This list focuses on production-ready and experimental MCP servers that extend AI capabilities through file access, database connections, API integrations, and other contextual services."

> "Read [The State of MCP in 2025](https://glama.ai/blog/2025-12-07-the-state-of-mcp-in-2025) report."

Fiegel's CONTRIBUTING-enshrined agent-PR governance:

> "If you are an automated agent, we have a streamlined process for merging agent PRs. Just add `🤖🤖🤖` to the end of the PR title to opt-in."

## 10. Cross-references

- **Pattern #17 ecosystem-layer individual/org peers:** [[(C) Cluster — punkpeye ecosystem + companion projects|Fiegel's 7-repo + Glama stack]] + [[03 Projects/awesome-design-md - Beginner Analysis/|VoltAgent v25]] + [[03 Projects/graphify - Beginner Analysis/|safishamsi v16]] + [[03 Projects/oh-my-claudecode - Beginner Analysis/|Yeachan v27]]
- **Pattern #50 commercial-funnel peer:** VoltAgent + getdesign.md v25
- **Pattern #18 MCP runtime peers:** OpenClaw (5+ wikis) + Hermes (3+ wikis)
- **MCP-consumer wiki cross-refs:** [[03 Projects/goclaw - Beginner Analysis/|goclaw v4]] / [[03 Projects/multica - Beginner Analysis/|multica v15]] / [[03 Projects/spec-kit - Beginner Analysis/|spec-kit v17]] / [[03 Projects/TrendRadar - Beginner Analysis/|TrendRadar v19]] / [[03 Projects/OpenHands - Beginner Analysis/|OpenHands v30]]

---

_Entity page. Part of Storm Bear LLM Wiki — 31st wiki. Written by Claude (C). Verified 2026-04-22._
