# (C) spec-kit — Hướng dẫn cho người mới / Beginner's Guide

> **Repo:** [github/spec-kit](https://github.com/github/spec-kit) — 89.2K ⭐, 7.7K forks, MIT, v0.7.3
> **Tagline:** *"💫 Toolkit to help you get started with Spec-Driven Development"*
> **Anti-thesis:** *"focus on product scenarios and predictable outcomes instead of vibe coding every piece from scratch"*
> **Wiki:** `(C) index` — 17th LLM Wiki in Storm Bear corpus
> **Audience:** VN developers + Scrum coaches + enterprise teams wanting disciplined AI-assisted development

---

## Part 1 — spec-kit là gì? / What is spec-kit?

### 🇻🇳 Tiếng Việt

**spec-kit** là **toolkit chính thức của GitHub** (Microsoft-owned) cho **Spec-Driven Development (SDD)** — một phương pháp **đảo ngược** mối quan hệ truyền thống giữa spec và code.

**Triết lý cốt lõi:** *"Specifications don't serve code — code serves specifications."*

Thay vì:
- Viết spec → bỏ spec → code → hack và fix

Thì với SDD:
- Viết spec **chính xác** → AI agent generate code từ spec → code serve spec

**Key claim:** *"12 giờ documentation traditional → 15 phút với SDD commands"* (48× speedup).

**Đáng chú ý cho Storm Bear corpus:**
- **89.2K stars** — **lớn thứ 2 trong corpus** (chỉ sau build-your-own-x 491K outside-scope)
- **2× BMAD** (45K) — scale anchor mới cho T1 tier
- **First official-corporate-backed T1** framework
- **First explicit anti-"vibe coding" stance**

### 🇬🇧 English

**spec-kit** is GitHub's **official Spec-Driven Development toolkit**. SDD inverts traditional development: specs become executable primary artifacts, code becomes generated secondary output.

**Claim:** 48× productivity speedup (12 hours → 15 minutes documentation-to-implementation).

**Corpus significance:** 2nd largest project overall, largest T1, first official-corporate T1 backing.

---

## Part 2 — Corpus firsts at v17

| Signal | spec-kit | Corpus context |
|--------|----------|----------------|
| **Official GitHub-corporate backing** | ✅ | **First T1 corporate** |
| **89.2K stars (2× BMAD)** | ✅ | **Largest T1, 2nd overall** |
| **30+ agent integrations** | ✅ | **Broadest in corpus** |
| **80+ community extensions** | ✅ | **Largest marketplace** |
| **9-article constitution** | ✅ | **First T1 constitutional governance** |
| **Anti-vibe-coding formal stance** | ✅ | **First explicit** |
| **uv tool install** | ✅ | **First uv use in corpus** |
| **AI-disclosure policy** | ✅ | **First formal policy** |
| **John Lam cited** | ✅ | **First non-Karpathy intellectual lineage** |
| **SDD convergence with GSD v5** | ✅ | **Pattern #21 candidate** |

---

## Part 3 — Cài đặt / Installation

### 🇻🇳 Quick install

**Requirement:** uv (Astral's Python packaging tool, replaces pip).

```bash
# Install uv first if not present
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install spec-kit
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v0.7.3

# Verify
specify version
```

### 🇬🇧 Alternative: one-time usage

```bash
uvx --from git+https://github.com/github/spec-kit.git@v0.7.3 specify init my-project
```

### Initialize a project

```bash
cd my-project
specify init
```

This creates:
```
my-project/
├── .specify/
│   ├── templates/
│   └── specs/
└── memory/
    └── constitution.md    # ← your project principles
```

---

## Part 4 — 7-step workflow

### 🇻🇳 Quy trình SDD hoàn chỉnh

#### Step 1: Constitution — Nguyên tắc dự án

```
/speckit.constitution
```

AI hỏi về:
- Code quality standards (tests, linting)
- Testing standards (TDD? BDD? Unit + Integration?)
- UX consistency (design system?)
- Performance requirements (SLA?)

Output: `memory/constitution.md` với 9 articles tailored.

**9 articles mặc định (từ spec-driven.md):**
- **Article I:** Library-first (mỗi feature = standalone library)
- **Article III:** Test-first imperative (no code before tests)
- **Article VII:** Simplicity
- **Article VIII:** Anti-abstraction
- (II, IV, V, VI, IX: thêm articles khác)

#### Step 2: Specify — Tạo spec

```
/speckit.specify "Add JWT authentication with refresh tokens"
```

Tự động:
- Tạo git branch `001-jwt-auth`
- Generate `spec.md` với functional requirements

#### Step 3: Clarify (optional) — Resolve ambiguities

```
/speckit.clarify
```

AI hỏi các câu hỏi mơ hồ trong spec, user trả lời, spec update.

#### Step 4: Plan — Technical implementation plan

```
/speckit.plan
```

Generate `plan.md`:
- Architecture
- Dependencies
- Sequence diagrams
- Technical decisions

#### Step 5: Tasks — Break into actionable tasks

```
/speckit.tasks
```

Generate `tasks.md` với parallelization markers:
```
[P1] Install JWT libraries
[P1] Create User model
[P2] Implement /login endpoint
[P2] Implement /refresh endpoint
[P3] Add auth middleware
[P3] Write contract tests
```

#### Step 6: Analyze (optional) — Cross-artifact consistency

```
/speckit.analyze
```

Check: spec.md ↔ plan.md ↔ tasks.md consistent?

#### Step 7: Implement — AI agent executes

```
/speckit.implement
```

AI:
- Executes tasks sequentially (or in parallel)
- Writes tests first (Article III)
- Commits per task
- Reports progress

---

## Part 5 — Constitution deep-dive

### 🇻🇳 Hiểu về constitution

Constitution là **DNA của project** — governs tất cả spec generation.

**Enforcement mechanism (verbatim):**
> "These gates act as compile-time checks for architectural principles. The LLM cannot proceed without either passing the gates or documenting justified exceptions."

Nghĩa là:
- LLM **respect** articles architecturally, không chỉ advisorially
- Nếu article bị vi phạm, LLM phải document lý do
- Amendment process có thể cần explicit documentation + approval

### 🇬🇧 Parallel to paperclip v14

**paperclip v14** dùng 5 invariants + 4 governance primitives (T5 app).
**spec-kit v17** dùng 9 constitutional articles (T1 assistant).

Both = **constitutional governance architecture** — first T1 in corpus to adopt this approach.

---

## Part 6 — 30+ agent integrations

### 🇻🇳 Chọn agent nào?

spec-kit works với **30+ AI coding agents**. 14 named in README:

**Phổ biến nhất:**
- **Claude Code** (Anthropic — skill-based integration)
- **GitHub Copilot** (Microsoft — owner)
- **Cursor CLI** (Cursor)
- **Codex CLI** (OpenAI)
- **Gemini CLI** (Google)

**Community:**
- **opencode, Qoder, Kiro, Forge, Goose, Pi** — alternative agents

**Regional:**
- **Qwen CLI** (Alibaba — Chinese ecosystem)

**Full list:** https://github.github.io/spec-kit/reference/integrations.html

### 🇬🇧 Not in spec-kit list

**Interesting absences:**
- **OpenClaw** — in 4 other wikis (codymaster, paperclip, multica, graphify)
- **Hermes** — in 3 other wikis

**Why?** Pattern #18 v17 finding: corporate-official framework selects mainstream + popular community agents, skips emerging community standards.

---

## Part 7 — 80+ community extensions

### Install extension

```bash
specify extension search jira
specify extension add jira-sync
```

### 5 categories

| Category | Examples |
|----------|----------|
| **docs** | auto-readme, doc-sync |
| **code** | formatter, linter, refactor |
| **process** | pr-reviewer, release-automation |
| **integration** | jira-sync, slack-notifier |
| **visibility** | cost-tracker, metrics-dashboard |

### 2 effect tiers

- **Read-only** — safe (analysis, reports)
- **Read+Write** — modifies code / external systems (higher trust)

### Corporate hands-off disclaimer

> "GitHub and the Spec Kit maintainers... do **not review, audit, endorse, or support the extension code itself**."

**Practical:** Use extensions at your own risk. Review code before running Read+Write extensions.

---

## Part 8 — John Lam intellectual influence

### 🇻🇳 John Lam là ai?

Từ README:
> "This project is heavily influenced by and based on the work and research of John Lam."

**John Lam (jflam on GitHub):**
- Microsoft principal engineer (historical)
- IronRuby / IronPython work
- SDD research (details not in spec-kit docs)

**Ý nghĩa cho Storm Bear:**
- **Đa dạng hóa nguồn trí tuệ** — corpus trước có 3 Karpathy touchpoints; v17 mở thêm John Lam node
- **Action item:** Read John Lam's GitHub repos + writings

### 🇬🇧 Lineage diversification

Pattern #19 candidate at v16 hypothesized Karpathy disproportionate influence. v17 shows other intellectual nodes exist. Pattern refined.

---

## Part 9 — spec-kit vs other T1 frameworks

### Head-to-head

| Aspect | spec-kit | BMAD (v11) | codymaster (v12) |
|--------|----------|------------|------------------|
| **Stars** | 89.2K | 45K | 38 |
| **Backer** | GitHub official | LLC | Solo VN |
| **Methodology** | SDD + 9 articles | BMM + 5 modules | 5-Tier Memory |
| **VN translation** | — | ✅ | ✅ (authored) |
| **Corporate stability** | ✅ High | Medium (LLC) | Low (solo) |
| **Learning curve** | Heavy | Heavy | Medium |
| **Extension marketplace** | ✅ 80+ | Emerging | 79 embedded |
| **Scrum fit** | Medium (spec-by-feature) | High (modular) | Medium |

### Choosing guide

- **Enterprise + corporate stability:** spec-kit
- **VN team first-onboarding:** BMAD (has VN translation)
- **VN peer-category learning:** codymaster (authored by VN dev)
- **Quick adoption without methodology:** ECC / Superpowers

---

## Part 10 — Storm Bear relevance (VN operator)

### 🇻🇳 Đánh giá cho Scrum coach

**Relevance level:** 🟢 **High** — enterprise-ready, methodology-forward, corporate-stable.

**Signal points:**
- ✅ **GitHub corporate backing** — stability reduces bus-factor risk
- ✅ **SDD methodology maps to Scrum** — spec = PBI, plan = sprint plan, tasks = sprint backlog
- ✅ **Constitution = team working agreements** — Scrum coach concept fit
- ✅ **30+ agent integration** — team flexibility
- ✅ **Enterprise governance** — VN enterprises prefer formal
- ❌ **English-only docs** — barrier cho team không quen English
- ❌ **Python-heavy** — TS/JS teams may resist initially
- ❌ **Heavy methodology** — không phù hợp với quick-experiment teams

### Scrum ceremony mapping

| Scrum ceremony | spec-kit step |
|----------------|---------------|
| Product backlog grooming | `/speckit.specify` |
| Sprint planning | `/speckit.plan` + `/speckit.tasks` |
| Daily standup | `/speckit.implement` progress |
| Sprint review | `/speckit.analyze` |
| Retrospective | Amend constitution |

---

## Part 11 — 4-week learning roadmap

### Week 1: Foundation

- Day 1-2: Install uv + spec-kit, init personal project
- Day 3-4: Write your first constitution
- Day 5-7: Try `/speckit.specify` + `/speckit.plan` on small feature

### Week 2: Full workflow

- Day 8-10: Complete 7-step workflow on real project
- Day 11-12: Compare with traditional approach (measure time)
- Day 13-14: Try different agents (Claude + Codex + Copilot)

### Week 3: Extensions + team

- Day 15-17: Browse + try 3 community extensions
- Day 18-19: Pilot on team project
- Day 20-21: Document team learnings

### Week 4: Scrum integration

- Day 22-24: Map spec-kit to team's Scrum ceremonies
- Day 25-26: Train 1 Scrum team
- Day 27-28: Retrospective + feedback to Storm Bear vault

---

## Part 12 — Tradeoffs + limitations

### Strengths

- ✅ **GitHub corporate backing** (low abandon-risk)
- ✅ **89.2K community + 80+ extensions** (mature ecosystem)
- ✅ **Constitutional governance** (disciplined workflow)
- ✅ **30+ agent flexibility**
- ✅ **Formal SDD methodology** (not vibe-coding)
- ✅ **Open source MIT** (permissive)
- ✅ **Active development** (v0.7.3, 813 commits)

### Limitations

- ❌ **Heavy learning curve** (9 articles + 7 commands)
- ❌ **EN-only docs** (no VN, no CJK)
- ❌ **Python-specific** (JS/TS developers extra step)
- ❌ **Pre-1.0 API** (may break in 0.8.x)
- ❌ **GitHub corporate drift risk** (strategic priorities change)
- ❌ **Extension un-audited** (security risk for Read+Write)
- ❌ **uv requirement** (additional tool to install)

---

## Part 13 — References + next action

### Wiki pages

- [[(C) index]] — phase tracking
- [[(C) README + spec-driven cluster summary]]
- [[(C) AGENTS + CONTRIBUTING + SECURITY + SUPPORT + DEVELOPMENT + COC cluster summary]]
- [[(C) Integration + Extensions + Packaging cluster summary]]
- [[(C) Spec-Driven Development methodology + Constitution + 7-step Workflow]]
- [[(C) 30+ Platform Integration + 80+ Community Extensions Marketplace]]
- [[(C) GitHub-Official Corporate Backing + T1 Corporate-vs-Community Bifurcation]]
- [[(C) T1 7-way + SDD Convergence + Intellectual Lineage Diversification + Storm Bear]]

### Cross-wiki siblings

- T1 peers: ECC v1, Superpowers v2, gstack v3, GSD v5, BMAD v11, codymaster v12
- SDD convergence: GSD v5
- Constitutional parallel: paperclip v14
- Pattern #18 contrast: community-platform wikis (codymaster, paperclip, multica, graphify)

### Official

- Repo: https://github.com/github/spec-kit
- Homepage: https://github.github.io/spec-kit/
- Integrations: https://github.github.io/spec-kit/reference/integrations.html
- Extensions: https://speckit-community.github.io/extensions/
- John Lam: https://github.com/jflam

### 🎯 Suggested next action (Storm Bear)

**Pilot spec-kit on 1 Scrum team feature development** (Week 2 of 4-week roadmap).

**Parallel action:** Read John Lam's GitHub + blog. Storm Bear vault has heavy Karpathy foundation; John Lam = diversification.

**After spec-kit pilot:** compare with BMAD pilot, choose methodology for VN enterprise Scrum engagements.

---

**Wiki 17/17 — T1 extended to N=7 + first corporate T1 + Pattern #9 Resolution D generalized + Pattern #21 SDD convergence candidate + Pattern #19 intellectual lineage diversification. Routine `llm-wiki-routine` v1 thứ 17 auto-execution.**
