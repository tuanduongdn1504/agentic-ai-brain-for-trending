# (C) agency-agents — Hướng dẫn cho người mới / Beginner's Guide

> **Repo:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) — 82.9K ⭐, 13.2K forks, MIT
> **Tagline:** *"A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers."*
> **Extended:** *"Assembling your dream team, except they're AI specialists who never sleep, never complain, and always deliver."*
> **Wiki:** `(C) index` — 18th LLM Wiki trong Storm Bear corpus
> **Audience:** VN developers + Scrum coaches + cross-functional teams (không chỉ software)

---

## Part 1 — agency-agents là gì? / What is agency-agents?

### 🇻🇳 Tiếng Việt

**agency-agents** là **thư viện 144+ agent personalities** chuyên biệt cho AI coding tools. Metaphor: **"AI agency"** — mỗi agent là 1 chuyên gia với personality + workflow + code examples + success metrics riêng, organized thành **12-14 divisions**:

- **Engineering** (27 agents)
- **Design** (8 — bao gồm Whimsy Injector + Brand Guardian)
- **Marketing** (26 — bao gồm Reddit Community Builder)
- **Sales** (9 — Discovery Coach + Deal Strategist)
- **Specialized** (41 — catch-all)
- **Game Development** (20+) — **first corpus**
- **Spatial Computing** (6) — AR/VR **first corpus**
- **Paid Media** (7) — **first corpus**
- + Product, Project Management, Testing, Support, Finance, Academic

**Origin:** *"born from a Reddit thread and months of iteration"* — viral launch với 50+ requests trong 12 giờ đầu.

**Author:** msitarzewski — **solo maintainer** nhưng project ở scale 82.9K stars (**3rd lớn nhất trong corpus**, gần bằng spec-kit 89K corporate).

### 🇬🇧 English

agency-agents is a **144+ AI agent personality library** organized across 12-14 divisions. "Agency" metaphor = coordinated collective of specialists, not interchangeable prompts. Reddit-originated, solo-maintained, yet reached **3rd largest scale in corpus** at 82.9K stars.

---

## Part 2 — Corpus firsts at v18

| Signal | agency-agents | Corpus context |
|--------|---------------|----------------|
| **Solo-at-enterprise-scale** | ✅ 82.9K solo | **First solo to near-corporate scale** (2.7× graphify v16 solo ceiling) |
| **144 agent library** | ✅ | **Largest in corpus** (codymaster 79, BMAD 12+) |
| **12-14 divisions** | ✅ | **Most-organized taxonomy** |
| **Game Development division** | ✅ 20+ | **First corpus** |
| **Spatial Computing division** | ✅ 6 | **First corpus** |
| **Paid Media division** | ✅ 7 | **First corpus** |
| **"Agency" metaphor** | ✅ | **First corpus use** |
| **Personality-driven design** | ✅ | **Novel T1 choice** |
| **Reality Checker 3-5 issues default** | ✅ | **First agent-level quantitative governance** |
| **Reddit-viral origin** | ✅ | **First community-viral scale path** |
| **CONTRIBUTING_zh-CN.md** | ✅ | **First CN contribution guide** |
| **5th wiki with OpenClaw** | ✅ | **Pattern #18 strengthened** |
| **No intellectual lineage cited** | ✅ | **Pattern #19 community-viral archetype** |

---

## Part 3 — Cài đặt / Installation

### 🇻🇳 Quick install (shell-based)

```bash
# Clone repo
git clone https://github.com/msitarzewski/agency-agents.git
cd agency-agents

# Generate integration files for all platforms
./scripts/convert.sh --parallel

# Interactive install (auto-detect installed AI tools)
./scripts/install.sh --interactive --parallel
```

### 🇬🇧 Targeted install

```bash
# Pick specific tool
./scripts/install.sh --tool claude-code
./scripts/install.sh --tool cursor
./scripts/install.sh --tool openclaw
./scripts/install.sh --tool copilot

# Install for ALL tools
./scripts/install.sh --no-interactive --tool all --parallel --jobs 4
```

### 11 supported platforms

1. **Claude Code** (native `.md`)
2. **GitHub Copilot**
3. **Antigravity** (Gemini research)
4. **Gemini CLI**
5. **OpenCode**
6. **OpenClaw** ← 5th wiki mentioning
7. **Cursor**
8. **Aider**
9. **Windsurf**
10. **Qwen Code** (Alibaba)
11. **Kimi Code** (Moonshot)

### System requirements

- Bash shell (Linux/macOS native; Windows needs WSL)
- Git
- One or more supported AI coding tool installed

---

## Part 4 — Cách dùng / Usage

### 🇻🇳 Invocation patterns

