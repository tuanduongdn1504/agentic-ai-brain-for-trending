# Agent Framework Taxonomy — ECC vs Superpowers vs gstack vs goclaw

> **Special deliverable:** **Taxonomy guide** (not forced 4-way comparison) — positions 4 AI agent frameworks by **architectural tier** và **use case** thay vì 1:1 compare. Unique output của Storm Bear vault — 4 wikis cùng vault, cùng format, synthesis unreproducible.
>
> **Tại sao taxonomy thay vì 4-way:** goclaw operates on **different architectural layer** than 3 siblings. Forced 4-way = apples-to-oranges. Taxonomy = clearer mental model.
>
> **Tác giả:** Storm Bear, dựa trên 4 project wikis:
> - ECC (v1, 2026-04-17)
> - Superpowers (v2, 2026-04-18)
> - gstack (v3, 2026-04-18)
> - goclaw (v4, 2026-04-18) — **4th routine auto-execution, adjacent domain**
>
> **Ngày:** 2026-04-18 | **Phiên bản:** v1
> **Audience:** Tech lead, Scrum coach, founder, dev team đang quyết định AI agent infrastructure
> **Song ngữ:** Tiếng Việt (chính) + English (technical terms)

---

## 📋 Mục lục

1. [Taxonomy overview — 2 tiers, 4 frameworks](#taxonomy-overview--2-tiers-4-frameworks)
2. [Tier 1: Agent-as-assistant (dev workflow)](#tier-1-agent-as-assistant-dev-workflow)
3. [Tier 2: Agent-as-service (end-user platform)](#tier-2-agent-as-service-end-user-platform)
4. [Cross-tier integration patterns](#cross-tier-integration-patterns)
5. [Decision tree — which tier + which framework](#decision-tree--which-tier--which-framework)
6. [Persona match (7 personas)](#persona-match-7-personas)
7. [Mix & match strategies](#mix--match-strategies)
8. [Common misconceptions](#common-misconceptions)
9. [Meta-relevance to Storm Bear vault](#meta-relevance-to-storm-bear-vault)
10. [FAQ](#faq)

---

## Taxonomy overview — 2 tiers, 4 frameworks

### The tiers

**Tier 1: Agent-as-assistant (Dev workflow enhancement)**
- Purpose: Enhance Claude Code cho individual developer productivity
- Deployment: Local tool on dev machine
- Audience: Developers
- Single-user scope

**Tier 2: Agent-as-service (End-user platform)**
- Purpose: Multi-tenant AI agent service for end users
- Deployment: Self-hosted server
- Audience: End users (via channels or UI)
- Multi-tenant scope

### The 4 frameworks

| Framework | Tier | Primary persona | Origin |
|-----------|------|-----------------|--------|
| **ECC** (Everything Claude Code) | **Tier 1** | Broad dev, polyglot team | Affaan Mustafa, Anthropic Hackathon Winner |
| **Superpowers** | **Tier 1** | Methodology-focused dev | Jesse Vincent (`obra`), OG dev tool author |
| **gstack** | **Tier 1** | Solo founder / CEO / tech lead | Garry Tan (YC President) |
| **goclaw** | **Tier 2** | End-user platform operator | `@nlb_io` (nextlevelbuilder), VN-focused |

### Why 2 tiers matter

**Mental model shift:**

If treat all 4 as competitors → confusion (why would CEO compare Claude Code skill framework với multi-tenant Go platform?)

If treat as 2 tiers → clarity:
- Tier 1 frameworks compete among themselves (dev chooses one)
- Tier 2 framework serves different need (deploy AI service)
- Cross-tier = complementary (dev builds with gstack, deploys via goclaw)

---

## Tier 1: Agent-as-assistant (dev workflow)

All 3 Tier 1 frameworks:
- Local installs on dev machine
- Enhance Claude Code (+ Codex, Cursor, OpenCode, etc.)
- Provide skills / agents / commands as building blocks
- Single-user scope
- Target: developer productivity

### Tier 1 comparison (12 axis)

| Axis | ECC | Superpowers | gstack |
|------|-----|-------------|--------|
| **Philosophy** | Performance optimization | Methodology (TDD Iron Law) | Role-based virtual team |
| **Scope** | 185 skills + 48 agents + 79 commands | 14 skills + 1 agent | 23 specialists + 8 power tools |
| **Workflow** | Sequential phases (flexible) | 7-stage hard-gated | Sprint pipeline (smart routing) |
| **TDD** | `tdd-workflow` skill (best practice) | Iron Law mandatory | Built into `/ship` |
| **Subagent** | 48 specialized | 1 + dynamic | 23 specialists |
| **Cross-harness** | 5 | 7 | **10** |
| **Browser** | Via MCP | Not core | **Built-in daemon** |
| **Tone** | Prescriptive | Iron Law + "your human partner" | Founder direct |
| **Voice protection** | None explicit | Terminology tuning | **3 hard-gates (ETHOS/promo/tone)** |
| **Update cadence** | Monthly | 5/month | **5+/week** |
| **License** | MIT | MIT | MIT |
| **Best audience** | Polyglot team | Disciplined dev | Solo founder + CEO |

→ **For Tier 1 selection detail,** xem [[(C) ECC vs Superpowers vs gstack 3-way comparison]] (previous deliverable).

### Tier 1 decision quick

- **Want broad skill library (Python/Rust/TS/Go/DB specialized):** ECC
- **Want Iron Law TDD + plan-before-code discipline:** Superpowers
- **Want founder velocity + role-based thinking + browser automation:** gstack

---

## Tier 2: Agent-as-service (end-user platform)

**Currently only goclaw in our analyzed set.**

**Other Tier 2 frameworks** (not analyzed in this vault):
- LangChain / LangGraph (agent orchestration library)
- AutoGPT ecosystem
- Custom FastAPI + Anthropic SDK deployments

**goclaw characteristics:**

| Dimension | goclaw |
|-----------|--------|
| **Language** | Go |
| **DB** | PostgreSQL 18 + pgvector (Standard) / SQLite (Lite) |
| **Multi-tenant** | ✅ Full (Standard) |
| **Channels** | 7 (Telegram, Discord, Slack, Zalo×2, Feishu, WhatsApp) |
| **LLM providers** | 20+ (incl. Claude CLI + Codex + ACP) |
| **Memory** | 3-tier (Working/Episodic/Semantic) + Knowledge Vault |
| **Security** | 5-layer defense + AES-256-GCM + RBAC |
| **License** | CC BY-NC 4.0 (non-commercial) |
| **Deployment** | Docker Compose or binary or desktop (Lite) |
| **Size** | 25MB single binary |
| **Agent teams** | First-class (Lead + Members + Task Board + Mailbox) |
| **i18n** | en / vi / zh |

### Use cases uniquely Tier 2

- **Deploy AI agent service cho non-dev end users** (Telegram bot, Zalo OA, etc.)
- **Multi-tenant SaaS** cho AI agents
- **Team coaching platform** (Storm Bear use case)
- **Personal AI desktop app** (Lite edition)
- **Enterprise deployment** with RBAC + audit logs

### Tier 2 decision quick

- **Solo founder, personal agent:** goclaw **Lite**
- **Team deploy agent service:** goclaw **Standard**
- **Enterprise with compliance needs:** goclaw Standard + OTel + Tailscale
- **VN market bot (Zalo):** **goclaw** (only framework với native Zalo support)

---

## Cross-tier integration patterns

### Pattern 1: Dev uses Tier 1, ships via Tier 2

**Flow:**
- Dev Alice uses gstack (Tier 1) cho own coding
- Alice ships features via gstack's `/ship`
- Alice deploys backend with goclaw (Tier 2) for multi-user service
- End users interact với goclaw via Zalo/Telegram
- goclaw spawns Claude Code sessions (via ACP provider) với gstack skills for complex tasks

**Best for:** Full-stack founder.

### Pattern 2: goclaw as skill-host

**Flow:**
- Install gstack/Superpowers/ECC on goclaw container
- goclaw's ACP provider spawns Claude Code sessions
- Skills auto-discoverable inside spawned session
- goclaw's agent → Claude Code's agent → skill invocation

**Caveat:** Not verified in this vault. Requires:
- goclaw Full Docker variant (has Node.js + Claude CLI)
- Skills installed per gstack/Superpowers/ECC instructions
- ACP provider config points to Claude CLI binary

### Pattern 3: Independent layers

**Flow:**
- Dev uses Tier 1 for dev work
- Production service uses Tier 2 (no Tier 1 dependency)
- Separate skill curation for each tier

**Best for:** Large team with dev/ops separation.

### Pattern 4: Storm Bear vault bridge

**Flow:**
- Storm Bear vault (Obsidian file-based) = canonical knowledge
- goclaw Lite local deploy với vault files symlinked
- Agent queries vault via natural language
- Cross-session learning compounds via consolidation workers
- Files remain git-versionable

**Best for:** Storm Bear pilot.

---

## Decision tree — which tier + which framework

```
Start →
│
├─ Cần deploy AI agent service cho end users không?
│  ├─ YES → Tier 2
│  │   └─ Choose goclaw (only Tier 2 analyzed)
│  │       ├─ Solo use / personal → Lite
│  │       └─ Team / production → Standard
│  │
│  └─ NO → Tier 1
│      │
│      ├─ Value Iron Law TDD + methodology discipline?
│      │  └─ YES → Superpowers
│      │
│      ├─ Cần broad skill library (polyglot team, 185 skills)?
│      │  └─ YES → ECC
│      │
│      ├─ Solo founder + role-based thinking + browser automation?
│      │  └─ YES → gstack
│      │
│      └─ Lưỡng lự?
│         ├─ Team < 5 → gstack (role-based dễ grasp)
│         ├─ Team 3-10 disciplined → Superpowers
│         └─ Team > 10 polyglot → ECC
│
└─ Cần cả hai tiers (dev work + production)?
   └─ Pattern 1: Tier 1 (dev) + Tier 2 (deploy)
       ├─ Dev với gstack → deploy goclaw Standard
       └─ Dev với Superpowers → deploy goclaw Standard (TDD discipline ships to prod)
```

---

## Persona match (7 personas)

### Persona 1: "Anh solo founder technical"

- **Situation:** Technical founder, duo team tối đa, ship volume cao
- **Best combo:**
  - Tier 1: **gstack** (role-based, velocity-focused)
  - Tier 2: **goclaw Lite** (personal AI agent)
- **Why:** gstack encoded Garry Tan's founder velocity. goclaw Lite = local AI without infrastructure.

### Persona 2: "Tech lead Scrum coach"

- **Situation:** Lead 3-8 engineers, production quality matters
- **Best combo:**
  - Tier 1: **Superpowers** (Iron Law TDD discipline)
  - Tier 2: **goclaw Standard** if need team-shared AI service
- **Why:** Superpowers enforces consistency. goclaw scales to team.

### Persona 3: "Senior dev polyglot"

- **Situation:** Python/Rust/TS/Go/DB — need specialized tooling
- **Best combo:**
  - Tier 1: **ECC** (185 skills, 48 agents)
  - Tier 2: not needed (dev-only scope)
- **Why:** ECC's broad coverage matches polyglot needs.

### Persona 4: "First-time Claude Code user"

- **Situation:** Dev but new to AI coding framework
- **Best combo:**
  - Tier 1: **gstack** (structured roles, easy mental model)
  - Tier 2: not needed yet
- **Why:** gstack's CEO/Eng/Designer metaphor is intuitive.

### Persona 5: "Vietnamese founder building for VN market"

- **Situation:** Building Zalo bot, Vietnamese-first UX
- **Best combo:**
  - Tier 1: **gstack** or **Superpowers** (dev work)
  - Tier 2: **goclaw Standard** (Zalo OA + Zalo Personal native support, Vietnamese i18n)
- **Why:** goclaw is **only framework với native Zalo** + VN bias.

### Persona 6: "Enterprise security team"

- **Situation:** Large org, compliance, audit requirements
- **Best combo:**
  - Tier 1: **Superpowers** (zero-dep supply chain)
  - Tier 2: **goclaw Standard** (5-layer defense, AES-256-GCM, RBAC, audit logs)
- **Why:** Most rigorous security posture in each tier.

### Persona 7: "Storm Bear vault maintainer (me)"

- **Situation:** Scrum coach + software dev, building personal knowledge system
- **Best combo:**
  - Tier 1: **gstack** (persona match — founder-like, solo)
  - Tier 2: **goclaw Lite** pilot (vault as query layer)
- **Why:** gstack matches velocity ambition. goclaw Lite adds natural language query to vault.
- **Blocker:** CC BY-NC 4.0 for Standard if coaching = commercial.

---

## Mix & match strategies

### Strategy 1: Single tier (MOST COMMON)

**Pick 1 Tier 1 framework, skip Tier 2:**
- Dev enhances own workflow
- No end-user deployment needed
- Simple

Most solo devs + small teams fit này.

### Strategy 2: Tier 1 + Tier 2 (FULL STACK)

**gstack (dev) + goclaw Lite (deploy):**
- Dev uses gstack for coding productivity
- Personal goclaw Lite runs local agents
- No cross-integration needed

### Strategy 3: Tier 1 + Tier 2 integrated

**Superpowers (dev) + goclaw Standard với ACP provider:**
- Dev ships production code disciplined (Superpowers Iron Law TDD)
- goclaw Standard deployed for end-user AI service
- goclaw's agents spawn Claude Code via ACP khi cần Superpowers skills
- Complex pattern, high power

### Strategy 4: 2 Tier 1 frameworks in different projects

- Project A (founder-velocity): gstack
- Project B (production-critical): Superpowers
- Project C (polyglot team): ECC

Per-project CLAUDE.md configures framework.

### Strategy 5: Storm Bear vault bridge

- Current: Storm Bear vault (Obsidian)
- Add: goclaw Lite với vault symlinked
- Keep: Obsidian primary editing
- Gain: Natural language query via goclaw agent

→ **Recommended pilot cho Storm Bear.**

---

## Common misconceptions

### Misconception 1: "goclaw competes with gstack"

**No.** Different tiers. goclaw = agent-as-service platform. gstack = dev workflow skills. **Complementary.**

### Misconception 2: "Tier 1 frameworks are interchangeable"

**Partially.** All enhance Claude Code. But philosophy + scope differ:
- ECC = toolbox (broad capability)
- Superpowers = discipline (narrow depth)
- gstack = team metaphor (role-based)

Pick based on persona, not feature count.

### Misconception 3: "goclaw replace Claude Code"

**No.** goclaw can USE Claude Code (via Claude CLI + ACP providers). Claude Code remains dev tool.

### Misconception 4: "Cross-harness count = best"

ECC = 5, Superpowers = 7, gstack = 10. Superficially gstack "best" on count. But:
- Count matters for portability
- Capability depth matters more per harness
- Most devs use 1-2 harnesses, so 5+ sufficient

### Misconception 5: "License doesn't matter for internal use"

**Depends.** ECC/Superpowers/gstack = MIT (worry-free).

goclaw = CC BY-NC 4.0 (non-commercial). Storm Bear's coaching business = gray area. Clarify before commercial deployment.

### Misconception 6: "Multi-tenant = overkill for small team"

**If team <3:** likely overkill. Use Tier 1 tool + shared git repo.

**If team > 3 OR customers interact với AI:** multi-tenant (goclaw Standard) essential.

### Misconception 7: "Pick newest = best"

goclaw is newer framework in this analysis. But newer ≠ better. gstack ships 5+/week. Superpowers 5/month. Cadence diff doesn't indicate quality. Match persona + use case first.

---

## Meta-relevance to Storm Bear vault

### Karpathy's LLM Wiki pattern across 4 frameworks

**Storm Bear vault = Karpathy's pattern implemented as Obsidian.**

**How each framework relates:**

| Framework | LLM Wiki pattern implementation |
|-----------|----------------------------------|
| ECC | Not core — ECC is skill catalog |
| Superpowers | Not core — Superpowers is methodology |
| gstack | Partial — `/learn` skill + cross-session memory |
| **goclaw** | **Full infrastructure** — Knowledge Vault với `[[wikilinks]]` + BM25 + pgvector + FS sync + 3-tier memory + consolidation workers |

→ **goclaw is only framework implementing Karpathy's pattern as infrastructure.**

### Potential Storm Bear deployment path

**Short-term (pilot):**
- GoClaw Lite on Storm Bear machine
- Symlink 4 project `02 Wiki/` folders into vault
- Test agent query over vault
- 1-week assessment

**Mid-term (if pilot positive):**
- goclaw Standard (Docker) local deploy
- Import Storm Bear vault as tenant
- Multiple users (Storm Bear + coaching clients?)
- Cross-session consolidation compounds vault knowledge

**Long-term (scale):**
- goclaw Standard cloud-hosted
- Coaching team accesses via web UI
- Zalo bot for VN clients
- Agent teams cho complex coaching workflows

**Blocker:** CC BY-NC 4.0 for commercial coaching. Needs clarity.

---

## FAQ

### Q1: Routine `llm-wiki-routine` had to reframe Phase 4b cho goclaw. Bình thường không?

Yes — **feature not bug**. Routine detected adjacent-domain vs forced 4-way comparison. Produced taxonomy guide (clearer mental model) instead.

Lesson: **Routines should handle domain-adjacency intelligently**, not force same output template.

### Q2: 4 frameworks same ecosystem chọn 1 default nào?

**No single default.** Persona-driven choice:
- Solo founder → gstack (Tier 1)
- Small disciplined team → Superpowers (Tier 1)
- Polyglot team → ECC (Tier 1)
- Personal AI → goclaw Lite (Tier 2)
- Multi-tenant service → goclaw Standard (Tier 2)

### Q3: Can I run all 4 on same machine?

Technically yes, không khuyến nghị. Skill name collisions (ECC's review vs gstack's `/review` vs Superpowers's code-review agent). Pick 1 Tier 1 + optionally goclaw.

### Q4: gstack's 10 hosts support = includes goclaw?

No. gstack's 10 hosts = 10 AI coding agents (Claude Code, Codex, Cursor, OpenCode, Factory, Slate, Kiro, Hermes, GBrain, OpenClaw). goclaw is **different tier** — platform, not coding agent.

### Q5: Integration pattern proven?

gstack + goclaw via ACP provider **theoretically works** (goclaw has Claude CLI provider; gstack installs as Claude Code skill).

**Not verified** in this vault. Pilot needed to confirm.

### Q6: License compatibility if mix?

- ECC/Superpowers/gstack = MIT (permissive)
- goclaw = CC BY-NC 4.0 (non-commercial)

Commercial user mixing all 4 = blocked by goclaw's NC clause. Resolve by licensing goclaw commercially or stay non-commercial.

### Q7: Which framework has steepest learning curve?

- **ECC:** 4-week roadmap (185 skills = overwhelming)
- **Superpowers:** 2-week roadmap (Iron Law strict but narrow)
- **gstack:** 1-week roadmap (role-based intuitive)
- **goclaw:** 1-week roadmap (Lite) / 2-week (Standard với channels + teams)

→ gstack = lowest friction cho Tier 1. goclaw Lite = lowest cho Tier 2.

### Q8: Storm Bear v1.0 recommendation?

**Pick 1 Tier 1 framework + goclaw Lite pilot:**
1. Tier 1 primary: **gstack** (persona match)
2. Tier 2 experiment: **goclaw Lite** (vault query layer)
3. Reassess after 2 weeks

### Q9: Vault skill + routine handle 4+ projects?

Yes. Routine `llm-wiki-routine` v1 executed 4 times. Pattern proven across:
- Feature framework (ECC)
- Methodology framework (Superpowers)
- Role-based framework (gstack)
- **Platform/infrastructure (goclaw)** — adjacent domain

Next expansion: different domain entirely (vd Anthropic MCP docs, Vercel AI SDK) → routine should handle nếu threshold + sibling-detection logic flexibly.

### Q10: Maintenance burden for knowing all 4?

**If chỉ use 1:** minimal.

**If maintain vault (Storm Bear role):** 4 wikis = ~1-2 hours/quarter để keep fresh (assuming quarterly-ish releases).

**If contribute upstream:** per-framework CLAUDE.md conventions differ. High maintenance if contribute to all 4.

---

## Storm Bear recommendation

### Tier 1 (dev work): **gstack**

**Why:**
- Persona match (founder/tech lead)
- Sprint Pipeline mental model intuitive
- `/retro` built-in aligns with Scrum coaching
- Browser automation bonus cho QA/dogfooding
- 10-host support = future-proof

### Tier 2 (personal AI): **goclaw Lite** (pilot)

**Why:**
- Knowledge Vault = Storm Bear vault's Karpathy pattern as infrastructure
- Natural language query over vault adds value
- Lite = zero infrastructure overhead
- CC BY-NC 4.0 OK cho personal use

### Deferred: goclaw Standard

**When to consider:**
- Storm Bear coaching team grows > 2 people
- Need multi-user shared vault
- CC BY-NC 4.0 commercial clarity resolved

### Final action plan

**Week 1 (Storm Bear pilot):**
1. Install gstack (if not done)
2. Run pilot theo gstack 1-week roadmap
3. Install goclaw Lite (30s)
4. Symlink 4 project wikis into vault
5. Test agent query

**Week 2 (assessment):**
- gstack velocity data
- goclaw Lite query quality
- Decision: continue, pivot, or stop

**Post-pilot:**
- Write Storm Bear iteration log (actual use data)
- Share findings with team / public blog
- Potentially: contribute back to framework chosen

---

## Closing thoughts — taxonomy > comparison

Storm Bear's 4-wiki synthesis revealed **mental model shift**: not all "AI agent frameworks" compete. They operate at different architectural layers.

**Old framing:** "Which AI agent framework is best?"
**New framing:** "Which tier (dev vs deploy)? Which persona?"

→ **Taxonomy unlocks better decisions.** Comparison between tiers = category error.

**Storm Bear vault's unique value:** 4 wikis + routine + taxonomy = reusable decision framework cho AI agent tooling. No external actor has built this (requires: same vault, same format, same tool, same timeframe). **This IS the moat.**

**Next meta-action cho vault:**
- Storm Bear pilot: gstack + goclaw Lite (real use data)
- Or: 5th wiki (different domain entirely, test routine generalization)
- Or: 2nd routine (non-wiki automation) — prove routine pattern scales

---

> **Wiki maintained by Storm Bear vault.** 4-wiki cross-synthesis + taxonomy framing = unique decision support. Nếu taxonomy thiếu sót, ping để fix.
>
> **Cross-references:**
> - ECC wiki: `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) index.md`
> - Superpowers wiki: `../../Superpowers - Beginner Analysis/02 Wiki/(C) index.md`
> - gstack wiki: `../../gstack - Beginner Analysis/02 Wiki/(C) index.md`
> - goclaw wiki: `../02 Wiki/(C) index.md`
> - Previous 2-way: `../../Superpowers - Beginner Analysis/03 Published/(C) ECC vs Superpowers comparison.md`
> - Previous 3-way: `../../gstack - Beginner Analysis/03 Published/(C) ECC vs Superpowers vs gstack 3-way comparison.md`
> - Vault routine: `../../../05 Skills/llm-wiki-routine.md`
