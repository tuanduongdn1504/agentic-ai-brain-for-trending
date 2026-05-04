# (C) Agent Framework Taxonomy v4 — 5-Tier Model (with Application)

> **Update to v7 4-tier taxonomy** (`../../notebooklm-py - Beginner Analysis/03 Published/(C) Agent framework taxonomy v3 - 4 tier with bridge.md`)
> Evolution: v4 (2-tier) → v6 (3-tier) → v7 (4-tier + orthogonality) → **v9 (5-tier + application)**
> Emerged từ 9-wiki corpus (v9 added deer-flow — third different-domain).
> 20-axis analysis.

---

## Tóm tắt / TL;DR

**Storm Bear vault sau 9 wikis nhận ra 5 tiers distinct cho agent ecosystem:**

| Tier | Purpose | Frameworks (n=9) | Verb |
|------|---------|------------------|------|
| **T3: Agent-as-education** | Teach concepts | ai-agents-for-beginners (1) | **Learn** |
| **T1: Agent-as-assistant** | Tool dev uses daily (Claude Code plug-in) | ECC, Superpowers, gstack, GSD (4) | **Use** |
| **T4: Agent-as-bridge** | Library connects agent to external service | notebooklm-py (1) | **Integrate** |
| **T5: Agent-as-application** (**NEW v9**) | **Standalone autonomous agent app** | **deer-flow (1)** | **Run** |
| **T2: Agent-as-service** | Multi-tenant platform hosting agents | goclaw (1) | **Deploy** |
| Outside scope | Meta-reference / aggregator | build-your-own-x (1) | — |

**9-wiki clean partition across 5 tiers + 1 outside-scope.**

**Progression:** Learn (T3) → Use (T1) → Integrate (T4) → Run (T5) → Deploy (T2).

**Key distinction T5 vs T2:**
- T5 = run YOUR autonomous agent (single-tenant, standalone)
- T2 = deploy agents AS service for tenants (multi-tenant platform)

---

## Part 1 — Why T5 extension needed

### v7 4-tier limitation observed during v9 pre-flight

deer-flow doesn't fit v7 4-tier cleanly:
- Not T1 assistant (not Claude Code plug-in; standalone app)
- Not T2 service (not multi-tenant; single-tenant autonomous)
- Not T3 education
- Not T4 bridge (bridges a service; deer-flow runs autonomously doing things)

deer-flow represents **Devin/AutoGPT/OpenHands category** — standalone autonomous agent apps.

### Tier 5 "Agent-as-application" definition

A **self-contained autonomous agent harness** that:
- Runs as standalone application (has own UI, own backend, own infrastructure)
- Executes long-horizon autonomous tasks (minutes-hours)
- User submits goal, app pursues autonomously
- Not a Claude Code plug-in (distinct from T1)
- Not multi-tenant SaaS (distinct from T2)
- Not a library imported by agents (distinct from T4)

### Test: place 9 corpus items

| Item | T1? | T2? | T3? | T4? | T5? | Outside? |
|------|-----|-----|-----|-----|-----|----------|
| ECC | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Superpowers | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| gstack | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| GSD | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| goclaw | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| course | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| notebooklm-py | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| **deer-flow** | **❌** | **❌** | **❌** | **❌** | **✅** | **❌** |
| build-your-own-x | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

→ **Clean partition.** 5-tier works.

---

## Part 2 — 5 Tiers detailed (updated v9)

### T3: Agent-as-education (unchanged từ v6)
**Purpose:** Teach concepts. **Verb:** Learn.
**Entrants:** ai-agents-for-beginners (1)

### T1: Agent-as-assistant (unchanged từ v4)
**Purpose:** Claude Code plug-in / skill library for daily coding. **Verb:** Use.
**Entrants:** ECC, Superpowers, gstack, GSD (4)

### T4: Agent-as-bridge (unchanged từ v7)
**Purpose:** Library wrapping external service for agent consumption. **Verb:** Integrate.
**Entrants:** notebooklm-py (1)

### T5: Agent-as-application (NEW v9)
**Purpose:** Standalone autonomous agent harness. **Verb:** Run.

**Characteristics:**
- Self-contained app (frontend + backend)
- Autonomous long-horizon tasks
- Single-tenant or small-team
- User submits goal, waits for results
- Batteries-included infrastructure (sandbox + memory + skills + sub-agents + gateway)

