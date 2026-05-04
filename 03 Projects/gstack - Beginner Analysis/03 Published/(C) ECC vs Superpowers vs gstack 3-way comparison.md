# ECC vs Superpowers vs gstack — 3-Way Comparison Guide

> **Special deliverable:** Guide so sánh **3 AI coding frameworks** để team Storm Bear quyết định **framework nào dùng cho project nào**. Unique output chỉ có trong Storm Bear vault — 3 wikis cùng vault, cùng tay, cùng format = cross-project synthesis không ai khác có thể reproduce.
>
> **Tác giả:** Storm Bear, dựa trên 3 project wikis:
> - ECC (v1, 2026-04-17)
> - Superpowers (v2, 2026-04-18)
> - gstack (v3, 2026-04-18) — **first run của routine `llm-wiki-routine`**
>
> **Ngày:** 2026-04-18 | **Phiên bản:** v1
> **Audience:** Tech lead, Scrum coach, founder, dev team đang chọn AI coding framework
> **Song ngữ:** Tiếng Việt (chính) + English (technical terms)

---

## 📋 Mục lục

1. [TL;DR — Chọn cái nào trong 60 giây](#tldr--chọn-cái-nào-trong-60-giây)
2. [Cheat sheet 1 trang](#cheat-sheet-1-trang)
3. [3 bản chất khác nhau](#3-bản-chất-khác-nhau)
4. [Comparison theo 15 axis](#comparison-theo-15-axis)
5. [Use case decision tree](#use-case-decision-tree)
6. [Persona match](#persona-match)
7. [Mix & match strategies](#mix--match-strategies)
8. [Migration paths](#migration-paths)
9. [FAQ](#faq)
10. [Storm Bear recommendation](#storm-bear-recommendation)

---

## TL;DR — Chọn cái nào trong 60 giây

| Bạn muốn | Chọn |
|----------|------|
| **Solo founder / CEO vẫn muốn ship, ship volume cao, role-based mental model** | **gstack** |
| **Discipline + methodology + Iron Law TDD + ít skills deep** | **Superpowers** |
| **Toolbox đa năng + 185 skills + polyglot team + broad coverage** | **ECC** |
| Force plan-before-code + hard gates | Superpowers |
| Cần browser automation real + parallel sprints | gstack |
| Cần specialized domain agents (security, DB, frontend) | ECC |
| Multi-host (Copilot, Slate, Kiro, etc.) | gstack (10 hosts) |
| Zero-dependency discipline | Superpowers |
| YC startup culture / founder voice | gstack |
| Team > 10, enterprise | ECC |
| Team 2-5, high-velocity solo/duo | gstack |
| Scrum coach culture, disciplined PRs | Superpowers |

→ **Default heuristic:** team size + persona — gstack cho solo/duo/founder; Superpowers cho 3-10 người disciplined; ECC cho 10+ polyglot.

---

## Cheat sheet 1 trang

| Axis | **ECC** | **Superpowers** | **gstack** |
|------|---------|-----------------|------------|
| **Author** | Affaan Mustafa | Jesse Vincent (obra) | Garry Tan (YC President) |
| **Credibility** | Anthropic Hackathon Winner | OG dev tool builder | YC President + ships 600K LOC/60 days |
| **Stars** | 140K+ | TBD | TBD |
| **Scope** | 185 skills + 48 agents + 79 commands | 14 skills + 1 agent | 23 specialists + 8 power tools |
| **Philosophy** | Performance optimization | Methodology (Iron Law) | Role-based (virtual team) |
| **Workflow** | Sequential phases (flexible) | 7-stage hard-gated | Sprint pipeline (smart routing) |
| **TDD style** | `tdd-workflow` skill (best practice) | "Iron Law" mandatory | Built into `/ship` test bootstrap |
| **Subagent** | 48 specialized | 1 + dynamic spawn | 23 specialists |
| **Cross-harness** | 5 | 7 | **10 (most)** |
| **Browser automation** | Via MCP tools | Not core | **Built-in daemon (sub-second)** |
| **Distribution** | Plugin + manual | Marketplace + git URL | Multi-host declarative TypeScript |
| **Dependencies** | Various | **Zero-dep philosophy** | Bun + Playwright + Chromium (bundled) |
| **Security** | AgentShield + 11-bar | Zero-dep supply chain | Localhost + bearer token + keychain |
| **Reflection** | Not explicit | Iteration logs (manual) | **`/retro` built-in + `/retro global`** |
| **Tone** | Prescriptive best-practice | Iron Law, "your human partner" | Founder direct, "Boil the Lake" |
| **Voice protection** | None explicit | Terminology tuning | 3 hard-gates (ETHOS/promo/tone) |
| **Commercial model** | Plugin + paid products separate | Pure OSS | OSS + YC recruiting funnel |
| **Update cadence** | Steady (monthly-ish) | Aggressive (5/month) | **Extremely aggressive (5+/week)** |
| **PR culture** | Open | 94% rejection | Voice + ethos hard-gates |
| **Best audience** | Broad dev, polyglot team | Methodology-focused dev | Founder/CEO + first-timer + tech lead |
| **Maturity** | Established 10+ months | ~6 months | Recent (v0.18, very active) |

---

## 3 bản chất khác nhau

### ECC = "Toolbox philosophy"

**Mental model:** "Tôi có vấn đề, tôi tìm skill phù hợp."

Affaan Mustafa build ECC như **Swiss Army knife**:
- 185 skills cover database, React, security, DevOps, Python, Rust, ...
- 48 specialized agents domain-domain
- Flexible workflow — agent có thể skip/choose freely

**Strength:** Broad coverage cho polyglot team.
**Weakness:** Easy skip discipline; 185 skills = context overhead.

### Superpowers = "Methodology philosophy"

**Mental model:** "Tôi có discipline, tôi áp lên mọi problem."

Jesse Vincent build Superpowers như **operating discipline**:
- 14 skills deep-tuned (eval-driven, regression tested)
- 7-stage workflow với HARD-GATE XML blocks
- Iron Law TDD: NO PROD CODE WITHOUT FAILING TEST FIRST
- 94% PR rejection rate (eval evidence mandatory)

**Strength:** Production-grade output mặc định.
**Weakness:** Friction tuần đầu, "opinionated" có thể frustrate team kháng cự process.

### gstack = "Team philosophy"

**Mental model:** "Tôi là CEO, Claude Code là engineering team."

Garry Tan build gstack như **virtual engineering team**:
- 23 specialists + 8 power tools
- Sprint pipeline Think→Plan→Build→Review→Test→Ship→Reflect
- Role-based mental model (CEO/Eng/Designer/QA/CSO/Release)
- Browser daemon cho real automation
- Designed cho parallel sprints (10-15 với Conductor)

**Strength:** Founder productivity multiplier (600K LOC/60 days claim).
**Weakness:** Opinionated roles; skills cần voice preservation (don't fork without understanding ETHOS).

### Tại sao cả 3 cùng có value

3 framework **giải bài toán khác nhau**:
- **ECC:** "Làm sao agent có capabilities cho mọi task?"
- **Superpowers:** "Làm sao agent làm việc đúng cho task quan trọng?"
- **gstack:** "Làm sao 1 developer ship như team 20 người?"

→ **Không phải 3 competitors.** Có thể mix (xem [Mix & match](#mix--match-strategies)) nhưng usually pick 1.

---

## Comparison theo 15 axis

### Axis 1: Workflow style

| | ECC | Superpowers | gstack |
|-|-----|-------------|--------|
| Style | Sequential phases (soft) | 7-stage hard-gated | Sprint pipeline (smart routing) |
| Enforcement | Guidance | HARD-GATE XML | Proactive skill suggestion |
| Skip stage | ✅ Free | ❌ Not for brainstorming/TDD | ⚙️ Smart auto-skip based on work type |
| Parallel | Skill-compose | Limited | **Conductor 10-15 parallel** |

→ **Trade-off:**
- ECC flexible — easy to skip discipline
- Superpowers rigid — hard gates ensure quality
- gstack adaptive — smart routing (CEO doesn't review infra)

### Axis 2: Skills count + depth

| | ECC | Superpowers | gstack |
|-|-----|-------------|--------|
| Skills | 185 | 14 | 23 specialists + 8 tools |
| Lines per skill | ~50-150 | ~200-400 | Variable (templates) |
| Overlap | Frequent | None (1 purpose) | Some by design (review vs cso vs codex) |
| Coverage model | Broad-shallow | Narrow-deep | **Role-broad, depth per role** |

→ gstack's 23 = sweet spot giữa ECC (185 overload) và Superpowers (14 narrow).

### Axis 3: Subagent architecture

| | ECC | Superpowers | gstack |
|-|-----|-------------|--------|
| Count | 48 specialized | 1 + dynamic | 23 specialists |
| Status protocol | Free-form | DONE/CONCERNS/BLOCKED/NEEDS_CONTEXT | Artifact hand-off |
| Invocation | Task tool | SDD spawn | Slash command |
| Voice match | Domain (security, DB) | Function (implementer, reviewer) | **Role (CEO, QA)** |

→ 3 orthogonal taxonomies. gstack maps to startup org chart.

### Axis 4: TDD philosophy

| | ECC | Superpowers | gstack |
|-|-----|-------------|--------|
| Enforcement | Skill `tdd-workflow` (best practice) | Iron Law MANDATORY | Built into `/ship` |
| Bypass | ✅ "user said skip" | ❌ No way | ⚙️ `/ship` bootstraps test framework if missing |
| Anti-pattern detection | Implicit | **11 Rationalizations + 13 Red Flags tables** | `/review` catches |
| Coverage audit | Manual | Regression required | Every `/ship` run |

→ Superpowers strictest. gstack most pragmatic (automated test bootstrap). ECC most lenient.

### Axis 5: Cross-harness support

| Harness | ECC | Superpowers | gstack |
|---------|-----|-------------|--------|
| Claude Code | ✅ Primary | ✅ Primary | ✅ Primary |
| Codex CLI | ✅ | ✅ | ✅ |
| Codex App | ❌ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ✅ |
| OpenCode | ✅ | ✅ | ✅ |
| Copilot CLI | ❌ | ✅ | ❌ |
| Gemini CLI | ✅ | ✅ | ❌ |
| OpenClaw | ❌ | ❌ | ✅ Native |
| Factory Droid | ❌ | ❌ | ✅ |
| Slate | ❌ | ❌ | ✅ |
| Kiro | ❌ | ❌ | ✅ |
| Hermes | ❌ | ❌ | ✅ |
| GBrain (mod) | ❌ | ❌ | ✅ |
| **Total** | **5** | **7** | **10** |

→ gstack most portable. Superpowers broader consumer-focus (Copilot/Codex App). ECC core set.

### Axis 6: Browser automation

| | ECC | Superpowers | gstack |
|-|-----|-------------|--------|
| Core feature | Via MCP tools | Not core | **Built-in daemon** |
| Latency | 2-3s per command (cold) | N/A | **~100-200ms (warm)** |
| State persistence | Loses between commands | N/A | Cookies/tabs/localStorage persist |
| Security | MCP standard | N/A | Localhost + bearer + keychain 5 layers |
| Cross-agent share | ❌ | ❌ | ✅ `/pair-agent` |

→ **gstack unique.** Browser automation built-in, not plugin.

### Axis 7: Security posture

| | ECC | Superpowers | gstack |
|-|-----|-------------|--------|
| Primary mechanism | **AgentShield scanner (paid)** | Zero-dependency supply chain | Localhost-only HTTP + bearer token |
| Production bar | 11-item checklist | Zero-dep mandate | OWASP + STRIDE via `/cso` |
| Cookie handling | N/A | N/A | 5 layers (keychain, in-process decrypt, read-only DB, session cache, no-log) |
| Prompt injection defense | Skill | None explicit | **4-layer defense (v0.15.12.0)** |

→ Different emphasis: ECC = audit tool; Superpowers = supply chain; gstack = runtime security.

### Axis 8: Distribution model

| | ECC | Superpowers | gstack |
|-|-----|-------------|--------|
| Channel 1 | Plugin install | Claude marketplace | `git clone` + `./setup` |
| Channel 2 | Manual git | Git URL per harness | Auto-detect + per-host symlinks |
| Manifest | `plugin.json` | `.<harness>/plugin.json` per harness | `hosts/<name>.ts` TypeScript |
| Team mode | Plugin | Shared marketplace | **`./setup --team` silent hourly auto-update** |

→ gstack's team mode most elegant — silent, network-safe, zero vendoring.

### Axis 9: Update cadence

| | ECC | Superpowers | gstack |
|-|-----|-------------|--------|
| Frequency | Monthly-ish | 5/month (aggressive) | **5+/week (extremely aggressive)** |
| Breaking change discipline | Rare | v5.0.0 deliberate | Semver strict — bump on every breaking |
| Changelog style | Contributor-facing | Technical | **User-facing ("You can now...")** |

→ gstack ships 10x faster than ECC. Active maintenance signal.

### Axis 10: Contribution culture

| | ECC | Superpowers | gstack |
|-|-----|-------------|--------|
| Openness | Open, welcome PRs | 94% rejection rate | Voice + ETHOS hard-gates |
| Required PR evidence | Light | **Eval evidence mandatory** | User approval cho voice/ETHOS changes |
| AI agent warning | None | Extensive CLAUDE.md | Community PR guardrails (3 hard-gates) |

→ gstack + Superpowers both protect voice. ECC most open.

### Axis 11: Reflection / learning

| | ECC | Superpowers | gstack |
|-|-----|-------------|--------|
| Weekly retro | N/A | Manual iteration log | **`/retro` built-in** |
| Cross-project | N/A | Manual | **`/retro global`** (Claude/Codex/Gemini) |
| Session memory | Continuous-learning v2 skill | N/A | **`/learn` cross-session** |

→ gstack most reflection-built-in. ECC has continuous-learning. Superpowers manual.

### Axis 12: Tone + voice

| | ECC | Superpowers | gstack |
|-|-----|-------------|--------|
| Register | Prescriptive helpful | Legalistic Iron Law | **Founder direct** |
| Distinctive phrase | "production-ready" | "your human partner" | "Boil the Lake" |
| Protected | None | Terminology tuning | ETHOS + promo + voice (3 gates) |

→ All 3 have distinctive voice. gstack + Superpowers actively protect.

### Axis 13: Audience + persona fit

| | ECC | Superpowers | gstack |
|-|-----|-------------|--------|
| Primary | Dev teams polyglot | Methodology-focused dev | **Founder/CEO + first-timer + tech lead** |
| Secondary | Enterprise | Solo dev production-critical | Solo founder high-velocity |
| Not for | Kháng cự complexity | Kháng cự strict process | Kháng cự role-based framing |

### Axis 14: Cost (token + time)

| | ECC | Superpowers | gstack |
|-|-----|-------------|--------|
| Per-task token | Lower (compact skills) | Higher (anti-pattern tables) | Medium (persona prompts) |
| Time-to-correct | Fastest prototype | Fastest production | Fastest volume |
| Test infrastructure cost | Free (usually) | Free | **$4/run max explicit (eval tier)** |

→ gstack most explicit cost model. Prod discipline ECC < Superpowers < gstack.

### Axis 15: Maturity signals

| | ECC | Superpowers | gstack |
|-|-----|-------------|--------|
| Ship rate | Steady | Fast | Extreme |
| Community | 170+ contributors | Smaller, strict | Active, voice-protected |
| Commercial backing | Yes (paid products separate) | None (pure OSS) | YC recruiting funnel |
| Author daily-use | ✅ (Affaan) | ✅ (Jesse) | ✅✅ (Garry, 10K+ LOC/day) |

---

## Use case decision tree

```
Bắt đầu →
│
├─ Solo founder hoặc duo, ship volume cao?
│  └─ YES → gstack
│
├─ Team >10, polyglot, cần broad capability?
│  └─ YES → ECC
│
├─ Team 3-10, disciplined culture, production-critical?
│  └─ YES → Superpowers
│
├─ Cần browser automation real (QA, scraping, testing)?
│  └─ YES → gstack (only built-in daemon)
│
├─ Cần Iron Law TDD + force plan-before-code?
│  └─ YES → Superpowers
│
├─ Cần specialized domain agents (48 specific: security, DB, frontend)?
│  └─ YES → ECC
│
├─ Dùng harness ngoài Claude/Codex/Cursor (Slate, Kiro, Factory, Hermes)?
│  └─ YES → gstack (only support)
│
├─ Team kháng cự strict process?
│  ├─ → ECC (flexible)
│  └─ NOT → Superpowers hoặc gstack
│
├─ Đang là first-time Claude Code user?
│  └─ YES → gstack (structured roles, role-based mental model dễ grasp)
│
├─ Team value eval-driven > opinion?
│  └─ YES → Superpowers
│
├─ Hackathon/demo, need capabilities fast?
│  └─ YES → ECC
│
└─ Vẫn lưỡng lự? → **gstack default cho solo/duo, Superpowers cho 3-10 discipline-minded, ECC cho 10+ polyglot**
```

---

## Persona match

### Persona 1: "Anh solo founder technical"

- **Situation:** Technical founder vẫn muốn ship, team chưa có hoặc 1-2 người
- **Pain:** Ship hơn 1 dev worth of code mỗi ngày
- **Best fit:** **gstack** (primary) hoặc Superpowers (nếu prioritize discipline)
- **Why gstack:** Role-based mental model, parallel sprints, browser automation, 600K LOC/60 days design target

### Persona 2: "Tech lead Scrum coach"

- **Situation:** Lead team 3-8 engineers, responsible cho velocity + quality
- **Pain:** Consistency across team, quality drift
- **Best fit:** **Superpowers** (primary) hoặc gstack
- **Why Superpowers:** Hard gates enforce consistency, Iron Law TDD = less drift, eval-driven changes

### Persona 3: "Senior dev polyglot"

- **Situation:** Works across Python/Rust/TS/Go/DB migrations
- **Pain:** Context switching cost, cần specialized tooling mỗi domain
- **Best fit:** **ECC** (primary)
- **Why ECC:** 185 skills cover 12+ ecosystems, 48 domain agents

### Persona 4: "First-time Claude Code user"

- **Situation:** Software dev nhưng chưa dùng AI coding framework trước đó
- **Pain:** Blank prompt paralysis
- **Best fit:** **gstack** (structured roles)
- **Why:** README says explicitly "First-time Claude Code users — structured roles instead of blank prompt"

### Persona 5: "Enterprise security-focused team"

- **Situation:** Large org, compliance, security audits required
- **Pain:** Supply chain, prompt injection, credential leaks
- **Best fit:** **Superpowers** (zero-dep) hoặc ECC (AgentShield)
- **Why:** Different angles — Superpowers supply chain; ECC active scanning

### Persona 6: "YC startup / founder-led"

- **Situation:** Early-stage, ambition cao, CEO still codes
- **Pain:** Need force multiplier, team hire later
- **Best fit:** **gstack** (built for this persona explicitly)
- **Why:** ETHOS, YC references, Garry's voice — cultural match

### Persona 7: "Scrum coach muốn standardize team"

- **Situation:** 5-15 people, mixed seniority, need workflow standardization
- **Pain:** Inconsistent PRs, some skip TDD, some skip review
- **Best fit:** **Superpowers** (hard gates) hoặc gstack (smart routing)

---

## Mix & match strategies

### Strategy 1: Single framework (RECOMMENDED default)

Pick **1 framework** based on persona. Stick for 1-3 months. Evaluate before mixing.

→ Mix increases cognitive load. Most teams don't need.

### Strategy 2: gstack for velocity + Superpowers as mental model

- Install gstack cho actual slash commands
- Adopt Superpowers's 7-stage mental model không cài
- Dùng gstack's `/office-hours` → `/autoplan` → `/review` → `/qa` → `/ship`
- Mental reminder: "Am I skipping brainstorming? (Superpowers stage 1)" "Am I skipping TDD? (Superpowers stage 5)"

**Risk:** Mental model conflict. Team must grok both.

### Strategy 3: ECC breadth + gstack workflow

- Install ECC cho 185 skills capabilities
- Adopt gstack's Sprint Pipeline mental model
- When need specialized (DB migration, Rust refactor) → ECC domain agent
- When need role-based (CEO review, QA, release) → use ECC skill với gstack mindset

**Risk:** Skill name collision (both have TDD, review). Test which triggers.

### Strategy 4: Different projects, different framework

- Project A (founder-led, high velocity) → gstack
- Project B (enterprise, large team) → ECC
- Project C (production-critical, disciplined) → Superpowers

Each project CLAUDE.md configures its own framework.

→ **Recommended if:** multiple projects with distinctly different cultures.

### Strategy 5: Framework for phase

- **Planning phase:** Superpowers (hard gates for brainstorming + planning)
- **Execution phase:** gstack (velocity via role pipeline)
- **Maintenance phase:** ECC (broad skill library for specialized fixes)

→ **Advanced.** Only try after comfortable với all 3.

---

## Migration paths

### ECC → gstack

1. Audit ECC skills currently used → list them
2. Map to gstack roles (ECC TDD skill → `/ship` auto-bootstrap; ECC review agent → `/review`)
3. Install gstack via `./setup`
4. Pilot 1 project (week 1 per gstack guide Part 5)
5. Decide keep hybrid or full switch

### Superpowers → gstack

1. Audit Superpowers 7 stages mapping:
   - Brainstorming → `/office-hours`
   - Worktrees → standard git
   - Writing plans → `/autoplan`
   - SDD → `/autoplan` + implementation
   - TDD → `/ship` test bootstrap
   - Code review → `/review`
   - Finishing → `/land-and-deploy`
2. Install gstack
3. Note: lose Iron Law strictness, gain velocity + browser
4. Decide based on culture fit

### gstack → Superpowers

1. Ship 1-2 weeks với gstack, observe where drift happens
2. If drift = "skipping TDD" or "skipping design review" → Superpowers helps
3. Install Superpowers
4. Adopt 7-stage with hard gates
5. Note: lose browser daemon, lose `/retro` built-in; gain TDD Iron Law

### gstack → ECC

1. Identify gap: gstack missing capability?
2. Install ECC overlay
3. Keep gstack's Sprint Pipeline mental model
4. Use ECC skills cho specialized tasks

---

## FAQ

### Q1: "Chọn 1 thôi, default nào?"

**Storm Bear opinion:** gstack cho solo/duo, Superpowers cho 3-10 disciplined, ECC cho 10+ polyglot.

### Q2: "Ship volume cao nhất?"

gstack design target = 10-15 parallel sprints + 600K LOC/60 days. Superpowers design target = production discipline (slower but safer). ECC = capability toolbox.

### Q3: "Security nhất?"

Different axes:
- **Supply chain:** Superpowers (zero-dep)
- **Audit tool:** ECC (AgentShield)
- **Runtime security:** gstack (localhost + bearer + keychain)
- **Prompt injection:** gstack (4-layer defense v0.15.12.0)

### Q4: "Tốn thời gian học nhất?"

- ECC: week 2-3 roadmap (185 skills)
- Superpowers: week 1-2 roadmap (14 skills)
- gstack: week 1 roadmap (23 roles + simple mental model)

### Q5: "Rủi ro lock-in?"

All 3 đều "lock in" ở concept level nếu team adopt deep. gstack's voice protection tightest (voice = hard to migrate away). ECC most neutral.

### Q6: "Vietnamese dev team, framework nào?"

Không có framework có native VN support. Nhưng:
- gstack tone direct (Garry voice translate OK VN)
- Superpowers tone legalistic (harder VN translate)
- ECC tone professional (easy VN translate)

→ gstack + ECC tone friendly VN translation. Storm Bear vault showcases bilingual documentation pattern for all 3.

### Q7: "Team size lớn nhất recommend cho gstack?"

Per Garry's usage: solo. Per Conductor integration: 10-15 parallel sprints managed by 1 CEO-level person.

→ gstack **not designed for 50+ team.** Scale gstack = multi-CEO-pattern (unproven).

### Q8: "Tools nhanh + discipline = khả thi không?"

Trade-off real. Options:
- Superpowers sacrifice velocity cho discipline
- gstack sacrifice discipline cho velocity
- **Hybrid** (Strategy 2 or 3 above) = attempt both, cognitive cost high

### Q9: "Karpathy's LLM Wiki pattern (Storm Bear) relate cái nào?"

All 3 cite Karpathy! gstack most explicit (README opens với Karpathy quote). Storm Bear vault's Wiki pattern = knowledge management; 3 frameworks = workflow. Orthogonal but philosophically convergent ("compound knowledge/capability instead of re-derive").

### Q10: "Storm Bear vault default recommendation cho self?"

Storm Bear opinion (post-3-wiki-build):
- **gstack** cho Storm Bear's Scrum coaching projects (founder-heavy, team small)
- **Superpowers** cho production vault skills (discipline protects vault quality)
- **ECC** reference library khi cần specialized capability

→ Actual plan depends on Storm Bear's workflow preference (discipline vs velocity vs coverage).

---

## Storm Bear recommendation

### Tier 1: Strongly recommend evaluate

**If you haven't tried any:** Start gstack (fastest week-1 roadmap + structured roles).

**If you've tried 1-2:** Try the third để complete mental model of landscape.

### Tier 2: Storm Bear team default (hypothetical)

Based on Scrum coach persona + small team + production ambition:
- **Primary:** gstack (velocity + role structure)
- **Secondary:** Adopt Superpowers's mental model (Iron Law TDD as north star)
- **Ad-hoc:** Reference ECC's 185 skills catalog khi cần specialized

### Tier 3: When to pivot

Monitor 3 signals:
1. **Velocity dropping** → gstack may not fit; try lighter framework (or remove framework)
2. **Quality dropping** → add Superpowers discipline
3. **Specialized gap** → reference ECC skill library

### Final insights (từ 3-wiki synthesis)

1. **3 frameworks target different persona.** Pick based on persona, not "which is best."
2. **All 3 converge on core principles:**
   - Plan before code
   - Test before ship
   - Review before merge
   - Learn from sessions
3. **Divergent on enforcement:**
   - ECC: guidance
   - Superpowers: hard gates
   - gstack: smart routing + role prompting
4. **Cross-project value emerges when you know ≥2.** Storm Bear vault's 3-wiki now allows comparison nobody else can make.

---

## Closing thoughts — meta-lesson cho Storm Bear vault

Building 3 LLM Wiki projects in 48 hours (ECC → Superpowers → gstack) proved:

1. **Skill `llm-wiki-ingest` + routine `llm-wiki-routine` generalize.** 3 different framework types, same pattern works.
2. **Cross-project synthesis = unique vault value.** This 3-way comparison guide exists only because 3 wikis cùng vault, cùng tay, cùng format.
3. **Velocity compounds.** v1 ECC 5-7 hours, v2 Superpowers 3-4 hours, v3 gstack 2-3 hours. 50% velocity gain per wiki via pattern reuse.
4. **Routine pattern works.** First auto-execution của routine hoàn tất toàn 7 phases without human checkpoint intervention.

→ **Next action cho Storm Bear:**
1. Decide primary framework cho Scrum coaching work (recommendation: gstack)
2. Pilot 1 week với chosen framework
3. Report back in next iteration log
4. If 4th wiki: candidate topics = Conductor (gstack parallelization), OpenClaw (npm stars + cited), Anthropic official skills docs

---

> **Wiki maintained by Storm Bear vault.** 3-wiki cross-synthesis = unique value. Nếu thấy comparison sai hoặc outdated (all 3 frameworks update fast), ping để fix.
>
> **Cross-references:**
> - ECC wiki: `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) index.md`
> - Superpowers wiki: `../../Superpowers - Beginner Analysis/02 Wiki/(C) index.md`
> - gstack wiki: `../02 Wiki/(C) index.md`
> - Previous 2-way comparison: `../../Superpowers - Beginner Analysis/03 Published/(C) ECC vs Superpowers comparison.md`
> - Vault skill: `../../../05 Skills/llm-wiki-ingest.md`
> - Vault routine: `../../../05 Skills/llm-wiki-routine.md`