**Claude Code:**
```
"Use the Frontend Developer agent to review this component."
"Use the Whimsy Injector agent to add personality to this loading state."
"Use the Reality Checker agent to audit this PR."
```

**Antigravity (Gemini):**
```
@agency-frontend-developer review this React component
@agency-brand-guardian check brand consistency
```

**OpenCode:**
```
@backend-architect design this API.
@security-engineer audit this auth flow.
```

**Cursor:**
```
Use the @security-engineer rules to review this code.
```

### 🇬🇧 Example workflow — Build a feature with multiple agents

```
1. Product Manager agent:
   "Write user story for JWT authentication"
   → user story + acceptance criteria

2. Backend Architect agent:
   "Design auth architecture based on above user story"
   → architecture doc + sequence diagrams

3. Security Engineer agent:
   "Review the proposed auth architecture"
   → security review + recommendations

4. Backend Developer agent:
   "Implement JWT auth based on reviewed design"
   → code + tests

5. Reality Checker agent:
   "Review the JWT auth implementation"
   → 3-5 issues found (by default) + visual proof required

6. Brand Guardian agent:
   "Check error messages for brand consistency"
   → voice/tone review
```

**Multi-agent coordination** = chef's kiss for complex work.

---

## Part 5 — Signature agents

### 🇻🇳 Whimsy Injector (Design)

**Purpose:** Thêm playfulness có mục đích vào products.

**Discipline:** *"Every playful element must serve a functional or emotional purpose."*

**Use cases:**
- Loading skeletons có animation nhẹ nhàng
- Error messages helpful + charming
- Easter eggs reinforce brand
- Onboarding có warmth

### 🇬🇧 Reality Checker (Testing)

**Purpose:** Find problems others miss.

**Behavior:** *"Defaults to finding 3–5 issues and requires visual proof for everything."*

**Use cases:**
- PR reviews với rigor
- Pre-launch audits
- Post-mortem analysis

**Novel:** First corpus agent với quantitative quality governance (3-5 issues default).

### Reddit Community Builder (Marketing)

**Purpose:** Authentic community engagement.

**Philosophy:** *"You're becoming a valued community member who happens to represent a brand."*

**Anti-patterns:**
- Astroturfing
- Hard-selling
- Drive-by promotion

**Corpus significance:** First agent với anti-inauthentic-marketing ethic.

### Brand Guardian (Design)

Cross-agent role: Reviews outputs from other agents để đảm bảo brand consistency.

---

## Part 6 — 3 corpus-first divisions

### Game Development (20+ agents)

Game designer, level designer, narrative designer, character designer, combat systems designer, monetization designer, playtesting coordinator, và more.

**Significance:** First corpus framework với substantial game-dev focus.

### Spatial Computing (6 agents)

AR designer, VR developer, spatial UX, 3D modeling, etc.

**Significance:** Future-ready AR/VR coverage.

### Paid Media (7 agents)

Paid search strategist, paid social expert, ad copy specialist, creative performance, attribution analyst, etc.

**Significance:** First corpus paid-media specialization.

---

## Part 7 — vs other T1 frameworks

### 🇻🇳 So sánh

| Aspect | agency-agents | spec-kit v17 | BMAD v11 | codymaster v12 |
|--------|---------------|--------------|----------|----------------|
| **Stars** | 82.9K | 89.2K | 45K | 38 |
| **Author** | Solo | GitHub corp | LLC | VN solo |
| **Agent count** | 144 | — | 12+ | 79 |
| **Design** | **Personality-driven** | SDD methodology | BMM methodology | Skills-functional |
| **Install** | Shell | uv tool install | npm | npm |
| **Governance** | Light (5 files) | Heavy (6 files) | Medium | Medium |
| **VN accessible** | ❌ | ❌ | ✅ trans | ✅ authored |
| **Extensibility** | 11 platforms | 30+ + 80 extensions | Emerging marketplace | 79 skills in-tree |

### Choosing guide

- **Cross-functional work (including marketing, design, game-dev):** agency-agents
- **Software-only, methodology discipline, enterprise stability:** spec-kit
- **VN team onboarding:** BMAD (translated) hoặc codymaster (authored)
- **Quick start with fewer choices:** ECC v1 hoặc Superpowers v2

---

## Part 8 — Storm Bear relevance (VN operator)

### 🇻🇳 Đánh giá cho Scrum coach

**Relevance level:** 🟡 **Medium** — Reddit-origin + solo bus-factor giảm enterprise appeal, nhưng 144 agents + broad division coverage = versatile cho Scrum team experimentation.

