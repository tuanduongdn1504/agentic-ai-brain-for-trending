# ECC vs Superpowers — Comparison Guide

> **Special deliverable:** Guide so sánh 2 framework để team Storm Bear quyết định **framework nào dùng cho project nào**. Đây là output unique của Storm Bear vault — không có ở đâu khác (vì 2 wiki được build cùng tay, cùng pattern).
>
> **Tác giả:** Storm Bear, dựa trên 2 project wiki:
> - `03 Projects/Everything Claude Code - Beginner Analysis/` (v1, 2026-04-17)
> - `03 Projects/Superpowers - Beginner Analysis/` (v1, 2026-04-18)
>
> **Ngày:** 2026-04-18 | **Phiên bản:** v1
> **Audience:** Tech lead, Scrum coach, dev team đang chọn AI coding framework
> **Song ngữ:** Tiếng Việt (chính) + English (technical terms)

---

## 📋 Mục lục

1. [TL;DR — Chọn cái nào trong 30 giây](#tldr--chọn-cái-nào-trong-30-giây)
2. [So sánh 1 trang (cheat sheet)](#so-sánh-1-trang-cheat-sheet)
3. [Bản chất khác biệt](#bản-chất-khác-biệt)
4. [Comparison theo 12 axis](#comparison-theo-12-axis)
5. [Use case decision tree](#use-case-decision-tree)
6. [Khi nào dùng cả 2](#khi-nào-dùng-cả-2)
7. [Migration paths](#migration-paths)
8. [FAQ chọn framework](#faq-chọn-framework)

---

## TL;DR — Chọn cái nào trong 30 giây

| Bạn muốn | Chọn |
|----------|------|
| **Discipline + methodology + ít skills nhưng deep** | **Superpowers** |
| **Toolbox đa năng + 185 skills + 48 agents broad coverage** | **ECC** |
| Force TDD + plan-before-code + subagent isolation | **Superpowers** |
| Performance optimization + cross-domain skills (Rust/Go/TS/Python/...) | **ECC** |
| Team < 5 người, ship deliberate PRs | **Superpowers** |
| Team > 10 người, multi-project polyglot | **ECC** |
| Hackathon/demo (need lots of pre-built capabilities fast) | **ECC** |
| Production codebase, long-term maintenance | **Superpowers** |
| Team kháng cự strict process | **ECC** (Superpowers sẽ frustrate) |
| Team value eval-driven evidence > opinion | **Superpowers** |

→ **Default recommendation:** Bắt đầu **Superpowers** nếu team < 5, **ECC** nếu team > 10. Lưỡng lự? Đọc tiếp.

---

## So sánh 1 trang (cheat sheet)

| Axis | ECC | Superpowers |
|------|-----|-------------|
| **Author** | Affaan Mustafa | Jesse Vincent (`obra`) |
| **Origin** | Anthropic Hackathon Winner | Personal project, public Oct 2025 |
| **Stars** | 140K+ | TBD verify (active growth) |
| **Repo size** | ~67KB README, broad | ~140KB total, narrow |
| **Approach** | Performance optimization system | Methodology + workflow framework |
| **Scope** | 185 skills + 48 agents + 79 commands | 14 skills + 1 agent + 0 commands (deprecated) |
| **Workflow** | Flexible — skills compose ad-hoc | 7-stage explicit, hard gates |
| **TDD style** | Skill `tdd-workflow` (best practice) | Iron Law: "NO PROD CODE WITHOUT FAILING TEST FIRST" |
| **Subagent** | 48 specialized (broad domain) | 1 reviewer + dynamic implementer/spec-reviewer |
| **Cross-harness** | Claude/Codex/Cursor/OpenCode/Gemini (5) | Claude/Codex/Cursor/OpenCode/Gemini/Copilot/Codex App (7) |
| **Security** | AgentShield + 11-item bar | Zero-dependency mandate (supply chain) |
| **Distribution** | Plugin + manual install | Claude marketplace + git URL per harness |
| **Tone** | Prescriptive best-practice | Iron Law, "your human partner", anti-pattern detection |
| **PR rejection** | Open contribution culture | 94% rejection rate (eval-driven discipline) |
| **Update cadence** | Steady (monthly-ish) | Aggressive (5 versions in March 2026) |
| **Dependencies** | Has paid products separately | Zero-dependency by design |
| **Maturity** | Established (10+ months daily use) | Active maintenance (~6 months) |
| **Best for** | Broad capability + flexibility | Discipline + production rigor |
| **Worst for** | Teams wanting strict process | Teams wanting flexibility |

---

## Bản chất khác biệt

### ECC = "Toolbox philosophy"

Affaan Mustafa build ECC như **Swiss Army knife** cho AI coding:
- Cần task X? Có skill cho X.
- Cần agent specialized cho domain Y? Có agent.
- 185 skills cover từ database migration đến React component generation đến security audit.

**Mental model:** "Tôi có vấn đề, tôi tìm skill phù hợp."

**Trade-off:**
- ✅ Fast iteration cho diverse tasks
- ✅ Onboarding dễ — pick & choose
- ❌ Easy để skip discipline (ad-hoc TDD, ad-hoc planning)
- ❌ 185 skills = overhead context loading + decision fatigue

### Superpowers = "Methodology philosophy"

Jesse Vincent build Superpowers như **operating discipline** cho AI coding:
- Mỗi feature đi qua 7 stages tuần tự.
- Hard gates ép designer + reviewer + tester roles.
- 14 skills mỗi cái deep tuned (eval-driven, regression tested).

**Mental model:** "Tôi có discipline, tôi áp lên mọi vấn đề."

**Trade-off:**
- ✅ Production-grade output mặc định
- ✅ Less drift, less rework
- ❌ Friction tuần đầu (hard gates feel restrictive)
- ❌ Không cover broad domain (need own skills cho specialized tasks)

### Tại sao 2 framework cùng giá trị

ECC và Superpowers **giải bài toán khác nhau**:
- ECC giải: "Làm sao agent có capabilities cho mọi task?"
- Superpowers giải: "Làm sao agent làm việc đúng cho task quan trọng?"

→ **Không phải competitor.** Có thể coexist (xem [Khi nào dùng cả 2](#khi-nào-dùng-cả-2)).

---

## Comparison theo 12 axis

### Axis 1: Workflow style

**ECC: Sequential phases (flexible)**
- Khái niệm phases (Planning → Implementation → Review) nhưng **soft** — agent có thể skip
- Skill `tdd-workflow` recommend tests, không enforce

**Superpowers: 7-stage hard-gated**
- Brainstorming → Worktrees → Plans → SDD → TDD → Review → Finishing
- HARD-GATE XML blocks ngăn skip stage 1 (brainstorming) và stage 5 (TDD)
- Skill auto-trigger qua description matching → enforce ngay cả khi user "quên"

→ **Pick:** Superpowers nếu team cần force discipline. ECC nếu team self-disciplined đã.

### Axis 2: Skills library size & depth

**ECC: 185 skills, broad-shallow**
- Cover 12+ language ecosystems
- Mỗi skill ~50-150 dòng trung bình
- Dễ overlap (multiple TDD-related skills)

**Superpowers: 14 skills, narrow-deep**
- Focus methodology, không cover specific languages
- Mỗi skill ~200-400 dòng (anti-pattern tables, hard gates, rationalizations)
- Không overlap (1 skill 1 purpose)

→ **Pick:** ECC nếu cần polyglot capability. Superpowers nếu cần fewer-but-better skills.

### Axis 3: Subagent architecture

**ECC: 48 specialized, pre-built**
- Mỗi agent có domain (security, performance, frontend, DB, ...)
- Spawn agent → run đến xong → return result
- Free-form output

**Superpowers: 1 reviewer + dynamic spawn**
- Chỉ 1 pre-built agent (`code-reviewer`)
- Implementer + spec-reviewer spawn dynamic per task
- **Structured status protocol:** DONE / DONE_WITH_CONCERNS / BLOCKED / NEEDS_CONTEXT
- Controller xử lý mỗi status khác nhau (re-dispatch, escalate, upgrade model)

→ **Pick:** ECC nếu cần specialized subagents domain-specific. Superpowers nếu value structured failure handling.

### Axis 4: TDD philosophy

**ECC: "Best practice" tone**
> "Use this skill when implementing any feature or bugfix. Enforces test-driven development with 80%+ coverage."

Prescriptive nhưng helpful. Agent có thể explain skip ("user said skip tests").

**Superpowers: "Iron Law"**
> "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST. Write code before the test? **Delete it. Start over.**"

11+ Common Rationalizations table teach agent recognize own excuses + STOP. 13 Red Flags để detect.

→ **Pick:** Superpowers nếu team có vấn đề agent rationalize skip TDD. ECC nếu team self-disciplined.

### Axis 5: Cross-harness support

**ECC: 5 harnesses**
- Claude Code, Codex, Cursor, OpenCode, Gemini
- Plugin model + manual install

**Superpowers: 7 harnesses**
- Above 5 + **Copilot CLI (v5.0.7)** + **Codex App**
- Per-harness manifest folder pattern (`.claude-plugin/`, `.codex/`, ...)
- Tool name mapping at runtime (TodoWrite → todowrite cho OpenCode)

→ **Pick:** Superpowers nếu team multi-harness (đặc biệt Copilot CLI). ECC nếu chỉ Claude Code.

### Axis 6: Security posture

**ECC: AgentShield + 11-item bar**
- Active security skill (AgentShield)
- 11-item production checklist
- Separate paid security products

**Superpowers: Zero-dependency mandate**
- Supply chain attack surface = 0
- "Reject all PRs adding dependencies"
- Custom WebSocket implementation thay Express/Chokidar

→ **Pick:** ECC nếu cần active security tooling. Superpowers nếu prioritize supply chain integrity.

### Axis 7: Distribution & install UX

**ECC:**
- Plugin marketplace: ✅
- Manual install: documented per harness
- Single source of truth: plugin.json

**Superpowers:**
- Claude marketplace: `/plugin install superpowers@superpowers-dev`
- Per-harness git URL install (Codex/Cursor/OpenCode/Copilot/Gemini)
- AGENTS.md → CLAUDE.md symlink convention
- Pin version qua git tag (`#v5.0.3`)

→ **Pick:** Superpowers nếu cần multi-harness install matrix. ECC nếu single-harness.

### Axis 8: Update cadence

**ECC: Steady**
- Monthly-ish releases
- Stable API, fewer breaking changes

**Superpowers: Aggressive**
- 5 versions trong March 2026
- v5.0.0 breaking change discipline (subagent-driven mandatory, slash commands deprecated)
- 6 months tuổi, 27+ releases

→ **Pick:** ECC nếu cần stability. Superpowers nếu OK với aggressive iteration + want latest patterns.

### Axis 9: Contribution culture

**ECC: Open**
- Welcome PRs, có contribution guide
- 170+ contributors

**Superpowers: Strict (94% rejection)**
- Public CLAUDE.md cảnh báo AI agents về consequences
- 5 mandatory PR checks
- 8 categories tự động reject
- "Skill changes require eval evidence" — modify skill cần regression test

→ **Pick:** ECC nếu team muốn contribute back. Superpowers nếu OK consume-only.

### Axis 10: Tone & terminology

**ECC: Prescriptive helpful**
- "Use this skill when..."
- "the user", "you" interchangeable
- Standard professional documentation tone

**Superpowers: Legalistic + identity-shaping**
- "Iron Law", "MANDATORY", ALL CAPS for non-negotiables
- "Your human partner" (deliberate, not interchangeable với "the user")
- HARD-GATE XML tags
- Anti-pattern tables for self-policing

→ **Pick:** Subjective. Superpowers tone strong → either resonate or alienate. Test với 1-2 dev trước khi rollout team.

### Axis 11: Cost (token + time)

**ECC: Lower per-task token, faster initial**
- Skills ngắn → less context loading
- Flexible workflow → can shortcut

**Superpowers: Higher per-task token, faster overall**
- Skills dài (anti-pattern tables) + 7-stage process → more context
- BUT: less rework, less drift → net faster cho production code
- v5.0.6 milestone: replaced subagent review loop với inline self-review = ~25 phút/run saved

→ **Pick:** ECC nếu cost-sensitive prototype. Superpowers nếu value time-to-correct-output.

### Axis 12: Maturity & community

**ECC:**
- 10+ months daily use bởi Affaan
- 140K stars, 170+ contributors
- Anthropic Hackathon Winner credibility

**Superpowers:**
- ~6 months public (Oct 2025 launch)
- Smaller community (TBD verify stars)
- Jesse Vincent OG dev tool credibility (private use longer than 6 months)
- Active community contributions (v5.0.x credits multiple contributors)

→ **Pick:** ECC nếu cần proven mass adoption. Superpowers nếu trust author judgment.

---

## Use case decision tree

```
Bắt đầu →
│
├─ Team có > 10 người + multi-project polyglot?
│  └─ YES → ECC (broad skill library)
│
├─ Team value Iron Law TDD + plan-before-code?
│  └─ YES → Superpowers
│
├─ Cần specialized agent cho domain (security, DB, frontend)?
│  └─ YES → ECC (48 specialized agents)
│
├─ Đang dùng Copilot CLI hoặc Codex App?
│  └─ YES → Superpowers (chỉ Superpowers support)
│
├─ Hackathon/demo, cần broad capability fast?
│  └─ YES → ECC
│
├─ Production codebase, long-term maintenance?
│  └─ YES → Superpowers (discipline payoff long-term)
│
├─ Team kháng cự strict process?
│  └─ YES → ECC (don't fight culture)
│
├─ Team value eval-driven > opinion?
│  └─ YES → Superpowers (eval-driven changes mandatory)
│
└─ Còn lưỡng lự? → Default **Superpowers** cho team < 5, **ECC** cho team > 10.
```

---

## Khi nào dùng cả 2

**Case 1: ECC làm broad capability + Superpowers làm methodology**

Cài ECC cho 185 skills capabilities, dùng Superpowers's 7-stage workflow như mental model. Khi conflict, follow Superpowers process, dùng ECC skills.

**Risk:** Skill name collision (cả 2 đều có TDD-related skill). Trigger sẽ chọn skill có description match closer. Cần test xem skill nào trigger.

**Case 2: Different projects, different framework**

- Project A (small, production-critical) → Superpowers
- Project B (large, polyglot) → ECC

Mỗi project có CLAUDE.md riêng → harness load đúng framework theo project.

**Case 3: Migration từ ECC → Superpowers**

Đang dùng ECC, muốn add discipline:
1. Keep ECC cài đặt
2. Cài Superpowers
3. Adopt 7-stage workflow như mental model
4. Khi quen, gradually replace ECC skills bằng Superpowers skills cho stages 1-7

→ Phase out ECC qua thời gian (3-6 tháng).

**Khuyến nghị Storm Bear:** Bắt đầu **chỉ 1 framework** trước. Mix tăng cognitive load. Sau khi đã thuần thục 1, mới consider mix.

---

## Migration paths

### Từ "no framework" → ECC

1. Đọc [[../../Everything Claude Code - Beginner Analysis/03 Published/(C) Everything Claude Code - Huong dan cho nguoi moi]]
2. Setup roadmap 4 tuần
3. Pick 5 skills core (TDD, code review, security, doc gen, refactoring)
4. Expand qua thời gian

### Từ "no framework" → Superpowers

1. Đọc [[(C) Superpowers - Huong dan cho nguoi moi]]
2. Setup roadmap 2 tuần
3. Force qua 7 stages cho 1 task pilot
4. Stress test Iron Law TDD
5. Ship 1 PR end-to-end

### Từ ECC → Superpowers

1. Audit hiện tại: bạn dùng ECC skills nào trong workflow? List ra.
2. Map sang Superpowers stages: skill ECC nào tương ứng stage Superpowers nào?
3. Disable ECC skills duplicate (TDD, code review)
4. Cài Superpowers
5. Run 7-stage workflow trên 1 pilot task
6. Sau 2 tuần: decide keep hybrid hay full switch

### Từ Superpowers → ECC

1. Identify gap: ECC có capability nào Superpowers không có mà bạn cần?
2. Cài ECC overlay
3. **Keep Superpowers's 7-stage workflow** như mental model — không bỏ discipline
4. Use ECC skills cho specific tasks (vd: ECC's database migration skill)

---

## FAQ chọn framework

### Q1: Nếu chỉ chọn 1, default nào?

**Storm Bear opinion (subjective):** Superpowers cho team < 5, ECC cho team > 10. Lý do: Superpowers's discipline payoff scale với product maturity, không phải team size; ECC's broad capability scale với team diversity.

### Q2: Tôi đã invest 3 tháng ECC, switch Superpowers có lãng phí?

Không. ECC kiến thức (skills concept, plugin model, harness understanding) chuyển sang Superpowers dễ. Cost: 1-2 tuần re-learn workflow.

### Q3: Superpowers's 94% PR rejection có scary cho contribute không?

Có, intentional. Đọc CLAUDE.md trước khi submit. Nếu PR bạn match 5 mandatory checks + có eval evidence, sẽ pass. Don't spray-and-pray.

### Q4: ECC và Superpowers có roadmap converge không?

Khả năng thấp. Khác philosophy bản chất. Có thể influence lẫn nhau (vd: ECC adopt structured status protocol từ Superpowers). Nhưng converge full thì không.

### Q5: Author của 2 framework có collaborate không?

TBD verify. Cả 2 active trong Anthropic ecosystem. Storm Bear chưa thấy public collaboration evidence.

### Q6: Framework nào tốt cho non-engineer (PM, designer)?

ECC nếu PM/designer cần broad capability (gen specs, gen mockups, etc.). Superpowers thiên engineer methodology — overkill cho PM/designer.

### Q7: Khi nào nên build framework riêng thay vì dùng 1 trong 2?

Khi cả 2 không match domain bạn (vd: legal tech, scientific computing với specialized workflows). Nhưng **đừng build trước khi try cả 2 ít nhất 1 tháng mỗi cái**. Build framework là expensive — most teams không cần.

### Q8: Storm Bear vault recommend cái nào cho self?

**Superpowers** cho project chính (Storm Bear's Scrum coaching tools — production-critical, small team). **ECC** như reference library khi cần specialized capabilities.

---

## Closing thoughts — chọn theo product maturity, không theo hype

ECC có **140K stars + Hackathon Winner badge** → easy default. Nhưng stars ≠ fit. Trước khi follow hype:

1. **Audit team culture** — flexibility lover hay discipline lover?
2. **Audit product stage** — prototype/demo hay production?
3. **Audit harness mix** — single-harness hay multi-harness?
4. **Audit team size** — small team value depth, large team value breadth

→ Trả lời 4 câu trên trước khi cài. Đừng cài cả 2 cùng lúc — overhead không đáng.

**Next action cho Storm Bear team:**
1. Đọc cả 2 beginner guide ([[../../Everything Claude Code - Beginner Analysis/03 Published/(C) Everything Claude Code - Huong dan cho nguoi moi]] + [[(C) Superpowers - Huong dan cho nguoi moi]])
2. Pick 1 pilot project
3. Run 1 framework cho 2 tuần
4. Retrospective: keep, switch, hoặc try khác

---

> **Wiki maintained by Storm Bear vault.** Đây là cross-project synthesis — value chỉ tồn tại vì 2 wiki cùng được build deliberate. Nếu thấy comparison thiếu sót, ping để fix.
>
> **Cross-references:**
> - Superpowers wiki: `02 Wiki/(C) index.md`
> - ECC wiki: `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) index.md`
> - Vault skill: `../../../05 Skills/llm-wiki-ingest.md` (proven pattern across 2 projects)
