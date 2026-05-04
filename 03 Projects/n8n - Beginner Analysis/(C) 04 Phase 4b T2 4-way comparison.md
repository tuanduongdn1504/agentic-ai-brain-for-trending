# Phase 4b — T2 Agent-as-Service 4-Way Comparison (N=4)

> **Mode:** T2 tier extension to N=4 + 12-axis comparative analysis across goclaw v4 + multica v15 + ruflo v42 + n8n v56.
>
> **Why this mode chosen:** n8n is the 4th T2 entrant in the Storm Bear corpus. T2 was previously N=3; n8n extends to N=4 with EXTREME primitive count + 7-year operational maturity + bidirectional MCP corpus-first at T2 + custom-non-OSI license. This 4-way comparison surfaces sub-archetype divergence axes within T2 that inform Pattern #18 / #29 / #31 / #50 strengthening.

---

## T2 Agent-as-Service tier definition reminder

**T2 Agent-as-service:** Workflow automation OR multi-tenant agent platform with persistent server runtime + integration breadth + non-coding-agent primary use case (distinguishes from T1 Agent-as-assistant which is CLI/IDE coding-focused).

**Current T2 corpus members (N=4 post-v56):**

| Wiki | Subject | Date | Tier confirmation rationale |
|---|---|---|---|
| **v4** | goclaw (`goclaw/goclaw`) | 2026-04-17 | Workflow-automation-as-a-service prototype; Storm Bear v4 origin |
| **v15** | multica (`multica/multica`) | 2026-04-19 | Multi-channel agent service platform |
| **v42** | ruflo (`ruflo/ruflo`) | 2026-04-25 | Workflow-with-AI-overlay platform |
| **v56** | n8n (`n8n-io/n8n`) | 2026-04-27 | Mature workflow-automation + AI-overlay; 4th entrant |

---

## 12-axis comparison matrix

| Axis | goclaw v4 | multica v15 | ruflo v42 | **n8n v56** |
|---|---|---|---|---|
| **Tier** | T2 1st | T2 2nd | T2 3rd | **T2 4th** |
| **Archetype** | Storm-Bear-origin proto-platform | Multi-channel-agent-platform | Workflow-with-AI-overlay (emerging) | **German-mature-commercial-startup-with-SUL + bidirectional MCP** |
| **Scale tier** | Small (Storm-Bear-origin scale) | Medium 16.2K stars | Large 28K stars (per v42 entry) | **XXX-Large 185,728 stars (3rd in corpus)** |
| **Primary lang** | varied | TypeScript | TypeScript | **TypeScript** |
| **Packaging** | early experimental | npm + cloud | npm + Docker + commercial-tier | **npm + Docker + n8n.cloud + self-host + Docker Desktop (5+ surfaces)** |
| **Origin story** | Storm-Bear-internal v4 origin | Multica startup | Ruflo emerging-startup | **Solo-founder-CEO Jan Oberhauser + 7-year-mature German GmbH** |
| **Methodology** | early prototype | Multi-channel-orchestration | Workflow + AI overlay | **Workflow + 6 AI agent types + 16 LLM providers + 11 vector stores + 8 memory + bidirectional MCP** |
| **Governance** | Light | Medium | Medium-Heavy | **Medium-Heavy (1,580 open issues)** |
| **Agent/skill count** | Low | Medium | Large (per v42 EXTREME flag) | **EXTREME (400+ integrations + 6 agents + 16 LLM + 11 vector + 8 memory)** |
| **i18n** | EN-only | EN-primary | EN-primary | **EN-primary (multi-lang docs likely; not-yet-verified)** |
| **Intellectual influence** | Storm Bear lineage | None explicit | None explicit | **Workflow-automation lineage (Zapier 2011 → Make → n8n 2019)** |
| **Agent platforms** | Custom proto | OpenCode-adjacent | Custom + commercial integrations | **BIDIRECTIONAL MCP (Client + Server Trigger) corpus-first at T2** |

---

## Sub-archetype divergence within T2

### Maturity axis (operational age)

- goclaw v4: ~6 months at probe (Storm-Bear-origin emerging)
- multica v15: ~2 years at probe
- ruflo v42: ~1 year emerging at probe
- **n8n v56: ~7 years (most-mature T2 by 7×)**

**Observation:** n8n is the **most-mature T2 commercial entity in corpus by operational age**. T2 maturity range 0.5-7 years now spans 14× ratio.

### Scale axis (stars)

