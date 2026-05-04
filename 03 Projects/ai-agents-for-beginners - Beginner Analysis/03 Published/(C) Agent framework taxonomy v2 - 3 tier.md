# (C) Agent Framework Taxonomy v2 — 3-Tier Model

> **Update to v4 taxonomy (`../../goclaw - Beginner Analysis/03 Published/(C) Agent framework taxonomy.md`)**
> v4 = 2-tier (Assistant + Service). v6 = **3-tier (Education + Assistant + Service)**.
> Emerged from 6-wiki corpus (v6 added ai-agents-for-beginners — first different-domain).
> 15-axis analysis extended.

---

## Tóm tắt / TL;DR

**Storm Bear vault sau 6 wikis nhận ra 3 tiers distinct cho agent ecosystem:**

| Tier | Purpose | Frameworks (n=6) | Verb |
|------|---------|------------------|------|
| **Tier 3: Agent-as-education** | Teach concepts | ai-agents-for-beginners (1) | **Learn** |
| **Tier 1: Agent-as-assistant** | Tool dev uses daily | ECC, Superpowers, gstack, GSD (4) | **Use** |
| **Tier 2: Agent-as-service** | Platform deploying agents | goclaw (1) | **Deploy** |

**Progression:** Learn (T3) → Use (T1) → Deploy (T2).

**Unique insight from N=6:** Tiers are **complementary, not competitive**. Serious agent practitioner touches all 3 tiers over career arc.

---

## Part 1 — Why 3-tier model beats 2-tier

### v4 2-tier model (from goclaw wiki)

- Tier 1: agent-as-assistant (ECC/Superpowers/gstack)
- Tier 2: agent-as-service (goclaw)

**Limitation observed during v6 pre-flight:** ai-agents-for-beginners doesn't fit either tier. It's neither an assistant nor a service — **it's a curriculum**. Education purpose.

### v6 3-tier model

Added Tier 3: agent-as-education.

**Test:** Place each of 6 corpus items:

| Item | Fit Tier 1? | Fit Tier 2? | Fit Tier 3? |
|------|-------------|-------------|-------------|
| ECC | ✅ | ❌ | ❌ |
| Superpowers | ✅ | ❌ | ❌ |
| gstack | ✅ | ❌ | ❌ |
| GSD | ✅ | ❌ | ❌ |
| goclaw | ❌ | ✅ | ❌ |
| ai-agents-for-beginners | ❌ | ❌ | ✅ |

→ **Clean partition. 3-tier sufficient for current corpus.**

### When would 4-tier emerge?

Potential Tier 4 candidates từ future wikis:
- **Tier 4a: Agent-as-infrastructure** — pure protocol/SDK (Anthropic Agent SDK raw, MCP spec)
- **Tier 4b: Agent-as-research** — academic/experimental (Microsoft Research projects, lab tools)

Monitor for 4-tier upgrade signal.

---

## Part 2 — 3 Tiers detailed

### Tier 3: Agent-as-education

**Purpose:** Teach concepts, frameworks, patterns at conceptual level.

**Consumer verb:** *Learn*

**Characteristics:**
- Curriculum structure (lessons, not reference docs)
- Linear progression (lesson 1 → N)
- Code samples optimized for learnability, not production
- Vendor-backed (Microsoft, eventually others)
- Free or low-cost access
- Community via learning channels (Discord, forums)

**Current entrants:**
- ai-agents-for-beginners (Microsoft) — 1 in corpus

**Potential future entrants:**
- LangChain Academy
- DeepLearning.AI short courses (agents track)
- Anthropic courses
- Coursera/Udemy agent-specific courses

**Emergence condition:** Tier 3 multi-entrant when 2+ educational resources published.

### Tier 1: Agent-as-assistant

**Purpose:** Tool that individual dev uses daily to accelerate coding.

**Consumer verb:** *Use*

