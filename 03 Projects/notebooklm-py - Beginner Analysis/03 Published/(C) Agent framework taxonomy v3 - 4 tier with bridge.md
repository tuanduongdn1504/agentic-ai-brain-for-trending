# (C) Agent Framework Taxonomy v3 — 4-Tier Model (with Bridge)

> **Update to v6 taxonomy** (`../../ai-agents-for-beginners - Beginner Analysis/03 Published/(C) Agent framework taxonomy v2 - 3 tier.md`)
> v4 (2-tier) → v6 (3-tier) → **v7 (4-tier with Bridge)**
> Emerged từ 7-wiki corpus (v7 added notebooklm-py — second different-domain).
> 18-axis analysis extended.

---

## Tóm tắt / TL;DR

**Storm Bear vault sau 7 wikis nhận ra 4 tiers distinct cho agent ecosystem:**

| Tier | Purpose | Frameworks (n=7) | Verb |
|------|---------|------------------|------|
| **Tier 3: Agent-as-education** | Teach concepts | ai-agents-for-beginners (1) | **Learn** |
| **Tier 1: Agent-as-assistant** | Tool dev uses daily | ECC, Superpowers, gstack, GSD (4) | **Use** |
| **Tier 2: Agent-as-service** | Platform deploying agents | goclaw (1) | **Deploy** |
| **Tier 4: Agent-as-bridge** (**NEW v7**) | Library connects agent to external service | notebooklm-py (1) | **Integrate** |

**Progression:** Learn (T3) → Use (T1) → [Integrate (T4)] → Deploy (T2).

**Unique insight from N=7:** Bridge/connector (T4) is **orthogonal** to assistant/service/education axis. Bridges get installed INTO Tier 1 tools OR Tier 2 platforms. May also be cross-cutting axis, not strict tier.

---

## Part 1 — Why 4-tier model extends 3-tier

### v6 3-tier model

- Tier 3: agent-as-education (learn)
- Tier 1: agent-as-assistant (use)
- Tier 2: agent-as-service (deploy)