**Signal points:**
- ✅ **11-platform coverage** — team members dùng different tools
- ✅ **Marketing + Sales divisions** — fits full-stack team (không chỉ engineering)
- ✅ **Personality-driven** — engaging cho team thay vì dry templates
- ✅ **Shell install** — DevOps-familiar
- ✅ **MIT permissive**
- ❌ **Solo maintainer** — bus-factor risk
- ❌ **No tagged releases** — không có stable API
- ❌ **EN-only docs** (CONTRIBUTING có zh-CN nhưng README không)
- ❌ **Heavy personality tone** — corporate clients may resist

### Scrum ceremony mapping (agents per ceremony)

| Ceremony | agency-agents agent |
|----------|---------------------|
| Backlog grooming | PM agent + Reality Checker |
| Sprint planning | Project Management agents + Engineering |
| Daily | — (use during task execution) |
| Sprint review | Reality Checker + stakeholder-agnostic Product |
| Retro | — |

**Limitation:** agency-agents không có Scrum-specific framework. Team phải map manually.

---

## Part 9 — 4-week learning roadmap

### Week 1: Install + explore

- Day 1-2: Clone repo + `./scripts/install.sh --tool claude-code`
- Day 3-4: Browse 12 divisions, read 5-10 agent personalities
- Day 5-7: Try 3 agents on small real tasks

### Week 2: Multi-agent workflow

- Day 8-10: Coordinate 3-5 agents for 1 feature development
- Day 11-12: Try Reality Checker on your code
- Day 13-14: Experiment với Whimsy Injector cho UX moments

### Week 3: Team pilot

- Day 15-17: Train 1 team member on 5-10 agents
- Day 18-19: Pilot on team project (1 sprint)
- Day 20-21: Gather feedback

### Week 4: Evaluate + scale

- Day 22-24: Compare với BMAD or spec-kit pilots
- Day 25-26: Document which agents fit Scrum context best
- Day 27-28: Decide keep / expand / replace

---

## Part 10 — Tradeoffs + limitations

### 🇻🇳 Strengths

- ✅ **144 agents** = broad coverage
- ✅ **12-14 divisions** = organized taxonomy
- ✅ **11-platform install** = flexibility
- ✅ **Personality-driven** = engaging
- ✅ **Reddit community validation** = battle-tested
- ✅ **Open source MIT**
- ✅ **Active solo maintainer** (currently)

### 🇬🇧 Limitations

- ❌ **Solo bus-factor** at 82.9K scale (highest risk in corpus)
- ❌ **No tagged releases** — API may break
- ❌ **Light governance** — quality variance across 144 agents
- ❌ **EN docs** — VN team barrier
- ❌ **Shell install** — Windows needs WSL
- ❌ **No cross-agent orchestration** documented
- ❌ **Heavy personality** may not fit all cultures
- ❌ **No academic lineage** — may resist formal-methodology teams

---

## Part 11 — References + next action

### Wiki pages

- [[(C) index]]
- [[(C) README + CONTRIBUTING + zh-CN cluster summary]]
- [[(C) SECURITY + Governance + Installation Scripts cluster summary]]
- [[(C) 12 Divisions + 144 Agents Taxonomy cluster summary]]
- [[(C) 144 Agent Personalities + 12 Divisions Taxonomy]]
- [[(C) 11-Platform Install + OpenClaw 5th Wiki Validation]]
- [[(C) Solo-at-Enterprise-Scale + Reddit Community Origin + Pattern 20 Revision]]
- [[(C) T1 8-way + Agent Persona Library + Pattern 19 No-Lineage + Storm Bear]]

### Cross-wiki siblings

- T1 peers (8-way): ECC, Superpowers, gstack, GSD, BMAD, codymaster, spec-kit
- OpenClaw peers: codymaster, paperclip, multica, graphify (5-wiki cluster)
- Solo-scale precedent: graphify v16

### Official

- Repo: https://github.com/msitarzewski/agency-agents
- No homepage

### 🎯 Suggested next action (Storm Bear)

Given v17-v18 both flagged **consolidation urgency** (27+ pattern candidates, 100+ action items, graphify-on-vault pending), the next action is NOT another wiki but:

1. **Run graphify on Storm Bear vault** (pending from v16) — highest leverage
2. **Pattern Library audit** — promote/retire 27 candidates with formal criteria
3. **Routine v2 refactor** — 100+ action items accumulated

After consolidation: T3 second entrant would close 5/5 tier validation. Alternative: agency-agents pilot for 1 Scrum team feature as experimental (Medium priority).

---

**Wiki 18/18 — T1 extended to N=8 + solo-at-enterprise-scale first + Pattern #20 MAJOR revision + Pattern #19 refined to 3 archetypes + Pattern #18 5th wiki confirmation + 4 new pattern candidates. Routine `llm-wiki-routine` v1 thứ 18 auto-execution.**