**Characteristics:**
- Reference docs (not lessons)
- Non-linear access (pick what you need)
- Production-grade code samples
- Community-driven or vendor-driven
- Variable cost (free to paid tiers)
- CLI + IDE integrations primary

**Current entrants:** ECC, Superpowers, gstack, GSD (4)

**4-way comparison already built** trong v5 `get-shit-done` wiki. See [[../../../get-shit-done - Beginner Analysis/03 Published/(C) Tier 1 4-way comparison]].

### Tier 2: Agent-as-service

**Purpose:** Platform that deploys agents as service to users/tenants.

**Consumer verb:** *Deploy*

**Characteristics:**
- Platform docs + APIs
- Multi-tenant architecture concerns
- Production hardening (auth, quotas, observability, SLA)
- Vendor-backed or OSS platform
- Paid or self-hosted cost model
- Web/API primary (CLI secondary)

**Current entrants:** goclaw (1)

**Potential future entrants:**
- AutoGen Studio (when platform-ized)
- LangGraph Platform
- Microsoft Agent Service (enterprise deployment)
- Azure AI Agent Service (though partially fits)
- E2B (agent sandboxes)

---

## Part 3 — Cross-tier relationships

### Education → Assistant progression

Course teaches concept → user picks Tier 1 tool implementing concept.

**Mapping table:**

| Concept (Tier 3 lesson) | Tier 1 implementation |
|------------------------|----------------------|
| L01 (7 agent types) | All siblings = Hierarchical |
| L03 (design patterns) | ECC skill format, gstack roles |
| L05 (Agentic RAG) | goclaw Knowledge Vault (but Tier 2) |
| L08 (multi-agent) | gstack specialists, GSD 33 agents |
| L11 (MCP) | ECC/Superpowers/gstack/GSD all integrate |
| L12 (context engineering) | GSD "context rot solution" |

→ **Every Tier 3 lesson has Tier 1 implementation.** Course = shared vocabulary.

### Assistant → Service progression

User masters Tier 1 tool → needs to serve multiple users → adopts Tier 2 platform.

**Natural progression path:**

1. Solo dev uses ECC/Superpowers/gstack/GSD daily (Tier 1)
2. Team needs shared agent workflow → still Tier 1 (with plugin sharing)
3. Team needs to ship agent-as-product → adopts goclaw or equivalent (Tier 2)

### Direct Education → Service?

Possible but unusual. Typically:
- Enterprise teams skip Tier 1 exploration, go straight to Azure AI Agent Service (Tier 2 Microsoft)
- But this assumes learners already have Tier 1 mental model via Tier 3 course

---

## Part 4 — 15-axis analysis (extended from v3 + v4)

| Axis | Tier 3 (ai-agents-for-beginners) | Tier 1 (ECC/SP/gstack/GSD) | Tier 2 (goclaw) |
|------|----------------------------------|----------------------------|-----------------|
| **Purpose** | Learn | Use | Deploy |
| **Target user** | Developer learner | Individual dev | Platform operator |
| **Scale** | 1 learner | 1-10 devs | 10-10,000 users |
| **Format** | Curriculum | Tool + docs | Platform + APIs |
| **Code quality** | Learnability-optimized | Production | Production hardened |
| **Sequencing** | Linear (L1→N) | Non-linear (pick) | Platform-dependent |
| **Cost** | Free (GitHub Models tier) | Free-to-paid | Platform cost + infra |
| **Community** | Discord (learning) | Discord/Slack (users) | Enterprise/self-hosted |
| **Vendor** | Microsoft | Mixed | Solo dev (goclaw) |
| **Language** | Multi (50+) | English-first mostly | Multi (Vi + i18n catalog) |
| **Distribution** | Git clone | npm/git/setup script | Docker/binary |
| **Outcome** | Knowledge gained | Code shipped | Service deployed |
| **Multi-tenant?** | N/A | No (single user) | Yes |
| **Learnability** | High (teaches) | Medium (docs) | Low (platform complexity) |
| **Commitment** | 2-4 weeks curriculum | 1-2 weeks per tool | Months for deployment |