- goclaw v4: Small Storm-Bear-origin
- multica v15: 16.2K (Medium)
- ruflo v42: 28K (Large)
- **n8n v56: 185,728 (XXX-Large; 6× over ruflo at #2 T2 scale; 11× over multica at #3 T2 scale)**

**Observation:** n8n is the **T2 corpus scale-leader by ~6×**. T2 scale range now spans Storm-Bear-origin → 185K = 4 distinct order-of-magnitude tiers.

### License axis (commercial restriction)

- goclaw v4: MIT (permissive OSI)
- multica v15: Apache 2.0 (permissive OSI)
- ruflo v42: MIT (permissive OSI)
- **n8n v56: n8n SUL (source-available non-OSI custom-commercial-restriction)**

**Observation:** n8n is **first non-OSI license at T2**. This breaks the prior 3/3 OSI-permissive T2 baseline and surfaces Pattern #29 sub-context strengthening (custom-non-OSI-commercial-restriction now N=3 across T1 omo + T2 n8n + T5 GitNexus).

### MCP integration axis

- goclaw v4: Pre-MCP-era (MCP didn't exist at v4 origin)
- multica v15: MCP-aware (Pattern #18 layer 1 universal-protocol consumer)
- ruflo v42: MCP-supportive (per v42 entry)
- **n8n v56: BIDIRECTIONAL MCP (consume + provide — corpus-first at T2)**

**Observation:** n8n is the **first explicit MCP-Server-Trigger naming in 56-wiki corpus**. This is the strongest Pattern #18 evidence at T2 to date and elevates Pattern #18 Layer 0 horizontal-aggregation from N=1 (gh-aw v48) to N=2.

### Commercial-funnel axis

- goclaw v4: No commercial funnel (origin Storm Bear)
- multica v15: Multica commercial entity with funnel (per v15 entry)
- ruflo v42: Ruflo commercial entity with funnel (per v42 entry)
- **n8n v56: n8n.cloud companion managed SaaS (Pattern #50 50a Standard sub-variant)**

**Observation:** Commercial-funnel coverage at T2 is now N=3 (multica + ruflo + n8n with commercial cloud companions). Pattern #50 50a Standard sub-variant strengthens at T2.

---

## Cross-tier observations

### vs T1 Agent-as-assistant

T1 (e.g., Claude Code, Aider, GSD-1, GSD-2 v54) is CLI/IDE-tool-bound coding-agent archetype. n8n is workflow-automation-platform — orthogonal use case. T1 ↔ T2 boundary is well-defined: workflow-orchestration vs in-IDE coding-assistance.

n8n's MCP Client node CONSUMES T1 outputs (e.g., n8n workflow can call Claude Code as a tool via MCP). n8n's MCP Server Trigger node EXPOSES n8n workflows as tools for T1 to call (e.g., Claude Code can invoke n8n workflow via MCP). This bidirectionality blurs T1↔T2 in interesting ways.

### vs T4 Agent-as-bridge

T4 (e.g., gh-aw v48, ollama v46, claude-context v44, MCP-bridge tools) connects external systems to agents. n8n's 400+ integrations could be reframed as "T4 functionality embedded in T2 platform" — but n8n's persistent runtime + visual canvas + multi-tenant model places it firmly T2 not T4.

### vs T5 Agent-as-application

T5 (e.g., DeepTutor v40, MiroFish v49, Skyvern v24) are standalone autonomous applications. n8n is a platform, not an end-user app — distinguishes T2 from T5.

---

## Pattern Library impact summary

**Patterns strengthened by n8n v56 at T2:**

1. **Pattern #18 Agent Runtime Standardization** — STRONGEST T2 evidence; bidirectional MCP first-explicit; Layer 0 horizontal-aggregation N=2
2. **Pattern #28 Multi-Provider AI Support** — 16 native (no LiteLLM)
3. **Pattern #29 License-Category Diversity** — sub-context custom-non-OSI-commercial-restriction N=3 promotion-candidate
4. **Pattern #31 Open-Core Commercial Entity** — 11th data point with Pro-docs-depth axis depth 3-4 estimate
5. **Pattern #50 Commercial-Funnel Companion Platform** — 50a Standard sub-variant strengthening at T2
6. **Pattern #17 variant 3 commercial-startup ecosystem** — 7-year mature, OLDEST commercial-startup observation at this variant
7. **Pattern #2 Distribution Evolution** — 5+ surfaces
8. **Pattern #27 Community-Viral Scale Path** — sustained-mature-organic sub-path 185K/7yr ≈ 71/day
9. **Pattern #69 Primitive-count taxonomy** — 6th EXTREME-tier wiki
10. **Pattern #19 archetype 4** — solo-founder-CEO 7-year operational lineage
11. **Pattern #12 Governance-Depth refined v42 3-factor** — baseline-fits HOLDS at mature commercial-startup-with-1580-open-issues

**Counter-evidence:**
- Pattern #52 Extreme-Viral-Velocity STAYS STALE — n8n is sustained-not-burst
- Pattern #45 Dual-Licensing STAYS STALE — n8n is single-SUL not dual
- Pattern #72 PolyForm-Noncommercial STAYS STALE — n8n SUL is custom-different-from-PolyForm

**0 new standalone candidates** registered. **STREAK: 20-CONSECUTIVE-WIKI ZERO-NEW-ACTIVE-CANDIDATES** (NEW LONGEST extending v55 19-streak).

---

## T2 sub-taxonomy emerging at N=4

With 4 T2 data points, sub-archetype taxonomy starts to emerge:

| Sub-archetype | Members | Key axis |
|---|---|---|
| **T2a Storm-Bear-origin / experimental** | goclaw v4 | Internal vault origin |
| **T2b Multi-channel-agent-platform** | multica v15 | Multi-channel orchestration emphasis |
| **T2c Workflow-with-AI-overlay (emerging-startup)** | ruflo v42 | Emerging commercial startup with workflow + AI |
| **T2d Mature-commercial-workflow-platform-with-SUL** | n8n v56 | 7-year-mature commercial GmbH + bidirectional MCP + custom-non-OSI license |

**Note:** This sub-taxonomy is OBSERVATIONAL at v56. Promotion to formal Pattern #X T2-sub-archetype-taxonomy requires N=2 in each sub-cell — currently N=1 each at v56. Defer formal sub-archetype pattern-registration until N=2 emerges.

---

## Recommendations for next T2 wiki

If a 5th T2 entrant emerges in v57+, prioritize:

1. **Sub-archetype overlap check** — does it match T2a/T2b/T2c/T2d or open T2e?
2. **Bidirectional MCP check** — does it have MCP-Server-Trigger-equivalent? If yes, Pattern #18 N=3 at T2 → strong promotion-candidate
3. **License axis** — OSI-permissive, OSI-copyleft, or non-OSI-custom-restriction? Continues to inform Pattern #29 sub-context
4. **Maturity axis** — adds to T2 maturity-range (currently 0.5-7 years; 14× ratio)