**Current entrants:** deer-flow (1)

**Potential future entrants:**
- OpenHands (prev OpenDevin)
- AutoGPT
- CrewAI (borderline; could be T1 or T5)
- Agent Zero
- Cognition Devin OSS alternative (if exists)

**Emergence condition:** Tier 5 multi-entrant when 2+ standalone autonomous agent apps published.

### T2: Agent-as-service (unchanged từ v4)
**Purpose:** Multi-tenant platform hosting agents for users. **Verb:** Deploy.
**Entrants:** goclaw (1)

### Outside scope (unchanged từ v8)
**Purpose:** Meta-reference / general aggregator (not agent-focused).
**Entrants:** build-your-own-x (1)

---

## Part 3 — Cross-tier relationships (updated v9)

### Education → Assistant progression (unchanged)
Course teaches concepts → user picks T1 tool.

### Assistant → Bridge adoption (unchanged v7)
T1 user adds T4 bridges for external services.

### Assistant → Application comparison (NEW v9)
**T1 vs T5 choice depends on task shape:**

- **Interactive coding (T1):** Claude Code session
- **Long research + report (T5):** deer-flow autonomous
- **Hybrid workflow:** Use both (complementary per deer-flow's README)

### Application → Service progression (NEW v9)
**Solo → small team → multi-tenant:**
- Solo: T5 (deer-flow single-tenant)
- Small team: T5 với multi-user config
- Enterprise multi-tenant: T2 (goclaw-class)

### T5 invokes T1 (interoperability)
deer-flow README explicit: can invoke Claude Code via OAuth.
**Implication:** Tiers not mutually exclusive; can chain.

### T5 ≠ T2 distinction

| Axis | T5 (application) | T2 (service) |
|------|-------------------|-------------|
| **Tenancy** | Single-tenant | Multi-tenant |
| **Deploy target** | User's infra | Cloud/SaaS |
| **Who uses** | You | Your users |
| **Complexity** | App complexity | Platform complexity |
| **Example** | deer-flow | goclaw |

---

## Part 4 — 20-axis analysis (extended từ v7 18-axis)

| Axis | T3 | T1 | T4 | **T5** | T2 |
|------|-----|-----|-----|--------|-----|
| **Purpose** | Learn | Use | Integrate | **Run** | Deploy |
| **Target user** | Learner | Individual dev | Agent user | **Task submitter** | Platform operator |
| **Scale** | 1 learner | 1-10 devs | Per-integration | **1-50 users** | 10-10,000 users |
| **Format** | Curriculum | Tool + docs | Library + Skill | **Standalone app** | Platform + APIs |
| **Task duration** | Lesson-paced | Interactive seconds-minutes | Per-call | **Minutes-hours** | Platform-paced |
| **Autonomy** | N/A | User-directed | Per-call | **Autonomous** | Platform-managed |
| **UI** | Static docs | CLI | CLI + lib | **Web app** | Web + API |
| **Deploy complexity** | Lowest | Low | Low-medium | **High** | Highest |
| **Code quality** | Learnability | Production | Production | **Production** | Hardened |
| **Sequencing** | Linear | Non-linear | On-demand | **Goal-driven** | Platform-dep |
| **Cost** | Free | Free-to-paid | External service | **Infra + LLM compute** | Platform + infra |
| **Community** | Discord | Varies | Service-specific | **GitHub + Discord** | Enterprise |
| **Vendor** | Microsoft | Mixed | Solo often | **ByteDance (corp)** | Mixed |
| **Language support** | Multi 50+ | English-first | English-first | **Multi (5 langs)** | Multi |
| **Distribution** | Git clone | npm/git | pip + CLI | **Git + Docker + make** | Docker/binary |
| **Outcome** | Knowledge | Code shipped | Automation | **Artifact** | Service live |
| **Multi-tenant?** | N/A | No | No | **No (single)** | Yes |
| **Commitment** | 2-4 weeks | 1-2 weeks | Days | **Hours (per task)** | Months |
| **External dependency** | None | None | Hard (service) | **LLM provider** | None |
| **Maintenance fragility** | Low | Medium | High | **Medium** | Medium |

---

## Part 5 — 5 emergent patterns (extended từ v7's 4)

### Pattern 1: Purpose → Format correlation (validated across all tiers)
| Purpose | Format |
|---------|--------|
| Learn (T3) | Curriculum |
| Use (T1) | Reference docs |
| Integrate (T4) | Library + CLI + Skill |
| **Run (T5)** | **Standalone app (UI + backend)** |
| Deploy (T2) | Platform + API |

### Pattern 2: Vendor consolidation increases với ambition (refined)

| Tier | Vendor pattern |
|------|----------------|
| T3 | Corporate (Microsoft) — curriculum requires resources |
| T1 | Mixed (solo + Anthropic) |
| T4 | Solo (bus factor 1) |
| **T5** | **Corporate (ByteDance) — app requires infrastructure** |
| T2 | Mixed (solo + corporate) |

**New insight:** T5 parallels T3 in requiring corporate backing. Standalone apps need infrastructure investment solo devs rarely afford.

### Pattern 3: Learning progression recursive (unchanged)

### Pattern 4: Orthogonality (validated từ v7)

T4 plugs into T1/T2/T5. Cross-cutting axis.

### Pattern 5 (NEW v9): Task duration correlates với form factor

| Task duration | Form factor |
|---------------|-------------|
| Interactive (seconds-minutes) | T1 Claude Code plug-in |
| Call-based | T4 library invocation |
| **Long-horizon (minutes-hours)** | **T5 standalone app** |
| Platform ops (continuous) | T2 service |

**Insight:** Longer tasks = more infrastructure. T5 is minimum viable infrastructure for autonomous long tasks.

---

## Part 6 — Practical usage by persona (8 personas extended)

### Persona 1: Complete beginner
**Path:** T3 → T1 → (optional T4 bridges) → T3 revisit

### Persona 2: Experienced dev, no agent experience
**Path:** T3 skim → T1 master → T4 bridges → evaluate T5

### Persona 3: Agent practitioner
**Path:** T1 depth → T4 adopt → **T5 for long tasks** → T2 if scale

### Persona 4: Team lead
**Path:** T3 team read → T1 standardize → T5 automate team workflows → T2 if enterprise

### Persona 5: Platform builder
**Path:** T2 direct → T5 for internal automation → T1/T3/T4 as needed

### Persona 6: Storm Bear vault operator (Cvtot)
**Path:** Already T1 (5 frameworks), T3 (course), T2 (goclaw surveyed), T4 (notebooklm-py), **now T5 (deer-flow)**

**Next:** T5 pilot — install deer-flow, test Scrum retro synthesis

### Persona 7: VN developer community
**Path:** T3 VN translation → T1 via Storm Bear → T5 standalone apps as productivity multiplier

### Persona 8 (NEW v9): Long-task automation user
**Path:** Skip T1 → Start T5 → User submits goals, waits for results

**Description:** Non-technical user, hates interactive AI coding, wants "tell AI what to do, get result." T5 fits better than T1.

---

## Part 7 — Integration patterns (updated v9)

### Pattern A: Education + Assistant (unchanged)
Course + T1 tool for learning + daily use.

### Pattern B: Education + Service (unchanged)
Course + T2 for enterprise deployment.

### Pattern C: Assistant + Service (unchanged)
T1 individual → T2 when scale.

### Pattern D: Full-stack 3-tier (unchanged)

### Pattern E: Assistant + Bridge (unchanged v7)
T1 tool + T4 library.

### Pattern F: Service + Bridge bundle (unchanged v7)
T2 platform bundles T4 bridges.

### Pattern G (NEW v9): Assistant + Application (complementary)
T1 Claude Code for interactive + T5 deer-flow for autonomous. Best of both.

### Pattern H (NEW v9): Application + Bridge
T5 deer-flow + T4 bridges (e.g., notebooklm-py) for service integrations.

### Pattern I (NEW v9): Full-stack 4-tier
Learn (T3) → Use (T1) → Integrate (T4) → Run (T5).
**Most complete practitioner path. 6-9 months.**

### Pattern J (NEW v9): Enterprise 5-tier
Learn (T3) → Use (T1) → Integrate (T4) → Run (T5) → Deploy (T2).
**Full lifecycle. 9-18 months.**

---

## Part 8 — Storm Bear vault implications

### v9 milestones unlocked

- ✅ **T5 slot identified** — deer-flow = first T5 entrant
- ✅ **5-tier taxonomy defensible** — 9 data points across 5 tiers + 1 outside
- ✅ **T5 vs T2 distinction clarified** — single-tenant autonomous vs multi-tenant platform
- ✅ **Task-duration → form-factor pattern observed** (new pattern 5)
- ✅ **9-wiki clean partition** — no forced fits

### Taxonomy health

**v9 5-tier = accurate cho current corpus.** Waiting 2nd T5 entrant validates multi-entrant.

Future monitoring:
- 2nd T5 entrant (OpenHands/AutoGPT/CrewAI/Agent Zero) — validates T5 tier
- 2nd T2 entrant — validates T2
- 2nd T3 entrant — validates T3
- 2nd T4 entrant — validates T4

### Storm Bear decision framework

**User asks "I need long autonomous task automation":**
→ Route to T5 (deer-flow)

**User asks "I want to use Claude Code productively":**
→ Route to T1 (4 options — GSD/Superpowers/ECC/gstack)

**User asks "Deploy agents for my users":**
→ Route to T2 (goclaw)

**User asks "Integrate service X":**
→ Route to T4 (notebooklm-py or similar)

**User asks "Learn AI agent concepts":**
→ Route to T3 (course)

### Complete decision tree now visible.

---

## Part 9 — Compare v6 → v7 → v9 evolution

| Axis | v6 (3-tier) | v7 (4-tier) | **v9 (5-tier)** |
|------|-------------|-------------|-----------------|
| Tiers | 3 | 4 | **5** |
| Coverage | Learn + Tool + Service | + Bridge | **+ Application** |
| Corpus | 6 | 7 | **9** |
| Emergence trigger | Different-domain education | Different-domain bridge | **Different-domain standalone app** |
| Orthogonality | N/A | T4 cross-cutting | T4 still cross-cutting; T5 separate tier |
| Single-entrant tiers | 2 (T2, T3) | 3 (T2, T3, T4) | **4 (T2, T3, T4, T5)** |
| Multi-entrant validation | T1 (4) only | T1 (4) only | **T1 (4) only** |

**Hypothesis:** v10 may validate 2nd entrant trong T2/T3/T4/T5. OR introduce Tier 6 (infrastructure layer like MCP spec raw?).

---

## Part 10 — What v9 can't yet answer

### 1. T5 multi-entrant validation

N=1 in T5. Can T5 multi-entrant prove diverse? Candidates exist (OpenHands, AutoGPT, CrewAI) — 10th wiki should test.

### 2. Orthogonality persistent?

T4 cross-cutting observed at v7. Does T5 also have orthogonality? (Can T5 apps be embedded in T2? Example: deer-flow as skill-in-goclaw?) Unclear.

### 3. Tier 6 emergence signal?

MCP protocol specs, Anthropic Agent SDK raw, research papers — could these constitute "Tier 6 Agent-as-protocol/spec"? Wait for 2nd wiki in this space.

### 4. T5 subcategories?

Are deer-flow (Chinese + app) + AutoGPT (US + classic) + Devin (commercial closed) + OpenHands (OSS OSS-alt) really same tier? Or T5a/T5b subcategories?

---

## References

- v4 taxonomy (2-tier): `../../goclaw - Beginner Analysis/03 Published/(C) Agent framework taxonomy.md`
- v6 taxonomy (3-tier): `../../ai-agents-for-beginners - Beginner Analysis/03 Published/(C) Agent framework taxonomy v2 - 3 tier.md`
- v7 taxonomy (4-tier + orthogonality): `../../notebooklm-py - Beginner Analysis/03 Published/(C) Agent framework taxonomy v3 - 4 tier with bridge.md`
- v5 Tier 1 4-way: `../../get-shit-done - Beginner Analysis/03 Published/(C) Tier 1 4-way comparison.md`
- Beginner guide: [[(C) deer-flow - Huong dan cho nguoi moi]]
- Entity pages this wiki:
  - [[../02 Wiki/(C) SuperAgent Harness Architecture]]
  - [[../02 Wiki/(C) Skill System (Progressive Loading)]]
  - [[../02 Wiki/(C) Sub-Agent System (Parallel Fan-out)]]
  - [[../02 Wiki/(C) Message Gateway (Multi-Channel)]]
- Sibling wikis (all 8):
  - 4 T1 agent-assistant
  - 1 T2 goclaw
  - 1 T3 course
  - 1 T4 notebooklm-py
  - 1 outside-scope build-your-own-x
- Routine: `../../../05 Skills/llm-wiki-routine.md`