---

## Part 5 — 3 emergent patterns unique to 3-tier view

### Pattern 1: Purpose → Format correlation

| Purpose (Tier) | Format |
|----------------|--------|
| Learn (T3) | Curriculum (ordered lessons) |
| Use (T1) | Reference docs (indexed commands) |
| Deploy (T2) | Platform + API specs |

→ **Format serves purpose.** Mixing = UX failure. Don't treat Tier 1 tool as curriculum (user overwhelmed by docs); don't treat Tier 3 course as reference (user can't find specific answer quickly).

### Pattern 2: Vendor consolidation increases with Tier

- **Tier 3:** Vendor-backed (Microsoft) — Tier 3 requires resources for curriculum production
- **Tier 1:** Mixed (vendor Anthropic for ECC, solo for Superpowers/gstack/GSD)
- **Tier 2:** Mixed (vendor Microsoft/Azure for MAF, solo for goclaw)

**Pattern:** Vendor commitment correlates với investment required. Tier 3 curriculum = high upfront cost, needs well-resourced backer. Tier 1 tool = individual dev can ship. Tier 2 platform = either extreme (vendor enterprise or ambitious solo).

### Pattern 3: Learning progression is **recursive**

User at Tier 1 mastery → realizes needs **more concepts** (returns to Tier 3)
User at Tier 2 deployment → realizes needs **better tooling** (returns to Tier 1)

→ **Tiers aren't stages to leave behind.** Advanced practitioner oscillates. 3-tier = stack, not ladder.

---

## Part 6 — Practical usage by persona

### Persona 1: Complete beginner (0 agent experience)

**Path:** Tier 3 (4 weeks) → Tier 1 (pick 1 tool, 2 weeks) → revisit Tier 3 for depth

**Start with:** ai-agents-for-beginners lessons 01-10 linearly

### Persona 2: Experienced dev, no agent experience

**Path:** Tier 3 skim (5 days) → Tier 1 (master 1 tool, 1 week) → evaluate Tier 2 as needed

**Skim Tier 3:** lessons 01, 03, 08, 11, 12

### Persona 3: Agent practitioner, expanding capability

**Path:** Tier 1 second tool (compare với first) → Tier 2 evaluation → Tier 3 advanced lessons (09, 14)

**Focus:** breadth at Tier 1, then Tier 2 for platform needs

### Persona 4: Team lead introducing AI agents to team

**Path:** Tier 3 team-read (week 1) → standardize on 1 Tier 1 tool (week 2-4) → Tier 2 plan when team grows

**Collaboration:** shared curriculum → shared tool → shared platform

### Persona 5: Platform builder

**Path:** Tier 2 direct study → Tier 1 + Tier 3 as needed for specific gaps

**Focus:** goclaw (Tier 2) patterns + lessons 10+14 (production + MAF)

### Persona 6: Storm Bear vault operator (Cvtot)

**Path:** Already used Tier 1 (5 frameworks), Tier 3 (this course), Tier 2 (goclaw surveyed)

**Next:** **Pilot Tier 1 tool trong real project**, complete cycle Learn→Use→Deploy

### Persona 7: VN developer community

**Path:** Tier 3 VN translation (already exists) → Tier 1 via Storm Bear vault wikis (VN-accessible)

**Storm Bear contribution:** wiki layer = accelerator for VN devs skipping English-only barriers

---

## Part 7 — Integration patterns

### Pattern A: Education + Assistant pair

Team uses ai-agents-for-beginners (Tier 3) + ECC (Tier 1) together:
- Morning: team reads lesson
- Afternoon: apply với ECC workflow
- Weekly: team discusses concept → tool mapping

### Pattern B: Education + Service pair

Enterprise trains team via Tier 3 course, deploys via goclaw (Tier 2):
- Week 1-3: team course completion
- Week 4-6: goclaw platform setup
- Ongoing: team operates goclaw with concept understanding

### Pattern C: Assistant + Service pair

Individual dev masters Tier 1 tool (e.g., GSD) → platformizes workflow via Tier 2 (goclaw):
- Personal: GSD daily
- Team product: goclaw-hosted agents
- Transfer: individual patterns → platform templates

### Pattern D: Full stack (3-tier)

Full progression:
- Learn (Tier 3 course)
- Use (Tier 1 daily tool)
- Deploy (Tier 2 platform for product)

→ **Most complete practitioner path.** Takes 3-6 months.

---

## Part 8 — Storm Bear vault implications

### v6 milestones unlocked

- ✅ **Tier 3 slot filled** (ai-agents-for-beginners = first Tier 3 entrant)
- ✅ **3-tier taxonomy defensible** — 6 data points across 3 tiers
- ✅ **Different-domain generalization proven** — routine handled non-dev-tool wiki
- ✅ **VN market signal repeated** — 2 of 6 wikis have native VN (course + goclaw)

### Taxonomy health

**v4 2-tier was under-specified.** v6 3-tier = better fit for corpus.
Future monitoring:
- 2nd Tier 3 entrant → validates Tier 3 multi-entrant
- 2nd Tier 2 entrant → validates Tier 2 multi-entrant
- Tier 4 emergence signal → watch for "infrastructure" or "research" tier

### Storm Bear decision framework

**Når user asks "học AI Agents starting from zero":**
→ Route to Tier 3 (ai-agents-for-beginners)

**Når user asks "pick a Claude-integrated tool":**
→ Route to Tier 1 4-way comparison (from v5 GSD wiki)

**Når user asks "deploy agent service":**
→ Route to Tier 2 goclaw wiki

**Når user asks "compare tiers / which tier":**
→ Route to this taxonomy v2 doc

---

## Part 9 — Compare v4 → v6 evolution

| Axis | v4 taxonomy (2-tier) | v6 taxonomy (3-tier) |
|------|----------------------|----------------------|
| Tiers | 2 | 3 |
| Coverage | Tool + Service | Learn + Tool + Service |
| Corpus at time | 4 (3 T1 + 1 T2) | 6 (4 T1 + 1 T2 + 1 T3) |
| Emergence trigger | Adjacent domain (goclaw) | Different domain (course) |
| Reframe vs extend? | Extend (added Tier 2) | Extend (added Tier 3) |
| Completeness | Partial (education gap) | Complete for corpus (?) |

**Hypothesis:** v7 taxonomy will emerge at N=8-10 unless stays at 3-tier stable.

---

## References

- v4 taxonomy (2-tier): `../../goclaw - Beginner Analysis/03 Published/(C) Agent framework taxonomy.md`
- v5 Tier 1 4-way: `../../get-shit-done - Beginner Analysis/03 Published/(C) Tier 1 4-way comparison.md`
- Beginner guide: [[(C) AI Agents for Beginners - Huong dan cho nguoi moi]]
- Entity pages this wiki:
  - [[../02 Wiki/(C) Agent Design Patterns]]
  - [[../02 Wiki/(C) Agentic RAG]]
  - [[../02 Wiki/(C) Multi-Agent Systems]]
  - [[../02 Wiki/(C) Agentic Protocols (MCP + A2A + NLWeb)]]
- Sibling wikis:
  - `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) index.md`
  - `../../Superpowers - Beginner Analysis/02 Wiki/(C) index.md`
  - `../../gstack - Beginner Analysis/02 Wiki/(C) index.md`
  - `../../get-shit-done - Beginner Analysis/02 Wiki/(C) index.md`
  - `../../goclaw - Beginner Analysis/02 Wiki/(C) index.md`
- Routine: `../../../05 Skills/llm-wiki-routine.md`
