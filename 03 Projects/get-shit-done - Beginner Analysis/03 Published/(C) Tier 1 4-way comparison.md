# Tier 1 4-Way Comparison — ECC vs Superpowers vs gstack vs GSD

> **Special deliverable:** 4-way comparison within **Tier 1 (agent-as-assistant)** established by v4 taxonomy. Completes Tier 1 slot với GSD as 4th entrant. Updates v3's 3-way + v4's taxonomy với new data point.
>
> **Tác giả:** Storm Bear, dựa trên 5 project wikis:
> - ECC (v1), Superpowers (v2), gstack (v3) — 3 Tier 1 originals
> - goclaw (v4) — Tier 2 (adjacent domain, separate taxonomy)
> - **GSD (v5)** — 4th Tier 1 entrant
>
> **Ngày:** 2026-04-18 | **Phiên bản:** v1
> **Audience:** Tech lead, founder, dev team đang quyết định Tier 1 framework
> **Song ngữ:** Tiếng Việt (chính) + English (technical terms)

---

## 📋 Mục lục

1. [TL;DR — Pick 1 in 60 seconds](#tldr--pick-1-in-60-seconds)
2. [Tier 1 context (from v4 taxonomy)](#tier-1-context-from-v4-taxonomy)
3. [Cheat sheet 1 page](#cheat-sheet-1-page)
4. [4 bản chất khác nhau](#4-bản-chất-khác-nhau)
5. [15-axis comparison](#15-axis-comparison)
6. [Decision matrix](#decision-matrix)
7. [Persona match (8 personas)](#persona-match-8-personas)
8. [4-way emergent patterns](#4-way-emergent-patterns)
9. [Mix & match strategies](#mix--match-strategies)
10. [Storm Bear recommendation](#storm-bear-recommendation)
11. [FAQ](#faq)

---

## TL;DR — Pick 1 in 60 seconds

| Bạn muốn | Chọn |
|----------|------|
| **Broad polyglot skills (185)** + domain agents (48) | **ECC** |
| **Iron Law TDD** + methodology discipline + "your human partner" | **Superpowers** |
| **Founder velocity** + role-based (CEO/Eng/Designer) + browser automation | **gstack** |
| **"Context rot" solution** + most harnesses (14) + spike/sketch/seeds | **GSD** |
| Team < 5 solo-ish, YC culture | gstack |
| Team 3-10 disciplined, production-critical | Superpowers |
| Team > 10 polyglot, enterprise | ECC |
| Long sessions with quality degradation pain | GSD |
| Want npm single-command install | GSD |
| Want git clone + setup script | gstack |
| Want Claude marketplace + git URL | Superpowers |
| Want plugin system | ECC |

→ **Default heuristic:** Pick by **culture fit first**, **scope needs second**.

---

## Tier 1 context (from v4 taxonomy)

**Tier 1 = Agent-as-assistant (dev workflow enhancement)**

Vs Tier 2 = Agent-as-service (end-user platform, goclaw).

**4 Tier 1 entrants:**

| Position | Framework | Author | First version ingested |
|----------|-----------|--------|------------------------|
| First (ECC) | Everything Claude Code | Affaan Mustafa | 2026-04-17 (v1 wiki) |
| Second (Superpowers) | Superpowers | Jesse Vincent (obra) | 2026-04-18 (v2) |
| Third (gstack) | gstack | Garry Tan | 2026-04-18 (v3) |
| **Fourth (GSD)** | **get-shit-done** | **TÂCHES (@gsd_foundation)** | **2026-04-18 (v5)** |

→ **Complete Tier 1 slot** với 4 frameworks giving "spectrum" analysis.

---

## Cheat sheet 1 page

| Axis | **ECC** | **Superpowers** | **gstack** | **GSD** |
|------|---------|-----------------|------------|---------|
| **Author** | Affaan Mustafa | Jesse Vincent | Garry Tan (YC) | TÂCHES |
| **Credibility** | Anthropic Hackathon Winner | OG dev tool author | YC President | Solo creator |
| **Core framing** | Performance optimization | Methodology (Iron Law) | Virtual team (role) | **"Context rot solution"** |
| **Scope** | 185 skills + 48 agents + 79 commands | 14 skills + 1 agent | 23 specialists + 8 tools + 1 agent | **33 agents + 83 commands + 11 hooks** |
| **Workflow** | Sequential phases | 7-stage HARD-GATE | Sprint pipeline smart-routing | **5-step + `/gsd-next` auto-route** |
| **Harnesses** | 5 | 7 | 10 | **14 (most)** |
| **Distribution** | Plugin + manual | Marketplace + git URL | Setup script + git | **npm (`npx get-shit-done-cc`)** |
| **TDD style** | `tdd-workflow` skill | Iron Law MANDATORY | Built into `/ship` | **Via `gsd-add-tests` command** |
| **Subagent model** | 48 specialized | 1 + dynamic spawn | 23 specialists | **Thin orchestrator + 33 specialists** |
| **Browser** | Via MCP | Not core | Built-in daemon | **Not core** |
| **Tone** | Prescriptive | Iron Law + "your human partner" | Founder direct | **Anti-enterprise-theater** |
| **Voice protection** | None explicit | Terminology tuning | 3 hard-gates | **Implied (TÂCHES voice)** |
| **Update cadence** | Monthly | 5/month | 5+/week | **Semver v1.37.x, active** |
| **License** | MIT | MIT | MIT | **MIT** |
| **Commercial model** | Plugin + paid products | None (pure OSS) | YC recruiting | **$GSD Solana token** |
| **VN support** | ❌ | ❌ | ❌ | ❌ (4 langs, no VN) |
| **Best audience** | Polyglot team 10+ | Disciplined team 3-10 | Solo founder | **Context rot-prone long sessions** |

---

## 4 bản chất khác nhau

### ECC = "Toolbox philosophy"

> "Tôi có vấn đề, tôi tìm skill phù hợp."

185 skills cover 12+ ecosystems. 48 specialized domain agents. Flexible workflow, skill compose freely.

**Strength:** Broad coverage cho polyglot team.
**Weakness:** Easy skip discipline. 185 skills = decision fatigue.

### Superpowers = "Methodology philosophy"

> "Tôi có discipline, tôi áp lên mọi problem."

14 skills deep-tuned. 7-stage workflow với HARD-GATE XML. Iron Law TDD non-negotiable. 94% PR rejection rate.

**Strength:** Production-grade output default.
**Weakness:** Friction first week. Opinionated can frustrate.

### gstack = "Team philosophy"

> "Tôi là CEO, Claude Code là engineering team."

23 specialists + 8 power tools. Sprint pipeline (Think/Plan/Build/Review/Test/Ship/Reflect). Browser daemon. Conductor parallel sprints.

**Strength:** Founder productivity multiplier.
**Weakness:** Role-based framing có thể restrict. Voice preservation hard-gates.

### GSD = "Context rot philosophy"

> "Claude's context fills up, quality degrades. I fix that."

33 agents + 83 commands. 5-step workflow với `/gsd-next` auto-routing. 4-mechanism stack cho context rot. Spike/Sketch/Seeds/Threads unique primitives.

**Strength:** Specific problem framing + most harnesses.
**Weakness:** 83 commands = learning cliff. Docs lag (33 vs 21 agents).

---

## 15-axis comparison

### Axis 1: Workflow style

| | ECC | Superpowers | gstack | GSD |
|-|-----|-------------|--------|-----|
| Stages | Sequential phases (soft) | 7 hard-gated | 7 smart-routed | **5 auto-routed** |
| Enforcement | Guidance | HARD-GATE XML | Proactive suggestion | **`/gsd-next` command** |
| Skip | Free | Can't skip 1/5 | Smart-skip | **Skip any via quick mode** |
| Parallelism | Skill-compose | SDD spawn | Conductor external | **Wave execution built-in** |

### Axis 2: Scope + learning curve

| | ECC | Superpowers | gstack | GSD |
|-|-----|-------------|--------|-----|
| Skills/commands | 185 + 79 legacy | 14 | 23 + 8 | **83** |
| Agents | 48 | 1 + dynamic | 23 (dual-role) | **33** |
| Setup roadmap | 4 weeks | 2 weeks | 1 week | **1 week** |
| Complexity | High (185) | Medium (14 deep) | Low (role-intuitive) | **Medium-high (83)** |

### Axis 3: Distribution + install

| | ECC | Superpowers | gstack | GSD |
|-|-----|-------------|--------|-----|
| Primary channel | Plugin | Marketplace | Setup script | **`npx` npm** |
| Install command | Plugin-specific | `/plugin install` | `./setup` | **`npx get-shit-done-cc@latest`** |
| Update | Plugin refresh | Marketplace refresh | `/gstack-upgrade` | **Re-run `npx`** |
| Scriptable | Limited | Limited | Flags | **Full flags (15+)** |
| Community ports | N/A | N/A | N/A | **✅ Section in README** |

### Axis 4: Harness count

| | ECC | Superpowers | gstack | GSD |
|-|-----|-------------|--------|-----|
| Count | 5 | 7 | 10 | **14** |
| Tier 1 (well-tested) | All 5 | Claude/Codex/Cursor | Claude/Codex/Cursor/OpenCode | Claude Code (most tested) |
| Tier 2 (secondary) | N/A | Gemini/Copilot CLI/Codex App | Factory/Slate/Kiro/Hermes/GBrain | **Kilo/Windsurf/Antigravity/Augment/Trae/Qwen/CodeBuddy/Cline** |

→ **GSD most inclusive.** But Claude Code still most-tested across all 4.

### Axis 5: TDD approach

| | ECC | Superpowers | gstack | GSD |
|-|-----|-------------|--------|-----|
| Style | Skill `tdd-workflow` | **Iron Law MANDATORY** | Built-in `/ship` | Via `gsd-add-tests` |
| Rationalizations detection | Implicit | **11 explicit** | `/review` catches | **Plan verifier** |
| Red flags | Implicit | **13 "STOP and restart"** | Code review | **Plan checker loop** |
| Bypass | ✅ Skip | ❌ No way | ⚙️ Auto-bootstrap | ✅ Skip |

### Axis 6: Subagent architecture

| | ECC | Superpowers | gstack | GSD |
|-|-----|-------------|--------|-----|
| Count | 48 pre-built | 1 + dynamic | 23 pre-built | **33 pre-built** |
| Taxonomy | **Domain** (security/DB/frontend) | **Function** (implementer/reviewer) | **Role** (CEO/QA/CSO) | **Function** (researcher/planner/executor) |
| Status protocol | Free-form | **DONE/CONCERNS/BLOCKED/NEEDS_CONTEXT** | Artifact hand-off | **Artifact hand-off** |
| Spawn discipline | User-called | SDD skill | Role command | **Orchestrator-auto** |

### Axis 7: Context management

| | ECC | Superpowers | gstack | GSD |
|-|-----|-------------|--------|-----|
| Problem named | Generic "agent" | "Context window pollution" (v5.0.2) | Implicit | **"Context rot" (explicit)** |
| Mechanism | Skills + hooks | Subagent isolation | Fresh Conductor sessions | **4-mechanism stack** |
| File-structured state | Hook artifacts | Iteration logs | `/learn` JSON | **`.planning/` folder** |
| Runtime monitor | ❌ | ❌ | ❌ | **`gsd-context-monitor.js` hook** |

→ **GSD most explicit** about context management.

### Axis 8: Hooks ecosystem

| | ECC | Superpowers | gstack | GSD |
|-|-----|-------------|--------|-----|
| Count | 8 standard | 1 SessionStart | None public | **11 custom (.js/.sh)** |
| Types | Lifecycle | Session | Internal | **Monitor/guard/scan/validate** |
| Prompt injection defense | None | None | None | **`read-injection-scanner.js`** |

### Axis 9: Commit discipline

| | ECC | Superpowers | gstack | GSD |
|-|-----|-------------|--------|-----|
| Atomic commits | Recommended | Skill-enforced | **"Always bisect"** | **Per-task automatic** |
| `.planning/` commits | N/A | Git-worktree | N/A | **Yes, with filtering** |
| PR hygiene | Manual | Manual | `/ship` auto | **`/gsd-ship` + `/gsd-pr-branch`** |

### Axis 10: Commercial model

| | ECC | Superpowers | gstack | GSD |
|-|-----|-------------|--------|-----|
| License | MIT | MIT | MIT | **MIT** |
| Paid products | Separate (AgentShield commercial) | None | None | **$GSD Solana token + foundation** |
| Funding signal | Paid products | Volunteer OSS | YC recruiting funnel | **Crypto-backed foundation** |

→ **GSD unique with crypto token.** Implications unclear.

### Axis 11: Reflection + learning

| | ECC | Superpowers | gstack | GSD |
|-|-----|-------------|--------|-----|
| Weekly retro | N/A | Manual iteration log | **`/retro` + `/retro global`** | **`/gsd-audit-milestone` + `/gsd-session-report`** |
| Cross-session memory | continuous-learning v2 skill | N/A | `/learn` | **`.planning/STATE.md` + threads** |
| Forward-looking capture | N/A | N/A | `/learn` stores | **`/gsd-plant-seed` with triggers** |

→ **GSD + gstack most built-in reflection.** ECC via skill. Superpowers manual.

### Axis 12: Unique primitives

| Framework | Unique primitive | Value |
|-----------|------------------|-------|
| **ECC** | 48 specialized domain agents | Deep domain knowledge |
| **Superpowers** | Iron Law + 11 Rationalizations + 13 Red Flags | Anti-drift discipline |
| **gstack** | Browser daemon + `/pair-agent` + Conductor parallel | Real browser + parallel |
| **GSD** | **Spike/Sketch + Seeds + Threads + Workstreams + Workspaces** | **Pre-planning experiments + forward capture** |

→ **GSD most novel primitives of 4.** Each solves specific pre-plan/cross-session pain.

### Axis 13: Voice + tone

| | ECC | Superpowers | gstack | GSD |
|-|-----|-------------|--------|-----|
| Register | Prescriptive helpful | Iron Law legalistic | Founder direct | **Anti-enterprise-theater** |
| Distinctive phrase | "production-ready" | "your human partner" | "Boil the Lake" | **"No enterprise roleplay bullshit"** |
| Voice protection | None | Terminology | 3 hard-gates | **Implied (TÂCHES voice)** |
| Protected voice | N/A | "your human partner" + Iron Law phrasing | ETHOS.md + promotional + tone | **N/A explicit** |

### Axis 14: Update cadence

| | ECC | Superpowers | gstack | GSD |
|-|-----|-------------|--------|-----|
| Releases | Monthly | 5/month | 5+/week | **v1.37.1 (2026-04-17), active** |
| Current version | ~N/A | 5.0.7 | v0.18.3.0 | **v1.37.1 mainline** |
| Total versions | Steady | 27+ | 126 | **30+ (v1.37.x series)** |
| Breaking change discipline | Rare | v5.0.0 deliberate | Strict semver | **Conservative (v1 mature)** |

### Axis 15: Unique features beyond core

| | ECC | Superpowers | gstack | GSD |
|-|-----|-------------|--------|-----|
| Signature | AgentShield security scan | Brainstorm visual companion | Browser sidebar agent | **Spike HTML mockup variants** |
| Cross-model | N/A | Codex via ACP | `/codex` second opinion | **Cross-AI review (future?)** |
| Multi-project | N/A | N/A | `/retro global` | **Workspaces via worktrees** |
| Community | 170+ contributors | Smaller strict | Active voice-protected | **Discord + `@gsd_foundation`** |

---

## Decision matrix

### By team size

| Team size | Recommended | Backup |
|-----------|-------------|--------|
| Solo (1) | gstack or GSD | Superpowers |
| Duo (2) | gstack | GSD |
| Small (3-5) | Superpowers | gstack |
| Medium (6-10) | Superpowers | ECC |
| Large (10+) | ECC | Superpowers |

### By project type

| Project | Recommended | Why |
|---------|-------------|-----|
| New product from scratch | gstack | Sprint pipeline sharp |
| Production app maintenance | Superpowers | Iron Law TDD |
| Legacy codebase migration | ECC | Specialized agents |
| Long research/analysis sessions | **GSD** | **Context rot-resistant** |
| Multi-harness dev machine | GSD | **14 harnesses support** |
| Hackathon/demo | ECC | Broad capability |
| VN-market bot | ❌ None Tier 1 | goclaw Tier 2 better |

### By pain point

| Pain | Pick |
|------|------|
| "Agent skips testing" | Superpowers |
| "Agent ignores scope" | gstack or Superpowers |
| "Agent quality drops mid-session" | **GSD** |
| "Need specialized domain skill" | ECC |
| "Team inconsistency" | Superpowers |
| "Too many commands to memorize" | gstack |
| "Want structured dev workflow" | **GSD or Superpowers** |
| "Want velocity, skip ceremony" | gstack |

---

## Persona match (8 personas)

### Persona 1: "Solo founder technical"

- gstack primary, GSD backup
- Both match founder-velocity. gstack role-based easier mental model; GSD context-rot framing if long sessions

### Persona 2: "Scrum coach"

- Superpowers primary, gstack backup
- Iron Law discipline matches Scrum practices
- gstack's `/retro` useful

### Persona 3: "Senior polyglot dev"

- ECC primary
- 185 skills + 48 agents cover polyglot needs

### Persona 4: "First-time Claude Code user"

- gstack primary, GSD backup
- Both easy mental models (role-based vs auto-routing)

### Persona 5: "Enterprise security team"

- Superpowers primary (zero-dep) + ECC backup (AgentShield)
- GSD's 5-layer not equivalent

### Persona 6: "YC startup founder"

- gstack primary
- Cultural fit với Garry Tan voice

### Persona 7: "Research-heavy long-session worker"

- **GSD primary** (newcomer to roster)
- Context rot solution targeted exactly this pain
- Spike/Sketch/Threads match research workflow

### Persona 8: "Multi-harness team (mixed tooling)"

- **GSD primary**
- 14 harnesses > 10 gstack > 7 Superpowers > 5 ECC
- Single `npx --all` command sets up everything

---

## 4-way emergent patterns

**Only visible với 4 data points:**

### Pattern 1: Framing specificity correlates với scope

| | Framing specificity | Scope |
|-|---------------------|-------|
| ECC | Generic "performance optimization" | Broad (185) |
| Superpowers | Medium "methodology" | Narrow (14) |
| gstack | Medium "virtual team" | Medium (23+8) |
| GSD | **Specific "context rot"** | Medium-large (33+83) |

→ **More specific framing** correlates với medium-large scope. Broad framing = broad scope (or over-claim).

### Pattern 2: Distribution mechanism evolution

| Generation | Distribution | Framework |
|------------|--------------|-----------|
| 1st | Plugin system | ECC |
| 2nd | Marketplace + git URL | Superpowers |
| 3rd | Setup script + git clone | gstack |
| 4th | **npm package** | **GSD** |

→ **Distribution gets friction-lower with each generation.** Trends toward Node.js ecosystem conventions.

### Pattern 3: Subagent taxonomy divergence

3 different taxonomies:
- **Domain** (ECC): security, DB, frontend
- **Function** (Superpowers + GSD): implementer/reviewer, researcher/planner
- **Role** (gstack): CEO, QA, CSO

Each valid. Trade-offs:
- Domain = deep specific knowledge
- Function = reusable across domains
- Role = metaphor-intuitive

→ **No single winner.** Different mental models.

### Pattern 4: Workflow stage count convergence

- ECC: ~5 sequential phases (soft)
- Superpowers: 7 hard-gated
- gstack: 7 sprint (Think/Plan/Build/Review/Test/Ship/Reflect)
- GSD: 5 steps + reflection

→ **Convergence around 5-7 stages** cho dev workflow. Coincidence or fundamental constraint?

### Pattern 5: Voice protection maturity

- ECC: none explicit
- Superpowers: terminology tuning
- gstack: 3 hard-gates (ETHOS/promo/tone)
- GSD: implied (TÂCHES voice)

→ **Voice protection increases over frameworks' maturity.** Indicates AI agent slop is real concern.

### Pattern 6: Commercial model diversification

- ECC: paid products + MIT core
- Superpowers: pure OSS
- gstack: YC recruiting funnel + MIT
- GSD: **$GSD Solana token + MIT**

→ **4 different monetization paths.** Token is newest experiment.

---

## Mix & match strategies

### Strategy 1: Single-framework (recommended default)

Pick 1 based on persona. Stick 1-3 months. Evaluate.

### Strategy 2: GSD + goclaw (Tier 1 + Tier 2)

- GSD for dev work (context rot-resistant)
- goclaw Lite for personal AI deployment
- Bridge: vault-as-backend pattern

### Strategy 3: Superpowers workflow + GSD commands

- Adopt Superpowers's 7-stage mental model
- Use GSD's 83 commands for implementation
- Risk: mental model conflict

### Strategy 4: GSD primary + Superpowers discipline layer

- Run GSD daily
- Apply Superpowers's 11 Rationalizations mentally at review stages
- Best of: automation + discipline

### Strategy 5: ECC skills + GSD workflow

- ECC's 185 specialized skills
- GSD's 5-step workflow orchestrating them
- Risk: skill collision

### Strategy 6: Different projects, different framework

Per-project CLAUDE.md configures framework. Teams can use different tools per project type:
- Research projects → GSD
- Production products → Superpowers
- Hackathon → ECC
- Founder solo work → gstack

### Strategy 7: Evolving rollout

Phase 1 (weeks 1-2): Start with gstack (easiest mental model)
Phase 2 (weeks 3-4): Add Superpowers discipline
Phase 3 (weeks 5+): Consider GSD if context rot appears
Phase 4 (months 2+): ECC for specialized needs

---

## Storm Bear recommendation

### Tier 1 choice (for Scrum coaching projects)

**Primary: gstack** (per v4 recommendation, unchanged)
- Persona match (founder/tech lead)
- Sprint Pipeline + `/retro` built-in
- Browser automation

**Secondary consideration: GSD** (if context rot appears in practice)
- Plan + execute long research sessions (coaching engagements)
- 14 harnesses flexibility

**Tertiary: Superpowers** (for production-critical vault maintenance)
- Iron Law TDD cho skill/routine code
- Eval-driven changes

**ECC** = reference library when need specialized capability.

### Tier 2 choice (for potential deploy)

**goclaw Lite** (per v4 recommendation, unchanged)
- Knowledge Vault = potential vault backend
- Zero infrastructure for pilot

### Action plan

**Week 1-2 pilot (from v3+v4 recommendation):**
1. Install gstack
2. Run 1 Scrum coaching project end-to-end
3. Install goclaw Lite, symlink vault
4. Test agent query

**Post-pilot decisions:**
- gstack working → keep
- Context rot appears → add GSD as overlay
- Need polyglot breadth → consider ECC
- TDD discipline gap → adopt Superpowers's Iron Law mentally

---

## FAQ

### Q1: 4 Tier 1 frameworks — complete set?

Other Tier 1 frameworks exist (BMAD, SpecKit, OpenSpec, Taskmaster — cited by TÂCHES). Not in Storm Bear wiki. Pick based on explicitly-analyzed options.

### Q2: GSD is new (v5 wiki) — less mature?

Versions: GSD v1.37.1 (2026-04-17), Superpowers v5.0.7, gstack v0.18.3.0, ECC ~mature.

**Version ≠ maturity.** GSD has 83 commands + 33 agents = more than gstack's 31 total. Feature-complete despite younger.

### Q3: $GSD Solana token — ảnh hưởng adoption không?

Current: MIT + free install. No paywall.

**Watch for:** future changes if token value ties to framework usage. Could introduce commercial tier.

### Q4: GSD không có VN support — blocker?

Không phải blocker technical. Commands + docs in English. But:
- Team readme/guides trong English
- No `@gsd_foundation` VN community presence
- Storm Bear wiki = first VN reference

→ **Contribution opportunity:** VN translation PR.

### Q5: Storm Bear pivot từ gstack → GSD?

**No strong signal yet.** Keep gstack as primary recommendation.

Switch triggers:
- Context rot concretely blocks work
- Need > 7 harness support
- Spike/Sketch/Seeds actively missed

### Q6: Can I install multiple Tier 1 frameworks?

Technical: yes. Practical: skill name collisions. Pick 1 per project.

Or: different projects, different framework (Strategy 6).

### Q7: Why 4 frameworks in same tier?

Different approaches to same problem (dev workflow enhancement):
- ECC: breadth
- Superpowers: depth
- gstack: metaphor
- GSD: specific problem framing

Market will consolidate eventually. Now = explore options.

### Q8: Best framework cho Claude Code only?

All 4 support Claude Code. Pick based on culture + scope:
- Polyglot → ECC
- Discipline → Superpowers
- Founder → gstack
- Context rot → GSD

### Q9: Worst framework cho solo learner?

**ECC** = 185 skills overwhelm. Start gstack or GSD.

**Superpowers** is strict but narrow (14 skills) = OK for learner actually.

### Q10: Storm Bear vault pivot decision?

No pivot. Current plan: pilot gstack + goclaw Lite (weeks). GSD on standby if context rot surfaces during pilot.

---

## Closing thoughts — 4 is enough for Tier 1 analysis

5 wikis complete:
- 3 original Tier 1 (ECC/Superpowers/gstack)
- 1 Tier 2 (goclaw, taxonomy unlock)
- 1 Tier 1 addition (GSD, spectrum completion)

**6th wiki projection:** diminishing returns unless new tier emerges (vd Tier 3: platform-to-platform integration like Zapier for AI agents).

**Storm Bear vault's unique moat strengthens với each wiki:**
- v3: 3-way comparison
- v4: Tier taxonomy (2-tier model)
- **v5: 4-way within Tier 1 + 6 emergent patterns (pattern #1-6 này doc)**

**Non-linear value compounds.** Each wiki adds dimension, not just data.

**Next meta-action:**
- Storm Bear pilot (Option A unchanged)
- Or: v6 wiki different domain (MCP spec, LangChain, Anthropic Agents SDK — test routine's outer generalization)
- Or: Routine v2 upgrade (encode 6 action items từ v4 log)

---

> **Wiki maintained by Storm Bear vault.** 5-wiki cross-synthesis. Tier 1 slot complete. If comparison sai hoặc GSD updates, ping để fix.
>
> **Cross-references:**
> - ECC wiki: `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) index.md`
> - Superpowers wiki: `../../Superpowers - Beginner Analysis/02 Wiki/(C) index.md`
> - gstack wiki: `../../gstack - Beginner Analysis/02 Wiki/(C) index.md`
> - goclaw wiki: `../../goclaw - Beginner Analysis/02 Wiki/(C) index.md`
> - Previous 2-way: `../../Superpowers - Beginner Analysis/03 Published/(C) ECC vs Superpowers comparison.md`
> - Previous 3-way: `../../gstack - Beginner Analysis/03 Published/(C) ECC vs Superpowers vs gstack 3-way comparison.md`
> - v4 taxonomy: `../../goclaw - Beginner Analysis/03 Published/(C) Agent framework taxonomy.md`
> - Vault routine: `../../../05 Skills/llm-wiki-routine.md`