**Limitation observed during v7 pre-flight:** notebooklm-py doesn't fit any of 3 tiers cleanly.
- Not education (doesn't teach concepts)
- Not assistant (doesn't BE an agent)
- Not service (doesn't host agents)
- **Is a library that agents IMPORT to connect to external service.**

### v7 4-tier model: "Agent-as-bridge"

**Definition Tier 4:** A library, skill, or connector that **bridges** an AI agent to an external service (SaaS API, proprietary tool, hardware, etc.) without BEING the agent itself.

**Core traits:**
- Provides **skill + CLI + library** for specific service
- Agents (Tier 1) install + invoke
- Platforms (Tier 2) can embed
- Not standalone usable without host agent

**Test:** Place each of 7 corpus items:

| Item | Fit T1? | Fit T2? | Fit T3? | Fit T4? |
|------|---------|---------|---------|---------|
| ECC | ✅ | ❌ | ❌ | ❌ |
| Superpowers | ✅ | ❌ | ❌ | ❌ |
| gstack | ✅ | ❌ | ❌ | ❌ |
| GSD | ✅ | ❌ | ❌ | ❌ |
| goclaw | ❌ | ✅ | ❌ | ❌ |
| ai-agents-for-beginners | ❌ | ❌ | ✅ | ❌ |
| **notebooklm-py** | **❌** | **❌** | **❌** | **✅** |

→ **Clean partition. 4-tier sufficient for current corpus.**

### Alternative model: cross-cutting axis

**Could Tier 4 instead be a 2D axis overlaid on T1/T2/T3?**

```
          Tier 3 (Learn)
               |
               |
T4 Bridge ─────┼───── T1 Assistant
               |
               |
          Tier 2 (Deploy)
```

Any T1/T2 entrant can adopt any T4 bridge. Bridge not standalone.

**Verdict:** Both models work. **4-tier** simpler cho classification. **Cross-cutting axis** clearer cho operational relationship. Document both; use 4-tier for naming, cross-cutting for usage diagrams.

### When would 5-tier emerge?

Potential Tier 5 candidates from future wikis:

- **Tier 5a: Agent-as-infrastructure** — pure protocol/SDK (MCP spec, Anthropic Agent SDK)
- **Tier 5b: Agent-as-research** — academic/experimental
- **Tier 5c: Agent-as-evaluation** — testing/benchmark frameworks (GAIA, HumanAgentBench)

Monitor for 5-tier upgrade signal.

---

## Part 2 — 4 Tiers detailed (updated for v7)

### Tier 3: Agent-as-education (unchanged from v6)

**Purpose:** Teach concepts, frameworks, patterns at conceptual level.
**Consumer verb:** *Learn*
**Current entrants:** ai-agents-for-beginners (1)

### Tier 1: Agent-as-assistant (unchanged from v4)

**Purpose:** Tool individual dev uses daily to accelerate coding.
**Consumer verb:** *Use*
**Current entrants:** ECC, Superpowers, gstack, GSD (4)

### Tier 2: Agent-as-service (unchanged from v4)

**Purpose:** Platform deploying agents as service to users/tenants.
**Consumer verb:** *Deploy*
**Current entrants:** goclaw (1)

### Tier 4: Agent-as-bridge (NEW v7)

**Purpose:** Library connecting agent to external service (SaaS, proprietary tool, hardware).

**Consumer verb:** *Integrate*

**Characteristics:**
- Library + CLI + Skill triple package
- Wraps external service's API (often unofficial/undocumented)
- Agent (T1) installs as skill, invokes operations
- Value = unlock service features not in web UI + automation + composability
- Not standalone — requires host agent + external service subscription

**Current entrants:** notebooklm-py (1)

**Potential future entrants:**
- `linear-py` (Linear issue tracker bridge)
- `slack-py-skill` (Slack workspace bridge)
- `github-skill` (enhanced beyond official MCP)
- `figma-py-skill` (Figma design bridge)
- `salesforce-py-skill`
- MCP servers (may be T4 or T5-infrastructure — edge case)

**Emergence condition:** Tier 4 multi-entrant when 2+ bridge libraries published.

---

## Part 3 — Cross-tier relationships (updated)

### Education → Assistant progression (unchanged)

Course teaches concept → user picks Tier 1 tool implementing concept.

### Assistant → Bridge adoption (new v7)

Tier 1 user discovers need for external service → adopts Tier 4 bridge.

**Example:** Claude Code user (T1 ECC) needs NotebookLM automation → installs notebooklm-py (T4).

### Assistant → Service progression (unchanged)

User masters Tier 1 tool → needs multi-user deployment → adopts Tier 2 platform.

### Service → Bridge embedding (new v7)

Tier 2 platform could bundle Tier 4 bridges as per-tenant skills.

**Example:** goclaw deployment could include notebooklm-py skill in default agent bundle.

### Direct Bridge use (new v7)

Advanced users skip Tier 1, use Bridge CLI directly via shell script.

**Example:** Researcher writes bash cron job invoking `notebooklm` CLI without agent involvement.

---

## Part 4 — 18-axis analysis (extended from v6 15-axis)

| Axis | Tier 3 (course) | Tier 1 (tools) | Tier 2 (platform) | **Tier 4 (bridge)** |
|------|-----------------|----------------|-------------------|---------------------|
| **Purpose** | Learn | Use | Deploy | **Integrate** |
| **Target user** | Learner | Individual dev | Operator | **Agent user** |
| **Scale** | 1 learner | 1-10 devs | 10-10,000 users | **Per-integration** |
| **Format** | Curriculum | Tool + docs | Platform + APIs | **Library + Skill** |
| **Code quality** | Learnability | Production | Hardened | **Production** |
| **Sequencing** | Linear | Non-linear | Platform-dep | **On-demand** |
| **Cost** | Free | Free-to-paid | Platform + infra | **External service cost** |
| **Community** | Discord | Varies | Enterprise | **Service-specific** |
| **Vendor** | Microsoft | Mixed | Mixed | **Solo often** |
| **Language** | Multi 50+ | English-first | Multi | **English-first** |
| **Distribution** | Git clone | npm/git/setup | Docker/binary | **pip/npm + CLI skill install** |
| **Outcome** | Knowledge | Code shipped | Service live | **Automation enabled** |
| **Multi-tenant?** | N/A | No | Yes | N/A (per-agent) |
| **Learnability** | High | Medium | Low | **Medium (CLI)** |
| **Commitment** | 2-4 weeks | 1-2 weeks | Months | **Days to adopt** |
| **Standalone use?** | Yes | Yes | Yes | **No (needs agent or service)** |
| **External dependency** | None | None | None | **Hard (service API)** |
| **Maintenance fragility** | Low | Medium | Medium | **High (unofficial APIs)** |

---

## Part 5 — 4 emergent patterns unique to 4-tier view (extended)

### Pattern 1: Purpose → Format correlation (from v6, validated)

| Purpose (Tier) | Format |
|----------------|--------|
| Learn (T3) | Curriculum (ordered lessons) |
| Use (T1) | Reference docs (indexed commands) |
| Deploy (T2) | Platform + API specs |
| **Integrate (T4)** | **Library + CLI + Skill triple** |

**v7 addition:** T4's format = triple-surface design. Most other tiers = single-surface.

### Pattern 2: Vendor consolidation vs solo maintainer (updated)

| Tier | Vendor-backed? | Solo-maintained? |
|------|----------------|------------------|
| T3 (education) | Yes (Microsoft) | No |
| T1 (assistant) | Mixed (Anthropic ECC; solo SP/gstack/GSD) | Half |
| T2 (service) | Mixed (MAF; solo goclaw) | Half |
| **T4 (bridge)** | **Solo often (bus factor = 1)** | **Yes** |

**Pattern:** T4 maintenance risk is systematically highest. Bridge maintainers work alone, face fragile APIs, drop frequently. Warning for adopters.

### Pattern 3: Learning progression is recursive (from v6, validated)

Advanced practitioners oscillate between tiers. v7 adds: **T4 adoption waves follow T1 growth** — each new T1 tool → users want same integrations in new tool → T4 libraries port across T1 tools.

### Pattern 4: Orthogonality of T4 (new v7)

T4 bridges are **orthogonal** to T1/T2/T3:
- Any T1 agent can install any T4 bridge
- Any T2 platform can embed any T4 bridge
- T3 course can teach about any T4 bridge type

→ **T4 = "plugin ecosystem axis"**, even though we call it a tier for simplicity.

---

## Part 6 — Practical usage by persona (extended)

### Persona 1: Complete beginner
**Path:** T3 (4 weeks) → T1 (pick tool) → T4 adopt as needed → T3 revisit

### Persona 2: Experienced dev, no agent experience
**Path:** T3 skim → T1 (master 1 tool) → T4 bridges for daily workflows → T2 if product needs

### Persona 3: Agent practitioner, expanding capability
**Path:** T1 second tool → **T4 bridges for service integrations** → T2 for scale

**v7 change:** T4 integrated earlier — once T1 tool mastered, T4 bridges deliver immediate productivity.

### Persona 4: Team lead
**Path:** T3 team-read → T1 standardize → **T4 bridges for team's services** → T2 when scale

**v7 change:** T4 = team workflow accelerator. Standardize T4 bridge list alongside T1 tool.

### Persona 5: Platform builder
**Path:** T2 direct study → T1/T3/**T4 as needed**

**v7 change:** Platform bundles **T4 bridges**. Tenants choose bundle.

### Persona 6: Storm Bear vault operator (Cvtot)
**Path:** Already T1 (5 frameworks), T3 (course), T2 (goclaw surveyed), **T4 (notebooklm-py)**

**Next (unchanged):** Pilot T1 tool trên real project; optionally add **T4 bridge** for podcast workflow.

### Persona 7: VN developer community
**Path:** T3 VN translation → T1 via Storm Bear wikis → **T4 bridges adapted cho VN context**

**v7 addition:** Storm Bear contributes T4 VN documentation/translation.

### Persona 8 (NEW v7): External service power user
**Path:** Start with T4 bridge directly (e.g., researcher adopts notebooklm-py standalone via CLI) → gradually adopt T1 tool for agent experience

---

## Part 7 — Integration patterns (extended)

### Pattern A: Education + Assistant (unchanged)
Team uses course + ECC together.

### Pattern B: Education + Service (unchanged)
Enterprise trains team via course, deploys via goclaw.

### Pattern C: Assistant + Service (unchanged)
Individual masters T1 → platformizes via T2.

### Pattern D: Full stack 3-tier (unchanged)
Learn → Use → Deploy.

### Pattern E (NEW v7): Assistant + Bridge
Dev uses Claude Code (T1) + notebooklm-py (T4) for research automation.

### Pattern F (NEW v7): Service + Bridge bundle
goclaw deployment bundles multiple T4 bridges as default per-tenant agent skills.

### Pattern G (NEW v7): Full stack 4-tier
Learn (T3) → Use (T1) → Integrate (T4) → Deploy (T2).

**Most complete practitioner path.** 6-12 months.

---

## Part 8 — Storm Bear vault implications

### v7 milestones unlocked

- ✅ **Tier 4 slot identified** (notebooklm-py = first T4 entrant)
- ✅ **4-tier taxonomy defensible** — 7 data points across 4 tiers
- ✅ **Orthogonality pattern observed** — T4 plugs into T1/T2
- ✅ **Bridge maintainer risk pattern** — T4 systematically solo-maintained

### Taxonomy health

**v7 4-tier = accurate cho current corpus.** Waiting for second T4 entrant to validate multi-entrant tier.

Future monitoring:
- 2nd T4 entrant → validates Tier 4 multi-entrant (watch Linear/Slack/GitHub bridges)
- 2nd T3 entrant → validates Tier 3 (LangChain Academy, DeepLearning.AI)
- Tier 5 emergence → infrastructure/research/evaluation tier

### Storm Bear decision framework

**When user asks "integrate NotebookLM":**
→ Route to T4 (notebooklm-py)

**When user asks "integrate [other service]":**
→ Check T4 bridges; if absent, flag as contribution opportunity

**When user asks "compare tiers / which tier":**
→ Route to THIS v7 taxonomy doc

---

## Part 9 — Compare v6 → v7 evolution

| Axis | v6 taxonomy (3-tier) | v7 taxonomy (4-tier) |
|------|----------------------|----------------------|
| Tiers | 3 | 4 |
| Coverage | Learn + Tool + Service | Learn + Tool + Bridge + Service |
| Corpus at time | 6 (4 T1 + 1 T2 + 1 T3) | 7 (4 T1 + 1 T2 + 1 T3 + 1 T4) |
| Emergence trigger | Different domain (course) | Different domain (bridge lib) |
| Reframe vs extend? | Extended (added T3) | Extended (added T4) |
| Orthogonality | Linear tiers | **T4 orthogonal** |
| Risk tracking | Framework maintenance | + **T4 bridge bus factor** |

**Hypothesis:** v8 will emerge at N=9-12. Possibilities:
- Tier 5 "infrastructure" (MCP spec, SDK raw)
- Sub-tier split (T1 becomes T1a-assistant + T1b-framework)
- Cross-cutting axis formalization (T4 + potential "deployment model" axis)

---

## Part 10 — Orthogonality formalization

### Tier 4 as plugin axis

```
            Tier 3 (Learn)
              education
                  ┃
                  ┃
[Tier 4 Bridges]━━╋━━[Tier 1/2 Hosts]
  notebooklm-py   ┃    ECC, Superpowers,
  (future: Linear, ┃    gstack, GSD (T1)
   Slack, GitHub,  ┃    goclaw (T2)
   Figma bridges) ┃
                  ┃
            Tier 2 (Deploy)
              service
```

**Readings:**
- T1/T2/T3 = **what kind of thing**
- T4 = **what extends/augments T1-T2**

### Bridge-host compatibility matrix

| Bridge | Compatible hosts |
|--------|------------------|
| notebooklm-py | Claude Code (T1 ECC), Codex, OpenClaw (T1 class), goclaw (T2 embed) |

Future T4 entrants likely same pattern: works with any T1 + embeddable in T2.

---

## References

- v4 taxonomy (2-tier): `../../goclaw - Beginner Analysis/03 Published/(C) Agent framework taxonomy.md`
- v6 taxonomy (3-tier): `../../ai-agents-for-beginners - Beginner Analysis/03 Published/(C) Agent framework taxonomy v2 - 3 tier.md`
- v5 Tier 1 4-way: `../../get-shit-done - Beginner Analysis/03 Published/(C) Tier 1 4-way comparison.md`
- Beginner guide: [[(C) notebooklm-py - Huong dan cho nguoi moi]]
- Entity pages this wiki:
  - [[../02 Wiki/(C) CLI Surface]]
  - [[../02 Wiki/(C) Python API Architecture]]
  - [[../02 Wiki/(C) Skill Integration (Claude Code + Codex + OpenClaw)]]
  - [[../02 Wiki/(C) Web-UI-Exclusive Capabilities]]
- Sibling wikis (all 6):
  - `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) index.md` (T1)
  - `../../Superpowers - Beginner Analysis/02 Wiki/(C) index.md` (T1)
  - `../../gstack - Beginner Analysis/02 Wiki/(C) index.md` (T1)
  - `../../get-shit-done - Beginner Analysis/02 Wiki/(C) index.md` (T1)
  - `../../goclaw - Beginner Analysis/02 Wiki/(C) index.md` (T2)
  - `../../ai-agents-for-beginners - Beginner Analysis/02 Wiki/(C) index.md` (T3)
- Routine: `../../../05 Skills/llm-wiki-routine.md`
